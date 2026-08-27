---
id: "SPEC-260827-0211"
title: "BOLT-003 — Versionado −4 por contexto + limpieza de citas Accelerate"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved"
origin: "US-001"
bolt: "US-001.BOLT-003"
revision: 2
associated_adrs:
  - "devflow/adrs/ADR-001-toolkit-transformacion.md"
prerequisites:
  - "devflow/spec/SPEC-260827-0124-bolt001-engine-transformacion.md"
  - "devflow/spec/SPEC-260827-0142-bolt002-verificador-reporte.md"
risk_class: "low"
autonomy_level: "L3"
turn_budget: 10
data_classification: "internal"
review_ready_at: "2026-08-27T02:11:30-03:00"
review:
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-27T02:21:03-03:00"
  decided_at: "2026-08-27T02:21:03-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Re-aprobación de la Revisión 2 (familia de manifests v1 con regla genérica −4 por placeholders versionados) por el propietario (Dev-validator autoasignado) sin hallazgos — 2026-08-27. G15 cumplido; el V-Bounce 2 de BOLT-003 se ejecuta bajo la revisión 2"
---

# SPEC-260827-0211 — BOLT-003: Versionado −4 por contexto + limpieza Accelerate

| Field | Value |
|-------|-------|
| **Origin** | US-001 |
| **Bolt** | US-001.BOLT-003 |
| **ADRs** | [ADR-001](../adrs/ADR-001-toolkit-transformacion.md) |
| **Risk Class** | low |
| **Revision** | 1 |

---

## 1. Objective

Completar la AC-1 de la US-001 en su parte de **numeración de versión −4**
(decisión OQ-003: MetaFlow = AvengaDevFlow − 4, 5.1 → 1.1) y limpiar las
**citas en-texto al libro *Accelerate*** (R2). La revisión crítica del kit
real (2026-08-27) detectó que `metaflow/VERSION` sigue en `5.1`, al igual que
las declaraciones `**Methodology version:** 5.1` (73×) y las referencias
`v5.1` / `Agent version: 5.1` / `# … v5.1 (Methodology)` (~12×) — deben pasar
a `1.1`. **Restricción crítica:** el renombre de versión es **solo por contexto** —
nunca un replace global de `5.1` → `1.1`, porque rompería las ~93
referencias de sección `§5.1` (invariante absoluto). La **familia de
manifests** sí se versiona: los schemas `manifest-v5-*.schema.json` pasan a
`manifest-v1-*.schema.json` (nombre de archivo) y su contenido declara la
familia `v1` (`"schema_version": "1.0"`, `"const": "1.0"`, URN `…:v1`,
título "Manifest v1") — decisión del propietario 2026-08-27 (Revisión 2,
G15). El **nombre de campo** `schema_version` se conserva.

**Regla GENÉRICA −4 (Revisión 2):** tanto la metodología como la familia de
manifests se versionan con la misma fórmula **mayor − 4, menor igual** (5.1 →
1.1 y v5 → v1; 6.1 → 2.1 y v6 → v2 en el futuro). El diccionario usa
**placeholders versionados** (`{{VERSION_IN}}`, `{{VERSION_OUT}}`,
`{{FAMILY_IN}}`, `{{FAMILY_OUT}}`) que el engine resuelve leyendo el
`devflow/VERSION` del kit de entrada y aplicando el offset −4 — así las
mismas reglas sirven para cualquier versión futura sin tocar `mapping.json`.

**Si no se implementa:** el kit declara la versión equivocada (5.1 en vez de
1.1) — incumple AC-1/RULE-03/PROC-001 Regla 4, y las citas a *Accelerate*
quedan como referencias a la autoría removida (R2).

## 2. Context

