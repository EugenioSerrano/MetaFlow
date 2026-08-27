---
id: "SPEC-260823-0051"
title: "Kit self-containment: remove the maintainer-repository identifier leaks (US-015, ADR-010, CHANGELOG/tools) from distribution-kit/"
date: "2026-08-23"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved" # draft | approved | blocked | obsolete
origin: "REV-004" # F-01 — the distributable-self-containment evidence
bolt: "US-000.BOLT-011" # ⚠️ MANDATORY
revision: 1
associated_adrs:
  - "devflow/adrs/ADR-004-repository-partition-v2.md" # kit-only edits
prerequisites: []
risk_class: "low" # mirrors the Bolt
autonomy_level: "L3" # low → L3 default; deterministic doc sweep
turn_budget: "" # platform default (10 loops without green)
data_classification: "internal"
review_ready_at: "2026-08-23T00:51:46-03:00"
review: # HITL-SPEC-Approval — recorded by the human reviewer (§3.0); decision dictated by the human in conversation ("aprobados!") and transcribed by the agent
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - user: "eugenio.serrano"
      role: "dev_validator"
    - user: "eugenio.serrano"
      role: "tech_lead"
  started_at: "2026-08-23T00:54:35-03:00"
  decided_at: "2026-08-23T00:54:35-03:00"
  findings: []
  acknowledged_without_comment: true # must be true when findings is empty (§3.0)
  acknowledgment_reason: "Approved revision 1 against the approved Bolt US-000.BOLT-011, REV-004 (F-01) and ADR-004. The location inventory matches the working tree; the ADR-010 mechanism decision (drop citations, no appendix) is confirmed; ACs are objectively checkable; gates n/a reasoned; stop conditions defined. Reviewer holds dev_validator and tech_lead (domain owner) — self-assigned, single-operator. V-Bounce authorized."
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs and headings (##) in
  English; prose content_language (en).

  DOGFOODING SPLIT: authored under v4.2 (root devflow/, ADR-006), own checkpoint
  HITL-SPEC-Approval, manifest schema_version 4.0. Implements US-000.BOLT-011 by
  editing the v5.0 PRODUCT (distribution-kit/, vocabulary AITL-*). Kit-only
  (ADR-004); the root tree inherits at the next §5.16 migration.

  ⚠️ DRAFT until HITL-SPEC-Approval. SPEC approval authorizes the V-Bounce; no
  code-run before it (G14).
-->

# SPEC-260823-0051 — Kit self-containment (REV-004 F-01)

| Field | Value |
|-------|-------|
| **Origin** | REV-004 (approved 2026-08-23 — F-01, the identifier-leak evidence) |
| **Bolt** | [US-000.BOLT-011](../functional/bolts/US-000.BOLT-011-kit-self-containment.md) — HITL-BOLT-READY-Approval 2026-08-23T00:51:05 |
| **ADRs** | ADR-004 (kit-only) |
| **Risk / Autonomy** | low / L3 |

---

## 1. Objective

Edit the v5.0 kit (`distribution-kit/`) so that **an adopter can resolve every
referenced identifier from the kit alone**. Remove the three leak families
evidenced by REV-004 F-01:

1. **`US-015`** — 10 files / 29 occurrences → replaced by version-neutral
   phrasing (the UAT dormant/reserved notes stay, without the ID).
2. **`ADR-010`** — 6 citations in the methodology presented as the normative
   basis of the actor grammar → **dropped** (the chosen mechanism; the actor
   grammar's normative content is fully written out in §3.0, so no appendix is
   needed — this is the maintainer's preferred option, to be confirmed at SPEC
   review; if changes are requested on this point, the appendix route is the
   fallback).
3. **CHANGELOG / tools dangling references** in `devflow/README.md` →
   CHANGELOG citation removed; `tools/README.md` reference rephrased as a
   forward reference to the tools track.

If NOT done: every adopter installs a kit whose methodology references
`US-015` and `ADR-010` (which do not exist in their repository) and cites a
CHANGELOG and a `tools/` folder the kit does not ship — the kit's defining
promise (self-contained distribution) is broken, and the fix gets more
expensive after release (every adopter copy carries the leaks).

**Scope boundary:** no rule, checkpoint, guardrail or schema changes. The
actor grammar text itself is untouched — only its `ADR-010` citations are
removed. The deliberate legacy `HITL-*` mentions (G05, §5.16) stay. Kit-only
(ADR-004).

---

## 2. Context

REV-004 (approved 2026-08-23, HITL-REV-Approval) evidenced that the kit —
structurally healthy per REV-002/REV-003 — is not yet self-contained: it
leaks identifiers that exist solely in the maintainer repository. The
`US-015` references describe the planned redesigned Unit/UAT model; the
`ADR-010` citations point at the decision behind the actor grammar (whose
content is already normative in §3.0 of the kit); the README cites internal
history (`CHANGELOG 4.0 "cross-model review round"`) and an unshipped file
(`tools/README.md`). This SPEC is the mechanical HOW for US-000.BOLT-011; the
location inventory (§4) was built by multiline grep of the current tree.

---

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | `devflow/functional/bolts/US-000.BOLT-011-kit-self-containment.md` | HITL-BOLT-READY-Approval ✓ 2026-08-23T00:51:05 |
| Origin REV | `devflow/reviews/REV-004-kit-self-containment-consistency-audit.md` | HITL-REV-Approval ✓ 2026-08-23T00:44:14 |
| Container | `devflow/functional/user-stories/US-000-non-functional.md` | no approval lifecycle ✓ |
| ADR | `devflow/adrs/ADR-004-repository-partition-v2.md` | HITL-ADR-Approval ✓ (accepted) |
| Repository baseline | current working tree on branch `5.0` | — |

Pre-SPEC evidence gate: **all governed sources approved** — no draft input.
The edited files are product files in `distribution-kit/`; their exact current
texts are captured in §4.

---

## 4. Scope — exact location inventory

All paths relative to `distribution-kit/`.

### Phase A — `US-015` → version-neutral phrasing (10 files, 29 occurrences)

| File | Line(s) | Context | Replacement direction |
|------|---------|---------|-----------------------|
| `devflow/avenga-devflow/Avenga-DevFlow.md` | 1743 | coverage note "(a redesigned model is planned, US-015)" | "(a redesigned model is planned for a future version)" |
| `devflow/avenga-devflow/Avenga-DevFlow.md` | 2815 | §3.11 release note "(US-015)" | "(planned for a future version)" |
| `devflow/avenga-devflow/Avenga-DevFlow.md` | 3924 | §4.7 "(US-015)" | same |
| `devflow/GUARDRAILS.md` | 96 | G20 response "…is planned, US-015)" | same |
| `devflow/GUARDRAILS.md` | 377 | coverage section "(a redesigned model is planned, US-015)" | same |
| `devflow/README.md` | 63 | folder map "uat/ UAT minutes — dormant/reserved (US-015)" | "dormant/reserved" |
| `devflow/README.md` | 352 | Known Limitations row "Where it is governed \| US-015, §4.6" | "§4.6 (redesigned model planned for a future version)" |
| `devflow/tests/README.md` | 27, 33, 60, 72 | "(US-015)" in structure/table/flow/traceability | "(dormant/reserved — the UAT approval layer was removed in v4.2)" |
| `devflow/tests/uat/README.md` | 10 | dormant note "(US-015)" | "(planned for a future version)" |
| `devflow/tests/uat/INDEX.md` | 8 | "(US-015)" | same |
| `devflow/tests/uat/TEMPLATE-UAT.md` | 28 | dormant banner "(US-015)" | same |
| `devflow/analysis/README.md` | 46, 87, 265 | "(US-015)" in notes/flow/relation table | same |
| `devflow/ONBOARDING.md` | 74 | glossary UAT row "(US-015)" | same |
| `devflow/reports/TEMPLATE-REPORT.html` | 426, 468, 630-631, 744, 1067, 1242-1243, 1305, 1770, 1795 | sample data `US-011`/`US-015` | neutral sample IDs `US-101`/`US-102` (ID tokens only; the surrounding sample prose and the "Shared Objective Detection / Synergies" title stay) |

Rule: the replacement never removes the informative part of the sentence
("removed in v4.2", "dormant/reserved", "redesigned model planned") — only the
`US-015` token and, where needed, the sentence glue.

### Phase B — `ADR-010` citations dropped (methodology, 6 occurrences)

| Line | Current text (excerpt) | Replacement |
|------|------------------------|-------------|
| 1602 | "**Canonical identity — the actor grammar (ADR-010):**" | "**Canonical identity — the actor grammar (§3.0):**" |
| 3188 | "records only `human:<user>` actors (AITL, §3.0/ADR-010)." | "records only `human:<user>` actors (AITL, §3.0)." |
| 3272 | "It is prefix-mandatory in the actor grammar (§3.0, ADR-010)." | "It is prefix-mandatory in the actor grammar (§3.0)." |
| 3279 | "(`null` when it did not — a human-operated run, ADR-010 §3.4)." | "(`null` when it did not — a human-operated run)." |
| 4698 | "the actor grammar (§3.0, ADR-010 §3.1–§3.4)." | "the actor grammar (§3.0)." |
| 4700 | "(`HITL-<CODE>-Approval` → `AITL-<CODE>-Approval`, ADR-010 §3.6–§3.7)" | "(`HITL-<CODE>-Approval` → `AITL-<CODE>-Approval`)" |

Rule: remove only the `ADR-010` token (and its section pointers); keep every
other word. The §3.0 actor-grammar content is authoritative on its own.

### Phase C — dangling CHANGELOG / tools references (`devflow/README.md`)

| Line | Current | Replacement |
|------|---------|-------------|
| 354 | Known Limitations "Monetary cost" row, "Where it is governed" = `CHANGELOG 4.0 "cross-model review round"` | "§3.12 — `runs[]` keeps the token model; cost stays computable retroactively" |
| 355 | "Validation tooling" row, "Where it is governed" = `…, §5.1, tools/README.md` | "…, §5.1 — tools track (arrives with `devflow/bin/`, §5.1)" |

Rule: no new promises; the rows still describe the limitation and where it is
governed — only the unshipped referents are replaced.

---

## 5. Prerequisites and baseline

- Baseline: current working tree on branch `5.0`; `distribution-kit/`
  untouched since REV-002/REV-003/REV-004 verification (grep evidence in
  REV-004 §4).
- No prior SPEC dependency.

---

## 6. Phases

### Phase A — `US-015` sweep (10 files, 29 occurrences)

Apply the Phase A table edits. After the sweep, re-grep `US-015` across
`distribution-kit/` — the result must be **zero** occurrences, with no file
left unedited (the count at each file is part of the evidence).

**Files created:** none.

**Files modified:**
- `devflow/avenga-devflow/Avenga-DevFlow.md` (3 edits)
- `devflow/GUARDRAILS.md` (2 edits)
- `devflow/README.md` (2 edits)
- `devflow/tests/README.md` (4 edits)
- `devflow/tests/uat/README.md` (1 edit)
- `devflow/tests/uat/INDEX.md` (1 edit)
- `devflow/tests/uat/TEMPLATE-UAT.md` (1 edit)
- `devflow/analysis/README.md` (3 edits)
- `devflow/ONBOARDING.md` (1 edit)
- `devflow/reports/TEMPLATE-REPORT.html` (11 ID tokens — US-011→US-101, US-015→US-102)

### Phase B — `ADR-010` citation removal (methodology, 6 edits)

Apply the Phase B table edits. The actor grammar's normative text (§3.0
actor-grammar paragraph) is **not** touched; only the `ADR-010` tokens and
section pointers are removed. Re-grep `ADR-010` across `distribution-kit/` —
result must be **zero** (the root `devflow/` is out of scope; its own
ADR-010 document is untouched).

