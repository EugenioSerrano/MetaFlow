---
id: "BUG-005"
title: "Kit self-containment residue — a maintainer finding ID (F-14) shipped in VERIFICATION.md (US-025 AC-9 violation)"
date: "2026-08-25"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
severity: "low"                  # cosmetic wording residue — no functional impact on adopters
nature: "functional"             # violates a feature AC (US-025 AC-9 — kit self-containment)
status: "closed"                 # draft | approved | in-fix | fixed | closed — Bolt Done 2026-08-25
owner: "eugenio.serrano"         # Functional Analyst / Developer / QA who drafted the BUG
detected_in: "review"            # self-containment sweep at the maintainer's request (2026-08-25)
detected_at: "2026-08-25T04:44:00-03:00"
incident_ref: ""
affected_artifacts:
  - "distribution-kit/devflow/agents/VERIFICATION.md" # line 51 — "(the F-14 shape — the reviewer ..."
expected_result: "The kit files carry no maintenance-partition references (US-025 AC-9): no REV finding IDs (F-NN) or any maintainer artifact reference resolvable only inside the maintainer repo"
actual_result: "`distribution-kit/devflow/agents/VERIFICATION.md` line 51 contains `(the F-14 shape — the reviewer \"produces REVs\" with write_paths: [])` — `F-14` is a finding ID of the maintainer's REV-005; an adopter cannot resolve it"
bolt: "US-025.BOLT-007"           # filled after AITL-BUG-Approval — dedicated Bolt under US-025
spec: "SPEC-260825-0448"
mem: "MEM-260825-0449"
sources:
  - "user report (self-containment sweep, 2026-08-25 — maintainer request)"
  - "devflow/reviews/REV-005-devflow-agents-adopter-smoke-test.md" # F-14 originates here
review_ready_at: "2026-08-25T04:45:38-03:00"
review: # AITL-BUG-Approval — decision dictated in conversation ("si aprobado") and transcribed by the agent (§3.0)
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "functional_analyst"
      model: null
  started_at: "2026-08-25T04:46:32-03:00"
  decided_at: "2026-08-25T04:46:32-03:00"
  findings: []
  acknowledged_without_comment: true # must be true when findings is empty (§3.0)
  acknowledgment_reason: "Approved as Functional Analyst: defect confirmed (grep reproduction, VERIFICATION.md:51), severity low confirmed, nature functional (US-025 AC-9 violation), routing to a dedicated Bolt under US-025 confirmed. Authorizes the creation of US-025.BOLT-007; does not approve the Bolt, SPEC, implementation, MEM or acceptance."
tags: ["kit-self-containment", "ac-9", "verification-md", "residue", "v5.1"]
---

# BUG-005 — Kit self-containment residue: maintainer finding ID in VERIFICATION.md

| Field              | Value |
|--------------------|-------|
| **Severity**       | low |
| **Nature**         | functional (violates US-025 AC-9 — kit self-containment) |
| **Detected in**    | review (self-containment sweep, maintainer request 2026-08-25) |
| **Status**         | draft |
| **Affected files** | `distribution-kit/devflow/agents/VERIFICATION.md` (line 51) |
| **Dedicated Bolt** | [US-025.BOLT-NNN — filled after AITL-BUG-Approval] |

## 1. Summary

The shipped kit carries a maintainer-partition reference: the phrase
"(the F-14 shape — ...)" in `devflow/agents/VERIFICATION.md` cites a
finding ID from the maintainer's REV-005, which no adopter can resolve.
The residue was introduced by US-025.BOLT-006's V-Bounce 1 (the
execution-evidence paragraph), whose wording carried the REV finding
reference into the kit.

---

## 2. Reproduction

1. Run `grep -rn "F-14" distribution-kit/` (or search "F-14" across the kit).
2. Observe the single hit at `distribution-kit/devflow/agents/VERIFICATION.md:51`.

