---
id: "BUG-014"
title: "G05 interno de los 4 agent definitions corrupto (placeholder y canónico mal declarado)"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
severity: "high"
nature: "functional"
status: "fixed"
owner: "eugenioserrano"
detected_in: "review"
detected_at: "2026-08-27T10:25:37-03:00"
incident_ref: ""
affected_artifacts:
  - "distribution-kit/CLAUDE.md, .agents/skills/ai-sdlc/SKILL.md, .github/agents/MetaFlow.agent.md, .opencode/agents/MetaFlow.md (síntoma); src/transform.py + mapping.json (root cause)"
expected_result: "El G05 de los wrappers debe ser legible y declarar el canónico correcto (`CP-<CODE>-Approval`), sin placeholder vacío: "Use a legacy checkpoint name (the pre-v5 checkpoint prefix) or non-canonical identifiers""
actual_result: "Los wrappers dicen: "| G05 | Legacy checkpoint names (the ) or any non-canonical `CITL-*` identifier (canonical is `CITL-*`; `CITL-*` , G36) |" — placeholder "(the )" vacío y "(canonical is `CITL-*`)" erróneo (variante del BUG-006/007 no cubierta: la versión del GUARDRAILS.md sí se corrigió con R11-1, la de los wrappers no)"
bolt: "US-001.BOLT-019-fix-g05-wrappers"
spec: "SPEC-260827-1029-fix-g05-wrappers.md"
mem: "MEM-260827-1034-fix-g05-wrappers.md"
sources: ["REV-004 (F-02)"]
review_ready_at: "2026-08-27T10:25:37-03:00"
review:
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "functional_analyst"
      model: null
  started_at: "2026-08-27T10:30:00-03:00"
  decided_at: "2026-08-27T10:30:00-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Aprobación del propietario (Functional Analyst autoasignado) sin hallazgos — BUG-013..019 aprobados en bloque desde REV-004 (AITL-REV-Approval 2026-08-27). Ruteo: US-001.BOLT-019 bajo US-001"
tags: [bug, kit, revision-004]
---

# BUG-014 — G05 interno de los 4 agent definitions corrupto (placeholder y canónico mal declarado)

| Field              | Value |
|--------------------|-------|
| **Severity**       | high |
| **Nature**         | functional |
| **Detected in**    | review (REV-004 F-02) |
| **Status**         | draft |
| **Affected files** | distribution-kit/CLAUDE.md, .agents/skills/ai-sdlc/SKILL.md, .github/agents/MetaFlow.agent.md, .opencode/agents/MetaFlow.md (síntoma); src/transform.py + mapping.json (root cause) |
| **Dedicated Bolt** | US-001.BOLT-019 (functional) |

## 1. Summary

G05 interno de los 4 agent definitions corrupto (placeholder y canónico mal declarado). Detectado en el análisis fresco del kit regenerado (REV-004, F-02):
el patrón quedó fuera de los tests de reproducción de BOLT-007..017 porque
verifican el MetaFlow.md y los patrones puntuales, no las variantes de los
wrappers ni las frases del charter.

## 2. Reproduction

1. Regenerar el kit: `python src/transform.py`.
2. Verificar en el output (grep del patrón):

**Expected result:** El G05 de los wrappers debe ser legible y declarar el canónico correcto (`CP-<CODE>-Approval`), sin placeholder vacío: "Use a legacy checkpoint name (the pre-v5 checkpoint prefix) or non-canonical identifiers"

**Actual result:** Los wrappers dicen: "| G05 | Legacy checkpoint names (the ) or any non-canonical `CITL-*` identifier (canonical is `CITL-*`; `CITL-*` , G36) |" — placeholder "(the )" vacío y "(canonical is `CITL-*`)" erróneo (variante del BUG-006/007 no cubierta: la versión del GUARDRAILS.md sí se corrigió con R11-1, la de los wrappers no)

## 3. Root cause

El diccionario/reglas del transform (mapping.json) no cubre este patrón
(variante condensada de los wrappers, frase del charter, anuncio residual):
las reglas de corrección de BOLT-007..017 apuntaron a los patrones del
MetaFlow.md y del GUARDRAILS.md, no a las versiones paralelas que viven en
los agent definitions ni a los anuncios de MetaFlow.md/README.md.

## 4. Impact

- **Users affected:** adoptantes del kit (agentes instalados y lectores de la metodología).
- **Data impact:** narrativa corrupta/tautológica en el agente y el charter; anuncios de archivos inexistentes.
- **Workaround available:** no (la corrección es del pipeline).

## 5. Classification and routing

| Aspect | Value |
|--------|-------|
| **Nature** | functional → Functional Analyst aprueba |
| **Violated expectation** | Vocabulario canónico del kit (CP-*, v1, CITL como concepto) y coherencia de anuncios |
| **Dedicated Bolt parent** | US-001 (feature — afecta el kit de salida) |

## 6. Fix status (strict TDD, ONE V-Bounce)

| Stage | Evidence | Status |
|-------|----------|--------|
| Reproduction test | RED: test del toolkit que exige el patrón corregido en el kit regenerado | Pending |
| Production fix | GREEN: reglas/diccionario del transform corrigen el patrón; kit regenerado sin coincidencias | Pending |
| MEM | MEM-YYMMDD-HHmm — red y green por separado | Pending |

> Fix TDD en el V-Bounce del Bolt dedicado. **No se edita el distribution-kit a mano**: se corrige el toolkit y se regenera.

## 7. Relations

| Relation | Reference |
|----------|-----------|
| **Detected in** | REV-004 (F-02) — AITL-REV-Approval 2026-08-27 |
| **Incident** | — |
| **Affected US / Bolt** | US-001 / BOLT-007..017 (ronda anterior de restos v5) |
| **Dedicated Bolt** | (a crear tras aprobación) |
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

---

## 9. History

| Date | Change | Author |
|------|--------|--------|
| 2026-08-27 | Defect reported (draft) — REV-004 F-02 | @eugenioserrano |
| 2026-08-27 | **AITL-BUG-Approval** — aprobado (bloque con BUG-013..019); US-001.BOLT-019 asignado | @eugenioserrano |
| 2026-08-27 | **Fix entregado** — MEM-260827-1034-fix-g05-wrappers.md (AITL-MEM-Approval 2026-08-27); BUG fixed | @eugenioserrano |
