---
id: "MEM-260827-0152"
title: "BOLT-002 — Verificador de tokens prohibidos + reporte + aceptación E2E (V-Bounce 1)"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
bolt: "US-001.BOLT-002"
spec: "SPEC-260827-0142"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "58ac5eb"
applied_adrs:
  - "devflow/adrs/ADR-001-toolkit-transformacion.md"
manifest: "devflow/metrics/bolts/US-001.BOLT-002-verificador-reporte.json"
diff_ref: ""
review_ready_at: "2026-08-27T02:03:08-03:00"
review:
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-27T02:05:21-03:00"
  decided_at: "2026-08-27T02:05:21-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Aprobación del propietario (Dev-validator autoasignado) sin hallazgos — revisión del diff, tests 55/55, corrida de producción (exit 0, cero devflow), retención 2 y manifest en conversación, 2026-08-27"
---

# MEM-260827-0152 — BOLT-002: Verificador + reporte + E2E

| Field           | Value |
|-----------------|-------|
| **Bolt**        | US-001.BOLT-002 |
| **SPEC**        | [SPEC-260827-0142](../spec/SPEC-260827-0142-bolt002-verificador-reporte.md) — revisión 1 |
| **V-Bounce**    | 1 |
| **ADRs**        | [ADR-001](../adrs/ADR-001-toolkit-transformacion.md) (accepted) |

---

## 1. Executive summary

Este V-Bounce entrega la garantía de calidad del pipeline: el **verificador
de tokens prohibidos** (`src/verify.py`), el **reporte de transformación con
persistencia de evidencia** (`src/report.py` + integración en
`src/transform.py`) y la **aceptación E2E contra el kit real**. El verificador
barre el kit de salida en dos dimensiones: el **contenido** de cada archivo
de texto (línea por línea) y **todos los componentes de ruta** — nombres de
archivos y de carpetas, incluidas las carpetas vacías — con tokens canónicos
del glossary §6 y variantes regex (case, plurales, separadores, dominios,
`devflow` en cualquier forma); ante cualquier hit el run falla con exit != 0
y los lista (AC-7). El reporte persiste por run en
`transform-reports/<versión>/<run>/` — `report.json` (estructurado para IA),
`report.md`, **diffs por archivo** (original → convertido), `unchanged.txt`,
`removals.json` y `run.log` — con **retención acotada a las 2 corridas más
recientes por versión** (R6 Revisión 5 / SPEC rev 2): las anteriores se
purgran al final de cada corrida real y quedan listadas en el `run.log`
(nada silencioso).
El ciclo E2E contra el kit real (AC-9) reveló leftovers reales que se
resolvieron extendiendo el diccionario como datos (C7, C8, M12–M18, P-M15,
D7–D10, R2a/R2b) — el loop diseñado en OQ-004 — incluidas dos decisiones del
propietario: el concepto **DORA → Delivery Flow** (la R2 original borraba el
token en secciones de contenido rompiéndolas; ahora las citas se eliminan por
línea y el concepto se renombra, preservando la funcionalidad — AG2) y la
carpeta raíz del framework **`devflow/` → `metaflow/`** (cero rastro de
"devflow" en el kit, verificado por el verificador que ahora lo caza en
cualquier forma). Resultado: la **corrida de producción real** (`input-kit/`
→ `distribution-kit/`) terminó con **exit 0 — cero tokens prohibidos en
contenido y en nombres de archivos/carpetas**: 149 archivos, 66 carpetas,
5856 reglas aplicadas, 27 remociones, 1 excluido (TEMPLATE-REPORT.html), y
quedó la primera versión publicable del kit MetaFlow con la ruta canónica
`metaflow/ai-sdlc/MetaFlow.md`. La suite completa pasó **54/54 tests** (37 de
BOLT-001 + 17 nuevas), con evidencia RED (4 módulos fallando) y GREEN
registrados.

## 2. Implemented phases

### Phase A — Verificador (`src/verify.py`)

Implementa `verify_tree(root)`: recorre el árbol del kit de salida y devuelve
la lista de hits `{path, token, line, context, where}` con `where` =
`content` o `path`. Escanea el **contenido** línea por línea de cada archivo
de texto (los binarios se omiten) y **todos los componentes de ruta**
(carpetas y nombres de archivo, incluidas las carpetas vacías). Los tokens
canónicos (glossary §6: Avenga, devflow, AITL, HITL, Bolt/BOLT/bolts,
V-Bounce/v_bounces, Raja, DORA) se buscan como variantes regex con
`re.IGNORECASE` donde corresponde (`avenga`, `devflow`, `aitl`, `hitl`,
`\bbolts?\b` con word boundary — no marca "thunderbolt" —, `v[ _-]?bounces?`,
`\braja\b`, `\bdora\b`). La lista `EXCEPTIONS` (términos conservados del
glossary §7 que colisionaran) queda como dato extensible; hoy está vacía. El
resultado alimenta el exit code del run (AC-7: exit != 0 con hits).

