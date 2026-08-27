"""Tests — CLI: dry-run, ejecución real, borrado de salida, exit codes."""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import transform

MAPPING = transform.load_mapping(Path(__file__).resolve().parents[2] / "mapping.json")
FIXTURES = Path(__file__).resolve().parent / "fixtures"
KIT_IN = FIXTURES / "kit-mini"
KIT_EXPECTED = FIXTURES / "kit-mini-expected"


def compare_trees(expected: Path, actual: Path):
    """Cada archivo del expected debe existir en actual con el mismo contenido."""
    for exp in sorted(expected.rglob("*")):
        rel = exp.relative_to(expected)
        act = actual / rel
        if exp.is_dir():
            assert act.is_dir(), f"falta carpeta {rel}"
        else:
            assert act.is_file(), f"falta archivo {rel}"
            assert act.read_text(encoding="utf-8") == exp.read_text(encoding="utf-8"), \
                f"contenido distinto en {rel}"


class TestCli(unittest.TestCase):
    def test_dry_run_writes_nothing(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "out"
            plan = transform.run_transform(KIT_IN, out, MAPPING, dry_run=True)
            self.assertFalse(out.exists())
            self.assertTrue(any(e.get("kind") == "file" for e in plan))

    def test_real_run_matches_expected_tree(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "out"
            transform.run_transform(KIT_IN, out, MAPPING, dry_run=False)
            compare_trees(KIT_EXPECTED, out)

    def test_real_run_cleans_previous_output(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "out"
            out.mkdir()
            (out / "stale.txt").write_text("residuo de corrida anterior", encoding="utf-8")
            transform.run_transform(KIT_IN, out, MAPPING, dry_run=False)
            self.assertFalse((out / "stale.txt").exists())
            self.assertTrue((out / "AGENTS.md").is_file())

    def test_refuses_output_inside_input(self):
        with tempfile.TemporaryDirectory() as td:
            inp = Path(td) / "in"
            inp.mkdir()
            bad = inp / "out"
            with self.assertRaises(transform.TransformError):
                transform.run_transform(inp, bad, MAPPING, dry_run=False)

    def test_missing_mapping_exit_1(self):
        self.assertEqual(
            transform.main(["--mapping", "no-such-mapping.json",
                            "--input", str(KIT_IN), "--output", "x"]), 1)

    def test_invalid_mapping_semantic_exit_2(self):
        with tempfile.TemporaryDirectory() as td:
            bad = Path(td) / "bad.json"
            bad.write_text('{"rules": [{"id": "X1", "type": "magic", "pattern": "a", "order": 1}]}',
                           encoding="utf-8")
            self.assertEqual(
                transform.main(["--mapping", str(bad),
                                "--input", str(KIT_IN), "--output", "x"]), 2)

    def test_cli_dry_run_exit_0(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "out"
            code = transform.main(["--dry-run", "--input", str(KIT_IN), "--output", str(out)])
            self.assertEqual(code, 0)
            self.assertFalse(out.exists())


if __name__ == "__main__":
    unittest.main()
