---
id: "BUG-001"
title: "Stale copies of the old non-functional BUG-approval route contradict the relaxed G29 rule"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
severity: "medium"            # critical | high | medium | low
nature: "non-functional"      # functional | non-functional — determines approval route and Bolt parent
status: "closed"              # draft | approved | in-fix | fixed | closed
owner: "eugenio.serrano"      # drafted this BUG
detected_in: "arev"           # surfaced by AREV-001 (Verdict approved)
detected_at: "2026-08-22T00:04:45-03:00"
incident_ref: ""
affected_artifacts:
  - "distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md"       # §3.0 prose (~1410-1414)
  - "distribution-kit/CLAUDE.md"                                       # HITL table, HITL-BUG-Approval row
  - "distribution-kit/.agents/skills/avenga-devflow/SKILL.md"         # HITL table row
  - "distribution-kit/.github/agents/AvengaDevFlow.agent.md"          # HITL table row
  - "distribution-kit/.opencode/agents/AvengaDevFlow.md"              # HITL table row
  - "distribution-kit/devflow/README.md"                              # checkpoint map (~248)
  - "distribution-kit/devflow/GUARDRAILS.md"                          # T02 (~230)
expected_result: "Every location that defines the non-functional BUG approval route states the relaxed G29 rule (severity: critical -> Architect/TL; high|medium|low -> any team member, author included), consistently, per SPEC-260821-0108."
actual_result: "The §3.0 prose, the four agents' HITL tables, the README checkpoint map and GUARDRAILS T02 still carry the pre-relaxation wording (\"Developer other than the BUG's own owner\", \"Developer≠author\", \"never the artifact's own owner/author\") — contradicting G29, the §3.0 table and §2.16 in the same documents. The four agents contradict themselves (relaxed G29 row vs stale HITL-table row)."
bolt: "US-000.BOLT-004"        # dedicated Bolt (created after HITL-BUG-Approval)
spec: "SPEC-260822-0018"
mem: "MEM-260822-0027-complete-g29-sweep.md"
sources:
  - "devflow/adversarial-reviews/AREV-001-role-availability-blockers-sweep/03-VERDICT.md"
  - "devflow/spec/SPEC-260821-0108-relax-non-critical-bug-approval-routing.md"
  - "devflow/adrs/ADR-002-documentation-defect-classification.md"
review_ready_at: ""
review: # HITL-BUG-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "developer"}]
  started_at: "2026-08-22T00:14:36-03:00"
  decided_at: "2026-08-22T00:14:36-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Confirmed as a real class-1 documentation defect (ADR-002): the relaxed G29 rule (SPEC-260821-0108) is contradicted by stale copies in the kit §3.0 prose, the four auto-loaded agents' HITL tables, the README checkpoint map and GUARDRAILS T02 — verified by AREV-001 F-01 (Verdict approved). Non-functional, severity medium → any team member, the author included, may approve (relaxed G29 route). Routed to its one dedicated Bolt US-000.BOLT-004."
