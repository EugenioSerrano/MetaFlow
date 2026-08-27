---
id: "REV-003"
title: "Restos del linaje v5 y errores de adaptación en el kit (schema_version, placeholders, checkpoints, rutas de agentes)"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "closed"
scope: "distribution-kit/ — restos del linaje Avenga v5 y errores de adaptación MetaFlow v1.1 en texto normativo, agent definitions, READMEs, templates y ejemplos"
methodology: "revisión manual dirigida por greps de tokens del linaje v5 (schema_version 5.0, manifest v5, placeholders vacíos, prefijos de checkpoint, rutas *51-agents*) + validación de los TEMPLATE-MANIFEST-*.json contra los schemas v1 con jsonschema"
reviewed_artifacts:
  - "distribution-kit/metaflow/ai-sdlc/MetaFlow.md (§3.12, §3.15, §5.16, frontmatter)"
  - "distribution-kit/metaflow/23-metrics/README.md + manifest-v1-*.schema.json + TEMPLATE-MANIFEST-*.json"
  - "distribution-kit/metaflow/README.md, ONBOARDING.md, GUARDRAILS.md"
  - "distribution-kit/metaflow/{12-functional,24-tests,22-memory,21-spec,13-bugs,42-reports,51-agents,53-actors}/TEMPLATE-*.md"
  - "distribution-kit/AGENTS.md, CLAUDE.md, .agents/skills/ai-sdlc/SKILL.md, .github/agents/MetaFlow.agent.md, .opencode/agents/MetaFlow.md"
adrs_checked:
  - "devflow/adrs/ADR-001-toolkit-transformacion.md"
  - "devflow/adrs/ADR-003-ajuste-numeracion-32-adv-reviews.md"
specs_checked: []
review_ready_at: "2026-08-27T03:42:42-03:00"
review:
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "tech_lead"
      model: null
  started_at: "2026-08-27T03:44:19-03:00"
  decided_at: "2026-08-27T03:44:19-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Aprobación del propietario (rol autoasignado) sin hallazgos — 2026-08-27. Hallazgos accionables: F-01..F-15 → BUG-002..BUG-012 (a crear); F-08 puede requerir DISC/ADR al resolver el target de carpetas"
tags: [kit, revision, restos-migracion, schema-version, checkpoints, agentes]
---

# REV-003 — Restos del linaje v5 y errores de adaptación en el kit

| Field           | Value |
|-----------------|-------|
| **Scope**       | `distribution-kit/` — texto normativo, agent definitions, READMEs, templates y ejemplos |
| **Methodology** | Greps dirigidos de tokens del linaje v5 + validación JSON Schema (jsonschema 4.26.0) |
| **Criteria**    | Decisión del REV-002/BOLT-003 (familia de manifests **v1**, `schema_version: "1.0"`), checkpoints canónicos `CP-<CODE>-Approval` (G05), ubicación real de los wrappers de agentes, `content_language` del kit = `en` (OQ-001) |

---

## 1. Purpose

Verificar que el kit de salida no conserve restos del linaje Avenga v5 ni
errores de adaptación que el escáner del REV-002 no detectó. El REV-002
buscó patrones JSON (`"schema_version": "5.0"`, `v5.1`, `manifest-v5`) y
no cubrió texto markdown suelto, placeholders truncados, prefijos de
checkpoint no canónicos ni la discrepancia entre rutas documentadas y
reales de los wrappers de agentes.

## 2. Artifacts reviewed

| Artifact | Files | Notes |
|----------|-------|-------|
| Metodología normativa | `metaflow/ai-sdlc/MetaFlow.md` | §3.12 (familia de manifests), §3.15, §5.16 (migración), frontmatter |
| Métricas | `metaflow/23-metrics/README.md`, `manifest-v1-{task,us,tc}.schema.json`, `TEMPLATE-MANIFEST-*.json` | Los 5 JSON de ejemplo validan contra los schemas (`schema_version: "1.0"`) ✅ |
| Documentos raíz del kit | `metaflow/README.md`, `ONBOARDING.md`, `GUARDRAILS.md` | Checkpoint map, G05, rutas |
| Templates | `TEMPLATE-{US,TC,TASK,SPEC,MEM,BUG,ADR,DISC,REV,AREV,RISK,INC,RETRO,UAT,PROMPT}.md` | Vocabulario, schema_version, contratos |
| Agent definitions | `distribution-kit/AGENTS.md`, `CLAUDE.md`, `.agents/skills/ai-sdlc/SKILL.md`, `.github/agents/MetaFlow.agent.md`, `.opencode/agents/MetaFlow.md` | Sección Manifest Family, spawn topology, rutas |
| Reports | `metaflow/42-reports/README.md` | Template anunciado vs presente |

