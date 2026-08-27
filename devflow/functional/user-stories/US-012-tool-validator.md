---
id: "US-012"
title: "validator tool — the compiled manifest validator that ships in devflow/bin/"
date: "2026-08-21"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "draft" # draft | approved | deprecated
owner: "eugenio.serrano" # Functional Analyst (governs this US)
unit: ""
story_points: 5 # proposed; confirmed at HITL-US-Approval (§2.6)
adrs: []
sources:
  - "tools/validator/DESIGN.md"
stakeholders: []
tags: ["tool", "validator", "gates", "manifest"]
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

# US-012 — validator tool: the compiled manifest validator that ships in devflow/bin/

| Field          | Value |
|----------------|-------|
| **Unit**       | — |
| **ADRs**       | — |
| **Status**     | draft |
| **Story points** | 5 (proposed) |

**As a** DevFlow user, **I want** the compiled manifest validator available
in `devflow/bin/`, **so that** the `Bolt-manifest-validation` AI-native gate
(§3.6) and the §3.12 timestamp-ordering rule are enforced mechanically in
every adopting project.

## 1. Acceptance criteria

- **Given** a manifest, **When** the validator runs, **Then** it checks
  presence, schema validity and applicable lifecycle decisions (§3.6).
- **Given** timestamps in a manifest, **When** validated, **Then** ordering
  violations are reported as errors (§3.12).
- **Given** the kit, **When** it ships, **Then** the compiled executable
  lives in `devflow/bin/` and the source in `tools/validator/`.

## 2. Notes / to refine before approval

- DESIGN.md: not a new concept — a missing implementation of what §3.6 and
  §3.12 already describe; the implementation lives beside the design.
