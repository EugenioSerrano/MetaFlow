---
id: "MEM-260824-1457"
title: "The kit G07 scoping deployed at six surfaces — the REV-005 F-02 gray zone closed at every altitude (US-025.BOLT-005, V-Bounce 1)"
date: "2026-08-24"
author: "eugenio.serrano"
llm: "claude-fable-5"
bolt: "US-025.BOLT-005"
spec: "devflow/spec/SPEC-260824-1447-kit-g07-scoping.md"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "463e21a"
applied_adrs:
  - "devflow/adrs/ADR-013-agent-lifecycle-governance.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "devflow/metrics/bolts/US-025.BOLT-005-kit-g07-scoping.json"
diff_ref: ""
review_ready_at: "2026-08-24T14:57:19-03:00"
review: # AITL-MEM-Approval — decision dictated in conversation ("aprobado!") and transcribed by the agent (§3.0)
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-24T14:59:37-03:00"
  decided_at: "2026-08-24T14:59:37-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved as Dev-validator: the 7-file diff inspected — the SCOPE clause at the GUARDRAILS altitude with the absolutism-preserving close, the byte-identical row x4, the four entry surfaces with the consistent compact formula (incl. AGENTS.md, the auto-loaded entry point), G-count 39x5, the lifecycle section untouched (pinned hash), and the zero-remaining sweep. REV-005 F-02 (the last Major) is CLOSED at every altitude the kit speaks from. V-Bounce 1 approved — BOLT-005 Development Completed; acceptance batched with the US-025 closure. Next: BOLT-004, the pilot."
---

# MEM-260824-1457 — The kit G07 scoping (US-025.BOLT-005, V-Bounce 1)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | US-025.BOLT-005 (kit-g07-scoping — the ADR-013 §3.7 citing Bolt) |
| **SPEC**        | [SPEC-260824-1447](../spec/SPEC-260824-1447-kit-g07-scoping.md) rev 1 |
| **V-Bounce**    | 1 |
| **ADRs**        | ADR-013 (the scoping decision this Bolt cites and the kit now expresses), ADR-004 |

---

## 1. Executive summary

