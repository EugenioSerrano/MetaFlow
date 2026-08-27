---
id: "SPEC-260823-0052"
title: "Fix the residual consistency gaps in the v5.0 kit (REV-004 F-02..F-07 + F-08)"
date: "2026-08-23"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved" # draft | approved | blocked | obsolete
origin: "REV-004" # F-02..F-07 (+F-08) — the residual-consistency evidence
bolt: "US-000.BOLT-012" # ⚠️ MANDATORY
revision: 2
associated_adrs:
  - "devflow/adrs/ADR-004-repository-partition-v2.md" # kit-only edits
prerequisites: []
risk_class: "low" # mirrors the Bolt
autonomy_level: "L3" # low → L3 default; deterministic doc sweep
turn_budget: "" # platform default (10 loops without green)
data_classification: "internal"
review_ready_at: "2026-08-23T01:09:25-03:00"
review: # HITL-SPEC-Approval rev 2 — recorded by the human reviewer (§3.0); decision dictated by the human in conversation ("aprobado!") and transcribed by the agent
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - user: "eugenio.serrano"
      role: "dev_validator"
    - user: "eugenio.serrano"
      role: "tech_lead"
  started_at: "2026-08-23T01:10:54-03:00"
  decided_at: "2026-08-23T01:10:54-03:00"
  findings: []
  acknowledged_without_comment: true # must be true when findings is empty (§3.0)
  acknowledgment_reason: "Approved revision 2 against the re-affirmed Bolt US-000.BOLT-012 (material revision: H1–H6 removal kit-wide, prose + G05 rows), REV-004 (F-02..F-08) and ADR-004. The rev-2 inventory (15 locations / 7 files) matches the current tree; AC-4 is now a residue sweep (grep H1–H6 = 0); G05's enforcement unchanged (canonical 13-code list); G-count 39. Rev-1 approval preserved append-only in the manifest. Reviewer holds dev_validator and tech_lead (domain owner) — self-assigned, single-operator. V-Bounce 2 authorized."
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs and headings (##) in
  English; prose content_language (en).

  DOGFOODING SPLIT: authored under v4.2 (root devflow/, ADR-006), own checkpoint
  HITL-SPEC-Approval, manifest schema_version 4.0. Implements US-000.BOLT-012 by
  editing the v5.0 PRODUCT (distribution-kit/, vocabulary AITL-*). Kit-only
  (ADR-004); the root tree inherits at the next §5.16 migration.

  ⚠️ DRAFT until HITL-SPEC-Approval. SPEC approval authorizes the V-Bounce; no
  code-run before it (G14).
-->

# SPEC-260823-0051 — Residual consistency gaps in the v5.0 kit (REV-004 F-02..F-07 + F-08)

| Field | Value |
|-------|-------|
| **Origin** | REV-004 (approved 2026-08-23 — F-02..F-07 + F-08) |
| **Bolt** | [US-000.BOLT-012](../functional/bolts/US-000.BOLT-012-kit-consistency-residue.md) — HITL-BOLT-READY-Approval 2026-08-23T00:51:05 |
| **ADRs** | ADR-004 (kit-only) |
| **Risk / Autonomy** | low / L3 |

---

## 1. Objective

Apply the six localized consistency corrections evidenced by REV-004
F-02..F-07 (plus the optional cosmetic F-08), so the kit's normative prose
and summaries agree with the kit's own rules:

1. **F-02 — §3.9 Dev-validator role:** remove "never one they themselves
   drafted or authored" and align the non-functional BUG approval description
   to G29 / §3.11 / §2.16 (guidance, never a gate; the BUG's own author
   included, any severity). **G29 itself is not modified.**
2. **F-03 — §0 Quick Start:** replace the absolute "A human checkpoint cannot
   be delegated to AI" with the AITL charter wording ("a human **by default**,
   a virtual DevFlow Agent only by explicit, valid configuration; absent or
   invalid config → human-only, no AI-signed approval possible").
3. **F-04 — `avenga-devflow/INDEX.md`:** remove `UNIT, UAT` from the named
   checkpoint enumeration (13 codes per §3.0; Unit/UAT dormant/removed).
4. **F-05 — legacy-name prose (maintainer direction, rev 2):** **remove** the
   v3-era `H1–H6` aliases kit-wide (prose **and** G05 rows in GUARDRAILS +
   the four agents). The legacy set becomes solely the pre-v5 `HITL-*`
   prefix; G05's enforcement is unchanged (canonical 13-code list, §3.0);
   G-count stays 39. Rev 1's "extend with `HITL-*`" direction is superseded.
5. **F-06 — `reviews/README.md`:** reword "must reach an Architect/Tech Lead"
   to the recommended-approver phrasing per G29.
6. **F-07 — methodology §3.1 `llm` rule:** declare the AREV per-phase-model
   exception that GUARDRAILS W09 already enforces
   (`challenger_model` / `defender_model` / `judge_model`, no separate
   `llm:` field).
7. **F-08 (cosmetic):** wrap the placeholder paths in
   `adversarial-reviews/TEMPLATE-AREV.md` and
   `functional/user-stories/TEMPLATE-US.md` in code spans.

If NOT done: the kit ships a role rule that contradicts its own G29 (F-02), a
quick-start absolute that negates the flagship AITL feature (F-03), and four
smaller prose/guardrail mismatches that a careful adopter will trip on.

**Scope boundary:** no guardrail text changes (G29, G18/G24, schemas
untouched); alignment only. Kit-only (ADR-004); root inherits via §5.16.

---

## 2. Context

REV-002 remediated the first kit-consistency pass (US-000.BOLT-007); REV-004
(approved 2026-08-23) found that two finding families survived at locations
the earlier sweep did not reach, plus three smaller cross-reference gaps and
one cosmetic. US-000.BOLT-010 (Done) established the current G29 wording
("guidance, never a gate; author included") — §3.9 still contradicts it. This
SPEC is the mechanical HOW for US-000.BOLT-012; the location inventory (§4)
was built by multiline grep of the current tree.

---

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | `devflow/functional/bolts/US-000.BOLT-012-kit-consistency-residue.md` | HITL-BOLT-READY-Approval ✓ 2026-08-23T00:51:05 |
| Origin REV | `devflow/reviews/REV-004-kit-self-containment-consistency-audit.md` | HITL-REV-Approval ✓ 2026-08-23T00:44:14 |
| Container | `devflow/functional/user-stories/US-000-non-functional.md` | no approval lifecycle ✓ |
| ADR | `devflow/adrs/ADR-004-repository-partition-v2.md` | HITL-ADR-Approval ✓ (accepted) |
| G29 baseline | `distribution-kit/devflow/GUARDRAILS.md` G29 + `US-000.BOLT-010` (Done) | reference text, not an edit target |
| Repository baseline | current working tree on branch `5.0` | — |

Pre-SPEC evidence gate: **all governed sources approved** — no draft input.
The edited files are product files in `distribution-kit/`; their exact current
texts are captured in §4.

---

## 4. Scope — exact location inventory

All paths relative to `distribution-kit/`.

### Phase A — F-02: §3.9 Dev-validator role (`avenga-devflow/Avenga-DevFlow.md`, lines 2594-2598)

Current (the clause spans the 2597-2598 line break):
"…and approve `high`/`medium`/`low`-severity non-functional BUGs (and their
dedicated Bolt) — never one they themselves / drafted or authored."

