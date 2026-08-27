---
id: "SPEC-260827-0124"
title: "BOLT-001 — Engine de transformación y CLI (dry-run y ejecución real)"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved"
origin: "US-001"
bolt: "US-001.BOLT-001"
revision: 2
associated_adrs:
  - "devflow/adrs/ADR-001-toolkit-transformacion.md"
prerequisites: []
risk_class: "low"
autonomy_level: "L3"
turn_budget: 10
data_classification: "internal"
review_ready_at: "2026-08-27T01:24:39-03:00"
review:
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-27T01:37:26-03:00"
  decided_at: "2026-08-27T01:37:26-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Re-aprobación de la Revisión 2 (exclusiones: TEMPLATE-REPORT.html no se migra) por el propietario (Dev-validator autoasignado) sin hallazgos — 2026-08-27. Autoriza la ejecución del V-Bounce de BOLT-001 bajo la revisión 2"
---

# SPEC-260827-0124 — BOLT-001: Engine de transformación y CLI

| Field | Value |
|-------|-------|
| **Origin** | US-001 |
| **Bolt** | US-001.BOLT-001 |
| **ADRs** | [ADR-001](../adrs/ADR-001-toolkit-transformacion.md) |
| **Risk Class** | low |
| **Revision** | 1 |

---

## 1. Objective

Implementar el **engine de transformación y su CLI** del BOLT-001: el
programa Python que, leyendo el diccionario de reglas (`mapping.json`),
transforma el kit de AvengaDevFlow (`input-kit/`) en el kit de MetaFlow
(`distribution-kit/`) aplicando los cuatro tipos de reglas (`rename`,
`regex_rename`, `remove`, `path_rename`) en orden longest-first, con dos
modos de operación: **dry-run** (plan sin escribir ni borrar) y **ejecución
real** (borra el contenido previo de `distribution-kit/` — cero residuos — y
escribe el kit nuevo). Incluye la versión inicial de `mapping.json` derivada
del diccionario canónico (`glossary/metaflow.md`) y los tests unitarios del
engine.

**Si no se implementa:** no existe ninguna forma de producir el kit MetaFlow
— el producto del repositorio (O1/O2/O3 de la visión) depende enteramente de
este Bolt. Es la base sobre la que BOLT-002 agrega verificación y reporte.

## 2. Context

La necesidad viene de la US-001 (aprobada, 5 SP, revisada con AC-11/R6) y su
BOLT-001 (aprobado en `AITL-BOLT-READY-Approval`). El proceso de negocio
está definido en PROC-001 (activo): ingreso del kit → dry-run → plan →
ejecución real → verificación → reporte → revisión humana → publicación. Este
BOLT implementa los pasos hasta "escribir `distribution-kit/`" (la
verificación y el reporte son BOLT-002).

Restricciones gobernantes:
- **ADR-001 (accepted):** Python 3.10+ (local 3.12.10), **solo stdlib**
  (`pathlib`, `re`, `json`, `argparse`, `dataclasses`, `unittest`), código en
  `src/`, `mapping.json` en la raíz del repositorio, salida en
  `distribution-kit/`, tests con `unittest`.
- **Glossary `metaflow.md` (stable):** diccionario canónico — familias
  M1–M11 (marca), C1–C6 (checkpoints CP/CITL), B1–B16 (TASK), D1–D6
  (Delivery Loop), R1–R4 (remociones); regla de orden **longest-first**.
