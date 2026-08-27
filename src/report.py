"""Reporte de transformación y persistencia de evidencia — BOLT-002.

Consume el plan del engine (reglas aplicadas, remociones, exclusiones,
changed/unchanged) y los hits del verificador, y persiste por run la
evidencia completa en transform-reports/<versión>/<run>/:
report.json (estructurado para IA), report.md (legible), diff/*.diff
(original → convertido), unchanged.txt, removals.json y run.log.
La carpeta de evidencia nunca se borra automáticamente (R6, AC-11).
"""
from __future__ import annotations

import difflib
import json
import shutil
from datetime import datetime
from pathlib import Path


def detect_version(input_dir: Path) -> str:
    """Versión del kit de entrada (devflow/VERSION); 'unknown' si no existe."""
    vf = input_dir / "devflow" / "VERSION"
    if vf.is_file():
        return vf.read_text(encoding="utf-8").strip() or "unknown"
    return "unknown"


def make_run_id(now: datetime | None = None) -> str:
    return (now or datetime.now()).strftime("%Y%m%d-%H%M%S")


def unified_diff(src_text: str, dst_text: str, src_name: str, dst_name: str) -> str:
    """Diff unificado original → convertido (stdlib difflib)."""
    return "".join(difflib.unified_diff(
        src_text.splitlines(keepends=True),
        dst_text.splitlines(keepends=True),
        fromfile=src_name, tofile=dst_name))


def build_report(plan: list, input_dir: Path, output_dir: Path, hits: list) -> dict:
    """Reporte estructurado del run (fuente para revisión humana o IA)."""
    files = []
    totals_applied: dict = {}
    totals_removals: dict = {}
    for e in plan:
        if e["kind"] == "dir":
            continue
        if e["kind"] == "excluded":
            files.append({"src": e["rel"], "status": "excluded"})
            continue
        dst = e["dst"].relative_to(output_dir).as_posix()
        if e["kind"] == "binary":
            files.append({"src": e["rel"], "dst": dst, "status": "binary-copy"})
            continue
        files.append({
            "src": e["rel"], "dst": dst,
            "status": "changed" if e.get("changed") else "unchanged",
            "rules_applied": e.get("applied", {}),
            "removals": e.get("removals", {}),
        })
        for k, v in e.get("applied", {}).items():
            totals_applied[k] = totals_applied.get(k, 0) + v
        for k, v in e.get("removals", {}).items():
            totals_removals[k] = totals_removals.get(k, 0) + v

    changed = [f for f in files if f["status"] == "changed"]
    unchanged = [f for f in files if f["status"] == "unchanged"]
    return {
        "run": {
            "version": detect_version(input_dir),
            "generated_at": make_run_id(),
        },
        "totals": {
            "files": len(files) - len([f for f in files if f["status"] == "excluded"]),
            "changed": len(changed),
            "unchanged": len(unchanged),
            "excluded": len([f for f in files if f["status"] == "excluded"]),
            "rules_applied": totals_applied,
            "removals": totals_removals,
        },
        "verification": {"ok": not hits, "hits": hits},
        "files": files,
    }


def build_markdown(report: dict) -> str:
    lines = [
        "# Reporte de transformación MetaFlow", "",
        f"- Versión: {report['run']['version']}",
        f"- Generado: {report['run']['generated_at']}",
        "- Verificación: " + ("OK — cero tokens prohibidos"
                              if report["verification"]["ok"]
                              else f"FAIL — {len(report['verification']['hits'])} hits"),
        "", "## Totales",
        f"- Archivos: {report['totals']['files']}",
        f"- Cambiados: {report['totals']['changed']}",
        f"- Sin cambios: {report['totals']['unchanged']}",
        f"- Excluidos: {report['totals']['excluded']}",
        "- Reglas aplicadas: " + ", ".join(
            f"{k}x{v}" for k, v in sorted(report["totals"]["rules_applied"].items())),
        "- Remociones: " + ", ".join(
            f"{k}x{v}" for k, v in sorted(report["totals"]["removals"].items())),
        "", "## Archivos", "",
    ]
    for f in report["files"]:
        dst = f.get("dst", "(excluido)")
        lines.append(f"- {f['src']} -> {dst} [{f['status']}]")
    if report["verification"]["hits"]:
        lines += ["", "## Hits de verificación", ""]
        for h in report["verification"]["hits"]:
            lines.append(f"- {h['path']}:{h['line']} [{h['token']}] {h['context']}")
    return "\n".join(lines) + "\n"


def persist_evidence(reports_root: Path, version: str, run_id: str, report: dict,
                     plan: list, input_dir: Path, output_dir: Path, hits: list,
                     log_text: str = "") -> Path:
    """Persiste la evidencia del run en reports_root/<version>/<run_id>/.

    Aditivo por diseño (R6): nunca borra carpetas de runs previos.
    """
    folder = reports_root / version / run_id
    folder.mkdir(parents=True, exist_ok=True)

    (folder / "report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    (folder / "report.md").write_text(build_markdown(report), encoding="utf-8")

    diff_dir = folder / "diff"
    diff_dir.mkdir(exist_ok=True)
    for e in plan:
        if e["kind"] == "file" and e.get("changed"):
            src_text = e["src"].read_text(encoding="utf-8")
            dst_path = e["dst"]
            dst_text = dst_path.read_text(encoding="utf-8") if dst_path.is_file() else ""
            dst_rel = e["dst"].relative_to(output_dir).as_posix()
            diff = unified_diff(src_text, dst_text, e["rel"], dst_rel)
            (diff_dir / (dst_rel.replace("/", "__") + ".diff")).write_text(
                diff, encoding="utf-8")

    unchanged = [f["src"] for f in report["files"] if f["status"] == "unchanged"]
    (folder / "unchanged.txt").write_text(
        "\n".join(unchanged) + ("\n" if unchanged else ""), encoding="utf-8")

    removals: dict = {}
    for f in report["files"]:
        for k, v in f.get("removals", {}).items():
            removals[k] = removals.get(k, 0) + v
    (folder / "removals.json").write_text(
        json.dumps(removals, indent=2, ensure_ascii=False), encoding="utf-8")

    (folder / "run.log").write_text(log_text, encoding="utf-8")
    return folder


def prune_runs(reports_root: Path, version: str, keep: int = 2) -> list:
    """Retención acotada (R6, rev 2): conserva las `keep` corridas más recientes
    de la versión y borra las anteriores. Devuelve los run_ids purgados.

    Los nombres de run son timestamps YYYYMMDD-HHMMSS: el orden
    lexicográfico es el cronológico. Nunca purga en dry-run (solo se llama
    desde corridas reales) y nunca toca otras versiones.
    """
    version_dir = reports_root / version
    if not version_dir.is_dir():
        return []
    runs = sorted([p for p in version_dir.iterdir() if p.is_dir()])
    pruned = runs[:-keep] if keep > 0 and len(runs) > keep else []
    for p in pruned:
        shutil.rmtree(p)
    return [p.name for p in pruned]
