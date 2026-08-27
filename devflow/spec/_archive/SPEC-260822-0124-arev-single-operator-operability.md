---
id: "SPEC-260822-0124"
title: "AREV single-operator operability — three-model requirement, no human arbiter, cancelled state"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
status: "approved" # draft | approved | blocked | obsolete
origin: "US-014"
bolt: "US-014.BOLT-002" # ⚠️ MANDATORY
revision: 1
associated_adrs:
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
prerequisites: []
risk_class: "medium"
autonomy_level: "L3"
turn_budget: ""
data_classification: "internal"
review_ready_at: "2026-08-22T01:24:58-03:00"
review: # HITL-SPEC-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "dev_validator"}]
  started_at: "2026-08-22T01:27:10-03:00"
  decided_at: "2026-08-22T01:27:10-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Reviewed revision 1 against US-014 (approved), the Bolt US-014.BOLT-002, AREV-002 F-02 and ADR-004: the D5 approach (≥3-model requirement, removal of the human-arbiter fallback, `cancelled` state added table-first per G39) is faithful and the recorded AREV-001/002 history is correctly left untouched. Approved as drafted — authorizes the V-Bounce."
---

<!--
  LANGUAGE POLICY (§3.15): schema in English; prose in content_language (en).
  Kit-only edits (ADR-004); root untouched. ⚠️ G39: the §3.15 AREV status
  vocabulary table is amended BEFORE any document uses `cancelled`.
-->

# SPEC-260822-0124 — AREV single-operator operability

| Field | Value |
|-------|-------|
| **Origin** | [US-014](../functional/user-stories/US-014-role-availability-policy.md) (approved) |
| **Bolt** | [US-014.BOLT-002](../functional/bolts/US-014.BOLT-002-arev-single-operator-operability.md) (approved) |
| **ADRs** | [ADR-004](../adrs/ADR-004-repository-partition-v2.md) (kit-only) |
| **Risk Class** | medium |
| **Revision** | 1 |

---

## 1. Objective

Implement **D5** of US-014 in the distributable: make the Adversarial Review
mechanism operable and terminable by a single operator who has **at least three
models**. Concretely: (1) state the **≥3-model requirement** for running an
AREV; (2) **remove the two-model human-arbiter fallback** — the human approves
the three AREV documents but does not arbitrate, the third model does; and (3)
add a **`cancelled`** terminal state to the AREV status vocabulary so an
initiated AREV that cannot proceed can be closed instead of living in limbo.

**If not implemented:** the AREV mechanism remains the AREV-002 F-02 trap — an
initiated AREV with no lawful Verdict path and no exit state.

---

## 2. Context

US-014 (approved) records D5. AREV-002 F-02 (Verdict approved) confirmed the
trap: §2.15 makes all three phases mandatory once initiated; §3.13 makes the
two-model fallback nominate a human who cannot exist in a single-operator team;
§3.15 has no terminal state for abandonment. This Bolt closes all three. The
change is kit-only (ADR-004); the root receives it at the next §5.16 migration.

---

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | `devflow/functional/bolts/US-014.BOLT-002-arev-single-operator-operability.md` | HITL-BOLT-READY-Approval ✓ (2026-08-22T00:53:56-03:00) |
| Parent US | `devflow/functional/user-stories/US-014-role-availability-policy.md` | HITL-US-Approval ✓ |
| Evidence | `devflow/adversarial-reviews/AREV-002-single-operator-sweep/03-VERDICT.md` (F-02) | HITL-AREV-VERDICT-Approval ✓ |
| ADR | `devflow/adrs/ADR-004-repository-partition-v2.md` | HITL-ADR-Approval ✓ |
| Repository baseline | branch `4.2`, HEAD `0c7f40d` (working tree: US-014 package uncommitted) | — |

Pre-SPEC evidence gate: **all governed sources approved**.

---

## 4. Scope

### In scope (`distribution-kit/`)

- **§2.15** (AREV "once initiated…mandatory and sequential"): add that running
  an AREV **requires ≥3 models available** (a single operator running three
  models is valid); an AREV that cannot meet this is not initiated (or, if
  already initiated, is set `cancelled`).
- **§3.13** (two-model fallback, ~current lines 3275–3281): **remove** the
  "qualified human arbitrates the Verdict / `judge_model: human:<…>`" fallback;
  restate that the Judge is always a third model distinct from the implementor
  and the Challenger, and the human approves the three AREV documents but does
  not arbitrate.
- **§3.15** AREV status row: add **`cancelled`** as a terminal state
  (`draft · in-progress · active · closed · cancelled`) — **the table is
  amended first (G39)**; note when it applies (an initiated AREV that cannot
  reach a Verdict).
