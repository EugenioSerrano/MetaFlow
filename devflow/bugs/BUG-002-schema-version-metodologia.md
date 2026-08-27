---
id: "BUG-002"
title: "MetaFlow.md §3.12/§5.16 declaran schema_version \"5.0\" y la sección de migración 4.0→5.0 quedó corrupta"
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
  - "distribution-kit/metaflow/ai-sdlc/MetaFlow.md:3268, 3272-3278, 4769-4783 (síntoma en el output)"
expected_result: "La fuente normativa del kit debe declarar `schema_version` exactamente `\"1.0\"` (familia v1, decidida en REV-002/BOLT-003 y fijada por los schemas `manifest-v1*.schema.json` con `const: \"1.0\"`); la §5.16 debe describir la conversión real (agregar campos como `null`, checkpoints `CP-*`) sin narrativa 4.0→5.0 del linaje Avenga"
actual_result: "§3.12 dice `schema_version is exactly 5.0` y narra un rename corrupto (`checkpoint_approvals[]` → `checkpoint_approvals[]`); la política de evolución dice `4.x keeps 4.0, a schema change means 5.0`; §5.16 instruye conversiones inválidas (`CP-<CODE>-Approval` → `CP-<CODE>-Approval`, `CITL ⊇ CITL`, \"v5 checkpoint enum accepts only CITL-*\", `schema_version becomes \"5.0\"`)"
bolt: "US-001.BOLT-007-fix-schema-version-metodologia"
spec: "SPEC-260827-0355-bolt007-fix-schema-version-metodologia.md"
mem: "MEM-260827-0406-fix-schema-version-metodologia.md"
sources: ["REV-003 (F-01, F-02)"]
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
  acknowledgment_reason: "Aprobación del propietario (Functional Analyst autoasignado) sin hallazgos — BUG-002..BUG-012 aprobados en bloque desde REV-003 (AITL-REV-Approval 2026-08-27). Ruteo: BOLT-007 bajo US-001"
tags: [bug, kit, schema-version, migracion, restos-v5]
---

# BUG-002 — §3.12/§5.16 del MetaFlow.md con schema_version "5.0" y migración corrupta

| Field              | Value |
|--------------------|-------|
| **Severity**       | high |
| **Nature**         | functional |
| **Detected in**    | review (REV-003 F-01/F-02) |
| **Status**         | approved |
| **Affected files** | output: `distribution-kit/metaflow/ai-sdlc/MetaFlow.md:3268, 3272-3278, 4769-4783` · root cause: `src/transform.py` + `mapping.json` |
| **Dedicated Bolt** | US-001.BOLT-007 (functional) |

## 1. Summary

El documento normativo del kit (MetaFlow.md) conserva la narrativa del
linaje Avenga v5: §3.12 declara `schema_version` "5.0" (los schemas v1
exigen `"1.0"`) y §5.16 describe una migración 4.0→5.0 con renames
corruptos (`checkpoint_approvals[]` → `checkpoint_approvals[]`, `CP-*` →
`CP-*`, "CITL ⊇ CITL") que, si un adoptante la siguiera, produce manifests
que **no validan** contra los schemas del propio kit.

## 2. Reproduction

1. Regenerar el kit: `python src/transform.py` (input-kit v5.1 → distribution-kit).
2. Verificar en el output:

**Expected result:** cero coincidencias de `schema_version is exactly 5.0`,
`a schema change means 5.0`, `becomes "5.0"`, `CITL ⊇ CITL` y `accepts only CITL-*`
en `distribution-kit/metaflow/ai-sdlc/MetaFlow.md`.

**Actual result:** coinciden en las líneas 3268, 3272-3278 y 4769-4783
(§3.12 y §5.16).

## 3. Root cause

El diccionario/reglas del transform no adaptaron la narrativa de la familia
de manifests del input-kit Avenga v5 (donde la familia era v4→v5 con
`hitl_approvals` → `checkpoint_approvals` y prefijos `HITL-*` → `AITL-*`):
esos pasajes se copiaron al kit MetaFlow con reemplazos mecánicos que
dejaron renames de identidad (`checkpoint_approvals[]` → `checkpoint_approvals[]`)
y una conversión que apunta a `"5.0"`/`CITL-*` — ambos inválidos contra
los schemas v1/CP-* del kit.

## 4. Impact

- **Users affected:** todos los adoptantes del kit (agentes que leen §3.12/§5.16).
- **Data impact:** manifests con `schema_version "5.0"` o checkpoints `CITL-*` no validan (G23) — la migración de un adoptante quedaría rota.
- **Workaround available:** no (la corrección es del pipeline).

## 5. Classification and routing

| Aspect | Value |
|--------|-------|
| **Nature** | functional → Functional Analyst aprueba |
| **Violated expectation** | Decisión REV-002/BOLT-003: familia v1 (`schema_version: "1.0"`); checkpoints canónicos `CP-*` |
| **Dedicated Bolt parent** | US-001 (feature — afecta el kit de salida) |

## 6. Fix status (strict TDD, ONE V-Bounce)

| Stage | Evidence | Status |
|-------|----------|--------|
| Reproduction test | RED: test del toolkit que exige cero `5.0`/`CITL ⊇ CITL`/`accepts only CITL-*` en el MetaFlow.md regenerado | Pending |
| Production fix | GREEN: reglas/diccionario del transform reescriben §3.12 (familia v1) y §5.16 (conversión real); kit regenerado sin coincidencias | Pending |
| MEM | MEM-YYMMDD-HHmm — red y green por separado | **Done** |

> El fix es estrictamente TDD en el V-Bounce del Bolt dedicado (BOLT-007).
> **No se edita el distribution-kit a mano**: se corrige el toolkit y se regenera.

## 7. Relations

| Relation | Reference |
|----------|-----------|
| **Detected in** | REV-003 (F-01, F-02) — AITL-REV-Approval 2026-08-27 |
| **Incident** | — |
| **Affected US / Bolt** | US-001 / BOLT-003 (familia de manifests v1 — origen de la decisión) |
| **Dedicated Bolt** | US-001.BOLT-007 |
| **Canonical SPEC** | (a crear) |
| **ADRs** | ADR-001 (toolkit de transformación); ADR-003 (numeración) |
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
| 2026-08-27 | Defect reported (draft) — REV-003 F-01/F-02 | @eugenioserrano |
| 2026-08-27 | **AITL-BUG-Approval** — aprobado (bloque con BUG-003..BUG-012); BOLT-007 asignado | @eugenioserrano |
| 2026-08-27 | **Fix entregado** — MEM-260827-0406-fix-schema-version-metodologia.md (AITL-MEM-Approval 2026-08-27); BUG fixed
