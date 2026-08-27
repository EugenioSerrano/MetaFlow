# Per-platform verification and usage notes

Status of the deployed role-agent wrappers per platform, re-verified
against current docs at implementation time. If a platform contract
changed since this note was written, regenerate the wrappers from the
canonical definitions and re-run the parity check.

## Canonical → wrapper mapping (field-level)

The wrappers project the canonical `agent.yaml` fields into each
platform's format. This table is the reference a MainAgent reads to
install or refresh a wrapper for its own platform. The charter body
(`prompt.md` / `charter.md`) becomes the wrapper body.

| Canonical field | Claude Code | OpenCode | GitHub Copilot | OpenAI Codex |
|-----------------|-------------|----------|----------------|--------------|
| `id` | `name:` (frontmatter) | filename `<id>.md` | `name:` (frontmatter) | `[agents.<id>]` key |
| `description` | `description:` | `description:` | `description:` | `description = "..."` |
| `model` | `model:` | session default | `model:` | `model = "..."` |
| `capabilities.tools` | `tools:` (mapped Read/Grep/Glob/Bash/Edit/Write) | `permission:` (`read`/`edit`/`bash`/`write`: ask) | `tools:` | role config |
| `capabilities.mcp_servers` | `mcpServers:` (only when named) | permission globs | `mcp-servers:` (not in IDEs) | config layer |
| `approves` / `modes` | charter body | charter body | charter body | charter body (system prompt) |
| charter body | body after `---` | body after `---` | body after `---` | `[agents.<id>.prompt] system = """..."""` |

### The permission-block derivation (deterministic)

A wrapper's permission set derives **only** from the definition's
`capabilities.tools` allowlist: each listed tool maps to its platform
permission per the table above, and **every tool absent from the allowlist
is explicitly denied** — nothing (`list`, `webfetch`, `websearch`, `task`
included) enters a wrapper without canonical backing.
Reviewer/approver-class agents (a non-empty `approves`, or a reviewer
charter) additionally deny `bash`, `edit`, `write`, `task` and the web
tools — the approver ceiling encoded at the wrapper level. Two projections
of one definition must be **byte-comparable**.

**`model: inherit`** is not a catalog value — at projection time the
wrapper **omits the model field entirely**, so each platform natively uses
its session/default model (deterministic and portable across the four).
Reviewer/approver-class agents should **pin a distinct model** from the
session's (model diversity — a model reviewing its own work is too
complacent).

**Spawn topology:** only the Coordinator (the platform agent itself) may
spawn role agents — Claude Code `Agent(...)` allowlist in the main
agent's preamble; OpenCode `permission.task`; Copilot the `agent` alias;
Codex instruction-based. The role wrappers carry no spawn capability
(`task: deny` / no `Agent` tool / no `agent` alias).

**Execution evidence (attribution integrity):** an executor's production
may be persisted by the Coordinator (the shape where an executor with
`write_paths: []` still produces — the Coordinator persists its output),
but the persistence act must trace to a **real spawn**: a stamp of another
actor's identity on content that actor never produced is a false claim,
not governed authorship. When spawn is unavailable, direct human
invocation is the only legitimate reviewer session. Evidence = the spawn
trace / the separate session / the commit history — never the `author:`
field alone.

## How the agents are installed and used

- The kit ships the **example definitions and the templates**
  (`devflow/agents/examples/`, `agents/TEMPLATE-new-role/`) and this
  **mapping**; it does **not** ship pre-built role wrappers. The project's
  **live definitions live in `devflow/agents/squad/`**. The
  **Coordinator** — the AvengaDevFlow MainAgent itself, one per tool —
  **installs and refreshes its platform's wrappers** into the project's
  platform folders (`.claude/agents/`, `.opencode/agents/`,
  `.github/agents/`, `.codex/agents/`) by projecting the live
  `agent.yaml` from `squad/` per the mapping above (the agent lifecycle,
  a governed operational act).
- Each platform loads its agent files from those folders **at session
  start** — after an install (or a wrapper change), start a fresh session
  so the new agents register.
- The role agents are spawned by the **Coordinator** — the Avenga DevFlow
  platform agent itself, evolved: the shared methodology body and each
  platform preamble declare the orchestrator identity (routes, delegates
  production, spawns approvers, records — **never signs**; the spawn
  topology per platform).

