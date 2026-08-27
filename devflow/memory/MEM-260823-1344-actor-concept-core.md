---
id: "MEM-260823-1344"
title: "Actor concept — the normative §3.0.1 The Actor section, canonical mermaid and the §5.1 actors/ tree entry (US-022.BOLT-001)"
date: "2026-08-23"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
bolt: "US-022.BOLT-001"
spec: "devflow/spec/SPEC-260823-1335-actor-concept-core.md"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "45d553f"
applied_adrs:
  - "devflow/adrs/ADR-007-devflow-agent-identity-model.md"
  - "devflow/adrs/ADR-008-aitl-approval-precept.md"
  - "devflow/adrs/ADR-010-actor-grammar-and-pure-v5-vocabulary.md"
manifest: "devflow/metrics/bolts/US-022.BOLT-001-actor-concept-core.json"
diff_ref: ""
review_ready_at: "2026-08-23T13:44:00-03:00"
review: # AITL-MEM-Approval — recorded by the human reviewer (§3.0); decision dictated in conversation and transcribed by the agent
  decision: "changes_requested"
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-23T15:28:00-03:00"
  decided_at: "2026-08-23T15:29:03-03:00"
  findings:
    - "Structural: the §3.0.1 heading was placed right after the precept paragraph, nesting the entire checkpoint charter (role routing, checkpoint tables, per-checkpoint prose) under 'The Actor' in the document outline. Fixed in V-Bounce 2 (MEM-260823-1352) by relocating §3.0.1 to the end of §3.0."
  acknowledged_without_comment: false
  acknowledgment_reason: "changes_requested — the V-Bounce 1 output had the nesting defect; superseded by V-Bounce 2 (MEM-260823-1352). Recorded to complete the review contract (G17/§3.3); the MEM narrative stays immutable."
---

# MEM-260823-1344 — Actor concept core (US-022.BOLT-001, V-Bounce 1)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | US-022.BOLT-001 (actor-concept-core) |
| **SPEC**        | [SPEC-260823-1335](../spec/SPEC-260823-1335-actor-concept-core.md) rev 1 |
| **V-Bounce**    | 1 |
| **ADRs**        | ADR-007 (identity), ADR-008 (precept), ADR-010 (grammar) |

---

## 1. Executive summary

This V-Bounce delivered the normative Actor definition into the kit's core
methodology: the new subsection `### 3.0.1 The Actor` inside the
Actor-in-the-Loop Charter (§3.0) states, once and canonically, what an
Actor is (the unit of identity in the AITL loop — a human by default, a
virtual DevFlow Agent only by explicit valid configuration), the
executor/approver/neither checkpoint relationship (the umbrella for the
Coordinator-never-signs rule), the actor grammar (`human:<user>` /
`agent:<id>` with the model as an attribute), the two independence layers
(actor floor, model hardening at high risk, human ceiling at
critical/regulatory), the open role taxonomy and the safe-default
invariant — plus the canonical Actor flow diagram (mermaid) that the
`actors/` README (BOLT-002) will reference, and the `actors/` entry in the
§5.1 canonical folder tree. The placement was chosen deliberately as
`### 3.0.1` (a new subsection of §3.0, which had no children) so that **no
existing section number moves**: the before/after heading-token check
proves the only addition is the new heading itself, so every §N reference
kit-wide keeps resolving (the review finding that motivated AC-9). All
verification checks are GREEN: section present, mermaid present, tree entry
present, heading set preserved (77 → 78 tokens, exactly +1), GUARDRAILS
count unchanged at 39, and `git status` shows only the kit's methodology
file modified (kit-only, ADR-004). No surprises or deviations from the
approved SPEC.

## 2. Implemented phases

### Phase A — The §Actor section

Added `### 3.0.1 The Actor` immediately after the opening AITL precept
paragraph of `## 3.0 Actor-in-the-Loop Charter (AITL)` (the first use of
the term "actor" in the charter), so the identity definition sits exactly
where the concept is introduced. The section's five blocks (definition +
checkpoint relationship, identity and grammar, independence layers, open
roles, safe default) are written in the methodology's own voice and cite
only internal references (§3.3 for the handoff rule) — no maintenance-repo
ADR citations, consistent with the charter's existing style. The content
implements US-022 AC-1..AC-5 and AC-10 verbatim in intent: human-by-default
with HITL as the default case inside AITL, actor-owned identity, the
actor-floor/hardening/ceiling ladder, open role archetypes (examples, not a
closed enum) and the zero-config pure-HITL invariant.

### Phase B — The canonical mermaid + §5.1 tree entry

