---
id: "BUG-025"
title: "Skill renombrada ai-sdlc → MetaFlow solo a mano (el pipeline sigue generando ai-sdlc — el kit no es reproducible) y sección de proyecto de AGENTS.md raíz vaciada (suite en rojo)"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
severity: "high"
nature: "functional"
status: "closed"
owner: "eugenioserrano"
detected_in: "tests"
detected_at: "2026-08-27T22:23:32-03:00"
incident_ref: ""
affected_artifacts:
  - "distribution-kit/.agents/skills/MetaFlow/SKILL.md (untracked — rename manual)"
  - "distribution-kit/.agents/skills/ai-sdlc/SKILL.md (borrado a mano; el pipeline lo regenera)"
  - "mapping.json (regla P-M6 path_rename avenga-devflow → ai-sdlc; sin regla para MetaFlow)"
  - "src/transform.py (apply_path por componente — sin soporte para renames full-path con '/')"
  - "AGENTS.md (raíz — sección de proyecto vacía bajo METAFLOW:PROJECT-SECTION)"
  - "README.md (raíz — tabla 'What lands' y nota de plataforma Codex aún citan ai-sdlc)"
  - "src/tests/test_front_door.py (FRONT_DOOR aún lista .agents/skills/ai-sdlc/SKILL.md)"
expected_result: "El pipeline regenera el kit con la skill en `.agents/skills/MetaFlow/SKILL.md` y frontmatter `name: MetaFlow` (idéntica al contenido actual salvo la ruta/nombre); `devflow/avenga-devflow/` sigue → `metaflow/ai-sdlc/` (carpeta de la metodología intacta); la sección de proyecto de AGENTS.md raíz documenta el modelo de dos particiones; README.md raíz cita `.agents/skills/MetaFlow/SKILL.md` en la tabla y la nota de plataforma; suite de tests 100 % verde (incluido test_front_door)"
actual_result: "El rename de la skill existe solo como edición manual (untracked) en la raíz y en distribution-kit/; una regeneración real de distribution-kit/ la revierte a `.agents/skills/ai-sdlc/SKILL.md` (regla P-M6) y pierde `MetaFlow/` — el kit no es reproducible desde el pipeline (viola la regla del workshop: nada edita distribution-kit/ a mano). Además AGENTS.md raíz quedó con la sección de proyecto vacía (`METAFLOW:PROJECT-SECTION -->`), el test test_front_door.test_agents_md_seccion_proyecto FALLA (104 tests → 1 failure), y README.md raíz referencia la sección ('it carries the two-partition model in its project section') y cita la skill ai-sdlc"
task: "US-001.TASK-030-fix-skill-metaflow"
spec: "SPEC-260827-2229-fix-skill-metaflow"
mem: "MEM-260827-2238-fix-skill-metaflow"
sources: ["user report (revisión del estado del workshop, 2026-08-27)", "tests (suite 104 tests → 1 failure)"]
review_ready_at: "2026-08-27T22:23:32-03:00"
review:
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "functional_analyst"
      model: null
  started_at: "2026-08-27T22:25:49-03:00"
  decided_at: "2026-08-27T22:25:49-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Aprobación del propietario (Functional Analyst autoasignado) sin hallazgos — BUG-025 confirmado: defecto, evidencia, severidad high y ruteo functional → TASK bajo US-001. CP-BUG-Approval 2026-08-27"
tags: [bug, workshop, kit, reproducibilidad, skill, front-door, tests]
---

# BUG-025 — Skill renombrada a MetaFlow sin codificar en el pipeline (kit no reproducible) + AGENTS.md raíz con sección de proyecto vaciada

| Field              | Value |
|--------------------|-------|
| **Severity**       | high |
| **Nature**         | functional |
| **Detected in**    | tests (sesión de revisión del workshop, 2026-08-27) |
| **Status**         | draft |
| **Affected files** | `mapping.json`, `src/transform.py`, `distribution-kit/.agents/skills/*`, `AGENTS.md` (raíz), `README.md` (raíz), `src/tests/test_front_door.py` |
| **Dedicated TASK** | US-001.TASK-030-fix-skill-metaflow (functional, bajo US-001) |

## 1. Summary

La skill de Codex del kit se renombró a `MetaFlow` (`.agents/skills/MetaFlow/SKILL.md` con `name: MetaFlow`) **solo como edición manual** en la raíz y en `distribution-kit/`. El pipeline (`mapping.json`, regla `P-M6` order 1009: `avenga-devflow → ai-sdlc`) sigue generando `.agents/skills/ai-sdlc/SKILL.md`: una regeneración real **borra el trabajo manual y revierte la skill a `ai-sdlc`** — el kit no es reproducible. En paralelo, la sección de proyecto de `AGENTS.md` raíz (el contrato de dos particiones del workshop, puesto por BUG-020/TASK-025) quedó vaciada por edición manual, dejando la suite de tests en rojo (`test_agents_md_seccion_proyecto` falla) y una referencia muerta en `README.md` raíz.

## 2. Reproduction

