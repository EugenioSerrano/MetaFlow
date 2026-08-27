---
id: "REV-002"
title: "Revisión integral de consistencia del kit (agentes, READMEs, templates, JSONs, schemas)"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "closed"
scope: "distribution-kit/ completo — agentes, READMEs, templates, JSONs, schemas, índices, markers"
methodology: "escáner integral (tokens, versiones, referencias viejas, JSON parse, schemas, índices, markers) + medición de sobre-match en prosa + chequeos puntuales"
reviewed_artifacts:
  - "distribution-kit/** (149 archivos: md/json/yaml/html/txt)"
  - "distribution-kit/metaflow/manifest-v1-*.schema.json"
  - "distribution-kit/.agents, .github, .opencode (wrappers de agentes)"
  - "mapping.json (reglas N de numeración)"
adrs_checked:
  - "devflow/adrs/ADR-002-numeracion-carpetas-kit.md"
specs_checked:
  - "devflow/spec/SPEC-260827-0239-bolt004-numeracion-carpetas.md"
review_ready_at: "2026-08-27T02:49:14-03:00"
review:
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "tech_lead"
      model: null
  started_at: "2026-08-27T02:51:33-03:00"
  decided_at: "2026-08-27T02:51:33-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Aprobación del propietario (rol autoasignado) sin hallazgos — 2026-08-27. Hallazgos accionables: F-04/F-05 → BOLT-005; F-06 → ADR-003 + BOLT-005"
tags: [kit, consistencia, revision, numeracion]
---

# REV-002 — Revisión integral de consistencia del kit

| Field           | Value |
|-----------------|-------|
| **Scope**       | `distribution-kit/` completo (agentes, READMEs, templates, JSONs, schemas, índices, markers) |
| **Methodology** | Escáner integral + medición de sobre-match en prosa + chequeos puntuales (2026-08-27) |
| **Criteria**    | ADR-002 (numeración), O1 (identidad), AC-1 (equivalencia), consistencia de vocabulario y de links |

---

## 1. Purpose

Verificar que el kit de salida no tenga inconsistencias tras los 4 Bolts de
la US-001: identidad (cero tokens de marca), versionado (1.1/familia v1),
numeración de carpetas (ADR-002), vocabulario en agentes/templates/schemas,
JSONs válidos, índices consistentes y links sanos.

## 2. Artifacts reviewed

| Artifact | Files | Notes |
|----------|-------|-------|
| Kit completo | 149 archivos (md/json/yaml/html/txt) | Escáner de tokens/versiones/refs viejas/JSON parse |
| Schemas de manifests | `manifest-v1-{task,tc,us}.schema.json` | IDs, const, enums, leftovers |
| Wrappers de agentes | `.agents/`, `.github/`, `.opencode/` | Nombres, versiones, paths |
| Templates | `TEMPLATE-*.md` + `TEMPLATE-MANIFEST-*.json` | Vocabulario nuevo, schema_version |
| Índices | `INDEX.md` del kit | Links internos resuelven |
| Reglas de numeración | `mapping.json` (N01–N53, PN01–PN53) | Sobre-match en prosa |

## 3. Severity legend

| Category | Meaning |
|----------|---------|
| **Compliant** | Implementado correctamente per ADR / estándar |
| **Documented deviation** | Diferencia justificada, registrada en MEM |
| **Minor gap** | Inconsistencia sin impacto funcional |
| **Major gap** | Problema que puede causar errores de runtime o romper validación |

## 4. Findings

### 4.1 — Identidad, versión, JSONs, links (todo OK)

#### F-01 [Compliant] — Identidad y tokens

**Actual:** 0 tokens prohibidos (`Avenga`, `devflow`, `AITL`, `HITL`, `Bolt`,
`V-Bounce`, `v_bounces`, `Raja`, `DORA`) en nombres y contenido de TODOS los
tipos de archivo; markers `METAFLOW:PROJECT-SECTION` correctos; wrappers
renombrados (`MetaFlow.agent.md`, `MetaFlow.md`, `.agents/skills/ai-sdlc/`).

#### F-02 [Compliant] — Versión y familia de manifests

**Actual:** 73 archivos con `**Methodology version:** 1.1` (ninguno con 5.x);
0 × `v5.1`/`manifest-v5`/`"schema_version": "5.0"`; schemas con
`$id: urn:metaflow:metaflow:manifest:…:v1` y `const: "1.0"`; templates de
manifests con `schema_version: 1.0`; VERSION = 1.1.

#### F-03 [Compliant] — JSONs válidos, índices y links

**Actual:** todos los `.json` parsean; los links de `INDEX.md` resuelven; 0
links reales rotos (test_links); las 20 carpetas numeradas + `ai-sdlc`.

### 4.2 — Sobre-match de las reglas de numeración (N-rules)

#### F-04 [Major gap] — 1224 corrupciones de prosa por sobre-match de las N-rules

**Location:** contenido del kit (medición 2026-08-27)

