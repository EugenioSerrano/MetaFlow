---
id: "SPEC-260822-1622"
title: "Document the v4.0→v5.0 manifest conversion in §5.16 (G36) + a validating worked example"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
status: "approved"
origin: "US-020"
bolt: "US-020.BOLT-003"
revision: 2
associated_adrs:
  - "devflow/adrs/ADR-008-aitl-approval-precept.md"
  - "devflow/adrs/ADR-006-versioning-and-self-development-model.md"
  - "devflow/adrs/ADR-005-removal-completeness-phrase-family-sweep.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
prerequisites: ["SPEC-260822-1546", "SPEC-260822-1607"]
risk_class: "medium"
autonomy_level: "L3"
turn_budget: ""
data_classification: "internal"
review_ready_at: "2026-08-22T16:44:16-03:00"
review: # HITL-SPEC-Approval (rev 2) — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "dev_validator"}]
  started_at: "2026-08-22T16:46:41-03:00"
  decided_at: "2026-08-22T16:46:41-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved rev 2: AC-3 narrowed to this Bolt's edited surface (§5.16 + the four agents' upgrade lines); the kit-wide v5-propagation sweep (A+B+C) is routed to US-020.BOLT-004. Edits unchanged from rev 1; the V-Bounce completes against rev 2 (no G16 span)."
---

<!--
  LANGUAGE POLICY (§3.15): schema in English; prose content_language (en).
  Kit-only (ADR-004); root untouched. This Bolt writes the CONVERSION RECIPE
  (the §5.16 section BOLT-002 deliberately preserved). It documents the rules;
  it does not convert this repo's manifests (that runs at the next §5.16).
-->

# SPEC-260822-1622 — v4.0→v5.0 manifest conversion in §5.16 (BOLT-003)

| Field | Value |
|-------|-------|
| **Origin** | [US-020](../functional/user-stories/US-020-manifest-aitl-evolution.md) (approved) |
| **Bolt** | [US-020.BOLT-003](../functional/bolts/US-020.BOLT-003-manifest-migration-path.md) (approved) |
| **ADRs** | ADR-008 (record shape), ADR-006 (version/migration), ADR-005 (sweep), ADR-004 (kit-only) |
| **Risk Class** | medium · **Autonomy** L3 |
| **Revision** | 1 · **Prereq:** SPEC-260822-1546 (BOLT-001) + SPEC-260822-1607 (BOLT-002), both Done |

---

## 1. Objective

Document, in the §5.16 Methodology Upgrade Protocol, **how a manifest converts
from `schema_version "4.0"` to `"5.0"`** when a project (or the root) upgrades to
v5.0 — the recipe BOLT-002 deliberately left untouched — under the G36
no-history-rewrite rule, and prove it with a **worked example that validates
against the v5 schema** (BOLT-001).

**Why:** without the recipe, an adopter running §5.16 to v5.0 has no correct way
to migrate their existing v4 manifests. **If not done:** US-020 is incomplete —
the v5 schema ships but the upgrade path to it is undocumented.

---

## 2. Context

BOLT-001 (Done) shipped the v5 schemas/templates; BOLT-002 (Done) aligned the
manifest **description** and preserved the §5.16 conversion section for this
Bolt. §5.16 currently documents the lossless rule with a `3.0`→`4.0` worked
example; BOLT-003 adds the `4.0`→`5.0` conversion. Kit-only (ADR-004).

---

## 3. Source inventory (pre-SPEC evidence gate)

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | `US-020.BOLT-003-manifest-migration-path.md` | HITL-BOLT-READY-Approval ✓ |
| Parent US | `US-020-manifest-aitl-evolution.md` | HITL-US-Approval ✓ |
| Prereq Bolts | BOLT-001 (v5 schemas) + BOLT-002 (v5 description) | **Done** ✓ |
| ADRs | ADR-008, ADR-006, ADR-005, ADR-004 | accepted ✓ |
| Baseline | branch `5.0`, HEAD `97125e7` (+ BOLT-001/002 kit changes in the working tree) | — |
| Current §5.16 | `Avenga-DevFlow.md` ~4600–4641 (lossless rule + `3.0`→`4.0` example + reconstruction table with `checkpoint_approvals[]`* row) · the four agents' "Methodology Upgrade Protocol" conversion lines (still carry `hitl_approvals` — this Bolt's targets) | — |

Pre-SPEC evidence gate: **all governed sources approved; BOLT-001 + BOLT-002 Done.**

---

## 4. The v4.0→v5.0 conversion rule (the content to document)

Under the §5.16 lossless rule (add new fields, apply renames, carry values,
never rewrite history — G36), the `4.0`→`5.0` conversion is:

1. **Rename** the approval array `hitl_approvals[]` → `checkpoint_approvals[]`.
2. **Per entry, add `mode`** = `"human"` (every recorded v4 approval was a human;
   agents did not exist in v4) — a derived value, not `null`.
