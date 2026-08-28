---
id: "BUG-024"
title: "Restos del linaje en el tooling del workshop: tools/BUILD.md y tools/README.md referencian 'devflow' y 'distribution-kit/devflow/bin/' (carpeta inexistente en el kit)"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
severity: "medium"
nature: "functional"
status: "fixed"
owner: "eugenioserrano"
detected_in: "review"
detected_at: "2026-08-27T17:04:54-03:00"
incident_ref: ""
affected_artifacts:
  - "tools/BUILD.md (destino de binarios, layout, cmd/devflow, SHA256SUMS)"
  - "tools/README.md (naming del binario, rutas devflow/)"
expected_result: "Las especificaciones del tooling track del workshop referencian la línea MetaFlow: binarios en `distribution-kit/metaflow/bin/` (la carpeta que el kit reserva), módulo/nombres sin el linaje previo (sin `devflow`), coherentes con el kit v1.1 y con ADR-001"
actual_result: "tools/BUILD.md y tools/README.md siguen describiendo el track del linaje previo: binarios en `distribution-kit/devflow/bin/` (carpeta que ya no existe — el kit usa metaflow/), layout con `cmd/devflow/`, binarios `devflow-windows-amd64.exe`, 'the devflow binary'. Es un resto del linaje en el workshop que apunta a un destino inexistente (detección 2026-08-27, sesión de análisis)"
task: "US-001.TASK-029"
spec: "SPEC-260827-1715-fix-tools-linaje"
mem: "MEM-260827-1725-fix-tools-linaje"
sources: ["user report (revisión del estado del workshop, 2026-08-27)"]
review_ready_at: "2026-08-27T17:04:54-03:00"
review:
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "functional_analyst"
      model: null
  started_at: "2026-08-27T17:13:56-03:00"
  decided_at: "2026-08-27T17:13:56-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: ""
tags: [bug, workshop, tools, linaje, devflow]
---

# BUG-024 — Restos del linaje en el tooling del workshop (tools/ → devflow/bin)

| Field              | Value |
|--------------------|-------|
| **Severity**       | medium |
| **Nature**         | functional |
| **Detected in**    | review (sesión de análisis del workshop) |
| **Status**         | draft |
| **Affected files** | `tools/BUILD.md`, `tools/README.md` (+ DESIGN docs que referencian el binario `devflow`) |
| **Dedicated TASK** | (a asignar tras CP-BUG-Approval — bajo US-001) |

## 1. Summary

El tooling track del workshop (specs, sin código aún) describe el track del
linaje previo: los binarios se construirían en `distribution-kit/devflow/bin/`
— carpeta que no existe en el kit actual (la línea MetaFlow usa `metaflow/`
y reserva `metaflow/bin/`). Igual que el BUG-020 (front door), es un resto
del linaje en el workshop; no se distribuye, pero el destino apunta a un
path inexistente y el naming (`cmd/devflow`, `devflow-windows-amd64.exe`)
pertenece al linaje previo.

## 2. Reproduction

1. Abrir `tools/BUILD.md` ("The compiled binaries land in **`distribution-kit/devflow/bin/`**").
2. Verificar que `distribution-kit/devflow/` no existe (el kit usa `metaflow/`).

**Expected result:** las especificaciones apuntan a `distribution-kit/metaflow/bin/`
y no usan el naming del linaje previo.

**Actual result:** destino `distribution-kit/devflow/bin/` (inexistente) y
naming `cmd/devflow` / `devflow-windows-amd64.exe` / "the devflow binary".

## 3. Root cause

`tools/` es la maquinaria del workshop y la transformación no la cubre (solo
transforma el kit). Las specs quedaron escritas para el linaje Avenga y no se
actualizaron al linaje MetaFlow.

## 4. Impact

- **Users affected:** el track de tooling futuro del workshop (el build seguiría un destino inexistente).
- **Data impact:** ninguno.
- **Workaround available:** no (la corrección es del texto de las specs).

## 5. Classification and routing

| Aspect | Value |
|--------|-------|
| **Nature** | functional → Functional Analyst aprueba |
| **Violated expectation** | Coherencia del workshop con el kit MetaFlow v1.1 (ADR-001) |
| **Dedicated TASK parent** | US-001 (toolkit de transformación — el tooling track es parte de su ecosistema) |

## 6. Fix status (strict TDD, ONE Delivery Loop)

| Stage | Evidence | Status |
|-------|----------|--------|
| Reproduction test | RED: test que exige cero `devflow` en tools/ (o en BUILD.md/README.md) y presencia de `distribution-kit/metaflow/bin` | Pending |
| Production fix | GREEN: BUILD.md/README.md re-expresados a la línea MetaFlow (paths + naming); suite completa | Pending |
| MEM | MEM-YYMMDD-HHmm — red y green por separado | Pending |

## 7. Relations

| Relation | Reference |
|----------|-----------|
| **Detected in** | user report (sesión de análisis 2026-08-27) |
| **Dedicated TASK** | (a asignar — US-001.TASK-NNN) |
| **ADRs** | ADR-001 (toolkit de transformación) |

---

## 8. CP-BUG-Approval

> **MetaFlow §2.16, §3.0.** Este BUG permanece en draft hasta que un
> humano calificado registra `CP-BUG-Approval`.

| Field | Value |
|-------|-------|
| **Approver** | human:eugenioserrano (rol autoasignado) |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-27T17:04:54-03:00` |
| **review.started_at** | `2026-08-27T17:13:56-03:00` |
| **review.decided_at** | `2026-08-27T17:13:56-03:00` |
| **Findings** | Ninguno — aprobado sin comentarios |

---

## 9. History

| Date | Change | Author |
|------|--------|--------|
| 2026-08-27 | **CP-BUG-Approval** — aprobado en bloque BUG-021..024; US-001.TASK-029 asignado | @eugenioserrano |
| 2026-08-27 | Defect reported (draft) — sesión de análisis del workshop | @eugenioserrano |
