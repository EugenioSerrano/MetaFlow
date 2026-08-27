---
id: "SPEC-260823-1232"
title: "Root README: English-language convention sentence (ADR-012/ADR-011) — US-000.BOLT-017"
date: "2026-08-23"
author: "human:eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved" # draft | approved | blocked | obsolete
origin: "US-000.BOLT-017"
bolt: "US-000.BOLT-017"
revision: 1 # material revision of this canonical SPEC (matches manifest spec_revisions[])
associated_adrs:
  - "devflow/adrs/ADR-012-english-all-methodology-artifacts-convention.md"
  - "devflow/adrs/ADR-011-english-commit-messages-repository-convention.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
prerequisites: []
risk_class: "low"
autonomy_level: "L3" # defaults by risk: low/medium→L3 (§3.3)
turn_budget: ""
data_classification: "internal"
review_ready_at: "2026-08-23T12:32:05-03:00"
review: # AITL-SPEC-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-23T12:32:45-03:00"
  decided_at: "2026-08-23T12:33:20-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Revision 1 approved: pre-SPEC evidence gate clean (Bolt approved, ADR-012/011/004 accepted, 0 open OQs), target sentence and placement specified exactly, RED/GREEN commands deterministic, stop conditions defined. V-Bounce authorized."
---

# SPEC-260823-1232 — Root README: English-language convention sentence

| Field | Value |
|-------|-------|
| **Origin** | US-000.BOLT-017 (approved 2026-08-23) |
| **Bolt** | [US-000.BOLT-017](../functional/bolts/US-000.BOLT-017-english-commit-messages-readme.md) (approved 2026-08-23) |
| **ADRs** | [ADR-012](../adrs/ADR-012-english-all-methodology-artifacts-convention.md) · [ADR-011](../adrs/ADR-011-english-commit-messages-repository-convention.md) · [ADR-004](../adrs/ADR-004-repository-partition-v2.md) |
| **Risk Class** | low |
| **Revision** | 1 |

---

## 1. Objective

Add one sentence to the root `README.md` (Repository surface, ADR-004) —
in the "Working on the methodology" section — stating the repository
language convention approved in **ADR-012** (generalizing **ADR-011**):
every methodology artifact of this repository, maintenance partition and
kit alike, is written in English, commit and PR messages included. The
sentence carries the ADR references so the governing decisions are citable
from the repository's front door.

If NOT implemented: the convention lives only in the decision log; a
contributor reading the README would not see it where they learn how the
repository works.

---

## 2. Context

ADR-011 (accepted) governs commit/PR messages in English; ADR-012 (accepted)
generalizes it to every methodology artifact in both partitions. The
maintainer wants the convention visible in the root README's
contributing-oriented section. Per ADR-004, the root README is Repository
surface — edited only within a Bolt's scope, which this Bolt provides.

**Repository baseline:** branch `5.1` @ `5278275` + uncommitted working
tree (ADR-011/ADR-012 + BOLT-017 artifacts).

---

## 3. Source inventory and approval references

Pre-SPEC evidence gate (G13, G35): every governed source is approved; zero
open/in-validation OQs against US-000.

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | `devflow/functional/bolts/US-000.BOLT-017-english-commit-messages-readme.md` | AITL-BOLT-READY-Approval ✓ (2026-08-23T12:32) |
| ADR-012 | all methodology artifacts in English (both partitions) | AITL-ADR-Approval ✓ (2026-08-23T12:30) |
| ADR-011 | commit/PR messages in English | AITL-ADR-Approval ✓ (2026-08-23T12:24) |
| ADR-004 | Repository surface — root README enters a Bolt's scope | accepted ✓ |
| OQ index | `devflow/analysis/open-questions/INDEX.md` | 0 open / 0 in-validation (G35 ✓) |
| Repository baseline | branch `5.1` @ `5278275` | — |

---

## 4. Scope

### In scope

- The root `README.md`, one sentence appended to the first paragraph of the
  "Working on the methodology" section.

### Out of scope

- Any other file; any other README section; the AGENTS.md project section
  (the ADRs are the governing record); the kit; the methodology; schemas;
  templates; the version/commit history.

---

## 5. Prerequisites and baseline

- Bolt US-000.BOLT-017 approved; ADR-012/ADR-011/ADR-004 accepted; 0 open OQs.
- Baseline grep (RED) recorded in Phase 0: the convention phrase family is
  absent from the root README.