3. **Per `decided_by[]` element, transform** `{user, role}` →
   `{actor: "human:<user>", role, model: null}` (the v4 `user` becomes a
   `human:`-prefixed actor; `model` is `null` for a human).
4. **Preserve the historical `HITL-*` checkpoint names** verbatim — they are
   recorded decisions and are **never** rewritten to `AITL-*` (G36). New v5.0
   approvals use `AITL-*` once the separate rename US ships; migrated history
   keeps `HITL-*`.
5. **Set `schema_version` to `"5.0"`.** All other fields (`bolt`/`us`/`tc`,
   `spec_revisions[]`, `v_bounces[]`, `generation`, timings, `story_points`,
   `verifies`, …) cross unchanged.
6. Anything that cannot be converted under this rule is **unresolved** —
   reported, never guessed (G36).

---

## 5. Scope

### In scope (kit)
- **`Avenga-DevFlow.md` §5.16:** add the `4.0`→`5.0` conversion (the §4 rule)
  alongside the existing `3.0`→`4.0` example; update the reconstruction table's
  `hitl_approvals[]` row (line ~4638) to `checkpoint_approvals[]` with the actor
  projection (`human:<user>`, `mode: human`).
- **The four agents' "Methodology Upgrade Protocol" conversion lines** (the
  preserved `hitl_approvals` references — CLAUDE.md ~603, and the peers):
  `hitl_approvals`→`checkpoint_approvals` **and** a one-line `4.0`→`5.0` note
  (rename + `mode:human` + actor + preserved `HITL-*`), identical across the four.

### Out of scope
- The v5 schemas/templates (BOLT-001, Done); the §3.12 structure description
  (BOLT-002, Done); the `HITL-*`→`AITL-*` rename (separate US); the root
  `devflow/` (ADR-004). This Bolt does **not** convert this repo's manifests
  (that runs when the root migrates to v5.0).
- **(rev 2) The kit-wide v5-propagation sweep** discovered during this Bolt's
  AC-3 check. BOLT-001/002 propagated the schemas and the core text but left the
  reference/template tier on v4: **(A)** `hitl_approvals`→`checkpoint_approvals`
  across `metrics/README.md`, the artifact templates (`TEMPLATE-BOLT/MEM/US/TC/REV.md`)
  and the folder READMEs; **(B)** reshaping the §3.12 embedded example +
  `metrics/README.md` approver prose to the v5 `{actor,role,model}`+`mode` shape
  so the example validates against the shipped schema; **(C)** fixing the broken
  `manifest-v4-*.schema.json` links (files BOLT-001 deleted) + "Schema family v4"
  labels + `schema_version "4.0"`. Routed to **US-020.BOLT-004** (A+B+C).

---

## 6. Phases

- **Phase A — §5.16** (Avenga-DevFlow.md): add the `4.0`→`5.0` rule + update the
  reconstruction table row. ~1h.
- **Phase B — the four agents' Upgrade Protocol** conversion lines (identical
  edits). ~0.5h.
- **Phase C — Verification (GREEN):** the worked example + grep + sync (§7).

---

## 7. Acceptance criteria

- **AC-1 (recipe documented):** §5.16 states the `4.0`→`5.0` conversion — the
  `hitl_approvals`→`checkpoint_approvals` rename, per-entry `mode: "human"`, the
  `decided_by` `{user,role}`→`{actor:"human:<user>",role,model:null}` transform,
  historical `HITL-*` names preserved (G36), `schema_version "5.0"`.
- **AC-2 (reconstruction table):** the §5.16 table row for the approval array
  reads `checkpoint_approvals[]` and notes the actor projection.
- **AC-3 (in-scope sweep, rev 2):** the four agents' Upgrade Protocol conversion
  lines carry `checkpoint_approvals` and the `4.0`→`5.0` note — byte-identical
  across the four; within **this Bolt's edited surface** (§5.16 of
  `Avenga-DevFlow.md` and the four agents' Upgrade-Protocol sections) no
  `hitl_approvals` remains **except** where it legitimately names the *v4 source*
  being converted. The **kit-wide** `hitl_approvals`→`checkpoint_approvals`
  sweep — plus the v5 approver reshape and the broken `manifest-v4` links across
  the manifest reference (`metrics/README.md`), the artifact templates and the
  folder READMEs — is **out of scope** here and routed to **US-020.BOLT-004**
  (rev-2 finding; see §5).
- **AC-4 (worked example validates):** a hand-built **v4 manifest** converted by
  the §4 rule yields a **v5 manifest that validates GREEN** against the v5 schema
  (BOLT-001); the converted entry shows `mode:human`, `actor:"human:<user>"`,
  `model:null`, and a preserved `HITL-*` checkpoint name.
- **AC-5 (history rule):** the recipe explicitly forbids rewriting `HITL-*`
  names to `AITL-*` (G36).
