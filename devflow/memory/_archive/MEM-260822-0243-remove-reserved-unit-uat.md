---
id: "MEM-260822-0243"
title: "Remove the UNIT/UAT approval-and-release layer from the kit (Option B, full)"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
bolt: "US-015.BOLT-001"
spec: "SPEC-260822-0212"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "c30a739"
applied_adrs:
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "US-015.BOLT-001-remove-reserved-unit-uat.json"
diff_ref: "" # uncommitted at MEM time (kit-only working tree)
review_ready_at: "2026-08-22T02:43:48-03:00"
review: # HITL-MEM-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "dev_validator"}]
  started_at: "2026-08-22T02:49:28-03:00"
  decided_at: "2026-08-22T02:49:28-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Reviewed the 13-file kit diff + the §9 deterministic sweep: no active UNIT/UAT checkpoint in the flow, §2.11 Deployment Unit + DORA retained and coherent, four-agent sync with G-count 39×5 (GUARDRAILS 39), tests/uat/ dormant with UAT-NNN id family and the §3.15 UAT status row kept, root framework untouched, manifest validates. The two SPEC §4 refinements (G20 kept as live rule minus the UNIT/UAT sequence; §3.15 UAT row kept) are correct and coherence-preserving. Approved — Bolt Development Completed; this V-Bounce closes v4.2."
---

<!--
  LANGUAGE POLICY (§3.15): schema/headings in English; prose in content_language (en).
  Documentation-only V-Bounce (not a BUG) → no red/green; deterministic grep/diff evidence.
  Kit-only edits (ADR-004); root devflow/ framework files untouched.
-->

# MEM-260822-0243 — Remove the UNIT/UAT approval-and-release layer (Option B, full)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | [US-015.BOLT-001](../functional/bolts/US-015.BOLT-001-remove-reserved-unit-uat.md) |
| **SPEC**        | [SPEC-260822-0212](../spec/SPEC-260822-0212-remove-reserved-unit-uat.md) — revision 1 |
| **V-Bounce**    | 1 |
| **ADRs**        | [ADR-004](../adrs/ADR-004-repository-partition-v2.md) (kit-only) |

---

## 1. Executive summary

