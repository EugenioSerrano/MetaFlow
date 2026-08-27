---
id: "MEM-260824-0125"
title: "The examples expansion — human actor + agent actor + illustrative roster, and the model-agent-required schema fix (US-024.BOLT-004, V-Bounce 2)"
date: "2026-08-24"
author: "eugenio.serrano"
llm: "claude-fable-5"
bolt: "US-024.BOLT-004"
spec: "devflow/spec/SPEC-260824-0054-roster-as-enablement-reshape.md"
spec_revision: 2
v_bounce: 2
execution_outcome: "ready_for_review"
baseline: "7e3eb5e"
applied_adrs:
  - "devflow/adrs/ADR-014-actors-roster-is-the-enablement.md"
  - "devflow/adrs/ADR-010-actor-grammar-and-pure-v5-vocabulary.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "devflow/metrics/bolts/US-024.BOLT-004-roster-as-enablement-reshape.json"
diff_ref: ""
review_ready_at: "2026-08-24T01:25:21-03:00"
review: # AITL-MEM-Approval — decision dictated in conversation ("aprobado y aceptado que avances") and transcribed by the agent (§3.0)
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-24T10:23:54-03:00"
  decided_at: "2026-08-24T10:23:54-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved as Dev-validator: V-Bounce 2 (SPEC rev 2 — the examples expansion + the model rule) inspected: the three examples on disk with kebab symmetry and cross-referenced ids, the five-case validation demo GREEN (human PASS under the new discriminator — the case rev 1 made impossible), references aligned (README/INDEX/TEMPLATE), self-containment 0 hits. Field-proven besides: the adopter smoke test consumed the three examples and validated the human shape with an independent third-party schema run (REV-005 C-03/F-16 evidence). BOLT-004 Development Completed (V-Bounces 1+2 both approved)."
---

# MEM-260824-0125 — The examples expansion (US-024.BOLT-004, V-Bounce 2)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | US-024.BOLT-004 (roster-as-enablement-reshape) |
| **SPEC**        | [SPEC-260824-0054](../spec/SPEC-260824-0054-roster-as-enablement-reshape.md) **rev 2** (Phases A'/B' — approved 01:21:56) |
| **V-Bounce**    | 2 (V-Bounce 1 delivered rev 1, MEM approved 01:21:56; this V-Bounce runs entirely under rev 2 — G16) |
| **ADRs**        | ADR-014 (the enablement), ADR-010 (the actor grammar the model rule realizes), ADR-004 (kit-only) |

---

## 1. Executive summary

