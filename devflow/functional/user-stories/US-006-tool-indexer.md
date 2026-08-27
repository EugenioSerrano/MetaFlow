---
id: "US-006"
title: "indexer tool — keep every INDEX true to its folder"
date: "2026-08-21"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "draft" # draft | approved | deprecated
owner: "eugenio.serrano" # Functional Analyst (governs this US)
unit: ""
story_points: 3 # proposed; confirmed at HITL-US-Approval (§2.6)
adrs: []
sources:
  - "tools/indexer/DESIGN.md"
stakeholders: []
tags: ["tool", "index", "traceability"]
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

# US-006 — indexer tool: keep every INDEX true to its folder

| Field          | Value |
|----------------|-------|
| **Unit**       | — |
| **ADRs**       | — |
| **Status**     | draft |
| **Story points** | 3 (proposed) |

**As a** DevFlow user, **I want** an `INDEX.md` rebuild tool, **so that**
ID allocation never drifts — an artifact created and never indexed, or a
`status` changed and never reflected, can no longer corrupt the next
sequential number (N02–N04, §5.15).

## 1. Acceptance criteria

- **Given** a folder with artifacts, **When** the indexer runs, **Then** it
  rebuilds the folder's `INDEX.md` rows from the artifacts' frontmatter.
- **Given** a `status` change in an artifact, **When** the indexer runs,
  **Then** the INDEX row reflects the new status.
- **Given** an artifact that was never indexed, **When** the indexer runs,
  **Then** it appears in its folder's INDEX.

## 2. Notes / to refine before approval

- Covers ordinary drift (artifact never indexed, status not reflected) as
  described in DESIGN.md; the §5.15 rule that the INDEX is where the next
  `NNN` is claimed is the invariant being protected.
