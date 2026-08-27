---
id: "MEM-260823-1120"
title: "§5.16 input/ scaffolding vs raw evidence clarification — US-000.BOLT-014 V-Bounce 1 (BUG-004)"
date: "2026-08-23"
author: "human:eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
bolt: "US-000.BOLT-014"
spec: "SPEC-260823-1114"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "c0decad + uncommitted 4.2→5.0 migration working tree (devflow/ = kit 5.0 install; devflowOLD/ = 4.2 copy)"
applied_adrs:
  - "devflow/adrs/ADR-002-documentation-defect-classification.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
  - "devflow/adrs/ADR-005-removal-completeness-phrase-family-sweep.md"
manifest: "devflow/metrics/bolts/US-000.BOLT-014-input-scaffolding-evidence-clarification.json"
diff_ref: "uncommitted working tree — the two methodology copies, §5.16 region only"
review_ready_at: "2026-08-23T11:20:06-03:00"
review: # AITL-MEM-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-23T11:20:45-03:00"
  decided_at: "2026-08-23T11:21:00-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "V-Bounce 1 approved: inspected the §5.16 diff of both methodology copies (rule 1 carve-out + cross-reference, parity byte-identical at 292,738 chars), RED evidence captured before any edit (R1 prescribed check passes 9/9 with 0 tree diffs while R2 shows 9 files/11+11- diverging, R3 colliding rules at L4579/L4597), GREEN evidence (G1 5/5 phrases both copies, G2 zero residue, G3 scope via edit log+git status, G4 parity, G5 G-count 39 + agents untouched), gates table (test-first pass, others n/a with reasons), manifest v_bounces[1] complete. Deviation G3-vs-uncommitted-migration-baseline recorded transparently (§8). Bolt → Development Completed."
---

# MEM-260823-1120 — §5.16 input/ scaffolding vs raw evidence clarification

| Field           | Value |
|-----------------|-------|
| **Bolt**        | US-000.BOLT-014 (BUG-004) |
| **SPEC**        | [SPEC-260823-1114](../spec/SPEC-260823-1114-input-scaffolding-evidence-clarification.md), revision 1 |
| **V-Bounce**    | 1 |
| **ADRs**        | ADR-002 · ADR-004 · ADR-005 |

---

## 1. Executive summary

This V-Bounce fixed the §5.16 ambiguity evidenced by BUG-004: the migration
procedure's `input/` rule ("in full, byte for byte") and its
"everything-else-comes-from-the-new-version" rule collided for the scaffolding
README/INDEX files the kit installs inside `input/`, and the prescribed
post-migration verification (tree + file count) could not detect byte-level
differences — reproduced here with the prescribed check passing (9/9 files,
0 tree differences) while all 9 scaffolding files differ by 11 lines. The fix
replaced §5.16 rule 1 in both methodology copies (`devflow/` and the
distribution kit) with an explicit carve-out — kit-installed `input/`
README/INDEX files come from the new version, and if the project modified one
it counts as evidence preserved byte for byte — and added a byte-level
verification of every non-scaffolding file ("byte-identical", byte-level
diff), plus a cross-reference sentence in the "Everything else comes from the
new version" paragraph so the two rules no longer contradict each other.
Both copies remain byte-identical after the symmetric edit (parity
preserved), all positive-coverage and absence greps pass, and no other rule,
guardrail (G-count still 39), agent definition, schema or tooling was
touched. The V-Bounce ran strict TDD: RED evidence (R1/R2/R3) was captured
before any edit; GREEN evidence (G1–G5) confirms the defect is closed and
the §5.16 text now states that a migration losing evidence stops.

---

## 2. Implemented phases

### Phase 0 — RED evidence (no production change)

Reproduced BUG-004 deterministically before touching any file: R1 ran the
prescribed §5.16 verification (recursive file listing of `devflow/input` vs
`devflowOLD/input`, relative-path comparison and count) and it PASSES — 9/9
files, 0 tree differences — although rule 1 demands byte-for-byte copy; R2
ran `git diff --no-index devflowOLD/input devflow/input` showing all 9
scaffolding files differ (11 insertions / 11 deletions: `Methodology
version: 4.2`→`5.0` and `HITL-*`→`AITL-*` names in `interviews/README.md`);
R3 located the two colliding normative statements in the working-tree
methodology (rule 1 at L4579, "Everything else comes from the new version"
at L4597, "are never copied forward" at L4601). No files were created or
modified in this phase.

### Phase 1 — Production change (§5.16, both copies)

