---
id: "ADR-014"
title: "The actors roster is the enablement — the AITL precept carried forward, the per-project AITL-enable ADR and the policy file retired (supersedes ADR-008)"
date: "2026-08-24"
author: "eugenio.serrano"
llm: "claude-fable-5"
status: "accepted" # draft | accepted | rejected | deprecated | superseded
decision_makers: ["architect", "tech_lead"]
sources:
  - "devflow/adrs/ADR-008-aitl-approval-precept.md"
  - "devflow/adrs/ADR-007-devflow-agent-identity-model.md"
  - "devflow/functional/user-stories/US-024-unified-actors-roster.md"
  - "devflow/discovery/DISC-001-aitl-and-subagent-orchestration.md"
  - "devflow/discovery/DISC-002-devflow-agents-architecture.md"
supersedes: ["devflow/adrs/ADR-008-aitl-approval-precept.md"]
conflicts_with: [] # supersedes ADR-008 whole (no partial supersede exists); every fixed invariant is carried forward in §3.1–3.7 so nothing governs by reference to a superseded ADR
tags: ["aitl", "precept", "roster", "enablement", "carry-forward", "v5.1", "foundational"]
nfrs: ["approval-integrity"]
waiver: # Only for gate-override ADRs (§3.6)
  gate: ""
  reason: ""
  owner: ""
  compensating_control: ""
  expires_at: ""
