---
id: "MEM-260824-0115"
title: "The roster-as-enablement reshape — actors/ family, the schema v1 rule and the mechanism named in the methodology and the four MainAgents (US-024.BOLT-004, V-Bounce 1)"
date: "2026-08-24"
author: "eugenio.serrano"
llm: "claude-fable-5"
bolt: "US-024.BOLT-004"
spec: "devflow/spec/SPEC-260824-0054-roster-as-enablement-reshape.md"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "7e3eb5e"
applied_adrs:
  - "devflow/adrs/ADR-014-actors-roster-is-the-enablement.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "devflow/metrics/bolts/US-024.BOLT-004-roster-as-enablement-reshape.json"
diff_ref: ""
review_ready_at: "2026-08-24T01:15:33-03:00"
review: # AITL-MEM-Approval — decision dictated in conversation ("Y lo aprobamos!", over the reviewed package) and transcribed by the agent (§3.0)
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-24T01:21:56-03:00"
  decided_at: "2026-08-24T01:21:56-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved as Dev-validator with an independent cross-model disk verification (PASS on every checklist item): the actors/ tree exact (the two retired files gone), the schema v1 rule + the F-S1 relax applied, the example moved with its squad pointer and no capabilities, the four MainAgents carrying the clause, the methodology §3.0.1 naming the human-configuration-act mechanism, both sweeps at 0 hits, MEM + manifest complete. V-Bounce 1 approved — BOLT-004 Development Completed. The examples expansion (human actor + agent actor + illustrative roster, and the model-required-only-for-agents schema fix) proceeds as SPEC revision 2 → V-Bounce 2."
---

