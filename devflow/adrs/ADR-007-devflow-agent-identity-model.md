---
id: "ADR-007"
title: "The DevFlow Agent: a governed identity (model as an attribute), with authority in structured fields"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
status: "accepted"
decision_makers: ["architect", "tech_lead"]
sources:
  - "devflow/discovery/DISC-002-devflow-agents-architecture.md"
  - "devflow/discovery/DISC-001-aitl-and-subagent-orchestration.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
  - "devflow/adrs/ADR-006-versioning-and-self-development-model.md"
supersedes: []
conflicts_with: []
tags: ["devflow-agents", "aitl", "identity", "v5.0", "product-design"]
nfrs: []
waiver:
  gate: ""
  reason: ""
  owner: ""
  compensating_control: ""
  expires_at: ""
review_ready_at: "2026-08-22T14:21:09-03:00"
review: # HITL-ADR-Approval evidence — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "architect"}]
  started_at: "2026-08-22T14:22:57-03:00"
  decided_at: "2026-08-22T14:22:57-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Accepted. Establishes the v5.0 agent substrate grounded in DISC-002: a DevFlow Agent is a governed identity (id) with the model as a swappable attribute; the actor (human or agent) is the unit of identity generalizing the handoff rule; authority lives in structured fields (modes/approves/capabilities/escalation), never in charter prose — the structural defense against injection-forged authority; Coordinator (shipped) vs role agents (project-built). Scope is a clean substrate: approval governance deferred to ADR-008, the manifest record to its own ADR, and the folder/schema/generator to the registry US. Alternatives B (model-as-identity, rejected by the maintainer) and C (prose authority, a security hole) correctly discarded. Immutable from now on."
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs and section headings
  stay in English (the schema); prose follows content_language (en).
  `HITL-ADR-Approval` is never translated.

  ⚠️ This ADR is a DRAFT until an Architect / Tech Lead records
  HITL-ADR-Approval. A draft ADR cannot govern.

  ⚠️ SCOPE: this is the first ADR in the maintainer partition about the
  v5.0 PRODUCT's design (ADR-002/004/005/006 govern the repo's process). It
  decides WHAT a DevFlow Agent is. It is decided/operated under v4.2 (ADR-006)
  and its methodology-text implementation lands in the kit via USs/Bolts.
-->

# ADR-007 — The DevFlow Agent: a governed identity, with authority in structured fields

| Field          | Value |
|----------------|-------|
| **Status**     | **accepted** (immutable — a new decision requires a superseding ADR) |
| **Decision-makers** | Architect / Tech Lead (maintainer) |
| **Sources**    | DISC-002 (approved), DISC-001 (approved), ADR-004 (partition), ADR-006 (versioning) |
| **Supersedes** | None |
| **Conflicts with** | None — the substrate for the AITL precept ADR (ADR-008, forthcoming) |

---

## 1. Context

v5.0 introduces **DevFlow Agents**: named actors that can execute work and, when
a project enables it, occupy an approval checkpoint — humans and virtual (AI)
actors side by side (the AITL direction, DISC-001/DISC-002). Before AITL can
define *how approvals work* (its own ADR), the methodology needs to fix *what an
agent is*. This is the substrate.

Two facts from DISC-002 (approved) force the decision:

