---
id: "REV-004"
title: "Análisis fresco del kit regenerado: sección de migración corrupta en agent definitions, G05 de wrappers, tautologías CITL y anuncios residuales"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "closed"
scope: "distribution-kit/ regenerado (corrida 20260827-102126) — agent definitions, MetaFlow.md §3.0/§5.12/§5.16, GUARDRAILS, READMEs, 24-tests"
methodology: "revisión independiente del kit regenerado con greps de contexto amplio (v5 suelto, CITL-* con asterisco, tautologías CITL, anuncios de archivos ausentes, placeholders {{ }}, TODO/TBD, acentos) + verificación del árbol vs folder map"
reviewed_artifacts:
  - "distribution-kit/CLAUDE.md, .agents/skills/ai-sdlc/SKILL.md, .github/agents/MetaFlow.agent.md, .opencode/agents/MetaFlow.md"
  - "distribution-kit/metaflow/ai-sdlc/MetaFlow.md (§3.0, §5.12, §5.16)"
  - "distribution-kit/metaflow/GUARDRAILS.md (G05, T12)"
  - "distribution-kit/metaflow/README.md, 42-reports/README.md, 24-tests/test-cases/README.md"
  - "Árbol del kit vs folder map del README"
adrs_checked:
  - "metaflow/11-adrs/ADR-001-toolkit-transformacion.md"
  - "metaflow/11-adrs/ADR-003-ajuste-numeracion-32-adv-reviews.md"
specs_checked:
  - "metaflow/21-spec/SPEC-260827-0355-bolt007-fix-schema-version-metodologia.md"
  - "metaflow/21-spec/SPEC-260827-0355-bolt011-fix-placeholders-g05.md"
  - "metaflow/21-spec/SPEC-260827-0355-bolt014-fix-template-report.md"
review_ready_at: "2026-08-27T10:25:00-03:00"
review:
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "tech_lead"
      model: null
  started_at: "2026-08-27T10:25:37-03:00"
  decided_at: "2026-08-27T10:25:37-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Aprobación del propietario (rol autoasignado) sin hallazgos — 2026-08-27. Hallazgos accionables: F-01..F-07 → BUG-013..BUG-019 (a crear)"
tags: [kit, revision, agentes, citl, migracion, restos]
---

# REV-004 — Análisis fresco del kit regenerado (coherencia)

| Field           | Value |
|-----------------|-------|
| **Scope**       | `distribution-kit/` regenerado (corrida 20260827-102126) |
| **Methodology** | Greps de contexto amplio (v5 suelto, CITL-*, tautologías, anuncios de archivos ausentes, placeholders, acentos) + árbol vs folder map |
| **Criteria**    | Coherencia interna del kit: vocabulario canónico (CP-*/v1/CITL como concepto), sin narrativas corruptas, sin anuncios de archivos inexistentes, árbol coherente |

---

## 1. Purpose

Revisar el kit regenerado con una mirada fresca e independiente de los fixes
de TASK-007..017: buscar incoherencias que los tests de reproducción no
cubren (porque verifican patrones puntuales del BUG, no el texto completo
del kit). El objetivo es confirmar — o refutar — que el kit es coherente de
punta a punta antes de considerarlo publicable.

## 2. Artifacts reviewed

| Artifact | Files | Notes |
|----------|-------|-------|
| Agent definitions | `CLAUDE.md`, `.agents/skills/ai-sdlc/SKILL.md`, `.github/agents/MetaFlow.agent.md`, `.opencode/agents/MetaFlow.md` | Sección de migración condensada y G05 interno |
| Metodología | `metaflow/ai-sdlc/MetaFlow.md` | §3.0 (charter CITL), §5.12 (reports), §5.16 (migración) |
| Guardrails | `metaflow/GUARDRAILS.md` | G05, T12 |
| READMEs | `metaflow/README.md`, `42-reports/README.md`, `24-tests/test-cases/README.md` | Anuncios de archivos ausentes, vocabulario |
| Árbol | `distribution-kit/metaflow/` | 20 carpetas numeradas + ai-sdlc; folder map del README |

## 3. Severity legend

