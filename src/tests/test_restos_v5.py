"""Tests de reproducción — BUG-002..BUG-012 (REV-003): restos del linaje v5.

Cada test verifica la AUSENCIA de un patrón de resto en el kit REAL
transformado (distribution-kit/). RED = el patrón está presente (falla);
GREEN = el patrón desapareció tras el fix del diccionario + regeneración.
"""
import re
import unittest
from pathlib import Path

KIT = Path(__file__).resolve().parents[2] / "distribution-kit"


def read(*parts):
    p = KIT.joinpath(*parts)
    if not p.is_file():
        return ""
    return p.read_text(encoding="utf-8")


def walk_texts():
    for entry in sorted(KIT.rglob("*")):
        if entry.is_file():
            try:
                yield entry, entry.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                pass


class TestBolt007SchemaVersionMetodologia(unittest.TestCase):
    def test_metaflow_md_sin_restos_v5(self):
        text = re.sub(r"\s+", " ", read("metaflow", "ai-sdlc", "MetaFlow.md"))
        for pat in [
            "schema_version` is exactly `5.0`",
            "a schema change means `5.0`",
            "CITL ⊇ CITL",
            "accepts only `CITL-*`",
            'becomes `"5.0"`',
            "checkpoint_approvals[]` → `checkpoint_approvals[]`",
            "CP-<CODE>-Approval` → `CP-<CODE>-Approval`",
        ]:
            self.assertNotIn(pat, text, f"resto v5 presente en MetaFlow.md: {pat}")


class TestBolt008SchemaVersionAgentes(unittest.TestCase):
    def test_wrappers_sin_5_0(self):
        wrappers = [
            "CLAUDE.md",
            ".agents", "skills", "ai-sdlc", "SKILL.md",
            ".github", "agents", "MetaFlow.agent.md",
            ".opencode", "agents", "MetaFlow.md",
        ]
        texts = [read(*w) for w in (wrappers[:1], wrappers[1:4], wrappers[4:7], wrappers[7:])]
        for t in texts:
            self.assertNotIn('(exactly `"5.0"`)', t, "schema_version 5.0 en agent definition")


class TestBolt009SchemaVersionContradicciones(unittest.TestCase):
    def test_docs_sin_5_0(self):
        docs = [
            read("metaflow", "23-metrics", "README.md"),
            read("metaflow", "12-functional", "user-stories", "TEMPLATE-US.md"),
            read("metaflow", "24-tests", "test-cases", "TEMPLATE-TC.md"),
        ]
        for t in docs:
            self.assertNotIn('schema_version "5.0"', t)
            self.assertNotIn('exactly "5.0"', t)


class TestBolt010NamingFamiliaV1(unittest.TestCase):
    def test_kit_sin_family_v5(self):
        bad = re.compile(
            r"Manifest family v5|Manifest Family v5|Schema family v5|manifest v5|"
            r"Schema v5 example|three v5 schemas|outside manifest v5|family \*\*v5\*\*|"
            r"manifest family v5"
        )
        hits = [str(p.relative_to(KIT)) for p, t in walk_texts() if bad.search(t)]
        self.assertEqual(hits, [], "restos de naming family v5 en: " + ", ".join(hits[:10]))


class TestBolt011Placeholders(unittest.TestCase):
    def test_kit_sin_placeholders_vacios(self):
        bad = re.compile(r"The  is invalid|the legacy  is invalid|Use  \(the \)")
        hits = [str(p.relative_to(KIT)) for p, t in walk_texts() if bad.search(t)]
        self.assertEqual(hits, [], "placeholders vacíos en: " + ", ".join(hits[:10]))


class TestBolt012PrefijoCitl(unittest.TestCase):
    def test_kit_sin_citl_checkpoint(self):
        bad = re.compile(r"CITL-(US|BUG|TC|DISC|REV|ADR)\b|CITL-AREV")
        hits = [str(p.relative_to(KIT)) for p, t in walk_texts() if bad.search(t)]
        self.assertEqual(hits, [], "prefijo CITL-* como checkpoint en: " + ", ".join(hits[:10]))


class TestBolt013RutasAgentes(unittest.TestCase):
    def test_kit_sin_rutas_51_plataforma(self):
        bad = re.compile(r"\.github/51-agents/|\.opencode/51-agents/|\.claude/51-agents/|\.codex/51-agents/|\.51-agents/skills/")
        hits = [str(p.relative_to(KIT)) for p, t in walk_texts() if bad.search(t)]
        self.assertEqual(hits, [], "rutas *51-agents* de plataforma en: " + ", ".join(hits[:10]))


