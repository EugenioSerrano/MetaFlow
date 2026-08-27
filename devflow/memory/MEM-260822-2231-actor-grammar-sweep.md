---
id: "MEM-260822-2231"
title: "Apply ADR-010 actor record grammar to the v5.0 kit (user→actor sweep, grammar only) — F-01…F-05, F-08 closed"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
bolt: "US-000.BOLT-008"
spec: "SPEC-260822-2120"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "488f95d"
applied_adrs:
  - "devflow/adrs/ADR-010-actor-grammar-and-pure-v5-vocabulary.md"
  - "devflow/adrs/ADR-005-removal-completeness-phrase-family-sweep.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "US-000.BOLT-008-adr009-actor-identity-grammar-sweep.json"
diff_ref: ""
review_ready_at: "2026-08-22T22:31:08-03:00"
review: # HITL-MEM-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers:
    - user: "eugenio.serrano"
      role: "dev_validator"
  started_at: "2026-08-22T22:33:11-03:00"
  decided_at: "2026-08-22T22:33:11-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved. V-Bounce GREEN: all SPEC §11 checks pass — 5/5 example manifests validate against the reshaped v5 schemas (incl. the agent-path example: developer-agent executes, qa-agent approves virtually), zero [{user, role}] / bare created_by / mode / hitlSubject / ADR-007-008 residue in the kit, four-agent parity (2-line diff each) + G-count 39×5, and git scope is distribution-kit/ + root governance records only (ADR-004). The deliberate transient (enum untouched + §5.16 'HITL preserved verbatim' left for BOLT-009) is correct — grammar swept, vocabulary purge is the sibling Bolt. Grammar-only scope (ADR-010 §3.1–§3.5) faithfully delivered."
---

<!--
  LANGUAGE POLICY (§3.15): schema in English; prose content_language (en).
  DOGFOODING SPLIT (ADR-004/006): this MEM is a v4.2 governance record (HITL-* own
  checkpoints, manifest schema_version 4.0) of a V-Bounce that edited the v5.0
  PRODUCT (distribution-kit/, AITL-* vocabulary, manifest family v5). Baseline 488f95d.

  ⚠️ MEM created before human review (§3.3 step 4) so the reviewer receives the
  complete package: diff + verification evidence + MEM + manifest. Pending
  HITL-MEM-Approval.
-->

# MEM-260822-2231 — ADR-010 actor record grammar sweep (V-Bounce 1)

| Field | Value |
|-------|-------|
| **Bolt** | US-000.BOLT-008 (non-functional, US-000) |
| **SPEC** | SPEC-260822-2120 rev 1 (approved, HITL-SPEC-Approval 2026-08-22T22:09:55) |
| **V-Bounce** | 1 · `execution_outcome: ready_for_review` |
| **Governing** | ADR-010 §3.1–§3.5 (grammar), REV-003 (approved inventory), ADR-005 (sweep discipline), ADR-004 (kit-only) |
| **Baseline** | `488f95d` |

---

## 1. Executive summary

This V-Bounce applied ADR-010's **actor record grammar** across the entire v5.0
kit (`distribution-kit/`) in one allowlist-aware pass, closing REV-003 findings
F-01…F-05 and F-08. Every place the kit recorded an identity now uses one
grammar — `human:<user>` | `agent:<id>` — prefix-mandatory in machine records and
review/enforcement fields, bare-as-human shorthand in descriptive frontmatter.
The three v5 manifest schemas were reshaped (`created_by` gains the actor
pattern, `runs[]` gains a nullable `agent`, `checkpointApproval` drops the derived
`mode`, `$defs.hitlSubject` → `checkpointSubject`); the review contract in the
methodology, GUARDRAILS and 14 template blocks became `reviewers: [{actor, role,
model}]`, turning the artifact↔manifest projection into a field-for-field copy;
and the kit's dangling maintainer-repo ADR citations (ADR-007/ADR-008) were
replaced by the §3.0 anchor. The five example manifests — including a new
agent-path example (developer-agent executes, qa-agent approves) — validate
against the reshaped schemas. The **vocabulary purge** (dropping `HITL-*` from the
`checkpoint` enum + the §5.16 name-rewrite, ADR-010 §3.6–§3.7) was deliberately
left to the sibling Bolt US-000.BOLT-009; this Bolt leaves the enum untouched, so
the kit is internally consistent at this stage (grammar swept, vocabulary purge
pending). Result: **GREEN** — all SPEC §11 acceptance checks pass.

