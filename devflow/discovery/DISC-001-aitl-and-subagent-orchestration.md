---
id: "DISC-001"
title: "AvengaDevFlow Agents — AITL approval precept, declarative agents/ registry and platform-native sub-agent orchestration"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved" # draft | approved | deprecated
category: "technology"
research_question: "How can AvengaDevFlow evolve into an agent-orchestrated development flow — an AITL (Agent-in-the-Loop) approval precept, a declarative agents/ registry, and platform-native sub-agent spawning across OpenCode, Copilot, Claude Code and Codex — while preserving the governance guarantees (human stops, identity separation, model neutrality)?"
sources:
  - "https://opencode.ai/docs/keybinds/"
  - "https://code.claude.com/docs/en/sub-agents"
  - "https://code.claude.com/docs/en/agent-sdk/hooks"
  - "https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-ide?tool=vscode"
  - "https://docs.github.com/en/copilot/reference/hooks-reference"
  - "https://github.com/openai/codex/blob/main/codex-rs/core/src/config/agent_roles.rs"
  - "https://github.com/openai/codex/blob/main/codex-rs/core/src/tools/handlers/multi_agents_v2/spawn.rs"
  - "https://github.com/openai/codex/blob/main/codex-rs/rollout-trace/README.md"
  - "https://github.com/microsoft/agent-framework"
  - "https://github.com/braintrustdata/squads"
  - "https://github.com/bradygaster/squad"
