---
id: "SPEC-260823-1337"
title: "Actor vocabulary and four agents — glossary + ONBOARDING entries, the four platform agents express the Actor concept (byte-sync + G-count via US-016), and the Actor phrase-family sweep (ADR-005)"
date: "2026-08-23"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved" # draft | approved | blocked | obsolete
origin: "US-022"
bolt: "US-022.BOLT-003" # ⚠️ MANDATORY — US-NNN.BOLT-NNN
revision: 2 # material revision of this canonical SPEC (matches manifest spec_revisions[])
associated_adrs:
  - "devflow/adrs/ADR-010-actor-grammar-and-pure-v5-vocabulary.md"
  - "devflow/adrs/ADR-005-removal-completeness-phrase-family-sweep.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
prerequisites:
  - "devflow/spec/SPEC-260823-1335-actor-concept-core.md" # the four agents express the §Actor concept (rev 2 — producer+approver)
  - "devflow/spec/SPEC-260823-1336-actors-folder.md" # the sweep's location set includes the actors/README.md
risk_class: "low" # mirrors the Bolt's risk_class
autonomy_level: "L3" # L1 | L2 | L3 | L4 — defaults by risk: low/medium→L3
turn_budget: "" # OPTIONAL — leave empty to use the platform default
data_classification: "internal"
review_ready_at: "2026-08-23T14:05:00-03:00"
review: # AITL-SPEC-Approval (rev 2) — recorded by the human reviewer (§3.0); revision dictated in conversation and transcribed by the agent
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-23T14:05:00-03:00"
  decided_at: "2026-08-23T14:05:43-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Revision 2 approved (G15 — source US-022 re-approved with the producer+approver reframe): the four-agent paragraph, the ONBOARDING entry and the actors/README surface state the Actor as producer + approver (executor side first-class); the phrase-family sweep includes the production terms and verifies no surface defines the Actor solely as 'the participant who occupies a checkpoint pause'. Byte-sync + G-count via US-016 preserved. Authorizes the V-Bounce against rev 2."
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs, and section
  headings (##) stay in English (the schema). Prose follows the project's
  content_language (en, devflow/LANGUAGE; ADR-012).

  ⚠️ AITL-SPEC-Approval: a draft SPEC cannot start a code-run or V-Bounce.
  Material source changes invalidate the approval → stop, revise, re-approve
  (G15). One V-Bounce never spans two SPEC revisions.

  ⚠️ PRE-SPEC EVIDENCE GATE (§2.4.1): verified — every governed source used
  below is approved (US-022 AITL-US-Approval ✓; ADR-010/005/004 accepted ✓;
  US-016 approved ✓). 0 open OQs (G35). The prerequisite SPECs are drafts —
  the BOLT-level dependencies (BOLT-001 + BOLT-002) govern the sequencing:
  this Bolt runs last, so its sweep covers the actors/ README.
-->

# SPEC-260823-1337 — Actor vocabulary, four agents and the sweep (US-022.BOLT-003)

| Field | Value |
|-------|-------|
| **Origin** | [US-022](../functional/user-stories/US-022-actor-concept.md) (approved) |
| **Bolt** | [US-022.BOLT-003](../functional/bolts/US-022.BOLT-003-actor-vocabulary-and-agents-sweep.md) (approved) |
| **ADRs** | ADR-010 (pure v5 vocabulary), ADR-005 (sweep discipline), ADR-004 (kit-only) |
| **Risk Class** | low · **Autonomy** L3 |
| **Revision** | 1 |

---

## 1. Objective
Make every kit surface that names the Actor concept speak one
consistent vocabulary, and verify it mechanically: (a) ONBOARDING's
minimal glossary gains the "Actor" entry; (b) the four platform agents
express the concept — the Actor as **producer + approver** (a team member
who produces the governed artifacts its role owns as executor and
participates in AITL approvals as approver when configured) — while
remaining **byte-identical** in their shared methodology regions (G-count
39×5, verified with the US-016 audit tool); (c) the **Actor phrase-family
sweep** (ADR-005 discipline) runs **last** — over a fixed location set
that includes the `actors/` README (BOLT-002) — and verifies, as an
**absence**, that no stale/competing terms remain outside a declared
allowlist, including the production vocabulary (no surface defines the
Actor **solely** as "the participant who occupies a checkpoint pause").

**Revision 2 (material):** the surfaces propagate the producer+approver
reframe of the re-approved US-022 / SPEC-1335 rev 2 (G15).

**Why:** US-022 AC-6/7/11 — the concept must be expressed consistently
everywhere it appears, or the kit drifts (the US-020 lesson: three misses
caught by the phrase-family discipline). **If not done:** the §Actor
section (BOLT-001) would be an island — the four agents, the glossary and
ONBOARDING would keep speaking differently.

---

## 2. Context

US-022 (approved, 5 SP) requires the vocabulary surfaces to express the
Actor concept. ADR-010 fixes the grammar and the pure-v5 vocabulary rule;
ADR-005 fixes the removal-completeness discipline (phrase-family sweep over
a fixed location set, verified as an absence, with an allowlist); ADR-004
scopes the work to the kit. US-016 (approved) automates the four-agent sync
and G-count checks — this Bolt uses it as the verification mechanism.

The four platform agents share their methodology sections byte-for-byte
(only the platform preambles differ); the Actor concept paragraph must be
added to that shared region identically in all four.

---

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | US-022.BOLT-003-actor-vocabulary-and-agents-sweep.md | AITL-BOLT-READY-Approval ✓ (2026-08-23, risk low) |
| Feature US | US-022-actor-concept.md | AITL-US-Approval ✓ (2026-08-23, 5 SP) |
| ADRs | ADR-010, ADR-005, ADR-004 | accepted ✓ |
| Prior work | US-016 (audit tool) | approved ✓ |
| Prior SPECs | SPEC-260823-1335 (BOLT-001), SPEC-260823-1336 (BOLT-002) | prerequisites (Bolt-level dependencies) |
| Repository baseline | commit `45d553f` | — |

Pre-SPEC evidence gate: **all governed sources approved**; no active-ADR
conflict (§3.5); 0 open OQs (G35).

---

## 4. Scope

### In scope (kit, documentation only)

- `distribution-kit/devflow/analysis/glossary/glossary.md` — the "Actor"
  entry (umbrella term: humans + DevFlow Agents; ADR-010 pure-v5 forms).
- `distribution-kit/devflow/ONBOARDING.md` — the "Actor" entry.
- The four platform agents' shared methodology region:
  `distribution-kit/CLAUDE.md`,
  `distribution-kit/.agents/skills/avenga-devflow/SKILL.md`,
  `distribution-kit/.github/agents/AvengaDevFlow.agent.md`,
  `distribution-kit/.opencode/agents/AvengaDevFlow.md` — the Actor concept
  paragraph, byte-identical.
- The Actor phrase-family sweep (ADR-005) over the kit — the location set
  includes the `actors/` README (BOLT-002 output); the allowlist covers
  historical/legacy mentions (G36).

### Out of scope

- The §Actor normative text and canonical mermaid (BOLT-001);
- The `actors/` folder + README (BOLT-002);
- Any guardrail added/removed (count invariant — G-count stays 39);
- Recorded history: approved artifacts' recorded terms are never rewritten
  (G36);
- The root `devflow/` (ADR-004).

---

## 5. Prerequisites and baseline

- SPEC-260823-1335 (BOLT-001) delivered — the §Actor concept exists for
  the four agents and the glossary to express.
- SPEC-260823-1336 (BOLT-002) delivered — the `actors/` README exists and
  is part of the sweep location set.
- US-016 delivered — the audit tool provides the sync/G-count evidence.
- Baseline commit `45d553f`.

---

## 6. Phases

### Phase A — Glossary and ONBOARDING entries

**Duration:** ~1h total cycle — **Complexity:** Low

#### A.1 Glossary entry

Add the "Actor" entry to the kit's glossary: the umbrella term covering
humans and DevFlow Agents; the default-case framing (human by default /
DevFlow Agent by explicit valid configuration); the grammar forms
(`human:<user>` / `agent:<id>`); a pointer to the §Actor section (BOLT-001)
as the normative definition.

**Files modified:**
- `distribution-kit/devflow/analysis/glossary/glossary.md` — the "Actor"
  entry

#### A.2 ONBOARDING entry

Add the "Actor" entry to ONBOARDING's glossary/vocabulary section, same
content discipline: definition + pointer to §Actor, no second source of
truth.

**Files modified:**
- `distribution-kit/devflow/ONBOARDING.md` — the "Actor" entry

### Phase B — The four platform agents

**Duration:** ~1h total cycle — **Complexity:** Low

#### B.1 The concept paragraph (shared region)

Add the Actor concept paragraph to the four agents' shared methodology
region (their AITL/precept section): the Actor as **producer + approver**
— a member of the team who **produces** the governed artifacts its role
owns (functional analyst → US, architect → ADR, developer → SPEC + code,
QA → TC/tests) as **executor**, and **participates** in AITL approvals as
**approver** when configured, under the independence floor; human by
default / DevFlow Agent by explicit valid configuration; HITL as the
default case inside AITL; the executor/approver/neither relationship
(Coordinator never signs). **The same text, byte-identical in all four**
(the only sanctioned divergence stays the `devflow/agents-data/<agent>/`
path line).

**Files modified (byte-identical shared region):**
- `distribution-kit/CLAUDE.md`
- `distribution-kit/.agents/skills/avenga-devflow/SKILL.md`
- `distribution-kit/.github/agents/AvengaDevFlow.agent.md`
- `distribution-kit/.opencode/agents/AvengaDevFlow.md`

### Phase C — The Actor phrase-family sweep (runs last)

**Duration:** ~1h total cycle — **Complexity:** Low–Medium

#### C.1 Sweep

Apply the ADR-005 phrase-family discipline to the Actor vocabulary family:
"Actor" (as the team-member identity term), "Actor-in-the-Loop",
"human-by-default, agent-by-explicit-configuration", and the **production
vocabulary** — "produces the artifacts its role owns", "executor mode" —
(plus the stale/competing candidates: a definition of the Actor **solely**
as "the participant who occupies a checkpoint pause", a lone "the human
governs" precept phrasing outside history). Fixed location set: the kit's
methodology text, READMEs, templates, the four agents, ONBOARDING, the
`actors/` README. Declared allowlist: historical/legacy mentions (G36:
recorded approvals, MEMs, `_archive/`), and the deliberate default-case
mentions of HITL (actor = human) that ADR-008 §3.1 requires.

**Verification = absence:** after the sweep, no family-competitor term
exists outside the allowlist; the location set and the allowlist are
recorded in the MEM as the sweep proof.

**Files modified:** per the sweep findings (expected: the glossary/ONBOARDING
entries + the four-agent paragraph from Phases A–B; anything else found is
corrected in place or allowlisted with reason).

### Phase D — Verification (GREEN)

**Duration:** ~0.5h total cycle — **Complexity:** Low

#### D.1 Evidence collection

Run: (a) US-016 audit output — four-agent shared-body byte-identity + G-count
39×5; (b) the sweep report — location set, allowlist, absence result; (c)
glossary + ONBOARDING entries present; (d) `git status` shows only
`distribution-kit/` + governance records.

**Files created (evidence):** none — evidence recorded in the MEM.

---

## 7. Acceptance criteria

### AC-1: Four agents express the concept (producer + approver), byte-identical

**Given** the four platform agents,
**When** their AITL sections are inspected,
**Then** they express the Actor concept — a team member who produces the
governed artifacts its role owns (executor) and participates in AITL
approvals (approver, when configured, under the independence floor) — and
remain byte-identical in their shared methodology regions; G-count 39×5
(US-016 audit passes) (US-022 AC-6, re-approved).

### AC-2: Glossary and ONBOARDING carry "Actor"

**Given** the vocabulary,
**When** the glossary and ONBOARDING are inspected,
**Then** "Actor" is defined as the umbrella term covering humans and
DevFlow Agents, consistent with the pure v5 vocabulary (ADR-010), pointing
to the §Actor section (US-022 AC-7).

### AC-3: The sweep verifies an absence

**Given** the Actor vocabulary family (incl. the production terms),
**When** the kit is swept (location set incl. the `actors/` README; declared
allowlist),
**Then** no stale/competing terms remain outside the allowlist — in
particular, no surface defines the Actor **solely** as "the participant who
occupies a checkpoint pause" — verified as an absence, per ADR-005
(US-022 AC-11).

### AC-4: G36 history preserved

**Given** recorded approvals and archived documents,
**When** the sweep runs,
**Then** their recorded `HITL-*`/historical terms are preserved verbatim
(allowlisted, never rewritten).

### AC-5: Kit-only

**Given** the diff,
**When** the Bolt lands,
**Then** `git status` shows only `distribution-kit/` + governance records
(ADR-004).

### AC mapping to source

| Source AC | How this SPEC satisfies it | Verifying test/evidence |
|-----------|----------------------------|--------------------------|
| US-022 AC-6 | four-agent concept paragraph | AC-1 — US-016 audit (byte-identity + G-count 39×5) |
| US-022 AC-7 | glossary + ONBOARDING entries | AC-2 — presence + pointer checks |
| US-022 AC-11 | phrase-family sweep (ADR-005) | AC-3 — sweep report (absence) |
| US-022 rule #2 (G36) | history preserved | AC-4 — allowlist + no rewrite |
| ADR-004 | kit-only | AC-5 — git status |

---

## 8. Testing strategy

Deterministic (documentation):

- **RED (before):** no "Actor" entries in glossary/ONBOARDING; the four
  agents carry no Actor concept paragraph; the family-competitor terms are
  present (sweep finds them).
- **GREEN (after):** AC-1..AC-5 — entries present; US-016 audit passes
  (byte-identity + G-count 39×5); the sweep report shows an **empty result
  outside the allowlist**; git status kit-only.
- **Edge cases:** the shared-region edit must not break the agents' preamble
  exemptions (only the agents-data path line differs — US-016 verifies);
  the sweep must not touch G36-protected history (allowlist); the count
  invariant (39) holds.

---

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | — | n/a — documentation-only, no runtime |
| SAST / SBOM | — | n/a — no dependencies, no runtime |
| Perf-smoke (p95/p99) | — | n/a — no runtime surface |
| Prompt-injection scan | — | pass — no runtime surface; static documentation |
| Secret-leak scan | — | pass — no secrets in documentation |
| Hallucination lint | refs resolve | pass — the §Actor pointer resolves (BOLT-001 prerequisite) |
| IP / license provenance | — | n/a — no third-party code |
| PII / DLP | — | n/a — no personal data (internal) |
| Dependency-confusion | — | n/a — no dependencies |
| Test-first evidence | — | n/a — documentation; RED/GREEN presence evidence in §8 |
| Behavioral reproducibility | deterministic | pass — US-016 audit + sweep reproduce identically |
| Bolt-manifest validation | validates | pass — BOLT-003 manifest + spec_revisions[] |

---

## 10. Security and data

Static governance documentation; no runtime boundary. The four-agent
paragraph states the safe-default (ADR-008) without implementing
enforcement. Data classification `internal`.

---

## 11. Migration, compatibility and rollback

- **Migration:** additive documentation in glossary, ONBOARDING and the
  four agents' shared region.
- **Compatibility:** the four agents' byte-identity invariant is preserved
  and verified (US-016); no adopter breakage.
- **Rollback:** revert the kit commit; the root `devflow/` is untouched.

---

## 12. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| Four-agent drift during the shared-region edit | 2 | 4 | US-016 audit (byte-identity + G-count 39×5) as the gate |
| Sweep misses a surface or overreaches into history | 2 | 4 | ADR-005 fixed location set + declared allowlist (G36); absence verified |
| Vocabulary contradiction (competing terms left) | 1 | 3 | The sweep's absence result is the completion evidence |
| Sweep touches root `devflow/` | 1 | 3 | ADR-004 scope + AC-5 git-status check |

---

## 13. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| The sweep runs last (after BOLT-001 + BOLT-002) | Its location set includes the §Actor section and the `actors/` README — the completeness gate covers all surfaces |
| Allowlist covers G36 history + the ADR-008 default-case HITL mentions | History is never rewritten; HITL-as-default is required by the precept |
| US-016 audit as the verification mechanism | The tool automates the four-agent sync + G-count checks (its approved purpose) |

---

## 14. Stop conditions

- The US-016 audit fails (byte-identity or G-count ≠ 39×5) → stop, fix the
  drift, re-run.
- The sweep finds a competitor term that cannot be allowlisted with reason
  → stop, resolve (never force it into the allowlist).
- Any file outside `distribution-kit/` + governance records in the diff →
  stop, revert, record (ADR-004).
- A governed source changes materially (G15) → stop, revise, re-approve.
- Turn budget (10) exhausted before GREEN → stop, MEM with progress.

---

## 15. Definition of Done (DoD)

- [ ] Phases A–D implemented
- [ ] AC-1..AC-5 pass
- [ ] GREEN evidence collected (entries present; US-016 audit; sweep absence; kit-only)
- [ ] ADR-010/005/004 followed; G36 history preserved
- [ ] Applicable gates pass / n/a with reason
- [ ] MEM created in `devflow/memory/` (exactly one per V-Bounce)
- [ ] Manifest `v_bounces[]` entry appended in `devflow/metrics/bolts/`
- [ ] AITL-MEM-Approval recorded

---

## 16. References

- US-022 (approved), US-022.BOLT-003 (approved)
- SPEC-260823-1335 (BOLT-001), SPEC-260823-1336 (BOLT-002) — prerequisites
- ADR-010 (grammar), ADR-005 (sweep discipline), ADR-004 (kit-only)
- US-016 (audit tool), DISC-001/DISC-002 (approved)

---

## 17. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-23 | eugenio.serrano | Revision 1 — initial |
| 2026-08-23 | eugenio.serrano | **Revision 2 (material, G15)** — source US-022 re-approved with the producer+approver reframe: the four-agent paragraph, the ONBOARDING entry and the `actors/` README surface state the Actor as producer + approver; the sweep includes the production vocabulary (no surface defines the Actor solely as "the participant who occupies a checkpoint pause") |

---

## 18. AITL-SPEC-Approval

> **Avenga DevFlow §2.4.1, §3.0.** This SPEC remains a draft until the
> Dev-validator (+ applicable domain owners) records `AITL-SPEC-Approval`
> (in the `review` frontmatter block). Bolt approval authorizes SPEC
> preparation; **SPEC approval authorizes the V-Bounce**. A material source
> change invalidates this approval — stop, revise, re-approve (G15).

| Field | Value |
|-------|-------|
| **review.reviewers** | eugenio.serrano (dev_validator) |
| **review.decision** | **approved** (rev 1) + **approved** (rev 2 — producer+approver propagation, 2026-08-23T14:05:43) |
| **review_ready_at** | rev 1 `2026-08-23T13:37:00-03:00` · rev 2 `2026-08-23T14:05:00-03:00` |
| **review.started_at** | rev 1 `2026-08-23T13:40:00-03:00` · rev 2 `2026-08-23T14:05:00-03:00` |
| **review.decided_at** | rev 1 `2026-08-23T13:42:30-03:00` · rev 2 `2026-08-23T14:05:43-03:00` |
| **Findings** | none — acknowledged_without_comment (reason in the frontmatter `review:` block) |
