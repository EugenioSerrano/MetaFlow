---
id: "MEM-260822-0119"
title: "Role routing as guidance, never a gate — per-cell fallback (V-Bounce 2)"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
bolt: "US-014.BOLT-001"
spec: "SPEC-260822-0053"
spec_revision: 1
v_bounce: 2
execution_outcome: "ready_for_review"
baseline: "0c7f40d"
applied_adrs:
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "US-014.BOLT-001-role-guidance-not-gate.json"
diff_ref: "" # uncommitted working-tree change — no commit made (G34)
review_ready_at: "2026-08-22T01:19:44-03:00"
review: # HITL-MEM-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "dev_validator"}]
  started_at: "2026-08-22T01:21:25-03:00"
  decided_at: "2026-08-22T01:21:25-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Inspected the per-cell diff: the no-holder fallback is present in all six single-role Owner cells across the §3.0 table, the GUARDRAILS map and the four agents (identical, 7× each — four-agent sync preserved), G-count 39×5, MEM approver rule and identity rules untouched, root methodology content untouched. Resolves the V-Bounce 1 changes_requested (literal Phase C). No deviations. Approved."
---

<!--
  LANGUAGE POLICY (§3.15): schema in English; prose in content_language (en).
  V-Bounce 2 — addresses the changes_requested on V-Bounce 1 (MEM-260822-0108):
  the literal per-cell fallback (SPEC Phase C as written).
-->

# MEM-260822-0119 — Role routing as guidance, never a gate: per-cell fallback (V-Bounce 2)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | [US-014.BOLT-001](../functional/bolts/US-014.BOLT-001-role-guidance-not-gate.md) |
| **SPEC**        | [SPEC-260822-0053](../spec/SPEC-260822-0053-role-guidance-not-gate.md) rev. 1 |
| **V-Bounce**    | 2 |
| **ADRs**        | ADR-004 (kit-only) |

---

## 1. Executive summary

This is V-Bounce 2 of US-014.BOLT-001, addressing the `changes_requested` on
V-Bounce 1 (MEM-260822-0108): the reviewer asked for the **literal per-cell
fallback** of SPEC Phase C rather than the single-source deviation. Building on
V-Bounce 1's output (the D1 operability principle, the D2 multiplicity clause,
and the two hard-route relaxations — all correct and retained), this V-Bounce
**appended the no-holder fallback clause to each single-role Owner cell** — US,
TC, BOLT-READY, ADR, SPEC and BOLT-DONE — across the §3.0 checkpoint table, the
`GUARDRAILS.md` checkpoint map, and the four agents' HITL tables: **36 cell
edits** (6 routes × 6 locations). The MEM approver rule was left untouched
(BOLT-003/D7) and the identity-separation rules untouched. Verification is
GREEN: the clause appears 7× per agent (identical across the four), 8× each in
the methodology and GUARDRAILS; G-count 39/39/39/39/39; and only
`distribution-kit/` + governance records changed (root methodology untouched).

---

## 2. Implemented phases

### Phase C (literal) — per-cell no-holder fallback

Appended the identical clause *"(or, if the/a named role has no holder, the
available qualified human records it, noting the self-assigned role)"* to the
Owner cell of each single-role route in three places each:
- **Methodology §3.0 checkpoint table:** US, TC, BOLT-READY, ADR, SPEC, BOLT-DONE.
- **`GUARDRAILS.md` checkpoint map:** the same six rows.
- **The four agents' HITL tables:** the same six rows, byte-identical across all four.

V-Bounce 1's D1 principle, D2 clause, critical-BUG relaxation and acceptance
note remain in place (they were correct; the reviewer's change was only the
per-cell coverage). The `HITL-MEM-Approval` (§3.3) owner cell was deliberately
**not** touched — its wholesale rewrite is US-014.BOLT-003 (D7). UNIT/UAT rows
were not touched (removed by US-015). Identity-separation rules unchanged.

### Phase D — Verification (GREEN)

Grep coverage + four-agent parity + G-count + root check (see §9).

---

## 3. Files created

| File | Purpose |
|------|---------|
| — | None — documentation edits to existing kit files. |

