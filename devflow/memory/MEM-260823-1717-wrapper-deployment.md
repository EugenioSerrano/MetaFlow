---
id: "MEM-260823-1717"
title: "Deployment Model-Y fix — coordinator wrappers removed, 20 role wrappers committed, the four main platform files carry the orchestrator identity (US-023.BOLT-003, V-Bounce 2)"
date: "2026-08-23"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
bolt: "US-023.BOLT-003"
spec: "devflow/spec/SPEC-260823-1602-wrapper-deployment.md"
spec_revision: 1
v_bounce: 2
execution_outcome: "ready_for_review"
baseline: "45d553f"
applied_adrs:
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "devflow/metrics/bolts/US-023.BOLT-003-wrapper-deployment.json"
diff_ref: ""
review_ready_at: "2026-08-23T17:17:00-03:00"
review: # AITL-MEM-Approval — recorded by the human reviewer (§3.0); decision dictated in conversation ("apruebo todos los mems, los bolts y la US23 de una") and transcribed by the agent
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-23T17:20:00-03:00"
  decided_at: "2026-08-23T17:21:43-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved as Dev-validator: the Model-Y deployment verified — coordinator wrappers removed, 20 role wrappers with parity PASS, the four main files carry the orchestrator identity (byte-sync 2 lines, G-count 39×5), VERIFICATION.md aligned. V-Bounce 2 approved — BOLT-003 Development Completed."
---

# MEM-260823-1717 — Deployment Model-Y fix (US-023.BOLT-003, V-Bounce 2)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | US-023.BOLT-003 (wrapper-deployment) |
| **SPEC**        | [SPEC-260823-1602](../spec/SPEC-260823-1602-wrapper-deployment.md) rev 1 |
| **V-Bounce**    | 2 (review-driven refinement — V-Bounce 1 MEM-1618 superseded) |
| **ADRs**        | ADR-004 (kit-only) |

---

## 1. Executive summary

This V-Bounce applies the **Model Y** deployment fix (the Coordinator is
the platform agent itself, ADR-007 §3.4): the four redundant
`coordinator.*` sub-agent wrappers were **removed** from the kit's
platform folders, the set was **regenerated with the BOLT-002 V-Bounce 2
generator** (which skips the coordinator), leaving **20 role wrappers** (5
roles × 4 platforms), and the **N×4 parity holds (0 drift)**. The
**spawn-topology enforcement (AC-6) now has its home in the four main
platform files**: each preamble carries the per-platform mechanics line
(Claude: the `Agent(...)` allowlist; OpenCode: the Coordinator keeps
`permission.task`; Copilot: the `agent` alias; Codex: instruction-based —
recorded) and the **shared body** (byte-identical ×4) gained the
**Coordinator (the orchestrator)** paragraph — routes, delegates
production, spawns approvers, records, **never signs** (`approves: []`),
approvers spawnable only through it. The four-agent sync is preserved
(2 sanctioned diff lines per agent) and the G-count holds at 39×5.
`VERIFICATION.md` was updated to the Model-Y topology framing, and the
BOLT-004 smoke runbook's topology step was aligned. The executor side of
the topology was already encoded in the role wrappers (no `Agent` tool /
`task: deny` / no `agent` alias), so "executors cannot spawn approvers" is
enforced on both sides now: restricted executors + the Coordinator's
allowlist declared in its own (main) files.

## 2. Implemented phases

### Phase A — The deployed set corrected

Removed `coordinator.md` (`.claude/agents/`), `coordinator.md`
(`.opencode/agents/`), `coordinator.agent.md` (`.github/agents/`) and
`coordinator.toml` (`.codex/agents/`) — the redundant sub-agent wrappers.
Regenerated with the BOLT-002 VB2 generator → 20 role wrappers; parity
PASS.

### Phase B — The four main files' orchestrator touch (minimal)

Shared body (byte-identical ×4): the "**The Coordinator (the
orchestrator)**" paragraph after the Actor paragraph — the Avenga DevFlow
agent itself is the Coordinator; routes, delegates production, spawns
approvers, records, **never signs**; approvers spawnable only through it;
per-platform mechanics in the preamble (US-023 AC-6). Preambles (exempt
zone, per platform): the spawn-topology line (Claude `Agent(...)`
allowlist with the 5 role ids; OpenCode `permission.task` kept by the
Coordinator; Copilot `agent` alias; Codex instruction-based — recorded).
Byte-sync verified (2 diff lines per agent), G-count 39×5.

### Phase C — Notes aligned

`VERIFICATION.md` updated to the Model-Y topology framing (the
Coordinator = the main platform agent; its preamble declares the
allowlist; executors restricted). The smoke runbook's topology step
aligned (MODEL Y).

## 3. Files created

