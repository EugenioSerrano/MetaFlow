---
id: "MEM-260822-0146"
title: "No risk-based approver counts — the executing DEV approves the MEM; SPEC/UAT minimum one approver"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
bolt: "US-014.BOLT-003"
spec: "SPEC-260822-0141"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "0c7f40d"
applied_adrs:
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "US-014.BOLT-003-no-risk-based-approver-counts.json"
diff_ref: "" # uncommitted working-tree change — no commit made (G34)
review_ready_at: "2026-08-22T01:46:21-03:00"
review: # HITL-MEM-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "dev_validator"}]
  started_at: "2026-08-22T01:47:46-03:00"
  decided_at: "2026-08-22T01:47:46-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Inspected the diff: risk-based approver counts removed (grep confirms zero); one approver (executing Dev-validator / incoming executor) at any risk; SPEC/UAT minimum one; risk classification retained; identity rules intact; G-count 39×5; four agents identical; root untouched. No deviations. Approved."
---

<!--
  LANGUAGE POLICY (§3.15): schema in English; prose in content_language (en).
-->

# MEM-260822-0146 — No risk-based approver counts (D7)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | [US-014.BOLT-003](../functional/bolts/US-014.BOLT-003-no-risk-based-approver-counts.md) |
| **SPEC**        | [SPEC-260822-0141](../spec/SPEC-260822-0141-no-risk-based-approver-counts.md) rev. 1 |
| **V-Bounce**    | 1 |
| **ADRs**        | ADR-004 (kit-only) |

---

## 1. Executive summary

This V-Bounce implemented D7 of US-014 — the removal of the risk-based
minimum-approver counts — completing the §3.3 MEM-approver area that
US-014.BOLT-001 deliberately left untouched. The `high` (2) and `critical` (3)
approver counts with their QA/Sec requirement were replaced, in the §3.3 risk
table and prose, the GUARDRAILS approver table and the four agents' tables, by
a single rule: **the executing Dev-validator approves the MEM — one approver at
any risk; after a recorded handoff, the incoming executor; QA/Sec/domain
reviewers optional**. The §3.0 MEM owner cell was aligned, and the SPEC and UAT
owner cells now state a **minimum of one approver**. The risk *classification*
(examples, REV/AREV, autonomy defaults, review-time budgets) was retained — only
the mandatory approver **count** was removed — and the identity-separation rules
(incoming-executor after handoff, G18/G24) are untouched, preserving segregation
of duty. Verification is GREEN: zero risk-based counts remain, "minimum one
approver" appears in the SPEC and UAT cells, G-count 39/39/39/39/39, and only
`distribution-kit/` changed (root untouched). This is the third and last Bolt of
US-014.

---

## 2. Implemented phases

### Phase A — §3.3 MEM approver rule

