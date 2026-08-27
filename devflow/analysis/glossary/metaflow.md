---
module: "metaflow"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
status: "stable"
tags: [metaf low, rename, diccionario]
sources: ["conversación de diseño 2026-08-27"]
---

# Glosario — MetaFlow (diccionario de transformación de nombres)

> Este es el **diccionario canónico de la transformación** AvengaDevFlow →
> MetaFlow. Es la fuente de las reglas de `mapping.json` del toolkit. Cada
> entrada describe un término fuente, su reemplazo y el contexto de aplicación.
> El orden de aplicación es crítico: **las cadenas más largas primero**
> (p. ej. `AvengaDevFlow` antes de `Avenga DevFlow` antes de `Avenga`), para
> que un término nunca quede parcialmente transformado.

---

## 1. Familia de marca

| Campo | Valor |
|-------|-------|
| **Definición** | Reglas de identidad: toda referencia a la marca AvengaDevFlow pasa a MetaFlow; toda atribución a Avenga LATAM pasa a Eugenio Serrano |
| **Sinónimos** | — |
| **No confundir con** | Renombrado de conceptos (checkpoints, TASK, Delivery Loop) — secciones 2–4 |
| **Entidad** | `../domain-model/entities/MappingRule.md` |
| **Ejemplo** | `Avenga DevFlow is the proprietary methodology` → `MetaFlow is the proprietary methodology` |
| **Fuente** | Conversación de diseño 2026-08-27 |

| # | Término fuente | Reemplazo | Ámbito |
|---|----------------|-----------|--------|
| M1 | `AvengaDevFlow` | `MetaFlow` | Contenido (nombres de agente, headings, frontmatter) |
| M2 | `Avenga DevFlow` | `MetaFlow` | Contenido |
| M3 | `DevFlow` (suelto, como nombre del framework) | `MetaFlow` | Contenido — **siempre**, con o sin prefijo "Avenga" |
| M4 | `Avenga LATAM` | `Eugenio Serrano` | Contenido (firma, atribución) |
| M5 | "proprietary methodology of Avenga LATAM" | reescritura a propiedad de Eugenio Serrano | Contenido |
| M6 | `avenga-devflow/` (carpeta) | `ai-sdlc/` | Rutas |
| P-M15 | `devflow` (componente de ruta del framework) | `metaflow` | Rutas — la carpeta raíz del framework pasa a `metaflow/` (decisión del propietario 2026-08-27) |
| M7 | `Avenga-DevFlow.md` (archivo normativo) | `MetaFlow.md` | Rutas |
| M8 | `AvengaDevFlow.agent.md` / `AvengaDevFlow.md` (wrappers) | `MetaFlow.agent.md` / `MetaFlow.md` | Rutas |
| M9 | `.agents/skills/avenga-devflow/` | `.agents/skills/ai-sdlc/` | Rutas |
| M10 | `AVENGA-DEVFLOW:PROJECT-SECTION` (marcador de AGENTS.md) | `METAFLOW:PROJECT-SECTION` | Contenido |
| M11 | `devflow/avenga-devflow/Avenga-DevFlow.md` (ruta en texto) | `metaflow/ai-sdlc/MetaFlow.md` | Contenido (rutas escritas en prosa) |
| M12 | `Avenga` (suelto, título — "framework of Avenga") | `Eugenio Serrano` | Contenido — aplicar tras M1/M2/M4/M5 |
| M13 | `avenga.com` (dominio en emails/URLs) | `metaflow.com` | Contenido |
| M14 | `avenga` (minúscula: URNs `urn:avenga:devflow:...`) | `metaflow` | Contenido — aplicar tras M13 |
| M15 | `devflow/` (carpeta del framework en rutas escritas) | `metaflow/` | Contenido — aplicar tras M11 |
| M16 | `devflow` (suelto, minúscula — "the devflow folder") | `metaflow` | Contenido — aplicar tras M15 |
| M17 | `Devflow` (título, f minúscula) | `MetaFlow` | Contenido |
| M18 | `DEVFLOW` (todo mayúsculas) | `METAFLOW` | Contenido |

## 2. Familia de checkpoints (CP / CITL)

