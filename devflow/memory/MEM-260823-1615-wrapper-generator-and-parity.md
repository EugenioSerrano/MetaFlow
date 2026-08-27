---
id: "MEM-260823-1615"
title: "Wrapper generator and N×4 parity check — the tools/agent-wrappers tool delivered (US-023.BOLT-002)"
date: "2026-08-23"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
bolt: "US-023.BOLT-002"
spec: "devflow/spec/SPEC-260823-1601-wrapper-generator-and-parity.md"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "45d553f"
applied_adrs:
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "devflow/metrics/bolts/US-023.BOLT-002-wrapper-generator-and-parity.json"
diff_ref: ""
review_ready_at: "2026-08-23T16:15:00-03:00"
review: # AITL-MEM-Approval — filled by the human reviewer (§3.0)
  decision: "" # approved | changes_requested | rejected
  reviewers: [] # [{actor, role, model}]
  started_at: "" # ISO 8601 with seconds + offset
  decided_at: "" # ISO 8601 with seconds + offset
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: ""
---

# MEM-260823-1615 — The wrapper generator and parity check (US-023.BOLT-002, V-Bounce 1)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | US-023.BOLT-002 (wrapper-generator-and-parity) |
| **SPEC**        | [SPEC-260823-1601](../spec/SPEC-260823-1601-wrapper-generator-and-parity.md) rev 1 |
| **V-Bounce**    | 1 |
| **ADRs**        | ADR-004 (kit-only) |

---

## 1. Executive summary