Replaced the `high`/`critical` approver-count cells in the §3.3 risk table with
"1 (the executing Dev-validator; incoming executor after a handoff)", and
rewrote the accompanying prose ("The risk rubric adds approvers: high adds
QA/Security; critical adds both") to "the MEM is approved by the executing
Dev-validator alone (one approver, any risk); after a recorded handoff, the
incoming executor; QA/Security/domain reviewers optional, never required by
count". The risk classification and its other columns were kept.

### Phase B — §3.0 owner cells

MEM owner cell aligned (executing Dev-validator / incoming executor; extra
reviewers optional). SPEC and UAT owner cells now state a **minimum of one
approver**.

### Phase C — GUARDRAILS + four agents

Rewrote the GUARDRAILS approver table + prose and the four agents' min-approver
table (identical) to the single-approver rule.

### Phase D — Verification (GREEN)

Grep + G-count + root check (see §9).

---

## 3. Files created / 5. renamed / 6. deleted

None.

---

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md` | §3.3 risk table (`high`/`critical` approver column → 1); §3.3 prose (removed the risk-rubric-adds-approvers text); §3.0 MEM owner cell; §3.0 SPEC + UAT owner cells (minimum one approver) |
| `distribution-kit/devflow/GUARDRAILS.md` | Approver-at-MEM prose + table (one approver, any risk) |
| `distribution-kit/CLAUDE.md` | Min-approver table (`high`/`critical` → 1) |
| `distribution-kit/.agents/skills/avenga-devflow/SKILL.md` | Same (identical) |
| `distribution-kit/.github/agents/AvengaDevFlow.agent.md` | Same (identical) |
| `distribution-kit/.opencode/agents/AvengaDevFlow.md` | Same (identical) |

---

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| One approver (executing DEV) at any risk | Maintainer D7 — the DEV who takes the Bolt owns finishing it and approving its MEM |
| Kept the risk classification (examples, REV/AREV, autonomy, budgets) | Risk class is still useful; only the mandatory approver count was the blocker (AREV-001 F-03) |
| Kept the identity rules (handoff incoming-executor, G18/G24) | They provide segregation of duty — not a role count |
| SPEC/UAT minimum one approver | Consistency; extra roles are guidance |
| Left the risk-table structure intact | Minimal change — only the approver column/prose |

---

## 8. Deviations and assumptions

None. Implemented exactly as SPEC-260822-0141 Phase A–C. Assumption: keeping the
risk table with a now-uniform "1" approver column (rather than deleting the
column) best preserves the risk rubric while making "no risk-based count"
explicit.

---

## 9. Verification evidence

### AC-1 (risk-based counts removed)
```
$ rg -n "2 \(the executing Dev-validator \+ QA|3 \(the executing Dev-validator \+ QA|adds QA \*or\* Sec|risk rubric adds" distribution-kit/
No matches found
```

### AC-2 (SPEC/UAT minimum one) / AC-4 (risk classification retained)
```
$ rg -c "minimum one approver" distribution-kit/   => Avenga-DevFlow.md: 2 (SPEC + UAT cells)
Risk table (Risk | Examples | REV/AREV | Approver) retained; only the approver column changed to 1.
```

### AC-3 (identity rules) / AC-5 (sync + G-count)
```
Handoff incoming-executor rule and G18/G24 not edited.
G-count: CLAUDE 39 · SKILL 39 · agent.md 39 · opencode 39 · GUARDRAILS 39. Agent tables identical.
```

### AC-6 (root) / AC-7 (manifest)
```
$ git status --short | (nothing outside distribution-kit/ and devflow/)
US-014.BOLT-003 manifest: valid JSON (v_bounces: 1, spec_revisions: 1).
```

### Gates
prompt-injection / secret-leak / hallucination-lint / behavioral-reproducibility /
bolt-manifest-validation `pass`; the rest `n/a` (documentation-only).

---

## 10. Manual interventions

None.

---

## 11. Evidence links

- **Diff / PR:** none — uncommitted working-tree change (G34).
- **Commit:** baseline `0c7f40d`; V-Bounce output uncommitted.
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-014.BOLT-003-no-risk-based-approver-counts.json`.

---

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~5 min |
| V-Bounce number | 1 |
| Tests created | n/a — deterministic grep/consistency checks |
| AI-generated code | 100% |
| First-pass approval | pending HITL-MEM-Approval |

---

## 13. Pending items and stubs

- [ ] `HITL-MEM-Approval` (this package).
- [ ] `HITL-BOLT-DONE-Approval` (acceptance — `feature` → PO/PM).
- [ ] After BOLT-003 Done, **US-014 is fully implemented** (all three Bolts) → commit + push (explicit user request — G34).
- [ ] Root receives the US-014 changes at the next §5.16 migration.

---

## 14. HITL-MEM-Approval

> **Avenga DevFlow §2.12, §3.0.** Created by the agent, no mutable status,
> never self-approved. Risk `medium` → 1 approver (the executing
> Dev-validator).

| Field | Value |
|-------|-------|
| **Reviewers** | eugenio.serrano (dev_validator) |
| **Decision** | approved |
| **review_ready_at** | `2026-08-22T01:46:21-03:00` |
| **review.started_at** | `2026-08-22T01:47:46-03:00` |
| **review.decided_at** | `2026-08-22T01:47:46-03:00` |
| **Review evidence** | counts-removed grep, minimum-one grep, G-count 39×5, git status, manifest JSON |
