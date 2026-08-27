---
id: "BUG-003"
title: "Los 4 agent definitions del kit instruyen schema_version \"5.0\""
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
severity: "high"
nature: "functional"
status: "fixed"
owner: "eugenioserrano"
detected_in: "review"
detected_at: "2026-08-27T03:45:23-03:00"
incident_ref: ""
affected_artifacts:
  - "src/transform.py + mapping.json (diccionario/reglas de contenido — root cause)"
  - "tools/ (verificador de tokens — debe fijar el patrón)"
  - "distribution-kit/CLAUDE.md:529, distribution-kit/.agents/skills/ai-sdlc/SKILL.md:546, distribution-kit/.github/agents/MetaFlow.agent.md:577, distribution-kit/.opencode/agents/MetaFlow.md:557 (síntoma en el output)"
expected_result: "Los 4 agent definitions (CLAUDE.md, SKILL.md, MetaFlow.agent.md, MetaFlow.md de .opencode) deben declarar `schema_version` exactly `\"1.0\"` (familia v1, según los schemas `manifest-v1*.schema.json`)"
actual_result: "La sección \"Manifest Family v5\" de cada wrapper dice `schema_version` (exactly `\"5.0\"`) — el agente instalado en proyectos adoptantes creará manifests con `schema_version: \"5.0\"` que fallan la validación G23 contra los schemas del kit"
task: "US-001.TASK-008-fix-schema-version-agentes"
spec: "SPEC-260827-0355-bolt008-fix-schema-version-agentes.md"
mem: "MEM-260827-0406-fix-schema-version-agentes.md"
sources: ["REV-003 (F-03)"]
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
  acknowledgment_reason: "Aprobación del propietario (Functional Analyst autoasignado) sin hallazgos — BUG-002..BUG-012 aprobados en bloque desde REV-003 (CP-REV-Approval 2026-08-27). Ruteo: TASK-008 bajo US-001"
tags: [bug, kit, agentes, schema-version, restos-v5]
---

# BUG-003 — Agent definitions con schema_version "5.0"

| Field              | Value |
|--------------------|-------|
| **Severity**       | high |
| **Nature**         | functional |
| **Detected in**    | review (REV-003 F-03) |
| **Status**         | approved |
| **Affected files** | output: los 4 wrappers de agentes (`CLAUDE.md`, `.agents/skills/ai-sdlc/SKILL.md`, `.github/agents/MetaFlow.agent.md`, `.opencode/agents/MetaFlow.md`) · root cause: `src/transform.py` + `mapping.json` |
| **Dedicated TASK** | US-001.TASK-008 (functional) |

## 1. Summary

Los 4 agent definitions que el kit instala en los proyectos adoptantes
conservan la instrucción `schema_version` exactly `"5.0"` de la sección
"Manifest Family" — el mismo resto del linaje Avenga v5 que contradice los
schemas v1 del kit. Es la instrucción más ejecutable del kit: el agente que
la siga creará manifests que **no validan** (G23).

## 2. Reproduction

1. Regenerar el kit: `python src/transform.py`.
2. Verificar en el output:

**Expected result:** cero coincidencias de `schema_version` (exactly `"5.0"`)
en `distribution-kit/CLAUDE.md`, `.agents/skills/ai-sdlc/SKILL.md`,
`.github/agents/MetaFlow.agent.md` y `.opencode/agents/MetaFlow.md`.

**Actual result:** una coincidencia en cada uno (líneas 529/546/577/557).

## 3. Root cause

El diccionario/reglas del transform no cubrió el texto de la sección
"Manifest Family v5" de los wrappers del input-kit Avenga v5 (que decía
`"5.0"`); los wrappers se regeneraron/renombraron (TASK-002) pero ese
valor quedó intacto en el cuerpo.

## 4. Impact

- **Users affected:** todos los adoptantes del kit (el agente instalado).
- **Data impact:** manifests con `schema_version: "5.0"` no validan contra `manifest-v1*.schema.json` (G23); el adoptante pierde la garantía de trazabilidad mecánica.
- **Workaround available:** no.

## 5. Classification and routing

| Aspect | Value |
|--------|-------|
| **Nature** | functional → Functional Analyst aprueba |
| **Violated expectation** | Decisión REV-002/TASK-003: familia v1 (`schema_version: "1.0"`) |
| **Dedicated TASK parent** | US-001 (feature — afecta el kit de salida) |

## 6. Fix status (strict TDD, ONE V-Bounce)

| Stage | Evidence | Status |
|-------|----------|--------|
| Reproduction test | RED: test del toolkit que exige cero `exactly "5.0"` en los 4 wrappers regenerados | Pending |
| Production fix | GREEN: diccionario/reglas corrigen la sección Manifest Family a `"1.0"`; wrappers regenerados | Pending |
| MEM | MEM-YYMMDD-HHmm — red y green por separado | Pending |

> Fix TDD en el V-Bounce del TASK dedicado (TASK-008). **No se edita el kit a mano.**
> Nota: corregir también el nombre "Manifest Family v5" de esa sección
> (ver BUG-005).

## 7. Relations

| Relation | Reference |
|----------|-----------|
| **Detected in** | REV-003 (F-03) — CP-REV-Approval 2026-08-27 |
| **Incident** | — |
| **Affected US / TASK** | US-001 / TASK-002 (wrappers — origen del rename) |
| **Dedicated TASK** | US-001.TASK-008 |
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
| 2026-08-27 | Defect reported (draft) — REV-003 F-03 | @eugenioserrano |
| 2026-08-27 | **CP-BUG-Approval** — aprobado (bloque con BUG-002..BUG-012); TASK-008 asignado | @eugenioserrano |
| 2026-08-27 | **Fix entregado** — MEM-260827-0406-fix-schema-version-agentes.md (CP-MEM-Approval 2026-08-27); BUG fixed