## 2. What was implemented and why

The v5 kit recorded identity in three inconsistent grammars (REV-003 F-01): only
`checkpoint_approvals[].decided_by[]` was actor-shaped; the review contract was
`{user, role}`; `created_by` and ~35 frontmatter fields were bare-human. That
split made a virtual approval (permitted by ADR-008) **unrecordable** on the
artifact side and made a generation **unattributable** to a specific agent
(F-02). ADR-010 fixes the grammar; this Bolt is its mechanical application. Done
pre-release so the reshape folds into the not-yet-shipped v5 family at zero
migration cost (REV-003 F-07).

## 3. Files changed (with reason)

**Machine contract — the 3 v5 schemas** (`distribution-kit/devflow/metrics/`):
- `manifest-v5-bolt.schema.json`, `manifest-v5-us.schema.json`,
  `manifest-v5-tc.schema.json` — `$defs.generation.created_by` gains
  `pattern: ^(human|agent):.+` (F-02); `$defs.run` gains a required, nullable
  `agent` (F-02); `$defs.checkpointApproval` drops the `mode` property, its
  `required` entry, and the mode if/then/else conditional (F-04, now derived from
  the actor prefix); (bolt only) `$defs.hitlSubject` → `$defs.checkpointSubject`
  and its `$ref` (F-05). The `checkpoint` enum is **untouched** (BOLT-009).

**Machine contract — the 5 example manifests** (`metrics/TEMPLATE-MANIFEST-*.json`):
- all `created_by` values prefixed `human:`; every `runs[]` entry gains
  `agent: null`; every `checkpoint_approvals[]` entry drops `mode`. In
  `TEMPLATE-MANIFEST-BOLT.json`, one V-Bounce was converted to an **agent path**
  (`code_generation`/`mem.generation` `created_by: agent:developer-agent`,
  `runs[].agent: developer-agent`) and its MEM approval to a **virtual approval**
  (`decided_by: agent:qa-agent`, `model: claude-opus-5`) — proving the reshape
  admits both an agent-attributed generation and a virtual approval, with the
  approver actor ≠ the executor actor.

**Methodology** (`avenga-devflow/Avenga-DevFlow.md`):
- §3.0 — the review-contract example became `{actor, role, model}`; the canonical
  identity paragraph now defines the two namespaces + the two strictness tiers +
  the bare=human normalization rule; the projection paragraph states it is a copy
  and that virtual is derived (no `mode`).
- §3.3 — the `risk_history` example `decided_by` became actor-shaped.
- §3.12 — the embedded example manifest transformed (validated against the
  reshaped bolt schema); the `mode` sentence removed (derived, G39); `created_by`
  reworded to "the actor"; `runs[].agent` documented; the `schema_version` note
  no longer cites `mode`.
- §5.16 — the `4.0`→`5.0` conversion gains the grammar rows (`created_by` →
  `human:`, `runs[]` gains `agent: null`); the reconstruction table's
  `created_by`/`checkpoint_approvals` rows updated. The "`HITL-*` names preserved
  verbatim" sentence was **left in place** for BOLT-009 (its name-rewrite reversal
  travels with the enum purge, keeping text and schema consistent at each stage).

**GUARDRAILS.md** — the review-contract YAML → `{actor, role, model}`; the
projection block → a copy + derived-virtual note; W11 field list updated.

**Templates** — 14 `reviewers: [] # [{user, role}]` comments → `# [{actor, role,
model}]`; ~30 frontmatter identity comments (`author:`/`owner:`/`validator:`/
`closed_by:`/`facilitator:`) + 3 approver-identity table cells note the actor
grammar (bare = human, agent always prefixed).