- **Domain-model (stable):** `MappingRule` (id, type, pattern, replacement,
  order, scope, report_on_match) y `RuleType` (rename | regex_rename | remove
  | path_rename); las reglas `path_rename` se aplican sobre el árbol ANTES
  del contenido.

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | `devflow/functional/bolts/US-001.BOLT-001-engine-transformacion.md` | AITL-BOLT-READY-Approval ✓ (2026-08-27) |
| Feature US | `devflow/functional/user-stories/US-001-toolkit-transformacion.md` | AITL-US-Approval ✓ (incl. Rev 4 — AC-10/R5, AC-11/R6) |
| ADRs | `devflow/adrs/ADR-001-toolkit-transformacion.md` | AITL-ADR-Approval ✓ (accepted) |
| Analysis | `devflow/analysis/glossary/metaflow.md`, `devflow/analysis/process/PROC-001-transformacion-kit.md`, `devflow/analysis/domain-model/entities/MappingRule.md`, `devflow/analysis/domain-model/enumerations/RuleType.md` | stable ✓ (validados por el propietario) |
| Open questions | — | 4/4 `answered` — G35 OK |
| Repository baseline | `58ac5eb` | — |

## 4. Scope

### In scope

- `mapping.json` (raíz): versión inicial del diccionario en formato de datos
  del engine, derivada 1:1 del glossary (reglas M, C, B, D, R con `order`
  longest-first por construcción y `report_on_match`), más la lista
  top-level `exclude` (archivos que **no se migran** — ver Phase B.4).
- `src/transform.py`: CLI (`argparse`) con `--dry-run` y ejecución real;
  carga y validación de `mapping.json`; aplicación de reglas de contenido
  (rename, regex_rename, remove) y de rutas (path_rename) en el orden
  correcto; borrado de `distribution-kit/` en modo real (ruta validada);
  **exclusión de archivos no migrados** (lista `exclude`, registrados en el
  run); escritura del árbol transformado; exit codes (0 éxito, 1 error,
  2 fallo detectado).
- `src/tests/`: tests unitarios del engine con `unittest` + fixtures pequeños
  (`src/tests/fixtures/`).

### Out of scope

- Verificador de tokens prohibidos → **BOLT-002**.
- Reporte de transformación, diffs y persistencia en `transform-reports/` →
  **BOLT-002** (AC-8, AC-11).
- Aceptación E2E contra el kit real → **BOLT-002** (AC-9).
- **Template HTML de reportes de MetaFlow** (branding propio) → entregable
  aparte, NO parte de BOLT-001 (el template de Avenga no se migra; se excluye
  del output — scope X6).
- Traducción, licencias, migración de la raíz → fuera del MVP (scope X1–X5).

## 5. Prerequisites and baseline

- Python 3.10+ disponible (verificado: 3.12.10 en la máquina del mantenedor).
- `input-kit/` presente en la raíz (kit AvengaDevFlow, solo lectura).
- `distribution-kit/` puede existir o no; el engine lo borra/recrea en modo
  real.
- Baseline del repositorio: commit `58ac5eb` (árbol de gobernanza intacto).

## 6. Phases

### Phase A — `mapping.json`: el diccionario como datos

**Duration:** 1h — **Complexity:** Low

#### A.1 Crear `mapping.json` desde el glossary

Se traduce el diccionario canónico (`glossary/metaflow.md` §1–§5) a un único
archivo JSON en la raíz con un array de reglas. Cada regla sigue la entidad
`MappingRule` del domain-model: `id` (M1…M11, C1…C6, B1…B16, D1…D6, R1…R4),
`type` (`rename` | `regex_rename` | `remove` | `path_rename`), `pattern`,
`replacement` (vacío/ausente para `remove`; N/A para `path_rename`), `order`
(1..N, longest-first por construcción: `AvengaDevFlow` antes de
`Avenga Dev Flow` antes de `Avenga`), `scope` (`content` | `path` | `both`),
`report_on_match` (siempre `true` para `remove`).

Además se incluye un bloque de metadatos con `version` de origen (glossary) y
la fecha de generación, y una lista top-level `exclude` con las rutas
relativas que el pipeline **no migra** (Phase B.4). El engine valida este
formato al cargar (Phase B).

**Files created:**
- `mapping.json` — Diccionario de transformación como datos (fuente: glossary
  `metaflow.md`; el engine lo lee sin tocar código — RULE-04 de MappingRule).

### Phase B — Engine y CLI (`src/transform.py`)

**Duration:** 3h — **Complexity:** Medium

#### B.1 Carga y validación del diccionario