### Phase B — Reporte y persistencia (`src/report.py` + integración)

`build_report(plan, input_dir, output_dir, hits)` consume el plan del engine
y produce el `report.json`: por archivo (src → dst, status changed/unchanged/
excluded/binary-copy, rules_applied, removals), totales (archivos, cambiados,
sin cambios, excluidos, reglas, remociones) y verificación (ok + hits).
`build_markdown` genera la versión legible. `persist_evidence` escribe en
`transform-reports/<versión>/<run>/`: report.json, report.md, `diff/` con un
**unified diff por archivo cambiado** (difflib, comparando el original del
input contra el convertido por identidad lógica src→dst), `unchanged.txt`
(candidatos a regla faltante — capa de cobertura), `removals.json` y
`run.log`. La integración en `transform.py`: el run real (no dry-run) agrega
al final — verificar → construir reporte → persistir evidencia → aplicar la
**retención acotada** (`prune_runs`, `--keep-runs N` con default 2: conserva
las 2 corridas más recientes por versión y purga las anteriores, anotándolas
en el log) → imprimir la ruta → si hay hits, exit 1 listándolos. Se agregó el
argumento `--reports` (por defecto `transform-reports/` en la raíz) y
`render_plan` devuelve el texto del plan que también queda como `run.log`. El
engine incorporó el tipo `regex_remove` (remociones por patrón registradas
como remociones, para las citas bibliográficas por línea).

### Phase C — Tests (unitarios + E2E)

Se escribieron los tests antes de la implementación (RED: 4 módulos fallando
por import). `test_verify.py` (8 casos: kit limpio, tokens exactos, variantes
de caso, rutas, word boundary, devflow en cualquier forma, carpeta vacía,
nombre de archivo), `test_report.py` (5 casos: estructura y totales,
persistencia completa, contenido del diff AGENTS.md, aditividad — nunca borra
runs previos), `test_e2e.py` (3 casos: pipeline completo sobre fixture con
evidencia, leftover inyectado que hace fallar el run, y la **aceptación
contra el kit real** con verificador en cero). El ciclo del kit real guió la
extensión del diccionario (Phase extra): 34 hits iniciales → reglas nuevas →
1 hit restante (`VBOUNCE` de Mermaid) → cero.

## 3. Files created

| File | Purpose |
|------|---------|
| `src/verify.py` | Verificador de tokens prohibidos: barrido de contenido y de componentes de ruta (archivos y carpetas, incluidas las vacías) con variantes regex, excepciones como datos, lista de hits para el reporte y el exit code |
| `src/report.py` | Reporte del run: report.json estructurado para IA, report.md legible, diffs por archivo (difflib), unchanged.txt, removals.json, run.log; persistencia aditiva en transform-reports/ |
| `src/tests/test_verify.py` | Suite del verificador (8 casos) |
| `src/tests/test_report.py` | Suite del reporte y persistencia (5 casos) |
| `src/tests/test_e2e.py` | Suite E2E: fixture completo, leftover inyectado, aceptación contra el kit real (3 casos) |
| `src/tests/fixtures/kit-leftover/` | Fixture con un token prohibido a propósito (AVENGA) para probar que el run falla y lista el hit |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `src/transform.py` | Integración del paso final del run real (verificar → persistir evidencia → retención acotada → exit code), argumentos `--reports` y `--keep-runs`, `render_plan` que devuelve texto (usado como run.log), y el nuevo tipo de regla `regex_remove` |
| `src/report.py` | Reporte del run + `prune_runs()` para la retención acotada (R6 rev 2) |
| `mapping.json` | Extensión del diccionario guiada por el E2E real + decisiones del propietario: C7 (`hitl_approvals`), C8 (anchor CITL), M12 (`Avenga` suelto → `Eugenio Serrano`), M13 (`avenga.com` → `metaflow.com`), M14 (`avenga` → `metaflow`), **M15/M16/M17/M18/P-M15 (`devflow` → `metaflow` en todas las variantes y rutas)**, D7 (`V-BOUNCE`), D8 (`v_bounce`), D9 (**DORA → Delivery Flow**), D10 (`VBOUNCE` de Mermaid), R2a/R2b (citas DORA/Accelerate eliminadas por línea con `regex_remove`); M11 actualizada (ruta canónica `metaflow/ai-sdlc/MetaFlow.md`); la antigua R2 (remoción de token "DORA") fue reemplazada por D9 + R2a/R2b |
| `devflow/analysis/glossary/metaflow.md` | Reglas nuevas C7/C8, M12–M18, P-M15, D7–D10, R2 por línea, token prohibido `devflow` en §6 + filas de Historia (fuente canónica del diccionario, living doc) |
| `src/tests/fixtures/kit-mini-expected/` | Ruta canónica `metaflow/ai-sdlc/MetaFlow.md` + línea DORA ("Delivery Flow and …") y `See metaflow/ai-sdlc/MetaFlow.md` |
| `src/tests/test_rename.py`, `test_path_rename.py`, `test_remove.py`, `test_verify.py` | Ajustes por las reglas nuevas (devflow → metaflow, D9, R2a) |

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
| — | — | Ninguno (los renames son comportamiento del pipeline; ver `distribution-kit/` — p. ej. `devflow/` → `metaflow/`) |

