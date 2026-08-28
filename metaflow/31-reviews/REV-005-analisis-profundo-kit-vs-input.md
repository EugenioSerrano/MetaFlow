---
id: "REV-005"
title: "Análisis profundo del distribution-kit vs input-kit: historia del linaje no declarada, shorthands de checkpoints no canónicos y declaración de propiedad con entidad inexistente"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "closed"
scope: "distribution-kit/ (corrida 20260827-165601) comparado contra input-kit/ (AvengaDevFlow v5.1): texto completo, links, árbol, schemas, agent definitions, vocabulario"
methodology: "comparación sistemática input→output: escaneo de tokens del linaje viejo (case-insensitive), artefactos de reemplazo mecánico, versiones de linaje, integridad de links, paridad de los 4 agent definitions, round-trip schema↔templates, coherencia árbol↔README, spot-checks semánticos"
reviewed_artifacts:
  - "distribution-kit/metaflow/ai-sdlc/MetaFlow.md (completo — 4900+ líneas)"
  - "distribution-kit/metaflow/{README,ONBOARDING,GUARDRAILS}.md"
  - "distribution-kit/metaflow/23-metrics/README.md, 42-reports/README.md"
  - "distribution-kit/metaflow/24-tests/README.md, 24-tests/uat/*, 02-analysis/README.md"
  - "distribution-kit/CLAUDE.md, .agents/skills/ai-sdlc/SKILL.md, .github/agents/MetaFlow.agent.md, .opencode/agents/MetaFlow.md"
  - "distribution-kit/metaflow/23-metrics/manifest-v1-*.schema.json + TEMPLATE-MANIFEST-*.json"
  - "input-kit/devflow/** (equivalentes del linaje original para cada punto)"
adrs_checked:
  - "metaflow/11-adrs/ADR-001-toolkit-transformacion.md"
  - "metaflow/11-adrs/ADR-003-ajuste-numeracion-32-adv-reviews.md"
specs_checked:
  - "metaflow/21-spec/SPEC-260827-1628-front-door-raiz.md"
  - "metaflow/21-spec/SPEC-260827-1029-fix-516-linaje.md"
review_ready_at: "2026-08-27T17:04:54-03:00"
review:
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "tech_lead"
      model: null
  started_at: "2026-08-27T17:09:37-03:00"
  decided_at: "2026-08-27T17:09:37-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Aprobación del propietario (rol autoasignado) sin hallazgos — 2026-08-27. Hallazgos accionables: F-01..F-03 → BUG-021..023 (a crear); F-03 con decisión del propietario: la entidad es Eugenio Serrano (sin LATAM); se agrega BUG-024 para el resto devflow en tools/"
tags: [kit, revision, transformacion, linaje, consistencia]
---

# REV-005 — Análisis profundo del distribution-kit vs input-kit (inconsistencias introducidas)

| Field           | Value |
|-----------------|-------|
| **Scope**       | `distribution-kit/` (corrida 20260827-165601) vs `input-kit/` |
| **Methodology** | Comparación sistemática input→output (escaneos + diff semántico) |
| **Criteria**    | Inconsistencias de la metodología en el kit que NO existen en la metodología original (input): solo se reporta lo introducido por la transformación |

---

## 1. Purpose

El usuario solicitó un análisis profundo del `distribution-kit/` para
encontrar inconsistencias de la metodología que **no existan en la
metodología original** (el `input-kit/`). El criterio de aceptación de cada
hallazgo es: el texto equivalente del input es coherente, y el texto del kit
es incoherente. Las observaciones heredadas (idénticas en el input) se
reportan por separado como heredadas, fuera del criterio.

## 2. Artifacts reviewed

| Artifact | Files | Notes |
|----------|-------|-------|
| Metodología | `metaflow/ai-sdlc/MetaFlow.md` (4900+ líneas) | §3.0/§3.15/§4.2/§5.1/§5.6/§5.7/§5.12/§5.16, References |
| README/ONBOARDING/GUARDRAILS | `metaflow/README.md`, `ONBOARDING.md`, `GUARDRAILS.md` | Marcadores, conteos G/W/N/T, folder map |
| Métricas/reportes | `metaflow/23-metrics/README.md`, `42-reports/README.md` | Tablas de lead time, shorthands |
| UAT/análisis | `metaflow/24-tests/**`, `02-analysis/README.md` | Menciones de linaje v4.2 |
| Agent definitions | `CLAUDE.md`, `SKILL.md`, `MetaFlow.agent.md`, `MetaFlow.md` | Paridad del cuerpo compartido, §5.16 condensado |
| Schemas/templates | `23-metrics/manifest-v1-*.schema.json`, `TEMPLATE-MANIFEST-*.json` | Round-trip y const |
| Input (baseline) | `input-kit/devflow/**` | Equivalentes del linaje Avenga para cada punto |

