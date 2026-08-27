---
id: "SPEC-260827-0142"
title: "TASK-002 — Verificador de tokens prohibidos + reporte + aceptación E2E"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved"
origin: "US-001"
task: "US-001.TASK-002"
revision: 2
associated_adrs:
  - "metaflow/11-adrs/ADR-001-toolkit-transformacion.md"
prerequisites:
  - "metaflow/21-spec/SPEC-260827-0124-bolt001-engine-transformacion.md"
risk_class: "low"
autonomy_level: "L3"
turn_budget: 10
data_classification: "internal"
review_ready_at: "2026-08-27T01:42:33-03:00"
review:
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-27T02:03:08-03:00"
  decided_at: "2026-08-27T02:03:08-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Re-aprobación de la Revisión 2 (retención acotada de evidencia: 2 corridas por versión) por el propietario (Dev-validator autoasignado) sin hallazgos — 2026-08-27. G15 cumplido; el V-Bounce 1 de TASK-002 continúa bajo la revisión 2"
---

# SPEC-260827-0142 — TASK-002: Verificador de tokens prohibidos + reporte + E2E

| Field | Value |
|-------|-------|
| **Origin** | US-001 |
| **TASK** | US-001.TASK-002 |
| **ADRs** | [ADR-001](../11-adrs/ADR-001-toolkit-transformacion.md) |
| **Risk Class** | low |
| **Revision** | 1 |

---

## 1. Objective

Implementar el **verificador de tokens prohibidos**, el **reporte de
transformación con persistencia de evidencia** y la **aceptación E2E contra
el kit real** del TASK-002. El verificador barre el kit de salida (contenido
y rutas) buscando cualquier resto de la marca previa — tokens exactos y
variantes — y **falla el run** (exit != 0) listando los hits si encuentra
alguno (AC-7, O1 de la visión). El reporte persiste por run la evidencia
completa en `transform-reports/<versión>/<run>/` — `report.json`
(estructurado para IA), `report.md` (legible), **diffs por archivo**
(original → convertido), lista de archivos sin cambios, remociones y log —
para revisión humana o procesamiento con IA posterior (AC-8, AC-11, R6). La
aceptación E2E corre el pipeline contra el kit real y exige el verificador en
cero (AC-9).

**Si no se implementa:** el pipeline no puede garantizar cero contaminación
de marca (BR-001 queda sin control), no deja evidencia revisable de cada run
(la revisión humana del journey pierde su insumo) y no hay forma de validar
la transformación contra el kit real.

## 2. Context

La necesidad viene de la US-001 (aprobada, Rev 4) y su TASK-002 (aprobado).
El **TASK-001 ya está entregado** (Development Completed): el engine
(`src/transform.py`) transforma `input-kit/` → `distribution-kit/` con
`mapping.json`, dry-run/real, borrado validado de salida y exclusiones; este
TASK agrega la garantía de salida y la evidencia. PROC-001 (activo) define el
proceso completo: tras escribir el kit → **verificar tokens** → **generar
reporte** → **persistir evidencia** → revisión humana → publicación.

Restricciones gobernantes:
- **ADR-001 (accepted):** Python 3.10+, stdlib únicamente, código en `src/`
  (`verify.py`, `report.py`), `unittest`.
- **Glossary `metaflow.md` (stable):** §6 lista de tokens prohibidos
  (`Avenga`, `AITL`, `HITL`, `Bolt`/`BOLT`/`bolts`, `V-Bounce`/`v_bounces`,
  `Raja`, `DORA`); §7 términos que se conservan (excepciones del barrido) y
  archivos excluidos.
- **Domain-model (stable):** `TransformRun` — si `forbidden_hits` no está
  vacío, el run es `failed` (RULE-01); el reporte es la evidencia que el
  humano revisa (RULE-03).

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| TASK | `metaflow/12-functional/tasks/US-001.TASK-002-verificador-reporte.md` | CP-TASK-READY-Approval ✓ (2026-08-27) |
| Feature US | `metaflow/12-functional/user-stories/US-001-toolkit-transformacion.md` | CP-US-Approval ✓ (incl. Rev 4 — AC-11/R6) |
| ADRs | `metaflow/11-adrs/ADR-001-toolkit-transformacion.md` | CP-ADR-Approval ✓ (accepted) |
| Prior SPEC | `metaflow/21-spec/SPEC-260827-0124-bolt001-engine-transformacion.md` (rev 2) | CP-SPEC-Approval ✓ + MEM-260827-0140 approved (TASK-001 Development Completed) |
| Analysis | `metaflow/02-analysis/glossary/metaflow.md` (§6/§7), `metaflow/02-analysis/process/PROC-001-transformacion-kit.md` (Reglas 3/6/7), `metaflow/02-analysis/domain-model/entities/TransformRun.md` | stable / active ✓ |
| Open questions | — | 4/4 `answered` — G35 OK |
| Repository baseline | `58ac5eb` (+ trabajo de TASK-001 sin commitear, G34) | — |

