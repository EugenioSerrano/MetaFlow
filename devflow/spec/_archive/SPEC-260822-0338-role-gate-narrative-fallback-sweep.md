---
id: "SPEC-260822-0338"
title: "Add the no-holder fallback to the §3.0 checkpoint narrative and TC route texts (ADR-005 positive-coverage sweep) — BUG-003 fix"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
status: "approved"
origin: "BUG-003"
bolt: "US-000.BOLT-006"
revision: 1
associated_adrs:
  - "devflow/adrs/ADR-005-removal-completeness-phrase-family-sweep.md"
  - "devflow/adrs/ADR-002-documentation-defect-classification.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
prerequisites: []
risk_class: "medium"
autonomy_level: "L3"
turn_budget: ""
data_classification: "internal"
review_ready_at: "2026-08-22T03:38:40-03:00"
review: # HITL-SPEC-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "dev_validator"}]
  started_at: "2026-08-22T03:40:33-03:00"
  decided_at: "2026-08-22T03:40:33-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Second ADR-005 application (positive-coverage form) approved: 9 route statements enumerated, canonical clause declared, allowlist protects the role-agnostic DISC/REV/AREV bullets and the just-fixed HITL-MEM. Authorizes the V-Bounce (kit-only, ADR-004)."
---

<!--
  LANGUAGE POLICY (§3.15): schema/headings English; prose content_language (en).
  BUG V-Bounce (ADR-002 class 1): RED/GREEN = deterministic grep. Kit-only
  (ADR-004); root untouched. Second application of ADR-005 — positive-coverage
  form ("every route statement carries the clause"), not absence.
-->

# SPEC-260822-0338 — No-holder fallback in the §3.0 narrative + TC route texts (BUG-003, ADR-005 positive-coverage sweep)

| Field | Value |
|-------|-------|
| **Origin** | [BUG-003](../bugs/BUG-003-role-gate-residuals-in-checkpoint-narrative.md) (approved) |
| **Bolt** | [US-000.BOLT-006](../functional/bolts/US-000.BOLT-006-role-gate-narrative-fallback-sweep.md) (approved) |
| **ADRs** | [ADR-005](../adrs/ADR-005-removal-completeness-phrase-family-sweep.md), [ADR-002](../adrs/ADR-002-documentation-defect-classification.md), [ADR-004](../adrs/ADR-004-repository-partition-v2.md) |
| **Risk Class** | medium |
| **Revision** | 1 |

---

## 1. Context

**Why:** `US-014.BOLT-001` (D1/D3) made role routing guidance, not a gate, by
adding the no-holder fallback to every single-role approval route. The sweep
reached the §3.0 **table** but not the §3.0 **normative narrative**, which still
states the named role unconditionally for 7 checkpoints (BUG-003, AREV-003 F-02
widened by the ADR-005 sweep).

