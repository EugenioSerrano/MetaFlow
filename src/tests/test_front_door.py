"""Tests de reproducción — BUG-020: front door de la raíz del workshop.

Verifican el front door del REPOSITORIO (no del kit): cero tokens del
linaje Avenga en los archivos de la raíz, el modelo de dos particiones en
README.md y AGENTS.md, y la ausencia del skill avenga-devflow.
RED = el front door actual conserva el texto Avenga / el skill existe;
GREEN = tras el fix del BUG-020 (SPEC-260827-1628, US-001.TASK-025).
"""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

FORBIDDEN = re.compile(r"Avenga|DevFlow|devflow|BOLT|AITL|HITL")

FRONT_DOOR = [
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    (".agents", "skills", "ai-sdlc", "SKILL.md"),
    (".github", "agents", "MetaFlow.agent.md"),
    (".opencode", "agents", "MetaFlow.md"),
]


def read(*parts):
    p = ROOT.joinpath(*parts)
    if not p.is_file():
        return ""
    return p.read_text(encoding="utf-8")


class TestFrontDoorSinAvenga(unittest.TestCase):
    def test_archivos_front_door_sin_tokens_prohibidos(self):
        for rel in FRONT_DOOR:
            label = "/".join(rel) if isinstance(rel, tuple) else rel
            text = read(*rel) if isinstance(rel, tuple) else read(rel)
            for m in FORBIDDEN.finditer(text):
                line_no = text[: m.start()].count("\n") + 1
                self.fail(f"token prohibido '{m.group()}' en {label}:{line_no}")

    def test_readme_sin_rutas_devflow(self):
        text = read("README.md")
        self.assertNotIn("devflow/", text, "README.md referencia rutas devflow/")

    def test_skill_avenga_ausente(self):
        p = ROOT / ".agents" / "skills" / "avenga-devflow"
        self.assertFalse(p.exists(), "el skill avenga-devflow sigue instalado en la raíz")


class TestFrontDoorDosParticiones(unittest.TestCase):
    def test_readme_documenta_dos_particiones(self):
        text = read("README.md")
        self.assertIn("MetaFlow", text, "README.md no nombra MetaFlow")
        self.assertIn("distribution-kit", text, "README.md no nombra distribution-kit")
        self.assertIn("metaflow/", text, "README.md no nombra la partición metaflow/")
        self.assertIn("1.1", text, "README.md no declara la versión 1.1")

    def test_agents_md_seccion_proyecto(self):
        text = read("AGENTS.md")
        self.assertIn("METAFLOW:PROJECT-SECTION", text, "AGENTS.md sin marcador de sección de proyecto")
        below = text[text.find("METAFLOW:PROJECT-SECTION"):]
        self.assertIn("distribution-kit", below, "sección de proyecto sin distribution-kit")
        self.assertIn("metaflow/", below, "sección de proyecto sin metaflow/")


if __name__ == "__main__":
    unittest.main()