1. **The maintainer's model is "divide by DevFlow Agent, not by model."** A team
   is a squad of role agents (a shipped Coordinator + project-built functional
   analyst, architect, developer, QA…), each with its own prompt, tools and
   model — like human team members. Independence for approvals must be measured
   between **actors**, generalizing the existing human handoff rule ("the
   approver is a different person than the executor"), not between raw models.
2. **Authority expressed in prose is unenforceable and unsafe.** DISC-002 §5.4
   documents the injection-forged-approval threat: if an approver's authority
   lived only in its prompt text, a prompt-injection could grant itself signing
   power. Authority must live in fields a coordinator and a validator can read,
   not in the charter's narrative.

Without a written identity model, "DevFlow Agent" would drift — sometimes a
model, sometimes a prompt, sometimes a role — and the AITL independence rule
would have no stable unit to compare.

---

## 2. Alternatives considered

### Alternative A — Agent is a governed identity; model is an attribute; authority in structured fields (✅ Selected)

| Aspect | Detail |
|--------|--------|
| **Pros** | Independence generalizes the human handoff cleanly (actor ≠ actor). Two agents may share a model (single-provider teams work) yet remain distinct identities. Authority is **enumerable and enforceable** (read a field, not prose). The model is a swappable attribute. Directly supports the squad model (DISC-002 §5.3) and every platform's per-agent definition (DISC-002 §4.2). |
| **Cons** | Requires a definition contract + validation and a governance layer (the Coordinator) that reads the fields — both are downstream work. |

### Alternative B — Model is the identity

| Aspect | Detail |
|--------|--------|
| **Pros** | Simplest; nothing beyond the model id. |
| **Cons** | Two role agents on the same model would be "the same identity" — you could not have a developer-agent and a qa-agent on one model with distinct authority. Breaks the squad model and forces multi-provider setups. **Explicitly rejected by the maintainer** ("dividir por agentes, no por modelos"). |

### Alternative C — Agents are role prompts only (living data), authority implied by prose

| Aspect | Detail |
|--------|--------|
| **Pros** | Maximum agility; edit a file, no ceremony. |
| **Cons** | An approver's authority in prose is unenforceable and a security hole — a prompt (or an injection) can claim signing rights (DISC-002 §5.4). No stable unit for independence checks. |

---

## 3. Decision

**We adopt Alternative A.** For v5.0:

1. **A DevFlow Agent is a governed identity, not a model.** Its `id`
   (kebab-case, stable) is the identity used wherever the methodology compares
   actors (independence, handoff, audit). The **model is an attribute** the
   agent declares; two agents may run the same model and remain distinct
   identities. Renaming or re-prompting an agent does not create a new identity;
   only a new `id` does.

2. **The actor is the unit of identity — humans and DevFlow Agents are peers.**
   Everywhere the methodology today says "person" for identity purposes (the
   handoff "incoming executor reviews", "the approver is someone else"), v5.0
   reads **"actor"** = a human **or** a DevFlow Agent. *How* that unit is used
   to gate approvals is decided by the AITL precept ADR (ADR-008); this ADR only
   fixes that the actor — the DevFlow Agent — is that unit.

3. **Authority lives in structured, machine-readable fields — never in the
   charter prose.** Every DevFlow Agent declares at least:
   - `id` — the identity;
   - `role` — the archetype (coordinator · functional-analyst · architect ·
     developer · qa · reviewer · project-defined…);
   - `model` — its own declared model (constrained to the platform catalog);
   - `modes` — `executor` and/or `approver`;
   - `approves` — the checkpoint classes it may sign (**empty = may never
     sign**, regardless of what its prose says);
   - `capabilities` — its capability **tier** and explicit tool/MCP allowlist
     (tiers T0–T3 per DISC-002 §5.4; the *ceilings and enforcement* are AITL
     governance, ADR-008);
   - `escalation` — role-specific conditions under which it must defer.

   The charter **body is the agent's judgment** (who I am, what I check, how I
   decide, when I escalate) — it is **never its authority**. A coordinator or a
   validator determines what an agent may do by reading the fields, so an agent
   with `approves: []` cannot sign even if its prompt claims otherwise. This is
   the structural defense against injection-forged authority (DISC-002 §5.4).

