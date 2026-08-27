---
id: "MEM-260827-0225"
title: "BOLT-003 — Familia de manifests v1 + regla genérica −4 (V-Bounce 2)"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
bolt: "US-001.BOLT-003"
spec: "SPEC-260827-0211"
spec_revision: 2
v_bounce: 2
execution_outcome: "ready_for_review"
baseline: "58ac5eb"
applied_adrs:
  - "devflow/adrs/ADR-001-toolkit-transformacion.md"
manifest: "devflow/metrics/bolts/US-001.BOLT-003-versionado-y-limpieza.json"
diff_ref: ""
review_ready_at: "2026-08-27T02:25:17-03:00"
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
  acknowledgment_reason: "Aprobación del propietario (Dev-validator autoasignado) sin hallazgos — revisión del diff, tests 64/64, corrida de producción (familia v1, regla genérica −4, invariantes) y manifest en conversación, 2026-08-27"
---

# MEM-260827-0225 — BOLT-003: Familia de manifests v1 + regla genérica −4

| Field           | Value |
|-----------------|-------|
| **Bolt**        | US-001.BOLT-003 |
| **SPEC**        | [SPEC-260827-0211](../spec/SPEC-260827-0211-bolt003-versionado-limpieza.md) — revisión 2 |
| **V-Bounce**    | 2 |
| **ADRs**        | [ADR-001](../adrs/ADR-001-toolkit-transformacion.md) (accepted) |

---

## 1. Executive summary

Este V-Bounce (SPEC revisión 2, G15) implementa la **familia de manifests v1**
y convierte el versionado en una **regla genérica −4**: el diccionario ya no
tiene literales `5.1 → 1.1` / `v5 → v1`, sino **placeholders versionados**
(`{{VERSION_IN}}`, `{{VERSION_OUT}}`, `{{FAMILY_IN}}`, `{{FAMILY_OUT}}`) que
el engine resuelve leyendo el `devflow/VERSION` del kit de entrada y
aplicando **mayor − 4, menor igual**. Con un input futuro v6, las mismas
reglas producen 6.1 → 2.1 y familia v6 → v2 **sin tocar `mapping.json`**
(verificado por el test `test_generic_rule_future_version_v6`). La familia de
manifests quedó renombrada en nombres de archivo (`manifest-v1-*.schema.json`
para task/tc/us) y en contenido (`"schema_version": "1.0"`, `"const":
"1.0"`, URN `urn:metaflow:metaflow:manifest:…:v1`, título "Manifest v1") — el
nombre de campo `schema_version` se conserva y las ~93 referencias de sección
`§5.1` permanecen intactas (invariante verificado input == output). Se
agregaron 7 reglas de contenido (S1b, S1–S5) y 3 de ruta (P-B9a/b/c, con
renumeración 1006–1012). Resultado de la corrida de producción: **EXIT=0**,
`metaflow/VERSION` = **1.1**, **0** ocurrencias de `manifest-v5` (nombres y
contenido), **0** de `"schema_version": "5.0"`, schemas `manifest-v1-*` con
URN `:v1`, `§5.1` 93 = 93, evidencia con retención en `transform-reports/`.
Suite completa en verde: **64/64 tests** (62 previos + 2 nuevos), con RED
registrado (5 fallas de expectativa) y GREEN. Con esto el kit MetaFlow queda
autoconsistente: metodología **MetaFlow v1.1**, familia de manifests **v1**,
y el pipeline listo para absorber versiones futuras sin cambios de diccionario.

## 2. Implemented phases

### Phase A/B2 — Reglas genéricas y familia de manifests (datos + engine)

