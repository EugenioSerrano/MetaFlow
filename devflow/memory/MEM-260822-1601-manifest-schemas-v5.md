---
id: "MEM-260822-1601"
title: "Manifest schemas + templates → v5 (checkpoint_approvals[], actor+mode) — US-020.BOLT-001"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
bolt: "US-020.BOLT-001"
spec: "SPEC-260822-1546"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "97125e7"
applied_adrs:
  - "devflow/adrs/ADR-008-aitl-approval-precept.md"
  - "devflow/adrs/ADR-007-devflow-agent-identity-model.md"
  - "devflow/adrs/ADR-006-versioning-and-self-development-model.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "US-020.BOLT-001-manifest-schemas-v5.json"
diff_ref: ""
review_ready_at: "2026-08-22T16:01:05-03:00"
review: # HITL-MEM-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "dev_validator"}]
  started_at: "2026-08-22T16:03:57-03:00"
  decided_at: "2026-08-22T16:03:57-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Reviewed the diff (3 v5 schemas created, 5 templates → v5, 3 v4 schemas removed) and the §9 validation suite: 3 schemas compile as draft-2020-12, 5 templates GREEN, the virtual-approval sample (agent+model, mode=virtual) GREEN, and 5 negative cases (v4-shaped, mode/actor mismatch, human+model, agent+null-model, extra property) all REJECTED — approval integrity is schema-enforced. Checkpoint enum kept HITL-* (rename is a separate US); kit-only (ADR-004), root untouched, BOLT-001 manifest validates v4.0. Bolt now Development Completed."
---

<!--
  LANGUAGE POLICY (§3.15): schema/headings English; prose content_language (en).
  Documentation/schema V-Bounce (not a BUG) → evidence is deterministic
  JSON-Schema validation. Kit-only edits (ADR-004); root untouched.
-->

# MEM-260822-1601 — Manifest schemas + templates → v5 (US-020.BOLT-001)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | [US-020.BOLT-001](../functional/bolts/US-020.BOLT-001-manifest-schemas-v5.md) |
| **SPEC**        | [SPEC-260822-1546](../spec/SPEC-260822-1546-manifest-schemas-v5.md) — revision 1 |
| **V-Bounce**    | 1 |
| **ADRs**        | ADR-008 (record shape), ADR-007 (actor+model), ADR-006 (version bump), ADR-004 (kit-only) |

---

## 1. Executive summary

This V-Bounce evolves the kit's manifest family from v4.0 to v5.0 — the schema
change that anchors the v5.0 product bump (ADR-006) and gives AITL an auditable
record (ADR-008). The three JSON-Schema files (`manifest-v5-{us,bolt,tc}.schema.json`)
and the five manifest templates now use `checkpoint_approvals[]` (replacing
`hitl_approvals[]`), where every entry carries a `mode` (`human`|`virtual`) and
each approver is an **actor** (`human:<user>` or `agent:<id>`) with its **model**
(null for humans, required for agents) — implementing ADR-007's "actor is the
identity, model is an attribute" at the record level. The transformation was done
programmatically (a deterministic Python pass over the v4 files) to avoid
hand-editing errors, preserving every non-approval structure verbatim
(`additionalProperties:false`, the SPEC→revision / MEM→v_bounce conditionals, the
per-level blocks). Two safety invariants are enforced by the schema itself:
`mode` must be `virtual` iff any approver is an agent, and an agent approver must
carry a non-null model while a human must not. Outcome: all three schemas compile
as valid draft-2020-12, the five templates validate green, a virtual-approval
sample validates green (the AITL path works end-to-end at the schema level), and
five negative cases — a v4-shaped manifest, a mode/actor mismatch, a human with a
model, an agent without a model, and an extra property — are all correctly
rejected. The checkpoint-name enum stays `HITL-*` (the HITL→AITL rename is a
separate US); the field name `checkpoint_approvals` is already neutral. Kit-only
(ADR-004): the root `devflow/` manifests and schemas remain v4.0 under the v4.2
operating methodology.

---

