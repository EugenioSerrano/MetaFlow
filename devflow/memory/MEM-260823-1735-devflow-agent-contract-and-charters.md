---
id: "MEM-260823-1735"
title: "Kit self-containment — the agents/ and actors/ families no longer reference the maintenance partition (US-023.BOLT-001, V-Bounce 4)"
date: "2026-08-23"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
bolt: "US-023.BOLT-001"
spec: "devflow/spec/SPEC-260823-1600-devflow-agent-contract-and-charters.md"
spec_revision: 1
v_bounce: 4
execution_outcome: "ready_for_review"
baseline: "45d553f"
applied_adrs:
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "devflow/metrics/bolts/US-023.BOLT-001-devflow-agent-contract-and-charters.json"
diff_ref: ""
review_ready_at: "2026-08-23T17:35:00-03:00"
review: # AITL-MEM-Approval — recorded by the human reviewer (§3.0); decision dictated in conversation ("aprobado!") and transcribed by the agent
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-23T17:36:00-03:00"
  decided_at: "2026-08-23T17:36:54-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved as Dev-validator: the self-containment cleanup inspected — 0 references to the maintenance partition across agents/ and actors/ (re-scanned); VERIFICATION.md explains the per-platform install/use; tests and parity hold. V-Bounce 4 approved — BOLT-001 final."
---

# MEM-260823-1735 — Kit self-containment cleanup (US-023.BOLT-001, V-Bounce 4)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | US-023.BOLT-001 (devflow-agent-contract-and-charters) |
| **SPEC**        | [SPEC-260823-1600](../spec/SPEC-260823-1600-devflow-agent-contract-and-charters.md) rev 1 |
| **V-Bounce**    | 4 (maintainer refinement — kit self-containment, post-approval) |
| **ADRs**        | ADR-004 (kit-only partition) |

---

## 1. Executive summary

The maintainer flagged a real governance defect: the kit (`distribution-kit/`)
is the product adopters copy wholesale — it must be **self-contained** and
must **never reference elements of the maintenance partition** (US-NNN,
Bolts, SPECs, MEMs, ADRs, DISCs, REVs, AC numbers), because those do not
deploy. The `agents/` family (README, INDEX, roles/README, the five role
templates, the TEMPLATE-new-role, VERIFICATION.md) and the `actors/` README
carried such references (e.g., "US-023 AC-6/7/8", "US-024", "ADR-007
§3.4", "ADR-008 §3.6", "DISC-002 §4.2/§5.5/rec #6", "(US-023.BOLT-003)",
"the pilot US"). All of them were **rewritten to self-contained
statements**: the kit now states the rules themselves (the approver
ceiling, the spawn topology, the MCP allowlist, the governance limit,
§3.0.1 anchors — which ARE kit-internal) without citing any
non-deployed artifact. `VERIFICATION.md` was also rewritten per the
maintainer's direction: it now explains **how each platform installs and
uses the agents in its folders** (the wrapper locations, session-start
loading, the trust requirement for Claude Code, the spawn topology, the
known gaps, the parity discipline). The verification is clean: **0
references** to the maintenance partition across `agents/` and `actors/`
(re-scanned), the generator tests pass (14/14), the deployed wrapper set
is unchanged (20) and the parity holds (0 drift). This V-Bounce is
recorded under BOLT-001 (the agents family docs are its deliverable); the
VERIFICATION.md (BOLT-003) and the actors/README (US-022) alignments are
recorded here as cross-Bolt refinements of the same cleanup, consistent
with the precedent of the model-placeholder fix.

## 2. Implemented phases

### Phase A — The inventory

Scanned `distribution-kit/devflow/agents/` and `distribution-kit/devflow/actors/`
for maintenance-partition references (US-NNN, BOLT-NNN, SPEC-, MEM-, ADR-,
DISC-, REV-, TC-, "AC-\d") — ~25 hits inventoried.

### Phase B — The cleanup (self-contained rewording)

- `agents/README.md`: "filled by US-024" → "filled by the roster family";
  "(US-022 producer+approver reframe)" → "(the producer + approver
  concept, §3.0.1)"; "(ADR-007 §3.4 …)" → ("the evolution of today's
  platform agent"); "(DISC-002 §5.5)"/"(ADR-007)" → removed/rewritten.
- `agents/INDEX.md`: "(ADR-007 §3.4; US-023 AC-6)" and "(DISC-002 §5.5)"
  → removed/rewritten.
- `agents/roles/README.md`: "(ADR-007)", "(US-023 AC-7/AC-8)", "(ADR-008
  §3.6)", "(US-024)", "(ADR-007 §3.3)", "(ADR-008 safe-default)" →
  self-contained equivalents ("the identity model", "the security rules",
  "the roster family", "the safe-default").
