---
id: "SPEC-260823-1741"
title: "The actors/ family in the standard shape — TEMPLATE-ACTOR, roster.schema.yaml, INDEX.md, project-policy and one file per actor (Modelo B) with validation"
date: "2026-08-23"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved" # draft | approved | blocked | obsolete
origin: "US-024"
bolt: "US-024.BOLT-001" # ⚠️ MANDATORY — US-NNN.BOLT-NNN
revision: 1 # material revision of this canonical SPEC (matches manifest spec_revisions[])
associated_adrs:
  - "devflow/adrs/ADR-007-devflow-agent-identity-model.md"
  - "devflow/adrs/ADR-010-actor-grammar-and-pure-v5-vocabulary.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
prerequisites:
  - "devflow/spec/SPEC-260823-1600-devflow-agent-contract-and-charters.md" # the role → artifacts mapping (US-023.BOLT-001) the production derivation uses
risk_class: "low" # mirrors the Bolt's risk_class
autonomy_level: "L3" # L1 | L2 | L3 | L4 — defaults by risk: low/medium→L3
turn_budget: "" # OPTIONAL — leave empty to use the platform default
data_classification: "internal"
review_ready_at: "2026-08-23T17:41:00-03:00"
review: # AITL-SPEC-Approval — recorded by the human reviewer (§3.0); decision dictated in conversation ("apruebo las 3 metele a las 3 en paralelo") and transcribed by the agent
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-23T17:52:00-03:00"
  decided_at: "2026-08-23T17:53:53-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved as Dev-validator: one-Bolt plan complete (the actors/ family shape — TEMPLATE-ACTOR + schema + INDEX + project-policy + example; the actors/actors/ path bug fixed; the self-containment check explicit; the policy knobs validate). Authorizes the V-Bounce."
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs, and section
  headings (##) stay in English (the schema). Prose in content_language
  (en, devflow/LANGUAGE; ADR-012).

  ⚠️ AITL-SPEC-Approval: a draft SPEC cannot start a code-run or V-Bounce.
  Material source changes invalidate the approval → stop, revise, re-approve
  (G15). One V-Bounce never spans two SPEC revisions.

  ⚠️ PRE-SPEC EVIDENCE GATE (§2.4.1): verified — US-024 re-approved ✓
  (Modelo B, 2026-08-23T17:37:47); ADR-007/010/004 accepted ✓; DISC-002
  approved ✓; US-023.BOLT-001 delivered ✓ (the mapping prerequisite);
  0 open OQs (G35).

  ⚠️ KIT SELF-CONTAINMENT: everything created in distribution-kit/ is
  self-contained — zero references to the maintenance partition
  (US/Bolt/SPEC/MEM/ADR/DISC/AC).
-->

# SPEC-260823-1741 — The `actors/` family shape (US-024.BOLT-001)

| Field | Value |
|-------|-------|
| **Origin** | [US-024](../functional/user-stories/US-024-unified-actors-roster.md) (re-approved, Modelo B) |
| **Bolt** | [US-024.BOLT-001](../functional/bolts/US-024.BOLT-001-roster-schema-and-validation.md) (approved) |
| **ADRs** | ADR-007 (identity), ADR-010 (grammar), ADR-004 (kit-only) |
| **Risk Class** | low · **Autonomy** L3 |
| **Revision** | 1 |

---

## 1. Objective

Deliver the `actors/` family in the **standard DevFlow family shape**
(Modelo B) inside the kit's `distribution-kit/devflow/actors/` folder
(created by US-022): a **`TEMPLATE-ACTOR`** (the kit template for creating
an actor), the actor **schema** (`roster.schema.yaml` — validates an actor
file), an **`INDEX.md`** listing the project's actors, a roster-level
**`project-policy.yaml`** (`aitl_enabled_checkpoints`, the `human_only`
floor), an **example actor file**, and a README update. **Each actor is
its own file** `actors/<actor-id>.yaml` (naming N-rule), created from the
template and listed in the INDEX — humans and DevFlow Agents as peers,
each carrying `id`, a project-chosen `name`, `role`, `model`, `modes`,
`approves` (agents also a `definition` pointer). **Definitions are
reusable** (N actors : 1 definition) and the **per-actor `model` is
authoritative** (per-instance). The **production mapping is derived from
`role`** (the single role → artifacts mapping from the charter templates,
US-023 BOLT-001, and §3.0.1) — **no per-agent `produces` field**.
Validation integration: an actor file validates against the schema
(validator tooling, US-012 family); a malformed one fails fast and the
safe default (humans) applies.

**Why:** the roster is the team map the Coordinator reads to resolve
roles, production and approval lookups — it must be a mechanically
checkable family like every other. **If not done:** the team map has no
shape, no validation, and the names/definitions/model flexibility (Modelo
B) has no home.

---

## 2. Context

US-024 (re-approved, Modelo B) defines the roster as the team map with
one file per actor, reusable definitions and per-instance models;
ADR-007 fixes the identity model (the actor as the unit, the model as an
attribute); ADR-010 fixes the grammar; DISC-002 §5.3 sketched the roster
(the US refines it to the family shape). The role → artifacts mapping
already exists in the charter templates (US-023.BOLT-001, delivered) and
§3.0.1 — the roster derives `produces` from `role`, no duplication. This
is kit documentation + schema, kit-only (ADR-004), and the deliverable
must be **self-contained** (no maintenance-partition references).

---

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | US-024.BOLT-001-roster-schema-and-validation.md | AITL-BOLT-READY-Approval ✓ (2026-08-23, risk low) |
| Feature US | US-024-unified-actors-roster.md | AITL-US-Approval ✓ (re-approved Modelo B, 2026-08-23T17:37:47) |
| ADRs | ADR-007, ADR-010, ADR-004 | accepted ✓ |
| DISC evidence | DISC-002 (§5.3 roster) | approved ✓ |
| Prior work | US-023.BOLT-001 (the mapping — delivered), US-022 (the actors/ folder) | delivered ✓ |
| Repository baseline | commit `45d553f` | — |

Pre-SPEC evidence gate: **all governed sources approved**; 0 open OQs (G35).

---

## 4. Scope

### In scope (kit, self-contained)

- `distribution-kit/devflow/actors/TEMPLATE-ACTOR.yaml` — the template for
  creating an actor file (every field with guidance comments).
- `distribution-kit/devflow/actors/roster.schema.yaml` — validates an
  actor file (the reconciled field set).
- `distribution-kit/devflow/actors/INDEX.md` — lists the project's actors.
- `distribution-kit/devflow/actors/project-policy.yaml` — the roster-level
  policy file (`aitl_enabled_checkpoints`, the `human_only` floor).
- `distribution-kit/devflow/actors/example.yaml` — the worked example actor
  file (created from the template, listed in the INDEX; flat in
  `actors/`, per the one-file-per-actor N-rule).
- `distribution-kit/devflow/actors/README.md` — updated with the family
  shape + the resolution-rules pointer (the rules text itself is BOLT-002).

### Out of scope

- The AITL-enable ADR template + the resolution-rule text (BOLT-002); the
  US-001 absorption (BOLT-003); the root `devflow/` (ADR-004).

---

## 5. Prerequisites and baseline

- US-023.BOLT-001 delivered (the role → artifacts mapping the production
  derivation uses); US-022 delivered (the `actors/` folder exists).
- Baseline commit `45d553f`.

---

## 6. Phases

### Phase A — The template and the schema

**Duration:** ~2h total cycle — **Complexity:** Low

#### A.1 `TEMPLATE-ACTOR.yaml`

Create the actor-file template with guidance comments: `id` (kebab-case —
THE identity), `name` (project-chosen free label, e.g. "Arq Juan",
".NET Architect"), `role` (open archetype), `model` (per-instance,
authoritative), `modes`, `approves` (real checkpoint codes; empty =
executor-only), `definition` (agents: the reusable blueprint pointer),
`capabilities` (agents: tier/tools/mcp_servers), `escalation`,
`write_paths` — plus the non-negotiable bounds (structured authority,
approver ceiling, MCP allowlist, independence) and the note that
`produces` is derived from `role` (never a field).

**Files created:**
- `distribution-kit/devflow/actors/TEMPLATE-ACTOR.yaml`

#### A.2 `roster.schema.yaml`

The validation schema for an actor file: required fields (`id`, `name`,
`role`, `model`, `modes`, `approves`; agents also `definition`),
enumeration constraints (`modes` ⊆ executor/approver; `approves` ⊆ the
checkpoint codes; `capabilities.tier` ⊆ T0..T3), the grammar forms
(`human:<user>` / `agent:<id>` for humans/agents), and the
additional-properties=false discipline — a malformed actor file fails fast.

**Files created:**
- `distribution-kit/devflow/actors/roster.schema.yaml`

### Phase B — The INDEX, the policy file and the example

**Duration:** ~1.5h total cycle — **Complexity:** Low

#### B.1 `INDEX.md` + `project-policy.yaml` + the example

`INDEX.md` lists the project's actors (the shipped example first) with
the family notes (one file per actor, the N-rule, definitions reusable
N:1, models per-instance). `project-policy.yaml` carries
`aitl_enabled_checkpoints` + the `human_only` floor. `actors/example.yaml`
is the worked example created from the template (e.g. a human actor and a
DevFlow Agent sharing a definition to demonstrate N:1).

**Files created:**
- `distribution-kit/devflow/actors/INDEX.md`
- `distribution-kit/devflow/actors/project-policy.yaml`
- `distribution-kit/devflow/actors/example.yaml`

### Phase C — The README + verification (GREEN)

**Duration:** ~0.5h total cycle — **Complexity:** Low

#### C.1 README update

`actors/README.md` gains the family-shape section (the five artifacts,
the one-file-per-actor rule, the N:1 definitions, the per-instance model,
the production-derivation note, the validation pointer).

#### C.2 Evidence

Presence of all six files; the example validates against the schema; a
malformed actor file fails fast (a validator run or a schema check); the
policy file's knobs validate; the grammar forms present; **the
self-containment check** — `grep -E "US-[0-9]{3}|ADR-[0-9]{3}|DISC-[0-9]{3}|BOLT-[0-9]|SPEC-26|MEM-26|REV-[0-9]{3}|TC-[0-9]{3}"` over the delivered kit files → **0 hits** (kit-internal anchors like §3.0.1 are allowed); `git status` kit-only; no BOM.

**Files created (evidence):** none — evidence recorded in the MEM.

---

## 7. Acceptance criteria

### AC-1: The family shape exists

**Given** the kit's `actors/` folder,
**When** a project builds its team,
**Then** it holds `TEMPLATE-ACTOR` + `roster.schema.yaml` + `INDEX.md` +
the `project_policy` file, with **one file per actor**
(`actors/<actor-id>.yaml`, from the template, listed in the INDEX);
humans + agents as peers, each with a project-chosen `name`; productive
outputs **derived from `role`** (no `produces` field); `definition`
**reusable N:1**; `model` **per-instance** (US-024 AC-1).

### AC-2: Validation

**Given** validation,
**When** an actor file is edited,
**Then** it validates against `roster.schema.yaml` — a malformed actor
file fails fast and the safe default (humans) applies until fixed
(US-024 AC-8).

### AC-3: The actor grammar

**Given** the actor grammar,
**When** the roster records actors,
**Then** it uses the `human:<user>` / `agent:<id>` forms consistent with
`checkpoint_approvals[]` (US-024 AC-9).

### AC mapping to source

| Source AC | How this SPEC satisfies it | Verifying test/evidence |
|-----------|----------------------------|--------------------------|
| US-024 AC-1 | the six family files + the one-file-per-actor rules | AC-1 presence checks |
| US-024 AC-8 | the schema + the validation integration | AC-2 (valid passes / malformed fails) |
| US-024 AC-9 | the grammar forms in the template/schema | AC-3 |

---

## 8. Testing strategy

Deterministic (documentation + schema):

- **RED (before):** `actors/` holds only the US-022 README — no family
  shape.
- **GREEN (after):** AC-1..AC-3 — the six files present; the example
  validates; a malformed actor file fails fast; the policy file's knobs
  validate; grammar forms present; the **self-containment grep → 0 hits**
  on the delivered kit files; kit-only.
- **Edge cases:** a human actor vs an agent actor (grammar forms); two
  actors sharing one `definition` (distinct `id`s, per-instance `model`s);
  `approves: []` (executor-only); a missing required field (fail fast);
  the policy file with a knob outside the allowed set (fail fast).

---

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | — | n/a — documentation + schema (the validation check IS the test) |
| SAST / SBOM | — | n/a — no runtime |
| Perf-smoke (p95/p99) | — | n/a — no runtime surface |
| Prompt-injection scan | — | pass — no runtime surface |
| Secret-leak scan | — | pass — no secrets |
| Hallucination lint | refs resolve | pass — §3.0.1/grammar refs resolve |
| IP / license provenance | — | n/a — original content |
| PII / DLP | — | n/a — no personal data (internal) |
| Dependency-confusion | — | n/a — no dependencies |
| Test-first evidence | — | n/a — documentation/schema; the validation evidence in §8 |
| Behavioral reproducibility | deterministic | pass — the validation runs reproduce |
| Bolt-manifest validation | validates | pass — BOLT-001 manifest + spec_revisions[] |

---

## 10. Security and data

The schema enforces the reconciled field set (no `produces`, structured
authority, the approver ceiling + MCP allowlist bounds carried from the
template). Data classification `internal`.

---

## 11. Migration, compatibility and rollback

- **Migration:** the `actors/` folder grows the family files; additive.
- **Compatibility:** the US-022 README keeps its content (updated, not
  replaced).
- **Rollback:** delete the new files; the root `devflow/` untouched.

---

## 12. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| Schema drifts from the template fields | 2 | 3 | Both derive from the same reconciled field set; the example validates |
| A `produces` field sneaks back | 2 | 3 | The template/schema carry the derivation note; the AC-1 check |
| Grammar divergence | 1 | 3 | ADR-010 forms reused in template + schema |

---

## 13. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| One file per actor + INDEX (Modelo B) | The standard family shape the maintainer chose — file-per-actor with naming N-rule, like every family |
| `project-policy.yaml` as the roster-level policy file | `project_policy` (enabled checkpoints + human-only floor) is team-level, not per-actor |
| `definition` reusable N:1 + `model` per-instance | Actors are named instances; the blueprint is shared; the model is per-instance (enabling model-level independence at `high`) |
| `produces` derived from `role` | One source (the charter mapping / §3.0.1); no duplicated field |

---

## 14. Stop conditions

- The example actor file cannot validate against the schema → stop, fix
  the schema or the example (never force a pass).
- Any maintenance-partition reference in the kit files → stop, fix
  (self-containment).
- A governed source changes materially (G15) → stop, revise, re-approve.
- Turn budget (10) exhausted before GREEN → stop, MEM with progress.

---

## 15. Definition of Done (DoD)

- [ ] Phases A–C implemented
- [ ] AC-1..AC-3 pass
- [ ] GREEN evidence (six files, validation pass/fail, grammar, kit-only)
- [ ] Self-contained (0 maintenance-partition references in the kit files)
- [ ] Applicable gates pass / n/a with reason
- [ ] MEM created in `devflow/memory/` (exactly one per V-Bounce)
- [ ] Manifest `v_bounces[]` entry appended in `devflow/metrics/bolts/`
- [ ] AITL-MEM-Approval recorded

---

## 16. References

- US-024 (re-approved — Modelo B), US-024.BOLT-001 (approved)
- ADR-007 (identity), ADR-010 (grammar), ADR-004 (kit-only)
- DISC-002 §5.3 (roster sketch); US-023.BOLT-001 (the mapping);
  US-022 (the actors/ folder)
- Example pattern: SPEC-260823-1600 (the agents/ family — same doc style)

---

## 17. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-23 | eugenio.serrano | Revision 1 — initial |

---

## 18. AITL-SPEC-Approval

> **Avenga DevFlow §2.4.1, §3.0.** This SPEC remains a draft until the
> Dev-validator (+ applicable domain owners) records `AITL-SPEC-Approval`
> (in the `review` frontmatter block). Bolt approval authorizes SPEC
> preparation; **SPEC approval authorizes the V-Bounce**. A material source
> change invalidates this approval — stop, revise, re-approve (G15).

| Field | Value |
|-------|-------|
| **review.reviewers** | Dev-validator + applicable domain owner(s) |
| **review.decision** | approved / changes_requested / rejected |
| **review_ready_at** | `2026-08-23T17:41:00-03:00` |
| **review.started_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **review.decided_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **Findings** | [findings or acknowledged_without_comment + reason] |
