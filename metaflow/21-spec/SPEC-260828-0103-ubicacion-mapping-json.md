---
id: "SPEC-260828-0103"
title: "Traslado de mapping.json a src/ — toolkit autocontenido"
date: "2026-08-28"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved" # draft | approved | blocked | obsolete
origin: "ADR-004"
task: "US-000.TASK-001"
revision: 1 # material revision of this canonical SPEC (matches manifest spec_revisions[])
associated_adrs:
  - "metaflow/11-adrs/ADR-004-ubicacion-mapping-json.md"
prerequisites: []
risk_class: "low" # low | medium | high | critical (mirrors the TASK's risk_class)
autonomy_level: "L3" # L1 | L2 | L3 | L4 — defaults by risk: low/medium→L3, high→L2, critical→L1; L4 requires an ADR (§3.3)
turn_budget: "" # OPTIONAL — leave empty to use the platform/agent default (§3.3)
data_classification: "internal" # public | internal | confidential | restricted
review_ready_at: "2026-08-28T01:03:18-03:00"
review: # CP-SPEC-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-28T01:04:30-03:00"
  decided_at: "2026-08-28T01:05:00-03:00"
  findings: []
  acknowledged_without_comment: true # must be true when findings is empty (§3.0)
  acknowledgment_reason: "Aprobación del propietario (Dev-validator autoasignado: no hay otro titular) sin hallazgos — revisión de la SPEC en conversación, 2026-08-28"
---

# SPEC-260828-0103 — Traslado de `mapping.json` a `src/`

