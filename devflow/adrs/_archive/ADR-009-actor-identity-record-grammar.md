---
id: "ADR-009"
title: "The actor record grammar: one identity vocabulary (human:<user> | agent:<id>) for every recorded identity — review contracts, generation records and frontmatter person fields"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-fable-5"
status: "superseded"
superseded_by: "ADR-010"
decision_makers: ["architect", "tech_lead"]
sources:
  - "devflow/adrs/ADR-007-devflow-agent-identity-model.md"
  - "devflow/adrs/ADR-008-aitl-approval-precept.md"
  - "devflow/reviews/REV-003-user-to-actor-identity-vocabulary.md"
  - "devflow/discovery/DISC-002-devflow-agents-architecture.md"
supersedes: []
conflicts_with: []
tags: ["aitl", "actor", "identity", "manifest", "review-contract", "v5.0"]
nfrs: ["identity-attribution"]
waiver:
  gate: ""
  reason: ""
  owner: ""
  compensating_control: ""
  expires_at: ""
review_ready_at: "2026-08-22T21:07:23-03:00"
review: # HITL-ADR-Approval evidence — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers:
    - user: "eugenio.serrano"
      role: "architect"
  started_at: "2026-08-22T21:11:59-03:00"
  decided_at: "2026-08-22T21:11:59-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Accepted. The 'manifest ADR' commissioned by ADR-008 §3.9, widened to the full identity grammar and grounded in REV-003 (approved). The two judgment calls confirmed consciously: (§3.2) two strictness tiers — prefix-mandatory in machine records and review/enforcement fields, bare-as-human shorthand in descriptive frontmatter with normalization, so pure-HITL projects write as in v4.2 and the agent form is never bare/ambiguous; and (§3.5) `mode` dropped as a derived state (G39), the actor prefixes being the single source of truth. reviewers→{actor,role,model} makes the projection a copy; created_by actor-shaped + runs[].agent attributes generation to the exact agent; hitlSubject→checkpointSubject. Complementary — supersedes nothing (ADR-007/ADR-008 unchanged). Immutable from now on. Implementation lands via one non-functional Bolt under US-000 (REV-003 §6)."
---

<!--
  ⚠️ SUPERSEDED by ADR-010 (2026-08-22T21:54:53-03:00). Per §3.5 the substantive
  content below is UNCHANGED (read-only); only `status` and this banner change.
  ADR-010 carries this ADR's actor grammar forward verbatim in intent (its
  §3.1–§3.5) and reverses only the vocabulary/migration clauses (§3.7/§3.8 here):
  v5 records are pure AITL-*, migration rewrites HITL-*→AITL-* names. Do not use
  this ADR as governing — see ADR-010.

  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs and section headings
  stay in English (the schema); prose follows content_language (en).
  `HITL-ADR-Approval` is never translated.

  ⚠️ SCOPE: this was the "manifest ADR" that ADR-008 §3.9 commissioned, widened
  to the full identity grammar. Decided/operated under v4.2 (ADR-006). Built on
  ADR-007 (what an actor is) and ADR-008 (who may approve).
-->

# ADR-009 — The actor record grammar: one identity vocabulary for every recorded identity

> ⛔ **SUPERSEDED by [ADR-010](ADR-010-actor-grammar-and-pure-v5-vocabulary.md)**
> (2026-08-22). Its grammar (§3.1–§3.5) is carried forward there verbatim in
> intent; its vocabulary/migration clauses (§3.7/§3.8) are reversed (v5 records
> are pure AITL-*, migration rewrites the names). Not governing.

| Field          | Value |
|----------------|-------|
| **Status**     | **superseded** by ADR-010 (was accepted 2026-08-22T21:11:59; content immutable, §3.5) |
| **Decision-makers** | Architect / Tech Lead (maintainer) |
| **Sources**    | ADR-007 (actor identity), ADR-008 (AITL precept, §3.9 commission), REV-003 (approved — the site inventory), DISC-002 (approved) |
| **Supersedes** | None — complementary: nothing in ADR-007/ADR-008 changes; this ADR supplies the record syntax both deferred |

