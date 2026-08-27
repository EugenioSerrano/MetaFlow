#!/usr/bin/env python3
"""Generate per-platform wrappers from the canonical DevFlow Agent
definitions (US-023.BOLT-002). Maintainer-run; output is committed to the
kit by the deployment Bolt (BOLT-003).

Usage:
  python generate.py <agents-dir> [--out <output-root>]

Default output: the kit's platform folders under the repo root
(.claude/agents/, .opencode/agents/, .github/agents/, .codex/agents/).
"""

import argparse
import pathlib
import sys

from agentmodel import parse

TOOLS_MAP = {
    "read": "Read", "grep": "Grep", "glob": "Glob", "bash": "Bash",
    "edit": "Edit", "write": "Write",
}

REQUIRED_FIELDS = ("id", "role", "description", "model", "modes",
                   "approves", "capabilities")


def load_definitions(agents_dir: str) -> dict:
    """Return {agent_id: {"data": parsed, "charter": str}}.

    Skips TEMPLATE-* folders — they are skeletons for adopters, not
    agents to wrap (the TEMPLATE-new-role placeholders are not valid
    filenames/id values).
    """
    root = pathlib.Path(agents_dir)
    defs = {}
    for yaml_file in sorted(root.rglob("agent.yaml")):
        if any(part.startswith("TEMPLATE") for part in yaml_file.parts):
            continue
        data = parse(yaml_file.read_text(encoding="utf-8"))
        missing = [f for f in REQUIRED_FIELDS if f not in data]
        if missing:
            raise SystemExit(
                f"FAIL {yaml_file}: missing required fields {missing}")
        if "tier" not in data.get("capabilities", {}):
            raise SystemExit(f"FAIL {yaml_file}: capabilities.tier missing")
        charter_file = yaml_file.parent / "prompt.md"
        if not charter_file.exists():
            charter_file = yaml_file.parent / "charter.md"
        charter = (charter_file.read_text(encoding="utf-8").strip()
                   if charter_file.exists() else "")
        defs[data["id"]] = {"data": data, "charter": charter}
    return defs


def _tools(data: dict) -> str:
    return ", ".join(
        TOOLS_MAP.get(t, t) for t in data["capabilities"].get("tools", []))


def _mcp(data: dict) -> str:
    return ", ".join(data["capabilities"].get("mcp_servers", []))


def build_claude(d: dict, charter: str, spawnable_ids: list) -> str:
    """Claude Code sub-agent (.claude/agents/<id>.md).

    Spawn topology (US-023 AC-6): only the Coordinator carries the Agent
    tool (an allowlist of the role agents); every other wrapper's tools
    omit it — executors cannot spawn approvers.
    """
    tools = [TOOLS_MAP.get(t, t) for t in d["capabilities"].get("tools", [])]
    if d["role"] == "coordinator" and spawnable_ids:
        tools.append(f"Agent({', '.join(spawnable_ids)})")
    lines = ["---",
             f'name: {d["id"]}',
             f'description: {d["description"].strip()}',
             f'tools: {", ".join(tools)}',
             f'model: {d["model"]}']
    mcp = _mcp(d)
    if mcp:
        lines.append(f"mcpServers: {mcp}")
    lines += ["---", "", charter]
    return "\n".join(lines) + "\n"


def build_opencode(d: dict, charter: str, spawnable_ids: list) -> str:
    """OpenCode agent (.opencode/agents/<id>.md).

    Spawn topology (US-023 AC-6): `permission.task` — the Coordinator
    keeps task access (ask); every other agent denies it (the task tool
    disappears from its tool description).
    """
    tools = [t for t in d["capabilities"].get("tools", [])
             if t in ("read", "edit", "bash", "write")]
    perm = {t: "ask" for t in tools} or {"bash": "ask"}
    if d["role"] == "coordinator":
        perm["task"] = "ask"
    else:
        perm["task"] = "deny"
    lines = ["---",
             f'description: {d["description"].strip()}',
             "mode: subagent",
             "temperature: 0.7",
             "permission:"]
    for tool, level in perm.items():
        lines.append(f"  {tool}: {level}")
    lines += ["---", "", charter]
    return "\n".join(lines) + "\n"


