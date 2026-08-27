---
id: "SPEC-260821-0108"
title: "Relax non-critical non-functional BUG approval routing (G29)"
date: "2026-08-21"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved" # draft | approved | blocked | obsolete
origin: "REV-001" # US-NNN, TC-NNN, BUG-NNN, DISC-NNN, REV-NNN, AREV-NNN, or ADR-NNN that motivated this SPEC
bolt: "US-000.BOLT-002" # ⚠️ MANDATORY — US-NNN.BOLT-NNN | US-000.BOLT-NNN | TC-NNN.BOLT-NNN
revision: 1 # material revision of this canonical SPEC (matches manifest spec_revisions[])
associated_adrs: ["devflow/adrs/ADR-001-repository-layout-methodology-and-product.md"]
prerequisites: []
risk_class: "medium" # mirrors the Bolt's risk_class
autonomy_level: "L3" # low/medium → L3 default
turn_budget: "" # platform default (10 loops without green)
data_classification: "internal"
review_ready_at: "2026-08-21T01:08:10-03:00"
review: # HITL-SPEC-Approval — filled by the human reviewer (§3.0)
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - user: "eugenio.serrano"
      role: "dev_validator"
  started_at: "2026-08-21T01:15:06-03:00"
  decided_at: "2026-08-21T01:15:06-03:00"
  findings: []
  acknowledged_without_comment: true # must be true when findings is empty (§3.0)
  acknowledgment_reason: "Reviewed revision 1 against the approved Bolt US-000.BOLT-002, the approved REV-001 (F-02) and ADR-001 (kit-only rule): the file inventory matches the grep-verified locations, the ACs are objectively checkable, the critical/functional routes are preserved by explicit phase wording, and the gates are correctly classified. Approved as drafted."
---

# SPEC-260821-0108 — Relax non-critical non-functional BUG approval routing (G29)

| Field | Value |
|-------|-------|
| **Origin** | REV-001 (approved — finding F-02, Major gap) |
| **Bolt** | [US-000.BOLT-002](../functional/bolts/US-000.BOLT-002-relax-non-critical-bug-approval-routing.md) |
| **ADRs** | [ADR-001](../adrs/ADR-001-repository-layout-methodology-and-product.md) — rules 2, 5, 7: changes land in `distribution-kit/` only, never in the root `devflow/` |
| **Risk Class** | medium |
| **Revision** | 1 |

---

## 1. Objective

Modify the distributable methodology so that the `HITL-BUG-Approval` routing
for **non-functional BUGs with `severity: high|medium|low`** no longer
requires "a Developer other than the BUG's own author": **any team member —
the author included — may record the approval**. The two other routes stay
byte-for-byte as they are today: functional BUGs remain approved by a
Functional Analyst, and non-functional BUGs with `severity: critical` remain
approved by an Architect or Tech Lead. The dedicated Bolt of a non-functional
BUG mirrors the relaxed route at non-critical severities, so the fix at the
BUG level is not re-blocked at the Bolt level.

If NOT implemented, a single-maintainer team remains structurally blocked on
every non-functional BUG at any severity: no valid approver exists, no
dedicated Bolt can be created (G02), and the governed route for fixing
non-functional defects stays closed — the REV-001 F-02 blocker.

This change lands **only** in `distribution-kit/` (the product tree,
ADR-001 rule 7). The root `devflow/` — the installed rulebook that governs
this repository — is **never touched**; it receives this change only through
the next §5.16 release migration.

---

## 2. Context

REV-001 (approved 2026-08-21, `HITL-REV-Approval`) inventoried all 15 HITL
checkpoints and their role routing. Finding **F-02 (Major gap)** established
that the non-functional BUG routing is structurally unsatisfiable in a
single-person team: with one member, no "Developer other than the author"
exists, so the whole non-functional BUG route closes by construction. The
approver decided to relax the non-critical route (Option A: any member,
author included) while keeping the `critical` route and the functional route
strict — the relaxation is deliberate policy, not an oversight; the
compensating control is that every approval still records the approver's
name, role, timestamps and evidence.

The Bolt (US-000.BOLT-002, `HITL-BOLT-READY-Approval` recorded) defines the
WHAT; this SPEC defines the HOW: the exact texts, files and verification for
a coordinated, drift-free edit of the distributable.

