---
id: "MEM-260823-0059"
title: "V-Bounce 1 — Residual consistency gaps fixed in the v5.0 kit (REV-004 F-02..F-07 + F-08)"
date: "2026-08-23"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
bolt: "US-000.BOLT-012"
spec: "SPEC-260823-0052"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "1f93ebb"
applied_adrs:
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "US-000.BOLT-012-kit-consistency-residue.json"
diff_ref: ""
review_ready_at: "2026-08-23T00:59:00-03:00"
review: # HITL-MEM-Approval — recorded by the human reviewer (§3.0); decision dictated by the human in conversation ("aprobado!" on the package: MEM-0058 approved, MEM-0059 changes_requested) and transcribed by the agent
  decision: "changes_requested" # approved | changes_requested | rejected
  reviewers:
    - user: "eugenio.serrano"
      role: "dev_validator"
  started_at: "2026-08-23T01:10:54-03:00"
  decided_at: "2026-08-23T01:10:54-03:00"
  findings:
    - "F-05 remediated incompletely: the four agents' 'AITL Checkpoints' section lines (CLAUDE.md:391, SKILL.md:408, .github/…:436, .opencode/…:419) still say '(legacy H1–H6 aliases are invalid)' without the pre-v5 `HITL-*` prefix — plus ONBOARDING.md:69 ('The old H1–H6 no longer exist'). Root cause: SPEC-0052 rev 1 inherited REV-004 F-05's narrow location and the MEM verified by presence ('present 5×') instead of a residue sweep. Maintainer direction (2026-08-23): remove the v3-era H1–H6 aliases kit-wide (prose + G05 rows) — supersedes the 'extend with HITL-*' approach."
  acknowledged_without_comment: false
  acknowledgment_reason: ""
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs and headings (##) in
  English; prose content_language (en).

  DOGFOODING SPLIT: this V-Bounce ran under v4.2 (root devflow/, ADR-006) — its
  checkpoint is HITL-MEM-Approval, its manifest schema_version 4.0. It edited the
  v5.0 PRODUCT (distribution-kit/, AITL-*). Kit-only (ADR-004).

  Not a BUG V-Bounce (no strict red/green): localized documentation
  corrections, verified by deterministic absence/presence sweeps, not a
  runtime test.
-->

# MEM-260823-0059 — Residual consistency gaps (REV-004 F-02..F-07 + F-08)

| Field        | Value |
|--------------|-------|
| **Bolt**     | [US-000.BOLT-012](../functional/bolts/US-000.BOLT-012-kit-consistency-residue.md) |
| **SPEC**     | [SPEC-260823-0052](../spec/SPEC-260823-0052-kit-consistency-residue.md) rev 1 |
| **V-Bounce** | 1 |
| **ADRs**     | ADR-004 (kit-only) |

---

## 1. Executive summary

This V-Bounce applied the six localized consistency corrections of REV-004
F-02..F-07 plus the cosmetic F-08 across 9 files of `distribution-kit/`,
aligning the kit's prose and summaries with its own normative rules. §3.9 no
longer forbids the BUG's own author from approving (it now states G29's
rule: guidance, never a gate, author included, any severity); §0's absolute
"cannot be delegated to AI" was replaced by the AITL charter's
human-by-default / explicit-valid-configuration wording; the checkpoint
INDEX lists exactly the 13 §3.0 codes (UNIT/UAT gone); the legacy-name prose
in `README.md` and all four agent preambles now includes the pre-v5
`HITL-*` prefix (matching G05); `reviews/README.md` says "recommended"
instead of "must reach"; §3.1 declares the AREV per-phase-model `llm`
exception that W09 already enforces; and the two templates' placeholder
links became code spans. Verification: every absence sweep returns zero, the
§3.1 exception and the 5× legacy phrase are present, G-count 39×5, four-agent
body parity at the sanctioned 2 lines per pair (the four preambles changed
in lockstep), and `git status` shows only kit files.

---

## 2. Implemented phases

### Phase A — F-02: §3.9 Dev-validator role

The clause "— never one they themselves drafted or authored" (which spanned
the 2597-2598 line break) was replaced: the Dev-validator now "approve[s]
non-functional BUGs (and their dedicated Bolt) at any severity — any
qualified team member, the BUG's own author included, may record the
approval (G29: guidance, never a gate)". G29 itself was not touched.

