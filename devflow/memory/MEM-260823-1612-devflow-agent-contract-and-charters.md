---
id: "MEM-260823-1612"
title: "DevFlow Agent contract and producer-first charters — the devflow/agents/ family delivered (US-023.BOLT-001)"
date: "2026-08-23"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
bolt: "US-023.BOLT-001"
spec: "devflow/spec/SPEC-260823-1600-devflow-agent-contract-and-charters.md"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "45d553f"
applied_adrs:
  - "devflow/adrs/ADR-007-devflow-agent-identity-model.md"
  - "devflow/adrs/ADR-008-aitl-approval-precept.md"
  - "devflow/adrs/ADR-010-actor-grammar-and-pure-v5-vocabulary.md"
manifest: "devflow/metrics/bolts/US-023.BOLT-001-devflow-agent-contract-and-charters.json"
diff_ref: ""
review_ready_at: "2026-08-23T16:12:00-03:00"
review: # AITL-MEM-Approval — filled by the human reviewer (§3.0)
  decision: "" # approved | changes_requested | rejected
  reviewers: [] # [{actor, role, model}]
  started_at: "" # ISO 8601 with seconds + offset
  decided_at: "" # ISO 8601 with seconds + offset
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: ""
---

# MEM-260823-1612 — The `devflow/agents/` family (US-023.BOLT-001, V-Bounce 1)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | US-023.BOLT-001 (devflow-agent-contract-and-charters) |
| **SPEC**        | [SPEC-260823-1600](../spec/SPEC-260823-1600-devflow-agent-contract-and-charters.md) rev 1 |
| **V-Bounce**    | 1 |
| **ADRs**        | ADR-007 (identity), ADR-008 (precept + separation of duties + approver ceiling), ADR-010 (grammar) |

---

## 1. Executive summary

This V-Bounce delivered the kit's `devflow/agents/` family — where "DevFlow
Agents are true actors" becomes operative. The family contains the
**canonical definition contract** reference (`roles/README.md` — every
`agent.yaml` field with `executor` as the first-class default and the
security rules), the shipped **Coordinator** (`coordinator/agent.yaml` +
`charter.md` — routes, delegates production, spawns, records, and **never
signs**: `approves: []`), and the **five producer-first charter
templates** (functional-analyst, architect, developer, qa, reviewer —
each with a structured `agent.yaml` and a charter body `prompt.md` that
opens with **WHAT I PRODUCE**, enumerating the role's outputs: FA → US,
architect → ADR, developer → SPEC + code + tests, QA → TC/tests + MEM
reviews, reviewer → REV + MEM/DISC approvals). The **security rules are
encoded** in every template: the approver capability ceiling (T0/T1, no
write paths, no transactional MCPs — the injection-forged-approval
defense, US-023 AC-7) and the `mcp_servers: []` named-allowlist default
(AC-8). The family README disambiguates `agents/` vs `actors/` and states
the templates-are-copied rule. Verification is GREEN: 14 files present,
WHAT I PRODUCE in all five charters, ceiling + MCP default in all five
agent.yaml files, Coordinator `approves: []`, kit-only (only the new
folder in distribution-kit), no BOM. The deliverable is the single source
the generator (BOLT-002), the deployment (BOLT-003), the smoke (BOLT-004)
and the roster (US-024, role → artifacts mapping) will consume.

## 2. Implemented phases

### Phase A — The contract reference and the Coordinator

Created `agents/roles/README.md` (the canonical contract: the field table,
the security rules AC-7/AC-8, the producer-first rule, the
templates-are-copied rule — the single source the roster's `produces`
derivation cites) and `agents/coordinator/` — `agent.yaml` (id
`coordinator`, `modes: [executor]`, **`approves: []`** — the ADR-008
separation of duties encoded in the field, not just the prose) +
`charter.md` (who I am, what I orchestrate, what I never do — including
"if I ever seem to approve, that is a defect").

### Phase B — The five producer-first charter templates

For each role: `agent.yaml` (structured fields per the contract — id
placeholder with the identity note, role, description, model placeholder,
`modes` with executor first-class, `approves` per role policy, tier,
tools, `mcp_servers: []`, escalation, write_paths — plus the APPROVER
CEILING comment) and `prompt.md` (who I am, **WHAT I PRODUCE** with the
role's outputs enumerated, what I check, how I decide, when I escalate,
what I may never do — each charter ends with the independence rule for its
own approvals). The family `agents/README.md` explains the two sides of an
agent (executor first-class / approver configured) and the folder
disambiguation vs `actors/`.

