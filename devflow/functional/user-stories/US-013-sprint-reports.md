---
id: "US-013"
title: "Sprint reports — generate reports at any moment, mid-sprint"
date: "2026-08-21"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "draft" # draft | approved | deprecated
owner: "eugenio.serrano" # Functional Analyst (governs this US)
unit: ""
story_points: 5 # proposed; confirmed at HITL-US-Approval (§2.6)
adrs: []
sources:
  - "distribution-kit/devflow/reports/README.md"
  - "tools/reporter/DESIGN.md"
  - "maintainer product direction (2026-08-21)"
stakeholders: []
tags: ["reports", "dora", "metrics", "sprints"]
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

# US-013 — Sprint reports: generate reports at any moment, mid-sprint

| Field          | Value |
|----------------|-------|
| **Unit**       | — |
| **ADRs**       | — |
| **Status**     | draft |
| **Story points** | 5 (proposed) |

**As a** project manager, **I want** to generate sprint progress reports at
any moment — mid-sprint included, **so that** delivery, quality and review
latency are visible whenever they are needed, not only at sprint close.

## 1. Acceptance criteria

- **Given** manifests and sprint definitions, **When** the report is
  requested, **Then** `REPORT-YYYY-Www.html` is generated immediately.
- **Given** a mid-sprint state, **When** the report runs, **Then** it
  reflects the current state of the sprint (partial data included).
- **Given** the report spec, **When** any number is computed, **Then** its
  derivation matches `reports/README.md` (DORA Five, HITL coverage, review
  latency, AI usage).
- **Given** the report output, **When** published, **Then** it is a derived
  artifact (never citable as governed evidence, §5.12 class).

## 2. Notes / to refine before approval

- Depends on US-002 (sprints planning data) and US-009 (reporter tool).
- The template and the report README exist; the missing piece is the
  generator + the sprint data layer.
