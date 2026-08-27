---
id: "MEM-260823-1755"
title: "The actors/ family shape — TEMPLATE-ACTOR, roster.schema.yaml, INDEX.md, project-policy, the example and the README (Modelo B) (US-024.BOLT-001)"
date: "2026-08-23"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
bolt: "US-024.BOLT-001"
spec: "devflow/spec/SPEC-260823-1741-actors-family-shape.md"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "45d553f"
applied_adrs:
  - "devflow/adrs/ADR-007-devflow-agent-identity-model.md"
  - "devflow/adrs/ADR-010-actor-grammar-and-pure-v5-vocabulary.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "devflow/metrics/bolts/US-024.BOLT-001-roster-schema-and-validation.json"
diff_ref: ""
review_ready_at: "2026-08-23T17:55:00-03:00"
review: # AITL-MEM-Approval — recorded by the human reviewer (§3.0); decision dictated in conversation ("aprobado punto 1 y 2") and transcribed by the agent
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-23T18:11:00-03:00"
  decided_at: "2026-08-23T18:12:42-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved as Dev-validator: the actors/ family shape (Modelo B) inspected — the six files, the validation runs (example PASS, malformed detected, policy PASS), the self-containment grep (0 hits), kit-only. V-Bounce 1 approved — BOLT-001 Development Completed."
---

# MEM-260823-1755 — The `actors/` family shape (US-024.BOLT-001, V-Bounce 1)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | US-024.BOLT-001 (roster-schema-and-validation) |
| **SPEC**        | [SPEC-260823-1741](../spec/SPEC-260823-1741-actors-family-shape.md) rev 1 |
| **V-Bounce**    | 1 |
| **ADRs**        | ADR-007 (identity), ADR-010 (grammar), ADR-004 (kit-only) |

---

## 1. Executive summary

This V-Bounce delivered the `actors/` family in the **standard DevFlow
family shape** (Modelo B): `TEMPLATE-ACTOR.yaml` (the actor-file template
with every field + the non-negotiable bounds and the
`produces`-derived-from-`role` note), `roster.schema.yaml` (the JSON
Schema that validates an actor file — required fields, kebab-case `id`,
`modes` ⊆ executor/approver, `approves` ⊆ the real checkpoint codes,
`capabilities.tier` ⊆ T0..T3, agents require the `definition` +
`capabilities` block), `INDEX.md` (lists the project's actors with the
family notes: one file per actor, definitions reusable N:1, model
per-instance, produces derived), `project-policy.yaml` (the roster-level
policy: `aitl_enabled_checkpoints` + the `human_only` floor —
[critical, regulatory]), `example.yaml` (the worked example — an agent
actor with a project-chosen name, the `definition` pointer and a
per-instance model), and the README's family-shape section (the six
files, the one-file-per-actor rule, N:1 definitions, per-instance models,
the zero-config invariant). The **verification is GREEN**: all six files
present; the example **validates** against the schema (PASS — the
parser-based check: required fields present, enums ok, agent block ok); a
**malformed actor file fails fast** (missing role/model/modes/approves
detected); the **policy knobs validate** (the human_only floor present);
the **self-containment check** passes (grep over the delivered kit files
for maintenance IDs → **0 hits**); kit-only; no BOM. The validation used
the generator's dependency-free parser (the tool suite remains at
14/14). The deliverables are fully self-contained — an adopter copying
the kit gets a working roster family with no dangling references.

## 2. Implemented phases

### Phase A — The template and the schema

`TEMPLATE-ACTOR.yaml` (every field with guidance comments: id/name/role/
model/modes/approves/definition/capabilities/escalation/write_paths + the
bounds block + the produces-derived note) and `roster.schema.yaml` (JSON
Schema draft 2020-12 in YAML form — validates an actor file; the
`additionalProperties: false` discipline; the grammar forms; the
allOf-if definition → requires capabilities).

### Phase B — The INDEX, the policy and the example

`INDEX.md` (the actor table with the example row + the family notes),
`project-policy.yaml` (the two knobs), `example.yaml` (the worked
example — id `example-qa`, name "Example QA", role qa, model inherit,
modes [executor, approver], approves [MEM], definition pointer, tier T1).

### Phase C — The README + verification (GREEN)

The README gained the family-shape section (the six files + the rules)
and the updated "What lives here". Verification ran: presence ×6,
example validation (PASS), malformed fail-fast (PASS), policy validation
(PASS), self-containment grep (0 hits), kit-only, no BOM.

## 3. Files created

