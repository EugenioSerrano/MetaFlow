---
id: "US-011"
title: "status tool — walk the documents and report their state"
date: "2026-08-21"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "draft" # draft | approved | deprecated
owner: "eugenio.serrano" # Functional Analyst (governs this US)
unit: ""
story_points: 3 # proposed; confirmed at HITL-US-Approval (§2.6)
adrs: []
sources:
  - "tools/status/DESIGN.md"
stakeholders: []
tags: ["tool", "status", "metrics"]
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

# US-011 — status tool: walk the documents and report their state

| Field          | Value |
|----------------|-------|
| **Unit**       | — |
| **ADRs**       | — |
| **Status**     | draft |
| **Story points** | 3 (proposed) |

**As a** DevFlow user, **I want** a command that walks the governed
documents and reports each one's state, **so that** answering "which BUGs
are still `draft`?" costs one command instead of reading every file.

## 1. Acceptance criteria

- **Given** a folder of governed documents, **When** the status tool runs,
  **Then** it reads each document's frontmatter and returns its state.
- **Given** a mixed-status folder, **When** filtered, **Then** the tool
  groups by status (e.g. draft / approved / closed).
- **Given** the tool, **When** run over the repository, **Then** it is
  cheap for a program and fast for a human.

## 2. Notes / to refine before approval

- DESIGN.md: the whole job is walking documents and returning the state each
  one already records — no state derivation beyond the frontmatter.
