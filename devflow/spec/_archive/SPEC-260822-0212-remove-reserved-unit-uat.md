---
id: "SPEC-260822-0212"
title: "Remove the UNIT/UAT approval-and-release layer from the kit (Option B, full); deployment concept + DORA retained"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
status: "approved" # draft | approved | blocked | obsolete
origin: "US-015"
bolt: "US-015.BOLT-001" # ⚠️ MANDATORY
revision: 1 # re-scoped in place from the earlier Option-A draft (never approved) to Option B — still revision 1
associated_adrs:
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
prerequisites: []
risk_class: "medium"
autonomy_level: "L3"
turn_budget: ""
data_classification: "internal"
review_ready_at: "2026-08-22T02:15:58-03:00"
review: # HITL-SPEC-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "dev_validator"}]
  started_at: "2026-08-22T02:25:43-03:00"
  decided_at: "2026-08-22T02:25:43-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Reviewed the re-scoped Option-B revision against US-015, AREV-002 F-03/AREV-001 F-06 and ADR-004: full removal of the UNIT/UAT approval-and-release layer, with §2.11 Deployment Unit and DORA retained+reworded, tests/uat kept dormant, UAT-NNN id family kept valid, G20 renumber-free, and all checkpoint counts reconciled (10→8 core). Scope boundary is now coherent (removes the flow that Option A could not cleanly reserve). Approved — authorizes the V-Bounce that closes v4.2."
---

<!--
  LANGUAGE POLICY (§3.15): schema in English; prose in content_language (en).
  Kit-only edits (ADR-004); root untouched. OPTION B: full removal of the
  UNIT/UAT approval-and-release *governance layer*. The Deployment-Unit concept
  (§2.11) and DORA (§3.7.1) are RETAINED and reworded (deployment still exists
  and is measured; DevFlow just no longer prescribes UNIT/UAT approval gates).
-->

# SPEC-260822-0212 — Remove the UNIT/UAT approval-and-release layer (Option B, full)

| Field | Value |
|-------|-------|
| **Origin** | [US-015](../functional/user-stories/US-015-unit-governance.md) (approved) |
| **Bolt** | [US-015.BOLT-001](../functional/bolts/US-015.BOLT-001-remove-reserved-unit-uat.md) (approved) |
| **ADRs** | [ADR-004](../adrs/ADR-004-repository-partition-v2.md) (kit-only) |
| **Risk Class** | medium |
| **Revision** | 1 (re-scoped draft: Option A → Option B, pre-approval) |

---

## 1. Objective

Remove the entire **UNIT/UAT approval-and-release governance layer** from the
distributable: the `HITL-UNIT-Approval` and `HITL-UAT-Approval` checkpoints,
their promotion sequence, the UAT section, their review budgets, coverage and
status vocabulary. In v4.2 the governed flow ends at **Bolt acceptance**
(`HITL-BOLT-DONE-Approval`); grouping, release and customer acceptance are
left to the adopting team's own process until a **redesigned** model is
introduced in a future release (US-015 part b, v5.0).

The **Deployment-Unit concept (§2.11)** and **DORA (§3.7.1)** are **retained**:
deployment still exists and is measured; only the *prescribed UNIT/UAT approval
gates* are removed. Wording that named those gates as active is reworded to
"the team's own release process".

**Why full (Option B):** the maintainer will redesign Unit/UAT from scratch to
reflect real corporate environment/promotion complexity; a half-reserved layer
would keep contradicting the flow (AREV-002 F-03). Removing it cleanly is the
honest v4.2 state.

**If not implemented:** the reserved, non-operational UNIT/UAT layer stays
entangled in the flow, contradicting itself.

---

## 2. Context

US-015 (approved) part (a), Option B (maintainer decision, 2026-08-22). A grep
sweep found UNIT/UAT woven across ~25 methodology locations plus GUARDRAILS, the
four agents and several READMEs — it is a subsystem, not two rows. The earlier
Option-A draft (mark-reserved-in-place) proved internally inconsistent (§4.6–4.8
and §3.11 steps *are* the flow), so the maintainer chose full removal. Kit-only
(ADR-004); the root receives it at the next §5.16 migration.

---

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | `devflow/functional/bolts/US-015.BOLT-001-remove-reserved-unit-uat.md` | HITL-BOLT-READY-Approval ✓ |
| Parent US | `devflow/functional/user-stories/US-015-unit-governance.md` | HITL-US-Approval ✓ |
| Evidence | AREV-002 F-03, AREV-001 F-06 (approved Verdicts) | approved ✓ |
| ADR | `devflow/adrs/ADR-004-repository-partition-v2.md` | HITL-ADR-Approval ✓ |
| Repository baseline | branch `4.2`, HEAD `c30a739` | — |