## Claude Code — full native coverage ✅

- **Folder:** `.claude/agents/*.md` — loaded from the project root at
  session start (the workspace trust dialog must be accepted for
  repo-level agents).
- Per-agent `model`, `tools` allowlist, `mcpServers`, hooks and spawn
  allowlists: all supported.
- **Spawn topology:** only the Coordinator carries the `Agent` tool; the
  role wrappers omit it, so executors cannot spawn approvers — approver
  agents are spawnable only through the Coordinator (or by a human).
- The approver ceiling (T0/T1) and the MCP allowlist are encoded in the
  canonical fields the wrappers project.

## OpenCode — solid, with the task gate ✅

- **Folder:** `.opencode/agents/*.md` — loaded from the project at
  session start.
- `permission` globs per tool supported.
- **Spawn topology:** `permission.task` — the Coordinator (the main
  agent) keeps it; every role wrapper carries `task: deny` (the task tool
  disappears from its description), so executors cannot spawn.
- **Picker behavior:** the Tab picker lists **primary agents only** —
  subagents (`mode: subagent`) are visible via ctrl+X / `opencode agent
  list` and are invoked through the Coordinator's task tool (the spawn
  topology working as designed). A session reload registers new agents.
- **Re-verification finding (2026-08-23, OpenCode 1.18.21):** in
  **headless** sessions (`opencode run` / `opencode serve`), the custom
  agent files were **not registered** — the `/agent` registry listed only
  the native agents (build, compaction, explore, general, plan, summary,
  title). The spawn mechanics themselves work (task spawn → produce →
  control return, proven with the built-in `general` agent). Registration
  must be re-verified in an **interactive session** (TUI / agent picker).
- No native audit hooks — noted, not blocking.

## GitHub Copilot — viable with environment caveats 🟡

- **Folder:** `.github/agents/*.agent.md` — repo-level custom agents.
- **Spawn topology:** the Coordinator's frontmatter `tools:` includes the
  `agent` alias (agent→agent invocation — the platform's canonical
  agent-invocation tool); the role wrappers omit it by construction —
  executors cannot invoke approvers. **Agent-initiated spawn requires the
  `agent` tool in the Coordinator's tools** — without it, delegated work
  is silently self-executed (verified 2026-08-25: a Coordinator without
  the tool ran the delegated review itself and stamped the reviewer's
  identity on the result).
- **Wrapper visibility:** role wrappers are **user-invocable by default**
  (they appear in the agent dropdown); set `user-invocable: false` in the
  wrapper for subagent-only visibility (the OpenCode `mode: subagent`
  equivalent). Direct human invocation of a role agent is legitimate —
  the spawn topology only governs agent-initiated invocation.
- **Post-edit validation:** validate the roster after an agent edit — the
  edit tool may write TAB indentation that strict YAML parsers reject
  (observed 2026-08-25: an agent-written roster failed PyYAML scanning
  while rendering fine in the IDE).
- Caveats (re-verify at implementation): `model` and `mcp-servers` are
  environment-dependent (VS Code / JetBrains / Eclipse / Xcode) and
  `mcp-servers` is not honored in IDEs; the 30,000-char prompt cap
  documented by GitHub applies to the **cloud agent** — the full agent
  body (≈68.9k chars; the whole file ≈69.6k) verified loading in VS Code
  (2026-08-25); re-verify per environment.

## OpenAI Codex — right primitives, known gaps 🟡

- **Folder:** `.codex/agents/*.toml` — role files with full config
  override (model, reasoning, sandbox).
- **Spawn topology:** no native per-agent spawn allowlist — the control
  is instruction-based (the Coordinator's charter: "approver agents are
  reachable only through me") + role `config_file`. The weakest platform
  control; re-verify when the platform adds allowlists.
- Known invocation gaps (open issues #14579/#15250): repo-local custom
  agents may not be invocable by name from tool-backed sessions — the
  documented fallback is the generic `agent_type` + explicit overrides.

## Parity

The N×4 parity check (regenerate the wrappers from the canonical
definitions and diff against the committed set) must PASS (0 drift) after
every regeneration. **Never hand-edit a generated wrapper** — fix the
generator or the canonical definition instead.
