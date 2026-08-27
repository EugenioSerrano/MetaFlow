# Memory (Project Memory)

**Methodology version:** 1.1

## Purpose

This folder stores the **project memory**: documents that capture WHAT was
done, HOW it was done, WHAT was decided and WHAT was learned during
implementation.

It is the technical logbook. It does not describe what SHOULD be done
(→ Specs) or what was DECIDED at an architectural level (→ ADRs). It
documents what **actually happened**.

"Knowledge is product." — MetaFlow §3.1.

---

## Flow that produces a MEM

Each MEM is the final output of this chain:

```
12-functional/tasks/     → defines TASKs (US-NNN.TASK-NNN / US-000.TASK-NNN / TC-NNN.TASK-NNN)
  └─ 21-spec/SPEC-YYMMDD  → Delivery Loop input (WHAT + HOW, CP-SPEC-Approval)
       └─ Delivery Loop     → agent generates code + tests (exactly ONE MEM per Delivery Loop)
            └─ 22-memory/MEM-YYMMDD-HHmm  → narrative record of that Delivery Loop
                 └─ 23-metrics/tasks/US-NNN.TASK-NNN-desc.json  → manifest delivery_loops[] entry
```

- **`MEM-YYMMDD-HHmm-<description>.md`** — Narrative document: what was
  implemented, decisions, tests, outcome. Exactly one per Delivery Loop.
- **TASK manifest** — Mechanical traceability (JSON) of the TASK: origin,
  SPEC revisions, Delivery Loops, CITL decisions. Lives in `metaflow/23-metrics/tasks/`
  (one per TASK, append-only, updated after every MEM). See MetaFlow
  §3.12.

> A TASK without a manifest in `metaflow/23-metrics/tasks/` **does not exist** (§0
> non-negotiable). The MEM is **not** optional either: a Delivery Loop without
> exactly one complete MEM cannot enter `CP-MEM-Approval` (§2.12, §3.3).

---

## What documents belong here?

- Summary of the executed Delivery Loop.
- List of files created/modified/renamed/deleted and their purpose.
- Repository baseline (git commit) of the Delivery Loop.
- Design decisions made during implementation.
- Deviations from the SPEC and assumptions.
- Test and gate results with evidence.
- Red/green evidence for BUG Delivery Loops (recorded separately, §3.3.1).
- Manual interventions (human patches) — measured, not hidden.
- Evidence links (diff/commit/PR + cumulative manifest entry).
- Risks, pending items or stubs for future work.
- Practical context to resume work without commit archaeology.

> **Mandatory post-execution sequence (§3.3, G17):** Record outcome →
> Create exactly one MEM → Update manifest → **PAUSE at
> `CP-MEM-Approval`**. Never continue to a new Delivery Loop or merge without
> the human decision. The agent never self-approves; the human records
> `CP-MEM-Approval` in both the MEM and the manifest (§3.0).

---

## Naming convention

```
MEM-YYMMDD-HHmm-short-description-of-work.md
```

Where:
- `MEM` — Fixed prefix.
- `YYMMDD` — Creation date (2-digit year, month, day).
- `HHmm` — Creation time (hour, minutes).
- `short-description` — **Stable kebab-case slug**: all MEMs for the same
  TASK and canonical SPEC reuse the identical slug; only the timestamp
  changes across Delivery Loops (§2.12). Never append `v2`, `retry`, `fix`, or
  `bounce-2` suffixes.
- `.md` — Markdown extension.

**Collision rule (§2.12):** filenames are reserved atomically; if two MEMs
would receive the same minute-level timestamp, the later MEM is created in
the next minute. Overwriting, suffixing or reusing the earlier MEM is
forbidden.

**Example:** `MEM-260802-1015-invoice-download.md`, then
`MEM-260802-1128-invoice-download.md` for the next Delivery Loop of the same TASK.

> ⚠️ **IMPORTANT — System timestamp:** The `YYMMDD` and `HHmm` values MUST
> be obtained from the ACTUAL system date and time when the file is created.
> **NEVER invent or estimate** the time. Use the system command:
> - **PowerShell:** `Get-Date -Format "yyMMdd-HHmm"`
> - **Bash/Zsh:** `date +"%y%m%d-%H%M"`
>
> If the AI agent cannot execute system commands, it must ask the user to
> provide the current date/time, or use the conversation context date/time.