4. **Two kinds of DevFlow Agent, by origin:**
   - **The Coordinator** — the single DevFlow Agent **shipped with the
     methodology** (the evolution of today's platform agent). It is the actor
     the human talks to; it routes work and spawns role agents as platform
     sub-agents, receiving control back via the spawn result (state = files,
     DISC-001). Its **approval constraints** (that it routes and records but
     never signs, and the spawn topology that keeps approvers out of an
     executor's subtree) are AITL governance and are decided in ADR-008; this
     ADR fixes only that the Coordinator **exists as the shipped DevFlow Agent**
     and is the orchestrator.
   - **Role agents** — **built per project** (the domain-aware functional
     analyst, architect, developer, QA, reviewer…), instantiated from kit-shipped
     charter templates. Their existence and domain knowledge are project
     artifacts, governed by the project's AITL-enable ADR (DISC-001 §5.6.3).

5. **This identity model is product design for v5.0.** Unlike ADR-002/004/005/006
   (process), ADR-007 shapes what the shipped methodology *is*. The **decision**
   is recorded here (root `devflow/adrs/`, under v4.2 per ADR-006); the
   **methodology-text and schema** that express it land in the kit via the
   registry US and the manifest ADR — not by this ADR.

**Out of scope (decided elsewhere), to keep this ADR a clean substrate:**
- *How approvals work* — independence rules (actor floor / model hardening /
  human ceiling), Coordinator-never-signs, approver capability ceiling,
  escalation floor, opt-in-superset + safe default → **AITL precept ADR
  (ADR-008)**.
- *The manifest record* of who approved → **manifest ADR** (`checkpoint_approvals[]`).
- *The implementation* — the `agents/` folder, the exact schema/field syntax,
  charter templates, the roster file, the wrapper generator + parity check →
  **the `agents/` registry US** (DISC-002 §5.5).

---

## 4. Consequences

**Positive:**
- The AITL precept ADR is unblocked: it has a stable unit ("actor" = DevFlow
  Agent) to define independence over.
- Authority is enumerable and enforceable, not prose — the structural basis for
  approval integrity (DISC-002 §5.4).
- The model becomes a swappable attribute recorded per agent, so both
  actor-level and model-level audits are possible later (feeds the manifest ADR).
- Single-provider teams remain first-class (distinct agents can share a model).
- Maps onto every target platform's native per-agent definition (DISC-002 §4.2).

**Trade-offs:**
- Introduces a definition contract that must be specified and validated (the
  registry US) and a governance layer that reads it (the Coordinator, ADR-008).
- Splits "agent" into product (Coordinator + templates + schema) and project
  (instantiated role agents + roster) — a boundary the registry US must make
  explicit.

**Technical debt / follow-up:**
- Exact field syntax, folder layout (`agents/`, G30-sanctioned), charter
  templates, roster schema and the wrapper generator are **the registry US**,
  not this ADR.
- Per-platform contract caveats (Codex invocation bugs #14579/#15250, Copilot
  env-dependent fields) are re-verified at implementation (DISC-002 §7).

---

## 5. Applicable NFRs

None defined here. Capability tiers touch security, but the governing rules
(approver ceiling, enforcement) are set by the AITL precept ADR (ADR-008).

---

## 6. References

- [DISC-002](../discovery/DISC-002-devflow-agents-architecture.md) (approved) —
  the agent definition contract (§5.1), the Coordinator (§5.2), the roster
  (§5.3), capability tiers and the injection-forged-approval threat (§5.4),
  product-vs-project (§5.5), platform matrix (§4.2).
- [DISC-001](../discovery/DISC-001-aitl-and-subagent-orchestration.md) (approved)
  — the AITL direction and platform sub-agent mechanics.
- [ADR-004](ADR-004-repository-partition-v2.md) — product (kit) vs governance
  (root) partition, which the product-vs-project split mirrors.
- [ADR-006](ADR-006-versioning-and-self-development-model.md) — v5.0 built under
  the v4.2 operating methodology.
- **Forthcoming:** ADR-008 (AITL precept — approval governance over this
  identity model) and the manifest ADR (`checkpoint_approvals[]`).

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
| **review_ready_at** | `2026-08-22T14:21:09-03:00` |
| **review.started_at** | `2026-08-22T14:22:57-03:00` |
| **review.decided_at** | `2026-08-22T14:22:57-03:00` |
| **Findings** | none — `acknowledged_without_comment: true` (see frontmatter) |
