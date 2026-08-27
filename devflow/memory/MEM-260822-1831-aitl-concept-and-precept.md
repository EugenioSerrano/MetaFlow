---
id: "MEM-260822-1831"
title: "AITL concept & precept — §0 reframe + §3.0 Charter + agents/README concept (US-021.BOLT-001)"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
bolt: "US-021.BOLT-001"
spec: "SPEC-260822-1817"
spec_revision: 2
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "97125e7"
applied_adrs:
  - "devflow/adrs/ADR-008-aitl-approval-precept.md"
  - "devflow/adrs/ADR-007-devflow-agent-identity-model.md"
  - "devflow/adrs/ADR-005-removal-completeness-phrase-family-sweep.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "US-021.BOLT-001-aitl-concept-and-precept.json"
diff_ref: "" # uncommitted working tree at MEM time
review_ready_at: "2026-08-22T18:31:47-03:00"
review: # HITL-MEM-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "dev_validator"}]
  started_at: "2026-08-22T18:34:26-03:00"
  decided_at: "2026-08-22T18:34:26-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Inspected the 6 concept files' diff, the AC-5 identifier-count boundary proof (1119->1119, zero identifier/adjective drift), the AITL precept + §3.0 Charter + AITL definition, four-agent sync + G-count 39x5, kit-only. V-Bounce GREEN against rev 2. Concept layer of the HITL->AITL evolution done."
---

<!--
  LANGUAGE POLICY (§3.15): schema/headings English; prose content_language (en).
  Kit-only product surface (ADR-004); root governance records stay on the 4.2
  maintenance partition (HITL-* naming, schema 4.0).
-->

# MEM-260822-1831 — AITL concept & precept (US-021.BOLT-001)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | [US-021.BOLT-001](../functional/bolts/US-021.BOLT-001-aitl-concept-and-precept.md) |
| **SPEC**        | [SPEC-260822-1817](../spec/SPEC-260822-1817-aitl-concept-and-precept.md) revision 2 |
| **V-Bounce**    | 1 |
| **ADRs**        | ADR-008 (§3.1/§3.2 precept), ADR-007 (actor), ADR-005 (boundary), ADR-004 (kit-only) |

---

## 1. Executive summary

This V-Bounce evolved the **Human-in-the-Loop concept** of the v5.0 kit into
**AITL (Actor-in-the-Loop)** — the conceptual heart of ADR-008 §3.1 and the first
of US-021's four Bolts. The core methodology's precept was reframed from *"the AI
generates, the human governs at every checkpoint"* to **"human-by-default,
agent-by-explicit-configuration"**: the Foundational principle now speaks of an
**actor** (a human by default, a virtual DevFlow Agent only by explicit valid
configuration) and states the **safe-default invariant** (no/invalid config → pure
Human-in-the-Loop, no AI-signed approval possible); §3.0's heading became the
**Actor-in-the-Loop Charter (AITL)** with an opening that **defines AITL + the
actor** and frames **HITL as the default case** (actor = human) inside AITL, not a
separate paradigm; the four platform agents' concept section and the README
concept heading/intro carry the same framing. The outcome is GREEN against the
rev-2 acceptance criteria; crucially, the **`HITL-<CODE>-Approval` identifier count
is unchanged (1,119 before and after)** — the boundary proof that this Bolt touched
only the concept, never the identifiers (BOLT-004) or the pervasive "HITL"
adjective (BOLT-004). A finding drove an in-cycle SPEC revision: execution-time
investigation showed "HITL" is pervasive (three categories, ~61 concept lines in
the core), so the SPEC was revised rev 1 → rev 2 to a **crisp 3-category boundary**
before any edit — BOLT-001 owns only category 1 (the precept-defining prose). No
guarantee was weakened; every checkpoint remains a mandatory pause.

---

## 2. Implemented phases

