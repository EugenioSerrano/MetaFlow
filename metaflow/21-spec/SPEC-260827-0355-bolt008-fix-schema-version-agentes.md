---
id: "SPEC-260827-0355-bolt008-fix-schema-version-agentes"
title: "SPEC TASK-008: schema_version \"5.0\" en los 4 agent definitions"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved"
origin: "BUG-003"
task: "US-001.TASK-008"
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
  acknowledgment_reason: "Aprobacion del propietario (Dev-validator autoasignado) sin hallazgos - SPEC US-001.TASK-008 aprobada en bloque 2026-08-27; autoriza el V-Bounce con TDD estricto (red->green)"
---

# SPEC-260827-0355 — TASK-008: fix schema_version "5.0" en agent definitions

| Field | Value |
|-------|-------|
| **Origin** | BUG-003 (REV-003 F-03) |
| **TASK** | US-001.TASK-008 |
| **ADRs** | ADR-001 (accepted) |
| **Risk Class** | low |
| **Revision** | 1 |

---

## 1. Objective

Corregir las reglas/diccionario del transform para que los 4 agent
definitions del kit regenerado (`CLAUDE.md`, `.agents/skills/ai-sdlc/SKILL.md`,
`.github/agents/MetaFlow.agent.md`, `.opencode/agents/MetaFlow.md`)
declaren `schema_version` exactly `"1.0"` (familia v1) en su sección
"Manifest Family", en lugar de `"5.0"`. Si no se corrige, el agente
instalado en proyectos adoptantes crea manifests que fallan la validación
G23 contra los schemas v1 del kit.

## 2. Context

El BUG-003 (aprobado) documenta la instrucción `schema_version` exactly
`"5.0"` en los 4 wrappers (líneas 529/546/577/557), resto del input-kit
Avenga v5 que sobrevivió al rename de los wrappers (TASK-002). La familia
v1 está fijada por los schemas (`const: "1.0"`) y REV-002/TASK-003.

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| TASK | US-001.TASK-008 | CP-TASK-READY-Approval ✓ (2026-08-27) |
| Feature US | US-001 | CP-US-Approval ✓ |
| BUG | BUG-003 | CP-BUG-Approval ✓ |
| REV evidence | REV-003 | CP-REV-Approval ✓ |
| ADRs | ADR-001 | CP-ADR-Approval ✓ |
| Repository baseline | (git commit del trabajo) | — |

## 4. Scope

### In scope

- Reglas/diccionario que corrigen la sección Manifest Family de los 4
  wrappers (`"5.0"` → `"1.0"`).
- Test de reproducción (RED) + tests de reglas + E2E.
- Regeneración del kit.

### Out of scope

- El nombre "Manifest Family v5" de la sección (BUG-005 → TASK-010).
- Otros defectos.

## 5. Prerequisites and baseline

- TASK-005/TASK-006 Done; Python 3 + stdlib (ADR-001).

## 6. Phases

### Phase A — Reproduction test (RED)

**Duration:** 0.5h — **Complexity:** Low

#### A.1 Test de reproducción

Test del toolkit que verifica cero `schema_version` (exactly `"5.0"`) en
los 4 wrappers del kit regenerado. Ejecutar y registrar el **RED**.

**Files created:**
- `tools/tests/test_bolt008_agentes_schema_version.py`.

### Phase B — Fix del diccionario/reglas

**Duration:** 1h — **Complexity:** Low

#### B.1 Reglas de contenido

Ampliar `mapping.json` para reemplazar `schema_version` (exactly `"5.0"`)
por exactly `"1.0"` en la sección Manifest Family de los wrappers.

**Files modified:**
- `mapping.json` — reglas para agent definitions.

### Phase C — Regeneración y GREEN

**Duration:** 0.5h — **Complexity:** Low

#### C.1 Regenerar el kit

Ejecutar `python src/transform.py`, regenerar `distribution-kit/`, correr
la suite completa y registrar el **GREEN** + evidencia en
`transform-reports/`.

## 7. Acceptance criteria

### AC-1: Wrappers con schema_version "1.0"

**Given** un kit transformado, **When** se inspecciona la sección Manifest
Family de los 4 wrappers, **Then** declara `schema_version` exactly
`"1.0"` y no contiene `"5.0"`.

| Source AC / outcome | How this SPEC satisfies it | Verifying test/evidence |
|---------------------|----------------------------|--------------------------|
| BUG-003 (expected result) | Reglas corrigen la sección | test_bolt008 (RED→GREEN) + grep |

## 8. Testing strategy

- **Unit tests:** reglas del diccionario para wrappers.
- **Integration tests:** transform completo.
- **E2E tests:** grep de los 4 wrappers en el kit regenerado.
- **BUG evidence:** RED → GREEN registrados.

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

## 10. Security and data

- Sin superficie externa; `data_classification: internal`.

## 11. Monitoring and observability

- n/a — evidencia en `transform-reports/`.

## 12. Migration, compatibility and rollback

- **Migration:** regeneración del kit (idempotente).
- **Compatibility:** sin cambios de API.
- **Rollback:** git revert + regeneración.

## 13. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| Regresión de otros textos al ampliar el diccionario | 2 | 3 | E2E de tokens + suite |

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| Fix en el diccionario del transform | El kit es output regenerado |

## 15. Stop conditions

- Tokens no reproducibles con las reglas (bloqueo → MEM con evidencia).

## 16. Definition of Done (DoD)

- [ ] Fase A con RED registrado
- [ ] Fases B/C implementadas; 4 wrappers con `"1.0"`
- [ ] Tests GREEN; AC-1 satisfecha
- [ ] MEM + manifest `delivery_loops[]` + CP-MEM-Approval

## 17. References

- BUG-003, REV-003, ADR-001, US-001.

## 18. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-27 | eugenioserrano | Rev 1 — SPEC inicial (draft) |

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