## 4. Scope

### In scope

- `src/verify.py`: verificador de tokens prohibidos sobre contenido y rutas
  del kit de salida — tokens exactos + variantes (case-insensitive,
  plurales/derivados, URLs, copyright), con lista de excepciones
  (términos conservados del glossary §7) como datos; exit 0 sin hits, exit
  != 0 con hits listados.
- `src/report.py`: reporte del run — `report.json` (por archivo: ruta
  antes/después, reglas aplicadas, remociones, changed/unchanged, cobertura),
  `report.md` legible, `diff/<archivo>.diff` (unified diff original →
  convertido), `unchanged.txt`, `removals.json`, `run.log`.
- `src/transform.py` (modificación): el run real integra al final —
  verificar → persistir evidencia en `transform-reports/<versión>/<run>/` →
  exit code según resultado.
- `src/tests/`: suites unitarias (verify, report) + E2E con fixture y contra
  el kit real (output temporal).
- `transform-reports/` (raíz): carpeta de evidencia por run, con **retención acotada a las 2 corridas más recientes por versión** (R6, Revisión 2).

### Out of scope

- Engine/CLI de transformación → TASK-001 (entregado).
- Template HTML de reportes de MetaFlow → entregable aparte (X6).
- Reglas `remove` difusas (R3, citas "Accelerate") → extensión del
  diccionario por versión (OQ-004).
- Traducción, licencias, migración de la raíz → fuera del MVP.

## 5. Prerequisites and baseline

- TASK-001 entregado: `src/transform.py` + `mapping.json` + fixtures
  (`src/tests/fixtures/kit-mini{,-expected}`) — suite 37/37 en verde.
- `input-kit/` presente (kit AvengaDevFlow real, solo lectura).
- Baseline: `58ac5eb` + trabajo de TASK-001 en el árbol (sin commitear, G34).

## 6. Phases

### Phase A — Verificador (`src/verify.py`)

**Duration:** 2h — **Complexity:** Medium

#### A.1 Barrido de tokens prohibidos (contenido y rutas)

El verificador recibe el kit de salida y la lista de tokens prohibidos
(glossary §6): `Avenga`, `AITL`, `HITL`, `Bolt`, `TASK`, `bolts`, `V-Bounce`,
`v_bounces`, `Raja`, `DORA`. Por cada archivo de texto (UTF-8) y por cada
ruta (archivos y carpetas) busca:

- **Tokens exactos** (case-sensitive para `V-Bounce`, `v_bounces`, `Bolt`,
  `BOLT`, `bolts` — según la lista del glossary).
- **Variantes con regex:** `[Aa]venga` (marca en cualquier forma), `AITL` /
  `HITL` case-insensitive, `bolt`/`bolts` case-insensitive (derivados),
  `v[-_ ]?bounce` (separadores), URLs/emails con dominio `avenga`, líneas
  `Copyright … Avenga`, headers con `# Avenga DevFlow`, `author: Avenga`.

El resultado es una lista de hits por archivo/ruta: `{path, token, line,
context}`. La **lista de excepciones** (términos conservados del glossary §7
— `US`, `TC`, `ADR`, `DISC`, `REV`, `AREV`, `OQ`, `BUG`, `INC`, `RISK`,
`RETRO`, `UAT`, `BR`, `PROMPT`, `PROC`, `INT`, `SPEC`, `MEM`, `G01`–`G39`,
`W01`–`W21`, `N01`–`N23`, `T01`–`T12`, `DoR`, `DoD`, `manifest`,
`schema_version`, `checkpoint_approvals`) se aplica para no marcar
falsos positivos — p. ej. `SPEC`, `MEM`, `BR` no contienen tokens prohibidos,
pero la lista queda como dato para cuando una futura versión introduzca
términos que sí colisionen.