tags: ["agents", "aitl", "orchestration", "subagents", "hitl", "platforms", "methodology-evolution"]
review_ready_at: "2026-08-22T01:47:18-03:00"
review: # HITL-DISC-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "research domain lead"}]
  started_at: "2026-08-22T02:01:23-03:00"
  decided_at: "2026-08-22T02:01:23-03:00"
  findings: []
  acknowledged_without_comment: true # must be true when findings is empty (§3.0)
  acknowledgment_reason: "Approved as governed input: the research question is answered with adequate, source-verified evidence (platform sub-agent mechanics against official docs, §5.3/§6), limits and assumptions are explicit (§7), and the conclusions are reliable enough to guide the v5.0 backlog. The opt-in-superset framing (§5.6) settles the alignment question — HITL-pure remains the zero-config default. Approval makes the conclusions citable; every downstream US/ADR/Bolt keeps its own lifecycle, and the foundational AITL precept is a separate v5.0 ADR decision, not authorized here."
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs, and section
  headings (##) stay in English (the schema). All prose — findings,
  observations, recommendations — goes in the project's content_language
  (declared in devflow/LANGUAGE).

  ⚠️ HITL-DISC-Approval (§2.13): this Discovery remains DRAFT until a
  qualified human records HITL-DISC-Approval. Until then, its conclusions
  cannot be used as governed input. Approval does not approve any
  downstream artifact. Executable spike/prototype code requires an
  approved non-functional Bolt under US-000 first.
-->

# DISC-001 — AvengaDevFlow Agents: AITL approvals, agents/ registry and platform-native sub-agent orchestration

| Field               | Value |
|---------------------|-------|
| **Category**        | technology |
| **Status**          | approved (HITL-DISC-Approval 2026-08-22) |
| **Research question** | How can AvengaDevFlow evolve into an agent-orchestrated flow — AITL approvals, a declarative `agents/` registry and platform-native sub-agents — while preserving governance guarantees? |
| **Date**            | 2026-08-22 |
| **Author**          | eugenio.serrano |
| **Sources**         | Official platform docs + framework repos (see §9) |

---

## 1. Research question

This Discovery consolidates a design exploration conducted across several
brainstorming sessions: the stakeholder wants a new layer — "AvengaDevFlow
Agents" — that minimizes human intervention to its minimum expression while
keeping the HITL stops as a capability. The material unknown being reduced:
**(a)** what the AITL (Agent-in-the-Loop) precept means as a methodology
change, **(b)** how a declarative `agents/` registry maps to the four platform
agent systems (OpenCode, GitHub Copilot, Claude Code, OpenAI Codex), and
**(c)** which mechanisms each platform natively offers for sub-agent
spawning, control return and governance — so the future US/ADR/Bolt family
can be scoped on verified facts instead of assumptions.

It is **not** a decision to implement anything: conclusions stay draft until
`HITL-DISC-Approval` and every downstream artifact follows its own lifecycle.

---

## 2. Scope

**In scope:**
- The AITL approval precept: checkpoint pauses resolved by a human **or** a
  virtual agent; `checkpoint_approvals[]` manifest shape; the
  risk-based "human depth" table; the independence rule; the escalation
  floor/ceiling model.
- The declarative `agents/` registry: canonical role prompts as single
  source + platform wrappers, roster semantics.
- Platform-native sub-agent mechanics (verified against official docs):
  OpenCode, GitHub Copilot, Claude Code, OpenAI Codex — file locations,
  spawn tools, control-return, model override, spawn restrictions,
  isolation, audit hooks, lifecycle control.
- Engine-level orchestration candidates: Microsoft Agent Framework,
  Braintrust Squads, Brady Gaster's Squad.
- Governance constraints that must survive: G18/G24, G37, the handoff
  identity rule, G25, G30/G31 path boundaries, §5.16 migration path,
  US-014/US-001 role-availability family.

**Out of scope:**
- Implementation code, prototypes or kit changes (need an approved Bolt).
- Deciding the AITL policy itself (that is an ADR/US-014-family decision).
- The AREV-001/AREV-002 confirmed findings (governed input elsewhere; only
  referenced).
- Manifest schema versioning decision (flagged, not resolved).

---

## 3. Executive summary

The stakeholder's vision is technically feasible on today's tooling: all
four target platforms (OpenCode, Copilot, Claude Code, Codex) already ship
**native sub-agent mechanisms** — per-role files in platform folders,
programmatic spawn tools with automatic control return, and (in Claude Code
and Codex) per-spawn model override that makes the AITL independence rule
native. The design that emerged has three pillars: **(1)** the AITL precept
— every checkpoint stays a pause, but the loop can be occupied by a human or
a virtual agent, recorded in a `checkpoint_approvals[]` array with a
`mode: human | virtual` discriminator; **(2)** a declarative `agents/`
folder as the single source of role prompts, with thin per-platform wrappers
generated and parity-checked like the four main agents; **(3)** the
escalation model — a deterministic floor (gates, budgets, risk) enforced by
the engine and a role-specific ceiling (judgment calls) expressed in each
agent's prompt. The critical boundary is the **independence rule**: an
approving agent must never be the executing agent (model ≠ executor),
generalizing G37 — otherwise AITL degenerates into universal self-approval.
Crucially, AITL is designed as an **opt-in superset, not a replacement**: with
no agents configured a project behaves **byte-for-byte like v4.2 HITL**
(human-only), so the current guarantee is preserved as the zero-config default;
virtual approvers occupy the loop **only** where a project explicitly enables
them, configurable per project type (§5.6).

---

## 4. Inventory / Mapping

| Concept | Design element | Notes |
|---------|----------------|-------|
| AITL precept | Checkpoint = decision pause; occupant = human or virtual agent | HITL stays as a capability, not a universal obligation |
| `checkpoint_approvals[]` | `{checkpoint, mode: human\|virtual, decided_by, decided_at, decision, evidence}` | Replaces/extends `hitl_approvals[]`; append-only; `decided_by: human:<user>` or `model:<id>` (G37 precedent) |
| Human depth by risk | low/medium → AITL OK; high → AITL + sampling; critical → HITL | Config table, not code |
| Independence rule | Approver model ≠ executor model | Generalization of G37; the one non-negotiable constraint |
| Escalation floor | gate red, turn-budget, risk critical, changes-requested loop, ADR-class change, missing evidence | Engine-enforced, never prompt-only |
| Escalation ceiling | "uncertainty too high", ambiguous ACs, role-specific judgment | Lives in each role prompt; always allowed above the floor |
| Consultation vs approval | `escalation:` event (guidance) vs `checkpoint_approvals[]` entry (decision) | Two different records, two metrics |
| `agents/` registry | Canonical role prompts (single source) + roster | `agents/roles/<role>/prompt.md` + `roster.yaml` |
| Platform wrappers | Generated per platform from the canonical prompt | Pre-built in the kit, parity-checked |
| Control return | Automatic via spawn tool result; manual via agent picker | Two mechanisms, never mixed in the automated flow |
| State = files | Sub-agents persist to repo; parent reads from disk | No in-memory handoff needed |
| Output contract | Structured final payload `{status, artifact, evidence, reason}` | Enforced by prompt (OpenCode) or hook (Copilot `subagentStop`/`modifiedResponse`) |
| Engine candidates | MAF, Braintrust Squads, bradygaster Squad | See §5.4 |

---

## 5. Detailed findings

### 5.1 The AITL approval precept

**Current state:** every checkpoint is `HITL-<CODE>-Approval` — human-only,
100% coverage per Bolt type, G18/G24 forbid any AI-delegated approval.

**Proposed precept:** every checkpoint becomes an **AITL pause** — the flow
stops identically, but the decision-maker is resolved from a roster of
available actors (humans and virtual agents). The checkpoint identifiers may
stay `HITL-<CODE>-Approval` (names of the gates) while the *entry* records
who actually signed:

```json
"checkpoint_approvals": [
  {
    "checkpoint": "MEM-Approval",
    "mode": "virtual",
    "decided_by": "deepseek/deepseek-v4-flash",
    "decided_at": "2026-08-22T01:47:18-03:00",
    "decision": "approved",
    "evidence": "diff + tests + manifest"
  }
]
```

**The independence rule (non-negotiable):** the virtual approver must be a
**different agent (model ≠ executor)** than the one that executed the work,
or the pause becomes a rubber stamp. This generalizes G37 (Judge ≠
Challenger) and the handoff rule (incoming executor reviews). The identity
rules G18/G24/G37 and the handoff are **explicitly excluded** from any
no-holder fallback — otherwise "no holder" becomes a universal self-approval
loophole.

**Human depth by risk (the knob):**

| Risk | MEM | BOLT-READY | SPEC | Approver |
|------|-----|------------|------|----------|
| low/medium | AITL (model ≠) | AITL | AITL | roster |
| high | AITL + human sampling | HITL | AITL (model ≠) | roster + audit |
| critical | HITL | HITL | HITL | human |
| Uncertainty / gate red / loop | forced HITL stop | — | — | escalation |

**Two pause types (never mixed):**
1. **Consultation** — the agent asks for guidance ("how do I continue?") →
   recorded as an `escalation:` event; the flow resumes with the answer.
2. **Approval** — a checkpoint decision → recorded as a
   `checkpoint_approvals[]` entry with `mode`; the flow resumes only when
   decided.

**Escalation floor vs ceiling:** minimum triggers (gate red, turn-budget,
critical risk, changes-requested loops, ADR-class change, missing evidence)
are **engine-enforced** — never left to prompt prose ("prompt-only
orchestration may be ignored" — Squad's stated rationale). Role-specific
judgment ("uncertainty too high", ambiguous ACs) lives in **each role's
prompt** — the agent may always escalate above the floor, never below it.

### 5.2 The declarative `agents/` registry

Layout proposal (single source + generated wrappers, same philosophy as the
four main agents):

```
distribution-kit/devflow/agents/
├── roles/                                  ← THE SOURCE (canonical prompts, governed)
│   ├── functional-analyst/prompt.md
│   ├── architect/prompt.md
│   ├── dev-validator/prompt.md
│   ├── qa/prompt.md
│   ├── reviewer/prompt.md
│   ├── guardrail/prompt.md
│   └── challenger/ · defender/ · judge/    ← AREV roles (model constraint: G37)
└── roster.yaml                             ← availability + fallbacks

distribution-kit/.opencode/agents/<role>.md            (wrappers: frontmatter + prompt)
distribution-kit/.claude/agents/<role>.md
distribution-kit/.github/agents/<role>.agent.md
distribution-kit/.agents/…                            (Codex: TOML role files)
```

- The human edits **one file** (`agents/roles/<role>/prompt.md`); a
  generator in `tools/` produces the four wrappers; results are **committed
  into the kit** (adopters copy wholesale, no runtime generation); a parity
  check (extension of the 4-agent diff: N roles × 4 platforms) prevents
  drift — the AREV-001 F-01 failure mode made mechanical.
- The roster **is** the team-description problem solved: it lists humans and
  virtual agents together, so the role-availability blockers of AREV-001/
  AREV-002 (US-014 family) resolve by roster lookup instead of hard gates.
- Terminology: **role** = persistent archetype (versioned product in the
  kit); **instance** = ephemeral spawn per step; **sub-agent** = nested
  instance (e.g. dev-validator spawning test-runner).
- Open design point: are role prompts product (Bolt+SPEC changes) or living
  data like `prompts/`? Prompts that approve define governance behavior —
  leaning product.

### 5.3 Platform-native sub-agent mechanics (verified against official docs)

| Capability | OpenCode | GitHub Copilot | Claude Code | OpenAI Codex |
|---|---|---|---|---|
| Role files | `.opencode/agents/*.md` | `.github/agents/*.agent.md` (or `~/.copilot/agents/`) | `.claude/agents/*.md` | `agents/*.toml` (recursive; legacy `.md` + migration module) |
| Spawn tool | `task` + `subagent_type` | `#runSubagent` / direct naming / automatic delegation | `Agent` (alias `Task`) tool | `spawn_agent` |
| Control return | automatic tool result | automatic to main chat session (hooks: `agentStop`/`subagentStop`) | automatic; result includes `usage` (tokens), `agentId` | notification via `agent_result` edge; explicit `close_agent` |
| Model override per spawn | no (config-level) | not documented | **yes** (sonnet/opus/haiku/fable) | **yes** (`model`, `reasoning_effort`, `service_tier`) |
| Spawn restriction | no native | tools per agent (SDK) | **`Agent(...)` allowlist in frontmatter** | no native (parent instruction; inheritance = environments + exec_policy only) |
| Isolation | no | no | **`isolation: worktree/remote`** | `sandbox_mode` per role file |
| Lifecycle control | spawn → result | spawn → result | spawn → result (+ resume via SDK) | **spawn / followup_task / send_message / wait_agent / close_agent** |
| Audit hooks | no | `agentStop`/`subagentStop` (+ `modifiedResponse`) | `SubagentStop` hook (agent_id, transcript path) | — |

**Manual access (human):** OpenCode — Tab cycles agents, `ctrl+x` is the
**leader key**, `ctrl+x`→`a` opens the agent list, `up` returns to the
parent session (`session_parent`); Copilot — agent picker in chat; Claude
Code — agent picker in interactive mode; Codex — agent selection in TUI.
The automated AITL flow uses the **spawn tools only** — keybinds/pickers are
human access, never part of the flow.

**Control-return principle:** spawn is synchronous from the parent's
perspective — the tool call returns the sub-agent's final message. Manual
switching (Tab/picker) keeps the same thread and returns control only when
the human switches back; the automated flow must not depend on it.

**Output-contract enforcement:** Copilot's `subagentStop` hook with
`modifiedResponse` can shape/replace the returned payload — the strongest
native enforcement point found. Claude Code returns `usage` stats per spawn
— free audit data for manifest `runs[]`.

### 5.4 Engine-level orchestration candidates

| Engine | Native fit | For DevFlow |
|---|---|---|
| **Microsoft Agent Framework** (Python/.NET) | SequentialOrchestration, HandoffBuilder, GroupChat + selection_func, ConcurrentBuilder, ContextMiddleware, session propagation, spawner | The E2E state machine (flow → checkpoints → AREV debate → parallel gates); middleware injects the normative text (anti-drift); ASP.NET hosting for the conductor |
| **Braintrust Squads** | Dynamic sub-agent spawning, sessions, HITL primitives | Spawning per V-Bounce; sessions per artifact |
| **bradygaster/squad** (Copilot runtime) | `defineSquad` with agents + routing rules **compiled to typed functions**; CostTracker; HookPipeline (allowedWritePaths, PII scrub, maxAskUserPerSession) | The declarative team + deterministic routing model; cost governance; write-path enforcement mirroring G30/G31 |

All three share the pattern: **declarative role definitions + deterministic
routing + tool-call control return**. The platforms already provide the
runtime; the engine layer adds the DevFlow-specific gobernance around the
spawn (roster resolution, output contract, AITL recording, escalation
floor).

### 5.5 Governance constraints that must survive

- **G18/G24** — no fabricated human decisions: a virtual approver records
  `decided_by: model:<id>`, never a human name. The AITL change modifies the
  *precept* (who may occupy the loop) without weakening the *record*.
- **G37** — AREV Judge neutrality: with sub-agents, the spawner must fail
  fast when no third model exists (AREV-002 F-02 trap — resolved at
  initiation, not at the Verdict).
- **G25** — AREV phases stay sequential; sub-agent debate phases record
  their own models per phase.
- **G30/G31** — sub-agent write permissions mirror the canonical folder
  structure (`input/` read-only, `_archive/` off-limits).
- **§5.16** — kit-only changes; the root `devflow/` receives the AITL
  precept at the next release migration.
- **US-014/US-001** — the roster (`agents/roster.yaml` + humans) is the
  natural implementation of the role-availability policy family.
- **L4 orchestration** — sequencing several approved Bolts with an engine
  requires an approved ADR (§3.3, W15).

### 5.6 AITL as an opt-in superset — HITL-pure is the zero-config default

The precept is **additive, not a replacement**. AITL is a superset of the
current model, resolved by configuration, so a v5.0 upgrade loses nothing:

- **Zero agents configured → pure HITL.** A project that configures no virtual
  agents behaves **byte-for-byte like v4.2**: every checkpoint is a human
  approval (`decided_by: human:<user>`). The existing HITL guarantee is the
  **default floor**, not a feature to switch on.
- **Configure virtual agents → they occupy the loop** only at the checkpoint
  classes the project enables, always under the independence rule and the
  human-depth-by-risk table (§5.1).
- **Configurable per project type.** A `regulatory`/high-assurance project can
  stay pure HITL; an internal-tooling project may delegate low/medium
  approvals. The "human depth by risk" table is the per-project knob.

**Design invariants that keep the superset safe (non-negotiable):**

1. **The safe default is inviolable.** It must be *impossible* for a project
   with no — or invalid — agent configuration to reach an AI-signed approval.
   The delegating path requires an explicit, present configuration; absence of
   config always resolves to human-only. This invariant is the whole contract.
2. **G18/G24 become scoped, not deleted.** "The AI never approves" holds
   **unless** the project has explicitly configured a virtual approver for that
   checkpoint class **and** the independence rule (model ≠ executor) holds. The
   record never fabricates a human — a virtual approval is always
   `decided_by: model:<id>`.
3. **Enabling AITL is itself a governed decision.** A project's choice to allow
   virtual approvers (which checkpoints, which risk classes) is recorded as a
   **per-project ADR**, never a silent flag — so the accountability for
   *delegating* remains an explicit human act.
4. **Human accountability is retained where it matters.** `critical` risk, the
   `regulatory` service class and UAT/Unit sign-off default to human-only even
   when AITL is enabled; a project's config may tighten this floor, never
   loosen it below it.
5. **Independence ≥ model.** Where a virtual approver is used, consider
   requiring a **different provider**, not only a different model — same-vendor
   models share blind spots, a weaker independence than a human reviewer
   provides.

**Why this matters for alignment.** Framed this way, AITL does not change the
methodology's identity — it **extends** it. HITL is not diluted; it is the
floor, and AITL is a configurable layer above it. The foundational precept
change (§0 "the human is the governor", G18/G24) is therefore a *scoping* of the
rules to "human-by-default, agent-by-explicit-configuration", to be decided in a
**top-level foundational ADR** (candidate for the v5.0 version bump) — **not**
folded into the US-014 role-availability family. These are orthogonal problems:
US-014/US-001 govern the *availability of a human role*; AITL governs the
*nature of the approver*. The roster (§5.2) is where they meet, but the opt-in
superset is the AITL decision, not the availability fix.

---

## 6. Experiments performed (if any)

No executable experiments were run (read-only investigation). Documentation
verification was performed against official sources:

| Verification | What was checked | Result |
|--------------|------------------|--------|
| OpenCode keybinds (official docs) | `ctrl+x` semantics, agent list, sub-agent session navigation | `ctrl+x` = leader key; `<leader>a` = agent_list; Tab = cycle; `up` = session_parent; child navigation right/left/down |
| Codex multi-agent sources | role file format, spawn lifecycle, inheritance | TOML roles with full config override; spawn/followup/send/wait/close; inheritance = environments + exec_policy only |
| Claude Code docs | sub-agent files, Agent tool, hooks, SDK | `Agent(...)` allowlist; model override; SubagentStop hook; usage in result; resume via SDK |
| Copilot docs | sub-agents, hooks, SDK | `#runSubagent`, automatic delegation, `agentStop`/`subagentStop`, `customAgents[]` in SDK |
| Context7 (MAF, Squads, Squad) | orchestration primitives | Patterns mapped in §5.4 |

---

## 7. Assumptions and limits

| # | Assumption / Limit | Severity | Impact |
|---|--------------------|----------|--------|
| 1 | Platform APIs evolve (Codex multi-agent is V2 with feature flags; Copilot agent-to-agent varies by release) | high | Each platform wrapper must be re-verified against current docs at implementation time (Context7 per platform) |
| 2 | "Virtual approver = different model" is assumed sufficient for independence | medium | Model≠executor prevents same-model self-approval; identity of the *operator* (who runs the model) is a separate question for the US-014 family |
| 3 | Sub-agent spawn cost/tokens are acceptable | medium | `usage` in results (Claude/Codex) + CostTracker pattern (Squad) mitigate; budgets are an open design point |
| 4 | The kit can ship generated wrappers pre-built (no adoption-time generation) | low | Consistent with the existing 4-agent no-build-step philosophy |
| 5 | No external frameworks were benchmarked beyond docs review | low | No runtime POC was executed; performance/behavioral claims are from official documentation |
| 6 | The manifest rename/schema change (`checkpoint_approvals[]`) is flagged, not decided | medium | G36 conversion rules apply; decision belongs to the ADR/US family |

---

## 8. Conclusions and recommendations

The exploration answers the research question affirmatively: the AITL
precept, the `agents/` registry and platform-native sub-agents are all
feasible on current tooling, with the independence rule and the escalation
floor as the two non-negotiable design constraints. The recommended path is
incremental and governed: decide the precept in the US-014 ADR family,
implement the kit layer (registry + wrappers + generator + parity check)
through a Bolt → SPEC V-Bounce, and pilot on one platform (Claude Code is
the strongest candidate: model override + `Agent(...)` allowlist + usage
audit) before the multi-platform pass.

| # | Recommendation | Generates | Reference |
|---|----------------|-----------|-----------|
| 1 | Decide the AITL precept + independence rule + human-depth-by-risk table as a policy | ADR (US-014 family) | §5.1 |
| 2 | Decide the manifest shape: `checkpoint_approvals[]` with `mode: human\|virtual` (and G36 conversion) | ADR / schema change | §5.1 |
| 3 | Scope the `agents/` registry (roles, roster.yaml, wrapper generator, parity check) as a kit feature | US → BOLT → SPEC | §5.2 |
| 4 | Pilot the flow on Claude Code first (model override, allowlist, usage audit) | US/BOLT (pilot) | §5.3 |
| 5 | Design the conductor engine evaluation (MAF vs Squads vs Squad) as a separate investigation before adopting | DISC-NNN / ADR | §5.4 |
| 6 | Re-verify platform APIs at implementation time (Codex V2 flags, Copilot releases) | BOLT prerequisite | §7 #1 |
| 7 | Keep G18/G24/G37 + handoff outside any fallback (identity rules never dissolved) | ADR constraint | §5.1, §5.5 |
| 8 | Treat AITL as an **opt-in superset** — guarantee the zero-config default is byte-for-byte HITL, make enabling virtual approvers a per-project ADR, and place the precept in a top-level foundational ADR (v5.0 bump), separate from the US-014 availability family | Foundational ADR (v5.0) | §5.6 |

**Affected analysis artifacts:** None (no analysis/ folder content updated by
this Discovery). It informs the US-014 family and future US/Bolt definitions.

---

## 9. Sources

| Source | Where |
|--------|-------|
| OpenCode keybinds (official docs) | https://opencode.ai/docs/keybinds/ |
| Claude Code sub-agents | https://code.claude.com/docs/en/sub-agents |
| Claude Code Agent SDK hooks (SubagentStop) | https://code.claude.com/docs/en/agent-sdk/hooks |
| Copilot chat in IDE (sub-agents) | https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-ide?tool=vscode |
| Copilot hooks reference (agentStop/subagentStop) | https://docs.github.com/en/copilot/reference/hooks-reference |
| Codex agent role files | https://github.com/openai/codex/blob/main/codex-rs/core/src/config/agent_roles.rs |
| Codex spawn_agent tool | https://github.com/openai/codex/blob/main/codex-rs/core/src/tools/handlers/multi_agents_v2/spawn.rs |
| Codex multi-agent thread flow | https://github.com/openai/codex/blob/main/codex-rs/rollout-trace/README.md |
| Microsoft Agent Framework | https://github.com/microsoft/agent-framework |
| Braintrust Squads | https://github.com/braintrustdata/squads |
| Brady Gaster's Squad (Copilot runtime) | https://github.com/bradygaster/squad |
| Repo context | AREV-001/AREV-002, REV-001, US-014, SPEC-260821-0108 (governed records) |

---

## 10. History

| Date | Change | Author |
|------|--------|--------|
| 2026-08-22 | Initial investigation (draft) — consolidates the AITL/sub-agent design exploration | @eugenio.serrano |
| 2026-08-22 | Added §5.6 (AITL as an opt-in superset; HITL-pure as the zero-config default + safe-default invariants) and recommendation #8; exec-summary clarified (via Claude Opus 4.8, maintainer direction) | @eugenio.serrano |

---

## 11. HITL-DISC-Approval

> **Avenga DevFlow §2.13, §3.0.** This Discovery remains a draft until a
> qualified human designated for the research domain records
> `HITL-DISC-Approval` (in the `review` frontmatter block). Approval confirms
> the research question was answered with adequate evidence, the limits and
> assumptions are explicit, and the conclusions are reliable enough to guide
> backlog or architecture decisions. It does **not** approve any downstream
> artifact — each US, Bolt, ADR or risk created from this Discovery follows
> its own lifecycle and HITL approval.

| Field | Value |
|-------|-------|
| **Reviewer** | eugenio.serrano |
| **Role** | qualified human for the research domain |
| **Decision** | approved |
| **review_ready_at** | `2026-08-22T01:47:18-03:00` |
| **review.started_at** | `2026-08-22T02:01:23-03:00` |
| **review.decided_at** | `2026-08-22T02:01:23-03:00` |
| **Findings** | None — acknowledged_without_comment (reason in the frontmatter `review:` block) |
