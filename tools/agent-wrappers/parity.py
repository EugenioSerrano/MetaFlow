#!/usr/bin/env python3
"""N×4 parity check (US-023.BOLT-002): regenerate the wrappers from the
canonical definitions into a temp tree and diff them against the committed
set in the kit. Any drift (hand-edited wrapper, stale generation, missing
file) FAILS. Exit 0 = PASS, 1 = FAIL.

Usage:
  python parity.py <agents-dir> <kit-root>
"""

import pathlib
import sys
import tempfile

from generate import generate, load_definitions


def main(argv=None) -> int:
    if len(argv or sys.argv[1:]) != 2:
        print("usage: parity.py <agents-dir> <kit-root>", file=sys.stderr)
        return 2
    agents_dir, kit_root = argv or sys.argv[1:]
    kit = pathlib.Path(kit_root)
    defs = load_definitions(agents_dir)
    with tempfile.TemporaryDirectory(prefix="agent-wrappers-parity-") as td:
        generated = {p.relative_to(td) for p in generate(defs, pathlib.Path(td))}
    committed = {p.relative_to(kit) for p in kit.rglob("*") if p.is_file()}
    expected = {p for p in generated}
    missing = sorted(expected - committed)
    extra = sorted(p for p in committed
                   if any(part.startswith((".claude", ".opencode",
                                          ".github", ".codex"))
                          for part in p.parts)
                   and "node_modules" not in p.parts
                   and p not in expected
                   and "AvengaDevFlow" not in p.name
                   and p.suffix in (".md", ".toml", ".agent.md"))
    drift = []
    for rel in sorted(expected & committed):
        got = (kit / rel).read_text(encoding="utf-8")
        with tempfile.TemporaryDirectory(prefix="agent-wrappers-parity-") as td:
            regen = next(p for p in generate(defs, pathlib.Path(td))
                         if p.relative_to(td) == rel)
            want = regen.read_text(encoding="utf-8")
        if got != want:
            drift.append(rel)
    problems = missing + extra + drift
    if problems:
        for p in problems:
            print(f"DRIFT: {p}")
        print(f"FAIL: {len(missing)} missing, {len(extra)} extra, "
              f"{len(drift)} drifted (expected N×4 = {len(expected)})")
        return 1
    print(f"PASS: N×4 parity holds — {len(expected)} wrappers, 0 drift")
    return 0


if __name__ == "__main__":
    sys.exit(main())
