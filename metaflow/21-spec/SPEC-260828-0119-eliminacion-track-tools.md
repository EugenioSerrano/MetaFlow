---
id: "SPEC-260828-0119"
title: "Eliminación del track heredado tools/ (legado AvengaDevFlow)"
date: "2026-08-28"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved" # draft | approved | blocked | obsolete
origin: "US-000.TASK-002"
task: "US-000.TASK-002"
revision: 1 # material revision of this canonical SPEC (matches manifest spec_revisions[])
associated_adrs:
  - "metaflow/11-adrs/ADR-001-toolkit-transformacion.md"
prerequisites: []
risk_class: "low" # low | medium | high | critical (mirrors the TASK's risk_class)
autonomy_level: "L3" # L1 | L2 | L3 | L4 — defaults by risk: low/medium→L3, high→L2, critical→L1; L4 requires an ADR (§3.3)
turn_budget: "" # OPTIONAL — leave empty to use the platform/agent default (§3.3)
data_classification: "internal" # public | internal | confidential | restricted
review_ready_at: "2026-08-28T01:19:22-03:00"
review: # CP-SPEC-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-28T01:21:30-03:00"
  decided_at: "2026-08-28T01:22:27-03:00"
  findings: []
  acknowledged_without_comment: true # must be true when findings is empty (§3.0)
  acknowledgment_reason: "Aprobación del propietario (Dev-validator autoasignado: no hay otro titular) sin hallazgos — revisión de la SPEC en conversación, 2026-08-28"
---

# SPEC-260828-0119 — Eliminación del track heredado `tools/`

