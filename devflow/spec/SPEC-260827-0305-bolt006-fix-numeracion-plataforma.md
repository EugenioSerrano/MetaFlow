---
id: "SPEC-260827-0305"
title: "BOLT-006 — Fix BUG-001: no numerar carpetas de plataforma (.github, .opencode)"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved"
origin: "BUG-001"
bolt: "US-001.BOLT-006"
revision: 1
associated_adrs:
  - "devflow/adrs/ADR-001-toolkit-transformacion.md"
  - "devflow/adrs/ADR-003-ajuste-numeracion-32-adv-reviews.md"
prerequisites:
  - "devflow/spec/SPEC-260827-0251-bolt005-correccion-numeracion.md"
risk_class: "low"
autonomy_level: "L3"
turn_budget: 10
data_classification: "internal"
review_ready_at: "2026-08-27T03:05:50-03:00"
review:
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-27T03:06:52-03:00"
  decided_at: "2026-08-27T03:06:52-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Aprobación del propietario (Dev-validator autoasignado) sin hallazgos — revisión de la SPEC de BOLT-006 en conversación, 2026-08-27. Autoriza el V-Bounce 6 (TDD estricto)"
---

# SPEC-260827-0305 — BOLT-006: Fix BUG-001 (plataforma sin numerar)

| Field | Value |
|-------|-------|
| **Origin** | BUG-001 |
| **Bolt** | US-001.BOLT-006 |
| **ADRs** | [ADR-001](../adrs/ADR-001-toolkit-transformacion.md) · [ADR-003](../adrs/ADR-003-ajuste-numeracion-32-adv-reviews.md) (accepted) |
| **Risk Class** | low |
| **Revision** | 1 |

---

## 1. Objective

Corregir el BUG-001 (aprobado): las reglas de ruta de numeración (`PN*`)
renombraron los componentes `agents` dentro de las carpetas ocultas de
plataforma — `.github/51-agents/` y `.opencode/51-agents/` — rompiendo el
reconocimiento de agentes (smoke test explotó). El fix excluye las reglas
`PN*` para los componentes bajo **carpetas ocultas** (el primer componente de
la ruta relativa empieza con `.`), conforme a la ADR-003. **Strict TDD en un
único V-Bounce:** test de reproducción (RED) → fix → GREEN + kit regenerado.

**Si no se implementa:** los agentes de plataforma no se reconocen en el kit
adoptado (BUG-001 sigue abierto).

## 2. Context

BUG-001 (approved, high): en `build_plan`, las path rules se aplican por
componente sin contexto — PN51 (`^agents$` → `51-agents`) coincide con el
componente `agents` de `.github/agents/` y `.opencode/agents/`. La
intención de la ADR-003 (la raíz de plataforma no se numera) no estaba
implementada en el motor. El resto del kit (las 20 carpetas de `metaflow/`)
sí debe seguir numerado.

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | `devflow/functional/bolts/US-001.BOLT-006-fix-numeracion-plataforma.md` | AITL-BOLT-READY-Approval ✓ |
| BUG | `devflow/bugs/BUG-001-numeracion-plataforma.md` | AITL-BUG-Approval ✓ |
| Feature US | `devflow/functional/user-stories/US-001-toolkit-transformacion.md` | AITL-US-Approval ✓ |
| ADRs | ADR-001, ADR-003 | AITL-ADR-Approval ✓ |
| Prior SPECs | BOLT-004 rev 1, BOLT-005 rev 1 (Done) | ✓ |
| Repository baseline | `58ac5eb` (+ trabajo previo sin commitear, G34) | — |

## 4. Scope

### In scope

- `src/transform.py` (`build_plan`): excluir reglas `PN*` para entradas cuya
  ruta relativa tiene el primer componente oculto (empieza con `.`).
- `src/tests/`: test de reproducción (RED) que exige `.github/agents/` y
  `.opencode/agents/` en el kit transformado + E2E real con plataforma
  intacta y `metaflow/` numerado.
- Regeneración del kit de producción.

### Out of scope

- Otros defectos; X6; migración de gobernanza; cambios de esquema.

## 5. Prerequisites and baseline

- BOLT-001..005 Done (suite 73/73). BUG-001 approved.
- Kit actual con `.github/51-agents/` y `.opencode/51-agents/` (a regenerar).

## 6. Phases

### Phase A — Fix del engine (build_plan)

**Duration:** 0.5h — **Complexity:** Low

#### A.1 Exclusión de PN* bajo carpetas ocultas

En `build_plan`, al calcular las rutas nuevas de cada entrada: si
`rel.parts[0]` empieza con `.` (carpetas ocultas de plataforma — `.agents/`,
`.github/`, `.opencode/`), se usan las path rules **excluyendo las de
numeración** (`id` con prefijo `PN`). El resto de las reglas de ruta
(P-M7/P-M8/P-B4/P-B9/P-M6/P-B2/P-B8/P-M15) se siguen aplicando (p. ej. los
wrappers `AvengaDevFlow.agent.md` → `MetaFlow.agent.md`). Las reglas de
contenido no cambian (las referencias a las carpetas numeradas de
`metaflow/` deben seguir numeradas dentro de los wrappers).

**Files modified:**
- `src/transform.py` — filtro de path rules por contexto (carpetas ocultas).

### Phase B — Tests (red → green)

**Duration:** 0.5h — **Complexity:** Low

#### B.1 Test de reproducción (RED) y regresión

- `test_numbering.py`: nuevo test que exige `.github/agents/` y
  `.opencode/agents/` en el kit real transformado (y que NO existan
  `.github/51-agents/` ni `.opencode/51-agents/`); se verifica además que
  `metaflow/51-agents/` sigue existiendo (no-regresión) y que los wrappers
  conservan su rename (`MetaFlow.agent.md`, `MetaFlow.md`).

