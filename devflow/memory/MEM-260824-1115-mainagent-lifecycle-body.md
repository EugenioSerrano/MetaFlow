---
id: "MEM-260824-1115"
title: "The lifecycle body deployed in the four MainAgents — byte-identical, with the shared-body AC-9 cleanup (US-025.BOLT-001, V-Bounce 1)"
date: "2026-08-24"
author: "eugenio.serrano"
llm: "claude-fable-5"
bolt: "US-025.BOLT-001"
spec: "devflow/spec/SPEC-260824-1101-mainagent-lifecycle-body.md"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "2b7ffd7"
applied_adrs:
  - "devflow/adrs/ADR-013-agent-lifecycle-governance.md"
  - "devflow/adrs/ADR-014-actors-roster-is-the-enablement.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "devflow/metrics/bolts/US-025.BOLT-001-mainagent-lifecycle-body.json"
diff_ref: ""
review_ready_at: "2026-08-24T11:15:43-03:00"
review: # AITL-MEM-Approval — decision dictated in conversation ("aprobado! sigamos con el que sigue") and transcribed by the agent (§3.0)
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-24T11:18:48-03:00"
  decided_at: "2026-08-24T11:18:48-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved as Dev-validator: the 4-file diff inspected against the approved SPEC payload — the section byte-identical (single hash cd24754c320d), the Coordinator paragraph cleaned per the exact Phase B strings, G-count 39x4, every cross-reference resolving, the scoped remainder exactly the known+routed set (with the Codex preamble's DISC-002 as the sweep's new catch, added to BOLT-002's list). The lifecycle is now contract in the four system prompts. V-Bounce 1 approved — BOLT-001 Development Completed; acceptance batched with the US-025 closure."
---

# MEM-260824-1115 — The lifecycle body in the four MainAgents (US-025.BOLT-001, V-Bounce 1)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | US-025.BOLT-001 (mainagent-lifecycle-body) |
| **SPEC**        | [SPEC-260824-1101](../spec/SPEC-260824-1101-mainagent-lifecycle-body.md) rev 1 |
| **V-Bounce**    | 1 |
| **ADRs**        | ADR-013 (the governance the section expresses), ADR-014 (the enablement it defers to), ADR-004 (kit-only) |

---

## 1. Executive summary

This V-Bounce deployed the **agent-lifecycle capability as contract** into
the four MainAgents. The section approved verbatim in the SPEC's Phase A —
the identity clause (MainAgent ≡ AvengaDevFlow ≡ Coordinator), the three
flows (**install** from `squad/` per the shipped mapping with the reload
notice; **create** with the role-generic and `content_language` rules at
the point of action, the roster **executor-only draft**, and the
authority-is-the-human's + commit-is-the-record reminders; **delete** with
the N:1 roster check) and the four governance rules (living data · human
authority · installing ≠ enabling · agent-system-only bounds) — was
inserted **immediately before the `## Guardrails (MUST enforce)` heading**
(the reviewer-adopted placement) in the four files, via a single scripted
edit that guarantees byte identity. The **shared-body cleanup** (US-025
AC-9) landed in the same pass: the Coordinator paragraph's `ADR-008`
mention became "separation of duties: the router never approves its own
routing" and its trailing `US-023 AC-6` became "(the spawn topology)" —
per-file uniqueness asserted before editing, so the per-platform
preambles' own references were untouched (they are BOLT-002's, see §13).
Verification is GREEN across every gate: the section extracts to a
**single md5 across the four** (`cd24754c320d…`), the modified Coordinator
paragraph likewise, **G-count 39 × 4** (no guardrail-table collateral),
every payload cross-reference resolves on disk, no BOM, and the scoped
self-containment sweep ends exactly on the **known, routed remainder**:
the per-platform preamble references (`ADR-007`, `US-023` in all four; +
`DISC-002` in the Codex preamble — a remainder item DISCOVERED by this
sweep and added to BOLT-002's list, alongside the already-noted stale
pre-built-wrapper mentions) and the naming table's fictional framework
examples (`TC-027.BOLT-001-…`, same class as `US-012.BOLT-003-…`, which
stay by design).

## 2. Implemented phases

### Phase A — The lifecycle section (the payload)