tags: ["governance", "g29", "bug-routing", "drift", "documentation-defect", "arev-001"]
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs, and section
  headings (##) stay in English (the schema). All prose in content_language
  (en, declared in devflow/LANGUAGE).

  ⚠️ BUG lifecycle (§2.16, §3.3.1): a BUG remains DRAFT until
  HITL-BUG-Approval. Only then may its EXACTLY ONE dedicated Bolt be created
  (non-functional → US-000). This is a class-1 documentation defect (ADR-002):
  the reproduction "test" is deterministic grep/diff before→after, not a
  runtime test. Production (kit) text may not change before red evidence.
-->

# BUG-001 — Stale copies of the old non-functional BUG-approval route contradict the relaxed G29 rule

| Field              | Value |
|--------------------|-------|
| **Severity**       | medium |
| **Nature**         | non-functional |
| **Detected in**    | arev (AREV-001, Verdict approved) |
| **Status**         | closed (fixed via US-000.BOLT-004, Done) |
| **Affected files** | kit methodology §3.0 prose, the four agent definitions, README, GUARDRAILS T02 |
| **Dedicated Bolt** | [US-000.BOLT-004](../functional/bolts/US-000.BOLT-004-complete-g29-sweep.md) |

## 1. Summary

SPEC-260821-0108 (US-000.BOLT-002, Done) relaxed G29 so a non-functional BUG
with `severity: high|medium|low` may be approved by any team member, the
author included. The relaxation sweep missed several locations, which still
carry the pre-relaxation route — so the distributable now **contradicts
itself** about who may approve a non-functional BUG.

---

## 2. Reproduction

Deterministic (class-1 documentation defect — grep/diff, not runtime):

1. In `distribution-kit/`, grep for the stale wording: `Developer≠author`,
   `other than the BUG's own`, `never the artifact's own`.
2. Compare against the relaxed rule in the same documents (G29 row, §3.0
   table, §2.16).

**Expected result:** zero stale matches; every BUG-route statement reads the
relaxed rule (SPEC-260821-0108).

**Actual result:** stale matches remain in the §3.0 prose (~1410–1414), the
four agents' HITL-`HITL-BUG-Approval` rows, the README checkpoint map (~248)
and GUARDRAILS T02 (~230) — each contradicting the relaxed G29 row that sits
in the same file.

---

## 3. Root cause

The SPEC-260821-0108 sweep searched only for the **new** phrasing ("author
included") and its file inventory omitted these locations; the stale phrase
also breaks across a line in the methodology (~1412–1413), so a single-line
grep for it returns nothing, and the compact notations ("Developer≠author",
T02's "never the artifact's own owner/author") were not in the search
patterns. Confirmed by AREV-001 (F-01, CONFIRMED 🔴; the Defense corrected
this root cause with verified evidence).

---

## 4. Impact

- **Users affected:** any agent or human reading the stale passages — the four
  agent files are auto-loaded every turn and contradict themselves.
- **Data impact:** none (documentation), but a strict reader enforces the old
  rule and blocks an approval G29 now permits — recreating the exact blocker
  SPEC-260821-0108 removed.
- **Workaround available:** yes — consult the G29 row / §3.0 table; but the
  contradiction must be removed.

---

## 5. Classification and routing

| Aspect | Value |
|--------|-------|
| **Nature** | non-functional (methodology text). Per ADR-002, class-1 documentation defect: the kit text contradicts an approved decision; deterministic grep/diff evidence. |
| **Severity route** | `medium` → any team member, the author included, may record `HITL-BUG-Approval` (G29 relaxed route; self-approval permitted off the `critical` route). |
| **Violated expectation** | The approved relaxed G29 rule (SPEC-260821-0108). |
| **Dedicated Bolt parent** | `US-000-non-functional.md`. |

---

## 6. Fix status (strict TDD, ONE V-Bounce)

| Stage | Evidence | Status |
|-------|----------|--------|
| Reproduction test | grep RED: 7 stale matches in `distribution-kit/` (6 single-line + 1 multiline §3.0) | ✅ Done |
| Production fix | grep/diff GREEN: 0 stale matches, relaxed rule at all 7 locations; G-count 39×5; root untouched | ✅ Done |
| MEM | [MEM-260822-0027-complete-g29-sweep.md](../memory/MEM-260822-0027-complete-g29-sweep.md) — red + green recorded separately | ✅ Done |

> Edits land in `distribution-kit/` only (ADR-004); the root receives them at
> the next §5.16 migration. Fix scope must use multiline + notation-variant
> greps and build its inventory from the phrase-family sweep, not from the
> prior SPEC's list (AREV-001 root-cause lesson).

---

## 7. Relations

| Relation | Reference |
|----------|-----------|
| **Detected in** | AREV-001 (F-01, Verdict approved 2026-08-21) |
| **Affected US / Bolt** | US-000 (non-functional container) |
| **Dedicated Bolt** | US-000.BOLT-NNN (after HITL-BUG-Approval) |
| **Prior related work** | US-000.BOLT-002 / SPEC-260821-0108 (the relaxation this sweep completes) |
| **ADRs** | ADR-002 (class-1 classification), ADR-004 (kit-only edits) |

---

## 8. HITL-BUG-Approval

> **Avenga DevFlow §2.16, §3.0.** This BUG remains a draft until a qualified
> human records `HITL-BUG-Approval` (non-functional, `severity: medium` →
> any team member, the author included; recorded in the `review` frontmatter
> block). Approval confirms the defect, evidence, nature and routing; it does
> **not** approve the future Bolt, SPEC, implementation, MEM or acceptance —
> each keeps its own checkpoint.

---

## 9. History

| Date | Change | Author |
|------|--------|--------|
| 2026-08-22 | Defect reported (draft) — routed from AREV-001 F-01 | @eugenio.serrano |
| 2026-08-22 | HITL-BUG-Approval recorded — dedicated Bolt US-000.BOLT-004 authorized | @eugenio.serrano |
| 2026-08-22 | Fixed via US-000.BOLT-004 V-Bounce 1 (SPEC-260822-0018, MEM-260822-0027); grep RED→GREEN; Bolt Done (HITL-BOLT-DONE-Approval) | @eugenio.serrano |
| 2026-08-22 | **Closed** — fix accepted in the kit; root receives it at the next §5.16 migration (ADR-004) | @eugenio.serrano |
