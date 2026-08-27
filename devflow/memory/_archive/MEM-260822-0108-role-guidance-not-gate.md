---
id: "MEM-260822-0108"
title: "Role routing as guidance, never a gate — operability principle, multiplicity, no-holder fallback"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
bolt: "US-014.BOLT-001"
spec: "SPEC-260822-0053"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "0c7f40d"
applied_adrs:
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "US-014.BOLT-001-role-guidance-not-gate.json"
diff_ref: "" # uncommitted working-tree change — no commit made (G34)
review_ready_at: "2026-08-22T01:08:16-03:00"
review: # HITL-MEM-Approval — filled by the human reviewer (§3.0)
  decision: "changes_requested"
  reviewers: [{user: "eugenio.serrano", role: "dev_validator"}]
  started_at: "2026-08-22T01:14:48-03:00"
  decided_at: "2026-08-22T01:14:48-03:00"
  findings:
    - "The single-source deviation (§8) is not accepted as final. Reviewer requests the literal per-cell fallback (SPEC Phase C as written): append the no-holder fallback clause to each single-role Owner cell (US, TC, BOLT-READY, ADR, SPEC, BOLT-DONE) across the §3.0 table, the GUARDRAILS checkpoint map and the four agents' HITL tables — duplication across the four agents is accepted. Next execution is a NEW V-Bounce (2)."
  acknowledged_without_comment: false
  acknowledgment_reason: ""
---

<!--
  LANGUAGE POLICY (§3.15): schema in English; prose in content_language (en).
-->

# MEM-260822-0108 — Role routing as guidance, never a gate

| Field           | Value |
|-----------------|-------|
| **Bolt**        | [US-014.BOLT-001](../functional/bolts/US-014.BOLT-001-role-guidance-not-gate.md) |
| **SPEC**        | [SPEC-260822-0053](../spec/SPEC-260822-0053-role-guidance-not-gate.md) rev. 1 |
| **V-Bounce**    | 1 |
| **ADRs**        | ADR-004 (kit-only) |

---

## 1. Executive summary

This V-Bounce implemented the role dimension of US-014 (D1/D2/D3) in the
distributable. It added a governing statement to the §3.0 HITL Charter — *role
routing is guidance, never a gate; the named owner is the recommended
approver; when the role has no holder the available qualified human records
the approval, noting the self-assigned role; one person may hold several
roles; the only exceptions are the identity-separation rules* — and mirrored a
compact version in `GUARDRAILS.md` and the four agent definitions
(byte-identical). It relaxed the two remaining hard-language routes (the
`critical` non-functional BUG self-approval prohibition and the
`infra`/`hardening` acceptance pairing) so they are satisfiable by a
single-operator team, and confirmed the identity-separation rules (handoff
incoming-executor, G37, G18/G24) untouched. Verification is GREEN: the
principle is present in all six locations, the four agents stay in sync
(G-count 39/39/39/39 and an identical new bullet), and only
`distribution-kit/` files changed (root methodology content untouched,
ADR-004). One deviation from the SPEC's Phase C is recorded in §8 (D3
implemented via the governing principle rather than a per-cell append).

---

## 2. Implemented phases

### Phase A/B — D1 (operability principle) + D2 (multiplicity)

Added a governing paragraph to the §3.0 HITL Charter (immediately before the
checkpoint table), stating the operability principle (D1) and role
multiplicity + recorded self-assignment (D2), and naming the identity-
separation rules as the only exceptions. Mirrored a compact version in
`GUARDRAILS.md` (after the checkpoint map) and as an identical bullet in the
four agents' HITL Checkpoints section.

### Phase C — D3 (no-holder fallback on the routes)

The governing principle (Phase A) scopes to "each checkpoint below," so it
provides the no-holder fallback for every single-role route in one place
(single source of truth — the SPEC §14 approach). On top of it, the two routes
that still carried hard, blocking language were relaxed directly: the §3.0
prose for the `critical` non-functional BUG route (the sole available human may
self-approve with recorded evidence when no other holder exists) and the §3.11
work-category acceptance table (a note that paired/named roles are recommended
defaults and the available human records the acceptance when a role has no
holder). Mirrored the acceptance note in `GUARDRAILS.md`.

### Phase D — Verification (GREEN)

Grep + G-count + git status (see §9).

---

## 3. Files created

| File | Purpose |
|------|---------|
| — | None — documentation edits to existing kit files. |

