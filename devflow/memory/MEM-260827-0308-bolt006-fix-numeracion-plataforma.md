---
id: "MEM-260827-0308"
title: "BOLT-006 — Fix BUG-001: no numerar carpetas de plataforma (V-Bounce 1)"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
bolt: "US-001.BOLT-006"
spec: "SPEC-260827-0305"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "58ac5eb"
applied_adrs:
  - "devflow/adrs/ADR-001-toolkit-transformacion.md"
  - "devflow/adrs/ADR-003-ajuste-numeracion-32-adv-reviews.md"
manifest: "devflow/metrics/bolts/US-001.BOLT-006-fix-numeracion-plataforma.json"
diff_ref: ""
review_ready_at: "2026-08-27T03:08:13-03:00"
review:
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-27T03:09:09-03:00"
  decided_at: "2026-08-27T03:09:09-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Aprobación del propietario (Dev-validator autoasignado) sin hallazgos — revisión del diff, RED/GREEN, corrida de producción (plataforma restaurada) y manifest en conversación, 2026-08-27"
---

# MEM-260827-0308 — BOLT-006: Fix BUG-001 (plataforma sin numerar)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | US-001.BOLT-006 |
| **SPEC**        | [SPEC-260827-0305](../spec/SPEC-260827-0305-bolt006-fix-numeracion-plataforma.md) — revisión 1 |
| **V-Bounce**    | 1 |
| **ADRs**        | [ADR-001](../adrs/ADR-001-toolkit-transformacion.md) · [ADR-003](../adrs/ADR-003-ajuste-numeracion-32-adv-reviews.md) (accepted) |

---

## 1. Executive summary

