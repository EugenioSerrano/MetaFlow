---
id: "SPEC-260823-1114"
title: "§5.16 clarification: input/ framework scaffolding vs raw evidence (BUG-004 / US-000.BOLT-014)"
date: "2026-08-23"
author: "human:eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved" # draft | approved | blocked | obsolete
origin: "BUG-004"
bolt: "US-000.BOLT-014"
revision: 1 # material revision of this canonical SPEC (matches manifest spec_revisions[])
associated_adrs:
  - "devflow/adrs/ADR-002-documentation-defect-classification.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
  - "devflow/adrs/ADR-005-removal-completeness-phrase-family-sweep.md"
prerequisites: []
risk_class: "low"
autonomy_level: "L3" # defaults by risk: low/medium→L3 (§3.3)
turn_budget: "" # platform default
data_classification: "internal"
review_ready_at: "2026-08-23T11:14:27-03:00"
review: # AITL-SPEC-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-23T11:15:00-03:00"
  decided_at: "2026-08-23T11:18:00-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Revision 1 approved: pre-SPEC evidence gate clean (BUG-004 and US-000.BOLT-014 approved, ADR-002/004/005 accepted, 0 open OQs, baseline root==kit byte-identical), target text for §5.16 rule 1 + cross-reference specified exactly, RED/GREEN evidence commands deterministic, gates with n/a reasons, stop conditions defined. V-Bounce authorized (strict TDD: RED before any edit, G19)."
---

# SPEC-260823-1114 — §5.16 clarification: input/ framework scaffolding vs raw evidence

| Field | Value |
|-------|-------|
| **Origin** | BUG-004 (approved 2026-08-23) |
| **Bolt** | [US-000.BOLT-014](../functional/bolts/US-000.BOLT-014-input-scaffolding-evidence-clarification.md) (approved 2026-08-23) |
| **ADRs** | [ADR-002](../adrs/ADR-002-documentation-defect-classification.md) · [ADR-004](../adrs/ADR-004-repository-partition-v2.md) · [ADR-005](../adrs/ADR-005-removal-completeness-phrase-family-sweep.md) |
| **Risk Class** | low |
| **Revision** | 1 |

---

## 1. Objective

Modify §5.16 of the Avenga DevFlow methodology (both copies: the operating
`devflow/avenga-devflow/Avenga-DevFlow.md` and the distribution-kit copy
`distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md`, which are
currently byte-identical) so the migration procedure unambiguously separates
the **framework scaffolding** that the kit installs inside `input/` (its
`README.md` / `INDEX.md` files) from the **raw evidence** the project deposits
there. The scaffolding is replaced by the new version (unless the project
modified it, in which case it is evidence); every other file is copied byte
for byte and the post-migration verification gains a byte-level check of
evidence, so the BUG-004 reproduction (the prescribed check passing while all
9 scaffolding files differ) no longer describes a gap that could swallow real
evidence.

If NOT implemented: the normative text keeps two colliding rules with no
precedence, and the day a project deposits real evidence into `input/`, a
migration executor can either overwrite it (reading the "everything else"
rule) or freeze stale scaffolding with outdated version markers and `HITL-*`
vocabulary (reading rule 1 literally) — the exact defect classes BUG-001,
BUG-003 and US-000.BOLT-013 removed.

---

## 2. Context

BUG-004 (approved) evidenced a class-1 self-contradiction (ADR-002) in §5.16:
rule 1 demands `input/` be copied "in full — 100%... byte for byte" and be
verified by "identical tree and the identical file count", while the
"Everything else comes from the new version" paragraph says folder
`README.md` / `INDEX.md` files are never copied forward. The 9 scaffolding
files inside `input/` fall under both rules, and the prescribed verification
(tree + file count) passes even when every one of them differs at the byte
level — reproduced on this repository's 4.2 → 5.0 migration (9/9 paths,
0 tree differences, 11 changed lines: version markers and `HITL-*` → `AITL-*`).

