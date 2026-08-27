---
id: "MEM-260821-0153"
title: "Prompts family shipped in the kit: devflow/prompts/ + four-agent sentence + §5.15 maps"
date: "2026-08-21"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
bolt: "US-003.BOLT-001"
spec: "SPEC-260821-0150"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "bfe585a"
applied_adrs:
  - "devflow/adrs/ADR-001-repository-layout-methodology-and-product.md"
manifest: "US-003.BOLT-001-prompts-family.json"
diff_ref: ""
review_ready_at: "2026-08-21T01:53:56-03:00"
review: # HITL-MEM-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers:
    - user: "eugenio.serrano"
      role: "dev_validator"
  started_at: "2026-08-21T01:55:04-03:00"
  decided_at: "2026-08-21T01:55:04-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Inspected the package: the diff of the 10 kit files (3 new family files with the approved template shape, the 4-agent identical sentence, the 3 map updates), the §9 verification output (file presence, naming greps, zero approval/manifest machinery, sentence byte-identical 4x, sync diff 2/2/2, root devflow untouched), the MEM narrative and the manifest v_bounces[1] entry. Matches US-003 ACs and SPEC revision 1. No findings."
---

# MEM-260821-0153 — Prompts family shipped in the kit: devflow/prompts/ + four-agent sentence + §5.15 maps

| Field           | Value |
|-----------------|-------|
| **Bolt**        | [US-003.BOLT-001](../functional/bolts/US-003.BOLT-001-prompts-family.md) |
| **SPEC**        | [SPEC-260821-0150](../spec/SPEC-260821-0150-prompts-family.md), **revision 1** |
| **V-Bounce**    | 1 |
| **ADRs**        | [ADR-001](../adrs/ADR-001-repository-layout-methodology-and-product.md) — rules 1, 2, 5, 7 (kit-only edits, root frozen) |

---

## 1. Executive summary

