---
id: "MEM-260823-1716"
title: "Generator Model-Y fix — only role agents are wrapped; TEMPLATE folders skipped (US-023.BOLT-002, V-Bounce 2)"
date: "2026-08-23"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
bolt: "US-023.BOLT-002"
spec: "devflow/spec/SPEC-260823-1601-wrapper-generator-and-parity.md"
spec_revision: 1
v_bounce: 2
execution_outcome: "ready_for_review"
baseline: "45d553f"
applied_adrs:
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "devflow/metrics/bolts/US-023.BOLT-002-wrapper-generator-and-parity.json"
diff_ref: ""
review_ready_at: "2026-08-23T17:16:00-03:00"
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
  acknowledgment_reason: "Approved as Dev-validator: the Model-Y generator fix (coordinator skipped), the TEMPLATE-* skip and the parity node_modules fix verified — 14/14 tests, 20 wrappers, parity PASS. V-Bounce 2 approved — BOLT-002 Development Completed."
---

# MEM-260823-1716 — Generator Model-Y fix (US-023.BOLT-002, V-Bounce 2)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | US-023.BOLT-002 (wrapper-generator-and-parity) |
| **SPEC**        | [SPEC-260823-1601](../spec/SPEC-260823-1601-wrapper-generator-and-parity.md) rev 1 |
| **V-Bounce**    | 2 (review-driven refinement — V-Bounce 1 MEM-1615 superseded) |
| **ADRs**        | ADR-004 (kit-only) |

---

## 1. Executive summary

This V-Bounce aligns the generator with **Model Y** (the Coordinator is
the platform agent itself, ADR-007 §3.4): `generate()` now **skips
`role: coordinator` definitions** — no separate coordinator sub-agent
wrapper is produced; only the **ROLE agents** (5) get wrappers (20 total,
down from 24). Two real defects were caught and fixed in the process:
**(1)** the first run after adding `TEMPLATE-new-role/` crashed with an
`OSError` (the template's `<your-agent-id>` placeholder is an invalid
Windows filename) → `load_definitions` now **skips `TEMPLATE-*` folders**
(templates are skeletons, never wrapped); **(2)** the parity check's
`extra` scan counted the kit's pre-existing `.opencode/node_modules`
files as drift → `node_modules` is excluded from the scan. The test suite
grew to **14 tests** (the two new ones: `test_coordinator_not_generated`
and `test_template_folder_skipped`), all passing; the generation run
produces exactly 20 wrappers and the **N×4 parity holds (0 drift)**.
`DESIGN.md` documents the Model-Y rule. The spawn-allowlist logic remains
in the builders (used when a coordinator-role definition is passed), but
the generation path never emits it — the Coordinator's allowlist lives in
the four main platform files (BOLT-003 V-Bounce 2).

## 2. Implemented phases

### Phase A — The Model-Y skip

`generate()` skips entries whose `role == "coordinator"` (with the MODEL Y
comment: the Coordinator is the platform agent itself; its projections are
the four main files, hand-synced). `DESIGN.md` gained the MODEL Y section
(only role agents get wrappers; no coordinator sub-agent).

### Phase B — The template skip + the parity fix

`load_definitions()` skips any path component starting with `TEMPLATE`
(the `TEMPLATE-new-role` placeholders are not valid filenames — the first
generation run crashed with `OSError`). `parity.py` excludes
`node_modules` from the `extra` scan (the kit's pre-existing opencode
deps are not wrappers).

### Phase C — Verification (GREEN)

14/14 tests; generation → 20 wrappers; parity → PASS (20, 0 drift).

## 3. Files created

| File | Purpose |
|------|---------|
| — | none (edits within the existing tool) |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `tools/agent-wrappers/generate.py` | `generate()` skips `role: coordinator` (Model Y); `load_definitions()` skips `TEMPLATE-*` folders |
| `tools/agent-wrappers/parity.py` | `node_modules` excluded from the `extra` scan |
| `tools/agent-wrappers/DESIGN.md` | MODEL Y section — only role agents are wrapped |
| `tools/agent-wrappers/tests/test_generate.py` | +2 tests (coordinator not generated; TEMPLATE folder skipped) — 14 total |

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
| The generator never emits a coordinator wrapper | Model Y: the Coordinator is the platform agent itself; a sub-agent wrapper for it is redundant and contradicts ADR-007 §3.4 |
| `TEMPLATE-*` folders skipped in `load_definitions` | Templates are skeletons — their placeholders are not valid ids/filenames (the OSError proved it) |
| `node_modules` excluded from parity's extra scan | The kit's pre-existing opencode deps are not wrappers; the scan must look at the agent folders' wrapper files only |
| The builders keep the coordinator spawn-allowlist logic | The tests cover it directly; if a project ever defines a coordinator-role entry for its own purposes, the builder is ready — the kit's generation path just never uses it for the Coordinator |

## 8. Deviations and assumptions

No deviations from SPEC-260823-1601 rev 1 (refinement in place). Assumption: the Coordinator's per-platform allowlist lands in the four main files (BOLT-003 V-Bounce 2).

## 9. Verification evidence

### Tests (RED → GREEN)

```
RED:   12 tests → after the Model-Y changes, the first generation run
       crashed with OSError (<your-agent-id> invalid filename) — the
       TEMPLATE skip fixed it (red → green)
GREEN: python -m unittest discover -s tools/agent-wrappers/tests
       Ran 14 tests in ~0.03s — OK
```

### Generation + parity

```
python tools/agent-wrappers/generate.py distribution-kit/devflow/agents
OK: 20 wrappers for 5 roles x 4 platforms (coordinator skipped)

python tools/agent-wrappers/parity.py distribution-kit/devflow/agents distribution-kit
PASS: N×4 parity holds — 20 wrappers, 0 drift
```

### Invariants

```
Kit + tools only: only tools/ + distribution-kit wrapper sets changed  PASS
No junk files: no angle-bracket filenames in the agent folders          PASS
```

### Gates

Tooling Bolt: unit/integration → **pass** (14); SAST/SBOM, perf, IP, PII,
dep-confusion → `n/a`; prompt-injection → `pass`; secret-leak → `pass`;
hallucination-lint → `pass`; behavioral-reproducibility → `pass` (parity
reproduces); bolt-manifest-validation → `pass`.

## 10. Manual interventions

None — the agent produced everything.

## 11. Evidence links

- **Diff / PR:** none (working tree, uncommitted)
- **Commit:** baseline `45d553f`
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-023.BOLT-002-wrapper-generator-and-parity.json`

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~10min |
| V-Bounce number | 2 |
| Tests created | 14 (was 12; +coordinator-not-generated, +template-skipped) |
| AI-generated code | 100% |
| First-pass approval | pending (this MEM) |

## 13. Pending items and stubs

- [ ] BOLT-003 V-Bounce 2 (the deployed set regeneration + the four main
      files' orchestrator touch)
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
| **review_ready_at** | `2026-08-23T17:16:00-03:00` |
| **review.started_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **review.decided_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **Review evidence** | diff of generate.py/parity.py/DESIGN/tests; 14/14 tests; generation (20); parity PASS; MEM, manifest |
| **Comments** | |
| **Findings** | |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | evidence inspected per the review-evidence column |
