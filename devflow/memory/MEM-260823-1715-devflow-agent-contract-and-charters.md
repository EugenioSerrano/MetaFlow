---
id: "MEM-260823-1715"
title: "Model Y + TEMPLATE-new-role — the Coordinator pinned as the platform agent itself, and the generic template for project-defined roles (US-023.BOLT-001, V-Bounce 2)"
date: "2026-08-23"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
bolt: "US-023.BOLT-001"
spec: "devflow/spec/SPEC-260823-1600-devflow-agent-contract-and-charters.md"
spec_revision: 1
v_bounce: 2
execution_outcome: "ready_for_review"
baseline: "45d553f"
applied_adrs:
  - "devflow/adrs/ADR-007-devflow-agent-identity-model.md"
  - "devflow/adrs/ADR-008-aitl-approval-precept.md"
  - "devflow/adrs/ADR-010-actor-grammar-and-pure-v5-vocabulary.md"
manifest: "devflow/metrics/bolts/US-023.BOLT-001-devflow-agent-contract-and-charters.json"
diff_ref: ""
review_ready_at: "2026-08-23T17:15:00-03:00"
review: # AITL-MEM-Approval — recorded by the human reviewer (§3.0); decision dictated in conversation ("apruebo todos los mems, los bolts y la US23 de una") and transcribed by the agent
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-23T17:20:00-03:00"
  decided_at: "2026-08-23T17:21:43-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved as Dev-validator: the Model-Y refinement (the Coordinator pinned as the platform agent itself, ADR-007 §3.4), the TEMPLATE-new-role, the agents/INDEX.md and the governance-limit note inspected against the repo — correct and complete. V-Bounce 2 approved — BOLT-001 Development Completed."
---

# MEM-260823-1715 — Model Y + TEMPLATE-new-role (US-023.BOLT-001, V-Bounce 2)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | US-023.BOLT-001 (devflow-agent-contract-and-charters) |
| **SPEC**        | [SPEC-260823-1600](../spec/SPEC-260823-1600-devflow-agent-contract-and-charters.md) rev 1 |
| **V-Bounce**    | 2 (review-driven refinement — V-Bounce 1 MEM-1612 superseded) |
| **ADRs**        | ADR-007 (identity), ADR-008 (precept), ADR-010 (grammar) |

---

## 1. Executive summary

This V-Bounce refines BOLT-001's deliverable per the maintainer's
philosophical review (the Coordinator question) and Opus's scope: **(a)
Model Y pinned** — the `agents/coordinator/` files now state explicitly
that the Coordinator is **the Avenga DevFlow platform agent itself**
(ADR-007 §3.4: "the evolution of today's platform agent"), NOT a separate
sub-agent: its projections are the four platform files (CLAUDE.md, SKILL.md,
AvengaDevFlow.agent.md, AvengaDevFlow.md), which carry the full methodology
body; `coordinator/agent.yaml` is the structured identity extract
(`approves: []`, `modes`, `capabilities` — machine-readable authority,
ADR-007). The `agents/README.md` and the coordinator charter now document
the same. **(b) `roles/TEMPLATE-new-role/` added** — the generic
"create your own agent" template (a fully-commented `agent.yaml` with all
fields + the non-negotiable bounds: structured authority, real checkpoint
codes in `approves`, the approver ceiling T0/T1 + MCP allowlist,
independence; and a `prompt.md` charter skeleton), plus the
"Create your own agent" guide in `roles/README.md` (copy → fill → generate
→ roster + AITL-enable ADR) — so each team configures its own agents as it wants, within the governed
bounds (the open role archetype, ADR-007 §3.3, US-022). The create-flow
note in `roles/README.md` now **states the governance limit explicitly**:
creating/updating an **executor** agent (or adding a member) is **living
data** (no approval — the US-024 roster rule), while creating/changing an
**approver** (its charter or authority fields) is a **governed act** that
**re-triggers the project's AITL-enable ADR** (ADR-008 safe-default — no
AI-signed approval without explicit human configuration; AvengaDevFlow may
draft/propose, a human signs the enabling). **(c) `agents/INDEX.md`
added** — the family index listing the definitions (the coordinator
identity extract, the five role templates, the `TEMPLATE-new-role/`
template, with the notes: templates-are-skeletons, project-defined agents
listed in the adopter's own copy, the Coordinator-is-not-generated MODEL
Y rule, and the VERIFICATION.md pointer) — closing the symmetry with
`actors/`. A light note was added to US-023 AC-1 ("+ a generic
`TEMPLATE-new-role/` for project-defined roles" + "an `agents/INDEX.md`
listing the definitions"). The wrapper generator picks up any `agent.yaml`
in the tree automatically, so a team's custom role is wrapped +
parity-checked with zero extra work. No other changes; the templates'
content is untouched apart from the Model-Y notes.

## 2. Implemented phases

### Phase A — Model Y pinned

Updated `coordinator/agent.yaml` (the MODEL Y comment block: this file is
the structured identity extract of the platform agent; its projections are
the four platform files, NOT generated sub-agent wrappers — the generator
produces only the ROLE agents), `coordinator/charter.md` ("Who I am (Model
Y)": I am the Avenga DevFlow agent itself; nobody spawns me; the human
invokes me as the main session agent), and `agents/README.md` (the
coordinator entry: identity extract + projections = the four platform
files; no separate coordinator sub-agent).

