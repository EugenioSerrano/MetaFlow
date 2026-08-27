---
id: "BUG-007"
title: "Prefijo no canónico CITL-* usado como nombre de checkpoint en README y TEMPLATE-SPEC"
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
  - "distribution-kit/metaflow/README.md:187-188,258; distribution-kit/metaflow/21-spec/TEMPLATE-SPEC.md:96 (síntoma en el output)"
expected_result: "Los checkpoints se nombran solo con el prefijo canónico `CP-*`: `CP-US-Approval`, `CP-BUG-Approval`, `CP-TC-Approval`, `CP-DISC-Approval`, `CP-REV-Approval`, `CP-AREV-CRITIQUE/DEFENSE/VERDICT-Approval` (G05 declara los identificadores `CITL-*` no canónicos)"
actual_result: "README.md:187-188 usa \"CITL-US | CITL-BUG | CITL-TC | CITL-DISC | CITL-REV | CITL-AREV-VERDICT | CITL-ADR\" como origin approvals; README.md:258 usa \"CITL-AREV-{CRITIQUE,DEFENSE,VERDICT}-Approval\"; TEMPLATE-SPEC.md:96 usa \"CITL-US / CITL-TC / CP-BUG-Approval\" — el propio kit contradice su G05"
task: "US-001.TASK-012-fix-prefijo-citl"
spec: "SPEC-260827-0355-bolt012-fix-prefijo-citl.md"
mem: "MEM-260827-0408-fix-prefijo-citl.md"
sources: ["REV-003 (F-07)"]
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
  acknowledgment_reason: "Aprobación del propietario (Functional Analyst autoasignado) sin hallazgos — BUG-002..BUG-012 aprobados en bloque desde REV-003 (CP-REV-Approval 2026-08-27). Ruteo: TASK-012 bajo US-001"
tags: [bug, kit, checkpoints, naming]
---

# BUG-007 — Prefijo no canónico CITL-* en checkpoints

| Field              | Value |
|--------------------|-------|
| **Severity**       | medium |
| **Nature**         | functional |
| **Detected in**    | review (REV-003 F-07) |
| **Status**         | approved |
| **Affected files** | output: `metaflow/README.md`, `metaflow/21-spec/TEMPLATE-SPEC.md` · root cause: `src/transform.py` + `mapping.json` |
| **Dedicated TASK** | US-001.TASK-012 (functional) |

## 1. Summary

Tres lugares del kit usan `CITL-*` como nombre de checkpoint (el prefijo
que el propio GUARDRAILS G05 declara no canónico), mientras el resto usa
`CP-<CODE>-Approval`. Riesgo real de registrar aprobaciones con el prefijo
equivocado.

## 2. Reproduction

1. Regenerar el kit: `python src/transform.py`.
2. Verificar en el output:

**Expected result:** cero coincidencias de `CITL-US`, `CITL-BUG`,
`CITL-TC`, `CITL-DISC`, `CITL-REV`, `CITL-AREV`, `CITL-ADR` como nombres
de checkpoint en `distribution-kit/`.

**Actual result:** 3 ubicaciones: README.md:187-188, README.md:258,
TEMPLATE-SPEC.md:96.

## 3. Root cause

El diccionario del transform adaptó el texto "origin approved (AITL-* |
...)" del input-kit Avenga reemplazando el prefijo `AITL-` por `CITL-`
(concepto) en vez de `CP-` (formato de checkpoint) en esas frases; el
formato canónico `CP-<CODE>-Approval` se aplicó en el resto.

## 4. Impact

- **Users affected:** adoptantes que copian el flujo "One path" del README o el template de SPEC.
- **Data impact:** aprobaciones registradas con identificador no canónico (G05) — invalida el checkpoint map.
- **Workaround available:** no.

## 5. Classification and routing

| Aspect | Value |
|--------|-------|
| **Nature** | functional → Functional Analyst aprueba |
| **Violated expectation** | GUARDRAILS G05: checkpoints canónicos `CP-<CODE>-Approval` |
| **Dedicated TASK parent** | US-001 (feature — afecta el kit de salida) |

## 6. Fix status (strict TDD, ONE V-Bounce)

| Stage | Evidence | Status |
|-------|----------|--------|
| Reproduction test | RED: test del toolkit que exige cero `CITL-` como prefijo de checkpoint en el kit | Pending |
| Production fix | GREEN: diccionario unifica a `CP-*`; kit regenerado | Pending |
| MEM | MEM-YYMMDD-HHmm — red y green por separado | Pending |

> Fix TDD en el V-Bounce del TASK dedicado (TASK-012). **No se edita el kit a mano.**

## 7. Relations

| Relation | Reference |
|----------|-----------|
| **Detected in** | REV-003 (F-07) — CP-REV-Approval 2026-08-27 |
| **Incident** | — |
| **Affected US / TASK** | US-001 (kit de salida) |
| **Dedicated TASK** | US-001.TASK-012 |
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
| 2026-08-27 | Defect reported (draft) — REV-003 F-07 | @eugenioserrano |
| 2026-08-27 | **CP-BUG-Approval** — aprobado (bloque con BUG-002..BUG-012); TASK-012 asignado | @eugenioserrano |
| 2026-08-27 | **Fix entregado** — MEM-260827-0408-fix-prefijo-citl.md (CP-MEM-Approval 2026-08-27); BUG fixed
