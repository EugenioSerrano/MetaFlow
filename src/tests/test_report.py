"""Tests — reporte de transformación y persistencia de evidencia (AC-8, AC-11)."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import transform
import verify
import report

MAPPING = transform.load_mapping(Path(__file__).resolve().parents[1] / "mapping.json")
FIXTURES = Path(__file__).resolve().parent / "fixtures"
KIT_IN = FIXTURES / "kit-mini"


class TestReport(unittest.TestCase):
    def _run(self, td):
        out = Path(td) / "out"
        plan = transform.run_transform(KIT_IN, out, MAPPING, dry_run=False)
        hits = verify.verify_tree(out)
        rep = report.build_report(plan, KIT_IN, out, hits)
        return out, plan, hits, rep

    def test_report_structure_and_totals(self):
        with tempfile.TemporaryDirectory() as td:
            _out, _plan, hits, rep = self._run(td)
            self.assertEqual(hits, [])
            self.assertTrue(rep["verification"]["ok"])
            self.assertEqual(rep["totals"]["excluded"], 1)      # TEMPLATE-REPORT.html
            self.assertEqual(rep["totals"]["files"], 9)         # 10 input - 1 excluido
            self.assertGreaterEqual(rep["totals"]["changed"], 8)
            self.assertGreaterEqual(rep["totals"]["rules_applied"]["M1"], 1)
            self.assertGreaterEqual(rep["totals"]["removals"]["R1b"], 1)
            self.assertEqual(len(rep["files"]), 10)             # 9 transformados + 1 excluido

    def test_persist_writes_all_artifacts(self):
        with tempfile.TemporaryDirectory() as td:
            out, plan, hits, rep = self._run(td)
            ev = report.persist_evidence(Path(td) / "reports", "fixture", "run-1", rep, plan, KIT_IN, out, hits, log_text="demo log")
            self.assertTrue((ev / "report.json").is_file())
            self.assertTrue((ev / "report.md").is_file())
            self.assertTrue((ev / "run.log").is_file())
            self.assertTrue((ev / "unchanged.txt").is_file())
            self.assertTrue((ev / "removals.json").is_file())
            diffs = list((ev / "diff").glob("*.diff"))
            self.assertGreaterEqual(len(diffs), 1)

    def test_diff_content_shows_rename(self):
        with tempfile.TemporaryDirectory() as td:
            out, plan, hits, rep = self._run(td)
            ev = report.persist_evidence(Path(td) / "reports", "fixture", "run-1", rep, plan, KIT_IN, out, hits)
            agents = ev / "diff" / "AGENTS.md.diff"
            self.assertTrue(agents.is_file())
            diff_text = agents.read_text(encoding="utf-8")
            self.assertIn("-AvengaDevFlow", diff_text)
            self.assertIn("+MetaFlow", diff_text)

    def test_evidence_additive_never_deleted(self):
        with tempfile.TemporaryDirectory() as td:
            out, plan, hits, rep = self._run(td)
            reports = Path(td) / "reports"
            report.persist_evidence(reports, "fixture", "run-1", rep, plan, KIT_IN, out, hits)
            report.persist_evidence(reports, "fixture", "run-2", rep, plan, KIT_IN, out, hits)
            self.assertTrue((reports / "fixture" / "run-1").is_dir())
            self.assertTrue((reports / "fixture" / "run-2").is_dir())

    def test_prune_keeps_last_two(self):
        with tempfile.TemporaryDirectory() as td:
            out, plan, hits, rep = self._run(td)
            reports = Path(td) / "reports"
            for rid in ("run-1", "run-2", "run-3"):
                report.persist_evidence(reports, "fixture", rid, rep, plan, KIT_IN, out, hits)
            pruned = report.prune_runs(reports, "fixture", keep=2)
            self.assertEqual(pruned, ["run-1"])
            self.assertTrue((reports / "fixture" / "run-2").is_dir())
            self.assertTrue((reports / "fixture" / "run-3").is_dir())
            self.assertFalse((reports / "fixture" / "run-1").exists())


if __name__ == "__main__":
    unittest.main()