## 3. Severity legend

| Category | Meaning |
|----------|---------|
| **Compliant** | Implementado correctamente per ADR / estándar |
| **Documented deviation** | Diferencia justificada, registrada en MEM |
| **Minor gap** | Inconsistencia sin impacto funcional, daña coherencia/lectura normativa |
| **Major gap** | Problema que rompe la lectura normativa o confunde al agente adoptante |

---

## 4. Findings

### 4.1 — Historia del linaje previo presentada como historia propia del kit

#### F-01 [Minor gap] — "removed in v4.2" y "versions up to 4.1" sin declarar el linaje previo

**Location:**
- `metaflow/24-tests/README.md` (líneas 27, 33, 72); `metaflow/24-tests/uat/README.md` (5-6, 32); `metaflow/24-tests/uat/INDEX.md` (5); `metaflow/24-tests/uat/TEMPLATE-UAT.md` (24-25); `metaflow/02-analysis/README.md` (46, 265); `metaflow/ONBOARDING.md` (75); `metaflow/README.md` (351); `metaflow/ai-sdlc/MetaFlow.md` (§4.2, línea ~3977)
- `CLAUDE.md`, `.agents/skills/ai-sdlc/SKILL.md`, `.github/agents/MetaFlow.agent.md`, `.opencode/agents/MetaFlow.md` (§5.16 condensado: "versions up to 4.1 shipped one inside `metaflow/`")

**Actual:** el kit declara como historia propia: "the UAT approval layer was removed in v4.2", "DORMANT / RESERVED (v4.2)", "versions up to 4.1 shipped one inside `metaflow/`". MetaFlow es v1.1 y nunca tuvo versiones 4.x — esas versiones pertenecen al linaje previo (Avenga), que la propia §5.16 del kit (arreglada por BUG-019) declara explícitamente como "History of the previous family".

**Expected:** las menciones de versiones del linaje previo deben declararse como tales ("removed in the previous lineage", "the previous lineage shipped one inside `metaflow/`") o reexpresarse sin números de versión del linaje ajeno ("the UAT layer is dormant/reserved in this release").

**Impact:** un adoptante de MetaFlow 1.1 lee que "MetaFlow removió UAT en v4.2" — una afirmación falsa para esta línea; incoherencia interna con la propia §5.16 del kit, que sí declara el linaje.

**Recommendation:** reglas del diccionario para las variantes (17 ubicaciones) + test de reproducción. → **BUG → TASK**.

**Evidencia de que es introducido:** el input (`devflow/`) dice "removed in v4.2"/"versions up to 4.1 shipped one inside `devflow/`" — **coherente** en el linaje Avenga (que sí tuvo v4.2/4.1). La misma frase en el kit es **incoherente** (MetaFlow no tuvo 4.x). El texto existía en el input; la *inconsistencia* no.

---

### 4.2 — Shorthands de checkpoints no canónicos en tablas de métricas

#### F-02 [Minor gap] — "TASK TASK-DONE" y "TASK-DONE − TASK-READY" sin el identificador canónico CP-*

**Location:**
- `metaflow/23-metrics/README.md` líneas 118-119: "| TASK lead time | TASK-DONE `decided_at` − TASK-READY `decided_at` (§3.7) |" y "| US lead time | last child TASK TASK-DONE `decided_at` − US `CP-US-Approval` `decided_at` |"
- `metaflow/42-reports/README.md` línea 70: "| TASK lead time | TASK-DONE − TASK-READY `decided_at` |"

**Actual:** el kit usa los identificadores "TASK-DONE" y "TASK-READY" — que no existen en su propio vocabulario (los checkpoints canónicos son `CP-TASK-DONE-Approval` y `CP-TASK-READY-Approval`, G05). La línea 119 produce la redacción doble "last child TASK TASK-DONE", que parece un typo.

**Expected:** `CP-TASK-DONE-Approval` / `CP-TASK-READY-Approval` (con backticks) en las tres tablas, consistente con el resto del kit.

**Impact:** tablas de métricas con identificadores no resolubles; el propio kit exige CP-<CODE>-Approval en todo el texto (G05/N05); la redacción "TASK TASK-DONE" daña la lectura.

