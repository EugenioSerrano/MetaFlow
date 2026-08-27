---
id: "MEM-260823-0112"
title: "V-Bounce 2 — H1–H6 removal kit-wide (REV-004 F-05, SPEC-260823-0052 rev 2)"
date: "2026-08-23"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
bolt: "US-000.BOLT-012"
spec: "SPEC-260823-0052"
spec_revision: 2
v_bounce: 2
execution_outcome: "ready_for_review"
baseline: "1f93ebb"
applied_adrs:
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "US-000.BOLT-012-kit-consistency-residue.json"
diff_ref: ""
review_ready_at: "2026-08-23T01:12:45-03:00"
review: # HITL-MEM-Approval — recorded by the human reviewer (§3.0); decision dictated by the human in conversation ("aprobados ambos mems!") and transcribed by the agent
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - user: "eugenio.serrano"
      role: "dev_validator"
  started_at: "2026-08-23T01:17:05-03:00"
  decided_at: "2026-08-23T01:17:05-03:00"
  findings: []
  acknowledged_without_comment: true # must be true when findings is empty (§3.0)
  acknowledgment_reason: "Reviewed the V-Bounce 2 package of US-000.BOLT-012: the 7-file diff (SPEC-0052 rev 2 inventory, 15 locations), the residue sweep H1–H6 = 0 over the whole kit (plus the ASCII variant), the regression sweeps at zero (V-Bounce-1 fixes intact), G-count 39×5, four-agent parity (2 lines/pair), the MEM narrative and the validating manifest. Matches SPEC-260823-0052 rev 2 and the re-affirmed Bolt scope (maintainer direction: remove the v3-era H1–H6 kit-wide). REV-004 F-05 is now fully closed. V-Bounce approved; Bolt → Development Completed."
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs and headings (##) in
  English; prose content_language (en).

  DOGFOODING SPLIT: this V-Bounce ran under v4.2 (root devflow/, ADR-006) — its
  checkpoint is HITL-MEM-Approval, its manifest schema_version 4.0. It edited the
  v5.0 PRODUCT (distribution-kit/, AITL-*). Kit-only (ADR-004).

  Not a BUG V-Bounce (no strict red/green): localized documentation removal,
  verified by a deterministic residue sweep, not a runtime test.

  V-Bounce 2 of US-000.BOLT-012: executes SPEC-260823-0052 rev 2 after
  V-Bounce 1 was closed unapproved (changes_requested, MEM-260823-0059 kept as
  immutable history) and the Bolt/SPEC were re-approved on the revised scope
  (G15).
-->

# MEM-260823-0112 — H1–H6 removal kit-wide (V-Bounce 2)

| Field        | Value |
|--------------|-------|
| **Bolt**     | [US-000.BOLT-012](../functional/bolts/US-000.BOLT-012-kit-consistency-residue.md) |
| **SPEC**     | [SPEC-260823-0052](../spec/SPEC-260823-0052-kit-consistency-residue.md) **rev 2** |
| **V-Bounce** | 2 |
| **ADRs**     | ADR-004 (kit-only) |

---

## 1. Executive summary

This V-Bounce removes the v3-era `H1–H6` aliases from the entire kit, closing
REV-004 F-05 completely. The maintainer direction (drop H1–H6 everywhere — it
is archaic) superseded rev 1's "extend the prose with `HITL-*`" approach; the
Bolt was re-affirmed on the revised scope and SPEC-260823-0052 was revised to
rev 2 (inventory: 15 locations / 7 files, including the G05 guardrail rows
and ONBOARDING, which the rev-1 inventory and its presence-based verification
had missed). All 15 locations were edited: the four agents' preambles, G05
rows and AITL-Checkpoints sections, GUARDRAILS' G05 row and response, the
README checkpoint line, and ONBOARDING's glossary row. The legacy set is now
solely the pre-v5 `HITL-*` prefix; G05's enforcement is unchanged (canonical
13-code list, §3.0); G-count stays 39. The residue sweep the review demanded
is now the acceptance check: `H1–H6` = 0 across `distribution-kit/`.

---

## 2. Implemented phases

### Phase D (rev 2) — `H1–H6` removal, kit-wide (7 files, 15 locations)

- **Four agent definitions** (CLAUDE.md, SKILL.md, .github/…agent.md,
  .opencode/…md), three edits each:
  - AITL preamble: "Legacy H1–H6 aliases and the pre-v5 `HITL-*` prefix are
    invalid." → "The pre-v5 `HITL-*` prefix is invalid."
  - G05 row: "Legacy checkpoint names (H1–H6, or the pre-v5 `HITL-*`
    prefix)…" → "Legacy checkpoint names (the pre-v5 `HITL-*` prefix)…"
  - AITL Checkpoints section: "(legacy H1–H6 aliases are invalid)" → "(the
    pre-v5 `HITL-*` prefix is invalid)"
- **GUARDRAILS.md G05 row + response**: both the row enumeration and the
  response text now name only the pre-v5 `HITL-*` prefix as legacy.
- **devflow/README.md**: "legacy numbered aliases (H1–H6) and the pre-v5
  `HITL-*` prefix are invalid." → "the legacy pre-v5 `HITL-*` prefix is
  invalid."
- **devflow/ONBOARDING.md**: "The old H1–H6 no longer exist." → "The pre-v5
  `HITL-*` prefix is invalid (G05)."

