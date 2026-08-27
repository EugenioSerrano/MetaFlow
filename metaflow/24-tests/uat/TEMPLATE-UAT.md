---
id: "UAT-NNN"
date: "YYYY-MM-DDTHH:mm:ss±HH:MM"  # point-in-time event: start of the UAT session
author: ""                # human:<user> (git-email local part) | agent:<id> — actor grammar (§3.0)
llm: ""                   # LLM used for first draft (e.g. "Claude Sonnet")
unit: ""                  # Unit / Milestone validated
facilitator: ""           # human:<user> (git-email local part) | agent:<id> — actor grammar (§3.0)
status: "draft"           # draft | approved | approved-with-observations | rejected
tasks: []                 # TASKs covered
adrs: []                  # related ADRs
linked_vision_outcomes: [] # outcomes from vision/ this UAT validates
linked_processes: []      # PROC-NNN this UAT exercises
review_ready_at: ""       # When this version is submitted for review (§3.0)
review: # CP-UAT-Approval — filled by the stakeholders (§3.0)
  decision: "" # approved | changes_requested | rejected
  reviewers: [] # [{actor, role, model}]
  started_at: ""
  decided_at: ""
  findings: []
  acknowledged_without_comment: true # must be true when findings is empty (§3.0)
  acknowledgment_reason: ""
---

> ⛔ **DORMANT / RESERVED (v4.2).** The UNIT/UAT approval-and-release layer was
> **removed from the active flow in v4.2** — `CP-UAT-Approval` is **not an
> active checkpoint** in this release. The governed flow ends at TASK
> acceptance (`CP-TASK-DONE-Approval`). This template is kept **dormant** for
> a redesigned model planned in a future version. The frontmatter and
> body below describe the future (reserved) UAT process, not an active gate.

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs, and section
  headings (##) stay in English (the schema). All prose — observations,
  feedback, sign-off notes — goes in the project's content_language
  (declared in metaflow/LANGUAGE).

  ⚠️ CP-UAT-Approval (§3.0): stakeholders sign off the Unit/Milestone.
  The UAT minutes in 24-tests/uat/ are the evidence — the TASK manifest
  carries NO UAT data (§3.12).

  ⚠️ Review contract (§3.0): review.decision uses the universal enum
  approved | changes_requested | rejected. The document status
  approved-with-observations is a UAT lifecycle label, not a decision
  value: it means review.decision: approved with non-empty findings[] —
  every finding routes to a new TASK (section 4 below).
-->

# UAT-NNN — [Unit / Milestone]

## 1. Scope validated

[Summary of what this UAT session covers — which TASKs, which user-visible
behaviour, which process flows.]

## 2. Signing stakeholders

| Name | Role | Signature | Date |
|------|------|-----------|------|
| @user |     |           |      |

## 3. Results per criterion (business ACs)

| AC    | Description | Result        | Evidence | Observation |
|-------|-------------|---------------|----------|-------------|
| AC-01 |             | [ok] / [warn] / [fail] |          |             |
| AC-02 |             | [ok] / [warn] / [fail] |          |             |

> Each AC must trace to a vision outcome or process rule. List the link in
> the *Observation* column when not obvious.

## 4. Agreed adjustments (derived TASKs)

- [ ] US-NNN.TASK-NNN — [adjustment]
- [ ] US-NNN.TASK-NNN — [adjustment]

## 5. Final decision

- [ ] Approved
- [ ] Approved with observations (TASKs listed above)
- [ ] Rejected — reason: [...]

## 6. CP-UAT-Approval

> **MetaFlow §3.0.** Stakeholders sign off the Unit/Milestone here and
> in the `review` frontmatter block. The UAT minutes are the evidence —
> the TASK manifest deliberately carries no UAT data (§3.12).

| Field | Value |
|-------|-------|
| **review.reviewers** | [stakeholders / customer] |
| **review.decision** | approved / changes_requested / rejected |
| **review_ready_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **review.started_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **review.decided_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **Findings** | [findings or acknowledged_without_comment + reason] |

## 7. Sources

| Source | Where |
|--------|-------|
| Vision outcomes | `../../02-analysis/vision/vision.md` *(from TEMPLATE-VISION.md)* |
| Processes      | `../../02-analysis/process/PROC-NNN.md` |
| TASKs          | `../../12-functional/tasks/US-NNN.TASK-NNN-<description>.md` |
| Delivery Loop evidence | `../../22-memory/MEM-YYMMDD-HHmm-<description>.md` |
