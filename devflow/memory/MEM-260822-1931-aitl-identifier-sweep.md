---
id: "MEM-260822-1931"
title: "Kit-wide HITL→AITL sweep — adjective + ~1,155 identifiers → AITL (US-021.BOLT-004)"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
bolt: "US-021.BOLT-004"
spec: "SPEC-260822-1916"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "97125e7"
applied_adrs:
  - "devflow/adrs/ADR-008-aitl-approval-precept.md"
  - "devflow/adrs/ADR-005-removal-completeness-phrase-family-sweep.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "US-021.BOLT-004-aitl-identifier-sweep.json"
diff_ref: ""
review_ready_at: "2026-08-22T19:31:13-03:00"
review: # HITL-MEM-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "dev_validator"}]
  started_at: "2026-08-22T19:33:47-03:00"
  decided_at: "2026-08-22T19:33:47-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Inspected the kit-wide diff (~69 files), the ADR-005 absence sweep (empty outside allowlist), the allowlist-intact checks, the G36 validation (migrated HITL-* still GREEN), G-count 39x5, four-agent sync, kit-only. The final HITL->AITL rename is complete and history-safe. V-Bounce GREEN."
---

<!--
  LANGUAGE POLICY (§3.15): schema/headings English; prose content_language (en).
  Kit-only product surface (ADR-004); root governance records stay 4.2.
  This MEM's OWN checkpoints are HITL-* (dogfooding split, ADR-008 §3.1): we build
  the AITL kit using the v4.2 operating methodology.
-->

# MEM-260822-1931 — kit-wide HITL→AITL sweep (US-021.BOLT-004)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | [US-021.BOLT-004](../functional/bolts/US-021.BOLT-004-aitl-identifier-sweep.md) |
| **SPEC**        | [SPEC-260822-1916](../spec/SPEC-260822-1916-aitl-identifier-sweep.md) revision 1 |
| **V-Bounce**    | 1 |
| **ADRs**        | ADR-008 (§3.1 rename), ADR-005 (phrase-family sweep), ADR-004 (kit-only) |

---

## 1. Executive summary

This V-Bounce performed the final, comprehensive rename that completes US-021: the
pervasive `HITL` **adjective** (category 2) and **every `HITL-<CODE>-Approval`
identifier** (category 3) → **AITL**, across the whole kit, under the ADR-005
phrase-family discipline with a declared allowlist. The result is GREEN and, most
importantly, **proven as an absence**: a definitive kit-wide grep for `HITL` minus
the allowlist (`HITL-*` legacy, `hitl_approvals`, the `Human-in-the-Loop (HITL)`
definition) returns **empty** — no `HITL` checkpoint identifier or concept-adjective
remains outside the intended history/legacy references. History is preserved (G36):
the manifest schema still lists `HITL-*` and a migrated `HITL-US-Approval` entry
still validates GREEN. The guardrail count is unchanged (**39×5**), the four agents
stay byte-identical in their shared regions, and the change is kit-only (root
untouched; the schema `.json` files were deliberately excluded to keep their `HITL-*`
history-support enums). With this, **US-021 is delivered and the v5.0 kit is fully
AITL** — concept (BOLT-001), guardrails (BOLT-002), schema (BOLT-003) and now every
identifier + adjective (BOLT-004).

The ADR-005 discipline earned its keep again: the strict `…-Approval` regex of the
first pass missed **compound/slash/brace forms** (`HITL-US/BUG/TC/DISC/REV/AREV-…`,
`HITL-DISC/REV/AREV-*-Approval`, `HITL-BOLT-DONE`, `HITL-AREV-{CRITIQUE,…}`), and my
over-broad `(?<!\()` guard skipped a handful of parenthetical adjectives
(`(HITL stops`, `(HITL, periodic)`, `HITL-approved`); the absence sweep surfaced
every one, and a follow-up pass + targeted fixes cleared them. A broken anchor from
BOLT-001's heading rename was also fixed.

---

## 2. Implemented phases

