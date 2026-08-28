---
id: "MEM-260828-0107"
title: "Traslado de mapping.json a src/ — toolkit autocontenido"
date: "2026-08-28"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
task: "US-000.TASK-001"
spec: "SPEC-260828-0103"
spec_revision: 1
delivery_loop: 1
execution_outcome: "ready_for_review"
baseline: "c531de2"
applied_adrs:
  - "metaflow/11-adrs/ADR-004-ubicacion-mapping-json.md"
manifest: "metaflow/23-metrics/tasks/US-000.TASK-001-ubicacion-mapping-json.json"
diff_ref: ""
review_ready_at: "2026-08-28T01:07:51-03:00"
review: # CP-MEM-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-28T01:12:00-03:00"
  decided_at: "2026-08-28T01:13:29-03:00"
  findings: []
  acknowledged_without_comment: true # must be true when findings is empty (§3.0)
  acknowledgment_reason: "Aprobación del propietario (Dev-validator ejecutor, autoasignado) sin hallazgos — revisó diff, 107 tests OK y la transformación real desde cero (kit regenerado byte-idéntico), 2026-08-28"
---

# MEM-260828-0107 — Traslado de `mapping.json` a `src/`

| Field           | Value |
|-----------------|-------|
| **TASK**        | US-000.TASK-001 |
| **SPEC**        | [SPEC-260828-0103](../21-spec/SPEC-260828-0103-ubicacion-mapping-json.md) rev 1 |
| **Delivery Loop**    | 1 |
| **ADRs**        | [ADR-004](../11-adrs/ADR-004-ubicacion-mapping-json.md) |

---

## 1. Executive summary

Este Delivery Loop trasladó el diccionario de transformación `mapping.json`
de la raíz del repositorio a `src/mapping.json`, ejecutando el ADR-004
aprobado: el toolkit de transformación queda ahora autocontenido en `src/`
(engine, verificador, reporte, diccionario y tests), y la raíz del repo queda
reservada a los dos kits (`input-kit/`, `distribution-kit/`) y los metadatos
del repositorio. El engine (`src/transform.py`) carga el diccionario por
default con una ruta relativa al módulo — el pipeline sigue invocándose
igual (`python src/transform.py`) desde cualquier directorio, y el flag
`--mapping` conserva su semántica de override. Los 13 archivos de tests que
referenciaban el diccionario en la raíz (`parents[2]`) se actualizaron a la
nueva ubicación (`parents[1]`), y la documentación viva (README de la raíz y
sección de proyecto de `AGENTS.md`) refleja el nuevo layout; los artefactos
históricos (MEMs, SPECs, ADRs, US, BUGs, REVs) no se tocaron (G36). El
resultado: la suite completa de 107 tests pasó sin regresiones (incluido el
E2E que regenera el kit real y verifica tokens prohibidos), el dry-run con el
default nuevo genera el plan completo de 149 archivos, y la verificación de
restos (grep de la ubicación antigua en código y docs vivas) no encontró
ninguno. No hubo desviaciones ni sorpresas respecto de la SPEC.

## 2. Implemented phases

### Phase A — Traslado del diccionario y del engine

Se ejecutó `git mv mapping.json src/mapping.json`, registrando el movimiento
como rename (historia del archivo preservada, diff legible, contenido intacto
— las 55 reglas y la lista `exclude` no cambiaron, RULE-04). En
`src/transform.py` el default `DEFAULT_MAPPING` pasó de `REPO_ROOT /
"mapping.json"` (raíz del repo) a `Path(__file__).resolve().parent /
"mapping.json"` — ruta relativa al módulo que hace al toolkit portable desde
cualquier cwd (ADR-001) y desacoplado de la raíz (ADR-004). El texto de ayuda
del CLI `--mapping` se actualizó a la nueva ubicación por defecto
(`default: src/mapping.json`); `REPO_ROOT` se mantiene porque sigue
alimentando los defaults de `input-kit/`, `distribution-kit/` y
`transform-reports/`.

### Phase B — Tests: rutas del diccionario

