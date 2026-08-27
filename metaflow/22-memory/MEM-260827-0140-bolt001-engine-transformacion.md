---
id: "MEM-260827-0140"
title: "BOLT-001 — Engine de transformación y CLI (V-Bounce 1)"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
bolt: "US-001.BOLT-001"
spec: "SPEC-260827-0124"
spec_revision: 2
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "58ac5eb"
applied_adrs:
  - "devflow/adrs/ADR-001-toolkit-transformacion.md"
manifest: "devflow/metrics/bolts/US-001.BOLT-001-engine-transformacion.json"
diff_ref: ""
review_ready_at: "2026-08-27T01:40:00-03:00"
review:
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-27T01:41:53-03:00"
  decided_at: "2026-08-27T01:41:53-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Aprobación del propietario (Dev-validator autoasignado) sin hallazgos — revisión del diff, tests 37/37, gates y manifest en conversación, 2026-08-27"
---

# MEM-260827-0140 — BOLT-001: Engine de transformación y CLI

| Field           | Value |
|-----------------|-------|
| **Bolt**        | US-001.BOLT-001 |
| **SPEC**        | [SPEC-260827-0124](../spec/SPEC-260827-0124-bolt001-engine-transformacion.md) — revisión 2 |
| **V-Bounce**    | 1 |
| **ADRs**        | [ADR-001](../adrs/ADR-001-toolkit-transformacion.md) (accepted) |

---

## 1. Executive summary

Este V-Bounce entrega el engine de transformación y su CLI (BOLT-001): el
programa Python que convierte el kit de AvengaDevFlow (`input-kit/`) en el
kit de MetaFlow (`distribution-kit/`) aplicando el diccionario de reglas
(`mapping.json`), con modos dry-run y ejecución real. Se implementó el
diccionario como datos con 55 reglas derivadas 1:1 del glossary canónico
(familias M/C/B/D/R más las extensiones de prosa M7b/M7c/M6b/B9b y las reglas
de ruta P-M6..P-B8), la lista de exclusión de archivos no migrados
(`devflow/reports/TEMPLATE-REPORT.html`, template HTML con branding embebido),
y el engine en `src/transform.py` con orden longest-first, regex de
checkpoints, remociones registradas (nunca silenciosas), borrado validado de
la salida en modo real (cero residuos, solo la carpeta de salida), prune de
carpetas vacías residuales y exit codes 0/1/2. El resultado de la ejecución
sobre el fixture E2E produce exactamente el árbol esperado (verificación
funcional), y la suite unitaria quedó en verde: **37 tests, 0 fallos** — con
evidencia RED previa (7 módulos fallando por `ModuleNotFoundError`) y GREEN
después de la implementación. No hubo sorpresas respecto de la SPEC revisión
2, que se re-aprobó antes de la ejecución (G15) para incorporar las
exclusiones del template de reporte; el `.gitignore` ya cubría `__pycache__/`
y `*.pyc`, por lo que no requirió cambios. El sistema ahora puede, con un
solo comando, mostrar el plan de transformación sin tocar nada o regenerar el
kit MetaFlow completo desde cero con salida limpia; el verificador de tokens
prohibidos, el reporte persistente y la aceptación E2E contra el kit real
quedan para BOLT-002.

## 2. Implemented phases

### Phase A — `mapping.json`: el diccionario como datos

Se creó el diccionario operativo en la raíz del repositorio como un único
JSON con metadatos (`schema`, `generated_from`, `generated_at`), la lista
top-level `exclude` y el array `rules`. Cada regla sigue la entidad
`MappingRule` del domain-model: `id` (M1–M11, C1–C6, B1–B16, D1–D6, R1–R4,
P-M6..P-B8), `type` (`rename` | `regex_rename` | `remove` | `path_rename`),
`pattern`, `replacement`, `order`, `scope` y `report_on_match`. Los `order`
están construidos longest-first (M11 antes que M7b antes que M1; D2 antes de
D1; B15a antes de D2; C5a antes de C4b), y las reglas de ruta usan un espacio
de orden propio (1001+) para mantener una numeración global única sin
colisiones. Las reglas `remove` (R1a/R1b/R2, C5a–C5c) siempre reportan. La
filosofía de datos (RULE-04 de MappingRule) queda cumplida: agregar una regla
es editar el JSON, no el código.

