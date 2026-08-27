---
id: "SPEC-260824-1423"
title: "The delete-safe consistency contract in squad/README.md — the N:1 cardinality pinned, the reference-check procedure and the edge cases"
date: "2026-08-24"
author: "eugenio.serrano"
llm: "claude-fable-5"
status: "approved" # draft | approved | blocked | obsolete — AITL-SPEC-Approval 2026-08-24
origin: "US-025"
bolt: "US-025.BOLT-003"
revision: 1
associated_adrs:
  - "devflow/adrs/ADR-013-agent-lifecycle-governance.md"
  - "devflow/adrs/ADR-014-actors-roster-is-the-enablement.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
prerequisites:
  - "devflow/spec/SPEC-260824-1101-mainagent-lifecycle-body.md" # the Delete flow this contract deepens (hash reference)
  - "devflow/spec/SPEC-260824-1144-per-platform-lifecycle.md" # the install surface the invariants span
risk_class: "low"
autonomy_level: "L3"
turn_budget: ""
data_classification: "internal"
review_ready_at: "2026-08-24T14:25:17-03:00"
review: # AITL-SPEC-Approval — decision dictated in conversation ("aprobado!") and transcribed by the agent (§3.0)
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-24T14:38:23-03:00"
  decided_at: "2026-08-24T14:38:23-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved as Dev-validator after an independent cross-model SPEC review (no blocking findings): the three READY observations verified resolved (the N:1 cardinality pinned with the three delete semantics; the contract opening with the shared body's own check order + the never-ship-a-rival-text stop condition; the one-line pointer), the payload's delete-semantics mapping checked against the shared body. The reviewer's one new observation adopted pre-stamp: wrapper naming pinned to the actor id (per-instance) — definition-named wrappers would collide in the spawn folder under N:1. Authorizes the V-Bounce (revision 1)."
---

# SPEC-260824-1423 — The delete-safe consistency contract

| Field | Value |
|-------|-------|
| **Origin** | US-025 (approved 2026-08-24) |
| **Bolt** | US-025.BOLT-003 (READY 2026-08-24, risk low) |
| **ADRs** | ADR-013 (bounds), ADR-014 (roster = membership authority), ADR-004 |
| **Risk Class** | low |
| **Revision** | 1 |

---

## 1. Objective

