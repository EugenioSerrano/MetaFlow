"""Tests unitarios — checkpoints con regex (C1-C6: AITL/HITL → CP, CITL)."""
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


class TestRegex(unittest.TestCase):
    def test_aitl_checkpoint_codes(self):
        self.assertEqual(content("AITL-SPEC-Approval is a checkpoint"),
                         "CP-SPEC-Approval is a checkpoint")
        self.assertEqual(content("AITL-MEM-Approval and AITL-US-Approval"),
                         "CP-MEM-Approval and CP-US-Approval")

    def test_hitl_checkpoint_codes(self):
        self.assertEqual(content("HITL-MEM-Approval is legacy"),
                         "CP-MEM-Approval is legacy")

    def test_literal_placeholders(self):
        self.assertEqual(content("AITL-<CODE>-Approval"), "CP-<CODE>-Approval")
        self.assertEqual(content("AITL-*-Approval"), "CP-*-Approval")
        self.assertEqual(content("AITL-Approval"), "CP-Approval")

    def test_bolt_ready_after_aitl(self):
        # C1 convierte AITL-...-Approval → CP-...-Approval; luego B6/B7 hacen TASK
        self.assertEqual(content("AITL-BOLT-READY-Approval"),
                         "CP-TASK-READY-Approval")
        self.assertEqual(content("AITL-BOLT-DONE-Approval"),
                         "CP-TASK-DONE-Approval")

    def test_concept_citl(self):
        self.assertEqual(content("Actor-in-the-Loop (AITL)"),
                         "Checkpoint-in-the-Loop (CITL)")
        self.assertEqual(content("Human-in-the-Loop (HITL)"),
                         "Checkpoint-in-the-Loop (CITL)")

    def test_bare_acronyms(self):
        self.assertEqual(content("the AITL methodology"),
                         "the CITL methodology")
        self.assertEqual(content("under HITL rules"),
                         "under CITL rules")


if __name__ == "__main__":
    unittest.main()