This V-Bounce closed the smoke test's Major finding (REV-005 F-02) at
**every altitude the kit speaks from**. Nine edits across seven files, in
one scripted pass with per-string uniqueness asserted first: the
**GUARDRAILS G07 row** gained the full SCOPE clause (the agent lifecycle
is operational configuration, not a code change — the agent-system
boundary, the §5.12/roster-rule anchor, the consistency-contract bounds,
the approver-authority exclusion, and the closing "everything else this
rule covers stays absolutely blocked"); the **four MainAgents' compressed
G07 row** gained the row-length scope (byte-identical ×4); and the **four
entry-surface statements** the cross-model pre-sweep found — `AGENTS.md`
(the adopter's auto-loaded entry point, where the gray zone would have
survived), `devflow/README.md`'s golden rule, and `devflow/ONBOARDING.md`'s
golden rule + FAQ answer — each gained the same compact scope-out formula.
Verification is GREEN on every gate: **G-count 39 × 5** surfaces (the
scope lives inside existing rows — zero collateral), the four agents' G07
row **hash-identical**, the lifecycle section **untouched** (pinned hash
== `cd24754c320d…` ×4), the scope-out markers present at every altitude,
and the **zero-remaining sweep** confirms no kit surface states G07's
absolutism without the scope-out anymore. The kit now says ONE thing about
the agent lifecycle — in the guardrail, in the agents' own tables, in the
lifecycle section, in the family READMEs and at every entry door. With
this, US-025's normative work is complete; only the pilot (BOLT-004)
remains.

## 2. Implemented phases

### Phase A — the GUARDRAILS row (the full clause) · Phase B — the four
MainAgents' row (byte-sync) · Phase B' — the four entry surfaces (the
compact formula; the widening the SPEC adopted pre-approval from the
reviewer's kit-wide pre-sweep) · Phase C — verification (GREEN, evidence
below).

## 3. Files created

| File | Purpose |
|------|---------|
| — | none |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `distribution-kit/devflow/GUARDRAILS.md` | The G07 response gains the SCOPE clause (bounds + anchors + the absolutism-preserving close) |
| The four MainAgents (`CLAUDE.md`, `SKILL.md`, `AvengaDevFlow.agent.md`, `AvengaDevFlow.md`) | The compressed G07 row gains the row-length scope (byte-identical ×4) |
| `distribution-kit/AGENTS.md` | The entry-point statement gains the compact scope-out |
| `distribution-kit/devflow/README.md` | The golden rule idem |
| `distribution-kit/devflow/ONBOARDING.md` | The golden rule + the FAQ answer idem (×2 spots) |

## 5. Files renamed / ## 6. Files deleted

None.

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| One consistent compact formula at the entry surfaces | Entry doors stay tight; the full bounds live at the GUARDRAILS altitude — one semantics, different depths |
| Per-string uniqueness asserted before any edit (9/9) | The absolutist phrase family repeats across the kit — the assertion is what makes "only these nine spots" verifiable |
| The sweep is a zero-remaining gate, not a report | After this Bolt there is no legitimate unscoped statement left — a seventh occurrence would be a defect, not a finding |

## 8. Deviations and assumptions

No deviations from SPEC-260824-1447 rev 1 (Phase B' executed exactly as
the pre-approval widening specified). No assumptions.

## 9. Verification evidence

```
STOP CONDITIONS:     9/9 old strings found exactly once
G-count:             39 × 5 surfaces (GUARDRAILS + the four agents)
G07 row ×4:          SINGLE hash (byte-identical)
Lifecycle section:   cd24754c320df93c85339aadcddb1803 == reference (UNTOUCHED)
Scope-out markers:   present at every altitude (GUARDRAILS · agents · AGENTS.md ·
                     README golden rule · ONBOARDING ×2)
Zero-remaining sweep: ZERO unscoped absolutist statements kit-wide
Encoding:            no BOM (×7)
```

### Gates

Documentation Bolt: unit/integration/perf `n/a` (per the approved SPEC
§9); prompt-injection `pass`; secret-leak `pass`; hallucination-lint
`pass` (the clause's anchors — §5.12, the family rules, the consistency
contract — exist in the kit); behavioral-reproducibility `pass`;
bolt-manifest-validation `pass` (v_bounces[1] appended, schema PASS).

## 10. Manual interventions

None — the agent produced everything.

## 11. Evidence links

- **Diff / PR:** working tree over baseline `463e21a` (uncommitted —
  presented for review)
- **Commit:** baseline `463e21a`
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-025.BOLT-005-kit-g07-scoping.json`

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~8min |
| V-Bounce number | 1 |
| Tests created | 0 (documentation; scripted evidence per SPEC §8) |
| AI-generated code | 100% |
| First-pass approval | pending (this MEM) |

## 13. Pending items and stubs

- [ ] **REV-005 F-02: CLOSED by this Bolt** (the last Major) — the REV's
      routing table row 2 completes; with the earlier closures
      (F-09/F-13/F-14 by BOLT-002) the REV-005 items routed to US-025 are
      all delivered.
- [ ] **BOLT-004 — the pilot**: the US-025 finale. The maintainer's second
      adopter test IS its execution vehicle: install → spawn → delete on
      the pilot platform, roster consistent, with the now-complete kit.
- [ ] AITL-BOLT-DONE-Approval ×4 (BOLT-001/002/003/005) batched with the
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
| **review_ready_at** | `2026-08-24T14:57:19-03:00` |
| **review.started_at** | `2026-08-24T14:59:37-03:00` |
| **review.decided_at** | `2026-08-24T14:59:37-03:00` |
| **Review evidence** | the 7-file diff (9 edits); the G-count/row-hash/section-hash evidence; the zero-remaining sweep; MEM, manifest |
| **Comments** | |
| **Findings** | |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | evidence inspected per the review-evidence column |