---

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | `devflow/functional/bolts/US-000.BOLT-002-relax-non-critical-bug-approval-routing.md` | HITL-BOLT-READY-Approval ✓ (2026-08-21T01:07:17-03:00) |
| Origin REV | `devflow/reviews/REV-001-hitl-checkpoint-role-inventory.md` | HITL-REV-Approval ✓ (2026-08-21T00:40:47-03:00) |
| Container | `devflow/functional/user-stories/US-000-non-functional.md` | US-000 — no approval lifecycle ✓ |
| ADR | `devflow/adrs/ADR-001-repository-layout-methodology-and-product.md` | HITL-ADR-Approval ✓ |
| Repository baseline | `0a47e3f` on branch `4.2` (working tree: REV-001 + INDEX + BOLT-002 + manifest, uncommitted) | — |

Pre-SPEC evidence gate: **all sources approved** — no draft governed input.
The affected files are product files in `distribution-kit/`; their current
texts were captured by grep (see §4).

---

## 4. Scope

### In scope

Every distributable text that defines `HITL-BUG-Approval` routing for
non-functional BUGs or the dedicated-Bolt mirror, all under
`distribution-kit/`:

- **Guardrail:** `distribution-kit/devflow/GUARDRAILS.md` — G29 row (line 58)
  and the checkpoint-map row for `HITL-BUG-Approval` (line 25).
- **Methodology:** `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md`
  — §0 E2E summary (line 23), §1 flow (line 130), §2.4 Bolt-routing footnote
  (line 445), §2.16 BUG-nature table (line 1282), §3.0 HITL checkpoint table
  (line 1374), §3.3.1 BUG correction rules (line 2613), §5.15 folder map
  (line 4323).
- **Agent definitions (×4):** `distribution-kit/CLAUDE.md` (G29 row line 245,
  Bug-Fix-Protocol line 526), `.agents/skills/avenga-devflow/SKILL.md`
  (262, 543), `.github/agents/AvengaDevFlow.agent.md` (290, 571),
  `.opencode/agents/AvengaDevFlow.md` (273, 554).
- **Onboarding:** `distribution-kit/devflow/ONBOARDING.md` (line 28).
- **BUG artifacts:** `distribution-kit/devflow/bugs/README.md` (line 68 and
  the severity-routing paragraph), `distribution-kit/devflow/bugs/TEMPLATE-BUG.md`
  (routing note in frontmatter and approval section).
- **Functional artifacts:** `distribution-kit/devflow/functional/README.md`
  (line 44), `distribution-kit/devflow/functional/bolts/TEMPLATE-BOLT.md`
  (line 176), `distribution-kit/devflow/functional/user-stories/US-000-non-functional.md`
  (line 69).

### Out of scope

- The root `devflow/` tree (installed rulebook — frozen, ADR-001 rule 1).
- Functional BUG routing and the `critical` non-functional route (unchanged
  by decision).
- REV-001 findings F-03..F-06 (acceptance routing pairs, multi-approver
  counts, role multiplicity, SPEC/UAT counts) — remain open, tracked in the
  REV.
- Team-roster family, role-multiplicity policy, any other checkpoint's
  routing.

---

## 5. Prerequisites and baseline