Los 13 archivos de tests que referenciaban el diccionario desde la raíz se
actualizaron: los 12 que usaban `Path(__file__).resolve().parents[2] /
"mapping.json"` pasaron a `parents[1]`, y `test_reproducibilidad.py` (que
definía `MAPPING = ROOT / "mapping.json"`) ahora calcula la ruta con
`parents[1]`, conservando `ROOT` únicamente para `input-kit/`. Las
referencias `parents[2]` que apuntan a `input-kit/`, `distribution-kit/` o
`ROOT` (test_e2e, test_links, test_numbering, test_version, test_front_door,
test_linaje, test_restos_v5) se dejaron intactas porque siguen siendo
correctas. La suite completa corre en verde y su E2E valida que el pipeline
regenera el kit con el mismo contenido y sin tokens prohibidos
(reproducibilidad de comportamiento, AC-4).

### Phase C — Documentación viva

Se actualizaron las dos referencias vivas que mencionaban la ubicación del
diccionario como `src/ + mapping.json`: `README.md` de la raíz (la regla de
las dos particiones describe ahora el pipeline como "(`src/` — engine,
`mapping.json` dictionary and tests)") y la sección de proyecto de
`AGENTS.md` (misma frase en el contrato de las dos particiones). PROC-001,
la introducción y el glossary se revisaron y son location-neutral (describen
el diccionario como datos, sin afirmar dónde vive) — no requirieron cambios.
Los artefactos históricos no se tocaron.

## 3. Files created

| File | Purpose |
|------|---------|
| `metaflow/11-adrs/ADR-004-ubicacion-mapping-json.md` | ADR aprobado que gobierna este cambio (supercede parcialmente al ADR-001 en la ubicación del diccionario) — creado en el ciclo de este TASK |
| `metaflow/12-functional/tasks/US-000.TASK-001-ubicacion-mapping-json.md` | TASK no-funcional aprobado que define el WHAT y la evidencia de completitud |
| `metaflow/21-spec/SPEC-260828-0103-ubicacion-mapping-json.md` | SPEC aprobada (revisión 1) que planificó el traslado en tres fases |
| `metaflow/23-metrics/tasks/US-000.TASK-001-ubicacion-mapping-json.json` | Manifest del TASK (validado contra `manifest-v1-task.schema.json`) con los checkpoints y esta entrada de Delivery Loop |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `src/transform.py` | `DEFAULT_MAPPING` ahora es relativo al módulo (`src/mapping.json`) en vez de la raíz del repo; texto de ayuda de `--mapping` actualizado al nuevo default |
| `src/tests/test_cli.py`, `test_e2e.py`, `test_exclusions.py`, `test_links.py`, `test_mapping.py`, `test_numbering.py`, `test_path_rename.py`, `test_regex.py`, `test_remove.py`, `test_rename.py`, `test_report.py`, `test_version.py` | Ruta del diccionario actualizada de `parents[2] / "mapping.json"` a `parents[1] / "mapping.json"` (una línea por archivo) |
| `src/tests/test_reproducibilidad.py` | `MAPPING` pasa de `ROOT / "mapping.json"` a `parents[1] / "mapping.json"`; `ROOT` se conserva para `input-kit/` |
| `README.md` (raíz) | La regla de las dos particiones describe el pipeline como autocontenido en `src/` (engine, `mapping.json` y tests) |
| `AGENTS.md` (sección de proyecto) | Misma actualización en el contrato de las dos particiones |

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
| `mapping.json` | `src/mapping.json` | Traslado del diccionario al toolkit autocontenido (ADR-004); `git mv` preserva la historia |

## 6. Files deleted

| File | Reason |
|------|--------|
| — | Ninguno — el movimiento fue un rename, sin borrados |

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| Default relativo al módulo (`Path(__file__).resolve().parent`) en vez de ruta absoluta al repo | Portability (ADR-001): el toolkit corre desde cualquier cwd sin depender de la raíz; `--mapping` conserva el override para fixtures y casos alternativos |
| Actualizar los 13 tests in-place (una línea cada uno) en vez de introducir un helper/conftest de rutas | Cambio mínimo y explícito para un movimiento mecánico; la suite existente es el oráculo; sin abstracciones nuevas |
| `git mv` (rename con historia) en vez de borrar+crear | Preserva la historia del archivo y mantiene el diff legible |
| No regenerar `distribution-kit/` en este loop | El kit es producto del pipeline; su regeneración con evidencia pertenece al proceso de publicación (PROC-001), no al refactor de ubicación |
| PROC-001 / introducción / glossary sin cambios | Revisados y location-neutral: describen el diccionario como datos sin afirmar su ubicación; tocarlos habría sido ruido |

## 8. Deviations and assumptions

