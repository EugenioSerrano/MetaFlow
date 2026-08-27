---
id: "BUG-003"
title: "Role-as-gate residuals: the §3.0 checkpoint narrative still gates 7 checkpoints on named roles, contradicting its own table"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-5"
severity: "medium"
nature: "non-functional"
status: "closed"
owner: "eugenio.serrano"
detected_in: "arev"
detected_at: "2026-08-22T02:53:30-03:00"
incident_ref: ""
affected_artifacts:
  - "distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md"
  - "distribution-kit/devflow/tests/test-cases/TEMPLATE-TC.md"
expected_result: "Every text that states who records a HITL checkpoint carries the no-holder fallback approved in US-014.BOLT-001 (D1/D3) — 'or, if a named role has no holder, the available qualified human records it, noting the self-assigned role' — so role routing reads as guidance everywhere, never as a gate. The §3.0 narrative bullets agree with the §3.0 table."
actual_result: "The §3.0 table rows carry the fallback, but the §3.0 narrative 'Who:' bullets for HITL-US, HITL-BUG (functional route), HITL-TC, HITL-BOLT-READY, HITL-ADR, HITL-SPEC and HITL-BOLT-DONE state the named role unconditionally ('Who: Functional Analyst.', 'Who: Architect or Tech Lead.'). §2.6.1 and TEMPLATE-TC §10 do the same for the TC route. A reader of the normative narrative concludes only the named role may approve — the exact gate US-014 removed."
bolt: "US-000.BOLT-006"
spec: "SPEC-260822-0338"
mem: "MEM-260822-0342"
sources:
  - "devflow/adversarial-reviews/AREV-003-v42-close-removal-traces-sweep/03-VERDICT.md"
  - "devflow/adrs/ADR-005-removal-completeness-phrase-family-sweep.md"
review_ready_at: "2026-08-22T03:20:10-03:00"
review:
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "developer"}]
  started_at: "2026-08-22T03:21:57-03:00"
  decided_at: "2026-08-22T03:21:57-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "BUG confirmed with deterministic positive-coverage evidence: 9 route statements across 7 checkpoints (+ §2.6.1 and TEMPLATE-TC §10) state a named-role route unconditionally while the §3.0 table rows carry the fallback (5/5) — a self-contradiction (ADR-002 class 1) that defeats US-014's single-operator operability for narrative readers. Widened correctly from AREV-003 F-02 (2 locations) by the ADR-005 sweep. Non-functional, severity medium → any team member, author included (G29). Authorizes exactly one dedicated Bolt under US-000."
tags: ["adr-002-class-1", "partial-sweep-pattern", "self-contradiction", "single-operator-operability"]
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs and headings stay in
  English (schema); prose in content_language (en, devflow/LANGUAGE).

  ⚠️ BUG lifecycle (§2.16, §3.3.1): DRAFT until HITL-BUG-Approval. Only then
  may its EXACTLY ONE dedicated Bolt be created (non-functional → US-000).

  ⚠️ SCOPE NOTE: this BUG originates in AREV-003 F-02, but the ADR-005
  phrase-family sweep found the defect is ~9 locations across 7 checkpoints,
  not the 2 TC texts F-02 reported. The evidence below is the sweep's, not a
  restatement of the Critique.
-->

# BUG-003 — Role-as-gate residuals in the §3.0 checkpoint narrative

| Field              | Value |
|--------------------|-------|
| **Severity**       | medium |
| **Nature**         | non-functional (documentation defect — ADR-002 class 1) |
| **Detected in**    | arev (AREV-003 F-02, then widened by the ADR-005 sweep) |
| **Status**         | draft |
| **Affected files** | `Avenga-DevFlow.md` (§3.0 narrative ×7, §2.6.1), `TEMPLATE-TC.md` (§10) |
| **Dedicated Bolt** | [US-000.BOLT-006](../functional/bolts/US-000.BOLT-006-role-gate-narrative-fallback-sweep.md) (candidate — pending `HITL-BOLT-READY-Approval`) |

## 1. Summary

`US-014.BOLT-001` (D1/D3) made role routing **guidance, never a gate**: every
single-role approval route gained the no-holder fallback. The sweep reached the
**tables** but not the **normative narrative**. The §3.0 checkpoint definitions
— the text that *defines* each checkpoint — still state the named role
unconditionally for **seven checkpoints**, contradicting their own table rows
in the same section, and defeating US-014's purpose (single-operator
operability) for anyone who reads the narrative rather than the table.

## 2. Reproduction

Deterministic grep/diff (ADR-002 class 1). Applying the ADR-005 sweep to the
*fallback* family — a **positive-coverage** sweep: enumerate every text that
states an approval route, then assert each carries the clause.

1. Enumerate the §3.0 narrative route statements:
   `grep -nA3 '^\s*- \*\*Who:\*\*' devflow/avenga-devflow/Avenga-DevFlow.md`
2. Positive control — the §3.0 **table** rows carry the fallback:
   `grep -nE '^\| .HITL-(US|BOLT-READY|ADR|SPEC|BOLT-DONE)-Approval.' … | grep 'no holder'` → **5/5 present**
3. Compare against the narrative bullets:

