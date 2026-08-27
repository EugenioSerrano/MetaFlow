---
id: "MEM-260823-1233"
title: "Root README English-language convention sentence — US-000.BOLT-017 V-Bounce 1"
date: "2026-08-23"
author: "human:eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
bolt: "US-000.BOLT-017"
spec: "SPEC-260823-1232"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "5278275 (branch 5.1) + uncommitted ADR-011/012 + BOLT-017 artifacts"
applied_adrs:
  - "devflow/adrs/ADR-012-english-all-methodology-artifacts-convention.md"
  - "devflow/adrs/ADR-011-english-commit-messages-repository-convention.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "devflow/metrics/bolts/US-000.BOLT-017-english-commit-messages-readme.json"
diff_ref: "working tree — README.md, one appended sentence"
review_ready_at: "2026-08-23T12:33:58-03:00"
review: # AITL-MEM-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-23T12:40:15-03:00"
  decided_at: "2026-08-23T12:40:30-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "V-Bounce 1 approved: README diff inspected (single hunk +3, only the language-convention sentence with ADR-011/ADR-012 references), RED (R1 zero matches, R2 anchor) before the edit, GREEN (G1 1x1 presence, G2 scoped diff, G3 status, G4 clean encoding), gates table (test-first pass, others n/a), manifest v_bounces[1] complete. Bolt → Development Completed."
---

# MEM-260823-1233 — Root README English-language convention sentence

| Field           | Value |
|-----------------|-------|
| **Bolt**        | US-000.BOLT-017 |
| **SPEC**        | [SPEC-260823-1232](../spec/SPEC-260823-1232-english-convention-readme.md), revision 1 |
| **V-Bounce**    | 1 |
| **ADRs**        | ADR-012 · ADR-011 · ADR-004 |

---

## 1. Executive summary