Sin desviaciones respecto de la SPEC aprobada (revisión 1). Se asumió que
las referencias de `parents[2]` a `input-kit/`, `distribution-kit/` y `ROOT`
en los tests siguen siendo correctas tras el traslado — verificado por la
suite en verde (el E2E corre el pipeline real contra `input-kit/`).

## 9. Verification evidence

### Build
```
Sin build — Python 3.12 + stdlib únicamente (ADR-001); sin dependencias.
```

### Tests
```
python -m unittest discover -s src/tests -p "test_*.py"
Ran 107 tests in 16.200s
OK
```

### Dry-run (AC-2, default = src/mapping.json)
```
python src/transform.py --dry-run
[plan completo] ... total: 149 archivos, 66 carpetas, 0 binarios copiados,
1 excluidos, 7576 reglas aplicadas, 26 remociones
```

### ACs verificadas
- AC-1: `src/mapping.json` existe; no existe `mapping.json` en la raíz ✓
- AC-2: dry-run con default carga el diccionario desde `src/` ✓
- AC-3: suite completa verde (107 tests, 0 fallos) ✓
- AC-4: E2E regenera el kit en temp con el mismo contenido y verificador OK ✓
- AC-5: grep de restos de la ubicación antigua en `src/` y docs vivas: vacío ✓
- AC-6: `git status` no muestra cambios en MEMs/SPECs/ADRs/US/BUGs/REVs ✓

### Gates
| Gate | Status |
|------|--------|
| Unit / integration (suite completa) | pass |
| Secret-leak scan (diff sin secretos) | pass |
| Hallucination lint (docs vivas coherentes) | pass |
| Behavioral reproducibility (E2E) | pass |
| TASK-manifest validation | pass |
| SAST/DAST, perf-smoke, prompt-injection, IP/license, PII/DLP, dependency-confusion, test-first-evidence | n/a (razones en SPEC §9: CLI local, stdlib, sin superficie externa, refactor no-BUG) |

## 10. Manual interventions

None — todo el cambio fue generado y verificado por el agente dentro del
Delivery Loop.

## 11. Evidence links

- **Diff / PR:** working tree (sin commit todavía — pendiente de `CP-MEM-Approval`)
- **Commit baseline:** `c531de2`
- **Cumulative TASK manifest:** `metaflow/23-metrics/tasks/US-000.TASK-001-ubicacion-mapping-json.json`

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~1h ciclo total (sesión 01:00–01:07) |
| Delivery Loop number | 1 |
| Tests created | 0 (13 tests existentes modificados en 1 línea cada uno) |
| AI-generated code | 100% |
| First-pass approval | pendiente de revisión humana |

## 13. Pending items and stubs

- [ ] Commit del paquete tras `CP-MEM-Approval` (G34: solo con orden explícita)
- [ ] `CP-TASK-DONE-Approval` (aceptación, Tech Lead — routing `refactor`)
- [ ] Fuera de scope: regeneración de `distribution-kit/` con evidencia (PROC-001)

---

## 14. CP-MEM-Approval

> **MetaFlow §2.12, §3.0.** This MEM is created by the agent with no
> mutable status and is **never self-approved**. A qualified human (the
> Dev-validator who executed the TASK; QA/Sec/domain reviewers optional, any risk)
> inspects the actual diff, test/gate evidence, MEM and manifest, and
> records `CP-MEM-Approval` here and in the manifest's
> `checkpoint_approvals[]`. `approved` completes the Delivery Loop (and, if latest,
> marks the TASK `Development Completed`); `changes_requested` keeps this
> MEM as immutable history and the next execution is a NEW Delivery Loop with a
> NEW MEM. `CP-TASK-DONE-Approval` is still required for `Done`.

| Field | Value |
|-------|-------|
| **Reviewers (executing Dev-validator; QA/Sec/domain optional)** | `human:eugenioserrano` |
| **Roles** | dev_validator |
| **Decision** | approved |
| **review_ready_at** | `2026-08-28T01:07:51-03:00` |
| **review.started_at** | `2026-08-28T01:12:00-03:00` |
| **review.decided_at** | `2026-08-28T01:13:29-03:00` |
| **Review evidence** | diff completo, 107 tests OK, transformación real desde cero (kit regenerado byte-idéntico) |
| **Comments** | None |
| **Findings** | None |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | Evidence inspected: diff + tests + run real (2026-08-28) |
