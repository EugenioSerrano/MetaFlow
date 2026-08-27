---
id: "SPEC-260827-1029-fix-template-report-anuncios"
title: "SPEC US-001.TASK-021: Anuncios de TEMPLATE-REPORT.html eliminados"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved"
origin: "BUG-016"
task: "US-001.TASK-021"
revision: 1
associated_adrs:
  - "metaflow/11-adrs/ADR-001-toolkit-transformacion.md"
prerequisites: []
risk_class: "low"
autonomy_level: "L3"
turn_budget: ""
data_classification: "internal"
review_ready_at: "2026-08-27T10:29:01-03:00"
review:
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-27T10:29:01-03:00"
  decided_at: "2026-08-27T10:29:01-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Aprobación del propietario (Dev-validator autoasignado) sin hallazgos — SPEC US-001.TASK-021 aprobada en bloque 2026-08-27; autoriza el V-Bounce con TDD estricto (red→green)"
---

# SPEC-260827-1029 — US-001.TASK-021: Anuncios de TEMPLATE-REPORT.html eliminados

| Field | Value |
|-------|-------|
| **Origin** | BUG-016 (REV-004) |
| **TASK** | US-001.TASK-021 |
| **ADRs** | ADR-001 (accepted) |
| **Risk Class** | low |
| **Revision** | 1 |

---

## 1. Objective

eliminar los anuncios del template ausente en MetaFlow.md §5.12 y README.md (Known Limitations) — decisión TASK-014. Si no se corrige, el kit sigue con narrativa corrupta/tautológica
o anuncios de archivos inexistentes que los tests de la ronda anterior no
cubrían (patrones del MetaFlow.md, no de los wrappers/charter).

## 2. Context

El BUG-016 (aprobado) documenta el patrón residual detectado en REV-004.
El fix vive en el diccionario del transform (`mapping.json`); el kit se
regenera (nunca se edita a mano).

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| TASK | US-001.TASK-021 | CP-TASK-READY-Approval ✓ (2026-08-27) |
| Feature US | US-001 | CP-US-Approval ✓ |
| BUG | BUG-016 | CP-BUG-Approval ✓ |
| REV evidence | REV-004 | CP-REV-Approval ✓ |
| ADRs | ADR-001 | CP-ADR-Approval ✓ |
| Repository baseline | (git commit del trabajo) | — |

---

## 4. Scope

### In scope

- Reglas/diccionario del transform que corrigen el patrón del BUG-016.
- Test de reproducción (RED) + tests de reglas + E2E.
- Regeneración del kit.

### Out of scope

- Otros defectos (TASKs dedicados TASK-018..024).

---

## 5. Prerequisites and baseline

- TASK-005/006/007 Done (baseline del diccionario y del texto §5.16);
  Python 3 + stdlib (ADR-001).

---

## 6. Phases

### Phase A — Reproduction test (RED)

**Duration:** 0.5h — **Complexity:** Low

#### A.1 Test de reproducción

Test del toolkit que verifica el patrón corregido sobre el kit regenerado.
Ejecutar y registrar el **RED**.

**Files created:**
- `tools/tests/test_fix-template-report-anuncios.py` (o ampliación de `test_restos_v5.py`).

### Phase B — Fix del diccionario/reglas

**Duration:** 1h — **Complexity:** Low

#### B.1 Reglas de contenido

Ampliar `mapping.json` con las reglas que corrigen el patrón del BUG-016.

**Files modified:**
- `mapping.json`.

### Phase C — Regeneración y GREEN

**Duration:** 0.5h — **Complexity:** Low

#### C.1 Regenerar el kit

Ejecutar `python src/transform.py`, regenerar `distribution-kit/`, correr
la suite completa y registrar el **GREEN** + evidencia en
`transform-reports/`.

---

## 7. Acceptance criteria

### AC-1: Patrón corregido en el kit regenerado

**Given** un kit transformado, **When** se inspecciona el patrón del
BUG-016, **Then** no aparece (expected result del BUG).

| Source AC / outcome | How this SPEC satisfies it | Verifying test/evidence |
|---------------------|----------------------------|--------------------------|
| BUG-016 (expected result) | Reglas del diccionario corrigen el patrón | test_fix-template-report-anuncios (RED→GREEN) + grep del kit regenerado |

---

## 8. Testing strategy

- **Unit tests:** reglas del diccionario (reemplazos exactos, whitespace flexible).
- **Integration tests:** transform completo sobre el input-kit.
- **E2E tests:** kit regenerado sin el patrón (grep) + suite completa.
- **BUG evidence:** RED (kit actual con el patrón) → GREEN (kit regenerado sin el patrón).

---

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | suite verde | pass (a verificar) |
| SAST / SBOM | — | n/a (stdlib) |
| Perf-smoke | — | n/a |
| Prompt-injection scan | — | n/a |
| Secret-leak scan | sin secretos | pass (a verificar) |
| Hallucination lint | sin APIs inventadas | pass (a verificar) |
| IP / license provenance | — | n/a |
| PII / DLP | — | n/a |
| Dependency-confusion | — | n/a |
| Test-first evidence | RED antes del fix | pass (a verificar) |
| Behavioral reproducibility | kit reproducible | pass (a verificar) |
| TASK-manifest validation | manifest v5 válido | pass (a verificar) |

---

## 10. Security and data

- Sin superficie externa; `data_classification: internal`.

---

## 11. Monitoring and observability

- n/a — evidencia en `transform-reports/`.

---

## 12. Migration, compatibility and rollback

- **Migration:** regeneración (idempotente).
- **Compatibility:** sin cambios de API.
- **Rollback:** git revert + regeneración.

---

## 13. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| Regresión de otros textos al ampliar el diccionario | 2 | 3 | E2E de tokens + suite completa |

---

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| Fix en el diccionario del transform | El kit es output regenerado |

---

## 15. Stop conditions

- El patrón no es reproducible con las reglas (bloqueo → MEM con evidencia).

---

## 16. Definition of Done (DoD)

- [ ] Fase A con RED registrado
- [ ] Fases B/C implementadas; kit regenerado sin el patrón
- [ ] Tests GREEN; AC-1 satisfecha
- [ ] MEM + manifest `delivery_loops[]` + CP-MEM-Approval

---

## 17. References

- BUG-016, REV-004, ADR-001, US-001.

---

## 18. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-27 | eugenioserrano | Rev 1 — SPEC inicial (aprobada en bloque) |

---

## 19. CP-SPEC-Approval

> **MetaFlow §2.4.1, §3.0.** Esta SPEC permanece en draft hasta que
> el Dev-validator registra `CP-SPEC-Approval`.

| Field | Value |
|-------|-------|
| **review.reviewers** | human:eugenioserrano (Dev-validator autoasignado) |
| **review.decision** | **approved** |
| **review_ready_at** | `2026-08-27T10:29:01-03:00` |
| **review.started_at** | `2026-08-27T10:29:01-03:00` |
| **review.decided_at** | `2026-08-27T10:29:01-03:00` |
| **Findings** | Ninguno — aprobado sin comentarios |