1. `python src/transform.py --dry-run` — el plan muestra `.agents/skills/avenga-devflow/SKILL.md -> .agents\skills\ai-sdlc\SKILL.md` (regla P-M6); la skill `MetaFlow` no existe en el plan.
2. `git status` — `distribution-kit/.agents/skills/MetaFlow/SKILL.md` aparece como untracked (trabajo manual) y `ai-sdlc/SKILL.md` como borrado.
3. `python -m unittest discover -s src/tests` → `FAIL: test_agents_md_seccion_proyecto` (sección de proyecto vacía).
4. `git diff HEAD AGENTS.md` — las 21 líneas de la sección "Two partitions — this workshop" fueron eliminadas.

**Expected result:** el pipeline produce `.agents/skills/MetaFlow/SKILL.md` con `name: MetaFlow`; la sección de proyecto de `AGENTS.md` raíz documenta las dos particiones; `README.md` raíz cita la skill `MetaFlow`; suite completa en verde.

**Actual result:** el pipeline produce `.agents/skills/ai-sdlc/SKILL.md` (revirtiendo el rename manual); `AGENTS.md` raíz tiene la sección vacía; `README.md` raíz cita `ai-sdlc` y una sección inexistente; `test_front_door` en rojo.

## 3. Root cause

Dos ediciones manuales fuera del pipeline y de la gobernanza:

1. **Rename de la skill a mano:** el usuario (o una sesión de agente) renombró `.agents/skills/ai-sdlc/` → `.agents/skills/MetaFlow/` (y `name: ai-sdlc` → `name: MetaFlow`) directamente en el árbol, sin codificarlo en `mapping.json`. La regla `P-M6` (path_rename, `avenga-devflow → ai-sdlc`) sigue vigente y el engine (`apply_path`) aplica renames **por componente de ruta**, sin capacidad de distinguir `.agents/skills/avenga-devflow` (que debe → `MetaFlow`) de `devflow/avenga-devflow` (que debe → `metaflow/ai-sdlc`). El kit perdió así su propiedad central: ser 100 % producto del pipeline.
2. **Vaciado de la sección de proyecto de AGENTS.md raíz:** la edición manual eliminó las 21 líneas de "Two partitions — this workshop" (contrato de BUG-020/TASK-025, MEM-260827-1632), rompiendo `test_front_door.test_agents_md_seccion_proyecto` y la referencia de README.md raíz.

## 4. Impact

- **Users affected:** todos — el equipo del workshop (reproducibilidad del producto) y cualquier agente/humano que lea el front door.
- **Data impact:** ninguno (documentación y configuración de pipeline), pero pérdida operativa real: una regeneración destruye el rename manual sin aviso; la suite en rojo enmascara regresiones futuras.
- **Workaround available:** no (el fix es codificar el rename en el pipeline + restaurar la sección).

## 5. Classification and routing

| Aspect | Value |
|--------|-------|
| **Nature** | functional → Functional Analyst aprueba (precedente BUG-020) |
| **Violated expectation** | Regla del workshop: *nada edita `distribution-kit/` a mano — se regenera* (README raíz, AGENTS.md raíz); suite de tests verde como gate del Delivery Loop |
| **Dedicated TASK parent** | US-001 (feature del toolkit de transformación) |

## 6. Fix status (strict TDD, ONE Delivery Loop)

| Stage | Evidence | Status |
|-------|----------|--------|
| Reproduction test | RED: `python -m unittest src.tests.test_reproducibilidad` → 2 failures (el plan generaba `.agents/skills/ai-sdlc/SKILL.md`; la skill MetaFlow no existía en la salida) + `test_front_door.test_agents_md_seccion_proyecto` FAIL (sección vacía) | **Done** |
| Production fix | GREEN: `python -m unittest src.tests.test_reproducibilidad` → 3/3 OK; suite completa → 107 tests OK; `python src/transform.py` ×2 → exit 0, 149 archivos idénticos (idempotencia), 0 tokens prohibidos, skill `.agents/skills/MetaFlow/SKILL.md` con `name: MetaFlow` | **Done** |
| MEM | [MEM-260827-2238-fix-skill-metaflow.md](../22-memory/MEM-260827-2238-fix-skill-metaflow.md) — red y green por separado | Pending CP-MEM-Approval |

> La reproducción y el fix son fases del MISMO Delivery Loop del TASK dedicado (§2.16, §3.3.1). Código de producción no cambia antes de la evidencia RED.

---

## 7. Relations

| Relation | Reference |
|----------|-----------|
| **Detected in** | user report + tests (suite 104 → 1 failure) |
| **Affected US / TASK** | US-001 / US-001.TASK-NNN (dedicado) |
| **ADRs** | ADR-001-toolkit-transformacion (reglas longest-first, path_rename) |
| **Precedente** | BUG-020 (front door raíz), BUG-001 (carpetas de plataforma) |

---

## 8. CP-BUG-Approval

> **MetaFlow §2.16, §3.0.** Este BUG permanece en draft hasta que un humano
> cualificado registre `CP-BUG-Approval` (recomendado: Functional Analyst para
> functional) — registrado en el bloque `review` del frontmatter. La aprobación
> confirma defecto, evidencia, naturaleza y ruteo; **no** aprueba el TASK, SPEC,
> implementación, MEM ni aceptación — cada uno mantiene su propio checkpoint.

---

## 9. History

| Date | Change | Author |
|------|--------|--------|
| 2026-08-27 | Defect reported (draft) — sesión de revisión del workshop: rename de skill no reproducible + AGENTS.md raíz vaciado | @eugenioserrano |
| 2026-08-27 | CP-BUG-Approval recorded | @user |