This migration resolved on the "new scaffolding" side (accepted by the
maintainer: the differing bytes are framework content only and the old state
lives in git). This SPEC makes that resolution the explicit rule for future
migrations, with evidence preservation as the hard invariant (G31).

**Repository baseline (pre-SPEC gate):** the working tree is mid-migration
(4.2 → 5.0 install over the root; `devflowOLD/` present; tree uncommitted;
HEAD = c0decad). The two target files are **byte-identical** (291,738 chars
each — verified). The fix edits exactly these two files.

---

## 3. Source inventory and approval references

Pre-SPEC evidence gate (G13, G35): every governed source is approved; zero
open/in-validation OQs against US-000.

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | `devflow/functional/bolts/US-000.BOLT-014-input-scaffolding-evidence-clarification.md` | AITL-BOLT-READY-Approval ✓ (2026-08-23T11:14) |
| BUG | `devflow/bugs/BUG-004-input-scaffolding-vs-evidence-rule.md` | AITL-BUG-Approval ✓ (2026-08-23T11:12) |
| Parent container | `devflow/functional/user-stories/US-000-non-functional.md` | always active, no approval lifecycle |
| ADR-002 | documentation defect classification | accepted ✓ |
| ADR-004 | repository partition — kit/root parity | accepted ✓ |
| ADR-005 | removal-completeness — phrase-family positive-coverage sweeps | accepted ✓ |
| OQ index | `devflow/analysis/open-questions/INDEX.md` | 0 open / 0 in-validation (G35 ✓) |
| Repository baseline | HEAD `c0decad` + working-tree migration state (root == kit, byte-identical) | — |

---

## 4. Scope

### In scope

- §5.16 **rule 1** (the `input/` copy rule) in the two methodology copies.
- §5.16 **"Everything else comes from the new version"** paragraph in the two
  copies — one cross-reference sentence aligning it with rule 1 (phrase-family
  alignment, ADR-005).
- The governance artifacts of this Bolt (MEM, manifest `v_bounces[]` entry).

### Out of scope

- Any other §5.16 step (AGENTS.md merge, LANGUAGE/VERSION, CHANGELOG,
  routing, manifests), any other section, G31 or any guardrail, agent
  definitions, schemas, `bin/` tooling, `US-000-non-functional.md`, or any
  file outside the two methodology copies (except this Bolt's own governance
  artifacts).
- Reverting this migration's already-accepted resolution (the new scaffolding
  in `devflow/input/` stays).
- Editing §5.6 (Raw inputs) — its text is consistent with the fix (it
  defines the folders and the read-only/G31 property; it does not state the
  migration copy rule).

---

## 5. Prerequisites and baseline

- BUG-004 approved and Bolt US-000.BOLT-014 approved (both recorded).
- The two target files currently byte-identical (parity baseline).
- No code, tooling or test suites involved — verification is deterministic
  grep/diff commands (documented in §8).

---

## 6. Phases

Strict TDD per §3.3.1: Phase 0 (RED) runs **before any production change**;
Phases 1–2 are the production change; Phase 3 is the GREEN verification.
All of it happens in the ONE V-Bounce of US-000.BOLT-014.

### Phase 0 — RED evidence: reproduce BUG-004 (no production change)

**Duration:** 0.5h total cycle — **Complexity:** Low

#### 0.1 Reproduce the gap

Run, in the repository root, and capture the output (this is the RED
evidence):

1. **R1 — prescribed check:** compare trees and counts of `devflow/input`
   and `devflowOLD/input`:
   `Get-ChildItem -Recurse -File` on both; compare relative paths and counts.
   Expected output: identical paths, 9/9 files, 0 tree differences — the
   check **passes** although rule 1 says "byte for byte".
