---
id: "MEM-260823-0004"
title: "V-Bounce 1 — BUG approval is never-blocking (descriptions kept, blocks removed, author may approve any BUG)"
date: "2026-08-23"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
bolt: "US-000.BOLT-010"
spec: "SPEC-260822-2350"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "247b4f1"
applied_adrs:
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
  - "devflow/adrs/ADR-005-removal-completeness-phrase-family-sweep.md"
manifest: "US-000.BOLT-010-severity-agnostic-bug-approval.json"
diff_ref: ""
review_ready_at: "2026-08-23T00:04:49-03:00"
review: # HITL-MEM-Approval — recorded by the human reviewer (§3.0)
  decision: "approved"
  reviewers:
    - user: "eugenio.serrano"
      role: "dev_validator"
  started_at: "2026-08-23T00:10:45-03:00"
  decided_at: "2026-08-23T00:10:45-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Reviewed the V-Bounce 1 package: the 13-file kit diff (independently cross-reviewed), the §9 deterministic sweep (absence sweep = 0 blocking clauses incl. multiline; 'guidance, never a gate' present across 13 files; recommended-approver descriptions kept; G-count 39×5; four-agent parity; AI self-approval rule G18/G24 untouched; kit-only), the MEM narrative and the validating manifest (0 errors). The change matches the approved SPEC-260822-2350 rev 1: BUG approval is never-blocking, descriptions kept, any qualified team member — the author included — may approve any BUG at any severity. The kit's remaining 12 `HITL-` mentions were verified deliberate (G05 bans the legacy prefix; §5.16 describes migration) — not a residual, out of scope for this Bolt. V-Bounce approved; Bolt → Development Completed."
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs and headings (##) in
  English; prose content_language (en).

  DOGFOODING SPLIT: this V-Bounce ran under v4.2 (root devflow/, ADR-006) — its
  checkpoint is HITL-MEM-Approval, its manifest schema_version 4.0. It edited the
  v5.0 PRODUCT (distribution-kit/, AITL-*). Kit-only (ADR-004).

  Not a BUG V-Bounce (no strict red/green): a deliberate policy change, verified
  by a deterministic before/after phrase-family sweep (ADR-005), not a runtime test.
-->

# MEM-260823-0004 — BUG approval is never-blocking

| Field        | Value |
|--------------|-------|
| **Bolt**     | [US-000.BOLT-010](../functional/bolts/US-000.BOLT-010-severity-agnostic-bug-approval.md) |
| **SPEC**     | [SPEC-260822-2350](../spec/SPEC-260822-2350-bug-approval-never-blocking.md) rev 1 |
| **V-Bounce** | 1 |
| **ADRs**     | ADR-004 (kit-only), ADR-005 (positive-coverage sweep) |

---

## 1. Executive summary

This V-Bounce made **BUG approval never-blocking** across the v5.0 kit
(`distribution-kit/`) while **preserving every recommended-approver
description**. The methodology still *describes* who should approve each BUG by
nature and severity (functional → Functional Analyst; non-functional `critical`
→ Architect / Tech Lead; non-functional `high|medium|low` → any team member),
but that description is now stated everywhere as **guidance, never a gate**: any
qualified team member — **the BUG's own author included** — may record
`AITL-BUG-Approval` at **any severity**, including `critical`. The last hard
block was removed: the "self-approval is never permitted on the `critical`
route" prohibition, the §2.16 "Self-approval safeguard" paragraph, and T02's
"never the BUG's own author" restriction are gone. This reverses the *blocking*
aspect of the SPEC-260821-0108 §14 decision (not its routing description) and
closes REV-001 F-02 completely for a single-maintainer team. Verification is
GREEN: the deterministic absence sweep returns **zero** blocking clauses
(multiline-aware), "guidance, never a gate" is present across 13 files, the
recommended-approver descriptions remain, the G-rule count holds at **39×5**,
the four agents stayed in parity, the **AI** self-approval prohibition
(G18/G24/ADR-008) is untouched, and only `distribution-kit/` + root governance
records changed (kit-only, ADR-004).

---

## 2. Implemented phases

### Phase A — GUARDRAILS.md
Repurposed **G29** so the *violation* is now **blocking** a BUG's approval (for
lack of the recommended-role approver, on account of severity, or by excluding
the author) — not the routing itself; the recommended approver is stated as
advice, and the 39-rule count is preserved (repurpose, not delete). Rewrote
**T02** to drop the "never the BUG's own author" restriction (the severity
approver is a recommendation). Updated the `AITL-BUG-Approval` checkpoint-map
row to carry "guidance, never a gate; author included at any severity" while
keeping the description.

