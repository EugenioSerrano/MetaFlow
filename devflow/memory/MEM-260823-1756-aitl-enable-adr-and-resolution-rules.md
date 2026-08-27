---
id: "MEM-260823-1756"
title: "The AITL-enable ADR template and the roster resolution rules (US-024.BOLT-002)"
date: "2026-08-23"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
bolt: "US-024.BOLT-002"
spec: "devflow/spec/SPEC-260823-1742-aitl-enable-adr-and-resolution-rules.md"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "45d553f"
applied_adrs:
  - "devflow/adrs/ADR-008-aitl-approval-precept.md"
  - "devflow/adrs/ADR-010-actor-grammar-and-pure-v5-vocabulary.md"
manifest: "devflow/metrics/bolts/US-024.BOLT-002-aitl-enable-adr-template.json"
diff_ref: ""
review_ready_at: "2026-08-23T17:56:00-03:00"
review: # AITL-MEM-Approval — recorded by the human reviewer (§3.0); decision dictated in conversation ("aprobado punto 1 y 2") and transcribed by the agent
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-23T18:11:00-03:00"
  decided_at: "2026-08-23T18:12:42-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved as Dev-validator: the AITL-enable ADR template (the one governed act + the guardrails) and the resolution rules (the five rules incl. the definitions-sharing clause) inspected; the self-containment grep (0 hits); kit-only. V-Bounce 1 approved — BOLT-002 Development Completed."
---

# MEM-260823-1756 — The AITL-enable ADR template + the resolution rules (US-024.BOLT-002, V-Bounce 1)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | US-024.BOLT-002 (aitl-enable-adr-template) |
| **SPEC**        | [SPEC-260823-1742](../spec/SPEC-260823-1742-aitl-enable-adr-and-resolution-rules.md) rev 1 |
| **V-Bounce**    | 1 |
| **ADRs**        | ADR-008 (the precept — safe default + human ceiling), ADR-010 (grammar) |

---

## 1. Executive summary

This V-Bounce delivered the roster's **decision layer** in the kit's
`actors/` folder: (1) `TEMPLATE-AITL-ENABLE-ADR.md` — the per-project
ADR template, the **one governed act** that enables virtual approvers:
context, the three decision fields (enabled checkpoint classes, roster
contents, instantiated approver charters) and the guardrails (the safe
default — no AI-signed approval without this human act; the `human_only`
floor that may be tightened, never loosened; the independence requirement;
the approver ceiling T0/T1; and the re-trigger note — changing an
approver's charter/authority fields re-opens the ADR's review); and (2)
the **resolution-rule text** in `actors/README.md` — the five rules:
role → actors (humans and agents as peers; agent holders only for enabled
checkpoint classes), who produces (derived from `role`), the independence
ladder (`approver.id ≠ executor.id`; model hardening at `high` — enabled
by the per-instance `model`; the human ceiling at
`critical`/`regulatory`), the definitions-sharing rule (two actors, one
definition, distinct ids/models), and the zero-config invariant (no actor
files, or none declares a DevFlow Agent → byte-for-byte pure HITL). The
verification is GREEN: the template present with the five fields + the
guardrails; all five rules present; the **self-containment check** passes
(grep over the delivered kit files → 0 hits); no BOM; kit-only. The
deliverables are self-contained — an adopter's AITL-enable ADR names its
roster without any maintenance references.

## 2. Implemented phases

### Phase A — The AITL-enable ADR template

`TEMPLATE-AITL-ENABLE-ADR.md` — the ADR-shaped template (context +
decision with the three fields + consequences), with the built-in
guardrails: the safe default (the only door), the human-only floor (may
be tightened, never loosened), the independence requirement, the approver
ceiling, and the re-trigger note.

### Phase B — The resolution-rule text

`actors/README.md` gained the "Resolution rules" section (the five rules
above) + the pointer to the template.

### Phase C — Verification (GREEN)

Template fields present ×5; rules present ×5; the self-containment grep
(0 hits); no BOM; kit-only.

## 3. Files created

