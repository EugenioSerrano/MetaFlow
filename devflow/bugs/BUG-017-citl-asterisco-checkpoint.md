---
id: "BUG-017"
title: ""CITL-*" usado como nombre de checkpoint en 24-tests/test-cases/README.md y GUARDRAILS T12"
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
  - "distribution-kit/metaflow/24-tests/test-cases/README.md, distribution-kit/metaflow/GUARDRAILS.md T12 (síntoma); src/transform.py + mapping.json (root cause)"
expected_result: "Los checkpoints se nombran con el prefijo canónico `CP-*` (o "CITL decision" como concepto): "`CP-*-Approval` codes are never translated" y "each artifact's `CP-*` decision""
actual_result: "24-tests/test-cases/README.md dice "`CITL-*` codes are never translated" y GUARDRAILS.md T12 dice "each artifact's `CITL-*` decision" — el prefijo `CITL-*` como nombre de checkpoint es no canónico (G05) y quedó fuera del patrón del test del BUG-007 (que busca CITL-<CODE> sin asterisco)"
bolt: "US-001.BOLT-022-fix-citl-asterisco"
spec: "SPEC-260827-1029-fix-citl-asterisco.md"
mem: "MEM-260827-1034-fix-citl-asterisco.md"
sources: ["REV-004 (F-05)"]
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
  acknowledgment_reason: "Aprobación del propietario (Functional Analyst autoasignado) sin hallazgos — BUG-013..019 aprobados en bloque desde REV-004 (AITL-REV-Approval 2026-08-27). Ruteo: US-001.BOLT-022 bajo US-001"
tags: [bug, kit, revision-004]
---

# BUG-017 — "CITL-*" usado como nombre de checkpoint en 24-tests/test-cases/README.md y GUARDRAILS T12

| Field              | Value |
|--------------------|-------|
| **Severity**       | medium |
| **Nature**         | functional |
| **Detected in**    | review (REV-004 F-05) |
| **Status**         | draft |
| **Affected files** | distribution-kit/metaflow/24-tests/test-cases/README.md, distribution-kit/metaflow/GUARDRAILS.md T12 (síntoma); src/transform.py + mapping.json (root cause) |
| **Dedicated Bolt** | US-001.BOLT-022 (functional) |

## 1. Summary

"CITL-*" usado como nombre de checkpoint en 24-tests/test-cases/README.md y GUARDRAILS T12. Detectado en el análisis fresco del kit regenerado (REV-004, F-05):
el patrón quedó fuera de los tests de reproducción de BOLT-007..017 porque
verifican el MetaFlow.md y los patrones puntuales, no las variantes de los
wrappers ni las frases del charter.

## 2. Reproduction

1. Regenerar el kit: `python src/transform.py`.
2. Verificar en el output (grep del patrón):

**Expected result:** Los checkpoints se nombran con el prefijo canónico `CP-*` (o "CITL decision" como concepto): "`CP-*-Approval` codes are never translated" y "each artifact's `CP-*` decision"

**Actual result:** 24-tests/test-cases/README.md dice "`CITL-*` codes are never translated" y GUARDRAILS.md T12 dice "each artifact's `CITL-*` decision" — el prefijo `CITL-*` como nombre de checkpoint es no canónico (G05) y quedó fuera del patrón del test del BUG-007 (que busca CITL-<CODE> sin asterisco)

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
| **Detected in** | REV-004 (F-05) — AITL-REV-Approval 2026-08-27 |
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
| 2026-08-27 | Defect reported (draft) — REV-004 F-05 | @eugenioserrano |
| 2026-08-27 | **AITL-BUG-Approval** — aprobado (bloque con BUG-013..019); US-001.BOLT-022 asignado | @eugenioserrano |
| 2026-08-27 | **Fix entregado** — MEM-260827-1034-fix-citl-asterisco.md (AITL-MEM-Approval 2026-08-27); BUG fixed | @eugenioserrano |
