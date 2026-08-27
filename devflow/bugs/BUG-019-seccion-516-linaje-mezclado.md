---
id: "BUG-019"
title: "§5.16: narrativa del linaje previo (3.0→4.0→5.0) mezclada con el presente del kit"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
severity: "medium"
nature: "functional"
status: "fixed"
owner: "eugenioserrano"
detected_in: "review"
detected_at: "2026-08-27T10:25:37-03:00"
incident_ref: ""
affected_artifacts:
  - "distribution-kit/metaflow/ai-sdlc/MetaFlow.md §5.16 (síntoma); src/transform.py + mapping.json (root cause)"
expected_result: "La §5.16 debe declarar explícitamente la historia 3.0→4.0→5.0 como narrativa del linaje previo no aplicable a MetaFlow v1.1, y describir la conversión real de la familia v1 — sin mezclar "v1 enum accepts only CP-*" dentro de la historia 4.0→5.0 ni "schema_version becomes `"1.0"`" en una narrativa que dice 4.0→5.0"
actual_result: "La §5.16 narra "`3.0` → `4.0` is exactly this shape... `4.0` → `5.0` is a rename... The v1 `checkpoint` enum accepts **only** `CP-*`... `schema_version` becomes `"1.0"`" — historia del linaje Avenga mezclada con el presente del kit; semántica confusa para un adoptante que migra"
bolt: "US-001.BOLT-024-fix-516-linaje"
spec: "SPEC-260827-1029-fix-516-linaje.md"
mem: "MEM-260827-1034-fix-516-linaje.md"
sources: ["REV-004 (F-07)"]
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
  acknowledgment_reason: "Aprobación del propietario (Functional Analyst autoasignado) sin hallazgos — BUG-013..019 aprobados en bloque desde REV-004 (AITL-REV-Approval 2026-08-27). Ruteo: US-001.BOLT-024 bajo US-001"
tags: [bug, kit, revision-004]
---

# BUG-019 — §5.16: narrativa del linaje previo (3.0→4.0→5.0) mezclada con el presente del kit

| Field              | Value |
|--------------------|-------|
| **Severity**       | medium |
| **Nature**         | functional |
| **Detected in**    | review (REV-004 F-07) |
| **Status**         | draft |
| **Affected files** | distribution-kit/metaflow/ai-sdlc/MetaFlow.md §5.16 (síntoma); src/transform.py + mapping.json (root cause) |
| **Dedicated Bolt** | US-001.BOLT-024 (functional) |

## 1. Summary

§5.16: narrativa del linaje previo (3.0→4.0→5.0) mezclada con el presente del kit. Detectado en el análisis fresco del kit regenerado (REV-004, F-07):
el patrón quedó fuera de los tests de reproducción de BOLT-007..017 porque
verifican el MetaFlow.md y los patrones puntuales, no las variantes de los
wrappers ni las frases del charter.

## 2. Reproduction

1. Regenerar el kit: `python src/transform.py`.
2. Verificar en el output (grep del patrón):

**Expected result:** La §5.16 debe declarar explícitamente la historia 3.0→4.0→5.0 como narrativa del linaje previo no aplicable a MetaFlow v1.1, y describir la conversión real de la familia v1 — sin mezclar "v1 enum accepts only CP-*" dentro de la historia 4.0→5.0 ni "schema_version becomes `"1.0"`" en una narrativa que dice 4.0→5.0

**Actual result:** La §5.16 narra "`3.0` → `4.0` is exactly this shape... `4.0` → `5.0` is a rename... The v1 `checkpoint` enum accepts **only** `CP-*`... `schema_version` becomes `"1.0"`" — historia del linaje Avenga mezclada con el presente del kit; semántica confusa para un adoptante que migra

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
| **Detected in** | REV-004 (F-07) — AITL-REV-Approval 2026-08-27 |
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
| 2026-08-27 | Defect reported (draft) — REV-004 F-07 | @eugenioserrano |
| 2026-08-27 | **AITL-BUG-Approval** — aprobado (bloque con BUG-013..019); US-001.BOLT-024 asignado | @eugenioserrano |
| 2026-08-27 | **Fix entregado** — MEM-260827-1034-fix-516-linaje.md (AITL-MEM-Approval 2026-08-27); BUG fixed | @eugenioserrano |