| Campo | Valor |
|-------|-------|
| **Definición** | Los códigos de aprobación `AITL-*-Approval` y `HITL-*-Approval` pasan a `CP-*-Approval` (CP = checkpoint); el concepto Actor-in-the-Loop/Human-in-the-Loop pasa a **Checkpoint-in-the-Loop (CITL)**; las referencias históricas al legado `HITL-*` se **eliminan** |
| **Sinónimos** | AITL → CITL |
| **No confundir con** | Los checkpoints de **este** repositorio (que sigue operando bajo AvengaDevFlow y usa `AITL-*` hasta migrar — ver OQ-003) |
| **Entidad** | `../domain-model/entities/MappingRule.md` |
| **Ejemplo** | `AITL-SPEC-Approval` → `CP-SPEC-Approval`; `HITL-MEM-Approval` → `CP-MEM-Approval` |
| **Fuente** | Conversación de diseño 2026-08-27 |

| # | Término fuente | Reemplazo | Ámbito |
|---|----------------|-----------|--------|
| C1 | `AITL-<CODE>-Approval` (cualquier código) | `CP-<CODE>-Approval` | Contenido — **regex**: el código es variable (`SPEC`, `MEM`, `US`, `TC`, `ADR`, `TASK-READY`, `TASK-DONE`…) |
| C2 | `HITL-<CODE>-Approval` (uso activo) | `CP-<CODE>-Approval` | Contenido — regex |
| C3 | `Actor-in-the-Loop (AITL)` / `Human-in-the-Loop (HITL)` | `Checkpoint-in-the-Loop (CITL)` | Contenido (concepto) |
| C4 | `AITL` / `HITL` como acrónimo en prosa | `CITL` | Contenido |
| C5 | Referencias históricas al legado: "pre-v5 `HITL-*` prefix", "legacy checkpoint names", G05 hablando del prefijo viejo, historia de migración, "survives only in migrated history" | **eliminar** | Contenido (remoción con reporte) |
| C6 | `AITL-<CODE>-Approval` dentro de tablas/headers de la metodología | `CP-<CODE>-Approval` | Contenido |
| C7 | `hitl_approvals[]` (campo de manifest migrado del legado v4) | `checkpoint_approvals[]` | Contenido (JSON) |
| C8 | Anchor markdown `#checkpoints-actor-in-the-loop--aitl` | `#checkpoints-checkpoint-in-the-loop--citl` | Contenido |

## 3. Familia TASK (antes Bolt)

| Campo | Valor |
|-------|-------|
| **Definición** | El concepto **Bolt** (unidad de trabajo) pasa a **TASK**, en todas sus formas: concepto, identificadores de archivo, templates, schemas, manifiestos y reglas derivadas |
| **Sinónimos** | Bolt → TASK; Bolts → TASKs |
| **No confundir con** | Tarea genérica; TASK es la unidad de trabajo con su ciclo de vida completo (readiness, SPEC, Delivery Loop, MEM, Done) |
| **Entidad** | `../domain-model/entities/Task.md` (concepto heredado) |
| **Ejemplo** | `US-012.BOLT-003-invoice-download.md` → `US-012.TASK-003-invoice-download.md` |
| **Fuente** | Conversación de diseño 2026-08-27 |

| # | Término fuente | Reemplazo | Ámbito |
|---|----------------|-----------|--------|
| B1 | `Bolt` / `Bolts` (concepto, prosa) | `TASK` / `TASKs` | Contenido |
| B2 | `BOLT` (en IDs tipo `US-NNN.BOLT-NNN`) | `TASK` | Contenido + rutas |
| B3 | `bolt` / `bolts` (minúscula en prosa: "the Bolt's History", "a bolt is NOT Done") | `task` / `tasks` | Contenido |
| B4 | `TEMPLATE-BOLT.md` | `TEMPLATE-TASK.md` | Rutas |
| B5 | `US-NNN.BOLT-NNN-<desc>.md` / `TC-NNN.BOLT-NNN-<desc>.md` / `US-000.BOLT-NNN-<desc>.md` | `…TASK-NNN-<desc>.md` | Rutas |
| B6 | `AITL-BOLT-READY-Approval` → luego `CP-BOLT-READY-Approval` | `CP-TASK-READY-Approval` | Contenido — aplicar tras C1/C2 |
| B7 | `BOLT-DONE-Approval` | `TASK-DONE-Approval` | Contenido |
| B8 | `metrics/bolts/` | `metrics/tasks/` | Rutas |
| B9 | `manifest-v5-bolt.schema.json` | `manifest-v5-task.schema.json` | Rutas |
| B10 | `TEMPLATE-MANIFEST-BOLT*.json` | `TEMPLATE-MANIFEST-TASK*.json` | Rutas |
| B11 | `bolt{…}` / `bolts[]` (campos de manifest) | `task{…}` / `tasks[]` | Contenido (JSON) |
| B12 | `test_bolts[]` (manifest de TC) | `test_tasks[]` | Contenido (JSON) |
| B13 | "Bolt-First Rule" | "TASK-First Rule" | Contenido |
| B14 | "Bolt Lead Time" | "TASK Lead Time" | Contenido |
| B15 | "V-Bounces per Bolt", "Model runs per Bolt", "per Bolt" | "Delivery Loops per TASK", "per TASK" | Contenido |
| B16 | `functional/bolts/` (carpeta) | `functional/tasks/` | Rutas |

