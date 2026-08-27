---
id: "SPEC-260824-1447"
title: "The kit G07 scoping — the lifecycle-as-operational-config clause in the GUARDRAILS row and the four MainAgents' row, one semantics at three altitudes"
date: "2026-08-24"
author: "eugenio.serrano"
llm: "claude-fable-5"
status: "approved" # draft | approved | blocked | obsolete — AITL-SPEC-Approval 2026-08-24
origin: "US-025"
bolt: "US-025.BOLT-005"
revision: 1
associated_adrs:
  - "devflow/adrs/ADR-013-agent-lifecycle-governance.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
prerequisites:
  - "devflow/spec/SPEC-260824-1101-mainagent-lifecycle-body.md" # the living-data clause this scoping backs (hash reference)
  - "devflow/spec/SPEC-260824-1423-delete-safe-consistency.md" # the bounds contract the clause references
risk_class: "low"
autonomy_level: "L3"
turn_budget: ""
data_classification: "internal"
review_ready_at: "2026-08-24T14:49:08-03:00"
review: # AITL-SPEC-Approval — decision dictated in conversation ("listo!!") and transcribed by the agent (§3.0)
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-24T14:55:43-03:00"
  decided_at: "2026-08-24T14:55:43-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved as Dev-validator after an independent cross-model SPEC review whose one substantive finding was adopted pre-stamp: the reviewer's kit-wide pre-sweep found the absolutist G07 phrase on SIX surfaces (not two) — including AGENTS.md, the adopter's auto-loaded entry point where the F-02 gray zone would otherwise survive — so the scope was widened explicitly pre-approval (the Bolt's own if-the-sweep-finds clause executed by design instead of stopping the V-Bounce mid-flight): Phase B' adds the four entry surfaces with one compact scope-out formula, and the Phase C sweep became a zero-remaining gate. The reviewer also verified the ADR-008 precedent real (G18/G24 carry their scoping in-row) and the old texts verbatim. Authorizes the V-Bounce (revision 1)."
---

# SPEC-260824-1447 — The kit G07 scoping

| Field | Value |
|-------|-------|
| **Origin** | US-025 (approved 2026-08-24) |
| **Bolt** | US-025.BOLT-005 (READY 2026-08-24, risk low — the ADR-013 §3.7 citing Bolt) |
| **ADRs** | ADR-013 (the scoping decision), ADR-004 (kit self-containment) |
| **Risk Class** | low |
| **Revision** | 1 |

---

## 1. Objective

Close the REV-005 **F-02** gray zone at the guardrail's letter: state in
the kit's two guardrail surfaces that **the agent lifecycle is operational
configuration, not a code change under G07** — bounded, and never touching
approver authority. After this, the kit's READMEs, the MainAgents'
lifecycle section and the guardrail itself say one thing; no adopter agent
has to resolve a divergence silently again.

## 2. Context

The adopter smoke test proved the failure mode: the kit's READMEs said
living data, G07 said "no code without a Bolt", and the MainAgent picked
one silently (REV-005 F-02, Major). ADR-013 decided the scoping and §3.7
requires the GUARDRAILS text to ship via a Bolt citing the ADR — BOLT-005
is that Bolt (the citation lives in the maintainer partition; the kit text
below stays self-contained, anchored on §5.12 and the shipped
family-README rules).

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | US-025.BOLT-005 | AITL-BOLT-READY-Approval ✓ (2026-08-24T14:47:07) |
| Feature US | US-025 | AITL-US-Approval ✓ |
| ADR | ADR-013 (§3.1–3.5, §3.7) / ADR-004 | AITL-ADR-Approval ✓ |
| REV evidence | REV-005 F-02 | AITL-REV-Approval ✓ |
| Repository baseline | `78094e8` | — |

## 4. Scope

### In scope
- `distribution-kit/devflow/GUARDRAILS.md` — the G07 row's agent response
  (the full-text altitude).
