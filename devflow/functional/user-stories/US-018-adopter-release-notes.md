---
id: "US-018"
title: "Adopter-facing release notes — AvengaDevFlow-Release-Notes.md digest in the kit root"
date: "2026-08-21"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "draft" # draft | approved | deprecated
owner: "eugenio.serrano" # Functional Analyst (governs this US)
unit: ""
story_points: 2 # proposed; confirmed at HITL-US-Approval (§2.6)
adrs: []
sources:
  - "maintainer product direction (2026-08-21)"
stakeholders: []
tags: ["release", "adopters", "kit", "communication"]
review_ready_at: ""
review: # HITL-US-Approval — filled by the human reviewer (§3.0)
  decision: ""
  reviewers: []
  started_at: ""
  decided_at: ""
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: ""
---

# US-018 — Adopter-facing release notes: AvengaDevFlow-Release-Notes.md digest in the kit root

| Field          | Value |
|----------------|-------|
| **Unit**       | — |
| **ADRs**       | — |
| **Status**     | draft |
| **Story points** | 2 (proposed) |

**As an** adopting team, **I want** a small, clearly-named file at the kit
root that tells me what improved in each DevFlow release — in plain terms,
not a full history — **so that** I know what changed when I upgrade, without
diffing the entire kit.

---

## 1. The problem (explained, complete)

### What exists today

- The framework's `CHANGELOG.md` lives at the **methodology repository
  root** and stopped shipping inside the kit in 4.2 (the distributable no
  longer carries it).
- The §5.16 migration procedure describes *how* to migrate (rename, copy,
  merge, reconcile) but never presents *what changed*.
- Today, an adopter upgrading from 4.2 to 4.3 has **no way to know what
  changed** except diffing the whole kit. Concrete example from the
  2026-08-21 session: the G29 relaxation (non-critical non-functional BUGs
  approvable by any member) and the new `devflow/prompts/` family shipped in
  the kit with **zero visibility** for adopters until they diff.

### Why a dedicated file, and why this name

- The adopting project already has its **own** release notes / changelog at
  its repository root (`RELEASE.md`, `CHANGELOG.md`, etc.). A file named
  `CHANGELOG.md` or `RELEASES.md` in the kit would land at the adopter's
  root and **collide with or be confused with their own**.
- Naming it `AvengaDevFlow-Release-Notes.md` (prefixed, unambiguous) makes
  the owner obvious: this is *DevFlow's* notes, not the project's.
- Location: kit root → adopter project root, next to `AGENTS.md` and
  `CLAUDE.md`. On migration the file is **overwritten by the new version**
  (pure framework content, same class as `CLAUDE.md` — not merged at a
  marker).

### Design: a digest, not a history

The file is intentionally **simplified**:

- Per release, four compact sections: **New** · **Changed** · **Removed** ·
  **Migration notes** — plain-language bullets for adopters (10–15 max per
  release).
- **Not a full history:** the digest keeps only the **latest 2–3 releases**
  (so an adopter jumping two versions still sees the delta); older entries
  are dropped on each version bump. Full history remains the framework's
  own `CHANGELOG.md` and git history.
- Each section states the *user-visible effect*, not the internal detail
  (e.g. "non-critical non-functional BUGs can now be approved by any team
  member, author included" — not "G29 row rewritten").

---

## 2. Acceptance criteria

- **Given** the kit, **When** it ships, **Then** the root contains
  `AvengaDevFlow-Release-Notes.md` (prefixed name — no collision with the
  adopter's own release notes).
- **Given** a release, **When** its notes are written, **Then** they follow
  the four-section digest format (New / Changed / Removed / Migration notes)
  in plain language, with a bounded number of bullets.
- **Given** an upgrade, **When** the adopter reads the file, **Then** they
  can identify what affects them (new families, rule changes, migration
  steps) without diffing the kit.
- **Given** a version bump, **When** the release closes, **Then** the notes
  for the new version are added and entries older than 2–3 versions back are
  dropped (digest stays small — no full history accumulates).
- **Given** the §5.16 migration, **When** the adopter migrates, **Then** the
  procedure references reading `AvengaDevFlow-Release-Notes.md` as the
  first step.
- **Given** the file's nature, **When** an adopter migrates, **Then** the
  file is replaced by the new version's (never merged, never carries
  project content).

## 3. Notes / to refine before approval

- **Origin:** maintainer direction after the 2026-08-21 session — adopters
  had no visibility of the G29 relaxation and the prompts family shipping
  in the kit; the framework CHANGELOG stopped shipping in 4.2.
- **Related backlog:** US-016 (audit tool) — the version-marker sweep list
  and the release-notes update are both release-closing steps; the bump
  procedure (AGENTS.md) gains one line for the notes file. US-017 (tooling
  distribution) also describes release-closing mechanics.
- **Open design points:**
  - ~~Keep only the latest release vs. the latest two~~ → **resolved: keep
    the latest 2–3 versions back** (maintainer decision), so jump upgrades
    still show the delta without accumulating a history.
  - Whether the file carries a version marker (proposal: no — it *describes*
    versions, it is not stamped; the marker sweep list stays unchanged).
  - Whether each bullet should carry a link to the relevant §/family in the
    new methodology (nice-to-have; proposal: yes for New/Changed items).
  - Who writes it: the release migration step, so it is written when the
    version closes (proposal: written as part of the release loop, reviewed
    like any product change).
- **Scope note:** this is the *adopter-facing digest*. The framework's own
  governance history (`CHANGELOG.md` at the methodology repo root) is
  untouched and stays out of the distributable.
