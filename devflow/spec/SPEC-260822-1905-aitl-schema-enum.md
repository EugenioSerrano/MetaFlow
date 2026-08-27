---
id: "SPEC-260822-1905"
title: "v5 manifest schemas accept AITL-* checkpoints (keep HITL-* history) + SPEC/MEM conditionals for both prefixes"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
status: "approved"
origin: "US-021"
bolt: "US-021.BOLT-003"
revision: 1
associated_adrs:
  - "devflow/adrs/ADR-008-aitl-approval-precept.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
prerequisites: ["SPEC-260822-1546"]
risk_class: "medium"
autonomy_level: "L3"
turn_budget: ""
data_classification: "internal"
review_ready_at: "2026-08-22T19:05:14-03:00"
review: # HITL-SPEC-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "dev_validator"}]
  started_at: "2026-08-22T19:06:51-03:00"
  decided_at: "2026-08-22T19:06:51-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved. Additive enum widening (AITL-* accepted, HITL-* kept for history/G36) across the 3 v5 schemas + SPEC/MEM conditionals for both prefixes; explicit closed enum; proven by a worked example (GREEN AITL+HITL / RED malformed) + no-regression check. Kit-only. Authorizes the V-Bounce."
---

<!--
  LANGUAGE POLICY (§3.15): schema in English; prose content_language (en).
  Kit-only (ADR-004); root operating methodology stays v4.2. Dogfooding split:
  this SPEC's own checkpoints are HITL-*. This Bolt WIDENS the v5 schema enums to
  accept AITL-* (keep HITL-* history, G36); it does NOT rename identifiers in
  docs/examples (US-021.BOLT-004) or touch prose enum lists (BOLT-004).
-->

# SPEC-260822-1905 — v5 schema accepts AITL-* checkpoints (US-021.BOLT-003)

| Field | Value |
|-------|-------|
| **Origin** | [US-021](../functional/user-stories/US-021-hitl-to-aitl-evolution.md) (approved) |
| **Bolt** | [US-021.BOLT-003](../functional/bolts/US-021.BOLT-003-aitl-schema-enum.md) (approved) |
| **ADRs** | ADR-008 (§3.1 record vocabulary), ADR-004 (kit-only) |
| **Risk Class** | medium · **Autonomy** L3 · **Revision** 1 |

---

## 1. Objective

