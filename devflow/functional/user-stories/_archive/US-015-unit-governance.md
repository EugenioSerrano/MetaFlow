---
id: "US-015"
title: "Unit governance — operationalize the units/ family, HITL-UNIT-Approval and UAT minutes"
date: "2026-08-21"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved" # draft | approved | deprecated
owner: "eugenio.serrano" # Functional Analyst (governs this US)
unit: ""
story_points: 8 # confirmed at HITL-US-Approval (raised from 5 — part (b) operationalization is large with real unknowns) (§2.6)
adrs: []
sources:
  - "devflow/avenga-devflow/Avenga-DevFlow.md"
  - "maintainer product direction (2026-08-21)"
  - "devflow/adversarial-reviews/AREV-001-role-availability-blockers-sweep/03-VERDICT.md"
  - "devflow/adversarial-reviews/AREV-002-single-operator-sweep/03-VERDICT.md"
  - "maintainer direction (2026-08-22): remove UNIT/UAT from the kit flow now; tests/uat/ folder stays dormant; reintroduce here later"
stakeholders: []
tags: ["units", "uat", "governance", "kit-family", "environments"]
review_ready_at: "2026-08-22T13:32:33-03:00"
review: # HITL-US-Approval (rev 2 — rescope) — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "functional_analyst"}]
  started_at: "2026-08-22T13:32:33-03:00"
  decided_at: "2026-08-22T13:32:33-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Re-approved after a material scope change (US split, 2026-08-22): US-015 is rescoped to part (a) — the interim removal of the reserved UNIT/UAT machinery from the kit flow (delivered by US-015.BOLT-001, Done, closes v4.2). Part (b) — the full operationalization of the units/ family, per-environment HITL-UNIT-Approval flow and UAT sequence — is transferred to the new US-019 (draft, backlog v5.0). With part (a) delivered and no remaining open scope, US-015 is closed. Original approval (2026-08-22, two-horizon scope, 8 SP) recorded in the revision history and the manifest hitl_approvals[]."
---

# US-015 — Unit governance: operationalize the units/ family, HITL-UNIT-Approval and UAT minutes

| Field          | Value |
|----------------|-------|
| **Unit**       | — |
| **ADRs**       | — |
| **Status**     | approved (HITL-US-Approval 2026-08-22; **rev 2 rescoped 2026-08-22** — see revision history) |
| **Story points** | 8 (confirmed — original two-horizon scope; see revision history) |

> **Revision (2026-08-22, US split):** US-015 is **rescoped to part (a)** —
> the interim removal of the reserved UNIT/UAT machinery from the kit flow,
> delivered by US-015.BOLT-001 (Done, closes v4.2). Part (b), the full
> operationalization of the `units/` family, per-environment
> `HITL-UNIT-Approval` flow and UAT sequence, was **transferred to
> [US-019](US-019-operationalize-units-family.md)** (draft, backlog v5.0).
> With part (a) delivered, **US-015 is closed**. The body below documents the
> original two-horizon analysis; part-(b) detail now lives in US-019.

**As a** project manager, **I want** the Unit-level governance that the
methodology reserves today to be fully operational — a `units/` family, the
per-environment `HITL-UNIT-Approval` flow and the UAT sign-off sequence —
**so that** a group of Bolts can be validated, accepted and promoted as one
cohesive deliverable, with each environment's approval recorded and
traceable.

---

## 1. The problem (explained, complete)

### What exists today

The methodology already names the **concepts** but not the **mechanics**:

- **§2.11 — Deployment Unit:** *"An artifact ready to be promoted (image /
  function / IaC) that has already passed every gate and is demonstrable.
  The 'releasable' output of one or more Bolt sequences within a Unit."*
  The DORA deployment definition builds on it: *"a production deployment is
  the promotion of a Deployment Unit to the production environment, made
  traceable by a release tag, image digest or equivalent identifier that
  links the deployment event to its included Bolts and commits."*