**Files created:**
- `src/verify.py` — Verificador de tokens prohibidos (contenido + rutas,
  exactos + variantes, excepciones como datos, exit 0/1).

### Phase B — Reporte y persistencia (`src/report.py` + integración)

**Duration:** 2h — **Complexity:** Medium

#### B.1 Reporte estructurado y diffs por archivo

`report.py` consume el plan del engine (reglas aplicadas, remociones,
exclusiones, changed/unchanged) y los hits del verificador, y genera:

- `report.json` — estructurado para IA (AC-11): por archivo `{src, dst,
  rules_applied, removals, changed}`, totales de reglas/remociones,
  cobertura (archivos sin cambios), hits de verificación, exclusión de
  `TEMPLATE-REPORT.html`.
- `report.md` — versión legible del mismo contenido.
- `diff/<rel-path>.diff` — **unified diff** (stdlib `difflib`) por cada
  archivo cambiado, comparando el original del input contra el convertido
  (para rutas renombradas se compara por identidad lógica src→dst).
- `unchanged.txt` — archivos con cero cambios (candidatos a regla faltante).
- `removals.json` — remociones ejecutadas (por regla y por archivo).
- `run.log` — salida completa del run.

Todo se persiste en `transform-reports/<versión-input>/<run-timestamp>/`
(R6). Al final de cada corrida real se aplica la **retención acotada**: se
conservan las **2 corridas más recientes por versión** y se purgan las
anteriores, listando las purgadas en el `run.log` (nada silencioso). El
parámetro `--keep-runs N` (default 2) controla la retención; el dry-run nunca
purga.

#### B.2 Integración con `transform.py`

El run real de `transform.py` agrega al final: correr `verify` sobre
`distribution-kit/` → si hay hits, el run falla (exit != 0) y se listan en el
reporte; si no, genera y persiste la evidencia (Phase B.1) y termina con
exit 0. El resumen de consola muestra el path de la carpeta de evidencia.

**Files created:**
- `src/report.py` — Generación y persistencia del reporte (JSON/MD, diffs,
  unchanged, removals, log).

**Files modified:**
- `src/transform.py` — Integración del paso final: verificación + persistencia
  de evidencia + exit code (TASK-002 extiende el run real del engine).

### Phase C — Tests (unitarios + E2E)

**Duration:** 2h — **Complexity:** Medium

#### C.1 Suites `unittest`

- `test_verify.py` — tokens exactos, variantes (case, plurales, URLs,
  copyright), barrido de rutas, excepciones, exit codes.
- `test_report.py` — estructura de `report.json`, diffs por archivo,
  `unchanged.txt`, `removals.json`, `run.log`, persistencia en
  `transform-reports/`, **retención: con 3 corridas, quedan las 2 más
  recientes y la más antigua se purga (listada en el log)**.
- `test_e2e.py` — E2E con fixture (kit-mini → output temporal: verificador en
  cero, carpeta de evidencia completa) y E2E contra el **kit real**
  (`input-kit/` → output temporal): verificador en cero o, si hay leftovers,
  lista los hits para extender el diccionario (OQ-004).

**Files created:**
- `src/tests/test_verify.py`, `test_report.py`, `test_e2e.py` — Suites.

---

## 7. Acceptance criteria

### AC-7: Verificador de tokens prohibidos

**Given** un kit transformado, **When** corre el verificador, **Then** el run
falla (exit != 0) y lista los hits si queda cualquier token prohibido; si no
queda ninguno, el run es exitoso.

### AC-8: Reporte de transformación

**Given** una ejecución real, **When** termina, **Then** se genera el reporte
con reglas aplicadas, conteos por regla y remociones listadas.

### AC-9: Aceptación E2E contra el kit real

**Given** el toolkit y el kit real en `input-kit/`, **When** se ejecuta la
suite E2E, **Then** la aceptación pasa con el verificador en cero (los
unitarios del engine ya viven en TASK-001).

### AC-11: Evidencia persistente por run

**Given** una ejecución real, **When** termina, **Then** la evidencia queda
persistida en `transform-reports/<versión>/<run>/` (reporte JSON+MD, diffs
por archivo, lista de sin-cambios, log).

### AC mapping to source (functional) / measurable outcome (non-functional)

