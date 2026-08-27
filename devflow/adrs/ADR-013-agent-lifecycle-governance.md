---
id: "ADR-013"
title: "Agent lifecycle governance — install/create/delete of DevFlow Agents is operational config (executor = living data, approver = governed), scoping G07"
date: "2026-08-23"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
status: "accepted" # draft | accepted | rejected | deprecated | superseded
decision_makers: ["architect", "tech_lead"]
sources:
  - "devflow/adrs/ADR-007-devflow-agent-identity-model.md"
  - "devflow/adrs/ADR-014-actors-roster-is-the-enablement.md"
  - "devflow/discovery/DISC-001-aitl-and-subagent-orchestration.md"
  - "devflow/discovery/DISC-002-devflow-agents-architecture.md"
supersedes: []
conflicts_with: [] # complements ADR-007 (identity) + ADR-014 (precept + roster enablement); scopes G07 (does not delete it)
tags: ["devflow-agents", "lifecycle", "governance", "g07-scoping", "v5.1", "product-design"]
nfrs: []
waiver: # Only for gate-override ADRs (§3.6)
  gate: ""
  reason: ""
  owner: ""
  compensating_control: ""
  expires_at: ""
review_ready_at: "2026-08-24T00:40:35-03:00" # When this version is submitted for review (§3.0)
review: # AITL-ADR-Approval evidence — decision dictated in conversation ("Aprobado, a darle GAS", over the reviewed queue) and transcribed by the agent (§3.0)
  decision: "approved" # approved | rejected
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "architect"
      model: null
  started_at: "2026-08-24T00:40:35-03:00"
  decided_at: "2026-08-24T00:40:35-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved as Architect after an independent cross-model final pass (PASS) verified the revision on disk: §3.3 approver leg now cites ADR-014 §3.8 (the human's roster configuration act — an agent never enables its own approval), §3.4 safe default cites ADR-014 §3.2, and §3.9 carries the examples–squad ship model (agents/examples/ read-only references + agents/squad/ live agents created by the Coordinator; the roster references squad/ only; no pre-built role wrappers ship — proven by the maintainer partition, which runs exactly this way). G07 scoping bounds (§3.5) and Coordinator locus (§3.6) unchanged. Base for US-025 and the BOLT-004/BOLT-005 kit work."
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs, and section
  headings (##) stay in English (the schema). ADR titles and prose go in
  the project's content_language (en). `AITL-ADR-Approval` is never
  translated.

  ⚠️ This ADR is a DRAFT until an Architect / Tech Lead records
  AITL-ADR-Approval. A draft ADR cannot govern.

  ⚠️ SCOPE: product design for v5.1. It DECIDES how the agent lifecycle is
  governed (scoping G07). Its methodology-text implementation (the GUARDRAILS
  scoping + the MainAgent capability) lands in the kit via US-025. Decided
  under the operating methodology; the text ships in the kit (dogfooding
  split, ADR-006).
-->

# ADR-013 — Agent lifecycle governance

| Field          | Value |
|----------------|-------|
| **Status**     | **accepted** (immutable — a new decision requires a superseding ADR) |
| **Decision-makers** | Architect / Tech Lead |
| **Sources**    | ADR-007 (identity), ADR-014 (precept + roster enablement), DISC-001/002 (approved) |
| **Supersedes** | None |
| **Conflicts with** | None — complements ADR-007 and ADR-014; scopes G07 (does not delete it) |

---

## 1. Context

The DevFlow Agents family — US-022 (the Actor), US-023 (the definition contract +
the agent family — definitions/templates) and US-024 (the unified actors roster) — defines *what*
agents, actors and the roster are. To **operate** that family, the **Coordinator**
(the AvengaDevFlow MainAgent, one per tool) must **install, create and delete**
agents: project-built role agents, per adopting team.

Read literally, **G07** ("no code change without an approved Bolt") would demand a
Bolt for **every** agent an adopter creates or installs — unworkable, and wrong in
kind: an agent's canonical definition and its installed platform wrapper are
**operational configuration** — the same class as the roster (`actors/`) and the
project prompts (`prompts/`), which the methodology already treats as living data
outside G07 (§5.12). ADR-014 already fixed *how approvals work* (the precept carried
from ADR-008 + the roster enablement: no AI-signed approval without a schema-valid
roster grant). What is undecided is
*how the agent lifecycle itself is governed* — without either freezing it behind
Bolt-per-agent, or opening a loophole that lets an approver be enabled silently.

Without a written rule, "creating an agent" would mean whatever each project
assumed: some would gate every agent behind a Bolt (no operability), others would
let agents — including approvers — appear with no governance (unsafe). The lifecycle
must be one governed, bounded statement.

---

## 2. Alternatives considered

### Alternative A — Lifecycle is operational config: executor = living data, approver = governed (✅ Selected)

| Aspect | Detail |
|--------|--------|
| **Pros** | No Bolt-per-agent friction; agents are operable like the roster/prompts; approval integrity is preserved (the approver path stays governed); consistent with the existing living-data model (§5.12). |
| **Cons** | Scopes a **blocking** guardrail (G07) — it must be tightly bounded so it never becomes a licence for arbitrary product-code changes. |

### Alternative B — Every install/create/delete is a Bolt (G07 literal)

| Aspect | Detail |
|--------|--------|
| **Pros** | No new rule; G07 applies unchanged. |
| **Cons** | Unworkable friction (a Bolt per agent); miscategorizes operational config as product code. Rejected. |

### Alternative C — No governance (free lifecycle)

| Aspect | Detail |
|--------|--------|
| **Pros** | Maximum agility. |
| **Cons** | Dissolves the safe default — an approver could be enabled with no governed act. Rejected: it is the failure mode this ADR exists to prevent. |

---

## 3. Decision

**We adopt Alternative A.** For v5.1:

1. **Agent lifecycle (install / create / delete) is an operational/config act — not a
   "code change" under G07.** It is **living data** of the same class as roster updates
   and prompts (§5.12). **G07 is scoped accordingly.**

2. **Executor agents** — create / install / delete = **living data**: no Bolt, no
   approval (the same treatment as a roster member joining or leaving).

3. **Approver agents** — creating one, or changing its authority (`approves` or its
   charter/authority fields), is **governed**: it happens only through the **human's
   roster configuration act** (ADR-014 §3.8 — a human writes or merges the actor's
   authority fields; the lifecycle may scaffold an actor as an **executor-only
   draft**, but an agent never enables its own approval). Installing the wrapper of
   an **already-enabled** approver is **execution of that governed act**, never a
   new approval.

4. **The safe default is intact (ADR-014 §3.2).** Installing an agent **never enables
   approval** by itself; with absent or invalid configuration, no AI-signed approval is
   possible. The lifecycle never bypasses AITL.

5. **Bounds (non-negotiable).** The lifecycle operates **only within the
   definition/roster system** (`agents/` + `actors/`); it **never edits the kit's
   shipped templates in place**; it never writes outside that system; and a change to an
   approver's authority fields is **itself the human's configuration act** (ADR-014
   §3.8) — an agent never performs it. These bounds are
   what keep the G07 scoping from becoming a loophole.

6. **Locus.** The capability belongs to the **Coordinator** — the AvengaDevFlow
   MainAgent, one per tool (Claude Code, GitHub Copilot, OpenCode, Codex). **Role
   agents do not carry it.**

7. **This scopes G07 — exactly as ADR-008 scoped G18/G24.** The GUARDRAILS text that
   expresses the scoping **ships in the kit via a Bolt that cites this ADR**. G07 may
   **not** be scoped in GUARDRAILS without this approved ADR (the G21 principle:
   guardrail changes require an approved ADR). An `AITL-*-Approval` still governs every
   *approver* enablement; this ADR governs only the *config lifecycle* around it.

8. **This is product design (maintainer partition).** The decision is recorded here
   (root `devflow/adrs/`); the methodology text (the GUARDRAILS scoping) and the
   operational capability (the MainAgent lifecycle) land in the **kit** via **US-025**.

9. **Ship model.** Within the agent system, the kit ships **only the four MainAgents**
   (one per tool, each named AvengaDevFlow) plus the **example role definitions**
   (`agents/examples/` — read-only references: copied, never referenced by the roster
   and never edited in place), the **templates** (`agents/TEMPLATE-new-role/`) and the
   **per-platform install mapping** (the roster family `actors/` and the methodology
   docs ship as their own families). The project's **live agents** are created by the
   Coordinator into **`agents/squad/`** (living data, points 1–2) — scaffolded from
   the examples/templates; the roster's `definition:` pointers reference `squad/`,
   never `examples/`. It ships **no pre-built role wrappers** — every role wrapper is
   **projected from `squad/` and installed into the adopting project by the
   Coordinator** (a governed operational act, points 1–6), never delivered in the
   kit. The four MainAgents live at their platform's native entry
   point (`CLAUDE.md` at the kit root, `SKILL.md` under `.agents/skills/`, and the
   AvengaDevFlow wrapper in `.github/agents/` and `.opencode/agents/`); the
   role-wrapper folders (`.claude/agents/`, `.codex/agents/`) ship empty or absent
   (US-023's "wrappers committed to the kit" wording is superseded by this point —
   the G15 re-revision of US-023 is part of the US-025 batch).

---

## 4. Consequences

**Positive:**
- Adopting teams operate their squad — create, install and delete agents — without
  Bolt-per-agent friction.
- The executor/approver split preserves approval integrity: the approver path stays
  behind the human's roster configuration act (ADR-014), while executor management is
  frictionless.
- Consistent with the living-data model already in the methodology (roster, prompts).

**Trade-offs:**
- G07 is **scoped** — a bounded exception. Its safety rests entirely on the §3 bounds
  (definition/roster system only; never the shipped templates; approver = governed).

**Technical debt / follow-up:**
- **US-025** implements the operational capability (the MainAgent lifecycle) and carries
  the GUARDRAILS-scoping Bolt that cites this ADR.
- The **validator** (US-012 family) consumes the agent/roster schemas.
- **US-017** (tooling distribution) ships the compiled generator as an **optional
  acceleration** — the deterministic install is **docs-primary** (the shipped
  per-platform mapping in `agents/`), with the N×4 parity check as the safety net
  and the compiled generator never a requirement of the primary path (US-025 AC-8).

---

## 5. Applicable NFRs

None new. Approval integrity is governed by ADR-014 (carrying ADR-008's precept); this
ADR governs the **config lifecycle** around it (what is living data vs a governed act),
not the approval itself.

---

## 6. References

- [ADR-007](ADR-007-devflow-agent-identity-model.md) — the agent identity model.
- [ADR-014](ADR-014-actors-roster-is-the-enablement.md) — the AITL precept (carried
  from the superseded ADR-008) + the roster enablement (§3.8) that governs approver
  enablement.
- [DISC-001](../discovery/DISC-001-aitl-and-subagent-orchestration.md),
  [DISC-002](../discovery/DISC-002-devflow-agents-architecture.md) (approved).
- US-022 / US-023 / US-024 (the DevFlow Agents family); **US-025** (the operational
  capability — draft; cites this ADR).
- GUARDRAILS **G07** (scoped here), **G21** (guardrail changes require an ADR), §5.12
  (living data).

---

## 7. AITL-ADR-Approval

> **AITL-ADR-Approval** (Avenga DevFlow §2.8, §3.0, §3.5). An ADR does not become
> `accepted` — and therefore governing — without the approval of an Architect / Tech
> Lead. This ADR is the source of truth for its own approval (recorded in the `review`
> frontmatter block). Only once `accepted` may the GUARDRAILS-scoping Bolt (US-025)
> cite it and scope G07. ADR approvals are never copied to the Bolt manifest.

| Field | Value |
|-------|-------|
| **Architect / Tech Lead** | `human:eugenio.serrano` |
| **Role** | architect |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-24T00:40:35-03:00` |
| **review.started_at** | `2026-08-24T00:40:35-03:00` |
| **review.decided_at** | `2026-08-24T00:40:35-03:00` |
| **Findings** | none blocking — the cross-model final pass verified §3.3/§3.4 citing ADR-014 and the §3.9 examples–squad ship model on disk (full reason in the frontmatter `review:` block) |