`transform.py` lee `mapping.json` (ruta por defecto junto al proyecto, raíz
del repo) y lo valida: tipos conocidos, `order` presente y sin colisiones,
`replacement` requerido salvo `remove`. Un diccionario inválido es un error
de carga (exit 1) — nunca una transformación parcial.

#### B.2 Orden de aplicación y tipos de regla

- Reglas de **contenido** (rename, regex_rename, remove): se aplican sobre el
  texto de cada archivo en el **orden explícito del campo `order`** (que por
  construcción es longest-first; ADR-001 + PROC-001 Regla 1).
- `regex_rename`: patrón con grupo de captura y re-emisión, p. ej.
  `AITL-([A-Z-]+)-Approval` → `CP-$1-Approval` (C1 del glossary).
- `remove`: elimina el fragmento y **registra la remoción** en una lista en
  memoria (la consume el reporte de BOLT-002; AC-5 exige que nada sea
  silencioso — esta SPEC garantiza el registro, BOLT-002 lo persiste).
- Reglas de **rutas** (`path_rename`): se aplican sobre el árbol de rutas
  **antes** de transformar el contenido (nota de RuleType), incluyendo
  archivos y carpetas (M6–M9, B4/B5/B8/B9/B10/B16 del glossary).

#### B.3 Modo dry-run vs ejecución real

- `--dry-run`: recorre el plan completo (rutas nuevas, reglas por archivo,
  remociones) y lo imprime a stdout **sin escribir ni borrar nada** (AC-6).
- Ejecución real (sin flag): valida que la salida sea exactamente
  `distribution-kit` (ruta relativa a la raíz; ante cualquier otra ruta
  configurada inesperada, aborta), **borra el contenido completo de
  `distribution-kit/`** (AC-10/R5), aplica el plan y escribe el árbol nuevo.
- El texto se procesa como UTF-8; los archivos no textuales se copian tal
  cual (RULE-03 de InputKit: se esperan solo texto; si aparece un binario, se
  copia sin transformar y se anota en la salida).

#### B.4 Exclusiones — archivos que no se migran

El engine lee la lista `exclude` del mapping (rutas relativas al kit de
entrada). Cualquier archivo cuya ruta relativa coincida **se excluye del
transform**: no se transforma ni se copia a `distribution-kit/`, y la
exclusión se registra en la lista de exclusiones del run (misma regla que las
remociones: nada silencioso).

Uso inicial: `devflow/reports/TEMPLATE-REPORT.html` — el template HTML de
reportes trae branding de Avenga embebido en el CSS (colores de marca, logo,
título); un rename de texto no alcanza para migrarlo (glossary §7, scope X6).
El template nuevo de MetaFlow es un entregable aparte, fuera de este Bolt.

**Files created:**
- `src/transform.py` — CLI del pipeline (BOLT-001): carga de mapping, engine
  de reglas, exclusiones, dry-run/real, borrado y escritura del kit de salida.

### Phase C — Tests unitarios del engine

**Duration:** 1h — **Complexity:** Low

#### C.1 Suite `unittest` en `src/tests/`

Se escriben los tests ANTES de considerar el código terminado (test-first,
gate test-first-evidence) cubriendo:

- `test_mapping.py` — carga válida, diccionario inválido → error, orden
  longest-first (AvengaDevFlow → Avenga Dev Flow → Avenga).
- `test_rename.py` — renames exactos, variantes de caso, sin reemplazos
  parciales.
- `test_regex.py` — checkpoints C1/C2: `AITL-SPEC-Approval` →
  `CP-SPEC-Approval`, `HITL-MEM-Approval` → `CP-MEM-Approval`, códigos
  variables preservados.
- `test_remove.py` — remoción de citas (R1/R2) y registro de cada remoción.
- `test_path_rename.py` — rutas antes que contenido; archivos y carpetas
  (M6–M9).
- `test_cli.py` — dry-run no escribe ni borra; ejecución real borra
  `distribution-kit/` y escribe el kit; borrado validado (solo esa carpeta).
