---
id: "MEM-260822-0332"
title: "Remove the risk-based approver-count residuals from the kit (ADR-005 absence sweep) — BUG-002 fix"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
bolt: "US-000.BOLT-005"
spec: "SPEC-260822-0326"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "c30a739"
applied_adrs:
  - "devflow/adrs/ADR-005-removal-completeness-phrase-family-sweep.md"
  - "devflow/adrs/ADR-002-documentation-defect-classification.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "US-000.BOLT-005-approver-count-residual-sweep.json"
diff_ref: "" # uncommitted at MEM time (kit-only working tree)
review_ready_at: "2026-08-22T03:32:19-03:00"
review: # HITL-MEM-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "dev_validator"}]
  started_at: "2026-08-22T03:36:01-03:00"
  decided_at: "2026-08-22T03:36:01-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Reviewed the diff (11 kit files) and the §9 RED/GREEN evidence, including a line-by-line over-removal audit: every removed QA/Sec/approver line has a rule-preserving replacement, the risk tables kept their autonomy/AREV columns (only the count cell changed 2/3->1), and the full allowlist (correct rule, escalation example, time-budget-per-risk, autonomy column, risk-class escalation, SPEC domain-owner guidance) is intact. AC-1..AC-7 pass: zero residuals, four agents agree and byte-synced (G-count 39x5), root untouched, manifest validates. The two unrelated removals in the combined diff (HITL-UAT/UNIT blocks) belong to the already-Done US-015. F-01 release blocker cleared. Bolt now Development Completed."
---

<!--
  LANGUAGE POLICY (§3.15): schema/headings English; prose content_language (en).
  BUG V-Bounce (ADR-002 class 1): RED/GREEN evidence is deterministic grep/diff,
  not an automated test suite (§9). Kit-only edits (ADR-004); root untouched.
  First application of ADR-005.
-->

# MEM-260822-0332 — Remove the risk-based approver-count residuals (BUG-002, ADR-005 absence sweep)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | [US-000.BOLT-005](../functional/bolts/US-000.BOLT-005-approver-count-residual-sweep.md) |
| **SPEC**        | [SPEC-260822-0326](../spec/SPEC-260822-0326-approver-count-residual-sweep.md) — revision 1 |
| **V-Bounce**    | 1 |
| **ADRs**        | ADR-005 (sweep standard), ADR-002 (class 1), ADR-004 (kit-only) |

---

## 1. Executive summary

This V-Bounce fixes BUG-002 (AREV-003 F-01, 🔴 release-blocking): the risk-based
approver-count rule that US-014.BOLT-003 removed still lived as active
instruction in ~20 sites across the kit, including the four auto-loaded agents,
contradicting the approved single-approver rule. It is the **first application
of ADR-005** — the completeness sweep over the fixed location set, phrased as an
absence. Following the SPEC's declared phrase family, location set and
legitimate-homonym allowlist, 22 residual sites were rewritten to the
single-approver rule ("one approver, at any risk; QA/Sec/domain reviewers
optional") and 2 stale section titles (F-06.1, "risk rubric") were aligned,
while every allowlist entry (the correct new rule, the escalation examples, the
review-time-budget-per-risk wording, the autonomy column, the risk-class
escalation concept) was deliberately preserved. Outcome: the post-fix absence
sweep returns **zero residuals** across the location set, the allowlist is
intact (over-removal avoided), the four agents agree with each other and with
§3.0 (byte-synced, G-count 39×5), and the root `devflow/` methodology is
untouched (ADR-004). The kit no longer contradicts itself about who approves the
MEM — the F-01 release blocker is cleared.

---

## 2. Implemented phases

### Phase A — Methodology + GUARDRAILS
Rewrote the §3.0 HITL-MEM narrative "Who" bullet (`Avenga-DevFlow.md`) — which
carried the semantic paraphrase "as required by risk and scope" that the
original BUG-002 grep missed and the ADR-005 phrase family caught — and the
GUARDRAILS checkpoint-map MEM row, both to the single-approver rule. Confirmed
the correct rule at §3.0 table (1398) and GUARDRAILS section (380) untouched.

### Phase B — Four agents (identical edits)
Rewrote, identically across `CLAUDE.md`, `SKILL.md`, `AvengaDevFlow.agent.md`
and `AvengaDevFlow.md`: the `HITL-MEM-Approval` HITL-table row (`+ QA/Sec per
risk` → single-approver), the V-Bounce step-8 prose (`+ QA/Sec for
high/critical` → optional-any-risk), and the "Minimum approvers … (risk rubric,
§3.3)" section title (dropped "risk rubric"). This is the highest-risk carrier —
an auto-loaded agent enforcing its own table would have demanded the removed
QA/Sec sign-off.

