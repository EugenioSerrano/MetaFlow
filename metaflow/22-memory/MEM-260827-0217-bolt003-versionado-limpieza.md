---
id: "MEM-260827-0217"
title: "BOLT-003 — Versionado −4 por contexto + limpieza de citas Accelerate (V-Bounce 1)"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
bolt: "US-001.BOLT-003"
spec: "SPEC-260827-0211"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "58ac5eb"
applied_adrs:
  - "devflow/adrs/ADR-001-toolkit-transformacion.md"
manifest: "devflow/metrics/bolts/US-001.BOLT-003-versionado-y-limpieza.json"
diff_ref: ""
review_ready_at: "2026-08-27T02:17:11-03:00"
review:
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-27T02:26:19-03:00"
  decided_at: "2026-08-27T02:26:19-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Aprobación del propietario (Dev-validator autoasignado) sin hallazgos — revisión del diff, tests 62/62, corrida de producción (versión 1.1, invariantes) y manifest en conversación, 2026-08-27"
---

# MEM-260827-0217 — BOLT-003: Versionado −4 + limpieza Accelerate

| Field           | Value |
|-----------------|-------|
| **Bolt**        | US-001.BOLT-003 |
| **SPEC**        | [SPEC-260827-0211](../spec/SPEC-260827-0211-bolt003-versionado-limpieza.md) — revisión 1 |
| **V-Bounce**    | 1 |
| **ADRs**        | [ADR-001](../adrs/ADR-001-toolkit-transformacion.md) (accepted) |

---

## 1. Executive summary

Este V-Bounce cierra los dos gaps que encontró la revisión crítica del kit
real (2026-08-27): la **numeración de versión −4** (AC-1 de la US-001,
decisión OQ-003) y las **citas en-texto al libro *Accelerate*** (R2 del
glossary). Se implementaron **8 reglas de contexto** en el diccionario (datos)
más el soporte de **alcance por archivo** en el engine (campo `path` opcional
por regla): V0 transforma el contenido del VERSION file (`5.1` → `1.1`) —
la única forma segura de tocar ese archivo sin un replace global — y V1–V7
renombran por contexto las declaraciones `**Methodology version:** 5.1`,
`**Agent version:** 5.1 — implements methodology v5.1`, `v5.1 (Methodology)`,
`v5.1 methodology`, `(v5.1)`, `MetaFlow v5.1` y `v5.1)`. Las reglas A1/A2
neutralizan las dos citas en-texto a *Accelerate* (decisión del propietario:
neutralizar, no eliminar — preserva el contenido, AG2). **Invariantes
protegidos y verificados por tests:** las ~93 referencias de sección `§5.1`
quedan intactas (conteo input == output) y `"schema_version": "5.0"` (familia
de manifests) se conserva. Resultado de la corrida de producción: **EXIT=0**,
`metaflow/VERSION` = **1.1**, **0** ocurrencias de `Methodology version: 5.1`
y `v5.1`, **93 = 93** de `§5.1`, **1** sola "Accelerate" (el verbo legítimo
"Accelerate value delivery using AI…"), 5944 reglas aplicadas y evidencia con
retención en `transform-reports/`. La suite completa quedó en verde:
**62/62 tests** (55 previos + 7 nuevos), con RED registrado (8 fallas) y
GREEN. Con esto, la AC-1 de la US-001 queda cumplida en su totalidad y el kit
declara su identidad completa: MetaFlow v1.1.

## 2. Implemented phases

### Phase A — Reglas de contexto de versión (datos + engine)

Se agregó al engine el campo **`path` opcional por regla**: `Rule.path`
(string; vacío = aplica a todos los archivos), leído en `load_mapping` y
aplicado en `build_plan` — al transformar cada archivo se filtran las reglas
de contenido por su **ruta relativa de salida** (post-path_rename): una regla
con `path` solo aplica cuando coincide. Esto permite que V0
(`5.1` → `1.1`, `path: metaflow/VERSION`) transforme solo el VERSION file sin
tocar `§5.1` del resto del kit. El diccionario agregó las reglas V1–V7 con
patrones de contexto explícitos (declaraciones de versión y referencias
`v5.1`), todas con orden posterior a las familias M/C/B/D (70–79) para que
corran sobre el texto ya renombrado (p. ej. `MetaFlow v5.1` tras M1/M2).

