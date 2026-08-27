---
id: "MEM-260822-0342"
title: "Add the no-holder fallback to the §3.0 checkpoint narrative and TC route texts (ADR-005 positive-coverage) — BUG-003 fix"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
bolt: "US-000.BOLT-006"
spec: "SPEC-260822-0338"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "c30a739"
applied_adrs:
  - "devflow/adrs/ADR-005-removal-completeness-phrase-family-sweep.md"
  - "devflow/adrs/ADR-002-documentation-defect-classification.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "US-000.BOLT-006-role-gate-narrative-fallback-sweep.json"
diff_ref: ""
review_ready_at: "2026-08-22T03:42:38-03:00"
review: # HITL-MEM-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "dev_validator"}]
  started_at: "2026-08-22T03:45:48-03:00"
  decided_at: "2026-08-22T03:45:48-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Reviewed the 2-file kit diff and the §9 RED/GREEN evidence: all 7 §3.0 checkpoint bullets + §2.6.1 + TEMPLATE-TC now carry the fallback clause (signature = 8, no double-insertion), the allowlist held (DISC/REV/AREV bullets and HITL-MEM untouched, verified by grep -A2), narrative agrees with the table, agents undisturbed and byte-synced 39x5, root untouched. BUG-003 cleared. Bolt now Development Completed."
---

<!--
  LANGUAGE POLICY (§3.15): schema/headings English; prose content_language (en).
  BUG V-Bounce (ADR-002 class 1): RED/GREEN = deterministic grep. Kit-only
  (ADR-004); root untouched. Second application of ADR-005 (positive-coverage).
-->

# MEM-260822-0342 — No-holder fallback in the §3.0 narrative + TC route texts (BUG-003, ADR-005 positive-coverage)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | [US-000.BOLT-006](../functional/bolts/US-000.BOLT-006-role-gate-narrative-fallback-sweep.md) |
| **SPEC**        | [SPEC-260822-0338](../spec/SPEC-260822-0338-role-gate-narrative-fallback-sweep.md) — revision 1 |
| **V-Bounce**    | 1 |
| **ADRs**        | ADR-005 (sweep standard), ADR-002 (class 1), ADR-004 (kit-only) |

---

## 1. Executive summary