- `test_exclusions.py` — un archivo en la lista `exclude` del mapping no
  aparece en el output, no se transforma y queda registrado en la lista de
  exclusiones del run.

**Files created:**
- `src/tests/__init__.py` — Marca el paquete de tests.
- `src/tests/test_mapping.py`, `test_rename.py`, `test_regex.py`,
  `test_remove.py`, `test_path_rename.py`, `test_cli.py` — Suites unitarias.
- `src/tests/fixtures/` — Kit mini de entrada/salida esperada para los tests
  (fixture textual con ejemplos de los 4 tipos de regla).

---

## 7. Acceptance criteria

### AC-1: Transformación completa con versión − 4

**Given** un kit de AvengaDevFlow en `input-kit/`,
**When** se ejecuta `python src/transform.py`,
**Then** `distribution-kit/` contiene el kit transformado según el
diccionario (solo cambios de nombres) y la versión de salida se deriva de la
entrada − 4 (5.1 → 1.1).

### AC-2: Diccionario como datos

**Given** `mapping.json` con una regla nueva,
**When** se ejecuta el engine sin cambios de código,
**Then** la regla se aplica.

### AC-3: Orden longest-first

**Given** reglas `AvengaDevFlow`, `Avenga Dev Flow`, `Avenga`,
**When** se transforma un texto con las tres formas,
**Then** ninguna queda parcialmente transformada (el término más largo se
reemplaza primero).

### AC-4: Checkpoints con regex

**Given** `AITL-SPEC-Approval` y `HITL-MEM-Approval` en el contenido,
**When** se transforma,
**Then** quedan `CP-SPEC-Approval` y `CP-MEM-Approval`.

### AC-5: Remociones registradas

**Given** contenido marcado para remover (citas Raja SP / DORA),
**When** se transforma,
**Then** el contenido se elimina y la remoción queda registrada en la lista
en memoria del run (persistida por BOLT-002).

### AC-6: Dry-run sin efectos

**Given** un kit en `input-kit/`,
**When** se ejecuta `python src/transform.py --dry-run`,
**Then** se imprime el plan y no se escribe ni borra nada en
`distribution-kit/`.

### AC-10: Salida limpia en ejecución real

**Given** una ejecución real con contenido previo en `distribution-kit/`,
**When** comienza la transformación,
**Then** el contenido completo de `distribution-kit/` se borra antes de
escribir el kit nuevo (y solo esa carpeta).

### AC mapping to source (functional) / measurable outcome (non-functional)

| Source AC / outcome | How this SPEC satisfies it | Verifying test/evidence |
|---------------------|----------------------------|--------------------------|
| US AC-1 | Engine aplica el diccionario completo; versión −4 en la metadata de salida | `test_cli.py` + fixture E2E mini |
| US AC-2 | `mapping.json` como datos; carga sin código | `test_mapping.py` (regla nueva aplica) |
| US AC-3 | Orden explícito longest-first por construcción | `test_mapping.py`, `test_rename.py` |
| US AC-4 | `regex_rename` con captura y re-emisión | `test_regex.py` |
| US AC-5 | `remove` elimina y registra la remoción | `test_remove.py` |
| US AC-6 | Modo dry-run no escribe ni borra | `test_cli.py` |
| US AC-10 | Borrado completo y acotado de la salida en modo real | `test_cli.py` |

---

## 8. Testing strategy

- **Unit tests (~14 casos):** carga/validación de mapping (2), orden
  longest-first (2), renames exactos y variantes (2), regex de checkpoints
  (2), remociones + registro (2), path_rename antes que contenido (2), CLI
  dry-run/real + borrado (2).
- **Integration tests:** ninguno en esta SPEC (el engine es autocontenido;
  la integración real contra el kit es E2E de BOLT-002).
- **E2E tests:** fixture mini dentro de `src/tests/fixtures/` (kit de 4–6
  archivos con los 4 tipos de regla); la E2E contra el kit real es BOLT-002.