- **`GUARDRAILS.md`** G37 (and G25 context): align with "Judge = third model;
  ≥3 models required; no human-arbiter fallback".
- **The four agents' AREV sections** (Judge-neutrality / "once initiated"
  text): identical alignment.
- **AREV templates:** `TEMPLATE-AREV.md` status enum (+`cancelled`);
  `TEMPLATE-03-VERDICT.md` `judge_model` guidance (drop the `human:<…>`
  two-model fallback, state the ≥3-model rule).

### Out of scope

- D1/D2/D3 (US-014.BOLT-001, Done); D7 (US-014.BOLT-003).
- The already-recorded AREV-001/AREV-002 documents (history — a past human
  Verdict stays valid; this changes the rule going forward, not the record).
- The root `devflow/` tree (ADR-004).

---

## 5. Prerequisites and baseline

- US-014 approved; US-014.BOLT-002 approved (readiness).
- Four agents in sync before the edit; pre-existing drift → stop, reconcile.
- Baseline: branch `4.2`, HEAD `0c7f40d`.

---

## 6. Phases

### Phase A — §3.15 vocabulary first (G39)

**Duration:** ~0.3h — **Complexity:** Low

Amend the §3.15 AREV status row to `draft · in-progress · active · closed ·
cancelled`, with a note that `cancelled` is the terminal state for an initiated
AREV that cannot proceed (e.g. fewer than three models and no qualified
arbiter). Add `cancelled` to `TEMPLATE-AREV.md`'s `status` enum. **This precedes
any use of the value (G39).**

### Phase B — §2.15 three-model requirement

**Duration:** ~0.3h — **Complexity:** Low

State in §2.15 that initiating an AREV requires ≥3 models (Critique, Defense and
Verdict each on a distinct model); a single operator running three models is
valid; an AREV that cannot meet this is not initiated, or is set `cancelled` if
already open.

### Phase C — §3.13 remove the human-arbiter fallback

**Duration:** ~0.5h — **Complexity:** Medium

Rewrite the §3.13 two-model passage: the Judge is always a third model distinct
from the implementor and the Challenger (G37); the human approves the three
AREV documents but does not arbitrate; **remove** the "with only two models…a
qualified human arbitrates / `judge_model: human:<…>`" fallback. Update G37 (and
G25 context) in `GUARDRAILS.md` and the four agents' AREV sections to match.
Update `TEMPLATE-03-VERDICT.md`'s `judge_model` guidance.

### Phase D — Verification (GREEN)

**Duration:** ~0.4h — **Complexity:** Low

Run the §8 suite.

---

## 7. Acceptance criteria

### AC-1: ≥3-model requirement stated
**Given** the edited kit, **When** grepping §2.15/§3.13, **Then** the ≥3-model
requirement for running an AREV is stated (single operator with three models valid).

### AC-2: human-arbiter fallback removed
**Given** the edited kit, **When** grepping for "qualified human arbitrates" /
"`judge_model: human`" in §3.13, G37, the four agents and the VERDICT template,
**Then** the two-model human-arbiter fallback is gone; the Judge is a third
model distinct from implementor and Challenger.

### AC-3: `cancelled` state added (G39 order)
**Given** the edited kit, **When** grepping the §3.15 AREV status row and the
AREV template status enum, **Then** `cancelled` is present as a terminal state,
and the table amendment precedes any document using it.

### AC-4: G37/G25 + four agents consistent
**Given** the edited kit, **When** reading G37/G25 and the four agents' AREV
sections, **Then** they state the ≥3-model rule and no human-arbiter fallback,
consistently.

### AC-5: four-agent sync + G-count
Whole-body diff = sanctioned divergence only; G-count 39/39/39/39; GUARDRAILS 39.

### AC-6: root untouched
`git status` shows only `distribution-kit/` + governance records.

### AC-7: Bolt-manifest validation
0 errors.

### AC mapping to source

| US-014 AC | How satisfied | Evidence |
|-----------|---------------|----------|
| AC-6 (AREV ≥3 models, human approves not arbitrates, `cancelled`) | Phases A/B/C | AC-1, AC-2, AC-3 |

---

## 8. Testing strategy

Deterministic, no runtime:
- Grep the ≥3-model rule (AC-1), the absence of the human-arbiter fallback (AC-2),
  the `cancelled` state (AC-3), and G37/agent consistency (AC-4).
