---
id: "ADR-010"
title: "The actor record grammar + a pure v5 vocabulary: one identity grammar everywhere, no HITL-* in any v5 record; migration rewrites names, the schema never carries legacy values (supersedes ADR-009)"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
status: "accepted"
decision_makers: ["architect", "tech_lead"]
sources:
  - "devflow/adrs/ADR-009-actor-identity-record-grammar.md"
  - "devflow/adrs/ADR-008-aitl-approval-precept.md"
  - "devflow/reviews/REV-003-user-to-actor-identity-vocabulary.md"
  - "devflow/discovery/DISC-002-devflow-agents-architecture.md"
supersedes: ["ADR-009"]
conflicts_with: []
tags: ["aitl", "actor", "identity", "manifest", "vocabulary", "migration", "v5.0"]
nfrs: ["identity-attribution", "schema-purity"]
waiver:
  gate: ""
  reason: ""
  owner: ""
  compensating_control: ""
  expires_at: ""
review_ready_at: "2026-08-22T21:38:53-03:00"
review: # HITL-ADR-Approval evidence — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers:
    - user: "eugenio.serrano"
      role: "architect"
  started_at: "2026-08-22T21:54:53-03:00"
  decided_at: "2026-08-22T21:54:53-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Accepted, superseding ADR-009. Restates the actor record grammar verbatim in intent (§3.1–§3.5, nothing lost) and adopts the pure-v5-vocabulary rule: the checkpoint enum is AITL-* only, migration rewrites HITL-*→AITL-* names, backward-compat lives in the frozen v4 schema. The §3.7 G36 reinterpretation confirmed consciously: G36 protects the decision (actor/timestamp/outcome/mode), not the vocabulary label; re-expressing the name in a governed human-reviewed migration is version-tracking, not falsification, and AITL ⊇ HITL makes the label truer. Principle §3.9 (one family, one pure schema) generalizes to all future majors. ADR-008 stays accepted — its §3.9 delegated this record decision. Immutable from now on. Implemented by BOLT-008 (grammar, re-pointed here) + BOLT-009 (purge)."
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs and section headings
  stay in English (the schema); prose follows content_language (en).
  HITL-ADR-Approval is never translated.

  ⚠️ DRAFT until an Architect / Tech Lead records HITL-ADR-Approval. A draft ADR
  cannot govern, and cannot supersede ADR-009: ADR-009 stays `accepted` until
  THIS ADR is accepted, at which moment ADR-009 flips to `superseded` (§3.5).

  ⚠️ Decided/operated under the v4.2 methodology (root devflow/, ADR-006), so this
  ADR's own checkpoint is HITL-ADR-Approval. It designs the v5.0 PRODUCT.
-->

# ADR-010 — Actor record grammar + a pure v5 vocabulary

| Field          | Value |
|----------------|-------|
| **Status**     | **accepted** (immutable — a new decision requires a superseding ADR) |
| **Decision-makers** | Architect / Tech Lead (maintainer) |
| **Sources**    | ADR-009 (superseded by this — its grammar is restated here), ADR-008 (precept; §3.9 delegated the record decision), REV-003 (approved inventory), DISC-002 (approved) |
| **Supersedes** | **ADR-009** (whole) — see §5 |
| **Conflicts with** | None — supersedes ADR-009; refines the record clause ADR-008 §3.9 delegated (§5) |

---

## 1. Context

ADR-009 (accepted ~1h before this) supplied the actor record grammar ADR-007
deferred. In doing so it also **carried forward the v4-era decision to preserve
`HITL-*` checkpoint names in migrated manifests** (its §3.7 "recorded values cross
untouched, history never rewritten", echoing ADR-008 §3.1 and §5.16). Review of
that choice found it is the wrong long-term design:

- A schema that must accept the previous vocabulary grows **monotonically**: v5
  accepts v4, v6 accepts v5+v4, and so on — the `checkpoint` enum is never pure,
  and "one family per repository" (§3.12) is contradicted at the value level even
  when it holds at the `schema_version` level.
- The backward-compatibility it was trying to serve **belongs in the old schema,
  not the new one**: a v4 manifest validates against the v4 schema (which has
  `HITL-*` because it *is* v4); the migration's job is to **convert the data** to
  v5, not to make the v5 schema tolerate v4 values.

ADR-008 **§3.9 explicitly delegated the manifest record decision to "the manifest
ADR."** That authority is exercised here. ADR-008's precept (human-by-default,
AITL everywhere) is unchanged and correct; only the record-vocabulary mechanics
move.

