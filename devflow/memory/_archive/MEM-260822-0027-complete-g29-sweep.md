---
id: "MEM-260822-0027"
title: "Complete the G29 relaxation sweep — remove stale non-functional BUG-route copies"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
bolt: "US-000.BOLT-004"
spec: "SPEC-260822-0018"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "c794948"
applied_adrs:
  - "devflow/adrs/ADR-002-documentation-defect-classification.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "US-000.BOLT-004-complete-g29-sweep.json"
diff_ref: "" # uncommitted working-tree change — no commit made (G34)
review_ready_at: "2026-08-22T00:27:06-03:00"
review: # HITL-MEM-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "dev_validator"}]
  started_at: "2026-08-22T00:29:16-03:00"
  decided_at: "2026-08-22T00:29:16-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Inspected the diff of the seven kit files, the RED (7 stale matches) and GREEN (0 stale, relaxed rule present at all seven) grep evidence, the four-agent G-count (39×5) and the now-identical HITL-BUG-Approval row, the git status (root methodology content untouched), and the valid manifest. The V-Bounce faithfully implements SPEC-260822-0018 and resolves BUG-001 with no deviations. Risk low → single approver (the executing dev_validator). Approved."
---

<!--
  LANGUAGE POLICY (§3.15): schema in English; prose in content_language (en).
  BUG V-Bounce (§3.3.1): RED and GREEN evidence recorded separately below.
-->

# MEM-260822-0027 — Complete the G29 relaxation sweep: remove stale non-functional BUG-route copies

| Field           | Value |
|-----------------|-------|
| **Bolt**        | [US-000.BOLT-004](../functional/bolts/US-000.BOLT-004-complete-g29-sweep.md) |
| **SPEC**        | [SPEC-260822-0018](../spec/SPEC-260822-0018-complete-g29-sweep.md) rev. 1 |
| **V-Bounce**    | 1 |
| **ADRs**        | ADR-002 (class-1 defect classification), ADR-004 (kit-only) |

---

## 1. Executive summary