---

## Recommended structure

The authoritative structure is [`TEMPLATE-MEM.md`](TEMPLATE-MEM.md) — its
**14 sections** (matched by heading keyword, never by number — §3.15), plus
the frontmatter, in this order:

- **Frontmatter** — ID (MEM-YYMMDD-HHmm), name, date, author (local part of
  `git config user.email`, §3.0), references. The MEM has **no status field**
  — its review state is derived from `CP-MEM-Approval` (§2.12).
1. **Executive summary** — Narrative of what the Delivery Loop delivered
   (3–5 sentences minimum, never a bullet list).
2. **Implemented phases** — What was built and how (per SPEC phase).
3. **Files created** — Every added file, with path and purpose.
4. **Files modified** — Every changed file, with path and purpose.
5. **Files renamed** — Every renamed file, with path and purpose.
6. **Files deleted** — Every deleted file, with path and purpose.
7. **Implementation decisions** — Practical trade-offs made during
   implementation.
8. **Deviations and assumptions** — Honest record of deviations from
   the SPEC.
9. **Verification evidence** — Build + tests + gates, with commands and
   results (red/green separately for BUG Delivery Loops).
10. **Manual interventions** — Anything a human did by hand during the
    Delivery Loop.
11. **Evidence links** — Diff/commit/PR and the cumulative TASK manifest
    entry (§2.12).
12. **Metrics** — the AI-native and CITL numbers of this Delivery Loop (AI
    generation time, Delivery Loop number, tests created, first-pass approval).
    **No Delivery Flow here:** the Delivery Flow Five are computed at deployment level from
    CI/CD and incidents, never from a MEM (§3.7.1 — see *Metrics* below).
13. **Pending items and stubs** — What remains for future work.
14. **CP-MEM-Approval record** — Reviewer, role, timestamps, decision,
    review evidence, comments and findings (§2.12, §3.0).

### Diagrams and visual elements

Use **Mermaid** for all diagrams, charts and any other visual element
(no ASCII art or embedded images).

---

## Importance

- **Continuity**: resume work without loss of context.
- **Context for AI**: agents read Memory to understand patterns and history.
- **Onboarding**: new team members understand implementation history.
- **Traceability**: SPEC revision → MEM → code → manifest `delivery_loops[]`.

---

## Minimum quality standard (MANDATORY)

A MEM **must be self-contained and explanatory**. Anyone (or an AI agent)
reading it months later must be able to understand WHAT was done, WHY
certain decisions were made, and WHAT the outcome was — without needing to
review commits or read other documents.

> ⚠️ **Quantitative floor (GUARDRAILS W03):** A MEM without the minimum
> content triggers a warning. This is a heuristic — a short MEM that meets
> all quality criteria below is acceptable; a long MEM that fails them is
> not.

### Minimum content rules

1. **Executive summary** — ALWAYS include a paragraph explaining what was
   implemented and the final outcome (build status, tests, errors found).
   Not just bullets.
2. **Files with purpose** — Do not list files without explaining WHAT they
   do. Every created/modified file must have a description explaining its
   role in the system.
3. **Implementation decisions** — ALWAYS document practical trade-offs:
   why one approach was chosen over another, what alternatives were
   discarded.
4. **Integration context** — Explain how the implementation connects with
   the rest of the system. What components consume the new code? What
   flow does it complete?
5. **Tests with results** — Not just "3 tests". State what they verify and
   the overall suite result (regressions, total passing). For BUG
   Delivery Loops, record red and green evidence **separately** (§3.3.1).

### Anti-patterns (DO NOT)

| ❌ Anti-pattern | ✅ Correct approach |
|-----------------|---------------------|
| 10-line telegram-style MEM | Minimum: summary + files with purpose + decisions + tests |
| "Created X, modified Y" with no explanation | Every file carries a description of its responsibility |
| Only listing files without explaining decisions | Decisions section explains WHY it was done that way |
| Omitting build/test results | Always include final build state and test suite results |
| MEM without context of the origin SPEC | Reference the SPEC revision and explain what objective it covered |

### Completeness metric

A well-written MEM answers these questions:
- Can I resume this work tomorrow without losing context? → If not, detail
  is missing.
- Do I understand why each decision was made? → If not, decisions are
  missing.