---

## 6. Phases

Strict evidence ordering: Phase 0 (RED) runs **before any edit**; Phase 1 is
the edit; Phase 2 is the GREEN verification; Phase 3 is governance close-out.
All in the ONE V-Bounce of US-000.BOLT-017.

### Phase 0 — RED evidence (no production change)

**Duration:** 0.5h total cycle — **Complexity:** Low

Capture the baseline:

1. **R1 — absence:** grep the root `README.md` for the convention phrase
   family (`every methodology artifact`, `is written in English`,
   `ADR-011`, `ADR-012`) → **zero matches** (the ADR refs appear nowhere in
   the README).
2. **R2 — anchor:** record the exact current text of the first paragraph of
   "Working on the methodology" (ends with "…No edit to the methodology
   reaches the kit outside that path.").

**Files created:** none. **Files modified:** none (strictly no edits before
RED is recorded).

---

### Phase 1 — Production change: the sentence (one edit)

**Duration:** 0.5h total cycle — **Complexity:** Low

In the root `README.md`, in the "Working on the methodology" section, append
to the first paragraph — immediately after "…No edit to the methodology
reaches the kit outside that path." — the following sentence:

```
**Language:** every methodology artifact of this repository — the maintenance
partition and the kit alike — is written in English, commit and PR messages
included (ADR-011, ADR-012).
```

The result reads:

```
**Changes to DevFlow are governed by DevFlow.** … No edit to the
methodology reaches the kit outside that path. **Language:** every methodology
artifact of this repository — the maintenance partition and the kit alike —
is written in English, commit and PR messages included (ADR-011, ADR-012).
```

Nothing else changes: the rest of the file is byte-identical.

**Files modified:**
- `README.md` — one sentence appended to the "Working on the methodology"
  first paragraph.

---

### Phase 2 — GREEN verification (no further edits)

**Duration:** 0.5h total cycle — **Complexity:** Low

Run and capture:

- **G1 — presence:** grep the root `README.md` for `every methodology
  artifact` and `ADR-011, ADR-012` → both present exactly once.
- **G2 — scoped diff:** `git diff README.md` shows only the added sentence
  (one hunk, the appended lines) — no other change.
- **G3 — scope containment:** `git status --short` shows only `README.md`
  (plus this Bolt's governance artifacts) changed by this V-Bounce.
- **G4 — encoding:** no BOM, no replacement characters in the edited file
  (byte check).

**Files created:** none. **Files modified:** none (verification only).

---

### Phase 3 — Governance close-out (executor, mandatory)

**Duration:** 0.5h total cycle — **Complexity:** Low

1. MEM (`devflow/memory/MEM-260823-<HHmm>-english-convention-readme.md`)
   with RED (Phase 0) and GREEN (Phase 2) evidence.
2. `v_bounces[]` entry (number 1, spec_revision 1) appended to
   `devflow/metrics/bolts/US-000.BOLT-017-english-commit-messages-readme.json`.
3. Present the package and PAUSE at `AITL-MEM-Approval`.

---

## 7. Acceptance criteria

### AC-1: Convention sentence present with ADR references

**Given** the root `README.md`
**When** reading the "Working on the methodology" section
**Then** the first paragraph ends with the language-convention sentence
citing ADR-011 and ADR-012, exactly as specified in Phase 1.

### AC-2: Diff scoped to the single addition

**Given** the V-Bounce execution
**When** running `git diff README.md`
**Then** the only change is the added sentence (one hunk) — no other text
modified.

### AC-3: Scope containment

**Given** the V-Bounce execution
**When** running `git status --short`
**Then** only `README.md` and this Bolt's governance artifacts changed.

### AC mapping to source (non-functional measurable outcome)

| Source outcome (Bolt §2) | How this SPEC satisfies it | Verifying test/evidence |
|---------------------------|----------------------------|--------------------------|
| Convention visible in the README | Phase 1 appends the sentence | AC-1 (G1) |
| Single-sentence change | One edit, byte-identical elsewhere | AC-2 (G2) |
| No other file touched | Edit set bounded to README.md | AC-3 (G3) |

---

## 8. Testing strategy

Documentation sentence — no unit/integration suites; verification is
deterministic grep/diff commands.

- **RED evidence (Phase 0):** R1 absence greps (zero matches), R2 anchor
  text recorded.
- **GREEN evidence (Phase 2):** G1 presence (exactly once), G2 scoped diff,
  G3 scope containment, G4 encoding.
- **Edge cases:** the sentence must not duplicate existing text (R1 proves
  absence); the ADR references must match the governing decisions' IDs.

---

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | — (no code) | `n/a` — one documentation sentence |
| SAST / SBOM | — | `n/a` — no buildable artifact |
| Perf-smoke (p95/p99) | — | `n/a` — no runtime |
| Prompt-injection scan | — | `n/a` — static README text |
| Secret-leak scan | — | `n/a` — no secrets; diff reviewed |
| Hallucination lint | the ADR references and quoted text match the files | `pass` — verified by R2/G1 |
| IP / license provenance | — | `n/a` — no third-party content |
| PII / DLP | — | `n/a` — internal documentation |
| Dependency-confusion | — | `n/a` — no dependencies |
| Test-first evidence | RED recorded before the edit | `pass` — Phase 0 before Phase 1 |
| Behavioral reproducibility | same commands, same output | `pass` — deterministic greps |
| Bolt-manifest validation | manifest validates at every step | `pass` — validated at creation and after each update |

---

## 10. Security and data

- No auth, secrets or external surfaces — one prose sentence in the root
  README.
- `data_classification: internal`.

---

## 11. Monitoring and observability

- `n/a` — no runtime; observability is the greppable sentence itself.

---

## 12. Migration, compatibility and rollback

- **Migration:** none.
- **Compatibility:** the README keeps its structure; only one paragraph
  gains a sentence.
- **Rollback:** remove the sentence (reverse the one edit) or `git checkout`
  from the committed baseline.

---

## 13. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| Wrong placement / duplicated text | 1 | 2 | R1 absence proof; G2 scoped diff |
| ADR reference drift | 1 | 2 | G1 greps the exact IDs; hallucination-lint |
| Encoding corruption | 1 | 2 | G4 byte check |

---

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| Sentence placed at the end of the first "Working on the methodology" paragraph | The paragraph is the section's intro on how the repository is governed/contributed to — the natural place a contributor learns conventions; a bullet would imply a procedure, this is a convention |
| Both ADR-011 and ADR-012 cited | ADR-012 is the general rule; ADR-011 remains the commit/PR citation — the sentence covers both scopes explicitly |
| "maintenance partition and the kit alike" phrasing | Mirrors the ADR-012 decision's two-partition scope in the README's own vocabulary |

---

## 15. Stop conditions

- **S1 — baseline drift:** the anchor paragraph differs from R2 at execution
  time → stop, re-baseline, revise this SPEC (G15).
- **S2 — unexpected matches:** R1 finds the phrase family already present →
  stop and report (the premise changed).
- Any stop condition → MEM with the blocker + manifest entry, then pause
  (§2.12).

---

## 16. Definition of Done (DoD)

- [ ] All phases implemented (0 RED → 1 edit → 2 GREEN)
- [ ] All acceptance criteria pass (AC-1..AC-3)
- [ ] RED evidence recorded before any edit; GREEN evidence recorded
- [ ] Edit follows ADR-012/ADR-011/ADR-004
- [ ] Applicable gates pass / n/a with reason (§9)
- [ ] MEM created in `devflow/memory/` (exactly one per V-Bounce)
- [ ] Manifest `v_bounces[]` entry appended (all eight fields)
- [ ] AITL-MEM-Approval recorded (human)

---

## 17. References

- `devflow/functional/bolts/US-000.BOLT-017-english-commit-messages-readme.md`
- `devflow/adrs/ADR-012-english-all-methodology-artifacts-convention.md`
- `devflow/adrs/ADR-011-english-commit-messages-repository-convention.md`
- `devflow/adrs/ADR-004-repository-partition-v2.md`
- `devflow/metrics/bolts/US-000.BOLT-017-english-commit-messages-readme.json`

---

## 18. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-23 | human:eugenio.serrano | Revision 1 — initial SPEC for US-000.BOLT-017 |

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
| **review_ready_at** | `2026-08-23T12:32:05-03:00` |
| **review.started_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **review.decided_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **Findings** | [findings or acknowledged_without_comment + reason] |