| Field | Value |
|-------|-------|
| **Origin** | US-000.TASK-002 |
| **TASK** | US-000.TASK-002 |
| **ADRs** | [ADR-001](file:///D:/MetaFlow/metaflow/11-adrs/ADR-001-toolkit-transformacion.md) (Alternative E — `src/` sobre `tools/`) |
| **Risk Class** | low |
| **Revision** | 1 |

---

## 1. Objective

Eliminar la carpeta `tools/` heredada del linaje AvengaDevFlow
(especificaciones del tooling Go original: clock, identity, indexer,
manifest, next-id, reporter, scaffold, status, validator; BUILD.md,
README.md; y la herramienta Python `agent-wrappers/`) que el proyecto no va
a usar, y actualizar los tests y la documentación viva que la referencian —
decisión del propietario 2026-08-28, precedida por una revisión completa de
referencias.

Si NO se implementa: el repo conserva peso muerto heredado que la suite de
tests y la documentación viva siguen referenciando (manteniéndolo "vivo"), la
raíz del workshop sigue mezclando el legado del linaje con el toolkit real
(`src/`), y el pendiente del scope X4 ("cuando se decida el futuro de la
pista") queda sin resolver.

---

## 2. Context

`tools/` proviene del repositorio original de AvengaDevFlow (track de
tooling Go). El ADR-001 (aprobado 2026-08-27, Alternative E) ya decidió no
escribir código nuevo ahí — `src/` es la ubicación del toolkit — y la visión
(AG4) excluye reimplementar la pista; el scope (X4) dejó su futuro como
pendiente ("Cuando se decida el futuro de la pista | OQ-004"). El proyecto
nunca usó `tools/` en el pipeline: la transformación lee `input-kit/` →
`distribution-kit/` y ninguno de los dos tiene folder `tools/`; el historial
git la toca solo en 2 commits (creación + un commit de reports).

La revisión de referencias (2026-08-28, previa a este TASK) encontró:
- **Dependencia dura:** `src/tests/test_linaje.py` (`TestBug024ToolsLinaje`)
  recorre `tools/*.md` y lee `tools/BUILD.md` — borrar el folder rompe la
  suite si no se actualiza.
- **Docs vivas:** `README.md` raíz ("everything under `tools/` is optional
  by contract"), `metaflow/02-analysis/vision/vision.md` (AG4) y
  `metaflow/02-analysis/scope/mvp-scope.md` (X4/D4).
- **No dependencias:** `src/mapping.json` regla R17-2 (transformación de
  strings del kit de entrada), `src/tests/test_restos_v5.py` (aserción
  negativa sobre un string), todo lo histórico (G36).
- **Texto del framework:** `metaflow/ai-sdlc/MetaFlow.md` §42-reports (y su
  copia en el kit) menciona "the tooling track (`tools/`)" como promesa
  futura de la metodología — **no se toca** (es genérica para adoptantes, no
  este folder heredado).

Restricciones gobernantes: ADR-001 (vigente en lo demás), visión AG4, scope
X4/D4, G36 (históricos), G38 (archivo solo con vida cerrada — ADR-002 ya
archivado en paralelo, fuera del alcance de esta SPEC).

---

## 3. Source inventory and approval references

> Pre-SPEC evidence gate (§2.4.1, G13): todas las fuentes gobernantes
> aprobadas — sin fuentes draft.

| Source | Ref | Approval |
|--------|-----|----------|
| TASK | US-000.TASK-002-eliminacion-track-tools.md | CP-TASK-READY-Approval ✓ (2026-08-28) |
| ADR | ADR-001-toolkit-transformacion.md | CP-ADR-Approval ✓ (2026-08-27) — Alternative E |
| Analysis | vision.md (AG4) · mvp-scope.md (X4/D4) | análisis estable (documentos del análisis) |
| OQs | OQ-001..004 | todas `answered` (ninguna `open`/`in-validation` — G35 OK) |
| Repository baseline | `2e564b4` | commiteado ✓ |

---

## 4. Scope

### In scope

- Borrar `tools/` completo (incluido `agent-wrappers/` con su código Python
  y tests) — registro como borrado gobernado, recuperable desde git.
- Actualizar `src/tests/test_linaje.py`: la clase `TestBug024ToolsLinaje`
  (reproducción del BUG-024) pierde su sujeto — se reemplaza por un guard de
  ausencia (el folder `tools/` no debe reaparecer); los tests de linaje del
  kit y front door (BUG-021..023) permanecen intactos.
- Actualizar la documentación viva:
  - `README.md` (raíz): la frase "everything under `tools/` is optional by
    contract" se reformula — la metodología no envía tooling; el párrafo
    "No tooling is required" se conserva sin la referencia al folder.
  - `metaflow/02-analysis/scope/mvp-scope.md` (X4): el futuro de la pista
    queda decidido — celda "Cuando se decida" → "Decidido 2026-08-28:
    eliminación (TASK-002)". D4 se conserva como registro de la decisión
    histórica (src/ sobre tools/).
  - `metaflow/02-analysis/vision/vision.md` (AG4): nota de resolución —
    la pista heredada fue eliminada 2026-08-28; el anti-objetivo (no
    reimplementarla) permanece.
- Verificación: suite completa verde + grep final sin restos del track en
  código y docs vivas.

### Out of scope

- Artefactos históricos (MEMs, SPECs, ADRs — incluido ADR-002 ya archivado
  —, US, BUGs, REVs, manifests, INDEX) — G36.
- Texto del framework: `metaflow/ai-sdlc/MetaFlow.md` §42-reports y el kit
  (`distribution-kit/`) — la promesa del tooling track futuro permanece
  (cambiarla sería un cambio de metodología aparte, con su propio origen
  gobernado).
- `mapping.json` (regla R17-2 — transformación de strings, independiente
  del folder) y el comportamiento del pipeline.
- Archivar otros documentos (ADR-001 parcialmente superado queda activo).

---

## 5. Prerequisites and baseline

- TASK US-000.TASK-002 aprobado (`CP-TASK-READY-Approval` 2026-08-28).
- Baseline commiteado `2e564b4` (traslado de `mapping.json`, TASK-001) —
  working tree limpio salvo los artefactos gobernados de este ciclo.
- Suite de tests existente (107 tests, `unittest`) como oráculo de no
  regresión.

---

## 6. Phases

### Phase A — Borrado del track heredado

**Duration:** ~15 min ciclo total — **Complexity:** Low

#### A.1 Eliminar `tools/`

`git rm -r tools/` (registro como borrado; recuperable desde git). Se borra
todo el contenido: 10 `DESIGN.md` (clock, identity, indexer, manifest,
next-id, reporter, scaffold, status, validator), `BUILD.md`, `README.md` y
`agent-wrappers/` (DESIGN.md, generate.py, parity.py, agentmodel.py, tests).
Ningún otro archivo del repo depende de él (verificado en la revisión de
referencias previa al TASK).

**Files deleted:**
- `tools/**` — track heredado del linaje AvengaDevFlow, sin uso en el
  proyecto (decisión del propietario 2026-08-28).

---

### Phase B — Suite de tests actualizada

**Duration:** ~20 min ciclo total — **Complexity:** Low

#### B.1 Actualizar `src/tests/test_linaje.py`

La clase `TestBug024ToolsLinaje` (que recorría `tools/*.md` y leía
`tools/BUILD.md` como reproducción del BUG-024) se elimina — su sujeto ya no
existe — y se reemplaza por un guard de ausencia: un test que afirma que el
folder `tools/` no existe en la raíz del repo (impide que el track reaparezca
sin un cambio deliberado). Las clases de linaje del kit/front door
(BUG-021..023: v4.2/4.1, shorthands, identidad) quedan intactas.

**Files modified:**
- `src/tests/test_linaje.py` — clase `TestBug024ToolsLinaje` reemplazada por
  guard de ausencia de `tools/`; resto de la clase de linaje intacto.

#### B.2 Correr la suite completa

`python -m unittest discover -s src/tests -p "test_*.py"` — 107 tests
(menos los 2 eliminados, más el guard) en verde; el E2E sigue validando el
pipeline y el front door.

---

### Phase C — Documentación viva

**Duration:** ~20 min ciclo total — **Complexity:** Low

#### C.1 Referencias vivas del track

- `README.md` (raíz, sección de adopción): el párrafo "everything under
  `tools/` is optional by contract — if the tooling is absent, MetaFlow
  works exactly as documented" se reformula sin la referencia al folder:
  "No tooling is required. The methodology is enforced by agents and humans
  following it — no tooling ships with it, and MetaFlow works exactly as
  documented." (mantiene el sentido, elimina la referencia al track).
- `metaflow/02-analysis/scope/mvp-scope.md` (X4): se marca la decisión del
  futuro de la pista — "Decidido 2026-08-28: eliminación del track (TASK-002)".
  D4 se conserva (registro de la decisión `src/` sobre `tools/`).
- `metaflow/02-analysis/vision/vision.md` (AG4): nota de resolución — la
  pista heredada fue eliminada 2026-08-28; el anti-objetivo (no
  reimplementarla) permanece vigente.

**Files modified:** los tres documentos anteriores.

---

## 7. Acceptance criteria

### AC-1: El track `tools/` ya no existe

**Given** el repositorio en baseline
**When** se inspecciona el árbol y el índice git
**Then** `tools/` no existe en el working tree ni en `git ls-files`

### AC-2: La suite completa queda en verde

**Given** el árbol tras el borrado
**When** se ejecuta `python -m unittest discover -s src/tests -p "test_*.py"`
**Then** todos los tests pasan (0 fallos), con `test_linaje.py` actualizado

### AC-3: Sin referencias vivas al track

**Given** el árbol tras el borrado
**When** se grepa `tools/` en `src/` y en la documentación viva
**Then** no quedan referencias al folder (salvo históricos — G36 — y el
texto del framework, AC-5)

### AC-4: Históricos intactos

**Given** el árbol tras el borrado
**When** se comparan MEMs/SPECs/ADRs/US/BUGs/REVs con el baseline
**Then** ningún artefacto histórico cambió (G36)

### AC-5: Framework y kit intactos

**Given** el árbol tras el borrado
**When** se comparan `metaflow/ai-sdlc/MetaFlow.md` y `distribution-kit/`
con el baseline
**Then** sin cambios (la promesa del tooling track futuro permanece)

### AC mapping to source (non-functional outcome)

| Measurable outcome (TASK §2) | How this SPEC satisfies it | Verifying test/evidence |
|---------------------|----------------------------|--------------------------|
| Repo sin track heredado | Borrado de `tools/` completo | AC-1 |
| Suite sin dependencia del folder | `test_linaje.py` actualizado con guard de ausencia | AC-2 |
| Docs vivas sin referencias | README, vision AG4, mvp-scope X4 actualizados | AC-3 |
| Históricos y framework intactos | Exclusiones explícitas | AC-4, AC-5 |

---

## 8. Testing strategy

- **Unit tests:** la suite existente como oráculo; `test_linaje.py` se
  actualiza (2 tests de reproducción del BUG-024 reemplazados por 1 guard de
  ausencia). 0 tests nuevos fuera de eso.
- **Integration / E2E:** `test_e2e.py` (pipeline completo) y
  `test_front_door.py` (front door del repo) siguen cubriendo el resto.
- **Edge cases:** ausencia del folder (guard), grep de restos en código y
  docs vivas.
- **BUG evidence:** n/a — no es un BUG (deuda técnica, sin TDD red→green).

---

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | Suite completa verde (unittest) | pass (objetivo) |
| SAST / DAST | — | n/a — sin superficie externa; borrado + tests |
| Perf-smoke (p95/p99) | — | n/a — sin cambios de comportamiento |
| Prompt-injection scan | — | n/a — sin superficie LLM nueva |
| Secret-leak scan | Sin secretos en el diff | pass (objetivo) |
| Hallucination lint | Docs vivas coherentes con el árbol | pass (objetivo) |
| IP / license provenance | — | n/a — sin dependencias nuevas; se BORRA código heredado |
| PII / DLP | — | n/a — sin datos personales (internal) |
| Dependency-confusion | — | n/a — sin dependencias |
| Test-first evidence | — | n/a — deuda técnica, no BUG |
| Behavioral reproducibility | E2E sigue verde | pass (objetivo) |
| TASK-manifest validation | Manifest válido contra schema | pass (objetivo) |

> Cada gate termina `pass` / `waived` (ADR-NNN) / `n/a` (con razón) (§3.6).

---

## 10. Security and data

- Sin autenticación, secretos ni superficie de red: borrado de archivos
  locales + actualización de tests/docs.
- `data_classification: internal` — sin datos personales; el código borrado
  es especificaciones/herramientas heredadas sin secretos.
- No se introducen dependencias; se elimina código del linaje anterior.

---

## 11. Monitoring and observability

- n/a — CLI local sin servicios; sin logs/métricas que agregar o modificar.

---

## 12. Migration, compatibility and rollback

- **Migration:** `git rm -r tools/` + actualización de tests y docs vivas en
  un único commit del Delivery Loop.
- **Compatibility:** nada depende de `tools/` en runtime (el pipeline lee
  `input-kit/` → `distribution-kit/`); la suite se mantiene verde.
- **Rollback:** `git revert` del commit del loop (o `git checkout` del
  folder desde el historial) — el borrado es recuperable íntegramente desde
  git.

---

## 13. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| Suite rota por dependencia no detectada del folder | 2 | 3 | Revisión de referencias previa + suite como oráculo (AC-2) |
| Referencia viva olvidada (docs) | 2 | 2 | Grep final explícito como AC-3 |
| Tocar un histórico o el framework por error | 1 | 4 | Exclusiones explícitas + AC-4/AC-5 |
| Perder capacidad de agent-wrappers sin querer | 2 | 2 | Decisión explícita del propietario (no se usa; cero refs externas); recuperable desde git |

---

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| Reemplazar `TestBug024ToolsLinaje` por un guard de ausencia en vez de borrar los tests sin más | La reproducción del BUG-024 pierde su sujeto, pero el guard impide que el track reaparezca sin un cambio deliberado |
| No tocar el texto del framework (`MetaFlow.md` §42-reports ni el kit) | La promesa del tooling track futuro es genérica de la metodología para adoptantes, no este folder heredado; cambiarla sería un cambio de metodología aparte |
| Reformulación mínima del párrafo de `README.md` | Conserva el mensaje ("no tooling required") sin la referencia muerta al folder |
| X4 se marca resuelto; D4 se conserva | X4 era el pendiente ("cuando se decida el futuro de la pista") — este cambio ES la decisión; D4 es el registro histórico de la decisión `src/` sobre `tools/` |
| ADR-001 queda activo (no se archiva) | Solo está parcialmente superado (ADR-004, ubicación de `mapping.json`); sus demás decisiones (Python+stdlib, `src/`, NFRs) siguen gobernando (G38) |

---

## 15. Stop conditions

- Durante la ejecución aparece una referencia viva que requiere tocar un
  artefacto histórico → detener (G36) y pedir decisión.
- El texto del framework requeriría cambios para completar el loop → detener
  (fuera de alcance; cambio de metodología aparte).
- El guard de ausencia o la suite no vuelven a verde → detener y registrar el
  hallazgo en el MEM.

---

## 16. Definition of Done (DoD)

- [ ] Todas las fases implementadas (A, B, C)
- [ ] AC-1..AC-5 verificados
- [ ] Suite completa GREEN (`unittest discover`)
- [ ] Código y docs siguen ADR-001 (vigente) y las decisiones de análisis
- [ ] Gates aplicables `pass` / `n/a` con razón
- [ ] MEM creado en `metaflow/22-memory/` (exactamente uno por Delivery Loop)
- [ ] Entrada `delivery_loops[]` agregada al manifest de US-000.TASK-002
- [ ] CP-MEM-Approval registrado

---

## 17. References

- ADR-001-toolkit-transformacion.md — Alternative E (`src/` sobre `tools/`).
- vision.md — AG4 (no reimplementar la pista).
- mvp-scope.md — X4 (futuro de la pista, ahora decidido) y D4 (decisión de
  ubicación del código).
- US-000.TASK-002-eliminacion-track-tools.md — TASK aprobado.
- BUG-024 y MEM-260827-1725-fix-tools-linaje.md — historia del track
  (referencia histórica, G36).

---

## 18. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-28 | human:eugenioserrano | Revisión 1 — creación |

---

## 19. CP-SPEC-Approval

> **MetaFlow §2.4.1, §3.0.** This SPEC remains a draft until the
> Dev-validator (+ applicable domain owners) records `CP-SPEC-Approval`
> (in the `review` frontmatter block). TASK approval (`CP-TASK-READY-Approval`)
> authorizes SPEC preparation; **SPEC approval** authorizes the code-run /
> Delivery Loop. A material source change invalidates this approval — stop,
> revise, re-approve (G15).

| Field | Value |
|-------|-------|
| **review.reviewers** | Dev-validator: `human:eugenioserrano` (autoasignado — no hay otro titular) |
| **review.decision** | approved |
| **review_ready_at** | `2026-08-28T01:19:22-03:00` |
| **review.started_at** | `2026-08-28T01:21:30-03:00` |
| **review.decided_at** | `2026-08-28T01:22:27-03:00` |
| **Findings** | None — acknowledged_without_comment (razón en el frontmatter) |
