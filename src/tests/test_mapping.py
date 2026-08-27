"""Tests unitarios — carga y validación del diccionario (mapping.json)."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import transform

MAPPING = Path(__file__).resolve().parents[2] / "mapping.json"
FIXTURES = Path(__file__).resolve().parent / "fixtures"


class TestMapping(unittest.TestCase):
    def test_load_real_mapping(self):
        mapping = transform.load_mapping(MAPPING)
        self.assertTrue(mapping.rules)
        self.assertEqual(mapping.rules, sorted(mapping.rules, key=lambda r: r.order))
        self.assertIn("devflow/reports/TEMPLATE-REPORT.html", mapping.exclude)

    def test_order_longest_first(self):
        mapping = transform.load_mapping(MAPPING)
        by_id = {r.id: r for r in mapping.rules}
        # La cadena más larga se reemplaza antes que la más corta
        self.assertLess(by_id["M1"].order, by_id["M3"].order)      # AvengaDevFlow < DevFlow
        self.assertLess(by_id["M11"].order, by_id["M7b"].order)    # ruta completa < fragmento
        self.assertLess(by_id["D2"].order, by_id["D1"].order)      # V-Bounces < V-Bounce
        self.assertLess(by_id["B15a"].order, by_id["B1b"].order)   # "per Bolt" < "Bolt"
        self.assertLess(by_id["C5a"].order, by_id["C4b"].order)    # legado HITL se remueve antes del bare HITL
        self.assertLess(by_id["C3a"].order, by_id["C4"].order)     # frase completa antes del acrónimo

    def test_invalid_json_raises(self):
        with tempfile.TemporaryDirectory() as td:
            bad = Path(td) / "bad.json"
            bad.write_text("{not json", encoding="utf-8")
            with self.assertRaises(transform.TransformError):
                transform.load_mapping(bad)

    def test_unknown_type_raises(self):
        with tempfile.TemporaryDirectory() as td:
            bad = Path(td) / "bad.json"
            bad.write_text(json.dumps({"rules": [
                {"id": "X1", "type": "magic", "pattern": "a", "order": 1}
            ]}), encoding="utf-8")
            with self.assertRaises(transform.TransformError):
                transform.load_mapping(bad)

    def test_missing_pattern_raises(self):
        with tempfile.TemporaryDirectory() as td:
            bad = Path(td) / "bad.json"
            bad.write_text(json.dumps({"rules": [
                {"id": "X1", "type": "rename", "replacement": "b", "order": 1}
            ]}), encoding="utf-8")
            with self.assertRaises(transform.TransformError):
                transform.load_mapping(bad)

    def test_order_collision_raises(self):
        with tempfile.TemporaryDirectory() as td:
            bad = Path(td) / "bad.json"
            bad.write_text(json.dumps({"rules": [
                {"id": "X1", "type": "rename", "pattern": "a", "replacement": "b", "order": 5},
                {"id": "X2", "type": "rename", "pattern": "c", "replacement": "d", "order": 5},
            ]}), encoding="utf-8")
            with self.assertRaises(transform.TransformError):
                transform.load_mapping(bad)


if __name__ == "__main__":
    unittest.main()
