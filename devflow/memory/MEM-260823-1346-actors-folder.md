---
id: "MEM-260823-1346"
title: "actors/ folder — the roster home with its explanatory README (US-022.BOLT-002)"
date: "2026-08-23"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
bolt: "US-022.BOLT-002"
spec: "devflow/spec/SPEC-260823-1336-actors-folder.md"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "45d553f"
applied_adrs:
  - "devflow/adrs/ADR-007-devflow-agent-identity-model.md"
  - "devflow/adrs/ADR-008-aitl-approval-precept.md"
  - "devflow/adrs/ADR-010-actor-grammar-and-pure-v5-vocabulary.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "devflow/metrics/bolts/US-022.BOLT-002-actors-folder.json"
diff_ref: ""
review_ready_at: "2026-08-23T13:46:00-03:00"
review: # AITL-MEM-Approval — recorded by the human reviewer (§3.0); decision dictated in conversation and transcribed by the agent
  decision: "changes_requested"
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-23T15:32:00-03:00"
  decided_at: "2026-08-23T15:33:05-03:00"
  findings:
    - "Stale documentation: this MEM describes the README as delivered at 13:46 (approver-centric, 'Files modified: none'), but the README was later reframed to the producer + approver concept with the new canonical mermaid (~14:07, as part of the propagation). The documented output no longer matches the delivered artifact."
  acknowledged_without_comment: false
  acknowledgment_reason: "changes_requested — superseded by V-Bounce 2 (the new MEM documents the delivered README). Recorded to complete the review contract (G17/§3.3); the MEM narrative stays immutable."
---

# MEM-260823-1346 — The `actors/` folder and its README (US-022.BOLT-002, V-Bounce 1)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | US-022.BOLT-002 (actors-folder) |
| **SPEC**        | [SPEC-260823-1336](../spec/SPEC-260823-1336-actors-folder.md) rev 1 |
| **V-Bounce**    | 1 |
| **ADRs**        | ADR-007 (identity), ADR-008 (precept), ADR-010 (grammar), ADR-004 (kit-only) |

---

## 1. Executive summary

