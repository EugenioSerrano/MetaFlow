---
id: "SPEC-260823-1742"
title: "The AITL-enable ADR template and the roster resolution rules — the one governed act that enables virtual approvers, plus role → actors / independence resolution text"
date: "2026-08-23"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved" # draft | approved | blocked | obsolete
origin: "US-024"
bolt: "US-024.BOLT-002" # ⚠️ MANDATORY — US-NNN.BOLT-NNN
revision: 1 # material revision of this canonical SPEC (matches manifest spec_revisions[])
associated_adrs:
  - "devflow/adrs/ADR-008-aitl-approval-precept.md"
  - "devflow/adrs/ADR-010-actor-grammar-and-pure-v5-vocabulary.md"
prerequisites:
  - "devflow/spec/SPEC-260823-1741-actors-family-shape.md" # the actors/ family (the roster files the rules govern)
risk_class: "low" # mirrors the Bolt's risk_class
autonomy_level: "L3" # L1 | L2 | L3 | L4 — defaults by risk: low/medium→L3
turn_budget: "" # OPTIONAL — leave empty to use the platform default
data_classification: "internal"
review_ready_at: "2026-08-23T17:42:00-03:00"
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
  acknowledgment_reason: "Approved as Dev-validator: one-Bolt plan complete (the AITL-enable ADR template + the resolution rules incl. the definitions-sharing clause; the self-containment check explicit). Authorizes the V-Bounce."
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs, and section
  headings (##) stay in English (the schema). Prose in content_language
  (en, devflow/LANGUAGE; ADR-012).

  ⚠️ AITL-SPEC-Approval: a draft SPEC cannot start a code-run or V-Bounce.
  Material source changes invalidate the approval → stop, revise, re-approve
  (G15). One V-Bounce never spans two SPEC revisions.

  ⚠️ PRE-SPEC EVIDENCE GATE (§2.4.1): verified — US-024 re-approved ✓
  (Modelo B); ADR-008/010 accepted ✓; DISC-001/002 approved ✓; 0 open OQs.

  ⚠️ KIT SELF-CONTAINMENT: everything created in distribution-kit/ is
  self-contained — zero references to the maintenance partition.
-->

# SPEC-260823-1742 — The AITL-enable ADR template + the resolution rules (US-024.BOLT-002)

| Field | Value |
|-------|-------|
| **Origin** | [US-024](../functional/user-stories/US-024-unified-actors-roster.md) (re-approved, Modelo B) |
| **Bolt** | [US-024.BOLT-002](../functional/bolts/US-024.BOLT-002-aitl-enable-adr-template.md) (approved) |
| **ADRs** | ADR-008 (the precept — safe default + human ceiling), ADR-010 (grammar) |
| **Risk Class** | low · **Autonomy** L3 |
| **Revision** | 1 |

---

## 1. Objective

Deliver the two governed surfaces of the roster's decision layer in the
kit's `actors/` folder: (1) the **per-project AITL-enable ADR template**
(`TEMPLATE-AITL-ENABLE-ADR.md`) — the **one governed act** that enables
virtual approvers, declaring the enabled checkpoint classes, the roster
contents and the instantiated approver charters (never a silent flag —
the safe-default: no AI-signed approval without explicit human
configuration); and (2) the **resolution-rule text** in `actors/README.md`
— role → actors (humans and agents as peers; agent holders count only for
enabled checkpoints), the production lookup (who produces — resolved from
`role`), the independence floor/hardening/ceiling ladder, the
**definitions-sharing** rule (two actors sharing one `definition` stay
independent at the actor level; at `high`, distinct per-instance models),
and the zero-config invariant (no actor files, or none declares a DevFlow
Agent → pure HITL).

**Why:** delegation must be an explicit, governed human act; the roster
must be a deterministic lookup. **If not done:** enabling virtual
approvers has no template (each project reinvents it), and the resolution
rules have no home.

---

## 2. Context

US-024 (re-approved, Modelo B) — AC-2/3/4/5/7; ADR-008 fixes the precept
(the safe default, the human ceiling, the independence layers, the
AITL-enable ADR as the per-project governing act — already stated in
§3.0.1 of the methodology); DISC-001 §5.6.3 and DISC-002 rec #7 specify
the one-act framing. The `actors/` family (BOLT-001, SPEC-1741) provides
the roster files the rules govern. Kit documentation, kit-only (ADR-004),
self-contained.

---

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | US-024.BOLT-002-aitl-enable-adr-template.md | AITL-BOLT-READY-Approval ✓ (2026-08-23, risk low) |
| Feature US | US-024-unified-actors-roster.md | AITL-US-Approval ✓ (re-approved Modelo B) |
| ADRs | ADR-008, ADR-010 | accepted ✓ |
| DISC evidence | DISC-001 (§5.6.3), DISC-002 (rec #7) | approved ✓ |
| Prior SPEC | SPEC-260823-1741 (the actors/ family) | prerequisite |
| Repository baseline | commit `45d553f` | — |

Pre-SPEC evidence gate: **all governed sources approved**; 0 open OQs.

---

## 4. Scope

### In scope (kit, self-contained)

- `distribution-kit/devflow/actors/TEMPLATE-AITL-ENABLE-ADR.md` — the
  per-project ADR template (the one governed act).
- `distribution-kit/devflow/actors/README.md` — the resolution-rule text
  (role → actors; production lookup; independence ladder; the
  definitions-sharing rule; the zero-config invariant).

### Out of scope

- The family files themselves (BOLT-001); the US-001 absorption
  (BOLT-003); the root `devflow/` (ADR-004).

---

## 5. Prerequisites and baseline

- SPEC-260823-1741 (BOLT-001) delivered — the actors/ family exists.
- Baseline commit `45d553f`.

---

## 6. Phases

### Phase A — The AITL-enable ADR template

**Duration:** ~1.5h total cycle — **Complexity:** Low

#### A.1 The template

`TEMPLATE-AITL-ENABLE-ADR.md` — the ADR-shaped template with the fields:
context (why the project enables virtual approvers), the **enabled
checkpoint classes** (which AITL checkpoints may be occupied by agents,
per risk class), the **roster contents** (which actors — the
`actors/` files — are agents), and the **instantiated approver charters**
(which agents may approve what). The template carries the guardrails:
the safe-default (no AI-signed approval without this explicit human act),
the human-only floor (`critical`/`regulatory` — may be tightened, never
loosened), the independence requirement (approver ≠ executor), the
approver ceiling (T0/T1), and the note that changing an approver's
charter/authority fields re-triggers this ADR's review.

**Files created:**
- `distribution-kit/devflow/actors/TEMPLATE-AITL-ENABLE-ADR.md`

### Phase B — The resolution-rule text

**Duration:** ~1.5h total cycle — **Complexity:** Low

#### B.1 The rules in the README

`actors/README.md` gains the "Resolution rules" section: (1) role →
actors — a checkpoint's recommended role resolves to the actors holding
it, humans and agents as peers; an agent holder counts only for
checkpoints the project's AITL policy enables; (2) the production lookup —
who produces an artifact class resolves from `role` (the single
role → artifacts mapping, §3.0.1); (3) the independence ladder —
`approver.id ≠ executor.id` (the actor floor), model hardening at `high`
(`approver.model ≠ executor.model` — the per-instance `model` makes this
possible between actors sharing a definition), the human ceiling at
`critical`/`regulatory`; (4) the definitions-sharing rule — two actors
sharing one `definition` stay independent at the actor level (distinct
`id`); (5) the zero-config invariant — no actor files, or none declares a
DevFlow Agent, behaves byte-for-byte as pure HITL.

**Files modified:**
- `distribution-kit/devflow/actors/README.md`

### Phase C — Verification (GREEN)

**Duration:** ~0.5h total cycle — **Complexity:** Low

#### C.1 Evidence

The template present with the five fields + the guardrails; the README
rules present; ADR-008 consistency (the safe default, the human ceiling,
the independence layers); **the self-containment check** — `grep -E
"US-[0-9]{3}|ADR-[0-9]{3}|DISC-[0-9]{3}|BOLT-[0-9]|SPEC-26|MEM-26|REV-[0-9]{3}|TC-[0-9]{3}"`
over the delivered kit files → **0 hits**; `git status` kit-only; no BOM.

**Files created (evidence):** none — evidence recorded in the MEM.

---

## 7. Acceptance criteria

### AC-1: The one governed act

**Given** the per-project AITL-enable ADR template,
**When** a project enables virtual approvers,
**Then** one governed act declares the enabled checkpoints, the roster
contents and the instantiated approver charters — the template ships in
the kit's `actors/` folder; enabling is never a silent flag (US-024 AC-7).

### AC-2: Zero-config stated

**Given** the resolution-rule text,
**When** no actor files exist (or none declares a DevFlow Agent),
**Then** the project behaves byte-for-byte as pure HITL — every checkpoint
resolves to humans (US-024 AC-2).

### AC-3: The production lookup stated

**Given** the resolution-rule text,
**When** the team needs an executor,
**Then** the roster returns the actors holding the role that owns the
artifact class — the production mapping resolves from `role` (US-024
AC-3).

### AC-4: The approver resolution stated

**Given** the resolution-rule text,
**When** an approver must be resolved,
**Then** the roster returns the actors holding the role (peers; agent
holders only for enabled checkpoints) (US-024 AC-4).

### AC-5: The independence ladder stated

**Given** the resolution-rule text,
**When** an approval is routed,
**Then** `approver.id ≠ executor.id`; model hardening at `high`; human-only
at `critical`/`regulatory`; two actors sharing one `definition` stay
independent at the actor level (distinct `id`s; distinct per-instance
`model`s at `high`) (US-024 AC-5).

### AC mapping to source

| Source AC | How this SPEC satisfies it | Verifying test/evidence |
|-----------|----------------------------|--------------------------|
| US-024 AC-7 | the AITL-enable ADR template | AC-1 presence + guardrails |
| US-024 AC-2 | the zero-config rule text | AC-2 |
| US-024 AC-3 | the production lookup text | AC-3 |
| US-024 AC-4 | the approver resolution text | AC-4 |
| US-024 AC-5 | the independence ladder + definitions-sharing | AC-5 |

---

## 8. Testing strategy

Deterministic (documentation):

- **RED (before):** no template; no resolution rules in the README.
- **GREEN (after):** AC-1..AC-5 — the template present with the five
  fields + the guardrails; the rules text present; ADR-008 consistency
  (safe default, human ceiling, independence); the **self-containment
  grep → 0 hits** on the delivered kit files; kit-only.
- **Edge cases:** the definitions-sharing clause (two actors, one
  definition, distinct ids/models); the zero-config wording (no actor
  files OR none is an agent).

---

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | — | n/a — documentation-only |
| SAST / SBOM | — | n/a — no runtime |
| Perf-smoke (p95/p99) | — | n/a — no runtime surface |
| Prompt-injection scan | — | pass — no runtime surface |
| Secret-leak scan | — | pass — no secrets |
| Hallucination lint | refs resolve | pass — §3.0.1/ADR refs resolve |
| IP / license provenance | — | n/a — original content |
| PII / DLP | — | n/a — no personal data (internal) |
| Dependency-confusion | — | n/a — no dependencies |
| Test-first evidence | — | n/a — documentation; presence evidence in §8 |
| Behavioral reproducibility | deterministic | pass |
| Bolt-manifest validation | validates | pass — BOLT-002 manifest + spec_revisions[] |

---

## 10. Security and data

The template is the governance gate: the safe-default (no AI-signed
approval without the explicit human act), the human-only floor, the
independence requirement and the approver ceiling — the
injection-forged-approval defense's governance half. Data classification
`internal`.

---

## 11. Migration, compatibility and rollback

- **Migration:** new template + README section; additive.
- **Compatibility:** the existing README content preserved.
- **Rollback:** delete the template; revert the README section; root
  untouched.

---

## 12. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| The template enables delegation silently | 2 | 5 | The safe-default + one-act framing + the human-only floor are built-in |
| The rules text drifts from ADR-008 | 2 | 3 | Written directly from the precept's clauses; consistency check |
| The definitions-sharing clause missed | 1 | 3 | AC-5 covers it explicitly |

---

## 13. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| The template lives in `actors/` (not `adrs/`) | It is the roster's enabling act — the family home (defensible, per the review) |
| The resolution rules live in the actors/README | The roster docs are where the lookup is explained; self-contained |
| The human-only floor may be tightened, never loosened | ADR-008: the safe default is a floor, not a ceiling of permissiveness |

---

## 14. Stop conditions

- The template would allow enabling without the human act → stop, fix.
- Any maintenance-partition reference in the kit files → stop, fix
  (self-containment).
- A governed source changes materially (G15) → stop, revise, re-approve.
- Turn budget (10) exhausted before GREEN → stop, MEM with progress.

---

## 15. Definition of Done (DoD)

- [ ] Phases A–C implemented
- [ ] AC-1..AC-5 pass
- [ ] GREEN evidence (template + rules present, ADR-008 consistent, kit-only)
- [ ] Self-contained (0 maintenance-partition references in the kit files)
- [ ] Applicable gates pass / n/a with reason
- [ ] MEM created in `devflow/memory/` (exactly one per V-Bounce)
- [ ] Manifest `v_bounces[]` entry appended in `devflow/metrics/bolts/`
- [ ] AITL-MEM-Approval recorded

---

## 16. References

- US-024 (re-approved — Modelo B), US-024.BOLT-002 (approved)
- ADR-008 (the precept), ADR-010 (grammar)
- DISC-001 §5.6.3, DISC-002 rec #7; SPEC-260823-1741 (the family)

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
| **review_ready_at** | `2026-08-23T17:42:00-03:00` |
| **review.started_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **review.decided_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **Findings** | [findings or acknowledged_without_comment + reason] |
