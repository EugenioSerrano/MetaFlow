"""Verificador de tokens prohibidos — BOLT-002 (US-001, SPEC-260827-0142).

Barre el kit de salida (contenido y rutas) buscando restos de la marca
previa: tokens canónicos del glossary §6 (Avenga, AITL, HITL, Bolt/BOLT/bolts,
V-Bounce/v_bounces, Raja, DORA) y sus variantes. Si hay hits, el run del
pipeline falla (AC-7, O1 de la visión: cero contaminación de marca).
"""
from __future__ import annotations

import re
from pathlib import Path

# Variantes regex: cubren los tokens canónicos del glossary §6 y sus formas
# (case, plurales, separadores, derivados). Los términos conservados del
# glossary §7 no contienen estos tokens; la lista EXCEPTIONS queda como dato
# por si una versión futura introduce colisiones.
VARIANTS = [
    (re.compile(r"avenga", re.IGNORECASE), "avenga"),
    (re.compile(r"devflow", re.IGNORECASE), "devflow"),
    (re.compile(r"aitl", re.IGNORECASE), "aitl"),
    (re.compile(r"hitl", re.IGNORECASE), "hitl"),
    (re.compile(r"\bbolts?\b", re.IGNORECASE), "bolt/bolts"),
    (re.compile(r"v[ _-]?bounces?", re.IGNORECASE), "v-bounce/v_bounces"),
    (re.compile(r"\braja\b", re.IGNORECASE), "raja"),
    (re.compile(r"\bdora\b", re.IGNORECASE), "dora"),
]

# Excepciones del barrido (términos conservados que colisionaran con un
# token prohibido) — vacío por ahora; extensible como dato.
EXCEPTIONS: list = []


def _scan_text(text: str, path: str, hits: list) -> None:
    for lineno, line in enumerate(text.splitlines(), start=1):
        for pattern, name in VARIANTS:
            if any(exc in line for exc in EXCEPTIONS):
                continue
            for _m in pattern.finditer(line):
                hits.append({
                    "path": path, "token": name, "line": lineno,
                    "context": line.strip()[:120], "where": "content",
                })


def _scan_path(rel_parts: tuple, hits: list) -> None:
    for part in rel_parts:
        for pattern, name in VARIANTS:
            if pattern.search(part):
                hits.append({
                    "path": "/".join(rel_parts), "token": name, "line": 0,
                    "context": f"ruta: {part}", "where": "path",
                })


def verify_tree(root: Path) -> list:
    """Barre el árbol del kit de salida. Devuelve la lista de hits (vacía = OK).

    Escanea el CONTENIDO de cada archivo de texto y TODOS los componentes de
    ruta (carpetas y nombres de archivo), incluidas las carpetas vacías.
    """
    hits: list = []
    for entry in sorted(root.rglob("*")):
        rel = entry.relative_to(root)
        _scan_path(rel.parts, hits)
        if entry.is_dir():
            continue
        try:
            text = entry.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue  # binario: no se barre
        _scan_text(text, rel.as_posix(), hits)
    return hits