### Phase C — Verification (GREEN)

Ran: tree (14 files), WHAT I PRODUCE ×5, ceiling + MCP default ×5,
Coordinator never-signs, kit-only git status, BOM check (0).

## 3. Files created

| File | Purpose |
|------|---------|
| `distribution-kit/devflow/agents/README.md` | Family README — what lives here, the two sides of an agent, the rules, the `actors/` disambiguation |
| `distribution-kit/devflow/agents/roles/README.md` | The canonical definition contract — every field, the security rules (AC-7/8), producer-first, templates-are-copied (the single source the roster derives `produces` from) |
| `distribution-kit/devflow/agents/coordinator/agent.yaml` | The Coordinator's structured definition — `approves: []` (never signs) |
| `distribution-kit/devflow/agents/coordinator/charter.md` | The Coordinator's charter body — orchestration duties, never-signs, escalation |
| `distribution-kit/devflow/agents/roles/<role>/agent.yaml` (×5) | Structured per-role definitions — executor first-class, approves per policy, tier, tools, `mcp_servers: []`, approver-ceiling note |
| `distribution-kit/devflow/agents/roles/<role>/prompt.md` (×5) | Charter bodies — WHAT I PRODUCE per role, checks, decisions, escalation, never-rules |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| — | none (new folder only) |

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
| The Coordinator's never-signs is encoded as `approves: []` | ADR-008 separation of duties in the structured field, not just prose (ADR-007) |
| Each template carries the APPROVER CEILING comment | US-023 AC-7 claimed by this Bolt (review finding): the ceiling is a property of the templates, visible to the generator |
| `mcp_servers: []` default in every agent.yaml | US-023 AC-8: no implicit MCP exposure; named + allowlisted only |
| `approves` per role policy (FA→US, architect→ADR, qa→MEM, reviewer→MEM/DISC, developer→[]) | The templates show the recommended checkpoint classes per role while staying configurable — and developer stays executor-only by default (production first) |
| Model as `<pick-from-platform-catalog>` placeholder | Templates are skeletons; the model is the adopter's declaration constrained to the platform catalog (ADR-007) |
| The `roles/README.md` carries the field table + security rules | One contract reference the generator (BOLT-002) and the roster (US-024) can cite |

## 8. Deviations and assumptions

No deviations from SPEC-260823-1600 rev 1. Assumption: `approves` per role
is a recommendation in the templates (adopters configure per their
AITL-enable ADR); the security rules (ceiling/MCP) are non-negotiable.

## 9. Verification evidence

### Presence (RED → GREEN)

```
RED:   distribution-kit/devflow/agents/ → ABSENT (0 files)
GREEN: 14 files present (README ×2, coordinator ×2, roles ×10)
       WHAT I PRODUCE in 5/5 charters
       APPROVER CEILING + mcp_servers: [] in 5/5 agent.yaml
       Coordinator approves: [] PRESENT
```

### Invariants

```
Kit-only (ADR-004): git status -- distribution-kit → only ?? agents/  PASS
Encoding: 0 files with BOM                                    PASS
```

### Gates

Documentation Bolt: runtime gates `n/a`; prompt-injection/secret-leak
`pass` (no runtime surface; the templates state constraints, they do not
implement enforcement); hallucination-lint `pass` (refs resolve);
behavioral-reproducibility `pass`; bolt-manifest-validation `pass`
(v_bounces[1] appended, JSON valid).

## 10. Manual interventions

None — the agent produced everything.

## 11. Evidence links

- **Diff / PR:** none (working tree, uncommitted)
- **Commit:** baseline `45d553f`
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-023.BOLT-001-devflow-agent-contract-and-charters.json`

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~12min |
| V-Bounce number | 1 |
| Tests created | 0 (documentation Bolt — deterministic presence/invariant checks instead) |
| AI-generated code | 100% |
| First-pass approval | pending (this MEM) |

## 13. Pending items and stubs

- [ ] BOLT-002 V-Bounce (the wrapper generator + N×4 parity — consumes
      these definitions)
- [ ] BOLT-003 (deployment), BOLT-004 (smoke) — the chain
- [ ] US-024 roster Bolts (derive `produces` from these charters)

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
| **review_ready_at** | `2026-08-23T16:12:00-03:00` |
| **review.started_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **review.decided_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **Review evidence** | diff of the 14 files; presence checks (WHAT I PRODUCE ×5, ceiling + MCP ×5, never-signs); kit-only; encoding; MEM, manifest |
| **Comments** | |
| **Findings** | |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | evidence inspected per the review-evidence column |