- **Edge cases:** archivo binario en el árbol (se copia sin transformar y se
  anota), rutas con espacios, encoding UTF-8, `distribution-kit/` inexistente
  (se crea), `distribution-kit/` con contenido previo (se borra), mapping
  inválido (error de carga, exit 1).
- **BUG evidence:** N/A (no es un BUG Bolt).

---

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | Suite `unittest` verde (`python -m unittest discover src/tests`) | pass (objetivo) |
| SAST / SBOM | Sin dependencias de terceros ni superficie de red | n/a — script local sin superficie atacable externa |
| Perf-smoke (p95/p99) | Pipeline completo < 1 min (NFR ADR-001) | n/a — medición del pipeline completo en BOLT-002 |
| Prompt-injection scan | No procesa prompts ni inputs externos | n/a — sin entrada no confiable |
| Secret-leak scan | Sin credenciales en el código | pass |
| Hallucination lint | Código verificado contra stdlib real de Python 3.10+ | pass |
| IP / license provenance | Cero dependencias; sin código de terceros | n/a — sin código de terceros |
| PII / DLP | No procesa datos personales | n/a — sin datos personales |
| Dependency-confusion | Cero dependencias instaladas | n/a — sin dependencias |
| Test-first evidence | Tests escritos antes de dar por terminado el código | pass (objetivo) |
| Behavioral reproducibility | Mismo input → mismo output (determinista) | pass (objetivo) |
| Bolt-manifest validation | Manifest válido contra schema v5 | pass |

---

## 10. Security and data

- El CLI no recibe credenciales, no abre sockets ni lee entradas no
  confiables: solo lee `input-kit/` y `mapping.json` (ambos del repo).
- **Borrado acotado:** la única operación destructiva es el borrado del
  contenido de `distribution-kit/`, validando que la ruta sea exactamente la
  carpeta de salida esperada antes de borrar; nunca en dry-run.
- `data_classification: internal` — código y datos internos del proyecto; sin
  PII ni secretos.

## 11. Monitoring and observability

- Salida de CLI estructurada y legible: resumen del plan (dry-run) o del run
  (real), conteos por regla y lista de remociones en stdout.
- Exit codes: `0` éxito, `1` error de ejecución/carga, `2` fallo detectado
  (p. ej. diccionario inválido).
- El log persistente (`run.log`) y el reporte estructurado llegan con
  BOLT-002 (AC-11).

## 12. Migration, compatibility and rollback

- **Migration:** N/A — producto nuevo, no hay datos que migrar.
- **Compatibility:** requiere Python 3.10+; cero dependencias externas.
- **Rollback:** el código vive en git (baseline `58ac5eb`); ante un
  `distribution-kit/` incorrecto se re-ejecuta el pipeline corregido
  (el borrado previo garantiza un árbol limpio).

## 13. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| Replace mal ordenado rompe texto (§4.1, números de versión) | 3 | 4 | Orden longest-first por construcción + tests de orden |
| Borrado destructivo de salida | 2 | 4 | Validación estricta de la ruta + dry-run siempre disponible |
| `mapping.json` inicial incompleto o divergente del glossary | 2 | 3 | Derivación 1:1 del glossary + tests con casos del diccionario |
| Rutas Windows (separadores, espacios, case) | 2 | 2 | `pathlib` para todas las operaciones de ruta |

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| `unittest` en vez de pytest | ADR-001: cero dependencias; la suite corre con la stdlib |
| Un solo `src/transform.py` (engine + CLI) | Simplicidad del MVP; BOLT-002 agrega `verify.py` y `report.py` sin acoplar |
| `mapping.json` en la raíz (no en `src/`) | ADR-001: datos separados del código, editables sin tocar el engine |
| Orden explícito `order` en cada regla (no solo por longitud) | Determinismo: el orden queda declarado y testeable |
| Archivos binarios se copian sin transformar | RULE-03 de InputKit (se esperan solo texto); se anota en la salida |
| Borrado del contenido (no de la carpeta) de `distribution-kit/` | La carpeta es el punto de salida fijo del repo; se vacía y recrea el árbol |
| Exclusiones como datos (`exclude` en `mapping.json`) | Misma filosofía que las reglas (datos, no código); el template HTML con branding embebido no se puede renombrar limpiamente — se excluye y se lista en el run (nada silencioso) |