### Phase A/B — the sweep (cat 3 identifiers + cat 2 adjective)
An EOL-preserving, allowlist-aware script over every `.md` under
`distribution-kit/` + the five `TEMPLATE-MANIFEST-*.json` example values:
- **cat 3:** `HITL-<CODE>-Approval` → `AITL-<CODE>-Approval` (full identifiers) +
  `HITL-<` placeholders → `AITL-<`.
- **cat 2:** standalone `HITL` concept-shorthand → `AITL`, skipping any line carrying
  an allowlist marker (`HITL-*`, `hitl_approvals`, `Human-in-the-Loop`).
- First pass: 66 files, 1,136 identifiers + 19 placeholders + 167 adjectives.

### Phase A′ — completeness follow-ups (ADR-005 absence caught these)
- **Compound/slash/brace forms** the strict regex missed → a `HITL-[A-Z]` → `AITL-`
  pass (7 files, 19 renames): the One-Path flow list, the conditional
  `AITL-DISC/REV/AREV-*-Approval` row, the `AITL-BOLT-DONE ROUTING` heading, the
  README compact list, `AITL-AREV-{…}`, and mixed template rows.
- **Parenthetical adjectives** skipped by the `(?<!\()` guard, + a `HITL-`+lowercase
  case: `(AITL stops…)` (README, ONBOARDING), `(AITL, periodic)` and
  `AITL-approved SPEC` (Avenga-DevFlow.md), `(AITL checkpoints…)` (reviews/README) —
  5 targeted fixes.
- **Broken anchor** from BOLT-001's heading rename: README
  `#hitl-checkpoints-human-in-the-loop` → `#checkpoints-actor-in-the-loop--aitl`.
- The ONBOARDING intro precept `(HITL)` → `(AITL — an actor, human by default)`.

---

## 3. Files created / 5. renamed / 6. deleted

_(none — content rename only; the sweep scripts ran from the OS temp scratchpad, W21)_

---

## 4. Files modified

Kit product surface — **~69 files** under `distribution-kit/`: the core methodology
(`Avenga-DevFlow.md`), `GUARDRAILS.md`, `ONBOARDING.md`, `README.md`, `AGENTS.md`,
the four platform agents, and every folder `README`/`TEMPLATE-*` that referenced a
checkpoint, plus the five `TEMPLATE-MANIFEST-*.json` example values. Governance
records (root, 4.2): `spec/SPEC-260822-1916*`,
`metrics/bolts/US-021.BOLT-004*.json`, this MEM.
**Not touched (allowlist):** the three `manifest-v5-*.schema.json` (keep `HITL-*`
history enums), the §5.16 migration recipe, G05/G18/G24, the agents' Upgrade-Protocol
notes, and the `Human-in-the-Loop (HITL)` definition.

---

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| One comprehensive sweep (cat 2 + cat 3), verified as an absence | ADR-005 — the discipline that had already caught three US-020 misses; it caught this Bolt's compound/adjective misses too |
| Allowlist by file / rule / section / sentence | `HITL-*` legacy, the schema enums, G05/G18/G24, the §5.16 recipe, and the `Human-in-the-Loop (HITL)` definition must remain (history/G36) |
| Rename the TEMPLATE-MANIFEST JSON examples to `AITL-*` | Adopters copy them; they should show the new canonical vocabulary (schema accepts both) |
| Keep the schema `.json` `HITL-*` enums | BOLT-003 — history support; a migrated `HITL-*` manifest must still validate (verified) |
| Follow-up `HITL-[A-Z]` pass for compound forms | The strict `…-Approval` regex cannot match `HITL-US/BUG/…` or `HITL-AREV-{…}`; `HITL-[A-Z]` is safe (no allowlisted `HITL-<uppercase>` exists) |

---

## 8. Deviations and assumptions

- **Two-pass execution + targeted fixes**, all within this V-Bounce and turn budget
  (15): the first pass under-matched compound/parenthetical forms; the ADR-005
  absence assertion surfaced them and they were cleared before GREEN. No SPEC
  revision needed.
- **Root manifests untouched:** the repo's own governance manifests are
  root-partition (v4.0, `hitl_approvals`, `HITL-*`) and out of scope (ADR-004); they
  migrate when the root moves to v5.0.

---

## 9. Verification evidence

