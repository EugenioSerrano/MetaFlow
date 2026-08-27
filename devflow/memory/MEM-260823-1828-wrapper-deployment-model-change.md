---
id: "MEM-260823-1828"
title: "Deployment model change — the kit ships no pre-built role wrappers; the Coordinator installs them in the adopting project (US-023.BOLT-003, V-Bounce 4)"
date: "2026-08-23"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
bolt: "US-023.BOLT-003"
spec: "devflow/spec/SPEC-260823-1602-wrapper-deployment.md"
spec_revision: 1
v_bounce: 4
execution_outcome: "ready_for_review"
baseline: "7e3eb5e"
applied_adrs:
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "devflow/metrics/bolts/US-023.BOLT-003-wrapper-deployment.json"
diff_ref: ""
review_ready_at: "2026-08-23T18:28:00-03:00"
review: # AITL-MEM-Approval — decision dictated in conversation ("Aprobado, a darle GAS", over the reviewed queue) and transcribed by the agent (§3.0)
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-24T00:40:35-03:00" # ISO 8601 with seconds + offset
  decided_at: "2026-08-24T00:40:35-03:00" # ISO 8601 with seconds + offset
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved as Dev-validator: the deployment-model change inspected against the working tree — the 20 role wrappers removed from the kit's dotfolders, the 4 MainAgents intact at their native entry points, the kit docs aligned (VERIFICATION.md, agents/README, roles/README, INDEX), maintainer-side parity PASS (20 wrappers, 0 drift), self-containment 0 hits, manifest v_bounces[4] appended and valid. The governance this V-Bounce anticipated is now in place: ADR-013 §3.9 (accepted 2026-08-24) fixes the ship model and US-023 revision 3 (re-approved) carries the G15 wording change this MEM flagged as follow-up. V-Bounce 4 approved — BOLT-003 Development Completed."
---

# MEM-260823-1828 — Deployment model change (US-023.BOLT-003, V-Bounce 4)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | US-023.BOLT-003 (wrapper-deployment) |
| **SPEC**        | [SPEC-260823-1602](../spec/SPEC-260823-1602-wrapper-deployment.md) rev 1 |
| **V-Bounce**    | 4 (maintainer decision — the deployment model changes; the prior V-Bounces remain history) |
| **ADRs**        | ADR-004 (kit-only) |

---

## 1. Executive summary

