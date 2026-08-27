---
id: "DISC-002"
title: "DevFlow Agents — the agent definition contract, the shipped Coordinator, the roster (humans + agents + models), capability governance and per-platform deployment"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-fable-5"
status: "approved"
category: "technology"
research_question: "What is the architecture of the DevFlow Agents layer — what exactly IS a DevFlow Agent (prompt + tools + model + capabilities), how does the methodology-shipped Coordinator orchestrate project-built role agents as platform sub-agents, how does the roster unify humans and agents (including model-per-agent declaration), and how is all of this governed and deployed on the four target platforms — so the AITL foundational ADR, the manifest ADR and the agents/ USs can be scoped on verified facts?"
sources:
  - "https://code.claude.com/docs/en/sub-agents"
  - "https://opencode.ai/docs/agents/"
  - "https://docs.github.com/en/copilot/reference/custom-agents-configuration"
  - "https://learn.chatgpt.com/docs/config-file/config-reference"
  - "https://github.com/openai/codex/issues/14579"
  - "https://github.com/openai/codex/issues/15250"
  - "https://github.com/bradygaster/squad"
  - "https://checkmarx.com/learn/mcp-security-risks-real-world-incidents-and-security-controls/"
  - "https://www.aptible.com/mcp-security/mcp-prompt-injection"
  - "devflow/discovery/DISC-001-aitl-and-subagent-orchestration.md (approved)"