Nothing has been implemented from ADR-009 (its Bolt's SPEC is still draft), so
restating its grammar with the correction is cheap and lossless.

---

## 2. Alternatives considered

### Alternative A — Pure v5 vocabulary; migration rewrites; grammar restated here (✅ Selected)

| Aspect | Detail |
|--------|--------|
| **Pros** | The v5 schema is pure (`AITL-*` only); no monotonic enum growth ever. "One family, one clean schema" is true at the value level too. Backward-compat sits where it belongs — the frozen v4 schema. G36's intent is preserved precisely (the decision is immutable; only the vocabulary label tracks the version). Consistent with ADR-008's own "AITL ⊇ HITL" framing. |
| **Cons** | Reverses a just-accepted ADR (ADR-009) and refines the record clause ADR-008 delegated — needs this superseding ADR (which is exactly the governed mechanism). The migration does one more transformation (rewrite the checkpoint-name field). |

### Alternative B — Keep ADR-009 as-is (enum accepts both; migration preserves HITL-* names)

| Aspect | Detail |
|--------|--------|
| **Pros** | No supersede; G36 read at its most literal (the name string is part of the immutable record). |
| **Cons** | Monotonic enum growth forever; the new schema carries dead legacy values; "one family" holds only at `schema_version`. Rejected — this is the design being corrected. |

### Alternative C — Narrowly amend only ADR-009 §3.7/§3.8

| Aspect | Detail |
|--------|--------|
| **Pros** | Smaller document. |
| **Cons** | Leaves two active ADRs contradicting on the same point (§3.5/§2.4.1 forbid it); the methodology resolves a reversal by a **superseding** ADR, and supersede is whole-ADR. Rejected on the governance model, not the content. |

---

## 3. Decision

**We adopt Alternative A.** ADR-010 restates ADR-009's grammar (§3.1–§3.5 below,
carried forward verbatim in intent) and adds the pure-vocabulary rule (§3.6–§3.8).

### 3.1 The identity grammar (from ADR-009 — unchanged)

Every recorded identity uses one of two namespaces:
- **`human:<user>`** — the local part of the person's `git config user.email`
  (§3.0; git config remains the *source* of the human namespace, never a field name);
- **`agent:<id>`** — the DevFlow Agent's stable kebab-case identity (ADR-007 §3.1),
  resolved against the agent definition / roster.

### 3.2 Two strictness tiers + normalization (from ADR-009 — unchanged)

- **Machine records and review/enforcement fields — prefix-mandatory**
  (`^(human|agent):.+`): `metrics/**/*.json` (`created_by`, `decided_by[].actor`)
  and the artifact-side review contract (`review.reviewers[].actor`,
  `acceptance_review.reviewers[].actor`, `risk_history[].decided_by[].actor`).
- **Descriptive frontmatter person fields — bare = human shorthand:** `author:`,
  `owner:`, `validator:`, `closed_by:`, `facilitator:` accept a bare `<user>`
  meaning `human:<user>`; an agent is **always** `agent:<id>` (never bare), so a
  bare value is never ambiguous.
- **Normalization:** wherever identities are compared or projected, a bare value
  compares equal to its `human:`-prefixed form (G18/G24/G29/T02/handoff work verbatim
  as actor comparisons).

### 3.3 The review contract records actors (from ADR-009 — unchanged)

`reviewers: [{user, role}]` → **`reviewers: [{actor, role, model}]`** (the
`checkpoint_approvals[].decided_by[]` shape; `model` `null` for a human, the model id
for an agent). Applies to `review:`, `acceptance_review:` and
`risk_history[].decided_by`. The §3.0/GUARDRAILS projection becomes a **copy**; its
mismatch rule becomes a real integrity control.

### 3.4 The generation record attributes actors — including which agent (from ADR-009 — unchanged)

- `generation.created_by` records the **actor** (prefix-mandatory; human by default);
  §3.12's "identifies the human" → "the actor (a human by default)".
- `runs[]` gains **`agent`** — required, nullable: `null` when not agent-executed, the
  agent `id` when it was. `tool`/`provider`/`model` unchanged.

