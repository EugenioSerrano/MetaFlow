---
id: "SPEC-260822-2238"
title: "Purge HITL-* from the v5 vocabulary — checkpoint enum → AITL-* only + §5.16 migration rewrites names (ADR-010 §3.6–§3.7)"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
status: "approved" # draft | approved | blocked | obsolete
origin: "ADR-010"
bolt: "US-000.BOLT-009"
revision: 1
associated_adrs:
  - "devflow/adrs/ADR-010-actor-grammar-and-pure-v5-vocabulary.md"
  - "devflow/adrs/ADR-005-removal-completeness-phrase-family-sweep.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
prerequisites:
  - "US-000.BOLT-008 (Done) — reshaped the grammar defs of the same v5 schemas; this Bolt edits the enum they left untouched"
risk_class: "medium"
autonomy_level: "L3"
turn_budget: "10"
data_classification: "internal"
review_ready_at: "2026-08-22T22:38:07-03:00"
review: # HITL-SPEC-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers:
    - user: "eugenio.serrano"
      role: "dev_validator"
    - user: "eugenio.serrano"
      role: "tech_lead"
  started_at: "2026-08-22T22:39:42-03:00"
  decided_at: "2026-08-22T22:39:42-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved. Vocabulary purge (ADR-010 §3.6–§3.7): the checkpoint enum of the 3 v5 schemas → AITL-* only (incl. the two bolt-schema allOf conditionals), and §5.16 (methodology + 4 agents) flips from 'HITL preserved verbatim' to the name-rewrite rule. Verification = zone-scoped absence (0 HITL- in v5 enums, 0 'preserved verbatim') + 5-example validation + a v4→v5 migration round-trip proving converted history validates against the pure schema + four-agent parity. Closes the transient BOLT-008 left. V-Bounce authorized."
---

<!--
  LANGUAGE POLICY (§3.15): schema in English; prose content_language (en).
  DOGFOODING SPLIT (ADR-004/006): authored under v4.2 (own checkpoints HITL-*),
  edits the v5.0 PRODUCT (distribution-kit/). Baseline: 488f95d + the BOLT-008
  grammar sweep applied in the working tree (uncommitted).

  ⚠️ DRAFT until HITL-SPEC-Approval. No distribution-kit/ file is edited before
  that checkpoint is recorded (G14).
-->

# SPEC-260822-2238 — Purge HITL-* from the v5 vocabulary (ADR-010 §3.6–§3.7)

| Field | Value |
|-------|-------|
| **Origin** | [ADR-010](../adrs/ADR-010-actor-grammar-and-pure-v5-vocabulary.md) (accepted) §3.6–§3.7 |
| **Bolt** | [US-000.BOLT-009](../functional/bolts/US-000.BOLT-009-adr010-hitl-vocabulary-purge.md) (approved, HITL-BOLT-READY-Approval 2026-08-22T22:36:36-03:00) |
| **Prerequisite** | US-000.BOLT-008 **Done** — this Bolt edits the `checkpoint` enum BOLT-008 left untouched |
| **Risk / Autonomy / Revision / turn_budget** | medium · L3 · 1 · 10 |
| **Baseline** | `488f95d` + the BOLT-008 grammar sweep (working tree, uncommitted) |

---

## 1. Objective

Make the v5 record vocabulary pure per **ADR-010 §3.6–§3.7**: the `checkpoint`
enum of the three `manifest-v5-*.schema.json` lists **only the `AITL-*`
identifiers** (the `HITL-*` values are removed), and the §5.16 `4.0`→`5.0`
conversion **rewrites** each checkpoint name `HITL-<CODE>-Approval` →
`AITL-<CODE>-Approval` (the decision is immutable; only the vocabulary label
tracks the version; AITL ⊇ HITL). This resolves the deliberate transient left by
BOLT-008 (enum still accepting both, §5.16 still saying "preserved verbatim") —
text and schema flip together. Backward compatibility stays in the **frozen v4
schema**, which keeps `HITL-*` because it is v4. Mechanical application of an
accepted decision — no new judgment.

## 2. Context (why)

BOLT-008 swept the actor grammar but deliberately left the enum and the §5.16
name-preservation wording so text and schema stayed consistent at each stage
(BOLT-008 MEM §5). This Bolt is the other half: it flips both, closing the
user→actor + pure-vocabulary axis (ADR-010) end to end. Done pre-release so no
adopter ever migrates against a schema that carried legacy values (ADR-010 §1/§4).

## 3. Source inventory and approval evidence (pre-SPEC gate)

| Source | Approval | Role |
|--------|----------|------|
| ADR-010 §3.6–§3.7 | accepted 2026-08-22T21:54:53 | the target decision |
| US-000.BOLT-008 | Done 2026-08-22T22:35:24 | prerequisite (grammar reshape of the same schemas) |
| ADR-005 | accepted | phrase-family sweep discipline; absence proven by zone |
| ADR-004 | accepted | kit-only partition |
| US-000 | permanent container | Bolt parent |

Baseline: `488f95d` with the BOLT-008 working-tree changes applied. No governed
source is draft/stale (gate passes).

## 4. Scope

**In (`distribution-kit/` only):**
- the `checkpoint` enum in the three `manifest-v5-{bolt,us,tc}.schema.json`;
- the §5.16 `4.0`→`5.0` conversion text in `avenga-devflow/Avenga-DevFlow.md`
  (the "historical `HITL-*` names preserved verbatim" sentence → the name-rewrite
  rule);
