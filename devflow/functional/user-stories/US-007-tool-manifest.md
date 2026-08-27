---
id: "US-007"
title: "manifest tool — append to the manifest family without breaking it"
date: "2026-08-21"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "draft" # draft | approved | deprecated
owner: "eugenio.serrano" # Functional Analyst (governs this US)
unit: ""
story_points: 5 # proposed; confirmed at HITL-US-Approval (§2.6)
adrs: []
sources:
  - "tools/manifest/DESIGN.md"
stakeholders: []
tags: ["tool", "manifest", "traceability"]
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

# US-007 — manifest tool: append to the manifest family without breaking it

| Field          | Value |
|----------------|-------|
| **Unit**       | — |
| **ADRs**       | — |
| **Status**     | draft |
| **Story points** | 5 (proposed) |

**As a** DevFlow user, **I want** a tool that performs safe append-only
manifest edits, **so that** the manifest family's constraints — append-only
arrays, monotonic timestamps (`created_at ≤ review_ready_at ≤
review_started_at ≤ decided_at`), and the three different shapes (Bolt, US,
TC) — are never broken by a hand edit (§3.12).

## 1. Acceptance criteria

- **Given** a manifest, **When** a lifecycle step completes, **Then** the
  tool appends the entry without rewriting history.
- **Given** timestamps in a manifest, **When** the tool validates them,
  **Then** monotonic ordering is enforced as an error.
- **Given** the three manifest shapes, **When** the tool operates, **Then**
  each validates against its own schema (`manifest-v4-*.schema.json`).

## 2. Notes / to refine before approval

- The design states a hand edit breaks the three constraints easily; the
  tool replaces the error-prone manual append.
