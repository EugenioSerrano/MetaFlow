---
id: "US-002"
title: "Sprints family — canonical folder for sprint planning data that feeds reports"
date: "2026-08-21"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "draft" # draft | approved | deprecated
owner: "eugenio.serrano" # Functional Analyst (governs this US)
unit: ""
story_points: 3 # proposed; confirmed at HITL-US-Approval (§2.6)
adrs: []
sources:
  - "distribution-kit/devflow/reports/README.md"
  - "maintainer product direction (2026-08-21)"
stakeholders: []
tags: ["sprints", "reports", "kit-family", "planning"]
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

# US-002 — Sprints family: canonical folder for sprint planning data that feeds reports

| Field          | Value |
|----------------|-------|
| **Unit**       | — |
| **ADRs**       | — |
| **Status**     | draft |
| **Story points** | 3 (proposed) |

**As a** project manager, **I want** a canonical `devflow/sprints/` folder
where each sprint records its start and end dates, goal and scope, **so
that** planning data exists in one governed place and progress reports can
be generated from it automatically.

## 1. Acceptance criteria

- **Given** the kit, **When** a project starts a sprint, **Then** it has a
  canonical `devflow/sprints/` family with a template, README and INDEX.
- **Given** a sprint document, **When** it is created, **Then** it records
  start date, end date, goal, and the US/Bolt references in scope.
- **Given** the sprint data and the manifest family, **When** the reporter
  runs, **Then** it derives per-sprint delivery/quality/review-latency
  numbers without hand-collected input.
- **Given** a methodology upgrade, **When** the project migrates, **Then**
  the sprints family travels with the migration (§5.15 routing covers it).

## 2. Notes / to refine before approval

- **Naming proposal:** `devflow/sprints/SPRINT-YYYY-Www.md` (ISO week,
  consistent with `REPORT-YYYY-Www.html`). Alternative: sequential
  `SPRINT-NNN`. To confirm.
- This is a **new canonical family**: G30 requires the kit to declare the
  folder, the template, the §5.15 routing row and the ONBOARDING map.
- Feeds US-013 (sprint reports) and the `reporter` tool (US-009).
- The methodology currently derives reports from `metrics/` manifests only;
  sprints add the planning layer that the report template's data needs.