### Phase A — core concept (Avenga-DevFlow.md)
Reframed the **Foundational principle** (~237–248) to the AITL precept
(actor / human-by-default / agent-by-explicit-config / safe-default invariant;
"no artifact reaches production without an approved checkpoint"), and the **§3.0
Charter** heading (`Human-in-the-Loop Charter (HITL)` → `Actor-in-the-Loop Charter
(AITL)`) + opening, which now **defines AITL and the actor** and states **HITL is
the default case of AITL**. Metric axis names (e.g. `human-review-time`, §3.7) were
left untouched (not part of the precept). The `HITL-<CODE>-Approval` identifiers,
the canonical naming rule, and the pervasive "HITL" adjective were deliberately
left for BOLT-004.

### Phase B — agents + README
Reframed the four platform agents' concept section — heading
(`# HITL -- HUMAN-IN-THE-LOOP …` → `# AITL -- ACTOR-IN-THE-LOOP …`) + precept intro
(actor / human-by-default / safe default / "never approve your own work") —
**byte-identical** across the four; and the README concept heading
(`## HITL Checkpoints (Human-in-the-Loop)` → `## Checkpoints (Actor-in-the-Loop —
AITL)`) + precept intro. The README's identifier-naming sentence
(`Checkpoints are named `HITL-<CODE>-Approval`; … H1–H6 … invalid`) was kept
**verbatim** (category 3 → BOLT-004).

---

## 3. Files created

| File | Purpose |
|------|---------|
| _(none)_ | Concept prose only; no new files. |

---

## 4. Files modified

| File | Change (category 1 — concept/precept only) |
|------|--------------------------------------------|
| `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md` | Foundational principle → AITL precept; §3.0 heading/opening → Actor-in-the-Loop Charter (AITL) + AITL definition |
| `distribution-kit/CLAUDE.md` | Concept section heading + precept intro → AITL (byte-synced) |
| `distribution-kit/.agents/skills/avenga-devflow/SKILL.md` | Same (byte-synced) |
| `distribution-kit/.github/agents/AvengaDevFlow.agent.md` | Same (byte-synced) |
| `distribution-kit/.opencode/agents/AvengaDevFlow.md` | Same (byte-synced) |
| `distribution-kit/devflow/README.md` | Checkpoints concept heading + precept intro → AITL (identifier-naming sentence kept verbatim) |
| `devflow/spec/SPEC-260822-1817*` (rev 1→2), `metrics/bolts/US-021.BOLT-001*.json`, this MEM | Governance records (root, 4.2) |

---

## 5. Files renamed / 6. Files deleted

_(none)_

---

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| In-cycle SPEC rev 1 → rev 2 (crisp 3-category boundary) | Investigation found "HITL" is pervasive (paradigm / adjective / identifier, ~61 core lines); the rev-1 boundary was ambiguous about the adjective. Fixed before any edit → no partial-sweep trap |
| BOLT-001 = category 1 (precept prose) only | The adjective (cat 2) and identifiers (cat 3) interleave on the same lines; one comprehensive BOLT-004 sweep is cleaner than splitting them |
| Kept the identifier-naming line + metric axis names verbatim | They are category 3 / §3.7 concerns, not the precept — out of scope here |
| State (not enforce) the safe-default invariant | Enforcement (Coordinator, validators) is downstream US/Bolt work; the precept must still state it |
| Keep "HITL" as the named default case | ADR-008 §3.1 — HITL does not disappear; it becomes actor = human inside AITL |

---

## 8. Deviations and assumptions

- **In-cycle SPEC revision (rev 1 → rev 2), finding-driven.** No edits were made
  under rev 1; the V-Bounce completes against rev 2 (no G16 span).
- **Intentional mid-development mixed state:** the kit now states the AITL precept
  but still carries the "HITL" adjective ("HITL approval", "HITL Coverage", …) and
  the `HITL-<CODE>-Approval` identifiers — both close in **BOLT-004**. This is by
  design (each Bolt independently demonstrable).
- **Assumption:** enforcement of the safe-default/independence rules is out of
  scope (later USs); this Bolt states them (ADR-008 §3.2/§3.3).

---

## 9. Verification evidence

### Build / Tests
```
n/a — concept/documentation Bolt. The deterministic checks are below.
```

