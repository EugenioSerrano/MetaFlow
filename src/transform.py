#!/usr/bin/env python3
"""MetaFlow transform engine + CLI — BOLT-001 (US-001), SPEC-260827-0124 rev 2.

Transforma el kit de AvengaDevFlow (input-kit/) en el kit de MetaFlow
(distribution-kit/) aplicando el diccionario de reglas (mapping.json):
rename, regex_rename, remove y path_rename, en orden longest-first.
Modos: --dry-run (plan sin escribir ni borrar) y ejecución real (borra el
contenido previo de la salida — cero residuos — y escribe el kit nuevo).
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MAPPING = REPO_ROOT / "mapping.json"
DEFAULT_INPUT = REPO_ROOT / "input-kit"
DEFAULT_OUTPUT = REPO_ROOT / "distribution-kit"
DEFAULT_REPORTS = REPO_ROOT / "transform-reports"

RULE_TYPES = {"rename", "regex_rename", "remove", "regex_remove", "path_rename"}
SCOPES = {"content", "path", "both"}
CONTENT_TYPES = {"rename", "regex_rename", "remove", "regex_remove"}
PATH_TYPES = {"rename", "regex_rename", "path_rename"}


class TransformError(Exception):
    """Error del pipeline (carga, validación o ejecución)."""


@dataclass
class Rule:
    id: str
    type: str
    pattern: str
    replacement: str = ""
    order: int = 0
    scope: str = "content"
    report_on_match: bool = True
    path: str = ""  # opcional: ruta relativa de SALIDA a la que aplica la regla (vacío = todas)


@dataclass
class Mapping:
    rules: list = field(default_factory=list)
    exclude: list = field(default_factory=list)

    @property
    def content_rules(self):
        return [r for r in self.rules
                if r.scope in ("content", "both") and r.type in CONTENT_TYPES]

    @property
    def path_rules(self):
        return [r for r in self.rules
                if r.scope in ("path", "both") and r.type in PATH_TYPES]


def compute_output_version(version_in: str, offset: int = -4) -> str | None:
    """Versión de salida = versión de entrada + offset (mayor − 4, menor igual):
    5.1 → 1.1, 6.2 → 2.2. None si el formato no es X.Y."""
    parts = version_in.split(".")
    if len(parts) != 2 or not parts[0].isdigit() or not parts[1].isdigit():
        return None
    major = max(int(parts[0]) + offset, 0)
    return f"{major}.{parts[1]}"


def render_rules(rules, version_in: str) -> list:
    """Rellena los placeholders versionados {{VERSION_IN}}, {{VERSION_OUT}},
    {{FAMILY_IN}}, {{FAMILY_OUT}} en pattern/replacement/path de cada regla.

    Regla GENÉRICA −4 (BOLT-003 rev 2): el diccionario es agnóstico de la
    versión del input — 5.1 → 1.1 y v5 → v1 hoy; 6.1 → 2.1 y v6 → v2 cuando
    llegue, sin tocar mapping.json.
    """
    version_out = compute_output_version(version_in) or version_in
    family_in = version_in.split(".")[0] if "." in version_in else version_in
    family_out = str(max(int(family_in) - 4, 0)) if family_in.isdigit() else family_in
    repl = {
        "{{VERSION_IN}}": version_in,
        "{{VERSION_OUT}}": version_out,
        "{{FAMILY_IN}}": family_in,
        "{{FAMILY_OUT}}": family_out,
    }

    def fill(s: str) -> str:
        for key, value in repl.items():
            s = s.replace(key, value)
        return s

    return [Rule(r.id, r.type, fill(r.pattern), fill(r.replacement),
                 r.order, r.scope, r.report_on_match, fill(r.path))
            for r in rules]


def load_mapping(path: Path) -> Mapping:
    """Carga y valida mapping.json. Lanza TransformError ante cualquier problema."""
    if not path.is_file():
        raise TransformError(f"mapping no encontrado: {path}")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise TransformError(f"mapping inválido (JSON): {exc}") from exc
    if not isinstance(data, dict) or not isinstance(data.get("rules"), list):
        raise TransformError("mapping inválido: falta el array 'rules'")

    rules = []
    for raw in data["rules"]:
        rid = str(raw.get("id", "?"))
        rtype = raw.get("type", "")
        if rtype not in RULE_TYPES:
            raise TransformError(f"regla {rid}: tipo desconocido '{rtype}'")
        pattern = raw.get("pattern")
        if not isinstance(pattern, str) or not pattern:
            raise TransformError(f"regla {rid}: pattern (string no vacío) requerido")
        replacement = raw.get("replacement", "")
        if rtype in ("rename", "regex_rename") and not isinstance(replacement, str):
            raise TransformError(f"regla {rid}: replacement debe ser string")
        order = raw.get("order")
        if not isinstance(order, int) or order < 1:
            raise TransformError(f"regla {rid}: order (entero >= 1) requerido")
        scope = raw.get("scope", "content")
        if scope not in SCOPES:
            raise TransformError(f"regla {rid}: scope desconocido '{scope}'")
        path = raw.get("path", "")
        if not isinstance(path, str):
            raise TransformError(f"regla {rid}: path debe ser string")
        rules.append(Rule(
            id=rid, type=rtype, pattern=pattern, replacement=replacement,
            order=order, scope=scope,
            report_on_match=bool(raw.get("report_on_match", True)),
            path=path,
        ))

    orders = [r.order for r in rules]
    if len(orders) != len(set(orders)):
        raise TransformError("colisión de 'order' entre reglas")

    exclude = data.get("exclude", [])
    if not isinstance(exclude, list) or not all(
            isinstance(x, str) and x for x in exclude):
        raise TransformError("mapping inválido: 'exclude' debe ser un array de rutas")

    rules.sort(key=lambda r: r.order)
    return Mapping(rules=rules, exclude=list(exclude))


def _to_python_repl(repl: str) -> str:
    """Convierte backrefs estilo $1 (JSON) a \\g<1> de Python re.sub."""
    return re.sub(r"\$(\d+)", r"\\g<\1>", repl)


def apply_content(text: str, rules) -> tuple[str, dict, dict]:
    """Aplica reglas de contenido en orden. Devuelve (texto, aplicadas, remociones)."""
    applied: dict = {}
    removals: dict = {}
    for rule in rules:
        if rule.type == "rename":
            if rule.pattern in text:
                n = text.count(rule.pattern)
                text = text.replace(rule.pattern, rule.replacement)
                if rule.report_on_match:
                    applied[rule.id] = applied.get(rule.id, 0) + n
        elif rule.type == "regex_rename":
            pattern = re.compile(rule.pattern)
            n = len(pattern.findall(text))
            if n:
                text = pattern.sub(_to_python_repl(rule.replacement), text)
                if rule.report_on_match:
                    applied[rule.id] = applied.get(rule.id, 0) + n
        elif rule.type == "remove":
            if rule.pattern in text:
                n = text.count(rule.pattern)
                text = text.replace(rule.pattern, "")
                removals[rule.id] = removals.get(rule.id, 0) + n
        elif rule.type == "regex_remove":
            pattern = re.compile(rule.pattern)
            n = len(pattern.findall(text))
            if n:
                text = pattern.sub("", text)
                removals[rule.id] = removals.get(rule.id, 0) + n
    return text, applied, removals


def apply_path(component: str, rules) -> str:
    """Aplica reglas de ruta sobre un componente (regex_rename con anclas o
    substring replace)."""
    for rule in rules:
        if rule.type == "regex_rename":
            pattern = re.compile(rule.pattern)
            component = pattern.sub(_to_python_repl(rule.replacement), component)
        elif rule.pattern in component:
            component = component.replace(rule.pattern, rule.replacement)
    return component


def build_plan(input_dir: Path, output_dir: Path, mapping: Mapping) -> list:
    from report import detect_version
    rules = render_rules(mapping.rules, detect_version(input_dir))
    content_rules = [r for r in rules
                     if r.scope in ("content", "both") and r.type in CONTENT_TYPES]
    path_rules = [r for r in rules
                  if r.scope in ("path", "both") and r.type in PATH_TYPES]
    plan = []
    for src in sorted(input_dir.rglob("*")):
        rel = src.relative_to(input_dir)
        rel_posix = rel.as_posix()
        entry = {"src": src, "rel": rel_posix,
                 "kind": "dir" if src.is_dir() else "file"}
        # BUG-001 (ADR-003): las carpetas ocultas de plataforma (.agents/,
        # .github/, .opencode/) NO se numeran — se excluyen las reglas PN*;
        # los renames de marca (P-M7/P-M8/...) siguen aplicando.
        if rel.parts and rel.parts[0].startswith("."):
            rules_for_path = [r for r in path_rules if not r.id.startswith("PN")]
        else:
            rules_for_path = path_rules
        new_parts = tuple(apply_path(p, rules_for_path) for p in rel.parts)
        entry["dst"] = output_dir.joinpath(*new_parts)
        if src.is_file():
            if rel_posix in mapping.exclude:
                entry["kind"] = "excluded"
            else:
                try:
                    text = src.read_text(encoding="utf-8")
                except UnicodeDecodeError:
                    entry["kind"] = "binary"
                else:
                    dst_rel = entry["dst"].relative_to(output_dir).as_posix()
                    file_rules = [r for r in content_rules
                                  if not r.path or r.path == dst_rel]
                    new_text, applied, removals = apply_content(text, file_rules)
                    entry["text"] = new_text
                    entry["applied"] = applied
                    entry["removals"] = removals
                    entry["changed"] = (new_text != text) or (entry["dst"] != src)
        plan.append(entry)
    return plan


def clean_output(output_dir: Path, input_dir: Path) -> None:
    """Borra el contenido completo de la salida (solo esa carpeta, nunca otra)."""
    out_res = output_dir.resolve()
    in_res = input_dir.resolve()
    if out_res == in_res or in_res in out_res.parents:
        raise TransformError(
            f"refusing: la salida '{output_dir}' contiene o coincide con la entrada '{input_dir}'")
    if output_dir.exists() and not output_dir.is_dir():
        raise TransformError(f"la salida no es una carpeta: {output_dir}")
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True)


def run_transform(input_dir: Path, output_dir: Path, mapping: Mapping,
                  dry_run: bool = False) -> list:
    plan = build_plan(input_dir, output_dir, mapping)
    if not dry_run:
        clean_output(output_dir, input_dir)
        for entry in plan:
            if entry["kind"] == "dir":
                entry["dst"].mkdir(parents=True, exist_ok=True)
            elif entry["kind"] == "binary":
                entry["dst"].parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(entry["src"], entry["dst"])
            elif entry["kind"] == "file":
                entry["dst"].parent.mkdir(parents=True, exist_ok=True)
                entry["dst"].write_text(entry["text"], encoding="utf-8")
        # Prune de carpetas vacías residuales (p. ej. padres de archivos excluidos)
        for dirpath in sorted(output_dir.rglob("*"), key=lambda p: len(p.parts), reverse=True):
            if dirpath.is_dir():
                try:
                    dirpath.rmdir()
                except OSError:
                    pass
    return plan


def _totals(plan):
    applied: dict = {}
    removals: dict = {}
    files = dirs = excluded = binaries = 0
    for e in plan:
        if e["kind"] == "dir":
            dirs += 1
        elif e["kind"] == "excluded":
            excluded += 1
        elif e["kind"] == "binary":
            binaries += 1
            files += 1
        else:
            files += 1
            for k, v in e.get("applied", {}).items():
                applied[k] = applied.get(k, 0) + v
            for k, v in e.get("removals", {}).items():
                removals[k] = removals.get(k, 0) + v
    return applied, removals, files, dirs, excluded, binaries


def render_plan(plan, input_dir: Path, output_dir: Path, dry_run: bool) -> str:
    """Devuelve el resumen del plan/run (también se usa como run.log)."""
    mode = "DRY-RUN" if dry_run else "REAL"
    lines = [f"=== METAFLOW TRANSFORM ({mode}) ===",
             f"input : {input_dir}",
             f"output: {output_dir}"]
    for e in plan:
        if e["kind"] == "dir":
            continue
        if e["kind"] == "excluded":
            lines.append(f"  [excluido] {e['rel']}")
        elif e["kind"] == "binary":
            lines.append(f"  [copia]    {e['rel']} -> {e['dst'].relative_to(output_dir)} (binario)")
        else:
            detail = []
            if e.get("applied"):
                detail.append("reglas: " + ", ".join(
                    f"{k}x{v}" for k, v in sorted(e["applied"].items())))
            if e.get("removals"):
                detail.append("remociones: " + ", ".join(
                    f"{k}x{v}" for k, v in sorted(e["removals"].items())))
            suffix = f" ({'; '.join(detail)})" if detail else ""
            lines.append(f"  [ok]       {e['rel']} -> {e['dst'].relative_to(output_dir)}{suffix}")
    applied, removals, files, dirs, excluded, binaries = _totals(plan)
    lines.append("---")
    lines.append(f"total: {files} archivos, {dirs} carpetas, {binaries} binarios copiados, "
                 f"{excluded} excluidos, {sum(applied.values())} reglas aplicadas, "
                 f"{sum(removals.values())} remociones")
    return "\n".join(lines)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        prog="transform", description="MetaFlow transform pipeline (BOLT-001)")
    parser.add_argument("--dry-run", action="store_true",
                        help="mostrar el plan sin escribir ni borrar nada")
    parser.add_argument("--mapping", default=str(DEFAULT_MAPPING),
                        help="ruta del diccionario (default: mapping.json en la raíz)")
    parser.add_argument("--input", default=str(DEFAULT_INPUT),
                        help="kit de entrada (default: input-kit/)")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT),
                        help="kit de salida (default: distribution-kit/)")
    parser.add_argument("--reports", default=str(DEFAULT_REPORTS),
                        help="carpeta de evidencia por run (default: transform-reports/)")
    parser.add_argument("--keep-runs", type=int, default=2,
                        help="retención de evidencia: corridas más recientes por versión (default: 2)")
    args = parser.parse_args(argv)

    mapping_path = Path(args.mapping)
    if not mapping_path.is_file():
        print(f"ERROR: mapping no encontrado: {mapping_path}", file=sys.stderr)
        return 1
    try:
        mapping = load_mapping(mapping_path)
    except TransformError as exc:
        print(f"ERROR: diccionario inválido: {exc}", file=sys.stderr)
        return 2

    input_dir = Path(args.input)
    if not input_dir.is_dir():
        print(f"ERROR: kit de entrada no encontrado: {input_dir}", file=sys.stderr)
        return 1
    output_dir = Path(args.output)

    try:
        plan = run_transform(input_dir, output_dir, mapping, dry_run=args.dry_run)
    except TransformError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    text = render_plan(plan, input_dir, output_dir, dry_run=args.dry_run)
    print(text)
    if args.dry_run:
        return 0

    # BOLT-002: verificar tokens prohibidos y persistir la evidencia del run
    from report import (build_report, detect_version, make_run_id,
                        persist_evidence, prune_runs)
    from verify import verify_tree

    version = detect_version(input_dir)
    hits = verify_tree(output_dir)
    rep = build_report(plan, input_dir, output_dir, hits)
    ev_dir = persist_evidence(
        Path(args.reports), version, make_run_id(),
        rep, plan, input_dir, output_dir, hits, log_text=text)
    print(f"evidencia: {ev_dir}")
    # Retención acotada (R6, SPEC rev 2): purgar corridas anteriores de la versión
    pruned = prune_runs(Path(args.reports), version, keep=args.keep_runs)
    if pruned:
        prune_line = f"purgadas (retención {args.keep_runs} por versión): " + ", ".join(pruned)
        with (ev_dir / "run.log").open("a", encoding="utf-8") as logf:
            logf.write("\n" + prune_line + "\n")
        print(prune_line)
    if hits:
        print(f"ERROR: {len(hits)} token(s) prohibido(s) en el kit de salida:",
              file=sys.stderr)
        for h in hits[:20]:
            print(f"  {h['path']}:{h['line']} [{h['token']}] {h['context']}",
                  file=sys.stderr)
        print(f"Detalle completo en {ev_dir / 'report.json'}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