**Problem:** §3.0 defines each checkpoint; a reader of the narrative concludes
only the named role may approve — the exact gate US-014 removed, defeating
single-operator operability (the release's headline change) for narrative
readers. The narrative contradicts its own table.

**If not done:** v4.2 ships with its normative checkpoint definitions still
gating on named roles.

Second application of **ADR-005**, in **positive-coverage** form: assert every
route statement *carries* the clause (not that a removed string is absent).

---

## 2. Source inventory (pre-SPEC evidence gate)

| Source | Ref | Approval |
|--------|-----|----------|
| BUG | BUG-003 | HITL-BUG-Approval ✓ |
| Bolt | US-000.BOLT-006 | HITL-BOLT-READY-Approval ✓ |
| Evidence | AREV-003 F-02 (🔶) | approved Verdict ✓ |
| ADR | ADR-005, ADR-002, ADR-004 | accepted ✓ |
| Baseline | branch `4.2`; kit working tree has US-015 close + BOLT-005 fix (uncommitted) | — |

Pre-SPEC evidence gate: **all governed sources approved.**

---

## 3. ADR-005 sweep contract (positive-coverage)

### 3.1 Coverage sweep
Enumerate every text that states who records a HITL checkpoint
(`grep -nA3 '**Who:**'` in §3.0 + the §2.6.1 lifecycle text + TEMPLATE-TC §10),
then assert each **carries the fallback clause** (or an explicit reference).

### 3.2 The clause (canonical wording)
> "If the named role has no holder, the available qualified human records the
> approval, noting the self-assigned role (role routing is guidance, not a gate)."

Appended concisely to each route statement, consistent with the §3.0 table rows
(which already carry the equivalent clause — positive control: 7 present).

### 3.3 Sites to FIX (9 — add the clause)

| # | Site | Current (gate) |
|---|------|----------------|
| 1 | `Avenga-DevFlow.md` §3.0 HITL-US `~2620` | "**Who:** Functional Analyst." |
| 2 | §3.0 HITL-BUG `~2630` (functional route only) | "Functional Analyst for a functional BUG" (the non-functional route is already relaxed — leave it) |
| 3 | §3.0 HITL-TC `~2644` | "QA plus a Functional Analyst or delegated business-domain owner…" |
| 4 | §3.0 HITL-BOLT-READY `~2658` | "Functional Analyst for a functional Bolt; Architect or Tech Lead…" |
| 5 | §3.0 HITL-ADR `~2670` | "**Who:** Architect or Tech Lead." |
| 6 | §3.0 HITL-SPEC `~2680` | "Dev-validator plus the applicable domain owner(s)…" |
| 7 | §3.0 HITL-BOLT-DONE `~2746` | "PO / PM for functional Bolts; routed technical owner…" |
| 8 | §2.6.1 lifecycle `~836-838` | "Functional expected results require QA review plus Functional Analyst…" |
| 9 | `TEMPLATE-TC.md` §10 `~113-114` | "QA plus the Functional Analyst/domain owner…" |

### 3.4 DO NOT TOUCH (allowlist — already correct)

| Site | Why |
|------|-----|
| §3.0 DISC/REV/AREV bullets (`~2691/2699/2705/2711/2717`) "Qualified human designated for…" | Role-agnostic by construction — no named-role gate |
| §3.0 HITL-MEM `~2729` "the Dev-validator who executed the Bolt — one approver at any risk…" | Just corrected by BOLT-005; the executor is not an availability gate |
| The §3.0 **table** rows (7) already carrying the clause | Positive control — the target pattern, not a defect |

> Over-editing the role-agnostic bullets is a failure (ADR-005 §3(3)).

---

## 4. Phases

- **Phase A — §3.0 narrative:** add the clause to the 7 checkpoint bullets
  (sites 1–7); leave DISC/REV/AREV and HITL-MEM untouched. ~0.75h.
- **Phase B — §2.6.1 + TEMPLATE-TC:** sites 8–9. ~0.25h.
- **Phase C — Verification (GREEN, §6).**

> Four agents: the §3.0 checkpoint narrative lives in the **methodology**, not
> in the agent files (the agents carry the checkpoint **table**, already correct
> from US-014.BOLT-001). Phase C confirms the agents are **not** disturbed and
> stay byte-synced (G-count 39×5). If any agent is found to carry the same
> narrative, it is swept identically.

---

## 5. Acceptance criteria

- **AC-1 (coverage):** each of the 9 sites carries the fallback clause (or an
  explicit reference); a `grep` over the §3.0 "Who" bullets + §2.6.1 +
  TEMPLATE-TC shows **no named-role route without the clause**.
- **AC-2 (allowlist intact):** the DISC/REV/AREV bullets and HITL-MEM are
  unchanged; the role-agnostic wording is preserved (over-edit = fail).
- **AC-3 (narrative agrees with table):** every §3.0 narrative route now matches
  its table row on role-as-guidance.
- **AC-4 (four-agent sync + G-count):** agents byte-synced; `grep -cE '^\| G[0-9][0-9] '` = 39 in GUARDRAILS + each agent.
- **AC-5 (root untouched):** `git status` = only `distribution-kit/` + governance records.
- **AC-6 (manifest):** BOLT-006 manifest validates; `v_bounces[0]` appended.

---

## 6. Test / evidence strategy

Deterministic (ADR-002 class 1):
- **RED:** the BUG-003 §2 positive-coverage inventory — 9 route statements without the clause vs 7 table rows with it.
- **GREEN:** post-fix — all 9 carry the clause; DISC/REV/AREV + HITL-MEM unchanged; G-count 39×5; `git status`.
- RED and GREEN recorded separately in the MEM.

---

## 7. Quality gates

Documentation-only/internal/not an automated-test BUG → unit/integration,
SAST/SBOM, perf, IP, PII, dep-confusion, test-first: `n/a`. Prompt-injection,
secret-leak, hallucination-lint, behavioral-reproducibility,
bolt-manifest-validation: `pass`.

---

## 8. Migration, compatibility, rollback

Migration none (next §5.16). Compatibility: semantics unchanged — the fallback
was already governing via the table; this aligns the narrative. G-count 39;
sync preserved. Rollback: revert the kit commit; root untouched.

---

## 9. Risks and stop conditions

| Risk | Mitigation |
|------|------------|
| Missed route statement | ADR-005 coverage sweep over the full enumeration; AC-1 |
| Over-edit of a role-agnostic bullet | §3.4 allowlist; AC-2 |
| Four-agent drift | Methodology-only edit; AC-4 diff + G-count |
| Root edited | Kit-only; AC-5 |

**Stop:** a bullet cannot take the clause without changing meaning → stop, ask.
Root file in the diff → stop, revert. Turn budget exhausted → stop, MEM, resume.

---

## 10. Definition of Done

- [ ] Phases A–C · AC-1..AC-6 pass
- [ ] GREEN (9 sites carry the clause; allowlist intact; sync 39×5; root untouched)
- [ ] ADR-005 (positive-coverage) + ADR-004 (kit-only) followed
- [ ] MEM (RED/GREEN separate) · manifest `v_bounces[]` appended
- [ ] HITL-MEM-Approval recorded

---

## 11. HITL-SPEC-Approval

> Draft until the Dev-validator records `HITL-SPEC-Approval`. Material source change → stop, revise, re-approve (G15).

| Field | Value |
|-------|-------|
| **review.reviewers** | eugenio.serrano (dev_validator) |
| **review.decision** | **approved** |
| **review_ready_at** | `2026-08-22T03:38:40-03:00` |
| **review.started_at** | `2026-08-22T03:40:33-03:00` |
| **review.decided_at** | `2026-08-22T03:40:33-03:00` |
