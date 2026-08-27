# agent-wrappers — canonical DevFlow Agent definitions → per-platform wrappers

Maintainer-run tooling (US-023.BOLT-002). Projects the canonical
`agent.yaml` definitions (`distribution-kit/devflow/agents/`) into the
four platform wrapper shapes and verifies the **N×4 parity** — the
four-agent sync philosophy extended to N roles × 4 platforms.

## Why

The wrappers must stay in sync with the canonical definitions forever — a
hand-maintained set would drift (the AREV-001 F-01 failure mode made
mechanical). Adopters copy the kit wholesale: the wrappers ship
pre-built, no adoption-time generation (DISC-002 §5.5).

## The four shapes (DISC-002 §4.2, re-verified at implementation)

| Platform | Location | Shape |
|----------|----------|-------|
| Claude Code | `.claude/agents/<id>.md` | frontmatter: `name`/`description`/`tools`/`model`/`mcpServers` + charter body |
| OpenCode | `.opencode/agents/<id>.md` | frontmatter: `description`/`mode: subagent`/`temperature` + `permission` + charter body |
| GitHub Copilot | `.github/agents/<id>.agent.md` | frontmatter: `name`/`description`/`tools`/`model` + charter body |
| OpenAI Codex | `.codex/agents/<id>.toml` | `[agents.<id>]` section: `description`/`model` + the charter as the system prompt |

**MODEL Y (the Coordinator is NOT generated):** only the **ROLE agents**
get wrappers. The Coordinator is the platform agent itself (the
AvengaDevFlow files — CLAUDE.md, `.agents/skills/…`, `.github/agents/…`,
`.opencode/agents/…`); its projections are those four main files, which
carry the orchestrator identity (spawn allowlist + never-signs) in their
preambles/shared body. The generator skips `role: coordinator`
definitions — no separate coordinator sub-agent wrapper is produced
(ADR-007 §3.4, DISC-002 §5.2).

**Known gaps (recorded, not assumed):** Codex has open invocation issues
for repo-local custom agents from tool-backed sessions (#14579/#15250) —
the wrapper is generated with the documented fallback (generic
`agent_type` + explicit overrides noted in the deployment notes).
Copilot's `model`/`mcp-servers` are environment-dependent (IDEs) — the
frontmatter carries them with a note. Re-verify both against current docs
at every implementation pass (DISC-002 rec #6).

## Running

```bash
# generate (default target: distribution-kit/ — the kit's platform folders)
python tools/agent-wrappers/generate.py distribution-kit/devflow/agents

# generate into an explicit output tree (used by the deployment Bolt)
python tools/agent-wrappers/generate.py distribution-kit/devflow/agents --out /tmp/wrappers

# parity: regenerate into a temp dir and diff against the committed set
python tools/agent-wrappers/parity.py distribution-kit/devflow/agents distribution-kit

# tests
python -m unittest discover -s tools/agent-wrappers/tests
```

## Design notes

- **Dependency-free:** a small deterministic parser (`agentmodel.py`)
  handles the canonical `agent.yaml` subset (comments, `key: value`,
  `key: >` blocks, inline lists, dash lists, one nested map level) — no
  PyYAML requirement, so the tool runs anywhere.
- **The charter body** comes from the role's `prompt.md` (the Coordinator
  keeps `charter.md`).
- **Never hand-edit the generated wrappers** — the parity check fails on
  drift; fix the generator or the canonical definition instead.