Methodology locations (grep-verified, `Avenga-DevFlow.md`): §0 (77), §2.11
(966–975, **retain+reword**), §3.0 naming (1387) + checkpoint rows (1400–1401),
review budgets UAT column (1653/1661), coverage §3.7.3 (1708–1709), §3.7 gates
(2394), §3.11 E2E steps 14–15 (2763–2788), status vocab UAT (3406), language
policy mentions (3330/3352/3365 — `UAT-NNN` id stays valid as a doc family),
DORA (2482/3947, **retain+reword**), §4.6/4.7/4.8 (3827–3871), archive note
(4181), §5.15 routing (4367/4406/4424/4520). Plus `GUARDRAILS.md`, the four
agents, `devflow/README.md`, `ONBOARDING.md`, `tests/README.md`,
`analysis/README.md`, `tests/uat/{README,INDEX,TEMPLATE-UAT}`.

Pre-SPEC evidence gate: **all governed sources approved**.

---

## 4. Scope

### In scope — REMOVE (the approval-and-release layer)

- **§3.0:** the `HITL-UNIT-Approval` and `HITL-UAT-Approval` checkpoint rows;
  drop `UNIT`/`UAT` from the canonical-naming checkpoint-code list. The charter
  becomes **8 core + 5 conditional** — reconcile every count in prose
  ("10 core", "15 checkpoints", coverage).
- **§3.11:** remove E2E steps 14 (Unit Approval) and 15 (UAT); the governed
  flow ends at Bolt acceptance.
- **§4.6/4.7/4.8:** remove the UNIT/UAT **approval gates**. §4.7 (UAT) is
  removed; §4.6 (packaging) and §4.8 (promotion) are **reworded** to "the
  adopting team's own release/promotion process — DevFlow does not prescribe
  Unit/UAT approval checkpoints in this release" (keeps the Deployment-Unit /
  DORA linkage without the removed gates).
- **Review budgets:** remove the UAT column.
- **§3.7.3 coverage:** remove the Unit-level-checkpoint coverage note.
- **§3.15 status vocab:** remove the UAT status row.
- **§0 (77):** remove the `HITL-UNIT-Approval` mention.
- **GUARDRAILS:** remove the UNIT/UAT checkpoint-map rows; **G20** — reword to a
  reserved placeholder **keeping its number** (preserve the 39-rule invariant and
  every G-reference; do NOT renumber).
- **Four agents:** remove the HITL-table UNIT/UAT rows and the UAT/UNIT bullets
  (identical edits); reconcile any checkpoint counts.
- **README / ONBOARDING / tests/README / analysis/README:** remove UNIT/UAT
  checkpoint references (maps, role map, folder descriptions).

### Retain (reword only — do NOT delete)

- **§2.11 Deployment Unit** and **§3.7.1 DORA**: deployment stays a concept and
  is measured; reword sentences that named UNIT/UAT approval as active to "the
  team's release process".
