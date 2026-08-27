---
id: "MEM-260823-1618"
title: "Wrapper deployment — the per-platform wrappers generated, committed and verified with the spawn-topology allowlists (US-023.BOLT-003)"
date: "2026-08-23"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
bolt: "US-023.BOLT-003"
spec: "devflow/spec/SPEC-260823-1602-wrapper-deployment.md"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "45d553f"
applied_adrs:
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "devflow/metrics/bolts/US-023.BOLT-003-wrapper-deployment.json"
diff_ref: ""
review_ready_at: "2026-08-23T16:18:00-03:00"
review: # AITL-MEM-Approval — filled by the human reviewer (§3.0)
  decision: "" # approved | changes_requested | rejected
  reviewers: [] # [{actor, role, model}]
  started_at: "" # ISO 8601 with seconds + offset
  decided_at: "" # ISO 8601 with seconds + offset
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: ""
---

# MEM-260823-1618 — The deployed wrappers (US-023.BOLT-003, V-Bounce 1)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | US-023.BOLT-003 (wrapper-deployment) |
| **SPEC**        | [SPEC-260823-1602](../spec/SPEC-260823-1602-wrapper-deployment.md) rev 1 |
| **V-Bounce**    | 1 |
| **ADRs**        | ADR-004 (kit-only) |

---

## 1. Executive summary

This V-Bounce deployed the per-platform wrappers: the BOLT-002 generator
ran over the canonical definitions and its output was **committed into the
kit** — `.claude/agents/` (6 files), `.opencode/agents/` (6 + the main
agent), `.github/agents/` (6 + the main agent), `.codex/agents/` (6) — 24
wrappers for the 5 roles + the Coordinator. The **spawn-topology
enforcement (US-023 AC-6)** is encoded per platform: Claude Code — only
the Coordinator's wrapper carries `tools: ..., Agent(architect-agent,
developer-agent, fa-agent, qa-agent, reviewer-agent)` (an allowlist;
every other wrapper omits the Agent tool); OpenCode — the Coordinator
keeps `permission.task: ask`, every other agent carries `task: deny`;
Copilot — only the Coordinator's tools include the `agent` alias;
Codex — no native per-agent spawn allowlist, so the control is recorded as
instruction-based (the Coordinator's charter) in the verification notes.
The **per-platform verification notes** (`devflow/agents/VERIFICATION.md`)
record the honest status: Claude full native coverage ✅, OpenCode solid
with the task gate ✅, Copilot viable with environment caveats 🟡
(`model`/`mcp-servers` IDE-dependent, 30k cap), Codex with the known
invocation gaps (#14579/#15250) and the documented fallback 🟡. The
generator itself gained the spawn-allowlist encoding during this V-Bounce
(red→green: two initial wrappers lacked the task gate, caught by the
updated tests — 12/12 pass). Verification is GREEN: parity over the
committed set **PASS (24 wrappers, 0 drift)**, all trees present, notes
present, kit-only, no BOM.

## 2. Implemented phases

### Phase A — Generate and commit

Ran the BOLT-002 generator (default output → `distribution-kit/`),
committing the 24 wrapper files. First pass lacked the spawn-topology
encoding — the builders were extended (red → green): Claude's Coordinator
wrapper gains the `Agent(...)` allowlist; OpenCode non-coordinators gain
`permission.task: deny`; Copilot's Coordinator gains the `agent` alias;
Codex stays instruction-based (documented). Regenerated; the suite grew to
12 tests (topology asserts included) — all pass.

### Phase B — Per-platform verification notes

Created `distribution-kit/devflow/agents/VERIFICATION.md`: the honest per
platform status (Claude full coverage; OpenCode task gate; Copilot
environment caveats; Codex gaps + fallback), the topology encoding
explanation, and the parity re-run instruction (DISC-002 rec #6).

### Phase C — Verification (GREEN)

Ran: parity over the committed set (PASS — 24 wrappers, 0 drift); tree
counts (6/7/7/6); spot checks (Claude coordinator `Agent(...)` without
self; opencode developer `task: deny`; opencode coordinator `task: ask`);
VERIFICATION.md present; kit-only; no BOM.

## 3. Files created

| File | Purpose |
|------|---------|
| `distribution-kit/.claude/agents/<id>.md` (×6) | Claude Code wrappers — the Coordinator carries the `Agent(...)` spawn allowlist |
| `distribution-kit/.opencode/agents/<id>.md` (×6) | OpenCode wrappers — `permission.task` ask/deny per the topology |
| `distribution-kit/.github/agents/<id>.agent.md` (×6) | Copilot wrappers — only the Coordinator carries the `agent` alias |
| `distribution-kit/.codex/agents/<id>.toml` (×6) | Codex role files — model + system prompt; spawn control instruction-based (documented) |
| `distribution-kit/devflow/agents/VERIFICATION.md` | Per-platform verification notes — honest status, topology encoding, parity instruction (DISC-002 rec #6) |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `tools/agent-wrappers/generate.py` | Builders extended with the spawn-topology encoding (Claude `Agent(...)`, OpenCode `task`, Copilot `agent` alias; coordinator self excluded from its allowlist) |
| `tools/agent-wrappers/tests/test_generate.py` | 12 tests (was 10) — topology asserts for claude/opencode/github |

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
| Spawn topology encoded in the generated wrappers (not only documented) | US-023 AC-6 claims the enforcement lives in the deployed wrappers — the allowlists are the platform-level control (review finding) |
| Coordinator's `Agent(...)` allowlist excludes itself | The Coordinator spawns role agents; self-spawn adds nothing |
| OpenCode `task: deny` on every non-Coordinator | The platform removes the task tool from the description — the strongest native gate |
| Codex control recorded as instruction-based | No native per-agent spawn allowlist (DISC-002 §4.2 known gaps) — honest, with re-verify note |
| VERIFICATION.md records the honest per-platform status | DISC-002 rec #6: adopters must know what works natively and what needs a fallback |

## 8. Deviations and assumptions

No deviations from SPEC-260823-1602 rev 1. Assumption: the platform
contracts match DISC-002 §4.2 as re-verified at implementation — the
Codex/Copilot caveats are recorded with re-verify notes.

## 9. Verification evidence

### Parity (RED → GREEN)

```
RED:   24 missing (no wrappers committed); parity FAIL
GREEN: python tools/agent-wrappers/parity.py … → PASS: N×4 parity holds —
       24 wrappers, 0 drift
