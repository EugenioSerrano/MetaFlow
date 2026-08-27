---
id: "MEM-260822-2242"
title: "Purge HITL-* from the v5 vocabulary — enum → AITL-* only + §5.16 migration rewrites names (ADR-010 §3.6–§3.7)"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
bolt: "US-000.BOLT-009"
spec: "SPEC-260822-2238"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "488f95d"
applied_adrs:
  - "devflow/adrs/ADR-010-actor-grammar-and-pure-v5-vocabulary.md"
  - "devflow/adrs/ADR-005-removal-completeness-phrase-family-sweep.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "US-000.BOLT-009-adr010-hitl-vocabulary-purge.json"
diff_ref: ""
review_ready_at: "2026-08-22T22:42:34-03:00"
review: # HITL-MEM-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers:
    - user: "eugenio.serrano"
      role: "dev_validator"
  started_at: "2026-08-22T22:44:01-03:00"
  decided_at: "2026-08-22T22:44:01-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved. V-Bounce GREEN: enum is AITL-*-only in all 3 v5 schemas (+ the two bolt allOf conditionals), §5.16 flipped to the name-rewrite rule in the methodology and the four agents (parity 39×5), 'preserved verbatim' gone, and the v4→v5 migration round-trip proves a HITL-MEM-Approval history converts to AITL-MEM-Approval and validates against the pure v5 schema with zero HITL-*. Closes the transient BOLT-008 left; ADR-010 fully implemented end to end."
---

<!--
  LANGUAGE POLICY (§3.15): schema in English; prose content_language (en).
  DOGFOODING SPLIT (ADR-004/006): v4.2 governance record (HITL-* own checkpoints,
  manifest schema_version 4.0) of a V-Bounce that edited the v5.0 PRODUCT
  (distribution-kit/). Baseline 488f95d + the BOLT-008 grammar sweep (working tree).

  ⚠️ MEM created before human review (§3.3 step 4). Pending HITL-MEM-Approval.
-->

# MEM-260822-2242 — HITL-* vocabulary purge (V-Bounce 1)

| Field | Value |
|-------|-------|
| **Bolt** | US-000.BOLT-009 (non-functional, US-000) |
| **SPEC** | SPEC-260822-2238 rev 1 (approved, HITL-SPEC-Approval 2026-08-22T22:39:42) |
| **V-Bounce** | 1 · `execution_outcome: ready_for_review` |
| **Governing** | ADR-010 §3.6–§3.7 (pure vocabulary), ADR-005 (sweep discipline), ADR-004 (kit-only) |
| **Prerequisite** | US-000.BOLT-008 (Done) — the grammar reshape of the same schemas |

---

## 1. Executive summary

This V-Bounce completed the ADR-010 axis by making the v5 record **vocabulary
pure**: the `checkpoint` enum of the three `manifest-v5-*.schema.json` now lists
**only the `AITL-*`** identifiers (the seven `HITL-*` values removed from the bolt
schema, the single `HITL-*` member removed from the us and tc enums, and the two
bolt-schema `allOf` conditionals narrowed to their `AITL-*` member), and the
§5.16 `4.0`→`5.0` conversion — in the methodology and, verbatim, in the four
agents — was flipped from "historical `HITL-*` names preserved verbatim" to the
**name-rewrite rule** (`HITL-<CODE>-Approval` → `AITL-<CODE>-Approval`; the
decision is immutable, only the vocabulary label tracks the version, AITL ⊇ HITL;
backward-compat lives in the frozen v4 schema). This resolves the deliberate
transient BOLT-008 left: text and schema flipped together. A **v4→v5 migration
round-trip** proves the design — a synthesized v4 manifest carrying
`HITL-MEM-Approval` converts to `AITL-MEM-Approval` (actor-shaped `decided_by`, no
`mode`), contains **zero** `HITL-*`, and validates against the **pure** v5 schema.
Result: **GREEN** — all SPEC §6 checks pass. With this Bolt the v5 kit records
identity in one actor grammar and one pure vocabulary end to end.

## 2. What was implemented and why

BOLT-008 swept the actor grammar but intentionally left the enum and the §5.16
name-preservation wording so each stage stayed internally consistent. ADR-010
§3.6–§3.7 requires the v5 schema to declare only the current vocabulary
(no monotonic enum growth) and the migration to adapt the *data*, not the schema.
This Bolt is that mechanical application, closing the axis pre-release so no
adopter ever migrates against a schema carrying legacy values.