### ADR-005 absence sweep — GREEN (as an absence)
```
Definitive: grep 'HITL' over distribution-kit/**/*.md  MINUS allowlist
  (HITL-*  |  hitl_approvals  |  Human-in-the-Loop (HITL))  =>  EMPTY
Full identifiers HITL-<CODE>-Approval (.md + TEMPLATE-MANIFEST json): 0
Compound/any HITL-[A-Z]: 0 · HITL- non-*/non-<: 0 · lowercase hitl (excl hitl_approvals): 0
Standalone HITL outside allowlist: 0
```

### AC-4 allowlist intact
```
Human-in-the-Loop (HITL) definition: 1 (preserved)
HITL-* legacy refs: 41 (preserved — G05 + §5.16 + history mentions)
hitl_approvals (v4-source, agents' upgrade notes + §5.16): 6 (preserved)
manifest-v5-*.schema.json: not in this V-Bounce's diff (HITL-* enums intact)
```

### AC-5 G36 — history still validates
```
migrated HITL-US-Approval entry vs manifest-v5-bolt.schema.json: GREEN
```

### AC-6 count + sync
```
G-count: GUARDRAILS 39 · CLAUDE 39 · SKILL 39 · AvengaDevFlow.agent 39 · AvengaDevFlow 39 (39×5)
four agents: "# AITL -- ACTOR-IN-THE-LOOP" 4/4 · "AITL-SPEC-Approval" 4/4 · compound lines 1× (byte-identical)
```

### AC-7 kit-only
```
git status: only distribution-kit/ + root governance records (spec/memory/metrics/functional). Root framework untouched.
```

### Gates
- unit/integration, SAST/DAST/SBOM, perf, IP, PII, dep-confusion, test-first: **n/a**.
- hallucination-lint (broken anchor fixed; refs resolve), behavioral-reproducibility
  (deterministic sweep), bolt-manifest-validation: **pass**.

### BUG V-Bounce evidence
n/a.

---

## 10. Manual interventions

None on production content beyond the agent-run sweep + agent-authored follow-up
fixes. The human role was HITL-SPEC-Approval and (pending) HITL-MEM-Approval.

---

## 11. Evidence links

- **Diff / PR:** none yet (uncommitted; 5.0 branch — the whole US-021 + US-020 tree).
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-021.BOLT-004-aitl-identifier-sweep.json`.

---

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~2.5h (sweep + two follow-up passes + verification) |
| V-Bounce number | 1 |
| Tests created | ADR-005 absence sweep (multi-pattern) + G36 schema validation + four-agent sync + G-count |
| AI-generated code | 100% (sweep scripts + fixes); no human fallback |
| First-pass approval | pending (this MEM) |

---

## 13. Pending items and stubs

- [ ] On acceptance → **US-021 delivered**: the v5.0 kit is fully AITL (concept +
      guardrails + schema + every identifier/adjective).
- [ ] (Later USs, ADR-008 §3.9) enabling virtual approvers (per-project config), the
      `agents/` registry + Coordinator + roster, and the pilot.

---

## 14. HITL-MEM-Approval

> **Avenga DevFlow §2.12, §3.0.** Created by the agent, no mutable status,
> **never self-approved**. The executing Dev-validator inspects the diff, the
> ADR-005 absence evidence, the G36 validation, this MEM and the manifest, and
> records `HITL-MEM-Approval` here and in the manifest's `hitl_approvals[]`.

| Field | Value |
|-------|-------|
| **Reviewers (executing Dev-validator; QA/Sec/domain optional)** | eugenio.serrano |
| **Roles** | dev_validator |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-22T19:31:13-03:00` |
| **review.started_at** | `2026-08-22T19:33:47-03:00` |
| **review.decided_at** | `2026-08-22T19:33:47-03:00` |
| **Review evidence** | Kit-wide diff (~69 files), ADR-005 absence sweep (empty), allowlist intact, G36 validation GREEN, G-count 39×5, four-agent sync, kit-only, manifest |
| **Comments** | Approved; the kit is fully AITL |
| **Findings** | none |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | Evidence inspected as above; V-Bounce GREEN |
