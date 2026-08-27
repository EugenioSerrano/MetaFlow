---
id: "BUG-002"
title: "Risk-based approver-count residuals: the removed rule survives in 8+ kit locations (self-contradiction)"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-sonnet-4-5"
severity: "high"
nature: "non-functional"
status: "closed"
owner: "eugenio.serrano"
detected_in: "arev"
detected_at: "2026-08-22T02:53:30-03:00"
incident_ref: ""
affected_artifacts:
  - "distribution-kit/CLAUDE.md"
  - "distribution-kit/.agents/skills/avenga-devflow/SKILL.md"
  - "distribution-kit/.github/agents/AvengaDevFlow.agent.md"
  - "distribution-kit/.opencode/agents/AvengaDevFlow.md"
  - "distribution-kit/devflow/GUARDRAILS.md"
  - "distribution-kit/devflow/README.md"
  - "distribution-kit/devflow/ONBOARDING.md"
  - "distribution-kit/devflow/memory/TEMPLATE-MEM.md"
  - "distribution-kit/devflow/risks/TEMPLATE-RISK.md"
  - "distribution-kit/devflow/risks/README.md"
expected_result: "The single-approver rule approved in US-014.BOLT-003 ('one approver, at any risk; additional QA/Sec/domain reviewers optional') is coherent across the entire kit — methodology, GUARDRAILS, the four agents, READMEs, templates — with zero traces of the removed risk-based approver-count rule."
actual_result: "The removed rule ('For `high` risk, QA *or* Security is added; for `critical`, both'; count tables `2`/`3`) survives as active instruction in 8+ locations: the four auto-loaded agents (HITL-MEM row + V-Bounce step 8), README ×3, ONBOARDING (FAQ + prose), TEMPLATE-MEM, TEMPLATE-RISK + risks/README (count tables), GUARDRAILS checkpoint-map row. The kit contradicts itself."
bolt: "US-000.BOLT-005"
spec: "SPEC-260822-0326"
mem: "MEM-260822-0332"
sources:
  - "devflow/adversarial-reviews/AREV-003-v42-close-removal-traces-sweep/03-VERDICT.md"
review_ready_at: "2026-08-22T03:07:37-03:00"
review:
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "developer"}]
  started_at: "2026-08-22T03:09:32-03:00"
  decided_at: "2026-08-22T03:09:32-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "BUG confirmed: the residuals were independently reproduced three times (AREV-003 Challenger, Defender and Judge) with deterministic grep evidence at file:line, and the Verdict confirmed F-01 as release-blocking. Classification correct (ADR-002 class 1, non-functional, severity high — documentation self-contradiction, no runtime or data impact). Non-functional route at severity high: any team member, author included (G29). Authorizes exactly one dedicated Bolt under US-000."
