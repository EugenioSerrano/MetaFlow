"""Minimal deterministic parser for the canonical DevFlow Agent definition
files (a constrained YAML subset). Dependency-free — a maintainer tool must
run anywhere.

Supported: comments, `key: value`, `key: >` block scalars, inline lists
`[a, b]`, dash lists, and ONE nested map level (the `capabilities:` map).
"""

import re

_KEY_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(.*)$")


def _strip_comment(line: str) -> str:
    """Remove a trailing # comment, respecting single/double quotes."""
    in_s = in_d = False
    for i, ch in enumerate(line):
        if ch == '"' and not in_s:
            in_d = not in_d
        elif ch == "'" and not in_d:
            in_s = not in_s
        elif ch == "#" and not in_s and not in_d:
            return line[:i]
    return line


def _clean(value: str) -> str:
    return value.strip().strip('"').strip("'")


def parse(text: str) -> dict:
    """Parse the canonical subset into a dict.

    Returns: {"id": ..., "description": ..., "capabilities": {"tier": ...,
    "tools": [...], "mcp_servers": [...]}, ...} — plain str/list/dict.
    """
    lines = text.splitlines()
    data: dict = {}
    nested: dict | None = None
    i = 0
    while i < len(lines):
        line = _strip_comment(lines[i]).rstrip()
        if not line.strip():
            i += 1
            continue
        indent = len(line) - len(line.lstrip())
        stripped = line.lstrip()
        if stripped.startswith("- "):
            i += 1  # dangling list item (not expected at top level)
            continue
        m = _KEY_RE.match(stripped)
        if not m:
            i += 1
            continue
        key, rest = m.group(1), m.group(2).strip()
        if indent == 0:
            nested = None
        target = nested if (nested is not None and indent > 0) else data

        if rest == ">":  # block scalar
            target[key] = ""
            i += 1
            while i < len(lines):
                nxt = _strip_comment(lines[i]).rstrip()
                if not nxt.strip():
                    i += 1
                    continue
                if len(nxt) - len(nxt.lstrip()) > 0:
                    target[key] += "\n" + nxt.strip()
                    i += 1
                else:
                    break
            continue

        if rest == "":  # nested map OR dash list under an empty key
            # Look ahead: if the next content line is a deeper-indented
            # dash item, this is a list (escalation:); otherwise a map.
            j = i + 1
            is_list = False
            while j < len(lines):
                nxt = _strip_comment(lines[j]).rstrip()
                if not nxt.strip():
                    j += 1
                    continue
                nind = len(nxt) - len(nxt.lstrip())
                is_list = nind > indent and nxt.lstrip().startswith("- ")
                break
            if is_list:
                items = []
                j = i + 1
                while j < len(lines):
                    nxt = _strip_comment(lines[j]).rstrip()
                    if not nxt.strip():
                        j += 1
                        continue
                    nind = len(nxt) - len(nxt.lstrip())
                    if nind > indent and nxt.lstrip().startswith("- "):
                        items.append(_clean(nxt.lstrip()[2:]))
                        j += 1
                    else:
                        break
                target[key] = items
                i = j
            else:
                target[key] = {}
                if indent == 0:
                    nested = target[key]
                i += 1
            continue

        if rest.startswith("[") and rest.endswith("]"):  # inline list
            inner = rest[1:-1].strip()
            target[key] = (
                [_clean(x) for x in inner.split(",")] if inner else []
            )
            i += 1
            continue

        if rest.startswith("- "):  # dash list, consumed eagerly
            items = [_clean(rest[2:])]
            i += 1
            while i < len(lines):
                nxt = _strip_comment(lines[i]).rstrip()
                if not nxt.strip():
                    i += 1
                    continue
                nind = len(nxt) - len(nxt.lstrip())
                if nind == indent and nxt.lstrip().startswith("- "):
                    items.append(_clean(nxt.lstrip()[2:]))
                    i += 1
                else:
                    break
            target[key] = items
            continue

        target[key] = _clean(rest)
        i += 1
    return data