**Expected result:** zero hits — the kit carries no maintenance-partition
references (US-025 AC-9: "the kit files carry no maintenance-partition
references (`US-`/`ADR-`/`DISC-`/`BOLT-`)"; the AC-9 intent covers REV
finding IDs — an adopter must never need the maintainer's governance
records to understand the kit).

**Actual result:** one hit — `(the F-14 shape — the reviewer "produces
REVs" with write_paths: [])`, where `F-14` is a finding ID of the
maintainer's REV-005 (approved 2026-08-24). The sentence is
understandable only with REV-005 in hand.

---

## 3. Root cause

The execution-evidence paragraph was written for US-025.BOLT-006 from the
SPEC's Phase B.2 wording, which referenced "the F-14 shape" (a shorthand
for REV-005's finding on the Coordinator-persists-executor-production
pattern). The shorthand is maintainer-internal vocabulary; it leaked into
kit text during the V-Bounce. The BOLT-006 acceptance checks covered the
new content's presence (greps) but not its self-containment (no sweep for
REV finding IDs in the kit) — the sweep that would have caught it was not
part of the V-Bounce evidence set.

---

## 4. Impact

- **Users affected:** all adopters reading `VERIFICATION.md`.
- **Data impact:** none.
- **Workaround available:** yes — the phrase "the F-14 shape" is
  contextually readable as "the shape where the Coordinator persists an
  executor's production"; no adopter workflow breaks.

Low severity: cosmetic/reference-quality defect; no functional,
security or compliance impact. It does, however, violate the kit's own
self-containment AC and would be flagged by any future
self-containment audit of the kit.

---

## 5. Classification and routing

| Aspect | Value |
|--------|-------|
| **Nature** | functional — violates feature AC-9 of US-025 |
| **Violated expectation** | US-025 AC-9 (kit self-containment — no maintenance-partition references) |
| **Dedicated Bolt parent** | US-025 (the feature whose Bolt introduced the residue) |

---

## 6. Fix status (strict TDD, ONE V-Bounce)

| Stage | Evidence | Status |
|-------|----------|--------|
| Reproduction test | RED: `grep -n "F-14" distribution-kit/` → 1 hit (VERIFICATION.md:51) | Pending |
| Production fix | GREEN: reword the phrase self-containedly ("the shape where the Coordinator persists an executor's production") + `grep -n "F-14" distribution-kit/` → 0 hits; G-count 39/39; four-agent sync diff unchanged | Pending |
| MEM | [MEM-YYMMDD-HHmm — records red and green separately] | Pending |

> The reproduction test and the fix are mandatory phases of the SAME
> V-Bounce of the BUG's dedicated Bolt (§2.16, §3.3.1). Production code
> may not change before red evidence exists.

---

## 7. Relations

| Relation | Reference |
|----------|-----------|
| **Detected in** | self-containment sweep (maintainer request, 2026-08-25) |
| **Incident** | — |
| **Affected US / Bolt** | US-025 / US-025.BOLT-006 (introduced the residue) |
| **Dedicated Bolt** | US-025.BOLT-NNN (to be created after AITL-BUG-Approval) |
| **Canonical SPEC** | SPEC-YYMMDD-HHmm (of the dedicated Bolt) |
| **ADRs** | ADR-004 (repository partition — kit-only) |
| **Risks** | — |

---

## 8. AITL-BUG-Approval

> **Avenga DevFlow §2.16, §3.0.** This BUG remains a draft until a qualified
> human records `AITL-BUG-Approval` — recorded in the `review` frontmatter
> block. Approval confirms the defect, evidence, nature and routing; it
> does **not** approve the future Bolt, SPEC, implementation, MEM or
> acceptance — each keeps its own checkpoint.

---

## 9. History

| Date | Change | Author |
|------|--------|--------|
| 2026-08-25 | Defect reported (draft) — self-containment sweep residue | eugenio.serrano (agent-drafted, deepseek/deepseek-v4-flash) |
| 2026-08-25 | AITL-BUG-Approval recorded — dedicated Bolt US-025.BOLT-007 authorized | eugenio.serrano |
