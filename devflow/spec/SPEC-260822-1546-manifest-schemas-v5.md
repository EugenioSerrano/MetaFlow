---
id: "SPEC-260822-1546"
title: "Manifest schemas + templates → v5 (checkpoint_approvals[], mode, actor+model, schema_version 5.0)"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
status: "approved"
origin: "US-020"
bolt: "US-020.BOLT-001"
revision: 1
associated_adrs:
  - "devflow/adrs/ADR-008-aitl-approval-precept.md"
  - "devflow/adrs/ADR-007-devflow-agent-identity-model.md"
  - "devflow/adrs/ADR-006-versioning-and-self-development-model.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
prerequisites: []
risk_class: "medium"
autonomy_level: "L3"
turn_budget: ""
data_classification: "internal"
review_ready_at: "2026-08-22T15:46:59-03:00"
review: # HITL-SPEC-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "dev_validator"}]
  started_at: "2026-08-22T15:57:27-03:00"
  decided_at: "2026-08-22T15:57:27-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved. Precise from→to for the v5 schemas (checkpoint_approvals[]/checkpointApproval, +mode, approver→actor+model with the agent/model conditional, schema_version 5.0, HITL-* enum kept for the separate rename US, allOf + additionalProperties preserved), the five templates, and a positive+negative validation suite. Kit-only (ADR-004), medium/L3. Authorizes the V-Bounce."
---

<!--
  LANGUAGE POLICY (§3.15): schema in English; prose in content_language (en).
  Kit-only (ADR-004); root untouched. Documentation/schema change — evidence is
  deterministic JSON-Schema validation, not a runtime test suite.
-->

# SPEC-260822-1546 — Manifest schemas + templates → v5

| Field | Value |
|-------|-------|
| **Origin** | [US-020](../functional/user-stories/US-020-manifest-aitl-evolution.md) (approved) |
| **Bolt** | [US-020.BOLT-001](../functional/bolts/US-020.BOLT-001-manifest-schemas-v5.md) (approved) |
| **ADRs** | ADR-008 (record shape), ADR-007 (actor+model), ADR-006 (version bump), ADR-004 (kit-only) |
| **Risk Class** | medium · **Autonomy** L3 |
| **Revision** | 1 |

---

## 1. Objective

Evolve the kit's **three manifest schema files** and **five templates** from v4.0
to v5.0 so the approval record is `checkpoint_approvals[]` — recording, per
entry, the **actor** (human or AI agent), its **model** and the **mode**
(`human`|`virtual`) — with `schema_version "5.0"`.

**Why:** ADR-008 (AITL) requires the manifest to record *who* signed and *how*
(human or agent). ADR-006 makes changing the manifest the technical trigger of
the v5.0 bump. **If not done:** the AITL precept has no auditable record and the
rest of v5.0 (registry, pilot) has nothing to write into.

---

## 2. Context

US-020 (approved) decomposes into three Bolts; this is **BOLT-001**, the
foundational schema Bolt (no dependencies). BOLT-002 (methodology text + agents)
and BOLT-003 (§5.16 conversion) depend on it. The change is **kit-only**
(ADR-004): the root `devflow/` stays v4.0 (operating methodology, v4.2) until it
migrates. This SPEC's V-Bounce produces the kit's v5 schema files + templates.

---

## 3. Source inventory and approval references (pre-SPEC evidence gate)

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | `devflow/functional/bolts/US-020.BOLT-001-manifest-schemas-v5.md` | HITL-BOLT-READY-Approval ✓ |
| Parent US | `devflow/functional/user-stories/US-020-manifest-aitl-evolution.md` | HITL-US-Approval ✓ |
| ADRs | ADR-008, ADR-007, ADR-006, ADR-004 | accepted ✓ |
| Repository baseline | branch `5.0`, HEAD `97125e7` | — |
| Current schema | `distribution-kit/devflow/metrics/manifest-v4-{us,bolt,tc}.schema.json` (`$defs/hitlDecision`, `hitl_approvals[]`, `schema_version "4.0"`, checkpoint enum of 7 `HITL-*` names, `allOf` conditionals for SPEC→revision / MEM→v_bounce) | — |

Pre-SPEC evidence gate: **all governed sources approved.** No draft/stale source.

---

## 4. Scope

### In scope — the kit's `distribution-kit/devflow/metrics/`

- **Three schema files** → v5: create `manifest-v5-us.schema.json`,
  `manifest-v5-bolt.schema.json`, `manifest-v5-tc.schema.json`; **remove** the
  three `manifest-v4-*.schema.json` (the kit ships one current schema family —
  same as the v3→v4 precedent, §5.16).
- **Five templates** → v5 shape: `TEMPLATE-MANIFEST-US.json`,
  `TEMPLATE-MANIFEST-BOLT.json`, `TEMPLATE-MANIFEST-BOLT-NONFUNCTIONAL.json`,
  `TEMPLATE-MANIFEST-BOLT-TEST.json`, `TEMPLATE-MANIFEST-TC.json`.