**Files modified:** `devflow/avenga-devflow/Avenga-DevFlow.md` (6 edits).

### Phase C — dangling references (`devflow/README.md`, 2 edits)

Apply the Phase C table edits. Re-grep for `CHANGELOG 4.0` (must be zero in
`distribution-kit/`) and for `tools/README.md` (must be zero, or the only
remaining mention is an explicit forward reference — the Phase C replacements
achieve zero).

**Files modified:** `devflow/README.md` (2 edits).

---

## 7. Acceptance criteria

- **AC-1:** `US-015` absent from `distribution-kit/` (grep = 0).
- **AC-2:** `ADR-010` absent from `distribution-kit/` (grep = 0); the actor
  grammar text in §3.0 is byte-identical except the citation tokens.
- **AC-3:** `CHANGELOG 4.0` absent from `distribution-kit/` (grep = 0).
- **AC-4:** `tools/README.md` absent from `distribution-kit/` (grep = 0).
- **AC-5:** every UAT/dormant note still present and informative (no sentence
  lost, only the ID token replaced).
- **AC-6:** G-count = 39 in GUARDRAILS and each of the four agents (39×5).
- **AC-7:** four-agent body parity unchanged (2 sanctioned diff lines per
  pair).
- **AC-8:** `git status` shows only `distribution-kit/` edits + root
  governance records (kit-only, ADR-004).
