---
id: "ADR-012"
title: "All methodology artifacts of this repository — maintenance partition and kit — are written in English"
date: "2026-08-23"
author: "human:eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "accepted" # draft | accepted | rejected | deprecated | superseded
decision_makers: ["tech_lead"]
sources:
  - "maintainer direction (2026-08-23)"
  - "devflow/adrs/ADR-011-english-commit-messages-repository-convention.md"
supersedes: [] # ADR-011 stays active for commit/PR messages; this ADR generalizes the convention without contradicting it (§3.5)
conflicts_with: [] # ADR-011 ⊂ this ADR — both hold simultaneously; no contradiction
tags: ["repository-convention", "language", "english", "maintenance-partition", "kit"]
nfrs: []
waiver: # Only for gate-override ADRs (§3.6)
  gate: ""
  reason: ""
  owner: ""
  compensating_control: ""
  expires_at: ""
review_ready_at: "2026-08-23T12:29:55-03:00"
review: # AITL-ADR-Approval evidence — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "tech_lead"
      model: null
  started_at: "2026-08-23T12:30:15-03:00"
  decided_at: "2026-08-23T12:30:40-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Accepted: every methodology artifact of this repository (maintenance + kit partitions) is written in English; ADR-011 stays active for commit/PR messages (ADR-011 ⊂ ADR-012, no conflict per §3.5); schema layer out of scope (English by definition, §3.15); repository-scoped. No conflicts with active ADRs. The root README will carry a pointer via US-000.BOLT-017."
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs, and section
  headings (##) stay in English (the schema). ADR titles and prose go in
  the project's content_language (en). `AITL-ADR-Approval` is never
  translated.
-->

# ADR-012 — All methodology artifacts of this repository (maintenance + kit) are written in English

| Field          | Value |
|----------------|-------|
| **Status**     | draft |
| **Decision-makers** | eugenio.serrano (tech_lead) |
| **Sources**    | maintainer direction (2026-08-23); ADR-011 (accepted) |
| **Supersedes** | None — ADR-011 remains active for commit/PR messages; this ADR is its generalization |
| **Conflicts with** | None — ADR-011 ⊂ this ADR; both hold simultaneously (§3.5) |

---

## 1. Context

ADR-011 (accepted 2026-08-23) established that commit and pull-request
messages in this repository are written in English. The maintainer wants the
convention stated at its full breadth: **every methodology artifact of this
repository** — in the **maintenance partition** (the root `devflow/`, the
root `AGENTS.md`/`README.md`, the governance documents) **and** in the
**product partition** (`distribution-kit/`) — is written in English. This
covers the prose of USs, Bolts, SPECs, MEMs, ADRs, BUGs, DISCs, REVs,
AREVs, TCs, RISKs, INC/RETRO records, INDEX/README prose, the methodology
text, the agent definitions' shared bodies, and the root surface documents —
everything except the schema layer (YAML keys, enum values, JSON fields),
which is English by definition (§3.15). Commit/PR messages stay governed by
ADR-011, which this ADR generalizes without superseding: ADR-011 ⊂ ADR-012,
both active and consistent. The convention is repository-scoped: other
repositories follow their own content language.

---

## 2. Alternatives considered

### Alternative A — New ADR that generalizes ADR-011 without superseding it (✅ Selected)

ADR-012 states the broad convention; ADR-011 stays active for commit/PR
messages.

| Aspect   | Detail |
|----------|--------|
| **Pros** | No rewrite of an approved ADR (G36); both decisions remain in the active log and agree (12 ⊇ 11); the narrower rule keeps its own citation for commit/PR topics |
| **Cons** | Two ADRs on the same topic — acceptable and explicit (§3.5 allows overlapping consistent decisions) |

### Alternative B — ADR-012 supersedes ADR-011

| Aspect   | Detail |
|----------|--------|
| **Pros** | Single operative statement |
| **Cons** | ADR-011 would leave the active set despite the maintainer wanting it to stand ("quedará el 11 para el repo") — rejected by the maintainer |

### Alternative C — Edit ADR-011 in place

| Aspect   | Detail |
|----------|--------|
| **Pros** | One document |
| **Cons** | Blocked: G36/G26 — an approved ADR is immutable; editing after the recorded approval would falsify the decision record |

---

## 3. Decision

**We adopt Alternative A.** In this repository, **every methodology artifact
is written in English** — prose included — in both partitions: the
**maintenance partition** (root `devflow/` and its governance documents, the
root `AGENTS.md` project section, the root `README.md`) and the **product
partition** (`distribution-kit/`, methodology text, guardrails prose, agent
definitions' shared bodies, templates' explanatory comments, README/INDEX
prose). The schema layer (YAML keys, enum values, JSON fields, IDs) is
English by definition (§3.15) and is not part of this decision's scope.
Commit and PR messages remain governed by ADR-011, which this ADR
generalizes: the two ADRs coexist without conflict. The convention is
scoped to this repository — other repositories follow their own content
language and conventions.

---

## 4. Consequences

**Positive:**
- A single, durable, repository-wide language convention covering every
  artifact in both partitions.
- The decision log keeps both records honest: ADR-011 (commits/PRs) and
  ADR-012 (all artifacts) — no rewritten history.
- Agents and humans writing in this repository have an explicit, citable
  rule that matches the already-consistent practice (the entire repository
  is written in English today).

**Trade-offs:**
- Two ADRs on the language topic instead of one — explicit and consistent
  (12 ⊇ 11), and each keeps its own citation value.

**Technical debt:**
- None.

---

## 5. Applicable NFRs

None — a repository convention, not a non-functional requirement.

---

## 6. References

- `devflow/adrs/ADR-011-english-commit-messages-repository-convention.md`
  (accepted — the commit/PR-message convention this ADR generalizes).
- `devflow/avenga-devflow/Avenga-DevFlow.md` §3.15 Language Policy.
- `devflow/adrs/ADR-004-repository-partition-v2.md` (the two partitions).

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
| **review_ready_at** | `2026-08-23T12:29:55-03:00` |
| **review.started_at** | `2026-08-23T12:30:15-03:00` |
| **review.decided_at** | `2026-08-23T12:30:40-03:00` |
| **Findings** | none — acknowledged_without_comment (reason in frontmatter `review:` block) |