---

## 1. Context

ADR-007 fixed that **the actor — a human or a DevFlow Agent — is the unit of
identity**, and explicitly deferred the record syntax; ADR-008 commissioned
"the manifest ADR" (§3.9) for exactly that. REV-003 (approved) inventoried the
kit and found **three coexisting identity grammars**:

1. **actor-shaped** — only `checkpoint_approvals[].decided_by[]`
   (`{actor: "human:<user>"|"agent:<id>", role, model}`);
2. **user-shaped** — the artifact-side review contract
   (`reviewers: [{user, role}]`, 16 template blocks + the §3.0 normative
   example + GUARDRAILS) and `risk_history[].decided_by[].user`;
3. **bare-human** — `generation.created_by` (schema: unconstrained string;
   §3.12: *"identifies the human"*) and ~35 frontmatter person fields
   (`author:`, `owner:`, `validator:`, `closed_by:`, `facilitator:`).

Two of REV-003's findings block capability that is **already decided**: a
virtual approver — permitted by ADR-008 and recordable in the manifest —
cannot be recorded on the artifact itself (F-01), and a generation cannot be
attributed to an agent at all: `runs[]` records the *model* but not the
*actor*, making two role agents on one model indistinguishable — the exact
failure ADR-007 rejected in its Alternative B (F-02).

The timing is the last cheap moment (REV-003 F-07): the v5 manifest family is
unreleased, so reshaping it folds into the already-mandatory `4.0`→`5.0`
conversion at zero migration cost. After the v5.0 release the same change is a
new major.

---

## 2. Alternatives considered

### Alternative A — One actor grammar, two strictness tiers (✅ Selected)

Prefix-mandatory in machine records and enforcement fields; bare-as-human
shorthand in descriptive frontmatter, with a normalization rule.

| Aspect | Detail |
|--------|--------|
| **Pros** | One vocabulary end to end; the artifact↔manifest projection becomes a field-for-field copy; strictness exactly where validators and identity comparisons operate; ergonomics preserved where humans type (an `author:` line looks like v4.2 unless an agent authored); the agent form is always marked, so bare is never ambiguous. |
| **Cons** | Two tiers to explain; validators must implement the bare→`human:` normalization. |

### Alternative B — Prefix-mandatory everywhere

| Aspect | Detail |
|--------|--------|
| **Pros** | Maximum uniformity; a single pattern validates every field. |
| **Cons** | Every `author:`/`owner:` line in every document gains a `human:` prefix that carries no information in the overwhelmingly common case — ceremony without signal, and needless friction for pure-HITL projects that never configure an agent. Rejected: the safe default should also be the ergonomic default. |

### Alternative C — Keep `user`/bare fields, add parallel agent fields

| Aspect | Detail |
|--------|--------|
| **Pros** | No renames; v4.2 muscle memory intact. |
| **Cons** | Two grammars forever; the projection stays a transform; every identity comparison (G18, G29, T02, handoff) special-cases two shapes. Rejected: it institutionalizes the drift REV-003 found. |

---

## 3. Decision

**We adopt Alternative A.** For v5.0:

### 3.1 The grammar

Every recorded identity uses one of two namespaces:

- **`human:<user>`** — `<user>` is the local part of the person's
  `git config user.email` (§3.0, unchanged: git config remains the *source*
  of the human namespace, never a field name).
- **`agent:<id>`** — `<id>` is the DevFlow Agent's stable kebab-case identity
  (ADR-007 §3.1), resolved against the agent definition / roster (the
  `agents/` registry US).

### 3.2 Two strictness tiers, one normalization rule