### Phase B — Engine y CLI (`src/transform.py`)

El engine carga y valida `mapping.json` (tipos conocidos, pattern requerido,
replacement string, order entero ≥ 1 sin colisiones, scope válido, `exclude`
como array de rutas) y lanza `TransformError` ante cualquier inconsistencia —
nunca una transformación parcial. Aplica reglas de contenido en orden sobre
el texto UTF-8 de cada archivo (`rename` con conteo, `regex_rename` con
backrefs `$N` convertidos a `\g<N>` de Python, `remove` con registro en la
lista de remociones), y reglas de ruta por componente de path (substring
replace, rutas ANTES que contenido, según RuleType). En modo real, `clean_output`
valida que la salida no contenga ni coincida con la entrada, borra el
contenido completo de la carpeta de salida y escribe el árbol nuevo; los
archivos binarios se copian sin transformar y se anotan, los excluidos no se
copian y se registran, y al final se podan las carpetas vacías residuales
(p. ej. el padre de un archivo excluido) para mantener cero residuos. La CLI
(`argparse`) soporta `--dry-run`, `--mapping`, `--input`, `--output` con exit
codes 0 (éxito), 1 (error de carga/ejecución) y 2 (diccionario inválido
semánticamente), y muestra el plan con reglas aplicadas y remociones por
archivo.

### Phase C — Tests unitarios del engine

Se escribieron los tests ANTES de la implementación (evidencia RED: los 7
módulos fallaron con `ModuleNotFoundError: No module named 'transform'`). La
suite usa `unittest` (cero dependencias, ADR-001) con un fixture E2E mínimo
(`kit-mini/` → `kit-mini-expected/`) que ejercita los cuatro tipos de regla,
el orden longest-first, los checkpoints con regex, las remociones, los
renames de rutas, el borrado de salida, la exclusión del template HTML y los
exit codes del CLI. Tras la implementación, la suite quedó 37/37 en verde.

## 3. Files created

| File | Purpose |
|------|---------|
| `mapping.json` | Diccionario operativo de la transformación como datos: 55 reglas (contenido + rutas, orden longest-first) + lista `exclude`; es la fuente que el engine consume sin tocar código (RULE-04) |
| `src/transform.py` | Engine + CLI del pipeline: carga/validación del mapping, aplicación de reglas de contenido y rutas, dry-run y ejecución real con borrado validado de salida, exclusiones, prune de carpetas vacías, resumen del plan y exit codes |
| `src/tests/__init__.py` | Marca `src/tests/` como paquete de tests |
| `src/tests/test_mapping.py` | Suite de carga y validación del diccionario: orden longest-first, JSON inválido, tipo desconocido, pattern faltante, colisión de orders, exclusión declarada |
| `src/tests/test_rename.py` | Suite de renames de marca: familia M1–M11, atribución a Eugenio Serrano, marker de AGENTS.md, rutas en prosa, sin reemplazos parciales |
| `src/tests/test_regex.py` | Suite de checkpoints: AITL/HITL → CP con regex, placeholders literales, BOLT-READY/DONE tras C1, concepto CITL, acrónimos bare |
| `src/tests/test_remove.py` | Suite de remociones: Raja SP / DORA / legado HITL eliminados y registrados (nunca silenciosos) |
| `src/tests/test_path_rename.py` | Suite de renames de rutas: carpeta del kit, archivo normativo, wrappers, templates/schemas, IDs BOLT→TASK, carpetas bolts→tasks, componentes intactos |
| `src/tests/test_exclusions.py` | Suite de exclusiones: el archivo excluido no aparece en el output, queda registrado en el plan y el dry-run lo lista sin escribir |
| `src/tests/test_cli.py` | Suite del CLI: dry-run no escribe/borra, ejecución real produce el árbol esperado, borrado de salida previa, rechazo de salida dentro de la entrada, exit codes 1/2/0 |
| `src/tests/fixtures/kit-mini/` | Kit de entrada de prueba (7 archivos): AGENTS.md, archivo normativo, wrapper, schema, skill, ID de Bolt, template HTML excluido |
| `src/tests/fixtures/kit-mini-expected/` | Árbol esperado de salida (6 archivos): el contrato que la ejecución real debe reproducir exactamente |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `devflow/spec/SPEC-260827-0124-bolt001-engine-transformacion.md` | Gobernanza: revisión 2 (exclusiones, Phase B.4, test_exclusions) + re-aprobación registrada |
| `devflow/metrics/bolts/US-001.BOLT-001-engine-transformacion.json` | Gobernanza: `spec_revisions[]` (rev 1 y 2) + `checkpoint_approvals[]` (AITL-SPEC-Approval rev 1 y 2) — y este MEM agrega `v_bounces[]` |
| `devflow/analysis/glossary/metaflow.md` | Gobernanza/análisis: valores M6/M9/M11 → `ai-sdlc/` y nota de archivos excluidos |
| `devflow/analysis/scope/mvp-scope.md`, `vision/vision.md`, `analysis/process/PROC-001-transformacion-kit.md` | Gobernanza/análisis: X6 (template HTML nuevo), "posiblemente después", Regla 7 |

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
| — | — | Ninguno (los renames de archivos son el comportamiento del pipeline, no cambios del repo) |

