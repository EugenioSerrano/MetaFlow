---
id: "SPEC-260823-1336"
title: "actors/ folder — the roster home: create devflow/actors/ with a README teaching the Actor concept (G30-sanctioned)"
date: "2026-08-23"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved" # draft | approved | blocked | obsolete
origin: "US-022"
bolt: "US-022.BOLT-002" # ⚠️ MANDATORY — US-NNN.BOLT-NNN
revision: 2 # material revision of this canonical SPEC (matches manifest spec_revisions[])
associated_adrs:
  - "devflow/adrs/ADR-007-devflow-agent-identity-model.md"
  - "devflow/adrs/ADR-008-aitl-approval-precept.md"
  - "devflow/adrs/ADR-010-actor-grammar-and-pure-v5-vocabulary.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
prerequisites:
  - "devflow/spec/SPEC-260823-1335-actor-concept-core.md" # the README points to the §Actor section (rev 2 — producer+approver)
risk_class: "low" # mirrors the Bolt's risk_class
autonomy_level: "L3" # L1 | L2 | L3 | L4 — defaults by risk: low/medium→L3
turn_budget: "" # OPTIONAL — leave empty to use the platform default
data_classification: "internal"
review_ready_at: "2026-08-23T15:30:00-03:00"
review: # AITL-SPEC-Approval (rev 2) — recorded by the human reviewer (§3.0); revision dictated in conversation and transcribed by the agent
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-23T15:31:00-03:00"
  decided_at: "2026-08-23T15:33:05-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Revision 2 approved (G15 — source US-022 re-approved with the producer+approver reframe): the actors/ README teaches the Actor as producer + approver (with the new canonical mermaid, identical to §3.0.1 / US-022 §4); the disambiguation, pointer and roster-note requirements are unchanged. Authorizes the V-Bounce 2 that documents the delivered README."
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs, and section
  headings (##) stay in English (the schema). Prose follows the project's
  content_language (en, devflow/LANGUAGE; ADR-012).

  ⚠️ AITL-SPEC-Approval: a draft SPEC cannot start a code-run or V-Bounce.
  Material source changes invalidate the approval → stop, revise, re-approve
  (G15). One V-Bounce never spans two SPEC revisions.

  ⚠️ PRE-SPEC EVIDENCE GATE (§2.4.1): verified — every governed source used
  below is approved (US-022 AITL-US-Approval ✓; ADR-007/008/010/004
  accepted ✓; DISC-001/002 approved ✓). 0 open OQs (G35). The prerequisite
  SPEC-260823-1335 is draft — the BOLT-level dependency (BOLT-001) governs
  the sequencing; its §Actor must exist before this Bolt's README points
  to it.
-->

# SPEC-260823-1336 — The `actors/` folder and its README (US-022.BOLT-002)

| Field | Value |
|-------|-------|
| **Origin** | [US-022](../functional/user-stories/US-022-actor-concept.md) (approved) |
| **Bolt** | [US-022.BOLT-002](../functional/bolts/US-022.BOLT-002-actors-folder.md) (approved) |
| **ADRs** | ADR-007 (identity model), ADR-008 (precept), ADR-010 (grammar), ADR-004 (kit-only) |
| **Risk Class** | low · **Autonomy** L3 |
| **Revision** | 1 |

---

## 1. Objective

Create the kit's `distribution-kit/devflow/actors/` folder — the **roster
home** (US-022 AC-8, G30-sanctioned by US-022) — with a README that teaches
the Actor concept (**producer + approver**, per the re-approved US-022 /
SPEC-1335 rev 2) and disambiguates `actors/` (who is in the team) from
`agents/` (the AI-member definitions, US-023) on its first line.

**Why:** US-024 will fill this folder with the roster schema + example and
the AITL-enable ADR template; US-023 creates `agents/` alongside. The
folder must exist with its explanatory README first, so the family lands in
a consistent structure and every reader immediately understands the Actor
concept. **If not done:** US-024 has no home for the roster and the
`actors/`/`agents/` name confusion goes unexplained.

**Revision 2 (material):** the README teaches the reframed concept — the
Actor as a team member who produces the artifacts its role owns (executor)
and participates in AITL approvals (approver, when configured) — with the
new canonical mermaid (producer → checkpoint → approver, identical to
§3.0.1 / US-022 §4).

---

## 2. Context

The folder-decision is settled in US-022 (approved): `devflow/actors/` is
the roster home — NOT `agents/`. ADR-007 §3.5/§4 delegates the layout to
the registry US, so no superseding ADR is needed. The README is
**explanatory only**: the normative definition lives in the §Actor section
of the methodology (SPEC-260823-1335 / BOLT-001); the README points to it
and never becomes a second source of truth (G28 discipline, US-022 rule
#6). The mermaid's canonical home is the §Actor section; the README
references/embeds it (no diagram drift, US-022 rule #6 / AC-9).

---

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | US-022.BOLT-002-actors-folder.md | AITL-BOLT-READY-Approval ✓ (2026-08-23, risk low) |
| Feature US | US-022-actor-concept.md | AITL-US-Approval ✓ (2026-08-23, 5 SP) |
| ADRs | ADR-007, ADR-008, ADR-010, ADR-004 | accepted ✓ |
| DISC evidence | DISC-001, DISC-002 | approved ✓ |
| Prior SPEC | SPEC-260823-1335 (BOLT-001 — the §Actor pointer target) | prerequisite |
| Repository baseline | commit `45d553f` | — |

Pre-SPEC evidence gate: **all governed sources approved**; no active-ADR
conflict (§3.5); 0 open OQs (G35).

---

## 4. Scope

### In scope (kit, documentation only)

- `distribution-kit/devflow/actors/` — new folder (G30-sanctioned by
  US-022).
- `distribution-kit/devflow/actors/README.md` — the explanatory README.

### Out of scope

- The roster schema + example and the AITL-enable ADR template (US-024).
- The agent definitions, Coordinator, charters, wrappers (US-023).
- The normative §Actor text and the canonical mermaid (SPEC-260823-1335 /
  BOLT-001).
- The root `devflow/` (ADR-004 kit-only).

---

## 5. Prerequisites and baseline

- SPEC-260823-1335 (BOLT-001) delivered — the §Actor section and the
  canonical mermaid exist so the README can point to them.
- Baseline commit `45d553f`.
- No other prerequisite.

---

## 6. Phases

### Phase A — The folder and the README

**Duration:** ~1.5h total cycle — **Complexity:** Low

#### A.1 Create the folder

Create `distribution-kit/devflow/actors/` (empty except the README from
A.2). The folder's purpose — the roster home — is stated in the README and
in the §5.1 tree (BOLT-001).

**Files created:**
- `distribution-kit/devflow/actors/` — the folder (G30-sanctioned)

#### A.2 Write the README

Write `README.md` teaching the Actor concept (**producer + approver**):

- **First line disambiguation** — `actors/` = who is in the team (the
  roster home: humans + DevFlow Agents as actors); `agents/` = the
  AI-member definitions (US-023). Never confuse the two.
- **The concept, explained** — Actor = a member of the team who
  **produces** the governed artifacts its role owns (FA → US, architect →
  ADR, developer → SPEC + code, QA → TC/tests) as **executor** and
  **participates** in AITL approvals as **approver** when configured,
  under the independence floor (human by default / DevFlow Agent by
  explicit valid configuration); the grammar (`human:<user>` /
  `agent:<id>`); the two independence layers; the open role taxonomy; the
  safe default — each **pointing to the normative §Actor section** of the
  methodology (links/anchors), never restating it as an independent
  authority.
- **The flow diagram** — the mermaid (the producer → checkpoint →
  approver flow), referencing/embedding the canonical one from the §Actor
  section (no forked copy).
- **Roster note** — "the roster schema + example land here with US-024";
  the per-project AITL-enable ADR template also lives here (US-024).

**Files created:**
- `distribution-kit/devflow/actors/README.md` — the explanatory README

### Phase B — Verification (GREEN)

**Duration:** ~0.5h total cycle — **Complexity:** Low

#### B.1 Evidence collection

Verify: (a) the folder + README exist; (b) the first line disambiguates
`actors/` vs `agents/`; (c) the README points to the §Actor section and
contains no normative claims of its own (a reviewer-style read: every
"definition" sentence carries a pointer, not an independent authority); (d)
the mermaid references the canonical one; (e) `git status` shows only
`distribution-kit/` + governance records.

**Files created (evidence):** none — evidence recorded in the MEM.

---

## 7. Acceptance criteria

### AC-1: The folder exists and is the roster home

**Given** the kit's `devflow/actors/` folder,
**When** a maintainer inspects it,
**Then** it contains a README; it is the roster home (schema + example
added by US-024) and its first line disambiguates it from `devflow/agents/`
(US-022 AC-8).

### AC-2: The README teaches and points (producer + approver)

**Given** the `actors/` README,
**When** a reader opens it,
**Then** it teaches the Actor concept — a team member who produces the
governed artifacts its role owns (executor) and participates in AITL
approvals (approver, when configured) — with the flow diagram (the
producer → checkpoint → approver mermaid, referencing/embedding the
canonical one from §3.0.1) and points to the normative definition in
Avenga-DevFlow.md — explanatory, never a second source of truth
(US-022 AC-9, re-approved).

### AC-3: Kit-only

**Given** the diff,
**When** the Bolt lands,
**Then** `git status` shows only `distribution-kit/` + governance records
(ADR-004).

### AC mapping to source

| Source AC | How this SPEC satisfies it | Verifying test/evidence |
|-----------|----------------------------|--------------------------|
| US-022 AC-8 | folder + README + roster home + disambiguation | AC-1 presence + first-line check |
| US-022 AC-9 | README teaches + pointer + canonical mermaid | AC-2 content checks |
| US-022 rule #6 | README explanatory (G28) | AC-2 pointer/no-authority read |
| ADR-004 | kit-only | AC-3 git status |

---

## 8. Testing strategy

Deterministic (documentation):

- **RED (before):** no `actors/` folder exists; no README.
- **GREEN (after):** AC-1..AC-3 — folder + README present, first-line
  disambiguation, pointer to §Actor present, no normative-claim sentences,
  git status kit-only.
- **Edge cases:** the README must not restate definitions as its own
  authority (checked by a read-through: every claim carries a pointer); the
  README must not create a second mermaid (only reference/embed).

---

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | — | n/a — documentation-only, no runtime |
| SAST / SBOM | — | n/a — no dependencies, no runtime |
| Perf-smoke (p95/p99) | — | n/a — no runtime surface |
| Prompt-injection scan | — | pass — no runtime surface; the README is static documentation |
| Secret-leak scan | — | pass — no secrets in documentation |
| Hallucination lint | refs resolve | pass — the §Actor pointer resolves (BOLT-001 prerequisite) |
| IP / license provenance | — | n/a — no third-party code |
| PII / DLP | — | n/a — no personal data (internal) |
| Dependency-confusion | — | n/a — no dependencies |
| Test-first evidence | — | n/a — documentation; RED/GREEN presence evidence in §8 |
| Behavioral reproducibility | deterministic | pass — same checks reproduce identically |
| Bolt-manifest validation | validates | pass — BOLT-002 manifest + spec_revisions[] |

---

## 10. Security and data

Static governance documentation; no runtime boundary. The README explains
the safe-default (ADR-008) without implementing enforcement. Data
classification `internal`.

---

## 11. Migration, compatibility and rollback

- **Migration:** new folder in the kit; additive.
- **Compatibility:** no impact on adopters (new path only).
- **Rollback:** delete the `actors/` folder; the root `devflow/` is
  untouched.

---

## 12. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| README becomes a second source of truth | 2 | 4 | AC-2 pointer rule + G28 discipline (US-022 rule #6) |
| `actors/` vs `agents/` confusion | 2 | 3 | First-line disambiguation (AC-1) + mirrored in US-023's README |
| Mermaid drift | 1 | 3 | Canonical home in §Actor; README references/embeds only (AC-2) |

---

## 13. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| US-022 creates the folder (Option A), US-024 fills it | The folder exists when US-024 needs it; US-022 gets a concrete kit artifact |
| README is explanatory, not normative | Single source of truth in the methodology (§Actor); G28 discipline |
| README embeds/references the canonical mermaid | No diagram drift across the family |

---

## 14. Stop conditions

- Any file outside `distribution-kit/` + governance records in the diff →
  stop, revert, record (ADR-004).
- The README carries a normative claim without a pointer → stop, revise the
  sentence.
- A governed source changes materially (G15) → stop, revise, re-approve.
- Turn budget (10) exhausted before GREEN → stop, MEM with progress.

---

## 15. Definition of Done (DoD)

- [ ] Phase A implemented (folder + README)
- [ ] AC-1..AC-3 pass
- [ ] GREEN evidence collected (folder/README present; disambiguation;
  pointer; kit-only)
- [ ] ADR-007/008/010/004 followed
- [ ] Applicable gates pass / n/a with reason
- [ ] MEM created in `devflow/memory/` (exactly one per V-Bounce)
- [ ] Manifest `v_bounces[]` entry appended in `devflow/metrics/bolts/`
- [ ] AITL-MEM-Approval recorded

---

## 16. References

- US-022 (approved), US-022.BOLT-002 (approved)
- SPEC-260823-1335 (BOLT-001 — the §Actor pointer target)
- ADR-007 (identity), ADR-008 (precept), ADR-010 (grammar), ADR-004 (kit-only)
- DISC-001/DISC-002 (approved)

---

## 17. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-23 | eugenio.serrano | Revision 1 — initial |
| 2026-08-23 | eugenio.serrano | **Revision 2 (material, G15)** — source US-022 re-approved with the producer+approver reframe: the README teaches the Actor as producer + approver (executor side first-class) with the new canonical mermaid (producer → checkpoint → approver, identical to §3.0.1 / US-022 §4); disambiguation, pointer and roster-note requirements unchanged |

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
| **review.decision** | **approved** (rev 1) + **approved** (rev 2 — producer+approver README, 2026-08-23T15:33:05) |
| **review_ready_at** | rev 1 `2026-08-23T13:36:00-03:00` · rev 2 `2026-08-23T15:30:00-03:00` |
| **review.started_at** | rev 1 `2026-08-23T13:40:00-03:00` · rev 2 `2026-08-23T15:31:00-03:00` |
| **review.decided_at** | rev 1 `2026-08-23T13:42:30-03:00` · rev 2 `2026-08-23T15:33:05-03:00` |
| **Findings** | none — acknowledged_without_comment (reason in the frontmatter `review:` block) |