- **Machine records and enforcement fields — prefix-mandatory** (pattern
  `^(human|agent):.+`): every identity field in `metrics/**/*.json`
  (`created_by`, `decided_by[].actor`) and every identity field of the
  artifact-side **review contract** (`review.reviewers[].actor`,
  `acceptance_review.reviewers[].actor`, `risk_history[].decided_by[].actor`)
  — these are the approval and generation evidence that G18/G24/G29/T02 audit.
- **Descriptive frontmatter person fields — bare = human shorthand:**
  `author:`, `owner:`, `validator:`, `closed_by:`, `facilitator:` (and any
  future person field) accept a bare `<user>` meaning `human:<user>`; an agent
  is **always** written `agent:<id>` — the agent form is never bare, so a bare
  value is never ambiguous.
- **Normalization:** wherever identities are compared or projected, a bare
  value compares equal to its `human:`-prefixed form. G18 (approver actor ≠
  executor actor), G29/T02 (approver ≠ BUG `owner`) and the handoff rule work
  verbatim as actor comparisons under this rule.

### 3.3 The review contract records actors

`reviewers: [{user, role}]` becomes **`reviewers: [{actor, role, model}]`** —
the exact shape of `checkpoint_approvals[].decided_by[]`: `model` is `null`
for a human and the model id for an agent (same conditional as the manifest's
`$defs.approver`). Applies to `review:`, `acceptance_review:` and
`risk_history[].decided_by`. The §3.0/GUARDRAILS **projection becomes a
copy**, and its mismatch rule gains teeth: artifact and manifest now share one
grammar, so a mismatch is a real divergence, never a shape artifact. W11's
field list updates accordingly.

### 3.4 The generation record attributes actors — including which agent

- `generation.created_by` records **the actor that initiated or controlled
  the generation** (prefix-mandatory; human by default). §3.12's *"identifies
  the human"* rewords to *"identifies the actor (a human by default)"*.
- `runs[]` gains **`agent`** — required, nullable, matching the family's
  explicit-null style: `null` when the run was not executed by a DevFlow
  Agent; the agent `id` when it was. `tool`/`provider`/`model` are unchanged
  (an agent run still records its model — the roster's model-per-agent
  declaration is auditable against it).

### 3.5 `mode` is dropped from `checkpoint_approvals[]`

`mode` is fully derivable — `virtual` iff any `decided_by[].actor` carries the
`agent:` prefix — and the family's own discipline (G39, §3.12) is that derived
states are never stored. Keeping it as a documented exemption was considered
and rejected: the actor prefixes are the single source of truth, and a stored
duplicate is one more field that can contradict them. Dashboards and
validators derive it in one expression.

### 3.6 Contract hygiene in the same pass

`$defs.hitlSubject` (manifest-v5-bolt.schema.json) is renamed
**`checkpointSubject`** — `HITL-*` phrase-family residue (ADR-005 class)
inside the v5 contract.

### 3.7 Conversion stays lossless (§5.16, G36)

The `4.0`→`5.0` conversion extends — same sanctioned reshape class as the
already-specified `decided_by` mapping:

| `4.0` value | `5.0` value |
|-------------|-------------|
| `reviewers: [{user: "<u>", role}]` | `[{actor: "human:<u>", role, model: null}]` |
| `created_by: "<u>"` | `"human:<u>"` |
| `runs[]` entry | gains `agent: null` |
| `hitl_approvals[]` entry | `checkpoint_approvals[]` per ADR-008/§5.16 — **no `mode` written** |

Every recorded value crosses untouched (prefixing reshapes the envelope, never
the evidence); recorded v4.2 history in governed documents is never rewritten.

### 3.8 Scope guards (from REV-003 F-06)

- **AREV phase fields stay model-based** (`challenger_model` /
  `defender_model` / `judge_model`): G37 neutrality is between *models*;
  deliberately outside the actor grammar (DISC-002 scope).
- **Role and domain fields are not identities:** `role`, `decision_makers`,
  `participants`, `stakeholders`, `real_name` are untouched.
- **History (G36):** nothing already recorded is rewritten; the conversion
  table above is where old shapes become actor-shaped.

