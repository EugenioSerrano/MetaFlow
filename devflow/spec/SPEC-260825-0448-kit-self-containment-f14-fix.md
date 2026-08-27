---
id: "SPEC-260825-0448"
title: "BUG-005 fix — remove the F-14 finding reference from VERIFICATION.md (US-025.BOLT-007)"
date: "2026-08-25"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved" # draft | approved | blocked | obsolete — AITL-SPEC-Approval 2026-08-25
origin: "BUG-005" # the governing defect
bolt: "US-025.BOLT-007" # ⚠️ MANDATORY — approved 2026-08-25 (AITL-BOLT-READY-Approval)
revision: 1 # material revision of this canonical SPEC (matches manifest spec_revisions[])
associated_adrs:
  - "devflow/adrs/ADR-004-repository-partition-v2.md" # kit-only partition
prerequisites: []
risk_class: "low" # mirrors the Bolt's risk_class
autonomy_level: "L3" # low → L3 (default)
turn_budget: "" # leave empty — platform default
data_classification: "internal"
review_ready_at: "2026-08-25T04:48:07-03:00"
review: # AITL-SPEC-Approval — decision dictated in conversation ("aprobado!") and transcribed by the agent (§3.0)
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-25T04:49:52-03:00"
  decided_at: "2026-08-25T04:49:52-03:00"
  findings: []
  acknowledged_without_comment: true # must be true when findings is empty (§3.0)
  acknowledgment_reason: "Approved as Dev-validator: source inventory verified (BUG-005, US-025, ADR-004 all approved), the exact replacement text reviewed, the strict TDD contract (RED before any edit) and the stop conditions (S2 — never extend scope) explicit. Authorizes the V-Bounce."
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs, and section
  headings (##) stay in English (the schema). Prose in English (ADR-012).
-->

# SPEC-260825-0448 — BUG-005 fix: kit self-containment residue

| Field | Value |
|-------|-------|
| **Origin** | BUG-005 (approved 2026-08-25) |
| **Bolt** | US-025.BOLT-007 (AITL-BOLT-READY-Approval 2026-08-25) |
| **ADRs** | ADR-004 (repository partition — kit-only) |
| **Risk Class** | low |
| **Revision** | 1 |

---

## 1. Objective

Remove the maintenance-partition residue shipped in
`distribution-kit/devflow/agents/VERIFICATION.md` by US-025.BOLT-006's
V-Bounce: the phrase "(the F-14 shape — ...)" references finding F-14 of
the maintainer's REV-005, which no adopter can resolve. The sentence is
reworded with kit-internal vocabulary only, restoring US-025 AC-9
(kit self-containment). **What if NOT done:** the kit keeps shipping a
reference to maintainer-internal records — every adopter copy carries
unresolvable vocabulary, and any future self-containment audit of the kit
flags it (BUG-005).

---

## 2. Context

The self-containment sweep (2026-08-25, maintainer request) found exactly
one confirmed residue: `F-14` at VERIFICATION.md:51. Root cause: the
execution-evidence paragraph was written from the SPEC-260825-0417 Phase
B.2 wording, which used "the F-14 shape" as shorthand for REV-005's
finding on the Coordinator-persists-executor-production pattern. The
shorthand is maintainer vocabulary that leaked into kit text. BUG-005
(severity low, nature functional — US-025 AC-9 violation) was opened and
approved; US-025.BOLT-007 is its dedicated Bolt. This SPEC fixes it with
strict TDD in ONE V-Bounce: red (grep reproduction) → production fix →
green (grep clean + invariants).

---

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | US-025.BOLT-007 | AITL-BOLT-READY-Approval ✓ (2026-08-25) |
| BUG | BUG-005 | AITL-BUG-Approval ✓ (2026-08-25) |
| Feature US | US-025 (AC-9) | AITL-US-Approval ✓ (2026-08-24) |
| ADR | ADR-004 | AITL-ADR-Approval ✓ |
| Repository baseline | `b3ddb4e` | — |

---

## 4. Scope

### In scope

- One sentence in `distribution-kit/devflow/agents/VERIFICATION.md`
  (the execution-evidence paragraph, line ~51): the `F-14` reference
  reworded self-containedly.
- The TDD evidence: red grep → fix → green grep + full sweep re-run +
  invariants (G-count, sync diff, frontmatter).

### Out of scope

- Any other kit file, agent body, or frontmatter.
- The soft residue (`human:eugenio.serrano` example actors — 17
  occurrences) — separate cleanup candidate, explicitly NOT this Bolt.
- Any change to the governance-side records (SPEC/BOLT/MEM texts may
  keep maintainer vocabulary — they live in the maintainer partition).

---

## 5. Prerequisites and baseline

- US-025.BOLT-006 Done (the text being corrected is in the tree at
  `b3ddb4e` + the uncommitted V-Bounce 1 changes — the working tree IS
  the baseline for this fix).
- Baseline: repository HEAD `b3ddb4e` (the BOLT-006 changes are
  uncommitted working-tree state).

---

## 6. Phases

### Phase A — Strict TDD: reproduce (RED), fix, verify (GREEN)

**Duration:** 0.5h total cycle — **Complexity:** Low

#### A.1 RED — capture the failing reproduction BEFORE any edit

Run and record:
```
grep -n "F-14" distribution-kit/
```
Expected output (recorded as the RED evidence): the single hit at
`distribution-kit/devflow/agents/VERIFICATION.md:51`. No file is touched
before this evidence exists (BUG protocol, §3.3.1).

#### A.2 The production fix (exact replacement)

`distribution-kit/devflow/agents/VERIFICATION.md`, execution-evidence
paragraph. Replace:

> "(the F-14 shape — the reviewer "produces REVs" with `write_paths: []`)"

with:

> "(the shape where an executor with `write_paths: []` still produces —
> the Coordinator persists its output)"