**Four agents** (`CLAUDE.md`, `.agents/…/SKILL.md`, `.github/…agent.md`,
`.opencode/…md`) — identical shared-body edits: `created_by` line, the
`checkpoint_approvals[]` summary (mode dropped, derived note), the §5.16 mapping
(mode dropped, created_by/runs added), and F-08 (G18's `(ADR-008 §3.2–§3.4)` →
`(§3.0)`; the manifest summary's `(AITL, §3.0/ADR-008)` → `(AITL, §3.0)`).

**F-08 elsewhere** — `AGENTS.md` (kit), the methodology charter §0/§1/§3.0 (the
`(ADR-007, ADR-008)` provenance citations dropped, `(§3.0)` anchor kept),
GUARDRAILS G18/G24 + checkpoint map, and one illustrative `spec/README.md`
example (→ "an approved ADR"). Net: **zero** `ADR-007`/`ADR-008` in the kit.

## 4. Verification evidence (SPEC §11 — all GREEN)

| # | Check (over `distribution-kit/`) | Result |
|---|----------------------------------|--------|
| 1 | `[{user, role}]` review-block residue | **0** (the one `{user, role}` left is the §5.16 conversion *source-shape* description) |
| 2 | bare (unprefixed) `created_by` in `metrics/*.json` | **0** |
| 3 | `mode` in `metrics/` (schemas + examples) | **0** |
| 4 | `hitlSubject` | **0** |
| 5 | `ADR-007`/`ADR-008` cited in the kit (F-08) | **0** |
| 6 | 5 `TEMPLATE-MANIFEST-*.json` validate vs reshaped schemas (Draft 2020-12 + format) | **all 5 VALID**, incl. the agent-path example |
| 7 | `checkpoint` enum untouched (BOLT-009's scope) | both `HITL-*`+`AITL-*` still present (consistent with un-purged enum) |
| 8 | four-agent shared-body parity + G-count | **2-line diff each** (the sanctioned `agents-data/<agent>` path) · **39/39 ×5** |
| 9 | `git status` scope | `distribution-kit/` (48 files) + root governance records only (INDEXes + this session's ADR/REV/Bolt/SPEC/manifest); root `devflow/` methodology content untouched (ADR-004) |

## 5. Decisions and deviations

- **Enum left untouched, `HITL-*`-preserved sentence left in §5.16 + agents:**
  deliberate, to keep the split clean — BOLT-009 flips the §5.16 name-rewrite
  text and purges the enum together, so text and schema stay consistent at each
  stage. Transient state after this Bolt: grammar is actor-shaped everywhere; the
  enum still accepts both vocabularies (matches the un-rewritten §5.16 text).
- **Agent-path example:** converted an existing V-Bounce rather than adding a new
  one, keeping the example minimal while proving the agent generation + virtual
  approval shapes. The human default is retained elsewhere in the same file.
- **Schemas edited by targeted string edits** (not a reformatting load→dump) to
  keep the diff reviewable; examples + the §3.12 embedded block edited by a
  transform script (canonical JSON, format preserved).
- **F-08 charter citations dropped rather than re-pointed to a section:** the
  charter *is* §3.0, so a self-citation added nothing; the rule is stated inline.

## 6. Risks / follow-ups

- **US-000.BOLT-009 (candidate)** must run next: purge `HITL-*` from the enum +
  rewrite §5.16 names (ADR-010 §3.6–§3.7), with a v4→v5 migration round-trip test.
  Until it lands, the §5.16 "preserved verbatim" wording is a known, intended
  transient that BOLT-009 resolves.
- No consumer of `mode` exists (kit `metrics/bolts/` empty; family shipped days
  ago), so dropping it is safe (SPEC §13 assumption held).

## 7. Manual interventions

None. Fully agent-generated under L3; the human steered via the approved SPEC and
the ADR decisions. Version-control actions deferred to the user (G34).

## 8. HITL-MEM-Approval

> The V-Bounce is complete and GREEN, but not **approved** until the executing
> Dev-validator records `HITL-MEM-Approval` after inspecting the diff + the §11
> verification evidence + this MEM + the manifest entry (§3.3). Pending.

| Field | Value |
|-------|-------|
| **Reviewer** | eugenio.serrano (dev_validator, executing) |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-22T22:31:08-03:00` |
| **review.started_at** | `2026-08-22T22:33:11-03:00` |
| **review.decided_at** | `2026-08-22T22:33:11-03:00` |
