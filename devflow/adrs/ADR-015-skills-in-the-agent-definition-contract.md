---
id: "ADR-015"
title: "Skills in the DevFlow Agent definition contract — an optional, projected, folder-atomic skills bundle"
date: "2026-08-26"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
status: "accepted" # draft | accepted | rejected | deprecated | superseded
decision_makers: ["architect", "tech_lead"]
sources:
  - "devflow/reviews/REV-007-testwriter-devagent-readiness.md"
  - "devflow/adrs/ADR-013-agent-lifecycle-governance.md"
  - "devflow/adrs/ADR-007-devflow-agent-identity-model.md"
  - "devflow/adrs/ADR-014-actors-roster-is-the-enablement.md"
supersedes: []
conflicts_with: [] # extends ADR-013's install act (more files, same governance class); ADR-007 identity and ADR-014 enablement untouched
tags: ["devflow-agents", "skills", "definition-contract", "projection", "parity", "v5.1", "tool-agnosticism"]
nfrs: []
waiver: # Only for gate-override ADRs (§3.6)
  gate: ""
  reason: ""
  owner: ""
  compensating_control: ""
  expires_at: ""
review_ready_at: "2026-08-26T17:54:33-03:00" # When this version is submitted for review (§3.0)
review: # AITL-ADR-Approval evidence — decision dictated in conversation ("aprobado!") and transcribed by the agent (§3.0)
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "architect"
      model: null
  started_at: "2026-08-26T18:01:40-03:00"
  decided_at: "2026-08-26T18:01:40-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved as Architect/TL. The decision content was steered by the maintainer in conversation before drafting (the skills bundle, strict symmetry, folder-atomicity, the never-silent fallback, skills-never-authority, tool-agnosticism of shipped skills, and the maintainer-partition scoping — normativity baked into kit framework files by US-023.BOLT-006, the ADR-013/014 pattern). Pre-approval, an independent cross-model review pass challenged the evidence base on three points (source approval status, the F-06 decision's existence, the measurement's attribution); all three were verified against the current repository state and refuted — REV-007 is approved with the decision recorded at 2026-08-26T17:52:15-03:00, its F-06 carries the maintainer tool-agnosticism decision, and the measured ~32.5k breakdown lives in its F-03. The same pass independently confirmed the character measurement byte-exact and validated the routing numbers (US-023.BOLT-006 free, US-026 next) and the no-schema-in-v1 premise. With this acceptance the US-023 G15 re-revision and US-023.BOLT-006 may cite this ADR (G13)."
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs, and section
  headings (##) stay in English (the schema). ADR titles and prose go in
  the project's content_language (en). `AITL-ADR-Approval` is never
  translated.

  ⚠️ This ADR is a DRAFT until an Architect / Tech Lead records
  AITL-ADR-Approval. A draft ADR cannot govern; until acceptance the
  definition contract remains the two-file pair.

  ⚠️ SCOPE — MAINTAINER PARTITION (the ADR-013/014 pattern): adopters ship
  no ADRs. This ADR governs THIS repository's change to the definition
  contract; the normative text the adopter receives is baked into the
  kit's framework files (agents/README.md, examples/README.md,
  VERIFICATION.md, the Coordinator platform preambles) by the
  implementing Bolt — the US-023 G15 re-revision → US-023.BOLT-006,
  citing this ADR. The adopter receives the rule there, never as an ADR.
-->

# ADR-015 — Skills in the DevFlow Agent definition contract

| Field          | Value |
|----------------|-------|
| **Status**     | **accepted** (immutable — a new decision requires a superseding ADR) |
| **Decision-makers** | Architect / Tech Lead |
| **Sources**    | REV-007 (approved — F-03/F-04), ADR-013 (lifecycle), ADR-007 (identity), ADR-014 (enablement) |
| **Supersedes** | None |
| **Conflicts with** | None — extends ADR-013's install act; ADR-007/014 untouched |

---

## 1. Context

The canonical DevFlow Agent definition is **one file pair** — `agent.yaml`
(structured fields) + `prompt.md` (the charter body) — and every rule that
moves a definition around (copy example → squad, Coordinator install, N×4
parity, delete) is written in terms of that pair
(`distribution-kit/devflow/agents/README.md`, `VERIFICATION.md`).