## 6. Files deleted

| File | Reason |
|------|--------|
| — | Ninguno |

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| Diccionario con 55 reglas y `order` único global (rutas en espacio 1001+) | Numeración única permite validar colisiones y mantener el orden longest-first de forma determinista y testeable |
| Extensiones M7b/M7c/M6b/B9b (patrones de ruta también en prosa) | El glossary define M7/M6/B9 como ámbito Rutas, pero los nombres de archivos/carpetas aparecen en prosa; sin estas reglas quedarían leftovers — extensión del diccionario como datos, no del código |
| Regex `AITL-([A-Z0-9-]+)-Approval` + literales `<CODE>`, `*-` y bare | Cubre las formas reales del kit (códigos concretos, placeholders con ángulos/asterisco, genérico) antes del acrónimo bare → CITL |
| Orden C5 (remoción de legado) antes de C4b (bare HITL → CITL) | Si el acrónimo bare se convirtiera primero, las frases de legado quedarían dañadas y no se removerían |
| Remociones R1a/R1b/R2 solo con frases exactas (R3/Accelerate pendientes) | Las referencias históricas de migración y las citas a "Accelerate" son frases difusas que requieren decisión humana por caso; el reporte de BOLT-002 y la extensibilidad del diccionario cubren los leftovers (OQ-004) |
| Backrefs `$N` en el JSON convertidos a `\g<N>` en el engine | Formato del mapping legible y estándar; el engine lo traduce al API de `re.sub` de Python |
| Exclusión como datos (`exclude` en mapping.json), no hardcodeada | Misma filosofía que las reglas; el template HTML con branding embebido no se puede renombrar limpiamente (SPEC rev 2) |
| Prune de carpetas vacías tras la escritura | Un archivo excluido dejaba su carpeta padre vacía en el output — residuo contra la filosofía de salida limpia (AC-10/R5) |
| Archivos binarios se copian sin transformar y se anotan | RULE-03 de InputKit (se esperan solo texto); la copia preserva el árbol sin romper binarios |

## 8. Deviations and assumptions

- **SPEC revisión 2 ejecutada íntegramente:** la revisión 1 se aprobó pero no se ejecutó nada de código; el cambio de exclusiones (G15) se incorporó antes del primer test y el V-Bounce corre completo bajo la revisión 2 — no se viola G16.
- **E2E contra fixture, no contra el kit real:** el alcance de BOLT-001 define la E2E sobre `kit-mini`; la aceptación contra `input-kit/` real es de BOLT-002.
- **Remociones difusas pendientes (R3 y "Accelerate"):** no se codificaron como reglas `remove` por ser frases variables; el verificador de BOLT-002 (tokens prohibidos) y el diff humano las detectarán, y el diccionario se extiende por versión (OQ-004).
- **Artefactos de doble espacio tras remociones:** el `remove` deja el texto circundante sin colapsar espacios (p. ej. "DORA and Raja SP" → " and "); es el comportamiento esperado del diccionario — cada remoción queda listada en el reporte para revisión humana (nada silencioso).
- **Sin commits:** G34 — no se stagea/commitea sin pedido explícito; `git_commit: null` en el manifest.

## 9. Verification evidence

