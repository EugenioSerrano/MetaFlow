---
id: "MEM-260823-1726"
title: "The Coordinator folder removed — the orchestrator identity lives in the four platform agents, evolved (US-023.BOLT-001, V-Bounce 3)"
date: "2026-08-23"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
bolt: "US-023.BOLT-001"
spec: "devflow/spec/SPEC-260823-1600-devflow-agent-contract-and-charters.md"
spec_revision: 1
v_bounce: 3
execution_outcome: "ready_for_review"
baseline: "45d553f"
applied_adrs:
  - "devflow/adrs/ADR-007-devflow-agent-identity-model.md"
  - "devflow/adrs/ADR-008-aitl-approval-precept.md"
  - "devflow/adrs/ADR-010-actor-grammar-and-pure-v5-vocabulary.md"
manifest: "devflow/metrics/bolts/US-023.BOLT-001-devflow-agent-contract-and-charters.json"
diff_ref: ""
review_ready_at: "2026-08-23T17:26:00-03:00"
review: # AITL-MEM-Approval — recorded by the human reviewer (§3.0); decision dictated in conversation ("apruebo!") and transcribed by the agent
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-23T17:27:00-03:00"
  decided_at: "2026-08-23T17:27:34-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved as Dev-validator: the coordinator folder removal + the doc alignments (README, INDEX, AC-1) inspected — the orchestrator identity lives in the four platform agents, evolved (ADR-007 §3.4), as directed; parity/byte-sync/G-count invariants hold. V-Bounce 3 approved — the final refinement of BOLT-001 (the Bolt remains Done)."
---

# MEM-260823-1726 — Coordinator folder removed (US-023.BOLT-001, V-Bounce 3)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | US-023.BOLT-001 (devflow-agent-contract-and-charters) |
| **SPEC**        | [SPEC-260823-1600](../spec/SPEC-260823-1600-devflow-agent-contract-and-charters.md) rev 1 |
| **V-Bounce**    | 3 (maintainer refinement after the batch approval — V-Bounce 2 MEM-1715 superseded) |
| **ADRs**        | ADR-007 (identity), ADR-008 (precept), ADR-010 (grammar) |

---

## 1. Executive summary

The maintainer rejected the "identity extract" abstraction: *"decir que es
el mismo no me gusta — prefiero evolucionar el agente DevFlow que tenemos
desde el inicio de los tiempos para que sepa cómo actuar en cada caso."*
So the `agents/coordinator/` folder (agent.yaml + charter.md) is
**removed** — the orchestrator identity is **not** a folder claiming to be
the platform agent; it is the **actual evolution of the four platform
agent files** (`CLAUDE.md`, `SKILL.md`, `AvengaDevFlow.agent.md`,
`AvengaDevFlow.md`), which already carry it (delivered in BOLT-003 VB2):
the shared body's **"The Coordinator (the orchestrator)"** paragraph
(routes, delegates production, spawns approvers, records — **never signs**,
`approves: []`) and the **per-platform spawn-topology lines** in each
preamble (Claude `Agent(...)` allowlist, OpenCode `permission.task`,
Copilot `agent` alias, Codex instruction-based) — the "how to act in each
case" the maintainer wants. The family docs were aligned: `agents/README.md`
now states "no separate coordinator folder — the Coordinator is the
DevFlow agent itself, evolved", `agents/INDEX.md` drops the coordinator
row and explains the same, and US-023 AC-1 was updated (the agents/
family contains the role templates + the contract + the INDEX; the
Coordinator is the four platform agents evolved — no folder, no generated
sub-agent). The generator's coordinator-skip guard stays (harmless
safety); the deployed wrapper set (20) is unchanged; parity still PASS.
The batch's approvals stand — this V-Bounce documents the final
refinement for the reviewer's confirmation.

## 2. Implemented phases

### Phase A — The folder removed

Deleted `distribution-kit/devflow/agents/coordinator/` (agent.yaml +
charter.md). The orchestrator identity's single home is now the four
platform agent files (the shared-body paragraph + the per-platform
preambles) — the genuine evolution of the DevFlow agent.

### Phase B — The family docs aligned

