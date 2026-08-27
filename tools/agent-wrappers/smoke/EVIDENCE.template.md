# Smoke evidence template (US-023.BOLT-004 — human-run)

Fill this template when running the smoke in a **trusted environment**
(see the runbook). Append the filled file (or its content) to the V-Bounce
MEM / the Bolt's evidence. **Never fabricate a result** — a negative run is
real evidence; a faked green defeats the Bolt's purpose.

## Run metadata

| Field | Value |
|-------|-------|
| Date/time | |
| Platform | Claude Code (interactive session) |
| Project root | (the adopting project — must have `.claude/agents/` on the session path) |
| Workspace trust | (trust dialog accepted / `hasTrustDialogAccepted: true`) |
| Agent under test | developer-agent (or another role agent) |
| Run command | (from the runbook) |

## 1. Wrapper loads

- [ ] `.claude/agents/developer-agent.md` was picked up (no frontmatter
      error; the agent appears in the available-agents list / agent picker)
- Note: ____

## 2. Spawn with the declared model/tools

- [ ] The Coordinator (parent) spawned the role agent via the Agent tool
- [ ] Declared model honored (`model: inherit` → the session model) —
      note the actual model: ____
- Note: ____

## 3. Takes the baton and produces

- [ ] The role agent produced a trivial artifact of its role (file path: ____)
- [ ] Artifact content verified: ____

## 4. Control returns

- [ ] The spawn result returned to the parent (state = files; usage/tokens
      reported where the platform provides them)
- Note: ____

## 5. Topology

- [ ] The executor's wrapper carries no `Agent(...)` tool (Claude) /
      `task: deny` (OpenCode) — approver spawning stays Coordinator-only
- Note: ____

## Result

- **PASS / FAIL / PARTIAL** — with the honest details above.
- Signed: ____ (the human who ran it — the executing Dev-validator or the
  pilot US operator)
