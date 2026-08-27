---
id: "BUG-004"
title: "§5.16 migration rule is ambiguous on input/ scaffolding: 'input/ 100% byte-for-byte' collides with 'README/INDEX never copied forward', and the prescribed check cannot detect byte-level loss"
date: "2026-08-23"
author: "human:eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
severity: "low"
nature: "non-functional"
status: "closed" # draft | approved | in-fix | fixed | closed
owner: "eugenio.serrano"
detected_in: "review"
detected_at: "2026-08-23T11:09:54-03:00"
incident_ref: ""
affected_artifacts:
  - "devflow/avenga-devflow/Avenga-DevFlow.md"
  - "distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md"
expected_result: "§5.16 distinguishes the framework scaffolding that ships inside input/ (the README.md/INDEX.md files installed by the kit) from project evidence: scaffolding is replaced by the new version (and is preserved only when the project modified it, in which case it counts as evidence), while every other file is raw evidence copied byte-for-byte; the post-migration verification is tree + file count + byte-identity of every non-scaffolding file, so a migration can never silently overwrite or drop real evidence (G31) — and the rule is stated identically in the distribution kit."
actual_result: "§5.16 rule 1 mandates input/ 'in full — 100%... byte for byte' with a verification of 'identical tree and identical file count', while the 'Everything else comes from the new version' paragraph states that folder README.md and INDEX.md files are never copied forward. Neither rule declares which one governs the scaffolding README/INDEX files that ship inside input/. The prescribed verification (tree + count) passes even when every scaffolding file differs at the byte level — reproduced on the 4.2→5.0 migration of this repository: devflow/input and devflowOLD/input have 9/9 identical paths, 0 tree differences, yet all 9 files differ (11 changed lines: 'Methodology version: 4.2'→'5.0' and 'HITL-*'→'AITL-*' checkpoint names). An executor migrating a project with real evidence can therefore either overwrite it (reading the 'everything else' rule) or freeze stale scaffolding (reading rule 1 literally — re-introducing the version-marker/HITL-vocabulary defect class BUG-001, BUG-003 and US-000.BOLT-013 removed)."
bolt: "US-000.BOLT-014" # US-NNN.BOLT-NNN (functional) | US-000.BOLT-NNN (non-functional)
                              # — the ONE dedicated Bolt (filled after AITL-BUG-Approval)
spec: "SPEC-260823-1114" # SPEC-YYMMDD-HHmm — the canonical SPEC of the BUG Bolt
mem: "MEM-260823-1120" # MEM-YYMMDD-HHmm — the fix V-Bounce MEM (red + green evidence)
sources:
  - "user report"
review_ready_at: "2026-08-23T11:10:00-03:00"
review: # AITL-BUG-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "developer"
      model: null
  started_at: "2026-08-23T11:11:40-03:00"
  decided_at: "2026-08-23T11:12:00-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "BUG confirmed with deterministic evidence: the §5.16 prescribed post-migration verification (tree + file count) passes while all 9 scaffolding files inside input/ differ at the byte level (11 lines: 'Methodology version: 4.2'→'5.0' and 'HITL-*'→'AITL-*') — reproduced on this repository's 4.2→5.0 migration (9/9 paths, 0 tree differences, git diff --no-index 9 files). Class-1 self-contradiction (ADR-002) between §5.16 rule 1 ('input/ in full, byte for byte') and the 'Everything else comes from the new version' paragraph (README/INDEX never copied forward), with no precedence clause for input/ scaffolding. Non-functional, severity low → any team member, author included (G29). Authorizes exactly one dedicated Bolt under US-000."
tags: ["adr-002-class-1", "self-contradiction", "migration", "input-raw-evidence", "g31"]
---

# BUG-004 — §5.16 ambiguity: input/ scaffolding vs raw evidence

| Field              | Value |
|--------------------|-------|
| **Severity**       | low |
| **Nature**         | non-functional |
| **Detected in**    | review (4.2 → 5.0 migration review) |
| **Status**         | closed |
| **Affected files** | `devflow/avenga-devflow/Avenga-DevFlow.md` (§5.16), `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md` (parity) |
| **Dedicated Bolt** | [US-000.BOLT-014-input-scaffolding-evidence-clarification.md](../functional/bolts/US-000.BOLT-014-input-scaffolding-evidence-clarification.md) — created after AITL-BUG-Approval |

## 1. Summary

The §5.16 migration procedure contains two normative rules that collide for the
scaffolding `README.md`/`INDEX.md` files that ship inside `input/`: rule 1
demands `input/` be copied "in full — 100%... byte for byte" and verified by
"identical tree and identical file count", while the "Everything else comes
from the new version" paragraph says folder README/INDEX files are never
copied forward. Neither rule declares which one governs `input/` scaffolding,
and the prescribed verification cannot detect a byte-level difference — so a
future migration could silently overwrite real evidence, or freeze stale
scaffolding. This migration resolved on the "new scaffolding" side; the
defect is the text ambiguity, which must be made explicit.

---

## 2. Reproduction

Deterministic, on this repository's 4.2 → 5.0 migration (reported during the
migration review):

1. Run the §5.16 post-migration verification on `devflow/input` vs
   `devflowOLD/input` (tree + file count):
   - 9/9 files, **0 tree differences** → the prescribed check **passes**.