- `US-000.BOLT-002` approved (`HITL-BOLT-READY-Approval` recorded).
- `REV-001` approved — findings actionable.
- Baseline commit `0a47e3f`; the working tree holds the uncommitted REV-001,
  INDEX and BOLT-002 package (the SPEC's own `sources` reference them).
- The four agent definitions are **in sync before the edit** (whole-body
  diff, ≤2 lines of sanctioned divergence). If a pre-existing drift is
  found, stop and reconcile first (4-agent maintenance rule, AGENTS.md).

---

## 6. Phases

### Phase A — Guardrail layer (GUARDRAILS.md)

**Duration:** ~0.5h total cycle — **Complexity:** Low

#### A.1 Rewrite the G29 row (line 58)

The violation column must no longer include "record as the same person who
drafted it" for non-critical severities. New row text:

```
| G29 | Route a `severity: critical` non-functional BUG (or its dedicated
Bolt) to a Developer, or block a non-critical non-functional BUG for lack of
an approver | ❌ *"Severity-gated routing (§2.16, §3.0): non-functional BUG
with `severity: critical` → Architect or Tech Lead — severity never
downgrades the `critical` route. `severity: high\|medium\|low` → any team
member may record `HITL-BUG-Approval`, the BUG's own author included; the
dedicated Bolt's `HITL-BOLT-READY-Approval` mirrors the same relaxed route.
Self-approval is never permitted on the `critical` route, and the `critical`
route is never routed to a Developer."* |
```

The row stays one G entry — the rule count must remain 39.

#### A.2 Rewrite the checkpoint-map row (line 25)

```
| `HITL-BUG-Approval` | Functional Analyst (functional) / Architect or Tech
Lead (non-functional, `severity: critical`) or any team member, author
included (non-functional, `severity: high\|medium\|low`) | BUG confirmed,
evidenced, classified; only then its one dedicated Bolt may be created. |
```

**Files modified:**
- `distribution-kit/devflow/GUARDRAILS.md` — G29 row and checkpoint-map row
  rewritten; header/footer version markers untouched.

---

### Phase B — Methodology (Avenga-DevFlow.md)

**Duration:** ~1h total cycle — **Complexity:** Medium

#### B.1 §0 E2E summary (line 23) and §1 flow (line 130)

Replace "otherwise by a Developer other than the BUG's own author" with
"otherwise by any team member (the author included)".

#### B.2 §2.4 Bolt-routing footnote (line 445) and §2.16 BUG-nature table (line 1282)

The dedicated-Bolt mirror must state the relaxed route:
"Architect or Tech Lead approves it when `severity: critical`, otherwise any
team member may approve it (the Bolt's own author included)".

#### B.3 §3.0 HITL checkpoint table (line 1374)

The Owner cell for `HITL-BUG-Approval` becomes: "Functional Analyst for
functional BUGs; for non-functional BUGs, Architect or Tech Lead when
`severity: critical`, otherwise any team member (the BUG's own author
included)".

#### B.4 §3.3.1 BUG correction rules (line 2613)

Align the self-approval sentence: the prohibition now applies to the
`critical` route only; non-critical non-functional BUGs may be approved by
the author with the approval still recorded (name, role, timestamps,
evidence).

#### B.5 §5.15 folder map (line 4323)

Rewrite the `bugs/` description cell to state the relaxed routing in the
same words as the checkpoint table.

**Files modified:**
- `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md` — six
  locations (23, 130, 445, 1282, 1374, 2613, 4323), each restating the same
  routing sentence. No other section changes.

---

### Phase C — Four agent definitions (shared body, one synchronized pass)

**Duration:** ~1h total cycle — **Complexity:** Medium

#### C.1 G29 inline row (5 occurrences × 1)

The compact G29 row in the four agent files becomes:

```
| G29 | Non-functional BUG (and its dedicated Bolt): `severity: critical` -> Architect/TL; `high\|medium\|low` -> any team member, author included. Self-approval never permitted on the `critical` route |
```

Applied **identically** in `CLAUDE.md` (245), `SKILL.md` (262),
`AvengaDevFlow.agent.md` (290), `AvengaDevFlow.md` (273).

#### C.2 Bug-Fix-Protocol bullet (4 occurrences)

Replace "non-functional: Architect/TL if severity=critical, else a Developer
other than the BUG's own author" with "non-functional: Architect/TL if
severity=critical, else any team member (author included)" in the four
Bug-Fix-Protocol steps (526, 543, 571, 554).

**Files modified:** the four agent definitions in `distribution-kit/` — each
gets the identical G29 row and the identical protocol bullet. The
`agents-data/<agent>/` path line remains the single sanctioned divergence.

---

### Phase D — Onboarding, BUG and functional artifacts

**Duration:** ~0.5h total cycle — **Complexity:** Low

#### D.1 ONBOARDING.md (line 28)

"…lower severities route to a Developer other than the BUG's own author" →
"…lower severities may be approved by any team member, author included".

#### D.2 bugs/README.md (line 68 + severity-routing paragraph)

Align the `approved` lifecycle row and the severity-routing explanation with
the new rule; keep the critical route wording unchanged.

#### D.3 bugs/TEMPLATE-BUG.md

Align the frontmatter routing note and the approval-section note
("Architect/TL when critical, otherwise any team member — the author
included; self-approval never permitted on the critical route").

#### D.4 functional/README.md (line 44) and functional/bolts/TEMPLATE-BOLT.md (line 176)

Align the dedicated-Bolt mirror footnote: critical → Architect/Tech Lead;
high/medium/low → any team member, the Bolt's own author included.

#### D.5 US-000-non-functional.md (line 69)

Align the BUG-route sentence; drop the now-false "self-approval is not
permitted" clause for the non-critical route.

**Files modified:** the six files above, each a minimal restatement of the
same routing sentence — no structural changes.

---

### Phase E — Verification suite (deterministic checks)

**Duration:** ~0.5h total cycle — **Complexity:** Low

Run and record the full verification set (§8) — greps, sync diff, G-rule
count, root-untouched check — and capture the output in the MEM.

---

## 7. Acceptance criteria

### AC-1: Relaxed rule present everywhere it is defined

**Given** the edited distributable,
**When** grepping for the new routing wording ("any team member",
"author included") in GUARDRAILS, methodology, ONBOARDING, templates and the
four agents,
**Then** each of the 15+ locations that define non-functional BUG routing
states the relaxed rule in consistent words.

### AC-2: No stale "other than" routing remains for non-critical non-functional BUGs

**Given** the edited distributable,
**When** grepping for `other than the (BUG|Bolt)'s own` and `other than its author`,
**Then** zero matches remain in `distribution-kit/` (the phrase is gone from
the routing; historical changelog/CHANGELOG text is not part of the
distributable and is not swept).

### AC-3: Critical and functional routes unchanged

**Given** the edited distributable,
**When** grepping for the critical route ("Architect or Tech Lead when
`severity: critical`" / "Architect/TL if severity=critical") and the
functional route ("Functional Analyst"),
**Then** both appear in every location that defines them, with their
original wording.

### AC-4: Dedicated-Bolt mirror relaxed consistently

**Given** the edited distributable,
**When** grepping §2.16, TEMPLATE-BOLT footnote, functional/README footnote
and the agent protocol bullets,
**Then** the mirror states the relaxed route at non-critical severities in
all of them.

### AC-5: Four-agent synchronization invariant

**Given** the edited agent definitions,
**When** running the whole-body diff from the `# Avenga DevFlow v4.2
(Methodology)` heading to EOF (tr -d '\r' normalized),
**Then** claude vs codex/gh/opencode differ by exactly 2 lines (the
`agents-data/<agent>/` path), and each file's inline G-rule table counts
39/39/39/39.

### AC-6: Root devflow untouched

**Given** the completed V-Bounce,
**When** running `git status`,
**Then** no file under the root `devflow/` (methodology content) is modified
— only `distribution-kit/` files, plus this SPEC's governance records.

### AC-7: Bolt-manifest validation

**Given** the manifest updated for this SPEC revision,
**When** validating against `manifest-v4-bolt.schema.json`,
**Then** 0 errors.

### AC mapping to source (non-functional)

| Source outcome | How this SPEC satisfies it | Verifying test/evidence |
|----------------|----------------------------|--------------------------|
| Bolt §2 objective: single-maintainer team can complete the NF BUG route at non-critical severities | Routing texts relaxed in every defining location | AC-1, AC-2, AC-4 |
| Bolt §2: critical and functional routes unchanged | Phases A-D leave those wordings intact | AC-3 |
| Bolt §2 evidence: 4-agent sync + G-rule count | Phase C + E | AC-5 |
| Bolt §2 exclusion: root tree untouched | Phase A-D touch kit files only | AC-6 |
| REV-001 F-02 (Major gap) resolved | The dead-end route is removed by policy | AC-1..AC-4 |
| REV-001 F-07 (consistency) preserved | All locations restate one routing sentence | AC-1, AC-3, AC-4 |

---

## 8. Testing strategy

No runtime exists — verification is the deterministic command set:

- **Grep checks (AC-1..AC-4):** count occurrences of the new phrasing and of
  the stale phrasing across `distribution-kit/`; expected counts are
  enumerated in the MEM.
- **Sync diff (AC-5):** the four-agent whole-body diff command from AGENTS.md
  (expected: 2 lines per comparison) plus `grep -cE '^\| G[0-9]{2} \|'`
  = 39 in each of the four agents and GUARDRAILS.
- **Root-untouched check (AC-6):** `git status --short` shows no root
  `devflow/` methodology file.
- **Manifest validation (AC-7):** `ConvertFrom-Json` + schema check.
- **Edge cases:** CRLF/LF line endings (normalize with `tr -d '\r'` before
  the sync diff); the G29 row's escaped pipe (`\|`) inside the table cell;
  the checkpoint-map row's pipe-separated severity list.
- **BUG evidence:** n/a — not a BUG Bolt; no red→green protocol.

---

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | — | `n/a` — documentation-only change, no executable code |
| SAST / SBOM | — | `n/a` — no code, no dependencies |
| Perf-smoke (p95/p99) | — | `n/a` — no runtime |
| Prompt-injection scan | — | `pass` — all text authored here, no external input |
| Secret-leak scan | — | `pass` |
| Hallucination lint | — | `pass` — every §-reference and file path resolves on disk (§2.16, §3.0, §2.4, §3.3.1, §5.15, ADR-001, REV-001, Bolt) |
| IP / license provenance | — | `n/a` — no third-party content |
| PII / DLP | — | `n/a` — `internal`, no personal data |
| Dependency-confusion | — | `n/a` — no dependencies |
| Test-first evidence | — | `n/a` — not a BUG Bolt |
| Behavioral reproducibility | — | `pass` — deterministic grep/diff/count checks, idempotent |
| Bolt-manifest validation | — | `pass` — 0 errors against `manifest-v4-bolt.schema.json` |

---

## 10. Security and data

- The change relaxes a governance routing rule; it touches **no** security
  boundary, credentials, runtime surface or data path. The `critical` route
  (the one with security-bearing defects) is deliberately kept strict.
- Data classification: `internal` — documentation text only, no personal
  data, no PII.

---

## 11. Monitoring and observability

`n/a` — no runtime, no logs, no metrics. The verification suite (§8) is the
observability of this change; its output is captured in the MEM.

---

## 12. Migration, compatibility and rollback

- **Migration:** none in this repository — the change lands in
  `distribution-kit/` and reaches adopting projects through their own
  §5.16 release migration when the next version ships.
- **Compatibility:** the G-rule count stays 39, the four-agent inline tables
  stay complete, and the checkpoint vocabulary is unchanged — no consumer of
  the schema or of the guardrail table breaks.
- **Rollback:** revert the kit commit(s); the root tree is untouched and
  keeps governing unchanged. The SPEC revision is immutable history in the
  Bolt manifest.

---

## 13. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| Text drift between the four agent definitions | 2 | 3 | Phase C applies identical text; AC-5 sync diff is mandatory evidence |
| A defining location is missed in the sweep | 2 | 3 | §4 inventory from grep; AC-2 asserts zero stale matches |
| Root `devflow/` accidentally modified | 1 | 4 | Phases restrict edits to `distribution-kit/`; AC-6 check |
| Weakening review independence for non-critical defects | 3 | 2 | Accepted by decision (F-02); approvals still record name/role/timestamps/evidence |
| Guardrail row breaks markdown table (escaped pipe) | 1 | 2 | Edge case listed in §8; verification reads the row text |

---

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| Author included for non-critical non-functional BUGs (Option A) | The only option that actually unblocks a single-maintainer team; the dead-end is removed by policy, with evidence recording as compensating control |
| `critical` and functional routes stay strict | Security-bearing and business-behavior defects keep their named approvers; the user's explicit decision |
| Dedicated-Bolt mirror relaxes in step | Otherwise the BUG is approvable but its Bolt is not — the fix would be pointless (Bolt §2) |
| F-03..F-06 stay out of scope | Scope discipline: one finding per Bolt; they remain routed and open in REV-001 |
| Change lands in `distribution-kit/` only | ADR-001 rules 1, 2, 5, 7 — the root rulebook is frozen until release migration |

---

## 15. Stop conditions

- Any root `devflow/` methodology file is modified or appears in the diff →
  **stop**, revert, record the blocker in the MEM.
- A pre-existing 4-agent drift is found before Phase C (sync diff > 2 lines)
  → **stop**, reconcile the drift first (AGENTS.md rule), record in the MEM.
- Any location defining non-functional BUG routing is missed and AC-2 fails
  with residual "other than" matches → **stop**, sweep again; do not paper
  over with an assumption.
- A governed source changes materially during execution (G15) → stop,
  revise this SPEC, re-approve.

---

## 16. Definition of Done (DoD)

- [ ] All phases (A–E) implemented
- [ ] All acceptance criteria (AC-1..AC-7) pass
- [ ] Verification suite GREEN (grep counts, sync diff 2 lines, G-count 39/39/39/39, root untouched, manifest 0 errors)
- [ ] Change follows ADR-001 (kit-only) and the approved Bolt
- [ ] Applicable gates pass / waived (ADR) / n/a (reason) — §9
- [ ] MEM created in `devflow/memory/` (exactly one per V-Bounce)
- [ ] Manifest `v_bounces[]` entry appended in `devflow/metrics/bolts/`
- [ ] HITL-MEM-Approval recorded

---

## 17. References

- `devflow/functional/bolts/US-000.BOLT-002-relax-non-critical-bug-approval-routing.md`
  (approved Bolt — the WHAT)
- `devflow/reviews/REV-001-hitl-checkpoint-role-inventory.md` (approved — F-02)
- `devflow/adrs/ADR-001-repository-layout-methodology-and-product.md` (rules 1, 2, 5, 7)
- `devflow/functional/user-stories/US-000-non-functional.md`
- AGENTS.md — four-agent maintenance rules and version-marker sweep

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
| **review_ready_at** | `2026-08-21T01:08:10-03:00` |
| **review.started_at** | `2026-08-21T01:15:06-03:00` |
| **review.decided_at** | `2026-08-21T01:15:06-03:00` |
| **Findings** | None — acknowledged_without_comment (reason in frontmatter `review:` block) |