- The five role `agent.yaml` files: "# APPROVER CEILING (US-023 AC-7)"
  → "# APPROVER CEILING (approver mode)"; developer's note de-cited;
  `developer/prompt.md`: "(ADR-004)" → "(kit-only)".
- `TEMPLATE-new-role/`: the bounds block de-cited (the identity model,
  the approver ceiling, the MCP allowlist rule); prompt.md §3.0.1 anchor.
- `VERIFICATION.md`: fully rewritten — self-contained + the per-platform
  install/usage explanation (folder, session-start loading, trust, spawn
  topology, known gaps, parity).
- `actors/README.md`: "Lands with US-024" ×2 → "Lands with the roster
  family".

### Phase C — Verification

Re-scan: **0 references** across the two families; the generator tests
pass; parity PASS over the unchanged 20-wrapper set.

## 3. Files created

| File | Purpose |
|------|---------|
| — | none (edits within existing files) |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `distribution-kit/devflow/agents/README.md` | Self-contained rewording (no US/ADR/DISC citations) |
| `distribution-kit/devflow/agents/INDEX.md` | Same |
| `distribution-kit/devflow/agents/roles/README.md` | Same (incl. the governance-limit table de-cited) |
| `distribution-kit/devflow/agents/roles/<role>/agent.yaml` (×5) | APPROVER CEILING comments de-cited |
| `distribution-kit/devflow/agents/roles/developer/prompt.md` | "(ADR-004)" → "(kit-only)" |
| `distribution-kit/devflow/agents/roles/TEMPLATE-new-role/{agent.yaml,prompt.md}` | Bounds de-cited; §3.0.1 anchor |
| `distribution-kit/devflow/agents/VERIFICATION.md` | **Rewritten** — self-contained + the per-platform install/usage explanation (BOLT-003 cross-refinement) |
| `distribution-kit/devflow/actors/README.md` | "Lands with US-024" → "Lands with the roster family" (US-022 cross-refinement) |

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
| The kit never cites the maintenance partition | It is the deployable product — adopter copies would carry dangling references to artifacts they do not have |
| Kit-internal anchors stay (§3.0.1, §sections, G-rules, the AITL-enable ADR) | They resolve inside the deployed kit |
| VERIFICATION.md explains the per-platform install/use | The maintainer's direction: each platform's folder, loading, trust, topology and gaps — useful for adopters |
| The cleanup is recorded under BOLT-001's V-Bounce 4 | The agents family docs are its deliverable; VERIFICATION.md (BOLT-003) and actors/README (US-022) are cross-refinements of the same cleanup (precedent: the model-placeholder fix) |

## 8. Deviations and assumptions

No deviations. Assumption: no behavior changed — the rewordings are
wording-level (the rules are identical, only the citations are gone).

## 9. Verification evidence

### Re-scan (RED → GREEN)

```
RED:   ~25 maintenance-partition references across agents/ + actors/
GREEN: 0 references (re-scanned with the same pattern set)      PASS
```

### Invariants

```
Generator tests: 14/14 PASS
Deployed wrappers: 20 (unchanged)
Parity: PASS — 20 wrappers, 0 drift
Encoding: no BOM in the edited files (tool-written)
```

### Gates

Documentation Bolt: runtime gates `n/a`; prompt-injection/secret-leak
`pass`; hallucination-lint `pass`; behavioral-reproducibility `pass`;
bolt-manifest-validation `pass` (v_bounces[4] appended, JSON valid).

## 10. Manual interventions

None — the agent produced everything.

## 11. Evidence links

- **Diff / PR:** none (working tree, uncommitted)
- **Commit:** baseline `45d553f`
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-023.BOLT-001-devflow-agent-contract-and-charters.json`

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~10min |
| V-Bounce number | 4 |
| Tests created | 0 (wording cleanup; the tool suite unchanged — 14 pass) |
| AI-generated code | 100% |
| First-pass approval | pending (this MEM) |

## 13. Pending items and stubs

- [ ] Batch approval of this MEM (the earlier approvals stand; this V-Bounce
      documents the self-containment cleanup)
- [ ] The same self-containment discipline applies to every future kit
      family (actors/ roster content, US-024 deliverables, the pilot)

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
| **review_ready_at** | `2026-08-23T17:35:00-03:00` |
| **review.started_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **review.decided_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **Review evidence** | diff of the rewrites; the 0-reference re-scan; tests/parity; MEM, manifest |
| **Comments** | |
| **Findings** | |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | evidence inspected per the review-evidence column |