Replacement:
"…and approve non-functional BUGs (and their dedicated Bolt) at any severity —
any qualified team member, the BUG's own author included, may record the
approval (G29: guidance, never a gate)."

Rule: no other §3.9 sentence changes.

### Phase B — F-03: §0 Quick Start (`avenga-devflow/Avenga-DevFlow.md`, line 141)

Current: "A human checkpoint cannot be delegated to AI."

Replacement: "A checkpoint is occupied by a human **by default**; a virtual
DevFlow Agent only by explicit, valid configuration — absent or invalid
configuration, every checkpoint is human-only and no AI-signed approval is
possible (§3.0)."

### Phase C — F-04: checkpoint enumeration (`avenga-devflow/INDEX.md`, line 13)

Current: "…(US, BUG, TC, BOLT-READY, BOLT-DONE, ADR, SPEC, MEM, DISC, REV,
AREV-CRITIQUE/DEFENSE/VERDICT, UNIT, UAT)…"

Replacement: drop `, UNIT, UAT` → "(US, BUG, TC, BOLT-READY, BOLT-DONE, ADR,
SPEC, MEM, DISC, REV, AREV-CRITIQUE/DEFENSE/VERDICT)".

### Phase D — F-05: `H1–H6` removal, kit-wide (7 files, 15 locations)

