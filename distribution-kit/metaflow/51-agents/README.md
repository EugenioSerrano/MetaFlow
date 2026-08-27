# 51-agents/ — the MetaFlow Agent definitions

> **Not `53-actors/`.** `metaflow/51-agents/` holds the **AI-member definitions** —
> the canonical contract, the shipped example definitions and your
> project's live agents. `metaflow/53-actors/` is the **roster home**: who is
> in the team (humans + MetaFlow Agents as actors), filled by the roster
> family.

## What lives here

- `examples/` — the five **example role definitions** (functional-analyst,
  architect, developer, qa, reviewer): `agent.yaml` (structured fields) +
  `prompt.md` (the charter body). **Read-only references**: copied, never
  referenced by the roster, never edited in place.
- `squad/` — **your project's live agents**. The folder the Coordinator
  writes when it creates an agent, and the **only** folder the roster's
  `definition:` pointers reference. Ships empty (see its README).
- `TEMPLATE-new-role/` — the generic template for any project-defined
  role: copy it (or the closest example) into `squad/<your-role>/`.
- `INDEX.md` — the family index (the shipped examples + your squad).
- `VERIFICATION.md` — the per-platform install mapping (the contract the
  Coordinator follows to project a definition into each tool's wrapper)
  and the capability status per platform.

## The Coordinator — the MetaFlow agent itself, evolved

There is **no separate coordinator folder**: the **Coordinator is the
MetaFlow agent we already ship per platform** — `CLAUDE.md`,
`.agents/skills/…`, `.github/agents/…`, `.opencode/agents/…` — **evolved**
to know how to act as the orchestrator in each case ("the evolution of
today's platform agent"). Its evolution lives in those four files: the
shared body carries the **"The Coordinator (the orchestrator)"**
paragraph (routes, delegates production, spawns approvers, records —
**never signs**, `approves: []`), and each platform preamble declares the
**spawn topology** mechanics (Claude Code `Agent(...)` allowlist, OpenCode
`permission.task`, Copilot `agent` alias, Codex instruction-based). The
wrappers are projections of ROLE agents only — nobody generates or spawns
a "coordinator sub-agent".

## The definition contract (canonical)

A MetaFlow Agent is a **governed identity** — a member of the team, like a
human — defined by one canonical file pair: `agent.yaml` (structured
fields) + `prompt.md` (the charter body). The productive mandate lives in
the charter body ("WHAT I PRODUCE"); the **authority lives in structured
fields, never in prose** (the identity model).

| Field | Meaning | Notes |
|-------|---------|-------|
| `id` | kebab-case identity | **THE identity** used in independence checks (`approver.id ≠ executor.id`) |
| `role` | archetype | coordinator · functional-analyst · architect · developer · qa · reviewer · project-defined… (open, never a closed enum) |
| `description` | when the Coordinator should delegate | |
| `model` | the agent's own declaration | constrained to the platform catalog by the wrapper |
| `modes` | `executor` \| `approver` | **`executor` (production) is the first-class default**; `approver` is a configured second role |
| `approves` | checkpoint classes it may sign | **empty = executor-only** (may never sign) |
| `capabilities.tier` | T0–T3 | T0 repo-only · T1 +read-only external · T2 transactional MCPs · T3 unrestricted |
| `capabilities.tools` | least-privilege allowlist | mapped per platform |
| `capabilities.mcp_servers` | named + allowlisted | **`[]` default** — no implicit MCP exposure |
| `escalation` | role-specific triggers | always allowed above the engine floor |
| `write_paths` | write-scope mirror | approver-mode agents write nothing |

## The security rules

- **Approver ceiling:** an agent acting as approver runs at **T0** (at
  most T1 with pinned trusted sources), **no write paths, no transactional
  MCPs** — the injection-forged-approval defense.
- **MCP allowlist:** every server is **named and allowlisted**
  (`mcp_servers: []` by default); there is no implicit or unrestricted MCP
  exposure.

## Producer-first

The charter body starts with **WHAT I PRODUCE** — the artifacts the role
owns (functional analyst → US, architect → ADR, developer → SPEC + code,
QA → TC/tests). This is the single **role → artifacts mapping** that the
roster (`53-actors/`, the roster family) derives from — it is defined once
here, never duplicated as a per-agent field.

## The two sides of an agent

| Side | Field | Meaning |
|------|-------|---------|
| **Executor (first-class)** | `modes: [executor]` + the charter body | What the agent **produces** — the artifacts its role owns (US, ADR, SPEC, code, tests) |
| **Approver (configured)** | `approves: [...]` | Checkpoint classes it may sign, under the independence floor — the capability ceiling T0/T1 applies (no write paths, no transactional MCPs) |

> **Production vs persistence:** an executor's production may be persisted
> by the Coordinator (a spawn result becomes files by the parent) —
> `write_paths` bounds the agent's own direct writes, not its output. But
> the persistence act must trace to a **real spawn**: stamping another
> actor's identity on content that actor never produced is a false claim
> (see VERIFICATION.md, "Execution evidence").

## Create your own agent (project-defined roles)

Teams configure their agents however they want — within the
non-negotiable bounds above. The **governance limit** decides who may do
it and when:

| Action | Governance |
|--------|-----------|
| **Create/update an EXECUTOR agent** (or add a member) | **Living data** — no approval required (the roster rule). Copy the template into `squad/`, fill it, have the Coordinator install it, list it in your `51-agents/INDEX.md`. |
| **Create/change an APPROVER agent** — its authority fields (`approves`, `modes`) | **The human's configuration act** — the roster entry is the enablement: a human writes `modes: [approver]` + `approves` in the actor file and lists it in the team's `roster.yaml` (`metaflow/53-actors/`; the safe default: no AI-signed approval without that explicit human configuration). MetaFlow may scaffold the agent as an executor-only draft; **granting the authority fields is the human's act — an agent never enables its own approval**. |

Steps:

1. **Copy `TEMPLATE-new-role/`** (or the closest `examples/` definition)
   to `squad/<your-role>/`.
2. **Fill `agent.yaml`** — pick your `id` (kebab-case, THE identity), your
   `role` (open archetype — project-defined…), the model
   from the platform catalog, `modes`/`approves`/`capabilities`/`escalation`/
   `write_paths`. The approver ceiling and the MCP allowlist are
   non-negotiable for approver mode.
3. **Write `prompt.md`** — who you are, WHAT YOU PRODUCE, what you check,
   how you decide, when you escalate, what you may never do.
4. **The Coordinator installs it** — the MetaFlow agent projects
   your new role into the four platform shapes (per the mapping in
   `VERIFICATION.md`) and installs them in the project's platform folders
   (the N×4 parity check as the safety net).
5. **List it in `51-agents/INDEX.md`** and add it to the roster (`53-actors/`,
   the roster family).
6. **If it may approve** — the human grants it **in the roster**:
   `modes: [approver]` + the `approves` classes in its actor file, listed
   in `roster.yaml` (`metaflow/53-actors/` — the human's configuration act,
   never the agent's); changing an approver's authority fields is again
   the human's act.

The five shipped examples are references, never a closed enum.

## Rules

- **Examples are copied, never edited in place** — adopters instantiate
  their own role agents from them (or from `TEMPLATE-new-role/`) into
  `squad/`; the roster never points at `examples/`.
- **Authority lives in structured fields**, never in charter prose — an
  agent with `approves: []` cannot sign, no matter what its prompt says.
- **The wrappers are projected, not hand-written** — the Coordinator
  projects the live definitions in `squad/` into the four platform shapes
  (`.claude/agents/`, `.opencode/agents/`, `.github/agents/`,
  `.codex/agents/`) following the mapping in `VERIFICATION.md`, with the
  N×4 parity check keeping them in sync. The kit ships no pre-built role
  wrappers — the MainAgent installs them in the adopting project.
- **Delete is checked, never blind** — the lifecycle consistency
  contract (the N:1 reference check and the four-leg invariants) lives in
  [`squad/README.md`](squad/README.md).
