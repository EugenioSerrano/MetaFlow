---
id: "AREV-002"
title: "Single-operator sweep — remaining HITL blockers, methodology/agent contradictions, and the one-role operability criterion"
date: "2026-08-21"
author: "eugenio.serrano"
llm: "claude-fable-5"
type: "themed"
focus: "other"
implementor_model: "N/A"
spec_reviewed: "N/A"
bolt: "N/A"
governing_adrs:
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
  - "devflow/adrs/ADR-002-documentation-defect-classification.md"
status: "closed"
requested_by: "eugenio.serrano — same objective as AREV-001, next pass: find places where the methodology or the agents contradict each other about the known blockers, and any blocker still present at an HITL checkpoint that stops an actor from doing their work. New explicit criterion: the whole methodology must be executable by ONE single role approving every HITL — role descriptions are kept as guidance and information, never as blockers. Must NOT repeat AREV-001's confirmed findings."
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs, and section
  headings (##) stay in English (the schema). All prose — descriptions,
  motivation, findings — goes in the project's content_language (en,
  declared in devflow/LANGUAGE).

  ⚠️ SEQUENTIAL PHASE APPROVALS (§2.15, §3.0): each phase remains DRAFT
  until its named human checkpoint is approved. The next phase cannot
  begin until the current one is approved. AREV approvals and verdicts
  are recorded ONLY in these AREV artifacts — never in the Bolt manifest.
  Agent/model selection between phases is a MANUAL human action (§3.13).
-->

# AREV-002 — Single-operator sweep

> **Note:** This file is an index for the AREV. The debate documents are in
> `01-CRITIQUE.md`, `02-DEFENSE.md` and `03-VERDICT.md` within this folder.

| Field | Value |
|-------|-------|
| **Type** | themed |
| **Focus** | other (governance / single-operator HITL satisfiability) |
| **Bolt** | N/A |
| **SPEC reviewed** | N/A (themed, not Bolt-bound) |
| **Implementor model** | N/A |
| **Status** | closed (all findings routed — 2026-08-22) |
| **Requested by** | eugenio.serrano — remaining blockers + methodology/agent contradictions + one-role operability criterion (see frontmatter) |
| **Scope** | Every distributable text that gates an HITL checkpoint or defines the AREV/UAT machinery: `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md` (§2.15, §3.0, §3.11, §3.13, §3.15), `GUARDRAILS.md` (checkpoint map, G25, G37, acceptance table), `ONBOARDING.md`, the four agent definitions, and the `tests/uat/` and `adversarial-reviews/` templates. The installed root `devflow/` is read as a mirror reference only — never edited (ADR-004). |
| **Reference sources** | None external — review based on the distributable artifacts and the repository's governance records exclusively: AREV-001 (Verdict approved 2026-08-21 — governed input, deliberately NOT re-found here), REV-001, US-014, SPEC-260821-0108, ADR-002, ADR-004 |

## 1. Motivation

AREV-001 (Verdict approved, FAIL) confirmed the role-availability blocker
family and routed it: the stale BUG-route copies to a BUG (ADR-002 class 1),
and the F-02..F-07 family to US-014 → ADR family → kit Bolt(s). The
stakeholder now raises the bar with a second pass and an explicit design
criterion: **the entire methodology must be executable by one single person
approving every HITL checkpoint** — role descriptions remain as guidance,
never as gates.

This AREV sweeps for what AREV-001 did **not** catalogue: single-role routes
missing from the routed enumeration, contradictions inside the methodology
or between the methodology and the agents about the blocking machinery
itself, and dead ends in the governance mechanisms (AREV, UAT/UNIT) that
close on a single operator. Per the stakeholder's explicit instruction,
**nothing already confirmed by AREV-001 is re-found here** — those findings
are governed input, referenced only.

## 2. Phases (all three mandatory, sequential — each stops at its approval)

| Phase | Document | Model (manually selected) | Status | Approval |
|-------|----------|---------------------------|--------|----------|
| ① Critique | [01-CRITIQUE.md](01-CRITIQUE.md) | claude-fable-5 (Challenger — manually selected 2026-08-21) | ✅ approved (2026-08-21, eugenio.serrano) | `HITL-AREV-CRITIQUE-Approval` |
| ② Defense | [02-DEFENSE.md](02-DEFENSE.md) | deepseek/deepseek-v4-flash (Defender — manually selected 2026-08-21) | ✅ approved (2026-08-21, eugenio.serrano) | `HITL-AREV-DEFENSE-Approval` |
| ③ Verdict | [03-VERDICT.md](03-VERDICT.md) | claude-opus-4-8 (Judge — manually selected 2026-08-21; ≠ Challenger, ≠ Defender, G37) | ✅ approved (2026-08-21, eugenio.serrano) — **FAIL** | `HITL-AREV-VERDICT-Approval` |

Phase status: `pending` → `in-review` → `approved` / `changes_requested`.
Every initiated AREV runs all three phases (§2.15) — the next phase cannot
begin until the current one is approved.

## 3. Final verdict

**FAIL** (Judge: claude-opus-4-8 — [03-VERDICT.md](03-VERDICT.md), in-review
pending `HITL-AREV-VERDICT-Approval`). One confirmed 🔴 (F-02 — the AREV
mechanism dead-ends for a single operator with two models: G25 mandatory
phases + §3.13 unsatisfiable human-arbiter identity + no `cancelled` state in
the §3.15 AREV row), two confirmed 🔶 (F-01 incomplete single-role
enumeration; F-04 operability principle stated nowhere), one reclassified 🔶
(F-03 UAT/UNIT sequencing — latent block + text divergence; suspended today
by G20 and the UAT README), one observation ⚠️ (F-05), one compliant ✅
(F-06). Only an approved Verdict produces actionable findings.

## 4. HITL phase approvals

> Recorded in each phase document's `review` block (§3.0). The AREV keeps
> its own approval evidence; nothing is written to the Bolt manifest.

## 5. Findings routing (closure, 2026-08-22)

All findings of the approved Verdict routed to their own artifacts (each
follows its own lifecycle and HITL approval). AREV set to `closed`.

| Finding | Sev. | Routed to |
|---------|------|-----------|
| F-01 — incomplete single-role enumeration | 🔶 | [US-014](../../functional/user-stories/US-014-role-availability-policy.md) §3 (completeness checklist) |
| F-02 — AREV dead-ends for a single operator | 🔴 | US-014 D5 (≥3 models, no human arbiter, `cancelled` state) |
| F-03 — UAT/UNIT sequencing (latent block + text divergence) | 🔶 | [US-015](../../functional/user-stories/US-015-unit-governance.md) (interim removal + reintroduction) |
| F-04 — operability principle absent | 🔶 | US-014 D1 |
| F-05 — escalation/demo forms | ⚠️ | No action (observation) |
| F-06 — compliant boundary | ✅ | No action (compliant) |
