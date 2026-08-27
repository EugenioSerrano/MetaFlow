---
id: "SPEC-260821-0320"
title: "Retire root prompts/ — remove analysis.txt and sync AGENTS.md references"
date: "2026-08-21"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved" # draft | approved | blocked | obsolete
origin: "ADR-003" # US-NNN, TC-NNN, BUG-NNN, DISC-NNN, REV-NNN, AREV-NNN, or ADR-NNN that motivated this SPEC
bolt: "US-000.BOLT-003" # ⚠️ MANDATORY — US-NNN.BOLT-NNN | US-000.BOLT-NNN | TC-NNN.BOLT-NNN
revision: 1 # material revision of this canonical SPEC (matches manifest spec_revisions[])
associated_adrs: ["devflow/adrs/ADR-003-prompts-family-canonical-home.md"]
prerequisites: []
risk_class: "low" # mirrors the Bolt's risk_class
autonomy_level: "L3" # low/medium → L3 default
turn_budget: ""
data_classification: "internal"
review_ready_at: "2026-08-21T03:20:51-03:00"
review: # HITL-SPEC-Approval — filled by the human reviewer (§3.0)
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - user: "eugenio.serrano"
      role: "dev_validator"
  started_at: "2026-08-21T03:22:06-03:00"
  decided_at: "2026-08-21T03:22:06-03:00"
  findings: []
  acknowledged_without_comment: true # must be true when findings is empty (§3.0)
  acknowledgment_reason: "Reviewed revision 1 against ADR-003 (retired zone + Bolt requirement) and the approved Bolt: the four AGENTS.md references are enumerated with their exact lines, the framework-block protection is explicit (AC-3), the content-continuity guarantee via PROMPT-001 is checkable, and the gates are correctly classified. Approved as drafted."
---

# SPEC-260821-0320 — Retire root prompts/: remove analysis.txt and sync AGENTS.md references

| Field | Value |
|-------|-------|
| **Origin** | ADR-003 (accepted — retired zone row) |
| **Bolt** | [US-000.BOLT-003](../functional/bolts/US-000.BOLT-003-retire-root-prompts.md) |
| **ADRs** | [ADR-003](../adrs/ADR-003-prompts-family-canonical-home.md) — retired zone + Bolt requirement |
| **Risk Class** | low |
| **Revision** | 1 |

---

## 1. Objective

Execute the retirement of the root `prompts/` zone authorized by ADR-003:
delete its only remaining file, `prompts/analysis.txt` (whose content
already lives in the family as `PROMPT-001-methodology-analysis.md`), and
update the root `AGENTS.md` project section so the repository's operational
memory no longer names root `prompts/` as editable product content.

If NOT implemented, the retired zone keeps a leftover file and the AGENTS.md
contradicts the approved zone table (ADR-003) — exactly the drift the
migration just eliminated.

---

## 2. Context

ADR-003 (accepted 2026-08-21) superseded ADR-001's rule 7: root `prompts/`
retired from the Product zone, with the explicit rule that *"its remaining
file is removed by Bolt and the folder is not recreated"*. The content is
preserved in the canonical family (`PROMPT-001-methodology-analysis.md`,
installed by the §5.16 migration and registered in the family INDEX). The
root `AGENTS.md` project section still lists `prompts/` in four places —
lines 68, 93, 110 and 172 — which must be synced to the amended zone table.

---

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| ADR | `devflow/adrs/ADR-003-prompts-family-canonical-home.md` | HITL-ADR-Approval ✓ (2026-08-21T03:17:55-03:00) |
| Feature US | `devflow/functional/user-stories/US-003-prompts-family.md` | HITL-US-Approval ✓ |
| Bolt | `devflow/functional/bolts/US-000.BOLT-003-retire-root-prompts.md` | HITL-BOLT-READY-Approval ✓ (2026-08-21T03:20:51-03:00) |
| Repository baseline | `e1b81c6` on branch `4.2` (working tree: ADR-003 + archive + PROMPT-001 + INDEX fixes, uncommitted) | — |

Pre-SPEC evidence gate: **all sources approved** — no draft governed input.

---

## 4. Scope

### In scope

- Delete `prompts/analysis.txt` (tracked file).
- Root `AGENTS.md` project section — the four `prompts/` references:
  - line 68: "`distribution-kit/` — together with `tools/` and `prompts/`,
    that is the only thing you edit…" → drop `prompts/` from the product
    list;
  - line 93: "`prompts/`." (in the two-tree contrast sentence) → reword to
    reflect the prompts family as the canonical home;
  - line 110: "`distribution-kit/`, `tools/` or `prompts/` is a product
    change…" → drop `prompts/`;
  - line 172: "**Neither this file, `tools/` nor `prompts/` is
    distributed.**" → drop `prompts/` (or reword to point at the family).