`agents/README.md`: the "What lives here" list loses the coordinator
entry; a new section "The Coordinator — the DevFlow agent itself,
evolved" states the four files as the home of the orchestrator identity
and the spawn topology. `agents/INDEX.md`: the coordinator row removed; a
"The Coordinator" section explains the same. US-023 AC-1 reworded
accordingly.

### Phase C — Verification

The agents/ tree contains only roles/ + the docs; the deployed wrappers
(20) and the four main files are unchanged from the approved state;
parity PASS.

## 3. Files created

| File | Purpose |
|------|---------|
| — | none (removal + doc alignment) |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `distribution-kit/devflow/agents/README.md` | Coordinator section rewritten — no separate folder; the four platform agents are the Coordinator, evolved |
| `distribution-kit/devflow/agents/INDEX.md` | Coordinator row removed; "The Coordinator" section added |
| `devflow/functional/user-stories/US-023-...md` | AC-1 reworded — the agents/ family = roles + contract + INDEX; the Coordinator = the four platform agents evolved |

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
| — | — | — |

## 6. Files deleted

| File | Reason |
|------|--------|
| `distribution-kit/devflow/agents/coordinator/agent.yaml` | The maintainer rejected the identity-extract abstraction — the orchestrator identity lives in the four platform agents, evolved (no abstract folder) |
| `distribution-kit/devflow/agents/coordinator/charter.md` | Same |

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| The coordinator folder is removed, not kept as an identity extract | The maintainer's direction: evolve the real agent, no abstract "same agent" folder |
| The four platform files are the Coordinator's only home | They already carry the orchestrator paragraph + the per-platform spawn topology (BOLT-003 VB2) — the evolution the maintainer wants ("sepa cómo actuar en cada caso") |
| The generator's coordinator-skip guard stays | Harmless safety for any project-defined coordinator-role entry; the kit generates only role agents |
| AC-1 reworded (light) | The agents/ family contents changed (no coordinator folder); the Coordinator is described as the evolved platform agent |

## 8. Deviations and assumptions

No deviations from SPEC-260823-1600 rev 1 beyond the already-sanctioned
refinements. Assumption: the roster (US-024) references the Coordinator
as an inline actor (no `definition` file) — noted for the US-024 SPECs.

## 9. Verification evidence

### Presence

```
agents/ tree: roles/ + README + INDEX + VERIFICATION (no coordinator/)
agents/README.md: "The Coordinator — the DevFlow agent itself, evolved" PRESENT
agents/INDEX.md: coordinator row REMOVED; "The Coordinator" section PRESENT
US-023 AC-1: reworded (no coordinator folder) PRESENT
Four main files: "The Coordinator (the orchestrator)" ×4 + spawn-topology
lines ×4 (unchanged from the approved state)          PRESENT
```

### Invariants

```
Deployed wrappers: 20 (unchanged); parity PASS
Four-agent byte-sync: 2 diff lines (unchanged)
G-count: 39×5 (unchanged)
Kit-only: only distribution-kit/ + the US-023 doc changed
```

### Gates

Documentation Bolt: runtime gates `n/a`; prompt-injection/secret-leak
`pass`; hallucination-lint `pass`; behavioral-reproducibility `pass`;
bolt-manifest-validation `pass` (v_bounces[3] appended, JSON valid).

## 10. Manual interventions

None — the agent produced everything.

## 11. Evidence links

- **Diff / PR:** none (working tree, uncommitted)
- **Commit:** baseline `45d553f`
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-023.BOLT-001-devflow-agent-contract-and-charters.json`

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~8min |
| V-Bounce number | 3 |
| Tests created | 0 (documentation refinement; the tool suite unchanged — 14 pass) |
| AI-generated code | 100% |
| First-pass approval | pending (this MEM) |

## 13. Pending items and stubs

- [ ] The roster (US-024) lists the Coordinator as an inline actor (no
      definition file) — noted for its SPECs
- [ ] Batch approval of this MEM (the earlier approvals stand; this V-Bounce
      documents the final refinement)

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
| **review_ready_at** | `2026-08-23T17:26:00-03:00` |
| **review.started_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **review.decided_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **Review evidence** | diff of the removal + the doc alignments; parity/byte-sync/G-count invariants; MEM, manifest |
| **Comments** | |
| **Findings** | |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | evidence inspected per the review-evidence column |
