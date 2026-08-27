---
id: "BUG-011"
title: "TEMPLATE-MEM describe delivery_loops[] con 6 campos; el schema exige 8"
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
  - "src/transform.py + mapping.json (diccionario/reglas de contenido — root cause)"
  - "tools/ (verificador de tokens — debe fijar el patrón)"
  - "distribution-kit/metaflow/22-memory/TEMPLATE-MEM.md:40-41 (síntoma en el output)"
expected_result: "El TEMPLATE-MEM debe listar los 8 campos requeridos de `delivery_loops[]`: number, spec_revision, git_commit, execution_outcome, code_generation, mem, review_ready_at, review_started_at (igual que 23-metrics/README.md:144 y GUARDRAILS.md:294-297 y el schema manifest-v1-task.schema.json)"
actual_result: "El template lista solo 6: \"(number, spec_revision, git_commit, execution_outcome, code_generation, mem)\" — omite review_ready_at y review_started_at"
bolt: "US-001.BOLT-016-fix-mem-campos-manifest"
spec: "SPEC-260827-0355-bolt016-fix-mem-campos-manifest.md"
mem: "MEM-260827-0410-fix-mem-campos-manifest.md"
sources: ["REV-003 (F-13)"]
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
  acknowledgment_reason: "Aprobación del propietario (Functional Analyst autoasignado) sin hallazgos — BUG-002..BUG-012 aprobados en bloque desde REV-003 (AITL-REV-Approval 2026-08-27). Ruteo: BOLT-016 bajo US-001"
tags: [bug, kit, template, manifest, contrato]
---

# BUG-011 — TEMPLATE-MEM con 6 de 8 campos de delivery_loops[]

| Field              | Value |
|--------------------|-------|
| **Severity**       | medium |
| **Nature**         | functional |
| **Detected in**    | review (REV-003 F-13) |
| **Status**         | approved |
| **Affected files** | output: `metaflow/22-memory/TEMPLATE-MEM.md:40-41` · root cause: `src/transform.py` + `mapping.json` |
| **Dedicated Bolt** | US-001.BOLT-016 (functional) |

## 1. Summary

El template del MEM describe el entry de `delivery_loops[]` con 6 campos,
pero el schema `manifest-v1-task.schema.json` exige 8 (faltan
`review_ready_at` y `review_started_at`). Un agente que siga el template
puede omitir 2 campos requeridos y producir un manifest inválido (G23).

## 2. Reproduction

1. Regenerar el kit: `python src/transform.py`.
2. Verificar en el output:

**Expected result:** la lista de campos de `delivery_loops[]` en
TEMPLATE-MEM.md incluye `review_ready_at` y `review_started_at`.

**Actual result:** solo "(number, spec_revision, git_commit,
execution_outcome, code_generation, mem)".

## 3. Root cause

El diccionario del transform actualizó la lista de 8 campos en
23-metrics/README.md y GUARDRAILS.md pero no la lista abreviada del
template del MEM (heredada del input-kit v5, que también la tenía
incompleta).

## 4. Impact

- **Users affected:** agentes que generan el MEM y el entry del manifest.
- **Data impact:** manifests con campos faltantes → no validan (G23) → el V-Bounce queda sin registro mecánico.
- **Workaround available:** no.

## 5. Classification and routing

| Aspect | Value |
|--------|-------|
| **Nature** | functional → Functional Analyst aprueba |
| **Violated expectation** | Contrato del schema manifest-v1-task.schema.json (8 campos) |
| **Dedicated Bolt parent** | US-001 (feature — afecta el kit de salida) |

## 6. Fix status (strict TDD, ONE V-Bounce)

| Stage | Evidence | Status |
|-------|----------|--------|
| Reproduction test | RED: test del toolkit que exige los 8 campos listados en TEMPLATE-MEM | Pending |
| Production fix | GREEN: diccionario completa la lista; kit regenerado | Pending |
| MEM | MEM-YYMMDD-HHmm — red y green por separado | Pending |

> Fix TDD en el V-Bounce del Bolt dedicado (BOLT-016). **No se edita el kit a mano.**

## 7. Relations

| Relation | Reference |
|----------|-----------|
| **Detected in** | REV-003 (F-13) — AITL-REV-Approval 2026-08-27 |
| **Incident** | — |
| **Affected US / Bolt** | US-001 / BOLT-003 (familia de manifests v1) |
| **Dedicated Bolt** | US-001.BOLT-016 |
| **Canonical SPEC** | (a crear) |
| **ADRs** | ADR-001 (toolkit de transformación) |
| **Risks** | — |

---

## 8. AITL-BUG-Approval

> **Avenga DevFlow §2.16, §3.0.** Este BUG permanece en draft hasta que un
> humano calificado registra `AITL-BUG-Approval` (Functional Analyst para
> functional). La aprobación confirma el defecto, la evidencia, la naturaleza
> y el ruteo; no aprueba el Bolt, la SPEC, la implementación, el MEM ni la
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
| 2026-08-27 | Defect reported (draft) — REV-003 F-13 | @eugenioserrano |
| 2026-08-27 | **AITL-BUG-Approval** — aprobado (bloque con BUG-002..BUG-012); BOLT-016 asignado | @eugenioserrano |
| 2026-08-27 | **Fix entregado** — MEM-260827-0410-fix-mem-campos-manifest.md (AITL-MEM-Approval 2026-08-27); BUG fixed
