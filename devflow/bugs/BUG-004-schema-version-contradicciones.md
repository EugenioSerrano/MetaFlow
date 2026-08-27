---
id: "BUG-004"
title: "Contradicciones \"5.0\" vs \"1.0\" de schema_version dentro de un mismo documento del kit"
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
  - "distribution-kit/metaflow/23-metrics/README.md:183, distribution-kit/metaflow/12-functional/user-stories/TEMPLATE-US.md:47, distribution-kit/metaflow/24-tests/test-cases/TEMPLATE-TC.md:42 (síntoma en el output)"
expected_result: "Cada documento debe declarar un único valor consistente: `schema_version: \"1.0\"` en 23-metrics/README (línea 46), TEMPLATE-US (sección 8) y TEMPLATE-TC (sección 11)"
actual_result: "23-metrics/README.md:183 dice `exactly \"5.0\"` (su línea 46 dice `\"1.0\"`); TEMPLATE-US.md:47 dice `schema_version \"5.0\"` (su sección 8, línea 154, dice `\"1.0\"`); TEMPLATE-TC.md:42 dice `\"5.0\"` (su línea 126 dice `\"1.0\"`) — el mismo documento se contradice"
bolt: "US-001.BOLT-009-fix-schema-version-contradicciones"
spec: "SPEC-260827-0355-bolt009-fix-schema-version-contradicciones.md"
mem: "MEM-260827-0406-fix-schema-version-contradicciones.md"
sources: ["REV-003 (F-04)"]
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
  acknowledgment_reason: "Aprobación del propietario (Functional Analyst autoasignado) sin hallazgos — BUG-002..BUG-012 aprobados en bloque desde REV-003 (AITL-REV-Approval 2026-08-27). Ruteo: BOLT-009 bajo US-001"
tags: [bug, kit, schema-version, templates, restos-v5]
---

# BUG-004 — Contradicciones "5.0" vs "1.0" dentro del mismo documento

| Field              | Value |
|--------------------|-------|
| **Severity**       | medium |
| **Nature**         | functional |
| **Detected in**    | review (REV-003 F-04) |
| **Status**         | approved |
| **Affected files** | output: `23-metrics/README.md`, `TEMPLATE-US.md`, `TEMPLATE-TC.md` · root cause: `src/transform.py` + `mapping.json` |
| **Dedicated Bolt** | US-001.BOLT-009 (functional) |

## 1. Summary

Tres documentos del kit dan dos valores distintos de `schema_version`
dentro de sí mismos: el resto `"5.0"` (linaje Avenga) sobrevive en un
comentario/sección mientras la sección de creación de manifest dice
`"1.0"`. Quien copie el template puede crear un manifest que no valida.

## 2. Reproduction

1. Regenerar el kit: `python src/transform.py`.
2. Verificar en el output:

**Expected result:** cero coincidencias de `schema_version "5.0"` y
`exactly "5.0"` en `23-metrics/README.md`, `TEMPLATE-US.md` y
`TEMPLATE-TC.md`.

**Actual result:** `23-metrics/README.md:183`, `TEMPLATE-US.md:47` y
`TEMPLATE-TC.md:42`.

## 3. Root cause

El diccionario del transform reemplazó la mayoría de las ocurrencias de
"5.0" por "1.0" pero no estas tres (un comentario YAML multilínea en los
templates y una línea de la sección "Common (all three)" del README), que
se heredaron del input-kit v5.

## 4. Impact

- **Users affected:** adoptantes que copian templates o leen el README de métricas.
- **Data impact:** riesgo de manifests con `schema_version: "5.0"` que no validan (G23).
- **Workaround available:** no.

## 5. Classification and routing

| Aspect | Value |
|--------|-------|
| **Nature** | functional → Functional Analyst aprueba |
| **Violated expectation** | Decisión REV-002/BOLT-003: familia v1 (`schema_version: "1.0"`) |
| **Dedicated Bolt parent** | US-001 (feature — afecta el kit de salida) |

## 6. Fix status (strict TDD, ONE V-Bounce)

| Stage | Evidence | Status |
|-------|----------|--------|
| Reproduction test | RED: test del toolkit que exige cero `"5.0"` en esos 3 archivos | Pending |
| Production fix | GREEN: diccionario unifica a `"1.0"`; kit regenerado | Pending |
| MEM | MEM-YYMMDD-HHmm — red y green por separado | Pending |

> Fix TDD en el V-Bounce del Bolt dedicado (BOLT-009). **No se edita el kit a mano.**

## 7. Relations

| Relation | Reference |
|----------|-----------|
| **Detected in** | REV-003 (F-04) — AITL-REV-Approval 2026-08-27 |
| **Incident** | — |
| **Affected US / Bolt** | US-001 / BOLT-003 (familia de manifests v1) |
| **Dedicated Bolt** | US-001.BOLT-009 |
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
| 2026-08-27 | Defect reported (draft) — REV-003 F-04 | @eugenioserrano |
| 2026-08-27 | **AITL-BUG-Approval** — aprobado (bloque con BUG-002..BUG-012); BOLT-009 asignado | @eugenioserrano |
| 2026-08-27 | **Fix entregado** — MEM-260827-0406-fix-schema-version-contradicciones.md (AITL-MEM-Approval 2026-08-27); BUG fixed