**Recommendation:** reescribir las 3 celdas con los checkpoints canónicos + test. → **BUG → TASK**.

**Evidencia de que es introducido:** el input decía "Bolt lead time | BOLT-DONE `decided_at` − BOLT-READY..." y "last child Bolt BOLT-DONE..." — "BOLT-DONE"/"BOLT-READY" eran sufijos del vocabulario real del input (AITL-BOLT-DONE-Approval, usado también en su tabla de estados). El kit heredó el shorthand mecánicamente ("Bolt"→"TASK", "BOLT-DONE"→"TASK-DONE") sin adaptar al vocabulario CP-*; "TASK-DONE" no es un identificador de la línea MetaFlow.

---

### 4.3 — Declaración de propiedad

#### F-03 [Minor gap] — "of Eugenio Serrano LATAM" como entidad de la declaración de propiedad

**Location:** `metaflow/ai-sdlc/MetaFlow.md` líneas 203-204 (y 219: "defined by this research team").

**Actual:** "**MetaFlow is the proprietary methodology and framework of Eugenio Serrano LATAM**, developed by the research team to systematize AI-assisted software development."

**Expected:** la declaración de propiedad de la metodología debe nombrar una entidad real y atribuir el "research team" (o declarar la autoría individual), coherente con la identidad del proyecto.

**Impact:** "Eugenio Serrano LATAM" no es un nombre de organización (Eugenio Serrano es la persona; LATAM es una región) — la frase sugiere una entidad inexistente; "the research team" queda sin atribución en el contexto MetaFlow.

**Recommendation:** decisión del propietario: "of **Eugenio Serrano** (LATAM)" si la autoría es personal, o el nombre real de la entidad; re-atribuir "the research team". Es una decisión de branding/identidad — requiere decisión humana antes del fix (si se toca texto, vía BUG → TASK; si define identidad, quizás ADR).

**Evidencia de que es introducido:** el input decía "**Avenga DevFlow is the proprietary methodology and framework of Avenga LATAM**, developed by the research team..." — coherente (Avenga LATAM es el nombre real de la organización, "the research team" es el de Avenga). El transform reemplazó "Avenga LATAM" → "Eugenio Serrano LATAM" mecánicamente, produciendo la entidad inexistente.

---

### 4.4 — Verificaciones Compliant (lo que el kit hace bien)

- **Cero tokens del linaje viejo** — escaneo case-insensitive de `Avenga|DevFlow|devflow|Bolt|V-Bounce|v_bounce|AITL|HITL` sobre los 149 archivos: **0 hits**.
- **Paridad de los 4 agent definitions** — desde el ancla "## Guardrails (MUST enforce)": exactamente **2 líneas de diferencia por par** (la divergencia sancionada `52-agents-data/<agent>/`). Invariante del four-step sync cumplido.
- **Round-trip schema↔templates** — los 5 `TEMPLATE-MANIFEST-*.json` validan contra sus `manifest-v1-*.schema.json` (const `schema_version: "1.0"`).
- **39 reglas G** coherentes entre `GUARDRAILS.md` y los 4 agentes; W01–W21 coherente (los hits W22/W23 son falsos positivos: formato ISO-week de un ejemplo RETRO y la tabla de naming).
- **73 marcadores** `**Methodology version:** 1.1` (el +1 detectado es una mención en prosa del procedimiento de bump).
- **Vocabulario §3.15 vs templates** — valores de status de 28 templates dentro del vocabulario (draft/candidate/open); sin violaciones G39.
- **INDEXes sin filas de ejemplo** — solo las referencias legítimas a US-000.
- **Árbol coherente** — 21 carpetas + `ai-sdlc`; las 21 mencionadas en `README.md`; cero referencias en prosa a carpetas viejas (`adrs/`, `spec/`, `memory/`, `metrics/`…).
- **Citas Accelerate/DORA limpiadas** — la sección References conserva las citas académicas + el AWS DevOps Blog; cero restos de las citas del libro Accelerate/DORA.
- **Cero anuncios de TEMPLATE-REPORT.html**; **cero placeholders** "The  is invalid" (fixes de BUG-011/014/016 vigentes en el kit regenerado).

### 4.5 — Observaciones heredadas (existen en el input — fuera del criterio)

