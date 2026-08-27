---
id: "SPEC-260822-0141"
title: "No risk-based approver counts — the executing DEV approves the MEM; SPEC/UAT minimum one approver"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
status: "approved" # draft | approved | blocked | obsolete
origin: "US-014"
bolt: "US-014.BOLT-003" # ⚠️ MANDATORY
revision: 1
associated_adrs:
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
prerequisites:
  - "SPEC-260822-0053" # BOLT-001 — established the operability principle; run first (Done)
risk_class: "medium"
autonomy_level: "L3"
turn_budget: ""
data_classification: "internal"
review_ready_at: "2026-08-22T01:41:34-03:00"
review: # HITL-SPEC-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "dev_validator"}]
  started_at: "2026-08-22T01:43:46-03:00"
  decided_at: "2026-08-22T01:43:46-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Reviewed revision 1 against US-014 (approved), the Bolt US-014.BOLT-003, AREV-001 F-03/F-07 and ADR-004: the D7 approach (remove the risk-based approver counts, executing DEV approves the MEM, SPEC/UAT minimum one, risk classification retained, identity rules kept) is faithful and correctly scoped to the §3.3 area BOLT-001 left untouched. Approved as drafted — authorizes the V-Bounce."
---

<!--
  LANGUAGE POLICY (§3.15): schema in English; prose in content_language (en).
  Kit-only edits (ADR-004); root untouched. Documentation change — deterministic
  grep/consistency verification.
-->

# SPEC-260822-0141 — No risk-based approver counts

| Field | Value |
|-------|-------|
| **Origin** | [US-014](../functional/user-stories/US-014-role-availability-policy.md) (approved) |
| **Bolt** | [US-014.BOLT-003](../functional/bolts/US-014.BOLT-003-no-risk-based-approver-counts.md) (approved) |
| **ADRs** | [ADR-004](../adrs/ADR-004-repository-partition-v2.md) (kit-only) |
| **Risk Class** | medium |
| **Revision** | 1 |

---

## 1. Objective

Implement **D7** of US-014 in the distributable: remove the **risk-based
minimum-approver counts** at `HITL-MEM-Approval` (the 1/1/2/3 rubric and its
QA/Sec requirement) and establish that **the DEV who takes the Bolt approves
its MEM** — one approver, regardless of risk; after a recorded handoff, the
incoming executor. `HITL-SPEC-Approval` and `HITL-UAT-Approval` have a
**minimum of one approver**; additional named roles are guidance, not a
required quorum.

**If not implemented:** the AREV-001 F-03 blocker persists — `high`/`critical`
work is structurally unapprovable at its final gate in a team without QA/Sec.

---

## 2. Context

US-014 (approved) records D7. This completes the §3.3 MEM-approver area that
US-014.BOLT-001 (D3, Done) deliberately left untouched to avoid double-editing:
BOLT-001 removed the role *block* on other routes; this Bolt removes the
*counts* and rewrites the MEM approver rule wholesale. Together they fully
relax the MEM gate for a single operator. Kit-only (ADR-004).

---

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | `devflow/functional/bolts/US-014.BOLT-003-no-risk-based-approver-counts.md` | HITL-BOLT-READY-Approval ✓ (2026-08-22T00:53:56-03:00) |
| Parent US | `devflow/functional/user-stories/US-014-role-availability-policy.md` | HITL-US-Approval ✓ |
| Evidence | AREV-001 F-03 / F-07 (approved Verdict), REV-001 F-04/F-06 (closed) | approved ✓ |
| ADR | `devflow/adrs/ADR-004-repository-partition-v2.md` | HITL-ADR-Approval ✓ |
| Prior Bolt | US-014.BOLT-001 (Done) — established the operability principle | HITL-BOLT-DONE-Approval ✓ |
| Repository baseline | branch `4.2`, HEAD `0c7f40d` (working tree: US-014 package uncommitted) | — |

Pre-SPEC evidence gate: **all governed sources approved**.

---

## 4. Scope

### In scope (`distribution-kit/`)

- **§3.3 MEM approver rule:** replace the risk-based minimum-approver table
  (`low`/`medium` 1, `high` 2 = Dev + QA/Sec, `critical` 3 = Dev + QA + Sec) and
  its prose ("The risk rubric adds approvers: high adds QA or Security…") with:
  **the executing Dev-validator approves the MEM (one approver); after a
  recorded handoff, the incoming executor** (§3.3). QA/Sec/domain reviewers are
  optional, never required by count.
- **§3.0 HITL-MEM-Approval owner cell:** align (drop "(+ QA/Sec/domain reviewers
  as risk requires)"; state the executing Dev-validator / incoming executor).