### Phase B — Neutralización de citas *Accelerate* (datos)

A1 reemplaza la frase completa `The longitudinal research synthesized in
***Accelerate*** shows that` por `The longitudinal research on software
delivery shows that` (se conserva la afirmación, se quita la cita de
autoría); A2 limpia `(*Accelerate* / Delivery Flow)` → `(Delivery Flow)`
(tras D9). El uso legítimo del verbo "accelerate" queda intacto porque los
patrones son frases completas con el asterisco de énfasis.

### Phase C — Tests

`test_version.py` (7 casos): VERSION file por `path` (vía fixture),
"Methodology version:", "Agent version:", heading y prosa `v5.1`, invariantes
`§5.1`/`schema_version`, neutralización de *Accelerate* con verbo intacto, y
la **E2E real** que verifica: versión 1.1, cero `Methodology version: 5.1` /
`v5.1`, conteo de `§5.1` igual entre input y output, `"schema_version":
"5.0"` presente y una sola "Accelerate". El fixture `kit-mini` incorporó
`devflow/VERSION` (→ `metaflow/VERSION` = 1.1) y `versioning.md` (líneas de
contexto e invariantes). Se corrigió el helper de tests para filtrar reglas
con `path` (mismo comportamiento que `build_plan`).

## 3. Files created

| File | Purpose |
|------|---------|
| `src/tests/test_version.py` | Suite de contexto de versión e invariantes (7 casos, incl. E2E real) |
| `src/tests/fixtures/kit-mini/devflow/VERSION` | Fixture: archivo de versión de entrada (5.1) |
| `src/tests/fixtures/kit-mini-expected/metaflow/VERSION` | Fixture: versión esperada tras el −4 (1.1) |
| `src/tests/fixtures/kit-mini/versioning.md` | Fixture: líneas de contexto (declaraciones, heading, §5.1, Accelerate, schema_version) |
| `src/tests/fixtures/kit-mini-expected/versioning.md` | Fixture: resultado esperado (1.1, neutralización, invariantes intactas) |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `src/transform.py` | Campo `path` opcional en `Rule` + lectura en `load_mapping` + filtro por archivo en `build_plan` (alcance por ruta de salida) |
| `mapping.json` | Reglas V0–V7 (versión −4 por contexto; V0 con `path`) y A1/A2 (neutralización *Accelerate*) — 9 reglas nuevas |
| `devflow/analysis/glossary/metaflow.md` | Fila de numeración actualizada con la implementación por contexto (V0–V7) + invariantes `§5.1`/`schema_version` |
| `src/tests/test_report.py` | Conteos del fixture actualizados (9 archivos input, 8 output, 1 excluido) |
| `src/tests/test_e2e.py` | Carpeta de versión del fixture (5.1 en vez de "unknown") |

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
| — | — | Ninguno (los renames son comportamiento del pipeline) |

## 6. Files deleted

| File | Reason |
|------|--------|
| — | Ninguno |

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| **Campo `path` en el engine** para el VERSION file | Única forma segura de transformar el contenido de un archivo específico sin un replace global de `5.1` (rompería `§5.1`) — data-driven y opcional (compatibilidad con diccionarios viejos) |
| **Reglas de versión por contexto (V1–V7)** | ~85 referencias de versión vs ~107 referencias de sección `§5.1` + `schema_version` invariante: solo patrones explícitos de declaración/referencia |
| **Neutralizar (no eliminar) las citas *Accelerate*** | Decisión del propietario (aprobada en BOLT-003): preserva el contenido (AG2) y cumple R2 (sin citas de autoría) |
| **V6/V7 tras la E2E real** | El kit real tenía 3 contextos más ("MetaFlow v5.1" ×2, "source, v5.1)") — extensiones de datos guiadas por evidencia (loop OQ-004) |
| **Helper de tests filtra reglas con `path`** | `apply_content` directo no conoce la ruta del archivo; el helper imita el filtro de `build_plan` (V0 se valida vía fixture/E2E) |