## 2. Implemented phases

### Phase A — Schemas (v4 → v5)
Transformed the three v4 schemas into `manifest-v5-{us,bolt,tc}.schema.json` via a
deterministic Python pass: `$id`/`title` v4→v5; `schema_version` const `"5.0"`;
`hitl_approvals`→`checkpoint_approvals` (property + `required`); `$defs.hitlDecision`
→`checkpointApproval` (+ `$ref` update); added a required `mode` (`human|virtual`);
replaced `$defs.approver` (`{user,role}`) with `{actor,role,model}` where `actor`
matches `^(human|agent):.+` and an `allOf`/`if` makes `model` a non-empty string
for agents and `null` for humans; appended a `mode`/actor consistency `allOf`
(`mode:virtual` iff a `decided_by[]` entry has an `agent:` actor, else
`mode:human`). The bolt schema keeps its SPEC→revision / MEM→v_bounce
conditionals. Removed the three `manifest-v4-*.schema.json`.

### Phase B — Templates (v5 shape)
Transformed the five `TEMPLATE-MANIFEST-*.json`: `schema_version "5.0"`;
`hitl_approvals`→`checkpoint_approvals`; each example entry gained `mode:"human"`
and `decided_by:[{actor:"human:<user>", role, model:null}]`. Example checkpoint
values stay `HITL-*` (rename is a separate US).

### Phase C — Verification (GREEN)
Ran the JSON-Schema validation suite (Python `jsonschema`, draft-2020-12). See §9.

---

## 3. Files created

| File | Purpose |
|------|---------|
| `distribution-kit/devflow/metrics/manifest-v5-us.schema.json` | v5 US-manifest schema (checkpoint_approvals[], actor+mode) |
| `distribution-kit/devflow/metrics/manifest-v5-bolt.schema.json` | v5 Bolt-manifest schema (all 7 checkpoints, SPEC/MEM conditionals kept) |
| `distribution-kit/devflow/metrics/manifest-v5-tc.schema.json` | v5 TC-manifest schema |
| `devflow/memory/MEM-260822-1601-manifest-schemas-v5.md` | This MEM |

---

## 4. Files modified

| File | Change |
|------|--------|
| `distribution-kit/devflow/metrics/TEMPLATE-MANIFEST-US.json` | → v5 shape (checkpoint_approvals[], mode:human, actor+model:null) |
| `distribution-kit/devflow/metrics/TEMPLATE-MANIFEST-BOLT.json` | → v5 shape |
| `distribution-kit/devflow/metrics/TEMPLATE-MANIFEST-BOLT-NONFUNCTIONAL.json` | → v5 shape |
| `distribution-kit/devflow/metrics/TEMPLATE-MANIFEST-BOLT-TEST.json` | → v5 shape |
| `distribution-kit/devflow/metrics/TEMPLATE-MANIFEST-TC.json` | → v5 shape |

---

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
| — | — | The v4 schemas are **deleted** (not renamed) and replaced by new v5 files (§6) |

## 6. Files deleted

| File | Reason |
|------|--------|
| `distribution-kit/devflow/metrics/manifest-v4-us.schema.json` | Replaced by v5 — the kit ships one current schema family per version (§5.16 precedent) |
| `distribution-kit/devflow/metrics/manifest-v4-bolt.schema.json` | Replaced by v5 |
| `distribution-kit/devflow/metrics/manifest-v4-tc.schema.json` | Replaced by v5 |

---

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| Programmatic transform (Python) instead of hand-editing | Precision — reproduces the full v4 structure with only the targeted changes; no typos in ~500-line schemas |
| `actor` string with `human:`/`agent:` prefix (replaces `user`) | Encodes ADR-008's `human:<user>`/`agent:<id>` in one queryable field |
| Schema-enforced `mode`/actor + agent/model conditionals (`if/then/else`) | Approval integrity is structural, not convention — an agent approval cannot be recorded as `human`, and a human cannot carry a model (verified by negative cases §9) |
| Keep the `HITL-*` checkpoint enum | Structure vs names split — the rename is a separate US; `checkpoint_approvals` is already a neutral field name |
| Delete v4 schema files | One current schema family per kit version (matches the v3→v4 §5.16 precedent) |