## 3. Severity legend

| Category | Meaning |
|----------|---------|
| **Compliant** | Implementado correctamente per ADR / estándar |
| **Documented deviation** | Diferencia justificada, registrada en MEM |
| **Minor gap** | Inconsistencia sin impacto funcional |
| **Major gap** | Problema que puede romper validación, instalación o lectura normativa |

---

## 4. Findings

### 4.1 — Familia de manifests: `schema_version` contradictorio (restos v5)

#### F-01 [Major gap] — §3.12 declara `schema_version` "5.0" y narra un rename corrupto

**Location:** `distribution-kit/metaflow/ai-sdlc/MetaFlow.md` líneas 3268 y 3272-3278

**Actual:** la regla normativa dice `schema_version is exactly 5.0 for this
family` y explica "(the v4→v5 change that renamed `checkpoint_approvals[]`
→ `checkpoint_approvals[]` and moved identity to the actor grammar)"; la
política de evolución dice "`4.x` keeps `4.0`, a schema change means `5.0`".

**Expected:** `schema_version` es exactamente `"1.0"` (lo que los schemas
`manifest-v1*.schema.json` exigen con `const: "1.0"` y lo que decidió
REV-002/BOLT-003: familia v1). El rename narrado "checkpoint_approvals →
checkpoint_approvals" es un resto del linaje Avenga (hitl_approvals →
checkpoint_approvals) sin sentido en MetaFlow.

**Impact:** la fuente normativa instruye un valor que **no valida** contra
los schemas del propio kit (G23); un agente que siga §3.12 crea manifests
rotos para los adoptantes.

**Recommendation:** reescribir §3.12 con la familia v1 (`"1.0"`, sin la
historia 4.x/5.0) y que el verificador del toolkit fije el const del
schema. → **BUG**.

#### F-02 [Major gap] — §5.16: sección de migración 4.0→5.0 corrupta

**Location:** `distribution-kit/metaflow/ai-sdlc/MetaFlow.md` líneas 4769-4783

**Actual:** "the approval array `checkpoint_approvals[]` becomes
`checkpoint_approvals[]`"; "re-expressed (`CP-<CODE>-Approval` →
`CP-<CODE>-Approval`)"; "because CITL ⊇ CITL"; "The v5 `checkpoint` enum
accepts **only** `CITL-*`; a v4 manifest validates against the frozen v4
schema, which keeps `CITL-*`"; "`schema_version` becomes `"5.0"`".

**Expected:** la §5.16 debe describir la conversión real de la familia v1
(agregar campos nuevos como `null`, aplicar renames, `schema_version`
queda `"1.0"`, checkpoints `CP-*`), o declarar explícitamente la historia
4.0→5.0 como narrativa del linaje previo no aplicable.

**Impact:** un adoptante que migre siguiendo §5.16 convierte sus manifests
a `schema_version "5.0"` y checkpoints `CITL-*` — ambos **invalidan**
contra los schemas v1/CP-* del kit; la migración queda rota.

**Recommendation:** reescribir la sección para la familia v1 y el
vocabulario `CP-*`. → **BUG**.

#### F-03 [Major gap] — Los 4 agent definitions instruyen `schema_version` "5.0"

**Location:** `CLAUDE.md:529`, `.agents/skills/ai-sdlc/SKILL.md:546`, `.github/agents/MetaFlow.agent.md:577`, `.opencode/agents/MetaFlow.md:557`

**Actual:** la sección "Manifest Family v5" de cada wrapper dice
"`schema_version` (exactly `"5.0"`) and `checkpoint_approvals[]` in all
three".

**Expected:** `"1.0"` (y el nombre de la familia corregido, ver F-05).

**Impact:** es la instrucción más ejecutable del kit: el agente instalado
en cada proyecto adoptante creará manifests con `schema_version: "5.0"`
que **fallan la validación G23** contra los schemas del kit.