2. **R2 — byte divergence:** `git diff --no-index devflowOLD/input devflow/input`
   Expected output: all 9 files differ, 11 changed lines (version markers
   `4.2`→`5.0`; `HITL-*`→`AITL-*` in `interviews/README.md`) — the byte-level
   divergence the prescribed check cannot see.
3. **R3 — the textual contradiction:** grep both methodology copies for the
   two rule statements and record the line numbers (rule 1 at ~4579;
   "Everything else… never copied forward" at ~4597). The reproduction is
   deterministic and re-runnable.

**Files created:** none. **Files modified:** none (strictly no edits before
RED is recorded — G19).

---

### Phase 1 — Production change: rule 1 gains the scaffolding carve-out and byte-level verification (both copies)

**Duration:** 1h total cycle — **Complexity:** Low

#### 1.1 Replace rule 1

In BOTH files, replace the current rule-1 text:

```
1. **`input/` in full — 100%, exactly as it stands.** Every file and every
   subfolder the project created inside it, byte for byte. It is raw evidence:
   never normalized, reorganized, filtered, renamed or partially copied
   (§5.6, G31). Afterwards, verify that `devflow/input/` and
   `devflowOLD/input/` have the identical tree and the identical file count.
```

with:

```
1. **`input/` in full — 100%, exactly as it stands, byte for byte — with one
   carve-out: the scaffolding the kit itself installs inside `input/`** (its
   `README.md` and `INDEX.md` files — the same framework files every other
   folder carries) **comes from the new version**, exactly like the
   README/INDEX of any other folder (below). If the project modified one of
   those scaffolding files, the modification is project content and the whole
   file is treated as evidence, preserved byte for byte like any other file
   in `input/`. Every other file in `input/` is raw evidence: never
   normalized, reorganized, filtered, renamed or partially copied (§5.6,
   G31). Afterwards, verify that `devflow/input/` and `devflowOLD/input/`
   have the identical tree and the identical file count, and that every
   non-scaffolding file is byte-identical — a byte-level diff of the
   evidence (e.g. `git diff --no-index devflowOLD/input devflow/input`) must
   show differences only in the scaffolding files. Any difference in an
   evidence file means the copy lost data and the migration stops.
```

The first check (tree + count) is kept — it is cheap and catches missing
files; the byte-identity check of evidence is added, closing the gap.

#### 1.2 Align the "Everything else comes from the new version" paragraph

In BOTH files, in that paragraph, immediately after the sentence
"...are never copied forward." add one cross-reference sentence:

```
The `input/` scaffolding README/INDEX files are covered by this rule with
the carve-out stated in rule 1: they are replaced by the new version unless
the project modified them — in which case they are evidence and are
preserved byte for byte.
```

This removes the contradiction at both ends (ADR-005 phrase-family
discipline: every sentence stating one of the two rules is aligned with the
other).

**Files modified (both copies):**
- `devflow/avenga-devflow/Avenga-DevFlow.md` — §5.16 rule 1 + cross-reference
- `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md` — identical edit (parity)

---

### Phase 2 — GREEN verification (no further edits)

**Duration:** 0.5h total cycle — **Complexity:** Low

Run and capture (deterministic, re-runnable):

- **G1 — positive coverage (ADR-005):** grep both copies for the phrase
  family: the scaffolding carve-out ("scaffolding the kit itself installs"),
  the modified-scaffolding-as-evidence clause, and the byte-identity check
  ("byte-identical", "byte-level diff"). Each phrase must be present in both
  copies.
- **G2 — absence:** grep both copies for the old sole verification wording
  "the identical tree and the identical file count" with no byte-level
  clause in the same rule-1 sentence → zero residue.
- **G3 — scope containment:** `git diff HEAD -- devflow/avenga-devflow/Avenga-DevFlow.md distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md`
  shows changed lines only inside §5.16; `git status --short` shows no other
  non-governance file changed by this V-Bounce (Bolt/BUG/SPEC/INDEX/manifest
  artifacts of this Bolt excluded).