| Category | Meaning |
|----------|---------|
| **Compliant** | Implementado correctamente per ADR / estándar |
| **Documented deviation** | Diferencia justificada, registrada en MEM |
| **Minor gap** | Inconsistencia sin impacto funcional |
| **Major gap** | Problema que puede romper lectura normativa o confundir al agente adoptante |

---

## 4. Findings

### 4.1 — Agent definitions: sección de migración y G05 internos corruptos

#### F-01 [Major gap] — Sección de migración condensada corrupta en los 4 agent definitions

**Location:** `CLAUDE.md`, `.agents/skills/ai-sdlc/SKILL.md`, `.github/agents/MetaFlow.agent.md`, `.opencode/agents/MetaFlow.md` (sección de migración §5.16 condensada)

**Actual:** el texto dice: "`4.0` → `5.0` renames `checkpoint_approvals[]` → `checkpoint_approvals[]` and reshapes each entry (...; checkpoint names re-expressed `CITL-*`→`CITL-*` — decision immutable, the v5 enum is `CITL-*`-only, v4 history stays in the frozen v4 schema, G36)". Incluye además "`3.0` → `4.0` is exactly that" (historia del linaje).

**Expected:** sin renames corruptos (`checkpoint_approvals[]` → `checkpoint_approvals[]`), sin "re-expressed `CITL-*`→`CITL-*`" ni "v5 enum is `CITL-*`-only" — vocabulario consistente con la familia v1 y los checkpoints `CP-*` (o la historia del linaje declarada explícitamente como no aplicable).

**Impact:** el agente instalado en proyectos adoptantes lee una narrativa sin sentido y contradictoria con su propio vocabulario (v5/CITL-* vs v1/CP-*) en la sección que instruye cómo migrar manifests.

**Recommendation:** reglas del diccionario para la versión condensada de los wrappers (patrones propios, no los del MetaFlow.md) + test que cubra los 4 wrappers. → **BUG → TASK**.

#### F-02 [Major gap] — G05 interno de los 4 agent definitions corrupto

**Location:** `CLAUDE.md`, `.agents/skills/ai-sdlc/SKILL.md`, `.github/agents/MetaFlow.agent.md`, `.opencode/agents/MetaFlow.md` (tabla de guardrails interna)

**Actual:** "| G05 | Legacy checkpoint names (the ) or any non-canonical `CITL-*` identifier (canonical is `CITL-*`; `CITL-*` , G36) |" — placeholder "(the )" vacío y "(canonical is `CITL-*`; `CITL-*` , G36)" erróneo (el prefijo canónico es `CP-*`, no `CITL-*`).

**Expected:** la versión corregida del GUARDRAILS.md ("Use a legacy checkpoint name (the pre-v5 checkpoint prefix) or non-canonical identifiers" / "Canonical checkpoints are `CP-<CODE>-Approval`...").

**Impact:** la regla G05 que el agente debe ENFORCE queda ilegible y con el canónico mal declarado en el propio agente.

**Recommendation:** reglas para la variante del G05 de los wrappers + test. → **BUG → TASK**.

### 4.2 — MetaFlow.md: tautologías del fundamento CITL

#### F-03 [Major gap] — "CITL is the default case of CITL" (tautología)

**Location:** `metaflow/ai-sdlc/MetaFlow.md` §3.0 (dos ocurrencias)

**Actual:** "**Checkpoint-in-the-Loop (CITL) is the default case of CITL** (actor = human), not a separate paradigm" y "**CITL is the default case inside CITL** (actor = human)".

**Expected:** "**Human-in-the-Loop is the default case inside CITL** (actor = human), not a separate paradigm" (o una redacción con sentido: el caso por defecto del checkpoint es un humano).

**Impact:** el fundamento del framework (CITL / actor por defecto) queda definido por una tautología sin significado — daña la lectura del charter.

**Recommendation:** regla del diccionario para las dos frases + test. → **BUG → TASK**.

### 4.3 — Anuncios residuales y vocabulario suelto

#### F-04 [Minor gap] — TEMPLATE-REPORT.html sigue anunciado en MetaFlow.md §5.12 y README.md