2. Byte-compare the same two trees:
   - `git diff --no-index devflowOLD/input devflow/input` → **all 9 files
     differ, 11 lines changed** → rule 1's "byte for byte" is not satisfied,
     yet the prescribed verification reports success.
3. Read §5.16: rule 1 ("input/ in full — 100%, byte for byte") vs
   "Everything else comes from the new version" ("Folder `README.md` and
   `INDEX.md` files... are never copied forward"). The 9 differing files are
   exactly README/INDEX files — both rules claim them; neither grants the
   other precedence, and no clause mentions scaffolding inside `input/`.

**Expected result:** §5.16 states explicitly which files inside `input/` are
framework scaffolding (replaced by the new version; preserved only if the
project modified them, in which case they are evidence) vs raw evidence
(copied byte-for-byte, G31), and the verification catches byte-level
differences of evidence (tree + count + byte-identity of non-scaffolding
files).

**Actual result:** the text does not distinguish scaffolding from evidence;
the prescribed verification (tree + count) cannot detect byte-level loss or
partial copies; the two normative rules contradict each other for the
scaffolding README/INDEX that ship inside `input/` (ADR-002 class 1).

---

## 3. Root cause

§5.16 was written for the general case — "input/ is raw evidence, copy 100%" —
without considering that the kit installs its own scaffolding (README/INDEX
with version markers and checkpoint vocabulary) inside `input/`. The
"Everything else comes from the new version" paragraph enumerates README/INDEX
as framework files but never cross-references `input/`, and rule 1 never
carves out scaffolding. The prescribed verification mirrors the intent
(evidence preserved) but measures only tree and count, not bytes, so it
cannot fail on a partial or replaced copy of non-evidence. The ambiguity is
the defect: two normative rules, no precedence, no scaffolding carve-out.

---

## 4. Impact

- **Users affected:** teams migrating between methodology versions (future migrations).
- **Data impact:** none today (this repository's `input/` holds no real evidence; the old scaffolding state lives in git). Potential loss of real raw evidence in a future migration if an executor reads the "everything else" rule — G31 violation.
- **Workaround available:** yes — consult git history and G31; this migration accepted the new scaffolding because the differing bytes are framework content only (version markers, HITL→AITL names) and the old state is committed (7e99e1b).

---

## 5. Classification and routing

| Aspect | Value |
|--------|-------|
| **Nature** | non-functional → severity `low`: any team member, this BUG's author included, may approve (G29) |
| **Violated expectation** | §5.16 normative self-consistency (ADR-002 class 1); G31 raw-evidence preservation invariant |
| **Dedicated Bolt parent** | US-000-non-functional.md |

---

## 6. Fix status (strict TDD, ONE V-Bounce)

| Stage | Evidence | Status |
|-------|----------|--------|
| Reproduction test | RED: R1 prescribed check passes (9/9 files, 0 tree diffs) while R2 shows 9 files / 11+11- diverging; R3 colliding rules at L4579/L4597 | ✅ Done |
| Production fix | GREEN: G1 5/5 phrases both copies · G2 zero residue · G3 scope (edit log + git status) · G4 parity byte-identical (292,738 chars) · G5 G-count 39, agents untouched | ✅ Done |
| MEM | [MEM-260823-1120](../memory/MEM-260823-1120-input-scaffolding-evidence-clarification.md) — red and green recorded separately; AITL-MEM-Approval 2026-08-23T11:21 | ✅ Done |

> The reproduction test and the fix are mandatory phases of the SAME
> V-Bounce of the BUG's dedicated Bolt — not two Bolts and not two SPECs
> (§2.16, §3.3.1). Production code may not change before red evidence exists.

---

## 7. Relations

| Relation | Reference |
|----------|-----------|
| **Detected in** | user report (4.2 → 5.0 migration review) |
| **Incident** | — |
| **Affected US / Bolt** | US-000 (methodology text) |
| **Dedicated Bolt** | US-000.BOLT-NNN (pending) |
| **Canonical SPEC** | SPEC-YYMMDD-HHmm (pending) |
| **ADRs** | — (localized text clarification; no structural decision expected) |
| **Risks** | — |

---

## 8. AITL-BUG-Approval

> **Avenga DevFlow §2.16, §3.0.** This BUG remains a draft until a qualified
> human records `AITL-BUG-Approval` (recommended: Functional Analyst for
> functional; Architect/Tech Lead when `severity: critical`, otherwise any team
> member for non-functional) — recorded in the `review` frontmatter block. The
> routing is guidance, never a gate: any qualified team member, the BUG's own
> author included, may record it at any severity. Approval
> confirms the defect, evidence, nature and
> routing; it does **not** approve the future Bolt, SPEC, implementation,
> MEM or acceptance — each keeps its own checkpoint.

---

## 9. History

| Date | Change | Author |
|------|--------|--------|
| 2026-08-23 | Defect reported (draft) | human:eugenio.serrano |
| 2026-08-23 | AITL-BUG-Approval recorded — dedicated Bolt US-000.BOLT-014 created | human:eugenio.serrano |
| 2026-08-23 | Fix V-Bounce executed (RED → GREEN), MEM-260823-1120 approved (AITL-MEM-Approval) — status fixed | human:eugenio.serrano |
| 2026-08-23 | US-000.BOLT-014 accepted (AITL-BOLT-DONE-Approval) — status closed | human:eugenio.serrano |
