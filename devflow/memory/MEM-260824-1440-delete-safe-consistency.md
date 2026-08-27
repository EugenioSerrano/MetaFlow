---
id: "MEM-260824-1440"
title: "The delete-safe consistency contract delivered — N:1 cardinality pinned, the check procedure and the edge cases (US-025.BOLT-003, V-Bounce 1)"
date: "2026-08-24"
author: "eugenio.serrano"
llm: "claude-fable-5"
bolt: "US-025.BOLT-003"
spec: "devflow/spec/SPEC-260824-1423-delete-safe-consistency.md"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "dce3618"
applied_adrs:
  - "devflow/adrs/ADR-013-agent-lifecycle-governance.md"
  - "devflow/adrs/ADR-014-actors-roster-is-the-enablement.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "devflow/metrics/bolts/US-025.BOLT-003-delete-safe-consistency.json"
diff_ref: ""
review_ready_at: "2026-08-24T14:40:10-03:00"
review: # AITL-MEM-Approval — decision dictated in conversation ("Aprobado!") and transcribed by the agent (§3.0)
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-24T14:44:35-03:00"
  decided_at: "2026-08-24T14:44:35-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved as Dev-validator: the 2-file diff inspected against the approved payload — the contract verbatim (N:1 cardinality + actor-id wrapper naming + the check procedure quoting the shared body's order + the four edge cases), the single pointer line, the pinned hash x4 unchanged, zero maintenance refs, and the transparently-recorded anchor-wrapping stop/fix (the stop condition working as designed, zero content impact). V-Bounce 1 approved — BOLT-003 Development Completed; acceptance batched with the US-025 closure. AC-4 covered; next: BOLT-005 (the kit G07 scoping) then BOLT-004 (the pilot)."
---

# MEM-260824-1440 — The delete-safe consistency contract (US-025.BOLT-003, V-Bounce 1)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | US-025.BOLT-003 (delete-safe-consistency) |
| **SPEC**        | [SPEC-260824-1423](../spec/SPEC-260824-1423-delete-safe-consistency.md) rev 1 |
| **V-Bounce**    | 1 |
| **ADRs**        | ADR-013 (bounds), ADR-014 (roster = membership authority), ADR-004 |

---

## 1. Executive summary

This V-Bounce turned "never break a referenced definition" into a
**checkable contract**. `agents/squad/README.md` gained "The lifecycle
consistency contract" exactly per the approved payload: the three
invariants with the **N:1 cardinality pinned** (a wrapper belongs to ONE
actor-instance and is **named by the actor `id`** — the reviewer's
observation that killed the spawn-folder collision; a definition needs
≥1 referencing actor; every agent actor is listed in `roster.yaml` — an
unlisted file is flagged, never silently adopted); the **reference-check
procedure** opening with the shared body's own order ("check `roster.yaml`
and the actor files first", quoted) and its three delete semantics
(actor-delete removes ITS wrapper+file+listing; the definition falls
**only at zero**; wrapper-only removal is legitimate); and the **four edge
cases** (shared definition, last actor, orphans, unlisted actor).
`agents/README.md` gained exactly **one** Rules line pointing at the
contract (the minimal collision surface with the sequenced US-023 docs
Bolts). Verification is GREEN: the **read-through** confirms the contract
quotes and concretizes — never contradicts — the shared body's Delete
flow; the four MainAgents' lifecycle section is untouched (**pinned hash
×4 == `cd24754c320d…`**); both touched files carry **zero** maintenance
references; the pointer is single; cross-references resolve; no BOM. One
execution note: the first run STOPPED correctly on an anchor mismatch (the
squad/README closing line wraps differently than the SPEC's anchor
guessed) — the stop condition did its job; the anchor was corrected to the
on-disk wording and the run completed (no content impact; recorded here
for transparency). This covers US-025 **AC-4** and anchors AC-3's
consistency legs — the lifecycle capability is now complete except the kit
G07 scoping (BOLT-005) and the pilot (BOLT-004).

## 2. Implemented phases

### Phase A — The contract
Appended to `squad/README.md` after the N:1 reuse paragraph — payload
verbatim (including the pre-approval naming pin).

### Phase B — The pointer
One line in `agents/README.md` Rules ("Delete is checked, never blind…").

### Phase C — Verification (GREEN)
Read-through (the check-order quote present in contract AND body); pinned
hash ×4 unchanged; maintenance refs ZERO ×2; pointer ×1; cross-refs; no BOM.

## 3. Files created

| File | Purpose |
|------|---------|
| — | none |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `distribution-kit/devflow/agents/squad/README.md` | + "The lifecycle consistency contract" (invariants with pinned N:1 cardinality + actor-id wrapper naming · the reference-check procedure · four edge cases) |
| `distribution-kit/devflow/agents/README.md` | + one Rules line pointing at the contract |

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
| The contract appended after the N:1 reuse paragraph | The reuse statement is the setup; the contract is its consequences — natural reading order |
| The anchor corrected at execution (same sentence, on-disk wrapping) | The stop condition fired exactly as designed on the mismatch; the fix matched the SPEC's intent (the closing N:1 paragraph) with zero content change |

## 8. Deviations and assumptions

No content deviations from SPEC-260824-1423 rev 1. One mechanical
adjustment recorded above (the anchor's line-wrapping, caught by the stop
condition — the insertion point and content are exactly as specified).

## 9. Verification evidence

```
READ-THROUGH:      "check roster.yaml and the actor files first" present in the
                   contract AND the shared body — concretization, no contradiction
Pinned hash x4:    cd24754c320df93c85339aadcddb1803 == reference (UNCHANGED)
Maintenance refs:  ZERO x2 (squad/README.md, agents/README.md)
Pointer:           exactly one line
Cross-refs:        ../INDEX.md, roster.yaml resolve
Encoding:          no BOM
```

### Gates

Documentation Bolt: unit/integration/perf `n/a` (per the approved SPEC
§9); prompt-injection `pass`; secret-leak `pass`; hallucination-lint
`pass`; behavioral-reproducibility `pass`; bolt-manifest-validation
`pass` (v_bounces[1] appended, schema PASS).

## 10. Manual interventions

None — the agent produced everything.

## 11. Evidence links

- **Diff / PR:** working tree over baseline `dce3618` (uncommitted —
  presented for review)
- **Commit:** baseline `dce3618`
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-025.BOLT-003-delete-safe-consistency.json`

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~8min |
| V-Bounce number | 1 |
| Tests created | 0 (documentation; scripted evidence per SPEC §8) |
| AI-generated code | 100% |
| First-pass approval | pending (this MEM) |

## 13. Pending items and stubs

- [ ] **BOLT-005** (the kit GUARDRAILS G07 scoping — REV-005 F-02 🔴, the
      last normative gap).
- [ ] **BOLT-004** (the pilot — the US-025 finale; the smoke-test E2E
      cycle formalized).
- [ ] AITL-BOLT-DONE-Approval ×3 (BOLT-001/002/003) batched with the
      US-025 closure.

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
| **review_ready_at** | `2026-08-24T14:40:10-03:00` |
| **review.started_at** | `2026-08-24T14:44:35-03:00` |
| **review.decided_at** | `2026-08-24T14:44:35-03:00` |
| **Review evidence** | the 2-file diff; the read-through quote check; the pinned-hash comparison; the sweeps; MEM, manifest |
| **Comments** | |
| **Findings** | |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | evidence inspected per the review-evidence column |
