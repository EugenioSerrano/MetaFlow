---
id: "ADR-008"
title: "The AITL approval precept: HITL becomes human-by-default, agent-by-explicit-configuration — an opt-in superset with layered independence and inviolable identity rules"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
status: "superseded" # superseded by ADR-014 (2026-08-24) — its §3.1–3.7 invariants are carried forward there; the §3.8 AITL-enable ADR mechanism is replaced by the roster enablement (ADR-014 §3.8–3.9). Body and recorded approval untouched (G36).
decision_makers: ["architect", "tech_lead"]
sources:
  - "devflow/adrs/ADR-007-devflow-agent-identity-model.md"
  - "devflow/discovery/DISC-001-aitl-and-subagent-orchestration.md"
  - "devflow/discovery/DISC-002-devflow-agents-architecture.md"
  - "devflow/adrs/ADR-006-versioning-and-self-development-model.md"
supersedes: []
conflicts_with: []
tags: ["aitl", "hitl", "precept", "independence", "opt-in-superset", "v5.0", "foundational"]
nfrs: ["approval-integrity"]
waiver:
  gate: ""
  reason: ""
  owner: ""
  compensating_control: ""
  expires_at: ""
review_ready_at: "2026-08-22T14:24:02-03:00"
review: # HITL-ADR-Approval evidence — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "architect"}]
  started_at: "2026-08-22T14:33:30-03:00"
  decided_at: "2026-08-22T14:33:30-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Accepted — the foundational v5.0 precept. HITL evolves into AITL (Actor-in-the-Loop) in concept and in every checkpoint name, throughout the product: actor = a human (default) or an AI agent / DevFlow Agent (virtual, by explicit config). Opt-in superset with the safe-default invariant (no/invalid config → pure HITL, no AI-signed approval possible); layered independence (actor floor / model hardening at high / human ceiling at critical+regulatory); G05/G18/G24 evolved-and-scoped, not deleted; Coordinator-never-signs; approver capability ceiling (T0/T1) against injection-forged approvals; engine-enforced escalation floor; human-depth as per-project config above the fixed floor. Built on ADR-007. History preserved (v4.2 HITL-* records untouched, G36); the HITL→AITL kit sweep executes as US/Bolt under the ADR-005 discipline. Immutable from now on."
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs and section headings
  stay in English (the schema); prose follows content_language (en).
  `HITL-ADR-Approval` is never translated.

  ⚠️ This ADR is a DRAFT until an Architect / Tech Lead records
  HITL-ADR-Approval. A draft ADR cannot govern.

  ⚠️ FOUNDATIONAL: this is the ADR that DEFINES v5.0 — it changes the
  methodology's core precept (§0). It is decided/operated under v4.2 (ADR-006);
  its methodology-text implementation (§0, GUARDRAILS G18/G24, the checkpoint
  charter) lands in the kit via USs/Bolts. Built on the actor identity model of
  ADR-007.
-->

# ADR-008 — The AITL approval precept: human-by-default, agent-by-explicit-configuration

| Field          | Value |
|----------------|-------|
| **Status**     | **accepted** (immutable — a new decision requires a superseding ADR) |
| **Decision-makers** | Architect / Tech Lead (maintainer) |
| **Sources**    | ADR-007 (actor identity), DISC-001 + DISC-002 (approved), ADR-006 (versioning) |
| **Supersedes** | None |
| **Conflicts with** | None — evolves/scopes G05, G18, G24 (does not delete them); see §3.1, §3.4 |

---

## 1. Context

The v5.0 vision (DISC-001, DISC-002, both approved) evolves **HITL → AITL**: a
checkpoint may be resolved by a human **or** a virtual DevFlow Agent. This is not
a feature bolted on the side — it changes the methodology's **core precept**.
Today §0 says, in effect, *"the AI generates, the human governs at every
checkpoint"*; G18/G24 forbid any AI-signed approval outright. v5.0 needs to state
precisely how an AI actor can occupy an approval **without** dissolving the
guarantee that made DevFlow trustworthy.

ADR-007 fixed the substrate: the **actor** (a human or a DevFlow Agent) is the
unit of identity, and authority lives in structured fields. This ADR decides the
**governance layer on top**: who may approve, under what independence, with what
safe default, and which rules can never be relaxed. The alignment question
DISC-001 §5.6 resolved — AITL as an **opt-in superset**, not a replacement — is
the spine of this decision.