### Phase B — F-03: §0 Quick Start

"A human checkpoint cannot be delegated to AI." became the charter wording:
"A checkpoint is occupied by a human **by default**; a virtual DevFlow Agent
only by explicit, valid configuration — absent or invalid configuration,
every checkpoint is human-only and no AI-signed approval is possible (§3.0)."

### Phase C — F-04: checkpoint enumeration

`avenga-devflow/INDEX.md` now lists exactly the 13 §3.0 codes; `UNIT, UAT`
were dropped from the enumeration.

### Phase D — F-05: legacy-name prose (5 files in lockstep)

`devflow/README.md` and the AITL preamble of all four agent definitions now
read "Legacy H1–H6 aliases and the pre-v5 `HITL-*` prefix are invalid"
(README: "legacy numbered aliases (H1–H6) and the pre-v5 `HITL-*` prefix are
invalid"), matching the G05 row carried inline in the same files.

### Phase E — F-06: reviews/README severity mapping

"`critical` when a non-functional BUG must reach an Architect/Tech Lead"
became "`critical` when the recommended approver for a non-functional BUG is
an Architect/Tech Lead (guidance, never a gate — any qualified team member,
the author included, may approve)".

### Phase F — F-07: §3.1 `llm`-rule exception

The LLM-traceability bullet now closes with: "The AREV phase templates are
the exception: they record the executing model via `challenger_model` /
`defender_model` / `judge_model` (§2.15, §3.13) and carry no separate `llm:`
field." — declaring exactly what W09 enforces.

### Phase G — F-08 (cosmetic): template placeholder links

The phase-table links in `TEMPLATE-AREV.md` and the Bolts-table links in
`TEMPLATE-US.md` are now code spans (`` `01-CRITIQUE.md` `` etc.) — they no
longer appear as markdown links and stop tripping link checkers.

---

## 3. Files created

| File | Purpose |
|------|---------|
| (none) | — this V-Bounce only modified existing kit files |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md` | 3 edits: §3.9 author-gate removed (G29 wording), §0 charter wording, §3.1 AREV `llm` exception |
| `distribution-kit/devflow/avenga-devflow/INDEX.md` | checkpoint enumeration → 13 codes (UNIT, UAT dropped) |
| `distribution-kit/devflow/README.md` | legacy-name line includes the pre-v5 `HITL-*` prefix |
| `distribution-kit/CLAUDE.md` | AITL preamble legacy line includes the pre-v5 `HITL-*` prefix |
| `distribution-kit/.agents/skills/avenga-devflow/SKILL.md` | same |
| `distribution-kit/.github/agents/AvengaDevFlow.agent.md` | same |
| `distribution-kit/.opencode/agents/AvengaDevFlow.md` | same |
| `distribution-kit/devflow/reviews/README.md` | "must reach" → "recommended" (G29 wording) |
| `distribution-kit/devflow/adversarial-reviews/TEMPLATE-AREV.md` | placeholder links → code spans |
| `distribution-kit/devflow/functional/user-stories/TEMPLATE-US.md` | placeholder links → code spans |

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
| —    | —        | —      |

## 6. Files deleted

| File | Reason |
|------|--------|
| —    | —      |

---

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| Align §3.9 to G29 instead of editing G29 | the direction is settled (G29 governs, US-000.BOLT-010 Done); §3.9 was the outlier — no ADR needed (REV-004 §6) |
| Per-file exact replacements in the four agent preambles | the four preambles' wording differs slightly from `README.md`'s; a single find/replace would over-match — each file got its own exact edit, then parity re-verified |
| Mirror W09's exact exception sentence in §3.1 | prevents F-07 wording drift between the guardrail and the methodology |

## 8. Deviations and assumptions

- **No deviations from SPEC-260823-0052 rev 1.** All edits landed at the
  inventoried locations; every target string matched exactly (the §3.9
  phrase was caught across its line break with a multiline-aware edit).
- **Sequential-overlap note (§3.2, G15):** BOLT-012 shares
  `Avenga-DevFlow.md` and `README.md` with BOLT-011, whose V-Bounce ran
  immediately before this one in the same session. The BOLT-011 edit ranges
  (US-015/ADR-010/README rows 63-355) are **disjoint** from this V-Bounce's
  targets (verified: every one of this V-Bounce's old-strings matched the
  post-BOLT-011 tree exactly, and no BOLT-011 edit touched lines 141, 1822,
  244 or 2597-2598 of the methodology/README). Recorded for the reviewer; no
  SPEC re-approval was triggered because the baseline change was not material
  to this SPEC's inventory.

---

## 9. Verification evidence

### Absence sweeps (deterministic, over `distribution-kit/`)

```
"never one they themselves"          → 0 occurrences
"cannot be delegated to AI"          → 0 occurrences
"must reach an Architect/Tech Lead"  → 0 occurrences
"UNIT, UAT"                          → 0 occurrences
```

### Presence assertions

```
§3.1 exception sentence ("challenger_model / defender_model / judge_model") → present (methodology)
"pre-v5 `HITL-*` prefix" in the legacy line → present 5× (README + 4 agent preambles)
```

### Invariant checks

```
G-count         → 39 in GUARDRAILS + 39 in each of the four agents (39×5)
Four-agent body parity → 2 sanctioned diff lines per pair (codex/ghcopilot/opencode)
git status      → 18 modified files, all in distribution-kit/ (BOLT-011 10 + BOLT-012 8)
```

### Gates

All applicable gates `pass` or `n/a` with reason (SPEC-260823-0052 §9):
secret-leak pass, hallucination-lint pass, behavioral-reproducibility pass,
bolt-manifest validation pass; product-code gates `n/a` (documentation
product).

---

## 10. Manual interventions

None — the agent produced the entire change.

---

## 11. Evidence links

- **Diff / PR:** working tree diff of the 9 kit files (not committed — the
  human owns repository history, G34).
- **Commit:** baseline `1f93ebb` (HEAD before this V-Bounce).
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-000.BOLT-012-kit-consistency-residue.json`.

---

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~5 min (edit + verification sweeps) |
| V-Bounce number | 1 |
| Tests created | 0 (documentation product — deterministic sweeps instead, §9) |
| AI-generated code | 100% of the edit (human fallback: none) |
| First-pass approval | pending HITL-MEM-Approval |

---

## 13. Pending items and stubs

- The version-marker sweep (`4.2 → 5.0` at release, REV-004 F-09) is a
  release-process step, out of scope for this Bolt.
- REV-004's cosmetic citation nit (F-02 parenthetical) is recorded in the
  REV's approval evidence; the REV is immutable, so the nit is informational
  only.

---

## 14. HITL-MEM-Approval

> **Avenga DevFlow §2.12, §3.0.** This MEM is created by the agent with no
> mutable status and is **never self-approved**. A qualified human (the
> Dev-validator who executed the Bolt) inspects the actual diff, the
> deterministic sweep evidence, this MEM and the manifest, and records
> `HITL-MEM-Approval` here and in the manifest's `hitl_approvals[]`.
> `approved` completes the V-Bounce (and, if latest, marks the Bolt
> `Development Completed`); `changes_requested` keeps this MEM as immutable
> history and the next execution is a NEW V-Bounce with a NEW MEM.
> `HITL-BOLT-DONE-Approval` is still required for `Done`.

| Field | Value |
|-------|-------|
| **Reviewers (executing Dev-validator)** | `eugenio.serrano` — dev_validator |
| **Decision** | **changes_requested** |
| **review_ready_at** | `2026-08-23T00:59:00-03:00` — package submitted |
| **review.started_at** | `2026-08-23T01:10:54-03:00` |
| **review.decided_at** | `2026-08-23T01:10:54-03:00` |
| **Review evidence** | diff of the 9 kit files + absence/presence sweeps + G-count 39×5 + parity + manifest validation |
| **Comments** | F-05 residue (5 lines: 4× agent AITL-Checkpoints + ONBOARDING:69) → SPEC-260823-0052 rev 2 (H1–H6 removal kit-wide) → V-Bounce 2 |
| **Findings** | see frontmatter `findings` |
| **acknowledged_without_comment** | false |
| **acknowledgment_reason** | — |
