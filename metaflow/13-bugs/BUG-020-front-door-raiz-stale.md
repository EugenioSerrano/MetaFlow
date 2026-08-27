---
id: "BUG-020"
title: "Front door de la raíz stale tras la migración: README.md aún describe Avenga DevFlow 5.1, sin modelo de dos particiones, y el skill .agents/skills/avenga-devflow quedó instalado"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
severity: "high"
nature: "functional"
status: "fixed"
owner: "eugenioserrano"
detected_in: "review"
detected_at: "2026-08-27T16:25:23-03:00"
incident_ref: ""
affected_artifacts:
  - "README.md (raíz — front door del workshop; texto íntegro de Avenga DevFlow 5.1)"
  - ".agents/skills/avenga-devflow/SKILL.md (skill viejo aún instalado junto a ai-sdlc)"
  - "AGENTS.md (raíz — sección de proyecto vacía; no documenta las dos particiones)"
  - "src/tests/ (nuevos tests de verificación del front door)"
expected_result: "El front door de la raíz describe el workshop MetaFlow 1.1 con el modelo de dos particiones (metaflow/ = árbol gobernante instalado, donde se usa MetaFlow; distribution-kit/ = el producto, el kit en construcción — la siguiente versión), con cero referencias a Avenga/DevFlow en README.md, AGENTS.md, CLAUDE.md y las definiciones de agente instaladas (.agents/, .github/, .opencode/); la sección de proyecto de AGENTS.md (bajo el marcador METAFLOW:PROJECT-SECTION) documenta las dos particiones; el skill avenga-devflow ya no existe en la raíz"
actual_result: "README.md (raíz) es el texto íntegro de Avenga DevFlow 5.1 — marca, rutas devflow/, tabla de adopción del kit Avenga, mención a ADR-006/avenga-devflow — sin explicar que este repositorio usa MetaFlow ni el modelo de dos particiones; .agents/skills/avenga-devflow/SKILL.md permanece instalado en la raíz junto a .agents/skills/ai-sdlc (un agente puede cargar la metodología equivocada, AITL-*/BOLT en lugar de CP-*/TASK); la sección de proyecto de AGENTS.md está vacía"
task: "US-001.TASK-025-front-door-raiz"
spec: "SPEC-260827-1628-front-door-raiz"
mem: "MEM-260827-1632-front-door-raiz"
sources: ["user report (revisión del estado del workshop)"]
review_ready_at: "2026-08-27T16:25:23-03:00"
review:
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "functional_analyst"
      model: null
  started_at: "2026-08-27T16:26:44-03:00"
  decided_at: "2026-08-27T16:26:44-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Aprobación del propietario (Functional Analyst autoasignado) sin hallazgos — BUG-020 confirmado: defecto, evidencia, severidad high y ruteo functional → TASK bajo US-001. CP-BUG-Approval 2026-08-27"
tags: [bug, workshop, migracion, restos-avenga, front-door]
---

# BUG-020 — Front door de la raíz stale tras la migración (README Avenga 5.1 + skill avenga-devflow instalado)

| Field              | Value |
|--------------------|-------|
| **Severity**       | high |
| **Nature**         | functional |
| **Detected in**    | review (revisión del estado del workshop) |
| **Status**         | approved |
| **Affected files** | `README.md`, `.agents/skills/avenga-devflow/SKILL.md`, `AGENTS.md` (sección de proyecto), `src/tests/` |
| **Dedicated TASK** | US-001.TASK-025-front-door-raiz (functional, bajo US-001) |

## 1. Summary

La migración §5.16 y el pipeline de transformación cubrieron el kit
(`distribution-kit/`) y el árbol gobernante (`metaflow/`), pero no el front
door del workshop: el `README.md` de la raíz sigue siendo el texto íntegro de
"Avenga DevFlow 5.1" (marca, rutas `devflow/`, instrucciones de adopción del
kit Avenga) y el skill `.agents/skills/avenga-devflow/` quedó instalado junto
al nuevo `ai-sdlc`. Además, el modelo de dos particiones que el README viejo
sí documentaba ("two devflow/ trees, and that is deliberate") no tiene
equivalente en el linaje MetaFlow, y la sección de proyecto del `AGENTS.md`
raíz está vacía.

## 2. Reproduction

1. Abrir `README.md` en la raíz del repositorio.
2. Verificar el contenido de `.agents/skills/` en la raíz.
3. Verificar la sección de proyecto de `AGENTS.md` (después del marcador `METAFLOW:PROJECT-SECTION`).

**Expected result:** `README.md` describe el workshop MetaFlow 1.1 con las
dos particiones (donde se usa MetaFlow = árbol `metaflow/` instalado;
`distribution-kit/` = el producto en construcción, la siguiente versión),
sin referencias a Avenga/DevFlow; `.agents/skills/` contiene únicamente
`ai-sdlc`; `AGENTS.md` documenta las dos particiones en su sección de
proyecto.