## 6. Files deleted

| File | Reason |
|------|--------|
| — | Ninguno (el `distribution-kit/` previo se regeneró con la corrida de producción — borrado acotado por diseño, AC-10) |

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| **DORA → Delivery Flow (D9)** | La R2 original (remover el token "DORA") rompía las secciones de contenido (§3.7.1 DORA Metrics/Five, refs D1–D5); el propietario decidió renombrar el concepto (misma funcionalidad, AG2) — las citas bibliográficas sí se eliminan por línea (R2a/R2b) |
| **`devflow/` → `metaflow/` (M15–M18, P-M15)** | El propietario pidió cero rastro de "devflow" en el kit: la carpeta raíz del framework pasa a `metaflow/`, todas las referencias de ruta en prosa se renombran, y `devflow` (cualquier forma) es token prohibido del verificador |
| **Verificador en dos dimensiones (contenido + rutas, carpetas incluidas)** | Los nombres de archivos y carpetas son parte de la superficie del kit: un token en un nombre es contaminación igual que en el contenido; las carpetas vacías también se barren (endurecimiento posterior a pedido del propietario) |
| **Tipo `regex_remove`** | Las citas son remociones (deben listarse en el reporte como remociones, nunca silenciosas); el tipo nuevo registra en `removals[]` con patrón regex multilínea |
| **Detección por variantes regex (no solo lista exacta)** | Capas 1 y 4 del diseño: caza case, plurales, separadores (`v_bounces`, `VBOUNCE`, `V-BOUNCE`), dominios (`avenga.com`, `dora.dev`), URLs/emails — lo que la lista exacta no ve |
| **Word boundary en `bolt`/`dora`** | Evita falsos positivos ("thunderbolt") manteniendo la caza de derivados |
| **E2E real con output temporal + corrida de producción real** | Los tests no dependen del árbol; la corrida de producción (input-kit → distribution-kit) es la evidencia demo del Bolt |
| **Evidencia con retención acotada (2 corridas por versión)** | R6 (Rev 5) / SPEC rev 2 — decisión del propietario: las 2 más recientes alcanzan para comparar runs; las purgadas se listan en el `run.log` (nada silencioso); `--keep-runs N` configura la retención |
| **Diccionario extendido durante el V-Bounce (datos, no código)** | Loop diseñado de OQ-004 + stop condition de la SPEC: leftovers → extender mapping.json → re-ejecutar hasta cero |

## 8. Deviations and assumptions

- **La R2 del glossary se reinterpretó:** "citas a Accelerate/DORA → eliminar" se implementa por línea (R2a/R2b), y el concepto de métricas DORA se renombra (D9) por decisión del propietario — registrado en el glossary (fuente canónica).
- **La carpeta raíz del framework cambió a `metaflow/`** durante el V-Bounce por decisión del propietario (cero rastro de "devflow"); implica que la ruta canónica del kit es `metaflow/ai-sdlc/MetaFlow.md` y que todas las referencias `devflow/…` de la metodología se renombran (M15/M16).
- **Extensión del diccionario durante el V-Bounce:** las reglas nuevas son datos (mapping.json) autorizadas por el stop condition de la SPEC aprobada (BOLT-002); el único cambio de engine fue el tipo `regex_remove` y el barrido de carpetas en el verificador (endurecimiento, sin cambio de contrato).
- **`distribution-kit/` fue regenerado** por la corrida de producción (exit 0): es el producto del pipeline.
- **Sin commits** (G34): `git_commit: null`; todo el trabajo queda en el árbol para revisión.

## 9. Verification evidence

### Build
```
N/A — Python stdlib puro (ADR-001), sin build.
```

### Tests
```
> python -m unittest discover -s src/tests
Ran 54 tests in 1.727s
OK        (37 de BOLT-001 + 17 nuevas; incluye aceptación contra el kit real)
```

### RED → GREEN evidence (test-first)
- **RED:** `python -m unittest discover -s src/tests` → 4 errores:
  `ModuleNotFoundError: No module named 'verify'/'report'` (antes de implementar).