- **O-01 [Heredada]:** 4 links de ejemplo rotos en templates/READMEs — `glossary/README.md → ../domain-model/entities/Customer.md`, `TEMPLATE-INTRODUCTION.md → ../vision/vision.md`, `TEMPLATE-JOURNEY.md → ../personas/PersonaName.md`, `TEMPLATE-ADR.md → url`. **Verificado:** los destinos tampoco existen en el input. No introducida por el transform; corregible como mejora futura si se desea.
- **O-02 [Heredada]:** doble span de código "`metaflow/01-input/` `01-input/`" en MetaFlow.md §5.6. Idéntico patrón en el input.

## 5. Summary

El kit regenerado es **estructuralmente sólido**: cero restos del linaje
viejo, paridad de agentes exacta (2 líneas sancionadas), schemas y templates
consistentes, vocabulario y árbol coherentes. El análisis profundo
input→output encontró **3 inconsistencias introducidas por la transformación**
(ninguna Major): la historia del linaje previo presentada como historia
propia del kit (F-01, 17+4 ubicaciones), shorthands de checkpoints no
canónicos en tablas de métricas (F-02) y la declaración de propiedad con una
entidad inexistente (F-03). El patrón común: la transformación copió
afirmaciones que eran coherentes en el linaje Avenga (versiones 4.x, sufijos
BOLT-*, "Avenga LATAM") y las dejó como afirmaciones incoherentes en el
linaje MetaFlow — exactamente la clase de defecto que este review debía
cazar y que los tests de tokens no detectan (los tokens prohibidos fueron
reemplazados; las *afirmaciones* quedaron).

## 6. Action plan

> Aplica solo después de `CP-REV-Approval`. Cada destino sigue su propio
> ciclo y aprobación (código → BUG aprobado → TASK dedicado, T10/T02).

| # | Finding | Severity | Action | Routes to |
|---|---------|----------|--------|-----------|
| 1 | F-01    | Minor    | Reglas del diccionario para "removed in v4.2"/"versions up to 4.1..." (declarar linaje previo) + test | BUG → TASK (US-001) |
| 2 | F-02    | Minor    | Reescribir las 3 celdas con `CP-TASK-DONE-Approval`/`CP-TASK-READY-Approval` + test | BUG → TASK (US-001) |
| 3 | F-03    | Minor    | Decisión del propietario sobre la entidad ("Eugenio Serrano (LATAM)" vs entidad real) → luego fix de texto | Decisión humana → BUG → TASK (o ADR si define identidad) |
| 4 | O-01/O-02 | Heredadas | Opcional, fuera del criterio — decidir si se corrigen en la misma ronda | TASK→SPEC (opcional) |

## 7. Conclusions

El kit está **publicable en lo estructural** y los 3 hallazgos son menores,
pero conviene corregirlos en la próxima ronda de fixes (mismo patrón que
REV-003/004 → BUGs → TASKs): la historia del linaje es la que más superficie
toca (21 ubicaciones) y es la más visible para un adoptante que lea la
metodología. F-03 requiere una decisión humana de identidad antes de
tocarse. No se requiere una nueva revisión de ciclo completo después de los
fixes; basta la suite de reproducción ampliada.

## 8. CP-REV-Approval

> **MetaFlow §2.14, §3.0.** Esta Review permanece en draft hasta que
> un humano calificado registra `CP-REV-Approval` (bloque `review` del
> frontmatter). La aprobación hace accionables los hallazgos; no aprueba
> ningún artefacto downstream.

| Field | Value |
|-------|-------|
| **Reviewer** | human:eugenioserrano (rol autoasignado: no hay otro titular) |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-27T17:04:54-03:00` |
| **review.started_at** | `2026-08-27T17:09:37-03:00` |
| **review.decided_at** | `2026-08-27T17:09:37-03:00` |
| **Findings** | Ninguno — aprobado sin comentarios; F-03 resuelto por el propietario (Eugenio Serrano) |

---

## 9. History

| Date | Change | Author |
|------|--------|--------|
| 2026-08-27 | Initial review (draft) — análisis profundo input→output | @eugenioserrano |
| 2026-08-27 | **CP-REV-Approval** — aprobado; F-01..F-03 → BUG-021..023 (a crear); decisión de identidad F-03: Eugenio Serrano | @eugenioserrano |
| 2026-08-27 | **Cerrada** — hallazgos ruteados y ejecutados: BUG-021..024 aprobados → TASK-026..029 (CP-TASK-DONE-Approval 2026-08-27, Done); kit regenerado con linaje declarado, identidad corregida y tools/ limpio; BUGs fixed | @eugenioserrano |