This V-Bounce added the repository language convention to the root README's
contributing section: the first paragraph of "Working on the methodology"
now ends with "**Language:** every methodology artifact of this repository —
the maintenance partition and the kit alike — is written in English, commit
and PR messages included (ADR-011, ADR-012)." The sentence makes the
convention approved in ADR-012 (generalizing ADR-011) visible at the
repository's front door, delivered through the proper Repository-surface
path (ADR-004: a Bolt's scope). The RED baseline proved the phrase family
was absent (zero matches); the GREEN verification confirms the sentence
appears exactly once with the exact ADR references, the diff is scoped to
the single addition (one hunk, +3 lines), `git status` shows only
`README.md` plus this Bolt's governance artifacts, and the file encoding is
clean (no BOM, no replacement characters). The V-Bounce ran strict
evidence-first: RED recorded before the edit, GREEN after.

---

## 2. Implemented phases

### Phase 0 — RED evidence (no production change)

Captured before any edit: R1 greps of the convention phrase family
(`every methodology artifact`, `is written in English`, `ADR-011`,
`ADR-012`) over the root `README.md` returned **zero matches**; R2 recorded
the exact anchor text of the "Working on the methodology" first paragraph
(ending with "…No edit to the methodology reaches the kit outside that
path."). No files were created or modified.

### Phase 1 — Production change (one edit)

Appended to the anchor paragraph, immediately after "…outside that path.",
the SPEC's exact sentence: "**Language:** every methodology artifact of this
repository — the maintenance partition and the kit alike — is written in
English, commit and PR messages included (ADR-011, ADR-012)." Nothing else
in the file changed.

### Phase 2 — GREEN verification (no further edits)

- **G1 presence:** `every methodology` → 1 match; `ADR-011, ADR-012` → 1
  match (the exact reference string).
- **G2 scoped diff:** `git diff README.md` = one hunk, +3 lines, only the
  sentence; no other text touched.
- **G3 scope containment:** `git status --short` shows `README.md` and this
  Bolt's governance artifacts (ADR-011, ADR-012, Bolt doc, manifest, SPEC,
  the two INDEX updates) — no other file.
- **G4 encoding:** 0 replacement characters, no BOM.

---

## 3. Files created

| File | Purpose |
|------|---------|
| `devflow/memory/MEM-260823-1233-english-convention-readme.md` | This MEM — the immutable V-Bounce record with RED and GREEN evidence |
| (Bolt lifecycle, pre-V-Bounce) `devflow/adrs/ADR-012-…`, `devflow/spec/SPEC-260823-1232-…`, `devflow/functional/bolts/US-000.BOLT-017-…`, `devflow/metrics/bolts/US-000.BOLT-017-….json` | The governed artifacts of this Bolt (ADR-011 created in the same working session) |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `README.md` | "Working on the methodology" first paragraph gains the language-convention sentence with ADR-011/ADR-012 references (+3 lines) |

## 5. Files renamed

None.

## 6. Files deleted

None.

---

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| Sentence appended to the section's first paragraph (not a bullet) | A bullet implies a procedure; this is a convention — the paragraph is where a contributor learns how the repository works |
| Both ADR-011 and ADR-012 cited | ADR-012 is the general rule, ADR-011 the commit/PR citation — the sentence covers both scopes explicitly |
| Wording mirrors ADR-012's two-partition scope | "the maintenance partition and the kit alike" matches the decision's own vocabulary (ADR-004's two trees) |
| Single hunk, +3 lines | The Bolt's completion evidence (one sentence, byte-identical elsewhere) — verified by G2 |

---

## 8. Deviations and assumptions

- **No deviation from the SPEC.** The sentence, placement and verification
  match revision 1 exactly.
- **Assumption:** the working tree remains uncommitted until the human
  decides (no commit was made — G34).

---

## 9. Verification evidence

### Build

```
n/a — one documentation sentence; no buildable artifact exists.
```

### Tests

```
n/a — verification is deterministic grep/diff commands (below).
```

### RED → GREEN evidence

- **RED (before any edit):**
  ```
  R1 — 'every methodology artifact' 0 · 'is written in English' 0 · 'ADR-011' 0 · 'ADR-012' 0
  R2 — anchor paragraph recorded (ends "...No edit to the methodology reaches the kit outside that path.")
  ```
- **GREEN (after the edit):**
  ```
  G1 — 'every methodology' 1 · 'ADR-011, ADR-012' 1
  G2 — git diff README.md: one hunk, +3 lines (only the sentence)
  G3 — git status: README.md + this Bolt's governance artifacts only
  G4 — 0 replacement chars, no BOM
  ```

### Gates

| Gate | Result |
|------|--------|
| Test-first evidence | `pass` — RED (R1/R2) recorded before the edit |
| Behavioral reproducibility | `pass` — deterministic greps |
| Hallucination lint | `pass` — ADR references and anchor text matched the files |
| Bolt-manifest validation | `pass` — manifest parsed and checked against the v5 schema at creation, approval and v_bounces update |
| Unit/integration, SAST/SBOM, perf-smoke, prompt-injection, secret-leak, IP/license, PII/DLP, dependency-confusion | `n/a` — one documentation sentence (reasons in SPEC §9) |

---

## 10. Manual interventions

None.

---

## 11. Evidence links

- **Diff / PR:** none — uncommitted working tree; the diff is the README.md
  single-hunk addition (+3 lines).
- **Commit:** none yet (baseline `5278275`).
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-000.BOLT-017-english-commit-messages-readme.json`

---

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~10 min (artifacts + V-Bounce, agent-generated) |
| V-Bounce number | 1 |
| Tests created | 0 (6 deterministic verification commands — documentation Bolt) |
| AI-generated code | 100% |
| First-pass approval | pending (this review) |

---

## 13. Pending items and stubs

- [ ] Human review of this MEM (`AITL-MEM-Approval`) — pending.
- [ ] After approval: `AITL-BOLT-DONE-Approval` (work_category `refactor` → Tech Lead) — pending.
- [ ] The working tree (ADR-011/012 + BOLT-017 package + README sentence) remains uncommitted (human decision, G34).

---

## 14. AITL-MEM-Approval

> **Avenga DevFlow §2.12, §3.0.** This MEM is created by the agent with no
> mutable status and is **never self-approved**. A qualified human (the
> Dev-validator who executed the Bolt; QA/Sec/domain reviewers optional, any risk)
> inspects the actual diff, test/gate evidence, MEM and manifest, and
> records `AITL-MEM-Approval` here and in the manifest's
> `checkpoint_approvals[]`. `approved` completes the V-Bounce (and, if latest,
> marks the Bolt `Development Completed`); `changes_requested` keeps this
> MEM as immutable history and the next execution is a NEW V-Bounce with a
> NEW MEM. `AITL-BOLT-DONE-Approval` is still required for `Done`.

| Field | Value |
|-------|-------|
| **Reviewers (executing Dev-validator; QA/Sec/domain optional)** | `human:eugenio.serrano` |
| **Roles** | dev_validator |
| **Decision** | approved |
| **review_ready_at** | `2026-08-23T12:33:58-03:00` |
| **review.started_at** | `2026-08-23T12:40:15-03:00` |
| **review.decided_at** | `2026-08-23T12:40:30-03:00` |
| **Review evidence** | README diff (single hunk +3), RED (R1/R2) and GREEN (G1–G4) outputs, gates table, manifest v_bounces[1] |
| **Comments** | — |
| **Findings** | none |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | Diff + RED/GREEN evidence + gates + manifest inspected (see frontmatter acknowledgment_reason) |
