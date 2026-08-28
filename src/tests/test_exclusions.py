"""Tests — exclusiones: archivos que no se migran (lista `exclude` del mapping)."""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import transform

MAPPING = transform.load_mapping(Path(__file__).resolve().parents[1] / "mapping.json")
FIXTURES = Path(__file__).resolve().parent / "fixtures"
KIT_IN = FIXTURES / "kit-mini"


class TestExclusions(unittest.TestCase):
    def test_excluded_file_absent_from_output(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "out"
            plan = transform.run_transform(KIT_IN, out, MAPPING, dry_run=False)
            self.assertFalse((out / "devflow" / "reports" / "TEMPLATE-REPORT.html").exists())
            self.assertFalse((out / "devflow" / "reports").exists())

    def test_exclusion_recorded_in_plan(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "out"
            plan = transform.run_transform(KIT_IN, out, MAPPING, dry_run=False)
            excluded = [e for e in plan if e.get("kind") == "excluded"]
            self.assertEqual(len(excluded), 1)
            self.assertEqual(excluded[0]["src"].name, "TEMPLATE-REPORT.html")

    def test_dry_run_lists_exclusion_without_writing(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "out"
            plan = transform.run_transform(KIT_IN, out, MAPPING, dry_run=True)
            excluded = [e for e in plan if e.get("kind") == "excluded"]
            self.assertEqual(len(excluded), 1)
            self.assertFalse(out.exists())


if __name__ == "__main__":
    unittest.main()