| Field | Value |
|-------|-------|
| **Origin** | ADR-004 |
| **TASK** | US-000.TASK-001 |
| **ADRs** | [ADR-004](file:///D:/MetaFlow/metaflow/11-adrs/ADR-004-ubicacion-mapping-json.md) (aprobado 2026-08-28) · ADR-001 (parcialmente superado por ADR-004 en la ubicación del diccionario) |
| **Risk Class** | low |
| **Revision** | 1 |

---

## 1. Objective

Trasladar el diccionario de transformación `mapping.json` de la raíz del
repositorio a `src/mapping.json`, dejando `src/` como el toolkit completo y
autocontenido: engine (`transform.py`), verificador (`verify.py`), reporte
(`report.py`), diccionario (`mapping.json`) y tests (`tests/`). El pipeline
debe seguir corriendo igual (`python src/transform.py`), con la misma
salida, y la documentación viva del proyecto debe reflejar la nueva
ubicación.

Si NO se implementa: el toolkit sigue sin ser autocontenido y la raíz del
repositorio sigue mezclando el diccionario del pipeline con los dos kits y
los metadatos — el estado que el propietario decidió corregir en ADR-004.

---

## 2. Context

El ADR-001 (aprobado 2026-08-27) fijó `mapping.json` en la raíz del repo
(Alternative F), registrando como costo: *"el toolkit no queda 100 %
autocontenido en `src/` (aceptable: el repo completo es el producto)"*.
Con el toolkit en uso, el propietario revisó la estructura y concluyó que
ese costo ya no es aceptable. El **ADR-004** (aprobado 2026-08-28, `CP-ADR-Approval`)
supercede **parcialmente** al ADR-001: reemplaza únicamente la decisión de
ubicación del diccionario; el resto del ADR-001 (Python 3.10+ con stdlib,
código en `src/`, salidas, NFRs de performance y portability) permanece
vigente.

Estado actual del código (baseline `c531de2`):
- `src/transform.py` — `DEFAULT_MAPPING = REPO_ROOT / "mapping.json"` (raíz),
  con flag CLI `--mapping <ruta>` ya soportado.
- 13 archivos de tests referencian `parents[2] / "mapping.json"` (raíz del
  repo).
- `mapping.json` en la raíz: 55 reglas (familias M/C/B/D/R + rutas) + lista
  `exclude` — su contenido NO cambia en este Delivery Loop.

Restricciones gobernantes (ADR-004): RULE-04 intacta (reglas como datos —
agregar una regla no toca el engine); la raíz queda solo con `input-kit/`,
`distribution-kit/` y metadatos del repo; el flag `--mapping` se conserva
para rutas alternativas.

---

## 3. Source inventory and approval references

> Pre-SPEC evidence gate (§2.4.1, G13): todas las fuentes gobernantes
> aprobadas — sin fuentes draft.

| Source | Ref | Approval |
|--------|-----|----------|
| TASK | US-000.TASK-001-ubicacion-mapping-json.md | CP-TASK-READY-Approval ✓ (2026-08-28) |
| ADR | ADR-004-ubicacion-mapping-json.md | CP-ADR-Approval ✓ (2026-08-28) |
| Container | US-000-non-functional.md | permanente, sin aprobación |
| OQs | OQ-001..004 | todas `answered` (ninguna `open`/`in-validation` — G35 OK) |
| Repository baseline | `c531de2` | commiteado ✓ |

---

## 4. Scope

### In scope

- Mover `mapping.json` a `src/mapping.json` (registrado como move, no como
  borrado+creado).
- Actualizar `src/transform.py`: el default de carga del diccionario pasa a
  ser relativo al módulo (`src/mapping.json`); el flag `--mapping` conserva
  su comportamiento (override).
- Actualizar los 13 archivos de tests que referencian la raíz.
- Actualizar la documentación viva que menciona la ubicación del diccionario:
  README raíz, sección de proyecto de `AGENTS.md`, PROC-001, y cualquier
  otra referencia viva encontrada por grep (introducción, glossary si aplica).
- Verificar el comportamiento: suite completa verde + dry-run y ejecución
  real con verificación OK.

### Out of scope

- Contenido de `mapping.json` (reglas, `exclude`) — intocable.
- Artefactos históricos (MEMs, SPECs, ADRs, US, BUGs, REVs) — registran la
  ubicación en su momento (G36).
- Comportamiento del pipeline, formato de salidas, reportes, NFRs.
- `distribution-kit/` — no se regenera en este loop (es el producto del
  pipeline, no el pipeline).

---

## 5. Prerequisites and baseline

- ADR-004 aprobado (`CP-ADR-Approval` 2026-08-28).
- TASK US-000.TASK-001 aprobado (`CP-TASK-READY-Approval` 2026-08-28).
- Baseline commiteado `c531de2` (migración §5.16) — working tree limpio
  salvo los artefactos gobernados recién creados.
- Suite de tests existente (107 tests, `unittest`) como oráculo de no
  regresión.

---

## 6. Phases

### Phase A — Traslado del diccionario y del engine

**Duration:** ~30 min ciclo total — **Complexity:** Low

#### A.1 Mover `mapping.json` a `src/`

`git mv mapping.json src/mapping.json` (preserva historia del archivo). El
archivo no se toca en contenido: solo cambia su ubicación.

**Files modified:**
- `mapping.json` → `src/mapping.json` — move registrado, contenido intacto.

#### A.2 Actualizar el default de carga en `src/transform.py`

`DEFAULT_MAPPING` pasa de `REPO_ROOT / "mapping.json"` a una ruta relativa
al módulo: `Path(__file__).resolve().parent / "mapping.json"` — portability
(ADR-001): el toolkit corre desde cualquier cwd, sin depender de la raíz del
repo. El flag `--mapping` mantiene su semántica actual (ruta explícita
gana al default). Se revisa el resto de `transform.py` por otras referencias
a la raíz (`REPO_ROOT`) que solo existieran para el diccionario.

**Files modified:**
- `src/transform.py` — `DEFAULT_MAPPING` (default del diccionario, relativo
  al módulo); ayuda del CLI actualizada si menciona "raíz".

---

### Phase B — Tests: rutas del diccionario

**Duration:** ~30 min ciclo total — **Complexity:** Low

#### B.1 Actualizar las referencias de ruta en los tests

Los 13 tests que usan `Path(__file__).resolve().parents[2] / "mapping.json"`
(o `ROOT / "mapping.json"` en `test_reproducibilidad.py`) pasan a
`parents[1]` (la carpeta `src/`, donde vive ahora el diccionario). Cada
archivo se revisa individualmente — la ruta es la única referencia que se
toca.

**Files modified:**
- `src/tests/test_exclusions.py`, `test_links.py`, `test_cli.py`,
  `test_e2e.py`, `test_path_rename.py`, `test_numbering.py`,
  `test_mapping.py`, `test_remove.py`, `test_regex.py`, `test_report.py`,
  `test_reproducibilidad.py`, `test_rename.py`, `test_version.py` —
  ruta del diccionario a `parents[1] / "mapping.json"`.

#### B.2 Correr la suite

`python -m unittest discover -s src/tests -p "test_*.py"` — 107+ tests en
verde. El E2E (`test_e2e.py`) regenera el kit en temp y valida
reproducibilidad (cubre AC-3/AC-4).

---

### Phase C — Documentación viva

**Duration:** ~30 min ciclo total — **Complexity:** Low

#### C.1 Referencias vivas

Grep de `mapping.json` sobre código + documentación viva (excluyendo
`metaflow/22-memory/`, `21-spec/`, `11-adrs/`, `13-bugs/`, `12-functional/`
— históricos, G36) y actualizar:

- `README.md` (raíz) — la referencia al diccionario pasa a `src/mapping.json`.
- `AGENTS.md` (sección de proyecto) — el pipeline se describe como `src/`
  (engine + diccionario autocontenido); se ajusta la mención
  "(`src/` + `mapping.json`)".
- `metaflow/02-analysis/process/PROC-001-transformacion-kit.md` — las
  menciones del diccionario indican la ubicación nueva.
- `metaflow/02-analysis/introduction/introduccion-a-metaflow.md`
  (derivada) — si menciona ubicación, se ajusta (fuente de verdad: los
  artefactos, G28).
- `metaflow/02-analysis/glossary/metaflow.md` — solo si menciona ubicación
  (es la fuente conceptual de las reglas; probablemente no requiera cambio).

**Files modified:** los detectados por el grep de restos (verificación: grep
final sin restos en código ni docs vivas).

---

## 7. Acceptance criteria

### AC-1: El diccionario vive en `src/`

**Given** el repositorio en baseline
**When** se inspecciona el árbol
**Then** `src/mapping.json` existe y no existe `mapping.json` en la raíz

### AC-2: El pipeline carga el diccionario por default

**Given** el árbol tras el traslado
**When** se ejecuta `python src/transform.py --dry-run` sin `--mapping`
**Then** termina con exit 0 y el plan refleja las 55 reglas del diccionario
(dry-run sin escribir nada)

### AC-3: La suite completa queda en verde

**Given** el árbol tras el traslado
**When** se ejecuta `python -m unittest discover -s src/tests -p "test_*.py"`
**Then** todos los tests pasan (0 fallos), incluido el E2E de reproducibilidad

### AC-4: Comportamiento idéntico (reproducibilidad)

**Given** el árbol tras el traslado
**When** se ejecuta la ejecución real del pipeline contra `input-kit/`
**Then** `distribution-kit/` se regenera con el mismo contenido que el
baseline y el verificador de tokens prohibidos pasa (cero leftover)

### AC-5: Sin restos de la ubicación antigua

**Given** el árbol tras el traslado
**When** se grepa `mapping.json` en `src/` y en la documentación viva
**Then** no quedan referencias a la raíz como ubicación del diccionario
(salvo históricos, G36)

### AC-6: Históricos intactos

**Given** el árbol tras el traslado
**When** se comparan MEMs/SPECs/ADRs/US/BUGs/REVs con el baseline
**Then** ningún artefacto histórico cambió (G36)

### AC mapping to source (non-functional outcome)

| Measurable outcome (TASK §2 / ADR-004) | How this SPEC satisfies it | Verifying test/evidence |
|---------------------|----------------------------|--------------------------|
| Toolkit autocontenido en `src/` | Traslado del diccionario + rutas relativas al módulo | AC-1, AC-2 |
| Raíz limpia (solo kits y metadatos) | Move del diccionario; sin archivos de trabajo del pipeline en la raíz | AC-1, AC-5 |
| Mismo comportamiento y salidas | Sin cambios de reglas ni de engine más allá del default de ruta | AC-3, AC-4 |
| RULE-04: reglas como datos | Contenido de `mapping.json` intacto | AC-6 |

---

## 8. Testing strategy

- **Unit tests:** los existentes (orden, regex, mapping, numbering, paths)
  actualizados a la nueva ruta — 0 tests nuevos necesarios; el oráculo es la
  suite completa (107+ tests).
- **Integration / E2E:** `test_e2e.py` (pipeline completo con kit real +
  verificador) — cubre AC-4; `test_front_door.py` y `test_linaje.py`
  siguen validando el front door del repo (AGENTS.md incluido).
- **Edge cases:** `--mapping` con ruta inexistente (test_cli ya lo cubre:
  `no-such-mapping.json` → error); default relativo al módulo invocado desde
  cualquier cwd.
- **BUG evidence:** n/a — no es un BUG (refactor técnico, sin TDD red→green).

---

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | Suite completa verde (unittest) | pass (objetivo) |
| SAST / DAST | — | n/a — pipeline local sin superficie externa, stdlib únicamente |
| Perf-smoke (p95/p99) | — | n/a — sin cambios de comportamiento; NFR < 1 min del ADR-001 se verifica en el run E2E |
| Prompt-injection scan | — | n/a — sin superficie LLM nueva |
| Secret-leak scan | Sin secretos en el diff | pass (objetivo) |
| Hallucination lint | Docs vivas coherentes con la realidad del árbol | pass (objetivo) |
| IP / license provenance | — | n/a — sin dependencias nuevas |
| PII / DLP | — | n/a — sin datos personales (data_classification internal) |
| Dependency-confusion | — | n/a — sin dependencias de terceros |
| Test-first evidence | — | n/a — refactor mecánico con suite existente (no es BUG) |
| Behavioral reproducibility | E2E regenera el mismo kit | pass (objetivo) |
| TASK-manifest validation | Manifest válido contra schema | pass (objetivo) |

> Cada gate termina `pass` / `waived` (ADR-NNN) / `n/a` (con razón) (§3.6).

---

## 10. Security and data

- Sin autenticación, autorización, secretos ni superficie de red: el toolkit
  es un CLI local que procesa archivos de texto del repositorio.
- `data_classification: internal` — el diccionario contiene nombres/reglas
  del proyecto, sin datos personales.
- El cambio no introduce ni modifica dependencias (stdlib únicamente,
  ADR-001).

---

## 11. Monitoring and observability

- n/a — CLI local sin servicios; el reporte del run (`transform-report-*`)
  sigue generándose igual (comportamiento no cambiado).

---

## 12. Migration, compatibility and rollback

- **Migration:** `git mv mapping.json src/mapping.json` + actualización de
  rutas (engine, tests, docs vivas) en un único commit del Delivery Loop.
- **Compatibility:** el flag `--mapping <ruta>` conserva el override — el
  pipeline sigue pudiendo leer un diccionario en cualquier ruta (usado por
  tests con fixtures); `python src/transform.py` no cambia su invocación.
- **Rollback:** `git revert` del commit del loop (o `git mv` inverso) — no
  hay migración de datos ni esquemas; el contenido del diccionario es
  inmutable en este loop.

---

## 13. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| Referencia residual a la raíz (código o docs vivas) | 2 | 3 | Grep de restos como AC-5 explícito + suite en verde |
| Regresión en rutas de tests | 2 | 3 | Suite completa como oráculo (AC-3) |
| E2E que dependa de la raíz para el diccionario | 2 | 3 | Actualización explícita en Phase B; AC-4 |
| Editar un histórico por error | 1 | 4 | Scope explícito (G36) + diff final revisado (AC-6) |

---

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| Default relativo al módulo (`Path(__file__).parent`) en vez de ruta absoluta al repo | Portability (ADR-001): el toolkit corre desde cualquier cwd; `--mapping` conserva el override |
| Los 13 tests se actualizan en vez de añadir un conftest/helper de ruta | Cambio mínimo y explícito; la suite ya es el oráculo; sin abstracciones nuevas para un movimiento mecánico |
| No regenerar `distribution-kit/` en el loop | El kit es producto del pipeline; su regeneración/evidencia pertenece al proceso de publicación (PROC-001), no al refactor de ubicación |
| `git mv` (move) en vez de borrar+crear | Preserva la historia del archivo y hace el diff legible |

---

## 15. Stop conditions

- La suite no vuelve a verde por una dependencia de ruta no identificada →
  detener, registrar el hallazgo en el MEM y pedir resolución (no asumir).
- Un artefacto histórico (MEM/SPEC/ADR/US/BUG/REV) requeriría modificación
  para completar el loop → detener (G36) y pedir decisión.
- Un cambio material en el contenido de `mapping.json` (fuera de scope) →
  detener (G15).

---

## 16. Definition of Done (DoD)

- [ ] Todas las fases implementadas (A, B, C)
- [ ] AC-1..AC-6 verificados
- [ ] Suite completa GREEN (`unittest discover`)
- [ ] Código y docs siguen ADR-004 (y el resto vigente del ADR-001)
- [ ] Gates aplicables `pass` / `n/a` con razón
- [ ] MEM creado en `metaflow/22-memory/` (exactamente uno por Delivery Loop)
- [ ] Entrada `delivery_loops[]` agregada al manifest de US-000.TASK-001
- [ ] CP-MEM-Approval registrado

---

## 17. References

- ADR-004-ubicacion-mapping-json.md — decisión gobernante de este cambio.
- ADR-001-toolkit-transformacion.md — decisiones vigentes restantes
  (Python + stdlib, `src/` para código, NFRs).
- US-000.TASK-001-ubicacion-mapping-json.md — TASK aprobado.
- PROC-001-transformacion-kit.md — proceso que el toolkit implementa.

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
| **review_ready_at** | `2026-08-28T01:03:18-03:00` |
| **review.started_at** | `2026-08-28T01:04:30-03:00` |
| **review.decided_at** | `2026-08-28T01:05:00-03:00` |
| **Findings** | None — acknowledged_without_comment (razón en el frontmatter) |