- **AC-6 (sync + kit-only):** four-agent sync + G-count 39×5; `git status` shows
  only `distribution-kit/` + governance records; root untouched.
- **AC-7 (manifest):** the BOLT-003 manifest gets its `v_bounces[]` entry and validates.

---

## 8. Testing strategy

Deterministic (documentation + one validation):
- **RED (before):** §5.16 has only the `3.0`→`4.0` example; the agents' upgrade
  lines still say `hitl_approvals` without a `4.0`→`5.0` note.
- **GREEN (after):** §5.16 + agents document `4.0`→`5.0`; a worked v4→v5 example
  (built in the V-Bounce, applying the §4 rule) validates GREEN against the v5
  schema and RED against a fabricated non-conforming variant; four-agent diff
  sanctioned-only; G-count unchanged; `git status` kit-only. Record in the MEM.

---

## 9. Quality gates

Documentation/internal → unit/integration, SAST/SBOM, perf, IP, PII,
dep-confusion, test-first: `n/a`. Prompt-injection, secret-leak,
hallucination-lint (refs resolve; the example validates against the real v5
schema), behavioral-reproducibility (deterministic), bolt-manifest-validation:
`pass`.

---

## 10. Security and data

Governance text only; no runtime boundary. Data `internal`.

---

## 11. Migration, compatibility, rollback

This Bolt **is** the migration documentation. Compatibility: the recipe is
additive to §5.16 (`3.0`→`4.0` stays as history; `4.0`→`5.0` added). Rollback:
revert the kit commit; root untouched.

---

## 12. Risk matrix

| Risk | Prob | Impact | Mitigation |
|------|------|--------|------------|
| The documented conversion doesn't actually validate | 2 | 4 | AC-4 builds the worked example and validates it against the real v5 schema |
| History-rewrite creeps in (HITL→AITL in the recipe) | 2 | 3 | AC-5 forbids it explicitly (G36); the example keeps HITL-* |
| Four-agent drift | 2 | 3 | Identical edits; AC-6 diff + G-count |
| Over-reach into BOLT-001/002 territory | 1 | 2 | Scope §5 limits to §5.16 + the agents' upgrade lines |

---

## 13. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| `mode: "human"` for converted v4 entries (derived, not null) | Every v4 approval was a human; the safe default is human — not "unknown" |
| `decided_by` `user`→`actor: "human:<user>"` + `model: null` | Matches the v5 approver shape (ADR-007/008) exactly; lossless |
| Historical `HITL-*` names preserved | G36 — recorded decisions are never rewritten; new v5 approvals use AITL-* after the rename US |
| Keep the `3.0`→`4.0` example, add `4.0`→`5.0` | §5.16 documents the general rule with per-major examples; both illustrate it |

---

## 14. Stop conditions

- The worked example fails to validate under the documented rule → the rule is
  wrong; stop, fix the rule, re-validate.
- Any root `devflow/` file in the diff → stop, revert, record.
- Turn budget (10) exhausted before GREEN → stop, MEM with progress, resume.
- A governed source changes materially (G15) → stop, revise, re-approve.

---

## 15. Definition of Done

- [ ] Phases A–C · AC-1..AC-7 pass
- [ ] GREEN (recipe documented; worked v4→v5 example validates; agents synced; kit-only)
- [ ] ADR-006 (migration) + ADR-005 (sweep) + ADR-004 (kit-only) followed
- [ ] MEM (worked-example evidence) · manifest `v_bounces[]` appended
- [ ] HITL-MEM-Approval recorded → then US-020 fully delivered

---

## 16. References

- US-020, US-020.BOLT-003 (approved); BOLT-001 + BOLT-002 (Done)
- ADR-004/005/006/008; §5.16 (Upgrade Protocol), §3.12 (Manifest Family)
- The v5 schemas (BOLT-001) the worked example validates against

---

## 17. HITL-SPEC-Approval

> Draft until the Dev-validator records `HITL-SPEC-Approval`. A material source
> change invalidates it — stop, revise, re-approve (G15).

**Revision 1** — approved 2026-08-22T16:26:29-03:00 (eugenio.serrano,
dev_validator). The V-Bounce (Phases A–C) executed under rev 1; AC-3's kit-wide
sweep surfaced the v5-propagation gap now routed to US-020.BOLT-004.

**Revision 2** — narrows AC-3 to this Bolt's edited surface and routes the
kit-wide sweep to BOLT-004 (§5, §7). The edits are unchanged; the V-Bounce
completes against rev 2 (no G16 span).

| Field | Value (rev 2) |
|-------|-------|
| **review.reviewers** | eugenio.serrano (dev_validator) |
| **review.decision** | **approved** |
| **review_ready_at** | `2026-08-22T16:44:16-03:00` |
| **review.started_at** | `2026-08-22T16:46:41-03:00` |
| **review.decided_at** | `2026-08-22T16:46:41-03:00` |
