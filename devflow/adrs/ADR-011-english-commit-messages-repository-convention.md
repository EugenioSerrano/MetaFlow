---
id: "ADR-011"
title: "Repository convention: commit and PR messages in this repository are written in English"
date: "2026-08-23"
author: "human:eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "accepted" # draft | accepted | rejected | deprecated | superseded
decision_makers: ["tech_lead"]
sources:
  - "maintainer direction (2026-08-23)"
supersedes: []
conflicts_with: []
tags: ["repository-convention", "language", "commits", "pr"]
nfrs: []
waiver: # Only for gate-override ADRs (§3.6)
  gate: ""
  reason: ""
  owner: ""
  compensating_control: ""
  expires_at: ""
review_ready_at: "2026-08-23T12:23:00-03:00"
review: # AITL-ADR-Approval evidence — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "tech_lead"
      model: null
  started_at: "2026-08-23T12:23:30-03:00"
  decided_at: "2026-08-23T12:24:30-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Accepted as the repository convention: commit and PR messages in this repository are written in English, scoped to this repository only (other repos keep their own language). No conflicts with active ADRs (reinforces §3.15). No AGENTS.md edit — the ADR is the governing record; the root README carries a pointer via its own Bolt (US-000.BOLT-017)."
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs, and section
  headings (##) stay in English (the schema). ADR titles and prose go in
  the project's content_language (en). `AITL-ADR-Approval` is never
  translated.
-->

# ADR-011 — Repository convention: commit and PR messages in English

| Field          | Value |
|----------------|-------|
| **Status**     | draft |
| **Decision-makers** | eugenio.serrano (tech_lead) |
| **Sources**    | maintainer direction (2026-08-23) |
| **Supersedes** | None |
| **Conflicts with** | None — §3.15's Language Policy already lists commit messages under "English always"; this ADR makes it an explicit, repository-scoped convention |

---

## 1. Context

This repository's commit and pull-request messages must be written in
**English**, consistently and permanently. The rule is scoped to **this
repository only**: other repositories follow their own content language and
conventions — a Spanish-speaking project may write its commits in Spanish.
The methodology's Language Policy (§3.15) already lists commit messages,
branch names and PR titles under "English always (schema)", but the
maintainer wants the convention recorded as a durable, governing decision of
this repository, independent of the framework's default — so it survives
context compaction and applies to every agent and human working here.

---

## 2. Alternatives considered

### Alternative A — Record the convention as an ADR (✅ Selected)

A short, governing ADR in the decision log.

| Aspect   | Detail |
|----------|--------|
| **Pros** | No Bolt required (decision-only artifact); immutable once accepted; durable across migrations (ADRs are project files copied forward by §5.16); visible in the adrs/ INDEX that agents read as part of the pre-implementation checklist; repository-scoped by nature |
| **Cons** | Not auto-loaded on every turn like the AGENTS.md project section — an agent that skips the adrs/ INDEX could miss it (mitigated: the practice is already aligned, and the Language Policy reinforces it) |

### Alternative B — Add the rule to the root AGENTS.md project section (via a Bolt)

| Aspect   | Detail |
|----------|--------|
| **Pros** | Auto-loaded by all four agents on every turn; survives migrations via the marker merge |
| **Cons** | ADR-004 classifies the project section as Repository surface: the edit must enter a Bolt's scope (G07) — full Bolt → SPEC → V-Bounce ceremony for one sentence; duplicates what an ADR already records |

### Alternative C — Platform memory only

| Aspect   | Detail |
|----------|--------|
| **Pros** | Zero ceremony |
| **Cons** | Personal, not repository-visible; lost for other agents and humans; not a governed record |

---

## 3. Decision

**We adopt Alternative A.** This repository records the convention as an
approved ADR: **every commit and pull-request message written in this
repository is in English** — subject line, body, and commit descriptions.
The rule is scoped to this repository; other repositories keep their own
language conventions. The convention is recorded here because it is this
repository's decision, not because the framework requires it (though §3.15
already lists commit messages under the English-always schema column, which
reinforces it). No AGENTS.md edit is made for this rule — the ADR is the
governing record.

---

## 4. Consequences

**Positive:**
- A durable, immutable, repository-scoped decision that any agent or human
  can cite.
- No ceremony: the ADR is created and approved without a Bolt.
- Consistent history: every future commit/PR message in this repo is
  English, matching the commits already pushed on the 5.1 line.

**Trade-offs:**
- The ADR is not auto-loaded every turn; enforcement relies on agents
  following the adrs/ checklist and the §3.15 Language Policy.

**Technical debt:**
- None.

---

## 5. Applicable NFRs

None — a repository convention, not a non-functional requirement.

---

## 6. References

- `devflow/avenga-devflow/Avenga-DevFlow.md` §3.15 Language Policy (English
  always: commit messages, branch names, PR titles).
- Related ADRs: ADR-004 (repository partition — this ADR lives in the
  Governance zone and binds the Repository surface).

---

## 7. AITL-ADR-Approval

> **AITL-ADR-Approval** (Avenga DevFlow §2.8, §3.0, §3.5). An ADR does not
> become `accepted` — and therefore governing — without the approval of an
> Architect / Tech Lead. This ADR is the **source of truth for its own
> approval** (recorded in the `review` frontmatter block with review
> evidence); when it governs a SPEC revision, its path appears in that
> revision's `sources`. ADR approvals are never copied to the Bolt manifest.

| Field | Value |
|-------|-------|
| **Architect / Tech Lead** | `human:eugenio.serrano` |
| **Role** | tech_lead |
| **Decision** | approved |
| **review_ready_at** | `2026-08-23T12:23:00-03:00` |
| **review.started_at** | `2026-08-23T12:23:30-03:00` |
| **review.decided_at** | `2026-08-23T12:24:30-03:00` |
| **Findings** | none — acknowledged_without_comment (reason in frontmatter `review:` block) |
