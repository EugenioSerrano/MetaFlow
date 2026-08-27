---
id: "ADR-002"
title: "Documentation-defect classification for the methodology repository"
date: "2026-08-21"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "accepted" # draft | accepted | rejected | deprecated | superseded
decision_makers: ["architect", "tech_lead"]
sources:
  - "devflow/reviews/REV-001-hitl-checkpoint-role-inventory.md"
  - "maintainer direction (2026-08-21)"
supersedes: []
conflicts_with: []
tags: ["maintainer-convention", "bug-classification", "governance"]
nfrs: []
waiver: # Only for gate-override ADRs (§3.6)
  gate: ""
  reason: ""
  owner: ""
  compensating_control: ""
  expires_at: ""
review_ready_at: "2026-08-21T02:35:48-03:00"
review: # HITL-ADR-Approval evidence — filled by the human reviewer (§3.0)
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - user: "eugenio.serrano"
      role: "architect"
  started_at: "2026-08-21T02:39:37-03:00"
  decided_at: "2026-08-21T02:39:37-03:00"
  findings: []
  acknowledged_without_comment: true # must be true when findings is empty (§3.0)
  acknowledgment_reason: "Reviewed the classification table against the REV-001 routing experience that motivated it (F-02..F-06 vehicle decisions): the BUG / REV->Bolt / US classes match the cases actually encountered, the default-to-REV->Bolt rule of thumb resolves ambiguity, and the explicit scope boundary (the kit's BUG contract for adopters is untouched; adopter-facing changes stay Bolt-shaped) preserves ADR-001's partition. Approved as drafted — serves future methodology-bug fixes and new-capability decisions."
---

# ADR-002 — Documentation-defect classification for the methodology repository

| Field          | Value |
|----------------|-------|
| **Status**     | draft |
| **Decision-makers** | eugenio.serrano (architect / tech_lead) |
| **Sources**    | REV-001 (approved — the routing ambiguity surfaced while classifying its findings), maintainer direction (2026-08-21) |
| **Supersedes** | None |
| **Conflicts with** | None — ADR-001 governs the two-tree layout; this ADR governs how we classify defects in the content of the product tree, without changing what adopters receive |

---

## 1. Context

This repository **builds** the methodology. That means the defects we
encounter are often **in the methodology itself**, not in a runtime product.
The kit's BUG flow (§2.16, §3.3.1) was designed for code defects: strict TDD,
a reproduction test, red→green evidence in one V-Bounce. When REV-001
surfaced F-02..F-06 — defects in the methodology's own role-routing rules —
we spent real time deciding the vehicle: BUG, REV→Bolt quality gap, or US.
The kit gives no guidance for this class, because adopters never face it:
an adopting team classifies defects in **its own product**; only the
maintainers of DevFlow classify defects in the **methodology itself**.

That distinction is the whole point of this decision: the classification
convention is a **maintainer-internal working rule**. It does not belong in
the distributable — adopters would receive a guide for a situation they
cannot have — and it must not change the kit's BUG definition, which is the
contract adopters operate under.

## 2. Alternatives considered

### Alternative A — Ship the guide in the kit (as a US → Bolt) (❌ Rejected)

Publish the classification guide as part of the distributable so adopters
"benefit" too.

| Aspect   | Detail |
|----------|--------|
| **Pros** | One canonical home; adopters could reuse it for their documentation bugs. |
| **Cons** | Adopters classify defects in their own product, not in the methodology — the guide's premise (defects *in the methodology*) cannot occur in an adopting project. It would pollute the distributable with maintainer-internal convention, contradicting the partition logic of ADR-001 (the kit holds only what adopters need). Rejected. |

### Alternative B — Amend the kit's BUG definition to cover methodology defects (❌ Rejected)

Change the BUG template/flow (red→green) so documentation defects fit.

| Aspect   | Detail |
|----------|--------|
| **Pros** | The BUG flow becomes more general. |
| **Cons** | It changes the contract every adopter operates under to solve a problem only the maintainers have. The red→green evidence semantics would need redefining for text (grep/diff "tests") in the distributable, adding complexity to the adopters' rules for zero adopter benefit. Rejected. |

