---
id: "BUG-021"
title: "Historia del linaje previo presentada como historia propia del kit: 'removed in v4.2' (17 ubicaciones) y 'versions up to 4.1 shipped one inside metaflow/' (4 agent definitions)"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
severity: "medium"
nature: "functional"
status: "fixed"
owner: "eugenioserrano"
detected_in: "review"
detected_at: "2026-08-27T17:04:54-03:00"
incident_ref: ""
affected_artifacts:
  - "distribution-kit/metaflow/24-tests/README.md (27, 33, 72)"
  - "distribution-kit/metaflow/24-tests/uat/README.md (5-6, 32), uat/INDEX.md (5), uat/TEMPLATE-UAT.md (24-25)"
  - "distribution-kit/metaflow/02-analysis/README.md (46, 265)"
  - "distribution-kit/metaflow/ONBOARDING.md (75), README.md (351)"
  - "distribution-kit/metaflow/ai-sdlc/MetaFlow.md (§4.2, ~3977)"
  - "distribution-kit/CLAUDE.md, .agents/skills/ai-sdlc/SKILL.md, .github/agents/MetaFlow.agent.md, .opencode/agents/MetaFlow.md (§5.16: 'versions up to 4.1 shipped one inside metaflow/')"
expected_result: "Las menciones de versiones del linaje previo (v4.2, 4.1) se declaran como historia del linaje anterior — 'removed in the previous lineage', 'the previous lineage shipped one inside metaflow/' — o se reexpresan sin números del linaje ajeno ('dormant/reserved in this release'), coherentes con MetaFlow 1.1 y con la §5.16 del kit (que ya declara 'History of the previous family')"
actual_result: "El kit declara como historia propia: 'the UAT approval layer was removed in v4.2', 'DORMANT / RESERVED (v4.2)', 'versions up to 4.1 shipped one inside metaflow/'. MetaFlow es v1.1 y nunca tuvo versiones 4.x — la afirmación es falsa para esta línea (REV-005 F-01)"
task: "US-001.TASK-026"
spec: "SPEC-260827-1715-fix-historia-linaje"
mem: "MEM-260827-1725-fix-historia-linaje"
sources: ["REV-005 (F-01, CP-REV-Approval 2026-08-27)"]
review_ready_at: "2026-08-27T17:04:54-03:00"
review:
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "functional_analyst"
      model: null
  started_at: "2026-08-27T17:13:56-03:00"
  decided_at: "2026-08-27T17:13:56-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: ""
tags: [bug, kit, linaje, historia, migracion]
---

# BUG-021 — Historia del linaje previo presentada como historia propia del kit

| Field              | Value |
|--------------------|-------|
| **Severity**       | medium |
| **Nature**         | functional |
| **Detected in**    | review (REV-005 F-01) |
| **Status**         | draft |
| **Affected files** | 17 ubicaciones "v4.2" + 4 agent definitions "versions up to 4.1" (ver frontmatter) |
| **Dedicated TASK** | (a asignar tras CP-BUG-Approval — bajo US-001) |

## 1. Summary

El kit conserva afirmaciones de historia del linaje Avenga ("removed in
v4.2", "versions up to 4.1 shipped one inside `metaflow/`") presentadas
como historia propia de MetaFlow, que es v1.1 y nunca tuvo versiones 4.x.
En el input esas frases eran coherentes (Avenga sí tuvo v4.2/4.1); la
inconsistencia la introduce la transformación. La propia §5.16 del kit
(arreglada por BUG-019) declara el linaje previo explícitamente; estas 21
ubicaciones no lo hacen.

## 2. Reproduction

1. `grep -ri "v4.2" distribution-kit/` y `grep -r "versions up to 4.1" distribution-kit/`.

**Expected result:** cero menciones de versiones 4.x del linaje ajeno sin
declarar, o declaradas como historia del linaje previo.

**Actual result:** 17 + 4 ubicaciones narran la historia del linaje previo
como propia (REV-005 F-01 con líneas exactas).

## 3. Root cause

La transformación reemplazó tokens y carpetas pero no adaptó las
afirmaciones históricas con números de versión del linaje de origen
(4.2/4.1), que solo son verdaderas en Avenga. El fix de BUG-019 cubrió la
apertura de §5.16 pero no las demás menciones.

## 4. Impact

- **Users affected:** todos los adoptantes del kit (leen una historia falsa de la metodología).
- **Data impact:** ninguno.
- **Workaround available:** no.

## 5. Classification and routing

| Aspect | Value |
|--------|-------|
| **Nature** | functional → Functional Analyst aprueba |
| **Violated expectation** | Coherencia de la línea MetaFlow 1.1 (la propia §5.16 declara el linaje previo como historia) |
| **Dedicated TASK parent** | US-001 (kit de salida) |

## 6. Fix status (strict TDD, ONE Delivery Loop)

| Stage | Evidence | Status |
|-------|----------|--------|
| Reproduction test | RED: test que exige cero "v4.2"/"versions up to 4.1" sin declaración de linaje en el kit regenerado | Pending |
| Production fix | GREEN: reglas del diccionario reexpresan las 21 ubicaciones; kit regenerado | Pending |
| MEM | MEM-YYMMDD-HHmm — red y green por separado | Pending |

## 7. Relations

| Relation | Reference |
|----------|-----------|
| **Detected in** | REV-005 (F-01) — CP-REV-Approval 2026-08-27 |
| **Dedicated TASK** | (a asignar — US-001.TASK-NNN) |
| **ADRs** | ADR-001 (toolkit de transformación) |

---

## 8. CP-BUG-Approval

> **MetaFlow §2.16, §3.0.** Este BUG permanece en draft hasta que un
> humano calificado registra `CP-BUG-Approval`.

| Field | Value |
|-------|-------|
| **Approver** | human:eugenioserrano (rol autoasignado) |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-27T17:04:54-03:00` |
| **review.started_at** | `2026-08-27T17:13:56-03:00` |
| **review.decided_at** | `2026-08-27T17:13:56-03:00` |
| **Findings** | Ninguno — aprobado sin comentarios |

---

## 9. History

| Date | Change | Author |
|------|--------|--------|
| 2026-08-27 | **CP-BUG-Approval** — aprobado en bloque BUG-021..024; US-001.TASK-026 asignado | @eugenioserrano |
| 2026-08-27 | Defect reported (draft) — REV-005 F-01 | @eugenioserrano |