REV-007 (approved 2026-08-26) evaluated a real multi-skill agent —
TestWriter, a QA test-design agent whose productive value lives in **5
skills, 7 progressive-disclosure reference files and 1 asset** — against
this contract and found the single structural gap of the evaluation
(F-03): skills have **no canonical field, no folder convention, no
per-platform projection row and no parity coverage**. The only port under
today's contract is inlining everything into `prompt.md`, which REV-007
measured and rejected: **~32.5k characters today** (skills + references +
asset: 22,952; agent + global instructions + shortcut prompt: 9,597) —
already over the documented GitHub Copilot cloud-agent **30k prompt cap**
before translation and porting guidance grow it, destroying on-demand
loading (every reference always in context) and the "add a heuristic =
drop a file in `references/`" extension property.

The gap is not TestWriter-specific: it blocks **every future multi-skill
DevFlow Agent**. Meanwhile the platform surfaces already exist (the kit
itself ships the Coordinator's skill at `.agents/skills/avenga-devflow/`;
Copilot has `.github/skills/`, Claude Code `.claude/skills/`) — what is
missing is the canonical side: the definition contract, the projection
mapping and the parity discipline.

Two constraints frame the decision: the **spawn topology** (executors
cannot spawn; skills must never become a spawning back door) and the
methodology's **tool- and model-agnosticism** (REV-007 F-06 maintainer
decision: the kit ships nothing tool-specific; integrations are adopter
configuration).

---

## 2. Alternatives considered

### Alternative A — Optional skills bundle inside the definition folder, projected per platform (✅ Selected)

| Aspect   | Detail |
|----------|--------|
| **Pros** | Skills live where the identity lives — the definition folder stays the single unit of copy/install/delete/parity. Progressive disclosure preserved (references load on demand). Declared in `agent.yaml`, so authority-bearing structure stays structured, never prose. Backward compatible: the pair alone remains a valid definition. Uses each platform's native skill surface. |
| **Cons** | The install act and the parity check grow (more files, per-platform skill rows). Platform skill surfaces vary and one may not exist — needs an explicit fallback policy (decided in §3.5). |

### Alternative B — Inline the skills into `prompt.md`

| Aspect   | Detail |
|----------|--------|
| **Pros** | Zero contract change. |
| **Cons** | Measured ~32.5k chars > the Copilot 30k cloud cap before porting even starts; every reference permanently in context (token waste, no progressive disclosure); extending a skill means editing the charter. Rejected on REV-007's measured evidence. |

### Alternative C — Skills as a shared repo-level library outside the definitions

| Aspect   | Detail |
|----------|--------|
| **Pros** | One skills folder, reusable across agents. |
| **Cons** | Breaks the definition folder as the atomic unit: copy/install/delete/parity would need a second root to track, and a squad copy would no longer be self-contained (an example copied into `squad/` silently depends on files outside it). Role know-how is charter-coupled, not global. Cross-agent reuse is still possible under A by copying — the definition stays self-contained. Rejected. |

### Alternative D — Model each skill as a sub-agent

| Aspect   | Detail |
|----------|--------|
| **Pros** | Maximal isolation per pipeline stage. |
| **Cons** | Violates the spawn topology: executors carry no spawn capability, so a role agent could not drive its own pipeline; and skills are **content**, not actors — they carry no identity, sign nothing, appear in no roster. Rejected outright. |

---

## 3. Decision

**We adopt Alternative A.** The canonical definition contract gains an
**optional skills bundle**, under the following rules.

### 3.1 The structure

A definition folder MAY contain a `skills/` area:

```
devflow/agents/<examples|squad>/<id>/
  agent.yaml
  prompt.md
  skills/
    <skill-name>/
      SKILL.md          # the skill instructions (progressive-disclosure entry)
      references/       # optional — detail files loaded on demand
      assets/           # optional — templates/data the skill uses
```

The two-file pair alone remains a **complete, valid definition** — the
five shipped examples conform unchanged. `skills/` is additive, never
required.

### 3.2 The declaration and its validation

`agent.yaml` gains an optional **`skills:`** field: the list of the
definition's skill names (matching the `skills/<skill-name>/` folders).
**Strict symmetry is a validation rule of the contract**: a skill folder
not declared in `skills:` fails validation exactly like a declared skill
with no folder — an undeclared extra is a failure, not a tolerated
addition (the manifest family's `additionalProperties: false` discipline
applied to the definition).