- The four MainAgents — the compressed G07 table row (byte-sync ×4).
- **The four entry-surface statements** (found by the reviewer's kit-wide
  pre-sweep — the Bolt's "if the sweep finds another surface" clause
  executed explicitly, pre-approval): `distribution-kit/AGENTS.md` (the
  adopter's auto-loaded entry point — the most-read surface, where the
  F-02 gray zone would otherwise survive), `devflow/README.md` L319, and
  `devflow/ONBOARDING.md` (the golden rule + the FAQ answer) — each gains
  the same compact scope-out pointer.

### Out of scope
- Every other guardrail row (G-count and their texts untouched); the
  lifecycle section (hash-locked); the methodology §3.2 prose (the sweep
  verifies no verbatim-absolutist duplicate exists — if one appears, stop
  and report, never widen silently); BOLT-004.

## 5. Prerequisites and baseline

- Baseline `78094e8` (BOLT-003's V-Bounce committed; tree clean).
- The verified surfaces: GUARDRAILS.md L72 (the only G07 mention there)
  and the four MainAgents' G07 row (identical ×4).

## 6. Phases

### Phase A — The GUARDRAILS row (full text)

**Duration:** ~30min — **Complexity:** Low

Replace the G07 row's response (old, verbatim on disk):

> ❌ *"No code without an approved Bolt — urgency and size create no exception (§3.2)."*

with:

> ❌ *"No code without an approved Bolt — urgency and size create no
> exception (§3.2). SCOPE: the agent lifecycle is operational
> configuration, not a code change — installing, creating or deleting
> DevFlow Agents within the agent system (`devflow/agents/` squad
> definitions and their platform wrappers; `devflow/actors/` actor files
> and roster listings) is living data (§5.12 and the roster's living-data
> rule), bounded by the lifecycle consistency contract: never the shipped
> examples/templates edited in place, never outside the agent system, and
> approver authority always the human's roster act. Everything else this
> rule covers stays absolutely blocked."*

The attempt column is untouched.

### Phase B — The four MainAgents' row (byte-sync ×4)

**Duration:** ~30min — **Complexity:** Low

Replace (old, identical in the four):

> | G07 | No code change without an approved Bolt (no exceptions — urgency and size create none) |

with:

> | G07 | No code change without an approved Bolt (no exceptions — urgency and size create none; the agent lifecycle — installing/creating/deleting DevFlow Agents within `devflow/agents/` + `devflow/actors/` — is operational config: living data, not a code change) |

### Phase B' — The four entry surfaces (the compact scope-out pointer)

**Duration:** ~30min — **Complexity:** Low

One consistent formula — *"the agent lifecycle within `devflow/agents/` +
`devflow/actors/` is operational config — living data, not a code
change"* — applied at the four spots (old strings verbatim on disk):

**`AGENTS.md`** — old: "approved Bolt and an approved SPEC. Urgency and
size create no exception (G07). If no Bolt authorizes the work, say so
and stop." → new: "approved Bolt and an approved SPEC. Urgency and size
create no exception (G07 — whose one scope-out: the agent lifecycle
within `devflow/agents/` + `devflow/actors/` is operational config —
living data, not a code change). If no Bolt authorizes the work, say so
and stop."

**`devflow/README.md`** — old: "**No code without an approved Bolt** — no
exceptions; urgency and size create none." → new: "**No code without an
approved Bolt** — no exceptions; urgency and size create none (the one
scope-out, G07: the agent lifecycle within `devflow/agents/` +
`devflow/actors/` is operational config — living data)."

**`devflow/ONBOARDING.md` (golden rule)** — old: "**No code without an
approved Bolt** — not a typo, not a config value (G07)." → new: "**No
code without an approved Bolt** — not a typo, not a config value (G07;
its one scope-out: the agent lifecycle within `devflow/agents/` +
`devflow/actors/` is operational config — living data)."

**`devflow/ONBOARDING.md` (FAQ)** — old: "require an approved Bolt.
Urgency and size create no exception." → new: "require an approved Bolt.
Urgency and size create no exception. The one scope-out: the agent
lifecycle (installing/creating/deleting DevFlow Agents within
`devflow/agents/` + `devflow/actors/`) is operational config — living
data, not a code change."

### Phase C — Verification

**Duration:** ~30min — **Complexity:** Low

(1) **G-count 39** in GUARDRAILS.md and in each MainAgent (the scoping
edits text within existing rows — the count invariant proves no
collateral). (2) The four MainAgents' G07 row hashes identically. (3) The
lifecycle section hash **unchanged** (`cd24754c320d…` ×4 — pinned
convention). (4) The **three-altitude read-through**: the GUARDRAILS
clause ⇔ the agents' row ⇔ the lifecycle section's living-data governance
rule express ONE semantics (same scope, same bounds, same
approver-authority exclusion) — any divergence → stop. (5)
Self-containment: no ADR/US references enter the kit text (the §5.12 and
family-rule anchors are shipped kit text). (6) The absolutist-duplicate
sweep, now a ZERO-remaining gate: after Phases A/B/B', **no kit surface
states G07's absolutism without the scope-out** (the six known surfaces
covered; a seventh found → stop, report). (7) No BOM.

