"""Tests — integridad de links relativos del kit (REV-001 F-02, BOLT-004)."""
import re
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import transform

MAPPING = transform.load_mapping(Path(__file__).resolve().parents[2] / "mapping.json")
FIXTURES = Path(__file__).resolve().parent / "fixtures"
KIT_IN = FIXTURES / "kit-mini"
REAL_KIT = Path(__file__).resolve().parents[2] / "input-kit"

PLACEHOLDER_TARGET = re.compile(
    r"(^|/)(url|example[^/]*\.md|.*Name\.md|Customer\.md|PersonaName\.md|TEMPLATE-REPORT\.html)$",
    re.IGNORECASE)


def check_links(root: Path):
    """Devuelve (total_links, broken). Clasifica y excluye placeholders de templates."""
    total, broken = 0, []
    for p in sorted(root.rglob("*.md")):
        if "TEMPLATE-" in p.name:
            continue  # los templates tienen links de ejemplo
        text = p.read_text(encoding="utf-8")
        for m in re.finditer(r"\[[^\]]*\]\(([^)]+)\)", text):
            target = m.group(1).split("#")[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            if PLACEHOLDER_TARGET.search(target):
                continue
            total += 1
            if not (p.parent / target).resolve().exists():
                broken.append(f"{p.relative_to(root)}: -> {target}")
    return total, broken


class TestLinks(unittest.TestCase):
    def _transform(self, td, kit):
        out = Path(td) / "out"
        code = transform.main(["--input", str(kit), "--output", str(out),
                               "--reports", str(Path(td) / "reports")])
        return code, out

    def test_placeholder_classification(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "TEMPLATE-X.md").write_text("[x](../vision/vision.md)", encoding="utf-8")
            (root / "ok.md").write_text("[y](url) and [z](Customer.md)", encoding="utf-8")
            (root / "real.md").write_text("[broken](../missing/file.md)", encoding="utf-8")
            _total, broken = check_links(root)
            self.assertEqual(len(broken), 1)
            self.assertIn("real.md", broken[0])

    def test_fixture_links_ok(self):
        with tempfile.TemporaryDirectory() as td:
            code, out = self._transform(td, KIT_IN)
            self.assertEqual(code, 0)
            _total, broken = check_links(out)
            self.assertEqual(broken, [])

    @unittest.skipUnless(REAL_KIT.is_dir(), "kit real no presente")
    def test_real_kit_links_ok(self):
        with tempfile.TemporaryDirectory() as td:
            code, out = self._transform(td, REAL_KIT)
            self.assertEqual(code, 0)
            total, broken = check_links(out)
            self.assertEqual(broken, [], f"{len(broken)} links rotos de {total}")


if __name__ == "__main__":
    unittest.main()
