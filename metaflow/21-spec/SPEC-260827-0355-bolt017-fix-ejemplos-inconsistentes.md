---
id: "SPEC-260827-0355-bolt017-fix-ejemplos-inconsistentes"
title: "SPEC US-001.TASK-017: Ejemplos inconsistentes: espanol en §3.12 y write_paths del repo de distribucion"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved"
origin: "BUG-012"
task: "US-001.TASK-017"
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
  acknowledgment_reason: "Aprobacion del propietario (Dev-validator autoasignado) sin hallazgos - SPEC US-001.TASK-017 aprobada en bloque 2026-08-27; autoriza el V-Bounce con TDD estricto (red->green)"
---

# SPEC-260827-0355 — US-001.TASK-017: Ejemplos inconsistentes: espanol en §3.12 y write_paths del repo de distribucion

| Field | Value |
|-------|-------|
| **Origin** | BUG-012 (REV-003) |
| **TASK** | US-001.TASK-017 |
| **ADRs** | ADR-001 (accepted) |
| **Risk Class** | low |
| **Revision** | 1 |

---

## 1. Objective

Corregir las reglas/diccionario del transform para que los dos ejemplos inconsistentes del kit queden normalizados: el comment del ejemplo inline de §3.12 en el MetaFlow.md pasa al content_language del kit (en, OQ-001) y el comentario de write_paths del ejemplo de agent (51-agents/examples/developer/agent.yaml) deja de referirse a carpetas del repo de distribucion (distribution-kit/, tools/). Si no se corrige, los ejemplos violan la politica de idioma y confunden al adoptante.

## 2. Context

El BUG-012 (aprobado) documenta el comment en espanol "Agregar manejo explicito de concurrencia." (MetaFlow.md:3156) y "the product tree (distribution-kit/, tools/)" (developer/agent.yaml:19), heredados del input-kit y del repo de desarrollo.

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| TASK | US-001.TASK-017 | CP-TASK-READY-Approval ✓ (2026-08-27) |
| Feature US | US-001 | CP-US-Approval ✓ |
| BUG | BUG-012 | CP-BUG-Approval ✓ |
| REV evidence | REV-003 | CP-REV-Approval ✓ |
| ADRs | ADR-001 | CP-ADR-Approval ✓ |
| Repository baseline | (git commit del trabajo) | — |

---

## 4. Scope

### In scope

- Reglas/diccionario de contenido para los dos ejemplos; test de reproduccion; E2E; regeneracion.

### Out of scope

- El resto de los ejemplos del kit.

---

## 5. Prerequisites and baseline

- TASK-005/TASK-006 Done (baseline del diccionario y regeneracion estable).
- Python 3 + stdlib (ADR-001); `src/transform.py` funcional.

---

## 6. Phases

### Phase A — Reproduction test (RED)

**Duration:** 0.5h — **Complexity:** Low

#### A.1 Test de reproduccion

Test del toolkit que verifica el patron del BUG (BUG-012) sobre el kit
regenerado. Ejecutar y registrar el **RED**.

**Files created:**
- `tools/tests/test_bolt017-fix-ejemplos-inconsistentes.py`.

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

### AC-1: Ejemplos consistentes (idioma y paths)

**Given** un kit transformado
**When** se inspeccionan el ejemplo de §3.12 y el ejemplo de agent
**Then** estan en en y no referencian distribution-kit//tools/

| Source AC / outcome | How this SPEC satisfies it | Verifying test/evidence |
|---------------------|----------------------------|--------------------------|
| BUG-012 (expected result) | Reglas del diccionario corrigen el patron | test_bolt017-fix-ejemplos-inconsistentes (RED→GREEN) + grep del kit regenerado |

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

- BUG-012, REV-003, ADR-001, US-001.

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