---

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md` | Appended the no-holder fallback to the 6 single-role Owner cells in the §3.0 checkpoint table |
| `distribution-kit/devflow/GUARDRAILS.md` | Appended the fallback to the same 6 rows in the checkpoint map |
| `distribution-kit/CLAUDE.md` | Appended the fallback to the 6 HITL-table Owner cells |
| `distribution-kit/.agents/skills/avenga-devflow/SKILL.md` | Same 6 cells (identical) |
| `distribution-kit/.github/agents/AvengaDevFlow.agent.md` | Same 6 cells (identical) |
| `distribution-kit/.opencode/agents/AvengaDevFlow.md` | Same 6 cells (identical) |

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
| Append the identical clause to each single-role cell | Reviewer's `changes_requested` on V-Bounce 1 — literal per-cell coverage (SPEC Phase C as written); duplication across the four agents accepted |
| Retain V-Bounce 1's principle/multiplicity/relaxations | They were correct; the change requested was only per-cell coverage |
| Leave the MEM approver cell untouched | Owned by US-014.BOLT-003 (D7); avoids double-editing §3.3 |
| Keep the clause identical across the four agents | Four-agent sync invariant (AGENTS.md) — AC-5 |
| No commit | G34 — staging/commit needs an explicit user request |

---

## 8. Deviations and assumptions

None. This V-Bounce implements SPEC Phase C literally (per-cell), resolving the
V-Bounce 1 deviation. Assumption: the two clause variants ("the named role" for
single-role cells, "a named role" for cells listing several roles) are
equivalent in meaning — chosen for grammatical fit; the routing rule is
identical.

---

## 9. Verification evidence

### AC-3 (literal per-cell coverage) + AC-5 (four-agent sync)
```
$ rg -c "noting the self-assigned role" distribution-kit/
CLAUDE.md: 7   SKILL.md: 7   AvengaDevFlow.agent.md: 7   AvengaDevFlow.md: 7   (identical → four-agent sync)
Avenga-DevFlow.md: 8   GUARDRAILS.md: 8
  (per agent: 1 principle bullet + 6 per-cell = 7; methodology/GUARDRAILS: principle + notes + 6 per-cell)
$ grep -cE '^\| G[0-9][0-9] ' <each of the four agents + GUARDRAILS>  => 39 / 39 / 39 / 39 / 39
```
The six single-role routes (US, TC, BOLT-READY, ADR, SPEC, BOLT-DONE) now carry
the fallback in their own cell in the methodology table, the GUARDRAILS map and
all four agents.

### AC-4 (identity rules) / AC-6 (root)
```
Handoff incoming-executor (§3.3), G37, G18/G24 — not edited.
$ git status --short | (nothing outside distribution-kit/ and devflow/)
  => only distribution-kit/ files + root devflow/ governance records changed;
     no root devflow/ methodology content.
```

### AC-7 (manifest)
```
US-014.BOLT-001 manifest: valid JSON (v_bounces: 2, spec_revisions: 1).
```

### Gates
prompt-injection / secret-leak / hallucination-lint / behavioral-reproducibility /
bolt-manifest-validation `pass`; unit/integration/SAST/SBOM/perf/PII/IP/
dependency-confusion/test-first `n/a` (documentation-only).

---

## 10. Manual interventions

None — the agent produced every edit.

---

## 11. Evidence links

- **Diff / PR:** none — uncommitted working-tree change (G34).
- **Commit:** baseline `0c7f40d`; V-Bounce output uncommitted.
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-014.BOLT-001-role-guidance-not-gate.json` (v_bounces 1 + 2).

---

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~5 min |
| V-Bounce number | 2 |
| Tests created | n/a — deterministic grep/consistency checks |
| AI-generated code | 100% |
| First-pass approval | pending HITL-MEM-Approval |

---

## 13. Pending items and stubs

- [ ] `HITL-MEM-Approval` for V-Bounce 2.
- [ ] `HITL-BOLT-DONE-Approval` (acceptance — `feature` → PO/PM).
- [ ] US-014.BOLT-002 (D5) and US-014.BOLT-003 (D7) — next V-Bounces.
- [ ] Commit (explicit user request — G34); root receives it at the next §5.16 migration.

---

## 14. HITL-MEM-Approval

> **Avenga DevFlow §2.12, §3.0.** Created by the agent, no mutable status,
> never self-approved. Risk `medium` → 1 approver (the executing
> Dev-validator). This V-Bounce (2) supersedes V-Bounce 1's approach per the
> recorded `changes_requested`; V-Bounce 1's MEM (MEM-260822-0108) stays as
> immutable history.

| Field | Value |
|-------|-------|
| **Reviewers** | eugenio.serrano (dev_validator) |
| **Decision** | approved |
| **review_ready_at** | `2026-08-22T01:19:44-03:00` |
| **review.started_at** | `2026-08-22T01:21:25-03:00` |
| **review.decided_at** | `2026-08-22T01:21:25-03:00` |
| **Review evidence** | per-cell coverage grep (7× per agent, identical), G-count 39×5, git status, manifest JSON (v_bounces 2) |