This V-Bounce delivered `tools/agent-wrappers/` — the maintainer tool that
projects the canonical DevFlow Agent definitions (BOLT-001) into the four
platform wrapper shapes and verifies the **N×4 parity**. The tool is
**dependency-free** by design: `agentmodel.py` is a small deterministic
parser for the canonical `agent.yaml` subset (comments, scalars, `>` block
scalars, inline lists, dash lists, one nested map level) so it runs
anywhere without PyYAML; `generate.py` builds the four shapes per
DISC-002 §4.2 (Claude Code `.claude/agents/*.md`, OpenCode
`.opencode/agents/*.md`, GitHub Copilot `.github/agents/*.agent.md`, Codex
`.codex/agents/*.toml` with the charter body as the system prompt);
`parity.py` regenerates into a temp tree and diffs against the committed
set — any drift, missing or extra wrapper FAILS (the "never hand-edit the
wrappers" invariant made mechanical). The unit suite (10 tests) covers the
parser, the four builders (including the MCP-omission rule when
`mcp_servers: []`), the end-to-end generation, and the missing-field
fail-fast. Verification is GREEN: **10/10 tests pass**, and a generation
run over the BOLT-001 definitions produces **24 wrappers (6 agents × 4
platforms)**. The Codex/Copilot known gaps are recorded in DESIGN.md with
their fallbacks (DISC-002 rec #6); the per-platform re-verification note
lands with the deployment Bolt. The committed wrapper set (BOLT-003) will
be the parity check's diff target.

## 2. Implemented phases

### Phase A — The generator

Created `tools/agent-wrappers/` with `DESIGN.md` (the mapping rules, the
platform shapes table, the recorded Codex/Copilot gaps and their
fallbacks, usage), `agentmodel.py` (the mini-parser), and `generate.py`
(the CLI: `python generate.py <agents-dir> [--out <root>]` — default
output lands in the kit's platform folders; `--out` targets a temp tree
for verification). Each builder maps the canonical fields to the platform
vocabulary: Claude Code frontmatter (`name`/`description`/`tools` mapped
to Read/Grep/Glob/Bash/Edit/Write/`model`/`mcpServers` only when named),
OpenCode (`mode: subagent` + per-tool `permission`), GitHub Copilot
(`name`/`description`/`tools`/`model`), Codex (TOML `[agents.<id>]` +
`[agents.<id>.prompt]` with the charter as the `system` block, escaped).

### Phase B — The N×4 parity check

Created `parity.py`: regenerates the wrappers from the canonical
definitions into a temp tree, diffs them against the committed set in the
kit, and reports missing/extra/drifted files — exit 0 = PASS, 1 = FAIL.
This is the four-agent sync discipline extended to N roles × 4 platforms;
the committed set (BOLT-003) is its diff target.

### Phase C — Verification (GREEN)

Ran the unit suite (10/10 OK) and a generation run over the BOLT-001
definitions (24 wrappers, 6 agents × 4 platforms).

## 3. Files created

| File | Purpose |
|------|---------|
| `tools/agent-wrappers/DESIGN.md` | The design doc — platform mapping, shapes table, recorded Codex/Copilot gaps + fallbacks (DISC-002 rec #6), usage |
| `tools/agent-wrappers/agentmodel.py` | The dependency-free mini-parser for the canonical `agent.yaml` subset (comments, block scalars, lists, nested map) |
| `tools/agent-wrappers/generate.py` | The generator CLI — canonical definitions → the four platform wrapper shapes |
| `tools/agent-wrappers/parity.py` | The N×4 parity check — regenerate + diff the committed set (0 drift or FAIL) |
| `tools/agent-wrappers/tests/test_generate.py` | 10 unit tests — parser, builders (incl. MCP omission), end-to-end, fail-fast |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| — | none (new tool folder only) |

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
| — | — | — |

## 6. Files deleted

| File | Reason |
|------|--------|
| — | — |

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| Dependency-free mini-parser instead of PyYAML | A maintainer tool must run anywhere (the kit's tooling philosophy); the canonical subset is small and fixed |
| Dash lists under an empty key supported (e.g. `escalation:`) | The canonical files use that shape; the initial parser missed it and the tests caught it (red → green) |
| Parity = regenerate + diff the committed set | The strongest drift check — a hand-edited wrapper fails mechanically ("never hand-edit to pass") |
| Codex TOML carries the charter as the `system` block | DISC-002 §4.2: role files with full config override; the generic-spawn fallback is documented for the known invocation gaps |
| `mcpServers` omitted when empty | The `[]` default must not leak an empty server block; named servers appear explicitly (AC-8) |

## 8. Deviations and assumptions

No deviations from SPEC-260823-1601 rev 1. Assumption: the platform shapes
follow DISC-002 §4.2 as re-verified at implementation — the Codex/Copilot
gaps are recorded in DESIGN.md and will be re-checked during the
deployment Bolt (BOLT-003).

## 9. Verification evidence

### Tests

```
python -m unittest discover -s tools/agent-wrappers/tests
Ran 10 tests in 0.020s — OK
```

### Generation run

```
python tools/agent-wrappers/generate.py distribution-kit/devflow/agents --out <tmp>
OK: 24 wrappers for 6 agents x 4 platforms
```

### Parity (RED state for BOLT-003)

```
No committed wrappers yet — parity.py reports the missing set (expected:
the deployment Bolt commits them; the check then must PASS with 0 drift).
```

### Invariants

```
Kit + tools only: git status shows only tools/agent-wrappers/ (new) +
the BOLT-001 agents/ folder (new) — no root devflow/ changes.  PASS
```

### Gates

Tooling Bolt: unit/integration → **pass** (10 tests); SAST/SBOM,
perf-smoke, IP, PII, dep-confusion → `n/a` (internal tooling, no external
deps); prompt-injection → `pass` (the generator treats agent.yaml as
data; no external content); secret-leak → `pass`; hallucination-lint →
`pass` (platform mapping refs recorded in DESIGN); test-first → `n/a`
(tooling — the tests ARE the evidence); behavioral-reproducibility →
`pass` (same input → same wrappers); bolt-manifest-validation → `pass`.

## 10. Manual interventions

None — the agent produced everything.

## 11. Evidence links

- **Diff / PR:** none (working tree, uncommitted)
- **Commit:** baseline `45d553f`
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-023.BOLT-002-wrapper-generator-and-parity.json`

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~15min |
| V-Bounce number | 1 |
| Tests created | 10 (unit: parser 3, builders 5, end-to-end 2) |
| AI-generated code | 100% |
| First-pass approval | pending (this MEM) |

## 13. Pending items and stubs

- [ ] BOLT-003 V-Bounce (generate + commit the wrappers; parity over the
      committed set; per-platform verification notes)
- [ ] BOLT-004 (smoke on Claude Code)

## 14. AITL-MEM-Approval

> **Avenga DevFlow §2.12, §3.0.** This MEM is created by the agent with no
> mutable status and is **never self-approved**. A qualified human (the
> Dev-validator who executed the Bolt) inspects the actual diff,
> test/gate evidence, MEM and manifest, and records `AITL-MEM-Approval`
> here and in the manifest's `checkpoint_approvals[]`.

| Field | Value |
|-------|-------|
| **Reviewers (executing Dev-validator)** | `human:eugenio.serrano` |
| **Roles** | dev_validator |
| **Decision** | approved / changes_requested / rejected |
| **review_ready_at** | `2026-08-23T16:15:00-03:00` |
| **review.started_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **review.decided_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **Review evidence** | diff of tools/agent-wrappers/; test run (10/10); generation run (24 wrappers); kit+tools only; MEM, manifest |
| **Comments** | |
| **Findings** | |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | evidence inspected per the review-evidence column |