Inserted byte-identical in the four files before the Guardrails heading.
Content exactly as approved in the SPEC (including the two reviewer
refinements adopted pre-approval: the precise living-data anchor "§5.12
and the roster's living-data rule", and the placement).

### Phase B — The shared-body cleanup (AC-9)

The two old→new replacements applied exactly as specified; the script
asserted each old string appears **once per file** before touching
anything (the stop condition protecting the preambles held).

### Phase C — Byte-sync + verification (GREEN)

Single scripted edit over the four files; section hash SINGLE ×4;
paragraph hash SINGLE ×4; G-count 39 ×4; cross-references resolve
(`squad/`, `TEMPLATE-new-role/`, `examples/`, `VERIFICATION.md`,
`roster.yaml`, `TEMPLATE-ACTOR.yaml`, `agents/INDEX.md`); scoped
self-containment = the known remainder only; no BOM.

## 3. Files created

| File | Purpose |
|------|---------|
| — | none (one insertion + one paragraph edit per MainAgent) |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `distribution-kit/CLAUDE.md` | + the lifecycle section (before ## Guardrails); the Coordinator paragraph cleaned (AC-9) |
| `distribution-kit/.agents/skills/avenga-devflow/SKILL.md` | idem — byte-identical |
| `distribution-kit/.github/agents/AvengaDevFlow.agent.md` | idem — byte-identical |
| `distribution-kit/.opencode/agents/AvengaDevFlow.md` | idem — byte-identical |

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
| One Python script edits the four files | Byte identity by construction, not by care — the hash gates then prove it |
| Uniqueness asserted per old-string before editing | The `US-023 AC-6` string also lives in the per-platform preambles; the assertion is what makes "only the shared paragraph" verifiable, not hoped |
| The Codex preamble's `DISC-002` added to BOLT-002's remainder list | Found by the sweep; it sits in the per-platform surface (the same paragraph that still mentions the stale `.codex/agents/*.toml` role agents) — same owner |
| `TC-027` classified framework (stays) | The naming table's fictional example, the same class as `US-012.BOLT-003-…` — documenting the framework, not referencing the maintainer partition |

## 8. Deviations and assumptions

No deviations from SPEC-260824-1101 rev 1 (the reviewer's four
observations were folded into the SPEC before approval and executed as
written). No assumptions — every anchor string was verified on disk before
the edit.

## 9. Verification evidence

### The gates (RED → GREEN)

```
STOP CONDITIONS: paragraph x1 + anchor x1 + section absent — clear in the four
AC-1 section hash x4:        SINGLE (cd24754c320d…)
Coordinator paragraph x4:    SINGLE
G-count x4:                  [39, 39, 39, 39]
Cross-references:            all resolve
BOM:                         none
```

### Scoped self-containment (AC-3)

```
Remainder after the cleanup (all known + routed):
  ADR-007, US-023      → the per-platform preambles (all four) — BOLT-002
  DISC-002             → the Codex preamble (SKILL.md) — added to BOLT-002's list
  TC-027.BOLT-001-…    → naming-table fictional example — framework, stays
  US-000, US-NNN, …    → the kit's own container US + placeholders — framework, stay
Shared body: 0 maintenance-partition references remain.
```

### Gates

Documentation Bolt: unit/integration/perf `n/a` (per the approved SPEC
§9); prompt-injection `pass` (the inserted text instructs the agent only —
no third-party-triggerable directives); secret-leak `pass`;
hallucination-lint `pass` (every referenced path resolves);
behavioral-reproducibility `pass` (the script + checks re-run
identically); bolt-manifest-validation `pass` (v_bounces[1] appended,
schema PASS).

## 10. Manual interventions

None — the agent produced everything.

## 11. Evidence links

- **Diff / PR:** working tree over baseline `2b7ffd7` (uncommitted —
  presented for review)
- **Commit:** baseline `2b7ffd7`
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-025.BOLT-001-mainagent-lifecycle-body.json`

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~10min |
| V-Bounce number | 1 |
| Tests created | 0 (documentation; scripted evidence per SPEC §8 — the script is reproducible) |
| AI-generated code | 100% |
| First-pass approval | pending (this MEM) |

## 13. Pending items and stubs

- [ ] **BOLT-002** (per-platform): the preambles' references (`ADR-007`,
      `US-023` ×4; **`DISC-002`** in the Codex preamble — new), the stale
      pre-built-wrapper lists (`Agent(architect-agent, …)` in Claude's;
      the `.codex/agents/*.toml` mention in Codex's), the projection
      permission spec, `inherit` handling, the OpenCode platform notes
      (REV-005 F-09/F-13/F-14).
- [ ] **BOLT-005**: the kit GUARDRAILS G07 scoping (closes REV-005 F-02's
      gray zone at the guardrail's letter — the section's living-data
      clause already stands on §5.12 + the roster rule).
- [ ] BOLT-003 (delete-safe depth) · BOLT-004 (the pilot).
- [ ] AITL-BOLT-DONE-Approval for this Bolt after the MEM approval.

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
| **review_ready_at** | `2026-08-24T11:15:43-03:00` |
| **review.started_at** | `2026-08-24T11:18:48-03:00` |
| **review.decided_at** | `2026-08-24T11:18:48-03:00` |
| **Review evidence** | the 4-file diff (the section + the cleaned paragraph); the hash/G-count/sweep/cross-ref evidence; MEM, manifest |
| **Comments** | |
| **Findings** | |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | evidence inspected per the review-evidence column |
