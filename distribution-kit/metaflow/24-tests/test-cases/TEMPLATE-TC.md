---
id: "TC-NNN"
title: ""
type: "functional"         # functional | non-functional — §2.6.1
date: "YYYY-MM-DD"
author: ""                 # human:<user> (git-email local part) | agent:<id> — actor grammar (§3.0)
llm: ""                    # LLM used for the first draft (if any)
status: "draft"            # draft | approved | deprecated
owner: ""                  # QA / Analyst — per §2.6.1 minimum metadata
source_task: ""            # ⚠️ MANDATORY — the EXACT approved product TASK this TC verifies
source_us: ""              # US-NNN for functional TCs (US-000 for non-functional — traceability only)
covered_acs: []            # ACs covered (functional TCs)
governing_sources: []      # ADRs / technical sources governing a non-functional TC
related_bugs: []           # BUG-NNN if this case came from a defect
review_ready_at: ""        # When this version is submitted for review (§3.0)
review: # CP-TC-Approval — filled by the human reviewer (§3.0)
  decision: "" # approved | changes_requested | rejected
  reviewers: [] # [{actor, role, model}]
  started_at: ""
  decided_at: ""
  findings: []
  acknowledged_without_comment: true # must be true when findings is empty (§3.0)
  acknowledgment_reason: ""
tags: []
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs stay in English
  (the schema). Section
  headings (##) follow the project's content_language. All prose — steps,
  expected results — goes in the project's content_language (declared in
  metaflow/LANGUAGE).
  `CP-*-Approval` codes are never translated.

  ⚠️ TEST-BASIS RULE (§2.6.1): expected results derive from APPROVED
  INTENT (US/ACs + approved source TASK, or non-functional TASK + ADRs),
  NEVER from the current implementation as oracle (G06).
  ⚠️ CP-TC-Approval: a draft TC cannot govern a SPEC or originate Test
  TASKs (TC-NNN.TASK-NNN). Approval is recorded in the review block.

  ⚠️ Manifest v1 (§3.12, G33): when creating this TC, create its manifest
  JSON in metaflow/23-metrics/test-cases/ (schema_version "5.0", tc, verifies,
  test_tasks: [], checkpoint_approvals: []). A TC without its manifest does not exist.
  Validate against manifest-v1-tc.schema.json.
-->

# TC-NNN — [Short title]

| Field | Value |
|-------|-------|
| **Type** | [functional / non-functional] |
| **Source TASK** | [US-NNN.TASK-NNN / US-000.TASK-NNN] |
| **Source US / ACs** | [US-NNN + AC list, or US-000 + governing ADRs] |
| **Status** | [draft / approved / deprecated] |

## 1. Objective

[What this test case verifies, in one sentence — the expected behavior from
approved intent, not what the code currently does.]

## 2. Preconditions

- [State the system must be in]
- [Test data required]
- [User / role required]

## 3. Steps

| # | Action | Expected result |
|:-:|--------|-----------------|
| 1 |        |                 |
| 2 |        |                 |
| 3 |        |                 |

## 4. Postconditions

- [State the system should be in after the test]

## 5. Alternative / negative paths

- **[Variant 1]** — when … expect …
- **[Variant 2]** — when … expect …

## 6. Pass/fail evidence

- [What evidence determines pass or fail — commands, screenshots, logs]

## 7. Traceability

- **Source TASK:** US-NNN.TASK-NNN (or US-000.TASK-NNN) — exactly one approved product TASK
- **Source US / ACs:** US-NNN / AC-NNN (functional)
- **Governing sources:** ADR-NNN (non-functional)
- **Related bugs:** BUG-NNN
- **Processes:** PROC-NNN — narrative traceability only. There is no `proc`
  frontmatter key and no manifest field: the governing chain of a TC is
  `source_us` + `covered_acs` (functional) or `source_us: US-000` + ADRs
  (non-functional), per §2.6.1.

## 8. Notes

- *(Optional: known limitations, environment-specific quirks, etc.)*

## 9. History

| Date | Change | Author |
|------|--------|--------|
| YYYY-MM-DD | Initial draft | @user |

## 10. CP-TC-Approval

> **MetaFlow §2.6.1, §3.0.** This TC remains a draft until a qualified
> human records `CP-TC-Approval` (in the `review` frontmatter block):
> QA plus the Functional Analyst/domain owner for functional expectations,
> or QA plus the applicable technical owner for non-functional. Role routing is
> guidance, not a gate: if a named role has no holder, the available qualified
> human records it, noting the self-assigned role. Approval
> confirms the test basis, coverage, preconditions, data, steps, expected
> results and pass/fail evidence — it does not approve implementation code.

---

## 11. Manifest creation (mandatory)

> ⚠️ **MANDATORY** — When this TC is created, also create its manifest JSON
> in `metaflow/23-metrics/test-cases/` with the same name (`.md` → `.json`):
> `schema_version: "1.0"`, the
> `tc{id,ref,sources,generation,review_ready_at,review_started_at}`
> block, the `verifies` block, and empty `test_tasks` / `checkpoint_approvals` arrays.
> A TC without its manifest **does not exist** (§3.12, G33). Validate
> against
> [`metaflow/23-metrics/manifest-v1-tc.schema.json`](../../23-metrics/manifest-v1-tc.schema.json);
> use [`TEMPLATE-MANIFEST-TC.json`](../../23-metrics/TEMPLATE-MANIFEST-TC.json)
> as the example. The agent appends `test_tasks[]` and the
> `CP-TC-Approval` decision — with its `review_ready_at`,
> `review_started_at` and `decided_at` timings — as the lifecycle
> progresses.
