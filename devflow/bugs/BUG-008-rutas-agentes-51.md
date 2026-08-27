---
id: "BUG-008"
title: "Rutas documentadas *51-agents* no coinciden con los wrappers reales (.agents/, .github/agents/, .opencode/agents/)"
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
  - "distribution-kit/AGENTS.md:11-12; metaflow/README.md:81; metaflow/51-agents/VERIFICATION.md:68-69,83,96,117,144; metaflow/51-agents/INDEX.md:10-11,41-42; metaflow/51-agents/README.md:29; metaflow/51-agents/squad/README.md:14-15; metaflow/ai-sdlc/MetaFlow.md:4172-4173,4253,4734-4735,4862; CLAUDE.md:41,596-597; SKILL.md:46,613-614; MetaFlow.agent.md:11,73,644-645; .opencode/agents/MetaFlow.md:57,624-625 (síntoma en el output)"
expected_result: "La documentación (AGENTS.md, README, VERIFICATION.md, §5.2/§5.16, preámbulos de spawn topology) debe describir la ubicación real que cada herramienta lee — los wrappers del kit viven en `.agents/skills/ai-sdlc/`, `.github/agents/`, `.opencode/agents/` (renombrados en BOLT-002/REV-002 F-01) — verificada a implementation time"
actual_result: "Los textos documentan `.51-agents/skills/`, `.github/51-agents/`, `.opencode/51-agents/`, `.claude/51-agents/`, `.codex/51-agents/` como ubicación de los agent definitions y spawn folders — rutas que no existen en el kit; un Coordinator de proyecto adoptante buscará/instalará wrappers donde la herramienta no los lee"
bolt: "US-001.BOLT-013-fix-rutas-agentes"
spec: "SPEC-260827-0355-bolt013-fix-rutas-agentes.md"
mem: "MEM-260827-0408-fix-rutas-agentes.md"
sources: ["REV-003 (F-08, F-09)"]
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
  acknowledgment_reason: "Aprobación del propietario (Functional Analyst autoasignado) sin hallazgos — BUG-002..BUG-012 aprobados en bloque desde REV-003 (AITL-REV-Approval 2026-08-27). Ruteo: BOLT-013 bajo US-001 (verificar convención por plataforma en el fix)"
tags: [bug, kit, agentes, rutas, spawn-topology]
---

# BUG-008 — Rutas *51-agents* documentadas vs wrappers reales

| Field              | Value |
|--------------------|-------|
| **Severity**       | high |
| **Nature**         | functional |
| **Detected in**    | review (REV-003 F-08/F-09) |
| **Status**         | approved |
| **Affected files** | output: ~17 ubicaciones en 9+ archivos (ver frontmatter) · root cause: `src/transform.py` + `mapping.json` |
| **Dedicated Bolt** | US-001.BOLT-013 (functional) |

## 1. Summary

La documentación del kit describe la instalación de agentes en carpetas
`*51-agents*` (`.claude/51-agents/`, `.opencode/51-agents/`,
`.github/51-agents/`, `.codex/51-agents/`, `.51-agents/skills/`) que **no
existen**: los wrappers reales están en `.agents/skills/ai-sdlc/`,
`.github/agents/` y `.opencode/agents/` (renombrados en BOLT-002/REV-002
F-01). Incluye el NOTE de VS2026 (MetaFlow.agent.md:11) y los preámbulos
de spawn topology de los 4 agent definitions — el Coordinator buscará sus
wrappers en el lugar equivocado y los agentes no se registran.

## 2. Reproduction

1. Regenerar el kit: `python src/transform.py`.
2. Verificar en el output:

**Expected result:** cero referencias a `.51-agents/`, `.github/51-agents/`,
`.opencode/51-agents/`, `.claude/51-agents/`, `.codex/51-agents/` en el kit
(las únicas ocurrencias válidas son `metaflow/51-agents/…` — la carpeta
canónica de definiciones).

**Actual result:** ~17 ubicaciones en 9+ archivos (ver frontmatter).

## 3. Root cause

El rename de los wrappers (BOLT-002) movió los archivos a las carpetas
nativas de cada plataforma (`.agents/`, `.github/agents/`,
`.opencode/agents/`), pero el diccionario del transform no actualizó las
referencias en prosa (AGENTS.md, VERIFICATION.md, §5.2/§5.16, preámbulos)
que seguían describiendo la convención `*51-agents*` del input-kit
Avenga. Puede existir ambigüedad real sobre la convención target por
plataforma → verificar a implementation time (DISC o decisión ADR si
aplica, VERIFICATION.md es el documento de re-verificación).

## 4. Impact

- **Users affected:** todos los adoptantes (instalación de agentes).
- **Data impact:** agentes que no se registran → el spawn topology y el sistema de roles se rompen silenciosamente.
- **Workaround available:** no.

## 5. Classification and routing

| Aspect | Value |
|--------|-------|
| **Nature** | functional → Functional Analyst aprueba |
| **Violated expectation** | La documentación debe reflejar la instalación real de los wrappers (REV-002 F-01: wrappers en `.agents/`, `.github/agents/`, `.opencode/agents/`) |
| **Dedicated Bolt parent** | US-001 (feature — afecta el kit de salida) |

## 6. Fix status (strict TDD, ONE V-Bounce)

| Stage | Evidence | Status |
|-------|----------|--------|
| Reproduction test | RED: test del toolkit que exige cero `*51-agents*` como ruta de plataforma (fuera de `metaflow/51-agents/`) | Pending |
| Production fix | GREEN: diccionario unifica las rutas documentadas con las reales (verificando la convención por plataforma); kit regenerado | Pending |
| MEM | MEM-YYMMDD-HHmm — red y green por separado | Pending |

> Fix TDD en el V-Bounce del Bolt dedicado (BOLT-013). **No se edita el kit a mano.**
> Si la verificación por plataforma revela ambigüedad de target, resolver
> con DISC y/o ADR antes de cerrar el fix.

## 7. Relations

| Relation | Reference |
|----------|-----------|
| **Detected in** | REV-003 (F-08, F-09) — AITL-REV-Approval 2026-08-27 |
| **Incident** | — |
| **Affected US / Bolt** | US-001 / BOLT-002 (rename de wrappers — origen) |
| **Dedicated Bolt** | US-001.BOLT-013 |
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
| 2026-08-27 | Defect reported (draft) — REV-003 F-08/F-09 | @eugenioserrano |
| 2026-08-27 | **AITL-BUG-Approval** — aprobado (bloque con BUG-002..BUG-012); BOLT-013 asignado | @eugenioserrano |
| 2026-08-27 | **Fix entregado** — MEM-260827-0408-fix-rutas-agentes.md (AITL-MEM-Approval 2026-08-27); BUG fixed