- Four-agent whole-body diff + `grep -cE '^\| G[0-9]{2} '` = 39 (AC-5).
- `git status --short` (AC-6); manifest schema validation (AC-7).
- Edge cases: G39 ordering (table amended before use — verified by grep that no
  live AREV uses `cancelled`); the AREV template status enum comment;
  CRLF/LF normalization for the sync diff.

---

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | — | `n/a` — documentation-only |
| SAST / SBOM | — | `n/a` |
| Perf-smoke | — | `n/a` |
| Prompt-injection | — | `pass` |
| Secret-leak | — | `pass` |
| Hallucination lint | — | `pass` — every §-reference/path resolves |
| IP / license | — | `n/a` |
| PII / DLP | — | `n/a` — internal |
| Dependency-confusion | — | `n/a` |
| Test-first evidence | — | `n/a` — not a BUG Bolt |
| Behavioral reproducibility | — | `pass` — deterministic grep/diff |
| Bolt-manifest validation | — | `pass` |

---

## 10. Security and data

Governance-mechanism text only; no security boundary or data path. Removing the
human-arbiter fallback **strengthens** Judge neutrality (always a third model),
never weakens it. Data `internal`.

---

## 11. Monitoring and observability

`n/a` — no runtime. The §8 suite is the observability; captured in the MEM.

---

## 12. Migration, compatibility and rollback

- **Migration:** none here; adopters receive it at their next §5.16 migration.
- **Compatibility:** a new terminal status value is added (validators must accept
  `cancelled` for AREV) — the §3.15 table is the normative source, amended
  first. G-count unchanged.
- **Rollback:** revert the kit commit(s); root untouched.

---

## 13. Risk matrix

| Risk | Prob | Impact | Mitigation |
|------|------|--------|------------|
| `cancelled` used before the table is amended (G39) | 1 | 3 | Phase A first; AC-3 checks order |
| A human-arbiter mention left behind | 2 | 3 | AC-2 greps all locations (§3.13, G37, agents, VERDICT template) |
| Four-agent drift | 2 | 3 | Identical edits; AC-5 |
| Root edited by mistake | 1 | 4 | Kit-only; AC-6 |

---

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| Require ≥3 models, drop the human-arbiter fallback | Maintainer D5: a genuine third model guarantees neutrality; the human-arbiter path is unsatisfiable for a solo operator and weaker on neutrality |
| Add `cancelled` rather than reuse `closed` | `closed` means "findings routed"; an abandoned AREV produced no Verdict, so it needs a distinct terminal state |
| Amend §3.15 table first (G39) | A status value must exist in the vocabulary before any document uses it |
| Leave recorded AREV-001/002 as-is | History; the rule changes forward, not the record |

---

## 15. Stop conditions

- Pre-existing four-agent drift before Phase C → stop, reconcile, record.
- Any root `devflow/` methodology file in the diff → stop, revert, record.
- A human-arbiter mention cannot be removed without breaking G37's meaning → stop, reassess.
- A governed source changes materially (G15) → stop, revise, re-approve.

---

## 16. Definition of Done (DoD)

- [ ] Phases A–D implemented (A before any use of `cancelled` — G39)
- [ ] AC-1..AC-7 pass
- [ ] Verification GREEN (≥3-model rule; no human-arbiter; `cancelled` present; sync 39×5; root untouched; manifest 0 errors)
- [ ] Follows ADR-004 (kit-only)
- [ ] Gates pass / n/a per §9
- [ ] MEM created (exactly one per V-Bounce)
- [ ] Manifest `v_bounces[]` entry appended
- [ ] HITL-MEM-Approval recorded

---

## 17. References

- US-014 (approved), US-014.BOLT-002 (approved), AREV-002 Verdict (F-02)
- ADR-004 (kit-only), AGENTS.md (four-agent sync)
- §2.15, §3.13, §3.15 (AREV machinery); G25, G37

---

## 18. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-22 | eugenio.serrano | Initial revision 1 (draft) |

---

## 19. HITL-SPEC-Approval

> **Avenga DevFlow §2.4.1, §3.0.** Draft until the Dev-validator records
> `HITL-SPEC-Approval`. Bolt approval authorizes SPEC preparation; **SPEC
> approval** authorizes the V-Bounce. A material source change invalidates
> this approval — stop, revise, re-approve (G15).

| Field | Value |
|-------|-------|
| **review.reviewers** | eugenio.serrano (dev_validator) |
| **review.decision** | approved |
| **review_ready_at** | `2026-08-22T01:24:58-03:00` |
| **review.started_at** | `2026-08-22T01:27:10-03:00` |
| **review.decided_at** | `2026-08-22T01:27:10-03:00` |
