---
id: "BUG-022"
title: "Shorthands de checkpoints no canónicos en tablas de métricas: 'TASK TASK-DONE' y 'TASK-DONE − TASK-READY' sin CP-* ni backticks"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
severity: "low"
nature: "functional"
status: "fixed"
owner: "eugenioserrano"
detected_in: "review"
detected_at: "2026-08-27T17:04:54-03:00"
incident_ref: ""
affected_artifacts:
  - "distribution-kit/metaflow/23-metrics/README.md (118-119)"
  - "distribution-kit/metaflow/42-reports/README.md (70)"
expected_result: "Las tablas de métricas usan los checkpoints canónicos del kit (`CP-TASK-DONE-Approval`, `CP-TASK-READY-Approval`, con backticks), consistentes con el resto del texto (G05/N05)"
actual_result: "El kit usa 'TASK-DONE' y 'TASK-READY' — identificadores que no existen en su vocabulario (canónico: `CP-TASK-DONE-Approval`/`CP-TASK-READY-Approval`) — y la línea 119 produce la redacción doble 'last child TASK TASK-DONE' que parece un typo (REV-005 F-02)"
task: "US-001.TASK-027"
spec: "SPEC-260827-1715-fix-shorthands-metricas"
mem: "MEM-260827-1725-fix-shorthands-metricas"
sources: ["REV-005 (F-02, CP-REV-Approval 2026-08-27)"]
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
tags: [bug, kit, metricas, checkpoints, naming]
---

# BUG-022 — Shorthands de checkpoints no canónicos en tablas de métricas

| Field              | Value |
|--------------------|-------|
| **Severity**       | low |
| **Nature**         | functional |
| **Detected in**    | review (REV-005 F-02) |
| **Status**         | draft |
| **Affected files** | `23-metrics/README.md` (118-119), `42-reports/README.md` (70) |
| **Dedicated TASK** | (a asignar tras CP-BUG-Approval — bajo US-001) |

## 1. Summary

Las tablas de lead time del kit usan los identificadores "TASK-DONE" y
"TASK-READY", que no existen en el vocabulario MetaFlow (los checkpoints
canónicos son `CP-TASK-DONE-Approval` y `CP-TASK-READY-Approval`), y la
celda del US lead time quedó con la redacción doble "last child TASK
TASK-DONE". En el input, "BOLT-DONE"/"BOLT-READY" eran sufijos del
vocabulario real (AITL-BOLT-DONE-Approval); el transform los copió
mecánicamente sin adaptar al vocabulario CP-*.

## 2. Reproduction

1. Abrir `distribution-kit/metaflow/23-metrics/README.md` líneas 118-119 y `42-reports/README.md` línea 70.

**Expected result:** `CP-TASK-DONE-Approval` / `CP-TASK-READY-Approval` con
backticks en las 3 celdas (G05: canónicos CP-*).

**Actual result:** "TASK-DONE `decided_at` − TASK-READY `decided_at`",
"last child TASK TASK-DONE `decided_at`" y "TASK-DONE − TASK-READY".

## 3. Root cause

Reglas mecánicas del diccionario ("Bolt"→"TASK", "BOLT-DONE"→"TASK-DONE",
"BOLT-READY"→"TASK-READY") que no mapearon los shorthands al identificador
canónico CP-<CODE>-Approval del linaje MetaFlow.

## 4. Impact

- **Users affected:** lectores de las tablas de métricas (identificadores no resolubles).
- **Data impact:** ninguno.
- **Workaround available:** no.

## 5. Classification and routing

| Aspect | Value |
|--------|-------|
| **Nature** | functional → Functional Analyst aprueba |
| **Violated expectation** | Vocabulario canónico del kit (G05/N05): checkpoints como `CP-<CODE>-Approval` |
| **Dedicated TASK parent** | US-001 (kit de salida) |

## 6. Fix status (strict TDD, ONE Delivery Loop)

| Stage | Evidence | Status |
|-------|----------|--------|
| Reproduction test | RED: test que exige `CP-TASK-DONE-Approval`/`CP-TASK-READY-Approval` en las 3 celdas | Pending |
| Production fix | GREEN: reglas del diccionario + kit regenerado | Pending |
| MEM | MEM-YYMMDD-HHmm — red y green por separado | Pending |

## 7. Relations

| Relation | Reference |
|----------|-----------|
| **Detected in** | REV-005 (F-02) — CP-REV-Approval 2026-08-27 |
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
| 2026-08-27 | **CP-BUG-Approval** — aprobado en bloque BUG-021..024; US-001.TASK-027 asignado | @eugenioserrano |
| 2026-08-27 | Defect reported (draft) — REV-005 F-02 | @eugenioserrano |
