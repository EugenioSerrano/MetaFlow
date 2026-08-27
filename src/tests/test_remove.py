"""Tests unitarios — remociones (R1-R4 y legado C5): nunca silenciosas."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import transform

MAPPING = Path(__file__).resolve().parents[2] / "mapping.json"
_RULES = transform.load_mapping(MAPPING).rules


class TestRemove(unittest.TestCase):
    def test_raja_removed_and_recorded(self):
        out, _applied, removals = transform.apply_content(
            "based on Raja SP, AWS", _RULES)
        self.assertNotIn("Raja SP", out)
        self.assertGreaterEqual(removals.get("R1b", 0), 1)

    def test_dora_concept_renamed(self):
        # D9: el concepto de métricas se RENOMBRA (no se elimina); con las
        # reglas de barra (ADR-003), "metrics" suelto ya no se numera
        out, _applied, _removals = transform.apply_content(
            "Accelerate / DORA metrics and DORA Five", _RULES)
        self.assertNotIn("DORA", out)
        self.assertIn("Delivery Flow metrics and Delivery Flow Five", out)

    def test_dora_citations_removed_by_line(self):
        citation = ("- **DevOps Research and Assessment (DORA).** (2024). "
                    "*Accelerate State of DevOps Report 2024*. "
                    "<https://dora.dev/research/2024/dora-report/>\n")
        out, _applied, removals = transform.apply_content(citation, _RULES)
        self.assertNotIn("DevOps Research and Assessment", out)
        self.assertNotIn("dora", out.lower())
        self.assertGreaterEqual(removals.get("R2a", 0), 1)

    def test_legacy_hitl_removed_before_bare_rename(self):
        # C5a remueve la frase de legado ANTES de que el acrónimo bare HITL → CITL
        out, _applied, removals = transform.apply_content(
            "pre-v5 `HITL-*` prefix is legacy", _RULES)
        self.assertNotIn("HITL-*", out)
        self.assertGreaterEqual(removals.get("C5a", 0), 1)

    def test_remove_never_silent(self):
        _out, _applied, removals = transform.apply_content(
            "pre-v5 `HITL-*` prefix is legacy. Raja SP.", _RULES)
        self.assertGreaterEqual(sum(removals.values()), 2)


if __name__ == "__main__":
    unittest.main()