Widen the three `manifest-v5-*.schema.json` `checkpoint` enums (and the Bolt
schema's SPEC/MEM `subject` conditionals) so **new** approvals may be recorded with
`AITL-<CODE>-Approval`, **while migrated history keeps `HITL-*`** (G36). This is the
structural prerequisite for BOLT-004's identifier rename — the schema must accept
`AITL-*` before the identifiers are renamed, or BOLT-004's manifests would fail.

**Why:** BOLT-001 stated the precept, BOLT-002 made the guardrails enforce it; the
schema must now *accept* the AITL vocabulary. **If not done:** any manifest written
with an `AITL-*` checkpoint fails validation, blocking BOLT-004.

---

## 2. Context

Current v5 schemas (US-020.BOLT-001): the **Bolt** schema's `checkpoint` is an
`enum` of 7 `HITL-*` (lines ~485–491) with SPEC/MEM `subject` conditionals keyed on
`const: HITL-SPEC-Approval` (~538) / `const: HITL-MEM-Approval` (~556); the **US**
schema's `checkpoint` is `const: HITL-US-Approval` (~276); the **TC** schema's is
`const: HITL-TC-Approval` (~313). The `mode`/actor rule is checkpoint-name-independent.

---

## 3. Source inventory (pre-SPEC evidence gate)

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | `US-021.BOLT-003-aitl-schema-enum.md` | HITL-BOLT-READY-Approval ✓ |
| Parent US | `US-021-hitl-to-aitl-evolution.md` | HITL-US-Approval ✓ |
| ADRs | ADR-008 (§3.1), ADR-004 | accepted ✓ |
| Prior Bolts | US-020.BOLT-001 (v5 schemas), US-021.BOLT-002 (G05 canonical AITL) | **Done** ✓ |

Pre-SPEC evidence gate: **all governed sources approved.** No active-ADR conflict.

---

## 4. The schema change to apply (RED → GREEN)

1. **Bolt schema** (`manifest-v5-bolt.schema.json`):
   - `checkpointApproval.checkpoint.enum` — add the 7 `AITL-*` names
     (`AITL-US-Approval`, `AITL-BUG-Approval`, `AITL-TC-Approval`,
     `AITL-BOLT-READY-Approval`, `AITL-SPEC-Approval`, `AITL-MEM-Approval`,
     `AITL-BOLT-DONE-Approval`) alongside the 7 `HITL-*` (14 total).
   - The SPEC `subject`-requires-`revision` conditional: `if checkpoint const
     HITL-SPEC-Approval` → `if checkpoint enum [HITL-SPEC-Approval,
     AITL-SPEC-Approval]`.
   - The MEM `subject`-requires-`v_bounce` conditional: likewise
     `enum [HITL-MEM-Approval, AITL-MEM-Approval]`.
   - The `mode`/actor `allOf` is unchanged.
2. **US schema** (`manifest-v5-us.schema.json`): `checkpoint.const
   "HITL-US-Approval"` → `enum ["HITL-US-Approval", "AITL-US-Approval"]`.
3. **TC schema** (`manifest-v5-tc.schema.json`): `checkpoint.const
   "HITL-TC-Approval"` → `enum ["HITL-TC-Approval", "AITL-TC-Approval"]`.

All three keep `HITL-*` (G36 — migrated history validates).

---

## 5. Scope

### In scope (kit)
- `distribution-kit/devflow/metrics/manifest-v5-bolt.schema.json` (enum + SPEC/MEM conditionals)
- `distribution-kit/devflow/metrics/manifest-v5-us.schema.json` (const → enum)
- `distribution-kit/devflow/metrics/manifest-v5-tc.schema.json` (const → enum)

### Out of scope
- Renaming identifiers in docs/examples/templates or prose enum lists (BOLT-004);
  the `HITL` adjective (BOLT-004); guardrails (BOLT-002, Done); the precept
  (BOLT-001, Done); the `TEMPLATE-MANIFEST-*.json` example values (valid as `HITL-*`;
  BOLT-004 may rename); enabling virtual approvers / registry / roster / pilot
  (later USs); the root `devflow/` (ADR-004).

---

## 6. Phases

- **Phase A — the three schemas:** enum widening + Bolt SPEC/MEM conditionals. ~1h.
- **Phase B — Verification (GREEN):** the worked example (§8) + all existing
  manifests still validate + kit-only. ~1h.

---

## 7. Acceptance criteria

- **AC-1 (Bolt enum + conditionals):** the Bolt schema accepts all 7 `AITL-*` (and
  keeps the 7 `HITL-*`); the SPEC/MEM `subject` conditionals fire for **both**
  `HITL-` and `AITL-` `SPEC`/`MEM` forms.
- **AC-2 (US/TC enum):** the US schema accepts `HITL-US-Approval` **and**
  `AITL-US-Approval`; the TC schema accepts `HITL-TC-Approval` **and**
  `AITL-TC-Approval`.
- **AC-3 (history still valid):** a manifest with a **historical `HITL-*`** entry
  validates GREEN (G36 — no regression).
- **AC-4 (AITL accepted + enforced):** a manifest with an **`AITL-*`** entry
  validates GREEN, including `AITL-SPEC-Approval` with `subject.revision` and
  `AITL-MEM-Approval` with `subject.v_bounce`; a malformed `AITL-SPEC-Approval`
  **without** `subject.revision` is **rejected RED**.
- **AC-5 (no regression on real manifests):** every existing
  `devflow/metrics/**/*.json` in the repo (all currently `HITL-*`) still validates
  against its (root v4) schema — untouched — and the **kit** v5 schemas still
  validate the kit templates.
- **AC-6 (kit-only):** `git status` shows only `distribution-kit/` (the 3 schema
  files) + governance records; root untouched.
- **AC-7 (manifest):** the BOLT-003 manifest gets its `v_bounces[]` entry and validates.

---

## 8. Testing strategy

Deterministic (schema validation):
- **RED (before):** a manifest with an `AITL-*` checkpoint fails the v5 schema
  (enum has only `HITL-*`).
- **GREEN (after):** build a worked v5 Bolt manifest carrying **one `AITL-*` entry**
  (`AITL-SPEC-Approval` with `subject.revision`, `AITL-MEM-Approval` with
  `subject.v_bounce`) **and one historical `HITL-*` entry** → validates GREEN
  against the edited `manifest-v5-bolt.schema.json`; a fabricated variant
  (`AITL-SPEC-Approval` missing `subject.revision`, and an unknown
  `AITL-FOO-Approval`) is **rejected RED**. Also validate a v5 US manifest with
  `AITL-US-Approval` (GREEN) and a TC manifest with `AITL-TC-Approval` (GREEN).
  Reuse the `jsonschema` (draft 2020-12) harness. Record commands + results in the MEM.

---

## 9. Quality gates

Schema/internal → unit/integration (product), SAST/DAST/SBOM, perf, IP, PII,
dep-confusion, test-first: `n/a`. hallucination-lint, behavioral-reproducibility
(deterministic validation), bolt-manifest-validation: `pass`.

---

## 10. Security and data

The schema is a structural contract; widening the enum does not weaken approval
integrity (the `mode`/actor rule and the safe default live in the record + the
guardrails, unchanged). Data `internal`.

---

## 11. Migration, compatibility, rollback

**Backward compatible:** `HITL-*` stays accepted (G36), so every existing manifest
still validates; the change is purely additive (`AITL-*` newly accepted). Rollback:
revert the three schema files; root untouched.

---

## 12. Risk matrix

| Risk | Prob | Impact | Mitigation |
|------|------|--------|------------|
| Widening breaks HITL-* validation | 1 | 5 | AC-3/AC-5 validate a historical HITL-* entry + all existing manifests |
| AITL-SPEC/MEM conditional not wired | 2 | 4 | AC-1/AC-4 test AITL-SPEC without revision → RED |
| Over-reach (renaming identifiers/prose) | 2 | 2 | Scope §5 = 3 schema files only; BOLT-004 owns identifiers/prose |
| Unknown AITL-* code accepted | 1 | 3 | AC-4: `AITL-FOO-Approval` rejected (enum is explicit, not a pattern) |

---

## 13. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| Explicit `enum` of both prefixes (not a regex pattern) | Keeps the enum closed — only the known checkpoints, in either vocabulary; an unknown code is still rejected |
| Keep `HITL-*` in every enum | ADR-008 §3.1 / G36 — migrated history is never invalidated |
| SPEC/MEM `if` conditions widened to `enum [both]` | The `subject` shape (revision/v_bounce) is required regardless of vocabulary |
| Leave templates/prose on `HITL-*` | They are valid under the widened enum; renaming is BOLT-004's identifier sweep |

---

## 14. Stop conditions

- A historical `HITL-*` manifest fails to validate → regression; stop, fix.
- The `AITL-SPEC` without `subject.revision` validates → conditional not wired;
  stop, fix.
- Any root `devflow/` file or any file beyond the 3 schemas in the diff → stop,
  revert.
- A governed source changes materially (G15) → stop, revise, re-approve.

---

## 15. Definition of Done

- [ ] Phases A–B · AC-1..AC-7 pass
- [ ] GREEN (AITL-* accepted + SPEC/MEM conditionals; HITL-* history still valid; malformed rejected; kit-only)
- [ ] ADR-008 (§3.1) + ADR-004 (kit-only) followed
- [ ] MEM (with the worked-example GREEN/RED evidence) · manifest `v_bounces[]` appended
- [ ] HITL-MEM-Approval recorded

---

## 16. References

- US-021, US-021.BOLT-003 (approved); US-020.BOLT-001 (v5 schemas), US-021.BOLT-002 (Done)
- ADR-008 §3.1 (record vocabulary); the three `manifest-v5-*.schema.json`

---

## 17. HITL-SPEC-Approval

> Draft until the Dev-validator records `HITL-SPEC-Approval`. A material source
> change invalidates it — stop, revise, re-approve (G15).

| Field | Value |
|-------|-------|
| **review.reviewers** | eugenio.serrano (dev_validator) |
| **review.decision** | **approved** |
| **review_ready_at** | `2026-08-22T19:05:14-03:00` |
| **review.started_at** | `2026-08-22T19:06:51-03:00` |
| **review.decided_at** | `2026-08-22T19:06:51-03:00` |