| Source AC / outcome | How this SPEC satisfies it | Verifying test/evidence |
|---------------------|----------------------------|--------------------------|
| US AC-7 | Phase A: barrido exacto + variantes sobre contenido y rutas; exit != 0 con hits | `test_verify.py` |
| US AC-8 | Phase B.1: reporte con reglas, conteos y remociones | `test_report.py` |
| US AC-9 | Phase C.1: E2E fixture + kit real con verificador en cero | `test_e2e.py` |
| US AC-11 | Phase B.1/B.2: persistencia en `transform-reports/` (nunca borrada) | `test_report.py` (persistencia + no-borrado) |

---

## 8. Testing strategy

- **Unit tests (~16 casos):** verify — tokens exactos (3), variantes (4),
  rutas (2), excepciones (2), exit codes (2); report — estructura JSON (2),
  diffs (2), unchanged/removals/log (3), persistencia y no-borrado (2).
- **Integration tests:** ninguno separado (la integración verify+report se
  cubre en E2E).
- **E2E tests (2):** fixture kit-mini completo y kit real `input-kit/` con
  output temporal.
- **Edge cases:** archivo binario en el output (no se barre), rutas con
  espacios, variantes Unicode del guion en `V-Bounce`, carpeta de evidencia
  con runs previos (no se borra), hits en rutas (no solo contenido).
- **BUG evidence:** N/A (no es un BUG TASK).

---

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | Suite `unittest` verde (incl. TASK-001: 37 + nuevas) | pass (objetivo) |
| SAST / SBOM | Sin dependencias de terceros ni superficie de red | n/a — script local sin superficie atacable externa |
| Perf-smoke (p95/p99) | Pipeline completo < 1 min (NFR ADR-001) | pass (objetivo) — medición del run real contra el kit |
| Prompt-injection scan | No procesa prompts ni inputs externos | n/a — sin entrada no confiable |
| Secret-leak scan | Sin credenciales en el código | pass |
| Hallucination lint | Código verificado contra stdlib real de Python 3.10+ | pass |
| IP / license provenance | Cero dependencias; sin código de terceros | n/a — sin código de terceros |
| PII / DLP | No procesa datos personales | n/a — sin datos personales |
| Dependency-confusion | Cero dependencias instaladas | n/a — sin dependencias |
| Test-first evidence | Tests escritos antes de dar por terminado el código | pass (objetivo) |
| Behavioral reproducibility | Mismo input → mismo output y misma evidencia | pass (objetivo) |
| TASK-manifest validation | Manifest válido contra schema v5 | pass |

---

## 10. Security and data

- El verificador y el reporte solo leen el kit de salida y escriben
  `transform-reports/` — sin credenciales, sin red, sin entradas no
  confiables.
- `data_classification: internal` — sin PII ni secretos; el reporte no
  incluye contenido sensible más allá del kit transformado.
- La carpeta de evidencia puede contener el kit completo convertido en
  diffs: es material interno del repositorio.

## 11. Monitoring and observability

- `run.log` persistido por run (output completo del pipeline).
- Resumen en consola: hits de verificación (o "cero"), path de la carpeta de
  evidencia, exit code.
- `report.json` como fuente estructurada para análisis con IA posterior
  (AC-11).

## 12. Migration, compatibility and rollback

- **Migration:** N/A — producto nuevo.
- **Compatibility:** `transform-reports/` es aditivo por diseño: los runs
  previos nunca se tocan.
- **Rollback:** git (baseline `58ac5eb`); una corrida errónea se re-ejecuta
  (el borrado de salida garantiza árbol limpio; la evidencia previa queda).

## 13. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| Falsos positivos del verificador (términos legítimos) | 2 | 3 | Lista de excepciones (glossary §7) como datos + revisión de hits |
| E2E contra el kit real revela reglas faltantes | 3 | 3 | Extender `mapping.json` (datos, OQ-004) y re-ejecutar; el verificador lista los hits |
| Difs grandes por archivo | 2 | 2 | Diffs por archivo individual (difflib unified) |
| `transform-reports/` crece con los runs | 1 | 1 | Retención acotada (2 corridas por versión, `--keep-runs` configurable) — Revisión 2 |

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| Verificador con tokens exactos + variantes regex (no solo la lista exacta) | La lista del glossary §6 caza lo canónico; las variantes (case, plurales, URLs, copyright) cazan lo no contemplado — capas 1 y 4 de la detección |
| `difflib.unified_diff` para los diffs | Stdlib (ADR-001), formato estándar consumible por humanos e IA |
| `report.json` como estructura principal y `report.md` derivado | El JSON es la fuente para IA (AC-11); el MD es la lectura humana |
| Evidencia con retención acotada (2 corridas por versión) | R6 (Revisión 2): las 2 más recientes alcanzan para comparar runs; las purgadas se listan en el log — nada silencioso |
| Integración en `transform.py` (verificar + persistir al final del run real) | El proceso (PROC-001) define la secuencia: escribir → verificar → reportar; un solo comando produce el ciclo completo |
| E2E real con output temporal (no `distribution-kit/` del repo) | Los tests no dependen del estado del árbol de trabajo; la corrida de producción queda como demo/aceptación |