## 15. Stop conditions

- **Diccionario divergente del glossary:** si una regla necesaria para los
  tests no tiene fuente en el glossary (o viceversa), se detiene y se resuelve
  con el propietario — nunca se inventa una regla.
- **Decisión de arquitectura emergente:** si el diseño del engine requiere
  una decisión fuera de la ADR-001, se detiene, se crea/actualiza la ADR y se
  re-aprueba la SPEC (G15).
- **Fallo no reproducible en tests:** si un test falla sin causa clara y no
  se resuelve dentro del turn budget, se detiene y se registra el blocker en
  el MEM.

## 16. Definition of Done (DoD)

- [ ] All phases implemented (A, B, C)
- [ ] All acceptance criteria pass (AC-1..6, AC-10)
- [ ] Tests GREEN: `python -m unittest discover src/tests` (unit, 0 failures)
- [ ] Code follows ADR-001 (Python stdlib, `src/`, `mapping.json` raíz)
- [ ] Applicable gates pass / waived (ADR) / n/a (reason)
- [ ] MEM created in `devflow/memory/` (exactly one per V-Bounce)
- [ ] Manifest `v_bounces[]` entry appended in
      `devflow/metrics/bolts/US-001.BOLT-001-engine-transformacion.json`
- [ ] AITL-MEM-Approval recorded

## 17. References

- `devflow/functional/user-stories/US-001-toolkit-transformacion.md` (aprobada, Rev 4)
- `devflow/functional/bolts/US-001.BOLT-001-engine-transformacion.md` (aprobado)
- `devflow/adrs/ADR-001-toolkit-transformacion.md` (accepted)
- `devflow/analysis/glossary/metaflow.md` (diccionario, stable)
- `devflow/analysis/process/PROC-001-transformacion-kit.md` (proceso, active)
- `devflow/analysis/domain-model/entities/MappingRule.md` y
  `devflow/analysis/domain-model/enumerations/RuleType.md` (modelo, stable)

## 18. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-27 | @eugenioserrano | Revision 1 — SPEC inicial de BOLT-001 |
| 2026-08-27 | @eugenioserrano | **AITL-SPEC-Approval** — `approved` por human:eugenioserrano (Dev-validator autoasignado), sin hallazgos |
| 2026-08-27 | @eugenioserrano | Revision 2 — exclusiones: `devflow/reports/TEMPLATE-REPORT.html` no se migra (branding embebido); lista `exclude` en `mapping.json`, Phase B.4, test_exclusions (G15 — solicitado por el propietario antes de ejecutar el V-Bounce) |
| 2026-08-27 | @eugenioserrano | **AITL-SPEC-Approval (Revisión 2)** — re-aprobado por human:eugenioserrano, sin hallazgos |

## 19. AITL-SPEC-Approval

> **Avenga DevFlow §2.4.1, §3.0.** Esta SPEC permanece en draft hasta que el
> Dev-validator (+ domain owners aplicables) registra `AITL-SPEC-Approval`
> (bloque `review` del frontmatter). La aprobación del Bolt autorizó la
> preparación de la SPEC; **la aprobación de la SPEC autoriza el code-run /
> V-Bounce**. Un cambio material en las fuentes invalida esta aprobación —
> detener, revisar, re-aprobar (G15).

| Field | Value |
|-------|-------|
| **review.reviewers** | human:eugenioserrano (Dev-validator — rol autoasignado: no hay otro titular) |
| **review.decision** | **approved** (Revisión 2) |
| **review_ready_at** | `2026-08-27T01:24:39-03:00` |
| **review.started_at** | `2026-08-27T01:37:26-03:00` |
| **review.decided_at** | `2026-08-27T01:37:26-03:00` |
| **Findings** | Ninguno — re-aprobado sin comentarios |