This V-Bounce fixes BUG-003 (AREV-003 F-02, widened by the ADR-005 sweep from 2
to 9 locations): the §3.0 **normative narrative** still gated 7 checkpoints on
named roles unconditionally, contradicting its own §3.0 table (which carried the
no-holder fallback from US-014.BOLT-001) and defeating single-operator
operability for narrative readers. It is the **second application of ADR-005**,
in its **positive-coverage** form — assert every route statement *carries* the
clause. The canonical fallback clause ("if a named role has no holder, the
available qualified human records the approval, noting the self-assigned role —
role routing is guidance, not a gate") was appended to the 7 §3.0 "Who" bullets
(US, BUG functional route, TC, BOLT-READY, ADR, SPEC, BOLT-DONE), to the §2.6.1
TC lifecycle text, and to `TEMPLATE-TC.md` §10. The 5 role-agnostic DISC/REV/AREV
bullets and the just-corrected HITL-MEM bullet were deliberately left untouched
(allowlist). Outcome: all 7 checkpoints now carry the clause, the clause
signature "guidance, not a gate" appears exactly 8× (7 narrative + §2.6.1) with
no double-insertion, the allowlist is intact (no clause leaked onto the
role-agnostic bullets), the four agents are undisturbed and byte-synced (G-count
39×5), and the root `devflow/` is untouched (ADR-004). The narrative now agrees
with the table; BUG-003 is cleared.

---

## 2. Implemented phases

### Phase A — §3.0 checkpoint narrative
Appended the canonical fallback clause to the 7 named-role "Who" bullets
(`HITL-US`, `HITL-BUG` functional route, `HITL-TC`, `HITL-BOLT-READY`,
`HITL-ADR`, `HITL-SPEC`, `HITL-BOLT-DONE`). The `HITL-MEM` bullet (executor, not
an availability gate — corrected by BOLT-005) and the DISC/REV/AREV bullets
("Qualified human designated for…", role-agnostic) were left untouched.

### Phase B — §2.6.1 + TEMPLATE-TC
Appended the clause to the §2.6.1 "Independent lifecycle" TC-approval prose and
to `TEMPLATE-TC.md` §10 (the `HITL-TC-Approval` blockquote).

### Phase C — Verification (GREEN, §9)
Per-checkpoint clause presence (multiline), allowlist non-leak, clause-signature
count, four-agent sync, G-count, root check.

---

## 3. Files created

| File | Purpose |
|------|---------|
| `devflow/memory/MEM-260822-0342-role-gate-narrative-fallback-sweep.md` | This MEM — RED/GREEN record of the BUG-003 fix |

---

## 4. Files modified

| File | Change |
|------|--------|
| `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md` | Fallback clause appended to 7 §3.0 "Who" bullets + the §2.6.1 TC-lifecycle prose (8 insertions) |
| `distribution-kit/devflow/tests/test-cases/TEMPLATE-TC.md` | Fallback clause in the §10 `HITL-TC-Approval` blockquote |

> Governance records for this V-Bounce also changed in the root `devflow/`
> (BUG-003, US-000.BOLT-006 doc + manifest, SPEC, this MEM, INDEXes) — DevFlow
> tracking, not framework files; AC-5 allows them.

---

## 5. Files renamed / 6. Files deleted

None / none.

---

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| Append a concise clause to each bullet (not a single section note) | Matches the §3.0 table's proven per-row pattern; robust to a reader landing on one bullet via deep link |
| Leave DISC/REV/AREV bullets untouched | Already role-agnostic ("Qualified human designated for…") — no named-role gate; editing them would be over-correction (ADR-005 §3(3), AC-2) |
| Leave the HITL-MEM bullet untouched | The executor approves their own MEM — that is not a role-availability gate, and BOLT-005 just set it correctly |
| Fix only the functional route of the HITL-BUG bullet | The non-functional route already carries the relaxed G29 rule ("any team member, author included") |
| Include §2.6.1 + TEMPLATE-TC (F-02's original 2 locations) | They are the AREV-003 F-02 sites; folded into this Bolt's 9-site scope |

---

## 8. Deviations and assumptions

No deviations from the approved SPEC. All 9 sites carry the clause; the allowlist
was preserved. Assumption: `?? .claude/` is the harness config, unrelated to
this V-Bounce (AC-5 holds).

---

## 9. Verification evidence

Documentation defect (ADR-002 class 1) — RED/GREEN is deterministic grep.

### RED (pre-fix — coverage gap)
BUG-003 §2 positive-coverage inventory: 9 route statements stating a named-role
route with **no** fallback clause (§3.0 narrative ×7, §2.6.1, TEMPLATE-TC §10),
while the §3.0 table rows carried it (positive control).

### GREEN (post-fix)
```
AC-1 coverage: all 7 §3.0 checkpoints carry the clause (per-checkpoint multiline check):
     HITL-US / HITL-BUG / HITL-TC / HITL-BOLT-READY / HITL-ADR / HITL-SPEC / HITL-BOLT-DONE — clause present
     §2.6.1 clause present (1) ; TEMPLATE-TC clause present (1)
     clause signature "guidance, not a gate" = 8 (7 narrative + §2.6.1) — no double-insertion
AC-2 allowlist: DISC/REV/AREV bullets — grep -A2 shows NO clause leaked (clean) ;
     HITL-MEM bullet unchanged (executor rule intact)
AC-3 narrative agrees with table (both carry the fallback)
AC-4 G-count: GUARDRAILS 39 ; CLAUDE 39 ; SKILL 39 ; agent.md 39 ; opencode 39 — agents undisturbed
AC-5 root: only distribution-kit/ + governance records changed (`?? .claude/` = harness config)
AC-6 manifest: v_bounces[0] appended, validates
```

### Gates (§7 of the SPEC)
Documentation-only/internal/not an automated-test BUG → unit/integration, SAST/SBOM,
perf, IP, PII, dep-confusion, test-first: `n/a`. Prompt-injection, secret-leak,
hallucination-lint, behavioral-reproducibility, bolt-manifest-validation: `pass`.

---

## 10. Manual interventions

None — all edits agent-generated.

---

## 11. Evidence links

- **Diff / PR:** uncommitted working tree at MEM time (kit + governance records)
- **Commit:** baseline `c30a739`; this V-Bounce's commit pending user request
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-000.BOLT-006-role-gate-narrative-fallback-sweep.json`

---

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~10 min |
| V-Bounce number | 1 |
| Tests created | 0 (documentation-only; deterministic grep RED/GREEN) |
| AI-generated code | 100% |
| First-pass approval | pending |

---

## 13. Pending items and stubs

- [ ] After acceptance → all AREV-003 findings routed and fixed; re-verify and close v4.2.
- [ ] Commit + push the v4.2 close (pending explicit user request, G34).

---

## 14. HITL-MEM-Approval

> **Avenga DevFlow §2.12, §3.0.** Created by the agent, never self-approved. The
> executing Dev-validator inspects the diff, the §9 RED/GREEN evidence, this MEM
> and the manifest. Risk medium → one approver.

| Field | Value |
|-------|-------|
| **Reviewers (executing Dev-validator)** | eugenio.serrano |
| **Roles** | dev_validator (risk medium → 1 approver) |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-22T03:42:38-03:00` |
| **review.started_at** | `2026-08-22T03:45:48-03:00` |
| **review.decided_at** | `2026-08-22T03:45:48-03:00` |
| **Review evidence** | diff (2 kit files) + §9 RED/GREEN sweep + allowlist non-leak check + manifest |
| **Findings** | none — `acknowledged_without_comment: true` |
