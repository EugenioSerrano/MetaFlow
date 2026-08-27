---
id: "SPEC-260824-0054"
title: "The roster-as-enablement reshape — the actors/ family per ADR-014 §3.9 + the mechanism named in the methodology and the four MainAgents"
date: "2026-08-24"
author: "eugenio.serrano"
llm: "claude-fable-5"
status: "approved" # draft | approved | blocked | obsolete — AITL-SPEC-Approval 2026-08-24 (executes after SPEC-260824-0050's V-Bounce + MEM approval)
origin: "US-024"
bolt: "US-024.BOLT-004"
revision: 2 # rev 2 (2026-08-24): the examples expansion — example-human + example-agent + example-roster — and the model-required-only-for-agents schema fix (V-Bounce 2; V-Bounce 1 delivered rev 1)
associated_adrs:
  - "devflow/adrs/ADR-014-actors-roster-is-the-enablement.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
prerequisites:
  - "devflow/spec/SPEC-260824-0050-agents-examples-squad-split.md" # executes FIRST — this SPEC's Phase C edits land in the post-split paths (agents/README.md)
risk_class: "low"
autonomy_level: "L3" # low risk → L3 default (§3.3)
turn_budget: ""
data_classification: "internal"
review_ready_at: "2026-08-24T01:21:56-03:00" # revision 2 (the examples expansion + the model rule); revision 1's approval (01:01:08) kept in the manifest + §18
review: # AITL-SPEC-Approval (revision 2) — decision dictated in conversation ("Y lo aprobamos!", over the reviewed rev-2 plan incl. the reviewer's naming + illustrative-header notes) and transcribed by the agent (§3.0)
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-24T01:21:56-03:00"
  decided_at: "2026-08-24T01:21:56-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Revision 2 approved as Dev-validator (material addition after V-Bounce 1's MEM approval — G15/G16: a new V-Bounce under the new revision): the examples expansion (example-human.yaml — a human actor, no model/definition, humans approve by default; example-agent.yaml — the existing worked example renamed for symmetry; example-roster.yaml — an illustrative filled team list with an explicit illustrative header, since the consistency rule applies to the real roster.yaml only) and the schema fix the human example surfaced: model leaves the base required set and becomes agent-required (definition present => model required) — a human actor file was impossible under the rev-1 schema (model minLength 1 vs the human:<user> -> model null grammar). Cross-model review of the plan: PASS with the two naming/header notes, both folded in. Authorizes V-Bounce 2."
---

# SPEC-260824-0054 — The roster-as-enablement reshape

| Field | Value |
|-------|-------|
| **Origin** | US-024 (revision 3 — approved 2026-08-24) |
| **Bolt** | US-024.BOLT-004 (READY 2026-08-24, risk low) |
| **ADRs** | ADR-014 (§3.8 the mechanism, §3.9 the family shape), ADR-004 (kit-only) |
| **Risk Class** | low |
| **Revision** | 2 |

---

## 1. Objective

Reshape the kit's `actors/` family to the roster-as-enablement model
(ADR-014) and name the mechanism everywhere an adopter can read the norm —
the family docs, the methodology §3.0.1 and the four MainAgents. The
maintainer's ADRs are invisible to adopters (ADR-004/G28): if the kit does
not say what "explicit, valid configuration" IS, the norm does not exist
for them. Without this Bolt the kit still ships the retired per-project
AITL-enable ADR template and the redundant policy file, contradicting the
accepted ADR-014.

## 2. Context

ADR-014 (accepted 2026-08-24) superseded ADR-008 with full carry-forward
and fixed the new mechanism: **a schema-valid, human-authored roster entry
is the explicit configuration** — no per-project ADR, no policy switch;
enablement is the human's act, never the agent's. US-024 revision 3
(approved 2026-08-24) carries the family shape (AC-1), the enablement
(AC-7) and the validation (AC-8). This SPEC executes **after**
SPEC-260824-0050 (the agents/ split), so its wording edits land in the
post-split locations.

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | US-024.BOLT-004 | AITL-BOLT-READY-Approval ✓ (2026-08-24T00:49:38) |
| Feature US | US-024 revision 3 | AITL-US-Approval ✓ (2026-08-24T00:40:35) |
| ADR | ADR-014 | AITL-ADR-Approval ✓ (2026-08-24T00:16:18) |
| ADR | ADR-004 | AITL-ADR-Approval ✓ (accepted) |
| Repository baseline | `7e3eb5e` (+ the SPEC-260824-0050 V-Bounce) | — |

