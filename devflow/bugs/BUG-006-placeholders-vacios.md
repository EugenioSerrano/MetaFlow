---
id: "BUG-006"
title: "Placeholders vacíos \"The  is invalid\" en 7 lugares del kit — incluida la regla G05"
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
  - "distribution-kit/CLAUDE.md:51, .github/agents/MetaFlow.agent.md:83, .opencode/agents/MetaFlow.md:67, .agents/skills/ai-sdlc/SKILL.md:56, metaflow/README.md:244, metaflow/ONBOARDING.md:70, metaflow/GUARDRAILS.md:60 (síntoma en el output)"
expected_result: "La regla G05 y las frases de checkpoint map deben nombrar explícitamente el prefijo legacy, p. ej. \"the legacy `AITL-*`/`HITL-*` prefix is invalid\" / \"Use a legacy checkpoint name (the pre-v5 `AITL-*`/`HITL-*` prefix) or non-canonical identifiers\""
actual_result: "7 frases truncadas con placeholder vacío: \"The  is invalid\" / \"the legacy  is invalid\" / \"Use  (the ) or non-canonical `CITL-*` identifiers\" — la definición de la regla G05 (que un agente DEBE enforce) no se puede leer"
bolt: "US-001.BOLT-011-fix-placeholders-g05"
spec: "SPEC-260827-0355-bolt011-fix-placeholders-g05.md"
mem: "MEM-260827-0407-fix-placeholders-g05.md"
sources: ["REV-003 (F-06)"]
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
  acknowledgment_reason: "Aprobación del propietario (Functional Analyst autoasignado) sin hallazgos — BUG-002..BUG-012 aprobados en bloque desde REV-003 (AITL-REV-Approval 2026-08-27). Ruteo: BOLT-011 bajo US-001"
tags: [bug, kit, guardrails, checkpoints, placeholders]
---

# BUG-006 — Placeholders vacíos "The  is invalid" (G05 ilegible)

| Field              | Value |
|--------------------|-------|
| **Severity**       | high |
| **Nature**         | functional |
| **Detected in**    | review (REV-003 F-06) |
| **Status**         | approved |
| **Affected files** | output: 7 archivos (ver frontmatter) · root cause: `src/transform.py` + `mapping.json` |
| **Dedicated Bolt** | US-001.BOLT-011 (functional) |

## 1. Summary

Durante la adaptación del linaje (AITL→CP) el reemplazo del prefijo legacy
dejó **espacios vacíos** en 7 frases del kit, incluida la definición de la
regla **G05** del GUARDRAILS ("Use  (the ) or non-canonical `CITL-*`
identifiers") y el checkpoint map del README ("the legacy  is invalid").
Un agente no puede leer qué debe bloquear.

## 2. Reproduction

1. Regenerar el kit: `python src/transform.py`.
2. Verificar en el output:

**Expected result:** cero frases con doble espacio vacío (`The  is`,
`the legacy  is`, `Use  (the )`) en `distribution-kit/`.

**Actual result:** 7 coincidencias: CLAUDE.md:51, MetaFlow.agent.md:83,
.opencode/agents/MetaFlow.md:67, SKILL.md:56, README.md:244,
ONBOARDING.md:70 y GUARDRAILS.md:60 (G05).

## 3. Root cause

El diccionario del transform reemplazó "`AITL-*`/`HITL-*` prefix" (o
similar) por la cadena vacía en esas frases — el patrón original del
input-kit Avenga ("The pre-v5 `HITL-*` prefix is invalid") quedó con el
token borrado y el espacio residual.

## 4. Impact

- **Users affected:** agentes que enforcean GUARDRAILS (G05) y humanos que leen el checkpoint map.
- **Data impact:** regla de bloqueo ilegible — riesgo de no bloquear nombres legacy.
- **Workaround available:** no.

## 5. Classification and routing

| Aspect | Value |
|--------|-------|
| **Nature** | functional → Functional Analyst aprueba |
| **Violated expectation** | Documentación normativa legible y ejecutable (G05) |
| **Dedicated Bolt parent** | US-001 (feature — afecta el kit de salida) |

## 6. Fix status (strict TDD, ONE V-Bounce)

| Stage | Evidence | Status |
|-------|----------|--------|
| Reproduction test | RED: test del toolkit que exige cero dobles espacios vacíos / frases truncadas en el kit | Pending |
| Production fix | GREEN: diccionario completa las 7 frases con el prefijo legacy explícito; kit regenerado | Pending |
| MEM | MEM-YYMMDD-HHmm — red y green por separado | Pending |

> Fix TDD en el V-Bounce del Bolt dedicado (BOLT-011). **No se edita el kit a mano.**

## 7. Relations

| Relation | Reference |
|----------|-----------|
| **Detected in** | REV-003 (F-06) — AITL-REV-Approval 2026-08-27 |
| **Incident** | — |
| **Affected US / Bolt** | US-001 (kit de salida) |
| **Dedicated Bolt** | US-001.BOLT-011 |
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
| 2026-08-27 | Defect reported (draft) — REV-003 F-06 | @eugenioserrano |
| 2026-08-27 | **AITL-BUG-Approval** — aprobado (bloque con BUG-002..BUG-012); BOLT-011 asignado | @eugenioserrano |
| 2026-08-27 | **Fix entregado** — MEM-260827-0407-fix-placeholders-g05.md (AITL-MEM-Approval 2026-08-27); BUG fixed