### The v5 schema change (the "how" — from → to)

1. **Field rename:** `hitl_approvals` → **`checkpoint_approvals`** (in all three
   schemas' top-level properties and `required`).
2. **`$def` rename:** `hitlDecision` → **`checkpointApproval`** (update the
   `$ref`).
3. **Add `mode`** to `checkpointApproval`: `enum: ["human", "virtual"]`,
   **required**.
4. **Evolve the approver `$def`** to record the actor and its model:
   - `actor`: string, **required**, pattern `^(human|agent):.+` (e.g.
     `human:eugenio.serrano`, `agent:qa-agent`) — replaces the v4 `user` field.
   - `role`: string, required (unchanged).
   - `model`: `string | null`, required — **non-null when the actor is
     `agent:*`**, **null when `human:*`** (conditional via `allOf`/`if`-`then`).
   - `additionalProperties: false` (unchanged).
5. **Entry-level consistency (`allOf`):** when any `decided_by[].actor` is
   `agent:*`, the entry `mode` MUST be `virtual`; when all are `human:*`, `mode`
   MUST be `human`. (The safe default — human — records exactly as before.)
6. **`schema_version` const:** `"4.0"` → **`"5.0"`** in all three.
7. **Preserved unchanged:** `additionalProperties: false` everywhere; the
   `checkpoint` **enum stays the 7 `HITL-*` values** (the HITL→AITL rename of the
   *values* is a separate US — this Bolt changes structure, not names); the
   `allOf` conditionals (SPEC-Approval → `subject.revision`, MEM-Approval →
   `subject.v_bounce`); all non-approval fields (`bolt`/`us`/`tc`,
   `spec_revisions`, `v_bounces`, `generation`, timings).

### The five templates (v5 examples)

- `schema_version: "5.0"`; the approval array is `checkpoint_approvals[]`; each
  example entry shows `mode: "human"`, `decided_by: [{actor: "human:<user>",
  role: "<role>", model: null}]`. Example **checkpoint values stay `HITL-*`**
  (rename is a separate US). Templates validate against the new v5 schemas.

### Out of scope

- Methodology §3.12 / G23 text + the four agents → **BOLT-002**.
- The §5.16 v4.0→v5.0 conversion recipe → **BOLT-003**.
- The `HITL-*`→`AITL-*` rename of checkpoint values (the enum) → separate US.
- The root `devflow/` schemas (operating v4.2 — untouched, ADR-004).
- The compiled validator tool (US-012) — flagged as dependent, not changed here.

---

## 5. Phases

- **Phase A — Schemas:** create the three `manifest-v5-*.schema.json` from the v4
  ones with the §4 changes; remove the v4 files. ~1.5h.
- **Phase B — Templates:** rewrite the five `TEMPLATE-MANIFEST-*.json` to the v5
  shape. ~1h.
- **Phase C — Verification (GREEN):** §6 validation suite.

---

## 6. Acceptance criteria

- **AC-1 (field/def):** all three v5 schemas expose `checkpoint_approvals[]`
  (no `hitl_approvals`), items `$ref` `checkpointApproval`.
- **AC-2 (mode+actor+model):** `checkpointApproval` requires `checkpoint`,
  `subject`, `mode` (`human|virtual`), `decision`, `decided_by`, `decided_at`;
  each `decided_by[]` has `actor` (`^(human|agent):.+`), `role`, `model`
  (`string|null`); model non-null iff actor is `agent:*`; `mode` agrees with the
  actors (virtual iff any agent).
- **AC-3 (version):** `schema_version` const is `"5.0"` in all three; v4 files
  removed.
- **AC-4 (preserved):** `additionalProperties:false` everywhere; the 7 `HITL-*`
  checkpoint enum retained; the SPEC→revision / MEM→v_bounce `allOf`
  conditionals retained; non-approval fields unchanged.
- **AC-5 (templates):** the five templates carry `schema_version "5.0"` and
  `checkpoint_approvals[]`, and validate green against the v5 schemas.
- **AC-6 (positive+negative validation):** a hand-written **v5 sample** (one per
  level, with one `human` entry and one `virtual` entry incl. `model`) validates
  **green**; a **v4-shaped** manifest (old `hitl_approvals[]`) validates **red**
  against v5 (the change bites); an entry with `mode:human` but an `agent:*`
  actor validates **red** (consistency rule works).
- **AC-7 (kit-only + manifest):** `git status` shows only
  `distribution-kit/devflow/metrics/` + governance records; the BOLT-001
  manifest gets its `v_bounces[]` entry and validates.

---

## 7. Testing strategy

Deterministic JSON-Schema validation (no runtime):
- Validate the three v5 schemas are themselves valid JSON Schema (draft
  compilation).
- **GREEN:** v5 sample manifests (US/Bolt/TC, each with a human + a virtual
  entry) validate against their v5 schema.
- **RED (must fail):** a v4-shaped manifest against v5; a `mode/actor` mismatch;
  an extra property (additionalProperties:false).
- Use a JSON-Schema validator (python `jsonschema`, or the kit's compiled
  validator if available); record commands + output in the MEM.

---

## 8. Quality gates

| Gate | Status |
|------|--------|
| Unit/integration, SAST/SBOM, perf, IP, PII, dependency-confusion | `n/a` — documentation/schema, internal |
| Test-first evidence | `n/a` — not a BUG Bolt (evidence is schema validation) |
| Prompt-injection, secret-leak | `pass` |
| Hallucination-lint | `pass` — every field/ref resolves; schemas compile |
| Behavioral-reproducibility | `pass` — deterministic validation |
| Bolt-manifest-validation | `pass` |

---

## 9. Security and data

No runtime/security boundary. The `mode`/`actor` fields are the audit basis for
`approval-integrity` (ADR-008 §5) but this Bolt only defines the schema. Data
`internal`.

---

## 10. Migration, compatibility, rollback

- **Migration:** the v4.0→v5.0 conversion recipe is **BOLT-003** (§5.16); this
  Bolt only ships the target schema. Existing v4 manifests in the root/adopters
  are unaffected until they migrate.
- **Compatibility:** the kit now validates only v5 manifests. The safe default
  (human approvals) records equivalently; the checkpoint values stay `HITL-*`
  until the rename US, so no downstream name breakage here.
- **Rollback:** revert the kit commit (v4 files restored); root untouched.

---

## 11. Monitoring and observability

`n/a` — no runtime. The §7 validation suite is the observability; captured in MEM.

---

## 12. Risk matrix

| Risk | Prob | Impact | Mitigation |
|------|------|--------|------------|
| The `mode`/`actor`/`model` conditional is mis-encoded in JSON Schema | 3 | 3 | AC-6 negative cases (mode/actor mismatch, human-with-model) prove the conditionals bite |
| Removing v4 files breaks the validator tool (US-012) | 3 | 2 | Out of scope here; flagged in US-020 §5 — US-012 handles v5; the root's v4 schema is untouched (operating) |
| `allOf` conditionals (SPEC→revision, MEM→v_bounce) lost in the rewrite | 2 | 3 | AC-4 asserts they are retained; carry them across verbatim |
| Templates drift from schemas | 2 | 2 | AC-5 validates templates against the v5 schemas |
| Accidental checkpoint-value rename (HITL→AITL) | 2 | 2 | AC-4 keeps the `HITL-*` enum; rename is a separate US |

---

## 13. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| New `manifest-v5-*` files; remove v4 | The kit ships one current schema family per version (§5.16 v3→v4 precedent); avoids ambiguity about which validates |
| `actor` string with `human:`/`agent:` prefix (replaces `user`) | Directly encodes ADR-008's `human:<user>` / `agent:<id>`; one field, unambiguous, queryable |
| `mode` explicit even though derivable from the actor prefix | ADR-008/DISC-002 specify it; explicit discriminator is clearer and cheap to validate |
| Keep the `HITL-*` checkpoint enum | Structure vs names split — the rename is a separate US; the field name `checkpoint_approvals` is already neutral |
| `model: null` for humans, required for agents | Records the model as an attribute (ADR-007) exactly where it exists |

---

## 14. Stop conditions

- A JSON-Schema construct needed for the `mode/actor/model` conditional proves
  unexpressible cleanly → stop, record options, ask.
- Any root `devflow/` schema in the diff → stop, revert, record.
- Turn budget (10) exhausted before GREEN → stop, MEM with progress, resume.
- A governed source changes materially (G15) → stop, revise, re-approve.

---

## 15. Definition of Done

- [ ] Phases A–C implemented · AC-1..AC-7 pass
- [ ] GREEN validation (v5 samples pass; v4/mismatch/extra-prop fail; templates validate)
- [ ] Follows ADR-004 (kit-only) · ADR-006/007/008 (shape)
- [ ] Gates pass / n/a per §8
- [ ] MEM created (validation evidence) · manifest `v_bounces[]` appended
- [ ] HITL-MEM-Approval recorded

---

## 16. References

- US-020, US-020.BOLT-001 (approved); ADR-004/006/007/008; DISC-002 (§5.1 record shape)
- Current: `manifest-v4-{us,bolt,tc}.schema.json` (`$defs/hitlDecision`, `approver`)
- §3.12 (Manifest Family) — described/aligned in BOLT-002; §5.16 conversion — BOLT-003

---

## 17. HITL-SPEC-Approval

> **Avenga DevFlow §2.4.1, §3.0.** Draft until the Dev-validator records
> `HITL-SPEC-Approval`. A material source change invalidates it — stop, revise,
> re-approve (G15).

| Field | Value |
|-------|-------|
| **review.reviewers** | eugenio.serrano (dev_validator) |
| **review.decision** | **approved** |
| **review_ready_at** | `2026-08-22T15:46:59-03:00` |
| **review.started_at** | `2026-08-22T15:57:27-03:00` |
| **review.decided_at** | `2026-08-22T15:57:27-03:00` |