## 15. Stop conditions

- **Leftovers en el kit real que requieran reglas nuevas:** se extiende
  `mapping.json` (datos) y se re-ejecuta; si un leftover requiere decisión
  del propietario (remoción ambigua, contenido nuevo), se detiene y se
  consulta (OQ-004).
- **Decisión de arquitectura emergente:** fuera de ADR-001 → detener, ADR,
  re-aprobar SPEC (G15).
- **Fallo no reproducible:** detener y registrar el blocker en el MEM.

## 16. Definition of Done (DoD)

- [ ] All phases implemented (A, B, C)
- [ ] All acceptance criteria pass (AC-7, AC-8, AC-9, AC-11)
- [ ] Tests GREEN: suite completa (TASK-001 + TASK-002) — 0 failures
- [ ] Code follows ADR-001 (Python stdlib, `src/`, `mapping.json` raíz)
- [ ] Applicable gates pass / waived (ADR) / n/a (reason)
- [ ] MEM created in `metaflow/22-memory/` (exactly one per V-Bounce)
- [ ] Manifest `delivery_loops[]` entry appended in
      `metaflow/23-metrics/tasks/US-001.TASK-002-verificador-reporte.json`
- [ ] CP-MEM-Approval recorded

## 17. References

- `metaflow/12-functional/user-stories/US-001-toolkit-transformacion.md` (aprobada, Rev 4)
- `metaflow/12-functional/tasks/US-001.TASK-002-verificador-reporte.md` (aprobado)
- `metaflow/11-adrs/ADR-001-toolkit-transformacion.md` (accepted)
- `metaflow/21-spec/SPEC-260827-0124-bolt001-engine-transformacion.md` (rev 2, entregado)
- `metaflow/22-memory/MEM-260827-0140-bolt001-engine-transformacion.md` (approved)
- `metaflow/02-analysis/glossary/metaflow.md` (§6/§7), `metaflow/02-analysis/process/PROC-001-transformacion-kit.md` (Reglas 3/6/7), `metaflow/02-analysis/domain-model/entities/TransformRun.md`

## 18. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-27 | @eugenioserrano | Revision 1 — SPEC inicial de TASK-002 |
| 2026-08-27 | @eugenioserrano | **CP-SPEC-Approval** — `approved` por human:eugenioserrano (Dev-validator autoasignado), sin hallazgos |
| 2026-08-27 | @eugenioserrano | Revision 2 — retención acotada de evidencia: 2 corridas más recientes por versión en `transform-reports/`, purgas listadas en el log, `--keep-runs N` (G15 — solicitado por el propietario) |
| 2026-08-27 | @eugenioserrano | **CP-SPEC-Approval (Revisión 2)** — re-aprobado por human:eugenioserrano, sin hallazgos |

## 19. CP-SPEC-Approval

> **MetaFlow §2.4.1, §3.0.** Esta SPEC permanece en draft hasta que el
> Dev-validator (+ domain owners aplicables) registra `CP-SPEC-Approval`
> (bloque `review` del frontmatter). La aprobación del TASK autorizó la
> preparación de la SPEC; **la aprobación de la SPEC autoriza el code-run /
> V-Bounce**.

| Field | Value |
|-------|-------|
| **review.reviewers** | human:eugenioserrano (Dev-validator — rol autoasignado: no hay otro titular) |
| **review.decision** | **approved** (Revisión 2) |
| **review_ready_at** | `2026-08-27T01:42:33-03:00` |
| **review.started_at** | `2026-08-27T02:03:08-03:00` |
| **review.decided_at** | `2026-08-27T02:03:08-03:00` |
| **Findings** | Ninguno — re-aprobado sin comentarios |