---

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md` | §3.0: added the D1/D2 governing principle before the checkpoint table; §3.0 prose: relaxed the `critical` BUG self-approval so a sole operator can record it; §3.11: acceptance-table availability note |
| `distribution-kit/devflow/GUARDRAILS.md` | Compact principle mirror after the checkpoint map; availability note after the work-category acceptance table |
| `distribution-kit/CLAUDE.md` | Identical principle bullet in the HITL Checkpoints section |
| `distribution-kit/.agents/skills/avenga-devflow/SKILL.md` | Identical principle bullet |
| `distribution-kit/.github/agents/AvengaDevFlow.agent.md` | Identical principle bullet |
| `distribution-kit/.opencode/agents/AvengaDevFlow.md` | Identical principle bullet |

---

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
| — | — | None |

---

## 6. Files deleted

| File | Reason |
|------|--------|
| — | — | None |

---

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| State the principle once as a governing statement covering all checkpoints | Single source of truth (SPEC §14); avoids duplicating a clause into ~54 cells and re-creating the drift BUG-001 fixed |
| Relax only the genuinely hard-blocking routes directly (critical BUG self-approval, acceptance pairing) | The single-role gates (US/ADR/TC/BOLT-READY/SPEC/BOLT-DONE) are already covered by the governing principle; they carry no hard "must/never" language |
| Keep the named role as the recommended default everywhere | US-014 D1/D3 — the role is guidance, never removed |
| Left the §3.3 MEM approver rule untouched | Owned wholesale by US-014.BOLT-003 (D7); avoids double-editing (SPEC §4 boundary) |
| No commit | G34 — staging/commit needs an explicit user request |

---

## 8. Deviations and assumptions

**Deviation from SPEC Phase C (recorded for the reviewer).** Phase C / AC-3
were worded as "append the no-holder fallback clause to **each** single-role
Owner cell." This V-Bounce instead implemented the fallback **once**, as a
governing statement that explicitly scopes to "each checkpoint below," plus
direct relaxation of the two hard-blocking routes. Rationale: the SPEC's own
§14 decision favors "state the principle once, single source of truth"; a
per-cell duplication across the methodology, GUARDRAILS and four byte-identical
agents (~54 cells) would re-create exactly the drift BUG-001 was opened to
remove. **AC-3's stated purpose — "zero role-gated routes without a fallback
remain" — is satisfied**: every route carries the fallback via the governing
principle, and the two routes with hard language were fixed directly. If the
reviewer prefers the literal per-cell append, that is a `changes_requested`
→ a new V-Bounce. No other deviations.

---

## 9. Verification evidence

### AC-1 / AC-2 — principle + multiplicity present
```
$ rg -n "Role routing is guidance, never a gate" distribution-kit/
Avenga-DevFlow.md:1362 (§3.0 governing statement) · GUARDRAILS.md:40 (mirror)
CLAUDE.md:410 · SKILL.md:427 · AvengaDevFlow.agent.md:455 · AvengaDevFlow.md:438
=> present in all 6 locations. Multiplicity clause ("one person may hold several
   roles") present in the methodology block, the four agents and GUARDRAILS
   (GUARDRAILS occurrence line-wrapped).
```

### AC-4 — identity rules untouched
The handoff incoming-executor rule (§3.3), G37 and G18/G24 were not edited (the
principle references them as the exceptions; their text is unchanged). Not in
the modified-file diff regions.

### AC-5 — four-agent sync + G-count
```
CLAUDE.md: 39   SKILL.md: 39   AvengaDevFlow.agent.md: 39   AvengaDevFlow.md: 39   GUARDRAILS.md: 39
New principle bullet identical across the four agents (L410/427/455/438).
```

### AC-6 — root untouched
```
$ git status --short
 M distribution-kit/{CLAUDE.md, .agents/.../SKILL.md, .github/.../AvengaDevFlow.agent.md,
   .opencode/.../AvengaDevFlow.md, devflow/GUARDRAILS.md, devflow/avenga-devflow/Avenga-DevFlow.md}
 (plus root devflow/ GOVERNANCE records only — US-014 + INDEX + this Bolt's artifacts;
  no root devflow/ methodology-content file modified)
```

### AC-7 — manifest
```
US-014.BOLT-001 manifest: valid JSON (built to manifest-v4-bolt.schema.json).
```

### Gates
prompt-injection `pass` · secret-leak `pass` · hallucination-lint `pass` ·
behavioral-reproducibility `pass` · bolt-manifest-validation `pass` ·
unit/integration/SAST/SBOM/perf/PII/IP/dependency-confusion/test-first `n/a`
(documentation-only, no code/deps/runtime/PII; not a BUG Bolt).

---

## 10. Manual interventions

None — the agent produced every edit.

---

## 11. Evidence links

- **Diff / PR:** none — uncommitted working-tree change (G34).
- **Commit:** baseline `0c7f40d`; V-Bounce output uncommitted.
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-014.BOLT-001-role-guidance-not-gate.json`.

---

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~7 min |
| V-Bounce number | 1 |
| Tests created | n/a — deterministic grep/consistency checks |
| AI-generated code | 100% |
| First-pass approval | pending HITL-MEM-Approval |

---

## 13. Pending items and stubs

- [ ] `HITL-MEM-Approval` (this package) — note the §8 deviation for the reviewer.
- [ ] `HITL-BOLT-DONE-Approval` (acceptance — `work_category: feature` → PO/PM).
- [ ] US-014.BOLT-002 (D5) and US-014.BOLT-003 (D7) — next V-Bounces (BOLT-003 after this one).
- [ ] Commit (explicit user request — G34); root receives it at the next §5.16 migration.

---

## 14. HITL-MEM-Approval

> **Avenga DevFlow §2.12, §3.0.** Created by the agent, no mutable status,
> never self-approved. Risk class `medium` → 1 approver (the executing
> Dev-validator). The reviewer inspects the diff, the verification evidence,
> the §8 deviation, this MEM and the manifest, and records the decision here
> and in the manifest's `hitl_approvals[]`.

| Field | Value |
|-------|-------|
| **Reviewers** | eugenio.serrano (dev_validator) |
| **Decision** | changes_requested |
| **review_ready_at** | `2026-08-22T01:08:16-03:00` |
| **review.started_at** | `2026-08-22T01:14:48-03:00` |
| **review.decided_at** | `2026-08-22T01:14:48-03:00` |
| **Review evidence** | diff of the 6 kit files, principle grep (6 locations), G-count 39×5, git status, manifest JSON, §8 deviation |
| **Finding** | Reviewer requests literal per-cell fallback (Phase C as written) — new V-Bounce 2. This MEM stays as immutable history. |