## 4. Familia Delivery Loop (antes V-Bounce)

| Campo | Valor |
|-------|-------|
| **Definición** | El ciclo de ejecución **V-Bounce** pasa a **Delivery Loop**, en todas sus formas (prosa, protocolo, campos de manifest) |
| **Sinónimos** | V-Bounce → Delivery Loop |
| **No confundir con** | DORA D2 (Change Lead Time) — el "TASK Lead Time" es una métrica de flujo separada |
| **Entidad** | `../domain-model/entities/TransformRun.md` (análogo en el pipeline) |
| **Ejemplo** | "the V-Bounce cycle" → "the Delivery Loop cycle"; `v_bounces[]` → `delivery_loops[]` |
| **Fuente** | Conversación de diseño 2026-08-27 |

| # | Término fuente | Reemplazo | Ámbito |
|---|----------------|-----------|--------|
| D1 | `V-Bounce` | `Delivery Loop` | Contenido |
| D2 | `V-Bounces` | `Delivery Loops` | Contenido |
| D3 | `v_bounces` / `v_bounces[]` (campos de manifest y schema) | `delivery_loops` / `delivery_loops[]` | Contenido (JSON) |
| D4 | "V-Bounce protocol", "V-Bounce execution", "V-Bounce cycle" | "Delivery Loop protocol", "ejecución", "ciclo" | Contenido |
| D5 | "one V-Bounce never spans two SPEC revisions" | "one Delivery Loop never spans two SPEC revisions" | Contenido |
| D6 | "V-Bounces per Bolt" | "Delivery Loops per TASK" | Contenido — combinar con B15 |
| D7 | `V-BOUNCE` (mayúsculas, headings/subgraph) | `DELIVERY LOOP` | Contenido |
| D8 | `v_bounce` (singular, campos de manifest: `"v_bounce": 1`, `subject.v_bounce`) | `delivery_loop` | Contenido (JSON) — aplicar tras D3 |
| D9 | `DORA` como **concepto de métricas** (§3.7.1: DORA Metrics, DORA Five, DORA D2, DORA review) | `Delivery Flow` | Contenido — decisión del propietario 2026-08-27: misma funcionalidad, nombre neutro; las **citas** a DORA/Accelerate se eliminan por línea (R2) |
| D10 | `VBOUNCE` (id de nodo Mermaid sin guion) | `DELIVERYLOOP` | Contenido |

## 5. Familia de remociones

| Campo | Valor |
|-------|-------|
| **Definición** | Contenido que se **elimina** (no se renombra): referencias históricas y citas técnicas de la autoría original. Toda remoción se registra en el reporte para revisión humana |
| **Sinónimos** | "rajamos" (decisión del propietario) |
| **No confundir con** | Banned terms del output (sección 6) — la remoción quita frases; los banned terms son la verificación final |
| **Entidad** | `../domain-model/entities/MappingRule.md` (tipo `remove`) |
| **Ejemplo** | "based on *AI-Driven Development Life Cycle: Reimagining Software Engineering* (Raja SP, AWS)" → se elimina |
| **Fuente** | Conversación de diseño 2026-08-27 |

| # | Término fuente | Tratamiento |
|---|----------------|-------------|
| R1 | Citas a "Raja SP" / "AI-Driven Development Life Cycle: Reimagining Software Engineering (Raja SP, AWS)" | eliminar |
| R2 | Citas a "*Accelerate* / DORA" (entradas bibliográficas) | **eliminar por línea** (R2a: "DevOps Research and Assessment…", R2b: "Forsgren, N.… *Accelerate*") — el concepto de métricas DORA del cuerpo se renombra (D9), no se elimina |
| R3 | Referencias históricas de migración (entradas de CHANGELOG-like, "5.0 migration", historia de versiones previas) | eliminar |
| R4 | Cláusulas de legado `HITL-*` (ver C5) | eliminar |

