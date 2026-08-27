---
id: "US-009"
title: "reporter tool — sprint reports from the manifest family"
date: "2026-08-21"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "draft" # draft | approved | deprecated
owner: "eugenio.serrano" # Functional Analyst (governs this US)
unit: ""
story_points: 5 # proposed; confirmed at HITL-US-Approval (§2.6)
adrs: []
sources:
  - "tools/reporter/DESIGN.md"
  - "distribution-kit/devflow/reports/README.md"
stakeholders: []
tags: ["tool", "reports", "dora", "metrics"]
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

# US-009 — reporter tool: sprint reports from the manifest family

| Field          | Value |
|----------------|-------|
| **Unit**       | — |
| **ADRs**       | — |
| **Status**     | draft |
| **Story points** | 5 (proposed) |

**As a** project manager, **I want** a generator that reads the manifest
family and emits sprint reports, **so that** DORA, HITL-coverage and
review-latency numbers are derived mechanically instead of hand-collected.

## 1. Acceptance criteria

- **Given** a repository with manifests, **When** the reporter runs, **Then**
  it emits `REPORT-YYYY-Www.html` per `TEMPLATE-REPORT.html`.
- **Given** the report spec, **When** a number is computed, **Then** its
  derivation matches the one defined in `reports/README.md` (DORA Five,
  HITL coverage, review latency).
- **Given** sprint planning data, **When** the reporter runs, **Then** it
  consumes it (see US-002) for per-sprint grouping.

## 2. Notes / to refine before approval

- DESIGN.md: planned with the tooling track — a generator existed in the 4.0
  cycle and was pulled before release; this US resumes it.
- Depends on US-002 (sprints data) and US-013 (reports at any moment).