**Recommendation:** corregir los 4 wrappers (o regenerarlos con el
toolkit). → **BUG**.

#### F-04 [Minor gap] — Contradicciones `"5.0"` vs `"1.0"` dentro de un mismo documento

**Location:** `metaflow/23-metrics/README.md:183` ("exactly `"5.0"`") vs su
línea 46 ("`"1.0"`"); `metaflow/12-functional/user-stories/TEMPLATE-US.md:47`
("schema_version \"5.0\"") vs su sección 8, línea 154 (`"1.0"`);
`metaflow/24-tests/test-cases/TEMPLATE-TC.md:42` ("\"5.0\"") vs su línea 126
(`"1.0"`).

**Actual:** el mismo documento da dos valores para `schema_version` en
secciones distintas.

**Expected:** `"1.0"` en todos lados (los schemas y los 5
`TEMPLATE-MANIFEST-*.json` — validados OK — usan `"1.0"`).

**Impact:** quien copie el template o lea el README puede crear un
manifest que no valida; confianza dañada en el kit.

**Recommendation:** unificar a `"1.0"`. → **BUG**.

#### F-05 [Minor gap] — Restos de naming "Manifest family v5" / "Schema family v5" / "manifest v5"

**Location:** `MetaFlow.md:2908, 2922, 2948, 3384`; `23-metrics/README.md:1, 177, 252`;
`metaflow/README.md:59, 177, 192, 377`; `GUARDRAILS.md:480`; `13-bugs/README.md:204`;
`ai-sdlc/INDEX.md:13`; `42-reports/README.md:45`; `.agents/skills/ai-sdlc/SKILL.md:3`
(descripción de la skill)

**Actual:** el nombre "Manifest family v5"/"Schema family v5"/"manifest
v5"/"Schema v5 example"/"the three v5 schemas" sobrevive en 8+ archivos
mientras la familia es v1 (`manifest-v1*.schema.json`, `schema_version:
"1.0"`).

**Expected:** "Manifest family v1" (o simplemente "manifest family").

**Impact:** naming contradictorio; el escáner del REV-002 no lo detectó
porque buscaba `v5.1`/`manifest-v5`/`"schema_version": "5.0"` literales.

**Recommendation:** rename del vocabulario en todos los archivos + test
del toolkit que fije "family v1" y cero "v5". → **BUG**.

### 4.2 — Checkpoints: placeholders truncados y prefijos no canónicos

#### F-06 [Major gap] — Placeholders vacíos "The  is invalid" (G05 ilegible)

**Location:** `CLAUDE.md:51`, `.github/agents/MetaFlow.agent.md:83`, `.opencode/agents/MetaFlow.md:67`,
`.agents/skills/ai-sdlc/SKILL.md:56`, `metaflow/README.md:244` ("the legacy  is invalid"),
`metaflow/ONBOARDING.md:70` ("The  is invalid (G05)"), `metaflow/GUARDRAILS.md:60`
(G05: "Use  (the ) or non-canonical `CITL-*` identifiers")

**Actual:** frases truncadas — la referencia al prefijo legacy (resto de la
migración AITL→CP) quedó **vacía** en 7 lugares, incluida la definición de
la regla G05 del GUARDRAILS.

**Expected:** nombrar el prefijo legacy explícitamente, p. ej. "the legacy
`AITL-*`/`HITL-*` prefix is invalid" / "Use a legacy checkpoint name (the
pre-v5 `AITL-*`/`HITL-*` prefix) or non-canonical identifiers".

**Impact:** la regla G05 — que un agente debe ENFORZAR — no se puede leer;
el checkpoint map del README y el ONBOARDING tienen frases rotas.

**Recommendation:** completar los 7 lugares. → **BUG**.

#### F-07 [Minor gap] — Prefijo `CITL-*` usado como nombre de checkpoint

**Location:** `metaflow/README.md:187-188` ("origin approved (CITL-US | CITL-BUG | CITL-TC |
CITL-DISC | CITL-REV | CITL-AREV-VERDICT | CITL-ADR)"), `metaflow/README.md:258`
("`CITL-AREV-{CRITIQUE,DEFENSE,VERDICT}-Approval`"), `metaflow/21-spec/TEMPLATE-SPEC.md:96`
("CITL-US / CITL-TC / CP-BUG-Approval")