- The empty `prompts/` folder needs no action (git does not track empty
  directories).

### Out of scope

- The `devflow/prompts/` family and `PROMPT-001` (untouched).
- `distribution-kit/` — no adopter-facing change (the kit never shipped the
  root `prompts/`).
- ADR-003's zone table (already approved, immutable).

---

## 5. Prerequisites and baseline

- ADR-003 accepted; Bolt `US-000.BOLT-003` approved (HITL-BOLT-READY-
  Approval recorded).
- Baseline `e1b81c6`; the working tree holds the uncommitted ADR-003 /
  archive / PROMPT-001 / INDEX-fix package.
- `PROMPT-001-methodology-analysis.md` exists in `devflow/prompts/` (the
  content continuity guarantee).

---

## 6. Phases

### Phase A — Remove the leftover file

**Duration:** ~0.2h total cycle — **Complexity:** Low

Delete `prompts/analysis.txt` from the working tree (tracked deletion —
`git rm`).

### Phase B — Sync the AGENTS.md project section

**Duration:** ~0.3h total cycle — **Complexity:** Low

Edit the four `prompts/` references in the root `AGENTS.md` project section
(lines 68, 93, 110, 172):

- Product list lines: remove `prompts/` from the editable-product
  enumeration (68, 110) and from the "not distributed" sentence (172),
  adding a short pointer that prompts live in the canonical
  `devflow/prompts/` family (living data).
- The two-tree contrast sentence (93): reword so root `prompts/` no longer
  appears as a product tree; the family is the prompts home.

