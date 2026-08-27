---
id: "SPEC-260822-2120"
title: "Apply the ADR-010 actor record grammar across the v5.0 kit (user→actor sweep — grammar only)"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
status: "approved" # draft | approved | blocked | obsolete
origin: "ADR-010"
bolt: "US-000.BOLT-008"
revision: 1
associated_adrs:
  - "devflow/adrs/ADR-010-actor-grammar-and-pure-v5-vocabulary.md"
  - "devflow/adrs/ADR-005-removal-completeness-phrase-family-sweep.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
prerequisites: []
risk_class: "medium"
autonomy_level: "L3"
turn_budget: "12"
data_classification: "internal"
review_ready_at: "2026-08-22T22:05:50-03:00" # resubmitted after the ADR-009→ADR-010 re-point + grammar-only rescope (still revision 1, never reviewed)
review: # HITL-SPEC-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers:
    - user: "eugenio.serrano"
      role: "dev_validator"
    - user: "eugenio.serrano"
      role: "tech_lead"
  started_at: "2026-08-22T22:09:55-03:00"
  decided_at: "2026-08-22T22:09:55-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved. Grammar-only sweep against ADR-010 §3.1–§3.5 (the enum purge is BOLT-009). Field shapes verified against the real $defs (created_by pattern, runs[].agent, drop mode, hitlSubject→checkpointSubject; enum untouched). The §6 agent-path example (agent:qa-agent approval + runs[].agent) is accepted as proof-of-shape. Verification = ADR-005 zone-scoped absence sweep + 5-example schema validation + four-agent parity (§11). Dev-validator + Tech Lead (schema + charter edits). V-Bounce authorized."
---

<!--
  LANGUAGE POLICY (§3.15): schema in English; prose content_language (en).
  DOGFOODING SPLIT (ADR-004/006): this SPEC is authored under the v4.2 operating
  methodology, so its own checkpoints are HITL-*. It edits the v5.0 PRODUCT
  (distribution-kit/), whose canonical vocabulary is AITL-* and whose manifest
  family is v5. Baseline: 488f95d.

  ⚠️ DRAFT until HITL-SPEC-Approval (Dev-validator + Tech Lead). No file in
  distribution-kit/ is edited before that checkpoint is recorded (G14).
-->

# SPEC-260822-2120 — ADR-010 actor record grammar sweep (grammar only)

| Field | Value |
|-------|-------|
| **Origin** | [ADR-010](../adrs/ADR-010-actor-grammar-and-pure-v5-vocabulary.md) (accepted; supersedes ADR-009) |
| **Bolt** | [US-000.BOLT-008](../functional/bolts/US-000.BOLT-008-adr009-actor-identity-grammar-sweep.md) (approved, HITL-BOLT-READY-Approval re-affirmed 2026-08-22T21:54:53-03:00) |
| **Inventory** | [REV-003](../reviews/REV-003-user-to-actor-identity-vocabulary.md) (approved) — F-01…F-05, F-08 |
| **ADRs** | ADR-010 §3.1–§3.5 (target grammar), ADR-005 (sweep discipline + absence proof), ADR-004 (kit-only) |
| **Risk / Autonomy / Revision / turn_budget** | medium · L3 · 1 · 12 |
| **Baseline** | `488f95d` (distribution-kit/ working tree) |
| **Sibling** | The vocabulary purge (ADR-010 §3.6–§3.7: enum → `AITL-*` only + §5.16 name-rewrite) is **US-000.BOLT-009**, run after this Bolt — **out of scope here** |

---

## 1. Objective

Apply ADR-010's actor record **grammar** (§3.1–§3.5) to `distribution-kit/` in one
allowlist-aware pass, so every recorded identity uses `human:<user>` | `agent:<id>` and
the artifact↔manifest review projection becomes a field-for-field copy. Every change
is **mechanical application of an accepted decision** — no new judgment. Closes
REV-003 F-01…F-05 and F-08. The **vocabulary purge** (ADR-010 §3.6–§3.7: dropping
`HITL-*` from the checkpoint enum + the §5.16 name-rewrite) is the sibling Bolt
US-000.BOLT-009, run after this one — **out of scope here**. Pre-release window
(REV-003 F-07): the reshape folds into the not-yet-shipped v5 family at zero migration cost.

## 2. Context (why, and what breaks if not done)