**Actual:** tres lugares usan el prefijo `CITL-*` como nombre de checkpoint,
mientras el GUARDRAILS G05 (F-06) declara los identificadores `CITL-*` **no
canónicos** y el resto del kit usa `CP-<CODE>-Approval`.

**Expected:** `CP-US-Approval`, `CP-BUG-Approval`, `CP-TC-Approval`,
`CP-DISC-Approval`, `CP-REV-Approval`, `CP-AREV-CRITIQUE/DEFENSE/VERDICT-Approval`.

**Impact:** naming contradictorio dentro del propio kit; riesgo de
registrar aprobaciones con el prefijo equivocado.

**Recommendation:** unificar a `CP-*`. → **BUG**.

### 4.3 — Instalación de agentes: rutas documentadas vs reales

#### F-08 [Major gap] — Rutas `*51-agents*` documentadas; wrappers reales en `.agents/`, `.github/agents/`, `.opencode/agents/`

**Location:** `distribution-kit/AGENTS.md:11-12`; `metaflow/README.md:81`;
`metaflow/51-agents/VERIFICATION.md:68-69, 83, 96, 117, 144`;
`metaflow/51-agents/INDEX.md:10-11, 41-42`; `metaflow/51-agents/README.md:29`;
`metaflow/51-agents/squad/README.md:14-15`; `MetaFlow.md:4172-4173, 4253, 4734-4735, 4862`;
y el preamble de spawn topology de los 4 agent definitions (`CLAUDE.md:41`,
`.agents/skills/ai-sdlc/SKILL.md:46`, `.github/agents/MetaFlow.agent.md:73`,
`.opencode/agents/MetaFlow.md:57`)

**Actual:** la documentación dice que los wrappers de plataforma viven en
`.claude/51-agents/`, `.opencode/51-agents/`, `.github/51-agents/`,
`.codex/51-agents/` y `.51-agents/skills/` — pero los wrappers reales del
kit están en `.agents/skills/ai-sdlc/`, `.github/agents/` y
`.opencode/agents/` (renombrados en BOLT-002/REV-002 F-01).

**Expected:** la documentación (AGENTS.md, README, VERIFICATION.md, §5.2,
§5.16, preámbulos de spawn topology) debe describir la ubicación real que
cada herramienta lee, verificada a implementation time.

**Impact:** el Coordinator de un proyecto adoptante buscará/instalará los
wrappers en carpetas que la herramienta **no lee** — los agentes no se
registran y el spawn topology se rompe silenciosamente.

**Recommendation:** unificar doc y realidad (verificar la convención por
plataforma al corregir — puede requerir un DISC o una decisión ADR si hay
ambigüedad de target). → **BUG** (+ DISC/ADR al resolver).

#### F-09 [Minor gap] — NOTE de VS2026 apunta a `.github/51-agents/`

**Location:** `.github/agents/MetaFlow.agent.md:11`

**Actual:** el NOTE dice "Visual Studio 2026 reads this same file from
`.github/51-agents/`" mientras el archivo está en `.github/agents/`.

**Expected:** la nota debe reflejar la ubicación real (o la convención
decidida en F-08).

**Impact:** refuerza la confusión de F-08; el adoptante no sabe dónde
debe estar el archivo.

**Recommendation:** corregir junto con F-08. → **BUG** (mismo destino).

### 4.4 — Archivos faltantes y metadata del documento normativo

#### F-10 [Minor gap] — `TEMPLATE-REPORT.html` anunciado pero ausente

**Location:** `metaflow/42-reports/README.md:28`

**Actual:** el README presenta `TEMPLATE-REPORT.html` como "design
reference" con ejemplo de datos; el archivo **no existe** en
`42-reports/` (solo está el README).

**Expected:** el template presente (aunque sea el mockup) o el README
corregido para no anunciar un archivo inexistente.

**Impact:** referencia rota en el kit; el adoptante no encuentra el
design reference prometido.

**Recommendation:** incluir el archivo o ajustar el texto. → **BUG**.

#### F-11 [Minor gap] — Frontmatter del MetaFlow.md dice `version: "5.1"`

**Location:** `metaflow/ai-sdlc/MetaFlow.md:3`

**Actual:** el frontmatter YAML declara `version: "5.1"` mientras
`metaflow/VERSION` = `1.1` y 73 archivos del kit dicen "Methodology
version: 1.1".

