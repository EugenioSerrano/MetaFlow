---
id: "ADR-006"
title: "Versioning and self-development model: build version N under the previous stable N-1"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
status: "accepted"
decision_makers: ["architect", "tech_lead"]
sources:
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
  - "README.md"
supersedes: []
conflicts_with: []
tags: ["versioning", "dogfooding", "release-loop", "git-flow", "maintainer-internal", "partition"]
nfrs: []
waiver:
  gate: ""
  reason: ""
  owner: ""
  compensating_control: ""
  expires_at: ""
review_ready_at: "2026-08-22T13:11:17-03:00"
review: # HITL-ADR-Approval evidence — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "architect"}]
  started_at: "2026-08-22T13:29:53-03:00"
  decided_at: "2026-08-22T13:29:53-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Accepted. The decision faithfully records the maintainer's long-standing flow (branches 4.0/4.1/4.2/5.0): product line = version being built (N) as a plain number in the kit VERSION + repo README; operating methodology (root devflow/ + agents) = previous stable (N-1), advanced only by the §5.16 migration run at the next version's branch start; branch-per-version released by PR to main (main = latest released); in-progress vs released told by branch-vs-main, so no version-text flip; releases marked by annotated git tags (v4.2 already created on main). Maintainer-internal like ADR-002/004/005; adds no rule to the kit; complements ADR-004. Immutable from now on."
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs and section headings
  stay in English (the schema); prose follows content_language (en).
  `HITL-ADR-Approval` is never translated.

  ⚠️ This ADR is a DRAFT until an Architect / Tech Lead records
  HITL-ADR-Approval. A draft ADR cannot govern.

  ⚠️ SCOPE: maintainer-internal, like ADR-002/ADR-004/ADR-005 — it governs how
  THIS repository versions and develops itself. It does NOT add a rule to the
  distributable kit.
-->

# ADR-006 — Versioning and self-development model: build version N under the previous stable N-1

| Field          | Value |
|----------------|-------|
| **Status**     | **accepted** (immutable — a new decision requires a superseding ADR) |
| **Decision-makers** | Architect / Tech Lead (maintainer) |
| **Sources**    | ADR-004 (partition + release loop), repo-root `README.md` |
| **Supersedes** | None |
| **Conflicts with** | None — complements ADR-004 |

---

## 1. Context

This repository **builds** Avenga DevFlow and **is governed by** Avenga DevFlow
(ADR-004: two `devflow/` trees). Because of that, more than one "version" is in
play at once, and they are deliberately **not** the same number:

1. the **product being built** — `distribution-kit/` and its `VERSION`, plus the
   repo-root `README.md` version line;
2. the **operating methodology** — the root `devflow/` (self-governance) and the
   platform agent definitions (`CLAUDE.md`, `SKILL.md`, `AvengaDevFlow.agent.md`,
   `AvengaDevFlow.md`), under whose rules the maintainer actually works.