## 3. Files changed (with reason)

- `metrics/manifest-v5-bolt.schema.json` — `$defs.checkpointApproval` enum: seven
  `HITL-*` values removed (seven `AITL-*` kept); the two `allOf` `if` conditionals
  (SPEC / MEM subject requirements) narrowed `["HITL-…","AITL-…"]` → `["AITL-…"]`.
- `metrics/manifest-v5-us.schema.json` — enum `["HITL-US-Approval","AITL-US-Approval"]`
  → `["AITL-US-Approval"]`.
- `metrics/manifest-v5-tc.schema.json` — enum → `["AITL-TC-Approval"]`.
- `avenga-devflow/Avenga-DevFlow.md` §5.16 — the "preserved verbatim / never
  rewritten to `AITL-*`" sentence replaced by the name-rewrite rule (decision
  immutable; enum `AITL-*`-only; v4 kept in the frozen v4 schema; G36 still forbids
  altering actor/timestamp/outcome/evidence or an approved MEM/ADR body).
- The four agents (`CLAUDE.md`, `.agents/…/SKILL.md`, `.github/…agent.md`,
  `.opencode/…md`) — the identical compact §5.16 clause flipped the same way
  (parity preserved).

## 4. Verification evidence (SPEC §6 — all GREEN)

| # | Check (over `distribution-kit/`) | Result |
|---|----------------------------------|--------|
| 1 | `HITL-` in the three v5 `checkpoint` enums (+ the two bolt `allOf` conditionals) | **0** |
| 2 | `"preserved verbatim"` in methodology + agents | **0** |
| 3 | schemas parse; 5 `TEMPLATE-MANIFEST-*.json` validate; enums are `AITL-*`-only | **all pass** |
| 4 | v4→v5 migration round-trip: `HITL-MEM-Approval` → `AITL-MEM-Approval`, no `mode`, actor `decided_by`, **0** `HITL-*`, validates against the **pure** v5 schema | **PASS** |
| 5 | four-agent shared-body parity + G-count | **2-line diff each** · **39/39 ×5** |
| 6 | `git status` scope | `distribution-kit/` (48 files) + root governance records; root methodology untouched (ADR-004) |

The one remaining `HITL-` token in the kit is the intentional rewrite-rule
explanation in §5.16 ("a historical `HITL-MEM-Approval` *is* an
`AITL-MEM-Approval` in human mode") — allowlisted, same class as the G05/G36
migration references (ADR-005 zone-scoped allowlist).

## 5. Decisions and deviations

- The two bolt-schema `allOf` conditionals (which key on the SPEC/MEM checkpoint)
  were narrowed to their `AITL-*` member — without this a v5 manifest naming the
  old checkpoint could still slip a `revision`/`v_bounce` requirement; consistent
  with "no v5 manifest carries a `HITL-*` name."
- The round-trip test is verification evidence (run in-session), not a shipped
  artifact — the kit ships only the pure v5 schemas; the v4 schema (with `HITL-*`)
  lives in an adopter's pre-migration tree.
- No enum values were left "just in case": backward compatibility is the frozen
  v4 schema's job, per ADR-010 §3.9 (one family, one pure schema).

## 6. Risks / follow-ups

- **None open on this axis.** ADR-010 is fully implemented: BOLT-008 (grammar) +
  BOLT-009 (vocabulary) both delivered. The v5 kit records identity in one actor
  grammar with a pure `AITL-*` vocabulary end to end.
- The next phase (DevFlow Agents build — registry US, roster, Coordinator, the
  initiative-governance ADR) is separate and future; it consumes this grammar.

## 7. Manual interventions

None. Fully agent-generated under L3; human steering via the approved SPEC + ADR.
Version-control actions deferred to the user (G34).

## 8. HITL-MEM-Approval

> V-Bounce complete and GREEN; not **approved** until the executing Dev-validator
> records `HITL-MEM-Approval` after inspecting the diff + §6 evidence + this MEM +
> the manifest entry (§3.3). Pending.

| Field | Value |
|-------|-------|
| **Reviewer** | eugenio.serrano (dev_validator, executing) |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-22T22:42:34-03:00` |
| **review.started_at** | `2026-08-22T22:44:01-03:00` |
| **review.decided_at** | `2026-08-22T22:44:01-03:00` |