**Location:** `metaflow/ai-sdlc/MetaFlow.md` §5.12 ("`TEMPLATE-REPORT.html` ships as a design reference with example data"); `metaflow/README.md` (Known Limitations: "`42-reports/TEMPLATE-REPORT.html` ships as a design reference")

**Actual:** el archivo no existe en el kit (decisión TASK-014: opción B) pero dos documentos más lo anuncian como presente — solo se corrigió `42-reports/README.md`.

**Expected:** ninguna mención que anuncie el archivo como presente (o el archivo incluido).

**Impact:** referencia rota persistente en la metodología y el README raíz del kit.

**Recommendation:** reglas para las dos menciones + test ampliado. → **BUG → TASK**.

#### F-05 [Minor gap] — "`CITL-*`" usado como nombre de checkpoint

**Location:** `metaflow/24-tests/test-cases/README.md` ("`CITL-*` codes are never translated"); `metaflow/GUARDRAILS.md` T12 ("each artifact's `CITL-*` decision")

**Actual:** el prefijo `CITL-*` (no canónico como nombre de checkpoint, G05) se usa para referirse a los checkpoints.

**Expected:** "`CP-*-Approval` codes are never translated" / "each artifact's `CP-*` decision" (o "CITL decision" como concepto).

**Impact:** vocabulario contradictorio con el G05 del propio kit.

**Recommendation:** reglas + test (extender el patrón del test a `CITL-\*`). → **BUG → TASK**.

#### F-06 [Minor gap] — G05 del GUARDRAILS: "the pre-v5 `CITL-*` names"

**Location:** `metaflow/GUARDRAILS.md` G05 ("Legacy prefixes — the pre-v5 `CITL-*` names, preserved only in migrated history (G36) — are invalid")

**Actual:** el "prefijo legacy" se nombra como `CITL-*` — pero CITL es el concepto ACTUAL del kit (Checkpoint-in-the-Loop); los prefijos legacy del linaje eran AITL/HITL (que no pueden nombrarse: tokens prohibidos).

**Expected:** "the pre-v5 legacy checkpoint names" (sin nombrar CITL-* como legacy).

**Impact:** confusión conceptual: el kit declara legacy algo que es su concepto vigente.

**Recommendation:** regla + test. → **BUG → TASK**.

#### F-07 [Minor gap] — §5.16: narrativa del linaje previo mezclada con el presente del kit

**Location:** `metaflow/ai-sdlc/MetaFlow.md` §5.16 ("`3.0` → `4.0` is exactly this shape... `4.0` → `5.0` is a rename... The v1 `checkpoint` enum accepts **only** `CP-*`...")

**Actual:** la sección narra migraciones del linaje Avenga (3.0→4.0→5.0) que un adoptante de MetaFlow v1.1 nunca vivirá, mezcladas con el presente del kit ("v1 enum accepts only CP-*"; "schema_version becomes `"1.0"`" dentro de la historia 4.0→5.0).

**Expected:** declarar explícitamente la historia 3.0→5.0 como narrativa del linaje previo no aplicable a MetaFlow v1.1, y describir la conversión real de la familia v1 (o eliminar la historia).

**Impact:** semántica confusa para un adoptante que migra; el texto mezcla dos mundos.

**Recommendation:** reescribir la apertura de la conversión para la familia v1 (declarando el linaje como historia) + test. → **BUG → TASK**.

### 4.4 — Verificaciones que quedaron OK (Compliant)

- Árbol del kit: 20 carpetas numeradas + `ai-sdlc` coherente con el folder map; `bin/` anunciado como "optional/reserved" y ausente — coherente con el texto (llega con el tooling track).
- Placeholders `{{ persona }}`, `{{ persona_type }}`, `{{ milestone }}` — legítimos de templates de análisis.
- `TODO` (open-questions/README) y `ADR-XXX` (TEMPLATE-ADR) — ejemplos intencionales de formato.
- Textos con acentos/ñ — solo menciones de la política de idioma y el ejemplo ES del vision/README (intencional).
- Cero restos de los BUG-002..012 ya corregidos (verificados por `test_restos_v5` + escaneo final).