**Actual:** las reglas de contenido `(?<![\w-])<nombre>(?![\w-])` numeran la
**palabra suelta**, no solo referencias de ruta. Resultado en el kit:
`12-functional analyst`, `12-functional TASK`, `12-functional Bolt` (254×),
`run existing 24-tests` (222×), `02-analysis artifacts` (176×),
`role 51-agents` (115×), `33-risks` (106×), `flow 23-metrics` (87×),
`01-input` como sustantivo (80×), `22-memory` (59×), `53-actors` (46×),
`31-reviews` (35×), `41-prompts` (24×), `34-incidents` (23×), `42-reports`
(21×), `21-spec` (9×), `03-discovery` (7×), `13-bugs` (6×), `11-adrs` (2×),
`35-retros` (1×). **Total: 1224 corrupciones** en prosa.

**Expected:** solo las **referencias de ruta** (`nombre/`) deben numerarse;
las palabras de vocabulario ("functional", "tests", "memory", "risks"…)
deben quedar intactas.

**Impact:** el kit quedó con vocabulario corrompido en agentes, READMEs y
templates — daña la calidad percibida y la consistencia del lenguaje.

**Recommendation:** reescribir las reglas de contenido para exigir la barra:
`(?<![\w-])<nombre>/` → `NN-<nombre>` (las substrings `business-risks/`,
`adversarial-reviews/`, `agents-data/` siguen protegidas por el lookbehind) →
**BOLT-005**.

#### F-05 [Major gap] — Enum del schema corrompido: `"functional"` → `"12-functional"`

**Location:** `distribution-kit/metaflow/23-metrics/manifest-v1-task.schema.json` (bolt.type enum)

**Actual:** el enum `["functional", "non-functional", "test"]` quedó como
`["12-functional", "non-functional", "test"]` (N12 numeró "functional";
"non-functional" quedó intacto por el lookbehind del guion).

**Expected:** el enum debe ser `["functional", "non-functional", "test"]` —
es vocabulario de tipos, no una referencia de carpeta.

**Impact:** un manifest con `"type": "functional"` **no valida** contra el
schema del kit (rompe la validación de manifests de los adoptantes).

**Recommendation:** mismo fix que F-04 (la regla con barra no toca el enum) +
test que fije el enum → **BOLT-005**.

#### F-06 [Minor gap] — Nombre de la carpeta 32 (decisión del propietario)

**Location:** esquema ADR-002

**Actual:** `32-adversarial-reviews` (largo).

**Expected:** `32-adv-reviews` (decisión del propietario 2026-08-27).

**Impact:** cosmético; requiere actualizar el esquema (ADR) y el diccionario.

**Recommendation:** **ADR-003** (supersede ADR-002) + aplicación en BOLT-005.

## 5. Summary

La identidad, el versionado, los JSONs, los índices y los links del kit están
**impecables** (0 tokens, 1.1 en todo, familia v1, JSONs válidos, 0 links
rotos). Pero la **numeración por palabras sueltas** de las N-rules produjo
**1224 corrupciones de prosa** y **rompió el enum del schema** de manifests
(F-04/F-05) — un defecto real que debe corregirse antes de considerar el kit
publicable. Se suma la decisión del propietario de acortar la carpeta 32
(F-06).

## 6. Action plan

> Aplica solo después de `AITL-REV-Approval`. Cada destino sigue su propio
> ciclo y aprobación.

| # | Finding | Severity | Action | Routes to |
|---|---------|----------|--------|-----------|
| 1 | F-04    | Major    | Reescribir N-rules con barra obligatoria (`nombre/`) + regenerar kit + test de prosa intacta | BOLT-005 (US-001) |
| 2 | F-05    | Major    | Fix del enum del schema + test que fija `["functional","non-functional","test"]` | BOLT-005 (US-001) |
| 3 | F-06    | Minor    | Rename `32-adv-reviews` (decisión del propietario) | ADR-003 + BOLT-005 |

## 7. Conclusions

El kit tiene una base excelente (identidad, versión, links) pero **no es
publicable todavía**: el sobre-match de la numeración corrompió prosa y
schemas. Con BOLT-005 (N-rules con barra + enum fix + rename 32) y ADR-003 el
kit queda consistente. Se recomienda re-correr la REV (o la E2E) tras el fix.

## 8. AITL-REV-Approval

> **Avenga DevFlow §2.14, §3.0.** Esta Review permanece en draft hasta que un
> humano calificado registra `AITL-REV-Approval` (bloque `review` del
> frontmatter).

| Field | Value |
|-------|-------|
| **Reviewer** | human:eugenioserrano (rol autoasignado: no hay otro titular) |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-27T02:49:14-03:00` |
| **review.started_at** | `2026-08-27T02:51:33-03:00` |
| **review.decided_at** | `2026-08-27T02:51:33-03:00` |
| **Findings** | Ninguno — aprobado sin comentarios |

---

## 9. History

| Date | Change | Author |
|------|--------|--------|
| 2026-08-27 | Initial review (draft) — escáner integral + medición de sobre-match | @eugenioserrano |
| 2026-08-27 | **AITL-REV-Approval** — aprobado; F-04/F-05 → BOLT-005, F-06 → ADR-003 | @eugenioserrano |
| 2026-08-27 | **Cerrada** — hallazgos ruteados: F-04/F-05/F-06 → ADR-003 + BOLT-005 (Done); kit verificado consistente | @eugenioserrano |