If left unwritten, "AITL" would mean whatever each project assumed: some would
let agents approve everything (unsafe), others nothing (no v5.0). The precept
must be one governed, immutable statement.

---

## 2. Alternatives considered

### Alternative A — AITL as an opt-in superset: human-by-default, agent-by-explicit-configuration (✅ Selected)

| Aspect | Detail |
|--------|--------|
| **Pros** | Loses nothing: zero config → byte-for-byte v4.2 HITL. Extends the methodology without diluting it — HITL is the floor, AITL a configurable layer above. Delegation is always an explicit, governed act. Identity/audit guarantees preserved. Enables the single-operator + squad model. |
| **Cons** | Adds a governance layer (the Coordinator) and per-project configuration; the safe-default invariant must be enforced in tooling, not trusted to prose. |

### Alternative B — Full replacement: agents may approve by default

| Aspect | Detail |
|--------|--------|
| **Pros** | Maximum autonomy; least human friction. |
| **Cons** | Dissolves the safe default and the methodology's identity ("the human governs"). One misconfiguration → AI signs its own release. Rejected outright — it is the failure mode this ADR exists to prevent. |

### Alternative C — Stay pure HITL (no AITL)

| Aspect | Detail |
|--------|--------|
| **Pros** | Simplest; nothing changes. |
| **Cons** | Does not deliver the v5.0 vision (agents as approvers / squad orchestration). |

---

## 3. Decision

**We adopt Alternative A.** The AITL precept for v5.0:

### 3.1 The precept — HITL evolves into AITL, in concept and in name

Every checkpoint remains a **mandatory pause** — nothing about the stops is
weakened. What changes is *who may occupy the pause*: a **human or a virtual
DevFlow Agent** (ADR-007). This is not a feature placed beside HITL — it is the
**evolution of the Human-in-the-Loop concept itself into AITL
(Actor-in-the-Loop)**, applied **throughout v5.0**: from the methodology's
conceptual definition (§0 and the paradigm it states) down to the **checkpoint
identifiers**. HITL does not disappear — it becomes the **default case** (actor =
human) inside the broader AITL concept.

**Definition (fixed here so it is never misread):** *AITL — **Actor**-in-the-Loop.
The actor in the loop is a **human by default**, and a virtual DevFlow Agent
**only by explicit, valid configuration** (§3.2).* The umbrella term is
**"actor"** — **a human or an AI agent** (an AI agent being, in this methodology,
a *DevFlow Agent*, ADR-007). The human is the **default** actor; the AI agent
(DevFlow Agent) is the **virtual** one, enabled only by explicit configuration.
"Actor" (not "agent") is the umbrella on purpose: a human is an actor, not an
"agent", so "actor-in-the-loop, default human" keeps its sense and "AITL" is
never read as "AI by default". (This fixes the canonical expansion;
it refines the exploratory "Agent-in-the-Loop" wording of DISC-001/DISC-002, which
remain as historical research.)

**Nomenclature evolution:** the canonical checkpoint identifiers change
`HITL-<CODE>-Approval` → **`AITL-<CODE>-Approval`** (`AITL-US-Approval`,
`AITL-BUG-Approval`, `AITL-TC-Approval`, `AITL-BOLT-READY-Approval`,
`AITL-ADR-Approval`, `AITL-SPEC-Approval`, `AITL-MEM-Approval`,
`AITL-BOLT-DONE-Approval`, `AITL-DISC/REV/AREV-*-Approval`). The identifiers name
the gates; the **record** — the manifest's `checkpoint_approvals[]` (its own
ADR) — states who actually signed and how (`human:<user>` or
`agent:<id>`/`model:<id>`). §0's precept is reframed from *"the human governs at
every checkpoint"* to **"human-by-default, agent-by-explicit-configuration."**

**History is not rewritten (G36).** Already-recorded v4.2 approvals keep their
`HITL-*` names as historical record; `AITL-*` is the vocabulary of the v5.0
**product** (the kit) and of artifacts created once the operating methodology is
v5.0. Artifacts created *now*, under the v4.2 operating methodology (ADR-006) —
**this ADR included** — correctly use `HITL-*`; that is not a contradiction, it
is the dogfooding split (we build v5.0 using v4.2). **G05 evolves with the
vocabulary:** the canonical set becomes `AITL-*`, and `HITL-*` joins H1–H6 as a
legacy prefix — scoped, not honored as canonical going forward (the same
treatment §3.4 gives G18/G24).