## 7. Acceptance criteria

### AC-1: The scoping present at every altitude — six surfaces
**Given** the kit, **When** G07 is read in GUARDRAILS.md, in any
MainAgent, in `AGENTS.md`, in `devflow/README.md` or in
`devflow/ONBOARDING.md` (both spots), **Then** the lifecycle scope-out is
stated (operational config / living data; the full bounds at the
GUARDRAILS altitude, the compact formula at the entry surfaces), and the
rule's blocking force for everything else is verbatim-preserved.

### AC-2: One semantics, three altitudes
**Given** the GUARDRAILS clause, the agents' row and the lifecycle
section, **When** compared, **Then** no contradiction — the row compresses
the clause, the clause backs the section.

### AC-3: Zero collateral
**Given** the diffs, **Then** G-count 39 ×5 surfaces, the four rows
byte-identical, the lifecycle section hash unchanged, no new
maintenance-partition references.

### AC mapping to source

| Source AC | How this SPEC satisfies it | Verifying evidence |
|-----------|----------------------------|--------------------|
| US-025 AC-5 (guardrail-letter completion) | The scoping stated by the guardrail itself | AC-1 + the read-through |
| US-025 AC-6 (reinforced) | The clause names approver authority as the human's roster act | AC-1 |

## 8. Testing strategy

Scripted evidence: G-count ×5, the row hash ×4, the pinned section hash ×4
(reference `cd24754c320d…`), the maintenance-ID sweep on the touched
files, the absolutist-duplicate sweep, BOM. The three-altitude
read-through recorded as a quoted comparison.

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration / SAST / perf | n/a — documentation Bolt | n/a |
| Prompt-injection scan | guardrail text instructs the agent only | pass expected |
| Secret-leak scan | no secrets | pass expected |
| Hallucination lint | the clause's anchors (§5.12, the family rules, the consistency contract) exist in the kit | pass expected |
| IP / license provenance | kit-original text | pass expected |
| PII / DLP | internal docs | pass expected |
| Dependency-confusion | n/a | n/a |
| Test-first evidence | the §8 checks defined before execution | pass expected |
| Behavioral reproducibility | hash/count checks re-run identically | pass expected |
| Bolt-manifest validation | v_bounces[1] appended, schema PASS | pass expected |

## 10. Security and data

