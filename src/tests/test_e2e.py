"""Tests — E2E: pipeline completo (fixture y kit real) con verificador y evidencia (AC-9)."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import transform

MAPPING = transform.load_mapping(Path(__file__).resolve().parents[2] / "mapping.json")
FIXTURES = Path(__file__).resolve().parent / "fixtures"
KIT_IN = FIXTURES / "kit-mini"
KIT_LEFTOVER = FIXTURES / "kit-leftover"
REAL_KIT = Path(__file__).resolve().parents[2] / "input-kit"


class TestE2E(unittest.TestCase):
    def test_fixture_full_pipeline_ok(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "out"
            reports = Path(td) / "reports"
            code = transform.main(["--input", str(KIT_IN), "--output", str(out),
                                   "--reports", str(reports)])
            self.assertEqual(code, 0)
            # evidencia persistida (versión del fixture: devflow/VERSION = 5.1)
            runs = list((reports / "5.1").glob("20*"))
            self.assertEqual(len(runs), 1)
            rep = json.loads((runs[0] / "report.json").read_text(encoding="utf-8"))
            self.assertTrue(rep["verification"]["ok"])
            self.assertTrue((runs[0] / "diff").is_dir())

    def test_leftover_fails_run(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "out"
            reports = Path(td) / "reports"
            code = transform.main(["--input", str(KIT_LEFTOVER), "--output", str(out),
                                   "--reports", str(reports)])
            self.assertEqual(code, 1)  # AC-7: run falla con exit != 0
            runs = list((reports / "unknown").glob("20*"))
            rep = json.loads((runs[0] / "report.json").read_text(encoding="utf-8"))
            self.assertFalse(rep["verification"]["ok"])
            self.assertGreaterEqual(len(rep["verification"]["hits"]), 1)

    @unittest.skipUnless(REAL_KIT.is_dir(), "kit real no presente")
    def test_real_kit_acceptance_zero_hits(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "out"
            reports = Path(td) / "reports"
            code = transform.main(["--input", str(REAL_KIT), "--output", str(out),
                                   "--reports", str(reports)])
            self.assertEqual(code, 0, "el kit real debe transformar con cero tokens prohibidos")


if __name__ == "__main__":
    unittest.main()
