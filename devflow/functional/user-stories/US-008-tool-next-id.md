---
id: "US-008"
title: "next-id tool — the next free sequential number"
date: "2026-08-21"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "draft" # draft | approved | deprecated
owner: "eugenio.serrano" # Functional Analyst (governs this US)
unit: ""
story_points: 3 # proposed; confirmed at HITL-US-Approval (§2.6)
adrs: []
sources:
  - "tools/next-id/DESIGN.md"
stakeholders: []
tags: ["tool", "ids", "naming"]
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

# US-008 — next-id tool: the next free sequential number

| Field          | Value |
|----------------|-------|
| **Unit**       | — |
| **ADRs**       | — |
| **Status**     | draft |
| **Story points** | 3 (proposed) |

**As a** DevFlow user, **I want** the next free sequential `NNN` computed
correctly per folder and per parent scope, **so that** numbers are never
reused, gaps stay gaps, and Bolt numbering stays scoped to its direct parent
(§2.4, §5.15, N02–N04).

## 1. Acceptance criteria

- **Given** a folder's INDEX, **When** asked for the next `NNN`, **Then** the
  tool returns the highest claimed number + 1, never reusing archived IDs.
- **Given** a gap in the sequence, **When** the tool computes the next id,
  **Then** the gap is not filled.
- **Given** Bolt numbering, **When** the tool is scoped to a parent, **Then**
  it respects the parent's own sequence (e.g. `US-000` shared container).

## 2. Notes / to refine before approval

- DESIGN.md: numbers are never reused; gaps are normal and must not be
  filled; Bolt numbering is scoped to its direct parent.