- **AC-9:** `TEMPLATE-REPORT.html` renders unchanged structurally (ID tokens
  only) — spot-check the replaced lines.

### AC mapping to source (measurable outcome)

| Source | How this SPEC satisfies it | Verifying test/evidence |
|--------|----------------------------|--------------------------|
| REV-004 F-01 (a) | Phase A removes all `US-015` references | grep `US-015` = 0 |
| REV-004 F-01 (b) | Phase B removes all `ADR-010` citations | grep `ADR-010` = 0 |
| REV-004 F-01 (c) | Phase C removes CHANGELOG/tools dangling refs | grep `CHANGELOG 4.0` = 0, grep `tools/README.md` = 0 |
| Bolt §2 completion criteria | AC-5..AC-9 | presence greps + G-count + parity + git status |

---

## 8. Testing strategy

Documentation product — verification replaces the test suite:

- **Absence sweeps (multiline-aware):** `US-015`, `ADR-010`, `CHANGELOG 4.0`,
  `tools/README.md` — each must return zero across `distribution-kit/`.
- **Presence assertions:** each Phase A/B/C replacement string present at its
  location (diff review).
- **Invariant checks:** G-count 39×5; four-agent body parity (2 lines per
  pair); `git status` kit-only.
- **Edge cases:** the report's sample-data replacements must not alter the
  HTML structure (spot-check the 11 edited lines); the UAT notes must keep
  their informative content.

