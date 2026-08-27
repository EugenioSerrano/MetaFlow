---
id: "SPEC-260827-0355-bolt016-fix-mem-campos-manifest"
title: "SPEC US-001.TASK-016: TEMPLATE-MEM describe delivery_loops[] con 6 campos; el schema exige 8"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved"
origin: "BUG-011"
task: "US-001.TASK-016"
revision: 1
associated_adrs:
  - "metaflow/11-adrs/ADR-001-toolkit-transformacion.md"
prerequisites: []
risk_class: "low"
autonomy_level: "L3"
turn_budget: ""
data_classification: "internal"
review_ready_at: "2026-08-27T03:55:34-03:00"
review:
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-27T03:58:00-03:00"
  decided_at: "2026-08-27T03:58:00-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Aprobacion del propietario (Dev-validator autoasignado) sin hallazgos - SPEC US-001.TASK-016 aprobada en bloque 2026-08-27; autoriza el V-Bounce con TDD estricto (red->green)"
---

# SPEC-260827-0355 — US-001.TASK-016: TEMPLATE-MEM describe delivery_loops[] con 6 campos; el schema exige 8

| Field | Value |
|-------|-------|
| **Origin** | BUG-011 (REV-003) |
| **TASK** | US-001.TASK-016 |
| **ADRs** | ADR-001 (accepted) |
| **Risk Class** | low |
| **Revision** | 1 |

---

## 1. Objective

Corregir las reglas/diccionario del transform para que TEMPLATE-MEM.md liste los 8 campos requeridos de delivery_loops[] (number, spec_revision, git_commit, execution_outcome, code_generation, mem, review_ready_at, review_started_at), consistente con 23-metrics/README.md, GUARDRAILS.md y el schema manifest-v1-task.schema.json. Si no se corrige, un agente que siga el template omite 2 campos requeridos y produce un manifest invalido (G23).

## 2. Context

El BUG-011 (aprobado) documenta la lista incompleta (6 campos) heredada del input-kit v5 que el diccionario no actualizo en el template del MEM.

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| TASK | US-001.TASK-016 | CP-TASK-READY-Approval ✓ (2026-08-27) |
| Feature US | US-001 | CP-US-Approval ✓ |
| BUG | BUG-011 | CP-BUG-Approval ✓ |
| REV evidence | REV-003 | CP-REV-Approval ✓ |
| ADRs | ADR-001 | CP-ADR-Approval ✓ |
| Repository baseline | (git commit del trabajo) | — |

---

## 4. Scope

### In scope

- Reglas/diccionario de contenido para TEMPLATE-MEM; test de reproduccion; E2E; regeneracion.

### Out of scope

- El contenido del resto del template.

---

## 5. Prerequisites and baseline

- TASK-005/TASK-006 Done (baseline del diccionario y regeneracion estable).
- Python 3 + stdlib (ADR-001); `src/transform.py` funcional.

---

## 6. Phases

### Phase A — Reproduction test (RED)

**Duration:** 0.5h — **Complexity:** Low

#### A.1 Test de reproduccion

Test del toolkit que verifica el patron del BUG (BUG-011) sobre el kit
regenerado. Ejecutar y registrar el **RED**.

**Files created:**
- `tools/tests/test_bolt016-fix-mem-campos-manifest.py`.

### Phase B — Fix del diccionario/reglas

**Duration:** 1h — **Complexity:** Low

#### B.1 Reglas de contenido

Ampliar `mapping.json` (y el diccionario del transform) para corregir el
patron del BUG en el output.

**Files modified:**
- `mapping.json`.

### Phase C — Regeneracion y GREEN

**Duration:** 0.5h — **Complexity:** Low

#### C.1 Regenerar el kit

Ejecutar `python src/transform.py`, regenerar `distribution-kit/`, correr
la suite completa y registrar el **GREEN** + evidencia en
`transform-reports/`.

---

## 7. Acceptance criteria