**v1 enforcement — explicit:** the definition family has no schema file in
v1, so the symmetry rule is enforced **deterministically by the
projection/parity tooling and the install act** (the Coordinator refuses
to install an asymmetric definition). When the definition family gains a
schema (the v2 hardening, §4), the `skills:` field enters it with the same
strict discipline.

### 3.3 Folder-atomicity

The **definition folder is the atomic unit** of every lifecycle act
(ADR-013's acts, extended — same governance class, same living-data rule):

- **Copy** (example → `squad/`): the whole folder, skills included.
- **Install**: the Coordinator projects the wrapper **and** the declared
  skills into the platform's surfaces; installing the wrapper while
  leaving declared skills behind is an **incomplete install** — the act
  fails, it does not degrade silently (§3.5 is the only sanctioned
  degradation, and it is explicit).
- **Delete**: removes the wrapper and its projected skill files; the
  N:1 reference check (squad README) protects shared definitions as
  today.
- **Parity**: the N×4 check regenerates and diffs **wrapper + projected
  skill files** per platform; drift in a projected skill file fails
  parity exactly like wrapper drift. Projected skill files are generated
  artifacts — **never hand-edited** (fix the canonical definition).

### 3.4 Per-platform projection

`VERIFICATION.md` gains a **skills row per platform**: the target surface
(GitHub Copilot `.github/skills/`, Claude Code `.claude/skills/`,
OpenCode and Codex per their skill surfaces), the projection shape, and
the caveats — each **re-verified against current platform docs at
implementation time**, as the mapping table already mandates for every
other row. Projected skill files carry a provenance marker naming their
canonical source (the parity check's anchor).

### 3.5 The never-silent fallback

On a platform with **no usable native skills surface**, the Coordinator
resolves the install in this order:

1. **Inline with warning** — fold the skills into the wrapper body only
   if the result stays under that platform's documented size cap; the
   install output states what was inlined and why.
2. **Degraded install with explicit notice** — install the wrapper
   without the skills **and record the degradation** (install output +
   the platform's row/notes in `VERIFICATION.md`), so the human knows
   this platform runs the agent without its skills.

**Prohibited:** the third option — installing the wrapper alone and
saying nothing. A silently lobotomized agent that references skills that
were never installed is the failure mode this section exists to exclude.

### 3.6 Skills are content, never authority (invariant)

Nothing in a `SKILL.md`, reference or asset grants anything: **authority
lives in structured fields only** (`modes`, `approves` — ADR-014's
human-authored roster act) and capability lives in `capabilities.*`. A
skill cannot raise a tier, add a tool or MCP server, create spawn
capability, or make an agent an approver — a skill that instructs
otherwise is dead text, exactly like charter prose claiming authority.
The approver capability ceiling (T0/T1, no write paths, no transactional
MCPs) is unchanged, and approver-mode agents' skills are bound by it like
the rest of their definition.

### 3.7 Tool-agnosticism of shipped skills (invariant)

Skills shipped in the kit's `agents/examples/` name **no MCP servers, no
external tools, no vendor schemas** (the REV-007 F-06 decision applied to
the skills layer). Kit examples ship with `mcp_servers: []`; wiring any
integration — and any skill content that drives one — is the adopting
team's configuration in its own `squad/` copy. The contract's allowlist
(`capabilities.mcp_servers`, named + allowlisted) is the generic capacity
that makes that adopter act possible without any kit coupling.

### 3.8 What does not change

- **Activation**: the roster remains the only switch (ADR-014); a skills
  bundle changes nothing about enablement, approver authority or the
  safe default.
- **Spawn topology**: skills are files, not actors — no spawn capability
  enters any wrapper because of them.
- **The lifecycle's governance class** (ADR-013): install/copy/delete of
  a definition with skills is the same living-data operational act; G07
  scoping is unchanged.
- **Examples discipline**: `examples/` stay read-only references, copied
  never edited, never installed from, never referenced by the roster.

### 3.9 Where the normativity lands

This ADR is a **maintainer-partition decision record** — adopters ship no
ADRs. The implementing Bolt (**US-023 G15 re-revision →
US-023.BOLT-006**, citing this ADR) bakes the normative text into the
kit's framework files: `agents/README.md` (the contract table + §3.1–3.3
rules), `examples/README.md` (folder-atomic copy), `VERIFICATION.md`
(projection rows, parity extension, fallback policy §3.4–3.5), and the
Coordinator platform preambles (the install act). The adopter receives
the rule there — the ADR-013/014 pattern.

---

## 4. Consequences

**Positive:**
- Multi-skill DevFlow Agents become shippable and installable — the
  immediate enabler for the test-designer example (REV-007 route #3,
  US-026) and every future one.
- Progressive disclosure survives the port: references load on demand
  instead of bloating charters past platform caps.
- Extension stays cheap and local: adding a heuristic to a squad agent is
  dropping a file and one list entry — then a reinstall, with parity
  keeping all four platforms honest.
- The definition folder remains self-contained: a squad copy carries
  everything it needs.

**Trade-offs (explicit, accepted for v1):**
- The install act and the parity check grow in surface (more files, more
  rows); install/regeneration takes longer and VERIFICATION.md gets
  denser.
- Platform skill surfaces are heterogeneous and drift-prone — each row
  needs re-verification at implementation time, and the fallback (§3.5)
  means one platform may legitimately run a degraded agent (visibly).
- The symmetry validation is tooling-enforced in v1, not schema-enforced
  — a gap between rule and schema until v2.

**Technical debt / follow-up:**
- **v2 hardening:** an agent-definition schema (validating `agent.yaml`
  including `skills:` with strict symmetry, `additionalProperties:
  false`), aligned with the actor-schema hardening ADR-014 already
  defers to v2.
- **US-023.BOLT-006** — the kit implementation (contract docs, projection
  rows, parity extension, Coordinator preambles).
- **US-026** — the first consumer (the test-designer example agent, per
  REV-007 routes #2–#4).
- OpenCode/Codex skill-surface verification results recorded in
  VERIFICATION.md at implementation time.

---

## 5. Applicable NFRs

None introduced — this ADR defines contract structure, not a measurable
quality threshold. The existing parity discipline (0 drift after
regeneration) simply extends to the projected skill files (§3.3).

| NFR | Description | Threshold | How it is measured |
|-----|-------------|-----------|-------------------|
| —   | —           | —         | —                  |

---

## 6. References

- [REV-007](../reviews/REV-007-testwriter-devagent-readiness.md) —
  approved; F-03/F-04 (the gap + the measured evidence), F-06 (the
  tool-agnosticism decision §3.7 applies), route #1 (this ADR +
  US-023.BOLT-006).
- [ADR-013](ADR-013-agent-lifecycle-governance.md) — the lifecycle acts
  this ADR extends (folder-atomic; same governance class).
- [ADR-007](ADR-007-devflow-agent-identity-model.md) — the identity
  model (untouched; skills carry no identity).
- [ADR-014](ADR-014-actors-roster-is-the-enablement.md) — the enablement
  (untouched; skills grant nothing, §3.6).
- `distribution-kit/devflow/agents/README.md` and `VERIFICATION.md` — the
  contract and mapping this ADR amends (via US-023.BOLT-006).
- `devflow/input/source-code/TestWriter/` — the raw evidence REV-007
  examined (human-deposited, read-only).

---

## 7. AITL-ADR-Approval

> **AITL-ADR-Approval** (Avenga DevFlow §2.8, §3.0, §3.5). An ADR does not
> become `accepted` — and therefore governing — without the approval of an
> Architect / Tech Lead. This ADR is the source of truth for its own
> approval (recorded in the `review` frontmatter block). Only once
> `accepted` may the US-023 G15 re-revision and US-023.BOLT-006 cite it
> (pre-SPEC evidence gate, G13); a draft cannot govern.

| Field | Value |
|-------|-------|
| **Architect / Tech Lead** | `human:eugenio.serrano` |
| **Role** | architect |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-26T17:54:33-03:00` |
| **review.started_at** | `2026-08-26T18:01:40-03:00` |
| **review.decided_at** | `2026-08-26T18:01:40-03:00` |
| **Findings** | none blocking — a pre-approval cross-model challenge to the evidence base (3 claims) was refuted against the current repository state; the same pass byte-confirmed the char measurement and the routing numbers. Full reason in the frontmatter `review:` block |