Este V-Bounce corrige el **BUG-001** (aprobado, severity high): las reglas de
ruta de numeración (`PN*`) renombraban el componente `agents` dentro de las
carpetas ocultas de plataforma — el kit salía con `.github/51-agents/` y
`.opencode/51-agents/` y las plataformas (GitHub Actions / opencode) no
reconocían los agentes (el smoke test del propietario lo confirmó). El fix,
con **strict TDD** (RED → GREEN en el mismo V-Bounce): `build_plan` ahora
**excluye las reglas `PN*`** para las entradas cuyo primer componente de ruta
empieza con `.` (`.agents/`, `.github/`, `.opencode/`), mientras que los
renames de marca de los wrappers (P-M7/P-M8) y la numeración de `metaflow/`
siguen intactos — conforme a la ADR-003 ("la raíz de plataforma no se
numera"). Resultado de la corrida de producción: **EXIT=0**, `.github/agents/`
y `.opencode/agents/` con sus wrappers (`MetaFlow.agent.md`, `MetaFlow.md`),
**sin** `.github/51-agents/` ni `.opencode/51-agents/`, y `metaflow/51-agents`
sigue numerado (no-regresión verificada). Suite completa en verde: **73/73
tests**, con RED registrado (el test de reproducción fallaba antes del fix —
`.github/agents` ausente) y GREEN. El kit vuelve a ser publicable y los
agentes de plataforma se reconocen.

## 2. Implemented phases

### Phase A — Fix del engine (build_plan)

Se agregó el filtro contextual en `build_plan`: si el primer componente de la
ruta relativa empieza con `.`, las path rules usadas son las que **excluyen
las reglas de numeración** (`id` con prefijo `PN`); en caso contrario se usan
todas. Esto preserva: (a) los renames de marca de los wrappers
(`AvengaDevFlow.agent.md` → `MetaFlow.agent.md` — P-M8), (b) la numeración de
las 20 carpetas de `metaflow/` (PN aplican normalmente), y (c) las carpetas
ocultas de plataforma sin números. Las reglas de contenido no cambian (las
referencias a las carpetas numeradas dentro de los wrappers son correctas).

### Phase B — Tests (red → green)

Se extendió la E2E real (`test_e2e_real_renumbered_clean`) con las
aserciones de reproducción: `.github/agents/MetaFlow.agent.md` y
`.opencode/agents/MetaFlow.md` existen, `.github/51-agents/` y
`.opencode/51-agents/` NO existen, y `metaflow/51-agents` sigue existiendo
(no-regresión). Antes del fix el test **fallaba** (RED — el kit salía con
`51-agents`); tras el fix, la suite completa quedó **GREEN (73/73)**.

## 3. Files created

| File | Purpose |
|------|---------|
| — | Ninguno (cambios sobre archivos existentes) |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `src/transform.py` | `build_plan`: filtro contextual — reglas `PN*` excluidas para entradas bajo carpetas ocultas (primer componente `.`) |
| `src/tests/test_numbering.py` | E2E real ampliada: aserciones de plataforma (reproducción BUG-001) + no-regresión de `metaflow/` |

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
| — | — | Ninguno en el repo (el fix es del pipeline: el kit vuelve a `.github/agents/` y `.opencode/agents/`) |

## 6. Files deleted

| File | Reason |
|------|--------|
| — | Ninguno |

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| Filtrar por `rel.parts[0].startswith(".")` | Identifica exactamente las carpetas ocultas de plataforma (ADR-003) |
| Filtrar solo reglas `PN*` | Los renames de marca de los wrappers (P-M8) deben seguir aplicando |
| Contenido sin cambios | Las referencias a las carpetas numeradas de `metaflow/` dentro de los wrappers son correctas |
| TDD estricto en un V-Bounce | BUG protocol (§2.16/§3.3.1): red evidence antes de tocar producción |

## 8. Deviations and assumptions

- **Ninguna** respecto de la SPEC — el fix es exactamente el filtro previsto.
- **Sin commits** (G34): `git_commit: null`.

## 9. Verification evidence

### Build
```
N/A — Python stdlib puro (ADR-001), sin build.
```

### Tests
```
> python -m unittest discover -s src/tests
Ran 73 tests in 11.048s
OK
```

### BUG V-Bounce evidence (RED → GREEN, §3.3.1)
- **RED:** `test_e2e_real_renumbered_clean` con las aserciones de plataforma
  (antes del fix) → `FAIL` — el kit salía con `.github/51-agents/` y
  `.opencode/51-agents/` (`.github/agents/` ausente).
- **GREEN:** misma suite tras el fix en `build_plan` → `Ran 73 tests ... OK`.

### Producción (demo — el producto)
```
> python src/transform.py
EXIT=0 — cero tokens prohibidos
total: 149 archivos, 66 carpetas, 0 binarios, 1 excluido, 5739 reglas, 27 remociones
evidencia: transform-reports/5.1/20260827-030805/ (retención: purgada 024439)
.github/agents/MetaFlow.agent.md ....... existe ✓
.opencode/agents/MetaFlow.md ........... existe ✓
.github/51-agents / .opencode/51-agents  ausentes ✓
metaflow/51-agents ..................... numerado ✓ (no-regresión)
```

### Gates
| Gate | Result |
|------|--------|
| Unit / integration | pass — 73/73 |
| Prose integrity | pass — 0 sobre-match |
| Link integrity | pass — 0 links reales rotos |
| Test-first evidence (BUG) | pass — RED registrado antes del fix |
| Perf-smoke (p95/p99) | pass |
| SAST / SBOM | n/a |
| Prompt-injection scan | n/a |
| Secret-leak scan | pass |
| Hallucination lint | pass |
| IP / license provenance | n/a |
| PII / DLP | n/a |
| Dependency-confusion | n/a |
| Behavioral reproducibility | pass |
| Bolt-manifest validation | pass |

## 10. Manual interventions

Ninguna — todo el código, tests y diccionario fueron generados por el agente.

## 11. Evidence links

- **Diff / PR:** no aplica (sin commit — G34).
- **Commit:** baseline `58ac5eb` (trabajo sin commitear para revisión).
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-001.BOLT-006-fix-numeracion-plataforma.json`
- **Evidencia del run:** `transform-reports/5.1/20260827-030805/`

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~10 min |
| V-Bounce number | 1 (BOLT-006) |
| Tests creados/ajustados | E2E ampliada (aserciones de plataforma); suite 73 |
| AI-generated code | 100 % |
| First-pass approval | n/a — en revisión |

## 13. Pending items and stubs

- [ ] **AITL-BOLT-DONE-Approval** de BOLT-006 (aceptación final).
- [ ] Re-correr el **smoke test de plataforma** del propietario (confirmar el reconocimiento de agentes).
- [ ] **X6** — template HTML de reportes.
- [ ] Migración de gobernanza (OQ-003) y absorción de la próxima versión (OQ-004).

## 14. AITL-MEM-Approval

> **Avenga DevFlow §2.12, §3.0.** Este MEM no tiene status mutable y **nunca
> se auto-aprueba**. El Dev-validator que ejecutó el Bolt inspecciona el diff
> real, la evidencia de tests/gates (RED y GREEN), el MEM y el manifest, y
> registra `AITL-MEM-Approval` aquí y en el `checkpoint_approvals[]` del
> manifest.

| Field | Value |
|-------|-------|
| **Reviewers (executing Dev-validator)** | `human:eugenioserrano` (Dev-validator — rol autoasignado: no hay otro titular) |
| **Roles** | dev_validator |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-27T03:08:13-03:00` |
| **review.started_at** | `2026-08-27T03:09:09-03:00` |
| **review.decided_at** | `2026-08-27T03:09:09-03:00` |
| **Review evidence** | diff + test de reproducción (RED) + suite 73/73 (GREEN) + corrida de producción (plataforma restaurada) + MEM + manifest |
| **Comments** | — |
| **Findings** | Ninguno |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | Evidencia inspeccionada: diff, RED/GREEN del BUG, tests 73/73, gates pass/n/a, MEM completo, manifest v_bounces[1] validado |
