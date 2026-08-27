---
id: "SPEC-260822-1817"
title: "Evolve the HITL concept to AITL (Actor-in-the-Loop): §0 foundational principle + §3.0 Charter + agents' concept sections"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
status: "approved"
origin: "US-021"
bolt: "US-021.BOLT-001"
revision: 2
associated_adrs:
  - "devflow/adrs/ADR-008-aitl-approval-precept.md"
  - "devflow/adrs/ADR-007-devflow-agent-identity-model.md"
  - "devflow/adrs/ADR-005-removal-completeness-phrase-family-sweep.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
prerequisites: []
risk_class: "medium"
autonomy_level: "L3"
turn_budget: ""
data_classification: "internal"
review_ready_at: "2026-08-22T18:25:02-03:00"
review: # HITL-SPEC-Approval (rev 2) — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "dev_validator"}]
  started_at: "2026-08-22T18:27:05-03:00"
  decided_at: "2026-08-22T18:27:05-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved rev 2: crisp 3-category boundary — BOLT-001 owns only category 1 (precept-defining prose); the pervasive HITL adjective (cat 2) + identifiers (cat 3) go to BOLT-004. AC-5 strengthened (identifier count 1119 unchanged + no adjective line changed). Authorizes the V-Bounce against rev 2."
---

<!--
  LANGUAGE POLICY (§3.15): schema in English; prose content_language (en).
  Kit-only (ADR-004); root operating methodology stays v4.2.
  DOGFOODING SPLIT (ADR-008 §3.1): this SPEC is authored under v4.2, so its OWN
  checkpoints are HITL-*. Its deliverable evolves the CONCEPT of the v5.0 kit.
  BOUNDARY: this Bolt changes the CONCEPT (the term "Human-in-the-Loop"/standalone
  "HITL" and the precept); it does NOT rename `HITL-<CODE>-Approval` IDENTIFIERS
  (US-021.BOLT-004) nor the canonical naming rule, GUARDRAILS (BOLT-002) or the
  schema enum (BOLT-003).
-->

# SPEC-260822-1817 — AITL concept & precept (US-021.BOLT-001)

| Field | Value |
|-------|-------|
| **Origin** | [US-021](../functional/user-stories/US-021-hitl-to-aitl-evolution.md) (approved) |
| **Bolt** | [US-021.BOLT-001](../functional/bolts/US-021.BOLT-001-aitl-concept-and-precept.md) (approved) |
| **ADRs** | ADR-008 (§3.1/§3.2 precept), ADR-007 (actor identity), ADR-005 (boundary sweep), ADR-004 (kit-only) |
| **Risk Class** | medium · **Autonomy** L3 |
| **Revision** | 1 |

---

## 1. Objective

Evolve the **Human-in-the-Loop concept** of the v5.0 kit into **AITL
(Actor-in-the-Loop)** — the conceptual core of ADR-008 §3.1. Reframe the
methodology's precept from *"the AI generates, the human governs at every
checkpoint"* to **"human-by-default, agent-by-explicit-configuration,"** and
define the **actor** (a human by default, or a virtual DevFlow Agent by explicit
valid configuration; ADR-007). Apply the same reframing to the four platform
agents' concept sections.

**Why:** v5.0's identity is AITL; the concept must be stated once, precisely,
before the guardrails (BOLT-002), the schema enum (BOLT-003) and the identifier
sweep (BOLT-004) build on it. **If not done:** the kit renames checkpoints to
`AITL-*` (later Bolts) while its precept still says "the human governs" — an
incoherent half-evolution.

---

## 2. Context

The concept lives in two places in the core methodology — the **Foundational
principle** (`Avenga-DevFlow.md` ~237–248) and **§3.0 "Human-in-the-Loop Charter
(HITL)"** (heading + opening, ~1364–1368) — plus the four agents' concept section
(their `# HITL — HUMAN-IN-THE-LOOP` block) and a mention in the kit `README.md`.
US-020 already shipped the manifest record (`checkpoint_approvals[]`) the precept
refers to. This Bolt is prose/definition only.

---