tags: ["devflow-agents", "aitl", "roster", "coordinator", "subagents", "mcp", "capabilities", "platforms", "v5.0"]
review_ready_at: "2026-08-22T14:07:56-03:00"
review: # HITL-DISC-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "research domain lead"}]
  started_at: "2026-08-22T14:18:08-03:00"
  decided_at: "2026-08-22T14:18:08-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved as governed input. Platform contracts re-verified against official docs (2026-08-22) and the maintainer's DevFlow Agents vision resolved into a buildable architecture: agent-as-identity (model as attribute), the kit-shipped Coordinator that routes/records but never signs, the roster unifying humans+agents+models so availability (US-014) and approval independence are one lookup, capability tiers with a hard approver ceiling (T0/T1), and the injection-forged-approval threat with its structural mitigation. Limits explicit (Codex invocation bugs #14579/#15250, Copilot env-dependent fields, no runtime POC). Conclusions reliable enough to scope the foundational AITL ADR, the DevFlow Agent ADR, the manifest ADR and the agents/ + pilot USs. Every downstream artifact keeps its own lifecycle."
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs, and section
  headings (##) stay in English (the schema). All prose — findings,
  observations, recommendations — goes in the project's content_language
  (en, declared in devflow/LANGUAGE).

  ⚠️ HITL-DISC-Approval (§2.13): this Discovery remains DRAFT until a
  qualified human records HITL-DISC-Approval. Until then, its conclusions
  cannot be used as governed input. Approval does not approve any
  downstream artifact. Executable spike/prototype code requires an
  approved non-functional Bolt under US-000 first.
-->

# DISC-002 — DevFlow Agents: definition contract, Coordinator, roster and capability governance

| Field               | Value |
|---------------------|-------|
| **Category**        | technology |
| **Status**          | approved (HITL-DISC-Approval 2026-08-22) |
| **Research question** | What IS a DevFlow Agent, how does the shipped Coordinator orchestrate project-built role agents as platform sub-agents, how does the roster unify humans + agents + models, and how is it all governed and deployed on the four platforms? |
| **Date**            | 2026-08-22 |
| **Author**          | eugenio.serrano (investigation run by claude-fable-5 under maintainer direction) |
| **Sources**         | Official platform docs (verified 2026-08-22), squad repo, MCP security landscape, DISC-001 (approved) |

---

## 1. Research question

DISC-001 (approved) established that AITL is feasible and settled the opt-in-
superset framing. What it deliberately left immature — and what blocks the
foundational AITL ADR, the manifest ADR and the `agents/` USs — is the **shape
of the agent layer itself**. The maintainer's vision, consolidated from the
v5.0 design sessions:

- There will be several **DevFlow Agents**, each with its **own prompt and/or
  tools to decide** — like members of a team.
- **One ships with the methodology: the Coordinator** (the orchestrator). The
  rest — a functional analyst who knows the business, an architect, a
  developer, a QA — are **built per project**.
- The scheme is **squad-like but inside the existing Avenga DevFlow agent**,
  with role agents running as **platform-native sub-agents**.
- The **roster** lists the team — **agents and humans together** — and each
  agent is **responsible for declaring which model it runs on**, within what
  the platform offers.
- Independence for approvals divides **by DevFlow Agent (actor), not only by
  model** — generalizing the human handoff rule.
- Agents should eventually **use MCPs and talk to the external world** — a
  capability that must be matured and governed, not just enabled.

The material unknowns this Discovery reduces: **(a)** the canonical DevFlow
Agent definition contract and how each field maps to the four platforms;
**(b)** the Coordinator's responsibilities and boundaries; **(c)** the roster
schema and how it resolves both role availability and approval independence;
**(d)** capability tiers (tools/MCPs/external world) and the governance that
keeps an agent with MCP access from becoming an ungoverned actor; **(e)** what
is kit product vs project configuration, and how the family deploys ("its own
little folder").

---

## 2. Scope

**In scope:**
- The **DevFlow Agent definition contract** (canonical, platform-neutral) and
  its verified per-platform mapping (Claude Code, OpenCode, GitHub Copilot,
  OpenAI Codex — official docs re-checked on 2026-08-22).
- **Model-per-agent**: whether and how each agent declares its own model, and
  the spawn-time override escape hatch.
- The **Coordinator**: responsibilities, separation of duties, spawn topology
  (who may spawn whom), and its native enforcement per platform.
- The **roster**: schema, humans + agents unified, role resolution, and how
  the two independence layers (actor-level, model-level) become lookups.
- **Capability tiers** for tools/MCPs/external access, and the security model
  (verified against the 2026 MCP threat landscape) — including the new threat
  class AITL introduces: **injection-forged approvals**.
- **Product vs project-config split** and the deployment model (the `agents/`
  family in the kit).

**Out of scope:**
- Deciding the AITL precept itself (foundational ADR — DISC-001 rec #1/#8).
- The manifest schema decision (`checkpoint_approvals[]` — its own ADR).
- The conductor/engine evaluation (MAF vs Squads vs squad — DISC-001 rec #5
  stays a separate investigation; this Discovery designs the methodology
  layer, not an execution engine).
- Implementation code, wrappers or prototypes (approved Bolts first).
- AREV mechanics (G37 stays as-is: model-based debate neutrality is a
  different concern from checkpoint approval independence).

---

## 3. Executive summary

The maintainer's model is buildable today, and one insight organizes all of
it: **the DevFlow Agent — not the model — is the unit of identity.** A DevFlow
Agent is a governed identity (`id` + role charter) that *has* a model, tools
and capabilities as attributes, exactly as a human team member has skills.
This generalizes the existing human rules without inventing new ones: the
handoff rule ("the approver is a different person than the executor") becomes
"the approver is a different **actor**", resolvable by roster lookup at
actor level (floor), hardened at model level for high risk, and escalated to
humans at the top (critical/regulatory). All four platforms verified today
support the essentials natively — **per-agent files, per-agent model,
per-agent tool restriction, and agent-scoped MCP servers** — with Claude Code
the most complete (per-agent model + tools + `mcpServers` + hooks + spawn
allowlists + persistent memory) and Codex carrying known invocation gaps. The
architecture lands as: a **kit-shipped Coordinator** (routes, spawns, records,
enforces the escalation floor — and **never signs**), **project-built role
agents** instantiated from kit charter templates, and a **project roster**
that unifies humans and agents and makes both independence checks and
role-availability (US-014) a single lookup. The riskiest finding is also the
most actionable: with MCP-enabled agents, **prompt injection can forge an
approval** — so approver-mode agents must run with minimal capabilities
(repo-read only), which is cheap to enforce because approving needs no
external tools at all.

---

## 4. Inventory / Mapping

### 4.1 The concept inventory

| Concept | What it is | Governed as |
|---------|-----------|-------------|
| **DevFlow Agent** | A named, versioned identity: role charter (prompt) + model + capabilities. The unit of independence. | Definition contract in the kit; instances per project |
| **Coordinator** | The one agent shipped with the methodology. Routes work, spawns role agents, resolves the roster, enforces the escalation floor, records evidence. **Never approves.** | Kit product (governed) |
| **Role agents** | Project-built instances (domain-aware FA, architect, developer, QA, reviewer…). | Project artifacts, instantiated from kit templates, governed by the project's AITL-enable ADR |
| **Roster** | The team list: humans + agents, roles, models, what each may approve. One lookup answers availability (US-014) and independence (AITL). | Schema = kit product; contents = project config |
| **Capability tier** | How far an agent may reach (repo-only → read-only external → transactional MCPs → unrestricted sandbox). | Declared per agent; ceilings per mode (executor/approver) |
| **Wrapper** | The per-platform projection of a canonical agent definition. | Generated + parity-checked, shipped in the kit |

### 4.2 Platform verification matrix (official docs, 2026-08-22)

| Capability | Claude Code | OpenCode | GitHub Copilot | OpenAI Codex |
|---|---|---|---|---|
| **Agent files** | `.claude/agents/*.md` (also user/CLI/plugin scopes) | `.opencode/agents/*.md` or `opencode.json` `agent:{}` | `.github/agents/*.agent.md` (repo/org/enterprise levels) | `[agents.<name>]` in `config.toml` + `.codex/agents/*.toml` |
| **Model per agent** | ✅ `model:` (sonnet/opus/haiku/fable, full IDs, `inherit`); resolution: env var → per-invocation → frontmatter → main | ✅ `model: provider/model-id`; subagents default to invoker's model | ✅ `model:` (environment-dependent: VS Code/JetBrains/Eclipse/Xcode) | ✅ per-role `config_file` TOML layer; `agents.default_subagent_model`; explicit spawn model wins |
| **Tools per agent** | ✅ `tools:` allowlist + `disallowedTools:` denylist | ✅ `permission:{}` per tool with glob patterns (`bash: {"git status *": allow}`) | ✅ `tools:` list (default: all) | via role `config_file` + `sandbox_mode` |
| **MCP per agent** | ✅ `mcpServers:` — inherit by name or inline definitions (inline requires folder trust) | 🟡 wildcard permissions (`mymcp_*: deny`) — filter, not per-agent server config | ✅ `mcp-servers:` per agent (**not in IDEs**; processing order: built-in → agent → repo) | 🟡 global `mcp_servers.*`, overridable via role `config_file`; no documented per-agent syntax |
| **Agent→agent invocation** | ✅ `Agent` tool with **allowlist** `tools: Agent(worker, researcher)`; depth 3 default; 20 concurrent | ✅ `permission.task` per subagent (deny removes it from the tool description) | ✅ `agent` tool alias ("invoke a different custom agent") | ✅ `spawn_agent`/`send_input`/`resume_agent`/`wait_agent`/`close_agent`; `features.multi_agent` flag |
| **Audit / hooks** | ✅ per-agent `hooks:` (Pre/PostToolUse, Stop) + session `SubagentStart`/`SubagentStop`; `usage` (tokens) in spawn result | ❌ none native | ✅ `agentStop`/`subagentStop` (+ `modifiedResponse` payload shaping) | ❌ not documented |
| **Isolation** | ✅ `isolation: worktree` | ❌ | ❌ (cloud env) | ✅ `sandbox_mode` per role |
| **Persistent memory** | ✅ `memory: user\|project\|local` | ❌ | ❌ | ❌ |
| **Other relevant** | `maxTurns`, `permissionMode`, `skills` preload, sibling roster for `SendMessage`, resume | `temperature`, `steps` cap, `hidden`, Tab/`@` manual access | `disable-model-invocation`, `user-invocable`, `target: vscode\|github-copilot`, 30k-char prompt cap | `max_concurrent_threads_per_session` |
| **Known gaps** ⚠️ | inline MCP trust rules per scope | MCP is filter-only; no audit hooks | `model` env-specific; `mcp-servers`/`metadata` ignored in IDEs | **Issues #14579/#15250:** repo-local custom agents not invocable by name from tool-backed sessions (spawn takes generic `agent_type` + explicit overrides) |

**Direct answer to the maintainer's question** (*"can each agent be
responsible for choosing its model, within what the tool has available?"*):
**yes, on all four platforms** — the declaration lives in the agent's
definition (frontmatter/TOML), constrained to the platform's catalog, with a
spawn-time override available on Claude Code and Codex as the Coordinator's
escape hatch. What is **not** standard anywhere is an agent re-choosing its
model mid-run — the choice binds at definition or spawn, which is actually
desirable: the roster stays the single source of truth for "who runs on what".

---

## 5. Detailed findings

### 5.1 The DevFlow Agent definition contract (canonical, platform-neutral)

A DevFlow Agent is **an identity, not a model**. The canonical definition —
one file per agent, projected into platform wrappers — needs exactly these
fields (verified representable on all four platforms):

```yaml
# agents/roles/<id>/agent.yaml  (canonical — wrappers are generated)
id: qa-agent                    # kebab-case; THE identity used in independence checks
role: qa                        # archetype: coordinator | functional-analyst | architect |
                                #   developer | qa | reviewer | (project-defined…)
description: >                  # when the Coordinator should delegate to it
  Verifies V-Bounce packages against ACs and gates; approves MEM checkpoints
  for low/medium risk when enabled by the roster.
model: claude-opus-5            # ★ the agent's OWN declaration (maintainer decision),
                                #   constrained to the platform catalog by the wrapper
modes: [executor, approver]     # what it may do; approver-mode triggers capability ceilings (§5.4)
approves: [MEM]                 # checkpoint classes it may sign (empty = executor-only)
capabilities:
  tier: T1                      # §5.4 — repo + read-only external
  tools: [read, grep, glob, bash]   # least-privilege allowlist (mapped per platform)
  mcp_servers: []               # explicit, named; empty by default
escalation:                     # role-specific ceiling — ALWAYS above the engine floor
  - "uncertainty too high to sign"
  - "evidence incomplete or contradictory"
write_paths: []                 # G30/G31 mirror; approvers write nothing
# --- body/charter: the system prompt (who I am, what I check, how I decide,
#     when I escalate, what I may never do) ---
```

Key contract decisions surfaced by the verification:

1. **`id` is the identity; `model` is an attribute.** Two agents may share a
   model (small teams will); the roster records both, and each independence
   layer reads its own field. Renaming a prompt does **not** create a new
   identity — the `id` does.
2. **`modes` + `approves` make approval authority explicit and enumerable.**
   An agent with `approves: []` can never sign anything, no matter what its
   prompt says — the Coordinator checks the field, not the prose. This is the
   engine-enforced complement to DISC-001's escalation floor.
3. **The charter body is the role's judgment**, never its authority. Authority
   lives in structured fields the Coordinator (and validators) can read.
4. Every field has a verified landing spot per platform (§4.2): `model` →
   frontmatter/TOML; `capabilities.tools` → `tools:`/`permission:{}`/role
   config; `mcp_servers` → `mcpServers:`/`mcp-servers:`/config layer;
   agent→agent restrictions → `Agent(...)` allowlist / `permission.task` /
   `agent` alias / spawn flags.

### 5.2 The Coordinator — ships with the methodology, routes everything, signs nothing

The one DevFlow Agent in the kit. Its charter is the methodology itself
(today's four platform definitions are, in effect, its ancestor). In the
squad-inside-the-mother-agent pattern, the existing **Avenga DevFlow platform
agent evolves into the Coordinator**: the session the human talks to, which
spawns role agents as platform sub-agents and receives control back via the
spawn tool result (state = files, per DISC-001).

**Responsibilities (all mechanical, none judgmental):**

| # | Responsibility | How |
|---|----------------|-----|
| 1 | **Roster resolution** | For each checkpoint/task: look up which actors (humans or agents) hold the role, per project policy |
| 2 | **Spawn orchestration** | Launch executor agents for V-Bounce work; launch approver agents for enabled checkpoints; pass the task, collect the structured result |
| 3 | **Independence enforcement** | Refuse to route an approval to the actor that executed (actor floor); at high risk, refuse same-model approvers (model hardening); at critical/regulatory, route to humans only |
| 4 | **Escalation floor** | Gate red, turn budget exhausted, changes-requested loop, ADR-class change, missing evidence → forced human stop, never delegable |
| 5 | **Recording** | Write the `checkpoint_approvals[]` entry (actor id + model + mode), append `runs[]` usage (Claude Code returns per-spawn token usage natively), log the spawn topology |
| 6 | **Boundary enforcement** | Sub-agent write paths mirror G30/G31 (`input/` read-only, `_archive/` off-limits) via per-agent tool permissions |

**The separation-of-duties rule (proposed, for the AITL ADR):** the
Coordinator **routes and records but never signs**. If the router could also
approve, every independence check would collapse into "the Coordinator
approved its own routing". Keeping it a pure administrator makes the audit
trail trustworthy and maps cleanly onto every platform: the Coordinator is
the only agent whose spawn list includes approver agents.

**Spawn topology (enforceable natively):** approver agents are spawned **only
by the Coordinator (or invoked by a human), never from an executor's
subtree** — otherwise the developer agent could spawn "its own" approver.
Claude Code enforces this with `Agent(...)` allowlists (executors get no
`Agent` tool, or only their helpers; the Coordinator gets
`Agent(qa-agent, reviewer-agent, …)`); OpenCode with `permission.task`
denials; Copilot by omitting the `agent` alias from executor tools; Codex by
parent instruction + role config (weakest — see §7).

```mermaid
flowchart TB
    H["Human operator"] -->|talks to| C["Coordinator<br/>(the Avenga DevFlow agent — ships with the kit)<br/>routes · spawns · records · NEVER signs"]
    C -->|spawn: execute Bolt| DEV["developer-agent<br/>model: sonnet · T1<br/>modes: [executor]"]
    C -->|spawn: approve MEM| QA["qa-agent<br/>model: opus · T0/T1<br/>modes: [approver] · approves: [MEM]"]
    C -.->|escalation floor:<br/>critical / gate red / budget| H
    R[("roster.yaml<br/>humans + agents + models + approves")] --- C
    DEV -->|structured result + files| C
    QA -->|decision + evidence| C
    C -->|checkpoint_approvals[] entry<br/>actor id + model + usage| M[("manifest")]
    DEV x-.-x|"forbidden: executor<br/>never spawns its approver"| QA
```

### 5.3 The roster — one lookup for availability AND independence

The roster is where the maintainer's two long-running threads meet: US-014's
role availability ("who holds this role?") and AITL's independence ("is the
approver a different actor?"). One file answers both:

```yaml
# agents/roster.yaml  (schema = kit product; contents = project config)
project_policy:
  aitl_enabled_checkpoints: [MEM]          # per-project ADR decision (DISC-001 §5.6.3)
  human_only: [critical, regulatory]       # floor — may be tightened, never loosened
actors:
  humans:
    - user: eugenio.serrano
      roles: [architect, tech_lead, dev_validator, functional_analyst, po]
  agents:
    - id: qa-agent
      role: qa
      model: claude-opus-5
      definition: agents/roles/qa-agent/agent.yaml
      modes: [approver]
      approves: [MEM]
    - id: developer-agent
      role: developer
      model: claude-sonnet-5
      definition: agents/roles/developer-agent/agent.yaml
      modes: [executor]
```

**Resolution rules the schema must support (for the USs):**
1. **Role → actors**: a checkpoint's recommended role resolves to the actors
   holding it; humans and agents are peers in the lookup; the no-holder
   fallback (US-014) applies to humans, and an *agent* holder counts only for
   checkpoints the project's AITL policy enables.
2. **Independence floor (actor)**: `approver.id ≠ executor.id` — for humans
   this **is** the existing handoff rule; the roster just generalizes the
   comparison to actors.
3. **Model hardening (risk-scaled)**: at `high`, additionally
   `approver.model ≠ executor.model` (both fields are in the roster — the
   check is a lookup, not an inference); recommendation only at lower risk.
4. **Human ceiling**: `critical` + `regulatory` resolve to humans regardless
   of roster contents (safe-default invariant, DISC-001 §5.6).
5. **Zero-config**: no roster, or no `agents:` section → pure HITL,
   byte-for-byte v4.2 behavior.

Prior art check: squad's `defineTeam`/`defineAgent` (+ per-agent `charter.md`
and `history.md`) validates the shape — a declarative team where each agent
declares role and model — and its "coordinator dispatches, human keeps
priorities and final decisions" stance matches this design. Claude Code even
hands each spawned sub-agent a **sibling roster** natively (for
`SendMessage`), so the concept has direct platform support.

### 5.4 Capabilities and the external world — tiers, and the one new threat AITL creates

The maintainer wants agents that can "use MCPs, talk to the outside world —
do whatever they need". The 2026 security landscape says this is exactly
where discipline pays: tool poisoning (malicious instructions in tool
metadata), prompt injection via processed content (the April 2026 incidents
hijacked Claude Code, Gemini CLI and Copilot through PR titles, exfiltrating
CI secrets), and exfiltration through over-privileged agent identities; the
consensus controls are least-privilege allowlists, endpoint restriction,
identity binding and human checkpoints. Rather than one on/off switch,
capabilities become **tiers declared per agent**:

| Tier | Reach | Typical holder | Platform enforcement |
|------|-------|----------------|----------------------|
| **T0** | Repo only (canonical paths; G30/G31 mirrored) | approver-mode agents | tool allowlists everywhere |
| **T1** | + read-only external (web fetch/search, docs MCPs) | most executors, QA | `tools` + named `mcpServers` |
| **T2** | + transactional external MCPs (Jira, Slack, DBs…), each server named + allowlisted | integration-specific executors | per-agent MCP config (Claude/Copilot native; Codex via role config; OpenCode via wildcard permissions) |
| **T3** | Unrestricted / experimental | sandboxed spikes only | `isolation: worktree` / `sandbox_mode`; mirrors L4 — proposed to require an ADR like L4 does |

**The finding that matters most — injection-forged approvals.** AITL creates
a threat class HITL never had: if an *approver* agent processes untrusted
external content (a fetched page, an MCP tool description, a PR title) during
its approval turn, a prompt injection can **forge a checkpoint approval** —
the attack signs the release. The mitigation is structural, and cheap:

> **Approver-mode ceiling:** an agent acting as approver runs at **T0 (at
> most T1 with pinned, trusted sources)**, with no transactional MCPs and no
> write paths. Approving needs nothing external — the evidence (diff, tests,
> MEM, manifest) is all in the repo.

This is enforceable today (per-agent tools/MCP on every platform) and should
be an invariant in the AITL ADR, not a prompt suggestion. Executor agents can
be as capable as the project dares; **approval integrity never depends on an
executor's capability tier.**

### 5.5 Product vs project — what lives in the kit's "little folder"

Resolving the question DISC-001 §5.2 left open (role prompts: product or
living data), now decidable because the *authority* fields (§5.1) are
separate from the *judgment* body:

| Artifact | Nature | Governance |
|----------|--------|-----------|
| Coordinator definition | **Kit product** | Bolt + SPEC, parity-checked like the four agents (it IS their evolution) |
| Role **charter templates** (FA/architect/developer/QA/reviewer skeletons) | **Kit product** | Bolt + SPEC; adopters instantiate, never edit in place |
| Roster **schema** + validation | **Kit product** | Bolt + SPEC |
| Wrapper **generator** + parity check | **Kit product** (tooling, ships pre-built results) | Bolt + SPEC — extends the 4-agent sync philosophy to N agents × 4 platforms |
| Instantiated role agents (domain knowledge) | **Project artifact** | Covered by the project's **AITL-enable ADR** (the same governed act that enables virtual approvers names who they are — DISC-001 §5.6.3); editing an *approver's* charter or authority fields re-triggers that ADR's review |
| `roster.yaml` contents | **Project config** | Same per-project ADR; zero-config = pure HITL |

Proposed kit layout (sanctioned via G30 in the US, matching DISC-001 §5.2):

```
distribution-kit/devflow/agents/
├── coordinator/agent.yaml + charter.md      ← ships concrete
├── roles/                                   ← charter TEMPLATES (skeletons)
│   ├── functional-analyst/  ├── architect/  ├── developer/
│   ├── qa/                  └── reviewer/
├── roster.schema.yaml + roster.example.yaml
└── README.md
(+ generated wrappers committed per platform: .claude/agents/, .opencode/agents/,
 .github/agents/, .codex/agents/ — parity-checked, no adoption-time build)
```

### 5.6 Why Claude Code stays the pilot, and what the others need

The re-verification sharpens DISC-001 rec #4. Claude Code is the only
platform with **all** of: per-agent model + tools + MCP servers + per-agent
hooks + spawn allowlists + depth/concurrency caps + worktree isolation +
persistent per-agent memory + usage-in-result. That covers every §5.1–§5.4
mechanism natively. OpenCode is a solid second (excellent permission globs;
no audit hooks). Copilot is viable with environment caveats (`model`
IDE-dependent; `mcp-servers` not honored in IDEs). Codex has the right
primitives but **open invocation bugs** (#14579/#15250: role files on disk
not reachable by name from tool-backed sessions) — its wrapper must be
re-verified at implementation time and may need the generic
`agent_type`+overrides path meanwhile.

---

## 6. Experiments performed (if any)

No executable experiments (read-only investigation; spikes require an
approved Bolt under US-000). Documentation verification performed 2026-08-22:

| Verification | Source | Key result |
|--------------|--------|------------|
| Claude Code sub-agent contract | official docs | `model`/`tools`/`disallowedTools`/`mcpServers`/`hooks`/`memory`/`isolation`/`maxTurns` per agent; `Agent(...)` allowlist; depth 3 / 20 concurrent; usage in result; sibling roster |
| OpenCode agent contract | official docs | per-agent `model`, `permission:{}` with glob patterns incl. `task` (subagent gating) and MCP wildcards; `steps` cap; no audit hooks |
| Copilot custom agents | official reference | `.agent.md`: `name`/`description`/`tools`/`model`(env-dependent)/`mcp-servers`(not IDEs)/`target`/`disable-model-invocation`/`user-invocable`; `agent` tool alias for agent→agent; repo/org/enterprise levels; 30k-char prompt cap |
| Codex multi-agent | config reference + repo issues | `[agents.<name>]` with `config_file` role layers; `default_subagent_model`/`_reasoning_effort`; `features.multi_agent`; spawn/send/resume/wait/close; **issues #14579/#15250 open** |
| squad (bradygaster) | repo | `defineSquad`/`defineTeam`/`defineAgent(name, role, model)`; per-agent charter+history files; coordinator dispatches, human keeps decisions; hook pipelines / write guards / PII scrub |
| MCP threat landscape 2026 | Checkmarx, Aptible, et al. | tool poisoning, injection-via-content incidents (April 2026), exfiltration; controls: least privilege, allowlists, endpoint restriction, human checkpoints → basis of §5.4 tiers |

---

## 7. Assumptions and limits

| # | Assumption / Limit | Severity | Impact |
|---|--------------------|----------|--------|
| 1 | Platform contracts keep evolving; Codex has **open bugs** on named custom-agent invocation (#14579/#15250) and Copilot's `model`/`mcp-servers` are environment-dependent | high | Every wrapper re-verified against current docs at implementation (DISC-001 rec #6 stands); Codex wrapper may need the generic-spawn fallback |
| 2 | Actor-level independence (agent id ≠ agent id) is assumed meaningful even when both agents share a model at low/medium risk | medium | Deliberate trade-off for single-provider teams; model hardening at `high`, humans at `critical`; **calibrate with pilot evidence** before tightening |
| 3 | The injection-forged-approval mitigation (approver ceiling T0/T1) is designed from documented incident patterns, not from a red-team exercise on this methodology | medium | A red-team pass on the pilot (try to forge an approval via injected content) should be part of the pilot US's ACs |
| 4 | Spawn-topology enforcement is native on Claude Code/OpenCode/Copilot but instruction-based on Codex | medium | On Codex, the Coordinator's own charter + role `config_file` are the control until the platform offers allowlists |
| 5 | Cost/token budgets per agent are recorded (usage in results) but no budget-enforcement design is proposed here | low | CostTracker-style budgets deferred to the conductor DISC (DISC-001 rec #5) |
| 6 | The `agents/` family naming (ids, N-rules) and INDEX/manifest treatment are sketched, not normed | low | The registry US defines naming + G30 sanctioning; no new artifact IDs invented here |
| 7 | No runtime POC executed — all claims are documentation-verified | low | First Bolt of the registry US should include a minimal spawn smoke test on the pilot platform |

---

## 8. Conclusions and recommendations

The research question is answered: a DevFlow Agent is a **governed identity
with a model as an attribute**; the Coordinator is a **kit-shipped pure
administrator** (routes, spawns, records, never signs); the roster is the
**single lookup** unifying humans + agents, availability + independence; and
capabilities are **tiered per agent with a hard ceiling for approver mode** —
all representable natively on the four platforms today, with Claude Code the
complete pilot target. The AITL foundational ADR is now unblocked: it can
define independence over **actors** (generalizing the handoff rule) instead
of over models alone, which was the design tension DISC-001 left open.

| # | Recommendation | Generates | Reference |
|---|----------------|-----------|-----------|
| 1 | Write the **foundational AITL ADR** with actor-level independence as the floor (`approver.id ≠ executor.id`), model hardening at `high`, human ceiling at `critical`/`regulatory`, the zero-config = pure-HITL invariant, and the **Coordinator-never-signs** and **approver-capability-ceiling (T0/T1)** rules as invariants | **ADR** (v5.0 foundational) | §5.2, §5.3, §5.4 |
| 2 | Write the **manifest ADR**: `checkpoint_approvals[]` records the **actor** (`agent:<id>` or `human:<user>`) **and** the model + mode — both fields, so actor-level and model-level audits are always possible; G36 conversion from `hitl_approvals[]` | **ADR** (schema, v5.0 bump) | §5.1, §5.3 |
| 3 | Define the **`agents/` registry US**: canonical definition contract (§5.1 fields), Coordinator, role charter templates, roster schema + validation, wrapper generator + N×4 parity check, G30 sanctioning of the folder | **US → BOLT → SPEC** | §5.1, §5.5 |
| 4 | Define the **pilot US on Claude Code** (full native coverage), with ACs that include the independence lookups, the approver ceiling, and a **red-team AC**: attempt to forge an approval via injected content | **US → BOLT** | §5.4, §5.6 |
| 5 | Keep the **conductor/engine evaluation separate** (DISC-001 rec #5) — this architecture is methodology-level; budgets/CostTracker land there | **DISC-NNN** | §7 #5 |
| 6 | **Re-verify Codex and Copilot contracts at implementation** (open issues #14579/#15250; env-dependent fields); wrappers may need platform-specific fallbacks | **BOLT prerequisite** | §4.2, §7 #1 |
| 7 | The per-project **AITL-enable ADR** (DISC-001 §5.6.3) covers: enabled checkpoints, the roster contents, and the instantiated approver charters — one governed act, re-triggered when an approver's charter or authority fields change | **ADR constraint** (into rec #1's ADR) | §5.5 |

**Affected analysis artifacts:** None (no `analysis/` content updated).
Supersedes nothing in DISC-001 — it deepens §5.1–§5.3 with the agent-identity
model and resolves its §5.2 open design point (product vs living data).

---

## 9. Sources

| Source | Where |
|--------|-------|
| Claude Code sub-agents (full contract) | https://code.claude.com/docs/en/sub-agents |
| OpenCode agents (config, permissions, task gating) | https://opencode.ai/docs/agents/ |
| Copilot custom agents configuration reference | https://docs.github.com/en/copilot/reference/custom-agents-configuration |
| Codex config reference (agents, multi_agent flags) | https://learn.chatgpt.com/docs/config-file/config-reference |
| Codex custom-agent invocation gaps | https://github.com/openai/codex/issues/14579 · https://github.com/openai/codex/issues/15250 |
| squad — declarative team + coordinator pattern | https://github.com/bradygaster/squad |
| MCP security landscape 2026 (tool poisoning, injection incidents, controls) | https://checkmarx.com/learn/mcp-security-risks-real-world-incidents-and-security-controls/ · https://www.aptible.com/mcp-security/mcp-prompt-injection |
| Repo context | DISC-001 (approved), US-014 family, ADR-004/ADR-006, AREV-001/002/003 records |

---

## 10. History

| Date | Change | Author |
|------|--------|--------|
| 2026-08-22 | Initial investigation (draft) — consolidates the DevFlow Agents architecture design; platform contracts re-verified against official docs; capability/MCP governance matured (maintainer direction, run by claude-fable-5) | @eugenio.serrano |
| 2026-08-22 | HITL-DISC-Approval recorded | @eugenio.serrano |

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
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-22T14:07:56-03:00` |
| **review.started_at** | `2026-08-22T14:18:08-03:00` |
| **review.decided_at** | `2026-08-22T14:18:08-03:00` |
| **Findings** | none — `acknowledged_without_comment: true` (see frontmatter) |