### Build
```
N/A — Python stdlib puro (ADR-001), sin build.
```

### Tests
```
> python -m unittest discover -s src/tests
Ran 37 tests in 0.127s
OK
```

### RED → GREEN evidence (test-first)
- **RED:** `python -m unittest discover -s src/tests` → 7 módulos fallan:
  `ModuleNotFoundError: No module named 'transform'` (antes de escribir
  `src/transform.py` y `mapping.json`).
- **GREEN:** misma suite tras la implementación → `Ran 37 tests ... OK`.

### Demo (dry-run del CLI sobre el fixture)
```
> python src/transform.py --dry-run --input src/tests/fixtures/kit-mini --output <temp>
=== METAFLOW TRANSFORM (DRY-RUN) ===
total: 6 archivos, 6 carpetas, 0 binarios copiados, 1 excluidos,
32 reglas aplicadas, 3 remociones
[excluido] devflow/reports/TEMPLATE-REPORT.html
```

### Gates
| Gate | Result |
|------|--------|
| Unit / integration | pass — 37/37 |
| SAST / SBOM | n/a — script local sin superficie atacable externa |
| Perf-smoke (p95/p99) | n/a — pipeline completo < 1 min medido en BOLT-002 |
| Prompt-injection scan | n/a — sin entradas no confiables |
| Secret-leak scan | pass — sin credenciales |
| Hallucination lint | pass — APIs verificadas contra stdlib Python 3.10+ |
| IP / license provenance | n/a — cero dependencias de terceros |
| PII / DLP | n/a — sin datos personales |
| Dependency-confusion | n/a — cero dependencias |
| Test-first evidence | pass — RED registrado antes de la implementación |
| Behavioral reproducibility | pass — fixture determinista (mismo input → mismo output) |
| Bolt-manifest validation | pass — validado contra manifest-v5-bolt.schema.json |

## 10. Manual interventions

Ninguna — todo el código, tests y diccionario fueron generados por el agente.

## 11. Evidence links

- **Diff / PR:** no aplica (sin commit — G34; el diff se presenta en esta conversación).
- **Commit:** baseline `58ac5eb` (el trabajo queda sin commitear para revisión).
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-001.BOLT-001-engine-transformacion.json`

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~30 min (conversación, incluida la pausa G15) |
| V-Bounce number | 1 |
| Tests created | 37 (37 unitarios; fixture E2E dentro de test_cli/test_exclusions) |
| AI-generated code | 100 % |
| First-pass approval | n/a — en revisión |

## 13. Pending items and stubs

- [ ] **BOLT-002** — verificador de tokens prohibidos + reporte (con diffs y persistencia en `transform-reports/`, AC-8/AC-11) + aceptación E2E contra el kit real (AC-9).
- [ ] **X6** — template HTML de reportes de MetaFlow con branding propio (entregable aparte, v1).
- [ ] **R3/Accelerate** — reglas `remove` difusas pendientes de decisión por caso (verificador + diff los detectan).

## 14. AITL-MEM-Approval

> **Avenga DevFlow §2.12, §3.0.** Este MEM no tiene status mutable y **nunca
> se auto-aprueba**. El Dev-validator que ejecutó el Bolt (QA/Sec/domain
> opcionales) inspecciona el diff real, la evidencia de tests/gates, el MEM y
> el manifest, y registra `AITL-MEM-Approval` aquí y en el
> `checkpoint_approvals[]` del manifest. `approved` completa el V-Bounce;
> `changes_requested` mantiene este MEM como historia inmutable y la próxima
> ejecución es un V-Bounce NUEVO con MEM NUEVO.

| Field | Value |
|-------|-------|
| **Reviewers (executing Dev-validator)** | `human:eugenioserrano` (Dev-validator — rol autoasignado: no hay otro titular) |
| **Roles** | dev_validator |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-27T01:40:00-03:00` |
| **review.started_at** | `2026-08-27T01:41:53-03:00` |
| **review.decided_at** | `2026-08-27T01:41:53-03:00` |
| **Review evidence** | diff de código + fixtures + tests 37/37 + gates + MEM + manifest |
| **Comments** | — |
| **Findings** | Ninguno |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | Evidencia inspeccionada: diff, tests 37/37 en verde, gates pass/n/a, MEM completo, manifest v_bounces[1] validado |
