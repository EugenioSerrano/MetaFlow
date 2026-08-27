---
id: "US-014"
title: "Single-operator HITL operability — role routing stays as guidance, never as a blocker"
date: "2026-08-21"
llm: "claude-opus-4-8"
status: "approved" # draft | approved | deprecated
owner: "eugenio.serrano" # Functional Analyst (governs this US)
unit: ""
story_points: 8 # proposed (raised from 5 — scope broadened to the full single-operator operability policy); confirmed at HITL-US-Approval (§2.6)
adrs: [] # the durable decisions below are formalized via ADR(s) at implementation time (HITL-ADR-Approval); none created yet
sources:
  - "devflow/reviews/REV-001-hitl-checkpoint-role-inventory.md"
  - "devflow/adversarial-reviews/AREV-001-role-availability-blockers-sweep/03-VERDICT.md"
  - "devflow/adversarial-reviews/AREV-002-single-operator-sweep/03-VERDICT.md"
stakeholders: []
tags: ["roles", "routing", "hitl", "single-operator", "operability", "policy"]
review_ready_at: "2026-08-22T00:37:30-03:00"
review: # HITL-US-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "functional_analyst"}]
  started_at: "2026-08-22T00:37:30-03:00"
  decided_at: "2026-08-22T00:37:30-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved as the single-operator HITL operability policy. Business intent and the seven ACs accurately represent the maintainer decisions (D1-D7) confirmed 2026-08-22 and the findings routed from REV-001, AREV-001 and AREV-002. story_points confirmed at 8 (relative complexity of a policy spanning every named-role route + AREV machinery + counting convention). Decomposed into Bolts, not sub-USs; the durable decisions are formalized via ADR at implementation. Only then decomposable."
---

# US-014 — Single-operator HITL operability: role routing stays as guidance, never as a blocker

| Field          | Value |
|----------------|-------|
| **Unit**       | — |
| **ADRs**       | — (durable decisions formalized via ADR at implementation) |
| **Status**     | approved (HITL-US-Approval 2026-08-22) |
| **Story points** | 8 (confirmed) |

**As an** adopting team of any size — down to a single maintainer, **I want**
every HITL checkpoint to be approvable by the qualified human(s) actually
present, with the named role kept as guidance rather than as a gate, **so
that** no checkpoint is structurally unsatisfiable and the methodology can be
run end-to-end by one person.

---

## 1. The problem (explained, complete)

The methodology routes every approval to **named roles** (Functional Analyst,
Architect, Tech Lead, QA, Sec, SRE, Dev-validator, PO/PM, Stakeholders). The
rules were written assuming a team large enough to fill them. Three approved
governance passes established that this assumption breaks the methodology for
small teams:

- **REV-001** (approved, closed) inventoried the 15 checkpoints and found the
  role-availability family: non-functional BUG routing, acceptance pairing,
  multi-approver MEM counts, two-role TC, role multiplicity, and the SPEC
  counting gap (F-02..F-06).
- **AREV-001** (Verdict approved, FAIL) confirmed them as structural blockers
  and reclassified the single-role gates (US/ADR/UNIT/UAT) as dependent on an
  undefined role-multiplicity policy.
- **AREV-002** (Verdict approved, FAIL) added the operability layer: the
  single-role-gate enumeration is incomplete, the AREV mechanism dead-ends
  for a solo operator, and the operability principle itself is stated
  nowhere.

**Shared root cause (named by all three):** the methodology defines *who*
should approve, but never *what happens when that who has no holder* — and it
has no governing statement that availability must never block.

This US consolidates that whole family into one policy, per maintainer
direction (2026-08-22): keep the role information as guidance, remove every
role-availability *block*, and make the methodology operable by one person.

---

## 2. The decisions (maintainer policy, 2026-08-22)

> These are the durable decisions this US records. They are **formalized via
> ADR(s) at `HITL-ADR-Approval`** and **implemented in the kit via Bolt(s)**
> (`distribution-kit/` only, ADR-004; the root receives them at the next
> §5.16 migration). No ADR or Bolt is created by this US itself — each keeps
> its own checkpoint.