El engine ganó `compute_output_version(version_in, offset=-4)` (mayor − 4,
menor igual; 5.1 → 1.1, 6.2 → 2.2) y `render_rules(rules, version_in)`, que
rellena los placeholders `{{VERSION_IN/OUT}}` y `{{FAMILY_IN/OUT}}` en
pattern/replacement/path de cada regla; `build_plan` resuelve la versión del
input (`devflow/VERSION`) y aplica las reglas renderizadas. Las reglas V0–V7
pasaron de literales a placeholders (mismo comportamiento con 5.1), y se
agregaron: **S1b** (referencia completa `manifest-v5-bolt.schema.json` →
`manifest-v1-task.schema.json` en prosa), **S1** (`manifest-v5` →
`manifest-v1` genérico), **S2** (títulos "Manifest v5" → "Manifest v1"),
**S3/S3b** (`"schema_version": "5.0"` → `"1.0"` en JSON y MD), **S4** (regex
de URNs `manifest:(task|us|tc):v5` → `:v1`) y **S5** (`"const": "5.0"` →
`"1.0"`). Las rutas P-B9a/b/c renombran los tres schemas
(`manifest-v{{FAMILY_IN}}-{bolt→task,us,tc}.schema.json` →
`manifest-v{{FAMILY_OUT}}-…`), con renumeración de órdenes de path
(1006–1012). Se eliminó la regla B9b antigua (literal, sustituida por S1b/S1).

### Phase C — Tests

`test_version.py` ampliado: familia v1 en contenido (S1b/S1/S2/S3/S4/S5),
invariante `§5.1` + familia de manifests, **regla genérica v6 → v2** (render
con "6.1": `**Methodology version:** 6.1` → `2.1`, `manifest-v6-us…` →
`manifest-v2-us…`, `"schema_version": "6.0"` → `"2.0"`), y la E2E real
actualizada (0 × `manifest-v5`, 0 × `"schema_version": "5.0"`, URN `:v1`,
`§5.1` input == output, una sola "Accelerate"). `test_path_rename` renderiza
las reglas (expectativas `manifest-v1-*`) y el fixture esperado incorporó
`docs/manifest-v1-task.schema.json` y la línea `schema_version: "1.0"`.

## 3. Files created

| File | Purpose |
|------|---------|
| — | Ninguno (cambios sobre archivos existentes) |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `src/transform.py` | `compute_output_version` (fórmula −4) + `render_rules` (placeholders versionados) + `build_plan` renderiza las reglas con la versión del input |
| `mapping.json` | V0–V7 a placeholders `{{VERSION_IN/OUT}}`; reglas S1b/S1–S5 (familia de manifests); path rules P-B9a/b/c con placeholders (renumeración 1006–1012); eliminada B9b literal |
| `devflow/analysis/glossary/metaflow.md` | Fila de numeración actualizada: regla genérica −4 con placeholders (v6 → v2 futuro) y familia de manifests v1 |
| `src/tests/test_version.py` | Tests de familia v1, invariante `§5.1`, regla genérica v6 → v2 y E2E real actualizado |
| `src/tests/test_path_rename.py` | Render de reglas y expectativas `manifest-v1-*` |
| `src/tests/fixtures/kit-mini/versioning.md` + expected | Línea `schema_version: "5.0"` → `"1.0"` (formato real del kit) |
| `src/tests/fixtures/kit-mini-expected/docs/` | Schema esperado renombrado a `manifest-v1-task.schema.json` (contenido `"schema_version"` de familia v1) |

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
| — | — | Ninguno (los renames son comportamiento del pipeline; ver `distribution-kit/metaflow/metrics/manifest-v1-*.schema.json`) |

## 6. Files deleted

| File | Reason |
|------|--------|
| — | Ninguno |

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| **Placeholders versionados en el diccionario** | La regla −4 debe ser genérica (decisión del propietario: v6 → v2 en el futuro); el diccionario queda agnóstico de la versión del input |
| **`compute_output_version` (mayor − 4, menor igual)** | Misma fórmula de OQ-003 aplicada a la metodología y a la familia de manifests |
| **S1b antes de S1 (longest-first)** | La referencia completa `manifest-v5-bolt.schema.json` debe convertirse a `manifest-v1-task.schema.json` antes del patrón genérico |
| **URN `urn:metaflow:metaflow:manifest:…:v1`** | El segmento "devflow" del URN se renombra por M16 (regla del propietario: cero rastro de "devflow"); el segmento de marca "avenga" → "metaflow" (M14) |
| **S3/S3b separados (JSON vs MD)** | El kit declara `"schema_version": "5.0"` en JSON (schemas/templates) y `schema_version: "5.0"` en MD |
| **P-B9a/b/c por tipo de schema** | Cada familia (task/tc/us) se renombra explícitamente; "bolt" → "task" solo en el schema de Bolt |

## 8. Deviations and assumptions