## 6. Términos prohibidos en el kit de salida (verificación final)

| Término prohibido | Razón | Usar en su lugar |
|-------------------|-------|------------------|
| `Avenga` | Marca ajena | — (eliminar/reemplazar por MetaFlow) |
| `devflow` / `DevFlow` (carpeta y término) | Identidad renombrada — cero rastro en el kit | `metaflow/` / `MetaFlow` |
| `AITL` / `HITL` | Acrónimos de la marca previa | `CITL` / `CP-*` |
| `Bolt` / `BOLT` / `bolts` | Concepto renombrado | `TASK` / `TASKs` |
| `V-Bounce` / `v_bounces` | Concepto renombrado | `Delivery Loop` / `delivery_loops` |
| `Raja` / `DORA` | Citas de autoría removidas | — |

> El verificador del toolkit (S4 del scope MVP) usa esta tabla como lista de
> tokens prohibidos: si alguno aparece en el output, el pipeline falla.

## 7. Términos que se conservan (NO se transforman)

| Término | Por qué se conserva |
|---------|---------------------|
| `US`, `TC`, `ADR`, `DISC`, `REV`, `AREV`, `OQ`, `BUG`, `INC`, `RISK`, `RETRO`, `UAT`, `BR`, `PROMPT`, `PROC`, `INT` | Vocabulario técnico neutral, no es identidad de marca |
| `SPEC`, `MEM` | Se conservan por decisión (punto 6 del diseño) |
| `G01`–`G39`, `W01`–`W21`, `N01`–`N23`, `T01`–`T12` | IDs de reglas, no nombres de marca |
| `DoR`, `DoD`, `manifest`, `schema_version`, `checkpoint_approvals[]` | Vocabulario del framework conservado |
| Números de versión (`5.1`, `5.0`) | La versión de MetaFlow = versión del kit de entrada **− 4** (mayor − 4, menor igual: 5.1 → 1.1) — decisión 2026-08-27 (OQ-003). **Implementación por contexto (BOLT-003):** `metaflow/VERSION` (regla con `path`), `**Methodology version:** 5.1`, `**Agent version:** 5.1 — implements methodology v5.1`, `v5.1 (Methodology)`, `v5.1 methodology`, `(v5.1)`, `MetaFlow v5.1`, `v5.1)` — **nunca** `§5.1` (secciones) ni `schema_version` |
| `LANGUAGE` del kit de entrada | Se hereda — el kit queda en inglés (OQ-001 respondida 2026-08-27) |

> **Archivos excluidos del transform (no se migran):**
> `devflow/reports/TEMPLATE-REPORT.html` — template HTML de reportes con
> branding de Avenga embebido en el CSS (colores, logo, título); un rename de
> texto no alcanza. El pipeline lo **excluye** (lista `exclude` de
> `mapping.json`): no se transforma ni se copia al output, y la exclusión se
> registra en el reporte del run (nada silencioso). El kit necesita un
> **template nuevo de MetaFlow** (entregable aparte, ver scope X6).

## 8. Historia

| Fecha | Cambio | Autor |
|-------|--------|-------|
| 2026-08-27 | Creado — diccionario completo de la conversación de diseño | @eugenioserrano |
| 2026-08-27 | Validado por el propietario — status `stable` | @eugenioserrano |
| 2026-08-27 | Revisión — valores de rutas M6/M9/M11: la carpeta del kit pasa a `ai-sdlc/` (ruta canónica `devflow/ai-sdlc/MetaFlow.md`; se evita el `metaflow/` redundante). M7/M8/M10 sin cambios | @eugenioserrano |
| 2026-08-27 | Revisión — reglas nuevas del E2E contra el kit real: C7 (`hitl_approvals`), C8 (anchor CITL), M12 (`Avenga` suelto), M13/M14 (`avenga.com`/`avenga`), D7 (`V-BOUNCE`), D8 (`v_bounce`), D9 (**DORA → Delivery Flow**, decisión del propietario), R2a/R2b (citas DORA/Accelerate eliminadas por línea) | @eugenioserrano |
| 2026-08-27 | Revisión — la carpeta raíz del framework pasa de `devflow/` a `metaflow/` (M15/M16/M17/M18/P-M15; M11 actualizada): ruta canónica del kit `metaflow/ai-sdlc/MetaFlow.md`; cero rastro de "devflow" (también es token prohibido del verificador) | @eugenioserrano |