### 3.5 `mode` is dropped from `checkpoint_approvals[]` (from ADR-009 — unchanged)

`mode` is derivable (`virtual` iff any `decided_by[].actor` is `agent:`); a stored
derived state violates §3.12/G39. The actor prefixes are the single source of truth.

### 3.6 The v5 vocabulary is pure — no `HITL-*` in any v5 record (NEW)

The `checkpoint` enum of all three `manifest-v5-*.schema.json` contains **only the
`AITL-*` identifiers**. The `HITL-*` values are removed. A v5 manifest never carries a
`HITL-*` checkpoint name. Backward compatibility for a v4 manifest lives in the **v4
schema** (which retains `HITL-*` because it is v4 and frozen), never in the v5 schema.
Also renamed for hygiene: `$defs.hitlSubject` → `$defs.checkpointSubject` (bolt schema).

### 3.7 Migration rewrites the vocabulary; the decision is immutable, the label tracks the version (NEW — reverses ADR-009 §3.7)

The §5.16 `4.0`→`5.0` conversion **rewrites** each checkpoint name to the current
vocabulary: `HITL-<CODE>-Approval` → `AITL-<CODE>-Approval`. This is **not** rewriting
history in the sense G36 forbids:

- **G36 protects the *decision*** — who approved, when, the outcome, and (now) the
  `mode`/actor. Every one of those crosses the migration untouched.
- **The checkpoint *name* is a vocabulary label, not the decision.** Re-expressing it
  in the current vocabulary during a **governed, human-reviewed** migration (§5.16) is
  a version-tracking transformation, not a falsification — and because **AITL is a
  strict superset of HITL** (ADR-008: HITL is the default case, actor = human), a
  historical `HITL-MEM-Approval` **is** an `AITL-MEM-Approval` in human mode. The label
  becomes truer, not falser.
- What G36 still forbids absolutely: altering the recorded actor, timestamp, outcome or
  evidence; inventing an approval; or rewriting an **approved MEM/ADR body**. None of
  that changes.

Consequence for **G05**: `HITL-*` is not merely "invalid for new approvals" — it is
**absent from v5 records entirely** (the migration leaves none behind). `HITL-*` survives
only inside a **v4.x repository** (frozen, pre-migration) and in this maintainer repo's
own v4.2 governance while it dogfoods (ADR-004/006) — never inside a migrated v5 record.

### 3.8 Scope guards (from ADR-009 §3.8 — carried, minus the reversed one)

Unchanged out-of-scope: AREV phase model fields
(`challenger_model`/`defender_model`/`judge_model`, G37, model-based by design);
`git config user.email` as the source of the human namespace; role/domain fields
(`role`, `decision_makers`, `participants`, `stakeholders`, `real_name`); approved
MEM/ADR bodies (G36). **Removed guard:** ADR-009 §3.8's "the enum keeps `HITL-*` (G36
history support)" — reversed by §3.6/§3.7 above.

### 3.9 Principle stated (NEW)

**One family, one pure schema.** A repository holds exactly one manifest family
(§3.12), and its schema declares **only the current vocabulary**. Migration adapts the
**data** to the new schema; it never makes the new schema tolerate old values. This is
the general rule for every future major bump, not a v4→v5 special case.

### 3.10 Decided elsewhere (from ADR-009)

- *Who may occupy an approval* → ADR-008 + the per-project AITL-enable ADR.
- *Who may initiate/execute* (agent initiative governance) → a forthcoming ADR.
- *The `agents/` registry, roster schema, wrapper syntax* → the registry US.
- *The kit's dangling maintainer-ADR citations* (REV-003 F-08) → a correction routed
  with the sweep Bolts, not a decision.

---

## 4. Consequences

**Positive:**
- The v5 schema is pure and stays pure across future majors — no monotonic enum growth.
- A virtual approval is recordable on the artifact (unblocks ADR-008's granted
  capability); a generation is attributable to the exact agent.
- G36's intent is expressed more precisely than before (decision immutable; label
  version-tracked), resolving the tension ADR-009 left.
- Backward-compat is located correctly (the frozen old schema), so the mental model
  "one repository = one vocabulary" is finally true end to end.