This V-Bounce shipped the `devflow/prompts/` family into the distributable
kit: a standalone, canonical folder where adopting teams create, modify and
improve their project prompts with sequential `PROMPT-NNN-<description>.md`
naming, share them through the repository and version-control them with git.
The family is **living data by design** — the prompt body is copied and
pasted into the agent as-is, with no approval and no manifest, exactly as
US-003's AC-5 requires. Three artifacts were created in the kit
(`README.md` with the copy-paste convention, `INDEX.md` with the "next NNN
is claimed here" rule, and the super-simple `TEMPLATE-PROMPT.md`), the four
agent definitions each received one byte-identical sentence in their §5.12
working-data paragraph — placing the contrast "prompts go to
`devflow/prompts/`, never `agents-data/`" beside the rule it corrects — and
the methodology maps (folder tree, §5.15 folder table, §5.15 ID-less routing
table, `devflow/README.md` tree, ONBOARDING glossary) all gained the
`prompts/` row so the family travels with §5.16 migrations. All seven
acceptance criteria pass: family files present with the approved template
shape, naming documented, zero approval/manifest machinery (only the
negations), the sentence present and byte-identical in exactly four agents,
the whole-body sync diff still at 2 sanctioned lines, every map carrying the
family, and the root `devflow/` untouched. No deviations from SPEC revision
1; no surprises.

---

## 2. Implemented phases

### Phase A — The family files (kit)

Created `distribution-kit/devflow/prompts/` with three files. The README
states the family's purpose (create/modify/improve prompts), the copy-paste
usage convention, the `PROMPT-NNN-<description>.md` naming rule, the living
data semantics (no approval — no HITL checkpoint applies; no manifest — not
part of the manifest family; versioned by git; shared with the team), the
prohibition on scattering prompts in `agents-data/`, and the language policy
for prompt bodies. The INDEX documents the "next free NNN is claimed here"
convention with an empty table. The TEMPLATE-PROMPT is the approved
super-simple shape: title + optional one-line description + prompt body —
nothing else.

### Phase B — Four agent definitions (one synchronized pass)

Appended the identical sentence to the §5.12 working-data paragraph in
`CLAUDE.md`, `SKILL.md`, `AvengaDevFlow.agent.md` and `AvengaDevFlow.md`:
*"Project prompts live in `devflow/prompts/` (`PROMPT-NNN-<description>.md`):
versioned, team-shared, copy-paste ready. Create, modify or improve them
there on request; never leave prompts scattered in `agents-data/`. Prompts
carry no approval and no manifest."* Verified byte-identical (258 chars)
across the four; the whole-body sync diff stays at exactly 2 lines per
comparison (the sanctioned `agents-data/<agent>/` path).

### Phase C — Methodology maps and onboarding

Added the `prompts/` row to four locations so the family is canonical and
travels on migration: the §5.15 folder table (next to `agents-data/`), the
§5.15 ID-less routing table (`Project prompt | prompts/ |
PROMPT-NNN-<description>.md`), the folder tree in the kit methodology, the
`devflow/README.md` folder tree, and the ONBOARDING glossary entry. No
G-rule changes — G30 is satisfied because the kit declares the family.

### Phase D — Verification suite

Executed the deterministic checks: family file presence, naming-documentation
greps, approval/manifest-absence greps (only the negations), the
four-agent sentence presence ×4 and byte-identity, the whole-body sync diff
(2/2/2), the map greps (methodology 2/2, README 1, ONBOARDING 1), `git
status` (no root `devflow/` methodology content modified) and the Bolt
manifest JSON validation (0 errors, 3 approvals recorded). All output in §9.

---

## 3. Files created

| File | Purpose |
|------|---------|
| `distribution-kit/devflow/prompts/README.md` | Family guide: purpose, copy-paste convention, `PROMPT-NNN` naming, living-data semantics (no approval/manifest), no-`agents-data` rule, language policy |
| `distribution-kit/devflow/prompts/INDEX.md` | Family INDEX with the "next free NNN is claimed here" convention (§5.15) |
| `distribution-kit/devflow/prompts/TEMPLATE-PROMPT.md` | The approved super-simple prompt template: title + optional one-liner + body, copy-paste ready |
| `devflow/memory/MEM-260821-0153-prompts-family.md` | This implementation memory — the V-Bounce 1 record |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `distribution-kit/CLAUDE.md` | §5.12 working-data paragraph: appended the identical prompts sentence |
| `distribution-kit/.agents/skills/avenga-devflow/SKILL.md` | Same sentence, verbatim |
| `distribution-kit/.github/agents/AvengaDevFlow.agent.md` | Same sentence, verbatim |
| `distribution-kit/.opencode/agents/AvengaDevFlow.md` | Same sentence, verbatim |
| `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md` | §5.15 folder-table row, §5.15 routing-table row, folder-tree line for `prompts/` |
| `distribution-kit/devflow/README.md` | Folder tree line for `prompts/` |
| `distribution-kit/devflow/ONBOARDING.md` | Glossary entry for `prompts/` |

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
| Family files carry no frontmatter and no manifest | US-003 AC-5: prompts are copy-paste living data; git is the version control |
| Sentence appended to the existing §5.12 paragraph rather than a new section | Places the contrast beside the rule it corrects; a single sentence keeps the four-agent sync trivial (still 2 diff lines) |
| `PROMPT-NNN-<description>.md` sequential naming with INDEX claiming | Matches the US-family convention the maintainer requested; the §5.15 convention for sequential IDs |
| §5.15 rows added in the same V-Bounce as the folder | Without the routing rows the family would not travel on §5.16 migrations — the family and its placement are one deliverable |
| No G-rule or schema changes | G30 is satisfied by the kit declaring the family; nothing else needs amending |
| Product `prompts/` tree untouched | ADR-001 rules 2/5/7 and US-003's explicit scope boundary |

---

## 8. Deviations and assumptions

**No deviations from SPEC revision 1.** Every phase landed as specified and
all seven ACs pass.

**Assumption:** prompt bodies may contain any content the team needs
(including agent instructions in any language), subject to the language
policy; nothing in the family executes code or requires runtime support.

**Observation:** the first prompt committed by an adopter will claim
`PROMPT-001` in the family INDEX; the INDEX ships empty by design.

**No unresolved risks** carried out of this V-Bounce.

---

## 9. Verification evidence

### Build

```
n/a — no runtime and no build. Verification is the deterministic command set below.
```

### Tests

```
AC-1   family files exist ......................... README.md ✓ INDEX.md ✓ TEMPLATE-PROMPT.md ✓
       template shape = title + optional one-liner + body ............. PASS
AC-2   PROMPT-NNN naming documented ............... 4 mentions in family docs         PASS
AC-3   approval/manifest machinery ................ only the negations ("No approval",
       "No manifest", "no approval, no manifest") ....................... PASS
AC-4   "Project prompts live in" sentence ......... exactly 4 files
       byte-identical (258 chars ×4) .............. PASS
       whole-body sync diff ....................... codex 2 | gh 2 | opencode 2       PASS
       G-rule count (unchanged) ................... 39/39/39/39                        PASS
AC-5   methodology routing row .................... 1 ("Project prompt")
       methodology folder-table row ............... 1 ("Project prompts (PROMPT-NNN…")
       methodology PROMPT-NNN mentions ............ 2
       README prompts/ line ....................... 1
       ONBOARDING prompts/ entry .................. 1                                  PASS
AC-6   agents-data mentions in family files ....... 2 — both the prohibition
       ("never scattered in agents-data") ............................... PASS
AC-7   git status: no root devflow/ methodology content modified —
       only governance records and kit files ........................... PASS
       Bolt manifest valid, approvals = 3 (US, BOLT-READY, SPEC) ........ PASS
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
| Hallucination lint | `pass` — §5.12, §5.15, §5.16, G30, US-003, ADR-001 all resolve on disk |
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
- **Commit:** baseline `bfe585a` on branch `4.2`, plus the uncommitted working tree
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-003.BOLT-001-prompts-family.json`

---

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~8 min (01:52 → 01:53 local), including the SPEC-approval recording |
| V-Bounce number | 1 |
| Tests created | n/a — 7 acceptance criteria, ~12 deterministic checks + the 4-agent sync diff |
| AI-generated code | 100% — no human fallback |
| First-pass approval | pending — package submitted for HITL-MEM-Approval |

---

## 13. Pending items and stubs

- [ ] `HITL-BOLT-DONE-Approval` — after MEM approval (routes to PO/PM per `feature`; the maintainer signs)
- [ ] Backlog drafts US-001, US-002, US-004..US-013 remain open for future refinement
- [ ] The uncommitted backlog + Bolt-002-package + this V-Bounce — pending the user's commit instruction

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
| **review_ready_at** | `2026-08-21T01:53:56-03:00` |
| **review.started_at** | `2026-08-21T01:55:04-03:00` |
| **review.decided_at** | `2026-08-21T01:55:04-03:00` |
| **Review evidence** | Diff of the 10 kit files (3 new family files + 4 agents + 3 maps), the §9 verification output (file presence, greps, sync diff, sentence identity, git status), the manifest `v_bounces[]` entry, and the SPEC/US references |
| **Comments** | None — package approved as submitted |
| **Findings** | none |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | recorded in the frontmatter `review:` block |
