---
id: "BUG-010"
title: "MetaFlow.md con frontmatter version \"5.1\" y autor vacío en la cita del paper"
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
  - "distribution-kit/metaflow/ai-sdlc/MetaFlow.md:3,184 (síntoma en el output)"
expected_result: "El frontmatter del MetaFlow.md debe declarar `version: \"1.1\"` (igual que `metaflow/VERSION` y los 73 archivos con \"Methodology version: 1.1\"); la cita del paper debe nombrar a su autor"
actual_result: "El frontmatter YAML (línea 3) declara `version: \"5.1\"` — el documento normativo se autodeclara de otra versión; la línea 184 dice \"by , Principal Solutions Architect at AWS\" — el nombre del autor quedó vacío. El escáner del REV-002 no detectó el frontmatter (buscaba \"v5.1\"/\"Methodology version: 5.x\")"
task: "US-001.TASK-015-fix-frontmatter-cita"
spec: "SPEC-260827-0355-bolt015-fix-frontmatter-cita.md"
mem: "MEM-260827-0409-fix-frontmatter-cita.md"
sources: ["REV-003 (F-11, F-12)"]
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
  acknowledgment_reason: "Aprobación del propietario (Functional Analyst autoasignado) sin hallazgos — BUG-002..BUG-012 aprobados en bloque desde REV-003 (CP-REV-Approval 2026-08-27). Ruteo: TASK-015 bajo US-001"
tags: [bug, kit, frontmatter, version, cita]
---

# BUG-010 — Frontmatter "5.1" y autor vacío en el MetaFlow.md

| Field              | Value |
|--------------------|-------|
| **Severity**       | medium |
| **Nature**         | functional |
| **Detected in**    | review (REV-003 F-11/F-12) |
| **Status**         | approved |
| **Affected files** | output: `metaflow/ai-sdlc/MetaFlow.md:3,184` · root cause: `src/transform.py` + `mapping.json` |
| **Dedicated TASK** | US-001.TASK-015 (functional) |

## 1. Summary

El documento normativo del kit se autodeclara `version: "5.1"` en su
frontmatter (la versión real es 1.1) y la cita del paper fundacional quedó
con el autor vacío ("by , Principal Solutions Architect at AWS").

## 2. Reproduction

1. Regenerar el kit: `python src/transform.py`.
2. Verificar en el output:

**Expected result:** `version: "1.1"` en el frontmatter del MetaFlow.md y
nombre del autor presente en la cita (línea 184).

**Actual result:** `version: "5.1"` (línea 3) y "by , Principal Solutions
Architect at AWS" (línea 184).

## 3. Root cause

El diccionario del transform versionó los encabezados "Methodology
version:" pero no el campo YAML `version:` del frontmatter del documento
normativo (patrón distinto); la cita del paper se heredó del input-kit con
el autor sin completar.

## 4. Impact

- **Users affected:** adoptantes y agentes que leen la versión del documento normativo.
- **Data impact:** ambigüedad de versión (el documento dice 5.1, VERSION dice 1.1).
- **Workaround available:** no.

## 5. Classification and routing

| Aspect | Value |
|--------|-------|
| **Nature** | functional → Functional Analyst aprueba |
| **Violated expectation** | Una única versión de metodología por repositorio (`metaflow/VERSION` = 1.1) |
| **Dedicated TASK parent** | US-001 (feature — afecta el kit de salida) |

## 6. Fix status (strict TDD, ONE V-Bounce)

| Stage | Evidence | Status |
|-------|----------|--------|
| Reproduction test | RED: test del toolkit que exige `version: "1.1"` en el frontmatter y autor no vacío en la cita | Pending |
| Production fix | GREEN: diccionario corrige frontmatter + completa la cita; kit regenerado | Pending |
| MEM | MEM-YYMMDD-HHmm — red y green por separado | Pending |

> Fix TDD en el V-Bounce del TASK dedicado (TASK-015). **No se edita el kit a mano.**

## 7. Relations

| Relation | Reference |
|----------|-----------|
| **Detected in** | REV-003 (F-11, F-12) — CP-REV-Approval 2026-08-27 |
| **Incident** | — |
| **Affected US / TASK** | US-001 / TASK-003 (versionado — origen) |
| **Dedicated TASK** | US-001.TASK-015 |
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
| 2026-08-27 | Defect reported (draft) — REV-003 F-11/F-12 | @eugenioserrano |
| 2026-08-27 | **CP-BUG-Approval** — aprobado (bloque con BUG-002..BUG-012); TASK-015 asignado | @eugenioserrano |
| 2026-08-27 | **Fix entregado** — MEM-260827-0409-fix-frontmatter-cita.md (CP-MEM-Approval 2026-08-27); BUG fixed