- ADR-007 fixed "the actor is the unit of identity"; ADR-010 (superseding ADR-009)
  supplies the record syntax it deferred. Until this lands, a **virtual approval
  permitted by ADR-008 cannot be written on the artifact** (`reviewers[].user` has no
  agent form), so the §3.0 projection-mismatch rule makes every valid virtual approval a
  validation error — the flagship capability is unrecordable. And a generation cannot be
  attributed to an agent (`runs[]` records the model, not the actor).
- This is the last foundation piece before the DevFlow-Agents build phase: the
  roster and agent definitions are written in this grammar.

## 3. Source inventory and approval evidence (pre-SPEC gate)

| Source | Approval | Role in this SPEC |
|--------|----------|-------------------|
| ADR-010 | accepted 2026-08-22T21:54:53 | the target grammar (§3.1–§3.5); supersedes ADR-009 |
| REV-003 | approved 2026-08-22T21:04:25 | the site inventory + per-finding routing (§4/§6) |
| ADR-005 | accepted | the phrase-family sweep discipline; absence proven by zone, not by token |
| ADR-004 | accepted | kit-only partition (root devflow/ untouched) |
| US-000 | permanent container | Bolt parent |

Baseline read at `488f95d`. No governed source is draft/stale (gate passes — ADR-009 is
superseded by ADR-010, which is the cited source; the superseded ADR is not used).

## 4. Scope

**In (`distribution-kit/` only):** the 3 `manifest-v5-*.schema.json` (the grammar defs —
`created_by`, `run`, `checkpointApproval`'s `mode`, `hitlSubject` — **not** the
`checkpoint` enum); the 5 `TEMPLATE-MANIFEST-*.json`;
`devflow/avenga-devflow/Avenga-DevFlow.md` (§3.0, §3.3, §3.12, and the **grammar rows**
of §5.16); `devflow/GUARDRAILS.md`; the 16 template review-contract blocks; the ~35
frontmatter person-field comments; the four agent definitions
(`CLAUDE.md`, `.agents/skills/avenga-devflow/SKILL.md`,
`.github/agents/AvengaDevFlow.agent.md`, `.opencode/agents/AvengaDevFlow.md`).

**Out — moved to US-000.BOLT-009 (ADR-010 §3.6–§3.7):** the `checkpoint` enum's `HITL-*`
values, and the §5.16 checkpoint-name rewrite (`HITL-*`→`AITL-*`). This Bolt leaves the
enum untouched.

**Out (ADR-010 §3.8 scope guards):** AREV phase model fields
(`challenger_model`/`defender_model`/`judge_model`); `git config user.email` as the
*source* of the human namespace; role/domain fields (`role`, `decision_makers`,
`participants`, `stakeholders`, `real_name`); approved MEM/ADR bodies (G36); recorded
v4.2 history; the root `devflow/` tree (ADR-004); **building** the agent layer
(roster/Coordinator/registry — later USs).

## 5. The target field shapes (the machine contract — F-02, F-04, F-05)

Apply to all three `manifest-v5-{bolt,us,tc}.schema.json`:

1. **`$defs.generation.created_by` (F-02):** `{ "type": "string", "minLength": 1 }`
   → `{ "type": "string", "pattern": "^(human|agent):.+" }`.
2. **`$defs.run` (F-02):** add property
   `"agent": { "oneOf": [ { "type": "string", "minLength": 1 }, { "type": "null" } ] }`
   and add `"agent"` to `run.required` (family style: every field required, nullable
   where unrecorded — `null` = not agent-executed).
3. **`$defs.checkpointApproval` (F-04):** remove the `"mode"` property and remove
   `"mode"` from `checkpointApproval.required`. (`decided_by` items are `$defs.approver`,
   already actor-shaped with the agent⇒model conditional — **unchanged**.)
4. **`$defs.hitlSubject` → `$defs.checkpointSubject` (F-05, bolt schema only):** rename
   the def and update the one `$ref` (`checkpointApproval.subject`). The us/tc schemas
   inline their subject — no change there.
5. **Not touched by this Bolt:** the `checkpoint` enum (its purge to `AITL-*` only is
   ADR-010 §3.6 → **US-000.BOLT-009**); `$defs.approver` (already actor-shaped).

## 6. The 5 manifest examples (F-02, F-04)

