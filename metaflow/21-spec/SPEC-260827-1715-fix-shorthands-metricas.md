---
id: "SPEC-260827-1715-fix-shorthands-metricas"
title: "SPEC US-001.TASK-027: shorthands de checkpoints canonicos en tablas de metricas"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved"
origin: "BUG-022"
task: "US-001.TASK-027"
revision: 1
associated_adrs:
  - "metaflow/11-adrs/ADR-001-toolkit-transformacion.md"
prerequisites: []
risk_class: "low"
autonomy_level: "L3"
turn_budget: ""
data_classification: "internal"
review_ready_at: "2026-08-27T17:04:54-03:00"
review:
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-27T17:18:20-03:00"
  decided_at: "2026-08-27T17:18:20-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: ""
---

# SPEC-260827-1715-fix-shorthands-metricas — SPEC US-001.TASK-027: shorthands de checkpoints canonicos en tablas de metricas

| Field | Value |
|-------|-------|
| **Origin** | BUG-022 (REV-005) |
| **TASK** | US-001.TASK-027 |
| **ADRs** | ADR-001 (accepted) |
| **Risk Class** | low |
| **Revision** | 1 |

---

## 1. Objective

Reescribir las 3 celdas de metricas con los checkpoints canonicos `CP-TASK-DONE-Approval`/`CP-TASK-READY-Approval` (con backticks), eliminando "TASK TASK-DONE". Si no se corrige, las tablas usan identificadores que no existen en el vocabulario del kit.

## 2. Context

El BUG-022 (aprobado en bloque BUG-021..024 desde REV-005, CP-REV-Approval
2026-08-27) documenta el patron residual. El fix vive en el diccionario del
transform (`mapping.json`) — el kit se regenera (nunca se edita a mano) —
salvo lo indicado como edicion directa (front door de la raiz / tools/).

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| TASK | US-001.TASK-027 | CP-TASK-READY-Approval ✓ (2026-08-27) |
| Feature US | US-001 | CP-US-Approval ✓ |
| BUG | BUG-022 | CP-BUG-Approval ✓ |
| REV evidence | REV-005 | CP-REV-Approval ✓ |
| ADRs | ADR-001 | CP-ADR-Approval ✓ |
| Repository baseline | (git commit del trabajo) | — |

---

## 4. Scope

### In scope

- Reglas/diccionario del transform (o re-expresion directa cuando se indica).
- Test de reproduccion (RED) + suite completa.
- Regeneracion del kit cuando corresponde.

### Out of scope

- Otros defectos (TASKs dedicados TASK-026..029).
- agent-wrappers code (.py) para TASK-029.

---

## 5. Prerequisites and baseline

- TASK-024/025 Done (baseline); Python 3 + stdlib (ADR-001); tests en unittest.

---

## 6. Phases

### Phase A — Test de reproduccion (RED)

**Duration:** 0.5h — **Complexity:** Low

#### A.1 Descripcion

Extension de src/tests (test_linaje.py o test_restos_v5.py): exige los checkpoints canonicos y ausencia de "TASK TASK-DONE" en las 3 celdas del kit REAL. Ejecutar y registrar RED.

**Files created/modified:** segun fase (mapping.json / src/tests / tools/ / README.md).

### Phase B — Reglas del diccionario

**Duration:** 0.5h — **Complexity:** Low

#### B.1 Descripcion

Reglas exactas para las 3 celdas: 1) "| TASK lead time | TASK-DONE `decided_at` − TASK-READY `decided_at` (§3.7) |" → "| TASK lead time | `CP-TASK-DONE-Approval` `decided_at` − `CP-TASK-READY-Approval` `decided_at` (§3.7) |"; 2) "| US lead time | last child TASK TASK-DONE `decided_at` − US `CP-US-Approval` `decided_at` |" → "| US lead time | last child TASK’s `CP-TASK-DONE-Approval` `decided_at` − US `CP-US-Approval` `decided_at` |"; 3) "| TASK lead time | TASK-DONE − TASK-READY `decided_at` |" → "| TASK lead time | `CP-TASK-DONE-Approval` − `CP-TASK-READY-Approval` `decided_at` |".