## 5. Summary

El kit regenerado es **mayormente coherente**: árbol, templates, schemas,
manifests y vocabulario principal (CP-*, v1, Delivery Loops, TASKs) están
consistentes, y los restos de los BUG-002..012 no reaparecieron. Pero el
análisis fresco encontró **3 hallazgos Major que los tests no cubrían**
porque viven en los agent definitions y en el charter CITL: la sección de
migración condensada de los 4 wrappers quedó corrupta (F-01), su G05
interno quedó ilegible y con el canónico mal declarado (F-02), y el
fundamento CITL quedó definido por tautologías (F-03). Se suman 4 hallazgos
menores de anuncios residuales y vocabulario suelto (F-04..F-07). El patrón
común: los tests de reproducción verifican patrones del MetaFlow.md pero no
las variantes condensadas de los wrappers ni las frases del charter.

## 6. Action plan

> Aplica solo después de `CP-REV-Approval`. Cada destino sigue su propio
> ciclo y aprobación (código → BUG aprobado → TASK dedicado, T10/T02).

| # | Finding | Severity | Action | Routes to |
|---|---------|----------|--------|-----------|
| 1 | F-01    | Major    | Reglas para la sección de migración condensada de los 4 wrappers + test que cubra los wrappers | BUG → TASK (US-001) |
| 2 | F-02    | Major    | Reglas para el G05 interno de los wrappers + test | BUG → TASK (US-001) |
| 3 | F-03    | Major    | Regla para las 2 tautologías CITL en §3.0 + test | BUG → TASK (US-001) |
| 4 | F-04    | Minor    | Reglas para las 2 menciones de TEMPLATE-REPORT en MetaFlow.md y README.md + test ampliado | BUG → TASK (US-001) |
| 5 | F-05    | Minor    | Reglas para "`CITL-*` codes"/"`CITL-*` decision" + test extendido a `CITL-\*` | BUG → TASK (US-001) |
| 6 | F-06    | Minor    | Regla para "the pre-v5 `CITL-*` names" del G05 + test | BUG → TASK (US-001) |
| 7 | F-07    | Minor    | Reescribir la apertura de la conversión §5.16 (historia del linaje declarada) + test | BUG → TASK (US-001) |

## 7. Conclusions

El kit está cerca de publicable pero **todavía no del todo**: los 3
hallazgos Major (F-01/F-02/F-03) afectan directamente a los agentes que el
kit instala (su sección de migración y su G05) y al fundamento del
framework (charter CITL). Con BUGs dedicados + TASKs bajo US-001 (mismo
patrón que TASK-007..017: reglas del diccionario + tests + regeneración) el
kit quedaría coherente de punta a punta. Se recomienda además ampliar
`test_restos_v5` para cubrir los wrappers y el charter en la misma ronda.

## 8. CP-REV-Approval

> **MetaFlow §2.14, §3.0.** Esta Review permanece en draft hasta que
> un humano calificado registra `CP-REV-Approval` (bloque `review` del
> frontmatter). La aprobación hace accionables los hallazgos; no aprueba
> ningún artefacto downstream.

| Field | Value |
|-------|-------|
| **Reviewer** | human:eugenioserrano (rol autoasignado: no hay otro titular) |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-27T10:25:00-03:00` |
| **review.started_at** | `2026-08-27T10:25:37-03:00` |
| **review.decided_at** | `2026-08-27T10:25:37-03:00` |
| **Findings** | Ninguno — aprobado sin comentarios |

---

## 9. History

| Date | Change | Author |
|------|--------|--------|
| 2026-08-27 | Initial review (draft) — análisis fresco del kit regenerado | @eugenioserrano |
| 2026-08-27 | **CP-REV-Approval** — aprobado; F-01..F-07 → BUG-013..BUG-019 (a crear) | @eugenioserrano |
| 2026-08-27 | **Cerrada** — hallazgos ruteados y ejecutados: BUG-013..019 aprobados → TASK-018..024 (CP-TASK-DONE-Approval 2026-08-27, Done); kit regenerado con cero restos; BUGs fixed | @eugenioserrano |
