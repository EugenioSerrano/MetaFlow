"""Tests — verificador de tokens prohibidos (AC-7)."""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import verify


def make_kit(files: dict, root: Path) -> Path:
    for rel, content in files.items():
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
    return root


class TestVerify(unittest.TestCase):
    def test_clean_kit_zero_hits(self):
        with tempfile.TemporaryDirectory() as td:
            kit = make_kit({"AGENTS.md": "MetaFlow is the methodology.\nCP-SPEC-Approval.\n"},
                           Path(td))
            self.assertEqual(verify.verify_tree(kit), [])

    def test_exact_tokens_detected(self):
        with tempfile.TemporaryDirectory() as td:
            kit = make_kit({"a.md": "AvengaDevFlow remains\nV-Bounce and v_bounces\n"},
                           Path(td))
            hits = verify.verify_tree(kit)
            joined = " | ".join(f"{h['token']}" for h in hits)
            self.assertIn("avenga", joined.lower())
            self.assertIn("v-bounce", joined.lower())

    def test_case_variants_detected(self):
        with tempfile.TemporaryDirectory() as td:
            kit = make_kit({"a.md": "AVENGA ALL CAPS\nAITL\nHITL\nBOLT\nDORA\n"}, Path(td))
            hits = verify.verify_tree(kit)
            self.assertGreaterEqual(len(hits), 5)

    def test_paths_scanned(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            kit = root / "avenga-devflow"
            kit.mkdir(parents=True)
            (kit / "x.md").write_text("clean", encoding="utf-8")
            hits = verify.verify_tree(root)
            self.assertTrue(any("path" in h.get("where", "") for h in hits))

    def test_word_boundary_bolt(self):
        with tempfile.TemporaryDirectory() as td:
            kit = make_kit({"a.md": "thunderbolt is fine\n"}, Path(td))
            self.assertEqual(verify.verify_tree(kit), [])

    def test_devflow_any_form_detected(self):
        with tempfile.TemporaryDirectory() as td:
            kit = make_kit({"a.md": "devflow/ and DevFlow and DEVFLOW\n"}, Path(td))
            hits = verify.verify_tree(kit)
            self.assertGreaterEqual(len(hits), 3)

    def test_empty_folder_name_detected(self):
        # Los nombres de carpetas se barren incluso sin archivos adentro
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "avenga-devflow").mkdir()
            hits = verify.verify_tree(root)
            self.assertTrue(any(h["where"] == "path" and "avenga" in h["context"]
                                for h in hits))

    def test_file_name_detected(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "clean").mkdir()
            (root / "clean" / "V-Bounce.md").write_text("ok", encoding="utf-8")
            hits = verify.verify_tree(root)
            self.assertTrue(any(h["where"] == "path" for h in hits))


if __name__ == "__main__":
    unittest.main()
