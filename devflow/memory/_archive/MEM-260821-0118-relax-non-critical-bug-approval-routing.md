---
id: "MEM-260821-0118"
title: "G29 relaxed: non-critical non-functional BUGs approvable by any team member, author included"
date: "2026-08-21"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
bolt: "US-000.BOLT-002"
spec: "SPEC-260821-0108"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "0a47e3f"
applied_adrs:
  - "devflow/adrs/ADR-001-repository-layout-methodology-and-product.md"
manifest: "US-000.BOLT-002-relax-non-critical-bug-approval-routing.json"
diff_ref: ""
review_ready_at: "2026-08-21T01:18:03-03:00"
review: # HITL-MEM-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers:
    - user: "eugenio.serrano"
      role: "dev_validator"
  started_at: "2026-08-21T01:20:42-03:00"
  decided_at: "2026-08-21T01:20:42-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Inspected the double-checked package: the diff of the 14 kit files (GUARDRAILS G29 + checkpoint map, 7 methodology locations, 4 agent definitions ×2 edits, 6 artifact locations), the §9 verification output (0 stale matches, sync diff 2/2/2, G-count 39/39/39/39, markers untouched, root devflow intact), the MEM narrative and the manifest v_bounces[1] entry. The relaxed routing reads consistently everywhere; the critical and functional routes are unchanged. No findings."
---

# MEM-260821-0118 — G29 relaxed: non-critical non-functional BUGs approvable by any team member, author included

| Field           | Value |
|-----------------|-------|
| **Bolt**        | [US-000.BOLT-002](../functional/bolts/US-000.BOLT-002-relax-non-critical-bug-approval-routing.md) |
| **SPEC**        | [SPEC-260821-0108](../spec/SPEC-260821-0108-relax-non-critical-bug-approval-routing.md), **revision 1** |
| **V-Bounce**    | 1 |
| **ADRs**        | [ADR-001](../adrs/ADR-001-repository-layout-methodology-and-product.md) — rules 1, 2, 5, 7 (kit-only edits, root frozen) |

---

## 1. Executive summary

This V-Bounce implemented the policy decision recorded in REV-001 finding
F-02: the `HITL-BUG-Approval` routing for **non-functional BUGs with
`severity: high|medium|low`** no longer requires "a Developer other than the
BUG's own author" — **any team member, the author included**, may now record
the approval, so a single-maintainer team is no longer structurally blocked
on non-critical non-functional defects. The `critical` route (Architect or
Tech Lead) and the functional route (Functional Analyst) were kept
byte-for-byte unchanged, and the dedicated Bolt's readiness approval mirrors
the relaxed route so the fix is not re-blocked at the Bolt level. The change
landed in every distributable location that defines the routing — the
GUARDRAILS G29 row and checkpoint map, seven places in the methodology,
the four agent definitions (G29 row + Bug-Fix-Protocol bullet each), and six
templates/READMEs — with the root `devflow/` untouched per ADR-001. All seven
acceptance criteria pass: zero stale "other than the author" matches remain
in the distributable, the critical/functional routes are intact, the
four-agent shared-body sync diff shows exactly the 2 sanctioned lines of
divergence (the `agents-data` path), the G-rule count stays 39/39/39/39, and
the Bolt manifest validates with 0 errors. No deviations from SPEC revision
1; no surprises; the only cosmetic note is that one of the methodology
phrases wraps across a line break and therefore appears as two grep hits
rather than one, which the pattern-based verification accounted for.

---

## 2. Implemented phases

### Phase A — Guardrail layer (GUARDRAILS.md)

Rewrote the G29 row so the *violation* is now routing a `critical`
non-functional BUG (or its dedicated Bolt) to a Developer, or blocking a
non-critical one for lack of an approver — the response text states the
relaxed rule with the author included and keeps the severity rule
("severity never downgrades the `critical` route"). Rewrote the
checkpoint-map row for `HITL-BUG-Approval` with the same three-branch
routing (FA / Architect-TL / any team member). The row count stays 39 — one
G entry, edited in place.