This edit touches the kit's strongest blocking rule — the design keeps its
teeth: the clause DEFINES the lifecycle as not-code (a scope statement),
it does not create an exception ladder; every bound (agent-system-only,
never-in-place, human's-act) is restated inside the clause itself so the
scope cannot be read wider than decided. Reviewed verbatim here.

## 11. Monitoring and observability

n/a — documentation family.

## 12. Migration, compatibility and rollback

- **Migration:** framework-file supersede on upgrade (§5.16).
- **Compatibility:** additive scope; adopter projects mid-flight gain
  clarity, lose nothing.
- **Rollback:** `git revert` of the V-Bounce commit.

## 13. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| The scope read wider than decided | 2 | 4 | The bounds restated inside the clause; the read-through vs ADR-013's §3.5 bounds |
| Guardrail-table collateral | 1 | 4 | G-count 39 ×5 + row-hash gates |
| Touching the lifecycle section | 1 | 3 | The pinned-hash unchanged gate |

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| The clause lives INSIDE G07's response, not as a new rule | A new G-row would break the count invariant and fragment the rule; the scope is part of what G07 means now (exactly how ADR-008's scoping reshaped G18/G24 in their own rows) |
| The kit text anchors on §5.12 + the family rules, never the ADR | ADR-004/G28 self-containment — the ADR citation lives in the Bolt (ADR-013 §3.7's own design) |
| "Everything else … stays absolutely blocked" closes the clause | The scope must not soften the rule's absolutism for actual code — stated explicitly to kill the wider reading |
| The scope widened to the six surfaces pre-approval (the reviewer's kit-wide pre-sweep) | The Bolt's own "if the sweep finds another surface" clause, executed explicitly instead of stopping the V-Bounce mid-flight; `AGENTS.md` is the adopter's auto-loaded entry point — leaving it absolutist would preserve the F-02 gray zone exactly where it bit; one compact formula keeps the entry surfaces tight |
| §18 records this as a pre-approval widening (rev 1 still) | The SPEC was draft; the widening is the governed, explicit path the stop condition demands |

## 15. Stop conditions

- The three-altitude read-through finds a semantic divergence → stop,
  reconcile.
- The absolutist-duplicate sweep finds another surface → stop, report
  (never widen the scope silently).
- Any need to touch another guardrail row or the lifecycle section →
  stop.

## 16. Definition of Done (DoD)

- [ ] Phases A–C implemented
- [ ] AC-1..AC-3 pass (evidence recorded)
- [ ] Applicable gates pass / n/a per §9
- [ ] MEM created in `devflow/memory/` (exactly one)
- [ ] Manifest `v_bounces[]` entry appended
- [ ] AITL-MEM-Approval recorded

## 17. References

- US-025 · US-025.BOLT-005 (READY — the ADR-013 §3.7 citing Bolt) ·
  ADR-013 §3.1–3.5/§3.7 · REV-005 F-02 · SPEC-260824-1101 (the section +
  hash reference) · SPEC-260824-1423 (the bounds contract).

## 18. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-24 | eugenio.serrano (agent-drafted) | Revision 1 |
| 2026-08-24 | eugenio.serrano (agent-drafted) | Rev 1 widened pre-approval: the reviewer's kit-wide pre-sweep found four more absolutist surfaces (AGENTS.md, devflow/README.md, ONBOARDING ×2) — Phase B' added; the Phase C sweep became a zero-remaining gate |

## 19. AITL-SPEC-Approval

> Draft until the Dev-validator records `AITL-SPEC-Approval` (frontmatter
> `review:` block). SPEC approval authorizes the code-run / V-Bounce (G14).

| Field | Value |
|-------|-------|
| **review.reviewers** | `human:eugenio.serrano` (dev_validator) |
| **review.decision** | **approved** |
| **review_ready_at** | `2026-08-24T14:49:08-03:00` |
| **review.started_at** | `2026-08-24T14:55:43-03:00` |
| **review.decided_at** | `2026-08-24T14:55:43-03:00` |
| **Findings** | one substantive (the six-surface pre-sweep) — adopted pre-stamp as Phase B' + the zero-remaining gate (reason in the frontmatter `review:` block) |