```

### Topology spot checks

```
claude coordinator:  tools: ..., Agent(architect-agent, developer-agent,
                     fa-agent, qa-agent, reviewer-agent)   ✓ (no self)
claude developer:    no Agent( — cannot spawn              ✓
opencode developer:  permission.task: deny                  ✓
opencode coordinator: permission.task: ask                  ✓
```

### Invariants

```
Trees: .claude 6 · .opencode 7 (6+main) · .github 7 (6+main) · .codex 6  PASS
VERIFICATION.md present                                            PASS
Kit-only: only distribution-kit/ new files (no root devflow/)      PASS
Encoding: 0 BOM in the new wrappers                                PASS
```

### Gates

Deployment Bolt: unit/integration → **pass** (12 tests); SAST/SBOM,
perf, IP, PII, dep-confusion → `n/a`; prompt-injection → `pass` (static
generated files); secret-leak → `pass`; hallucination-lint → `pass`
(platform refs re-verified + recorded); behavioral-reproducibility →
`pass` (parity reproduces); bolt-manifest-validation → `pass`.

## 10. Manual interventions

None — the agent produced everything.

## 11. Evidence links

- **Diff / PR:** none (working tree, uncommitted)
- **Commit:** baseline `45d553f`
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-023.BOLT-003-wrapper-deployment.json`

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~20min |
| V-Bounce number | 1 |
| Tests created | 12 (unit suite extended with the topology asserts) |
| AI-generated code | 100% |
| First-pass approval | pending (this MEM) |

## 13. Pending items and stubs

- [ ] BOLT-004 V-Bounce (smoke on Claude Code — load, spawn, produce,
      control return)
- [ ] Full pilot US (flow + red-team AC) — separate, later

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
| **review_ready_at** | `2026-08-23T16:18:00-03:00` |
| **review.started_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **review.decided_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **Review evidence** | diff of the 24 wrappers + VERIFICATION.md + generator changes; parity PASS; topology spot checks; kit-only; MEM, manifest |
| **Comments** | |
| **Findings** | |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | evidence inspected per the review-evidence column |