## 4. Scope

### In scope
- `distribution-kit/devflow/actors/**` (the reshape).
- The enablement wording: the methodology `avenga-devflow/Avenga-DevFlow.md`
  §3.0.1; the governance references at their post-split home
  (`agents/README.md`); the shared-body clause in the four MainAgents
  (`CLAUDE.md`, `.agents/skills/avenga-devflow/SKILL.md`,
  `.github/agents/AvengaDevFlow.agent.md`, `.opencode/agents/AvengaDevFlow.md`).

### Out of scope
- The agents/ structural split (SPEC-260824-0050 — already executed).
- The MainAgent lifecycle capability (US-025) and the v2 hardening
  (capability fields, schema-enforced ceiling, authority-change audit).

## 5. Prerequisites and baseline

- **SPEC-260824-0050's V-Bounce executed and its MEM approved** (the
  agents/ split in place — F3 sequencing).
- Current `actors/` tree: `README.md`, `INDEX.md`, `TEMPLATE-ACTOR.yaml`,
  `TEMPLATE-AITL-ENABLE-ADR.md`, `example.yaml`, `project-policy.yaml`,
  `roster.schema.yaml`.

## 6. Phases

### Phase A — The `actors/` family reshape

**Duration:** ~1.5h — **Complexity:** Low