### Phase C — README + ONBOARDING
Rewrote the three README MEM-approval bullets and the two ONBOARDING locations
(the self-approval bullet and the "Who approves my MEM?" FAQ) to the
single-approver rule.

### Phase D — Templates
Rewrote `TEMPLATE-MEM.md` (the HITL-MEM blockquote + the two reviewer/role table
cells) and the `TEMPLATE-RISK.md` / `risks/README.md` min-approver **count
cells** (`high: 2`, `critical: 3` → `1`), keeping the autonomy column (L3/L2/L1
genuinely varies by risk) intact.

### Phase E — Verification (GREEN, §9)
Absence sweep, allowlist presence, four-agent agreement, G-count, root check.

---

## 3. Files created

| File | Purpose |
|------|---------|
| `devflow/memory/MEM-260822-0332-approver-count-residual-sweep.md` | This MEM — RED/GREEN record of the BUG-002 fix |

---

## 4. Files modified

| File | Change |
|------|--------|
| `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md` | §3.0 HITL-MEM narrative "Who" bullet (semantic paraphrase → single-approver rule) |
| `distribution-kit/devflow/GUARDRAILS.md` | Checkpoint-map HITL-MEM row → single-approver rule |
| `distribution-kit/CLAUDE.md` | HITL-MEM table row + V-Bounce step 8 + "(risk rubric)" title |
| `distribution-kit/.agents/skills/avenga-devflow/SKILL.md` | Identical to CLAUDE.md (four-agent sync) |
| `distribution-kit/.github/agents/AvengaDevFlow.agent.md` | Identical to CLAUDE.md (four-agent sync) |
| `distribution-kit/.opencode/agents/AvengaDevFlow.md` | Identical to CLAUDE.md (four-agent sync) |
| `distribution-kit/devflow/README.md` | 3 MEM-approval bullets → single-approver rule |
| `distribution-kit/devflow/ONBOARDING.md` | Self-approval bullet + "Who approves my MEM?" FAQ |
| `distribution-kit/devflow/memory/TEMPLATE-MEM.md` | HITL-MEM blockquote + 2 reviewer/role table cells |
| `distribution-kit/devflow/risks/TEMPLATE-RISK.md` | Min-approver count cells high/critical → 1 (autonomy column kept) |
| `distribution-kit/devflow/risks/README.md` | Min-approver count cells high/critical → 1 (autonomy column kept) |

> Governance records for this V-Bounce also changed in the root `devflow/`
> (BUG-002, US-000.BOLT-005 doc + manifest, SPEC, this MEM, INDEXes) — DevFlow
> tracking, not methodology framework files; AC-6 allows them.

---

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
| —    | —        | —      |

## 6. Files deleted

| File | Reason |
|------|--------|
| —    | —      |

---

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| Follow the ADR-005 declared phrase family, location set and allowlist verbatim | First application of the standard; the point is to prove the sweep, not improvise it |
| Preserve every allowlist entry (correct rule, escalation examples, time-budget-per-risk, autonomy column, risk-class escalation) | ADR-005 §3(3): over-removal is a failure, not a success. AC-4 asserts their presence |
| Keep the `risks/` min-approver **table** (fix only the count cells to `1`) | The autonomy column (L3/L2/L1) genuinely varies by risk — the table is still meaningful; only the approver count was the residual |
| Reword rather than delete the §3.0 narrative "Who" bullet | The bullet must still state who approves (the Dev-validator); only the "as required by risk" count paraphrase was wrong |
| Leave `Avenga-DevFlow.md:2682` (SPEC domain-owner guidance) untouched | It is the HITL-SPEC "Who" bullet — BUG-003/BOLT-006 territory, not BUG-002; editing it here would cross Bolt scope (G04) |

---

## 8. Deviations and assumptions

No deviations from the approved SPEC. All 22 fix-sites + 2 title alignments
applied as declared; the allowlist was preserved.

**Assumption:** `?? .claude/` in `git status` is the Claude Code harness config
directory, pre-existing and unrelated to this V-Bounce — not a root `devflow/`
methodology file, so AC-6 holds.