def build_github(d: dict, charter: str, spawnable_ids: list) -> str:
    """GitHub Copilot custom agent (.github/agents/<id>.agent.md).

    Spawn topology (US-023 AC-6): only the Coordinator's tools include the
    `agent` alias (agent→agent invocation); the others omit it by
    construction (their tools lists carry only their capability tools).
    """
    tools = list(d["capabilities"].get("tools", []))
    if d["role"] == "coordinator":
        tools.append("agent")
    lines = ["---",
             f'name: {d["id"]}',
             f'description: {d["description"].strip()}',
             f'tools: {", ".join(tools)}',
             f'model: {d["model"]}',
             "---", "", charter]
    return "\n".join(lines) + "\n"


def build_codex(d: dict, charter: str, spawnable_ids: list) -> str:
    """OpenAI Codex role (.codex/agents/<id>.toml).

    Spawn topology (US-023 AC-6): Codex has no native per-agent spawn
    allowlist — the control is instruction-based (the parent/Coordinator
    charter) + role config, recorded in VERIFICATION.md (DISC-002 §4.2
    known gaps).
    """
    esc = charter.replace("\\", "\\\\").replace('"""', '\\"\\"\\"')
    lines = [f'[agents.{d["id"]}]',
             f'description = "{d["description"].strip()}"',
             f'model = "{d["model"]}"',
             "",
             '[agents.{id}.prompt]'.replace("{id}", d["id"]),
             'system = """',
             esc,
             '"""',
             ""]
    return "\n".join(lines) + "\n"


BUILDERS = {
    "claude": (".claude/agents", ".md", build_claude),
    "opencode": (".opencode/agents", ".md", build_opencode),
    "github": (".github/agents", ".agent.md", build_github),
    "codex": (".codex/agents", ".toml", build_codex),
}


def generate(defs: dict, out_root: pathlib.Path) -> list:
    """Write every wrapper; return the list of written paths (relative).

    MODEL Y: only ROLE agents get wrappers. The Coordinator is the
    platform agent itself (CLAUDE.md etc.) — its projections are those
    four main files (hand-synced), NOT a generated sub-agent wrapper.
    """
    written = []
    spawnable_ids = sorted(defs.keys())
    for agent_id, entry in sorted(defs.items()):
        if entry["data"].get("role") == "coordinator":
            continue  # no sub-agent wrapper for the Coordinator (Model Y)
        # The Coordinator's Agent(...) allowlist names the role agents —
        # never itself.
        allow = [i for i in spawnable_ids if i != agent_id]
        for platform, (rel_dir, ext, builder) in BUILDERS.items():
            target_dir = out_root / rel_dir
            target_dir.mkdir(parents=True, exist_ok=True)
            out_file = target_dir / f"{agent_id}{ext}"
            out_file.write_text(
                builder(entry["data"], entry["charter"], allow),
                encoding="utf-8")
            written.append(out_file)
    return written


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("agents_dir", help="the devflow/agents directory")
    ap.add_argument("--out", default=None,
                    help="output root (default: the repo root, so wrappers "
                         "land in the kit's platform folders)")
    args = ap.parse_args(argv)

    cwd = pathlib.Path.cwd()
    default_root = cwd / "distribution-kit"
    if not default_root.is_dir():
        default_root = cwd  # running from inside the kit tree
    out_root = (pathlib.Path(args.out) if args.out else default_root)
    defs = load_definitions(args.agents_dir)
    if not defs:
        print("FAIL: no agent.yaml definitions found", file=sys.stderr)
        return 1
    written = generate(defs, out_root)
    for w in written:
        print(f"wrote {w}")
    print(f"OK: {len(written)} wrappers for {len(defs)} agents x 4 platforms")
    return 0


if __name__ == "__main__":
    sys.exit(main())
