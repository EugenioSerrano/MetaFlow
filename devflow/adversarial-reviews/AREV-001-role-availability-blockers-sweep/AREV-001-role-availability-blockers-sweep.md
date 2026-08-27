---
id: "AREV-001"
title: "Role-availability blockers and routing drift sweep across the distributable methodology"
date: "2026-08-21"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
type: "themed"
focus: "other"
implementor_model: "N/A"
spec_reviewed: "N/A"
bolt: "N/A"
governing_adrs:
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
  - "devflow/adrs/ADR-002-documentation-defect-classification.md"
status: "closed"
requested_by: "eugenio.serrano — sweep the whole distributable methodology (including the four agent definitions) for approval routing that blocks work because a named role has no holder or is unavailable. Role descriptions stay as-is; hard role-availability blocks must be removed (pending the US-014 team-description decision)."
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

# AREV-001 — Role-availability blockers and routing drift sweep

> **Note:** This file is an index for the AREV. The debate documents are in
> `01-CRITIQUE.md`, `02-DEFENSE.md` and `03-VERDICT.md` within this folder.

| Field | Value |
|-------|-------|
| **Type** | themed |
| **Focus** | other (governance / role routing) |
| **Bolt** | N/A |
| **SPEC reviewed** | N/A (ad-hoc, not Bolt-bound) |
| **Implementor model** | N/A |
| **Status** | closed (all findings routed — 2026-08-22) |
| **Requested by** | eugenio.serrano — remove role-availability blockers from the distributable methodology |
| **Scope** | Every distributable text that defines approval routing: `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md`, `distribution-kit/devflow/GUARDRAILS.md`, `distribution-kit/devflow/README.md`, `distribution-kit/devflow/ONBOARDING.md`, the four agent definitions (`CLAUDE.md`, `.agents/skills/avenga-devflow/SKILL.md`, `.github/agents/AvengaDevFlow.agent.md`, `.opencode/agents/AvengaDevFlow.md`), and the `devflow/` templates and folder READMEs (BUG, Bolt, US, TC, SPEC, MEM, ADR, UAT, RISK). The installed root `devflow/` is read as a mirror reference only — it is never edited (ADR-004). |
| **Reference sources** | None external — review based on the distributable artifacts, REV-001, SPEC-260821-0108, US-014 and the active ADRs (ADR-002, ADR-004) exclusively |

## 1. Motivation

REV-001 (approved) classified four role-availability blockers (F-02..F-05) and
one counting gap (F-06) as a single decision family routed to US-014. One of
them (F-02, the non-critical non-functional BUG route) was already relaxed by
SPEC-260821-0108 / US-000.BOLT-002 — but the sweep behind that change only
searched for the new phrasing, so stale copies of the old route survive in the
normative source, the four agents, the README and the traceability rules.

The stakeholder now asks for a **complete sweep**: find every place where an
approval route is a hard block because it requires a named role (Architect,
Tech Lead, Functional Analyst, QA, Sec, SRE, domain owner, Stakeholders) that
may not exist in the team. The role descriptions themselves stay — only the
hard requirement that "this person must come and approve this artifact" is a
blocker and must go, replaced by an explicit satisfiable routing once US-014
decides the team-description policy.

## 2. Phases (all three mandatory, sequential — each stops at its approval)

| Phase | Document | Model (manually selected) | Status | Approval |
|-------|----------|---------------------------|--------|----------|
| ① Critique | [01-CRITIQUE.md](01-CRITIQUE.md) | deepseek/deepseek-v4-flash (Challenger) | ✅ approved (2026-08-21, eugenio.serrano) | `HITL-AREV-CRITIQUE-Approval` |
| ② Defense | [02-DEFENSE.md](02-DEFENSE.md) | claude-fable-5 (Defender — manually selected 2026-08-21) | ✅ approved (2026-08-21, eugenio.serrano) | `HITL-AREV-DEFENSE-Approval` |
| ③ Verdict | [03-VERDICT.md](03-VERDICT.md) | claude-opus-4-8 (Judge — manually selected 2026-08-21; ≠ Challenger, ≠ Defender, G37) | ✅ approved (2026-08-21, eugenio.serrano) — **FAIL** | `HITL-AREV-VERDICT-Approval` |

Phase status: `pending` → `in-review` → `approved` / `changes_requested`.
Every initiated AREV runs all three phases (§2.15) — the next phase cannot
begin until the current one is approved.

## 3. Final verdict

**FAIL** (Judge: claude-opus-4-8 — [03-VERDICT.md](03-VERDICT.md), in-review
pending `HITL-AREV-VERDICT-Approval`). Four confirmed 🔴 (F-01 stale BUG-route
copies; F-02 untracked `critical` NF BUG route; F-03 MEM approver counts; F-04
acceptance SRE/Sec pairing), two confirmed 🔶 (F-05 two-role TC; F-07 SPEC
counting convention), one reclassified 🔶 (F-06 single-role gates — dependent
on the role-multiplicity policy), two compliant ✅ (F-08, F-09). Only an
approved Verdict produces actionable findings.

## 4. HITL phase approvals

> Recorded in each phase document's `review` block (§3.0). The AREV keeps
> its own approval evidence; nothing is written to the Bolt manifest.

## 5. Findings routing (closure, 2026-08-22)

All findings of the approved Verdict routed to their own artifacts (each
follows its own lifecycle and HITL approval). AREV set to `closed`.

| Finding | Sev. | Routed to |
|---------|------|-----------|
| F-01 — stale BUG-route copies | 🔴 | [BUG-001](../../bugs/BUG-001-stale-bug-route-copies.md) (class-1 defect, ADR-002) |
| F-02 — `critical` NF BUG route (untracked) | 🔴 | [US-014](../../functional/user-stories/US-014-role-availability-policy.md) D3 |
| F-03 — MEM approver counts | 🔴 | US-014 D7 |
| F-04 — acceptance SRE/Sec pairing | 🔴 | US-014 D3 |
| F-05 — two-role TC | 🔶 | US-014 D3 |
| F-06 — single-role gates | 🔶 | US-014 (US/ADR part, D1/D3) · [US-015](../../functional/user-stories/US-015-unit-governance.md) (UNIT/UAT part) |
| F-07 — SPEC counting convention | 🔶 | US-014 D7 |
| F-08 — non-critical relaxation correct | ✅ | No action (compliant) |
| F-09 — identity rules not role blocks | ✅ | No action (kept; excluded from the fallback per US-014 D3) |