Applied the SPEC's target text verbatim to `devflow/avenga-devflow/Avenga-DevFlow.md`
and `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md` (the two
files were byte-identical before the edit, 291,738 chars each, and received
identical edits):
1. Rule 1 replaced with the carve-out version: the kit-installed
   `README.md`/`INDEX.md` inside `input/` come from the new version (like
   any other folder's README/INDEX); a project-modified scaffolding file is
   project content and is treated as evidence; every other `input/` file is
   raw evidence copied byte for byte (§5.6, G31); the post-migration
   verification now requires identical tree, identical file count **and**
   byte-identical non-scaffolding files, checked by a byte-level diff that
   may show differences only in scaffolding — any evidence difference means
   the copy lost data and the migration stops.
2. One cross-reference sentence added to the "Everything else comes from the
   new version" paragraph, immediately after "are never copied forward.",
   stating that `input/` scaffolding README/INDEX are covered by that rule
   with the rule-1 carve-out (replaced by the new version unless the project
   modified them → evidence, preserved byte for byte).

The edit keeps the existing tree+count check (cheap structural guard) and
adds the byte-level check additively, exactly as the SPEC prescribed.

### Phase 2 — GREEN verification (no further edits)

All SPEC §8/§7 checks executed and passed: G1 positive coverage (5/5 phrase
hits in each copy: "scaffolding the kit itself installs", "byte-identical",
"byte-level diff", "project modified", "carve-out stated in"); G2 absence
(0 matches of the old rule-1 heading "exactly as it stands.** Every file",
0 bare "identical file count." — the sentence now continues into the byte
clause); G4 parity (both copies identical after the symmetric edit,
292,738 chars each); G5 invariants (G-count in GUARDRAILS.md = 39; agent
definitions untouched). G3 scope containment was verified via the edit log
and `git status` (only the two methodology files modified by this V-Bounce
plus the four governance artifacts; the root file also carries the
pre-existing, uncommitted 4.2→5.0 migration diff vs HEAD, which is not part
of this V-Bounce — see §8).

---

## 3. Files created

| File | Purpose |
|------|---------|
| `devflow/memory/MEM-260823-1120-input-scaffolding-evidence-clarification.md` | This MEM — the immutable V-Bounce record with RED and GREEN evidence |
| (Bolt lifecycle, pre-V-Bounce) `devflow/spec/SPEC-260823-1114-…`, `devflow/functional/bolts/US-000.BOLT-014-…`, `devflow/bugs/BUG-004-…`, `devflow/metrics/bolts/US-000.BOLT-014-….json` | The governed artifacts of this Bolt — created and approved before the V-Bounce |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `devflow/avenga-devflow/Avenga-DevFlow.md` | §5.16 rule 1 replaced with the scaffolding carve-out + byte-level evidence verification (added ~17 lines); cross-reference sentence added to the "Everything else comes from the new version" paragraph (added ~4 lines) |
| `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md` | Identical edit, preserving kit/root parity |

## 5. Files renamed

None.

## 6. Files deleted

None.

---

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| Edit both copies symmetrically (root + distribution kit) | The kit is the product copy; BUG-004's scope (approved) lists both; parity is an invariant (ADR-004) — verified byte-identical before and after |
| Keep tree+count as the first verification, add byte-identity of evidence as the second | Cheap structural check stays valid; the added check closes exactly the gap BUG-004 evidenced, without invalidating the existing check wording |
| Add a cross-reference in the "Everything else" paragraph, not only the carve-out in rule 1 | Both normative statements must be aligned (ADR-005 phrase-family); a carve-out only in rule 1 would leave the other paragraph reading as an absolute for a reader landing there |
| Project-modified scaffolding file → whole file treated as evidence | Avoids a file-level merge problem; if the project touched it, it is project content (mirrors the AGENTS.md marker-merge principle in §5.16) |
| No edit to §5.6 (Raw inputs) | §5.6 defines the folders and the read-only/G31 property — consistent with the fix; editing it would widen the approved scope without need |
| `git_commit: null` in the manifest entry | The V-Bounce runs on the uncommitted migration working tree (baseline = HEAD c0decad + uncommitted install); there is no commit of this change yet (G34: no commit without explicit user request) |

---

## 8. Deviations and assumptions

- **G3 scope check adapted to the baseline reality.** The SPEC's G3 read
  "git diff HEAD … shows changed lines only inside §5.16". At execution
  time `git diff HEAD` on the root copy shows ~300 hunks — but they are the
  pre-existing, uncommitted 4.2→5.0 migration install (HEAD's `devflow/`
  is still 4.2, `devflow/VERSION` = "4.2"), not this V-Bounce. Scope
  containment was instead proven by: (a) the edit log (exactly 4 edits, all
  in §5.16 of the two copies), (b) `git status` (only the two methodology
  files modified by this V-Bounce, plus the four untracked governance
  artifacts), (c) parity and RED-baseline checks. No assumption was made
  about HEAD content; the deviation is recorded here, not hidden.
- **Line numbers shifted** after the edit (rule 1 now at ~4579/15 lines,
  cross-reference at ~4601→4611) — expected for a text edit; all greps use
  content, not line numbers.
- **Assumption:** the working tree remains as-is until the human commits
  (no commit was made — G34; the migration itself is still uncommitted and
  will be committed by the human after review).

---

## 9. Verification evidence

### Build

```
n/a — documentation-only Bolt; no buildable artifact exists.
```

### Tests

```
n/a — methodology text; verification is deterministic grep/diff commands (below).
```

### BUG V-Bounce evidence (RED → GREEN, strictly ordered)

- **RED (before any edit):**
  ```
  R1 — prescribed check: NEW count 9 / OLD count 9, Tree differences 0  → check PASSES (the gap)
  R2 — git diff --no-index devflowOLD/input devflow/input: 9 files changed, 11 insertions(+), 11 deletions(-)
  R3 — L4579 rule 1 "input/ in full — 100%, exactly as it stands.**"; L4597 "Everything else comes from the new version."; L4601 "distributable) are never copied forward."
  ```
- **GREEN (after the fix):**
  ```
  G1 — positive coverage: both copies 5/5 phrases present (scaffolding carve-out, byte-identical, byte-level diff, project modified, carve-out cross-ref)
  G2 — absence: 0 matches of old rule-1 heading; 0 bare "identical file count." in both copies
  G3 — scope: 4 edits, all §5.16 of the two copies (edit log + git status); pre-existing migration diff vs HEAD excluded (see §8)
  G4 — parity: both copies byte-identical (292,738 chars each) after the symmetric edit
  G5 — invariants: G-count in GUARDRAILS.md = 39; four agent definitions untouched; devflow/input/ untouched
  ```

### Gates

| Gate | Result |
|------|--------|
| Test-first evidence | `pass` — RED (R1–R3) recorded before any edit (G19) |
| Behavioral reproducibility | `pass` — all commands deterministic and re-runnable |
| Hallucination lint | `pass` — every §5.16 quote and line number in the SPEC matched the file at execution time |
| Bolt-manifest validation | `pass` — manifest parsed and checked against `manifest-v5-bolt.schema.json` at creation, approval and v_bounces update |
| Unit/integration, SAST/SBOM, perf-smoke, prompt-injection, secret-leak, IP/license, PII/DLP, dependency-confusion | `n/a` — documentation-only Bolt (reasons recorded in SPEC §9) |

---

## 10. Manual interventions

None — the agent produced everything (edits, verification, governance
artifacts). No human patch fallback was needed.

---

## 11. Evidence links

- **Diff / PR:** none — uncommitted working tree; the diff is the §5.16
  region of the two methodology copies (this MEM §4 documents it).
- **Commit:** none yet (baseline `c0decad` + uncommitted migration state).
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-000.BOLT-014-input-scaffolding-evidence-clarification.json`

---

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~25 min (artifact + V-Bounce, agent-generated) |
| V-Bounce number | 1 |
| Tests created | 0 (10 deterministic verification commands, 0 unit/integration — documentation Bolt) |
| AI-generated code | 100% |
| First-pass approval | pending (this review) |

---

## 13. Pending items and stubs

- [ ] Human review of this MEM (`AITL-MEM-Approval`) — pending.
- [ ] After approval: `AITL-BOLT-DONE-Approval` (work_category `refactor` → Tech Lead) — pending.
- [ ] The repository's 4.2→5.0 migration remains uncommitted (human decision, G34) — out of this Bolt's scope.

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
| **review_ready_at** | `2026-08-23T11:20:06-03:00` |
| **review.started_at** | `2026-08-23T11:20:45-03:00` |
| **review.decided_at** | `2026-08-23T11:21:00-03:00` |
| **Review evidence** | §5.16 diff of both copies (rule 1 + cross-reference), RED (R1–R3) and GREEN (G1–G5) outputs, gates table, manifest v_bounces[1] |
| **Comments** | — |
| **Findings** | none |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | Diff + RED/GREEN evidence + gates + manifest inspected (see frontmatter acknowledgment_reason) |