The rest of the paragraph is unchanged: "...but the persistence act must
trace to a **real spawn**: a stamp of another actor's identity on content
that actor never produced is a false claim, not governed authorship...".
The replacement keeps the full meaning (executor produces, Coordinator
persists) with zero maintainer vocabulary.

**Files modified:**
- `distribution-kit/devflow/agents/VERIFICATION.md` — one phrase, one
  line.

#### A.3 GREEN — verify

```
grep -n "F-14" distribution-kit/            # expected: 0 hits
grep -rnE "\b[FC]-[0-9]{2}\b" distribution-kit/   # expected: only the template placeholders (F-01/F-02/F-03 in TEMPLATE-REV/AREV-*)
```

Then the invariants:
- G-count sweep: `^\| G[0-9]{2} \|` = 39/39 in GUARDRAILS.md + the four
  agent files.
- Four-agent sync diff (methodology heading → EOF): unchanged from the
  BOLT-006 state (2 sanctioned lines per comparison — the touched file
  is not an agent body).
- Frontmatter of VERIFICATION.md untouched (it has none — the file's
  structure unchanged).

---

## 7. Acceptance criteria

### AC-1: The residue is gone

**Given** the updated kit,
**When** `grep -n "F-14" distribution-kit/` runs,
**Then** it returns 0 hits (and the RED evidence of the pre-fix hit at
line 51 is recorded in the MEM).

### AC-2: The kit sweep stays clean

**Given** the updated kit,
**When** the full finding-ID sweep runs (`F-NN`/`C-NN`),
**Then** only the sanctioned template placeholders (F-01/F-02/F-03 in
TEMPLATE-REV and TEMPLATE-AREV-*) match — no other finding references.

### AC-3: Invariants hold

**Given** the updated kit,
**When** the G-count and sync-diff checks run,
**Then** G-count is 39/39 everywhere and the four-agent shared body is
byte-identical (2 sanctioned path lines only).

### AC mapping to source

| Source AC / outcome | How this SPEC satisfies it | Verifying test/evidence |
|---------------------|----------------------------|--------------------------|
| US-025 AC-9 (kit self-containment) | The F-14 reference removed; kit vocabulary only | AC-1 + AC-2 |
| BUG-005 expected_result | grep reproduction red → green | AC-1 (RED evidence in the MEM) |
| BUG-005 routing (US-025) | Dedicated Bolt under US-025 executed | the V-Bounce records |

---

## 8. Testing strategy