| File | Purpose |
|------|---------|
| `distribution-kit/devflow/actors/TEMPLATE-ACTOR.yaml` | The actor-file template — every field with guidance + the non-negotiable bounds + the produces-derived-from-role note |
| `distribution-kit/devflow/actors/roster.schema.yaml` | The validation schema for an actor file (JSON Schema, fail-fast discipline, the grammar forms) |
| `distribution-kit/devflow/actors/INDEX.md` | Lists the project's actors + the family notes (one file per actor, N:1 definitions, per-instance models) |
| `distribution-kit/devflow/actors/project-policy.yaml` | The roster-level policy knobs (`aitl_enabled_checkpoints` + the `human_only` floor) |
| `distribution-kit/devflow/actors/example.yaml` | The worked example actor file (validates, demonstrates the definition pointer + per-instance model) |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `distribution-kit/devflow/actors/README.md` | The family-shape section (the six files + the rules) + the updated "What lives here" (the old roster.example references removed) |

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
| — | — | — |

## 6. Files deleted

| File | Reason |
|------|--------|
| — | — (the README kept its US-022 content; no old roster files existed) |

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| `roster.schema.yaml` keeps its name (validates an actor file) | The approved US-024 AC-1 names it so; renaming would re-open the US (a conscious no-op per the review's optional #3) |
| `project-policy.yaml` as the roster-level policy file | `project_policy` is team-level, not per-actor |
| The schema uses JSON Schema draft 2020-12 in YAML | The validator tooling (US-012) is JSON-Schema-based; YAML form keeps it human-readable |
| The example is an agent actor (qa) with the definition pointer | Demonstrates the agent block + the N:1 + per-instance model; validates against the schema |
| The validation evidence uses the generator's dependency-free parser | No new tooling needed; the same parser discipline as the agents family |

## 8. Deviations and assumptions

No deviations from SPEC-260823-1741 rev 1. Assumption: the validator
tooling (US-012 family) will consume `roster.schema.yaml` as-is when it
lands; the fail-fast check here used a scripted required-field/enum
check.

## 9. Verification evidence

### Presence (RED → GREEN)

```
RED:   actors/ holds only README.md
GREEN: TEMPLATE-ACTOR.yaml · roster.schema.yaml · INDEX.md ·
       project-policy.yaml · example.yaml · README.md — all PRESENT
```

### Validation (scripted, parser-based)

```
EXAMPLE VALIDATION: PASS (required fields present; modes/approves/tier
                     enums ok; agent block ok — definition + capabilities)
MALFORMED DETECTED: PASS (a file with only id/name → missing
                     role/model/modes/approves detected — fail fast)
POLICY VALIDATION:  PASS (aitl_enabled_checkpoints + human_only floor
                     [critical, regulatory])
```

### Self-containment (the review's explicit check)

```
grep -E "US-[0-9]{3}|ADR-[0-9]{3}|DISC-[0-9]{3}|BOLT-[0-9]|SPEC-26|MEM-26|
REV-[0-9]{3}|TC-[0-9]{3}" over distribution-kit/devflow/actors/* →
0 hits — SELF-CONTAINED PASS
```

### Invariants

```
Kit-only (ADR-004): only distribution-kit/ changes (the actors/ family +
the previously delivered agents/ family)        PASS
Encoding: 0 files with BOM                       PASS
```

### Gates

Documentation + schema Bolt: runtime gates `n/a`; prompt-injection/
secret-leak `pass`; hallucination-lint `pass` (the §3.0.1 anchors
resolve); behavioral-reproducibility `pass` (the validation runs
reproduce); bolt-manifest-validation `pass` (v_bounces[1] appended, JSON
valid).

## 10. Manual interventions

None — the agent produced everything.

## 11. Evidence links

- **Diff / PR:** none (working tree, uncommitted)
- **Commit:** baseline `45d553f`
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-024.BOLT-001-roster-schema-and-validation.json`

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~15min |
| V-Bounce number | 1 |
| Tests created | 0 new (the tool suite stays 14/14; the validation checks are scripted evidence) |
| AI-generated code | 100% |
| First-pass approval | pending (this MEM) |

## 13. Pending items and stubs

- [ ] BOLT-002 V-Bounce (the AITL-enable ADR template + the resolution
      rules in the README)
- [ ] BOLT-003 V-Bounce (the human-roster guarantees + the US-001 record
      closure)
- [ ] The validator tooling (US-012 family) will consume the schema

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
| **review_ready_at** | `2026-08-23T17:55:00-03:00` |
| **review.started_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **review.decided_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **Review evidence** | diff of the six files; the validation runs (example PASS, malformed detected, policy PASS); the self-containment grep (0 hits); kit-only; encoding; MEM, manifest |
| **Comments** | |
| **Findings** | |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | evidence inspected per the review-evidence column |