### AC-5 boundary proof — identifier count unchanged
```
HITL-[A-Z][A-Z-]*-Approval  in distribution-kit/*.md :  RED (before) 1119  →  GREEN (after) 1119
=> this Bolt changed ZERO identifiers (categories 2+3 untouched; BOLT-004's).
```

### AITL concept present (AC-1/2/3)
```
Avenga-DevFlow.md:237  "> **Foundational principle (Actor-in-the-Loop — AITL, non-negotiable):**"
Avenga-DevFlow.md:1367 "## 3.0 Actor-in-the-Loop Charter (AITL)" + opening defines AITL, the actor,
                        HITL-as-default-case and the safe-default invariant.
```

### Four-agent sync (AC-4) + kit-only (AC-6)
```
concept heading "# AITL -- ACTOR-IN-THE-LOOP (OVERRIDES AUTONOMY)": 4/4
concept intro (actor / human-by-default / safe default): 4/4 byte-identical
G-count: 39 · 39 · 39 · 39
git status: only distribution-kit/ (the 6 concept files) + root governance records; root framework untouched.
```

### Gates
- unit/integration, SAST/DAST/SBOM, perf, IP, PII, dep-confusion, test-first: **n/a** (concept/internal, SPEC §9).
- hallucination-lint (refs resolve), behavioral-reproducibility (deterministic),
  bolt-manifest-validation (validates GREEN vs. root v4 schema): **pass**.

### BUG V-Bounce evidence
n/a — not a BUG V-Bounce.

---

## 10. Manual interventions

None. All edits agent-generated; the human role was HITL-SPEC-Approval (rev 1 +
rev 2) and the rev-2 boundary decision.

---

## 11. Evidence links

- **Diff / PR:** none yet (uncommitted; accumulates on the 5.0 branch).
- **Commit:** baseline at the maintainer's latest 5.0-branch commit (US-020 delivered).
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-021.BOLT-001-aitl-concept-and-precept.json`.

---

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~1.5h (concept prose + one in-cycle SPEC revision) |
| V-Bounce number | 1 |
| Tests created | boundary check (identifier count invariance) + concept-presence checks |
| AI-generated code | 100% (docs); no human fallback |
| First-pass approval | pending (this MEM) |

---

## 13. Pending items and stubs

- [ ] **US-021.BOLT-002** — GUARDRAILS scoping (G05 canonical → AITL, HITL legacy; G18/G24 per ADR-008 §3.4; G37/handoff note; count unchanged).
- [ ] **US-021.BOLT-003** — schema enum accepts `AITL-*` (SPEC/MEM conditionals for both prefixes; keep `HITL-*`).
- [ ] **US-021.BOLT-004** — comprehensive kit-wide sweep: the "HITL" **adjective** (cat 2) **and** the `HITL-<CODE>-Approval` **identifiers** (cat 3, ~1,119) + naming rule → AITL, ADR-005 phrase family + allowlist.
- [ ] On all four Done → US-021 delivered (kit fully AITL).

---

## 14. HITL-MEM-Approval

> **Avenga DevFlow §2.12, §3.0.** This MEM is created by the agent with no mutable
> status and is **never self-approved**. The executing Dev-validator inspects the
> diff, the boundary/concept evidence, this MEM and the manifest, and records
> `HITL-MEM-Approval` here and in the manifest's `hitl_approvals[]`. `approved`
> completes the V-Bounce and (latest MEM) marks the Bolt `Development Completed`;
> `HITL-BOLT-DONE-Approval` is still required for `Done`.

| Field | Value |
|-------|-------|
| **Reviewers (executing Dev-validator; QA/Sec/domain optional)** | eugenio.serrano |
| **Roles** | dev_validator |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-22T18:31:47-03:00` |
| **review.started_at** | `2026-08-22T18:34:26-03:00` |
| **review.decided_at** | `2026-08-22T18:34:26-03:00` |
| **Review evidence** | The 6 concept files' diff, AC-5 identifier-count boundary proof (1119→1119), AITL concept presence, four-agent sync + G-count 39×5, rev-2 manifest |
| **Comments** | Approved; concept layer of HITL→AITL done |
| **Findings** | none |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | Evidence inspected as above; V-Bounce GREEN against rev 2 |