**Note (validates ADR-005):** the site at `Avenga-DevFlow.md:2730` ("as required
by risk and scope") was a **semantic paraphrase** that the original BUG-002
literal grep did not catch — it surfaced only because ADR-005 §3(1) mandates
sweeping paraphrases, and BUG-002's `expected_result` already covered "every
location that describes MEM approval". Fixing it here needed no scope change.

---

## 9. Verification evidence

Documentation defect (ADR-002 class 1) — RED/GREEN is deterministic grep.

### RED (pre-fix — residuals present)
The BUG-002 §2 inventory, reproduced independently during AREV-003 by
Challenger, Defender and Judge:
```
Avenga-DevFlow.md:2730  "as required by risk and scope"
GUARDRAILS.md:30        "(+ QA/Sec/domain as risk requires)"
README.md:203,232,253   "(+ QA/Sec for high/critical)" x2, "(+ QA/Sec per risk)"
ONBOARDING.md:52,101     "(+ QA/Sec for high/critical risk)", "For high risk, QA or Security is added; for critical, both"
TEMPLATE-MEM.md:233,246,247
TEMPLATE-RISK.md:77,78   "2 (…+ QA or Sec)", "3 (…+ QA + Sec)"
risks/README.md:118,119  same count table
4 agents x2 (HITL-MEM row :401/418/446/429 + step 8 :307/324/352/335)
4 agents titles "(risk rubric, §3.3)"
```

### GREEN (post-fix)
```
AC-1 absence sweep (residual phrase family, full location set): ZERO residuals — PASS
AC-2 four agents agree: HITL-MEM row = 1/1/1/1 ; step-8 new phrasing = 1/1/1/1 — PASS
AC-3 titles: no "(risk rubric)" remains ; every min-approver cell = 1 (4 cells) — PASS
AC-4 allowlist intact: §3.0 table rule (1), GUARDRAILS 380 rule (1), escalation
     example 2160 (1), review-time-budgets title (1), risk-class escalation (1) — PASS
AC-5 G-count: GUARDRAILS 39 ; CLAUDE 39 ; SKILL 39 ; agent.md 39 ; opencode 39 — PASS
AC-6 root: only distribution-kit/ + governance records changed (`?? .claude/` = harness config, unrelated) — PASS
```

### Gates (§7 of the SPEC)
Documentation-only/internal/not an automated-test BUG → unit/integration, SAST/SBOM,
perf, IP, PII, dep-confusion, test-first: `n/a`. Prompt-injection, secret-leak,
hallucination-lint, behavioral-reproducibility, bolt-manifest-validation: `pass`.

---

## 10. Manual interventions

None — all edits agent-generated.

---

## 11. Evidence links

- **Diff / PR:** uncommitted working tree at MEM time (kit + governance records)
- **Commit:** baseline `c30a739`; this V-Bounce's commit pending user request
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-000.BOLT-005-approver-count-residual-sweep.json`

---

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~15 min |
| V-Bounce number | 1 |
| Tests created | 0 (documentation-only; deterministic grep RED/GREEN) |
| AI-generated code | 100% |
| First-pass approval | pending |

---

## 13. Pending items and stubs

- [ ] **BUG-003 / US-000.BOLT-006** — the sibling role-as-gate residuals in the
  §3.0 narrative (approved, Bolt ready; independent of this Bolt).
- [ ] After both Bolts Done → re-verify and close v4.2.

---

## 14. HITL-MEM-Approval

> **Avenga DevFlow §2.12, §3.0.** Created by the agent with no mutable status;
> never self-approved. The executing Dev-validator inspects the diff, the §9
> RED/GREEN evidence, this MEM and the manifest, and records `HITL-MEM-Approval`
> here and in the manifest `hitl_approvals[]`. Risk medium → one approver.

| Field | Value |
|-------|-------|
| **Reviewers (executing Dev-validator)** | eugenio.serrano |
| **Roles** | dev_validator (risk medium → 1 approver) |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-22T03:32:19-03:00` |
| **review.started_at** | `2026-08-22T03:36:01-03:00` |
| **review.decided_at** | `2026-08-22T03:36:01-03:00` |
| **Review evidence** | diff (11 kit files) + §9 RED/GREEN sweep + over-removal audit + manifest |
| **Findings** | none — `acknowledged_without_comment: true` |