### Phase B — The generic template + the governance limit + the family INDEX

Created `agents/roles/TEMPLATE-new-role/agent.yaml` (every field with
guidance comments + the NON-NEGOTIABLE BOUNDS block) and `prompt.md` (the
charter skeleton: who I am / WHAT I PRODUCE / what I check / how I decide /
when I escalate / what I may never do). Added the "Create your own agent
(project-defined roles)" section to `roles/README.md` with the
**governance-limit table** (executor = living data, no approval; approver
= governed act, re-triggers the AITL-enable ADR — human-signed) and the 6
steps (copy → fill → write the charter → run the generator → list in the
INDEX → roster + AITL-enable ADR for approvers). Created
`agents/INDEX.md` (the family index: coordinator + the five role templates
+ TEMPLATE-new-role + the notes). Added the light AC-1 notes to the
approved US-023 (+ TEMPLATE-new-role, + agents/INDEX.md).

## 3. Files created

| File | Purpose |
|------|---------|
| `distribution-kit/devflow/agents/roles/TEMPLATE-new-role/agent.yaml` | The generic "create your own agent" definition — all fields with guidance + the non-negotiable bounds (structured authority, approver ceiling, MCP allowlist, independence) |
| `distribution-kit/devflow/agents/roles/TEMPLATE-new-role/prompt.md` | The charter skeleton for any project-defined role |
| `distribution-kit/devflow/agents/INDEX.md` | The family index — coordinator + role templates + TEMPLATE-new-role + the notes (templates-are-skeletons, MODEL Y, adopter copies grow with their team) |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `distribution-kit/devflow/agents/coordinator/agent.yaml` | MODEL Y comment block — the Coordinator is the platform agent itself; this file is its structured identity extract (no generated sub-agent wrapper) |
| `distribution-kit/devflow/agents/coordinator/charter.md` | "Who I am (Model Y)" section — I am the Avenga DevFlow agent itself; nobody spawns me |
| `distribution-kit/devflow/agents/README.md` | Coordinator entry updated to the identity-extract framing + the TEMPLATE mention |
| `distribution-kit/devflow/agents/roles/README.md` | "Create your own agent" guide — with the governance-limit table (executor = living data; approver = AITL-enable ADR re-trigger) |
| `devflow/functional/user-stories/US-023-...md` | Light AC-1 notes: "+ a generic `TEMPLATE-new-role/` for project-defined roles" + "an `agents/INDEX.md` listing the definitions" |

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
| — | — | — |