### AC-1: TEMPLATE-MEM con los 8 campos

**Given** un kit transformado
**When** se inspecciona TEMPLATE-MEM.md
**Then** la lista de delivery_loops[] tiene los 8 campos requeridos

| Source AC / outcome | How this SPEC satisfies it | Verifying test/evidence |
|---------------------|----------------------------|--------------------------|
| BUG-011 (expected result) | Reglas del diccionario corrigen el patron | test_bolt016-fix-mem-campos-manifest (RED→GREEN) + grep del kit regenerado |

---

## 8. Testing strategy

- **Unit tests:** reglas del diccionario (reemplazos exactos).
- **Integration tests:** transform completo sobre el input-kit.
- **E2E tests:** kit regenerado sin el patron del BUG (grep).
- **Edge cases:** variantes de espaciado/comillas/contexto del patron.
- **BUG evidence:** RED (kit actual con el patron) → GREEN (kit
  regenerado sin el patron).

---

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | suite verde | pass (a verificar) |
| SAST / SBOM | — | n/a (sin dependencias nuevas; Python stdlib) |
| Perf-smoke (p95/p99) | — | n/a (sin superficie de servicio) |
| Prompt-injection scan | — | n/a (sin prompts de entrada) |
| Secret-leak scan | sin secretos | pass (a verificar) |
| Hallucination lint | sin APIs inventadas | pass (a verificar) |
| IP / license provenance | — | n/a (sin codigo de terceros nuevo) |
| PII / DLP | — | n/a (sin PII) |
| Dependency-confusion | — | n/a (stdlib) |
| Test-first evidence | RED registrado antes del fix | pass (a verificar) |
| Behavioral reproducibility | kit reproducible | pass (a verificar) |
| TASK-manifest validation | manifest v5 valido | pass (a verificar) |

---

## 10. Security and data

- Sin superficie externa; el toolkit procesa documentos del repo
  (`data_classification: internal`).
- Sin secretos, sin PII.

---

## 11. Monitoring and observability

- n/a — herramienta de transformacion local; la evidencia se registra en
  `transform-reports/`.

---

## 12. Migration, compatibility and rollback

- **Migration:** regeneracion del kit (idempotente).
- **Compatibility:** sin cambios de API.
- **Rollback:** git revert del cambio de reglas + regeneracion previa.

---

## 13. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| Regresion de otros textos al ampliar el diccionario | 2 | 3 | E2E completa de tokens + suite |

---

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| Fix en el diccionario del transform, no edicion manual del kit | El kit es output regenerado; la edicion manual se pierde en la proxima corrida |

---

## 15. Stop conditions

- El patron del BUG no es reproducible con las reglas (bloqueo → MEM con
  evidencia).
- Aparece una fuente gobernada draft/inconsistente (G15).

---

## 16. Definition of Done (DoD)

- [ ] Fase A con RED registrado
- [ ] Fases B/C implementadas; kit regenerado sin el patron del BUG
- [ ] Tests GREEN; AC-1 satisfecha
- [ ] MEM + manifest `delivery_loops[]` + CP-MEM-Approval

---

## 17. References

- BUG-011, REV-003, ADR-001, US-001.

---

## 18. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-27 | eugenioserrano | Rev 1 — SPEC inicial (draft) |

---

## 19. CP-SPEC-Approval

> **MetaFlow §2.4.1, §3.0.** Esta SPEC permanece en draft hasta que
> el Dev-validator registra `CP-SPEC-Approval`.

| Field | Value |
|-------|-------|
| **review.reviewers** | human:eugenioserrano (Dev-validator autoasignado) |
| **review.decision** | **approved** |
| **review_ready_at** | `2026-08-27T03:55:34-03:00` |
| **review.started_at** | `2026-08-27T03:58:00-03:00` |
| **review.decided_at** | `2026-08-27T03:58:00-03:00` |
| **Findings** | Ninguno — aprobado sin comentarios |