- Do I know what broke or was found during implementation? → If not,
  13-bugs/issues are missing.
- Can a new developer understand what exists now? → If not, explanation
  is missing.

---

## MEM lifecycle

A MEM has **no mutable status** (§2.12): its review state is derived from
the associated `CP-MEM-Approval` — no decision means pending review,
`approved` means an approved Delivery Loop, `changes_requested` or `rejected`
means an immutable historical attempt that did not advance. After the human
decision, the MEM is **immutable history**; the next agent execution is a
NEW Delivery Loop with a NEW MEM.

An approved MEM for the latest Delivery Loop marks the TASK
**`Development Completed`** — it does **not** make the TASK `Done`;
acceptance remains governed by `CP-TASK-DONE-Approval` (§2.12,
§3.0).

This folder has **no `INDEX.md`** (§5.15): the `YYMMDD-HHmm` timestamp already
assigns and orders every MEM, so no central allocator is needed — and no
shared file has to be edited on every Delivery Loop, which would conflict on every
concurrent branch.

---

## Documents

Documents in this folder follow the convention
`MEM-YYMMDD-HHmm-description.md` and are identified by their unique
timestamp. The file listing itself is the inventory — there is no `INDEX.md`
(§5.15).

---

## Metrics (Delivery Flow + AI-native + CITL)

The MetaFlow methodology defines key metrics to measure development
health (§3.7). **The MEM provides narrative context; the metrics are
computed from the TASK manifest and deployment telemetry** — the manifest
family deliberately does not duplicate Delivery Flow, gates, or cost data (§3.12).

### Delivery Flow metrics connection

Delivery Flow is computed at **deployment level** from CI/CD deployment events,
incidents and production-fix deployments (§3.7.1) — **not** from MEMs or
the TASK manifest. The MEM only records the narrative of what was
implemented.

### AI-native flow metrics (§3.7.2)

| Metric | What it measures | Source |
|--------|-----------------|--------|
| **Model runs per TASK** | `runs[]` across TASK/SPEC/code/MEM generation | manifest generation blocks |
| **Delivery Loops per TASK** | Packages submitted for human validation | `delivery_loops[]` count |
| **Spec Drift** | Agent questions + material SPEC revisions | `spec_revisions[]` + agent questions |
| **Manual Intervention Rate** | % of TASKs whose MEMs report direct human code changes | MEMs (recorded in narrative, not the manifest) |
| **SPEC first-review approval rate** | SPEC revisions whose first `CP-SPEC-Approval` is approved | `checkpoint_approvals[]` |
| **Delivery Loop first-review approval rate** | TASKs whose first Delivery Loop MEM is approved | `checkpoint_approvals[]` |

### CITL governance metrics (§3.7.3)

| Metric | What it measures | Source |
|--------|-----------------|--------|
| **CITL Coverage** | % of TASKs with all required named checkpoints signed with evidence | Manifest `checkpoint_approvals[]` + governed artifacts |
| **Time-to-Human-Review** | `review_ready_at` → `review.started_at` (agent completion → human starts) | Artifact review contract + telemetry |
| **Approval-without-Comment Rate** | % of approved decisions with empty findings | Artifact `review.findings` |

### Example metrics section in a MEM

```markdown
## Metrics

| Metric | Value |
|--------|-------|
| Lead Time (CP-TASK-READY-Approval → CP-TASK-DONE-Approval) | 5h total (ai: 47min · review: 35min · wait: 3h 38min) |
| AI generation time | 47min |
| Delivery Loops | 1 |
| Tests created | 17 (10 unit + 4 integration + 3 e2e) |
| AI-generated code | 100% |
| First-pass approval | yes |
```

> **Note:** Aggregated project metrics (dashboards, trends) are computed
> from TASK manifest data in `metaflow/23-metrics/tasks/` and deployment telemetry,
> never from MEM narratives alone (§3.12). TASK Lead Time is decomposed
> into `ai_generation_minutes | human_review_minutes | wait_minutes`
> (§3.7.1) and is never reported as Delivery Flow Change Lead Time.

---

## Language

YAML keys, status enums, IDs, and template section headings stay in **English**
(the schema). All prose — descriptions, context, rationale, findings — goes in
the project's `content_language`, declared in [`../LANGUAGE`](../LANGUAGE)
(see §3.15).