tags: ["adr-002-class-1", "partial-sweep-pattern", "self-contradiction"]
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs, and section
  headings (##) stay in English (the schema). All prose — descriptions,
  root cause analysis, reproduction steps — goes in the project's
  content_language (en, declared in devflow/LANGUAGE).

  ⚠️ BUG lifecycle (§2.16, §3.3.1): this BUG remains DRAFT until
  HITL-BUG-Approval. Only then may its EXACTLY ONE dedicated Bolt be
  created (non-functional → US-000). The fix uses strict TDD inside ONE
  V-Bounce. The BUG never authorizes code by itself.
-->

# BUG-002 — Risk-based approver-count residuals (kit self-contradiction)

| Field              | Value |
|--------------------|-------|
| **Severity**       | high |
| **Nature**         | non-functional (documentation defect — ADR-002 class 1) |
| **Detected in**    | arev (AREV-003 — v4.2 close removal-traces sweep) |
| **Status**         | draft |
| **Affected files** | Four agents (CLAUDE.md, SKILL.md, AvengaDevFlow.agent.md, AvengaDevFlow.md), GUARDRAILS.md, README.md, ONBOARDING.md, TEMPLATE-MEM.md, TEMPLATE-RISK.md, risks/README.md |
| **Dedicated Bolt** | [US-000.BOLT-005](../functional/bolts/US-000.BOLT-005-approver-count-residual-sweep.md) (candidate — pending `HITL-BOLT-READY-Approval`) |

## 1. Summary

The risk-based approver-count rule that US-014.BOLT-003 removed ("For `high`
risk, QA *or* Security is added; for `critical`, both") still lives as active
instruction in 8+ locations across `distribution-kit/`, including the four
auto-loaded agent files. The kit contradicts itself about who approves the MEM
— §3.3 and GUARDRAILS MEM section say "one approver, at any risk", while the
agents' HITL-MEM row, ONBOARDING FAQ, TEMPLATE-MEM, TEMPLATE-RISK and
risks/README say QA/Sec are required at high/critical risk.

## 2. Reproduction

Deterministic grep/diff (ADR-002 class 1):

1. Read `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md` §3.3
   min-approvers table (lines ~2179–2184): all rows show `1 (the executing
   Dev-validator)`.
2. Read `distribution-kit/devflow/GUARDRAILS.md` MEM section (lines ~377–387):
   states "one approver, at any risk; additional QA/Sec/domain reviewers
   optional".
3. Grep the phrase family `QA/Sec per risk`, `QA/Sec for high/critical`,
   `QA *or* Sec`, `QA + Sec`, `per risk`, across `distribution-kit/`:
   ```
   CLAUDE.md:307, 401
   SKILL.md:324, 418
   AvengaDevFlow.agent.md:352, 446
   AvengaDevFlow.md:335, 429
   GUARDRAILS.md:30
   README.md:203, 232, 253
   ONBOARDING.md:52, 101
   TEMPLATE-MEM.md:233, 246, 247
   TEMPLATE-RISK.md:77–78
   risks/README.md:118–119
   ```
4. Read any of those locations: the removed rule is present verbatim (the RISK
   tables even state hard counts `2`/`3`).

**Expected result:** zero occurrences of the removed rule; the single-approver
rule in every location that describes MEM approval (the four agents' HITL-MEM
row and V-Bounce step 8, README, ONBOARDING, templates, GUARDRAILS map row).

**Actual result:** the removed rule survives as active instruction in 8+
carriers, four of them auto-loaded agent files. An agent reading its own table
will demand QA/Sec sign-off the release explicitly abolished.

## 3. Root cause

US-014.BOLT-003's completion criterion stated "no risk-based count survives"
and "the four agents' risk/approver tables are consistent". The sweep updated
the numeric min-approver tables (methodology §3.3, GUARDRAILS MEM section) and
the agents' *risk-rubric* tables (all rows → `1`), verified those two
locations, and declared completion. It did **not** extend the phrase-family
grep (`QA/Sec`, `QA *or* Sec`, `QA + Sec`, `per risk`, `high/critical`) to:
- The four agents' HITL-checkpoint **row** prose and V-Bounce step **prose**
- README / ONBOARDING prose
- TEMPLATE-MEM / TEMPLATE-RISK / risks/README prose and count tables
- GUARDRAILS checkpoint-**map** row

Same failure mode as AREV-001 → BUG-001: a removal sweep that passes its own
narrow acceptance grep (the locations it edited) while leaving the removed
text active in the locations the grep never covered. This is the **third**
occurrence of the partial-sweep pattern — systemic, not incidental.

## 4. Impact

- **Users affected:** all adopters of the v4.2 kit; the four agent files are
  auto-loaded, so every agent execution reads the contradicting rule.
- **Data impact:** none (documentation defect, no runtime data).
- **Workaround available:** an adopter reading both the §3.3 table and an
  agent's HITL row sees the contradiction and must guess which one governs. No
  clean workaround — the kit must be corrected.
- **Release impact:** AREV-003 Verdict classified this as **release-blocking**
  (🔴). The v4.2 close cannot proceed until the fix is Done.

## 5. Classification and routing

| Aspect | Value |
|--------|-------|
| **Nature** | non-functional → Architect/Tech Lead approves if `severity: critical`, otherwise any team member, this BUG's author included, approves (G29) |
| **Violated expectation** | US-014.BOLT-003 (approved) removed the risk-based approver counts and established the single-approver rule across the kit; ADR-002 class 1 (kit self-contradiction with deterministic grep/diff evidence) |
| **Dedicated Bolt parent** | US-000-non-functional.md |

## 6. Fix status (strict TDD, ONE V-Bounce)

| Stage | Evidence | Status |
|-------|----------|--------|
| Reproduction test | Deterministic grep (AREV-003 F-01 evidence already reproduced by Challenger + Defender + Judge independently) | GREEN (defect confirmed) |
| Production fix | Grep the full phrase family across ALL kit files; rewrite every carrier to the single-approver rule; fold in AREV-003 F-02 (TC fallback) + F-06 (titles); preserve F-06.2 legitimate mentions. Verify four-agent sync + G-count 39. | Pending |
| MEM | MEM-YYMMDD-HHmm — records reproduction evidence (grep) and green evidence (post-fix grep clean) | Pending |

> **Note (BUG-specific):** this BUG's "reproduction test" is deterministic
> grep/diff evidence (ADR-002 class 1), not an automated test suite. The
> "RED" phase is the grep showing the residuals; the "GREEN" phase is the
> post-fix grep showing zero matches. Both are recorded in the MEM.

## 7. Relations

| Type | ID | Relation |
|------|----|----------|
| Origin | AREV-003 | [AREV-003 F-01](../adversarial-reviews/AREV-003-v42-close-removal-traces-sweep/03-VERDICT.md) — confirmed 🔴 finding (FAIL verdict) |
| Incomplete removal | US-014.BOLT-003 | [US-014.BOLT-003-no-risk-based-approver-counts.md](../functional/bolts/US-014.BOLT-003-no-risk-based-approver-counts.md) — the removal Bolt whose sweep was incomplete (Done; its MEM is immutable history — this BUG's fix is a separate Bolt) |
| Sibling pattern | BUG-001 | [BUG-001-stale-bug-route-copies.md](BUG-001-stale-bug-route-copies.md) — same partial-sweep root cause (AREV-001 finding → fixed via US-000.BOLT-004) |
| Classification | ADR-002 | [ADR-002-documentation-defect-classification.md](../adrs/ADR-002-documentation-defect-classification.md) — class 1 (kit self-contradiction, deterministic evidence) |

## 8. HITL-BUG-Approval

> **Avenga DevFlow §2.16, §3.0.** This BUG remains DRAFT until a qualified
> human records `HITL-BUG-Approval` (in the `review` frontmatter block):
> non-functional → Architect/Tech Lead if `severity: critical`, otherwise any
> team member, this BUG's author included (G29). Only after approval may the
> dedicated Bolt be created. The BUG never authorizes code by itself.

| Field | Value |
|-------|-------|
| **Approver** | eugenio.serrano (any team member, author included — severity `high`, G29) |
| **Role** | developer |
| **Decision** | approved |
| **review_ready_at** | `2026-08-22T03:07:37-03:00` |
| **review.started_at** | `2026-08-22T03:09:32-03:00` |
| **review.decided_at** | `2026-08-22T03:09:32-03:00` |
| **Authorizes** | Exactly one dedicated **non-functional Bolt under US-000** |
