"""Tests — versionado −4 por contexto (AC-1) y neutralización de citas Accelerate (BOLT-003)."""
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
_RULES = transform.render_rules(MAPPING.rules, "5.1")  # reglas resueltas para input 5.1


def content(text: str) -> str:
    # Reglas sin alcance por archivo (path) — imita el filtro de build_plan;
    # la regla V0 (path: metaflow/VERSION) se valida vía el fixture/E2E.
    rules = [r for r in _RULES if not r.path]
    out, _a, _r = transform.apply_content(text, rules)
    return out


class TestVersionContext(unittest.TestCase):
    def test_version_file_by_path(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "out"
            transform.run_transform(KIT_IN, out, MAPPING, dry_run=False)
            self.assertEqual((out / "metaflow" / "VERSION").read_text(encoding="utf-8").strip(),
                             "1.1")

    def test_methodology_version_line(self):
        self.assertEqual(content("**Methodology version:** 5.1"),
                         "**Methodology version:** 1.1")

    def test_agent_version_line(self):
        self.assertEqual(
            content("**Agent version:** 5.1 — implements methodology v5.1"),
            "**Agent version:** 1.1 — implements methodology v1.1")

    def test_heading_and_prose_version(self):
        self.assertEqual(content("# Avenga DevFlow v5.1 (Methodology)"),
                         "# MetaFlow v1.1 (Methodology)")
        self.assertEqual(content("follows the MetaFlow v5.1 methodology"),
                         "follows the MetaFlow v1.1 methodology")
        self.assertEqual(content("(v5.1) — the methodology governs"),
                         "(v1.1) — the methodology governs")

    def test_invariants_section_and_schema_family(self):
        # §5.1 (sección) NO se toca; la familia de manifests SÍ se versiona (5.0 → 1.0)
        self.assertEqual(content('§5.1 stays and schema_version: "5.0" stays'),
                         '§5.1 stays and schema_version: "1.0" stays')

    def test_manifest_family_v1(self):
        self.assertEqual(content("manifest-v5-bolt.schema.json"),
                         "manifest-v1-task.schema.json")
        self.assertEqual(content("manifest-v5-us.schema.json"),
                         "manifest-v1-us.schema.json")
        self.assertEqual(content("Manifest v5"), "Manifest v1")
        self.assertEqual(content('"schema_version": "5.0"'),
                         '"schema_version": "1.0"')
        self.assertEqual(content('"const": "5.0"'), '"const": "1.0"')
        self.assertEqual(content("urn:avenga:devflow:manifest:task:v5"),
                         "urn:metaflow:metaflow:manifest:task:v1")

    def test_generic_rule_future_version_v6(self):
        # La regla es genérica (−4): con input v6 → v2, sin tocar el diccionario
        rules6 = transform.render_rules(MAPPING.rules, "6.1")
        rules6 = [r for r in rules6 if not r.path]
        out, _a, _r = transform.apply_content(
            "**Methodology version:** 6.1 and manifest-v6-us.schema.json and "
            '"schema_version": "6.0"', rules6)
        self.assertEqual(out, "**Methodology version:** 2.1 and "
                              "manifest-v2-us.schema.json and "
                              '"schema_version": "2.0"')
        v6 = {r.id: r for r in rules6}
        self.assertIn("**Methodology version:** 6.1", v6["V1"].pattern)
        self.assertIn("2.1", v6["V1"].replacement)
        self.assertIn("manifest-v6", v6["S1"].pattern)
        self.assertIn("manifest-v2", v6["S1"].replacement)

    def test_accelerate_neutralized_verb_intact(self):
        self.assertEqual(
            content("The longitudinal research synthesized in ***Accelerate*** shows that X."),
            "The longitudinal research on software delivery shows that X.")
        self.assertEqual(content("evidence (*Accelerate* / DORA)."),
                         "evidence (Delivery Flow).")
        self.assertEqual(content("1. Accelerate value delivery using AI."),
                         "1. Accelerate value delivery using AI.")

    @unittest.skipUnless(REAL_KIT.is_dir(), "kit real no presente")
    def test_e2e_real_kit_version_and_invariants(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "out"
            reports = Path(td) / "reports"
            code = transform.main(["--input", str(REAL_KIT), "--output", str(out),
                                   "--reports", str(reports)])
            self.assertEqual(code, 0)
            self.assertEqual((out / "metaflow" / "VERSION").read_text(encoding="utf-8").strip(),
                             "1.1")
            # Versión renombrada en todo el kit
            texts = [p.read_text(encoding="utf-8") for p in out.rglob("*")
                     if p.is_file() and p.suffix in (".md", ".json", ".yaml", ".yml")]
            joined = "\n".join(texts)
            self.assertNotIn("Methodology version: 5.1", joined)
            self.assertNotIn("v5.1", joined)
            # Familia de manifests: nombres y contenido en v1 (nunca v5)
            self.assertNotIn("manifest-v5", joined)
            self.assertIn("manifest-v1-task.schema.json", joined)
            self.assertIn('"schema_version": "1.0"', joined)
            self.assertNotIn('"schema_version": "5.0"', joined)
            self.assertIn("urn:metaflow:metaflow:manifest:task:v1", joined)
            # §5.1: mismo conteo que el input
            def count_sections(root):
                n = 0
                for p in root.rglob("*.md"):
                    n += p.read_text(encoding="utf-8").count("§5.1")
                return n
            self.assertEqual(count_sections(out), count_sections(REAL_KIT))
            # Accelerate: solo el verbo legítimo (1 ocurrencia)
            self.assertEqual(joined.count("Accelerate"), 1)


if __name__ == "__main__":
    unittest.main()