Delete `TEMPLATE-AITL-ENABLE-ADR.md` and `project-policy.yaml` (retired by
ADR-014 §3.9 — the `human_only` `[critical, regulatory]` ceiling is already
stated as a fixed rule in the methodology §3.0.1; `aitl_enabled_checkpoints`
is redundant: the actor's `approves` is the grant). Create **`roster.yaml`**
— a shipped skeleton (header comments + an empty `actors:` list) stating it
is **the team list, the single membership authority**: one entry per actor
referencing its `<actor-id>.yaml`; a file not listed is not in the team.
Create `examples/` and move `example.yaml` → `examples/example.yaml`,
fixing its `definition:` pointer to the post-split path
(`agents/squad/<id>/agent.yaml` — illustrative) and **removing its
`capabilities` block** to match the simplified v1 contract (one consistent
shape everywhere; the full shape returns with the v2 hardening). Simplify
`TEMPLATE-ACTOR.yaml`: keep `id`, `name`, `role`, `model`, `modes`,
`approves`, `definition` (+ the non-negotiable bounds note); remove the
`capabilities` block with an explicit "deferred to the v2 hardening —
the T0/T1 approver ceiling governs as a methodology rule" comment. Rewrite
`README.md`: the family-shape table (roster.yaml row, examples/ row; the
policy row gone), resolution rule 1 → "an agent holder counts for the
checkpoint classes **its own `approves` grants**", the living-data rule →
"an approver's authority fields are the **human's configuration act** — an
agent never writes them", the two "Enabling virtual approvers → see
TEMPLATE-AITL-ENABLE-ADR" callouts → one "the roster is the enablement"
paragraph, and "What lives here" updated. Update `INDEX.md` (the family
docs; the team lives in `roster.yaml`).

**Files created:** `actors/roster.yaml` · `actors/examples/example.yaml` (moved + pointer fix)
**Files modified:** `actors/README.md` · `actors/INDEX.md` · `actors/TEMPLATE-ACTOR.yaml`
**Files deleted:** `actors/TEMPLATE-AITL-ENABLE-ADR.md` · `actors/project-policy.yaml` · `actors/example.yaml` (moved)

### Phase A' — The examples expansion (revision 2 — V-Bounce 2)

**Duration:** ~45min — **Complexity:** Low

Rename `examples/example.yaml` → **`examples/example-agent.yaml`**
(kebab symmetry). Create **`examples/example-human.yaml`** — a human actor
(e.g. "Arq Juan", role architect): `id`, `name`, `role`, `modes:
[executor, approver]`, `approves` (humans approve by default) — **no
`model`, no `definition`** (the `human:<user>` grammar: model is null; the
definition block is agents-only). Create **`examples/example-roster.yaml`**
— a filled team list showing the human + the agent actors listed together,
with an **explicit illustrative header** ("illustrative — copy and
instantiate"): the id-resolves-to-file consistency rule applies to the
real `roster.yaml`, never to this example. Update the references that name
the old example path (`actors/README.md` family table + what-lives-here,
`actors/INDEX.md` docs table).

**Files created:** `examples/example-human.yaml` · `examples/example-roster.yaml`
**Files renamed:** `examples/example.yaml` → `examples/example-agent.yaml`
**Files modified:** `actors/README.md` · `actors/INDEX.md` (example references)

### Phase B' — The model rule (revision 2 — the gap the human example surfaced)

**Duration:** ~20min — **Complexity:** Low

Under the rev-1 schema a human actor file is **impossible**: `model` sits
in the base `required` with `minLength: 1`, while the actor grammar
records a human's model as null. Fix: **`model` leaves the base required
set** (`required: [id, name, role, modes, approves]`) and becomes
**agent-required** via the `allOf` (`definition` present ⇒ `required:
[model]`) — every agent carries `definition` + `model` (the model matters
for the record and for model-level independence); every human omits both.
Consistent with the actor grammar — no upstream change needed.

### Phase B — The schema v1 rule

**Duration:** ~30min — **Complexity:** Low

`roster.schema.yaml` gains the v1 rule (ADR-014 §3.8.4): `modes` contains
`approver` ⇒ `approves` is non-empty (an `allOf`/`if-then` with
`minItems: 1`). **And the existing `definition ⇒ required: [capabilities]`
`allOf` is relaxed** (F-S1): with the `capabilities` block deferred from the
v1 template, that requirement would fail every actor instantiated from it —
the requirement is dropped with a "returns with the v2 hardening" note,
while the `capabilities` property definition **stays in the schema as
optional** (a project already declaring capabilities still validates).
Nothing else changes in v1. The `roster.yaml` consistency
check (every listed id resolves to an existing `<actor-id>.yaml`) is
**documented** in the README as the list's validation rule — the validator
tooling (US-012 family) automates it later.

### Phase C — The mechanism named across the kit

**Duration:** ~1h — **Complexity:** Low

**Methodology §3.0.1** (`avenga-devflow/Avenga-DevFlow.md`, the "Safe
default" paragraph): "no roster, or no `agents:` section" → "no roster
entry, or no schema-valid approver entry"; "a governed per-project act (the
AITL-enable ADR), never a silent flag" → "a **human's configuration act —
a schema-valid roster entry granting the checkpoint class**
(`modes: [approver]` + non-empty `approves`) — never a silent flag, never
the agent's own act". **`agents/README.md`** (the post-split home of the
governance table + the create-guide step 6): the two AITL-enable references
→ the roster grant (same wording family). **The four MainAgents** (shared
body, byte-identical ×4): the AITL section's "a virtual DevFlow Agent only
by explicit, valid configuration" gains the inline definition "— a
schema-valid, human-authored entry in the project's `devflow/actors/`
roster (`modes: [approver]` + `approves`); an agent never enables its own
approval —". The guardrail table text is untouched (G-count invariant).

### Phase D — Verification

**Duration:** ~45min — **Complexity:** Low

Directory listing of the final `actors/` tree; the schema fail-fast demo (a
malformed entry — `modes: [approver]`, `approves: []` — rejected; the
worked example validates); the ADR-005 phrase-family sweep over the kit for
the retired mechanism (`AITL-enable`, `project-policy`,
`aitl_enabled_checkpoints`) → 0 normative references; the four-agent
byte-sync diff of the shared body + the G-count check (39); self-containment
grep (0 maintenance IDs); no BOM.

## 7. Acceptance criteria

### AC-1: The family shape
**Given** the kit after the revision-2 V-Bounce, **When** `actors/` is
listed, **Then** it contains exactly `README.md`, `INDEX.md`,
`roster.yaml`, `roster.schema.yaml`, `TEMPLATE-ACTOR.yaml` and
`examples/{example-agent.yaml, example-human.yaml, example-roster.yaml}` —
and the two retired files do not exist.

### AC-2: The schema rules
**Given** an actor file with `modes: [approver]` and empty `approves`,
**When** validated, **Then** it fails fast; the **agent** example (v1
shape — `definition` + `model`, no `capabilities`) **passes**; the
**human** example (no `model`, no `definition`) **passes** (revision 2);
an agent file with `definition` but **no `model`** **fails fast**
(revision 2 — the agent-required rule); and an actor file that still
declares `capabilities` **also passes** (optional in v1, the relaxed
`allOf`).

### AC-3: The mechanism named
**Given** the methodology §3.0.1, `agents/README.md` and the four
MainAgents, **When** read, **Then** each names the enablement as the
schema-valid, human-authored roster entry (never self-enabled) — the four
agents byte-identical in the shared clause, G-count 39 preserved.

### AC-4: Zero retired references
**Given** the kit-wide sweep, **When** it runs, **Then** 0 normative
references to the AITL-enable ADR / project-policy remain.

### AC mapping to source

| Source AC | How this SPEC satisfies it | Verifying evidence |
|-----------|----------------------------|--------------------|
| US-024 rev 3 AC-1 | Phase A builds the exact ADR-014 §3.9 shape | Directory listing |
| US-024 rev 3 AC-7 | Phase A README ("the roster is the enablement") + Phase C wording | README/method diff + sweep |
| US-024 rev 3 AC-8 | Phase B schema rule + the documented consistency check | Fail-fast demo |

## 8. Testing strategy

Documentation/schema Bolt — scripted evidence: the schema validation pair
(example PASS / malformed FAIL, parser-based like US-024.BOLT-001's), the
directory-shape check, the sweep counts, the byte-sync diff + G-count,
self-containment, BOM. No unit/integration/E2E (no runtime surface).

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | n/a — documentation/schema Bolt, no runtime surface | n/a |
| SAST / SBOM | n/a — no code | n/a |
| Perf-smoke (p95/p99) | n/a — no runtime | n/a |
| Prompt-injection scan | no injected instructions in the four-agent clause or docs | pass expected |
| Secret-leak scan | no secrets | pass expected |
| Hallucination lint | every referenced path/anchor resolves (incl. the squad/ pointer) | pass expected |
| IP / license provenance | kit-original content only | pass expected |
| PII / DLP | internal docs, no personal data | pass expected |
| Dependency-confusion | n/a — no dependencies | n/a |
| Test-first evidence | the §8 checks defined before execution | pass expected |
| Behavioral reproducibility | validation/sweep checks re-run identically | pass expected |
| Bolt-manifest validation | v_bounces[1] appended, schema PASS | pass expected |

## 10. Security and data

Internal documentation/config. The reshape **is** the security posture of
v1: the schema gate (fail-fast → safe default), the human-only authority
fields (never self-enabled — stated at every reading point), the fixed
`[critical, regulatory]` human ceiling (methodology rule), and the T0/T1
approver ceiling carried as an ADR-014 §3.6 text rule (schema enforcement
= v2).

## 11. Monitoring and observability

n/a — documentation family.

## 12. Migration, compatibility and rollback

- **Migration:** adopters of prior kits upgrade via §5.16 (framework files
  superseded; the retired files simply no longer ship). A project that
  copied the old template keeps it as its own project ADR — unaffected.
- **Compatibility:** `example.yaml` moves into `examples/` — any doc
  referencing the old path is updated in Phase A.
- **Rollback:** `git revert` of the V-Bounce commit.

## 13. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| Wording drift between the four MainAgents | 2 | 3 | Byte-sync diff of the shared clause (US-016 discipline) |
| A stale retired-mechanism reference survives | 2 | 3 | The ADR-005 phrase-family sweep (positive coverage) |
| The simplified template loses a needed field | 1 | 2 | Only `capabilities` is deferred (explicit v2 note); all authority fields stay; **the schema's `definition ⇒ capabilities` requirement is relaxed in the same pass (F-S1)** so a v1-template actor validates |

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| `roster.yaml` ships as a commented skeleton | The kit never ships a team (the roster is project config); the skeleton makes the contract readable at the point of use |
| The consistency check is documented, not schema-encoded, in v1 | JSON Schema cannot cross-check the filesystem; the validator tooling (US-012) automates it — honest v1 boundary |
| One inline clause in the MainAgents (not a full section) | The methodology carries the depth; the agents need the definition at the decision point — minimal byte-sync surface |
| The example drops `capabilities` (instead of keeping it as full-shape illustration) | One consistent v1 shape everywhere — a reader instantiating from the template never wonders where an example-only field came from; the full shape (template + example + schema requirement) returns together in v2 |
| The relaxed `allOf` keeps `capabilities` optional, not forbidden | Forward-compatible: a project that already declares capabilities keeps validating; v2 only re-tightens |
| `example-*` kebab naming for the three examples (rev 2) | Symmetry, and `example-roster.yaml` avoids the visual collision with the real `roster.yaml` (reviewer note) |
| The example roster carries an explicit illustrative header (rev 2) | The id-resolves-to-file consistency rule applies to the real `roster.yaml` only — the header prevents a false validation failure reading (reviewer note) |
| `model` becomes agent-required via `definition` (rev 2) | The discriminator: every agent carries definition + model (record + model-level independence); every human omits both — matches the `human:<user>` → model-null grammar, which the rev-1 base `required` contradicted |

## 15. Stop conditions

- The four MainAgents' shared body differs before editing (byte-sync broken
  upstream) → stop, record, ask.
- A retired-mechanism reference that is neither updatable nor allowlistable
  prose → stop, record in the MEM, ask.
- Anything requiring a change outside the kit (maintainer partition).

## 16. Definition of Done (DoD)

- [ ] Phases A–D implemented
- [ ] AC-1..AC-4 pass (evidence recorded)
- [ ] Applicable gates pass / n/a per §9
- [ ] MEM created in `devflow/memory/` (exactly one)
- [ ] Manifest `v_bounces[]` entry appended
- [ ] AITL-MEM-Approval recorded

## 17. References

- US-024 revision 3 · US-024.BOLT-004 · ADR-014 §3.8/§3.9 (+ §3.3.3/§3.6
  carried rules) · ADR-004 · SPEC-260824-0050 (the prerequisite split) ·
  US-025 (consumes the shape) · US-016 (byte-sync discipline).

## 18. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-24 | eugenio.serrano (agent-drafted) | Revision 1 (approved 01:01:08; delivered by V-Bounce 1, MEM approved 01:21:56) |
| 2026-08-24 | eugenio.serrano (agent-drafted) | Revision 2 — Phase A' (example-human + example-agent rename + example-roster with the illustrative header) + Phase B' (`model` agent-required via `definition`; base required drops it); AC-1/AC-2 extended (V-Bounce 2) |

## 19. AITL-SPEC-Approval

> Draft until the Dev-validator records `AITL-SPEC-Approval` (frontmatter
> `review:` block). SPEC approval authorizes the code-run / V-Bounce (G14).

| Field | Value |
|-------|-------|
| **review.reviewers** | `human:eugenio.serrano` (dev_validator) |
| **review.decision** | **approved** |
| **review_ready_at** | `2026-08-24T00:55:21-03:00` |
| **review.started_at** | `2026-08-24T01:01:08-03:00` |
| **review.decided_at** | `2026-08-24T01:01:08-03:00` |
| **Findings** | F-S1 (schema allOf vs the simplified template) fixed pre-approval in this revision; O-1 folded into the risk matrix; O-2 (`model: inherit` semantics) pending — routed to US-025, not assumed |
