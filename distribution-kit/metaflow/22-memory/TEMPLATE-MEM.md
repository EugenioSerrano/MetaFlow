---
id: "MEM-YYMMDD-HHmm"
title: ""
date: "YYYY-MM-DD"
author: "" # human:<user> (git-email local part) | agent:<id> — actor grammar (§3.0)
llm: "" # LLM model used (e.g. "Claude Sonnet", "GPT")
task: "" # US-NNN.TASK-NNN | US-000.TASK-NNN | TC-NNN.TASK-NNN — the TASK this Delivery Loop executed
spec: "" # SPEC-YYMMDD-HHmm of the canonical SPEC revision executed
spec_revision: 1 # revision of the canonical SPEC used by this Delivery Loop
delivery_loop: 1 # Delivery Loop number within the TASK (matches manifest delivery_loops[].number)
execution_outcome: "ready_for_review" # ready_for_review | failed | blocked | cancelled — describes execution before human review (§3.12)
baseline: "" # git commit of the repository baseline used by this Delivery Loop
applied_adrs: []
manifest: "" # Path to the TASK manifest in metaflow/23-metrics/tasks/ (e.g. "US-012.TASK-003-invoice-download.json")
diff_ref: "" # Link/identifier of the diff (PR/commit) for this Delivery Loop, when present
review_ready_at: "" # When this version is submitted for review (§3.0) — ISO 8601 with seconds + offset, e.g. 2026-08-02T11:45:00-03:00
review: # CP-MEM-Approval — filled by the human reviewer (§3.0)
  decision: "" # approved | changes_requested | rejected
  reviewers: [] # [{actor, role, model}]
  started_at: "" # ISO 8601 with seconds + offset
  decided_at: "" # ISO 8601 with seconds + offset
  findings: []
  acknowledged_without_comment: true # must be true when findings is empty (§3.0)
  acknowledgment_reason: "" # required when acknowledged_without_comment is true
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs, and section
  headings (##) stay in English (the schema). All prose — narrative
  summary, decisions, lessons learned — goes in the project's
  content_language (declared in metaflow/LANGUAGE).

  ⚠️ MANDATORY TIMESTAMP: To generate the ID and filename:
  1. Run: Get-Date -Format "yyMMdd-HHmm" (PowerShell) or date +"%y%m%d-%H%M" (Bash)
  2. Use that ACTUAL value to replace YYMMDD-HHmm in the id, title and filename.
  3. NEVER invent or estimate the time. If you cannot run the command, ask the user for the time.
  ⚠️ MANDATORY LLM: Fill the llm field with the exact model generating this document.
  ⚠️ MANDATORY — Manifest update: After writing this MEM, the agent MUST update the TASK
     manifest in metaflow/23-metrics/tasks/US-NNN.TASK-NNN-<description>.json by appending a new
     delivery_loops[] entry (number, spec_revision, git_commit, execution_outcome,
     code_generation, mem). The manifest is the mechanical evidence of the TASK (§3.12).
     Flow: US/TC → TASK → SPEC → Delivery Loop (code) → MEM + manifest delivery_loops[] entry.
  ⚠️ The MEM has NO mutable status: its state is derived from the associated
     CP-MEM-Approval decision (§2.12). The agent never self-approves it.
     The MEM + manifest + code form the complete package presented at CP-MEM-Approval.
     This template applies to EVERY Delivery Loop attempt — including blocked,
     failed, or turn-budget-exhausted ones (record the blocker in the
     summary and set execution_outcome accordingly). Filenames are reserved
     atomically; on a same-minute collision, the later MEM is created in the
     next minute (never overwrite, suffix, or reuse the earlier MEM).
     Mandatory post-execution sequence (G17): record outcome → create
     exactly one MEM → update manifest → PAUSE at CP-MEM-Approval. Never
     continue to a new Delivery Loop or merge without the human decision.
-->

# MEM-YYMMDD-HHmm — [Descriptive title]

| Field           | Value |
|-----------------|-------|
| **TASK**        | [US-NNN.TASK-NNN] |
| **SPEC**        | [link to the SPEC + revision] |
| **Delivery Loop**    | [number] |
| **ADRs**        | [links to applied ADRs] |

---

## 1. Executive summary

<!--
⚠️ MANDATORY: This CANNOT be a bullet list or a single line.
It must be a narrative paragraph explaining:
- What was implemented (concrete functionality, not just file names)
- What the outcome was (build OK, N tests, 0 regressions)
- Whether there were surprises, problems or deviations from the SPEC
Minimum 3–5 sentences with enough context to understand the complete work.
-->

[Concise description of what was implemented + key outcome
(e.g. "0 errors, 17 new tests passed, 106 existing without regression").
Include what functionality is now available to the user/system after this work.]

---

## 2. Implemented phases

<!--
⚠️ MANDATORY: Each phase must explain WHAT was built and HOW.
It is not enough to say "Created X". Explain what X does, what pattern it
follows, and how it integrates with the rest of the system. A new developer
must be able to understand the implemented architecture by reading only
this MEM.
-->

### Phase A — [Name]

[Description of what was built in this phase. What components were created,
what patterns were applied, how they interact with each other. Key decisions
made during implementation.]

### Phase B — [Name]

[Description of what was built in this phase. Same detail criteria.]

---

## 3. Files created

<!--
⚠️ MANDATORY: "Purpose" is NOT the file name repeated.
It must explain WHAT responsibility the file has in the system.
E.g.: NOT "EntityResponse DTO" → YES "DTO that exposes code, name and sector of the entity to the frontend via REST"
-->

| File | Purpose |
|------|---------|
|      |         |

---

## 4. Files modified

| File | Description of change |
|------|----------------------|
|      |                      |

---

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
|      |          |        |

---

## 6. Files deleted

| File | Reason |
|------|--------|
|      |        |

---

## 7. Implementation decisions

<!--
⚠️ MANDATORY: This section CANNOT be empty.
There are always decisions during implementation: which approach was chosen,
which alternatives were discarded, which trade-offs were accepted.
If "there were no decisions" it is because they were not documented — there
always are.
-->

| Decision | Reason |
|----------|--------|
|          |        |

---

## 8. Deviations and assumptions

[SPEC deviations, assumptions made, and unresolved risks from this Delivery Loop.]

---

## 9. Verification evidence

<!--
⚠️ MANDATORY: Record commands and results. For BUG Delivery Loops (§3.3.1),
record the red evidence and the green evidence SEPARATELY — a BUG Delivery Loop
without both pieces of evidence cannot receive approved CP-MEM-Approval.
-->

### Build
```
[output of dotnet build / npm run build]
```

### Tests
```
[output of dotnet test / npm test — count passed/failed/skipped]
```

### BUG Delivery Loop evidence (if applicable)
- **RED:** [command + result of the failing reproduction test]
- **GREEN:** [command + result after the fix]

### Gates
[Applicable gates results: pass / waived (ADR-NNN) / n/a with reason]

---

## 10. Manual interventions

[Direct human code patches applied as fallback — recorded, not punished
(§3.0, §2.12). "None" if the agent produced everything.]

---

## 11. Evidence links

- **Diff / PR:** [link or identifier, when present]
- **Commit:** [hash — see `baseline` in frontmatter]
- **Cumulative TASK manifest:** [path to `metaflow/23-metrics/tasks/` manifest]

---

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | [Xh / Xmin] |
| Delivery Loop number | [N] |
| Tests created | [N (breakdown by type)] |
| AI-generated code | [100% — or note human fallback] |
| First-pass approval | [yes / no] |

---

## 13. Pending items and stubs

[What remains for future work.]

- [ ] Pending item 1
- [ ] Pending item 2

---

## 14. CP-MEM-Approval

> **MetaFlow §2.12, §3.0.** This MEM is created by the agent with no
> mutable status and is **never self-approved**. A qualified human (the
> Dev-validator who executed the TASK; QA/Sec/domain reviewers optional, any risk)
> inspects the actual diff, test/gate evidence, MEM and manifest, and
> records `CP-MEM-Approval` here and in the manifest's
> `checkpoint_approvals[]`. `approved` completes the Delivery Loop (and, if latest,
> marks the TASK `Development Completed`); `changes_requested` keeps this
> MEM as immutable history and the next execution is a NEW Delivery Loop with a
> NEW MEM. `CP-TASK-DONE-Approval` is still required for `Done`.
>
> The machine-readable record lives in the frontmatter `review` block
> (below); the table summarizes it for the human.

| Field | Value |
|-------|-------|
| **Reviewers (executing Dev-validator; QA/Sec/domain optional)** | `human:<user>` (git-email local part) or `agent:<id>` — actor grammar (§3.0) |
| **Roles** | dev_validator (+ optional QA/Sec/domain reviewers) |
| **Decision** | approved / changes_requested / rejected |
| **review_ready_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` — set at package submission, before review |
| **review.started_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **review.decided_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **Review evidence** | [what was inspected: diff, tests, gates, MEM, manifest] |
| **Comments** | [reviewer comments] |
| **Findings** | [findings] |
| **acknowledged_without_comment** | [true/false — must be true if findings is empty] |
| **acknowledgment_reason** | [evidence inspected, if acknowledged without comment] |