Hallazgo de la revisión crítica del kit real (informe 2026-08-27, GAP 1 y
GAP 2). La regla −4 está decidida en OQ-003 y documentada en: visión O2,
scope (resumen), glossary §7, US AC-1, `DistributionKit` RULE-03, PROC-001
Regla 4 — pero el diccionario no la implementa porque un replace global de
`5.1 → 1.1` rompería las referencias de sección. BOLT-001 (engine) y
BOLT-002 (verificador/reporte) están Done; este Bolt extiende el diccionario
(datos) con un pequeño soporte de engine: **reglas con alcance por archivo**
(campo `path` opcional) para el VERSION file.

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | `devflow/functional/bolts/US-001.BOLT-003-versionado-y-limpieza.md` | AITL-BOLT-READY-Approval ✓ (2026-08-27) |
| Feature US | `devflow/functional/user-stories/US-001-toolkit-transformacion.md` | AITL-US-Approval ✓ (AC-1; Rev 6) |
| ADRs | `devflow/adrs/ADR-001-toolkit-transformacion.md` | AITL-ADR-Approval ✓ |
| Prior SPECs | BOLT-001 rev 2, BOLT-002 rev 2 (MEMs aprobados — Done) | ✓ |
| Analysis | glossary §7 (numeración, schema_version conservada, R2), `DistributionKit.md` RULE-03, PROC-001 Regla 4 | stable / active ✓ |
| Revisión crítica | Informe 2026-08-27 (GAP 1: versión 5.1; GAP 2: *Accelerate*) | Propietario ✓ |
| Repository baseline | `58ac5eb` (+ trabajo previo sin commitear, G34) | — |

## 4. Scope

### In scope

- `mapping.json`: reglas de contexto de versión (V0–V7), de neutralización
  de *Accelerate* (A1, A2) y de **familia de manifests v5 → v1** (S1–S4:
  nombres `manifest-v1-*` y contenido `"schema_version": "1.0"`, `"const":
  "1.0"`, URN `…:v1`, títulos "Manifest v1") — datos.
- `src/transform.py`: soporte de **`path` opcional por regla** (la regla solo
  aplica al archivo cuya ruta relativa de salida coincide) — cambio mínimo
  del engine, data-driven.
- `src/tests/`: `test_version.py` (contexto de versión, invariante `§5.1`,
  familia de manifests v1) + fixture actualizado (VERSION file, líneas de
  contexto y schemas) + E2E real (versión 1.1, invariante `§5.1`, familia
  v1).

### Out of scope

- `§5.1`/secciones (invariante absoluto — se testea).
- El verbo inglés "accelerate" (uso legítimo).
- Template HTML (X6), traducciones, migración de la raíz.

## 5. Prerequisites and baseline

- BOLT-001/002 Done: engine + verificador + reporte (suite 55/55).
- `input-kit/` presente (v5.1); evidencia del último run en
  `transform-reports/5.1/`.
- Baseline: `58ac5eb` + trabajo previo en el árbol.

## 6. Phases

### Phase A — Reglas de contexto de versión (datos + engine)

**Duration:** 1h — **Complexity:** Low

#### A.1 Soporte de `path` por regla en el engine

`Rule` gana el campo opcional `path` (string; vacío = aplica a todos los
archivos). `load_mapping` lo lee de la entrada JSON si existe. En
`build_plan`, al transformar cada archivo, las reglas de contenido se filtran
por archivo: una regla con `path` solo aplica cuando la **ruta relativa de
salida** del archivo (post-path_rename) coincide. Es la única forma segura de
renombrar el contenido del VERSION file sin tocar `§5.1` del resto del kit.

**Files modified:**
- `src/transform.py` — Campo `path` en `Rule`, lectura en `load_mapping`,
  filtro por archivo en `build_plan`.

#### A.2 Reglas de versión en `mapping.json`

| id | type | pattern | replacement | path | order | nota |
|----|------|---------|-------------|------|-------|------|
| V0 | rename | `5.1` | `1.1` | `metaflow/VERSION` | 70 | Solo el VERSION file (ruta de salida) |
| V1 | rename | `**Methodology version:** 5.1` | `**Methodology version:** 1.1` | — | 71 | 73 declaraciones README/INDEX |
| V2 | rename | `**Agent version:** 5.1 — implements methodology v5.1` | `**Agent version:** 1.1 — implements methodology v1.1` | — | 72 | Wrappers (4×) |
| V3 | rename | `v5.1 (Methodology)` | `v1.1 (Methodology)` | — | 73 | Heading `# … v5.1 (Methodology)` (4×) |
| V4 | rename | `v5.1 methodology` | `v1.1 methodology` | — | 74 | "follows the … v5.1 methodology" (2×) |
| V5 | rename | `(v5.1)` | `(v1.1)` | — | 75 | AGENTS.md "(v5.1) — the methodology governs" |