**Actual result:** `README.md` = texto íntegro "Avenga DevFlow 5.1" con
marca, rutas `devflow/` y tabla de adopción del kit Avenga;
`.agents/skills/` contiene `ai-sdlc` **y** `avenga-devflow`;
`AGENTS.md` tiene la sección de proyecto vacía.

## 3. Root cause

La migración §5.16 instaló el árbol `metaflow/` y regeneró el kit, y el
pipeline de transformación reescribe solo el contenido de
`distribution-kit/`. Los archivos del taller que viven fuera de ambos —
`README.md` y `AGENTS.md` de la raíz, y la carpeta `.agents/skills/` del
workshop — no fueron reescritos: el README conservó el texto del linaje
Avenga (la migración lo trató como documento del producto viejo y no fue
transformado ni reemplazado), el skill viejo no fue removido cuando se
instaló `ai-sdlc`, y la sección de proyecto de `AGENTS.md` nunca se pobló.
El resultado es un front door que declara una metodología que este
repositorio ya no usa.

## 4. Impact

- **Users affected:** todos (quien aterrice en el repo — humanos y agentes — lee que esto es Avenga DevFlow 5.1).
- **Data impact:** ninguno (documentación), pero riesgo operativo real: un agente puede cargar el skill `avenga-devflow` (checkpoints `AITL-*`, `BOLT`) en un repositorio gobernado por MetaFlow (`CP-*`, `TASK`).
- **Workaround available:** no (la corrección es del front door del workshop).

## 5. Classification and routing

| Aspect | Value |
|--------|-------|
| **Nature** | functional → Functional Analyst aprueba |
| **Violated expectation** | Migración §5.16 (CHANGELOG [1.1 migration]): el repositorio opera sobre MetaFlow 1.1; el modelo de dos particiones del README viejo debería tener equivalente MetaFlow |
| **Dedicated TASK parent** | US-001 (feature del toolkit de transformación — afecta la entrega del workshop) |

## 6. Fix status (strict TDD, ONE Delivery Loop)

| Stage | Evidence | Status |
|-------|----------|--------|
| Reproduction test | RED: `python -m unittest src.tests.test_front_door` → Ran 5, FAILED (failures=4) | **Done** |
| Production fix | GREEN: test_front_door 5/5 OK + suite completa 96/96 + tools 14/14 | **Done** |
| MEM | [MEM-260827-1632-front-door-raiz.md](../22-memory/MEM-260827-1632-front-door-raiz.md) — red y green por separado | Pending CP-MEM-Approval |

> El fix es estrictamente TDD en el Delivery Loop del TASK dedicado.
> **No se regenera el kit**: los archivos tocados viven fuera de
> `distribution-kit/` y se editan directamente (front door del workshop).

## 7. Relations

| Relation | Reference |
|----------|-----------|
| **Detected in** | user report (revisión del estado del workshop, 2026-08-27) |
| **Incident** | — |
| **Affected US / TASK** | US-001 (toolkit de transformación) |
| **Dedicated TASK** | (a asignar — US-001.TASK-NNN) |
| **Canonical SPEC** | (a crear) |
| **ADRs** | ADR-001 (toolkit de transformación) |
| **Risks** | BR-001 (contaminación de marca — este defecto es una instancia) |

---

## 8. CP-BUG-Approval

> **MetaFlow §2.16, §3.0.** Este BUG permanece en draft hasta que un
> humano calificado registra `CP-BUG-Approval` (Functional Analyst para
> functional). La aprobación confirma el defecto, la evidencia, la naturaleza
> y el ruteo; no aprueba el TASK, la SPEC, la implementación, el MEM ni la
> aceptación — cada uno mantiene su propio checkpoint.

| Field | Value |
|-------|-------|
| **Approver** | human:eugenioserrano (rol autoasignado) |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-27T16:25:23-03:00` |
| **review.started_at** | `2026-08-27T16:26:44-03:00` |
| **review.decided_at** | `2026-08-27T16:26:44-03:00` |
| **Findings** | Ninguno — aprobado sin comentarios |

---

## 9. History

| Date | Change | Author |
|------|--------|--------|
| 2026-08-27 | Defect reported (draft) | @eugenioserrano |
| 2026-08-27 | **CP-BUG-Approval** — aprobado; TASK-025 asignado bajo US-001 | @eugenioserrano |
| 2026-08-27 | **Fix entregado** — Delivery Loop 1 (SPEC-260827-1628): RED 4/5 → GREEN 5/5 + suite 110 tests OK; MEM-260827-1632 pending CP-MEM-Approval | @eugenioserrano |
| 2026-08-27 | **CP-MEM-Approval** — MEM-260827-1632 aprobado; BUG fixed | @eugenioserrano |
| 2026-08-27 | **CP-TASK-DONE-Approval** — US-001.TASK-025 Done; BUG cerrado | @eugenioserrano |
