---
id: "BUG-001"
title: "Las reglas PN numeran las carpetas de plataforma .github/agents y .opencode/agents"
date: "2026-08-27"
author: "human:eugenioserrano"
llm: "deepseek/deepseek-v4-flash"
severity: "high"
nature: "functional"
status: "approved"
owner: "eugenioserrano"
detected_in: "production"
detected_at: "2026-08-27T03:03:38-03:00"
incident_ref: ""
affected_artifacts:
  - "src/transform.py (build_plan — aplicación de path rules)"
  - "mapping.json (reglas PN01–PN53)"
  - "distribution-kit/.github/51-agents/, distribution-kit/.opencode/51-agents/"
expected_result: "Las carpetas ocultas de plataforma (`.agents/`, `.github/`, `.opencode/`) no se numeran — la ADR-003 (y la ADR-002) lo declara explícitamente; `.github/agents/` y `.opencode/agents/` deben conservar sus nombres para que las plataformas reconozcan los agentes"
actual_result: "Las reglas de ruta PN (`^agents$` → `51-agents`) renombraron el componente `agents` dentro de `.github/` y `.opencode/`, dejando `.github/51-agents/` y `.opencode/51-agents/` — las plataformas ya no reconocen los agentes en el kit adoptado"
task: "US-001.TASK-006"
spec: ""
mem: ""
sources: ["informe del propietario 2026-08-27"]
review_ready_at: "2026-08-27T03:03:38-03:00"
review:
  decision: "approved"
  reviewers:
    - actor: "human:eugenioserrano"
      role: "functional_analyst"
      model: null
  started_at: "2026-08-27T03:04:43-03:00"
  decided_at: "2026-08-27T03:04:43-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Aprobación del propietario (Functional Analyst autoasignado) sin hallazgos — defecto confirmado por el smoke test de producción, 2026-08-27. Ruteo: TASK-006 bajo US-001"
tags: [bug, numeracion, plataforma, agentes]
---

# BUG-001 — Carpetas de plataforma numeradas (.github/agents, .opencode/agents)

| Field              | Value |
|--------------------|-------|
| **Severity**       | high |
| **Nature**         | functional |
| **Detected in**    | production (informe del propietario sobre el kit generado) |
| **Status**         | draft |
| **Affected files** | `src/transform.py` (path rules), `mapping.json` (PN01–PN53), `.github/51-agents/`, `.opencode/51-agents/` del kit |
| **Dedicated TASK** | US-001.TASK-006 (functional — pendiente de CP-BUG-Approval) |

## 1. Summary

Las reglas de ruta de numeración (`PN*`, `^agents$` → `51-agents`) se aplican
por componente de path **sin distinguir** las carpetas ocultas de plataforma:
`.github/agents/` y `.opencode/agents/` quedaron como `.github/51-agents/` y
`.opencode/51-agents/`, rompiendo el reconocimiento de agentes por parte de
las plataformas (GitHub Actions / opencode) en el kit adoptado — en
contradicción con la ADR-003/ADR-002 ("las carpetas de plataforma de la raíz
no se numeran").

## 2. Reproduction

1. Ejecutar `python src/transform.py` (input-kit v5.1 → distribution-kit).
2. Listar `distribution-kit/.github/` y `distribution-kit/.opencode/`.

**Expected result:** `.github/agents/` y `.opencode/agents/` (sin números) —
las plataformas reconocen los wrappers `MetaFlow.agent.md` / `MetaFlow.md`.

**Actual result:** `.github/51-agents/` y `.opencode/51-agents/` — los
agentes no se reconocen.

## 3. Root cause

`build_plan` aplica las reglas de ruta por componente con `apply_path` sin
contexto de la ruta completa: la regla PN51 (`^agents$` → `51-agents`)
coincide con el componente `agents` de `.github/agents/` y
`.opencode/agents/`. La intención de la ADR (no numerar la raíz de
plataforma) no se tradujo al motor: faltaba excluir las rutas bajo carpetas
ocultas (primer componente con `.`).

## 4. Impact

- **Users affected:** todos los adoptantes del kit.
- **Data impact:** inconsistencia estructural del kit (nombres de carpetas de
  plataforma incorrectos).
- **Workaround available:** renombrar manualmente `.github/51-agents` →
  `.github/agents` (y `.opencode`) tras cada corrida — frágil.

## 5. Classification and routing

| Aspect | Value |
|--------|-------|
| **Nature** | functional → Functional Analyst aprueba |
| **Violated expectation** | ADR-003/ADR-002: las carpetas de plataforma de la raíz no se numeran |
| **Dedicated TASK parent** | US-001 (feature — afecta el kit de salida) |

## 6. Fix status (strict TDD, ONE V-Bounce)

| Stage | Evidence | Status |
|-------|----------|--------|
| Reproduction test | RED: test que exige `.github/agents/` y `.opencode/agents/` en el kit transformado | Pending |
| Production fix | GREEN: `build_plan` excluye reglas PN* bajo carpetas ocultas (primer componente `.`); kit regenerado | Pending |
| MEM | MEM-YYMMDD-HHmm — red y green por separado | Pending |

> El fix es estrictamente TDD en el V-Bounce del TASK dedicado (TASK-006).

## 7. Relations

| Relation | Reference |
|----------|-----------|
| **Detected in** | informe del propietario 2026-08-27 (kit de producción) |
| **Incident** | — |
| **Affected US / TASK** | US-001 / TASK-004 (numeración — origen del defecto) |
| **Dedicated TASK** | US-001.TASK-006 (a crear tras aprobación) |
| **Canonical SPEC** | (a crear) |
| **ADRs** | ADR-003 (aceptada — declara que la raíz de plataforma no se numera) |
| **Risks** | — |

---

## 8. CP-BUG-Approval

> **MetaFlow §2.16, §3.0.** Este BUG permanece en draft hasta que un
> humano calificado registra `CP-BUG-Approval` (Functional Analyst para
> functional). La aprobación confirma el defecto, la evidencia, la naturaleza
> y el ruteo; no aprueba el TASK, la SPEC, la implementación, el MEM ni la
> aceptación — cada uno mantiene su propio checkpoint.

---

## 9. History

| Date | Change | Author |
|------|--------|--------|
| 2026-08-27 | Defect reported (draft) — informe del propietario | @eugenioserrano |
| 2026-08-27 | **CP-BUG-Approval** — aprobado; defecto confirmado por smoke test; TASK-006 asignado | @eugenioserrano |