This V-Bounce created the kit's `devflow/actors/` folder — the **roster
home** (G30-sanctioned by US-022, ADR-007 §3.5/§4 delegating the layout to
the US) — with a README that teaches the Actor concept to anyone who lands
there. The README opens with the mandatory **first-line disambiguation**
(`actors/` = who is in the team / roster home; `agents/` = the AI-member
definitions), explains the Actor concept in plain terms (definition,
grammar, independence layers), embeds the canonical mermaid exactly as it
lives in §3.0.1 (no forked diagram — BOLT-001's canonical home, US-022 rule
#6), states the grammar in one glance (`human:<user>` / `agent:<id>`), and
announces what will land here with US-024 (the roster schema + example and
the AITL-enable ADR template). Every definition sentence carries a pointer
to the normative §3.0.1 section — the README is explanatory only, never a
second source of truth (G28 discipline, US-022 rule #6). The zero-config
invariant is restated: with no roster — or no `agents:` section — every
checkpoint resolves to a human (pure HITL). Verification is GREEN: file
present, disambiguation present, pointer present, mermaid embedded, no
independent normative claims, and `git status` confirms kit-only changes.
No surprises or deviations from the approved SPEC.

## 2. Implemented phases

### Phase A — The folder and the README

Created `distribution-kit/devflow/actors/README.md` (the folder comes into
existence with the file). The README's structure follows the SPEC's
requirements: (1) first-line disambiguation via a blockquote that contrasts
`actors/` vs `agents/` and explains the human-row-without-file vs
agent-row-plus-definition distinction; (2) "What is an Actor?" — the
concept taught in plain language with the pointer to the normative §3.0.1
(the only authority); (3) the canonical mermaid embedded verbatim from
§3.0.1; (4) a grammar table (human → `human:<user>` / model `null`; agent →
`agent:<id>` / declared model); (5) "What lives here" — the US-024 items
(roster schema + example, AITL-enable ADR template); (6) the zero-config
invariant closing note.

### Phase B — Verification (GREEN)

Checked: file present; first-line disambiguation present; §3.0.1 pointer
present; mermaid (`flowchart TB`) present; pointer-style read confirmed
(no sentence asserts a definition without pointing to the normative
section — 4 pointer sentences found); `git status` shows only the kit's
modified methodology file (V-Bounce 1) and the new `actors/` folder
(kit-only, ADR-004).

## 3. Files created

| File | Purpose |
|------|---------|
| `distribution-kit/devflow/actors/README.md` | The roster-home folder's explanatory README: teaches the Actor concept, disambiguates `actors/` vs `agents/` on its first line, points to the normative §3.0.1, embeds the canonical mermaid, and announces the US-024 roster items |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| — | none (the V-Bounce 1 methodology edit is from the prior Bolt) |

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
| README opens with the blockquote disambiguation | US-022 AC-8 requires the first line to disambiguate `actors/` vs `agents/` — the two similar names are the family's main confusion point |
| The mermaid is embedded verbatim from §3.0.1 | US-022 AC-9 / rule #6: canonical home in the methodology; the README references/embeds, never forks |
| Every definition sentence points to §3.0.1 | The README is explanatory (G28 discipline) — the normative text has a single home in Avenga-DevFlow.md |
| US-024 items announced as "lands with US-024" | The folder is the roster home but the schema/example/template are US-024's scope — the README states the intent without pre-empting it |
| Zero-config invariant restated at the end | The safe-default (ADR-008 §3.2) is the concept's anchor — a reader must leave with it |

## 8. Deviations and assumptions

No deviations from SPEC-260823-1336 rev 1. Assumption: writing the README
file creates the folder (standard filesystem behavior); no placeholder
files added — the folder will hold the US-024 artifacts.

## 9. Verification evidence

### Presence (RED → GREEN)

```
RED:   distribution-kit/devflow/actors/          → ABSENT
       distribution-kit/devflow/actors/README.md → ABSENT
GREEN: README.md                                  → PRESENT
       first-line disambiguation ("Not `agents/`") → PRESENT
       §3.0.1 pointer                             → PRESENT
       mermaid (flowchart TB)                     → PRESENT
```

### Content discipline (US-022 AC-9 / rule #6)

```
Pointer-style read: 4 pointer sentences found; no definition sentence
asserts authority without pointing to the normative §3.0.1. PASS
```

### Kit-only (ADR-004)

```
git status -- distribution-kit:
  M distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md  (V-Bounce 1)
  ?? distribution-kit/devflow/actors/                          (this V-Bounce)
No root devflow/ changes. PASS
```

### Gates

Documentation Bolt: unit/integration, SAST/SBOM, perf, IP, PII,
dep-confusion, test-first → `n/a` (no runtime, no dependencies, no personal
data). prompt-injection, secret-leak → `pass` (no runtime surface).
hallucination-lint → `pass` (the §3.0.1 pointer resolves — BOLT-001
prerequisite delivered). behavioral-reproducibility → `pass` (deterministic
checks). bolt-manifest-validation → `pass` (manifest updated, JSON valid).

## 10. Manual interventions

None — the agent produced everything.

## 11. Evidence links

- **Diff / PR:** none (working tree, uncommitted)
- **Commit:** baseline `45d553f`
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-022.BOLT-002-actors-folder.json`

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~5min |
| V-Bounce number | 1 |
| Tests created | 0 (documentation Bolt — deterministic presence/invariant checks instead) |
| AI-generated code | 100% |
| First-pass approval | pending (this MEM) |

## 13. Pending items and stubs

- [ ] BOLT-003 V-Bounce (vocabulary + four agents + the sweep — the sweep's
      location set includes this README)
- [ ] US-024 V-Bounces (the roster schema + example and the AITL-enable ADR
      template land in this folder)

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
| **review_ready_at** | `2026-08-23T13:46:00-03:00` |
| **review.started_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **review.decided_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **Review evidence** | diff of the new README, presence checks, content-discipline read, kit-only status, MEM, manifest |
| **Comments** | |
| **Findings** | |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | evidence inspected per the review-evidence column |