**Expected:** `version: "1.1"`.

**Impact:** el documento normativo se autodeclara de otra versión; el
escáner del REV-002 buscó "v5.1"/"Methodology version: 5.x" y no detectó
el frontmatter YAML.

**Recommendation:** corregir el frontmatter + test del toolkit. → **BUG**.

#### F-12 [Minor gap] — Autor vacío en la cita del paper

**Location:** `metaflow/ai-sdlc/MetaFlow.md:184`

**Actual:** "based on the paper *"AI-Driven Development Life Cycle:
Reimagining Software Engineering"* by , Principal Solutions Architect at
AWS." — el nombre del autor quedó vacío.

**Expected:** nombre del autor del paper (o la atribución corregida).

**Impact:** cita incompleta en el documento normativo; resta credibilidad
y trazabilidad de la fuente.

**Recommendation:** completar la cita. → **BUG**.

### 4.5 — Ejemplos y contratos menores

#### F-13 [Minor gap] — TEMPLATE-MEM describe `delivery_loops[]` con 6 campos; el schema exige 8

**Location:** `metaflow/22-memory/TEMPLATE-MEM.md:40-41`

**Actual:** "(number, spec_revision, git_commit, execution_outcome,
code_generation, mem)" — omitidos `review_ready_at` y `review_started_at`.

**Expected:** los 8 campos requeridos (el `23-metrics/README.md:144` y
`GUARDRAILS.md:294-297` sí los listan).

**Impact:** el agente que siga el template del MEM puede omitir 2 campos
requeridos → manifest inválido (G23).

**Recommendation:** completar la lista. → **BUG**.

#### F-14 [Minor gap] — Comentario en español en el ejemplo inline de §3.12

**Location:** `metaflow/ai-sdlc/MetaFlow.md:3156`

**Actual:** `"comment": "Agregar manejo explícito de concurrencia."` — el
`content_language` del kit es `en` (OQ-001; `metaflow/LANGUAGE` = `en`); el
`TEMPLATE-MANIFEST-TASK.json` equivalente usa "Add explicit concurrency
handling.".

**Expected:** comentario en inglés, consistente con el resto del ejemplo.

**Impact:** inconsistencia de idioma en el ejemplo normativo.

**Recommendation:** traducir el comentario. → **BUG**.

#### F-15 [Minor gap] — Ejemplo de agent con paths del repo de distribución

**Location:** `metaflow/51-agents/examples/developer/agent.yaml:19`

**Actual:** `write_paths: []  # the product tree (distribution-kit/, tools/) +
governed records` — referencia a carpetas del repo de distribución, no de
un proyecto adoptante.

**Expected:** el ejemplo debe hablar de la estructura del proyecto
adoptante (p. ej. `src/` + `metaflow/`), o dejar el comentario genérico.

**Impact:** confusión para quien copia el ejemplo en su proyecto (esas
carpetas no existen ahí).

**Recommendation:** ajustar el comentario del ejemplo. → **BUG**.

---

## 5. Summary

El REV-002 dejó el kit con identidad, versión (1.1), JSONs, índices y
links impecables, y la familia de manifests **v1** quedó fijada en
schemas y templates JSON (los 5 `TEMPLATE-MANIFEST-*.json` validan contra
los schemas). Pero **quedaron restos del linaje v5 y errores de
adaptación** que el escáner del REV-002 no detectó por buscar patrones
JSON/versión literales: `schema_version "5.0"` y una sección de migración
corrupta en el propio MetaFlow.md (§3.12/§5.16), `"5.0"` en los 4 agent
definitions, 7 placeholders truncados (incluida la regla G05), 3 usos del
prefijo no canónico `CITL-*`, rutas `*51-agents*` que no coinciden con los
wrappers reales, un `TEMPLATE-REPORT.html` anunciado pero ausente, y
varios menores (frontmatter `5.1`, autor vacío, 6-vs-8 campos, idioma y
paths de ejemplos). Los hallazgos F-01/F-02/F-03/F-06/F-08 pueden romper
la operación de los adoptantes (manifests que no validan, G05 ilegible,
agentes que no se instalan).

## 6. Action plan

> Aplica solo después de `AITL-REV-Approval`. Cada destino sigue su propio
> ciclo y aprobación (código → BUG aprobado → Bolt dedicado, T10/T02).