The framework block above the marker is **not touched** — only the project
section (this Bolt's repository-surface scope).

### Phase C — Verification

**Duration:** ~0.2h total cycle — **Complexity:** Low

Run the deterministic checks (§8) and capture the output in the MEM.

---

## 7. Acceptance criteria

### AC-1: Leftover file gone

**Given** the completed V-Bounce,
**When** checking `prompts/analysis.txt`,
**Then** it does not exist in the working tree and git shows a tracked
deletion.

### AC-2: Content preserved

**Given** the completed V-Bounce,
**When** checking the family,
**Then** `devflow/prompts/PROMPT-001-methodology-analysis.md` exists with
the prompt body intact.

### AC-3: AGENTS.md synced

**Given** the root AGENTS.md,
**When** grepping its project section for `prompts/`,
**Then** no line lists root `prompts/` as editable product content; the
four references (68, 93, 110, 172) are updated; the framework block above
the marker is unchanged (diff shows only project-section lines).

### AC-4: No dangling references

**Given** the repository,
**When** grepping for `prompts/analysis.txt` and the retired-folder
phrasing,
**Then** zero matches outside the governance records that document the
retirement (ADR-003, this SPEC, the Bolt) and the historical CHANGELOG.

### AC-5: Manifest validation

**Given** the Bolt manifest,
**When** validating,
**Then** 0 errors against `manifest-v4-bolt.schema.json`.

### AC mapping to source (non-functional)

| Source outcome (Bolt §2 / ADR-003) | How this SPEC satisfies it | Verifying test/evidence |
|-------------------------------------|----------------------------|--------------------------|
| `analysis.txt` removed by Bolt | Phase A | AC-1 |
| AGENTS.md operational memory matches the amended zone table | Phase B | AC-3 |
| Content preserved in the family | Phase A/B leave the family untouched | AC-2 |
| No dangling references to the retired folder | Phase C | AC-4 |

---

## 8. Testing strategy

No runtime exists — verification is the deterministic command set:

- `Test-Path prompts\analysis.txt` → False; `git status` shows the tracked
  deletion (AC-1).
- `Test-Path devflow\prompts\PROMPT-001-methodology-analysis.md` → True +
  body spot-check (AC-2).
- `git diff AGENTS.md` → only the project-section lines in scope; the
  framework block byte-identical (AC-3).
- grep for `prompts/analysis.txt` and the retired-folder phrasing across the
  repository → 0 outside the documenting records (AC-4).
- `ConvertFrom-Json` + schema check on the Bolt manifest (AC-5).
- **Edge cases:** the `**Neither this file…**` sentence reworded without
  breaking its meaning; CRLF/LF handling; the four lines edited with no
  collateral changes.

**BUG evidence:** n/a — not a BUG Bolt.

---

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | — | `n/a` — documentation-only change, no executable code |
| SAST / SBOM | — | `n/a` — no code, no dependencies |
| Perf-smoke (p95/p99) | — | `n/a` — no runtime |
| Prompt-injection scan | — | `pass` — all text authored here |
| Secret-leak scan | — | `pass` |
| Hallucination lint | — | `pass` — ADR-003, US-003, Bolt and all paths resolve on disk |
| IP / license provenance | — | `n/a` — no third-party content |
| PII / DLP | — | `n/a` — `internal`, no personal data |
| Dependency-confusion | — | `n/a` — no dependencies |
| Test-first evidence | — | `n/a` — not a BUG Bolt |
| Behavioral reproducibility | — | `pass` — deterministic checks, idempotent |
| Bolt-manifest validation | — | `pass` — 0 errors against `manifest-v4-bolt.schema.json` |

---

## 10. Security and data

- No security boundary touched. The deleted file is a plain-text prompt; its
  content remains in the family (no data loss).
- Data classification: `internal`.

---

## 11. Monitoring and observability

`n/a` — no runtime. Verification output is captured in the MEM.

---

## 12. Migration, compatibility and rollback

- **Migration:** none — this is a maintainer-side retirement; adopters are
  unaffected (the kit never shipped root `prompts/`).
- **Compatibility:** the AGENTS.md framework block is untouched; agents and
  the family behave as before.
- **Rollback:** `git checkout HEAD -- prompts/analysis.txt` restores the
  file; the AGENTS.md edits revert with the same command. Both are
  committed history afterwards.

---

## 13. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| Content loss | 1 | 3 | PROMPT-001 presence check (AC-2) |
| AGENTS.md framework block accidentally touched | 1 | 4 | Phase B restricted to the project section; AC-3 diff check |
| A missed reference to the retired folder | 2 | 2 | AC-4 grep sweep |
| Wording breaks the "not distributed" meaning | 2 | 2 | Explicit reword in Phase B + AC-3 review |

---

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| Delete the file instead of keeping a stub | ADR-003's explicit rule ("its remaining file is removed by Bolt and the folder is not recreated") |
| Reword the AGENTS.md references rather than leaving them | The operational memory must match the approved zone table; drift is what the migration just eliminated |
| Family and PROMPT-001 untouched | Content continuity is the guarantee that makes the deletion safe |
| No adopter-facing change | The kit never contained root `prompts/` — retirement is maintainer-side only |

---

## 15. Stop conditions

- The framework block of AGENTS.md appears in the diff → stop, revert,
  record in the MEM.
- PROMPT-001 is missing or altered before Phase A → stop; the deletion would
  lose content.
- A reference to the retired folder is found outside the documenting
  records (AC-4 fails) → stop, complete the sweep; never assume.

---

## 16. Definition of Done (DoD)

- [ ] All phases (A–C) implemented
- [ ] All acceptance criteria (AC-1..AC-5) pass
- [ ] Verification suite GREEN (deletion, content presence, AGENTS.md diff scope, grep 0, manifest 0 errors)
- [ ] Change follows ADR-003 and the approved Bolt
- [ ] Applicable gates pass / waived (ADR) / n/a (reason) — §9
- [ ] MEM created in `devflow/memory/` (exactly one per V-Bounce)
- [ ] Manifest `v_bounces[]` entry appended in `devflow/metrics/bolts/`
- [ ] HITL-MEM-Approval recorded

---

## 17. References

- `devflow/adrs/ADR-003-prompts-family-canonical-home.md` (accepted — retired zone)
- `devflow/functional/bolts/US-000.BOLT-003-retire-root-prompts.md` (approved Bolt)
- `devflow/functional/user-stories/US-003-prompts-family.md` (the family)
- Root `AGENTS.md` — project section (repository surface, in scope by rule)

---

## 18. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-21 | eugenio.serrano | Initial revision 1 (draft) |

---

## 19. HITL-SPEC-Approval

> **Avenga DevFlow §2.4.1, §3.0.** This SPEC remains a draft until the
> Dev-validator (+ applicable domain owners) records `HITL-SPEC-Approval`
> (in the `review` frontmatter block). Bolt approval (`HITL-BOLT-READY-Approval`)
> authorizes SPEC preparation; **SPEC approval** authorizes the code-run /
> V-Bounce. A material source change invalidates this approval — stop,
> revise, re-approve (G15).

| Field | Value |
|-------|-------|
| **review.reviewers** | eugenio.serrano (dev_validator) |
| **review.decision** | approved |
| **review_ready_at** | `2026-08-21T03:20:51-03:00` |
| **review.started_at** | `2026-08-21T03:22:06-03:00` |
| **review.decided_at** | `2026-08-21T03:22:06-03:00` |
| **Findings** | None — acknowledged_without_comment (reason in frontmatter `review:` block) |