### 3.2 The safe-default invariant (non-negotiable)

With **no — or invalid — agent configuration**, a project behaves **byte-for-byte
like v4.2**: every checkpoint is a human approval. It must be **impossible** for a
project with absent or invalid configuration to reach an AI-signed approval. The
delegating path requires an explicit, present, valid configuration; absence
always resolves to human-only. This invariant is the whole contract — it is
enforced in tooling, never left to prompt prose.

### 3.3 Independence, layered (the core rule)

Built on ADR-007's actor unit:
1. **Floor (always): approver actor ≠ executor actor.** The actor that approves
   is never the actor that executed. This **generalizes the existing human
   handoff** ("incoming executor reviews") and G37 (Judge ≠ Challenger) to
   actors. Same actor approving its own work = never.
2. **Model hardening (high risk): approver.model ≠ executor.model.** At `high`,
   different agents must also run different models (shared-model blind spots
   matter more as stakes rise). At `low`/`medium`, model diversity is
   recommended, not required — so single-provider teams remain first-class.
3. **Human ceiling (top): `critical` + `regulatory` = human only.** A project's
   configuration may **tighten** this floor (more human), never loosen it.

### 3.4 Identity rules stay hard — scoped, never dissolved

G18/G24 are **scoped, not deleted**: *"the AI never approves"* becomes *"the AI
never approves **unless** the project has explicitly configured a virtual
approver for that checkpoint class **and** the independence rule (§3.3) holds"*.
The record **never fabricates a human** — a virtual approval is always
`agent:<id>` / `model:<id>`, never a human name. **G37** (AREV neutrality) and
the **handoff** rule are **excluded from any no-holder fallback** (the US-014
family): "no holder" may route a human role to another available human, but it
can never become a licence for self-approval. These identity rules are the one
place the opt-in superset does not reach.

### 3.5 Separation of duties — the Coordinator never signs

The Coordinator (ADR-007: the shipped orchestrator) **routes and records but
never signs a checkpoint**. If the router could also approve, every independence
check would collapse into "the Coordinator approved its own routing". Approver
agents are spawned **only by the Coordinator or invoked by a human — never from
an executor's subtree** (spawn topology), so an executor can never spawn "its
own" approver. (Native enforcement per platform: DISC-002 §5.2.)

### 3.6 Approver capability ceiling — approval integrity

AITL creates a threat HITL never had: **injection-forged approvals** (DISC-002
§5.4). An agent **acting as approver** runs at **capability tier T0** (at most T1
with pinned, trusted sources) — **no transactional MCPs, no write paths**.
Approving needs nothing external: the evidence (diff, tests, MEM, manifest) is in
the repo. Executor agents may be as capable as a project dares; **approval
integrity never depends on an executor's capability tier.** This is an invariant,
enforced by the agent's declared capabilities (ADR-007), not a suggestion.

### 3.7 The escalation floor (engine-enforced)

Regardless of configuration, these force a **human stop**, non-delegable:
gate red, turn-budget exhausted, a changes-requested loop, an ADR-class change,
or missing/contradictory evidence. The floor is engine-enforced, never left to
prompt prose (DISC-001 §5.1). A role's prompt may always escalate **above** the
floor (role-specific judgment); never below it.

### 3.8 Human-depth is per-project config above a fixed floor

This ADR fixes the **floor** (§3.2 safe default; §3.3 human ceiling for
critical/regulatory) and leaves the rest — which checkpoint classes may be
delegated to virtual approvers at low/medium/high — to **per-project
configuration**, declared in an explicit **per-project AITL-enable ADR**
(DISC-001 §5.6.3). Enabling virtual approvers is itself always a governed human
act; the methodology does not hardcode a single delegation table.

### 3.9 Scope — decided elsewhere

- *What an actor/agent is* → **ADR-007** (done).
- *The manifest record* (`checkpoint_approvals[]` replacing `hitl_approvals[]`,
  `schema_version 5.0`, G36 conversion) → **the manifest ADR**.
- *Implementation* — the §0/GUARDRAILS/charter rewrites, the **HITL→AITL rename
  sweep across the whole kit** (concept + every `HITL-<CODE>-Approval`
  identifier, governed by the ADR-005 phrase-family sweep discipline), the
  scoping of G05/G18/G24, the `agents/` registry, the roster, the Coordinator,
  the pilot → **USs/Bolts** (this ADR decides that it happens; the sweep executes
  it).