- **Unit tests:** n/a — docs fix; the "tests" are the deterministic
  greps (the BUG protocol's reproduction test IS the grep).
- **Integration tests:** n/a.
- **E2E tests:** n/a.
- **Edge cases:** the sweep must distinguish sanctioned template
  placeholders (F-01..F-03 in TEMPLATE-REV/AREV) from residue — the
  AC-2 grep lists the expected whitelist; the G-count and sync diff must
  not move.
- **BUG evidence:** RED = `grep -n "F-14" distribution-kit/` → 1 hit
  (recorded BEFORE the edit); GREEN = same command → 0 hits + AC-2/AC-3.

---

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | — | n/a — docs fix, no runtime |
| SAST / SBOM | — | n/a — no dependencies |
| Perf-smoke (p95/p99) | — | n/a — no runtime |
| Prompt-injection scan | — | n/a — no new executable content |
| Secret-leak scan | — | pass — no secrets |
| Hallucination lint | — | pass — the replacement is a verbatim reword verified by grep |
| IP / license provenance | — | n/a — no third-party content |
| PII / DLP | — | n/a — internal docs |
| Dependency-confusion | — | n/a — no dependencies |
| Test-first evidence | — | pass — RED evidence captured before the fix (BUG protocol) |
| Behavioral reproducibility | — | pass — the greps are deterministic |
| Bolt-manifest validation | — | pass — BOLT-007 manifest validates |

---

## 10. Security and data

- No security surface: one doc phrase. No secrets, no PII;
  `data_classification` internal.
- The change removes a reference that could leak maintainer-internal
  artifact vocabulary into adopter projects (a self-containment/hygiene
  control, ADR-004).

---

## 11. Monitoring and observability

n/a — the "monitoring" is the self-containment sweep; per the C-25
lesson, the sweep now belongs in the V-Bounce evidence of any kit-text
change (candidate for the lifecycle-step family, C-2 destination).

---

## 12. Migration, compatibility and rollback

- **Migration:** N/A — kit docs; adopters get the fix on the next copy.
- **Compatibility:** the sentence meaning is unchanged for readers; no
  tooling reads that phrase.
- **Rollback:** restore VERIFICATION.md from the working-tree state
  (revert the one-line change); the greps immediately re-verify.

---

## 13. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| The reword loses meaning | 2 | 2 | SPEC fixes the exact replacement; reviewer checks the paragraph in the MEM |
| The sweep catches other residue mid-V-Bounce | 2 | 3 | Stop condition S2 — record and route separately, never extend scope |
| Invariant drift (G-count/sync) | 1 | 3 | Gates in A.3 |

---

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| Reword "the F-14 shape" → "the shape where an executor with `write_paths: []` still produces" | Keeps the exact meaning (executor produces, Coordinator persists) with kit vocabulary; mirrors the F-14 finding's content without its ID |
| Fix-only this one sentence | The sweep found exactly one confirmed residue; the soft residue is a separate cleanup candidate |
| RED evidence via grep before any edit | The BUG protocol's strict TDD (§3.3.1) — production may not change before red evidence |

---

## 15. Stop conditions

- **S1** — The RED reproduction does not reproduce (no F-14 hit at the
  expected location) → stop; reconcile the baseline before proceeding.
- **S2** — The GREEN sweep finds additional residue beyond the sanctioned
  whitelist → stop; record the new hits in the MEM, route them as a new
  finding/BUG — never extend this Bolt's scope.
- **S3** — G-count or the four-agent sync diff drifts → stop; restore the
  invariant before continuing.

---

## 16. Definition of Done (DoD)

- [ ] Phase A complete (RED → fix → GREEN)
- [ ] AC-1, AC-2, AC-3 pass
- [ ] RED and GREEN evidence recorded in the MEM (BUG protocol)
- [ ] Code follows applicable ADRs (ADR-004)
- [ ] Applicable gates pass / waived (ADR) / n/a (reason)
- [ ] MEM created in `devflow/memory/` (exactly one per V-Bounce)
- [ ] Manifest `v_bounces[]` entry appended in `devflow/metrics/bolts/`
- [ ] AITL-MEM-Approval recorded

---

## 17. References

- BUG-005-kit-self-containment-f14-residue.md (approved 2026-08-25)
- US-025.BOLT-007-kit-self-containment-f14-fix.md (approved)
- US-025-mainagent-agent-lifecycle.md (AC-9)
- ADR-004-repository-partition-v2.md

---

## 18. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-25 | eugenio.serrano (agent-drafted, deepseek/deepseek-v4-flash) | Initial draft (revision 1) |
| 2026-08-25 | eugenio.serrano | AITL-SPEC-Approval recorded — V-Bounce authorized |

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
| **review.reviewers** | eugenio.serrano (dev_validator) |
| **review.decision** | **approved** |
| **review_ready_at** | `2026-08-25T04:48:07-03:00` |
| **review.started_at** | `2026-08-25T04:49:52-03:00` |
| **review.decided_at** | `2026-08-25T04:49:52-03:00` |
| **Findings** | none on the SPEC itself — approved with the exact replacement and the TDD contract (reason in the frontmatter `review:` block) |
