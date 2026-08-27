---
id: "BUG-012"
title: "Ejemplos inconsistentes: comentario en español en §3.12 y write_paths con paths del repo de distribución"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
severity: "low"
nature: "functional"
status: "fixed"
owner: "eugenioserrano"
detected_in: "review"
detected_at: "2026-08-27T03:45:23-03:00"
incident_ref: ""
affected_artifacts:
  - "src/transform.py + mapping.json (diccionario/reglas de contenido — root cause)"
  - "tools/ (verificador de tokens — debe fijar el patrón)"
  - "distribution-kit/metaflow/ai-sdlc/MetaFlow.md:3156; distribution-kit/metaflow/51-agents/examples/developer/agent.yaml:19 (síntoma en el output)"
expected_result: "El ejemplo inline de §3.12 debe usar el content_language del kit (`en`): \"Add explicit concurrency handling.\" (como el TEMPLATE-MANIFEST-TASK.json); el ejemplo de agent debe referirse a la estructura de un proyecto adoptante (p. ej. `src/` + `metaflow/`), no al repo de distribución"
actual_result: "MetaFlow.md:3156 usa \"Agregar manejo explícito de concurrencia.\" (español; OQ-001 fijó `en`); 51-agents/examples/developer/agent.yaml:19 comenta \"the product tree (distribution-kit/, tools/) + governed records\" — carpetas del repo de distribución que no existen en proyectos adoptantes"
task: "US-001.TASK-017-fix-ejemplos-inconsistentes"
spec: "SPEC-260827-0355-bolt017-fix-ejemplos-inconsistentes.md"
mem: "MEM-260827-0410-fix-ejemplos-inconsistentes.md"
sources: ["REV-003 (F-14, F-15)"]
review_ready_at: "2026-08-27T03:45:23-03:00"
review:
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "functional_analyst"
      model: null
  started_at: "2026-08-27T03:49:12-03:00"
  decided_at: "2026-08-27T03:49:12-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Aprobación del propietario (Functional Analyst autoasignado) sin hallazgos — BUG-002..BUG-012 aprobados en bloque desde REV-003 (CP-REV-Approval 2026-08-27). Ruteo: TASK-017 bajo US-001"
tags: [bug, kit, ejemplos, idioma, plantillas]
---

# BUG-012 — Ejemplos inconsistentes (idioma y paths del repo de distribución)

| Field              | Value |
|--------------------|-------|
| **Severity**       | low |
| **Nature**         | functional |
| **Detected in**    | review (REV-003 F-14/F-15) |
| **Status**         | approved |
| **Affected files** | output: `metaflow/ai-sdlc/MetaFlow.md:3156`, `metaflow/51-agents/examples/developer/agent.yaml:19` · root cause: `src/transform.py` + `mapping.json` |
| **Dedicated TASK** | US-001.TASK-017 (functional) |

## 1. Summary

Dos ejemplos del kit quedaron inconsistentes con su contexto: el ejemplo
inline de §3.12 tiene un `comment` en español (el `content_language` del
kit es `en`, OQ-001) y el ejemplo de agent de `51-agents/examples/`
menciona carpetas del repo de distribución (`distribution-kit/`, `tools/`)
que no existen en un proyecto adoptante.

## 2. Reproduction

1. Regenerar el kit: `python src/transform.py`.
2. Verificar en el output:

**Expected result:** cero texto en español en ejemplos del kit (LANGUAGE =
`en`) y cero referencias a `distribution-kit/` o `tools/` fuera de la
documentación de instalación del kit.

**Actual result:** "Agregar manejo explícito de concurrencia."
(MetaFlow.md:3156) y "the product tree (distribution-kit/, tools/)"
(developer/agent.yaml:19).

## 3. Root cause

El diccionario del transform no normalizó el idioma del comentario del
ejemplo inline (heredado del input-kit, que usaba español en ese ejemplo)
ni el comentario de `write_paths` del ejemplo de agent (copiado del repo
de desarrollo).

## 4. Impact

- **Users affected:** adoptantes que copian ejemplos (confusión sobre qué carpetas escribir).
- **Data impact:** inconsistencia de idioma en el ejemplo normativo (viola la política §3.15 en la práctica).
- **Workaround available:** no.

## 5. Classification and routing

| Aspect | Value |
|--------|-------|
| **Nature** | functional → Functional Analyst aprueba |
| **Violated expectation** | `content_language` del kit = `en` (OQ-001); ejemplos referidos al proyecto adoptante |
| **Dedicated TASK parent** | US-001 (feature — afecta el kit de salida) |

## 6. Fix status (strict TDD, ONE V-Bounce)

| Stage | Evidence | Status |
|-------|----------|--------|
| Reproduction test | RED: test del toolkit que exige cero español en ejemplos y cero `distribution-kit/`/`tools/` en `51-agents/examples/` | Pending |
| Production fix | GREEN: diccionario traduce/ajusta los dos ejemplos; kit regenerado | Pending |
| MEM | MEM-YYMMDD-HHmm — red y green por separado | Pending |

> Fix TDD en el V-Bounce del TASK dedicado (TASK-017). **No se edita el kit a mano.**

## 7. Relations

| Relation | Reference |
|----------|-----------|
| **Detected in** | REV-003 (F-14, F-15) — CP-REV-Approval 2026-08-27 |
| **Incident** | — |
| **Affected US / TASK** | US-001 (kit de salida) |
| **Dedicated TASK** | US-001.TASK-017 |
| **Canonical SPEC** | (a crear) |
| **ADRs** | ADR-001 (toolkit de transformación) |
| **Risks** | — |

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
| **review_ready_at** | `2026-08-27T03:45:23-03:00` |
| **review.started_at** | `2026-08-27T03:49:12-03:00` |
| **review.decided_at** | `2026-08-27T03:49:12-03:00` |
| **Findings** | Ninguno — aprobado sin comentarios |

---

## 9. History

| Date | Change | Author |
|------|--------|--------|
| 2026-08-27 | Defect reported (draft) — REV-003 F-14/F-15 | @eugenioserrano |
| 2026-08-27 | **CP-BUG-Approval** — aprobado (bloque con BUG-002..BUG-012); TASK-017 asignado | @eugenioserrano |
| 2026-08-27 | **Fix entregado** — MEM-260827-0410-fix-ejemplos-inconsistentes.md (CP-MEM-Approval 2026-08-27); BUG fixed