### Phase B — Methodology (Avenga-DevFlow.md)

Updated the seven locations that state the routing so each one restates the
same sentence: §0 E2E summary, §1 flow bullet, §2.4 Bolt-routing footnote
(dedicated-Bolt mirror), §2.16 BUG-nature table, §3.0 HITL checkpoint table,
§3.3.1 BUG-correction "Who" line (self-approval now prohibited only on the
`critical` route), and the §5.15 folder-map `bugs/` description.

### Phase C — Four agent definitions (one synchronized pass)

Applied the identical new G29 inline row ("any team member, author included.
Self-approval never permitted on the `critical` route") and the identical
Bug-Fix-Protocol bullet ("else any team member, author included") to
`CLAUDE.md`, `SKILL.md`, `AvengaDevFlow.agent.md` and `AvengaDevFlow.md`.
Post-edit verification: shared-body diff exactly 2 lines per comparison
(only the `devflow/agents-data/<agent>/` path line), G-rule counts
39/39/39/39.

### Phase D — Onboarding, BUG and functional artifacts

Aligned the six remaining locations: ONBOARDING role row (Architect/TL now
notes lower severities may be approved by any team member), bugs/README
lifecycle row and severity-routing paragraph (rewritten to the relaxed rule
with "the person who drafted it included"), TEMPLATE-BUG routing note in the
classification table and the HITL-BUG-Approval section, functional/README
and TEMPLATE-BOLT mirror footnotes, and US-000-non-functional rule 5.

### Phase E — Verification suite

Executed the deterministic checks: stale-phrase grep (0 matches), new-phrase
grep (22 "author included" matches across 12 files plus 1 multiline wrap),
critical-route grep (28 matches, wording intact), the four-agent whole-body
sync diff (2 lines each), the G-rule count (39/39/39/39 + GUARDRAILS 39),
`git status` (no root `devflow/` methodology content modified) and the Bolt
manifest JSON validation (0 errors). All output recorded in §9.

---

## 3. Files created

| File | Purpose |
|------|---------|
| `devflow/memory/MEM-260821-0118-relax-non-critical-bug-approval-routing.md` | This implementation memory — the V-Bounce 1 record of Bolt US-000.BOLT-002 |

*(Governance records created earlier in the Bolt lifecycle: the Bolt
document, its manifest, the SPEC and the REV-001 inventory — listed in the
Bolt's own manifest; the V-Bounce itself modified product files only.)*

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `distribution-kit/devflow/GUARDRAILS.md` | G29 row (line 58) and checkpoint-map row (line 25) rewritten to the relaxed routing; critical route and rule count (39) unchanged |
| `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md` | Seven locations restated: §0 (23), §1 (130–131), §2.4 footnote (445), §2.16 table (1282), §3.0 checkpoint table (1374), §3.3.1 Who line (2612–2613), §5.15 folder map (4323) |
| `distribution-kit/CLAUDE.md` | G29 inline row (245) + Bug-Fix-Protocol bullet (526) — new routing |
| `distribution-kit/.agents/skills/avenga-devflow/SKILL.md` | Same two edits, verbatim (262, 543) |
| `distribution-kit/.github/agents/AvengaDevFlow.agent.md` | Same two edits, verbatim (290, 571) |
| `distribution-kit/.opencode/agents/AvengaDevFlow.md` | Same two edits, verbatim (273, 554) |
| `distribution-kit/devflow/ONBOARDING.md` | Architect/TL reading-order row (28) — lower severities approvable by any team member |
| `distribution-kit/devflow/bugs/README.md` | Lifecycle `approved` row (68) + severity-gated routing paragraph (172–180) |
| `distribution-kit/devflow/bugs/TEMPLATE-BUG.md` | Classification "Nature" row (99) + HITL-BUG-Approval note (136–141) |
| `distribution-kit/devflow/functional/README.md` | Dedicated-Bolt mirror footnote (42–44) |
| `distribution-kit/devflow/functional/bolts/TEMPLATE-BOLT.md` | Same mirror footnote (174–176) |
| `distribution-kit/devflow/functional/user-stories/US-000-non-functional.md` | Rule 5 (67–71) — BUG routing sentence aligned |

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
| — | — | None |

## 6. Files deleted

| File | Reason |
|------|--------|
| — | None |

---

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| Keep the G29 entry count at 39 by editing the row in place | The four-agent inline invariant and the guardrail table count are load-bearing; a removal would force a coordinated count change across five files with no benefit |
| Apply the exact same sentence to all locations instead of paraphrasing per file | Preserves the REV-001 F-07 consistency invariant and makes the verification greps exact |
| Restrict the self-approval prohibition to the `critical` route only | Mirrors the user's Option A decision: non-critical non-functional BUGs may be approved by the author; the security-bearing route stays strict |
| Mirror the relaxed route on the dedicated Bolt's readiness approval | Without it the BUG would be approvable but its Bolt would still require another Developer — the single-maintainer dead-end would merely move one step later |
| Leave the root `devflow/` untouched and edit only `distribution-kit/` | ADR-001 rules 1/2/5/7: the installed rulebook is frozen; adopters receive the change through the next §5.16 release migration |
| Accept a multiline wrap in one methodology sentence (line 130–131) | The original text wrapped the same way; splitting the phrase differently would have created gratuitous diff noise — verification uses pattern groups that span the wrap |

---

## 8. Deviations and assumptions

**No deviations from SPEC revision 1.** Every phase landed as specified and
all seven ACs pass.

**Assumption:** the phrase "any team member" means any human member of the
adopting project's team (per the project's own roster of contributors if one
exists, otherwise the repository's contributors) — no role filter applies at
non-critical severities. The `critical` route is unchanged, so
security-bearing non-functional defects still require an Architect or Tech
Lead.

**Known residual:** the review-independence weakening for non-critical
non-functional BUGs is an accepted policy trade-off (REV-001 F-02); the
approval still records approver name, role, timestamps and evidence.

**No unresolved risks** carried out of this V-Bounce. REV-001 findings
F-03..F-06 remain open and routed (noted in the Bolt's exclusions).

---

## 9. Verification evidence

### Build

```
n/a — no runtime and no build. Verification is the deterministic command set below.
```

### Tests

```
AC-1/AC-4  "author included" phrasing present ......... 22 matches across 12 files
           (plus 1 methodology phrase wrapped across a line break — verified
            by the "own author" context grep: lines 23, 130, 445, 1282, 1374,
            2613, 4323 all present)
AC-2       stale "other than the (BUG|Bolt)'s own" /
           "other than its author" / "a Developer who is **not**" ... 0 matches  PASS
AC-3       "severity: critical" / "severity=critical" ... 28 matches, wording intact
           functional route ("Functional Analyst") present in all defining rows      PASS
AC-5       shared-body sync diff:
           codex vs claude: 2 lines | ghcopilot vs claude: 2 | opencode vs claude: 2
           (the 2 lines are the sanctioned devflow/agents-data/<agent>/ path)
           G-rule count: GUARDRAILS 39 | claude 39/39 | codex 39/39 |
           ghcopilot 39/39 | opencode 39/39                                           PASS
AC-6       git status: no root devflow/ methodology content modified —
           only governance records (INDEX/REV-001/SPEC/BOLT-002/manifest)
           and distribution-kit/ product files                                     PASS
AC-7       Bolt manifest valid (ConvertFrom-Json), spec_revisions=1,
           v_bounces=1 (after this entry), approvals=2                              PASS
```

### BUG V-Bounce evidence

`n/a` — not a BUG Bolt; no red→green protocol.

### Gates

| Gate | Result |
|------|--------|
| Unit / integration | `n/a` — documentation-only change, no executable code |
| SAST / SBOM | `n/a` — no code, no dependencies |
| Perf-smoke | `n/a` — no runtime |
| Prompt-injection scan | `pass` — all text authored here |
| Secret-leak scan | `pass` |
| Hallucination lint | `pass` — §2.16, §3.0, §2.4, §3.3.1, §5.15, ADR-001, REV-001, Bolt all resolve on disk |
| IP / license provenance | `n/a` — no third-party content |
| PII / DLP | `n/a` — `internal`, no personal data |
| Dependency-confusion | `n/a` — no dependencies |
| Test-first evidence | `n/a` — not a BUG Bolt |
| Behavioral reproducibility | `pass` — deterministic grep/diff/count checks, idempotent |
| Bolt-manifest validation | `pass` — 0 errors against `manifest-v4-bolt.schema.json` |

---

## 10. Manual interventions

None — the agent produced everything.

---

## 11. Evidence links

- **Diff / PR:** none — nothing staged or committed (G34)
- **Commit:** baseline `0a47e3f` on branch `4.2`, plus the uncommitted working tree
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-000.BOLT-002-relax-non-critical-bug-approval-routing.json`

---

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~12 min (01:15 → 01:18 local), including the SPEC-approval recording |
| V-Bounce number | 1 |
| Tests created | n/a — 7 acceptance criteria, ~8 deterministic checks + the 4-agent sync diff |
| AI-generated code | 100% — no human fallback |
| First-pass approval | pending — package submitted for HITL-MEM-Approval |

---

## 13. Pending items and stubs

- [ ] `HITL-BOLT-DONE-Approval` — after MEM approval (routes to Tech Lead + Sec; Sec unavailable in this single-maintainer repo, recorded with TL as in BOLT-001)
- [ ] REV-001 findings F-03..F-06 remain open (acceptance routing pairs, multi-approver counts, role multiplicity, SPEC/UAT counts) — for future decisions
- [ ] The root `devflow/` installed rulebook still carries the old G29 text — it updates only through the next §5.16 release migration (ADR-001 rule 1)
- [ ] The uncommitted governance records of this session (REV-001, SPEC, BOLT-002 package) — pending the user's commit instruction

---

## 14. HITL-MEM-Approval

> **Avenga DevFlow §2.12, §3.0.** This MEM is created by the agent with no
> mutable status and is **never self-approved**. A qualified human (the
> Dev-validator who executed the Bolt, + QA/Sec for high/critical risk)
> inspects the actual diff, test/gate evidence, MEM and manifest, and
> records `HITL-MEM-Approval` here and in the manifest's
> `hitl_approvals[]`. `approved` completes the V-Bounce (and, if latest,
> marks the Bolt `Development Completed`); `changes_requested` keeps this
> MEM as immutable history and the next execution is a NEW V-Bounce with a
> NEW MEM. `HITL-BOLT-DONE-Approval` is still required for `Done`.

| Field | Value |
|-------|-------|
| **Reviewers (executing Dev-validator + QA/Sec for high/critical)** | eugenio.serrano |
| **Roles** | dev_validator (risk_class medium → 1 approver) |
| **Decision** | approved |
| **review_ready_at** | `2026-08-21T01:18:03-03:00` |
| **review.started_at** | `2026-08-21T01:20:42-03:00` |
| **review.decided_at** | `2026-08-21T01:20:42-03:00` |
| **Review evidence** | Diff of the 14 kit files (12 modified + 4 agents), the §9 verification output (grep counts, sync diff, G-count, git status), the manifest `v_bounces[]` entry, and the SPEC/REV-001 references |
| **Comments** | None — double-checked package approved as submitted |
| **Findings** | none |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | recorded in the frontmatter `review:` block |
