"""Tests unitarios — renames de contenido (familia de marca, M1-M11)."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import transform

MAPPING = Path(__file__).resolve().parents[1] / "mapping.json"
_RULES = transform.load_mapping(MAPPING).rules


def content(text: str) -> str:
    out, _applied, _removals = transform.apply_content(text, _RULES)
    return out


class TestRename(unittest.TestCase):
    def test_brand_family(self):
        self.assertEqual(content("AvengaDevFlow is a methodology"),
                         "MetaFlow is a methodology")
        self.assertEqual(content("Avenga DevFlow is a methodology"),
                         "MetaFlow is a methodology")
        self.assertEqual(content("DevFlow is a methodology"),
                         "MetaFlow is a methodology")

    def test_attribution(self):
        self.assertEqual(content("proprietary methodology of Avenga LATAM"),
                         "proprietary methodology of Eugenio Serrano")
        self.assertEqual(content("Avenga LATAM is the author"),
                         "Eugenio Serrano is the author")

    def test_no_partial_replacement(self):
        self.assertEqual(content("AvengaDevFlowX"), "MetaFlowX")

    def test_marker_agents(self):
        self.assertEqual(content("AVENGA-DEVFLOW:PROJECT-SECTION"),
                         "METAFLOW:PROJECT-SECTION")

    def test_paths_in_prose(self):
        self.assertEqual(content("See devflow/avenga-devflow/Avenga-DevFlow.md"),
                         "See metaflow/ai-sdlc/MetaFlow.md")
        self.assertEqual(content("File Avenga-DevFlow.md is normative"),
                         "File MetaFlow.md is normative")
        self.assertEqual(content("Folder avenga-devflow is the kit"),
                         "Folder ai-sdlc is the kit")

    def test_no_devflow_trace(self):
        # Cero rastro de "devflow" en ninguna variante
        self.assertEqual(content("the devflow folder and devflow/spec/"),
                         "the metaflow folder and metaflow/21-spec/")
        self.assertEqual(content("Devflow and DEVFLOW"),
                         "MetaFlow and METAFLOW")


if __name__ == "__main__":
    unittest.main()