- **§3.0 HITL-SPEC-Approval and HITL-UAT-Approval owner cells:** state a
  **minimum of one approver** (BOLT-001 already added the no-holder fallback;
  this adds the explicit minimum).
- **`GUARDRAILS.md`** min-approver table (Risk class | Min approvers) → same rule.
- **The four agents' "Minimum approvers at HITL-MEM-Approval (risk rubric)"
  table** → same rule (identical across the four).

### Out of scope

- D1/D2/D3 (US-014.BOLT-001, Done); D5 (US-014.BOLT-002, Done).
- The identity-separation rules (handoff incoming-executor, G18/G24) — kept:
  the executing DEV approving the MEM is never AI self-approval, and after a
  handoff the *incoming* executor approves.
- The risk **rubric itself** as a risk-classification aid (examples, autonomy
  defaults, review-time budgets) — only the *approver counts* are removed, not
  the notion of risk class.
- The root `devflow/` tree (ADR-004).

---

## 5. Prerequisites and baseline

- US-014 approved; US-014.BOLT-003 approved (readiness); US-014.BOLT-001 Done.
- Four agents in sync before the edit; pre-existing drift → stop, reconcile.
- Baseline: branch `4.2`, HEAD `0c7f40d`.

---

## 6. Phases

### Phase A — §3.3 MEM approver rule

**Duration:** ~0.5h — **Complexity:** Medium

Replace the §3.3 risk-based min-approver table and its accompanying prose with
the single-approver rule: the executing Dev-validator approves the MEM (one
approver, any risk); after a recorded handoff, the incoming executor; QA/Sec/
domain reviewers optional. Preserve the risk *classification* (examples,
autonomy, budgets) — only the approver **count** changes.

**Files modified:** kit methodology §3.3 (table + prose at ~1625–1627 and ~2181–2186).

### Phase B — §3.0 owner cells (MEM, SPEC, UAT)

**Duration:** ~0.4h — **Complexity:** Low

MEM owner cell: the executing Dev-validator / incoming executor (drop the
risk-count clause). SPEC and UAT owner cells: state a minimum of one approver.

**Files modified:** kit methodology §3.0 checkpoint table.

### Phase C — GUARDRAILS + four agents

**Duration:** ~0.6h — **Complexity:** Medium

Rewrite the `GUARDRAILS.md` min-approver table and the four agents' min-approver
table to the single-approver rule (identical across the four agents).

**Files modified:** `GUARDRAILS.md`; the four agents.

### Phase D — Verification (GREEN)

Grep + four-agent parity + G-count + root check (§8).

---

## 7. Acceptance criteria

### AC-1: risk-based MEM approver counts removed
**Given** the edited kit, **When** grepping §3.3, GUARDRAILS and the four agents,
**Then** no "2 (… + QA *or* Sec)" / "3 (… + QA + Sec)" minimum-approver count
remains; the MEM approver rule is "the executing Dev-validator (incoming
executor after a handoff), one approver, any risk".

### AC-2: SPEC/UAT minimum one approver
**Given** the edited kit, **When** grepping the §3.0 SPEC and UAT owner cells,
**Then** each states a minimum of one approver.

### AC-3: identity rules preserved
**Given** the edited kit, **When** reading the handoff rule and G18/G24, **Then**
they are unchanged; the MEM is approved by the executing/incoming DEV, never AI
self-approval.

### AC-4: risk classification retained
**Given** the edited kit, **When** reading §3.3, **Then** risk class, its
examples, autonomy defaults and review-time budgets remain (only the approver
count was removed).

### AC-5: four-agent sync + G-count
Whole-body diff = sanctioned divergence only; G-count 39/39/39/39; GUARDRAILS 39.

### AC-6: root untouched
`git status` shows only `distribution-kit/` + governance records.

### AC-7: Bolt-manifest validation
0 errors.

### AC mapping to source

| US-014 AC | How satisfied | Evidence |
|-----------|---------------|----------|
| AC-4 (DEV approves the MEM; no risk multi-approver) | Phases A/B/C | AC-1, AC-3 |
| AC-5 (SPEC/UAT minimum one approver) | Phase B | AC-2 |
| AC-3 (high/critical MEM — count half) | Phase A | AC-1 |

---

## 8. Testing strategy

Deterministic, no runtime:
- Grep the removed counts (AC-1), the SPEC/UAT minimum-one (AC-2), the retained
  risk classification (AC-4).