**D1 — Operability principle (governing default).** Role routing *informs who
should review*; **availability never blocks**. Every HITL checkpoint is
satisfiable by the qualified human(s) actually present. The named role is
preserved everywhere as **guidance and information** — it is never removed —
but it is never a gate. New checkpoints inherit this default by construction.

**D2 — Role multiplicity and self-assignment.** One person may hold several
roles simultaneously. When a person approves acting in a role they hold, the
approval **records which role was self-assigned** (e.g. "approved as QA:
eugenio.serrano"), until the team roster (US-001) provides the resolution
layer. Role assignment is living data, not a decision requiring approval.

**D3 — No role-availability blocks on any route.** The role requirement is
removed as a *block* on every checkpoint — including the routes AREV-001
confirmed: the `critical` non-functional BUG route, the `infra`/`hardening`
acceptance pairing (SRE/Sec), the two-role TC, and the single-role gates
(US, ADR — and, once reintroduced, UNIT/UAT). The available person approves,
recording the role. **The only exceptions kept are the identity-separation
rules** (they are about a *different person/model*, not a *different role*),
which stay intact: the handoff incoming-executor rule, G37 Judge-model
neutrality, and G18/G24 (no AI self-approval, no fabricated reviewer). The
no-holder fallback must never dissolve these, or "no holder" becomes a
self-approval loophole (AREV-001 F-09, AREV-002 F-06).

**D5 — AREV operability for a single operator.** An AREV requires **at least
three models** available (so Critique, Defense and Verdict each run on a
distinct model and G37 neutrality is met). A single human operator running
three models is valid; the human approves the three AREV documents but does
**not** act as arbiter — the third model arbitrates. The two-model
**human-arbiter** fallback is **removed**. A **`cancelled`** terminal state is
added to the AREV status vocabulary (§3.15) — through its own governed change,
so the table is amended before any document uses the value (G39) — so an
initiated AREV that cannot proceed can be closed instead of living in limbo.

**D7 — No risk-based approver counts.** The risk-based minimum-approver counts
are removed. **The DEV who takes the Bolt is responsible for finishing it and
approving its MEM** (one approver; after a recorded handoff, the incoming
executor). SPEC and UAT approvals likewise have a **minimum of one** approver;
any additional named roles are guidance, not a required quorum.

---

## 3. Complete single-role-route enumeration (AREV-002 F-01 — the completeness checklist)

D1–D3 apply to **every** named-role route, not only those AREV-001 listed.
The implementing ADR/Bolt must cover all of them (methodology §3.0 table,
`GUARDRAILS.md` checkpoint map + work-category table, **and the four agents'
compact HITL tables** — the runtime layer where drift survives, AREV-001
F-01's lesson):

| Checkpoint / route | Named role today (kept as guidance) |
|--------------------|-------------------------------------|
| `HITL-US-Approval` | Functional Analyst |
| `HITL-BUG-Approval` (functional) | Functional Analyst |
| `HITL-BUG-Approval` (non-functional `critical`) | Architect / Tech Lead |
| `HITL-TC-Approval` | QA + domain/technical owner |
| `HITL-BOLT-READY-Approval` | FA / Architect-TL / QA Lead-QA Automation Lead-Architect-TL |
| `HITL-ADR-Approval` | Architect / Tech Lead |
| `HITL-SPEC-Approval` | Dev-validator + domain owner(s) |
| `HITL-MEM-Approval` | Executing Dev-validator (+ QA/Sec by risk — removed by D7) |
| `HITL-BOLT-DONE-Approval` (feature) | PO / PM |
| `HITL-BOLT-DONE-Approval` (work_category) | `infra`→TL+SRE · `hardening`→TL+Sec · `refactor`/`debt`→TL · `qa_automation`→QA Lead |
| `HITL-UNIT-Approval` / `HITL-UAT-Approval` | Tech Lead / Stakeholders — **out of scope here (routed to US-015)** |

> Completeness verification for the implementing Bolt: grep every Owner cell
> in the three tables and the four agents that names exactly one role/class
> with no fallback; each must carry the D1 guidance-not-gate treatment.

---

## 4. Acceptance criteria

- **Given** any HITL checkpoint and a team missing the named role, **When** an
  approval is due, **Then** the qualified human present may record it, and the
  approval captures the self-assigned role (D1, D2) — no route is a dead end.
- **Given** the role information in every text, **When** the policy is
  applied, **Then** the named role is still stated as guidance/recommendation
  everywhere it appears (nothing is lost) but never as a block (D1, D3).
- **Given** a `critical` non-functional BUG, a `high`/`critical` MEM, an
  `infra`/`hardening` acceptance, or a TC, in a one-person team, **When**
  approval is due, **Then** the available person approves it with recorded
  evidence — none of these routes blocks (D3, D7).
- **Given** a Bolt taken by a DEV, **When** its MEM is due, **Then** that DEV
  approves it (one approver; incoming executor after a handoff), with no
  risk-based multi-approver requirement (D7).
- **Given** SPEC and UAT approvals, **When** the count is checked, **Then**
  the minimum is one approver; extra roles are guidance (D7).
- **Given** an AREV, **When** it is initiated, **Then** it requires ≥3 models
  (a single operator running three models is valid); the human approves the
  three documents but does not arbitrate; and an AREV that cannot proceed can
  be set `cancelled` (D5).
- **Given** the identity-separation rules (handoff incoming-executor, G37,
  G18/G24), **When** the no-holder fallback is applied, **Then** those rules
  are explicitly excluded and remain intact (D3).
- **Given** the complete single-role-route enumeration (§3), **When** the
  implementing Bolt runs, **Then** every route — including the four agents'
  HITL tables — carries the guidance-not-gate treatment (AREV-002 F-01).

## 5. Findings resolved by this US

| Finding | What it becomes here |
|---------|----------------------|
| REV-001 F-03, F-04, F-05, F-06 | D3 (acceptance/MEM/TC), D2 (multiplicity) |
| AREV-001 F-02 (critical BUG route, untracked) | D3 — now owned and unblocked |
| AREV-001 F-03 (MEM counts) | D7 |
| AREV-001 F-04 (infra/hardening SRE/Sec) | D3 |
| AREV-001 F-05 (two-role TC) | D3 |
| AREV-001 F-06 (single-role gates — US/ADR part) | D1/D3 (UNIT/UAT part → US-015) |
| AREV-001 F-07 (SPEC counting) | D7 |
| AREV-002 F-01 (incomplete enumeration) | §3 checklist |
| AREV-002 F-02 (AREV mechanism dead-end) | D5 |
| AREV-002 F-04 (operability principle absent) | D1 |

## 6. Notes / to refine before approval

- **Vehicle chain:** this US (policy) → `HITL-US-Approval` → ADR(s) that
  formalize D1–D7 as durable constraints (`HITL-ADR-Approval`) → kit Bolt(s)
  under US-000 that implement them in `distribution-kit/` (`HITL-BOLT-READY`
  → SPEC → V-Bounce). Nothing is created by this US; each step keeps its own
  checkpoint.
- **Story points:** raised 5 → 8 to reflect the broadened scope. If the FA
  prefers, it may be split at approval (e.g. role policy · AREV operability ·
  counting convention); kept consolidated per maintainer direction. A
  possible split into ~2–4 Bolts is the plausibility band for 8 SP.
- **Companion USs:** US-001 (team roster) is the optional resolution layer for
  D2 (records who holds each role, including external reviewers); US-015 owns
  the UNIT/UAT topic (D3's UNIT/UAT portion is deferred there).
- **Related BUG:** the stale copies of the old BUG route (AREV-001 F-01) are a
  separate class-1 documentation defect fixed via its own BUG, not this US.
- **Boundary:** identity-separation rules are preserved, not relaxed (D3).

## 7. HITL-US-Approval

> **Avenga DevFlow §2.6, §3.0.** This US remains a draft until the Functional
> Analyst records `HITL-US-Approval` (in the `review` frontmatter block),
> confirming the business intent, the ACs and the `story_points`. Only then
> may it be decomposed into Bolts. Approval of this US does not approve any
> ADR, Bolt, SPEC or downstream artifact — each keeps its own checkpoint.

| Field | Value |
|-------|-------|
| **Functional Analyst** | eugenio.serrano |
| **Decision** | approved |
| **story_points (confirmed)** | 8 |
| **review_ready_at** | `2026-08-22T00:37:30-03:00` |
| **review.started_at** | `2026-08-22T00:37:30-03:00` |
| **review.decided_at** | `2026-08-22T00:37:30-03:00` |
