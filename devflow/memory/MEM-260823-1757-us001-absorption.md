---
id: "MEM-260823-1757"
title: "The human-roster guarantees absorption + the US-001 deprecation record closure (US-024.BOLT-003)"
date: "2026-08-23"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
bolt: "US-024.BOLT-003"
spec: "devflow/spec/SPEC-260823-1743-us001-absorption.md"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "45d553f"
applied_adrs:
  - "devflow/adrs/ADR-010-actor-grammar-and-pure-v5-vocabulary.md"
manifest: "devflow/metrics/bolts/US-024.BOLT-003-us001-absorption.json"
diff_ref: ""
review_ready_at: "2026-08-23T17:57:00-03:00"
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
  acknowledgment_reason: "Approved as Dev-validator: the human-roster guarantees section (named without the maintenance ID; 'US-001' absent from the kit README) + the deprecation record closure (G36) inspected; the self-containment grep (0 hits); record consistency. V-Bounce 1 approved — BOLT-003 Development Completed."
---

# MEM-260823-1757 — The human-roster guarantees + the record closure (US-024.BOLT-003, V-Bounce 1)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | US-024.BOLT-003 (us001-absorption) |
| **SPEC**        | [SPEC-260823-1743](../spec/SPEC-260823-1743-us001-absorption.md) rev 1 |
| **V-Bounce**    | 1 |
| **ADRs**        | ADR-010 (grammar) |

---

## 1. Executive summary

This V-Bounce absorbed the deprecated human roster's guarantees as a
special case of the unified actors roster and closed the deprecation
record. The kit's `actors/README.md` gained the **"Single-maintainer /
human-roster guarantees"** section — named **without the maintenance ID**
(an adopter has no US-001): external reviewers (single-maintainer teams
may name one), optionality (an empty roster changes nothing), migration
travel (the roster family travels with the §5.16 migration), and living
data (member join/leave updates require no approval — except an
*approver's* charter or authority fields, which re-trigger the
AITL-enable ADR review). The US-001 deprecation record was **confirmed
and completed**: its status was already `deprecated`; the body now states
explicitly that its ACs are absorbed as a special case in the kit's
roster docs; the INDEX row (Deprecated section) is consistent. History is
preserved (G36 — US-001 was never approved, so no recorded decision is
affected). The verification is GREEN: the section present (0 occurrences
of the string "US-001" in the kit README), the four special cases
present, the **self-containment check** passes (grep over the delivered
kit files → 0 hits), the US-001 doc + INDEX consistent, no BOM. With this
Bolt, **US-024 is fully delivered** — the roster family (shape + decision
layer + legacy guarantees) is complete in the kit.

## 2. Implemented phases

### Phase A — The absorption text (kit)

`actors/README.md` gained the "Single-maintainer / human-roster
guarantees" section (the four special cases + the AITL-enable ADR
pointer), self-contained wording, no maintenance IDs.

### Phase B — The deprecation record closure (maintenance)

US-001's body table now states the absorption explicitly ("its ACs are
absorbed as a special case in the kit's roster docs — the
'Single-maintainer / human-roster guarantees' section"); the frontmatter
`status: deprecated` and the INDEX row (Deprecated section) confirmed
consistent.

### Phase C — Verification (GREEN)

Section present; "US-001" string absent from the kit README; the four
special cases present; the self-containment grep (0 hits); US-001 doc +
INDEX consistent; no BOM.

## 3. Files created

| File | Purpose |
|------|---------|
| — | none (edits within existing files) |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `distribution-kit/devflow/actors/README.md` | The "Single-maintainer / human-roster guarantees" section (the four special cases, self-contained, no maintenance IDs) |
| `devflow/functional/user-stories/US-001-team-roster.md` | The deprecation record completed — the body states the absorption (status `deprecated` already present; history preserved) |

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
| The section is named without the maintenance ID | Self-containment (the review's explicit fix): an adopter has no US-001 |
| The US-001 record is confirmed, not rewritten | G36: history preserved; it was never approved, so closure is clean |
| The special cases stay verbatim | They are the human-roster guarantees — absorbed, not altered |
| The INDEX row needed no change | It was already in the Deprecated section, consistent |

## 8. Deviations and assumptions

No deviations from SPEC-260823-1743 rev 1. Assumption: the INDEX row and
the frontmatter were already consistent (confirmed); only the body's
absorption statement was completed.

## 9. Verification evidence

### Presence (RED → GREEN)

```
RED:   no "Single-maintainer / human-roster guarantees" section
GREEN: section PRESENT; "US-001" string in the kit README: 0
       special cases: External reviewers · Optionality · Migration ·
       Living data — all PRESENTE
```

### Self-containment (the review's explicit check)

```
grep -E "US-[0-9]{3}|ADR-[0-9]{3}|DISC-[0-9]{3}|BOLT-[0-9]|SPEC-26|MEM-26|
REV-[0-9]{3}|TC-[0-9]{3}" over distribution-kit/devflow/actors/* →
0 hits — SELF-CONTAINED PASS
```

### Record consistency (maintenance partition)

```
US-001 doc: status deprecated + "its ACs are absorbed as a special case
in the kit's roster docs" present
INDEX: US-001 row present in the Deprecated section
G36: no recorded decision affected (never approved)
```

### Invariants

```
Kit-only for the kit part + the two maintenance records  PASS
Encoding: 0 files with BOM                               PASS
```

### Gates

Documentation Bolt: runtime gates `n/a`; prompt-injection/secret-leak
`pass`; hallucination-lint `pass` (refs resolve);
behavioral-reproducibility `pass`; bolt-manifest-validation `pass`
(v_bounces[1] appended, JSON valid).

## 10. Manual interventions

None — the agent produced everything.

## 11. Evidence links

- **Diff / PR:** none (working tree, uncommitted)
- **Commit:** baseline `45d553f`
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-024.BOLT-003-us001-absorption.json`

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~10min |
| V-Bounce number | 1 |
| Tests created | 0 (documentation Bolt — presence/self-containment/consistency evidence) |
| AI-generated code | 100% |
| First-pass approval | pending (this MEM) |

## 13. Pending items and stubs

- [ ] Batch approvals: MEM-1755 (BOLT-001), MEM-1756 (BOLT-002), this MEM
      (BOLT-003) + AITL-BOLT-DONE ×3 → **US-024 delivered**
- [ ] The pilot US + US-025 (MainAgent lifecycle) are the next family
      chapters

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
| **review_ready_at** | `2026-08-23T17:57:00-03:00` |
| **review.started_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **review.decided_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **Review evidence** | diff of the README section + the US-001 record; the "US-001 absent from the kit README" check; the self-containment grep (0 hits); record consistency; MEM, manifest |
| **Comments** | |
| **Findings** | |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | evidence inspected per the review-evidence column |