class TestBolt014TemplateReport(unittest.TestCase):
    def test_readme_no_anuncia_template_ausente(self):
        text = re.sub(r"\s+", " ", read("metaflow", "42-reports", "README.md"))
        self.assertNotIn("TEMPLATE-REPORT.html` is currently a **design reference**", text)


class TestBolt015FrontmatterCita(unittest.TestCase):
    def test_frontmatter_y_cita(self):
        text = re.sub(r"\s+", " ", read("metaflow", "ai-sdlc", "MetaFlow.md"))
        self.assertNotIn('version: "5.1"', text)
        self.assertNotIn("by , Principal", text)
        self.assertNotIn("**,** , Principal", text)


class TestBolt016MemCampos(unittest.TestCase):
    def test_template_mem_con_8_campos(self):
        text = read("metaflow", "22-memory", "TEMPLATE-MEM.md")
        self.assertIn(
            "number, spec_revision, git_commit, execution_outcome, code_generation, mem, review_ready_at, review_started_at",
            text,
            "TEMPLATE-MEM no lista los 8 campos de delivery_loops[]",
        )


class TestBolt017Ejemplos(unittest.TestCase):
    def test_ejemplos_consistentes(self):
        meta = read("metaflow", "ai-sdlc", "MetaFlow.md")
        agent = read("metaflow", "51-agents", "examples", "developer", "agent.yaml")
        self.assertNotIn("Agregar manejo explícito de concurrencia", meta)
        self.assertNotIn("distribution-kit/, tools/", agent)


# ---- REV-004: BUG-013..019 (análisis fresco del kit) ----

WRAPPERS = [
    ("CLAUDE.md",),
    (".agents", "skills", "ai-sdlc", "SKILL.md"),
    (".github", "agents", "MetaFlow.agent.md"),
    (".opencode", "agents", "MetaFlow.md"),
]


def wrapper_texts():
    return [read(*w) for w in WRAPPERS]


class TestBolt018MigracionAgentes(unittest.TestCase):
    def test_wrappers_sin_migracion_corrupta(self):
        for i, t in enumerate(wrapper_texts()):
            t = re.sub(r"\s+", " ", t)
            for pat in [
                "renames `checkpoint_approvals[]` → `checkpoint_approvals[]`",
                "re-expressed `CITL-*`→`CITL-*`",
                "the v5 enum is `CITL-*`-only",
            ]:
                self.assertNotIn(pat, t, f"migración corrupta en wrapper {i}: {pat}")


class TestBolt019G05Wrappers(unittest.TestCase):
    def test_wrappers_g05_legible(self):
        for i, t in enumerate(wrapper_texts()):
            t = re.sub(r"\s+", " ", t)
            self.assertNotIn("Legacy checkpoint names (the )", t, f"G05 placeholder en wrapper {i}")
            self.assertNotIn("canonical is `CITL-*`", t, f"G05 canónico erróneo en wrapper {i}")


class TestBolt020TautologiasCitl(unittest.TestCase):
    def test_metaflow_sin_tautologias(self):
        text = re.sub(r"\s+", " ", read("metaflow", "ai-sdlc", "MetaFlow.md"))
        self.assertNotIn("CITL) is the default case of CITL", text)
        self.assertNotIn("CITL is the default case inside CITL", text)


class TestBolt021TemplateReportAnuncios(unittest.TestCase):
    def test_sin_anuncios_template_ausente(self):
        for rel in [("metaflow", "ai-sdlc", "MetaFlow.md"), ("metaflow", "README.md")]:
            t = re.sub(r"\s+", " ", read(*rel))
            self.assertNotIn("`TEMPLATE-REPORT.html` ships as a design reference", t, f"anuncio en {'/'.join(rel)}")


class TestBolt022CitlAsterisco(unittest.TestCase):
    def test_sin_citl_asterisco_checkpoint(self):
        tc = re.sub(r"\s+", " ", read("metaflow", "24-tests", "test-cases", "README.md"))
        g = re.sub(r"\s+", " ", read("metaflow", "GUARDRAILS.md"))
        self.assertNotIn("`CITL-*` codes are never translated", tc)
        self.assertNotIn("each artifact's `CITL-*` decision", g)


class TestBolt023G05PreV5(unittest.TestCase):
    def test_g05_sin_pre_v5_citl(self):
        g = re.sub(r"\s+", " ", read("metaflow", "GUARDRAILS.md"))
        self.assertNotIn("the pre-v5 `CITL-*` names", g)


class TestBolt024Seccion516Linaje(unittest.TestCase):
    def test_516_linaje_declarado(self):
        text = re.sub(r"\s+", " ", read("metaflow", "ai-sdlc", "MetaFlow.md"))
        self.assertNotIn("`3.0` → `4.0` is exactly this shape", text)
        self.assertIn("History of the previous family", text)


if __name__ == "__main__":
    unittest.main()