- **The `UAT-NNN` document-id family** in the language/naming lists stays a
  valid id prefix (the artifact family isn't renamed), but no active checkpoint
  produces them in v4.2.
- **§5.15 routing:** keep the `tests/uat/` routing row so the dormant folder
  still migrates.

### tests/uat/ — kept DORMANT (not deleted)

`tests/uat/README.md`, `INDEX.md`, `TEMPLATE-UAT.md`: dormant/reserved banner
("the UNIT/UAT approval layer was removed in v4.2; a redesigned model is planned
— US-015 part b"); folder and template stay in place.

### Out of scope

- Redesigning Unit/UAT (US-015 part b, v5.0).
- Identity rules, other checkpoints, root `devflow/` tree (ADR-004).

---

## 5. Prerequisites and baseline

- US-015 approved; US-015.BOLT-001 approved (readiness).
- Four agents in sync before the edit; pre-existing drift → stop, reconcile.
- Baseline: branch `4.2`, HEAD `c30a739`.

---

## 6. Phases

### Phase A — Methodology, part 1: charter, flow, sections

**Duration:** ~1.5h — **Complexity:** High

Remove §3.0 rows + naming entries; remove §3.11 steps 14–15; remove §4.7 and
rework §4.6/§4.8; remove the UAT budget column, §3.7.3 Unit-coverage note, §3.15
UAT status row, §0 mention. Reconcile all checkpoint counts (10→8 core; "15
checkpoints"→13).

### Phase B — Methodology, part 2: retain-and-reword

**Duration:** ~0.5h — **Complexity:** Medium

Reword §2.11 (Deployment Unit) and §3.7.1 (DORA) so deployment stays coherent
without the removed approval gates; adjust the archive note (4181), §5.15
routing wording, and any dangling cross-reference to a removed section.

### Phase C — GUARDRAILS + four agents

**Duration:** ~1h — **Complexity:** Medium

Remove the GUARDRAILS checkpoint-map UNIT/UAT rows; reword **G20** to a reserved
placeholder keeping the number (39 preserved). Remove the four agents' HITL-table
UNIT/UAT rows and UAT/UNIT bullets (identical); reconcile counts. Verify G-count
39/39/39/39/39.

### Phase D — READMEs + tests/uat dormant

**Duration:** ~0.75h — **Complexity:** Low

Remove UNIT/UAT references in README/ONBOARDING/tests/analysis; add the dormant
banner to `tests/uat/`.

### Phase E — Verification (GREEN)

Grep (no active UNIT/UAT checkpoint; §2.11/DORA retained; counts reconciled;
`UAT-NNN` id still valid) + four-agent diff + G-count + folder-present + root
check (§8).

---

## 7. Acceptance criteria

### AC-1: the UNIT/UAT approval layer is gone
No `HITL-UNIT-Approval` / `HITL-UAT-Approval` **checkpoint** remains in §3.0,
§3.11, §4.x, GUARDRAILS map or the four agents; the governed flow ends at
`HITL-BOLT-DONE-Approval`.

### AC-2: deployment concept + DORA retained and coherent
§2.11 (Deployment Unit) and §3.7.1 (DORA) remain, reworded so no sentence
references a removed approval gate as active; no dangling cross-reference to a
removed section survives.

### AC-3: counts reconciled
The charter reads 8 core + 5 conditional; every "10 core"/"15 checkpoints"/
coverage count is updated; the GUARDRAILS G-count is **39** (G20 renumber-free).

### AC-4: tests/uat/ dormant, UAT-NNN id valid
`tests/uat/` present with the dormant banner (not deleted); `UAT-NNN` stays a
valid id prefix in the naming lists (no active checkpoint emits it).

### AC-5: four-agent sync + G-count
Whole-body diff = sanctioned divergence only; G-count 39/39/39/39; GUARDRAILS 39.

### AC-6: root untouched
`git status` shows only `distribution-kit/` + governance records.

### AC-7: Bolt-manifest validation
0 errors.

### AC mapping to source

| US-015 AC | How satisfied | Evidence |
|-----------|---------------|----------|
| Interim removal (Option B, full) | Phases A–D | AC-1, AC-3, AC-4 |
| Deployment stays coherent | Phase B | AC-2 |

---

## 8. Testing strategy

Deterministic, no runtime:
- Grep the active-flow locations for UNIT/UAT checkpoints → none (AC-1).
- Read §2.11/§3.7.1 → retained, no active-gate wording; grep for dangling
  `§4.7`/step-14/15 refs → none (AC-2).
- Grep counts ("10 core", "15", coverage) → reconciled; `grep -cE '^\| G[0-9]{2} '`
  = 39 (AC-3, AC-5).
- List `tests/uat/` → present + banner; grep `UAT-NNN` in naming lists → present (AC-4).
- Four-agent whole-body diff (AC-5); `git status` (AC-6); manifest validation (AC-7).
- Edge cases: G20 number preserved (reworded, not deleted); DORA "deployment =
  promotion of a Deployment Unit" reworded to not imply a removed gate;
  cross-references to §4.7/steps 14-15 elsewhere; CRLF/LF.

---

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | — | `n/a` — documentation-only |
| SAST / SBOM | — | `n/a` |
| Perf-smoke | — | `n/a` |
| Prompt-injection | — | `pass` |
| Secret-leak | — | `pass` |
| Hallucination lint | — | `pass` — every §-reference/path resolves post-edit |
| IP / license | — | `n/a` |
| PII / DLP | — | `n/a` — internal |
| Dependency-confusion | — | `n/a` |
| Test-first evidence | — | `n/a` — not a BUG Bolt |
| Behavioral reproducibility | — | `pass` — deterministic grep/diff |
| Bolt-manifest validation | — | `pass` |

---

## 10. Security and data

Governance-text only; no security boundary. Removing a reserved, non-operational
approval layer weakens no active control. Data `internal`.

---

## 11. Monitoring and observability

`n/a` — no runtime. The §8 suite is the observability; captured in the MEM.

---

## 12. Migration, compatibility and rollback

- **Migration:** none here; adopters receive it at the next §5.16 migration.
- **Compatibility:** DORA + Deployment Unit + the `UAT-NNN` id family stay, so
  metrics/validators don't break; the HITL charter drops to 8 core checkpoints;
  the G-count stays 39. Adopters lose the prescribed UNIT/UAT gates (they were
  reserved/non-operational anyway).
- **Rollback:** revert the kit commit(s); root untouched; `tests/uat/` not deleted.

---

## 13. Risk matrix

| Risk | Prob | Impact | Mitigation |
|------|------|--------|------------|
| Dangling reference to a removed section/step | 4 | 3 | §8 grep for `§4.7`/steps 14-15/removed rows; fix every cross-ref |
| Over-removal breaks DORA/Deployment Unit | 3 | 4 | §4 retains + rewords §2.11/§3.7.1; AC-2 verifies coherence |
| G-count breaks 39 (G20) | 3 | 3 | Keep G20's number, reword to reserved placeholder; AC-3/AC-5 |
| Count prose left stale ("10 core"/"15") | 3 | 2 | §8 reconcile; AC-3 |
| Four-agent drift | 2 | 3 | Identical edits; AC-5 |
| tests/uat deleted | 1 | 2 | Kept + banner; AC-4 |
| Root edited | 1 | 4 | Kit-only; AC-6 |
| Scope larger than one clean pass | 3 | 2 | If turn budget exhausts before GREEN → stop, MEM with progress, resume in a new V-Bounce (§15) |

---

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| Full removal of the approval layer (Option B) | Maintainer will redesign from scratch (v5.0); a half-reserved layer keeps contradicting the flow |
| Retain + reword §2.11 Deployment Unit and DORA | Deployment still exists and is measured; deleting them would break DORA and over-reach |
| Keep `UAT-NNN` id family valid | Avoids invalidating the artifact-id namespace; the dormant template still uses it |
| Keep G20's number, reword to reserved | Preserves the 39-rule invariant and all G-references without renumbering |
| tests/uat/ dormant, not deleted | US-015 part (b) rebuilds; avoids losing the template |
| Flow ends at Bolt acceptance | v4.2 governs to `HITL-BOLT-DONE-Approval`; release/UAT is the team's process until v5.0 |

---

## 15. Stop conditions

- Pre-existing four-agent drift before Phase C → stop, reconcile, record.
- Any root `devflow/` methodology file in the diff → stop, revert, record.
- Removing the layer would force deleting §2.11/DORA or renumbering the G-rules → stop, reassess.
- A dangling reference cannot be resolved without a new decision → stop, record, ask.
- Turn budget exhausted before GREEN → stop, MEM with progress + blocker, resume as a new V-Bounce.
- A governed source changes materially (G15) → stop, revise, re-approve.

---

## 16. Definition of Done (DoD)

- [ ] Phases A–E implemented
- [ ] AC-1..AC-7 pass
- [ ] Verification GREEN (no active UNIT/UAT; §2.11/DORA retained+coherent; counts reconciled; tests/uat dormant; UAT-NNN valid; sync 39×5; root untouched; manifest 0 errors)
- [ ] Follows ADR-004 (kit-only)
- [ ] Gates pass / n/a per §9
- [ ] MEM created (exactly one per V-Bounce)
- [ ] Manifest `v_bounces[]` entry appended
- [ ] HITL-MEM-Approval recorded

---

## 17. References

- US-015 (approved), US-015.BOLT-001 (approved), AREV-001 F-06, AREV-002 F-03
- ADR-004 (kit-only), AGENTS.md (four-agent sync + G-count invariant)
- §2.11 (Deployment Unit), §3.7.1 (DORA), §3.0 (charter/naming), §3.11 (E2E), §4.6–4.8, §5.15 (routing)

---

## 18. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-22 | eugenio.serrano | Initial draft (Option A — mark reserved in place) |
| 2026-08-22 | eugenio.serrano | Re-scoped draft to **Option B** (full removal of the approval-and-release layer; §2.11/DORA retained) before approval, after scope mapping showed Option A internally inconsistent |

---

## 19. HITL-SPEC-Approval

> **Avenga DevFlow §2.4.1, §3.0.** Draft until the Dev-validator records
> `HITL-SPEC-Approval`. Bolt approval authorizes SPEC preparation; **SPEC
> approval** authorizes the V-Bounce. A material source change invalidates
> this approval — stop, revise, re-approve (G15).

| Field | Value |
|-------|-------|
| **review.reviewers** | eugenio.serrano (dev_validator) |
| **review.decision** | approved |
| **review_ready_at** | `2026-08-22T02:15:58-03:00` |
| **review.started_at** | `2026-08-22T02:25:43-03:00` |
| **review.decided_at** | `2026-08-22T02:25:43-03:00` |
