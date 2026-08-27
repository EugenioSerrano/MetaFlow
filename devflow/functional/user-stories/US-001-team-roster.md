---
id: "US-001"
title: "Team roster — declare members and roles so approval routing resolves against real people"
date: "2026-08-21"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "deprecated" # draft | approved | deprecated — superseded by the US-022/US-024 family (2026-08-23): the human-only roster is absorbed as a special case of the unified actors roster
owner: "eugenio.serrano" # Functional Analyst (governs this US)
unit: ""
story_points: 3 # proposed; confirmed at HITL-US-Approval (§2.6)
adrs: []
sources:
  - "devflow/reviews/REV-001-hitl-checkpoint-role-inventory.md"
stakeholders: []
tags: ["roles", "routing", "hitl", "kit-family"]
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

# US-001 — Team roster: declare members and roles so approval routing resolves against real people

| Field          | Value |
|----------------|-------|
| **Unit**       | — |
| **ADRs**       | — |
| **Status**     | ⛔ **deprecated (2026-08-23)** — superseded by the DevFlow Agents family: US-022 (Actor concept) and US-024 (unified actors roster). **Its ACs are absorbed as a special case** in the kit's roster docs (the "Single-maintainer / human-roster guarantees" section of `distribution-kit/devflow/actors/README.md`): external reviewers, optionality, migration travel and living data. Never approved (draft); no recorded decision affected (G36). |
| **Story points** | 3 (proposed — never confirmed) |

**As an** adopting team, **I want** to declare my members and their roles in
a team roster, **so that** HITL approval routing resolves against real people
and teams of any size can identify approvers — including external reviewers.

## 1. Acceptance criteria

- **Given** a project that ships with the roster family, **When** the team fills in person → roles, **Then** the roster is the resolvable reference for every named-role checkpoint.
- **Given** an approval rule that names a role, **When** the agent (or a human) needs the approver, **Then** the roster returns the people holding that role without ambiguity.
- **Given** a single-maintainer team, **When** no local member holds a required role, **Then** the roster may name an external reviewer to fill it.
- **Given** a team with full role coverage, **When** the roster is empty or unused, **Then** the methodology behaves exactly as today (roster is optional).
- **Given** a methodology upgrade, **When** the project migrates, **Then** the roster family travels with the migration (§5.15 routing covers it).
- **Given** the roster exists, **When** a member joins or leaves, **Then** updating the roster requires no approval (living data, not a decision).

## 2. Notes / to refine before approval

- G29 was already relaxed in `US-000.BOLT-002` (any member may approve
  non-critical non-functional BUGs) — the roster is therefore the **optional
  resolution layer**, not a blocker fix.
- Design open points: file vs folder (`devflow/team/` vs a single
  `TEAM.md`-style file), schema of the person→roles mapping, and how the
  four agents are told to read it (4-file sync).
- Related REV-001 findings: F-05 (role multiplicity declared), and the
  external-reviewer idea covers the small-team gap documented in F-02..F-04.