- **§3.0 HITL table:** `HITL-UNIT-Approval` exists ("Unit approval — Tech
  Lead") and `HITL-UAT-Approval` exists ("UAT sign-off — Stakeholders").
- **§3.11 sequence (intended rule):** *"per named environment; staging UNIT
  precedes UAT; UAT precedes production UNIT"* — and *"requires
  `HITL-UNIT-Approval` for staging first; its approval is a precondition for
  `HITL-UNIT-Approval` for production."*
- **§3.7.3 coverage note:** Unit-level checkpoints are NOT part of per-Bolt
  coverage — they apply to the Deployment Unit **as a group**.
- **kit folder:** `tests/uat/` exists with `TEMPLATE-UAT.md` (UAT minutes,
  `UAT-NNN`, `HITL-UAT-Approval`).

### What is missing (the gap)

1. **No `units/` folder.** The methodology's own §3.11 says Unit governance
   is *"Reserved — full governance will be defined when the `units/` folder
   is introduced."* The folder does not exist in the kit, so there is no
   canonical place for a Unit record: which Bolts compose it, which
   environment it targets, which approvals it carries.
2. **No Unit record template.** Nothing defines a `UNIT-NNN` document: its
   frontmatter (status, environment, composed Bolts with their manifests,
   deployment evidence, gates), its lifecycle (draft → in-validation →
   approved per environment), or its INDEX.
3. **No operational sequence.** The "staging UNIT → UAT → production UNIT"
   chain exists as an *intended rule* in one paragraph but has no step-by-step
   contract: what evidence each step requires, what blocks what, what happens
   when UAT produces an Adjustment List (the methodology mentions "Approved
   UAT minutes or Adjustment List (New Bolts)"), and how promotion is
   recorded against the DORA deployment definition.
4. **No §5.15 routing.** The migration routing table has no row for Unit
   records — so a future release migration would not know where to place or
   carry them.
5. **No relationship definitions.** How Bolts group into a Unit (by sprint?
   by milestone? by environment target?), how the Unit's gate evidence is
   aggregated from member Bolts, and how the per-Bolt 100% coverage
   interacts with the Unit-level approvals.

### Why it matters

Without Unit governance, teams can only approve **Bolts individually**. A
release is more than the sum of its Bolts: it needs a package-level sign-off
(customer UAT, environment promotion) with evidence linking the deployment
event to its included Bolts — exactly what the DORA metrics (D1–D5) and
production promotion require. This US turns the reserved placeholder into
the operational mechanism.

### Interim decision (maintainer, 2026-08-22) — remove now, reintroduce here

AREV-001 (F-06, UNIT/UAT part) and AREV-002 (F-03) confirmed that the
reserved `HITL-UNIT-Approval` / `HITL-UAT-Approval` machinery is a live
contradiction: the §3.0 table, the four agents and the UAT README state a
"staging UNIT → UAT → production UNIT" precondition around a checkpoint the
same table declares non-operational, while `tests/uat/TEMPLATE-UAT.md`
carries none — four texts disagreeing on a gate that today is only latent
(suspended by GUARDRAILS G20 and the UAT README).

Rather than patch the contradiction in place, the maintainer decided to
**pull the reserved machinery out of the kit's active flow now**, and
operationalize it properly through this US later:

- **Now (interim):** an implementing kit Bolt removes every trace of
  `HITL-UNIT-Approval` and `HITL-UAT-Approval` from the **active governance
  flow** — the §3.0 checkpoint table, §3.11 sequence, the §3.15 status row
  (UAT), the `GUARDRAILS.md` checkpoint map / G20 / acceptance references,
  the four agent definitions, and the coverage tables — so no reader hits a
  gate that points at undefined governance. The `tests/uat/` **folder stays
  physically in place, dormant**, as the placeholder for the future work; its
  files are marked dormant (pointing at this US) rather than deleted.
- **Later (this US):** UNIT/UAT are reintroduced with full `units/` governance
  as specified in §2 below — the proper operational mechanism, not a
  placeholder.

This is consistent with US-014's single-operator operability policy: while
reserved, these checkpoints must not sit as blockers on anyone's path.

---

## 2. Acceptance criteria

- **Given** the kit, **When** a team wants to package a release, **Then** it
  has a canonical `units/` family with a Unit record template, README and
  INDEX (`UNIT-NNN-<description>.md`, sequential numbering).
- **Given** a Unit record, **When** it is created, **Then** it declares its
  environment target, the composed Bolts (with manifest refs), the gate
  evidence and its lifecycle status.
- **Given** the environment sequence, **When** a Unit moves through staging,
  **Then** the methodology prescribes the step-by-step contract: staging
  `HITL-UNIT-Approval` (Tech Lead) → UAT minutes (`HITL-UAT-Approval`,
  stakeholders) → production `HITL-UNIT-Approval`, each with its evidence
  and its blocking relationships.
- **Given** UAT feedback, **When** stakeholders reject or adjust, **Then**
  the minutes record the Adjustment List and the methodology routes it to
  New Bolts without rewriting the Unit's history.
- **Given** a production promotion, **When** it is recorded, **Then** it
  links the deployment event to the Unit's included Bolts and commits
  (DORA deployment definition, §2.11).
- **Given** a methodology upgrade, **When** the project migrates, **Then**
  the `units/` family travels with the migration (§5.15 routing covers it).
- **Given** the checkpoint map, **When** Unit approvals are recorded,
  **Then** they follow the same review contract as other checkpoints
  (named approver, timestamps, evidence) and are NOT written to any Bolt
  manifest (Unit-level, §3.7.3).
- **Given** the reserved UNIT/UAT machinery today (interim decision, §1),
  **When** the interim kit Bolt runs, **Then** `HITL-UNIT-Approval` and
  `HITL-UAT-Approval` are removed from the active flow across the checkpoint
  map, §3.11, §3.15, GUARDRAILS, the four agents and the coverage tables,
  the `tests/uat/` folder stays dormant in place (not deleted), and no
  reader is blocked by a gate pointing at undefined governance. (Routes here:
  AREV-001 F-06 UNIT/UAT part, AREV-002 F-03.)

## 3. Notes / to refine before approval

- **Origin:** the methodology itself reserves this governance (§3.11);
  `HITL-UNIT-Approval` and `HITL-UAT-Approval` exist in the §3.0 table with
  no operating mechanism; `tests/uat/TEMPLATE-UAT.md` already ships.
- **Related backlog:** US-002 (sprints) defines the planning layer — Units
  may group Bolts per sprint or per milestone; the relationship is a design
  decision for this US's refinement.
- **Open design points:**
  - Naming/location: `devflow/units/UNIT-NNN-<description>.md` (proposed)
    vs. extending `tests/uat/`.
  - Whether Unit records carry manifests (proposal: no — derived from
    member Bolts; Unit state is derived like Bolt state).
  - How the Adjustment List from UAT becomes New Bolts (existing lifecycle
    or a new shortcut).
  - Whether `HITL-UNIT-Approval` per named environment needs a dedicated
    frontmatter block or one block with per-environment rows.
  - Aggregation of gate evidence from member Bolts (automatic vs. manual
    declaration).
- **Scope note:** this US is about the Unit *governance mechanics* (records,
  sequence, routing); the deployment tooling itself (CI promotion) belongs
  to the infra/tooling Bolts, not here.

---

## 4. Revision history (US split, 2026-08-22)

| Rev | Date | Change | Author |
|-----|------|--------|--------|
| 1 | 2026-08-22 | Original approval — two-horizon scope: (a) interim UNIT/UAT removal now (closes v4.2), (b) full operationalization later. story_points confirmed 8. BOLT-001 = part (a). (HITL-US-Approval 2026-08-22T02:06:40-03:00) | @eugenio.serrano |
| 2 | 2026-08-22 | **Material scope change (US split):** US-015 rescoped to part (a) only — the interim removal, delivered by US-015.BOLT-001 (Done). Part (b) (operationalize `units/`, per-environment `HITL-UNIT-Approval`, UAT sequence) transferred to **US-019** (draft, backlog v5.0). Re-approved (HITL-US-Approval rev 2, 2026-08-22T13:32:33-03:00). **US-015 closed.** | @eugenio.serrano |
