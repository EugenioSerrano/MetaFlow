---
id: "SPEC-260821-0150"
title: "Prompts family — ship devflow/prompts/ in the kit"
date: "2026-08-21"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved" # draft | approved | blocked | obsolete
origin: "US-003" # US-NNN, TC-NNN, BUG-NNN, DISC-NNN, REV-NNN, AREV-NNN, or ADR-NNN that motivated this SPEC
bolt: "US-003.BOLT-001" # ⚠️ MANDATORY — US-NNN.BOLT-NNN | US-000.BOLT-NNN | TC-NNN.BOLT-NNN
revision: 1 # material revision of this canonical SPEC (matches manifest spec_revisions[])
associated_adrs: ["devflow/adrs/ADR-001-repository-layout-methodology-and-product.md"]
prerequisites: []
risk_class: "medium" # mirrors the Bolt's risk_class
autonomy_level: "L3" # low/medium → L3 default
turn_budget: "" # platform default (10 loops without green)
data_classification: "internal"
review_ready_at: "2026-08-21T01:50:07-03:00"
review: # HITL-SPEC-Approval — filled by the human reviewer (§3.0)
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - user: "eugenio.serrano"
      role: "dev_validator"
  started_at: "2026-08-21T01:52:12-03:00"
  decided_at: "2026-08-21T01:52:12-03:00"
  findings: []
  acknowledged_without_comment: true # must be true when findings is empty (§3.0)
  acknowledgment_reason: "Reviewed revision 1 against the approved Bolt US-003.BOLT-001 and US-003: the family files, the four-agent sentence and the §5.15 map rows match the approved ACs, the scope boundaries (root devflow and product prompts/ untouched) are explicit, and the ACs are objectively checkable. Approved as drafted."
---

# SPEC-260821-0150 — Prompts family: ship devflow/prompts/ in the kit

| Field | Value |
|-------|-------|
| **Origin** | US-003 (approved — 2 SP, 7 ACs) |
| **Bolt** | [US-003.BOLT-001](../functional/bolts/US-003.BOLT-001-prompts-family.md) |
| **ADRs** | [ADR-001](../adrs/ADR-001-repository-layout-methodology-and-product.md) — rules 2, 5, 7: changes land in `distribution-kit/` only |
| **Risk Class** | medium |
| **Revision** | 1 |

---

## 1. Objective

Ship the `devflow/prompts/` family in the distributable kit: a standalone,
canonical folder where an adopting team **creates, modifies and improves**
its prompts with sequential `PROMPT-NNN-<description>.md` naming, shares
them through the repository and version-controls them with git. Prompts are
**living data**: the file body is copied and pasted into the agent as-is,
with no approval and no manifest. The four agent definitions learn that
project prompts belong in `devflow/prompts/`, never scattered in
`agents-data/`, and the §5.15 routing tables carry the family across
methodology upgrades.

If NOT implemented, project prompts keep being generated disorderly in
`agents-data/` with no shared, versioned home, and adopting teams have no
canonical place to build and reuse their prompt library.

The change lands **only** in `distribution-kit/` (ADR-001 rule 7); the root
`devflow/` — the installed rulebook governing this repository — is never
touched. The product `prompts/` tree of this repository is explicitly out of
scope.

---

## 2. Context

US-003 was approved on 2026-08-21 (2 SP) with the maintainer's clarified
intent: the family is standalone (no functional relation to other folders),
prompts are copy-paste living data, and numbering is correlative like the US
family. Today, prompts used with agents land in `agents-data/` (per-agent,
unorganized, not a shared library). The kit declares the canonical folder
structure (§5.12, G30), so a new family must be added to the kit's maps —
the folder tree, the §5.15 folder table and the §5.15 ID-less routing table —
for adopters to receive it and for migrations to carry it.

---

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| Feature US | `devflow/functional/user-stories/US-003-prompts-family.md` | HITL-US-Approval ✓ (2026-08-21T01:48:07-03:00) |
| Bolt | `devflow/functional/bolts/US-003.BOLT-001-prompts-family.md` | HITL-BOLT-READY-Approval ✓ (2026-08-21T01:50:07-03:00) |
| ADR | `devflow/adrs/ADR-001-repository-layout-methodology-and-product.md` | HITL-ADR-Approval ✓ |
| Repository baseline | `bfe585a` on branch `4.2` (working tree: US-003 + Bolt package + backlog drafts, uncommitted) | — |

Pre-SPEC evidence gate: **all sources approved** — no draft governed input.

---

## 4. Scope

### In scope

- **New family files** in the kit: `distribution-kit/devflow/prompts/` with
  `README.md`, `INDEX.md` and `TEMPLATE-PROMPT.md`.
