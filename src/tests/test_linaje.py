"""Tests de reproducción — BUG-021..024 (REV-005): linaje, shorthands, propiedad, tools.

Verifican la AUSENCIA de los patrones en el output REAL:
- BUG-021: historia del linaje previo ("v4.2", "versions up to 4.1") sin declarar.
- BUG-022: shorthands de checkpoints no canónicos ("TASK-DONE"/"TASK-READY", "TASK TASK-DONE").
- BUG-023: entidad inexistente "Eugenio Serrano LATAM" (kit + front door).
- BUG-024: resto del linaje en tools/ ("devflow").
RED = los patrones están presentes (falla); GREEN = desaparecieron tras el fix.
"""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KIT = ROOT / "distribution-kit"


def read(root, *parts):
    p = root.joinpath(*parts)
    if not p.is_file():
        return ""
    return p.read_text(encoding="utf-8")


class TestBug021HistoriaLinaje(unittest.TestCase):
    def test_kit_sin_v42(self):
        bad = []
        for p in KIT.rglob("*"):
            if not p.is_file():
                continue
            try:
                t = p.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            if "v4.2" in t:
                bad.append(str(p.relative_to(KIT)))
        self.assertEqual(bad, [], "menciones de v4.2 sin declarar en: " + ", ".join(bad[:10]))

    def test_kit_sin_versions_up_to_41(self):
        bad = []
        for p in KIT.rglob("*"):
            if not p.is_file():
                continue
            try:
                t = p.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            if "versions up to 4.1" in t:
                bad.append(str(p.relative_to(KIT)))
        self.assertEqual(bad, [], "versions up to 4.1 en: " + ", ".join(bad[:10]))


class TestBug022Shorthands(unittest.TestCase):
    def test_metricas_checkpoints_canonicos(self):
        m = read(KIT, "metaflow", "23-metrics", "README.md")
        r = read(KIT, "metaflow", "42-reports", "README.md")
        self.assertNotIn("TASK TASK-DONE", m, "celda 'last child TASK TASK-DONE' en 23-metrics/README")
        self.assertIn("`CP-TASK-DONE-Approval` `decided_at` \u2212 `CP-TASK-READY-Approval` `decided_at`", m,
                      "23-metrics/README sin checkpoints canónicos en TASK lead time")
        self.assertIn("last child TASK\u2019s `CP-TASK-DONE-Approval`", m,
                      "23-metrics/README sin checkpoints canónicos en US lead time")
        self.assertIn("`CP-TASK-DONE-Approval` \u2212 `CP-TASK-READY-Approval` `decided_at`", r,
                      "42-reports/README sin checkpoints canónicos")


class TestBug023Propiedad(unittest.TestCase):
    def test_kit_sin_eugenio_serrano_latam(self):
        bad = []
        for p in KIT.rglob("*"):
            if not p.is_file():
                continue
            try:
                t = p.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            if "Eugenio Serrano LATAM" in t or "Eugenio Serrano\nLATAM" in t:
                bad.append(str(p.relative_to(KIT)))
        self.assertEqual(bad, [], "entidad inexistente en: " + ", ".join(bad[:10]))

    def test_front_door_sin_latam(self):
        t = read(ROOT, "README.md")
        self.assertNotIn("Eugenio Serrano LATAM", t, "README raíz con entidad inexistente")
        self.assertNotIn("Eugenio Serrano\nLATAM", t, "README raíz con entidad inexistente (salto de línea)")

    def test_metaflow_con_framework_eugenio_serrano(self):
        t = read(KIT, "metaflow", "ai-sdlc", "MetaFlow.md")
        self.assertIn("framework of Eugenio Serrano", t, "MetaFlow.md sin la entidad real")


class TestBug024ToolsLinaje(unittest.TestCase):
    def test_tools_sin_devflow(self):
        bad = []
        for p in (ROOT / "tools").rglob("*.md"):
            t = p.read_text(encoding="utf-8")
            if re.search(r"devflow", t, re.I):
                bad.append(str(p.relative_to(ROOT)))
        self.assertEqual(bad, [], "referencias devflow en tools/*.md: " + ", ".join(bad[:10]))

    def test_build_destino_metaflow_bin(self):
        t = read(ROOT, "tools", "BUILD.md")
        self.assertIn("distribution-kit/metaflow/bin/", t, "BUILD.md sin destino metaflow/bin")


if __name__ == "__main__":
    unittest.main()