This V-Bounce delivered the maintainer-requested examples expansion of the
`actors/` family and the schema fix the human example surfaced. The
`examples/` folder now holds the **three worked examples** with kebab
symmetry: **`example-human.yaml`** — a human actor ("Arq Juan", architect;
`modes: [executor, approver]`, `approves: [ADR, BOLT-READY]`) with **no
`model` and no `definition`**, realizing the actor grammar (`human:<user>`
→ model null); **`example-agent.yaml`** — the existing DevFlow Agent QA
worked example, renamed for symmetry (git rename, content untouched); and
**`example-roster.yaml`** — a filled team list showing the human + the
agent listed together, with an **explicit illustrative header** stating
that the id-resolves-to-file consistency rule applies to the real
`roster.yaml` only (the reviewer's note, folded in). The **schema fix**:
under rev 1, a human actor file was **impossible** — `model` sat in the
base `required` with `minLength: 1` while the grammar records a human's
model as null; now `model` **leaves the base required set** and is
**agent-required via the discriminator** (`definition` present ⇒ `model`
required): every agent carries `definition` + `model`, every human omits
both. The references were aligned (README family table + the each-actor
paragraph now states "humans omit both"; INDEX lists the three examples;
TEMPLATE-ACTOR marks `model` as agents-only). Verification is GREEN on the
**five validation cases** (human PASS · agent PASS · approver-with-empty-
approves FAIL-FAST · **agent-without-model FAIL-FAST (the new rule)** ·
capabilities-declared PASS — parser-based, dependency-free), the roster
example's ids cross-reference the two actor examples, self-containment 0
hits, no BOM.

## 2. Implemented phases

### Phase A' — The examples expansion

`example.yaml` → `example-agent.yaml` (git mv); `example-human.yaml`
created (the human shape — the header explains why `model`/`definition`
are absent and that humans approve by default); `example-roster.yaml`
created (the illustrative filled list, its header carrying the
copy-and-instantiate warning and the never-self-enabled note on the
agent's row). References updated: `actors/README.md` (family table row +
the each-actor-carries paragraph), `actors/INDEX.md` (the three example
rows + the intro), `TEMPLATE-ACTOR.yaml` (model marked agents-only; the
humans-omit note extended to the model field).

### Phase B' — The model rule

`roster.schema.yaml`: base `required` → `[id, name, role, modes,
approves]` (model out, with the explanatory comment); a second `allOf`
clause added — `definition` present ⇒ `required: [model]` (the agent
discriminator); the `model` property comment marks it agents-only.

### Verification (GREEN)

Shape: `examples/` = exactly the three files. The five-case validation
demo (parser-based — pyyaml unavailable, the family's own precedent):
human PASS, agent PASS, malformed-approver FAIL-FAST, agent-without-model
FAIL-FAST, with-capabilities PASS. The roster example's two ids
cross-reference the two actor examples. Self-containment 0 hits over
`actors/`; no BOM.

## 3. Files created

| File | Purpose |
|------|---------|
| `distribution-kit/devflow/actors/examples/example-human.yaml` | The human-actor worked example — no `model`/`definition`, humans approve by default (`approves: [ADR, BOLT-READY]`) |
| `distribution-kit/devflow/actors/examples/example-roster.yaml` | The filled team list worked example — illustrative header; shows the human + the agent listed, with the never-self-enabled note |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `distribution-kit/devflow/actors/roster.schema.yaml` | `model` out of base `required` (comment explains); the agent discriminator `allOf` added (`definition` ⇒ `model` required); property comments |
| `distribution-kit/devflow/actors/README.md` | Family table (the three examples named); the each-actor paragraph — agents carry `model` + `definition`, humans omit both |
| `distribution-kit/devflow/actors/INDEX.md` | The three example rows + the intro sentence |
| `distribution-kit/devflow/actors/TEMPLATE-ACTOR.yaml` | `model` marked DevFlow-Agent-only; the humans-omit note covers the field and the block |

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
| `actors/examples/example.yaml` | `actors/examples/example-agent.yaml` | Kebab symmetry with the two new examples (the reviewer's naming note) |

## 6. Files deleted

| File | Reason |
|------|--------|
| — | — |

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| The human example approves `[ADR, BOLT-READY]` | A realistic architect grant; role routing stays guidance — the header says so, avoiding a "humans need a grant to approve" misreading |
| `example-roster.yaml` (not `roster.yaml` inside examples/) | Avoids the visual collision with the real `actors/roster.yaml` (the reviewer's note) |
| The roster example's ids are the two actor examples' ids | The three files cross-reference into one coherent worked team — a reader follows the whole model in one sitting |
| The discriminator is `definition`, not `model` | `definition` is the field that MAKES an actor an agent; `model` follows from it — one direction, no circularity |

## 8. Deviations and assumptions

No deviations from SPEC-260824-0054 rev 2. O-2 (`model: inherit`
semantics) remains routed to US-025 — the agent example keeps `inherit`
untouched, no semantics assumed.

## 9. Verification evidence

### Shape (RED → GREEN)

```
RED:   examples/ = example.yaml
GREEN: examples/ = example-agent.yaml · example-human.yaml · example-roster.yaml
```

### Validation (parser-based, dependency-free — five cases)

```
HUMAN (no model/definition):          PASS   (rev-1 schema would have FAILED it)
AGENT (model + definition → squad):   PASS
MALFORMED (approver + empty approves):FAIL-FAST (the v1 rule)
AGENT without model:                  FAIL-FAST (the rev-2 discriminator)
WITH capabilities declared:           PASS   (optional in v1)
```

### Invariants

```
Roster example ids ↔ actor examples: arq-juan + example-qa cross-referenced  PASS
Self-containment (actors/): maintenance IDs + tools/ → 0 hits                PASS
Encoding: no BOM                                                             PASS
Kit-only (ADR-004): only distribution-kit/devflow/actors/** changed          PASS
```

### Gates

Documentation/schema Bolt: unit/integration/perf `n/a` (per the approved
SPEC §9); prompt-injection/secret-leak `pass`; hallucination-lint `pass`
(the cross-references resolve); behavioral-reproducibility `pass`;
bolt-manifest-validation `pass` (v_bounces[2] appended, schema PASS).

## 10. Manual interventions

None — the agent produced everything.

## 11. Evidence links

- **Diff / PR:** none (working tree, uncommitted — part of the v5.1 batch)
- **Commit:** baseline `7e3eb5e`
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-024.BOLT-004-roster-as-enablement-reshape.json`

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~8min |
| V-Bounce number | 2 |
| Tests created | 0 (documentation/schema; the five-case scripted demo per SPEC §8) |
| AI-generated code | 100% |
| First-pass approval | pending (this MEM) |

## 13. Pending items and stubs

- [ ] AITL-BOLT-DONE-Approval for BOLT-004 (V-Bounces 1+2) and BOLT-005.
- [ ] O-2 (`model: inherit`) → US-025; the v2 hardening (capabilities
      return end-to-end) → future US/Bolt.
- [ ] Commit + push of the whole v5.1 batch on the maintainer's order.

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
| **review_ready_at** | `2026-08-24T01:25:21-03:00` |
| **review.started_at** | `2026-08-24T10:23:54-03:00` |
| **review.decided_at** | `2026-08-24T10:23:54-03:00` |
| **Review evidence** | the 2 new examples + the rename; the schema discriminator diff; the README/INDEX/TEMPLATE reference updates; the five-case validation demo; self-containment; MEM, manifest |
| **Comments** | |
| **Findings** | |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | evidence inspected per the review-evidence column |