- Confirm identity rules unchanged (AC-3).
- Four-agent whole-body diff + `grep -cE '^\| G[0-9]{2} '` = 39 (AC-5).
- `git status --short` (AC-6); manifest schema validation (AC-7).
- Edge cases: distinguish the *approver-count* rows (removed) from the *risk
  rubric* rows (kept — examples/autonomy/budgets); escaped pipes; CRLF/LF.

---

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | — | `n/a` — documentation-only |
| SAST / SBOM | — | `n/a` |
| Perf-smoke | — | `n/a` |
| Prompt-injection | — | `pass` |
| Secret-leak | — | `pass` |
| Hallucination lint | — | `pass` |
| IP / license | — | `n/a` |
| PII / DLP | — | `n/a` — internal |
| Dependency-confusion | — | `n/a` |
| Test-first evidence | — | `n/a` — not a BUG Bolt |
| Behavioral reproducibility | — | `pass` — deterministic grep/diff |
| Bolt-manifest validation | — | `pass` |

---

## 10. Security and data

Governance-routing text only; no security boundary or data path. Segregation of
duty is preserved by the **identity** rules (incoming-executor after handoff,
G18/G24), which are untouched — only the role/count *quorum* is removed. Data
`internal`.

---

## 11. Monitoring and observability

`n/a` — no runtime. The §8 suite is the observability; captured in the MEM.

---

## 12. Migration, compatibility and rollback

- **Migration:** none here; adopters receive it at their next §5.16 migration.
- **Compatibility:** risk class and its rubric stay; only the approver count is
  removed — no validator/consumer of risk class breaks. G-count unchanged.
- **Rollback:** revert the kit commit(s); root untouched.

---

## 13. Risk matrix

| Risk | Prob | Impact | Mitigation |
|------|------|--------|------------|
| Removing counts also removes the risk rubric by accident | 2 | 3 | Scope note: only the approver-count column/rows change; AC-4 verifies the rubric stays |
| A count survives in one location | 2 | 3 | AC-1 greps §3.3, GUARDRAILS and the four agents |
| Weakening segregation of duty | 2 | 3 | Identity rules (handoff, G18/G24) kept — AC-3 |
| Four-agent drift | 2 | 3 | Identical edits; AC-5 |
| Root edited | 1 | 4 | Kit-only; AC-6 |

---

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| The executing DEV approves the MEM (one approver, any risk) | Maintainer D7 — the DEV who takes the Bolt owns finishing it |
| Keep risk class + rubric (examples, autonomy, budgets) | Risk classification is still useful; only the mandatory approver *count* was the blocker |
| Keep the identity rules | They provide the real segregation of duty (incoming executor; no AI self-approval) — not a role count |
| SPEC/UAT minimum one | Consistency with the MEM rule; extra roles are guidance |

---

## 15. Stop conditions

- Pre-existing four-agent drift before Phase C → stop, reconcile, record.
- Any root `devflow/` methodology file in the diff → stop, revert, record.
- The edit would remove the risk classification itself (not just the count) → stop, reassess.
- A governed source changes materially (G15) → stop, revise, re-approve.

---

## 16. Definition of Done (DoD)

- [ ] Phases A–D implemented
- [ ] AC-1..AC-7 pass
- [ ] Verification GREEN (counts removed; SPEC/UAT min one; rubric retained; identity rules intact; sync 39×5; root untouched; manifest 0 errors)
- [ ] Follows ADR-004 (kit-only)
- [ ] Gates pass / n/a per §9
- [ ] MEM created (exactly one per V-Bounce)
- [ ] Manifest `v_bounces[]` entry appended
- [ ] HITL-MEM-Approval recorded

---

## 17. References

- US-014 (approved), US-014.BOLT-003 (approved), US-014.BOLT-001 (Done)
- AREV-001 F-03/F-07, REV-001 F-04/F-06
- ADR-004 (kit-only), AGENTS.md (four-agent sync)

---

## 18. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-22 | eugenio.serrano | Initial revision 1 (draft) |

---

## 19. HITL-SPEC-Approval

> **Avenga DevFlow §2.4.1, §3.0.** Draft until the Dev-validator records
> `HITL-SPEC-Approval`. Bolt approval authorizes SPEC preparation; **SPEC
> approval** authorizes the V-Bounce. A material source change invalidates
> this approval — stop, revise, re-approve (G15).

| Field | Value |
|-------|-------|
| **review.reviewers** | eugenio.serrano (dev_validator) |
| **review.decision** | approved |
| **review_ready_at** | `2026-08-22T01:41:34-03:00` |
| **review.started_at** | `2026-08-22T01:43:46-03:00` |
| **review.decided_at** | `2026-08-22T01:43:46-03:00` |