This V-Bounce removes the entire **UNIT/UAT approval-and-release governance
layer** from the distributable (`distribution-kit/`), the fix routed from
AREV-002 F-03 and the UNIT/UAT half of AREV-001 F-06: a reserved,
non-operational set of checkpoints (`HITL-UNIT-Approval`, `HITL-UAT-Approval`)
that was woven through the flow (§3.11 E2E steps, §4.6–4.8 promotion sequence,
the review-budget and coverage tables, the §3.0 charter and naming lists,
GUARDRAILS, and the four agents) while pointing at governance that does not
exist in v4.2 — a self-contradiction for any reader. With Option B (full
removal, the maintainer's decision) the governed flow now ends cleanly at Bolt
acceptance (`HITL-BOLT-DONE-Approval`); grouping, release and customer
acceptance are left to the adopting team's own process until a redesigned model
ships in a future release (US-015 part b, v5.0). The **Deployment-Unit concept
(§2.11)** and **DORA (§3.7.1)** are retained and reworded — deployment still
exists and is measured, only the prescribed approval gates are gone — and
`tests/uat/` plus the `UAT-NNN` id family are kept **dormant** (banner, not
deleted) so the future redesign inherits the template. Outcome: a
documentation-only change verified deterministically — no active UNIT/UAT
checkpoint survives anywhere in the active flow, the four agents stay byte-synced
with G-count 39/39/39/39 (GUARDRAILS 39), the root `devflow/` framework is
untouched, and the Bolt manifest validates. This is the V-Bounce that closes
v4.2.

---

## 2. Implemented phases

### Phase A — Methodology core, part 1: charter, flow, sections

Removed the UNIT/UAT **approval gates** from `Avenga-DevFlow.md`: the §3.0
checkpoint-table rows and the two entries in the canonical-naming checkpoint-code
list; the §0 `HITL-UNIT-Approval` mention; the §3.11 end-to-end steps that stated
the "staging UNIT → UAT → production UNIT" sequence (replaced with a note that the
governed flow ends at Bolt acceptance and release follows the team's process); the
review-budget table's Promotion/UAT columns and their prose; the §3.7.3 Unit-level
coverage note (reworded); and the §3.7 "Unit/Milestone gates" heading (→ "Release
level"). §4.7 (UAT) was replaced with "Release and customer acceptance (not
prescribed in this release)"; §4.6 (packaging) and §4.8 (promotion) were reworded
to point at the adopting team's own release/promotion process.

### Phase B — Methodology core, part 2: retain-and-reword

Kept §2.11 (Deployment Unit) and §3.7.1 (DORA) as concepts and reworded any
sentence that had named a UNIT/UAT approval as active, so deployment stays
coherent without the removed gates (the pipeline diagram edge became
"Build → Deployment Unit → Prod (team release process)"). Verified no dangling
cross-reference to §4.7 or to the removed §3.11 steps survives.

### Phase C — GUARDRAILS + four agents

`GUARDRAILS.md`: removed the checkpoint-map UNIT/UAT rows; dropped the
Promotion/UAT budget columns; reworded the coverage note and the
"Unit/Milestone level" → "Release level" gates heading. **G20** carried the
UNIT/UAT promotion sequence inside its explanation column — the embedded
"staging UNIT → UAT → production UNIT" text was stripped while the live rule
("Merge, promote, or accept a Bolt without the applicable approvals") and its
number were kept, so the 39-rule invariant and every G-reference are preserved.
The four agents (`CLAUDE.md`, `.agents/skills/avenga-devflow/SKILL.md`,
`.github/agents/AvengaDevFlow.agent.md`, `.opencode/agents/AvengaDevFlow.md`)
received the identical edits: HITL-table UNIT/UAT rows removed and budget-table
Promotion/UAT columns dropped, gates heading reworded.

### Phase D — READMEs + tests/uat dormant

Removed the UNIT/UAT active-checkpoint references from `devflow/README.md`
(flow diagram edge, govern/acceptance rows, checkpoint map, step 9, roadmap row,
folder-map line), `ONBOARDING.md` (Stakeholder sign-off + UAT glossary),
`tests/README.md` (folder-map node, table row, traceability bullet),
`analysis/README.md` (pipeline diagram node + folder-description table row).
Added a **DORMANT / RESERVED** banner to `tests/uat/README.md`, `INDEX.md` and
`TEMPLATE-UAT.md`, keeping the folder and template in place for US-015 part b.

### Phase E — Verification (GREEN)

Deterministic sweep across `distribution-kit/` (see §9): no active UNIT/UAT
checkpoint in the flow; §2.11 + DORA retained; four-agent sync + G-count 39×5;
`UAT-NNN` id family and §3.15 UAT status row kept; root framework untouched.

---

## 3. Files created

| File | Purpose |
|------|---------|
| `devflow/memory/MEM-260822-0243-remove-reserved-unit-uat.md` | This MEM — narrative record of the Option-B removal V-Bounce |

---

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md` | §0 mention; §2.11 + §3.7.1 DORA retained/reworded; §3.0 checkpoint rows + naming list; review-budget Promotion/UAT columns; §3.7.3 coverage; §3.7 gates heading; §3.11 E2E steps; §4.6/4.7/4.8; pipeline diagram edge. §3.15 UAT status row + §5.15 UAT-NNN routing row kept |
| `distribution-kit/devflow/GUARDRAILS.md` | Checkpoint-map UNIT/UAT rows removed; budget Promotion/UAT columns dropped; coverage + gates heading reworded; **G20** promotion-sequence text stripped (rule + number preserved, 39 intact); `UAT-NNN` naming entry kept |
| `distribution-kit/CLAUDE.md` | HITL-table UNIT/UAT rows removed; budget Promotion/UAT columns dropped; gates heading → "Release level" |
| `distribution-kit/.agents/skills/avenga-devflow/SKILL.md` | Identical to CLAUDE.md edits (four-agent sync) |
| `distribution-kit/.github/agents/AvengaDevFlow.agent.md` | Identical to CLAUDE.md edits (four-agent sync) |
| `distribution-kit/.opencode/agents/AvengaDevFlow.md` | Identical to CLAUDE.md edits (four-agent sync) |
| `distribution-kit/devflow/README.md` | Flow diagram edge, govern/acceptance rows, checkpoint map, step 9, roadmap row, folder-map line reworded/removed |
| `distribution-kit/devflow/ONBOARDING.md` | Stakeholder sign-off reworded; UAT glossary row → "removed in v4.2; team's own process (US-015)" |
| `distribution-kit/devflow/tests/README.md` | uat/ folder-map node + table row + traceability bullet marked dormant/reserved |
| `distribution-kit/devflow/analysis/README.md` | Pipeline diagram node + folder-description table row marked dormant |
| `distribution-kit/devflow/tests/uat/README.md` | DORMANT/RESERVED banner; "is active" line corrected to dormant |
| `distribution-kit/devflow/tests/uat/INDEX.md` | DORMANT/RESERVED banner |
| `distribution-kit/devflow/tests/uat/TEMPLATE-UAT.md` | DORMANT/RESERVED banner after the frontmatter |

> Governance-tracking records for this work also changed in the **root**
> `devflow/` (not kit): `functional/user-stories/US-015-unit-governance.md` +
> its manifest, `functional/INDEX.md`, `discovery/INDEX.md` +
> `discovery/DISC-001-...md`, and this Bolt's own doc/SPEC/manifest. These are
> DevFlow tracking artifacts, not methodology framework files — AC-6 explicitly
> allows them (see §8).

---

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
| —    | —        | —      |

---

## 6. Files deleted

| File | Reason |
|------|--------|
| —    | — (`tests/uat/` deliberately kept dormant, not deleted — AC-4) |

---

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| Full removal of the approval layer (Option B) | Maintainer will redesign Unit/UAT from scratch (v5.0) to reflect real corporate environment/promotion complexity; a half-reserved layer keeps contradicting the flow (AREV-002 F-03) |
| Retain + reword §2.11 Deployment Unit and §3.7.1 DORA | Deployment still exists and is measured; deleting them would break DORA and over-reach the fix |
| G20 kept as its live general rule (not turned into a "reserved placeholder") | G20's rule ("Merge, promote, or accept a Bolt without the applicable approvals") is still valid — only its explanation column had embedded the removed UNIT/UAT sequence. Stripping that text preserves the rule, its number and the 39-invariant. This refines the SPEC §4 wording ("reword to a reserved placeholder"), see §8 |
| Keep the §3.15 UAT status row | `tests/uat/` and `TEMPLATE-UAT.md` stay dormant and still declare `draft/approved/approved-with-observations/rejected`; removing the row would leave the dormant template using a status vocabulary absent from the normative §3.15 table (G39). Refines SPEC §4, see §8 |
| Keep the `UAT-NNN` id family + §5.15 routing row | Avoids invalidating the artifact-id namespace; the dormant folder still migrates (§5.16) |
| tests/uat/ dormant, not deleted | US-015 part (b) rebuilds on it; avoids losing the template |
| Flow ends at Bolt acceptance | v4.2 governs to `HITL-BOLT-DONE-Approval`; release/UAT is the team's own process until v5.0 |

---

## 8. Deviations and assumptions

Two refinements of the SPEC §4 literal wording, both toward greater coherence
(no material scope change — no re-approval required under G15):

- **(a) G20** — SPEC §4 said "reword G20 to a reserved placeholder keeping its
  number". On inspection, G20's *rule* is a live, still-valid general rule
  ("Merge, promote, or accept a Bolt without the applicable approvals"); only its
  *explanation column* had embedded the removed "staging UNIT → UAT → production
  UNIT" sequence. Correct action: keep G20 as the live rule and strip only the
  UNIT/UAT sequence text — not turn it into a placeholder. Number and the 39-rule
  invariant preserved either way. (This also resolves a mid-session confusion
  where G20 was briefly thought to be unrelated to UNIT/UAT — it did carry the
  sequence, in its explanation.)
- **(b) §3.15 UAT status row** — SPEC §4 listed it under "REMOVE". Kept instead:
  `tests/uat/` and `TEMPLATE-UAT.md` remain dormant and still use those status
  values, so removing the row would violate G39 (a status outside the normative
  §3.15 table). Keeping the row is coherent with the dormant-folder decision.

Assumption: **AC-3's count-phrase clause is non-applicable** — the methodology
never stated a numeric checkpoint count in prose ("10 core"/"15 checkpoints"
etc. do not exist literally; verified by grep, §9). Only AC-3's substantive
clause (G-count = 39) applied, and it holds.

No stop condition (§15 of the SPEC) was triggered; the turn budget was not
exhausted.

---

## 9. Verification evidence

Documentation-only V-Bounce (not a BUG) — evidence is deterministic grep/diff.

### AC-1 — no active UNIT/UAT checkpoint in the flow
```
grep 'HITL-UNIT-Approval|HITL-UAT-Approval|UNIT/UAT|Unit/Milestone sign-off|staging.*UNIT|production.*UNIT'
  → Avenga-DevFlow.md: No matches found
grep 'HITL-UNIT-Approval|HITL-UAT-Approval' (four agents) → none
```
Remaining `HITL-UAT-Approval` strings live only inside `tests/uat/`
(README/INDEX/TEMPLATE-UAT), all under the DORMANT/RESERVED banner — reserved
future process, not an active gate (AC-4).

### AC-2 — Deployment Unit + DORA retained and coherent
```
grep -c 'Deployment Unit' Avenga-DevFlow.md → 6
grep -c 'DORA'            Avenga-DevFlow.md → 28
```
No sentence references a removed approval gate as active; no dangling §4.7 /
step-14/15 cross-reference (AC-1 grep empty for the sequence phrases).

### AC-3 — counts reconciled / G-count 39
```
grep '10 core|15 checkpoint|ten core|fifteen checkpoint'  → none (never existed literally)
grep '[0-9]+ (core|named|conditional|hitl) checkpoint ...' → no numeric checkpoint-count claim anywhere
G-count (grep -cE '^\| G[0-9][0-9] '):
  CLAUDE.md 39 · SKILL.md 39 · AvengaDevFlow.agent.md 39 · AvengaDevFlow.md 39 · GUARDRAILS.md 39
```

### AC-4 — tests/uat/ dormant, UAT-NNN id valid
```
tests/uat/{README.md,INDEX.md,TEMPLATE-UAT.md} present, each with the DORMANT banner
grep -c 'UAT-NNN' GUARDRAILS.md → 1 (naming list) ; §5.15 routing row kept (Avenga-DevFlow.md:4373)
§3.15 UAT status row kept (Avenga-DevFlow.md:3384)
```

### AC-5 — four-agent sync + G-count
39/39/39/39 (agents) + GUARDRAILS 39; UNIT/UAT rows + Promotion/UAT budget
columns absent from all four (grep confirmed).

### AC-6 — root untouched
```
git status --short | (paths outside distribution-kit/ + governance records) → none
```
Root `devflow/` methodology framework files (Avenga-DevFlow.md, GUARDRAILS.md,
templates, READMEs) unchanged; only governance-tracking records changed there.

### AC-7 — Bolt-manifest validation
Manifest `v_bounces[0]` appended (all 8 required fields); JSON parses; schema
`additionalProperties:false` respected (see §11).

### Gates (per SPEC §9)
Unit/integration, SAST/SBOM, perf-smoke, IP/license, PII/DLP,
dependency-confusion, test-first: `n/a` (documentation-only / internal / not a
BUG Bolt). Prompt-injection, secret-leak, hallucination-lint (every
§-reference/path resolves post-edit), behavioral-reproducibility (deterministic
grep/diff), bolt-manifest-validation: `pass`.

---

## 10. Manual interventions

The 02-DEFENSE phase of AREV-002 was run by the maintainer with an external
model — not part of this V-Bounce. Within this V-Bounce, all edits were
agent-generated; no human code patch. None.

---

## 11. Evidence links

- **Diff / PR:** uncommitted working tree at MEM time (kit-only + governance records)
- **Commit:** baseline `c30a739` (frontmatter `baseline`); this V-Bounce's commit pending user request
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-015.BOLT-001-remove-reserved-unit-uat.json`

---

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~4h (spanned scope re-mapping A→B) |
| V-Bounce number | 1 |
| Tests created | 0 (documentation-only; deterministic grep/diff evidence) |
| AI-generated code | 100% (no human fallback in this V-Bounce) |
| First-pass approval | pending |

---

## 13. Pending items and stubs

- [ ] **US-015 part (b)** — full operationalization / redesign of Unit + UAT
  release governance (real-world environment/promotion complexity), planned for
  v5.0. `tests/uat/` and `TEMPLATE-UAT.md` are the dormant seed.
- [ ] Root `devflow/` receives this change at the next §5.16 migration (ADR-004).

---

## 14. HITL-MEM-Approval

> **Avenga DevFlow §2.12, §3.0.** This MEM is created by the agent with no
> mutable status and is **never self-approved**. The Dev-validator who executed
> the Bolt inspects the actual diff, verification evidence, MEM and manifest, and
> records `HITL-MEM-Approval` here and in the manifest's `hitl_approvals[]`.
> `approved` completes the V-Bounce (and marks the Bolt `Development Completed`);
> `changes_requested` keeps this MEM as immutable history and the next execution
> is a NEW V-Bounce with a NEW MEM. `HITL-BOLT-DONE-Approval` is still required
> for `Done`.

| Field | Value |
|-------|-------|
| **Reviewers (executing Dev-validator)** | eugenio.serrano |
| **Roles** | dev_validator (risk medium → 1 approver, §3.3) |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-22T02:43:48-03:00` |
| **review.started_at** | `2026-08-22T02:49:28-03:00` |
| **review.decided_at** | `2026-08-22T02:49:28-03:00` |
| **Review evidence** | diff (13 kit files) + §9 grep/diff sweep + manifest |
| **Comments** | Two SPEC §4 refinements (G20 live rule minus UNIT/UAT sequence; §3.15 UAT row kept) verified coherence-preserving |
| **Findings** | none |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | See frontmatter `review.acknowledgment_reason` |
