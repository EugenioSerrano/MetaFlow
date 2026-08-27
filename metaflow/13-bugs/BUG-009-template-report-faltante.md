---
id: "BUG-009"
title: "TEMPLATE-REPORT.html anunciado en 42-reports/README pero ausente del kit"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
severity: "medium"
nature: "functional"
status: "fixed"
owner: "eugenioserrano"
detected_in: "review"
detected_at: "2026-08-27T03:45:23-03:00"
incident_ref: ""
affected_artifacts:
  - "src/transform.py + mapping.json (reglas/lista de archivos del kit — root cause)"
  - "tools/ (verificador de integridad — debe fijar el patrón)"
  - "distribution-kit/metaflow/42-reports/README.md:28 (síntoma en el output)"
expected_result: "El kit debe incluir `metaflow/42-reports/TEMPLATE-REPORT.html` (design reference con ejemplo de datos, como anuncia el README) — o el README corregido para no anunciar un archivo inexistente"
actual_result: "El README de 42-reports presenta `TEMPLATE-REPORT.html` como design reference poblado con ejemplo de datos, pero la carpeta solo contiene README.md — el archivo no se genera ni se copia"
task: "US-001.TASK-014-fix-template-report"
spec: "SPEC-260827-0355-bolt014-fix-template-report.md"
mem: "MEM-260827-0408-fix-template-report.md"
sources: ["REV-003 (F-10)"]
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
  acknowledgment_reason: "Aprobación del propietario (Functional Analyst autoasignado) sin hallazgos — BUG-002..BUG-012 aprobados en bloque desde REV-003 (CP-REV-Approval 2026-08-27). Ruteo: TASK-014 bajo US-001"
tags: [bug, kit, reports, archivo-faltante]
---

# BUG-009 — TEMPLATE-REPORT.html anunciado pero ausente

| Field              | Value |
|--------------------|-------|
| **Severity**       | medium |
| **Nature**         | functional |
| **Detected in**    | review (REV-003 F-10) |
| **Status**         | approved |
| **Affected files** | output: `metaflow/42-reports/` (README sin template) · root cause: `src/transform.py` + `mapping.json` |
| **Dedicated TASK** | US-001.TASK-014 (functional) |

## 1. Summary

El README de `42-reports/` anuncia `TEMPLATE-REPORT.html` como design
reference (mockup autocontenido con ejemplo de datos) pero el archivo no
existe en el kit: referencia rota que el adoptante no puede encontrar.

## 2. Reproduction

1. Regenerar el kit: `python src/transform.py`.
2. Verificar en el output:

**Expected result:** `distribution-kit/metaflow/42-reports/TEMPLATE-REPORT.html`
existe (o el README no lo anuncia).

**Actual result:** la carpeta `42-reports/` contiene solo `README.md`.

## 3. Root cause

La regla/lista de archivos del transform no incluye el `TEMPLATE-REPORT.html`
del input-kit (o el input no lo trae), mientras el texto del README que
sí se copió lo declara como presente.

## 4. Impact

- **Users affected:** adoptantes que buscan el design reference de reportes.
- **Data impact:** referencia rota en la documentación del kit.
- **Workaround available:** no.

## 5. Classification and routing

| Aspect | Value |
|--------|-------|
| **Nature** | functional → Functional Analyst aprueba |
| **Violated expectation** | El kit debe contener lo que su documentación anuncia |
| **Dedicated TASK parent** | US-001 (feature — afecta el kit de salida) |

## 6. Fix status (strict TDD, ONE V-Bounce)

| Stage | Evidence | Status |
|-------|----------|--------|
| Reproduction test | RED: test del toolkit que exige `TEMPLATE-REPORT.html` presente en `42-reports/` (o texto sin anuncio) | Pending |
| Production fix | GREEN: el transform copia/regenera el template (o el diccionario ajusta el README); kit regenerado | Pending |
| MEM | MEM-YYMMDD-HHmm — red y green por separado | Pending |

> Fix TDD en el V-Bounce del TASK dedicado (TASK-014). **No se edita el kit a mano.**

## 7. Relations

| Relation | Reference |
|----------|-----------|
| **Detected in** | REV-003 (F-10) — CP-REV-Approval 2026-08-27 |
| **Incident** | — |
| **Affected US / TASK** | US-001 (kit de salida) |
| **Dedicated TASK** | US-001.TASK-014 |
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
| 2026-08-27 | Defect reported (draft) — REV-003 F-10 | @eugenioserrano |
| 2026-08-27 | **CP-BUG-Approval** — aprobado (bloque con BUG-002..BUG-012); TASK-014 asignado | @eugenioserrano |
| 2026-08-27 | **Fix entregado** — MEM-260827-0408-fix-template-report.md (CP-MEM-Approval 2026-08-27); BUG fixed