| # | Finding | Severity | Action | Routes to |
|---|---------|----------|--------|-----------|
| 1 | F-01    | Major    | Reescribir §3.12 a familia v1 + test del toolkit que fije `"1.0"` | BUG → Bolt (US-001) |
| 2 | F-02    | Major    | Reescribir §5.16 a familia v1 / vocabulario `CP-*` | BUG → Bolt (US-001) |
| 3 | F-03    | Major    | Corregir `"5.0"` → `"1.0"` en los 4 agent definitions (o regenerar) | BUG → Bolt (US-001) |
| 4 | F-04    | Minor    | Unificar `"1.0"` en 23-metrics/README, TEMPLATE-US, TEMPLATE-TC | BUG → Bolt (US-001) |
| 5 | F-05    | Minor    | Rename "Manifest family v5"/"Schema v5" → v1 + test de cero "v5" | BUG → Bolt (US-001) |
| 6 | F-06    | Major    | Completar los 7 placeholders + G05 (nombrar el prefijo legacy) | BUG → Bolt (US-001) |
| 7 | F-07    | Minor    | Unificar `CITL-*` → `CP-*` en README y TEMPLATE-SPEC | BUG → Bolt (US-001) |
| 8 | F-08    | Major    | Unificar rutas de agentes; verificar convención por plataforma | BUG → Bolt (US-001) + DISC/ADR si hay ambigüedad de target |
| 9 | F-09    | Minor    | Corregir NOTE de VS2026 (junto con F-08) | BUG → Bolt (US-001) |
| 10 | F-10    | Minor    | Incluir `TEMPLATE-REPORT.html` o corregir el README | BUG → Bolt (US-001) |
| 11 | F-11    | Minor    | Frontmatter `version: "1.1"` + test | BUG → Bolt (US-001) |
| 12 | F-12    | Minor    | Completar autor del paper | BUG → Bolt (US-001) |
| 13 | F-13    | Minor    | Listar los 8 campos de `delivery_loops[]` en TEMPLATE-MEM | BUG → Bolt (US-001) |
| 14 | F-14    | Minor    | Traducir comentario del ejemplo §3.12 a `en` | BUG → Bolt (US-001) |
| 15 | F-15    | Minor    | Ajustar `write_paths` del ejemplo de agent | BUG → Bolt (US-001) |

## 7. Conclusions

El kit no está listo para publicarse tal cual: los restos del linaje v5
(F-01..F-05) contradicen la familia v1 ya fijada, los placeholders
(F-06) rompen la lectura de la regla G05, y las rutas de agentes (F-08)
describen una instalación que no coincide con los wrappers reales. La
corrección es mecánica (texto + regeneración con el toolkit) y se puede
cubrir con BUGs dedicados + Bolts bajo US-001. Se recomienda re-correr la
E2E/REV tras el fix para confirmar cero restos del linaje.

## 8. AITL-REV-Approval

> **Avenga DevFlow §2.14, §3.0.** Esta Review permanece en draft hasta que
> un humano calificado registra `AITL-REV-Approval` (bloque `review` del
> frontmatter). La aprobación hace accionables los hallazgos; no aprueba
> ningún artefacto downstream — cada BUG/Bolt sigue su propio ciclo.

| Field | Value |
|-------|-------|
| **Reviewer** | human:eugenioserrano (rol autoasignado: no hay otro titular) |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-27T03:42:42-03:00` |
| **review.started_at** | `2026-08-27T03:44:19-03:00` |
| **review.decided_at** | `2026-08-27T03:44:19-03:00` |
| **Findings** | Ninguno — aprobado sin comentarios |

---

## 9. History

| Date | Change | Author |
|------|--------|--------|
| 2026-08-27 | Initial review (draft) — restos del linaje v5 y errores de adaptación | @eugenioserrano |
| 2026-08-27 | **AITL-REV-Approval** — aprobado; F-01..F-15 → BUG-002..BUG-012 (a crear); F-08 puede requerir DISC/ADR | @eugenioserrano |
| 2026-08-27 | **Cerrada** — hallazgos ruteados y ejecutados: BUG-002..BUG-012 aprobados → BOLT-007..017 (AITL-BOLT-DONE-Approval 2026-08-27, Done); kit regenerado con cero restos; BUGs fixed | @eugenioserrano |