This V-Bounce completed the G29 relaxation that `US-000.BOLT-002` /
`SPEC-260821-0108` began, fixing the self-contradiction documented in BUG-001
(routed from AREV-001 F-01). The kit still carried the pre-relaxation
non-functional BUG-approval route in seven places while its G29 rows and §3.0
table already stated the relaxed rule — so the four auto-loaded agent
definitions literally disagreed with themselves. Following the SPEC's strict
TDD protocol for a class-1 documentation defect (ADR-002), a stale-phrase grep
was run first as RED evidence (seven matches confirmed), the seven locations
were then edited to the approved relaxed wording ("any team member, author
included"), and a GREEN grep confirmed **zero** stale matches with the relaxed
rule present at every location. The four agents remain byte-synchronized
(whole-body G-rule count 39/39/39/39 and an identical `HITL-BUG-Approval`
row), the `critical` and functional routes are untouched, the manifest is
valid JSON, and no root `devflow/` methodology content was modified — only the
seven `distribution-kit/` files (ADR-004). All seven acceptance criteria pass.

---

## 2. Implemented phases

### Phase A — Reproduction (RED)

Ran the stale-phrase grep over `distribution-kit/` before any edit
(deterministic reproduction for a class-1 documentation defect — there is no
runtime test). Six single-line matches plus one multiline match in the §3.0
prose confirmed the defect exactly as BUG-001 / AREV-001 F-01 described. See §9.

### Phase B — Fix (kit edits, four agents synchronized)

Edited the seven locations to the relaxed routing, phrased identically to the
already-installed relaxed G29 row. The four agent HITL-table rows received the
**identical** replacement to preserve four-agent synchronization; T02 was
rewritten to keep its traceability intent (reviewer matches the severity
route) while removing the now-false "never the author" absolute; the §3.0
prose replaced the "Developer other than the BUG's own owner" clause with
"any team member, the BUG's own author included," keeping self-approval
prohibited only on the `critical` route. No other lines changed.

### Phase C — Verification (GREEN)

Re-ran the stale grep (zero matches, single-line and multiline), the
relaxed-phrase grep (present at all seven), the G-rule count (39 in each of
the four agents and GUARDRAILS), a git status check (root methodology content
untouched) and a JSON parse of the manifest. All pass. See §9.

---

## 3. Files created

| File | Purpose |
|------|---------|
| — | None — this V-Bounce only modified existing distributable text. (The BUG, Bolt, SPEC, manifest and this MEM are governance records of the V-Bounce, not its code output.) |

---

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `distribution-kit/CLAUDE.md` (L396) | `HITL-BUG-Approval` HITL-table row → relaxed non-functional route ("else any team member, author included") |
| `distribution-kit/.agents/skills/avenga-devflow/SKILL.md` (L413) | Same identical row edit (four-agent sync) |
| `distribution-kit/.github/agents/AvengaDevFlow.agent.md` (L441) | Same identical row edit (four-agent sync) |
| `distribution-kit/.opencode/agents/AvengaDevFlow.md` (L424) | Same identical row edit (four-agent sync) |
| `distribution-kit/devflow/README.md` (L248) | Checkpoint-map `HITL-BUG-Approval` row → relaxed route |
| `distribution-kit/devflow/GUARDRAILS.md` (L230, T02) | Traceability rule T02 → keeps "reviewer matches severity route", fixes routing (critical → Architect/TL never author; otherwise any team member, author included) |
| `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md` (§3.0 prose, L1411–1413) | Replaced "Developer other than the BUG's own owner (self-approval not permitted)" with "any team member, the BUG's own author included (self-approval permitted; prohibited only on the critical route)" |

---

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
| — | — | None |

---

## 6. Files deleted

| File | Reason |
|------|--------|
| — | None |

---

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| Phrase every location as "any team member, author included" | Matches the already-installed relaxed G29 row — one wording everywhere (REV-001 F-07 / AREV-001 F-01 consistency) |
| T02 keeps its structure, only the routing fact changes | Preserves the traceability rule while removing the false "never the author" absolute |
| Identical edit across the four agents | Four-agent synchronization invariant (AGENTS.md) — AC-5 |
| Kit-only edits, root untouched | ADR-004 rules 1, 2 — the root rulebook is frozen until the next §5.16 migration |
| No commit made | G34 — staging/committing needs an explicit user request; left as working-tree change |

---

## 8. Deviations and assumptions

No deviations from the SPEC. All seven SPEC-inventoried locations were found
exactly as listed and edited as prescribed. No pre-existing four-agent drift
was found before Phase B. Assumption: the relaxed wording variants
("author included" / "the author included" / "the BUG's own author included")
are equivalent in meaning and each fits its sentence naturally — acceptable
since the schema-bearing content (the routing rule) is identical.

---

## 9. Verification evidence

### BUG V-Bounce evidence

**RED** (before edit — `rg` over `distribution-kit/`, run 2026-08-22T00:23):
```
$ rg -n "Developer≠author|other than the BUG's own|never the artifact's own|other than its author" distribution-kit/
distribution-kit/CLAUDE.md:396: ... else Developer≠author (non-functional) ...
distribution-kit/.agents/skills/avenga-devflow/SKILL.md:413: ... else Developer≠author ...
distribution-kit/.github/agents/AvengaDevFlow.agent.md:441: ... else Developer≠author ...
distribution-kit/.opencode/agents/AvengaDevFlow.md:424: ... else Developer≠author ...
distribution-kit/devflow/README.md:248: ... else Developer≠author ...
distribution-kit/devflow/GUARDRAILS.md:230: ... is never the artifact's own `owner`/author ...
$ rg -nU "other than the BUG" distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md
1412: ...otherwise to a Developer other than the BUG's / own `owner` (self-approval is not permitted...)
=> 7 stale locations (6 single-line + 1 multiline). Defect reproduced.
```

**GREEN** (after edit — same greps, run 2026-08-22T00:25):
```
$ rg -n "Developer≠author|other than the BUG's own|never the artifact's own|other than its author" distribution-kit/
No matches found
$ rg -nU "other than the BUG" distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md
No matches found
$ rg -n "any team member, (author|the author|the BUG's own author) included" distribution-kit/
=> relaxed rule present at all seven edited locations (plus the pre-existing relaxed rows)
```

### Four-agent sync + G-count (AC-5)
```
CLAUDE.md: 39   SKILL.md: 39   AvengaDevFlow.agent.md: 39
AvengaDevFlow.md: 39   GUARDRAILS.md: 39
HITL-BUG-Approval row identical across the four agents (L396/413/441/424).
```

### Root untouched (AC-6)
```
$ git status --short
 M distribution-kit/CLAUDE.md
 M distribution-kit/.agents/skills/avenga-devflow/SKILL.md
 M distribution-kit/.github/agents/AvengaDevFlow.agent.md
 M distribution-kit/.opencode/agents/AvengaDevFlow.md
 M distribution-kit/devflow/GUARDRAILS.md
 M distribution-kit/devflow/README.md
 M distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md
 (plus root devflow/ GOVERNANCE records only — INDEX/US/manifests/new artifacts;
  no root devflow/ methodology-content file modified)
```

### Manifest (AC-7)
```
US-000.BOLT-004 manifest: valid JSON (built to manifest-v4-bolt.schema.json).
```

### Gates (§9 of SPEC)
prompt-injection `pass` · secret-leak `pass` · hallucination-lint `pass` ·
behavioral-reproducibility `pass` · test-first-evidence `pass` (RED→GREEN) ·
bolt-manifest-validation `pass` · unit/integration/SAST/SBOM/perf/PII/IP/
dependency-confusion `n/a` (documentation-only, no code/deps/runtime/PII).

---

## 10. Manual interventions

None — the agent produced every edit. No human code patch.

---

## 11. Evidence links

- **Diff / PR:** none — uncommitted working-tree change (G34: no commit without explicit request).
- **Commit:** baseline `c794948`; the V-Bounce output is uncommitted.
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-000.BOLT-004-complete-g29-sweep.json`.

---

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~4 min (single V-Bounce) |
| V-Bounce number | 1 |
| Tests created | n/a — deterministic grep/diff (RED + GREEN captured) |
| AI-generated code | 100% (no human fallback) |
| First-pass approval | pending HITL-MEM-Approval |

---

## 13. Pending items and stubs

- [ ] `HITL-MEM-Approval` (this package).
- [ ] `HITL-BOLT-DONE-Approval` (acceptance — `work_category: debt` → Tech Lead).
- [ ] Commit the working-tree change (only on explicit user request — G34).
- [ ] The root `devflow/` receives this fix at the next §5.16 release migration (ADR-004).

---

## 14. HITL-MEM-Approval

> **Avenga DevFlow §2.12, §3.0.** This MEM is created by the agent with no
> mutable status and is **never self-approved**. The executing Dev-validator
> inspects the diff, the RED/GREEN evidence, the gates, this MEM and the
> manifest, and records `HITL-MEM-Approval` here and in the manifest's
> `hitl_approvals[]`. Risk class `low` → 1 approver (the executing
> Dev-validator).

| Field | Value |
|-------|-------|
| **Reviewers** | eugenio.serrano (dev_validator) |
| **Decision** | approved |
| **review_ready_at** | `2026-08-22T00:27:06-03:00` |
| **review.started_at** | `2026-08-22T00:29:16-03:00` |
| **review.decided_at** | `2026-08-22T00:29:16-03:00` |
| **Review evidence** | diff of the 7 kit files, RED/GREEN grep, G-count 39×5, git status, manifest JSON |