| File | Purpose |
|------|---------|
| — | none (edits + removals within the kit) |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `distribution-kit/.claude/agents/*.md` (×5) | Regenerated role wrappers (no coordinator) |
| `distribution-kit/.opencode/agents/*.md` (×5) | Regenerated role wrappers (no coordinator) |
| `distribution-kit/.github/agents/*.agent.md` (×5) | Regenerated role wrappers (no coordinator) |
| `distribution-kit/.codex/agents/*.toml` (×5) | Regenerated role wrappers (no coordinator) |
| `distribution-kit/CLAUDE.md` | Preamble: the spawn-allowlist line (Agent(...)); shared body: the Coordinator paragraph |
| `distribution-kit/.agents/skills/avenga-devflow/SKILL.md` | Preamble: the Codex instruction-based topology line; shared body: the Coordinator paragraph (byte-identical) |
| `distribution-kit/.github/agents/AvengaDevFlow.agent.md` | Preamble: the agent-alias topology line; shared body: the Coordinator paragraph (byte-identical) |
| `distribution-kit/.opencode/agents/AvengaDevFlow.md` | Preamble: the permission.task topology line; shared body: the Coordinator paragraph (byte-identical) |
| `distribution-kit/devflow/agents/VERIFICATION.md` | Model-Y topology framing per platform |
| `tools/agent-wrappers/smoke/README.md` | Topology step aligned (MODEL Y) |

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
| — | — | — |

## 6. Files deleted

| File | Reason |
|------|--------|
| `distribution-kit/.claude/agents/coordinator.md` | Model Y: the Coordinator is the platform agent itself — no redundant sub-agent wrapper |
| `distribution-kit/.opencode/agents/coordinator.md` | Same |
| `distribution-kit/.github/agents/coordinator.agent.md` | Same |
| `distribution-kit/.codex/agents/coordinator.toml` | Same |

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| The coordinator wrappers are removed, not kept | Model Y: a sub-agent wrapper for the Coordinator contradicts ADR-007 §3.4 ("the evolution of today's platform agent") — the reviewer's philosophical point |
| AC-6's home moves to the four main files (minimal touch) | The spawn allowlist must live where the Coordinator actually is — the main platform agent; byte-sync + G-count preserved (US-016) |
| The shared-body paragraph is byte-identical ×4 | The four-agent sync invariant; the platform mechanics go in the exempt preambles |
| The executors' restriction stays in the role wrappers | Both sides of the topology now enforced: executors cannot spawn (wrappers), approvers spawnable only through the Coordinator (main files) |

## 8. Deviations and assumptions

No deviations from SPEC-260823-1602 rev 1 (refinement in place). Assumption: the pilot US re-verifies the spawn + the topology mechanics per platform (DISC-002 §7 #1).

## 9. Verification evidence

### Deployment (RED → GREEN)

```
RED:   4 coordinator.* wrappers present (redundant) — 24 wrappers
GREEN: coordinator.* removed; regenerated → 20 role wrappers
       python tools/agent-wrappers/parity.py … → PASS: 20 wrappers, 0 drift
```

### Four-agent sync + G-count (US-016 discipline)

```
tail from '# Avenga DevFlow v5.1 (Methodology)' + CR-strip + diff vs CLAUDE:
  codex 2 · ghcopilot 2 · opencode 2 diff lines (sanctioned agents-data
  path only)                                              PASS
G-count: GUARDRAILS 39 + CLAUDE 39 + SKILL 39 + agent.md 39 + AvengaDevFlow.md 39  PASS
Coordinator paragraph present ×4                          PASS
```

### Invariants

```
Trees: .claude 5 · .opencode 6 (5+main) · .github 6 (5+main) · .codex 5  PASS
Kit-only: only distribution-kit/ + tools/ files changed             PASS
No junk (angle-bracket) files                                       PASS
```

### Gates

Deployment Bolt: unit/integration → **pass** (14 — the tool suite);
SAST/SBOM, perf, IP, PII, dep-confusion → `n/a`; prompt-injection →
`pass`; secret-leak → `pass`; hallucination-lint → `pass`;
behavioral-reproducibility → `pass` (parity reproduces);
bolt-manifest-validation → `pass`.

## 10. Manual interventions

None — the agent produced everything.

## 11. Evidence links

- **Diff / PR:** none (working tree, uncommitted)
- **Commit:** baseline `45d553f`
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-023.BOLT-003-wrapper-deployment.json`

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~12min |
| V-Bounce number | 2 |
| Tests created | 14 (tool suite — via BOLT-002 VB2) |
| AI-generated code | 100% |
| First-pass approval | pending (this MEM) |

## 13. Pending items and stubs

- [ ] The pilot US re-verifies the spawn + topology per platform (DISC-002
      §7 #1); the human-run smoke (BOLT-004) is ready
- [ ] Batch approvals (all pending MEMs) + AITL-BOLT-DONE ×4

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
| **review_ready_at** | `2026-08-23T17:17:00-03:00` |
| **review.started_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **review.decided_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **Review evidence** | diff of the removed/regenerated wrappers + the four main files (preamble + shared body) + VERIFICATION.md; parity PASS; byte-sync 2 lines; G-count 39×5; MEM, manifest |
| **Comments** | |
| **Findings** | |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | evidence inspected per the review-evidence column |
