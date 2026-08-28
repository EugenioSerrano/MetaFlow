"""Tests de reproducción — BUG-025: la skill de Codex debe generarse como
`.agents/skills/MetaFlow/SKILL.md` con `name: MetaFlow` (no `ai-sdlc`).

RED = el pipeline produce `.agents/skills/ai-sdlc/SKILL.md` con
`name: ai-sdlc` (regla P-M6) — el rename manual no está codificado;
GREEN = tras el fix (regla path full-path + regla content del frontmatter,
SPEC-260827-2229, US-001.TASK-030).
"""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import transform

ROOT = Path(__file__).resolve().parents[2]
REAL_KIT = ROOT / "input-kit"
MAPPING = Path(__file__).resolve().parents[1] / "mapping.json"

SKILL_REL = Path(".agents/skills/MetaFlow/SKILL.md")
SKILL_OLD_REL = Path(".agents/skills/ai-sdlc/SKILL.md")


def run_pipeline(out_dir: Path):
    """Corre el pipeline real (input-kit → out_dir) y devuelve el plan."""
    mapping = transform.load_mapping(MAPPING)
    return transform.run_transform(REAL_KIT, out_dir, mapping, dry_run=False)


class TestReproducibilidadSkillMetaFlow(unittest.TestCase):
    @unittest.skipUnless(REAL_KIT.is_dir(), "kit real no presente")
    def test_plan_genera_skill_metaflow(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "out"
            plan = run_pipeline(out)
            dsts = [Path(e["dst"]) for e in plan if e["kind"] == "file"]
            self.assertIn(
                out / SKILL_REL, dsts,
                "el plan debe generar .agents/skills/MetaFlow/SKILL.md")
            self.assertNotIn(
                out / SKILL_OLD_REL, dsts,
                "el plan no debe generar .agents/skills/ai-sdlc/SKILL.md")

    @unittest.skipUnless(REAL_KIT.is_dir(), "kit real no presente")
    def test_skill_generada_con_name_metaflow(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "out"
            run_pipeline(out)
            skill = out / SKILL_REL
            self.assertTrue(skill.is_file(), "la skill MetaFlow debe existir en la salida")
            text = skill.read_text(encoding="utf-8")
            self.assertIn("name: MetaFlow", text,
                          "el frontmatter debe decir name: MetaFlow")
            self.assertNotIn("name: ai-sdlc", text,
                             "el frontmatter no debe decir name: ai-sdlc")

    @unittest.skipUnless(REAL_KIT.is_dir(), "kit real no presente")
    def test_carpeta_metodologia_intacta(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "out"
            plan = run_pipeline(out)
            dsts = [Path(e["dst"]) for e in plan if e["kind"] == "file"]
            self.assertTrue(
                any("metaflow" in p.parts and "ai-sdlc" in p.parts for p in dsts),
                "la carpeta de la metodología metaflow/ai-sdlc/ debe seguir existiendo")


if __name__ == "__main__":
    unittest.main()