- **Four agent definitions** (`CLAUDE.md`, `.agents/skills/avenga-devflow/SKILL.md`,
  `.github/agents/AvengaDevFlow.agent.md`, `.opencode/agents/AvengaDevFlow.md`):
  one identical sentence appended to the §5.12 working-data paragraph.
- **Methodology maps** in `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md`:
  §5.15 folder-table row for `prompts/`, §5.15 ID-less routing-table row
  (`Project prompt | prompts/ | PROMPT-NNN-<description>.md`), and the
  folder tree.
- **Folder map** in `distribution-kit/devflow/README.md` (tree + description).
- **Glossary** in `distribution-kit/devflow/ONBOARDING.md` (one entry).

### Out of scope

- The root `devflow/` tree (installed rulebook — frozen, ADR-001 rule 1).
- The product `prompts/` tree of this repository (untouched).
- Any approval, manifest or governance machinery for prompts (explicitly
  excluded by US-003 AC-5).
- Other kit families (roster US-001, sprints US-002) — separate USs.
- G-rule changes: G30 needs no amendment — the kit declaring the family
  makes it canonical.

---

## 5. Prerequisites and baseline

- `US-003.BOLT-001` approved (`HITL-BOLT-READY-Approval` recorded).
- Baseline commit `bfe585a`; the working tree holds the uncommitted US-003 /
  Bolt package and the backlog drafts.
- The four agent definitions are **in sync before the edit** (whole-body
  diff, ≤2 lines of sanctioned divergence). If a pre-existing drift is
  found, stop and reconcile first.

---

## 6. Phases

### Phase A — The family files (kit)

**Duration:** ~0.5h total cycle — **Complexity:** Low

#### A.1 `distribution-kit/devflow/prompts/README.md` (new)