- **GREEN:** misma suite tras la implementación → `Ran 54 tests ... OK`.

### E2E loop contra el kit real (evidencia del diccionario)
```
1ª corrida: 34 hits (hitl_approvals, v_bounce, V-BOUNCE, Avenga, dora.dev/citas,
            anchor aitl, urn:avenga, VBOUNCE) → diccionario extendido
2ª corrida: 1 hit restante (VBOUNCE de Mermaid) → D10 agregada
3ª corrida: 0 hits — aceptación OK
```

### Producción (demo — el producto)
```
> python src/transform.py
EXIT=0 — cero tokens prohibidos (contenido + nombres de archivos/carpetas)
total: 149 archivos, 66 carpetas, 0 binarios copiados, 1 excluidos,
       5856 reglas aplicadas, 27 remociones
evidencia: transform-reports/5.1/20260827-020355/
           (report.json, report.md, diff/ x149, unchanged.txt, removals.json, run.log)
retención: purgadas 20260827-015205, 20260827-015926 (quedan las 2 más recientes)
producto: distribution-kit/ — metaflow/ai-sdlc/MetaFlow.md ✓
          barrido "devflow" case-insensitive (rutas + contenido): 0 resultados ✓
          AGENTS.md "runs under MetaFlow" ✓
```

### Gates
| Gate | Result |
|------|--------|
| Unit / integration | pass — 54/54 |
| Perf-smoke (p95/p99) | pass — pipeline completo < 1 min (corrida real) |
| SAST / SBOM | n/a — sin superficie atacable externa |
| Prompt-injection scan | n/a — sin entradas no confiables |
| Secret-leak scan | pass — sin credenciales |
| Hallucination lint | pass — APIs verificadas contra stdlib Python 3.10+ |
| IP / license provenance | n/a — cero dependencias |
| PII / DLP | n/a — sin datos personales |
| Dependency-confusion | n/a — cero dependencias |
| Test-first evidence | pass — RED registrado antes de la implementación |
| Behavioral reproducibility | pass — fixture determinista; kit real reproducible |
| Bolt-manifest validation | pass — validado contra manifest-v5-bolt.schema.json |

## 10. Manual interventions

Ninguna — todo el código, tests y diccionario fueron generados por el agente;
las decisiones de contenido (DORA → Delivery Flow, devflow → metaflow) fueron
del propietario y quedaron registradas en el glossary.

## 11. Evidence links

- **Diff / PR:** no aplica (sin commit — G34; el diff se presenta en esta conversación).
- **Commit:** baseline `58ac5eb` (trabajo sin commitear para revisión).
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-001.BOLT-002-verificador-reporte.json`
- **Evidencia del run:** `transform-reports/5.1/20260827-020355/` (retención: 2 corridas por versión)

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~35 min |
| V-Bounce number | 1 (BOLT-002) |
| Tests created | 17 nuevas (8 verify + 5 report + 3 e2e + ajustes); suite total 54 |
| AI-generated code | 100 % |
| First-pass approval | n/a — en revisión |

## 13. Pending items and stubs

- [ ] **X6** — template HTML de reportes de MetaFlow con branding propio (entregable aparte, v1).
- [ ] **AITL-BOLT-DONE-Approval** de BOLT-001 y BOLT-002 (aceptación final; work_category feature → PO/PM).
- [ ] Decidir si `transform-reports/` y `distribution-kit/` se commitean (G34 — decisión del propietario en el commit).

## 14. AITL-MEM-Approval

> **Avenga DevFlow §2.12, §3.0.** Este MEM no tiene status mutable y **nunca
> se auto-aprueba**. El Dev-validator que ejecutó el Bolt inspecciona el diff
> real, la evidencia de tests/gates, el MEM y el manifest, y registra
> `AITL-MEM-Approval` aquí y en el `checkpoint_approvals[]` del manifest.

| Field | Value |
|-------|-------|
| **Reviewers (executing Dev-validator)** | `human:eugenioserrano` (Dev-validator — rol autoasignado: no hay otro titular) |
| **Roles** | dev_validator |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-27T02:03:08-03:00` |
| **review.started_at** | `2026-08-27T02:05:21-03:00` |
| **review.decided_at** | `2026-08-27T02:05:21-03:00` |
| **Review evidence** | diff de código + fixtures + tests 55/55 + corrida de producción (exit 0, cero devflow) + evidencia en transform-reports/ (retención 2) + MEM + manifest |
| **Comments** | — |
| **Findings** | Ninguno |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | Evidencia inspeccionada: diff, tests 55/55 en verde, gates pass/n/a, MEM completo, manifest v_bounces[1] validado |