The maintainer directed the deployment-model change aligned with
ADR-013/US-025 (the agent lifecycle): **the kit ships no pre-built role
wrappers** — the platform dotfolders carry **only the 4 main agents**
(every one of them named AvengaDevFlow, one per tool). The **20 role
wrappers** previously committed to the kit's dotfolders were **removed**
(they were "examples" that must not ship — the Coordinator installs them
in the adopting project at adoption time, a governed operational act per
ADR-013). The kit keeps everything the Coordinator needs to install: the
canonical definitions (`devflow/agents/roles/*`), the templates, the
INDEX and the **field-level mapping** (VERIFICATION.md, shipped in V-Bounce
3). The kit docs were aligned to the new model: VERIFICATION.md's
intro (no more "ships pre-built / no build step" — now "the Coordinator
installs and refreshes its platform's wrappers per this mapping"),
`agents/README.md`, `agents/roles/README.md` (step 4: "the Coordinator
installs it" instead of "run the generator at tools/") and `agents/INDEX.md`
(the wrappers are projected by the Coordinator, not shipped). Verification:
the **4 main agents intact** (CLAUDE.md, SKILL.md, AvengaDevFlow.agent.md,
AvengaDevFlow.md); the dotfolders state exactly the new model (`.claude/agents/`
empty — the Coordinator creates it; `.codex/agents/` absent — same;
`.opencode/agents/` and `.github/agents/` hold only the main agent); the
maintainer-side generator + parity (tools/) still pass (20 wrappers
generated, 0 drift — its role is now the maintainer's generation
validation + the adopting project's install verification); the
self-containment check passes (0 hits). **Follow-up (governed):** US-023
AC-9's "wrappers generated and committed to the kit" wording is
materially superseded by this model → a G15 re-revision of US-023 is
folded into the ADR-013/US-025 batch (with Opus). The prior V-Bounce MEMs
(1618/1717/1814) remain as history — nothing in their content is
corrected; the model evolved.

## 2. Implemented phases

### Phase A — The dotfolders reduced to the 4 main agents

The 20 role wrappers removed from the kit's platform dotfolders:
`.claude/agents/*.md` (5, folder left empty — the Coordinator creates it
at install), `.opencode/agents/*.md` (5, only AvengaDevFlow.md remains),
`.github/agents/*.agent.md` (5, only AvengaDevFlow.agent.md remains),
`.codex/agents/*.toml` (5, folder removed — Codex's main agent is
`.agents/skills/.../SKILL.md`). The 4 main agents verified intact.

### Phase B — The kit docs aligned to the new model

VERIFICATION.md intro rewritten (the Coordinator installs/refreshes its
platform's wrappers per the shipped mapping; no pre-built wrappers; fresh
session to reload); agents/README.md (the wrappers are projected by the
Coordinator, not hand-written; the kit ships no pre-built role wrappers);
roles/README.md step 4 (the Coordinator installs the new role); INDEX.md
(the wrappers are projected by the Coordinator into the project's
platform folders).

### Phase C — Verification (GREEN)

4 main agents OK; dotfolders state per the new model; parity PASS
(maintainer-side, 20 wrappers, 0 drift); self-containment grep (0 hits);
no BOM.

## 3. Files created

| File | Purpose |
|------|---------|
| — | none (removal + doc alignment) |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `distribution-kit/devflow/agents/VERIFICATION.md` | Intro rewritten — the Coordinator installs/refreshes its platform's wrappers per the mapping; no pre-built wrappers ship |
| `distribution-kit/devflow/agents/README.md` | The wrappers are projected by the Coordinator into the four platform shapes; the kit ships no pre-built role wrappers |
| `distribution-kit/devflow/agents/roles/README.md` | Step 4: "the Coordinator installs it" (per the mapping) instead of "run the generator at tools/" |
| `distribution-kit/devflow/agents/INDEX.md` | The wrappers are projected by the Coordinator into the project's platform folders; no pre-built role wrappers |

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
| — | — | — |

## 6. Files deleted

| File | Reason |
|------|--------|
| `distribution-kit/.claude/agents/{architect,developer,fa,qa,reviewer}-agent.md` (×5) | The deployment model change — no pre-built role wrappers ship; the Coordinator installs them in the adopting project (ADR-013/US-025) |
| `distribution-kit/.opencode/agents/{...}-agent.md` (×5) | Same |
| `distribution-kit/.github/agents/{...}-agent.agent.md` (×5) | Same |
| `distribution-kit/.codex/agents/{...}-agent.toml` (×5) + the folder | Same |

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| The kit ships only the 4 main agents in the dotfolders | The maintainer's direction — the role wrappers are installed by the Coordinator at adoption, not delivered pre-built |
| The kit keeps the canonical definitions + templates + the mapping | The Coordinator reads them to install (US-025 AC-8's docs-reading primary) |
| The generator + parity stay in tools/ (maintainer-side) | Their role evolves: maintainer generation validation + the adopting project's install verification |
| US-023 AC-9's "committed to the kit" wording is superseded | Material change (G15) — folded into the ADR-013/US-025 batch for the US re-revision |

## 8. Deviations and assumptions

The deployment model changed per the maintainer's direction — a deliberate
evolution, not a correction of prior V-Bounce content. Assumption: the
Coordinator's install capability lands with US-025 (ADR-013 as its base);
until then the mapping + the definitions are the kit's install reference.

## 9. Verification evidence

### State (RED → GREEN)

```
RED:   20 role wrappers committed in the kit's dotfolders (from 7e3eb5e)
GREEN: dotfolders per the new model:
       .claude/agents/    → empty (the Coordinator creates it)
       .opencode/agents/  → AvengaDevFlow.md only
       .github/agents/    → AvengaDevFlow.agent.md only
       .codex/agents/     → absent (Codex's main is SKILL.md)
       4 main agents: CLAUDE.md · SKILL.md · AvengaDevFlow.agent.md ·
       AvengaDevFlow.md — all OK
```

### Invariants

```
Parity (maintainer-side): PASS — 20 wrappers, 0 drift
Self-containment grep over agents/ + actors/: 0 hits
Encoding: no BOM
```

### Gates

Documentation Bolt: runtime gates `n/a`; prompt-injection/secret-leak
`pass`; hallucination-lint `pass`; behavioral-reproducibility `pass`;
bolt-manifest-validation `pass` (v_bounces[4] appended, JSON valid).

## 10. Manual interventions

None — the agent produced everything (the removal was directed by the
maintainer and recorded here).

## 11. Evidence links

- **Diff / PR:** none (working tree, uncommitted; the prior commit 7e3eb5e
  included the removed wrappers)
- **Commit:** baseline `7e3eb5e`
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-023.BOLT-003-wrapper-deployment.json`

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~10min |
| V-Bounce number | 4 |
| Tests created | 0 (documentation/model change; the tool suite unchanged) |
| AI-generated code | 100% |
| First-pass approval | pending (this MEM) |

## 13. Pending items and stubs

- [ ] US-023 G15 re-revision (AC-9's "committed to the kit" → the install
      model) — folded into the ADR-013/US-025 batch
- [ ] US-025 implements the Coordinator's install capability (ADR-013
      base; the mapping as the reference)
- [ ] Batch approval of this MEM (the prior approvals stand; the model
      evolved)

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
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-23T18:28:00-03:00` |
| **review.started_at** | `2026-08-24T00:40:35-03:00` |
| **review.decided_at** | `2026-08-24T00:40:35-03:00` |
| **Review evidence** | the removals + the doc alignments; the 4 main agents check; the dotfolders state; parity; the self-containment grep; MEM, manifest |
| **Comments** | |
| **Findings** | |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | evidence inspected per the review-evidence column |