The edits landed in lockstep across the four agents (parity re-verified), and
the residue sweep (`H1–H6` over the whole kit) returns zero.

---

## 3. Files created

| File | Purpose |
|------|---------|
| (none) | — this V-Bounce only modified existing kit files |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `distribution-kit/CLAUDE.md` | 3 edits: preamble, G05 row, AITL-Checkpoints — `H1–H6` dropped |
| `distribution-kit/.agents/skills/avenga-devflow/SKILL.md` | 3 edits, same patterns |
| `distribution-kit/.github/agents/AvengaDevFlow.agent.md` | 3 edits, same patterns |
| `distribution-kit/.opencode/agents/AvengaDevFlow.md` | 3 edits, same patterns |
| `distribution-kit/devflow/GUARDRAILS.md` | G05 row + response text — `H1–H6` dropped |
| `distribution-kit/devflow/README.md` | checkpoint line — `H1–H6` dropped, legacy = pre-v5 `HITL-*` |
| `distribution-kit/devflow/ONBOARDING.md` | glossary row — `H1–H6` dropped, `HITL-*` invalid (G05) |

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
| Remove `H1–H6` from the G05 rows too (not just the prose) | a partial sweep would recreate the same zone inconsistency (prose says legacy = `HITL-*`, G05 says `H1–H6` or `HITL-*`) — the maintainer direction was "remove it from everywhere" |
| Keep G05's enforcement unchanged, only clean the enumeration | the rule (legacy and non-canonical checkpoint names are invalid for new approvals) is preserved via the canonical 13-code list in §3.0; G-count stays 39 |
| ONBOARDING reworded to "The pre-v5 `HITL-*` prefix is invalid (G05)" | informative and precise — "no longer exist" was loose and tied to the removed aliases |

## 8. Deviations and assumptions

- **No deviations from SPEC-260823-0052 rev 2.** All 15 inventoried locations
  matched their exact current strings and were edited; the residue sweep
  (`H1–H6` = 0) is the acceptance evidence.
- V-Bounce 1 (MEM-260823-0059) remains immutable history with
  `changes_requested`; its findings are fully addressed by this V-Bounce.

---

## 9. Verification evidence

### Residue sweep (the AC-4 acceptance check, over `distribution-kit/`)

```
H1–H6  → 0 occurrences   (was 15 in 7 files: 12 agent lines + GUARDRAILS G05 + README + ONBOARDING)
H1-H6  → 0 occurrences   (ASCII-hyphen variant, belt-and-braces)
```

### Other absence sweeps (regression — the V-Bounce-1 fixes still hold)

```
never one they themselves          → 0
cannot be delegated to AI          → 0
must reach an Architect/Tech Lead  → 0
UNIT, UAT                          → 0
US-015 / ADR-010 / CHANGELOG 4.0 / tools/README → 0 (BOLT-011 scope intact)
```

### Invariant checks

```
G-count         → 39 in GUARDRAILS + 39 in each of the four agents (39×5)
Four-agent body parity → 2 sanctioned diff lines per pair (codex/ghcopilot/opencode)
git status      → 18 modified files, all in distribution-kit/ (SPEC inventories)
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

- **Diff / PR:** working tree diff of the 7 kit files (not committed — the
  human owns repository history, G34).
- **Commit:** baseline `1f93ebb` (HEAD before this V-Bounce).
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-000.BOLT-012-kit-consistency-residue.json`.

---

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~4 min (15 edits + verification sweeps) |
| V-Bounce number | 2 (V-Bounce 1: changes_requested) |
| Tests created | 0 (documentation product — deterministic sweeps instead, §9) |
| AI-generated code | 100% of the edit (human fallback: none) |
| First-pass approval | pending HITL-MEM-Approval (V-Bounce 1 was not first-pass) |

---

## 13. Pending items and stubs

- The version-marker sweep (`4.2 → 5.0` at release, REV-004 F-09) is a
  release-process step, out of scope for this Bolt.
- Once this V-Bounce is approved, US-000.BOLT-011/012 reach `Development
  Completed`; the remaining checkpoint is `HITL-BOLT-DONE-Approval` for both,
  after which REV-004 can move to Closed in `reviews/INDEX.md`.

---

## 14. HITL-MEM-Approval

> **Avenga DevFlow §2.12, §3.0.** This MEM is created by the agent with no
> mutable status and is **never self-approved**. A qualified human (the
> Dev-validator who executed the Bolt) inspects the actual diff, the residue
> sweep evidence, this MEM and the manifest, and records `HITL-MEM-Approval`
> here and in the manifest's `hitl_approvals[]`. `approved` completes the
> V-Bounce (and, if latest, marks the Bolt `Development Completed`);
> `changes_requested` keeps this MEM as immutable history and the next
> execution is a NEW V-Bounce with a NEW MEM. `HITL-BOLT-DONE-Approval` is
> still required for `Done`.

| Field | Value |
|-------|-------|
| **Reviewers (executing Dev-validator)** | `eugenio.serrano` — dev_validator |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-23T01:12:45-03:00` — package submitted |
| **review.started_at** | `2026-08-23T01:17:05-03:00` |
| **review.decided_at** | `2026-08-23T01:17:05-03:00` |
| **Review evidence** | diff of the 7 kit files + residue sweep H1–H6 = 0 + regression sweeps at zero + G-count 39×5 + parity + manifest validation |
| **Comments** | none |
| **Findings** | none |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | see frontmatter |