**Trade-offs:**
- Reverses a just-accepted ADR (ADR-009) — done through the governed supersede path.
- The migration does one extra transformation (rewrite the checkpoint-name field);
  it must be covered by the §5.16 rewrite and tested (a migrated manifest validates
  against the **pure** v5 schema with **zero** `HITL-*`).

**Technical debt / follow-up (the two Bolts, maintainer's structure):**
- **US-000.BOLT-008** (re-pointed from ADR-009 to this ADR): the user→actor grammar
  sweep (§3.1–§3.5) — schemas' `created_by`/`runs[].agent`/drop-`mode`/rename, the 5
  examples, §3.0/§3.3/§3.12, GUARDRAILS, the 16 review blocks, the ~35 frontmatter
  comments, the four agents, and REV-003 F-08.
- **US-000.BOLT-009** (new): the pure-vocabulary purge (§3.6–§3.9) — the `checkpoint`
  enum → `AITL-*` only in the 3 schemas, and the §5.16 conversion rewritten to
  rewrite names. Sequenced **after** BOLT-008 (both touch the v5 schemas; no
  concurrent executors, G11/§3.2).

---

## 5. Supersede and the ADR-008 relationship

- **ADR-009 → superseded by ADR-010** (whole-ADR, §3.5). ADR-009's substantive content
  is not edited; its `status` flips `accepted` → `superseded` with a `superseded_by:
  ADR-010` pointer, recorded **only when this ADR is accepted**. Its user→actor grammar
  is carried forward here (§3.1–§3.5) so nothing is lost; only the vocabulary/migration
  clauses (its §3.7/§3.8) are reversed (§3.6/§3.7 here).
- **ADR-008 stays `accepted`.** Its precept is unchanged and correct. ADR-008 **§3.9
  delegated the manifest-record decision to the manifest ADR** — the authority ADR-010
  now exercises — so there is no contradiction to resolve at the ADR-008 level. ADR-008
  §3.1's mention of "preserving HITL-* names / HITL-* as a legacy prefix" is refined by
  this ADR on the delegated point: the **concept** of HITL as the human-default case of
  AITL survives (pedagogical, historical), while **v5 records carry no `HITL-*` values**.

---

## 6. Applicable NFRs

| NFR | Description | Threshold | How it is measured |
|-----|-------------|-----------|-------------------|
| `identity-attribution` | Every recorded generation and approval resolves to one actor id in the canonical grammar | Zero non-prefixed identities in machine records; zero agent-executed runs without `runs[].agent` | Schema `^(human\|agent):.+` patterns + the sweep Bolt's ADR-005 absence checks |
| `schema-purity` | A v5 schema declares only the current (`AITL-*`) vocabulary; a migrated v5 manifest carries no `HITL-*` | Zero `HITL-*` in the v5 `checkpoint` enums; zero `HITL-*` in any migrated v5 manifest; a v4 manifest validates only against the v4 schema | Schema inspection + a migration round-trip test (v4 in → pure-v5 out, validates) |

---

## 7. References

- [ADR-009](ADR-009-actor-identity-record-grammar.md) — superseded by this ADR; its
  grammar is restated in §3.1–§3.5.
- [ADR-008](ADR-008-aitl-approval-precept.md) — the precept (unchanged); §3.9 delegated
  the record decision exercised here.
- [ADR-007](ADR-007-devflow-agent-identity-model.md) — the actor as the unit of identity.
- [REV-003](../reviews/REV-003-user-to-actor-identity-vocabulary.md) (approved) — the
  site inventory (F-01…F-05, F-08).
- [DISC-002](../discovery/DISC-002-devflow-agents-architecture.md) (approved) — the
  roster/agent fields this grammar is looked up against.

---

## 8. HITL-ADR-Approval

> **HITL-ADR-Approval** (Avenga DevFlow §2.8, §3.0, §3.5). An ADR does not become
> `accepted` — and therefore governing — without the approval of an Architect / Tech
> Lead. Accepting this ADR is also what flips ADR-009 to `superseded`. This ADR is the
> source of truth for its own approval.

| Field | Value |
|-------|-------|
| **Architect / Tech Lead** | eugenio.serrano |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-22T21:38:53-03:00` |
| **review.started_at** | `2026-08-22T21:54:53-03:00` |
| **review.decided_at** | `2026-08-22T21:54:53-03:00` |