---

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | n/a — documentation product, no runtime | n/a |
| SAST / SBOM | n/a | n/a |
| Perf-smoke (p95/p99) | n/a | n/a |
| Prompt-injection scan | n/a — no prompts concatenated | n/a |
| Secret-leak scan | pass — no secrets introduced (text-only edits) | pass |
| Hallucination lint | pass — every edited phrase resolves on disk | pass |
| IP / license provenance | n/a — original text only, no new code | n/a |
| PII / DLP | n/a | n/a |
| Dependency-confusion | n/a — no dependencies | n/a |
| Test-first evidence | n/a — documentation-only; absence sweeps are the evidence (§8) | n/a |
| Behavioral reproducibility | pass — re-running the sweep from the SPEC + captured tree reproduces zero | pass |
| Bolt-manifest validation | pass — Bolt manifest validates against `manifest-v4-bolt.schema.json` | pass |

> Each gate ends `pass` / `waived` (ADR-NNN) / `n/a` (with reason) (§3.6).

---

## 10. Security and data

- Text-only edits to distributed documentation; `data_classification: internal`.
- No secrets, no new dependencies, no runtime surface.
- The report sample data contains no real user/PII — ID tokens only.

---

## 11. Monitoring and observability

n/a — documentation product; the "observability" is the absence-sweep and
parity evidence in §8.

