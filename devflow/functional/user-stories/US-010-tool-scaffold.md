---
id: "US-010"
title: "scaffold tool — create an artifact and its manifest in one step"
date: "2026-08-21"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "draft" # draft | approved | deprecated
owner: "eugenio.serrano" # Functional Analyst (governs this US)
unit: ""
story_points: 5 # proposed; confirmed at HITL-US-Approval (§2.6)
adrs: []
sources:
  - "tools/scaffold/DESIGN.md"
stakeholders: []
tags: ["tool", "scaffold", "g33"]
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

# US-010 — scaffold tool: create an artifact and its manifest in one step

| Field          | Value |
|----------------|-------|
| **Unit**       | — |
| **ADRs**       | — |
| **Status**     | draft |
| **Story points** | 5 (proposed) |

**As an** agent, **I want** to create a governed artifact and its paired
manifest in one step, **so that** the expensive second half — the manifest
that G33 makes mandatory — is never skipped under pressure.

## 1. Acceptance criteria

- **Given** an artifact type, **When** the scaffold runs, **Then** it reads
  the folder README, the `TEMPLATE-*`, the INDEX next number and the
  matching `TEMPLATE-MANIFEST-*.json`, and writes both files with
  consistent frontmatter.
- **Given** the created pair, **When** validated, **Then** the manifest
  validates against its schema and the INDEX row is registered.
- **Given** any governed artifact family, **When** scaffolded, **Then** the
  two files are created in the canonical folders.

## 2. Notes / to refine before approval

- DESIGN.md: highest leverage after the validator — creation today costs
  many reads per artifact, every time.