### Phase B — Neutralización de citas *Accelerate* (datos)

**Duration:** 0.5h — **Complexity:** Low

#### B.1 Reglas A1/A2 en `mapping.json`

- **A1** (order 76): `The longitudinal research synthesized in ***Accelerate*** shows that` → `The longitudinal research on software delivery shows that` — neutraliza la cita en-texto del cuerpo (§3.7.1-afín) sin perder la afirmación.
- **A2** (order 77): `(*Accelerate* / Delivery Flow)` → `(Delivery Flow)` — corre tras D9 (57) y deja limpia la referencia "evidence (*Accelerate* / DORA)".

El verbo "accelerate" (p. ej. "Accelerate value delivery using AI…") queda
intacto: los patrones A1/A2 son frases completas con el asterisco de énfasis.

### Phase B2 — Familia de manifests v5 → v1 (datos) [Revisión 2]

**Duration:** 0.5h — **Complexity:** Low

#### B2.1 Reglas S1–S5 en `mapping.json` (con placeholders versionados)

- **S1** (content, order 80): `manifest-v{{FAMILY_IN}}` → `manifest-v{{FAMILY_OUT}}` — referencias a los nombres de schema en prosa.
- **S2** (content, order 81): `Manifest v{{FAMILY_IN}}` → `Manifest v{{FAMILY_OUT}}` — títulos `"title": "… Manifest v5"`.
- **S3** (content, order 82): `"schema_version": "{{FAMILY_IN}}.0"` → `"schema_version": "{{FAMILY_OUT}}.0"` — JSON de schemas y templates de manifests.
- **S3b** (content, order 83): `schema_version: "{{FAMILY_IN}}.0"` → `schema_version: "{{FAMILY_OUT}}.0"` — estilo MD.
- **S4** (content, order 84): regex `manifest:(task|us|tc):v{{FAMILY_IN}}` → `manifest:$1:v{{FAMILY_OUT}}` — URNs `"$id": "urn:metaflow:devflow:manifest:task:v5"`.
- **S5** (content, order 85): `"const": "{{FAMILY_IN}}.0"` → `"const": "{{FAMILY_OUT}}.0"` — validación del schema.
- **Rutas:** `manifest-v{{FAMILY_IN}}-bolt.schema.json` → `manifest-v{{FAMILY_OUT}}-task.schema.json`, `manifest-v{{FAMILY_IN}}-us.schema.json` → `manifest-v{{FAMILY_OUT}}-us.schema.json`, `manifest-v{{FAMILY_IN}}-tc.schema.json` → `manifest-v{{FAMILY_OUT}}-tc.schema.json` (path_rename, órdenes 1006–1008; el resto de path rules se renumera).

#### B2.2 Resolución de placeholders en el engine

El engine lee `devflow/VERSION` del kit de entrada (p. ej. `5.1`), calcula la
salida con **mayor − 4, menor igual** (`1.1`) y la familia (`5` → `1`), y
rellena los placeholders `{{VERSION_IN}}`, `{{VERSION_OUT}}`,
`{{FAMILY_IN}}`, `{{FAMILY_OUT}}` en pattern/replacement/path de cada regla
antes de aplicarlas. Las reglas V0–V7 pasan de literales a placeholders con
el mismo comportamiento. Con un input futuro v6 el diccionario funciona sin
cambios (6.1 → 2.1, v6 → v2).

### Phase C — Tests

**Duration:** 1h — **Complexity:** Low

#### C.1 `test_version.py` + fixture

- Fixture `kit-mini`: agregar `devflow/VERSION` (`5.1`) → esperado
  `metaflow/VERSION` (`1.1`); línea `**Methodology version:** 5.1`; heading
  `# Avenga DevFlow v5.1 (Methodology)`; `§5.1` (referencia); `(*Accelerate*
  / DORA)`; schema `manifest-v5-bolt.schema.json` → esperado
  `manifest-v1-task.schema.json` con contenido `"schema_version": "1.0"`.
- Casos: VERSION → 1.1; "Methodology version: 1.1"; "v1.1 (Methodology)";
  A1/A2 neutralizados; **invariante:** `§5.1` intacto; **familia de
  manifests:** nombres `manifest-v1-*` y contenido `"schema_version":
  "1.0"`/`"const": "1.0"`/URN `:v1`/título "Manifest v1".
