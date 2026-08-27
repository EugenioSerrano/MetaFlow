"""Unit tests for the wrapper generator (US-023.BOLT-002)."""

import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

from agentmodel import parse
from generate import (build_claude, build_codex, build_github,
                      build_opencode, load_definitions, generate)

SAMPLE = """\
# comment line
id: qa-agent
role: qa
description: >
  Verifies V-Bounce packages against ACs and gates.
model: claude-opus-5
modes: [executor, approver]
approves: [MEM]            # inline comment
capabilities:
  tier: T1
  tools: [read, grep, glob, bash, edit, write]
  mcp_servers: []
escalation:
  - "evidence missing"
  - "gate overridden"
write_paths: ["devflow/tests/"]
"""


class TestParser(unittest.TestCase):
    def test_parses_canonical_subset(self):
        d = parse(SAMPLE)
        self.assertEqual(d["id"], "qa-agent")
        self.assertEqual(d["role"], "qa")
        self.assertIn("Verifies V-Bounce packages", d["description"])
        self.assertEqual(d["modes"], ["executor", "approver"])
        self.assertEqual(d["approves"], ["MEM"])
        self.assertEqual(d["capabilities"]["tier"], "T1")
        self.assertEqual(d["capabilities"]["tools"],
                         ["read", "grep", "glob", "bash", "edit", "write"])
        self.assertEqual(d["capabilities"]["mcp_servers"], [])
        self.assertEqual(d["escalation"], ["evidence missing",
                                           "gate overridden"])
        self.assertEqual(d["write_paths"], ["devflow/tests/"])

    def test_empty_inline_list(self):
        self.assertEqual(parse("approves: []\n")["approves"], [])

    def test_comment_stripping(self):
        d = parse("model: claude-opus-5 # pick from catalog\n")
        self.assertEqual(d["model"], "claude-opus-5")


class TestBuilders(unittest.TestCase):
    def setUp(self):
        self.d = parse(SAMPLE)  # qa-agent (non-coordinator)
        self.spawnable = ["fa-agent", "qa-agent"]

    def test_claude_frontmatter(self):
        out = build_claude(self.d, "charter", self.spawnable)
        self.assertIn("name: qa-agent", out)
        self.assertIn("model: claude-opus-5", out)
        self.assertIn("tools: Read, Grep, Glob, Bash, Edit, Write", out)
        self.assertNotIn("mcpServers", out)  # [] default → omitted
        self.assertNotIn("Agent(", out)  # non-coordinator cannot spawn
        self.assertTrue(out.endswith("charter\n"))

    def test_claude_coordinator_has_agent_allowlist(self):
        coord = parse(SAMPLE.replace("id: qa-agent", "id: coordinator")
                           .replace("approves: [MEM]", "approves: []")
                           .replace("role: qa", "role: coordinator"))
        out = build_claude(coord, "charter", self.spawnable)
        self.assertIn("Agent(fa-agent, qa-agent)", out)

    def test_claude_mcp_present_when_named(self):
        d = parse(SAMPLE.replace("mcp_servers: []", "mcp_servers: [jira]"))
        self.assertIn("mcpServers: jira",
                      build_claude(d, "charter", self.spawnable))

    def test_opencode_permission(self):
        out = build_opencode(self.d, "charter", self.spawnable)
        self.assertIn("mode: subagent", out)
        self.assertIn("  read: ask", out)
        self.assertIn("  bash: ask", out)
        self.assertIn("  task: deny", out)  # non-coordinator cannot spawn

    def test_opencode_coordinator_keeps_task(self):
        coord = parse(SAMPLE.replace("id: qa-agent", "id: coordinator")
                           .replace("role: qa", "role: coordinator"))
        out = build_opencode(coord, "charter", self.spawnable)
        self.assertIn("  task: ask", out)

    def test_github_frontmatter(self):
        out = build_github(self.d, "charter", self.spawnable)
        self.assertIn("name: qa-agent", out)
        self.assertIn("model: claude-opus-5", out)
        self.assertNotIn("agent", out.splitlines()[4])  # no agent alias

    def test_codex_toml(self):
        out = build_codex(self.d, 'system "prompt"', self.spawnable)
        self.assertIn("[agents.qa-agent]", out)
        self.assertIn('model = "claude-opus-5"', out)
        self.assertIn('system = """', out)
        self.assertIn('system "prompt"', out)


class TestEndToEnd(unittest.TestCase):
    def test_generate_and_load(self):
        with tempfile.TemporaryDirectory() as td:
            agents = pathlib.Path(td) / "agents"
            (agents / "roles" / "qa").mkdir(parents=True)
            (agents / "roles" / "qa" / "agent.yaml").write_text(
                SAMPLE, encoding="utf-8")
            (agents / "roles" / "qa" / "prompt.md").write_text(
                "charter", encoding="utf-8")
            defs = load_definitions(str(agents))
            self.assertEqual(list(defs), ["qa-agent"])
            out_root = pathlib.Path(td) / "out"
            written = generate(defs, out_root)
            self.assertEqual(len(written), 4)
            self.assertTrue(
                (out_root / ".claude" / "agents" / "qa-agent.md").exists())
            self.assertTrue(
                (out_root / ".codex" / "agents" / "qa-agent.toml").exists())

    def test_coordinator_not_generated(self):
        """MODEL Y: the Coordinator is the platform agent itself — the
        generator produces NO coordinator sub-agent wrapper."""
        with tempfile.TemporaryDirectory() as td:
            agents = pathlib.Path(td) / "agents"
            (agents / "roles" / "coordinator").mkdir(parents=True)
            (agents / "roles" / "coordinator" / "agent.yaml").write_text(
                "id: coordinator\nrole: coordinator\n"
                "description: >\n  The orchestrator.\nmodel: inherit\n"
                "modes: [executor]\napproves: []\ncapabilities:\n"
                "  tier: T1\n  tools: [read]\n  mcp_servers: []\n",
                encoding="utf-8")
            (agents / "roles" / "coordinator" / "charter.md").write_text(
                "charter", encoding="utf-8")
            defs = load_definitions(str(agents))
            out_root = pathlib.Path(td) / "out"
            written = generate(defs, out_root)
            self.assertEqual(written, [])  # nothing generated for the coordinator

    def test_template_folder_skipped(self):
        """TEMPLATE-* folders are skeletons, never wrapped (their
        placeholders are not valid filenames)."""
        with tempfile.TemporaryDirectory() as td:
            agents = pathlib.Path(td) / "agents"
            (agents / "roles" / "TEMPLATE-new-role").mkdir(parents=True)
            (agents / "roles" / "TEMPLATE-new-role" / "agent.yaml").write_text(
                "id: <your-agent-id>\nrole: <your-role>\n", encoding="utf-8")
            (agents / "roles" / "qa").mkdir(parents=True)
            (agents / "roles" / "qa" / "agent.yaml").write_text(
                SAMPLE, encoding="utf-8")
            (agents / "roles" / "qa" / "prompt.md").write_text(
                "charter", encoding="utf-8")
            defs = load_definitions(str(agents))
            self.assertEqual(list(defs), ["qa-agent"])  # template skipped

    def test_missing_required_field_fails(self):
        with tempfile.TemporaryDirectory() as td:
            agents = pathlib.Path(td) / "agents"
            (agents / "roles" / "x").mkdir(parents=True)
            (agents / "roles" / "x" / "agent.yaml").write_text(
                "id: x\nrole: qa\n", encoding="utf-8")
            with self.assertRaises(SystemExit):
                load_definitions(str(agents))


if __name__ == "__main__":
    unittest.main()