`TEMPLATE-MANIFEST-{BOLT,BOLT-NONFUNCTIONAL,BOLT-TEST,US,TC}.json` and the embedded
example in `Avenga-DevFlow.md` §3.12:

- every `generation.created_by` / `code_generation.created_by`: bare → `human:<u>`
  (e.g. `"eugenio.serrano"` → `"human:eugenio.serrano"`, `"dev1"` → `"human:dev1"`);
- every `runs[]` entry gains `"agent": null`;
- every `checkpoint_approvals[]` entry drops its `"mode": "human"` line;
- `decided_by[].actor` values are already `human:<u>` — unchanged.

**One example must exercise the agent path** so the reshape is proven, not just
asserted: in `TEMPLATE-MANIFEST-BOLT.json` (the fullest example), add — or convert one
existing V-Bounce's — `code_generation` to carry a `runs[].agent: "developer-agent"`
with its model, and record one `checkpoint_approvals[]` entry whose `decided_by` is
`{ "actor": "agent:qa-agent", "role": "qa", "model": "<id>" }` (a low/medium MEM
approval), demonstrating both a virtual approval and an agent-attributed generation
validate. Keep the human default present elsewhere in the same file.

## 7. The methodology prose (F-01, F-02, F-03, F-04)

`Avenga-DevFlow.md`:

- **§3.0** — the canonical-identity paragraph (~:1594-1604) defines **two namespaces**:
  `human:<local-part-of-git-email>` (source unchanged) and `agent:<id>` (roster/agent
  definition), plus the **normalization rule** (a bare value equals its `human:`-prefixed
  form for comparison/projection). The `review:`/`reviewers` example becomes
  `reviewers: [{actor, role, model}]`. The projection paragraph (~:1606-1625) states the
  projection is now a copy (`review.reviewers[].actor` → `decided_by[].actor`), and drops
  the `mode` mention.
- **§3.3** — `risk_history[].decided_by[]` example: `user` → `actor` (+ `model`).
- **§3.12** — `created_by` sentence "identifies the **human**" → "the **actor** (human by
  default)"; the `checkpoint_approvals[]` description drops `mode` (now derived, note it as
  derived per G39); `runs[]` description adds `agent`.
- **§5.16 (grammar rows only)** — extend the `4.0`→`5.0` conversion table with the
  grammar reshapes: `reviewers {user,role}` → `{actor:"human:<u>", role, model:null}`;
  `created_by "<u>"` → `"human:<u>"`; `runs[]` gains `agent: null`; **no `mode` written**.
  The **checkpoint-name rewrite** (`HITL-*`→`AITL-*`) row is added by US-000.BOLT-009
  (ADR-010 §3.7) — not here.

Two strictness tiers per ADR-010 §3.2: prefix-mandatory in machine records and
review/enforcement fields; bare-as-human in descriptive frontmatter.

## 8. GUARDRAILS.md (F-01, F-04)

- The review-contract block and the manifest-projection block: `reviewers` →
  `{actor, role, model}`; drop the `mode` line from the projection description.
- **W11** field list: `reviewers` shape updated.
- G18/G24/G29/T02 wording unchanged in meaning — they already compare "actor"; verify
  they read cleanly against the new shape (no edit expected beyond the projection block).

## 9. The 16 template review blocks + ~35 frontmatter comments (F-01, F-03)

- Every `reviewers: [] # [{user, role}]` → `reviewers: [] # [{actor, role, model}]`
  (ADR, AREV 01/02/03, BUG, DISC, BOLT ×2 incl. acceptance, US, MEM, REV, SPEC, TC, UAT).
- Every frontmatter person-field comment (`author:`/`owner:`/`validator:`/`closed_by:`/
  `facilitator:` — `# local part of git config user.email (§3.0)`) gains the bare-as-human
  note (e.g. `# actor: bare = human:<user> (git email local part); agent = agent:<id> (§3.0)`).

## 10. The four agents (F-01, F-02, F-04, F-08)

Applied identically to all four (four-agent parity, verbatim shared body):

- the `created_by (human)` line → actor-shaped wording;
- the `checkpoint_approvals[]` summary line: drop `mode`, note it derived;
- the §5.16 mapping mention: `reviewers`/`created_by` reshape;
- **F-08:** replace the maintainer-repo citations — G18's `(ADR-008 §3.2–§3.4)` and the
  manifest summary's `(AITL, §3.0/ADR-008)` → the methodology anchor `(AITL, §3.0)`; same
  in `distribution-kit/AGENTS.md` (`(ADR-008)` → `(§3.0)`) and `spec/README.md`.

