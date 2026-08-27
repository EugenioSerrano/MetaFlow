---
id: "SPEC-260823-1743"
title: "US-001 absorption — the deprecated team-roster ACs as a special case of the unified roster, and the deprecation record closure"
date: "2026-08-23"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved" # draft | approved | blocked | obsolete
origin: "US-024"
bolt: "US-024.BOLT-003" # ⚠️ MANDATORY — US-NNN.BOLT-NNN
revision: 1 # material revision of this canonical SPEC (matches manifest spec_revisions[])
associated_adrs:
  - "devflow/adrs/ADR-010-actor-grammar-and-pure-v5-vocabulary.md"
prerequisites:
  - "devflow/spec/SPEC-260823-1741-actors-family-shape.md" # the roster docs the ACs are absorbed into
risk_class: "low" # mirrors the Bolt's risk_class
autonomy_level: "L3" # L1 | L2 | L3 | L4 — defaults by risk: low/medium→L3
turn_budget: "" # OPTIONAL — leave empty to use the platform default
data_classification: "internal"
review_ready_at: "2026-08-23T17:43:00-03:00"
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
  acknowledgment_reason: "Approved as Dev-validator: one-Bolt plan complete (the human-roster guarantees section named without the maintenance ID + the record closure; the self-containment check explicit with the partition boundary). Authorizes the V-Bounce."
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs, and section
  headings (##) stay in English (the schema). Prose in content_language
  (en, devflow/LANGUAGE; ADR-012).

  ⚠️ AITL-SPEC-Approval: a draft SPEC cannot start a code-run or V-Bounce.
  Material source changes invalidate the approval → stop, revise, re-approve
  (G15). One V-Bounce never spans two SPEC revisions.

  ⚠️ PRE-SPEC EVIDENCE GATE (§2.4.1): verified — US-024 re-approved ✓
  (Modelo B); REV-001 approved ✓; US-001 deprecated ✓; 0 open OQs.

  ⚠️ SELF-CONTAINMENT BOUNDARY: this Bolt touches BOTH partitions — the
  kit docs (self-contained) and the maintenance deprecation record (the
  US-001 doc + the INDEX, which are governance records, not kit content).
-->

# SPEC-260823-1743 — US-001 absorption (US-024.BOLT-003)

| Field | Value |
|-------|-------|
| **Origin** | [US-024](../functional/user-stories/US-024-unified-actors-roster.md) (re-approved, Modelo B) |
| **Bolt** | [US-024.BOLT-003](../functional/bolts/US-024.BOLT-003-us001-absorption.md) (approved) |
| **ADRs** | ADR-010 (grammar) |
| **Risk Class** | low · **Autonomy** L3 |
| **Revision** | 1 |

---

## 1. Objective

Absorb the deprecated US-001 (team roster, never approved) ACs as a
**special case** of the unified actors roster, stated in the kit's roster
docs: single-maintainer teams may name **external reviewers**; an **empty
roster changes nothing** (optionality); the roster family **travels with
the §5.16 migration**; roster updates (members join/leave) require **no
approval** (living data) — except an *approver's* charter or authority
fields, which **re-trigger the project's AITL-enable ADR review**.
Additionally, close the **US-001 deprecation record** (doc + INDEX):
status `deprecated`, absorbed by US-024, with the history preserved
(G36 — US-001 was never approved, so no recorded decision is affected).

**Why:** the human-only roster's guarantees must survive as a special
case of the actors roster, with a clean deprecation trail. **If not
done:** the guarantees vanish silently and the US-001 record dangles.

---

## 2. Context

US-024 AC-6 (the special-case absorption); US-001 (deprecated
2026-08-23 — the ACs absorbed here); REV-001 (approved — the role
inventory the ACs came from); ADR-010 (grammar). The kit's roster docs
(`actors/README.md`, SPEC-1741's family) are the absorption home; the
US-001 doc + the functional INDEX are the maintenance deprecation record.

---

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | US-024.BOLT-003-us001-absorption.md | AITL-BOLT-READY-Approval ✓ (2026-08-23, risk low) |
| Feature US | US-024-unified-actors-roster.md | AITL-US-Approval ✓ (re-approved Modelo B) |
| Prior US | US-001-team-roster.md | deprecated ✓ (no recorded decision) |
| Review evidence | REV-001-hitl-checkpoint-role-inventory.md | approved ✓ |
| Prior SPEC | SPEC-260823-1741 (the roster docs) | prerequisite |
| Repository baseline | commit `45d553f` | — |

Pre-SPEC evidence gate: **all governed sources approved/closed**; 0 open OQs.

---

## 4. Scope

### In scope

- `distribution-kit/devflow/actors/README.md` — the
  **"Single-maintainer / human-roster guarantees"** section (the special
  cases — named without the maintenance ID: adopters have no US-001).
- `devflow/functional/user-stories/US-001-team-roster.md` — the
  deprecation record confirmation (already `deprecated`; the absorbed-by
  note).
- `devflow/functional/INDEX.md` — the US-001 deprecation row (already
  present; consistency check).

### Out of scope

- The family files themselves (BOLT-001); the AITL-enable ADR template +
  rules (BOLT-002); the root methodology text.

---

## 5. Prerequisites and baseline

- SPEC-260823-1741 (BOLT-001) delivered — the roster docs exist.
- Baseline commit `45d553f`.

---

## 6. Phases

### Phase A — The absorption text (kit)

**Duration:** ~1h total cycle — **Complexity:** Low

#### A.1 The special cases in the README

`actors/README.md` gains the **"Single-maintainer / human-roster
guarantees"** section (named without the maintenance ID — adopters have
no US-001): external reviewers (single-maintainer teams may name one);
optionality (an empty roster changes nothing); migration travel (the
roster family travels with the §5.16 migration); living data (member
join/leave updates require no approval) — except an approver's charter or
authority fields, which re-trigger the AITL-enable ADR review (BOLT-002's
template). Self-contained wording throughout.

**Files modified:**
- `distribution-kit/devflow/actors/README.md`

### Phase B — The deprecation record closure (maintenance)

**Duration:** ~0.5h total cycle — **Complexity:** Low

#### B.1 The US-001 record

Confirm/complete US-001's frontmatter + body: status `deprecated`
(present), the reason notes the absorption by US-024 (the unified actors
roster — the human roster is its special case), the INDEX row consistent
(present). History preserved — no recorded decision exists (never
approved), so G36 holds trivially.

**Files modified:**
- `devflow/functional/user-stories/US-001-team-roster.md`
- `devflow/functional/INDEX.md` (row consistency)

### Phase C — Verification (GREEN)

**Duration:** ~0.5h total cycle — **Complexity:** Low

#### C.1 Evidence

The README section present (named "Single-maintainer / human-roster
guarantees" — **no "US-001" string in the kit file**); US-001 doc + INDEX
consistent (deprecated, absorbed by US-024); **the self-containment
check** — `grep -E "US-[0-9]{3}|ADR-[0-9]{3}|DISC-[0-9]{3}|BOLT-[0-9]|SPEC-26|MEM-26|REV-[0-9]{3}|TC-[0-9]{3}"`
over the **delivered kit file** (the README) → **0 hits** (the
maintenance records — the US-001 doc + the INDEX — are governance, not
kit content, and are exempt by the boundary); `git status` shows the kit
README + the two maintenance records; no BOM.

**Files created (evidence):** none — evidence recorded in the MEM.

---

## 7. Acceptance criteria

### AC-1: The special cases hold

**Given** the human-roster ACs of the deprecated US-001,
**When** the unified roster lands,
**Then** they hold as a special case: single-maintainer teams may name
external reviewers; an empty roster changes nothing; the roster family
travels with the §5.16 migration; roster updates require no approval
(living data) — except an approver's charter or authority fields, which
re-trigger the AITL-enable ADR review (US-024 AC-6).

### AC mapping to source

| Source AC | How this SPEC satisfies it | Verifying test/evidence |
|-----------|----------------------------|--------------------------|
| US-024 AC-6 | the README absorption section + the record closure | AC-1 presence + record consistency |

---

## 8. Testing strategy

Deterministic (documentation):

- **RED (before):** the README has no human-roster guarantees section.
- **GREEN (after):** AC-1 — the section present (named without the
  maintenance ID) with the five special cases; US-001 doc + INDEX
  consistent; the **self-containment grep → 0 hits** on the delivered kit
  file; kit-only for the kit part; history preserved (G36).
- **Edge cases:** the authority re-trigger clause; the "never approved"
  note (no recorded decision affected); the kit README must not contain
  the string "US-001".

---

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | — | n/a — documentation-only |
| SAST / SBOM | — | n/a — no runtime |
| Perf-smoke (p95/p99) | — | n/a — no runtime surface |
| Prompt-injection scan | — | pass — no runtime surface |
| Secret-leak scan | — | pass — no secrets |
| Hallucination lint | refs resolve | pass — US-001/REV-001 refs resolve |
| IP / license provenance | — | n/a — original content |
| PII / DLP | — | n/a — no personal data (internal) |
| Dependency-confusion | — | n/a — no dependencies |
| Test-first evidence | — | n/a — documentation; presence evidence in §8 |
| Behavioral reproducibility | deterministic | pass |
| Bolt-manifest validation | validates | pass — BOLT-003 manifest + spec_revisions[] |

---

## 10. Security and data

No security surface; the absorption keeps the guarantees intact (the
authority re-trigger is the governance boundary). Data classification
`internal`.

---

## 11. Migration, compatibility and rollback

- **Migration:** README section + record consistency; additive.
- **Compatibility:** no behavior change; history preserved (G36).
- **Rollback:** remove the section; revert the record edits; root
  untouched.

---

## 12. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| The absorption weakens a guarantee | 2 | 4 | The US-001 ACs held verbatim as special cases |
| The deprecation record drifts | 2 | 2 | Doc + INDEX consistency check; G36 |

---

## 13. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| The absorption lives in the roster README, not a new file | The family docs are the home of the roster's rules; self-contained |
| The US-001 record is confirmed, not rewritten | G36: history preserved; it was never approved, so closure is clean |
| External reviewers/optionality/migration/living-data stay verbatim | They are the human-roster guarantees — absorbed, not altered |

---

## 14. Stop conditions

- The absorption text alters a US-001 AC's meaning → stop, fix.
- The US-001 record would rewrite recorded history → stop (G36).
- A governed source changes materially (G15) → stop, revise, re-approve.
- Turn budget (10) exhausted before GREEN → stop, MEM with progress.

---

## 15. Definition of Done (DoD)

- [ ] Phases A–C implemented
- [ ] AC-1 pass
- [ ] GREEN evidence (section present; records consistent; kit-only for the kit part)
- [ ] G36 preserved
- [ ] Applicable gates pass / n/a with reason
- [ ] MEM created in `devflow/memory/` (exactly one per V-Bounce)
- [ ] Manifest `v_bounces[]` entry appended in `devflow/metrics/bolts/`
- [ ] AITL-MEM-Approval recorded

---

## 16. References

- US-024 (re-approved — Modelo B), US-024.BOLT-003 (approved)
- US-001 (deprecated — the absorbed ACs), REV-001 (approved)
- ADR-010 (grammar); SPEC-260823-1741 (the roster docs)

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
| **review_ready_at** | `2026-08-23T17:43:00-03:00` |
| **review.started_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **review.decided_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **Findings** | [findings or acknowledged_without_comment + reason] |