- the four agents' compact §5.16 mention (the identical shared-body clause
  "historical `HITL-*` names preserved, never rewritten to `AITL-*`, G36" → the
  rewrite wording) — applied verbatim to all four (parity).

**Out:** the grammar defs (BOLT-008, Done — `created_by`/`runs[].agent`/`mode`/
`checkpointSubject`); the **v4** schemas (frozen, keep `HITL-*`); recorded v4.2
history in this maintainer repo (ADR-004/006); the root `devflow/` tree; the
`agents/` registry / roster / Coordinator (later USs).

## 5. The target change (the machine contract)

**Enum — all three `manifest-v5-*.schema.json` (`$defs.checkpointApproval.properties.checkpoint.enum`):**
- **`manifest-v5-bolt.schema.json`** — remove the seven `HITL-*` values
  (`HITL-US-Approval`, `HITL-BUG-Approval`, `HITL-TC-Approval`,
  `HITL-BOLT-READY-Approval`, `HITL-SPEC-Approval`, `HITL-MEM-Approval`,
  `HITL-BOLT-DONE-Approval`); keep the seven `AITL-*` values.
- **`manifest-v5-us.schema.json`** — the enum is `["HITL-US-Approval",
  "AITL-US-Approval"]` → `["AITL-US-Approval"]`.
- **`manifest-v5-tc.schema.json`** — `["HITL-TC-Approval", "AITL-TC-Approval"]`
  → `["AITL-TC-Approval"]`.
- The two `allOf` `if` conditionals in the bolt schema that key on the SPEC/MEM
  checkpoints already list both prefixes (`["HITL-SPEC-Approval",
  "AITL-SPEC-Approval"]`, `["HITL-MEM-Approval", "AITL-MEM-Approval"]`); drop the
  `HITL-*` member of each so they read `["AITL-SPEC-Approval"]` /
  `["AITL-MEM-Approval"]` (consistency — no v5 manifest carries the HITL name).

**§5.16 conversion text (methodology + the four agents):** the
"preserved verbatim / never rewritten to `AITL-*`" clause becomes the
name-rewrite rule: migration re-expresses `HITL-<CODE>-Approval` →
`AITL-<CODE>-Approval`; the **decision** (actor, timestamp, outcome) is
immutable, only the vocabulary label tracks the version (AITL ⊇ HITL — a
historical `HITL-MEM-Approval` *is* an `AITL-MEM-Approval` in human mode); G36
still forbids altering the recorded actor/timestamp/outcome/evidence or
rewriting an approved MEM/ADR body. Backward-compat lives in the frozen v4 schema.

## 6. Test / verification strategy (ADR-005 zone-scoped absence + a migration round-trip)

All over `distribution-kit/`:

1. `grep` for `HITL-` in the three v5 `checkpoint` enums (and the two bolt-schema
   `allOf` `if` conditionals) → **0**.
2. `grep -rn "preserved verbatim"` in the methodology + agents → **0**; the
   name-rewrite wording present instead.
3. **Schema validity:** all three reshaped schemas parse; the 5
   `TEMPLATE-MANIFEST-*.json` (already `AITL-*`) still validate.
4. **Migration round-trip (the ADR-010 §3.7 proof):** synthesize a `4.0` manifest
   carrying `HITL-MEM-Approval` + `{user, role}`; apply the §5.16 conversion
   (rename → `AITL-MEM-Approval`, reshape `decided_by`/`created_by`/`runs`);
   assert the result **validates against the pure v5 schema** and contains
   **zero** `HITL-*`.
5. **Four-agent parity:** shared-body byte-identity except the sanctioned
   `agents-data/<agent>` line; G-count 39×5.
6. `git status` shows only `distribution-kit/` + root governance records.

The MEM records the before/after enum values and the round-trip result.

## 7. Gates

- **bolt-manifest-validation:** the BOLT-009 manifest (root, v4) stays valid — `pass`.
- **unit/integration/SAST/DAST/perf, secret/PII/hallucination:** `n/a`/`pass` —
  documentation + schema only, no runtime, no secrets (§3.6).
- **test-first-evidence:** `n/a` — the §6 absence sweep + round-trip is the brake.

## 8. Risks, assumptions, stop conditions

- **Risk:** removing enum values breaks a manifest that used them → none in the
  kit (examples are `AITL-*`); the round-trip proves converted v4 history still
  validates post-rename.
- **Assumption:** BOLT-008's grammar reshape is in the working tree (it is —
  Done). If the schemas were reverted, stop.
- **Stop condition:** if any §6 check cannot reach 0 without touching an ADR-010
  §3.8 scope-guard zone (AREV model fields, v4 schema, root tree), stop, write the
  MEM with the blocker, pause at HITL-MEM-Approval.

## 9. HITL-SPEC-Approval

> DRAFT until Dev-validator + Tech Lead record `HITL-SPEC-Approval`. Approval
> authorizes the first code-run / V-Bounce; **no `distribution-kit/` file is
> edited before it (G14).**

| Field | Value |
|-------|-------|
| **Reviewers** | eugenio.serrano (dev_validator) + eugenio.serrano (tech_lead) |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-22T22:38:07-03:00` |
| **review.started_at** | `2026-08-22T22:39:42-03:00` |
| **review.decided_at** | `2026-08-22T22:39:42-03:00` |