The maintainer direction (2026-08-23) supersedes rev 1's "extend with
`HITL-*`": the v3-era `H1–H6` aliases are **removed** from every location;
the legacy set becomes solely the pre-v5 `HITL-*` prefix. G05's enforcement
is unchanged (legacy and non-canonical names are invalid for new approvals;
the canonical 13-code list in §3.0 is the normative reference); G-count stays
39. Inventory against the **current** tree (post V-Bounce 1 of BOLT-011/012):

| File | Line(s) | Current (excerpt) | Replacement |
|------|---------|-------------------|-------------|
| `CLAUDE.md` | 49 (AITL preamble) | "Legacy H1–H6 aliases and the pre-v5 `HITL-*` prefix are invalid." | "The pre-v5 `HITL-*` prefix is invalid." |
| `CLAUDE.md` | 221 (G05 row) | "Legacy checkpoint names (H1–H6, or the pre-v5 `HITL-*` prefix) or any non-canonical `AITL-*` identifier (canonical is `AITL-*`; `HITL-*` survives only in migrated history, G36)" | "Legacy checkpoint names (the pre-v5 `HITL-*` prefix) or any non-canonical `AITL-*` identifier (canonical is `AITL-*`; `HITL-*` survives only in migrated history, G36)" |
| `CLAUDE.md` | 391 (AITL Checkpoints) | "Checkpoints are `AITL-<CODE>-Approval` (legacy H1–H6 aliases are invalid)." | "Checkpoints are `AITL-<CODE>-Approval` (the pre-v5 `HITL-*` prefix is invalid)." |
| `.agents/skills/avenga-devflow/SKILL.md` | 54, 238, 408 | same three patterns as CLAUDE.md | same three replacements |
| `.github/agents/AvengaDevFlow.agent.md` | 78, 266, 436 | same | same |
| `.opencode/agents/AvengaDevFlow.md` | 65, 249, 419 | same | same |
| `GUARDRAILS.md` | 60 (G05 row + response) | row: "Use legacy checkpoint names (H1–H6, or the pre-v5 `HITL-*` prefix) or non-canonical `AITL-*` identifiers"; response: "Legacy prefixes — the numbered H1–H6 aliases and the pre-v5 `HITL-*` names, preserved only in migrated history (G36) — are invalid for new approvals (§3.0)." | drop the `H1–H6` mentions in both |
| `devflow/README.md` | 244 | "`AITL-<CODE>-Approval`; legacy numbered aliases (H1–H6) and the pre-v5 `HITL-*` prefix are invalid." | "`AITL-<CODE>-Approval`; the legacy pre-v5 `HITL-*` prefix is invalid." |
| `devflow/ONBOARDING.md` | 69 | "The old H1–H6 no longer exist." | "The pre-v5 `HITL-*` prefix is invalid (G05)." |

