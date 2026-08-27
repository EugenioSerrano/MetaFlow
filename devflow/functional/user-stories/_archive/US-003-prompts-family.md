---
id: "US-003"
title: "Prompts family — canonical devflow/prompts/ folder for versioned, team-shared prompts"
date: "2026-08-21"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved" # draft | approved | deprecated
owner: "eugenio.serrano" # Functional Analyst (governs this US)
unit: ""
story_points: 2 # confirmed at HITL-US-Approval (§2.6)
adrs: []
sources:
  - "maintainer product direction (2026-08-21)"
stakeholders: []
tags: ["prompts", "kit-family", "agents"]
review_ready_at: "2026-08-21T01:48:07-03:00"
review: # HITL-US-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers:
    - user: "eugenio.serrano"
      role: "functional_analyst"
  started_at: "2026-08-21T01:48:07-03:00"
  decided_at: "2026-08-21T01:48:07-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "US and ACs reviewed against the maintainer's stated intent: a standalone adopter-facing devflow/prompts/ family for creating, modifying and improving team-shared prompts with sequential PROMPT-NNN numbering, no approval and no manifest (copy-paste usage), plus the proposed template and the four-agent wording. ACs are verifiable and the scope boundaries (not the product prompts/ tree) are explicit. Story points 2 confirmed."
---

# US-003 — Prompts family: canonical devflow/prompts/ folder for versioned, team-shared prompts

| Field          | Value |
|----------------|-------|
| **Unit**       | — |
| **ADRs**       | — |
| **Status**     | draft |
| **Story points** | 2 (proposed) |

**As an** adopting team, **I want** a canonical `devflow/prompts/` folder
where we **create, modify and improve** our prompts as needs arise, **so
that** the team shares them through the repository and keeps version control
of them in the same place — instead of scattering them across `agents-data/`.

## 1. Acceptance criteria

- **Given** the kit, **When** a project wants a prompt — new, modified or
  improved — **Then** it has a canonical `devflow/prompts/` family with a
  template, README and INDEX.
- **Given** a new prompt, **When** it is created, **Then** it is named with
  sequential numbering like the US family (`PROMPT-NNN-<description>.md`).
- **Given** an existing prompt, **When** the team asks the agent to modify
  or improve it, **Then** the updated version lands back in the same folder,
  never in `agents-data/`.
- **Given** a prompt in the folder, **When** the team works with it, **Then**
  it is shared and version-controlled through the repository (the folder is
  committed like any other project file).
- **Given** a prompt file, **When** someone uses it, **Then** its body is
  copied and pasted directly into the agent — no approval, no manifest, no
  governance ceremony (prompts are living data).
- **Given** the four agent definitions, **When** they reference project
  prompts, **Then** they point at `devflow/prompts/` (4-file sync).
- **Given** a methodology upgrade, **When** the project migrates, **Then**
  the prompts family travels with the migration (§5.15 routing covers it).

## 2. Notes / to refine before approval

- **Scope confirmed with the maintainer:** adopter-facing prompts family in
  the kit — **not** the product `prompts/` tree of this repository, which
  stays untouched. The family is standalone: it has no functional relation
  to the other folders; its only job is to hold the project's prompts.
- **Naming proposal:** sequential `PROMPT-NNN-<description>.md` (like US
  numbering) — expected volume is small.
- **No approval, no manifest:** prompts are files users copy-paste into
  agents; version control is the repository's git history.
- **Template proposal (super-simple, copy-paste ready):**

  ```markdown
  # PROMPT-NNN — [short name]

  [optional one-line description: what this prompt is for]

  [the prompt body — copy and paste into the agent as-is]
  ```

  The folder README explains the convention: title + optional one-liner +
  body; the INDEX lists `PROMPT-NNN` + short name.

- **Four-agent wording proposal** (one sentence appended to the shared-body
  §5.12 working-data paragraph, byte-identical across the four):

  > Project prompts live in `devflow/prompts/` (`PROMPT-NNN-<description>.md`):
  > versioned, team-shared, copy-paste ready. Create, modify or improve them
  > there on request; never leave prompts scattered in `agents-data/`.
  > Prompts carry no approval and no manifest.

- Design open points: ordering within the folder (alphabetical vs numeric),
  and whether the folder README lives in the kit or is project-authored.



---

## 3. Bolts

| # | Bolt | Type | Layer | Description | Est. active delivery |
|---|------|------|-------|-------------|----------------------|
| 1 | [BOLT-001](../bolts/US-003.BOLT-001-prompts-family.md) | functional | Documentation | Ship the devflow/prompts/ family in the kit: template, README, INDEX, PROMPT-NNN naming, no-approval semantics, four-agent wording, �5.15 routing | ~3h |

> Plausibility check (�2.6): 2 SP ? 1�2 Bolts � one Bolt is within band.

---

## 4. HITL-US-Approval

> **Avenga DevFlow �2.6, �3.0.** This feature US was approved by a Functional
> Analyst (recorded in the eview frontmatter block) on 2026-08-21. Only
> now may it be decomposed into candidate functional Bolts. US-000 is
> outside this lifecycle.
