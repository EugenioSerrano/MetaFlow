---
id: "MEM-260823-0058"
title: "V-Bounce 1 — Kit self-containment: US-015 / ADR-010 / CHANGELOG-tools leaks removed from distribution-kit/"
date: "2026-08-23"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
bolt: "US-000.BOLT-011"
spec: "SPEC-260823-0051"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "1f93ebb"
applied_adrs:
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "US-000.BOLT-011-kit-self-containment.json"
diff_ref: ""
review_ready_at: "2026-08-23T00:58:30-03:00"
review: # HITL-MEM-Approval — recorded by the human reviewer (§3.0); decision dictated by the human in conversation ("aprobado!") and transcribed by the agent
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - user: "eugenio.serrano"
      role: "dev_validator"
  started_at: "2026-08-23T01:10:54-03:00"
  decided_at: "2026-08-23T01:10:54-03:00"
  findings: []
  acknowledged_without_comment: true # must be true when findings is empty (§3.0)
  acknowledgment_reason: "Reviewed the V-Bounce 1 package of US-000.BOLT-011: the 10-file kit diff (exactly the SPEC-0051 §4 inventory), the absence sweeps at zero (US-015/ADR-010/CHANGELOG 4.0/tools-README over the whole kit), G-count 39×5, four-agent parity (2 lines/pair), the informative UAT notes preserved, the report template ID-token-only change, the MEM narrative and the validating manifest. Matches SPEC-260823-0051 rev 1 and REV-004 F-01. The sequential-overlap note (disjoint edit ranges vs BOLT-012) was verified. V-Bounce approved; Bolt → Development Completed."
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs and headings (##) in
  English; prose content_language (en).

  DOGFOODING SPLIT: this V-Bounce ran under v4.2 (root devflow/, ADR-006) — its
  checkpoint is HITL-MEM-Approval, its manifest schema_version 4.0. It edited the
  v5.0 PRODUCT (distribution-kit/, AITL-*). Kit-only (ADR-004).

  Not a BUG V-Bounce (no strict red/green): documentation self-containment pass,
  verified by deterministic absence/presence sweeps (REV-004/ADR-005 method),
  not a runtime test.
-->

# MEM-260823-0058 — Kit self-containment (REV-004 F-01)

| Field        | Value |
|--------------|-------|
| **Bolt**     | [US-000.BOLT-011](../functional/bolts/US-000.BOLT-011-kit-self-containment.md) |
| **SPEC**     | [SPEC-260823-0051](../spec/SPEC-260823-0051-kit-self-containment.md) rev 1 |
| **V-Bounce** | 1 |
| **ADRs**     | ADR-004 (kit-only) |

---

## 1. Executive summary

This V-Bounce made the v5.0 kit self-contained: an adopter can now resolve
every identifier the kit references from the kit alone. Three leak families
evidenced by REV-004 F-01 were removed from 10 files of `distribution-kit/`:
(1) all 29 occurrences of the maintainer-repository ID `US-015` were replaced
with version-neutral phrasing, keeping the informative content of every UAT
dormant/reserved note ("removed in v4.2", "redesigned model planned"); (2) the
6 `ADR-010` citations in the methodology were dropped — the actor grammar's
normative content stands on §3.0 itself, and the approved SPEC's chosen
mechanism (drop, no appendix) was confirmed at HITL-SPEC-Approval; (3) the
dangling `CHANGELOG 4.0` citation and the `tools/README.md` forward-reference
in `devflow/README.md` were replaced with in-kit references. The report
template's sample data moved from the repo-colliding US-011/US-015 to neutral
US-101/US-102 (ID tokens only, structure untouched). Verification: absence
sweeps return zero for all four leak families; G-count 39×5; four-agent body
parity at the sanctioned 2 lines per pair; `git status` shows exactly the 10
kit files of the SPEC inventory, nothing else.

---

## 2. Implemented phases

### Phase A — `US-015` sweep (10 files, 29 occurrences)

Every `US-015` token was replaced by context-preserving phrasing:
`(a redesigned model is planned for a future version)` in the methodology
coverage note, `planned for a future version` in the §3.11/§4.7 release
notes, the GUARDRAILS G20 and coverage-section notes, the folder-map and
Known-Limitations rows of `devflow/README.md`, the four `tests/README.md`
spots, the three `tests/uat/` files, the three `analysis/README.md` spots,
ONBOARDING's UAT glossary row, and 11 sample-data ID tokens in
`TEMPLATE-REPORT.html`. No sentence lost its meaning; only the unresolvable
ID went away.

### Phase B — `ADR-010` citation removal (methodology, 6 occurrences)

The six citations (`the actor grammar (ADR-010)`, `§3.0/ADR-010)`,
`(§3.0, ADR-010)`, `ADR-010 §3.4`, `ADR-010 §3.1–§3.4`, `ADR-010 §3.6–§3.7`)
were removed; the surrounding text now references §3.0 or nothing. The actor
grammar paragraph itself is byte-identical except the citation tokens — the
rule content did not change.

### Phase C — dangling references (`devflow/README.md`, 2 edits)

The Known-Limitations "Monetary cost" row now cites `§3.12` (the token model
in `runs[]`) instead of `CHANGELOG 4.0 "cross-model review round"`, and the
"Validation tooling" row cites the tools track (`§5.1`) instead of
`tools/README.md`.

---

## 3. Files created

| File | Purpose |
|------|---------|
| (none) | — this V-Bounce only modified existing kit files |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md` | 3× `US-015` → neutral phrasing; 6× `ADR-010` citations dropped (actor grammar content untouched) |
| `distribution-kit/devflow/GUARDRAILS.md` | 2× `US-015` → "planned for a future version" (G20 row + coverage note) |
| `distribution-kit/devflow/README.md` | 4 edits: folder-map row, Known-Limitations "Where it is governed" cells (US-015; CHANGELOG 4.0; tools/README.md) |
| `distribution-kit/devflow/tests/README.md` | 4× `(US-015)` removed, informative text kept |
| `distribution-kit/devflow/tests/uat/README.md` | "future release (US-015)" → "future version" |
| `distribution-kit/devflow/tests/uat/INDEX.md` | "future release (US-015)" → "future version" |
| `distribution-kit/devflow/tests/uat/TEMPLATE-UAT.md` | dormant banner "(US-015)" removed |
| `distribution-kit/devflow/analysis/README.md` | 3× `(US-015)` removed (notes, flow node, relation table) |
| `distribution-kit/devflow/ONBOARDING.md` | UAT glossary row "ships (US-015)" → "ships in a future version" |
| `distribution-kit/devflow/reports/TEMPLATE-REPORT.html` | 11 sample-data ID tokens: US-011 → US-101, US-015 → US-102 (structure untouched) |

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
| Drop the `ADR-010` citations rather than ship an appendix | the actor grammar is already fully normative in §3.0; an appendix would duplicate normative text (drift risk). Confirmed at HITL-SPEC-Approval |
| Keep every informative UAT note, replace only the ID token | the information ("removed in v4.2", "dormant/reserved", "redesigned model planned") is the point; the ID is the leak (SPEC AC-5) |
| US-101/US-102 as neutral report sample IDs | 3-digit schema pattern preserved, no collision with real repository IDs |

## 8. Deviations and assumptions

- **No deviations from SPEC-260823-0051 rev 1.** All edits landed at the
  inventoried locations; one GUARDRAILS occurrence (G20 row) needed a
  full-context second edit because its surrounding text differed from the
  sweep pattern — the outcome is identical (zero residue).
- **Sequential-overlap note (§3.2, G15):** BOLT-011 and BOLT-012 both touch
  `Avenga-DevFlow.md` and `README.md`; the two V-Bounces ran sequentially in
  one session. BOLT-012's SPEC-inventoried edit ranges (§3.9, §0:141, §3.1,
  README:244, INDEX, reviews/README, templates) are **disjoint** from this
  V-Bounce's ranges (verified: every BOLT-012 edit target matched its exact
  pre-edit string after this V-Bounce completed), so this V-Bounce's baseline
  change was not material to BOLT-012's approved SPEC. Recorded for the
  reviewer; no SPEC re-approval was triggered.

---

## 9. Verification evidence

### Absence sweeps (deterministic, over `distribution-kit/`)

```
US-015          → 0 occurrences   (was 29 in 10 files)
ADR-010         → 0 occurrences   (was 6 in the methodology)
CHANGELOG 4.0   → 0 occurrences   (was 1 in devflow/README.md)
tools/README    → 0 occurrences   (was 1 in devflow/README.md)
```

### Invariant checks

```
G-count         → 39 in GUARDRAILS + 39 in each of the four agents (39×5)
Four-agent body parity → 2 sanctioned diff lines per pair (codex/ghcopilot/opencode)
git status      → 10 modified files, all in distribution-kit/ (SPEC §4 inventory)
TEMPLATE-REPORT.html → structure intact (ID-token-only edits, spot-checked)
```

### Gates

All applicable gates `pass` or `n/a` with reason (SPEC-260823-0051 §9):
secret-leak pass, hallucination-lint pass (every edited phrase resolves on
disk), behavioral-reproducibility pass (sweeps re-runnable), bolt-manifest
validation pass; product-code gates `n/a` (documentation product).

---

## 10. Manual interventions

None — the agent produced the entire change.

---

## 11. Evidence links

- **Diff / PR:** working tree diff of the 10 kit files (not committed — the
  human owns repository history, G34).
- **Commit:** baseline `1f93ebb` (HEAD before this V-Bounce).
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-000.BOLT-011-kit-self-containment.json`.

---

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~7 min (edit + verification sweeps) |
| V-Bounce number | 1 |
| Tests created | 0 (documentation product — deterministic sweeps instead, §9) |
| AI-generated code | 100% of the edit (human fallback: none) |
| First-pass approval | pending HITL-MEM-Approval |

---

## 13. Pending items and stubs

- The version-marker sweep (`4.2 → 5.0` at release, REV-004 F-09) is a
  release-process step, out of scope for this Bolt.
- The root `devflow/` inherits the kit's self-contained state at the next
  §5.16 migration (ADR-004).

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
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-23T00:58:30-03:00` — package submitted |
| **review.started_at** | `2026-08-23T01:10:54-03:00` |
| **review.decided_at** | `2026-08-23T01:10:54-03:00` |
| **Review evidence** | diff of the 10 kit files + absence sweeps at zero + G-count 39×5 + parity + manifest validation |
| **Comments** | none |
| **Findings** | none |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | see frontmatter |