- *The conductor/engine* (MAF/Squads/squad) → a separate DISC (DISC-001 rec #5).

---

## 4. Consequences

**Positive:**
- v5.0's identity is defined without diluting HITL: it is the floor; AITL is a
  configurable layer above it. Every previous guarantee survives at zero config.
- Delegation is always explicit and governed (a per-project ADR names who may
  sign what) — accountability for *delegating* stays a human act.
- Independence generalizes rules the methodology already had (handoff, G37),
  so the change is conceptually small even though it is foundational.
- Approval integrity is structurally protected against the new injection threat.
- Enables the single-operator and squad models the maintainer is building toward.

**Trade-offs:**
- A governance layer (Coordinator) and per-project configuration are now
  required for the delegating path; the safe-default invariant must be enforced
  in tooling.
- `critical`/`regulatory` stay human even with AITL enabled — deliberate.

**This is the v5.0-defining decision.** The §0 precept change ("the human
governs" → "human-by-default, agent-by-explicit-configuration"), the
**HITL→AITL evolution in concept and in every checkpoint name**, and the scoping
of G05/G18/G24 are what make the release v5.0 (per ADR-006, the product line
bumps for a change of this magnitude; the manifest change reinforces it). The
rename touches the entire kit (core, GUARDRAILS, the four agents, templates,
READMEs, schemas) — a large but mechanical sweep, executed under the ADR-005
discipline (phrase-family over a fixed location set, allowlisting the legacy
`HITL-*` references that are historical or intentionally about the old term).

**Technical debt / follow-up:**
- The manifest schema (`checkpoint_approvals[]`) and its G36 conversion are the
  manifest ADR + a Bolt.
- Enforcement (the Coordinator, validators for the safe-default invariant and
  the approver ceiling) is downstream US/Bolt work.
- The pilot (DISC-002 rec #4) must include a **red-team AC**: attempt to forge an
  approval via injected content and prove the §3.6 ceiling holds.

---

## 5. Applicable NFRs

| NFR | Description | Threshold | How it is measured |
|-----|-------------|-----------|-------------------|
| `approval-integrity` | An AI-signed approval can occur only under explicit valid configuration, with the approver actor ≠ executor actor, and never via injected content | Zero AI-signed approvals under absent/invalid config; zero approver actors equal to the executor; approver-mode agents never above T1 | Safe-default invariant tests + independence lookup (roster) + the pilot red-team AC (§4); recorded per approval in `checkpoint_approvals[]` (manifest ADR) |

---

## 6. References

- [ADR-007](ADR-007-devflow-agent-identity-model.md) — the actor identity model
  this precept governs.
- [DISC-001](../discovery/DISC-001-aitl-and-subagent-orchestration.md) (approved)
  — the AITL precept, opt-in-superset framing (§5.6), escalation floor (§5.1).
- [DISC-002](../discovery/DISC-002-devflow-agents-architecture.md) (approved) —
  Coordinator-never-signs (§5.2), roster independence lookups (§5.3), the
  injection-forged-approval threat and approver ceiling (§5.4).
- [ADR-006](ADR-006-versioning-and-self-development-model.md) — why a change of
  this magnitude (and the manifest change) makes the product line v5.0.
- **Forthcoming:** the manifest ADR (`checkpoint_approvals[]`); the `agents/`
  registry US; the Claude Code pilot US.

---

## 7. HITL-ADR-Approval

> **HITL-ADR-Approval** (Avenga DevFlow §2.8, §3.0, §3.5). An ADR does not become
> `accepted` — and therefore governing — without the approval of an Architect /
> Tech Lead. This ADR is the source of truth for its own approval (recorded in
> the `review` frontmatter block). ADR approvals are never copied to the Bolt
> manifest.

| Field | Value |
|-------|-------|
| **Architect / Tech Lead** | eugenio.serrano |
| **Role** | architect / tech_lead |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-22T14:24:02-03:00` |
| **review.started_at** | `2026-08-22T14:33:30-03:00` |
| **review.decided_at** | `2026-08-22T14:33:30-03:00` |
| **Findings** | none — `acknowledged_without_comment: true` (see frontmatter) |
