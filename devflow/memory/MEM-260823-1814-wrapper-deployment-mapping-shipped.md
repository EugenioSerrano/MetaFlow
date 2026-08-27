---
id: "MEM-260823-1814"
title: "The shipped canonical → wrapper mapping — VERIFICATION.md carries the field-level mapping per platform that the MainAgent lifecycle reads (US-023.BOLT-003, V-Bounce 3)"
date: "2026-08-23"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
bolt: "US-023.BOLT-003"
spec: "devflow/spec/SPEC-260823-1602-wrapper-deployment.md"
spec_revision: 1
v_bounce: 3
execution_outcome: "ready_for_review"
baseline: "45d553f"
applied_adrs:
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "devflow/metrics/bolts/US-023.BOLT-003-wrapper-deployment.json"
diff_ref: ""
review_ready_at: "2026-08-23T18:14:00-03:00"
review: # AITL-MEM-Approval — recorded by the human reviewer (§3.0); decision dictated in conversation ("aprobado!") and transcribed by the agent
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-23T18:15:00-03:00"
  decided_at: "2026-08-23T18:15:21-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved as Dev-validator: the shipped canonical → wrapper mapping inspected — the field-level table per platform present, self-contained (0 hits), kit-only. V-Bounce 3 approved — the US-025 AC-8 prerequisite is closed."
---

# MEM-260823-1814 — The shipped canonical → wrapper mapping (US-023.BOLT-003, V-Bounce 3)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | US-023.BOLT-003 (wrapper-deployment) |
| **SPEC**        | [SPEC-260823-1602](../spec/SPEC-260823-1602-wrapper-deployment.md) rev 1 |
| **V-Bounce**    | 3 (additive refinement — the field-level mapping shipped in the kit) |
| **ADRs**        | ADR-004 (kit-only) |

---

## 1. Executive summary

The consolidated review flagged the one remaining gap in the US-023
deliverable: the precise **canonical `agent.yaml` → wrapper mapping per
platform** lived only in `tools/agent-wrappers/DESIGN.md` — maintainer
tooling, **not shipped** — while the future MainAgent lifecycle (US-025
AC-8, docs-reading primary) needs that mapping **in the kit**. This
V-Bounce ships it: `distribution-kit/devflow/agents/VERIFICATION.md` now
carries a **"Canonical → wrapper mapping (field-level)"** section — the
per-platform field table (`id`, `description`, `model`,
`capabilities.tools`, `capabilities.mcp_servers`, `approves`/`modes`,
the charter body) projected into Claude Code, OpenCode, GitHub Copilot
and OpenAI Codex formats, plus the spawn-topology note (only the
Coordinator — the platform agent itself — may spawn; the role wrappers
carry no spawn capability). The section is fully **self-contained** (0
maintenance-partition references — verified with the grep check), no
BOM, kit-only. With this, the kit carries everything a MainAgent needs
to install/refresh its platform's wrappers by reading the docs — the
prerequisite of US-025 is closed. Additive refinement: the prior V-Bounce
2 (MEM-1717, approved) remains valid; nothing in its deliverable was
corrected.

## 2. Implemented phases

### Phase A — The mapping shipped

Added the "Canonical → wrapper mapping (field-level)" section to
`VERIFICATION.md` (after the intro, before the per-platform usage
sections): the field table (canonical → Claude/OpenCode/Copilot/Codex)
+ the spawn-topology note. The charter body's destination per platform
(body after `---` / the Codex `system` block) is included, so a
MainAgent can reconstruct a wrapper from the canonical definition alone.

### Phase B — Verification (GREEN)

Section present (line 8); all six mapping rows present; the
self-containment grep over `agents/` → 0 hits; no BOM; kit-only.

## 3. Files created

| File | Purpose |
|------|---------|
| — | none (edit within VERIFICATION.md) |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `distribution-kit/devflow/agents/VERIFICATION.md` | New "Canonical → wrapper mapping (field-level)" section — the per-platform field table + the spawn-topology note (the shipped reference the MainAgent lifecycle reads) |

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
| The mapping ships in VERIFICATION.md (not a new doc) | It is the platform-contract reference the file already exists to carry; keeps the family docs consolidated |
| Field-level (not just usage) detail | US-025 AC-8's docs-reading primary requires the exact canonical → frontmatter projection |
| Self-contained wording | The kit never references the maintenance partition; the mapping is the kit's own reference |
| The prior V-Bounce 2 MEM stays approved | This is additive — nothing in the deployed set or the notes was corrected |

## 8. Deviations and assumptions

No deviations from SPEC-260823-1602 rev 1 (the refinement is additive).
Assumption: US-025's MainAgent lifecycle consumes this mapping as its
primary projection reference; the compiled generator (US-017) remains an
optional automation path.

## 9. Verification evidence

### Presence (RED → GREEN)

```
RED:   VERIFICATION.md has no field-level mapping (only the usage notes)
GREEN: "Canonical → wrapper mapping (field-level)" PRESENT (line 8)
       rows: id · description · model · capabilities.tools ·
       capabilities.mcp_servers · charter body — all PRESENTE
```

### Self-containment

```
grep -E "US-[0-9]{3}|ADR-[0-9]{3}|DISC-[0-9]{3}|BOLT-[0-9]|SPEC-26|MEM-26|
REV-[0-9]{3}|TC-[0-9]{3}" over distribution-kit/devflow/agents/* →
0 hits — SELF-CONTAINED PASS
```

### Invariants

```
Kit-only: only distribution-kit/ changes   PASS
Encoding: 0 files with BOM                  PASS
Deployed wrappers: 20 (unchanged) · parity PASS
```

### Gates

Documentation Bolt: runtime gates `n/a`; prompt-injection/secret-leak
`pass`; hallucination-lint `pass`; behavioral-reproducibility `pass`;
bolt-manifest-validation `pass` (v_bounces[3] appended, JSON valid).

## 10. Manual interventions

None — the agent produced everything.

## 11. Evidence links

- **Diff / PR:** none (working tree, uncommitted)
- **Commit:** baseline `45d553f`
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-023.BOLT-003-wrapper-deployment.json`

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~8min |
| V-Bounce number | 3 |
| Tests created | 0 (documentation — presence/self-containment evidence) |
| AI-generated code | 100% |
| First-pass approval | pending (this MEM) |

## 13. Pending items and stubs

- [ ] Batch approval of this MEM (additive; the prior approvals stand)
- [ ] US-025 (MainAgent lifecycle) consumes this mapping — with ADR-013
      as its base

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
| **review_ready_at** | `2026-08-23T18:14:00-03:00` |
| **review.started_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **review.decided_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **Review evidence** | diff of the mapping section; presence checks; the self-containment grep (0 hits); kit-only; MEM, manifest |
| **Comments** | |
| **Findings** | |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | evidence inspected per the review-evidence column |