Explains the family in the kit's standard README voice: what `prompts/` is
for (create, modify, improve project prompts), the copy-paste usage
convention, the naming rule `PROMPT-NNN-<description>.md` (sequential, like
the US family), the "living data" semantics (no approval, no manifest, no
INDEX-of-record beyond the folder's own INDEX), the rule that prompts never
go to `agents-data/`, and the language policy (prompt bodies follow the
project's `content_language`; names follow the schema rules).

#### A.2 `distribution-kit/devflow/prompts/INDEX.md` (new)

The family's INDEX: a table of `PROMPT-NNN` + short name + one-line purpose,
with the "next NNN is claimed here" note (§5.15 convention), starting empty.

#### A.3 `distribution-kit/devflow/prompts/TEMPLATE-PROMPT.md` (new)

The super-simple copy-paste template, exactly as approved in US-003:

```markdown
# PROMPT-NNN — [short name]

[optional one-line description: what this prompt is for]

[the prompt body — copy and paste into the agent as-is]
```

**Files created:**
- `distribution-kit/devflow/prompts/README.md`
- `distribution-kit/devflow/prompts/INDEX.md`
- `distribution-kit/devflow/prompts/TEMPLATE-PROMPT.md`

---

### Phase B — Four agent definitions (one synchronized pass)

**Duration:** ~0.5h total cycle — **Complexity:** Low

Append the identical sentence to the §5.12 working-data paragraph in the
four agent definitions (the paragraph that today describes `agents-data/`):

> Project prompts live in `devflow/prompts/` (`PROMPT-NNN-<description>.md`):
> versioned, team-shared, copy-paste ready. Create, modify or improve them
> there on request; never leave prompts scattered in `agents-data/`.
> Prompts carry no approval and no manifest.

The sentence is byte-identical across the four; the `agents-data/<agent>/`
path line stays the single sanctioned divergence.

**Files modified:**
- `distribution-kit/CLAUDE.md`
- `distribution-kit/.agents/skills/avenga-devflow/SKILL.md`
- `distribution-kit/.github/agents/AvengaDevFlow.agent.md`
- `distribution-kit/.opencode/agents/AvengaDevFlow.md`

---

### Phase C — Methodology maps and onboarding

**Duration:** ~0.5h total cycle — **Complexity:** Low

#### C.1 `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md`

- **§5.15 folder table** (next to the `agents-data/` row, ~line 4319): new
  row `| prompts/ | Project prompts (PROMPT-NNN-<description>.md) — versioned,
  team-shared, copy-paste ready; living data with no approval and no
  manifest; never scattered into agents-data (see §5.12). |`
- **§5.15 ID-less routing table** (next to `Sprint report | reports/ | …`,
  ~line 4367): new row `| Project prompt | prompts/ | PROMPT-NNN-<description>.md |`.
- **Folder tree** (~lines 4074–4085): add a `prompts/` line next to
  `agents-data/`.

#### C.2 `distribution-kit/devflow/README.md`

- Folder tree (next to `agents-data/`, ~line 70): add
  `├── prompts/            ← Project prompts (PROMPT-NNN, copy-paste ready)`.
- Folder description table: one row for `prompts/` (same semantics as the
  §5.15 row).

#### C.3 `distribution-kit/devflow/ONBOARDING.md`

- Glossary (next to the `agents-data/` entry, ~line 76): one entry for
  `prompts/` with the copy-paste convention and the no-approval semantics.

**Files modified:**
- `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md`
- `distribution-kit/devflow/README.md`
- `distribution-kit/devflow/ONBOARDING.md`

---

### Phase D — Verification suite (deterministic checks)

**Duration:** ~0.5h total cycle — **Complexity:** Low

Run and record the full verification set (§8) and capture the output in the
MEM.

---

## 7. Acceptance criteria

### AC-1: Family files present in the kit

**Given** the edited kit,
**When** checking `distribution-kit/devflow/prompts/`,
**Then** `README.md`, `INDEX.md` and `TEMPLATE-PROMPT.md` exist and the
template matches the approved shape (title + optional one-liner + body).

### AC-2: Naming convention documented

**Given** the README and INDEX of the family,
**When** read,
**Then** they document `PROMPT-NNN-<description>.md` sequential numbering
and the "next NNN is claimed here" convention.

### AC-3: Living-data semantics

**Given** the family documentation,
**When** searched for approval/manifest requirements,
**Then** none exist — prompts are copy-paste living data (no
`HITL-*` checkpoint, no manifest reference anywhere in the family files).

### AC-4: Four-agent sentence present and identical

**Given** the four agent definitions,
**When** grepping for "Project prompts live in `devflow/prompts/`",
**Then** exactly 1 match per file, byte-identical across the four, and the
whole-body sync diff stays at 2 lines per comparison.

### AC-5: §5.15 and maps carry the family

**Given** the edited methodology, README and ONBOARDING,
**When** grepping for `prompts/`,
**Then** the §5.15 folder-table row, the §5.15 routing-table row, the
folder tree line and the ONBOARDING glossary entry are present.

### AC-6: No scatter into agents-data

**Given** the edited kit,
**When** grepping the new family files and agent sentences for
`agents-data`,
**Then** the only mentions are the explicit prohibition ("never leave
prompts scattered in `agents-data/`") — prompts are never routed there.

### AC-7: Root devflow untouched + manifest valid

**Given** the completed V-Bounce,
**When** running `git status` and the manifest validation,
**Then** no root `devflow/` methodology content is modified, and the Bolt
manifest validates with 0 errors.

### AC mapping to source (functional)

| Source AC (US-003) | How this SPEC satisfies it | Verifying test/evidence |
|---------------------|----------------------------|--------------------------|
| AC-1 — family with template, README, INDEX | Phase A creates the three files | AC-1 |
| AC-2 — `PROMPT-NNN-<description>.md` naming | README/INDEX document the convention | AC-2 |
| AC-3 — modified/improved prompts land back in the folder | README states the rule; agents' sentence forbids `agents-data/` | AC-4, AC-6 |
| AC-4 — shared and versioned through the repository | Family files are committed kit content | AC-1, AC-7 |
| AC-5 — copy-paste, no approval/manifest | TEMPLATE shape + README semantics; no machinery added | AC-3 |
| AC-6 — agents point at `devflow/prompts/` (4-file sync) | Phase B sentence, byte-identical | AC-4 |
| AC-7 — migration carries the family (§5.15) | Phase C rows | AC-5 |

---

## 8. Testing strategy

No runtime exists — verification is the deterministic command set:

- **File presence (AC-1):** `Test-Path` the three family files; compare the
  template body against the approved shape.
- **Grep checks (AC-2..AC-6):** naming convention, absence of
  approval/manifest machinery, sentence presence 4×, `prompts/` rows in the
  three maps, `agents-data` mentions limited to the prohibition.
- **Sync diff (AC-4):** the four-agent whole-body diff (expected: 2 lines
  per comparison) and the G-rule count check (39/39/39/39, unaffected).
- **Root-untouched + manifest (AC-7):** `git status --short` and
  `ConvertFrom-Json` + schema check.
- **Edge cases:** LF/CRLF normalization (`tr -d '\r'`) before the sync
  diff; the template's inline backticks; table-row pipe escaping in the
  §5.15 additions.
- **BUG evidence:** n/a — not a BUG Bolt.

---

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | — | `n/a` — documentation-only change, no executable code |
| SAST / SBOM | — | `n/a` — no code, no dependencies |
| Perf-smoke (p95/p99) | — | `n/a` — no runtime |
| Prompt-injection scan | — | `pass` — all text authored here |
| Secret-leak scan | — | `pass` |
| Hallucination lint | — | `pass` — every §-reference and path resolves on disk (§5.12, §5.15, G30, US-003, ADR-001) |
| IP / license provenance | — | `n/a` — no third-party content |
| PII / DLP | — | `n/a` — `internal`, no personal data |
| Dependency-confusion | — | `n/a` — no dependencies |
| Test-first evidence | — | `n/a` — not a BUG Bolt |
| Behavioral reproducibility | — | `pass` — deterministic grep/diff/count checks, idempotent |
| Bolt-manifest validation | — | `pass` — 0 errors against `manifest-v4-bolt.schema.json` |

---

## 10. Security and data

- No security boundary, credentials, runtime surface or data path touched.
  Prompts are markdown text; the family adds no execution surface.
- Data classification: `internal` — documentation text only.

---

## 11. Monitoring and observability

`n/a` — no runtime, no logs, no metrics. The verification suite (§8) is the
observability; its output is captured in the MEM.

---

## 12. Migration, compatibility and rollback

- **Migration:** none in this repository — the change lands in
  `distribution-kit/` and reaches adopting projects through their own §5.16
  release migration; the §5.15 rows added here are what make the family
  travel.
- **Compatibility:** no schema, G-rule count or checkpoint vocabulary
  changes; the four-agent sync invariant is preserved (still 2 lines).
- **Rollback:** revert the kit commit(s); the root tree is untouched and
  keeps governing unchanged.

---

## 13. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| 4-agent text drift | 2 | 3 | Phase B identical sentence; AC-4 sync diff mandatory |
| A map location missed (tree, §5.15, README, ONBOARDING) | 2 | 3 | §4 inventory; AC-5 greps each location |
| Ambiguity with the product `prompts/` tree | 2 | 2 | Explicit scope wording in README and SPEC |
| Users expect approval/manifest for prompts | 2 | 2 | README states living-data semantics; AC-3 asserts none |
| Root `devflow/` accidentally modified | 1 | 4 | Phases restrict edits to `distribution-kit/`; AC-7 |

---

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| Family is standalone living data (no approval, no manifest) | Maintainer's explicit intent (US-003 AC-5): prompts are copy-paste files; git is the version control |
| Sequential `PROMPT-NNN-<description>.md` naming like US | Maintainer's explicit intent; volume is small |
| Sentence appended to the §5.12 working-data paragraph in the agents | Same place agents already learn about `agents-data/` — the contrast ("prompts go here, not there") sits beside the rule it corrects; one sentence keeps the sync trivial |
| §5.15 rows added so the family travels on migration | Without them, adopters would receive the folder but migrations would not carry its files by family (§5.15 routing is where ID-less families are placed) |
| Product `prompts/` tree untouched | ADR-001 rules 2/5/7 and US-003's explicit scope boundary |
| No G-rule change | G30 is satisfied by the kit declaring the family canonical — no amendment needed |

---

## 15. Stop conditions

- Any root `devflow/` methodology file is modified → stop, revert, record in
  the MEM.
- Pre-existing 4-agent drift before Phase B (sync diff > 2 lines) → stop,
  reconcile first.
- Any map location for `prompts/` is missing after Phase C and AC-5 fails →
  stop, complete the sweep; never assume it.
- A governed source changes materially during execution (G15) → stop,
  revise this SPEC, re-approve.

---

## 16. Definition of Done (DoD)

- [ ] All phases (A–D) implemented
- [ ] All acceptance criteria (AC-1..AC-7) pass
- [ ] Verification suite GREEN (file presence, greps, sync diff 2 lines, G-count 39/39/39/39, root untouched, manifest 0 errors)
- [ ] Change follows ADR-001 (kit-only) and the approved Bolt
- [ ] Applicable gates pass / waived (ADR) / n/a (reason) — §9
- [ ] MEM created in `devflow/memory/` (exactly one per V-Bounce)
- [ ] Manifest `v_bounces[]` entry appended in `devflow/metrics/bolts/`
- [ ] HITL-MEM-Approval recorded

---

## 17. References

- `devflow/functional/user-stories/US-003-prompts-family.md` (approved US — the intent)
- `devflow/functional/bolts/US-003.BOLT-001-prompts-family.md` (approved Bolt — the WHAT)
- `devflow/adrs/ADR-001-repository-layout-methodology-and-product.md` (rules 1, 2, 5, 7)
- AGENTS.md — four-agent maintenance rules and sync-diff command

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
| **review_ready_at** | `2026-08-21T01:50:07-03:00` |
| **review.started_at** | `2026-08-21T01:52:12-03:00` |
| **review.decided_at** | `2026-08-21T01:52:12-03:00` |
| **Findings** | None — acknowledged_without_comment (reason in frontmatter `review:` block) |
