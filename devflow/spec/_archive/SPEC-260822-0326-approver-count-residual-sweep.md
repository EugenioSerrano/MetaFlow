---
id: "SPEC-260822-0326"
title: "Remove the risk-based approver-count residuals from the kit (ADR-005 absence sweep) — BUG-002 fix"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
status: "approved"
origin: "BUG-002"
bolt: "US-000.BOLT-005"
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
review_ready_at: "2026-08-22T03:26:47-03:00"
review: # HITL-SPEC-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "dev_validator"}]
  started_at: "2026-08-22T03:28:50-03:00"
  decided_at: "2026-08-22T03:28:50-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "First ADR-005 application (absence form) approved: phrase family, full location set and the legitimate-homonym allowlist are declared; 22 fix-sites + 2 F-06.1 title alignments enumerated with target wording; allowlist protects the correct new rule, escalation examples, time-budget-per-risk wording and the autonomy column; AC-4 makes over-removal a failure; scope cleanly excludes 2682 (BUG-003/BOLT-006 territory). Authorizes the V-Bounce (kit-only, ADR-004)."
---

<!--
  LANGUAGE POLICY (§3.15): schema/headings English; prose content_language (en).
  BUG V-Bounce: RED/GREEN evidence is deterministic grep/diff (ADR-002 class 1),
  not an automated test suite. Kit-only edits (ADR-004); root untouched.
  First application of ADR-005 — the phrase family, location set and allowlist
  below are the ADR-005 contract for this sweep.
-->

# SPEC-260822-0326 — Remove the risk-based approver-count residuals (BUG-002, ADR-005 absence sweep)

| Field | Value |
|-------|-------|
| **Origin** | [BUG-002](../bugs/BUG-002-risk-based-approver-count-residuals.md) (approved) |
| **Bolt** | [US-000.BOLT-005](../functional/bolts/US-000.BOLT-005-approver-count-residual-sweep.md) (approved) |
| **ADRs** | [ADR-005](../adrs/ADR-005-removal-completeness-phrase-family-sweep.md) (sweep standard), [ADR-002](../adrs/ADR-002-documentation-defect-classification.md) (class 1), [ADR-004](../adrs/ADR-004-repository-partition-v2.md) (kit-only) |
| **Risk Class** | medium |
| **Revision** | 1 |

---

## 1. Context