Embedded the canonical Actor flow diagram (mermaid) in §3.0.1 — the single
canonical home that the `actors/` README (BOLT-002) references/embeds, per
US-022 rule #6 (no diagram drift). Added the `actors/` entry to the §5.1
canonical folder tree between `functional/` and `adrs/` (alphabetical
placement, sibling comment style): "who is in the team: the roster home
(humans + DevFlow Agents as actors; §3.0.1)".

### Phase C — Verification (GREEN)

Captured the before/after evidence: RED (no `### 3.0.1` heading, no
`actors/` tree entry, heading-token set of 77, G-count 39) → implemented →
GREEN (section at line 1381, mermaid at line 1416, tree entry at line 4203,
heading-token set 77 → 78 with the single expected addition `3.0.1 The
Actor`, G-count still 39, git status kit-only with exactly one modified
file). File encoding verified clean UTF-8 without BOM and zero replacement
characters (the US-016 encoding discipline).

## 3. Files created

| File | Purpose |
|------|---------|
| — | none (documentation edit within an existing file) |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md` | New `### 3.0.1 The Actor` subsection (definition, grammar, independence layers, open roles, safe default) + the canonical Actor mermaid + the `actors/` entry in the §5.1 canonical folder tree |

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
| §Actor lands as `### 3.0.1 The Actor` (new subsection of the AITL Charter §3.0), not a new top-level numbered section | §3.0 had no children, so **no existing number shifts** — a mid-family insertion would have renumbered §3.1–§3.15 and broken dozens of §N references kit-wide (review finding; AC-9). The `### N.M.K` scheme already exists in the doc (3.2.1, 3.3.1, 3.7.1…) |
| Placed right after the opening precept paragraph of §3.0 | The term "actor" is first used there; the identity definition deepens the precept where it is introduced |
| Section written in the methodology's own voice with internal refs only (§3.3) | The kit is the product — it must not cite maintenance-repo ADRs; consistency with the charter's existing style |
| Mermaid embedded once (canonical home) | The `actors/` README (BOLT-002) references/embeds it — no forked diagrams, no drift (US-022 rule #6) |
| `actors/` tree entry placed alphabetically before `adrs/` | Mirrors sibling entries; the canonical tree stays ordered |

## 8. Deviations and assumptions

No deviations from SPEC-260823-1335 rev 1. Assumption: the exact line
placement (right after the precept paragraph) is the least disruptive spot,
as the SPEC allowed; recorded here for the family's reference.

## 9. Verification evidence

### Presence (RED → GREEN)

```
RED:   "### 3.0.1" heading  → ABSENT
       "actors/" in §5.1    → ABSENT
GREEN: "### 3.0.1 The Actor" → PRESENT (line 1381)
       mermaid (Checkpoint pause (AITL)) → PRESENT (line 1416)
       "actors/" tree entry → PRESENT (line 4203)
```

### AC-9 section-number preservation

```
Heading token set: 77 before → 78 after; Compare-Object diff = exactly one
added token: "3.0.1 The Actor". Zero existing numbers changed — every §N
reference keeps resolving. PASS
```

### Invariants

```
G-count (kit GUARDRAILS): 39 before → 39 after   PASS
Kit-only (ADR-004):       git status -- distribution-kit = 1 modified file
                          (Avenga-DevFlow.md only)              PASS
Encoding (US-016):        clean UTF-8, no BOM, 0 replacement chars  PASS
```

### Gates

Documentation Bolt: unit/integration, SAST/SBOM, perf, IP, PII,
dep-confusion, test-first → `n/a` (no runtime, no dependencies, no personal
data). prompt-injection, secret-leak → `pass` (no runtime surface).
hallucination-lint → `pass` (all referenced artifacts resolve).
behavioral-reproducibility → `pass` (deterministic checks).
bolt-manifest-validation → `pass` (manifest updated, JSON valid).

## 10. Manual interventions

None — the agent produced everything.

## 11. Evidence links

- **Diff / PR:** none (working tree, uncommitted)
- **Commit:** baseline `45d553f`
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-022.BOLT-001-actor-concept-core.json`

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~10min |
| V-Bounce number | 1 |
| Tests created | 0 (documentation Bolt — deterministic presence/invariant checks instead) |
| AI-generated code | 100% |
| First-pass approval | pending (this MEM) |

## 13. Pending items and stubs

- [ ] BOLT-002 V-Bounce (the `actors/` folder + README — depends on this
      §3.0.1 section as its pointer target)
- [ ] BOLT-003 V-Bounce (vocabulary + four agents + the sweep, which
      includes this section and the README in its location set)

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
| **review_ready_at** | `2026-08-23T13:44:00-03:00` |
| **review.started_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **review.decided_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **Review evidence** | diff of Avenga-DevFlow.md, presence checks, AC-9 token-set proof, G-count, kit-only status, MEM, manifest |
| **Comments** | |
| **Findings** | |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | evidence inspected per the review-evidence column |
