---
id: "REV-001"
title: "Ruido de renombrar carpetas internas del kit (p. ej. `input` → `1 - input`)"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "closed"
scope: "kit MetaFlow — árbol interno de `metaflow/` (carpetas del framework)"
methodology: "análisis de referencias por grep sobre el contenido del kit (input-kit/), conteo de menciones de ruta y superficie de archivos afectados"
reviewed_artifacts:
  - "input-kit/devflow/** (contenido fuente del kit: md/yaml/json)"
  - "mapping.json (reglas de rename del pipeline)"
  - "transform-reports/ (diffs de la corrida de producción)"
adrs_checked: []
specs_checked: []
review_ready_at: "2026-08-27T02:28:00-03:00"
review:
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "tech_lead"
      model: null
  started_at: "2026-08-27T02:32:05-03:00"
  decided_at: "2026-08-27T02:32:05-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Aprobación del propietario (rol autoasignado) sin hallazgos — 2026-08-27. Se adopta el Plan B (renombrar con prefijos numéricos sin espacios, con gaps para crecer) del action plan; F-01/F-02 se rutean a ADR + BOLT bajo US-001"
tags: [kit, renombrado, ruido, revision]
---

# REV-001 — Ruido de renombrar carpetas internas del kit

| Field           | Value |
|-----------------|-------|
| **Scope**       | Kit MetaFlow — carpetas internas del árbol `metaflow/` |
| **Methodology** | Análisis de referencias (grep + conteo) sobre `input-kit/` (144 archivos md/yaml/json) |
| **Criteria**    | O1/AC-1 (equivalencia funcional verificable: "solo nombres cambiaron"), O3 (transformación repetible), calidad de la revisión de diffs |

---

## 1. Purpose

Evaluar cuánto **ruido** introduciría renombrar las carpetas internas del kit
(p. ej. `input` → `1 - input`, `discovery` → `2 - discovery`, etc.): cuántas
referencias habría que reescribir, qué superficie de archivos se ensucia en
el diff, qué riesgos de links rotos y qué fricción de tooling generaría. El
objetivo es decidir con datos si el beneficio (orden visual) justifica el
costo.

## 2. Artifacts reviewed

| Artifact | Files | Notes |
|----------|-------|-------|
| Contenido fuente del kit | `input-kit/devflow/**` (144 archivos md/yaml/json) | Se contaron referencias `name/` (rutas en prosa, links relativos `../`, backticks) y menciones del nombre sin barra |
| Diccionario del pipeline | `mapping.json` | Capacidad actual de renames de rutas (path_rename) y contenido |
| Evidencia de la corrida de producción | `transform-reports/5.1/20260827-022508/` | Diffs por archivo (149) — la herramienta de revisión que el rename ensuciaría |

## 3. Severity legend

| Category | Meaning |
|----------|---------|
| **Compliant** | Implementado correctamente per ADR / estándar |
| **Documented deviation** | Diferencia justificada, registrada en MEM |
| **Minor gap** | Inconsistencia sin impacto funcional, reduce calidad |
| **Major gap** | Problema que puede causar errores de runtime o exposición |

## 4. Findings

### 4.1 — Impacto medido del rename

#### F-01 [Major gap] — El diff del kit quedaría ilegible: 1524 referencias y 63 % de archivos tocados

**Location:** contenido de `input-kit/devflow/**` (medición 2026-08-27)

**Actual:** el kit tiene 23 carpetas internas; el conteo de referencias de
ruta (`name/`) por carpeta es: `analysis` 207 (37 archivos), `input` 147
(42), `metrics` 147 (19), `agents` 144 (21), `functional` 123 (36), `risks`
97 (23), `tests` 71 (21), `reviews` 65 (13), `adrs` 63 (31), `discovery` 59
(21), `memory` 58 (18), `agents-data` 55 (11), `actors` 50 (19), `spec` 50
(27), `adversarial-reviews` 39 (12), `avenga-devflow` 38 (12), `bugs` 33
(16), `uat` 26 (13), `reports` 19 (10), `incidents` 15 (9), `prompts` 10
(8), `retros` 6 (3), `units` 2 (2). **Total: 1524 referencias**; con las
menciones en prosa sin barra, **1700 menciones**. **91 de 144 archivos
(63 %) contienen al menos una referencia** de ruta.

**Expected:** un rename de carpetas con prefijo numérico requiere reescribir
cada una de esas referencias en el contenido (reglas `rename` de contenido +
`path_rename` de rutas) — y el diff resultante toca el 63 % de los archivos.

