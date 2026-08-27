---
id: "BUG-005"
title: "Restos de naming \"Manifest family v5\" / \"Schema family v5\" / \"manifest v5\" en 8+ archivos del kit"
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
  - "distribution-kit/metaflow/ai-sdlc/MetaFlow.md:2908,2922,2948,3384; 23-metrics/README.md:1,177,252; README.md:59,177,192,377; GUARDRAILS.md:480; 13-bugs/README.md:204; ai-sdlc/INDEX.md:13; 42-reports/README.md:45; .agents/skills/ai-sdlc/SKILL.md:3 (síntoma en el output)"
expected_result: "El nombre de la familia de manifests debe ser \"Manifest family v1\" (o simplemente \"manifest family\") en todos los archivos — la familia es v1 (`manifest-v1*.schema.json`, `schema_version: \"1.0\"`, decisión REV-002/TASK-003)"
actual_result: "\"Manifest family v5\" / \"Schema family v5\" / \"manifest v5\" / \"Schema v5 example\" / \"the three v5 schemas\" sobrevive en 8+ archivos (título §3.12, READMEs, GUARDRAILS, INDEX, SKILL.md description) — el escáner del REV-002 no lo detectó por buscar patrones literales `v5.1`/`manifest-v1`"
task: "US-001.TASK-010-fix-naming-familia-v1"
spec: "SPEC-260827-0355-bolt010-fix-naming-familia-v1.md"
mem: "MEM-260827-0407-fix-naming-familia-v1.md"
sources: ["REV-003 (F-05)"]
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
  acknowledgment_reason: "Aprobación del propietario (Functional Analyst autoasignado) sin hallazgos — BUG-002..BUG-012 aprobados en bloque desde REV-003 (CP-REV-Approval 2026-08-27). Ruteo: TASK-010 bajo US-001"
tags: [bug, kit, naming, restos-v5]
---

# BUG-005 — Restos de naming "Manifest family v5" en el kit

| Field              | Value |
|--------------------|-------|
| **Severity**       | medium |
| **Nature**         | functional |
| **Detected in**    | review (REV-003 F-05) |
| **Status**         | approved |
| **Affected files** | output: 8+ archivos del kit (ver frontmatter) · root cause: `src/transform.py` + `mapping.json` |
| **Dedicated TASK** | US-001.TASK-010 (functional) |

## 1. Summary

El nombre "Manifest family v5"/"Schema family v5" (y variantes) del linaje
Avenga sobrevive en la documentación del kit aunque la familia de manifests
es **v1**. Incluye la descripción de la skill `ai-sdlc` (lo primero que lee
un agente al cargar la skill).

## 2. Reproduction

1. Regenerar el kit: `python src/transform.py`.
2. Verificar en el output:

**Expected result:** cero coincidencias de `Manifest family v5`,
`Schema family v5`, `manifest v5`, `Schema v5 example`, `three v5 schemas`
y `outside manifest v5` en `distribution-kit/`.

**Actual result:** 13+ coincidencias en 8+ archivos (ver frontmatter).

## 3. Root cause

El diccionario del transform renombró la familia a v1 en schemas, JSONs y
la mayoría del texto, pero no las apariciones del nombre compuesto
"Manifest family v5" ni los títulos de sección "Schema family v5"/"Schema
v5 example" — el escáner del REV-002 tampoco las buscó.

## 4. Impact

- **Users affected:** adoptantes y agentes (la skill se autodescribe como v5).
- **Data impact:** naming contradictorio; confusión sobre la versión de la familia.
- **Workaround available:** no.

## 5. Classification and routing

| Aspect | Value |
|--------|-------|
| **Nature** | functional → Functional Analyst aprueba |
| **Violated expectation** | Decisión REV-002/TASK-003: familia v1 |
| **Dedicated TASK parent** | US-001 (feature — afecta el kit de salida) |

## 6. Fix status (strict TDD, ONE V-Bounce)

| Stage | Evidence | Status |
|-------|----------|--------|
| Reproduction test | RED: test del toolkit que exige cero `family v5`/`Schema v5`/`manifest v5` en todo el kit | Pending |
| Production fix | GREEN: diccionario renombra a v1; kit regenerado sin coincidencias | Pending |
| MEM | MEM-YYMMDD-HHmm — red y green por separado | Pending |

> Fix TDD en el V-Bounce del TASK dedicado (TASK-010). **No se edita el kit a mano.**

## 7. Relations

| Relation | Reference |
|----------|-----------|
| **Detected in** | REV-003 (F-05) — CP-REV-Approval 2026-08-27 |
| **Incident** | — |
| **Affected US / TASK** | US-001 / TASK-003 (familia de manifests v1) |
| **Dedicated TASK** | US-001.TASK-010 |
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
| 2026-08-27 | Defect reported (draft) — REV-003 F-05 | @eugenioserrano |
| 2026-08-27 | **CP-BUG-Approval** — aprobado (bloque con BUG-002..BUG-012); TASK-010 asignado | @eugenioserrano |
| 2026-08-27 | **Fix entregado** — MEM-260827-0407-fix-naming-familia-v1.md (CP-MEM-Approval 2026-08-27); BUG fixed
