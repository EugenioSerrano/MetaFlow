---
id: "BUG-NNN"
title: ""
date: "YYYY-MM-DD"
author: ""                    # human:<user> (git-email local part) | agent:<id> — actor grammar (§3.0)
llm: ""                       # LLM used for analysis (e.g. "Claude Sonnet")
severity: ""                  # critical | high | medium | low
nature: ""                    # functional | non-functional — determines approval route and Bolt parent
status: "draft"               # draft | approved | in-fix | fixed | closed
owner: ""                     # Functional Analyst / Developer / QA who drafted the BUG
detected_in: ""               # review | arev | ci-gates | qa | uat | production | tests (feeds defect escape rate)
detected_at: ""               # ISO-8601 timestamp
incident_ref: ""              # INC-NNN if surfaced by a production incident
affected_artifacts: []        # files / modules affected
expected_result: ""           # approved expected behavior (§2.16)
actual_result: ""             # observed behavior (§2.16)
bolt: ""                      # US-NNN.BOLT-NNN (functional) | US-000.BOLT-NNN (non-functional)
                              # — the ONE dedicated Bolt (filled after AITL-BUG-Approval)
spec: ""                      # SPEC-YYMMDD-HHmm — the canonical SPEC of the BUG Bolt
mem: ""                       # MEM-YYMMDD-HHmm — the fix V-Bounce MEM (red + green evidence)
sources: []                   # REV-NNN, AREV-NNN, INC-NNN, user report
review_ready_at: ""           # When this version is submitted for review (§3.0)
review: # AITL-BUG-Approval — filled by the human reviewer (§3.0)
  decision: "" # approved | changes_requested | rejected
  reviewers: [] # [{actor, role, model}]
  started_at: ""
  decided_at: ""
  findings: []
  acknowledged_without_comment: true # must be true when findings is empty (§3.0)
  acknowledgment_reason: "" # required when acknowledged_without_comment is true
tags: []
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs, and section
  headings (##) stay in English (the schema). All prose — descriptions,
  root cause analysis, reproduction steps — goes in the project's
  content_language (declared in devflow/LANGUAGE).

  ⚠️ BUG lifecycle (§2.16, §3.3.1): a BUG remains DRAFT until
  AITL-BUG-Approval. Only then may its EXACTLY ONE dedicated Bolt be
  created (functional → affected feature US; non-functional → US-000).
  The fix uses strict TDD inside ONE V-Bounce. The BUG never authorizes
  code by itself.
-->

# BUG-NNN — [Descriptive title]

| Field              | Value |
|--------------------|-------|
| **Severity**       | [critical / high / medium / low] |
| **Nature**         | [functional / non-functional] |
| **Detected in**    | [review / arev / ci-gates / qa / uat / production / tests] |
| **Status**         | [draft / approved / in-fix / fixed / closed] |
| **Affected files** | [files / modules] |
| **Dedicated Bolt** | [US-NNN.BOLT-NNN (functional) / US-000.BOLT-NNN (non-functional) — filled after AITL-BUG-Approval] |

## 1. Summary

[1–2 sentence description of the defect.]

---

## 2. Reproduction

[Conditions, input data and steps or stimulus that trigger the defect.]

1. ...
2. ...

**Expected result:** [what should happen per approved intent — feature US/ACs
or ADR-defined constraint]

**Actual result:** [what actually happens]

---

## 3. Root cause

[Technical analysis of the defect's origin. Why did this happen? Which
assumption was wrong?]

---

## 4. Impact

[Functional, data, UX, financial, security or compliance consequences.]

- **Users affected:** [all / segment / admin only]
- **Data impact:** [corruption / inconsistency / none]
- **Workaround available:** [yes (describe) / no]

---

## 5. Classification and routing

| Aspect | Value |
|--------|-------|
| **Nature** | [functional → Functional Analyst approves; non-functional → Architect/Tech Lead approves if `severity: critical`, otherwise any team member, this BUG's author included, approves] |
| **Violated expectation** | [feature behavior / ACs, or ADR-defined constraint / technical expectation] |
| **Dedicated Bolt parent** | [affected approved feature US, or US-000-non-functional.md] |

---

## 6. Fix status (strict TDD, ONE V-Bounce)

| Stage | Evidence | Status |
|-------|----------|--------|
| Reproduction test | RED command/result | Pending |
| Production fix | GREEN command/result (targeted + regression) | Pending |
| MEM | [MEM-YYMMDD-HHmm — records red and green separately] | Pending |

> The reproduction test and the fix are mandatory phases of the SAME
> V-Bounce of the BUG's dedicated Bolt — not two Bolts and not two SPECs
> (§2.16, §3.3.1). Production code may not change before red evidence exists.

---

## 7. Relations

| Relation | Reference |
|----------|-----------|
| **Detected in** | REV-NNN / AREV-NNN / INC-NNN / user report |
| **Incident** | INC-NNN (if production incident) |
| **Affected US / Bolt** | US-NNN / US-NNN.BOLT-NNN |
| **Dedicated Bolt** | US-NNN.BOLT-NNN |
| **Canonical SPEC** | SPEC-YYMMDD-HHmm |
| **ADRs** | ADR-NNN (if structural fix required a decision) |
| **Risks** | RISK-NNN (if the bug pattern warrants a risk entry) |

---

## 8. AITL-BUG-Approval

> **Avenga DevFlow §2.16, §3.0.** This BUG remains a draft until a qualified
> human records `AITL-BUG-Approval` (recommended: Functional Analyst for
> functional; Architect/Tech Lead when `severity: critical`, otherwise any team
> member for non-functional) — recorded in the `review` frontmatter block. The
> routing is guidance, never a gate: any qualified team member, the BUG's own
> author included, may record it at any severity. Approval
> confirms the defect, evidence, nature and
> routing; it does **not** approve the future Bolt, SPEC, implementation,
> MEM or acceptance — each keeps its own checkpoint.

---

## 9. History

| Date | Change | Author |
|------|--------|--------|
| YYYY-MM-DD | Defect reported (draft) | @user |
| YYYY-MM-DD | AITL-BUG-Approval recorded | @user |