- E2E real: `metaflow/VERSION` = `1.1`; 0 × `Methodology version: 5.1`; 0 ×
  `v5.1`; la cantidad de `§5.1` del output == la del input; 0 ×
  `manifest-v5-*` (nombres y contenido) y 0 × `"schema_version": "5.0"`;
  verificador en cero.

**Files created:**
- `src/tests/test_version.py` — Suite de contexto de versión e invariantes.

---

## 7. Acceptance criteria

### AC-1 (completa): Versión de salida = entrada − 4

**Given** un kit de AvengaDevFlow v5.1 en `input-kit/`,
**When** se ejecuta el pipeline,
**Then** `metaflow/VERSION` = `1.1`, las declaraciones
`**Methodology version:** 1.1` y las referencias `v1.1` reemplazan a `5.1`,
**y** `§5.1` (secciones) y `schema_version: 5.0` (manifests) permanecen
intactos.

### AC (BOLT-003): Citas *Accelerate* neutralizadas

**Given** el kit real transformado,
**When** se busca "Accelerate" en el cuerpo,
**Then** solo queda el uso legítimo como verbo ("Accelerate value delivery
using AI…") — las referencias en-texto al libro quedan neutralizadas.

### AC (Revisión 2): Familia de manifests v1

**Given** el kit real transformado,
**When** se inspeccionan los schemas de manifests,
**Then** los nombres de archivo son `manifest-v1-*.schema.json` y el contenido
declara `"schema_version": "1.0"`, `"const": "1.0"`, URN `…:v1` y título
"Manifest v1" — con `§5.1` intacto.

### AC mapping to source (functional) / measurable outcome (non-functional)

| Source AC / outcome | How this SPEC satisfies it | Verifying test/evidence |
|---------------------|----------------------------|--------------------------|
| US AC-1 (versión) | Phase A: reglas V0–V7 por contexto (VERSION file con `path`) | `test_version.py` + E2E real |
| US AC-1 (resto) | Invariante `§5.1` protegido por tests | `test_version.py` |
| R2 del glossary (*Accelerate*) | Phase B: A1/A2 neutralizan las citas en-texto | `test_version.py` + E2E real |
| Familia de manifests v1 (Revisión 2) | Phase B2: S1–S5 + path renames | `test_version.py` + E2E real |

---

## 8. Testing strategy

- **Unit tests (~8 casos):** VERSION file por `path` (1), "Methodology
  version:" (1), "Agent version:" (1), heading `v5.1 (Methodology)` (1),
  `(v5.1)` (1), A1 (1), A2 (1), invariantes `§5.1` + `schema_version` (2).
- **E2E (1):** kit real regenerado — versión 1.1, 0 × `5.1`-versión,
  invariantes, verificador en cero.
- **Edge cases:** `§5.1` en el mismo archivo que "Methodology version: 5.1";
  `schema_version: 5.0` junto a `v5.1`; VERSION file sin path (regla global
  no debe tocar).
- **BUG evidence:** N/A (no es BUG Bolt).

---

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | Suite completa verde (55 + nuevas) | pass (objetivo) |
| SAST / SBOM | Sin dependencias ni red | n/a |
| Perf-smoke (p95/p99) | Pipeline < 1 min | pass (objetivo) |
| Prompt-injection scan | Sin inputs no confiables | n/a |
| Secret-leak scan | Sin credenciales | pass |
| Hallucination lint | APIs de stdlib verificadas | pass |
| IP / license provenance | Cero dependencias | n/a |
| PII / DLP | Sin datos personales | n/a |
| Dependency-confusion | Cero dependencias | n/a |
| Test-first evidence | Tests antes del código | pass (objetivo) |
| Behavioral reproducibility | Mismo input → mismo output | pass (objetivo) |
| Bolt-manifest validation | Manifest válido contra schema v5 | pass |

---

## 10. Security and data

- Sin cambios de superficie: reglas de texto y filtro por ruta; el campo
  `path` se valida como string (nunca como ruta absoluta fuera del kit).
- `data_classification: internal`.

## 11. Monitoring and observability

- El reporte del run lista las reglas V0–V5/A1/A2 aplicadas (conteos por
  regla); la evidencia queda en `transform-reports/` (retención 2).

## 12. Migration, compatibility and rollback

- **Migration:** N/A — el kit se regenera completo.
- **Compatibility:** el campo `path` es opcional: diccionarios viejos sin
  `path` siguen funcionando (regresión cubierta por la suite previa).
- **Rollback:** git + re-ejecución (evidencia previa conservada).

## 13. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| Renombre de versión toca `§5.1` | 2 | 5 | Reglas por contexto + invariantes testeados (conteo de `§5.1` antes/después) |
| `schema_version: 5.0` renombrada | 1 | 4 | Invariante testeado |
| El campo `path` del engine rompe diccionarios viejos | 1 | 3 | Opcional por defecto + suite completa de regresión |

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| Reglas de versión por contexto (nunca replace global) | ~107 `§5.1` y `schema_version` son invariantes (glossary §7) |
| Campo `path` en el engine para el VERSION file | Única forma segura de transformar solo ese archivo; data-driven y opcional |
| Neutralizar (no eliminar) las citas *Accelerate* | Preserva el contenido (AG2: misma funcionalidad) sin la cita de autoría (R2); decisión del propietario confirmada en la aprobación del Bolt |
| V5 patrón `(v5.1)` acotado | Solo existe en AGENTS.md como "(v5.1) — the methodology governs" (verificado en el input) |

## 15. Stop conditions

- Si aparece un contexto de `5.1` no clasificado (ni versión ni `§`): detener
  y clasificar con el propietario — nunca renombrar a ciegas.
- Si el conteo de `§5.1` cambia entre input y output: detener (invariante
  rota).

## 16. Definition of Done (DoD)

- [ ] All phases implemented (A, B, C)
- [ ] AC-1 completada (versión 1.1) + citas Accelerate neutralizadas
- [ ] Tests GREEN (suite completa, 0 failures) — invariantes `§5.1`/`schema_version` verificados
- [ ] Code follows ADR-001 (Python stdlib)
- [ ] Applicable gates pass / waived (ADR) / n/a (reason)
- [ ] MEM created in `devflow/memory/` (exactly one per V-Bounce)
- [ ] Manifest `v_bounces[]` entry appended in
      `devflow/metrics/bolts/US-001.BOLT-003-versionado-y-limpieza.json`
- [ ] AITL-MEM-Approval recorded

## 17. References

- US-001 (AC-1, Rev 6), BOLT-003 (aprobado), ADR-001 (accepted)
- Glossary §7 (numeración, schema_version, R2), `DistributionKit.md` RULE-03, PROC-001 Regla 4
- Informe de revisión crítica del kit real (2026-08-27)

## 18. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-27 | @eugenioserrano | Revision 1 — SPEC inicial de BOLT-003 |
| 2026-08-27 | @eugenioserrano | **AITL-SPEC-Approval** — `approved` por human:eugenioserrano (Dev-validator autoasignado), sin hallazgos |
| 2026-08-27 | @eugenioserrano | Revision 2 — familia de manifests v5 → v1 (nombres `manifest-v1-*` y contenido: `"schema_version": "1.0"`, `"const": "1.0"`, URN `:v1`, títulos "Manifest v1"); **regla genérica −4 con placeholders versionados** (v6 → v2 automático en el futuro); `§5.1` sigue invariante (G15 — solicitado por el propietario) |
| 2026-08-27 | @eugenioserrano | **AITL-SPEC-Approval (Revisión 2)** — re-aprobado por human:eugenioserrano, sin hallazgos |

## 19. AITL-SPEC-Approval

> **Avenga DevFlow §2.4.1, §3.0.** Esta SPEC permanece en draft hasta que el
> Dev-validator registra `AITL-SPEC-Approval` (bloque `review` del
> frontmatter). La aprobación autoriza el code-run / V-Bounce.

| Field | Value |
|-------|-------|
| **review.reviewers** | human:eugenioserrano (Dev-validator — rol autoasignado: no hay otro titular) |
| **review.decision** | **approved** (Revisión 2) |
| **review_ready_at** | `2026-08-27T02:11:30-03:00` |
| **review.started_at** | `2026-08-27T02:21:03-03:00` |
| **review.decided_at** | `2026-08-27T02:21:03-03:00` |
| **Findings** | Ninguno — re-aprobado sin comentarios |
