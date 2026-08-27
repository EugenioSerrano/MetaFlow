---
id: "REV-NNN"
title: ""
date: "YYYY-MM-DD"
author: ""                # human:<user> (git-email local part) | agent:<id> — actor grammar (§3.0)
llm: ""                   # LLM used (e.g. "Claude Sonnet")
status: "draft"           # draft | approved | closed
scope: ""                 # modules, projects or systems reviewed
methodology: ""           # static inspection, ADR compliance, grep analysis, etc.
reviewed_artifacts: []    # files, modules or systems evaluated
adrs_checked: []          # ADRs against which we review
specs_checked: []         # implemented SPECs being reviewed
review_ready_at: ""       # When this version is submitted for review (§3.0)
review: # CP-REV-Approval — filled by the human reviewer (§3.0)
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
  headings (##) stay in English (the schema). All prose — findings,
  observations, recommendations — goes in the project's content_language
  (declared in metaflow/LANGUAGE).

  ⚠️ CP-REV-Approval (§2.14, §3.0): findings remain DRAFT until a
  qualified human records CP-REV-Approval. Approval does NOT approve any
  downstream artifact. Code-related outcomes still require an approved TASK
  (T10 — never REV → SPEC directly). The Delivery Loop checkpoint is
  CP-MEM-Approval, recorded in the TASK manifest — never conflate the two.
-->

# REV-NNN — [Descriptive title]

| Field           | Value |
|-----------------|-------|
| **Scope**       | [modules / projects reviewed] |
| **Methodology** | [static inspection, ADR compliance, etc.] |
| **Criteria**    | [ADRs and standards against which we review] |

---

## 1. Purpose

[Why this review exists. What we aim to verify.]

---

## 2. Artifacts reviewed

| Artifact | Files | Notes |
|----------|-------|-------|
|          |       |       |

---

## 3. Severity legend

| Category | Meaning |
|----------|---------|
| **Compliant** | Implemented correctly per ADR / standard |
| **Documented deviation** | Justified difference, recorded in MEM |
| **Minor gap** | Inconsistency without functional impact, reduces quality |
| **Major gap** | Problem that can cause runtime errors or security exposure |

---

## 4. Findings

### 4.1 — [Domain / Category]

#### F-01 [Major gap] — [Finding title]

**Location:** `path/file.ext` line N

**Actual:** [What the code does today]

**Expected:** [What it should do per ADR / standard]

**Impact:** [Consequences of not fixing]

**Recommendation:** [Proposed fix]

---

#### F-02 [Minor gap] — [Finding title]

**Location:** `path/file.ext` line N

**Actual:** [...]

**Expected:** [...]

**Impact:** [...]

**Recommendation:** [...]

---

### 4.2 — [Another domain / Category]

#### F-03 [Compliant] — [What is correct]

[Brief description of what meets the standard.]

---

## 5. Summary

[Overall state in 2-3 sentences.]

---

## 6. Action plan

> Applies only after `CP-REV-Approval`. Each destination follows its own
> lifecycle and CITL approval (code → approved TASK first, T10).

| # | Finding | Severity | Action | Routes to |
|---|---------|----------|--------|-----------|
| 1 | F-01    | Major    |        | BUG / TASK→SPEC / ADR / RISK / DISC |
| 2 | F-02    | Minor    |        | TASK→SPEC |

---

## 7. Conclusions

[Overall state and recommendation: can we proceed? Is another review
cycle needed?]

---

## 8. CP-REV-Approval

> **MetaFlow §2.14, §3.0.** This Review remains a draft until a
> qualified human records `CP-REV-Approval` (in the `review` frontmatter
> block). Approval makes the findings actionable; it does not approve any
> downstream artifact. The Delivery Loop checkpoint is `CP-MEM-Approval`
> (recorded in the TASK manifest's `checkpoint_approvals[]`) — a REV and a
> Delivery Loop approval are different events.

| Field | Value |
|-------|-------|
| **Reviewer** | [qualified human designated for the Review] |
| **Decision** | approved / changes_requested / rejected |
| **review_ready_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **review.started_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **review.decided_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **Findings** | [findings or acknowledged_without_comment + reason] |

---

## 9. History

| Date | Change | Author |
|------|--------|--------|
| YYYY-MM-DD | Initial review (draft) | @user |
| YYYY-MM-DD | CP-REV-Approval recorded | @user |