Rule: remove the `H1–H6` tokens; keep the informative content; the legacy set
is now exclusively the pre-v5 `HITL-*` prefix. After the sweep, grep
`H1–H6` over `distribution-kit/` — result must be **zero** (this is the
residue check rev 1's presence-verification missed).

### Phase E — F-06: severity mapping (`reviews/README.md`, line 183)

Current: "…`critical` when a non-functional BUG must reach an Architect/Tech
Lead"

Replacement: "…`critical` when the recommended approver for a non-functional
BUG is an Architect/Tech Lead (guidance, never a gate — any qualified team
member, the author included, may approve)".

### Phase F — F-07: `llm`-rule exception (`avenga-devflow/Avenga-DevFlow.md`, §3.1, after line 1826)

Insert after the LLM-traceability bullet: "The AREV phase templates are the
exception: they record the executing model via `challenger_model` /
`defender_model` / `judge_model` (§2.15, §3.13) and carry no separate `llm:`
field."

### Phase G — F-08 (cosmetic): placeholder links (2 files)

| File | Links | Change |
|------|-------|--------|
| `adversarial-reviews/TEMPLATE-AREV.md` | `[01-CRITIQUE.md](01-CRITIQUE.md)`, `[02-DEFENSE.md](02-DEFENSE.md)`, `[03-VERDICT.md](03-VERDICT.md)` (phase table) | wrap in backticks: `` `01-CRITIQUE.md` `` (etc.) — no link |
| `functional/user-stories/TEMPLATE-US.md` | `[BOLT-001](../bolts/US-NNN.BOLT-001-short-title.md)`, `[BOLT-002](../bolts/US-NNN.BOLT-002-short-title.md)` (Bolts table) | wrap the paths in backticks — no link |

---

## 5. Prerequisites and baseline

- Baseline: current working tree on branch `5.0`; the four agent bodies are
  byte-identical except the sanctioned `agents-data/<agent>/` line (parity
  diff = 2 lines per pair) — this is the pre-edit baseline the Phase D edits
  must preserve.
- No prior SPEC dependency.

---

## 6. Phases

### Phase A — F-02 (§3.9)

Apply the Phase A replacement. Verify with a multiline grep that "never one
they themselves" returns **zero** in `distribution-kit/`.

**Files modified:** `devflow/avenga-devflow/Avenga-DevFlow.md`.

### Phase B — F-03 (§0)

Apply the Phase B replacement. Verify "cannot be delegated to AI" returns
**zero** in `distribution-kit/`.

**Files modified:** `devflow/avenga-devflow/Avenga-DevFlow.md`.

### Phase C — F-04 (INDEX enumeration)

Apply the Phase C replacement. Verify the enumeration lists exactly the 13
§3.0 codes.

**Files modified:** `devflow/avenga-devflow/INDEX.md`.

### Phase D — F-05 (legacy prose, 5 files in lockstep)

Apply the Phase D replacements to `README.md` and all four agent preambles.
Re-run the four-agent parity diff — the result must stay **2 lines per pair**
(the sanctioned `agents-data/<agent>/` divergence), proving the preamble edit
landed identically in all four.

**Files modified:** `devflow/README.md`, `CLAUDE.md`,
`.agents/skills/avenga-devflow/SKILL.md`,
`.github/agents/AvengaDevFlow.agent.md`,
`.opencode/agents/AvengaDevFlow.md`.

### Phase E — F-06 (reviews/README)

Apply the Phase E replacement. Verify "must reach an Architect/Tech Lead"
returns **zero** in `distribution-kit/`.

**Files modified:** `devflow/reviews/README.md`.

### Phase F — F-07 (§3.1 exception)

Insert the exception sentence after the LLM-traceability bullet in §3.1.
Verify the sentence is present verbatim and that W09's cited sections
(§2.15, §3.13) now match the declared exception.

**Files modified:** `devflow/avenga-devflow/Avenga-DevFlow.md`.

### Phase G — F-08 (cosmetic, optional)

Apply the code-span changes to the two templates. Verify the links no longer
appear as markdown links.

**Files modified:** `devflow/adversarial-reviews/TEMPLATE-AREV.md`,
`devflow/functional/user-stories/TEMPLATE-US.md`.

---

## 7. Acceptance criteria

- **AC-1 (F-02):** §3.9 carries no author-exclusion clause; its non-functional
  BUG wording matches G29 / §3.11 (author included, any severity).
- **AC-2 (F-03):** §0's checkpoint-delegation sentence mirrors the
  human-by-default / explicit-valid-configuration wording of `GUARDRAILS.md`.
- **AC-3 (F-04):** the `avenga-devflow/INDEX.md` checkpoint enumeration lists
  exactly the 13 §3.0 codes (no UNIT, no UAT).
- **AC-4 (F-05):** `H1–H6` is **absent kit-wide** (grep over
  `distribution-kit/` = 0 — prose + G05 rows); every legacy-name statement
  names only the pre-v5 `HITL-*` prefix; G-count stays 39.
- **AC-5 (F-06):** `reviews/README.md` phrases the Architect/Tech Lead as
  recommended for `critical`, never "must reach".
- **AC-6 (F-07):** methodology §3.1 declares the AREV phase-template `llm`
  exception explicitly.
- **AC-7 (F-08):** the placeholder links no longer appear as markdown links.
- **AC-8:** G-count = 39×5 unchanged; four-agent body parity at 2 lines per
  pair.
- **AC-9:** `git status` shows only `distribution-kit/` edits + root
  governance records (kit-only, ADR-004).

### AC mapping to source (measurable outcome)

| Source | How this SPEC satisfies it | Verifying test/evidence |
|--------|----------------------------|--------------------------|
| REV-004 F-02 | Phase A | grep "never one they themselves" = 0; presence of the replacement |
| REV-004 F-03 | Phase B | grep "cannot be delegated to AI" = 0 |
| REV-004 F-04 | Phase C | enumeration = 13 codes |
| REV-004 F-05 | Phase D | parity diff = 2 lines/pair; phrase present 5× |
| REV-004 F-06 | Phase E | grep "must reach an Architect/Tech Lead" = 0 |
| REV-004 F-07 | Phase F | presence of the exception sentence |
| REV-004 F-08 | Phase G | no markdown link to the placeholders |
| Bolt §2 completion criteria | AC-8, AC-9 | G-count + parity + git status |

---

## 8. Testing strategy

Documentation product — verification replaces the test suite:

- **Absence sweeps (multiline-aware):** "never one they themselves",
  "cannot be delegated to AI", "must reach an Architect/Tech Lead",
  "UNIT, UAT", **"H1–H6"** — each returns zero in `distribution-kit/`.
- **Presence assertions:** each replacement string found at its location;
  the §3.1 exception sentence present verbatim; the legacy phrase with
  `HITL-*` present 5× (README + 4 agents).
- **Invariant checks:** G-count 39×5; four-agent body parity (2 lines per
  pair) — the Phase D lockstep edit is the risky one.
- **Edge cases:** the §3.9 phrase spans a line break (2597-2598) — the
  multiline grep must catch the wrapped form; the agent preamble lines differ
  slightly in wording between `README.md` and the agents (see §4 table) — each
  file gets its own exact replacement.

---

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | n/a — documentation product, no runtime | n/a |
| SAST / SBOM | n/a | n/a |
| Perf-smoke (p95/p99) | n/a | n/a |
| Prompt-injection scan | n/a | n/a |
| Secret-leak scan | pass — text-only edits | pass |
| Hallucination lint | pass — every edited phrase resolves on disk | pass |
| IP / license provenance | n/a | n/a |
| PII / DLP | n/a | n/a |
| Dependency-confusion | n/a | n/a |
| Test-first evidence | n/a — documentation-only; absence/presence sweeps are the evidence (§8) | n/a |
| Behavioral reproducibility | pass — re-running the sweeps from the SPEC + captured tree reproduces the results | pass |
| Bolt-manifest validation | pass — Bolt manifest validates against `manifest-v4-bolt.schema.json` | pass |

> Each gate ends `pass` / `waived` (ADR-NNN) / `n/a` (with reason) (§3.6).

---

## 10. Security and data

- Text-only edits to distributed documentation; `data_classification: internal`.
- No secrets, no new dependencies, no runtime surface.

---

## 11. Monitoring and observability

n/a — documentation product; the "observability" is the sweep and parity
evidence in §8.

---

## 12. Migration, compatibility and rollback

- **Migration:** n/a — no schema, config or runtime change.
- **Compatibility:** n/a.
- **Rollback:** per-file git revert of the touched phrases; canonical SPEC
  revision 1 remains valid for a re-run.

---

## 13. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| Phase D edit lands unevenly across the four agents (drift) | 2 | 4 | parity diff must stay at 2 lines/pair (AC-8) |
| Over-broad edit touches G29 or a guardrail despite the scope guard | 1 | 4 | explicit exclusion list in §1/§2; diff review |
| Multiline grep misses the wrapped §3.9 phrase | 2 | 2 | multiline-aware absence sweep (REV-004's own method) |
| F-07 wording contradicts W09 | 1 | 2 | mirror W09's exact exception sentence |

---

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| Align §3.9 to G29 instead of editing G29 | the direction is settled (G29 governs, US-000.BOLT-010 Done); §3.9 is the outlier — no ADR needed |
| Keep the §3.9 sentence structure, replace only the restrictive clause | minimal diff; the role description keeps its shape |
| Per-file exact replacements in the four preambles (wording differs slightly) | a single find/replace string would miss or over-match; the §4 table pins each |
| F-08 folded into this Bolt | one localized-text pass; matches the approved Bolt scope |

---

## 15. Stop conditions

- Any edit that would change G29, G18/G24, a schema or another guardrail →
  stop, revise the Bolt/SPEC, re-approve (G15).
- Parity diff after Phase D exceeds 2 lines per pair → stop; the four-agent
  lockstep is broken, fix before proceeding.
- A stale phrase found in a file NOT listed in §4 → stop; extend the
  inventory, revise the SPEC, re-approve.

---

## 16. Definition of Done (DoD)

- [ ] All Phase A..G edits applied
- [ ] AC-1..AC-9 verified (absence/presence sweeps, enumeration, parity, G-count, git status)
- [ ] `US-000.BOLT-012` manifest valid (`manifest-v4-bolt.schema.json`)
- [ ] MEM created in `devflow/memory/` (exactly one per V-Bounce)
- [ ] Manifest `v_bounces[]` entry appended in `devflow/metrics/bolts/`
- [ ] HITL-MEM-Approval recorded

---

## 17. References

- `devflow/reviews/REV-004-kit-self-containment-consistency-audit.md` (F-02..F-08)
- `devflow/functional/bolts/US-000.BOLT-012-kit-consistency-residue.md`
- `devflow/adrs/ADR-004-repository-partition-v2.md`

---

## 18. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-23 | eugenio.serrano | Initial draft (revision 1) |
| 2026-08-23 | eugenio.serrano | **Revision 2 (material, G15):** F-05 remediated by removing the v3-era `H1–H6` aliases kit-wide (prose + G05 rows) per maintainer direction; legacy set = pre-v5 `HITL-*` only; inventory extended to 15 locations / 7 files; AC-4 redefined as a residue sweep (grep `H1–H6` = 0). Supersedes rev 1's "extend with `HITL-*`" scope. Re-approval pending at `HITL-SPEC-Approval` |
| 2026-08-23 | eugenio.serrano | `HITL-SPEC-Approval` rev 2 recorded (approved) — V-Bounce 2 authorized |

---

## 19. HITL-SPEC-Approval

> **Avenga DevFlow §2.4.1, §3.0.** **Revision 2.** This SPEC remains a draft
> until the Dev-validator (+ applicable domain owners) records
> `HITL-SPEC-Approval` (in the `review` frontmatter block). Rev 1's approval
> is preserved append-only in the manifest; rev 2 supersedes it (G15). A
> material source change invalidates this approval — stop, revise, re-approve
> (G15).

| Field | Value |
|-------|-------|
| **review.reviewers** | eugenio.serrano (dev_validator + tech_lead) |
| **review.decision** | **approved** |
| **review_ready_at** | `2026-08-23T01:09:25-03:00` |
| **review.started_at** | `2026-08-23T01:10:54-03:00` |
| **review.decided_at** | `2026-08-23T01:10:54-03:00` |
| **Findings** | none — `acknowledged_without_comment: true` (see frontmatter) |