# MEM-260824-0115 — The roster-as-enablement reshape (US-024.BOLT-004, V-Bounce 1)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | US-024.BOLT-004 (roster-as-enablement-reshape) |
| **SPEC**        | [SPEC-260824-0054](../spec/SPEC-260824-0054-roster-as-enablement-reshape.md) rev 1 |
| **V-Bounce**    | 1 (executed after SPEC-260824-0050's V-Bounce + MEM approval — the F3 sequencing) |
| **ADRs**        | ADR-014 (§3.8 the mechanism, §3.9 the shape; §3.3.3/§3.6 carried rules), ADR-004 (kit-only) |

---

## 1. Executive summary

This V-Bounce deployed the roster-as-enablement model into the kit — the
only place adopters can read the norm. The `actors/` family was reshaped
to the target: the two retired files **deleted**
(`TEMPLATE-AITL-ENABLE-ADR.md`, `project-policy.yaml`); **`roster.yaml`
created** as the shipped, commented, empty team list — the single
membership authority, stating in its own header that the schema-valid,
human-authored entry IS the explicit configuration and that an agent never
enables its own approval; the worked example **moved to `examples/`** with
its `definition:` pointer fixed to the post-split `agents/squad/` path and
its `capabilities` block removed (the v1 shape, F-S1);
**`TEMPLATE-ACTOR.yaml` simplified** (capabilities deferred to v2 with the
explicit note that the T0/T1 approver ceiling governs as a methodology
rule meanwhile; listing now targets `roster.yaml`); the README rewritten
around the new "The roster is the enablement" section and the updated
resolution rules (an agent holder counts for what **its own `approves`
grants**; membership is the list; authority fields are the human's act);
the INDEX rebuilt as a family-docs index (the team lives in
`roster.yaml`). The **schema** gained the v1 rule (`approver` in `modes` ⇒
non-empty `approves`) and the **existing `definition ⇒ capabilities`
requirement was relaxed** (F-S1 — capabilities stays defined as optional,
so a project already declaring it still validates; the requirement returns
in v2). The **mechanism was named at every adopter-facing surface**: the
methodology §3.0.1 safe-default paragraph now says "a human configuration
act — a schema-valid roster entry granting the checkpoint class… never the
agent's own act"; `agents/README.md`'s governance table row and
create-guide step 6 now grant via the roster; and the **four MainAgents**
carry one byte-identical inline clause defining "explicit, valid
configuration" at the decision point. Verification is GREEN across the
board: exact shape; the three-case validation demo (example v1 PASS ·
approver-with-empty-approves FAIL-FAST · capabilities-declared PASS) via
the dependency-free parser check (pyyaml unavailable — the BOLT-001
precedent); **0 references to the retired mechanism and 0 `roles/` paths
kit-wide** (the 3 allowlisted hits from the previous V-Bounce fixed here,
as its reviewer required); clause hash identical ×4; G-count 39 ×4;
self-containment 0 hits; no BOM.

## 2. Implemented phases

### Phase A — The `actors/` family reshape

Deletions (git rm): the AITL-enable ADR template + the policy file.
Creations: `roster.yaml` (commented skeleton, `actors: []`),
`examples/example.yaml` (git mv + the pointer/capabilities edits).
Rewrites: `TEMPLATE-ACTOR.yaml` (v1 shape + the never-self-enabled bound +
roster.yaml listing), `README.md` (the enablement section + rules 1/5/6 +
living-data + what-lives-here), `INDEX.md` (family docs; the team lives in
roster.yaml).

### Phase B — The schema v1 rule + the F-S1 relax

`roster.schema.yaml`: the new `allOf` (modes contains approver ⇒ approves
minItems 1) replacing the v2-deferred `definition ⇒ capabilities`
requirement (kept as a comment); `capabilities` annotated optional-in-v1;
the `definition` comment now points at `agents/squad/`.

### Phase C — The mechanism named across the kit

Methodology §3.0.1 (the safe-default paragraph — the stale "no `agents:`
section" roster shape also updated to "no schema-valid approver entry");
`agents/README.md` (the governance table's approver row + step 6 — the
carried-as-is wording from the previous V-Bounce rewritten here, in its
final home); the four MainAgents (`CLAUDE.md`, `SKILL.md`,
`AvengaDevFlow.agent.md`, `AvengaDevFlow.md`) — one identical inline
clause in the AITL section.

### Phase D — Verification (GREEN)

Shape exact; three-case validation (parser-based, dependency-free);
retired-mechanism sweep 0 hits; `roles/` path sweep 0 hits (the reviewer's
carried reminder honored — the 3 allowlisted fixes verified explicitly);
clause byte-identical ×4 (single md5 across the four); G-count 39 ×4;
self-containment 0 hits over `actors/`; no BOM.

## 3. Files created

| File | Purpose |
|------|---------|
| `distribution-kit/devflow/actors/roster.yaml` | The team list — the single membership authority; ships empty with the enablement contract in its header comments |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `distribution-kit/devflow/actors/examples/example.yaml` | (moved from `actors/example.yaml`) pointer → `agents/squad/example-qa/agent.yaml`; `capabilities` removed (v1 shape); header explains squad-only pointers + roster.yaml membership |
| `distribution-kit/devflow/actors/TEMPLATE-ACTOR.yaml` | v1 shape — `capabilities` deferred (explicit v2 note; ceiling = methodology rule); listing → `roster.yaml`; the never-self-enabled bound added; `definition` placeholder → `agents/squad/` |
| `distribution-kit/devflow/actors/roster.schema.yaml` | + v1 rule (approver ⇒ approves non-empty); the `definition ⇒ capabilities` requirement relaxed to a v2 comment; `capabilities` marked optional-in-v1 |
| `distribution-kit/devflow/actors/README.md` | Rewritten — "The roster is the enablement" section; family table (roster.yaml + examples/, policy row gone); resolution rules 1/5/6 updated; living-data rule = the human's act |
| `distribution-kit/devflow/actors/INDEX.md` | Rebuilt as the family-docs index — the team lives in `roster.yaml`; the enablement note |
| `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md` | §3.0.1 safe-default paragraph — the mechanism named (human configuration act via the roster entry), the stale `agents:`-section shape fixed |
| `distribution-kit/devflow/agents/README.md` | Governance table approver row + create-guide step 6 → the roster grant (the wording carried as-is by the previous V-Bounce, rewritten in its final home) |
| `distribution-kit/CLAUDE.md` · `.agents/skills/avenga-devflow/SKILL.md` · `.github/agents/AvengaDevFlow.agent.md` · `.opencode/agents/AvengaDevFlow.md` | The byte-identical inline clause defining "explicit, valid configuration" (the roster entry; never self-enabled) — G-count untouched |

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
| `actors/example.yaml` | `actors/examples/example.yaml` | The examples/ subfolder (family shape) |

## 6. Files deleted

| File | Reason |
|------|--------|
| `distribution-kit/devflow/actors/TEMPLATE-AITL-ENABLE-ADR.md` | Retired — the roster entry is the enablement; no per-project ADR |
| `distribution-kit/devflow/actors/project-policy.yaml` | Retired — `aitl_enabled_checkpoints` redundant (the actor's `approves` is the grant); the `human_only` floor is the fixed §3.0.1 rule |

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| `roster.yaml` ships as a commented skeleton with `actors: []` | The kit never ships a team; the header carries the enablement contract at the point of use |
| The example drops `capabilities` (F-S1 choice) | One consistent v1 shape everywhere; template + example + schema requirement return together in v2 |
| The relaxed `allOf` keeps `capabilities` optional, not forbidden | Forward-compatible — a project already declaring it keeps validating; v2 only re-tightens |
| The validation demo used a dependency-free parser check | pyyaml unavailable in the environment — the same precedent the family's first delivery used; the checks re-run identically |
| A prior-MEM note corrected here, not there | The previous MEM said the governance table still carried the "run the generator" phrase for this V-Bounce to fix; in fact the absorption had already fixed that row — only the two enablement references remained, both rewritten here. Approved MEMs are immutable history; the correction is recorded in this one |

## 8. Deviations and assumptions

No deviations from SPEC-260824-0054 rev 1 (the F-S1 handling executed
exactly as specified). Assumption: none — every governed source was
approved before execution. O-2 (`model: inherit` semantics — the
definition's default vs the platform session's model) remains deliberately
unresolved and routed to US-025; nothing in this V-Bounce assumed either
reading.

## 9. Verification evidence

### Shape (RED → GREEN)

```
RED:   actors/ = README · INDEX · TEMPLATE-ACTOR · TEMPLATE-AITL-ENABLE-ADR ·
       example.yaml · project-policy.yaml · roster.schema.yaml
GREEN: actors/ = README · INDEX · TEMPLATE-ACTOR · roster.schema.yaml ·
       roster.yaml · examples/example.yaml      — the two retired files gone
```

### Validation (parser-based, dependency-free)

```
EXAMPLE (v1, no capabilities):            PASS (required ok; approver⇒approves ok;
                                          definition → agents/squad/example-qa/agent.yaml)
MALFORMED (approver + empty approves):    FAIL-FAST (the v1 rule detects it)
WITH capabilities declared:               PASS (optional in v1 — the relaxed allOf)
```

### Sweeps (AC-4 + the carried reviewer reminder)

```
kit-wide "AITL-enable|project-policy|aitl_enabled_checkpoints" → 0 hits
kit-wide "agents/roles" paths                                  → 0 hits
  (the 3 allowlisted from the previous V-Bounce — example.yaml pointer,
   actors/INDEX row, TEMPLATE-ACTOR placeholder — fixed and verified here)
```

### Invariants

```
Four-MainAgent clause: single md5 across the four (byte-identical)  PASS
G-count: 39 × 4                                                     PASS
Self-containment (actors/): maintenance IDs + tools/ → 0 hits       PASS
Encoding: no BOM                                                    PASS
Kit-only (ADR-004): only distribution-kit/** changed                PASS
```

### Gates

Documentation/schema Bolt: unit/integration/perf `n/a` (no runtime
surface, per the approved SPEC §9); prompt-injection/secret-leak `pass`;
hallucination-lint `pass` (every path resolves — the squad pointer
included); behavioral-reproducibility `pass` (the checks re-run
identically); bolt-manifest-validation `pass` (v_bounces[1] appended,
schema PASS).

## 10. Manual interventions

None — the agent produced everything.

## 11. Evidence links

- **Diff / PR:** none (working tree, uncommitted — part of the v5.1 batch)
- **Commit:** baseline `7e3eb5e`
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-024.BOLT-004-roster-as-enablement-reshape.json`

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~15min |
| V-Bounce number | 1 |
| Tests created | 0 (documentation/schema; scripted evidence per SPEC §8) |
| AI-generated code | 100% |
| First-pass approval | pending (this MEM) |

## 13. Pending items and stubs

- [ ] AITL-BOLT-DONE-Approval for BOLT-004 and BOLT-005 after this MEM's
      approval (both Development Completed then).
- [ ] O-2 (`model: inherit` semantics) — routed to US-025.
- [ ] The v2 hardening (capability fields return: template + example +
      the schema requirement + the enforced approver ceiling +
      authority-change audit) — future US/Bolt.
- [ ] US-025's Bolts (the MainAgent lifecycle capability) consume this
      shape.
- [ ] Commit + push of the whole v5.1 batch on the maintainer's order.

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
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-24T01:15:33-03:00` |
| **review.started_at** | `2026-08-24T01:21:56-03:00` |
| **review.decided_at** | `2026-08-24T01:21:56-03:00` |
| **Review evidence** | the actors/ diff (2 deletes, 1 create, 5 rewrites, 1 move); the methodology + agents/README + four-MainAgent edits; the three-case validation demo; the two sweeps (retired mechanism + roles/); the clause hash ×4 + G-count; MEM, manifest |
| **Comments** | |
| **Findings** | |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | evidence inspected per the review-evidence column |