### 3.9 Decided elsewhere

- *Who may occupy an approval* → ADR-008 + the per-project AITL-enable ADR.
- *Who may initiate/execute* (agent initiative governance) → a forthcoming
  ADR of the DevFlow Agents phase.
- *The `agents/` registry, roster schema, wrapper syntax* → the registry US
  (DISC-002 rec #3).
- *The kit's dangling maintainer-ADR citations* (REV-003 F-08) → a
  correction, not a decision: routed with the sweep Bolt.

---

## 4. Consequences

**Positive:**
- One identity grammar end to end; the artifact↔manifest projection is a copy,
  and its mismatch check becomes a genuine integrity control.
- A virtual approval is recordable on the artifact itself (unblocks the
  capability ADR-008 already granted), and a generation is attributable to the
  exact DevFlow Agent (unblocks the executor/initiator phase).
- Every identity comparison the methodology already had (G18, G24, G29, T02,
  handoff) works verbatim over actors.
- Pure-HITL projects notice nothing: bare human values remain valid in
  documents, and zero-config behavior is unchanged (ADR-008 §3.2).

**Trade-offs:**
- A schema reshape — free only while v5 is unreleased (REV-003 F-07); after
  release this same decision would cost a new major with full conversion.
- Validators and the future Coordinator must implement the normalization rule.
- Anything already reading `mode` must derive it (no known consumer exists —
  the family shipped days ago and the kit's `metrics/bolts/` is empty).

**Technical debt / follow-up:**
- One non-functional Bolt under US-000 executes the sweep (REV-003 §6 item 2):
  3 schemas + 5 manifest examples + §3.0/§3.3/§3.12/§5.16 + GUARDRAILS + 16
  template review blocks + ~35 frontmatter comments + the four agents + the
  F-05/F-08 corrections, under the ADR-005 phrase-family discipline
  (`[{user, role}]`, bare `created_by`, the canonical-identity paragraph).
- The registry US consumes this grammar for the roster and agent definitions.

---

## 5. Applicable NFRs

| NFR | Description | Threshold | How it is measured |
|-----|-------------|-----------|-------------------|
| `identity-attribution` | Every recorded generation and approval resolves to exactly one actor id in the canonical grammar | Zero non-prefixed identities in machine records; zero agent-executed runs without `runs[].agent`; zero review contracts whose projection mismatches the manifest | Schema validation (`^(human\|agent):.+` patterns) + the sweep Bolt's ADR-005 absence checks + the §3.0 projection mismatch rule |

---

## 6. References

- [ADR-007](ADR-007-devflow-agent-identity-model.md) — the actor as the unit
  of identity; the syntax this ADR supplies is the piece it deferred.
- [ADR-008](ADR-008-aitl-approval-precept.md) — §3.9 commissioned this ADR;
  §3.4 (the record never fabricates a human) is enforced by this grammar.
- [REV-003](../reviews/REV-003-user-to-actor-identity-vocabulary.md)
  (approved) — the full-kit inventory: F-01…F-05 gaps, F-06 scope guards,
  F-07 timing window, F-08 citation correction.
- [DISC-002](../discovery/DISC-002-devflow-agents-architecture.md) (approved)
  — the roster and agent-definition fields this grammar will be looked up
  against.

---

## 7. HITL-ADR-Approval

> **HITL-ADR-Approval** (Avenga DevFlow §2.8, §3.0, §3.5). An ADR does not
> become `accepted` — and therefore governing — without the approval of an
> Architect / Tech Lead. This ADR is the source of truth for its own approval
> (recorded in the `review` frontmatter block). ADR approvals are never copied
> to the Bolt manifest.

| Field | Value |
|-------|-------|
| **Architect / Tech Lead** | eugenio.serrano |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-22T21:07:23-03:00` |
| **review.started_at** | `2026-08-22T21:11:59-03:00` |
| **review.decided_at** | `2026-08-22T21:11:59-03:00` |
