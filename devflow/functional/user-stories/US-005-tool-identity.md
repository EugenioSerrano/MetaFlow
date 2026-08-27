---
id: "US-005"
title: "identity tool — one canonical human identifier"
date: "2026-08-21"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "draft" # draft | approved | deprecated
owner: "eugenio.serrano" # Functional Analyst (governs this US)
unit: ""
story_points: 3 # proposed; confirmed at HITL-US-Approval (§2.6)
adrs: []
sources:
  - "tools/identity/DESIGN.md"
stakeholders: []
tags: ["tool", "identity", "traceability"]
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

# US-005 — identity tool: one canonical human identifier

| Field          | Value |
|----------------|-------|
| **Unit**       | — |
| **ADRs**       | — |
| **Status**     | draft |
| **Story points** | 3 (proposed) |

**As a** DevFlow user, **I want** one canonical human identifier shared by
the five fields that name a person, **so that** reviewers, approvers and
owners resolve to the same individual and the four blocking rules that
compare those values (G-rules) hold mechanically.

## 1. Acceptance criteria

- **Given** a human referenced anywhere, **When** the five fields
  (`review.reviewers[].user`, `generation.created_by`,
  `hitl_approvals[].decided_by[].user`, `author:`/`owner:`, and the
  `human:<…>` AREV `judge_model` form) are compared, **Then** they all
  resolve to the same canonical string.
- **Given** a document, **When** it is checked, **Then** any identity
  mismatch across the five fields is reported as an error.
- **Given** the tool, **When** run against a repository, **Then** it
  validates every governed artifact's identity fields.

## 2. Notes / to refine before approval

- DESIGN.md notes this is not cosmetic: four blocking rules compare those
  values — the tool turns the comparison into a mechanical check.