### Phase B — Avenga-DevFlow.md (methodology)
Updated §1 principles, the §2.16 routing bullets (deleting the "Self-approval
safeguard" paragraph and replacing it with a "guidance, never a gate; author
included" note), the §2.16 nature/Bolt-table mirror, the §3.0 checkpoint-table
row, the §3.0 post-table narrative, and the §3.0 "Who:" bullet — each keeps the
recommended-approver description and removes the self-approval-on-critical block.

### Phase C — the four agent definitions (synchronized)
Applied byte-identical edits to the **G29 inline row** and the
`AITL-BUG-Approval` **checkpoint-table row** in `CLAUDE.md`, `SKILL.md`,
`AvengaDevFlow.agent.md`, `.opencode/AvengaDevFlow.md`. Parity preserved
(identical text, G-count 39×5).

### Phase D — other kit artifacts
`devflow/README.md` checkpoint row; `bugs/README.md` (state-table row + item 9);
`bugs/TEMPLATE-BUG.md` §8; `US-000-non-functional.md` item 5; the dedicated-Bolt
mirror footnotes in `functional/README.md` and `functional/bolts/TEMPLATE-BOLT.md`;
and `reviews/README.md` ("decides who may approve" → "recommends who should
approve"). Descriptions kept; blocks removed; author-inclusive framing added.

### Phase E — verification
Ran the deterministic suite (§9): absence sweep, presence/positive-coverage,
G-count, parity, root-untouched, AI-rule-untouched.

---

## 3. Files created

| File | Purpose |
|------|---------|
| — | none — all changes are modifications to existing kit files |

---

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `distribution-kit/devflow/GUARDRAILS.md` | G29 repurposed (guards *blocking*, count 39), T02 author-exclusion removed, checkpoint-map row de-gated + author-inclusive |
| `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md` | §1, §2.16 (safeguard paragraph deleted), §2.16 mirror, §3.0 table row, §3.0 narrative, §3.0 "Who:" bullet — descriptions kept, blocks removed, author-inclusive |
| `distribution-kit/CLAUDE.md` | G29 row + `AITL-BUG-Approval` checkpoint row de-gated (identical to the other agents) |
| `distribution-kit/.agents/skills/avenga-devflow/SKILL.md` | same two-row edit (parity) |
| `distribution-kit/.github/agents/AvengaDevFlow.agent.md` | same two-row edit (parity) |
| `distribution-kit/.opencode/agents/AvengaDevFlow.md` | same two-row edit (parity) |
| `distribution-kit/devflow/README.md` | `AITL-BUG-Approval` checkpoint row de-gated + author-inclusive |
| `distribution-kit/devflow/bugs/README.md` | `approved` state row + item 9 (severity now a recommendation, never a gate; author at any severity) |
| `distribution-kit/devflow/bugs/TEMPLATE-BUG.md` | §8 approval callout — blocking clause removed, author-inclusive |
| `distribution-kit/devflow/functional/user-stories/US-000-non-functional.md` | item 5 — self-approval block removed, author at any severity |
| `distribution-kit/devflow/functional/README.md` | dedicated-Bolt mirror footnote de-gated |
| `distribution-kit/devflow/functional/bolts/TEMPLATE-BOLT.md` | dedicated-Bolt mirror footnote de-gated |
| `distribution-kit/devflow/reviews/README.md` | severity now *recommends* (not *decides*) who approves |

---

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
| — | — | none |

---

## 6. Files deleted

| File | Reason |
|------|--------|
| — | none (the §2.16 "Self-approval safeguard" *paragraph* was removed in place, not a file) |

---

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| Keep the recommended-approver descriptions, remove only the blocking | The maintainer's explicit corrected intent (BOLT-010 re-affirmation) — the routing is useful guidance, not a gate |
| Repurpose G29 rather than delete it | Preserves a meaningful blocking rule (now: *blocking* approval is the violation) and the 39-count invariant (AC-5) |
| Leave the AI self-approval prohibition (G18/G24) untouched | Different axis — a *human* author approving their own BUG vs an *AI* approving its own work; ADR-008 stands (AC-7) |
| Procedural Bug-Fix-Protocol bullets in the agents left as-is | They describe the *recommendation* flow and carry no blocking clause; the authoritative never-a-gate rule now lives unambiguously in G29 + the checkpoint rows |
| Kit-only edits | ADR-004 — the root v4.2 tree inherits at the next §5.16 migration |

---

## 8. Deviations and assumptions

No deviations from the approved SPEC. The four agents' Bug-Fix-Protocol bullets
were intentionally not edited (SPEC C.3 — no blocking clause present); the
severity-based recommendation they describe remains consistent with the new
never-a-gate rule stated authoritatively elsewhere. Assumption: the four agents'
shared bodies were in parity before this V-Bounce (confirmed post-edit: identical
G29 + checkpoint rows, G-count 39×5).

---

## 9. Verification evidence

Deterministic before/after sweep (ADR-005; not a runtime test — documentation
change). All under `distribution-kit/`.

### Absence sweep (AC-2 — blocks removed) — expected 0
```
rg -U "self-approval is (never|not) permitted on the"        → No matches
rg    "never the BUG's own author|Self-approval safeguard|severity never downgrades" → No matches
rg -U "self-approval is\s+(never|not)\s+permitted\s+on\s+the\s+.?critical"           → No matches
```

### Presence / positive-coverage (AC-1/AC-3/AC-4) — expected > 0
```
rg -c "guidance, never a gate"   → 27 occurrences across 13 files (every BUG-route site + operability paragraphs)
```
Recommended-approver descriptions (Functional Analyst / Architect or Tech Lead
when `critical` / any team member) verified still present at each edited site;
"author included … at any severity" carries with no critical exclusion.

### G-count (AC-5) — expected 39 each
```
GUARDRAILS.md : 39
CLAUDE.md : 39
SKILL.md : 39
AvengaDevFlow.agent.md : 39
.opencode/AvengaDevFlow.md : 39
```

### Four-agent parity (AC-6)
The edited G29 row and `AITL-BUG-Approval` checkpoint row are byte-identical
across the four agents (grep-confirmed: 1 identical occurrence each); no new
divergence introduced (edits applied identically), sanctioned-divergence regions
untouched.

### AI self-approval untouched (AC-7)
All remaining `self-approval` occurrences in `distribution-kit/` are the AI/actor
axis (G18/G24: "no AI self-approval", "AI self-approval prohibition", the
`human:`-prefix identity comparison) — the BUG-route human self-approval block is
fully gone.

### Kit-only (AC-8)
`git status --short` shows only `distribution-kit/` files + root governance
records (this Bolt's BOLT-010/SPEC/manifest + the earlier REV-003 bookkeeping).
No root `devflow/` methodology framework file changed.

### Gates
prompt-injection `pass` · secret-leak `pass` · hallucination-lint `pass` (§4
inventory resolved on disk) · behavioral-reproducibility `pass` (deterministic
grep/diff) · bolt-manifest-validation `pass` (see §11) · unit/SAST/perf/etc. `n/a`
(documentation-only, no runtime).

---

## 10. Manual interventions

None — the agent produced all edits. (Reviewer approvals recorded by the human
maintainer are governance, not code patches.)

---

## 11. Evidence links

- **Diff / PR:** none yet (uncommitted working tree; no commit requested — G34)
- **Commit / baseline:** `247b4f1` (HEAD; this V-Bounce's changes uncommitted)
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-000.BOLT-010-severity-agnostic-bug-approval.json`

---

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~single V-Bounce session |
| V-Bounce number | 1 |
| Tests created | n/a (documentation change; deterministic sweep is the verification) |
| AI-generated code | 100% (no human fallback) |
| First-pass approval | pending HITL-MEM-Approval |

---

## 13. Pending items and stubs

- [ ] The root `devflow/` (v4.2 operating tree) inherits this change at the next §5.16 migration (ADR-006) — not part of this V-Bounce.
- [ ] `HITL-BOLT-DONE-Approval` still required for the Bolt to be `Done`.

---

## 14. HITL-MEM-Approval

> **Avenga DevFlow §2.12, §3.0.** This MEM has no mutable status and is **never
> self-approved**. The executing Dev-validator inspects the actual diff,
> verification evidence, this MEM and the manifest, and records
> `HITL-MEM-Approval` here and in the manifest `hitl_approvals[]`.

| Field | Value |
|-------|-------|
| **Reviewers (executing Dev-validator; QA/Sec/domain optional)** | eugenio.serrano |
| **Roles** | dev_validator |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-23T00:04:49-03:00` |
| **review.started_at** | `2026-08-23T00:10:45-03:00` |
| **review.decided_at** | `2026-08-23T00:10:45-03:00` |
| **Review evidence** | 13-file kit diff (independently cross-reviewed) + §9 deterministic sweep (absence=0, G-count 39×5, parity, kit-only, AI-rule untouched) + MEM + validating manifest |
| **Findings** | none — `acknowledged_without_comment: true` |
