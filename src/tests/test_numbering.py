"""Tests — numeración de carpetas internas del kit (ADR-003, BOLT-005).

Las reglas de contenido numeran SOLO referencias de ruta (`nombre/`); la
palabra suelta en prosa y los enums de schemas quedan intactos.
"""
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import transform

MAPPING = transform.load_mapping(Path(__file__).resolve().parents[1] / "mapping.json")
_RULES = [r for r in transform.render_rules(MAPPING.rules, "5.1") if not r.path]
_PATH = [r for r in transform.render_rules(MAPPING.rules, "5.1")
         if r.type == "path_rename" or (r.scope in ("path", "both") and r.type == "regex_rename")]
REAL_KIT = Path(__file__).resolve().parents[2] / "input-kit"

SCHEME = [("01", "input", "input"), ("02", "analysis", "analysis"),
          ("03", "discovery", "discovery"), ("11", "adrs", "adrs"),
          ("12", "functional", "functional"), ("13", "bugs", "bugs"),
          ("21", "spec", "spec"), ("22", "memory", "memory"),
          ("23", "metrics", "metrics"), ("24", "tests", "tests"),
          ("31", "reviews", "reviews"), ("32", "adversarial-reviews", "adv-reviews"),
          ("33", "risks", "risks"), ("34", "incidents", "incidents"),
          ("35", "retros", "retros"), ("41", "prompts", "prompts"),
          ("42", "reports", "reports"), ("51", "agents", "agents"),
          ("52", "agents-data", "agents-data"), ("53", "actors", "actors")]


def content(text: str) -> str:
    out, _a, _r = transform.apply_content(text, _RULES)
    return out


class TestNumbering(unittest.TestCase):
    def test_all_20_numbered_as_paths(self):
        text = " ".join(f"{_src}/" for _p, _src, _dst in SCHEME)
        out = content(text)
        for prefix, _src, dst in SCHEME:
            self.assertIn(f"{prefix}-{dst}/", out)

    def test_prose_intact(self):
        # La palabra suelta NO se numera (REV-002 F-04)
        self.assertEqual(content("functional analyst stays, run the tests, "
                                 "the memory, risks of X, inputs"),
                         "functional analyst stays, run the tests, "
                                 "the memory, risks of X, inputs")

    def test_substring_protection(self):
        self.assertEqual(content("analysis/business-risks/ stays"),
                         "02-analysis/business-risks/ stays")
        self.assertEqual(content("adversarial-reviews/ and reviews/"),
                         "32-adv-reviews/ and 31-reviews/")
        self.assertEqual(content("agents-data/ and agents/"),
                         "52-agents-data/ and 51-agents/")

    def test_plural_and_field_names_protected(self):
        self.assertEqual(content("inputs and spec_revisions and test_bolts"),
                         "inputs and spec_revisions and test_tasks")

    def test_path_components(self):
        self.assertEqual(transform.apply_path("input", _PATH), "01-input")
        self.assertEqual(transform.apply_path("business-risks", _PATH), "business-risks")
        self.assertEqual(transform.apply_path("agents-data", _PATH), "52-agents-data")
        self.assertEqual(transform.apply_path("adversarial-reviews", _PATH), "32-adv-reviews")
        self.assertEqual(transform.apply_path("reviews", _PATH), "31-reviews")
        self.assertEqual(transform.apply_path("tests", _PATH), "24-tests")
        self.assertEqual(transform.apply_path("ai-sdlc", _PATH), "ai-sdlc")

    @unittest.skipUnless(REAL_KIT.is_dir(), "kit real no presente")
    def test_e2e_real_renumbered_clean(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "out"
            code = transform.main(["--input", str(REAL_KIT), "--output", str(out),
                                   "--reports", str(Path(td) / "reports")])
            self.assertEqual(code, 0)
            folders = {p.name for p in (out / "metaflow").iterdir() if p.is_dir()}
            for prefix, _src, dst in SCHEME:
                self.assertIn(f"{prefix}-{dst}", folders, f"falta {prefix}-{dst}")
            self.assertIn("ai-sdlc", folders)
            self.assertNotIn("32-adversarial-reviews", folders)

            # BUG-001: las carpetas ocultas de plataforma NO se numeran
            self.assertTrue((out / ".github" / "agents" / "MetaFlow.agent.md").is_file(),
                            "falta .github/agents/MetaFlow.agent.md")
            self.assertTrue((out / ".opencode" / "agents" / "MetaFlow.md").is_file(),
                            "falta .opencode/agents/MetaFlow.md")
            self.assertFalse((out / ".github" / "51-agents").exists(),
                             ".github/51-agents no debería existir")
            self.assertFalse((out / ".opencode" / "51-agents").exists(),
                             ".opencode/51-agents no debería existir")
            # No-regresión: la carpeta de metodología SÍ sigue numerada
            self.assertTrue((out / "metaflow" / "51-agents").is_dir())

            texts = []
            for p in out.rglob("*"):
                if p.is_file() and p.suffix in (".md", ".json", ".yaml", ".yml"):
                    texts.append(p.read_text(encoding="utf-8"))
            joined = "\n".join(texts)

            # 0 sobre-match: ningún "NN-nombre" sin "/" después
            over = re.compile(r"(?<![\w-])\d{2}-(?:input|analysis|discovery|adrs|"
                              r"functional|bugs|spec|memory|metrics|tests|reviews|"
                              r"adv-reviews|risks|incidents|retros|prompts|reports|"
                              r"agents|agents-data|actors)(?![\w/-])")
            self.assertEqual(len(over.findall(joined)), 0, "sobre-match en prosa")

            # 0 referencias viejas como ruta — el lookbehind excluye el contexto
            # de plataforma (".github/agents/", ".opencode/agents/", ".agents/skills/",
            # ".claude/agents/", ".codex/agents/"), que NO se numera (ADR-003, BUG-001,
            # BUG-008): las menciones de plataforma usan los nombres reales sin número.
            old = re.compile(
                r"(?<![\w./-])(input|analysis|discovery|adrs|functional|bugs|spec|"
                r"memory|metrics|tests|reviews|adversarial-reviews|risks|incidents|"
                r"retros|prompts|reports|agents|agents-data|actors)/")
            self.assertEqual(len(old.findall(joined)), 0, "referencias viejas")

            # Enum del schema restaurado (REV-002 F-05) — la clave es "task" (B-rules)
            schema = json.loads((out / "metaflow/23-metrics/manifest-v1-task.schema.json")
                                .read_text(encoding="utf-8"))
            enum = schema["properties"]["task"]["properties"]["type"]["enum"]
            self.assertEqual(enum, ["functional", "non-functional", "test"])


if __name__ == "__main__":
    unittest.main()