## 8. Deviations and assumptions

- **Dos reglas adicionales (V6, V7)** se agregaron durante la E2E real al
  detectar 3 contextos no cubiertos — datos, sin cambio de SPEC (el stop
  condition de la SPEC prevé clasificar contextos nuevos).
- **Sin commits** (G34): `git_commit: null`; todo el trabajo queda en el
  árbol para revisión.

## 9. Verification evidence

### Build
```
N/A — Python stdlib puro (ADR-001), sin build.
```

### Tests
```
> python -m unittest discover -s src/tests
Ran 62 tests in 3.449s
OK        (55 previos + 7 nuevos)
```

### RED → GREEN evidence (test-first)
- **RED:** 8 fallas (las nuevas de versión + fixture-dependentes) antes de la
  implementación.
- **GREEN:** misma suite tras la implementación → `Ran 62 tests ... OK`.

### Producción (demo — el producto)
```
> python src/transform.py
EXIT=0 — cero tokens prohibidos
total: 149 archivos, 66 carpetas, 0 binarios, 1 excluido, 5944 reglas, 27 remociones
evidencia: transform-reports/5.1/20260827-021702/ (retención: purgada 020002)
metaflow/VERSION ................ 1.1 ✓
"Methodology version: 5.1" ...... 0 ✓
v5.1 ............................ 0 ✓
§5.1 (output) ................... 93 = input 93 ✓ (invariante)
"schema_version": "5.0" ......... presente ✓ (invariante)
"Accelerate" .................... 1 (solo el verbo legítimo) ✓
```

### Gates
| Gate | Result |
|------|--------|
| Unit / integration | pass — 62/62 |
| Perf-smoke (p95/p99) | pass — pipeline < 1 min |
| SAST / SBOM | n/a — sin superficie atacable |
| Prompt-injection scan | n/a — sin entradas no confiables |
| Secret-leak scan | pass |
| Hallucination lint | pass — stdlib verificada |
| IP / license provenance | n/a — cero dependencias |
| PII / DLP | n/a — sin datos personales |
| Dependency-confusion | n/a — cero dependencias |
| Test-first evidence | pass — RED registrado |
| Behavioral reproducibility | pass — fixture y kit real deterministas |
| Bolt-manifest validation | pass — validado contra schema v5 |

## 10. Manual interventions

Ninguna — todo el código, tests y diccionario fueron generados por el agente;
la decisión de neutralizar (no eliminar) las citas *Accelerate* fue del
propietario y quedó registrada en la aprobación del BOLT-003.

## 11. Evidence links

- **Diff / PR:** no aplica (sin commit — G34).
- **Commit:** baseline `58ac5eb` (trabajo sin commitear para revisión).
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-001.BOLT-003-versionado-y-limpieza.json`
- **Evidencia del run:** `transform-reports/5.1/20260827-021702/`

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~10 min |
| V-Bounce number | 1 (BOLT-003) |
| Tests created | 7 nuevos; suite total 62 |
| AI-generated code | 100 % |
| First-pass approval | n/a — en revisión |

## 13. Pending items and stubs

- [ ] **AITL-BOLT-DONE-Approval** de BOLT-003 (aceptación final).
- [ ] **X6** — template HTML de reportes de MetaFlow (entregable aparte).
- [ ] Migración de gobernanza (OQ-003) y absorción de la próxima versión (OQ-004).

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
| **review_ready_at** | `2026-08-27T02:17:11-03:00` |
| **review.started_at** | `2026-08-27T02:26:19-03:00` |
| **review.decided_at** | `2026-08-27T02:26:19-03:00` |
| **Review evidence** | diff de código + fixture + tests 62/62 + corrida de producción (exit 0, versión 1.1, invariantes) + MEM + manifest |
| **Comments** | — |
| **Findings** | Ninguno |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | Evidencia inspeccionada: diff, tests 62/62 en verde, gates pass/n/a, MEM completo, manifest v_bounces[1] validado |