| File | Purpose |
|------|---------|
| `distribution-kit/devflow/actors/TEMPLATE-AITL-ENABLE-ADR.md` | The per-project ADR template — the one governed act that enables virtual approvers (enabled checkpoint classes, roster contents, approver charters + the guardrails) |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `distribution-kit/devflow/actors/README.md` | The "Resolution rules" section (role → actors, production lookup, independence ladder, definitions-sharing, zero-config) + the template pointer |

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
| — | — | — |

## 6. Files deleted

| File | Reason |
|------|--------|
| — | — |

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| The template lives in `actors/` (not `adrs/`) | It is the roster's enabling act — the family home |
| The resolution rules live in the actors/README | The roster docs are where the lookup is explained; self-contained |
| The template's guardrails are built-in, not advisory | The safe-default + the human-only floor are the ADR's contract — an enabling act without them is not an enabling act |
| The definitions-sharing rule included in the resolution text | US-024 AC-5 (Modelo B): actors sharing a definition stay independent at the actor level; distinct per-instance models at `high` |

## 8. Deviations and assumptions

No deviations from SPEC-260823-1742 rev 1. Assumption: the adopter's
AITL-enable ADR follows the template as-is (the three fields + the
guardrails).

## 9. Verification evidence

### Presence (RED → GREEN)

```
RED:   no TEMPLATE-AITL-ENABLE-ADR.md; no "Resolution rules" in the README
GREEN: template PRESENT — fields: Enabled checkpoint classes · Roster
       contents · Instantiated approver charters · safe default ·
       human_only · re-triggers (all PRESENTE)
       README rules PRESENT — Role → actors · Who produces ·
       Independence ladder · Definitions shared · Zero-config
```

### Self-containment (the review's explicit check)

```
grep -E "US-[0-9]{3}|ADR-[0-9]{3}|DISC-[0-9]{3}|BOLT-[0-9]|SPEC-26|MEM-26|
REV-[0-9]{3}|TC-[0-9]{3}" over distribution-kit/devflow/actors/* →
0 hits — SELF-CONTAINED PASS
```

### Invariants

```
Kit-only: only distribution-kit/ changes   PASS
Encoding: 0 files with BOM                  PASS
```

### Gates

Documentation Bolt: runtime gates `n/a`; prompt-injection/secret-leak
`pass`; hallucination-lint `pass` (the §3.0.1 anchors resolve);
behavioral-reproducibility `pass`; bolt-manifest-validation `pass`
(v_bounces[1] appended, JSON valid).

## 10. Manual interventions

None — the agent produced everything.

## 11. Evidence links

- **Diff / PR:** none (working tree, uncommitted)
- **Commit:** baseline `45d553f`
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-024.BOLT-002-aitl-enable-adr-template.json`

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~10min |
| V-Bounce number | 1 |
| Tests created | 0 (documentation Bolt — presence/self-containment evidence) |
| AI-generated code | 100% |
| First-pass approval | pending (this MEM) |

## 13. Pending items and stubs

- [ ] BOLT-003 V-Bounce (the human-roster guarantees + the US-001 record
      closure)
- [ ] The adopter's AITL-enable ADR instances follow the template

## 14. AITL-MEM-Approval

> **Avenga DevFlow §2.12, §3.0.** This MEM is created by the agent with no
> mutable status and is **never self-approved**. A qualified human (the
> Dev-validator who executed the Bolt) inspects the actual diff,
> test/gate evidence, MEM and manifest, and records `AITL-MEM-Approval`
> here and in the manifest's `checkpoint_approvals[]`.

| Field | Value |
|-------|-------|
| **Reviewers (executing Dev-validator)** | `human:eugenio.serrano` |
| **Roles** | dev_validator |
| **Decision** | approved / changes_requested / rejected |
| **review_ready_at** | `2026-08-23T17:56:00-03:00` |
| **review.started_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **review.decided_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **Review evidence** | diff of the template + the README rules; presence checks; the self-containment grep (0 hits); kit-only; MEM, manifest |
| **Comments** | |
| **Findings** | |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | evidence inspected per the review-evidence column |