## 11. Test / verification strategy (ADR-005 zone-scoped absence proof — F-02 method)

Completeness is declared here as **acceptance criteria phrased as an absence**, verified
over the whole kit, not only edited files. All run against `distribution-kit/`:

1. `grep -rn '\[{user, role}\]'` → **0** (all review blocks reshaped).
2. `created_by` bare (unprefixed by `human:`/`agent:`) in any `.json` / schema `pattern`
   still `minLength:1` → **0**.
3. `grep -rn '"mode"' devflow/metrics` and `mode` in any `checkpointApproval` def → **0**.
4. `grep -rn 'hitlSubject'` → **0**.
5. `grep -rnE 'ADR-00[78]' distribution-kit` → **0** (F-08; citations now §3.0).
6. **Schema validation:** all 5 `TEMPLATE-MANIFEST-*.json` validate against the reshaped
   v5 schemas (Draft 2020-12 + format checker), including the agent-path example (§6).
7. **Enum untouched here:** the `checkpoint` enum of the 3 schemas is byte-identical to
   the baseline (this Bolt does not purge it — that is BOLT-009); the existing `AITL-*`
   example manifests still validate. (The migrated-history story is proven by BOLT-009's
   migration round-trip, not here.)
8. **Four-agent parity:** shared-body byte-identity except the sanctioned
   `agents-data/<agent>` line; G-count 39×5 (the AGENTS.md sync procedure).
9. `git status` shows only `distribution-kit/` + root governance records (kit-only, ADR-004).

The MEM records before/after counts for 1–5 and the pass/fail of 6–9.

## 12. Gates

- **bolt-manifest-validation:** the BOLT-008 manifest (root, v4) stays valid — `pass`.
- **hallucination-lint / secret-leak / PII:** docs+schema only, no secrets — `n/a`/`pass`.
- **unit/integration/SAST/DAST/perf:** `n/a` — documentation product, no runtime (§3.6).
- **test-first-evidence:** `n/a` — no behavior code; the §11 absence sweep + schema
  validation is the objective brake.

## 13. Risks, assumptions, stop conditions

- **Risk:** a schema reshape breaks one example's validation → §11.6 catches it before
  MEM; fix the example, not the schema semantics.
- **Risk:** the sweep accidentally touches the `checkpoint` enum (BOLT-009's territory) or
  an AREV model field → the §4 scope guards + §11.3-4 are scoped to
  `checkpointApproval.mode`/`created_by`, never the enum; §11.7 asserts the enum is unchanged.
- **Assumption:** no consumer reads `mode` (family shipped days ago; `metrics/bolts/` in
  the kit is empty) — if one is found, **stop** and record it (mode-drop would need a note).
- **Stop condition:** if any §11 absence check cannot reach 0 without touching an ADR-010
  §3.8 scope-guard zone (or the enum), stop, write the MEM with the blocker, pause at
  HITL-MEM-Approval.

## 14. HITL-SPEC-Approval

> **Avenga DevFlow §2.4.1, §3.0.** Approved — Dev-validator + Tech Lead recorded
> `HITL-SPEC-Approval` at 2026-08-22T22:09:55-03:00. The first code-run / V-Bounce is
> authorized.

| Field | Value |
|-------|-------|
| **Reviewers** | eugenio.serrano (dev_validator) + eugenio.serrano (tech_lead) |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-22T22:05:50-03:00` |
| **review.started_at** | `2026-08-22T22:09:55-03:00` |
| **review.decided_at** | `2026-08-22T22:09:55-03:00` |

| Field | Value |
|-------|-------|
| **Reviewers** | *(pending)* Dev-validator + Tech Lead |
| **Decision** | *(pending)* approved / changes_requested / rejected |
| **review_ready_at** | `2026-08-22T21:20:12-03:00` |
| **review.started_at** | *(pending)* |
| **review.decided_at** | *(pending)* |

Replicated in the Bolt manifest (`spec_revisions[]` appended now; the
`HITL-SPEC-Approval` decision is appended to `hitl_approvals[]` only when recorded).