| Checkpoint | Narrative line | Text | Fallback |
|-----------|----------------|------|----------|
| `HITL-US-Approval` | 2620 | "**Who:** Functional Analyst." | ❌ absent |
| `HITL-BUG-Approval` (functional route) | 2630 | "Functional Analyst for a functional BUG" | ❌ absent (the non-functional route is correct — G29 relaxed) |
| `HITL-TC-Approval` | 2644–2647 | "QA plus a Functional Analyst or delegated business-domain owner…" | ❌ absent *(AREV-003 F-02)* |
| `HITL-BOLT-READY-Approval` | 2658–2661 | "Functional Analyst for a functional Bolt; Architect or Tech Lead for a non-functional Bolt…" | ❌ absent |
| `HITL-ADR-Approval` | 2670 | "**Who:** Architect or Tech Lead." | ❌ absent |
| `HITL-SPEC-Approval` | 2680–2683 | "Dev-validator plus the applicable domain owner(s)…" | ❌ absent |
| `HITL-BOLT-DONE-Approval` | 2745–2746 | "PO / PM for functional Bolts; routed technical owner…" | ❌ absent |
| DISC / REV / AREV | 2691–2717 | "Qualified human designated for…" | ✅ n/a — role-agnostic by construction, no gate |

4. Two more locations outside §3.0:
   - `Avenga-DevFlow.md:835–841` (§2.6.1 "Independent lifecycle"): "Functional
     expected results require QA review plus Functional Analyst or delegated
     business-domain approval. Non-functional expected results require QA review
     plus the applicable Architect, Tech Lead, …" — ❌ absent.
   - `TEMPLATE-TC.md` §10 (`HITL-TC-Approval`): ❌ absent *(AREV-003 F-02)*.

**Expected result:** every route statement above carries the fallback clause
(or an explicit reference to it), so narrative and table agree.

**Actual result:** 9 locations state a named-role route unconditionally while
the §3.0 table says the opposite.

## 3. Root cause

`US-014.BOLT-001`'s D3 enumeration was "every single-role route". The sweep
enumerated the **tables** (§3.0 checkpoint table, GUARDRAILS checkpoint map,
the four agents' HITL tables) and verified those — the same
**partial-enumeration** failure mode as BUG-001 and BUG-002, in its third
variant: this time the missed surface is the *normative narrative of the very
section whose table was fixed*.

Note the inverse shape: BUG-001/BUG-002 are **residuals of a removal** (find
text that should be gone); this is an **omission of an addition** (find text
that should have gained a clause). ADR-005's location set still applies, but the
assertion flips from "zero matches" to "every route statement carries the
clause" — a positive-coverage sweep. The SPEC must state it that way.

## 4. Impact

- **Users affected:** every adopter reading §3.0 — the normative definition of
  the checkpoints — or filling `TEMPLATE-TC.md`.
- **Data impact:** none (documentation defect).
- **Workaround available:** none clean. A reader who follows the narrative
  blocks on an unavailable role; a reader who follows the table does not. The
  document contradicts itself.
- **Release impact:** US-014 (single-operator operability) is the release's
  headline change. Shipping v4.2 with its normative narrative still gating
  seven checkpoints on named roles largely defeats that change for narrative
  readers. Recommend fixing **before** the v4.2 close, even though AREV-003
  rated F-02 as 🔶 on the strength of the 2 locations then known.

## 5. Classification and routing

| Aspect | Value |
|--------|-------|
| **Nature** | non-functional → `severity: medium` ⇒ any team member, this BUG's author included, approves (G29) |
| **Violated expectation** | US-014.BOLT-001 (approved, D1/D3): role routing is guidance, never a gate, in **every** route statement; ADR-002 class 1 (self-contradiction, deterministic evidence) |
| **Dedicated Bolt parent** | `US-000-non-functional.md` |

## 6. Fix status (strict TDD, ONE V-Bounce)

| Stage | Evidence | Status |
|-------|----------|--------|
| Reproduction | The §2 positive-coverage sweep: 9 route statements without the clause vs 5/5 table rows with it | GREEN (defect confirmed) |
| Production fix | Add the fallback clause (or an explicit cross-reference to it) to each of the 9 locations; keep the DISC/REV/AREV bullets untouched (role-agnostic already); re-run the sweep | Pending |
| MEM | `MEM-YYMMDD-HHmm` — records the before sweep (9 missing) and the after sweep (0 missing) separately | Pending |

> **Note:** as in BUG-002, the "RED"/"GREEN" evidence is deterministic
> grep/diff (ADR-002 class 1), not an automated test suite.

## 7. Relations

| Type | ID | Relation |
|------|----|----------|
| Origin | AREV-003 | [F-02](../adversarial-reviews/AREV-003-v42-close-removal-traces-sweep/03-VERDICT.md) — confirmed 🔶; this BUG widens it from 2 to 9 locations via the ADR-005 sweep |
| Governing standard | ADR-005 | [ADR-005](../adrs/ADR-005-removal-completeness-phrase-family-sweep.md) — the sweep that found the 7 additional locations; its first exercise |
| Incomplete removal | US-014.BOLT-001 | [US-014.BOLT-001-role-guidance-not-gate.md](../functional/bolts/US-014.BOLT-001-role-guidance-not-gate.md) — Done; its MEM is immutable history, so this BUG's fix is a separate Bolt |
| Sibling pattern | BUG-001, BUG-002 | Same partial-enumeration root cause (1st, 2nd and 3rd variants) |
| Classification | ADR-002 | class 1 (self-contradiction, deterministic evidence) |

## 8. HITL-BUG-Approval

> **Avenga DevFlow §2.16, §3.0.** DRAFT until a qualified human records
> `HITL-BUG-Approval`: non-functional → Architect/Tech Lead if
> `severity: critical`, otherwise any team member, this BUG's author included
> (G29). Only after approval may the dedicated Bolt be created.

| Field | Value |
|-------|-------|
| **Approver** | eugenio.serrano (any team member, author included — severity `medium`, G29) |
| **Role** | developer |
| **Decision** | approved |
| **review_ready_at** | `2026-08-22T03:20:10-03:00` |
| **review.started_at** | `2026-08-22T03:21:57-03:00` |
| **review.decided_at** | `2026-08-22T03:21:57-03:00` |
| **Authorizes** | Exactly one dedicated **non-functional Bolt under US-000** |