---

## 8. Deviations and assumptions

No deviations from the approved SPEC. All §4 changes applied; the checkpoint enum
kept `HITL-*`; kit-only.

**Assumption:** the compiled validator tool (US-012) is out of scope here and
will be aligned to v5 separately (flagged in US-020 §5). The root `devflow/`
schemas stay v4.0 (operating v4.2, ADR-006 dogfooding split).

---

## 9. Verification evidence

Documentation/schema V-Bounce — deterministic JSON-Schema validation (Python
`jsonschema`, draft-2020-12).

### GREEN
```
1. schemas valid draft-2020-12:  manifest-v5-us VALID · -bolt VALID · -tc VALID
2. templates vs their v5 schema:  US GREEN · BOLT GREEN · BOLT-NONFUNCTIONAL GREEN
                                  · BOLT-TEST GREEN · TC GREEN
3. virtual approval sample (agent:qa-agent + model claude-opus-5, mode=virtual): GREEN
   → the AITL record path validates end-to-end at the schema level
```

### RED (negative cases — all correctly REJECTED)
```
a) v4-shaped manifest (hitl_approvals + schema_version 4.0)  → REJECTED
b) mode=human but an agent:* actor present                    → REJECTED (consistency allOf)
c) human actor carrying a non-null model                     → REJECTED (approver conditional)
d) extra property inside an approval entry                   → REJECTED (additionalProperties:false)
e) agent actor with model:null                               → REJECTED (approver conditional)
```

### AC-7 (kit-only)
`git status`: only `distribution-kit/devflow/metrics/` (5 templates modified, 3 v4
schemas deleted, 3 v5 schemas added) + this Bolt's governance records (SPEC, MEM,
manifest). Root `devflow/` untouched.

### Gates
Unit/integration, SAST/SBOM, perf, IP, PII, dep-confusion, test-first: `n/a`
(documentation/schema, internal). Prompt-injection, secret-leak,
hallucination-lint (schemas compile; refs resolve), behavioral-reproducibility
(deterministic validation), bolt-manifest-validation: `pass`.

---

## 10. Manual interventions

None — the transform and validation were agent-generated Python; no human patch.

---

## 11. Evidence links

- **Diff / PR:** uncommitted working tree at MEM time (kit metrics + governance)
- **Commit:** baseline `97125e7`; this V-Bounce's commit pending user request
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-020.BOLT-001-manifest-schemas-v5.json`

---

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~20 min |
| V-Bounce number | 1 |
| Tests created | 0 automated; 3 GREEN + 5 RED schema-validation checks (deterministic) |
| AI-generated code | 100% (Python transform + validation) |
| First-pass approval | pending |

---

## 13. Pending items and stubs

- [ ] **BOLT-002** — align §3.12 / G23 / the four kit agents to the v5 manifest.
- [ ] **BOLT-003** — document the v4.0→v5.0 conversion in §5.16 (G36).
- [ ] **US-012 (validator tool)** — align the compiled validator to v5 (separate US).

---

## 14. HITL-MEM-Approval

> **Avenga DevFlow §2.12, §3.0.** Created by the agent, never self-approved. The
> executing Dev-validator inspects the diff (v5 schemas + templates, v4 removed),
> the §9 GREEN/RED evidence, this MEM and the manifest. Risk medium → one approver.

| Field | Value |
|-------|-------|
| **Reviewers (executing Dev-validator)** | eugenio.serrano |
| **Roles** | dev_validator (risk medium → 1 approver) |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-22T16:01:05-03:00` |
| **review.started_at** | `2026-08-22T16:03:57-03:00` |
| **review.decided_at** | `2026-08-22T16:03:57-03:00` |
| **Review evidence** | diff (3 v5 schemas + 5 templates + 3 v4 removed) + §9 validation suite + manifest |
| **Findings** | none — `acknowledged_without_comment: true` |