**Why:** `US-014.BOLT-003` removed the risk-based approver counts and set the
single-approver rule ("one approver, at any risk; additional QA/Sec/domain
reviewers optional"). Its sweep verified only the two numeric tables it edited
(§3.3 min-approvers, GUARDRAILS MEM section) and missed the same rule living in
~20 other sites — including the four auto-loaded agents. AREV-003 confirmed this
as F-01 (🔴, release-blocking); it is BUG-002.

**What problem:** the kit contradicts itself about who approves the MEM. An
auto-loaded agent reading its own `HITL-MEM-Approval` table row (`+ QA/Sec per
risk`) will demand a QA/Sec sign-off the release abolished.

**If not done:** v4.2 ships a self-contradiction right after BUG-001 fixed the
same class of defect — the third occurrence of the partial-sweep pattern.

This is the **first application of ADR-005**: completeness is proven by a
phrase-family sweep over the fixed location set, phrased as an **absence**.

---

## 2. Source inventory and approval references (pre-SPEC evidence gate)

| Source | Ref | Approval |
|--------|-----|----------|
| BUG | `devflow/bugs/BUG-002-risk-based-approver-count-residuals.md` | HITL-BUG-Approval ✓ (2026-08-22) |
| Bolt | `devflow/functional/bolts/US-000.BOLT-005-approver-count-residual-sweep.md` | HITL-BOLT-READY-Approval ✓ |
| Evidence | AREV-003 F-01 (🔴), F-06.1 (⚠️) | approved Verdict ✓ |
| ADR | ADR-005 (sweep standard) | HITL-ADR-Approval ✓ (accepted) |
| ADR | ADR-002 (class 1), ADR-004 (kit-only) | accepted ✓ |
| Parent | `US-000-non-functional.md` | container (no approval) |
| Baseline | branch `4.2`, HEAD `c30a739` (kit working tree has the US-015 close, uncommitted) | — |

Pre-SPEC evidence gate: **all governed sources approved.** No draft/rejected/stale source.

---

## 3. ADR-005 sweep contract

### 3.1 Phrase family (the removed rule, all forms)

Grep **case-insensitive, multiline** (`rg -Ui` / `multiline`) for:

- Notation variants: `QA/Sec`, `QA *or* Sec`, `QA + Sec`, `QA/Sec/domain`
- Explicit conditionals: `for high/critical`, `for \`high\`/\`critical\``, `per risk`
- Count phrasings: `2 (executing Dev-validator + …)`, `3 (executing Dev-validator + …)`
- **Semantic paraphrases:** `as risk requires`, `as required by risk`, `QA *or* Security is added; for …, both`
- Stale table titles (F-06.1): `(risk rubric`, `Minimum approvers`, `Min approvers at HITL-MEM-Approval`

### 3.2 Location set (ADR-005 — swept in full regardless of where edits land)

Methodology `Avenga-DevFlow.md`; `GUARDRAILS.md`; the four agents (`CLAUDE.md`,
`SKILL.md`, `AvengaDevFlow.agent.md`, `AvengaDevFlow.md`) — tables **and** step
prose; `README.md`; `ONBOARDING.md`; `memory/TEMPLATE-MEM.md`;
`risks/TEMPLATE-RISK.md`; `risks/README.md`. (`INDEX.md`s and metrics schemas
swept for completeness — no expected hits.)

### 3.3 Sites to FIX (residuals — align to the single-approver rule)

| # | File:line | Current (residual) | Target |
|---|-----------|--------------------|--------|
| 1 | `Avenga-DevFlow.md:2730` | "…or other domain reviewers **as required by risk and scope**." | "…or other domain reviewers **optional at any risk** (one approver, any risk)." |
| 2 | `GUARDRAILS.md:30` | "Dev-validator who executed the Bolt **(+ QA/Sec/domain as risk requires)**" | "Dev-validator who executed the Bolt (one approver, any risk; QA/Sec/domain reviewers optional)" |
| 3 | `README.md:203` | "…approves the MEM at `HITL-MEM-Approval` **(+ QA/Sec for high/critical)**." | "…approves the MEM at `HITL-MEM-Approval` (QA/Sec/domain reviewers optional, any risk)." |
| 4 | `README.md:232` | "…**Dev-validator who executed the Bolt** (+ QA/Sec for high/critical); the agent never self-approves." | "…**Dev-validator who executed the Bolt** (QA/Sec/domain reviewers optional, any risk); the agent never self-approves." |
| 5 | `README.md:253` | "Dev-validator who executed the Bolt **(+ QA/Sec per risk)**" | "Dev-validator who executed the Bolt (one approver, any risk; QA/Sec/domain optional)" |
| 6 | `ONBOARDING.md:52` | "…signed by the Dev-validator who executed the Bolt **(+ QA/Sec for high/critical risk)**." | "…signed by the Dev-validator who executed the Bolt (QA/Sec/domain reviewers optional, any risk)." |
| 7 | `ONBOARDING.md:101` (FAQ) | "The Dev-validator who executed the Bolt — the same developer who took it. **For `high` risk, QA *or* Security is added; for `critical`, both.**" | "The Dev-validator who executed the Bolt — the same developer who took it. One approver at any risk; QA or Security may be added as optional reviewers, never required." |
| 8 | `TEMPLATE-MEM.md:233` | "Dev-validator who executed the Bolt, **+ QA/Sec for high/critical risk**)" | "Dev-validator who executed the Bolt; QA/Sec/domain reviewers optional, any risk)" |
| 9 | `TEMPLATE-MEM.md:246` | "**Reviewers (executing Dev-validator + QA/Sec for high/critical)**" | "**Reviewers (executing Dev-validator; QA/Sec/domain optional)**" |
| 10 | `TEMPLATE-MEM.md:247` | "dev_validator **(+ QA/Sec for high/critical)**" | "dev_validator (+ optional QA/Sec/domain reviewers)" |
| 11 | `TEMPLATE-RISK.md:77` | "high … **2 (executing Dev-validator + QA *or* Sec)**" | "high … **1 (the executing Dev-validator; QA/Sec optional)**" |
| 12 | `TEMPLATE-RISK.md:78` | "critical … **3 (executing Dev-validator + QA + Sec)**" | "critical … **1 (the executing Dev-validator; QA/Sec optional)**" |
| 13 | `risks/README.md:118` | "**high** … 2 (executing Dev-validator + QA *or* Sec)" | "**high** … 1 (the executing Dev-validator; QA/Sec optional)" |
| 14 | `risks/README.md:119` | "**critical** … 3 (executing Dev-validator + QA + Sec)" | "**critical** … 1 (the executing Dev-validator; QA/Sec optional)" |
| 15–18 | four agents `:401/418/446/429` (HITL-MEM row) | "…after a recorded handoff **(+ QA/Sec per risk)**" | "…after a recorded handoff (one approver, any risk; QA/Sec/domain optional)" |
| 19–22 | four agents `:307/324/352/335` (V-Bounce step 8) | "…outgoing executor, incoming executor, reason) **(+ QA/Sec for high/critical)**." | "…outgoing executor, incoming executor, reason). QA/Sec/domain reviewers optional, any risk." |

### 3.4 F-06.1 — stale titles over the now-all-`1` table (fold in)

| # | File:line | Current | Target |
|---|-----------|---------|--------|
| 23 | four agents `### Minimum approvers at HITL-MEM-Approval (risk rubric, §3.3)` (`421/438/466/449`) | "**(risk rubric, §3.3)**" | "(§3.3 — one approver at any risk)" — drop "risk rubric" |
| 24 | `Avenga-DevFlow.md:2179` + `TEMPLATE-RISK.md:73` + `risks/README.md:114` | table column header "Min approvers at HITL-MEM-Approval" over rows now all `1` | keep the column (the **autonomy** column still varies by risk) but ensure every "Min approvers" cell reads `1`; no header change needed beyond the cell fixes in 11–14 |

### 3.5 ALLOWLIST — legitimate homonyms, DO NOT TOUCH (ADR-005 §3(3))

| File:line | Text | Why it stays |
|-----------|------|--------------|
| `Avenga-DevFlow.md:1398` | §3.0 table HITL-MEM row: "(one approver, any risk; additional QA/Sec/domain reviewers optional)" | This is the **correct new rule** — the target, not a residual |
| `GUARDRAILS.md:380` | "one approver, at any risk — there is no risk-based approver count; QA/Sec/domain reviewers are optional" | The correct new rule |
| `Avenga-DevFlow.md:2160` | "A pure approver-level escalation (e.g. adding QA/Sec to the approval)…" | Escalation **example** of a control, not a required count (AREV-003 F-06.2) |
| `Avenga-DevFlow.md:2682` | HITL-SPEC "Who": "QA/Security/Data specialists when required by risk or affected domain" | Different checkpoint (SPEC), and it is **BUG-003 / BOLT-006** territory, not BUG-002 |
| `GUARDRAILS.md:342` · `CLAUDE.md:410` + agents `Review-time budgets … per risk_class` · `CLAUDE.md:290` + agents Sizing "review budget per risk_class" | Review **time budgets** genuinely vary by risk_class | A legitimate, unchanged concept — time budget, not approver count |
| `TEMPLATE-RISK.md:68` · `risks/README.md:123` | "risk_class … escalated at any subsequent review (QA/Sec); can never be reduced…" | Risk-**class escalation** concept (who may escalate the risk), not the approver count |
| `TEMPLATE-RISK.md:73` · `risks/README.md:114` · `Avenga-DevFlow.md:2179` `Default autonomy` column | Autonomy L3/L2/L1 **does** vary by risk | Keep the table; only the min-approvers cells change |

> Over-removing any allowlist entry is a **failure** of this V-Bounce, not a
> success (ADR-005 §3(3)). The GREEN sweep must show these still present.

---

## 4. Phases

### Phase A — Methodology + GUARDRAILS (sites 1, 2, 24-partial)
Fix `Avenga-DevFlow.md:2730` and `GUARDRAILS.md:30`; confirm `1398` and `380`
(the correct rule) untouched. **~0.5h.**

### Phase B — Four agents (sites 15–22, 23) — identical edits
Fix the HITL-MEM row and step-8 prose in all four; drop "(risk rubric)" from the
section titles. Whole-body diff must stay sanctioned-divergence-only. **~0.5h.**

### Phase C — README + ONBOARDING (sites 3–7)
Fix the three README MEM bullets and the two ONBOARDING locations. **~0.5h.**

### Phase D — Templates (sites 8–14)
Fix `TEMPLATE-MEM.md` (3 sites) and the `TEMPLATE-RISK.md` / `risks/README.md`
count-table cells (high→1, critical→1). **~0.5h.**

### Phase E — Verification (GREEN, §7)
Absence sweep, allowlist presence, four-agent sync, G-count, root check.

---

## 5. Acceptance criteria

- **AC-1 (absence):** the §3.1 phrase family returns **zero residual matches**
  across the §3.2 location set, outside the §3.5 allowlist. Specifically: no
  `+ QA/Sec per risk`, `+ QA/Sec for high/critical`, `QA/Sec/domain as risk
  requires`, `as required by risk and scope` (in a MEM-approver context), count
  cells `2`/`3`, or "For high risk, QA or Security is added; for critical, both".
- **AC-2 (single-approver rule present):** every site in §3.3 now states the
  single-approver rule; the four agents' HITL-MEM row **and** step 8 agree with
  each other and with §3.0 table line 1398.
- **AC-3 (F-06.1):** no agent section title reads "(risk rubric)"; every
  min-approvers cell reads `1`.
- **AC-4 (allowlist intact):** every §3.5 entry still present (the correct rule,
  the escalation examples, the review-time-budget-per-risk wording, the autonomy
  column, the risk-escalation concept). Over-removal fails this AC.
- **AC-5 (four-agent sync + G-count):** whole-body diff = sanctioned divergence
  only; `grep -cE '^\| G[0-9][0-9] '` = **39** in GUARDRAILS and each agent.
- **AC-6 (root untouched):** `git status` shows only `distribution-kit/` files +
  governance records; no root `devflow/` methodology file changed (ADR-004).
- **AC-7 (manifest):** BOLT-005 manifest validates; `v_bounces[0]` appended.

---

## 6. Test / evidence strategy

Deterministic, no runtime (ADR-002 class 1):
- **RED:** the §2 inventory of BUG-002 — the residual matches present pre-fix
  (already captured; the reproduction evidence).
- **GREEN:** post-fix re-run of the §3.1 sweep → zero residuals; allowlist
  presence sweep → all present; four-agent diff; G-count; `git status`.
- Record RED and GREEN separately in the MEM.

---

## 7. Quality gates

| Gate | Status |
|------|--------|
| Unit / integration / SAST / SBOM / perf / IP / PII / dep-confusion | `n/a` — documentation-only, internal |
| Test-first evidence | `n/a` — not an automated-test BUG; RED/GREEN is grep (ADR-002 class 1) |
| Prompt-injection / secret-leak | `pass` |
| Hallucination-lint | `pass` — every §-ref/path resolves post-edit |
| Behavioral-reproducibility | `pass` — deterministic grep/diff |
| Bolt-manifest-validation | `pass` |

---

## 8. Migration, compatibility, rollback

- **Migration:** none; adopters receive it at the next §5.16 migration.
- **Compatibility:** semantics unchanged — the single-approver rule was already
  the governing one (§3.3 table); this removes the contradicting copies. G-count
  stays 39; four-agent sync preserved.
- **Rollback:** revert the kit commit; root untouched.

---

## 9. Risks and stop conditions

| Risk | Mitigation |
|------|------------|
| Missed residual (partial sweep #4) | ADR-005 sweep over the full §3.2 set; AC-1 is an absence assertion, not a spot check |
| Over-removal of a legitimate mention | §3.5 allowlist with per-entry reason; AC-4 asserts presence |
| Four-agent drift | Identical edits; AC-5 diff + G-count |
| Root edited | Kit-only; AC-6 `git status` |

**Stop conditions:** a residual cannot be reworded without changing meaning →
stop, record, ask. Any root `devflow/` methodology file in the diff → stop,
revert, record. Turn budget exhausted before GREEN → stop, MEM with progress,
resume as a new V-Bounce.

---

## 10. Definition of Done

- [ ] Phases A–E done · AC-1..AC-7 pass
- [ ] GREEN sweep (zero residuals; allowlist intact; sync 39×5; root untouched)
- [ ] Follows ADR-005 (sweep contract) + ADR-004 (kit-only)
- [ ] MEM created (RED/GREEN recorded separately) · manifest `v_bounces[]` appended
- [ ] HITL-MEM-Approval recorded

---

## 11. HITL-SPEC-Approval

> Draft until the Dev-validator records `HITL-SPEC-Approval`. A material source
> change invalidates it — stop, revise, re-approve (G15).

| Field | Value |
|-------|-------|
| **review.reviewers** | eugenio.serrano (dev_validator) |
| **review.decision** | **approved** |
| **review_ready_at** | `2026-08-22T03:26:47-03:00` |
| **review.started_at** | `2026-08-22T03:28:50-03:00` |
| **review.decided_at** | `2026-08-22T03:28:50-03:00` |