## 3. Source inventory (pre-SPEC evidence gate)

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | `US-021.BOLT-001-aitl-concept-and-precept.md` | HITL-BOLT-READY-Approval ✓ |
| Parent US | `US-021-hitl-to-aitl-evolution.md` | HITL-US-Approval ✓ |
| ADRs | ADR-008, ADR-007, ADR-005, ADR-004 | accepted ✓ |
| Prior work | US-020 (manifest v5) | **delivered** ✓ |
| Baseline | branch `5.0`, working tree at the maintainer's latest commit (US-020 delivered + kept active) | — |

Pre-SPEC evidence gate: **all governed sources approved.** No active-ADR conflict (§3.5).

---

## 4. The concept change to apply

Reframe, in the concept prose only (never touching identifiers):

1. **Foundational principle (~237–248):** "The AI agent generates … the human's
   role is to steer, review and approve at the named HITL checkpoints" →
   the **AITL precept**: the AI generates the intended-final draft; an **actor**
   steers, reviews and approves at every named checkpoint — a **human by default**,
   a **virtual DevFlow Agent only by explicit valid configuration** (ADR-007). Keep
   every existing guarantee: every checkpoint is still a mandatory pause; nothing
   reaches production without an approved checkpoint. Add the **safe-default
   invariant** (ADR-008 §3.2): with no/invalid configuration a project behaves
   exactly like pure HITL — no AI-signed approval is possible.
2. **§3.0 Charter (~1364–1368):** heading `## 3.0 Human-in-the-Loop Charter (HITL)`
   → `## 3.0 Actor-in-the-Loop Charter (AITL)`; opening "Human-in-the-loop is the
   load-bearing principle … the human is the governor" → AITL framing
   (human-by-default; the actor governs; a human governs by default, a configured
   virtual DevFlow Agent may under §3.3–§3.6 of ADR-008). **HITL is named as the
   default case (actor = human) inside AITL**, not a separate paradigm.
3. **The AITL definition** stated once, prominently (foundational or §3.0):
   *AITL — Actor-in-the-Loop; the actor is a human (default) or an AI agent (a
   DevFlow Agent, virtual, by explicit config).*
4. **The four agents' concept section** (`# HITL — HUMAN-IN-THE-LOOP …`): the
   heading + precept prose reframed to AITL, **byte-identical** across the four in
   their shared region.
5. **`README.md`** concept mention → AITL (concept only).