Write the **lifecycle consistency contract** the shared body's Delete flow
points at: the four-leg invariants with the **N:1 cardinality pinned**
(the READY reviewer's substantive observation — without it, "solo su
wrapper" is ambiguous under definition reuse), the concrete reference-check
procedure, and the edge cases — in `agents/squad/README.md`, the operating
surface. If not implemented, "never break a referenced definition" stays a
declared intention without a checkable procedure, and an adopter's
Coordinator improvises the check.

## 2. Context

BOLT-001 declared the Delete flow ("check `roster.yaml` and the actor
files first"); BOLT-002 fixed the install surface. This SPEC writes the
contract both point at. Covers US-025 **AC-4** and anchors AC-3's
consistency legs.

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | US-025.BOLT-003 | AITL-BOLT-READY-Approval ✓ (2026-08-24T14:23:28) |
| Feature US | US-025 | AITL-US-Approval ✓ |
| ADR | ADR-013 / ADR-014 / ADR-004 | AITL-ADR-Approval ✓ |
| Repository baseline | `ee22639` | — |

## 4. Scope

### In scope
- `distribution-kit/devflow/agents/squad/README.md` — the contract (Phase A).
- `distribution-kit/devflow/agents/README.md` — one pointer line (Phase B).

### Out of scope
- The four MainAgents (hash-locked); `actors/` files; any tooling/automation
  of the check (US-012 family later); BOLT-004/005.

## 5. Prerequisites and baseline

- Baseline `ee22639` (BOLT-002's V-Bounce committed; tree clean).
- The shared-body hash reference `cd24754c320d…` (the pinned §8 convention
  of SPEC-260824-1101).

## 6. Phases

### Phase A — The contract (the payload, appended to `squad/README.md`)

**Duration:** ~1.5h — **Complexity:** Low

Append the following section to `agents/squad/README.md` (after the
existing "Reuse is expected…" paragraph). The content blocks are
contractual; wording may take micro-edits at review.

> ## The lifecycle consistency contract
>
> Every lifecycle act (install · create · delete) must leave the four
> legs agreeing — and under N:1 reuse the **cardinality matters**:
>
> - **Every installed wrapper belongs to ONE actor-instance** and points
>   at one live definition in `squad/` — two actors sharing a definition
>   have **two wrappers** (each with its own actor `id` and per-instance
>   model). **Wrapper files are named by the actor `id`** — under N:1,
>   two actors produce two distinctly-named wrappers (naming by the
>   definition would collide in the spawn folder).
> - **Every definition in `squad/`** has its row in [`../INDEX.md`](../INDEX.md)
>   and **≥1 actor** referencing it — zero referencing actors makes it a
>   deletion candidate (or it gets flagged; never a silent ghost).
> - **Every agent actor** (`devflow/actors/<id>.yaml` with a
>   `definition:`) is **listed in `roster.yaml`** — an unlisted actor file
>   is not in the team: flag it to the human, never silently adopt it.
>
> **The reference check (before any delete)** — per the shared body:
> check `roster.yaml` and the actor files first. Concretely: enumerate
> every actor file whose `definition:` points at the target
> `squad/<id>/agent.yaml`, and each one's `roster.yaml` listing. Then:
>
> - **Deleting an actor** removes ITS wrapper, its actor file and its
>   roster listing — the definition stays while ANY other listed actor
>   references it.
> - **The definition falls only at zero**: when the enumeration finds no
>   remaining referencing actor, the definition (and its INDEX row) may
>   go with it.
> - **Wrapper-only removal is legitimate**: the actor stops being
>   spawnable on that platform until reinstalled; the definition and the
>   roster entry stay.
>
> **Edge cases:**
>
> - *Shared definition (N:1):* deleting one actor removes its wrapper +
>   actor file + listing; the definition and the other actors' wrappers
>   stay.
> - *The last actor:* the enumeration hits zero — the definition and its
>   INDEX row may go with it.
> - *Orphans* (a wrapper without a definition; a definition without an
>   INDEX row): repair toward the invariants — reinstall or list — or
>   remove; never leave a leg dangling.
> - *An unlisted actor file:* outside the team (`roster.yaml` is the
>   membership authority) — flag it to the human; the lifecycle never
>   adopts it silently.

### Phase B — The pointer (one line in `agents/README.md`)

**Duration:** ~10min — **Complexity:** Low

Add to the README's **Rules** section:

> - **Delete is checked, never blind** — the lifecycle consistency
>   contract (the N:1 reference check and the four-leg invariants) lives
>   in [`squad/README.md`](squad/README.md).

Kept to one line deliberately (the future US-023 docs Bolts touch this
file — minimal collision surface).

### Phase C — Verification

**Duration:** ~30min — **Complexity:** Low

(1) **The contract-vs-body read-through** (the reviewer's second
observation): the contract must not contradict the shared body's Delete
wording — it opens with the body's own order ("check `roster.yaml` and
the actor files first", quoted) and only *concretizes* it; any semantic
divergence found → stop and reconcile. (2) The pinned-hash gate: the
shared lifecycle section ×4 still equals `cd24754c320d…` (the four
MainAgents untouched). (3) Self-containment: the two touched files carry
0 maintenance IDs. (4) The contract's cross-references resolve
(`../INDEX.md`, `roster.yaml`, `devflow/actors/`). (5) No BOM.

## 7. Acceptance criteria

### AC-1: The contract present and cardinality-unambiguous
**Given** `squad/README.md`, **When** read, **Then** it states the three
invariants with the N:1 cardinality explicit (wrapper = actor-instance;
definition falls only at zero referencing actors), the concrete check
procedure, and the four edge cases.

### AC-2: No contradiction with the shared body
**Given** the contract and the MainAgents' Delete flow, **When** compared,
**Then** the contract concretizes — never contradicts — the body (same
check order, same never-break rule), and the four MainAgents hash
unchanged (`cd24754c320d…`).

### AC-3: The pointer, minimal
**Given** `agents/README.md`, **When** read, **Then** exactly one new
Rules line points at the contract.

### AC mapping to source

| Source AC | How this SPEC satisfies it | Verifying evidence |
|-----------|----------------------------|--------------------|
| US-025 AC-4 | The check procedure + never-break + roster/INDEX consistency, written and checkable | AC-1 + the read-through |
| US-025 AC-3 (anchoring) | The create-flow legs (INDEX + roster listing) are now invariants | AC-1 |

## 8. Testing strategy

Scripted evidence: the pinned-hash comparison ×4 (the SPEC-1101 §8
convention, reference `cd24754c320d…`); content checks on the two files
(the invariants/procedure/edge-case markers present; exactly one new line
in agents/README); the maintenance-ID sweep on both; BOM. The
read-through is a recorded manual check (quoted-order match).

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration / SAST / perf | n/a — documentation Bolt | n/a |
| Prompt-injection scan | family docs, no triggerable directives | pass expected |
| Secret-leak scan | no secrets | pass expected |
| Hallucination lint | the contract's cross-references resolve | pass expected |
| IP / license provenance | kit-original text | pass expected |
| PII / DLP | internal docs | pass expected |
| Dependency-confusion | n/a | n/a |
| Test-first evidence | the §8 checks defined before execution | pass expected |
| Behavioral reproducibility | hash/sweep checks re-run identically | pass expected |
| Bolt-manifest validation | v_bounces[1] appended, schema PASS | pass expected |

## 10. Security and data

Internal docs. The contract itself is a control: it closes the
silent-adoption path (an unlisted actor file never enters the team) and
makes definition removal a zero-references decision, not a judgment call.

## 11. Monitoring and observability

n/a — documentation family.

## 12. Migration, compatibility and rollback

- **Migration:** framework-file supersede on upgrade (§5.16).
- **Compatibility:** additive; consistent with the shipped flows.
- **Rollback:** `git revert` of the V-Bounce commit.

## 13. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| Contract contradicts the shared body | 2 | 3 | The read-through (AC-2) + quoting the body's own check order |
| Touching the MainAgents by accident | 1 | 4 | The pinned-hash gate |
| Collision with the future US-023 docs Bolts | 2 | 1 | The one-line pointer; the contract lives in squad/README (not their main target sections) |

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| The cardinality pinned as invariant #1 (wrapper = actor-instance) | The READY reviewer's observation: under N:1 a reader could believe one wrapper serves all actors of a definition — the delete semantics collapse without this line |
| The contract opens by quoting the shared body's check order | Kills the order-inversion friction the reviewer flagged; the contract is visibly a concretization, not a rival text |
| The contract lives in squad/README, not agents/README | The operating surface (where the Coordinator works); agents/README keeps one pointer — minimal collision with the sequenced US-023 docs Bolts |
| Wrapper naming pinned to the actor `id` (reviewer's SPEC-pass observation) | The natural termination of the cardinality pin: definition-named wrappers would collide in the spawn folder the moment two actors share a definition on one platform |

## 15. Stop conditions

- The read-through finds a semantic divergence with the shared body →
  stop, reconcile (never ship a rival text).
- Any need to touch a MainAgent or an actors/ file → stop (wrong Bolt).

## 16. Definition of Done (DoD)

- [ ] Phases A–C implemented
- [ ] AC-1..AC-3 pass (evidence recorded)
- [ ] Applicable gates pass / n/a per §9
- [ ] MEM created in `devflow/memory/` (exactly one)
- [ ] Manifest `v_bounces[]` entry appended
- [ ] AITL-MEM-Approval recorded

## 17. References

- US-025 · US-025.BOLT-003 (READY) · ADR-013 · ADR-014 §3.8/§3.9 ·
  SPEC-260824-1101 (the Delete flow + hash reference) · SPEC-260824-1144
  (the install surface).

## 18. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-24 | eugenio.serrano (agent-drafted) | Revision 1 |

## 19. AITL-SPEC-Approval

> Draft until the Dev-validator records `AITL-SPEC-Approval` (frontmatter
> `review:` block). SPEC approval authorizes the code-run / V-Bounce (G14).

| Field | Value |
|-------|-------|
| **review.reviewers** | `human:eugenio.serrano` (dev_validator) |
| **review.decision** | **approved** |
| **review_ready_at** | `2026-08-24T14:25:17-03:00` |
| **review.started_at** | `2026-08-24T14:38:23-03:00` |
| **review.decided_at** | `2026-08-24T14:38:23-03:00` |
| **Findings** | none blocking — the reviewer's naming observation adopted pre-stamp (reason in the frontmatter `review:` block) |
