---
id: "US-004"
title: "clock tool — repository time, not developer time"
date: "2026-08-21"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "draft" # draft | approved | deprecated
owner: "eugenio.serrano" # Functional Analyst (governs this US)
unit: ""
story_points: 3 # proposed; confirmed at HITL-US-Approval (§2.6)
adrs: []
sources:
  - "tools/clock/DESIGN.md"
stakeholders: []
tags: ["tool", "timestamps", "clock"]
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

# US-004 — clock tool: repository time, not developer time

| Field          | Value |
|----------------|-------|
| **Unit**       | — |
| **ADRs**       | — |
| **Status**     | draft |
| **Story points** | 3 (proposed) |

**As a** DevFlow user, **I want** timestamps resolved against a single
repository time source, **so that** artifact ordering matches chronology
across time zones (W04/N05/N06: no invented timestamps, RFC 3339 with
seconds + offset, and `SPEC-`/`MEM-` filename `HHmm` read in the same offset
as `generation.created_at`).

## 1. Acceptance criteria

- **Given** a SPEC or MEM filename, **When** its `HHmm` is checked, **Then**
  it is consistent with the artifact's own `generation.created_at` offset.
- **Given** any timestamp the methodology records, **When** it is emitted,
  **Then** it is RFC 3339 with seconds and zone designator, never invented.
- **Given** a multi-timezone team, **When** two members create artifacts,
  **Then** the alphabetical order of filenames matches chronological order.

## 2. Notes / to refine before approval

- DESIGN.md states it **requires a methodology change** — impact on N05/N06
  and W04 must be mapped during refinement.
- Architecture decisions for the implementation belong in an ADR when the
  US reaches Bolt stage.