**Files created/modified:** segun fase (mapping.json / src/tests / tools/ / README.md).

### Phase C — Regeneracion y GREEN

**Duration:** 0.5h — **Complexity:** Low

#### C.1 Descripcion

python src/transform.py; suite completa verde; evidencia en transform-reports/.

**Files created/modified:** segun fase (mapping.json / src/tests / tools/ / README.md).


---

## 7. Acceptance criteria

### AC-1: Patron corregido

**Given** el output (kit regenerado / front door / tools/), **When** se
inspecciona el patron del BUG, **Then** no aparece (expected result del BUG).

| Source AC / outcome | How this SPEC satisfies it | Verifying test/evidence |
|---------------------|----------------------------|--------------------------|
| BUG-022 (expected result) | Fases B/C corrigen el patron | test (RED→GREEN) + suite completa |

---

## 8. Testing strategy

- **Unit tests:** test de reproduccion del patron sobre el output REAL.
- **Integration tests:** transform completo sobre el input-kit.
- **E2E tests:** suite completa.
- **BUG evidence:** RED (output actual con el patron) → GREEN (output corregido).

---

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | suite verde | pass (a verificar) |
| SAST / SBOM | — | n/a |
| Perf-smoke | — | n/a |
| Prompt-injection scan | — | n/a |
| Secret-leak scan | sin secretos | pass (a verificar) |
| Hallucination lint | sin APIs inventadas | pass (a verificar) |
| IP / license provenance | — | n/a |
| PII / DLP | — | n/a |
| Dependency-confusion | — | n/a |
| Test-first evidence | RED antes del fix | pass (a verificar) |
| Behavioral reproducibility | output verificable por test | pass (a verificar) |
| TASK-manifest validation | manifest v1 valido | pass (a verificar) |

---

## 10. Security and data

- Sin superficie externa; `data_classification: internal`.

---

## 11. Monitoring and observability

- n/a — evidencia en transform-reports/ (cuando se regenera) + tests.

---

## 12. Migration, compatibility and rollback

- **Migration:** regeneracion (idempotente) / edicion directa acotada.
- **Compatibility:** sin cambios de API.
- **Rollback:** git revert + regeneracion.

---

## 13. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| Regresion de otros textos al ampliar el diccionario | 2 | 3 | E2E de tokens + suite completa |

---

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| Fix en el diccionario del transform | El kit es output regenerado |
| Edicion directa solo donde se indica (front door / tools/) | Esos archivos viven fuera del kit |

---

## 15. Stop conditions

- El patron no es reproducible con las reglas (bloqueo → MEM con evidencia).
- Cambio material de fuentes gobernadas (G15): detener, revisar, re-aprobar.

---

## 16. Definition of Done (DoD)

- [ ] Fase A con RED registrado
- [ ] Fases B/C implementadas; patron corregido
- [ ] Tests GREEN; AC-1 satisfecha
- [ ] MEM + manifest `delivery_loops[]` + CP-MEM-Approval

---

## 17. References

- BUG-022, REV-005, US-001, ADR-001.

---

## 18. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-27 | eugenioserrano | Rev 1 — SPEC inicial (US-001.TASK-027) |

---

## 19. CP-SPEC-Approval

> **MetaFlow §2.4.1, §3.0.** Esta SPEC permanece en draft hasta que
> el Dev-validator registra `CP-SPEC-Approval`.

| Field | Value |
|-------|-------|
| **review.reviewers** | human:eugenioserrano (Dev-validator autoasignado) |
| **review.decision** | **approved** |
| **review_ready_at** | `2026-08-27T17:04:54-03:00` |
| **review.started_at** | `2026-08-27T17:18:20-03:00` |
| **review.decided_at** | `2026-08-27T17:18:20-03:00` |
| **Findings** | Ninguno — aprobado sin comentarios |