The maintainer has developed several versions this way (branches `4.0`, `4.1`,
`4.2`, now `5.0`): a new version is built **using the previous stable version as
the operating toolchain** (dogfooding), which is what makes every release run the
real §5.16 upgrade path (ADR-004's "release loop"). Without a written rule this
reads as a contradiction — the branch is `5.0` while every `VERSION` file reads
`4.2` — and it is not obvious that this is **correct**. This ADR records the model
so it is applied the same way every version.

---

## 2. Alternatives considered

### Alternative A — Product line = N on its own branch (merged to `main` to release), operating methodology = N-1 (✅ Selected)

| Aspect | Detail |
|--------|--------|
| **Pros** | Matches the maintainer's long-standing flow. Unambiguous: the product line (N) and the governing methodology (N-1) each have a defined meaning and a defined moment to flip. `main` = the latest released version; in-progress vs released is told by branch-vs-`main`, so no version-text qualifier ever needs flipping. Preserves the ADR-004 dogfooding guarantee. |
| **Cons** | On a version branch the kit content is still converging to N while `VERSION`/README already read N — acceptable because the branch (not `main`) signals in-progress. Retrieving an exact past release needs a git tag, not the moving `main` pointer. |

### Alternative B — One version everywhere, flipped at release

| Aspect | Detail |
|--------|--------|
| **Pros** | Simplest single number. |
| **Cons** | Erases the dogfooding split — you cannot tell which methodology version governs the work, reintroducing the "which version am I operating under?" ambiguity this ADR exists to remove. |

### Alternative C — "Stable X · in development Y" (or "under construction") text in the README

| Aspect | Detail |
|--------|--------|
| **Pros** | Shows progress state in prose. |
| **Cons** | Static text that must be flipped when the branch merges to `main`; the maintainer flagged this maintenance hassle. Redundant once branch-vs-`main` already signals in-progress-vs-released. |

---

## 3. Decision

**We adopt Alternative A.** The model, applied every version:

1. **The product line carries the version being built (N), as a plain number.**
   `distribution-kit/devflow/VERSION` and the repo-root `README.md` version line
   read **N** — no "under construction" / "stable-dev" qualifier.
2. **The operating methodology stays at the previous stable version (N-1).** The
   root `devflow/` (self-governance artifacts + `VERSION`) and the four platform
   agent definitions read **N-1** while N is built (dogfooding).
3. **Branch-per-version, released by merging to `main`.** A new version N starts
   by branching `N` from `main`. At that branch's start, the ordinary §5.16
   migration installs the **just-finished** previous version into the operating
   root (root: N-2 → N-1) — and that migration is where development of N begins
   (ADR-004's release loop). Work happens on branch `N`; short-lived sub-branches
   off `N` (features, experiments) are fine and merge back into `N`. When N is
   complete, **PR `N` → `main`** — that merge is the release, and `main` then
   carries N.
4. **`main` always holds the latest released version.** In-progress vs released
   is signaled by **branch-vs-`main`**, never by version text — so nothing in the
   `README`/`VERSION` needs flipping at merge time.
5. **Each release is tagged on `main`** (`vN`, annotated) — the immutable,
   retrievable marker. Branches move or are deleted; a tag pins the exact release
   commit forever, even after `main` advances to N+1.

**Worked example (this repo, today):** branches `4.0`/`4.1`/`4.2` finished and
merged; `main` = **4.2** (PR #7). Branch `5.0` is in progress with the product
line = **5.0** (kit `VERSION` + README) and the operating methodology = **4.2**
(root `devflow/` + agents, set by the §5.16 migration run at the start of `5.0`).
Pending: tag **`v4.2`** on `main` to mark the released 4.2 (no tags exist yet).

---

## 4. Consequences

**Positive:**
- The two numbers are unambiguous — product line (`5.0`) and operating
  methodology (`4.2`) each have a defined meaning and moment to flip.
- The repo-root README self-documents the state; a web visitor understands it
  without reading git history.
- Zero text flips: because branch-vs-`main` signals in-progress-vs-released, the
  version prose never has to change at merge time.
- The dogfooding guarantee (every release runs the real §5.16 upgrade on a real
  repository) is preserved and formally tied to the branch/version model.

**Trade-offs:**
- `main` HEAD is always a finished release; the in-construction line lives on its
  branch until the PR. Consumers who want a specific past release use its tag.

**Technical debt / follow-up:**
- **Release tagging is required and currently missing** — the repository has no
  git tags. `main` is at 4.2, so **`v4.2` should be tagged now**; every future
  merge-to-`main` gets its `vN` tag. Tag creation is a maintainer git action,
  outside this ADR.

---

## 5. Applicable NFRs

None. This ADR defines a process/versioning convention, not a runtime NFR.

---

## 6. References

- [ADR-004](ADR-004-repository-partition-v2.md) — the two-tree partition and the
  "release loop" this ADR fixes the numbering and git-flow for.
- Repo-root [`README.md`](../../README.md) — the visible expression (version line
  + "Two trees" table) updated in the same change that introduces this ADR.
- Related maintainer-internal ADRs: **ADR-002** (defect classification),
  **ADR-005** (removal-completeness sweep).

---

## 7. HITL-ADR-Approval

> **HITL-ADR-Approval** (Avenga DevFlow §2.8, §3.0, §3.5). An ADR does not become
> `accepted` — and therefore governing — without the approval of an Architect /
> Tech Lead. This ADR is the source of truth for its own approval (recorded in
> the `review` frontmatter block). ADR approvals are never copied to the Bolt
> manifest.

| Field | Value |
|-------|-------|
| **Architect / Tech Lead** | eugenio.serrano |
| **Role** | architect / tech_lead |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-22T13:11:17-03:00` |
| **review.started_at** | `2026-08-22T13:29:53-03:00` |
| **review.decided_at** | `2026-08-22T13:29:53-03:00` |
| **Findings** | none — `acknowledged_without_comment: true` (see frontmatter) |