- **Dos expectativas de test corregidas durante el V-Bounce:** el URN queda
  `urn:metaflow:metaflow:manifest:…` (M16 renombra el segmento "devflow") y el
  fixture de `schema_version` usa el formato real del kit (con comillas).
- **El V-Bounce 1 (SPEC rev 1) sigue siendo historia válida** — sus reglas
  literales V0–V7/A1/A2 quedaron re-expresadas como placeholders en este
  V-Bounce; su MEM queda pendiente de aprobación junto con este.
- **Sin commits** (G34): `git_commit: null`.

## 9. Verification evidence

### Build
```
N/A — Python stdlib puro (ADR-001), sin build.
```

### Tests
```
> python -m unittest discover -s src/tests
Ran 64 tests in 3.400s
OK        (62 previos + 2 nuevos: familia v1 + regla genérica v6)
```

### RED → GREEN evidence (test-first)
- **RED:** 5 fallas de expectativa (URN con "devflow", formato de
  `schema_version`, path rules sin renderizar) antes de corregir.
- **GREEN:** misma suite tras los ajustes → `Ran 64 tests ... OK`.

### Producción (demo — el producto)
```
> python src/transform.py
EXIT=0 — cero tokens prohibidos
total: 149 archivos, 66 carpetas, 0 binarios, 1 excluido, 6065 reglas, 27 remociones
evidencia: transform-reports/5.1/20260827-022508/ (retención: purgada 020355)
metaflow/VERSION ............................ 1.1 ✓
schemas: manifest-v1-task/tc/us.schema.json ... 3/3 ✓
$id: urn:metaflow:metaflow:manifest:task:v1 ... ✓
title: "MetaFlow TASK Manifest v1" ........... ✓
"manifest-v5" (nombres + contenido) .......... 0 ✓
"schema_version": "5.0" ..................... 0 ✓
§5.1 (output) ............................... 93 = input 93 ✓
```

### Gates
| Gate | Result |
|------|--------|
| Unit / integration | pass — 64/64 |
| Perf-smoke (p95/p99) | pass — pipeline < 1 min |
| SAST / SBOM | n/a — sin superficie atacable |
| Prompt-injection scan | n/a |
| Secret-leak scan | pass |
| Hallucination lint | pass — stdlib verificada |
| IP / license provenance | n/a — cero dependencias |
| PII / DLP | n/a |
| Dependency-confusion | n/a |
| Test-first evidence | pass — RED registrado |
| Behavioral reproducibility | pass — determinista |
| Bolt-manifest validation | pass — validado contra schema v5 (este repo) |

## 10. Manual interventions

Ninguna — todo el código, tests y diccionario fueron generados por el agente;
la decisión de la regla genérica −4 y la familia v1 fue del propietario
(aprobada en la SPEC rev 2).

## 11. Evidence links

- **Diff / PR:** no aplica (sin commit — G34).
- **Commit:** baseline `58ac5eb` (trabajo sin commitear para revisión).
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-001.BOLT-003-versionado-y-limpieza.json`
- **Evidencia del run:** `transform-reports/5.1/20260827-022508/`

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~15 min |
| V-Bounce number | 2 (BOLT-003) |
| Tests created | 2 nuevos; suite total 64 |
| AI-generated code | 100 % |
| First-pass approval | n/a — en revisión |

## 13. Pending items and stubs

- [ ] **AITL-MEM-Approval** de los dos V-Bounces de BOLT-003 (MEM-260827-0217 y este).
- [ ] **AITL-BOLT-DONE-Approval** de BOLT-003 (aceptación final).
- [ ] **X6** — template HTML de reportes de MetaFlow.
- [ ] Migración de gobernanza (OQ-003) y absorción de la próxima versión (OQ-004; con la regla genérica, v6 → v2 sin tocar el diccionario).

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
| **review_ready_at** | `2026-08-27T02:25:17-03:00` |
| **review.started_at** | `2026-08-27T02:26:19-03:00` |
| **review.decided_at** | `2026-08-27T02:26:19-03:00` |
| **Review evidence** | diff de código + fixture + tests 64/64 + corrida de producción (exit 0, familia v1, invariantes) + MEM + manifest |
| **Comments** | — |
| **Findings** | Ninguno |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | Evidencia inspeccionada: diff, tests 64/64 en verde, gates pass/n/a, MEM completo, manifest v_bounces[2] validado |
