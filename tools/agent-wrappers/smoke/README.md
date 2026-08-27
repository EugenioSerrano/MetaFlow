# Spawn smoke test (US-023.BOLT-004)

Minimal proof on the pilot platform (Claude Code) that the deployed
wrappers (BOLT-003) load and a role agent can be spawned to **take the
baton, produce a trivial artifact of its role, and return control** — the
executor side of the Actor (US-022/023 AC-3) — plus the spawn-topology
confirmation (AC-6).

## What the smoke verifies

1. **Wrapper loads** — the `.claude/agents/*.md` file is readable by
   Claude Code (frontmatter valid).
2. **Spawn with the declared model/tools** — the parent session spawns the
   role agent via the `Agent` tool.
3. **Takes the baton and produces** — the agent writes a trivial artifact
   of its role (a one-line file).
4. **Control returns** — the spawn result comes back to the parent (state
   = files).
5. **Topology (MODEL Y)** — the Coordinator is the platform agent itself
   (its preamble declares the spawn allowlist); the executor's wrapper
   carries no `Agent(...)` tool / `task: deny` (it cannot spawn an
   approver).

## Running

```bash
# from the kit root (so .claude/agents/ is on the session path)
cd distribution-kit
claude -p "Use the developer-agent sub-agent to create the file
<tempdir>/smoke-output.txt containing 'smoke ok', then report the spawn
result and the file contents."
```

The run evidence (spawn outcome, produced artifact, control-return note,
any platform variance) is recorded in the V-Bounce MEM — never fabricated.

## Findings from the first runs (2026-08-23, recorded honestly)

- **Defect found and FIXED in-repo:** the templates shipped
  `model: <pick-from-platform-catalog>` — not a valid model id; any
  adopter's spawn would fail or mis-route. Corrected to
  `model: inherit` (the safe default — follow the session model; adopters
  override per platform catalog) in all five role templates, and the
  wrappers were regenerated.
- **Environmental blocker (not a product defect):** Claude Code registers
  `.claude/agents/` at **session start**. Three `claude -p` runs from the
  kit (workdir `distribution-kit/`) all reported the wrapper as
  well-formed but "Agent type 'developer-agent' not found" — the running
  sessions had loaded their registry before the files existed, and the
  workspace trust dialog had not been accepted (repo-level config is
  ignored in untrusted workspaces). The spawn proof requires a **fresh,
  trusted Claude Code session** with the kit's `.claude/agents/` on the
  project path — i.e., an adopting project (the kit copied to its root) or
  this repo after the workspace is trusted and the session restarted.
- **OpenCode headless (1.18.21):** five attempts (repo-root project, kit
  cwd, an isolated temp adopting project, and a **dedicated `opencode
  serve`** server) all reported "Unknown agent type: developer-agent is
  not a valid agent type" — the `/agent` registry listed only the native
  agents (build, compaction, explore, general, plan, summary, title).
  The custom `.opencode/agents/*.md` files were **not registered in
  headless sessions** (the spawn mechanics themselves were proven with the
  built-in `general` agent: task spawn → produce → control return, all
  real on OpenCode + Deepseek). Registration must be re-verified in an
  **interactive session** (TUI / agent picker) — recorded for the pilot US
  (DISC-002 rec #6).
- The file was **never fabricated** — a negative run is real evidence; a
  faked green would defeat the Bolt's purpose (SPEC-1603 stop condition).

## Expected result

- The wrapper loads (no frontmatter error).
- The spawn returns a result; the artifact file exists with `smoke ok`.
- Known caveat: the templates carry `model: <pick-from-platform-catalog>`
  placeholders — a spawn may require an explicit model override until an
  adopter fills its roster's models. The actual behavior is recorded as
  evidence either way.
