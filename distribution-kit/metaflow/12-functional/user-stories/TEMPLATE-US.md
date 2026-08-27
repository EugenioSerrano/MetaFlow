---
id: "US-NNN"
title: ""
date: "YYYY-MM-DD"
author: "" # human:<user> (git-email local part) | agent:<id> — actor grammar (§3.0)
llm: "" # LLM model used (e.g. "Claude Sonnet", "GPT")
status: "draft" # draft | approved | deprecated
owner: "" # Functional Analyst (governs this US)
unit: "" # Unit or epic (e.g. "1 — Payments Module")
story_points: null # Fibonacci 1|2|3|5|8|13 — relative functional complexity
                   # (ACs, rules, flows, integrations, unknowns), NEVER time.
                   # Proposed by the agent, confirmed at CP-US-Approval (§2.6).
                   # Informational only: no gate, no velocity, no hour conversion.
                   # Scoring: use the §2.6 rubric — score the HIGHEST dimension,
                   # never the average; compare against approved USs in INDEX.md
                   # when they exist; open OQs targeting this US = unknowns.
                   # 13 = splitting signal: propose decomposition before approval.
adrs: [] # Related ADRs
sources: [] # evidence the US was derived from — 01-input/ refs, REV-NNN, AREV-NNN, interviews (required, min 1)
stakeholders: []
tags: []
review_ready_at: "" # When this version is submitted for review (§3.0)
review: # CP-US-Approval — filled by the human reviewer (§3.0)
  decision: "" # approved | changes_requested | rejected
  reviewers: [] # [{actor, role, model}]
  started_at: ""
  decided_at: ""
  findings: []
  acknowledged_without_comment: true # must be true when findings is empty (§3.0)
  acknowledgment_reason: "" # required when acknowledged_without_comment is true
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs stay in English
  (the schema). Section
  headings (##) follow the project's content_language. All prose — descriptions,
  acceptance criteria, scenarios — goes in the project's content_language
  (declared in metaflow/LANGUAGE).
  `CP-*-Approval` codes are never translated.

  ⚠️ CP-US-Approval (§2.6, §3.0): a feature US remains DRAFT until a
  Functional Analyst records CP-US-Approval. Only then may it be
  decomposed into candidate functional TASKs. US-000 is outside this
  lifecycle. Approval is never inherited from related artifacts.

  ⚠️ Manifest v1 (§3.12, G33): when creating this feature US, create its
  manifest JSON in metaflow/23-metrics/user-stories/ (schema_version "5.0", us,
  story_points, tasks: [], checkpoint_approvals: []). A feature US without
  its manifest does not exist. Validate against manifest-v1-us.schema.json.
  US-000 has no manifest — it is a permanent container with no approval
  lifecycle.
-->

> **Naming convention (mandatory):** Files go in `user-stories/` with the
> format `US-NNN-<description>.md`. Example: `US-001-payment-processing.md`.
> The `US-NNN` prefix is required for traceability across ADRs, SPECs, MEMs,
> BUGs, and TASK manifests.

# US-NNN — [User Story title]

| Field          | Value |
|----------------|-------|
| **Unit**       | [Unit / Epic] |
| **ADRs**       | [links to applicable ADRs] |
| **Status**     | [draft / approved / deprecated] |
| **Story points** | [1 / 2 / 3 / 5 / 8 / 13 — relative functional complexity, never time (§2.6)] |

---

**As a** [role], **I want** [capability], **so that** [value].

## 1. Acceptance criteria

- **Given** [context], **When** [action], **Then** [expected result].
- **Given** [context], **When** [action], **Then** [expected result].
- **Given** [context], **When** [action], **Then** [expected result].

> ACs are verifiable functional criteria only — non-functional constraints
> live in ADRs (§2.7).

## 2. TASKs

| # | TASK | Type | Layer | Description | Est. active delivery |
|---|------|------|-------|-------------|----------------------|
| 1 | `TASK-001` (`../tasks/US-NNN.TASK-001-short-title.md`) | functional | Backend | [Description] | 3h |
| 2 | `TASK-002` (`../tasks/US-NNN.TASK-002-short-title.md`) | functional | Frontend | [Description] | 4h |

> **Note:** TASKs are detailed in separate documents using
> [TEMPLATE-TASK.md](../tasks/TEMPLATE-TASK.md) and MUST be placed in the
> `tasks/` subfolder with the naming convention
> `US-NNN.TASK-NNN-<description>.md`. Only approved USs decompose into
> candidate functional TASKs. Each TASK has its own `CP-TASK-READY-Approval`,
> DoR (validated within it) and DoD.
>
> **Estimation:** the `Est. active delivery` column follows the AI-native
> estimation rule (§2.4) — composed from expected Delivery Loops, review budgets
> per risk_class and setup/integration overhead, never from manual coding
> effort. Typical low/medium TASKs: 1–4h.
>
> **Plausibility check (§2.6):** the TASK count should roughly match the
> US's story points band (1–2 SP → 1–2 TASKs; 3–5 → 2–4; 8 → 4+). Far
> outside the band → re-examine the score or the slicing — never force a
> decomposition to fit the band, and never convert points to hours (W18).

---

## 3. Business rules

[Domain constraints and conditions.]

| # | Rule | Condition | Action |
|---|------|-----------|--------|
|   |      |           |        |

---

## 4. User flows

```mermaid
flowchart TB
    A["Start"] --> B["Step 1"] --> C["Step 2"] --> D["End"]
```

---

## 5. Impact

[Affected modules, dependencies, risks.]

---

## 6. SDLC tool alignment

[Associated Work Items, Sprint, Board — optional, per the team's own SDLC
integration.]

---

## 7. CP-US-Approval

> **MetaFlow §2.6, §3.0.** This feature US remains a draft until a
> Functional Analyst records `CP-US-Approval` (recorded in the `review`
> frontmatter block), confirming that the US and its ACs faithfully
> represent the evidence in `01-input/` and the analysis in `02-analysis/`.
> Only then may it be decomposed into candidate functional TASKs. US-000
> is outside this lifecycle.

---

## 8. Manifest creation (mandatory)

> ⚠️ **MANDATORY** — When this feature US is created, also create its
> manifest JSON in `metaflow/23-metrics/user-stories/` with the same name
> (`.md` → `.json`): `schema_version: "1.0"`, the
> `us{id,ref,sources,generation,review_ready_at,review_started_at}`
> block, `story_points`, and empty `tasks` / `checkpoint_approvals`
> arrays. A feature US without its manifest **does not exist** (§3.12,
> G33). Validate against
> [`metaflow/23-metrics/manifest-v1-us.schema.json`](../../23-metrics/manifest-v1-us.schema.json);
> use [`TEMPLATE-MANIFEST-US.json`](../../23-metrics/TEMPLATE-MANIFEST-US.json)
> as the example. The agent appends `tasks[]` and the `CP-US-Approval`
> decision — with its `review_ready_at`, `review_started_at` and
> `decided_at` timings — as the lifecycle progresses.
>
> **US-000 is excluded:** it is a permanent traceability container with no
> approval lifecycle, and therefore carries no manifest.