### Alternative C — Internal ADR convention (✅ Selected)

Record the classification rule in this repository's decision log, where the
maintainers' other governing conventions live (ADR-001), without touching
the kit.

| Aspect   | Detail |
|----------|--------|
| **Pros** | The convention is binding for our own work, visible in the decision log, immutable once approved; the distributable stays clean; the kit's BUG contract is untouched. |
| **Cons** | It is a convention, not machinery — it governs by consultation, exactly like ADR-001's rules. |

---

## 3. Decision

This repository classifies defects **in the methodology itself** (the
content of `distribution-kit/` and the governance of building it) as
follows:

1. **BUG** — when the kit text **contradicts itself or an approved ADR**:
   the expected behavior is clear from another part of the kit or from a
   governing ADR, and the fix is a correction of the text. The BUG flow
   applies with **deterministic evidence** as the reproduction "test"
   (grep/diff before → after), instead of a runtime test.
2. **REV → Bolt** (quality gap, under US-000) — when the rule **works as
   written but is incomplete or blocking** for a class of teams (e.g. role
   routing that assumes roles which may not exist — REV-001 F-02..F-06).
   This is the default for design gaps in the methodology.
3. **US** — when the change **adds a new capability to the distributable**
   that adopters will use (e.g. a new family, a new tool contract).
4. **Nothing ships without a Bolt.** Whichever class applies, any change to
   the distributable still requires the full governed path
   (approved origin → Bolt → SPEC → V-Bounce → MEM → approvals), per
   ADR-001 rules 2 and 5.

This decision **does not modify the kit**: the BUG definition, templates and
flows that adopters receive remain exactly as shipped. Any future
adopter-facing clarification of the BUG flow is a separate Bolt.

## 4. Consequences

**Positive:**
- Classification is decided once and consulted afterwards — no more
  debating the vehicle when a methodology defect appears (the exact
  friction REV-001 triggered).
- The distributable stays clean: maintainer-internal conventions live in
  the decision log, not in the kit.
- The kit's BUG contract for adopters is untouched.

**Trade-offs:**
- It is a consultation convention, not an automated gate — it governs by
  being read (same class as ADR-001's rules).
- A future case may straddle two classes (e.g. a text contradiction that is
  also a design gap); the convention's rule of thumb is: defect → BUG,
  design gap → REV→Bolt, new capability → US, and when in doubt, prefer
  REV→Bolt (it surfaces findings before committing to a fix).

**Technical debt:**
- None introduced; this is a governance convention.

---

## 5. Applicable NFRs

None — this ADR defines a maintainer working convention, not a
non-functional requirement of the distributable.

---

## 6. References

- `devflow/adrs/ADR-001-repository-layout-methodology-and-product.md` — the
  two-tree partition this convention operates within.
- `devflow/reviews/REV-001-hitl-checkpoint-role-inventory.md` — the review
  whose finding-routing ambiguity motivated this decision.
- Kit §2.16 / §3.3.1 (BUG flow) and §5.15 (artifact routing) — referenced,
  not modified.

---

## 7. HITL-ADR-Approval

> **HITL-ADR-Approval** (Avenga DevFlow §2.8, §3.0, §3.5). An ADR does not
> become `accepted` — and therefore governing — without the approval of an
> Architect / Tech Lead. This ADR is the **source of truth for its own
> approval** (recorded in the `review` frontmatter block with review
> evidence); when it governs a SPEC revision, its path appears in that
> revision's `sources`. ADR approvals are never copied to the Bolt manifest.

| Field | Value |
|-------|-------|
| **Architect / Tech Lead** | eugenio.serrano |
| **Role** | architect |
| **Decision** | approved |
| **review_ready_at** | `2026-08-21T02:35:48-03:00` |
| **review.started_at** | `2026-08-21T02:39:37-03:00` |
| **review.decided_at** | `2026-08-21T02:39:37-03:00` |
| **Findings** | None — acknowledged_without_comment (reason in frontmatter `review:` block) |
