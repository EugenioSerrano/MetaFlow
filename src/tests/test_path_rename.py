"""Tests unitarios — renames de rutas (path_rename: M6-M9, B4/B5/B8/B9/B10/B16)."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import transform

MAPPING = Path(__file__).resolve().parents[1] / "mapping.json"
_PATH_RULES = [r for r in transform.render_rules(
    transform.load_mapping(MAPPING).rules, "5.1")
    if r.type == "path_rename"]


class TestPathRename(unittest.TestCase):
    def test_kit_folder(self):
        self.assertEqual(transform.apply_path("avenga-devflow", _PATH_RULES),
                         "ai-sdlc")

    def test_normative_file(self):
        self.assertEqual(transform.apply_path("Avenga-DevFlow.md", _PATH_RULES),
                         "MetaFlow.md")

    def test_wrappers(self):
        self.assertEqual(transform.apply_path("AvengaDevFlow.agent.md", _PATH_RULES),
                         "MetaFlow.agent.md")
        self.assertEqual(transform.apply_path("AvengaDevFlow.md", _PATH_RULES),
                         "MetaFlow.md")

    def test_templates_and_schema(self):
        self.assertEqual(transform.apply_path("TEMPLATE-BOLT.md", _PATH_RULES),
                         "TEMPLATE-TASK.md")
        self.assertEqual(transform.apply_path("TEMPLATE-MANIFEST-BOLT.json", _PATH_RULES),
                         "TEMPLATE-MANIFEST-TASK.json")
        self.assertEqual(transform.apply_path("manifest-v5-bolt.schema.json", _PATH_RULES),
                         "manifest-v1-task.schema.json")
        self.assertEqual(transform.apply_path("manifest-v5-us.schema.json", _PATH_RULES),
                         "manifest-v1-us.schema.json")
        self.assertEqual(transform.apply_path("manifest-v5-tc.schema.json", _PATH_RULES),
                         "manifest-v1-tc.schema.json")

    def test_bolt_ids_and_folders(self):
        self.assertEqual(transform.apply_path("US-012.BOLT-003-invoice.md", _PATH_RULES),
                         "US-012.TASK-003-invoice.md")
        self.assertEqual(transform.apply_path("bolts", _PATH_RULES), "tasks")
        self.assertEqual(transform.apply_path("US-001.BOLT-001-engine.md", _PATH_RULES),
                         "US-001.TASK-001-engine.md")

    def test_unchanged_components(self):
        self.assertEqual(transform.apply_path("devflow", _PATH_RULES), "metaflow")
        self.assertEqual(transform.apply_path("AGENTS.md", _PATH_RULES), "AGENTS.md")


if __name__ == "__main__":
    unittest.main()