## 6. Files deleted

| File | Reason |
|------|--------|
| — | — |

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| Model Y pinned (the Coordinator = the platform agent) | ADR-007 §3.4 already decides it ("the evolution of today's platform agent"); the V-Bounce 1 framing left a redundant coordinator definition — the review caught it |
| The coordinator's projections are the four platform files, not generated wrappers | The four files are the full agent (methodology body + platform preamble); a small identity file cannot generate them — the relationship is 4 files ⊃ identity extract |
| The TEMPLATE-new-role is a kit product skeleton | Teams configure their agents freely within the governed bounds; the generator wraps any custom role automatically |
| The bounds are non-negotiable (structured authority, ceiling, allowlist, independence) | The injection-forged-approval defense and ADR-007 authority model — the rest is team freedom |

## 8. Deviations and assumptions

No deviations from SPEC-260823-1600 rev 1 (this V-Bounce refines the
deliverable in place; the AC-1 note is a light clarification sanctioned in
the review). Assumption: the coordinator Model-Y + the template land with
the pending batch approvals.

## 9. Verification evidence

### Presence

```
coordinator/agent.yaml: MODEL Y block PRESENT
coordinator/charter.md: "Who I am (Model Y)" PRESENT
agents/README.md: identity-extract framing PRESENT
roles/TEMPLATE-new-role/{agent.yaml,prompt.md}: PRESENT
roles/README.md: "Create your own agent" guide + governance-limit table PRESENT
agents/INDEX.md: PRESENT (coordinator + 5 templates + TEMPLATE + notes)
US-023 AC-1: TEMPLATE-new-role + agents/INDEX.md notes PRESENT
```

### Invariants

```
Kit-only (ADR-004): only distribution-kit/ + the US-023 doc (governance
record) changed — no root devflow/ methodology content    PASS
Encoding: files written without BOM                        PASS
```

### Gates

Documentation Bolt: runtime gates `n/a`; prompt-injection/secret-leak
`pass`; hallucination-lint `pass` (ADR refs resolve);
behavioral-reproducibility `pass`; bolt-manifest-validation `pass`
(v_bounces[2] appended, JSON valid).

## 10. Manual interventions

None — the agent produced everything.

## 11. Evidence links

- **Diff / PR:** none (working tree, uncommitted)
- **Commit:** baseline `45d553f`
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-023.BOLT-001-devflow-agent-contract-and-charters.json`

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~10min |
| V-Bounce number | 2 |
| Tests created | 0 (documentation refinement; the generator tests land in BOLT-002) |
| AI-generated code | 100% |
| First-pass approval | pending (this MEM) |

## 13. Pending items and stubs

- [ ] The generator/deployment sides of the Model-Y fix (BOLT-002/003
      V-Bounces 2) — the coordinator wrappers removal + the orchestrator
      touch on the four main files
- [ ] Batch approvals (all pending MEMs) + AITL-BOLT-DONE ×4

## 14. AITL-MEM-Approval

> **Avenga DevFlow §2.12, §3.0.** This MEM is created by the agent with no
> mutable status and is **never self-approved**. A qualified human (the
> Dev-validator who executed the Bolt) inspects the actual diff,
> test/gate evidence, MEM and manifest, and records `AITL-MEM-Approval`
> here and in the manifest's `checkpoint_approvals[]`.

| Field | Value |
|-------|-------|
| **Reviewers (executing Dev-validator)** | `human:eugenio.serrano` |
| **Roles** | dev_validator |
| **Decision** | approved / changes_requested / rejected |
| **review_ready_at** | `2026-08-23T17:15:00-03:00` |
| **review.started_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **review.decided_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **Review evidence** | diff of the coordinator files + READMEs + the template; presence checks; kit-only; MEM, manifest |
| **Comments** | |
| **Findings** | |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | evidence inspected per the review-evidence column |