**Impact:** la garantía central del pipeline (O1/AC-1: "solo nombres
cambiaron", equivalencia funcional verificable) se pierde de facto: el diff
de `input` → `1 - input` y sus 147+ referencias convierte cada archivo en un
diff gigante de churn; la revisión de calidad de la migración (el propósito
de `transform-reports/diff/`) se ahoga en ruido.

**Recommendation:** medir antes de decidir (este REV) y, si se avanza, hacerlo
como Bolt dedicado con reescritura completa y test de integridad de links —
ver action plan.

---

#### F-02 [Major gap] — Riesgo de links rotos sin detección automática

**Location:** links relativos `../analysis/`, `../../metrics/`, `../functional/` en los 91 archivos con referencias

**Actual:** los links relativos del kit dependen de los nombres de carpeta
reales. El verificador actual solo controla **tokens prohibidos** — no la
integridad de los links.

**Expected:** un rename parcial (o una regla que no cubra alguna variante,
p. ej. `input` en prosa sin barra) deja links rotos en el kit adoptado sin
que ningún test lo detecte.

**Impact:** el adoptante recibe un kit con navegación rota; el defecto es
silencioso (no falla el pipeline, no lo marca el verificador).

**Recommendation:** si se renombra, agregar un **test de integridad de links**
(E2E: todos los links relativos del kit resuelven) — nueva superficie de
garantía que hoy no existe.

---

#### F-03 [Minor gap] — Fricción de tooling y mantenimiento del esquema numérico

**Location:** nombres de carpeta con espacios ("1 - input") y prefijos numéricos

**Actual:** los nombres actuales son simples (una palabra, sin espacios).

**Expected:** con prefijos numéricos: rutas sin comillas en shells (espacios),
patrones de grep y scripts que referencian `input/` se rompen; el orden
numérico queda desactualizado cuando aparece una carpeta nueva (renumeración
en cadena — churn adicional en cada versión absorbida, OQ-004).

**Impact:** fricción diaria del mantenedor y del adoptante; cada versión
futura de AvengaDevFlow con carpetas nuevas exige redecidir la numeración.

**Recommendation:** si se busca orden, preferir prefijos **sin espacios**
(`01-input`) o mantener el orden actual (ver F-05).

---

#### F-04 [Compliant] — El pipeline PUEDE hacerlo técnicamente

**Location:** `mapping.json` (path_rename + reglas de contenido) + tests E2E

**Actual:** el pipeline ya reescribe rutas y contenido con orden
longest-first y lo verifica con la E2E contra el kit real (64/64 tests).

**Expected:** nada impide implementar el rename — el costo es de
**contenido** (1524+ reglas/reescrituras) y de **legibilidad**, no de
capacidad técnica.

**Impact:** ninguno — constatación.

**Recommendation:** la decisión es de costo/beneficio, no de viabilidad.

---

#### F-05 [Compliant] — El orden ya está resuelto por la semántica de las carpetas

**Location:** estructura `analysis/ → functional/ → spec/` y INDEX/README por carpeta

**Actual:** las carpetas del framework ya siguen un orden de fase (análisis →
funcional → spec → memoria → métricas) y cada carpeta tiene su README/INDEX.

**Expected:** el "orden visual" que motivaría el prefijo numérico ya está
expresado en la semántica de los nombres y en los índices.

**Impact:** el beneficio del prefijo es cosmético.

**Recommendation:** mantener los nombres actuales (opción A del action plan).

---

## 5. Summary

El rename de carpetas con prefijos numéricos es **técnicamente viable** pero
de **alto costo**: 1524 referencias de ruta y 1700 menciones a reescribir, 91
de 144 archivos (63 %) tocados en el diff, riesgo de links rotos sin
detección automática y fricción de tooling. El beneficio es cosmético (orden
visual que ya está expresado en la semántica e índices de las carpetas). La
recomendación es **no renombrar**; si el propietario prioriza el orden, hacerlo
con prefijos sin espacios y un test de integridad de links.

## 6. Action plan

> Aplica solo después de `AITL-REV-Approval`. Cada destino sigue su propio
> ciclo y aprobación (código → Bolt aprobado primero, T10).

| # | Finding | Severity | Action | Routes to |
|---|---------|----------|--------|-----------|
| 1 | F-01/F-03/F-05 | Major/Minor | **Opción A (recomendada): no renombrar** — mantener los nombres actuales; documentar la decisión | ADR (decisión de naming del kit) |
| 2 | F-01/F-02 | Major | **Opción B (si el propietario prioriza el orden):** prefijos sin espacios (`01-input`) + reescritura completa de referencias + test de integridad de links | BOLT→SPEC (US-001) |
| 3 | F-02 | Major | Test de integridad de links en el E2E (recomendado en ambos escenarios) | BOLT→SPEC (US-001) |

## 7. Conclusions

Se recomienda **no renombrar** las carpetas internas del kit: el costo
medido (63 % de los archivos con churn de diff, 1524 referencias, riesgo de
links rotos, fricción de tooling) supera ampliamente el beneficio cosmético.
Si la decisión final es renombrar, debe hacerse con prefijos sin espacios,
reescritura completa y un test de integridad de links nuevo. No se requiere
otro ciclo de revisión para esta evaluación; la decisión es del propietario.

## 8. AITL-REV-Approval

> **Avenga DevFlow §2.14, §3.0.** Esta Review permanece en draft hasta que un
> humano calificado registra `AITL-REV-Approval` (bloque `review` del
> frontmatter). La aprobación hace accionables los hallazgos; no aprueba
> ningún artefacto downstream.

| Field | Value |
|-------|-------|
| **Reviewer** | human:eugenioserrano (rol autoasignado: no hay otro titular) |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-27T02:28:00-03:00` |
| **review.started_at** | `2026-08-27T02:32:05-03:00` |
| **review.decided_at** | `2026-08-27T02:32:05-03:00` |
| **Findings** | Ninguno — aprobado sin comentarios (Plan B del action plan) |

---

## 9. History

| Date | Change | Author |
|------|--------|--------|
| 2026-08-27 | Initial review (draft) — medición de referencias y evaluación de ruido | @eugenioserrano |
| 2026-08-27 | **AITL-REV-Approval** — aprobado; Plan B (prefijos numéricos sin espacios con gaps) adoptado | @eugenioserrano |
| 2026-08-27 | **Cerrada** — hallazgos ruteados: F-01/F-02 → ADR-002 + BOLT-004 (Done); F-02 test de links → BOLT-004 (Done) | @eugenioserrano |