**Not changed here (deferred) — rev 2 makes this crisp:** three things stay:
**(cat. 2) the pervasive `HITL` adjective/shorthand** ("HITL approval", "HITL
checkpoint(s)", "HITL governance", "HITL Coverage", "HITL operating rules", "What
HITL is NOT", …, ~55 refs in the core + agents + README) → **BOLT-004**;
**(cat. 3) every `HITL-<CODE>-Approval` identifier** (the §3.0 table, ~1,119
kit-wide) + the **canonical naming rule** (~1386–1390) → **BOLT-004**; plus
**G05/G18/G24** → BOLT-002 and the **schema enum** → BOLT-003; and enabling
virtual approvers / registry / Coordinator / roster / pilot → later USs. BOLT-004
sweeps cat. 2 **and** cat. 3 together (they interleave on the same lines), one
ADR-005 pass with allowlist.

---

## 5. Scope

### In scope (kit, concept only)
- `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md` — Foundational
  principle + §3.0 Charter heading/opening + the AITL definition.
- `distribution-kit/CLAUDE.md`, `.agents/skills/avenga-devflow/SKILL.md`,
  `.github/agents/AvengaDevFlow.agent.md`, `.opencode/agents/AvengaDevFlow.md` —
  the concept/precept section (byte-synced shared region).
- `distribution-kit/devflow/README.md` — the concept mention.

### Boundary — three categories of "HITL" (ADR-005, rev 2)

"HITL" appears three ways; this Bolt owns **only category 1**:

1. **Paradigm name / precept (THIS Bolt):** the **defining prose** that states
   *what the paradigm is* — the Foundational principle (~237–248), the §3.0
   Charter **heading + opening** (~1364–1368), the AITL definition, the agents'
   **concept section** (the `# HITL — HUMAN-IN-THE-LOOP` heading + its precept
   intro), and the README concept **heading + intro**. These are reframed to AITL.
2. **Pervasive adjective/shorthand (NOT this Bolt → BOLT-004):** "HITL approval",
   "HITL checkpoint(s)", "HITL governance", "HITL Coverage", "HITL operating
   rules", etc. — left untouched here; swept by BOLT-004.
3. **Identifiers (NOT this Bolt → BOLT-004):** `HITL-<CODE>-Approval` and the
   canonical naming rule — left untouched here; swept by BOLT-004.

**Why 2+3 both go to BOLT-004:** the adjective and identifiers interleave on the
same lines, so one comprehensive ADR-005 sweep is cleaner than splitting them.
Mid-development the kit is intentionally mixed (AITL precept + still-HITL
adjective) until BOLT-004 lands — each Bolt stays independently demonstrable.

**Enforcement:** ripgrep here lacks look-around, so the boundary is checked by (a)
the identifier form `HITL-[A-Z][A-Z-]*-Approval` count staying **exactly**
unchanged (AC-5), and (b) this Bolt editing only the category-1 spots listed above
(the diff is inspected to confirm no category-2 adjective line changed).

### Out of scope
- Identifiers, naming rule, GUARDRAILS, schema enum (other US-021 Bolts); the
  root `devflow/` (ADR-004); any behavioral change (concept prose only).

---

## 6. Phases

- **Phase A — core concept:** reframe the Foundational principle + §3.0 Charter
  heading/opening + add the AITL definition (Avenga-DevFlow.md). ~1.5h.
- **Phase B — agents + README:** reframe the four agents' concept section
  (byte-identical) + the README mention. ~1h.
- **Phase C — Verification (GREEN):** boundary sweep (§8) + four-agent sync +
  G-count + kit-only. ~0.5h.

---

## 7. Acceptance criteria

- **AC-1 (precept reframed):** the Foundational principle states
  **human-by-default, agent-by-explicit-configuration**, defines the **actor**
  (human/DevFlow Agent), keeps every existing guarantee (each checkpoint a
  mandatory pause; nothing to production without an approved checkpoint), and
  states the **safe-default invariant** (ADR-008 §3.2).
- **AC-2 (charter reframed):** §3.0's heading reads **Actor-in-the-Loop Charter
  (AITL)** and its opening frames HITL as the **default case (actor = human)**
  inside AITL.
- **AC-3 (AITL defined):** the kit defines **AITL = Actor-in-the-Loop** and the
  actor once, prominently.
- **AC-4 (agents synced):** the four agents' concept section carries the AITL
  framing, **byte-identical** in the shared region; **G-count 39×5**.
- **AC-5 (boundary — zero identifier + zero adjective drift, rev 2):** **no
  `HITL-<CODE>-Approval` identifier is changed** (the count of
  `HITL-[A-Z][A-Z-]*-Approval` in the kit is **unchanged**, 1,119 before/after);
  the canonical naming rule is untouched; and **no category-2 adjective line is
  changed** (only the category-1 precept spots in §5 are edited — confirmed by
  diff inspection). Categories 2 and 3 are BOLT-004's.
- **AC-6 (kit-only):** `git status` shows only `distribution-kit/` + governance
  records; the root `devflow/` is untouched.
- **AC-7 (manifest):** the BOLT-001 manifest gets its `v_bounces[]` entry and validates.

---

## 8. Testing strategy

Deterministic (documentation/concept):
- **RED (before):** the precept says "the human governs"; §3.0 is
  "Human-in-the-Loop Charter (HITL)"; no AITL/actor definition.
- **GREEN (after):** AC-1..AC-4 present; **AC-5 boundary check** — the count of
  `HITL-[A-Z][A-Z-]*-Approval` identifiers in the kit is **identical**
  before/after (this Bolt touches concept, not identifiers); four-agent sync +
  G-count 39×5; `git status` kit-only. Record the identifier before/after counts
  in the MEM as the boundary proof.

---

## 9. Quality gates

Documentation/internal → unit/integration, SAST/DAST/SBOM, perf, IP, PII,
dep-confusion, test-first: `n/a`. hallucination-lint (refs resolve),
behavioral-reproducibility (deterministic), bolt-manifest-validation: `pass`.
prompt-injection, secret-leak: `pass` (no runtime surface).

---

## 10. Security and data

Governance/concept text only; no runtime boundary. The reframing **states** the
safe-default and independence guarantees (ADR-008); it does not implement
enforcement (later USs). Data `internal`.

---

## 11. Migration, compatibility, rollback

Additive concept alignment; no behavioral change; identifiers unchanged (so no
adopter breakage from this Bolt). Rollback: revert the kit commit; root untouched.

---

## 12. Risk matrix

| Risk | Prob | Impact | Mitigation |
|------|------|--------|------------|
| Concept edit bleeds into identifiers | 2 | 3 | AC-5 boundary check: identifier count unchanged; identifier form matched explicitly |
| Reframing dilutes a guarantee | 2 | 4 | AC-1 keeps every pause + states the safe-default invariant (ADR-008 §3.2); no checkpoint weakened |
| Four-agent drift | 2 | 3 | Byte-identical shared region; AC-4 sync + G-count |
| Over-reach into guardrails/schema | 1 | 2 | Scope §5 limits to concept prose; those are BOLT-002/003 |

---

## 13. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| Concept and identifiers as separate Bolts | Different phrase families; separating them keeps each ADR-005 sweep clean (the US-020 lesson) |
| Keep the word "HITL" as the named default case | ADR-008 §3.1 — HITL does not disappear; it becomes actor = human inside AITL |
| State (not enforce) the safe-default invariant | Enforcement is downstream US/Bolt work (Coordinator, validators); the precept must still state it |

---

## 14. Stop conditions

- The AC-5 identifier count differs before/after → concept edit leaked into
  identifiers; stop, revert the leak, re-verify.
- Any root `devflow/` file in the diff → stop, revert, record.
- A governed source changes materially (G15) → stop, revise, re-approve.
- Turn budget (10) exhausted before GREEN → stop, MEM with progress.

---

## 15. Definition of Done

- [ ] Phases A–C · AC-1..AC-7 pass
- [ ] GREEN (precept + charter + AITL definition reframed; identifier count unchanged; agents synced; kit-only)
- [ ] ADR-008 (§3.1/§3.2) + ADR-005 (boundary) + ADR-004 (kit-only) followed
- [ ] MEM (with the identifier before/after boundary proof) · manifest `v_bounces[]` appended
- [ ] HITL-MEM-Approval recorded

---

## 16. References

- US-021, US-021.BOLT-001 (approved); US-020 (delivered)
- ADR-008 §3.1 (precept), §3.2 (safe default); ADR-007 (actor); ADR-005 (sweep boundary); ADR-004 (kit-only)
- Avenga-DevFlow.md ~237–248 (foundational principle), ~1364–1368 (§3.0 Charter)

---

## 17. HITL-SPEC-Approval

> Draft until the Dev-validator records `HITL-SPEC-Approval`. A material source
> change invalidates it — stop, revise, re-approve (G15).

**Revision 1** — approved 2026-08-22T18:19:34-03:00 (eugenio.serrano,
dev_validator). Execution-time investigation then found "HITL" is pervasive
(3 categories; ~61 concept lines in the core) and the rev-1 boundary was
ambiguous about the category-2 adjective.

**Revision 2** — crisp 3-category boundary: BOLT-001 owns **only category 1**
(the precept-defining prose); the pervasive adjective (cat. 2) and identifiers
(cat. 3) both go to BOLT-004. No edits were made under rev 1; the V-Bounce
executes against rev 2.

| Field | Value (rev 2) |
|-------|-------|
| **review.reviewers** | eugenio.serrano (dev_validator) |
| **review.decision** | **approved** |
| **review_ready_at** | `2026-08-22T18:25:02-03:00` |
| **review.started_at** | `2026-08-22T18:27:05-03:00` |
| **review.decided_at** | `2026-08-22T18:27:05-03:00` |