review_ready_at: "2026-08-24T00:10:04-03:00" # When this version is submitted for review (§3.0)
review: # AITL-ADR-Approval evidence — decision dictated in conversation and transcribed by the agent (§3.0)
  decision: "approved" # approved | rejected
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "architect"
      model: null
  started_at: "2026-08-24T00:12:00-03:00"
  decided_at: "2026-08-24T00:16:18-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved as Architect. Review protocol executed: an independent cross-model carry-forward diff of §3.1-3.7 against ADR-008 §3.1-3.7 returned PASS — the carried invariants are faithful in substance; exactly two agreed changes, both explicitly marked in the text as changes rather than carries: (1) §3.3.3 the per-project tighten knob retires with project-policy.yaml, the [critical, regulatory] ceiling becomes a fixed methodology rule (re-add tighten-only is v2); (2) §3.6 the approver capability ceiling's enforcement modality moves from declared capability fields to a text rule for v1, schema enforcement returns in v2 — the ceiling itself (T0/T1, no write paths, no transactional MCPs) is carried intact. Two minor restorations applied pre-stamp from the same review: §3.3.2 single-provider rationale, §3.10 the conductor/engine DISC pointer. The new mechanism (§3.8-3.9: a schema-valid roster entry is the explicit configuration; enablement is the human's act, never self-enabled; roster.yaml as team-membership authority; the two retired files) matches the maintainer's directed design. ADR-008 moves to superseded with this acceptance."
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs, and section
  headings (##) stay in English (the schema). ADR titles and prose go in
  the project's content_language (en). `AITL-ADR-Approval` is never
  translated.

  ⚠️ This ADR is a DRAFT until an Architect / Tech Lead records
  AITL-ADR-Approval. A draft ADR cannot govern; until acceptance ADR-008
  remains the governing precept.

  ⚠️ SUPERSEDE WITH CARRY-FORWARD: the methodology has no partial
  supersede — a superseded ADR is ignored whole. This ADR therefore
  supersedes ADR-008 entirely and RE-STATES every invariant that stays
  fixed (§3.1–3.7, the carried precept) before deciding what changes
  (§3.8–3.9, the enablement mechanism). The carried sections preserve
  ADR-008's substance without drift — the independent cross-model review
  diffs them against ADR-008 before approval.

  ⚠️ SCOPE: product design for v5.1 (maintainer partition). The kit
  implementation (the actors/ reshape, the schema rule, the methodology
  §3.0 text) lands via the US-024 G15 re-revision + a Bolt citing this
  ADR. Version 1 is deliberately simple; the hardening is explicit
  follow-up (§4).
-->

# ADR-014 — The actors roster is the enablement

| Field          | Value |
|----------------|-------|
| **Status**     | **accepted** (immutable — a new decision requires a superseding ADR) |
| **Decision-makers** | Architect / Tech Lead |
| **Sources**    | ADR-008 (the precept being carried), ADR-007 (identity), US-024 (roster), DISC-001/002 (approved) |
| **Supersedes** | **ADR-008** (whole — its fixed invariants are carried forward here, §3.1–3.7) |
| **Conflicts with** | None — ADR-007/010 stay active (their passing references to the retired mechanism read against this ADR, §3.10) |

---

## 1. Context

ADR-008 defined the AITL precept — human-by-default,
agent-by-explicit-configuration — and fixed its safe default, independence
layers and identity rules. For the *mechanism* of that explicit
configuration, its §3.8 required each adopting project to sign a
**per-project AITL-enable ADR** (operationalized by US-024 as
`TEMPLATE-AITL-ENABLE-ADR.md`, plus a roster-level `project-policy.yaml`
with an `aitl_enabled_checkpoints` switch).

The maintainer's review found that mechanism **redundant and too heavy**:
the team already configures its actors in the roster
(`actors/<actor-id>.yaml` — id, role, model, `modes`, `approves`) as
human-authored, versioned, schema-validated configuration. Requiring a
*second* governed artifact (a signed ADR) plus a *third* switch (the
policy file) for the same team to enable its configured agents adds
ceremony without adding configuration: **the roster entry is the explicit
configuration**.

Because §3.8's vehicle is written into an accepted — immutable — ADR, and
the methodology has **no partial supersede** (a superseded ADR is ignored
whole), the change requires superseding ADR-008 entirely and **carrying
forward** everything that stays fixed. That is this ADR: §3.1–3.7 carry
the precept unchanged in substance; §3.8–3.9 decide the new mechanism.

---

## 2. Alternatives considered

### Alternative A — Supersede ADR-008 with full carry-forward (✅ Selected)

| Aspect   | Detail |
|----------|--------|
| **Pros** | One active precept ADR, one enablement vehicle — no textual conflict between active ADRs. Every fixed invariant re-stated here, so nothing governs by reference to a superseded document. Methodologically clean (§3.5: supersede is the only amendment mechanism). |
| **Cons** | The carry-forward must be faithful — any drift in the re-stated invariants would weaken the precept. Mitigated by an independent cross-model diff against ADR-008 before approval. |

### Alternative B — Complement ADR-008 ("the roster implements §3.8")

| Aspect   | Detail |
|----------|--------|
| **Pros** | ADR-008 stays active; smaller document. |
| **Cons** | Leaves a latent textual conflict: ADR-008 §3.8 literally requires "an explicit per-project AITL-enable ADR" while this ADR retires it — two active ADRs prescribing different vehicles for the same requirement can legitimately trip the §3.5 conflict gate. The methodology has no "interpretive amendment"; it has supersede. Rejected. |

### Alternative C — Keep the per-project AITL-enable ADR

| Aspect   | Detail |
|----------|--------|
| **Pros** | The shipped mechanism; ceremony and immutability per project. |
| **Cons** | Duplicates the roster's configuration; friction for every adopting team; the maintainer's direction is the opposite. Rejected. |

### Alternative D — No enablement rule (free delegation)

| Aspect   | Detail |
|----------|--------|
| **Pros** | Maximum agility. |
| **Cons** | Dissolves the safe default — any agent could sign anything. Rejected outright: it is the failure mode the AITL precept exists to prevent. |

---

## 3. Decision

**We adopt Alternative A.** Sections **3.1–3.7 carry ADR-008's invariants
forward unchanged in substance** — they remain the law exactly as decided
there; only the section numbering is local to this ADR. Sections
**3.8–3.9 are the new decision**.

### 3.1 The precept (carried) — AITL, human-by-default

Every checkpoint remains a **mandatory pause** — nothing about the stops
is weakened. **AITL — Actor-in-the-Loop:** the actor in the loop is a
**human by default**, and a virtual DevFlow Agent **only by explicit,
valid configuration** (§3.8). The umbrella term is **"actor"** — a human
or an AI agent (a *DevFlow Agent*, ADR-007). HITL does not disappear — it
is the **default case** (actor = human) inside AITL. The canonical
checkpoint identifiers are `AITL-<CODE>-Approval`; the record — the
manifest's `checkpoint_approvals[]` — states who actually signed and how
(`human:<user>` or `agent:<id>`/`model:<id>`). History is never rewritten
(G36): recorded `HITL-*` approvals stay as history; `AITL-*` is the
canonical vocabulary (G05 scopes the legacy prefix).

### 3.2 The safe-default invariant (carried, non-negotiable)

With **no — or invalid — agent configuration**, a project behaves as
**pure HITL**: every checkpoint is a human approval. It must be
**impossible** for a project with absent or invalid configuration to reach
an AI-signed approval. The delegating path requires an explicit, present,
valid configuration; absence always resolves to human-only. This invariant
is the whole contract — it is **enforced in tooling, never left to prompt
prose**.

### 3.3 Independence, layered (carried — the floor is now fixed)

1. **Floor (always): approver actor ≠ executor actor.** The actor that
   approves is never the actor that executed — the generalization of the
   human handoff rule and G37 (Judge ≠ Challenger). Same actor approving
   its own work = never.
2. **Model hardening (high risk): approver.model ≠ executor.model.** At
   `high`, different actors must also run different models. At
   `low`/`medium`, model diversity is recommended, not required — so
   single-provider teams remain first-class.
3. **Human ceiling (top): `critical` + `regulatory` = human only.**
   **Changed from ADR-008 — explicit:** with `project-policy.yaml`
   retired (§3.9), the per-project "may tighten the floor" knob
   disappears in v1. The ceiling `[critical, regulatory]` is now a
   **fixed methodology rule** — not configurable in either direction.
   Re-adding a tighten-only knob is v2 follow-up if a project needs it.

### 3.4 Identity rules stay hard (carried — scoped, never dissolved)

G18/G24 are **scoped, not deleted**: *"the AI never approves"* means *"the
AI never approves **unless** the project has explicitly configured a
virtual approver for that checkpoint class (§3.8) **and** the independence
rule (§3.3) holds"*. The record **never fabricates a human** — a virtual
approval is always `agent:<id>` / `model:<id>`, never a human name.
**G37** (AREV neutrality) and the **handoff** rule are **excluded from any
no-holder fallback**: "no holder" may route a human role to another
available human, but it can never become a licence for self-approval.

### 3.5 Separation of duties (carried) — the Coordinator never signs

The Coordinator (the AvengaDevFlow MainAgent, ADR-007) **routes and
records but never signs a checkpoint**. Approver agents are spawned **only
by the Coordinator or invoked by a human — never from an executor's
subtree** (spawn topology), so an executor can never spawn "its own"
approver.

### 3.6 Approver capability ceiling (carried — text rule in v1)

An agent **acting as approver** runs at **capability tier T0** (at most T1
with pinned, trusted sources) — **no transactional MCPs, no write paths**
(the injection-forged-approval defense). Approving needs nothing external:
the evidence (diff, tests, MEM, manifest) is in the repo. Executor agents
may be as capable as a project dares; **approval integrity never depends
on an executor's capability tier.**
**v1 note — explicit:** with `TEMPLATE-ACTOR.yaml` simplified (§3.9), the
`capabilities` fields are deferred, so in v1 this ceiling governs **as a
rule of this ADR** (text — agents and reviewers enforce it), not as a
schema-checked field. Schema enforcement returns with the v2 hardening
(§4) when the capability fields return.

### 3.7 The escalation floor (carried, engine-enforced)

Regardless of configuration, these force a **human stop**, non-delegable:
gate red, turn-budget exhausted, a changes-requested loop, an ADR-class
change, or missing/contradictory evidence. The floor is engine-enforced,
never left to prompt prose. A role's prompt may escalate **above** the
floor; never below it.

### 3.8 The new mechanism — the roster is the enablement

1. **The roster entry is the explicit, valid configuration.** A DevFlow
   Agent configured in the project's roster — a **schema-valid**
   `actors/<actor-id>.yaml` with `modes` containing `approver` and a
   **non-empty `approves`** — may occupy those AITL checkpoint classes
   **exactly like a human**, under §3.2–3.7. This satisfies G24's
   "explicit valid configuration". **No per-project ADR is required, and
   no separate policy switch exists** — the actor's `approves` is the
   grant.
2. **Enablement is the human's configuration act.** The roster is
   human-authored configuration: a human writes or merges the actor file
   and the roster listing — the git history is the record. **An agent
   never enables its own approval**: the MainAgent lifecycle (ADR-013)
   may scaffold an actor as an **executor-only draft**, but the authority
   fields (`modes: [approver]`, `approves`) are configured by the human,
   never by an agent.
3. **Safe default, restated for the mechanism:** no roster, no listing,
   or no schema-valid approver entry → the checkpoint resolves to humans
   (zero-config = pure HITL, §3.2). The schema is the validity gate: an
   invalid actor file **fails fast** and the safe default applies until
   fixed.
4. **v1 schema rule (minimal, the only addition):** `roster.schema.yaml`
   gains — `modes` contains `approver` ⇒ `approves` is non-empty. Nothing
   else is added in v1.

### 3.9 The roster family shape (v1) — what exists, what retires

The `actors/` family in the kit:

| File | Role |
|------|------|
| `roster.yaml` | **New — the team list, the single membership authority:** one entry per actor referencing its `<actor-id>.yaml`. An actor file **not listed is not in the team** (drafts/retired actors carry no authority). |
| `actors/<actor-id>.yaml` | One file per actor (unchanged model) — the detail: id, name, role, model, `modes`, `approves`, `definition` for agents. |
| `roster.schema.yaml` | Validates an **actor file** (unchanged role) + the v1 rule (§3.8.4). **v1 validation of the list:** every id in `roster.yaml` resolves to an existing `<actor-id>.yaml` — a consistency check, not a second schema. |
| `TEMPLATE-ACTOR.yaml` | Kept, **simplified** — the `capabilities` block is deferred to v2 (see §3.6's v1 note); fields return incrementally. |
| `README.md`, `INDEX.md` | Kept — README rewritten to this model; INDEX lists the family docs (the *team* lives in `roster.yaml`). |
| `examples/` | **New subfolder** — the worked examples move here (`examples/example.yaml`). |
| `project-policy.yaml` | **Retired.** `aitl_enabled_checkpoints` is redundant (the actor's `approves` is the grant); the `human_only` floor moves into the fixed rule of §3.3.3. |
| `TEMPLATE-AITL-ENABLE-ADR.md` | **Retired.** The mechanism it carried is replaced by §3.8. |

The file-level implementation lands via the **US-024 G15 re-revision + a
Bolt citing this ADR** (the kit reshape, the schema rule, the README
rewrite, the methodology §3.0 text and the `agents/roles/README`
references).

### 3.10 Reading notes — scope of the supersede

- **ADR-008 → superseded** (whole). Its substance survives as §3.1–3.7
  here; its §3.8 mechanism is replaced by §3.8–3.9 here.
- **ADR-007 and ADR-010 stay active.** Each mentions the retired
  AITL-enable ADR **once, in passing** (context/scope, not their
  decisions); those references now read against this ADR's mechanism.
- **ADR-013** (draft) is revised to cite this ADR for the approver leg of
  its executor/approver split, then follows its own approval.
- **Delivered artifacts** (US-022/023/024, their MEMs, SPECs and recorded
  approvals) are history — never rewritten (G36).
- **Carried pointer (the one open item from ADR-008 §3.9):** the
  conductor/engine evaluation (MAF/Squads/squad) remains a separate,
  forthcoming DISC (DISC-001 rec #5).

---

## 4. Consequences

**Positive:**
- One configuration source: teams configure their squad once (the roster)
  and their configured agents act as peers of humans at the checkpoints
  the team granted them — no second artifact, no third switch.
- The precept survives intact: §3.1–3.7 carry every ADR-008 invariant, so
  the supersede loses nothing.
- Adoption friction drops exactly where the maintainer wanted: enablement
  = editing versioned config, not signing ceremony.

**Trade-offs (explicit, accepted for v1):**
- The approval path's safety rests on (a) the human authorship of the
  roster and (b) schema validity — a lighter guard than the signed-ADR
  ceremony.
- The approver capability ceiling (§3.6) is a text rule in v1 — no
  schema-checked field until the capability fields return.
- The "tighten the floor" knob is gone in v1 (§3.3.3) — the ceiling is
  fixed at `[critical, regulatory]`.

**Technical debt / follow-up (the v2 hardening, maintainer's pending
design):**
- Capability fields return to `TEMPLATE-ACTOR.yaml` + schema-enforced
  approver ceiling (tier ≤ T1, no write paths, no transactional MCPs).
- Authority-change audit (changes to `modes`/`approves` reviewed —
  the never-self-enabled rule enforced, not only stated).
- Optionally: a tighten-only floor knob, if a project needs more classes
  human-only.
- **US-024 G15 re-revision** + **US-024.BOLT-004** (the kit reshape).
- **ADR-013** revision (§3.3 cites this ADR) → its own re-approval.
- **US-025** (draft) and **US-023 rev 3** updated to cite this ADR where
  they cite ADR-008's mechanism.

---

## 5. Applicable NFRs

| NFR | Description | Threshold | How it is measured |
|-----|-------------|-----------|-------------------|
| `approval-integrity` | Carried from ADR-008 with the mechanism updated: an AI-signed approval can occur only with a schema-valid roster entry granting that checkpoint class, with approver actor ≠ executor actor, and never via injected content | Zero AI-signed approvals without a valid roster grant; zero approver actors equal to the executor; approver agents never above T1 (§3.6 — text rule in v1) | Safe-default + schema fail-fast tests; independence lookup on the roster; recorded per approval in `checkpoint_approvals[]` |

---

## 6. References

- [ADR-008](ADR-008-aitl-approval-precept.md) — **superseded by this
  ADR**; the source of the carried §3.1–3.7 (diffed against this text at
  review).
- [ADR-007](ADR-007-devflow-agent-identity-model.md) — the actor identity
  model (active; its one passing AITL-enable reference reads per §3.10).
- [ADR-010](ADR-010-actor-grammar-and-pure-v5-vocabulary.md) — the actor
  grammar (active; same reading note).
- [ADR-013](ADR-013-agent-lifecycle-governance.md) — the agent lifecycle
  (draft; revised to cite this ADR).
- [US-024](../functional/user-stories/US-024-unified-actors-roster.md) —
  the roster family (G15 re-revision pending this ADR).
- [DISC-001](../discovery/DISC-001-aitl-and-subagent-orchestration.md),
  [DISC-002](../discovery/DISC-002-devflow-agents-architecture.md)
  (approved) — the research base (DISC-001 §5.6.3's AITL-enable-ADR
  suggestion is the part this ADR replaces).
- GUARDRAILS **G18/G24** — unchanged in force, scoped per §3.4/§3.8.

---

## 7. AITL-ADR-Approval

> **AITL-ADR-Approval** (Avenga DevFlow §2.8, §3.0, §3.5). An ADR does not
> become `accepted` — and therefore governing — without the approval of an
> Architect / Tech Lead. This ADR is the source of truth for its own
> approval (recorded in the `review` frontmatter block). Only once
> `accepted` does ADR-008 move to `superseded`, and only then may the
> US-024 re-revision and the kit Bolt cite this ADR. Review protocol:
> **diff §3.1–3.7 against ADR-008 §3.1–3.7** (the carry-forward fidelity
> check) before deciding.

| Field | Value |
|-------|-------|
| **Architect / Tech Lead** | `human:eugenio.serrano` |
| **Role** | architect |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-24T00:10:04-03:00` |
| **review.started_at** | `2026-08-24T00:12:00-03:00` |
| **review.decided_at** | `2026-08-24T00:16:18-03:00` |
| **Findings** | none blocking — the carry-forward diff (§3.1–3.7 vs ADR-008) returned PASS; the two agreed changes (§3.3.3 fixed ceiling, §3.6 text-rule enforcement in v1) are marked as changes in the text; two minor restorations (single-provider rationale, conductor/engine pointer) applied pre-stamp. Full reason in the frontmatter `review:` block |