- **G4 — parity:** diff the §5.16 region of the two copies → identical
  (or re-verify full-file byte identity: both files must remain identical
  after the symmetric edit).
- **G5 — invariants:** G-count still 39×5 (`GUARDRAILS.md` untouched — not in
  the edit set); the four agent definitions untouched; `devflow/input/`
  content untouched (this migration's accepted resolution preserved).

**Files created:** none. **Files modified:** none (verification only).

---

### Phase 3 — Governance close-out (executor, mandatory)

**Duration:** 0.5h total cycle — **Complexity:** Low

1. Create the MEM (`devflow/memory/MEM-260823-<HHmm>-input-scaffolding-evidence-clarification.md`)
   with the RED evidence (Phase 0 output) and GREEN evidence (Phase 2 output)
   recorded separately.
2. Append the `v_bounces[]` entry (number 1, spec_revision 1) to
   `devflow/metrics/bolts/US-000.BOLT-014-input-scaffolding-evidence-clarification.json`
   with all eight required fields.
3. Present the package and PAUSE at `AITL-MEM-Approval`.

---

## 7. Acceptance criteria

### AC-1: Scaffolding carve-out is normative

**Given** the two methodology copies
**When** reading §5.16 rule 1 (or grepping for "scaffolding the kit itself installs")
**Then** both state that the kit-installed `README.md`/`INDEX.md` inside `input/` come from the new version, and that a project-modified scaffolding file counts as evidence preserved byte for byte.

### AC-2: Verification catches byte-level evidence differences

**Given** the two methodology copies
**When** reading the post-migration verification of `input/`
**Then** it includes a byte-level check of every non-scaffolding file (byte-identical evidence / byte-level diff), so the BUG-004 reproduction (tree+count pass while evidence bytes differ) cannot occur for evidence.

### AC-3: Contradiction removed at both ends

**Given** the two methodology copies
**When** grepping for the old sole verification wording in rule 1 and for an unqualified "never copied forward" statement that does not cross-reference the rule-1 carve-out
**Then** zero matches — both rules are aligned.

### AC-4: Kit/root parity preserved

**Given** the edit applied to both copies
**When** diffing `devflow/avenga-devflow/Avenga-DevFlow.md` against `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md`
**Then** the files remain byte-identical (or differ only in the recorded, symmetric edit — verified identical after the V-Bounce).

### AC-5: Scope containment

**Given** the V-Bounce execution
**When** running `git status --short` and `git diff HEAD` on the target files
**Then** the only changed non-governance files are the two methodology copies, and their diffs touch only §5.16.

### AC-6: Invariants untouched

**Given** the V-Bounce execution
**When** checking G-count and agent definitions
**Then** G-count remains 39×5, the four agent definitions are unchanged, and `devflow/input/` content is untouched.

### AC mapping to source (non-functional measurable outcome)

| Source outcome (BUG-004 / Bolt §2) | How this SPEC satisfies it | Verifying test/evidence |
|-------------------------------------|----------------------------|--------------------------|
| Scaffolding vs evidence distinction explicit in §5.16 | Rule-1 carve-out + cross-reference sentence (Phases 1.1–1.2) | AC-1, AC-3 greps |
| Verification cannot miss byte-level evidence loss | Byte-identity check added to rule 1 | AC-2; R1+R2 reproduction re-run shows the gap closed |
| Stated identically in operating tree and kit | Symmetric edits to both byte-identical copies | AC-4 parity diff |
| Zero change to any other rule | Scoped edit set (two files, §5.16 only) | AC-5, AC-6 |

---

## 8. Testing strategy

Documentation Bolt — no unit/integration/E2E test suites exist for methodology
text; verification is deterministic, re-runnable grep/diff commands (ADR-005
positive-coverage discipline).

- **RED evidence (Phase 0, before any edit):** R1 tree+count (passes — the
  gap), R2 byte-level diff (9 files/11 lines — the divergence), R3 line
  numbers of the two colliding rules.
- **GREEN evidence (Phase 2):** G1 positive coverage in both copies, G2
  absence of the old wording, G3 scope containment, G4 parity, G5 invariants.
- **Edge cases:** project-modified scaffolding file (the carve-out clause
  covers it — verified by the G1 grep for the "project modified" phrase);
  tree+count check still present (no regression of the existing check);
  both copies edited symmetrically (no drift).
- **BUG evidence:** RED (Phase 0 outputs) → GREEN (Phase 2 outputs),
  recorded separately in the MEM.

---

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | — (no code) | `n/a` — documentation-only Bolt; verification is grep/diff commands |
| SAST / SBOM | — (no code, no third-party) | `n/a` — no buildable artifact or dependency graph |
| Perf-smoke (p95/p99) | — | `n/a` — no runtime component |
| Prompt-injection scan | — | `n/a` — static methodology text, not an externally reachable prompt surface |
| Secret-leak scan | — | `n/a` — no secrets possible in the edited §5.16 text; diff reviewed |
| Hallucination lint | every §5.16 quote and line number in this SPEC must match the file at execution time | `pass` — verified by R3/G1/G3 against the actual file content |
| IP / license provenance | — | `n/a` — no third-party code introduced |
| PII / DLP | — | `n/a` — internal documentation; no personal data |
| Dependency-confusion | — | `n/a` — no dependencies |
| Test-first evidence | RED recorded before any production edit (G19) | `pass` — Phase 0 output captured before Phase 1 |
| Behavioral reproducibility | same commands, same output on re-run | `pass` — R1/R2/G1–G5 deterministic |
| Bolt-manifest validation | manifest validates against `manifest-v5-bolt.schema.json` at every step | `pass` — validated at creation and after each update |

---

## 10. Security and data

- No auth, authorization, secrets, or external surfaces involved — the edit
  is prose in two Markdown files.
- `data_classification: internal` — methodology text; no personal or
  regulated data; PII/DLP gate `n/a`.
- The G31 invariant (input/ raw evidence read-only for agents) is the
  security-relevant property being protected by this fix.

---

## 11. Monitoring and observability

- `n/a` — no runtime component; observability of the fix is the greppable
  §5.16 text itself (G1–G5 evidence).

---

## 12. Migration, compatibility and rollback

- **Migration:** this SPEC is itself the product of a §5.16 migration (4.2 →
  5.0 in progress, uncommitted working tree). The edit applies to the
  working-tree files; the pre-edit content is captured in the RED evidence
  and in `devflowOLD/` (4.2) and HEAD (c0decad).
- **Compatibility:** the first check (tree + count) is kept — the
  strengthened verification is additive; no existing migration step is
  invalidated. The carve-out changes behavior only where scaffolding bytes
  differ (the exact case this migration already resolved).
- **Rollback:** reverse the two edits (restore the quoted current text in
  §5.16) or restore both files from the recorded pre-edit state; no other
  file is affected. The distribution-kit copy is rolled back symmetrically.

---

## 13. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| Partial sweep — another sentence states the rule unaligned | 2 | 3 | ADR-005 phrase-family positive-coverage greps (G1–G3) cover both copies |
| Kit/root drift after edit | 2 | 2 | Symmetric edit + G4 parity diff |
| Baseline drift — working-tree §5.16 differs from this SPEC's quotes at execution time | 1 | 3 | Stop condition S1: re-baseline and stop before editing |
| Third file (outside scope) states the rule | 1 | 3 | Stop condition S2: widen scope only via Bolt revision |
| Uncommitted migration tree interferes with the edit | 2 | 2 | Edit set limited to the two files; verified by G3 |

---

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| Edit rule 1 **and** add a cross-reference in the "Everything else" paragraph | Both rules must align (ADR-005); a carve-out only in rule 1 leaves the other paragraph still reading as an absolute, keeping the contradiction alive for a reader landing there |
| Keep tree + count as the first verification, add byte-identity of evidence as the second | Cheap structural check stays; the new check closes exactly the gap BUG-004 evidenced without invalidating the existing check wording |
| Scaffolding defined as "the kit-installed README.md/INDEX.md files inside input/" | Precise, greppable, matches the 9 files that actually differ; any other file is evidence by definition |
| Project-modified scaffolding file → whole file treated as evidence | Avoids a file-level merge problem; if the project touched it, it is project content (same rule as the AGENTS.md marker merge, §5.16) |
| No edit to §5.6 | §5.6 defines folders and the read-only/G31 property — consistent with the fix; editing it would widen scope without need |

---

## 15. Stop conditions

- **S1 — baseline drift:** the §5.16 text in the working tree at execution
  time differs from the quoted current text (Section 6, Phase 1) → stop,
  re-baseline, revise this SPEC (G15) — never edit blind.
- **S2 — out-of-scope carrier found:** a third file (outside the two
  methodology copies) states the input/ copy rule and needs alignment →
  stop and ask: the Bolt scope must be revised before touching it.
- **S3 — governed source change:** BUG-004 or US-000.BOLT-014 changes
  materially (revision/status) → stop and revise this SPEC (G15).
- **S4 — RED unreproducible:** the Phase 0 reproduction yields different
  results (e.g. input/ trees no longer 9/9 or the diff is empty) → stop and
  report; the BUG's premise changed.
- Any stop condition → MEM with the blocker + manifest entry, then pause
  (§2.12).

---

## 16. Definition of Done (DoD)

- [ ] All phases implemented (0 RED → 1–2 edit → 2 GREEN)
- [ ] All acceptance criteria pass (AC-1..AC-6)
- [ ] RED evidence recorded before any edit; GREEN evidence recorded (BUG protocol)
- [ ] Edits follow the applicable ADRs (ADR-002/004/005)
- [ ] Applicable gates pass / n/a with reason (§9)
- [ ] MEM created in `devflow/memory/` (exactly one per V-Bounce)
- [ ] Manifest `v_bounces[]` entry appended in `devflow/metrics/bolts/` (all eight fields)
- [ ] AITL-MEM-Approval recorded (human)

---

## 17. References

- `devflow/bugs/BUG-004-input-scaffolding-vs-evidence-rule.md`
- `devflow/functional/bolts/US-000.BOLT-014-input-scaffolding-evidence-clarification.md`
- `devflow/adrs/ADR-002-documentation-defect-classification.md`
- `devflow/adrs/ADR-004-repository-partition-v2.md`
- `devflow/adrs/ADR-005-removal-completeness-phrase-family-sweep.md`
- `devflow/metrics/bolts/US-000.BOLT-014-input-scaffolding-evidence-clarification.json`

---

## 18. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-23 | human:eugenio.serrano | Revision 1 — initial SPEC for US-000.BOLT-014 (BUG-004) |

---

## 19. AITL-SPEC-Approval

> **Avenga DevFlow §2.4.1, §3.0.** This SPEC remains a draft until the
> Dev-validator (+ applicable domain owners) records `AITL-SPEC-Approval`
> (in the `review` frontmatter block). Bolt approval (`AITL-BOLT-READY-Approval`)
> authorizes SPEC preparation; **SPEC approval** authorizes the code-run /
> V-Bounce. A material source change invalidates this approval — stop,
> revise, re-approve (G15).

| Field | Value |
|-------|-------|
| **review.reviewers** | Dev-validator + applicable domain owner(s) — minimum one approver |
| **review.decision** | approved / changes_requested / rejected |
| **review_ready_at** | `2026-08-23T11:14:27-03:00` |
| **review.started_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **review.decided_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **Findings** | [findings or acknowledged_without_comment + reason] |