---

## 12. Migration, compatibility and rollback

- **Migration:** n/a — no schema, config or runtime change. The edited
  phrases are prose; existing adopter copies (none yet — the kit is
  pre-release) are unaffected.
- **Compatibility:** n/a.
- **Rollback:** per-file git revert of the touched phrases; the canonical
  SPEC revision 1 remains valid for a re-run.

---

## 13. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| Over-broad sweep deletes informative sentence glue with the ID | 2 | 3 | AC-5 presence assertion + diff review |
| `TEMPLATE-REPORT.html` structure broken by ID replacement | 1 | 2 | ID-token-only edits, spot-check |
| `ADR-010` removal leaves the actor grammar under-referenced | 1 | 3 | §3.0 is self-contained; AC-2 diff check |
| Root tree accidentally edited (ADR-004 violation) | 1 | 4 | AC-8 git-status check |

---

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| Drop the `ADR-010` citations instead of shipping an appendix | the actor grammar's normative content is already fully written in §3.0; an appendix would duplicate normative text (drift risk). Maintainer confirmation requested at SPEC review; appendix is the fallback if changes are requested |
| Neutral sample IDs `US-101`/`US-102` in the report | 3-digit pattern preserved, no collision with this repo's real IDs |
| UAT notes keep "removed in v4.2 / dormant / redesigned model planned" without the ID | the information is the point; the ID is the leak |

---

## 15. Stop conditions

- Any Phase A/B/C edit that would change a rule, checkpoint, guardrail or
  schema → stop, revise the Bolt/SPEC, re-approve (G15).
- `US-015`/`ADR-010`/`CHANGELOG 4.0`/`tools/README.md` residue found in a file
  NOT listed in §4 → stop; extend the inventory, revise the SPEC, re-approve.
- An unexpected reference to `ADR-010` in the root `devflow/` being pulled
  into the edit → stop (out of scope, ADR-004).

---

## 16. Definition of Done (DoD)

- [ ] All Phase A/B/C edits applied
- [ ] AC-1..AC-9 verified (greps at zero, presence, G-count, parity, git status)
- [ ] `US-000.BOLT-011` manifest valid (`manifest-v4-bolt.schema.json`)
- [ ] MEM created in `devflow/memory/` (exactly one per V-Bounce)
- [ ] Manifest `v_bounces[]` entry appended in `devflow/metrics/bolts/`
- [ ] HITL-MEM-Approval recorded

---

## 17. References

- `devflow/reviews/REV-004-kit-self-containment-consistency-audit.md` (F-01)
- `devflow/functional/bolts/US-000.BOLT-011-kit-self-containment.md`
- `devflow/adrs/ADR-004-repository-partition-v2.md`

---

## 18. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-23 | eugenio.serrano | Initial draft (revision 1) |
| 2026-08-23 | eugenio.serrano | `HITL-SPEC-Approval` recorded (approved) — ADR-010 drop mechanism confirmed; V-Bounce authorized |

---

## 19. HITL-SPEC-Approval

> **Avenga DevFlow §2.4.1, §3.0.** This SPEC remains a draft until the
> Dev-validator (+ applicable domain owners) records `HITL-SPEC-Approval`
> (in the `review` frontmatter block). Bolt approval (`HITL-BOLT-READY-Approval`)
> authorizes SPEC preparation; **SPEC approval** authorizes the V-Bounce. A
> material source change invalidates this approval — stop, revise, re-approve
> (G15).

| Field | Value |
|-------|-------|
| **review.reviewers** | eugenio.serrano (dev_validator + tech_lead) |
| **review.decision** | **approved** |
| **review_ready_at** | `2026-08-23T00:51:46-03:00` |
| **review.started_at** | `2026-08-23T00:54:35-03:00` |
| **review.decided_at** | `2026-08-23T00:54:35-03:00` |
| **Findings** | none — `acknowledged_without_comment: true` (see frontmatter); ADR-010 drop mechanism confirmed |