---

## 7. Acceptance criteria

### AC (BUG-001): Plataforma sin numerar

**Given** el kit real transformado,
**When** se inspeccionan `.github/` y `.opencode/`,
**Then** existen `.github/agents/MetaFlow.agent.md` y
`.opencode/agents/MetaFlow.md` (sin números), NO existen
`.github/51-agents/` ni `.opencode/51-agents/`, y `metaflow/51-agents/`
sigue numerado.

### AC mapping to source (functional) / measurable outcome (non-functional)

| Source AC / outcome | How this SPEC satisfies it | Verifying test/evidence |
|---------------------|----------------------------|--------------------------|
| BUG-001 (expected) | Phase A: exclusión de PN* bajo carpetas ocultas | Test de reproducción + E2E real |
| ADR-003 (plataforma no numerada) | Phase A | E2E real |
| No-regresión (metaflow/ numerado) | Phase A (solo se filtra por contexto oculto) | E2E real (20 carpetas + ai-sdlc) |

---

## 8. Testing strategy

- **Reproducción (RED):** antes del fix, el test exige `.github/agents/` y
  falla (el kit actual tiene `51-agents`).
- **Regresión (GREEN):** suite completa 73 + nuevos, 0 failures.
- **E2E real:** plataforma intacta + `metaflow/` numerado + 0 tokens + 0
  links rotos + 0 sobre-match.
- **BUG evidence:** RED y GREEN por separado (obligatorio, §3.3.1).

---

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | Suite completa verde (73 + nuevos) | pass (objetivo) |
| Prose integrity | 0 sobre-match | pass (objetivo) |
| Link integrity | 0 links reales rotos | pass (objetivo) |
| SAST / SBOM | n/a | n/a |
| Prompt-injection scan | n/a | n/a |
| Secret-leak scan | pass | pass |
| Hallucination lint | pass | pass |
| IP / license provenance | n/a | n/a |
| PII / DLP | n/a | n/a |
| Dependency-confusion | n/a | n/a |
| Test-first evidence | RED antes del fix (BUG) | pass (objetivo) |
| Behavioral reproducibility | Determinista | pass (objetivo) |
| Bolt-manifest validation | Manifest válido | pass |

---

## 10. Security and data

- Sin cambios de superficie; `data_classification: internal`.

## 11. Monitoring and observability

- Reporte del run con reglas aplicadas; evidencia en `transform-reports/`.

## 12. Migration, compatibility and rollback

- **Migration:** N/A — kit regenerado.
- **Compatibility:** el filtro es contextual (solo carpetas ocultas); el
  resto de la numeración no cambia.
- **Rollback:** git + re-ejecución.

## 13. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| No-regresión de la numeración de metaflow/ | 1 | 4 | E2E exige las 20 carpetas + ai-sdlc |
| Filtro por prefijo `PN` demasiado amplio | 1 | 3 | Solo se filtra en contexto oculto; el resto del kit usa todas las reglas |
| Wrappers con renames perdidos | 1 | 3 | E2E verifica `MetaFlow.agent.md` / `MetaFlow.md` |

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| Filtrar por `rel.parts[0].startswith(".")` | Identifica exactamente las carpetas ocultas de plataforma (ADR-003) |
| Filtrar solo reglas `PN*` (no todas) | Los renames de marca de los wrappers (P-M8, etc.) deben seguir aplicándose |
| Las reglas de contenido no cambian | Las referencias a las carpetas numeradas de `metaflow/` dentro de los wrappers son correctas |

## 15. Stop conditions

- Si el test de reproducción no queda RED antes del fix: detener (no se
  toca código sin evidencia roja — §3.3.1).
- Si la no-regresión de `metaflow/` falla: detener e investigar.

## 16. Definition of Done (DoD)

- [ ] All phases implemented (A, B)
- [ ] BUG-001 corregido (plataforma sin números) — red + green registrados
- [ ] Tests GREEN (suite completa, 0 failures)
- [ ] Code follows ADR-001/ADR-003
- [ ] Applicable gates pass / waived (ADR) / n/a (reason)
- [ ] MEM created in `devflow/memory/` (exactly one per V-Bounce)
- [ ] Manifest `v_bounces[]` entry appended in
      `devflow/metrics/bolts/US-001.BOLT-006-fix-numeracion-plataforma.json`
- [ ] AITL-MEM-Approval recorded

## 17. References

- US-001 (AC-1, Rev 9), BOLT-006 (aprobado), BUG-001 (aprobado)
- ADR-001/ADR-003 (accepted)

## 18. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-27 | @eugenioserrano | Revision 1 — SPEC inicial de BOLT-006 |
| 2026-08-27 | @eugenioserrano | **AITL-SPEC-Approval** — `approved` por human:eugenioserrano (Dev-validator autoasignado), sin hallazgos |

## 19. AITL-SPEC-Approval

> **Avenga DevFlow §2.4.1, §3.0.** Esta SPEC permanece en draft hasta que el
> Dev-validator registra `AITL-SPEC-Approval` (bloque `review` del
> frontmatter). La aprobación autoriza el code-run / V-Bounce.

| Field | Value |
|-------|-------|
| **review.reviewers** | human:eugenioserrano (Dev-validator — rol autoasignado: no hay otro titular) |
| **review.decision** | **approved** |
| **review_ready_at** | `2026-08-27T03:05:50-03:00` |
| **review.started_at** | `2026-08-27T03:06:52-03:00` |
| **review.decided_at** | `2026-08-27T03:06:52-03:00` |
| **Findings** | Ninguno — aprobado sin comentarios |
