---
id: "SPEC-260827-1715-fix-historia-linaje"
title: "SPEC US-001.TASK-026: historia del linaje previo declarada como tal en el kit"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved"
origin: "BUG-021"
task: "US-001.TASK-026"
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

# SPEC-260827-1715-fix-historia-linaje — SPEC US-001.TASK-026: historia del linaje previo declarada como tal en el kit

| Field | Value |
|-------|-------|
| **Origin** | BUG-021 (REV-005) |
| **TASK** | US-001.TASK-026 |
| **ADRs** | ADR-001 (accepted) |
| **Risk Class** | low |
| **Revision** | 1 |

---

## 1. Objective

Reexpresar las 17 menciones de "v4.2" y las 4 de "versions up to 4.1 shipped one inside metaflow/" como historia del linaje previo (o sin numeros del linaje ajeno), coherentes con MetaFlow 1.1. Si no se corrige, el kit narra una historia falsa de la metodologia (MetaFlow nunca tuvo 4.x).

## 2. Context

El BUG-021 (aprobado en bloque BUG-021..024 desde REV-005, CP-REV-Approval
2026-08-27) documenta el patron residual. El fix vive en el diccionario del
transform (`mapping.json`) — el kit se regenera (nunca se edita a mano) —
salvo lo indicado como edicion directa (front door de la raiz / tools/).

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| TASK | US-001.TASK-026 | CP-TASK-READY-Approval ✓ (2026-08-27) |
| Feature US | US-001 | CP-US-Approval ✓ |
| BUG | BUG-021 | CP-BUG-Approval ✓ |
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

Nuevo test en src/tests (test_linaje.py o extension de test_restos_v5.py) que exige cero coincidencias de "v4.2" y de "versions up to 4.1" sin declaracion de linaje en el kit REAL. Ejecutar y registrar RED.

**Files created/modified:** segun fase (mapping.json / src/tests / tools/ / README.md).

### Phase B — Reglas del diccionario

**Duration:** 0.5h — **Complexity:** Low

#### B.1 Descripcion

Ampliar mapping.json con reglas que reescriben las frases: "removed in v4.2" → "removed in the previous lineage"; "dormant/reserved in v4.2" → "dormant/reserved"; "DORMANT / RESERVED (v4.2)" → "DORMANT / RESERVED"; "removed from the active flow in v4.2" → "removed from the active flow in the previous lineage"; "versions up to 4.1 shipped one inside `metaflow/`" → "the previous lineage shipped one inside `metaflow/`".

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
| BUG-021 (expected result) | Fases B/C corrigen el patron | test (RED→GREEN) + suite completa |

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

- BUG-021, REV-005, US-001, ADR-001.

---

## 18. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-27 | eugenioserrano | Rev 1 — SPEC inicial (US-001.TASK-026) |

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
