---
id: "REV-005"
title: "DevFlow Agents v5.1 — adopter smoke-test review (OpenCode): the kit as a fresh adopter experiences it"
date: "2026-08-24"
author: "eugenio.serrano"
llm: "claude-fable-5"
status: "approved"        # draft | approved | closed — findings actionable, routing in progress
scope: "The v5.1 DevFlow Agents kit deliverables (actors/ + agents/ families, roster.schema.yaml, the four MainAgents, VERIFICATION.md, kit GUARDRAILS) as exercised by a fresh adopter project"
methodology: "Live adopter smoke test (OpenCode, fresh project outside the repo, DeepSeek V4 Flash as the MainAgent's model): version identity → language switch → team configuration (one human + one reviewer agent) → wrapper install → subagent spawn → the spawned reviewer's own REV of the package; plus Claude's independent disk audit of every claim"
reviewed_artifacts:
  - "distribution-kit/devflow/actors/ (roster.yaml, roster.schema.yaml, TEMPLATE-ACTOR.yaml, README, INDEX, examples/)"
  - "distribution-kit/devflow/agents/ (README, INDEX, VERIFICATION.md, TEMPLATE-new-role/, examples/, squad/)"
  - "distribution-kit/devflow/GUARDRAILS.md (G07 as shipped)"
  - "distribution-kit/CLAUDE.md + the three platform MainAgents (the enablement clause)"
  - "distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md §3.0.1"
adrs_checked:
  - "devflow/adrs/ADR-014-actors-roster-is-the-enablement.md"
  - "devflow/adrs/ADR-013-agent-lifecycle-governance.md"
  - "devflow/adrs/ADR-007-devflow-agent-identity-model.md"
  - "devflow/adrs/ADR-010-actor-grammar-and-pure-v5-vocabulary.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
specs_checked:
  - "devflow/spec/SPEC-260824-0050-agents-examples-squad-split.md"
  - "devflow/spec/SPEC-260824-0054-roster-as-enablement-reshape.md"
review_ready_at: "2026-08-24T02:14:54-03:00"
review: # AITL-REV-Approval — decision dictated in conversation ("aprobado") and transcribed by the agent (§3.0)
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "architect"
      model: null
  started_at: "2026-08-24T10:14:32-03:00"
  decided_at: "2026-08-24T10:14:32-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved as Architect/TL after full reconciliation against the smoke-test session (the maintainer ran the adopter test personally and verified the log→REV mapping; the charter-language rule in F-15 was confirmed and made explicit during this review). The 17 findings and their §6 routing plan are actionable: 2 OQs + 3 candidate doc/charter Bolts as net-new artifacts; everything else lands in already-planned work (US-025's Bolts, the ADR-014 v2 backlog). Downstream artifacts follow their own lifecycles — this approval approves none of them (T10)."
tags: ["devflow-agents", "smoke-test", "adopter", "opencode", "v5.1", "roster-enablement", "lifecycle"]
---

<!--
  LANGUAGE POLICY (§3.15): prose in English (ADR-012 — every methodology
  artifact of this repository is written in English).

  ⚠️ AITL-REV-Approval (§2.14, §3.0): findings remain DRAFT until a
  qualified human records AITL-REV-Approval. Approval does NOT approve any
  downstream artifact. Code-related outcomes still require an approved Bolt
  (T10 — never REV → SPEC directly).

  Informative annex (G32 — never a governed source): the raw session notes
  live at devflow/agents-data/claude/SMOKE-TEST-260824-opencode-adopter.md.
  Every finding below stands on its own evidence (kit file + observed
  behavior); the annex is background only.
-->

# REV-005 — DevFlow Agents v5.1: adopter smoke-test review

| Field           | Value |
|-----------------|-------|
| **Scope**       | The v5.1 DevFlow Agents kit as a fresh adopter experiences it (actors/ + agents/ + MainAgents + GUARDRAILS + VERIFICATION) |
| **Methodology** | Live adopter smoke test on OpenCode (fresh project, third-party model) + independent disk audit; the spawned reviewer agent's own findings were re-verified against the kit sources before inclusion |
| **Criteria**    | ADR-014 (roster enablement), ADR-013 (lifecycle + ship model), ADR-007/010 (identity/grammar), ADR-004 (self-containment), the kit's own GUARDRAILS and §3.0.1 |

---

## 1. Purpose

First end-to-end exercise of the v5.1 DevFlow Agents delivery from the
adopter's seat: can a MainAgent, with **no lifecycle instructions in its
body** (US-025 not yet implemented) and the maintainer's ADRs invisible,
configure a real team — a human Architect/TL plus a critical reviewer
agent — install it, spawn it, and stay inside the governance rails, using
only what the kit ships? The test both **validates** the deployed
mechanism (the roster-as-enablement norm reached the agent through kit
text alone) and **surfaces** the gaps that survive in the shipped surface.
Verifying is the point: several findings below were produced by the
spawned reviewer agent itself and independently re-verified against the
kit files before being adopted here.

---

## 2. Artifacts reviewed

| Artifact | Files | Notes |
|----------|-------|-------|
| The roster family | `actors/` — roster.yaml, roster.schema.yaml, TEMPLATE-ACTOR.yaml, README, INDEX, examples/ (×3) | The enablement mechanism surface |
| The agents family | `agents/` — README, INDEX, VERIFICATION.md, TEMPLATE-new-role/, examples/ (×5), squad/ | The definition/lifecycle surface |
| The four MainAgents | kit `CLAUDE.md`, `SKILL.md`, `AvengaDevFlow.agent.md`, `AvengaDevFlow.md` | The enablement clause; the (absent) lifecycle capability |
| Kit GUARDRAILS | `GUARDRAILS.md` | G07 as shipped (unscoped) |
| Methodology | `avenga-devflow/Avenga-DevFlow.md` §3.0.1 | The safe default + enablement wording |

---

## 3. Severity legend

| Category | Meaning |
|----------|---------|
| **Compliant** | Implemented correctly per ADR / standard |
| **Documented deviation** | Justified difference, recorded (here: the ADR-014 v1 debts) |
| **Minor gap** | Inconsistency without functional impact, reduces quality |
| **Major gap** | Problem that can cause governance errors or security exposure |

---

## 4. Findings

### 4.1 — The enablement mechanism (actors/ + schema + GUARDRAILS)

#### F-01 [Major gap] — The `approves` enum grants what the methodology reserves for humans

**Location:** `distribution-kit/devflow/actors/roster.schema.yaml` (the
`approves` items enum) vs `avenga-devflow/Avenga-DevFlow.md` (the
checkpoint table: `AITL-DISC/REV/AREV-*-Approval` → "Qualified humans").

**Actual:** the enum accepts `DISC`, `REV`, `AREV-CRITIQUE`,
`AREV-DEFENSE`, `AREV-VERDICT` for any actor — a roster entry granting an
agent `approves: [REV]` is schema-valid.

**Expected:** either the methodology's human designation for those
checkpoint classes is a hard boundary (then the enum, or a schema rule,
must exclude them for agent actors), or it is routing guidance (then the
boundary must be documented so a grant is a conscious act, not a false
affordance).

**Impact:** a future "enable the reviewer for REVs" would be schema-valid
and methodologically dubious — the safe default's validity gate would
bless a grant the methodology arguably forbids. Found by the spawned
reviewer; verified against both files.

**Recommendation:** open question first (is the human designation for
DISC/REV/AREV normative or guidance?), then the schema/doc fix its answer
dictates.

---

#### F-02 [Major gap] — Kit G07 still unscoped: the READMEs and the guardrail disagree

**Location:** `distribution-kit/devflow/GUARDRAILS.md` (G07) vs
`actors/README.md` ("living data" / the human's configuration act) and
`agents/README.md` (the executor governance row).

**Actual:** the READMEs teach that executor agent lifecycle is living
data (no Bolt); G07 still reads "no code change without an approved Bolt"
with no lifecycle exception. In the test the MainAgent followed the
READMEs and never mentioned a Bolt — resolving the conflict **silently**.
A stricter agent could just as legitimately have blocked.

**Expected:** the G07 scoping decided by ADR-013 expressed in the kit
GUARDRAILS (the ADR is invisible to adopters — the kit text is the only
norm they have).

**Impact:** every adopter's agent-lifecycle act currently sits in a
normative gray zone; behavior depends on which text the agent weighs more.

**Recommendation:** this is exactly **US-025.BOLT-005** (already planned);
this finding is its motivating field evidence — no new artifact needed.

---

#### F-03 [Minor gap] — "The git history is the record" — but nothing says the record requires a commit

**Location:** `actors/roster.yaml` header, `actors/README.md` (the
enablement section) — verified empirically: the test workspace was not a
git repository, so the enablement was in effect with **no audit trail**.

**Actual:** the enablement text promises the git history as the record of
the human's configuration act; nothing tells the adopter that the act's
record materializes only when the human commits (and G34 guarantees the
agent will never commit it for them).

**Expected:** one line in `roster.yaml`'s header + the README: *the
grant's record is your commit — an uncommitted grant has no audit trail;
committing the roster change completes the act* (the human's commit is,
in effect, the signature).

**Impact:** an adopter can run indefinitely with enablements whose
authorship is unprovable.

**Recommendation:** doc fix (actors family) — one candidate docs Bolt.

---

#### F-04 [Minor gap] — Human `approves` semantics: descriptive or restrictive?

**Location:** `actors/README.md` (resolution rules — the agent-holder
restriction is stated; the human reading is not) + `roster.schema.yaml`
(requires `approves` for every actor).

**Actual:** the examples treat a human's `approves` as the "go-to
approver" list (descriptive), but nothing says a literal resolver must
not treat it as a grant boundary — read restrictively, the test's single
human (approves: [ADR, BOLT-READY, SPEC, MEM, BOLT-DONE]) could not sign
US/BUG/TC/DISC/REV, which as the only human they must.

**Expected:** an explicit line: a human's `approves` is routing guidance,
never a restriction (role routing is guidance; humans may approve any
checkpoint they are qualified for); only an **agent's** `approves` is a
hard grant.

**Impact:** a future validator or a strict agent could wrongly refuse a
human approval.

**Recommendation:** doc fix (actors README + a schema comment) — same
docs Bolt as F-03.

---

#### F-05 [Minor gap] — `write_paths` semantics: informative mirror or enforced restriction?

**Location:** `agents/README.md` (the contract table: "write-scope
mirror") + the worked examples.

**Actual:** the field's force is undefined. Read restrictively, the
test's human (write_paths: adrs/spec/memory) could not create Bolts,
BUGs, TCs or manifests — the heart of their work. Also unstated: an
executor's production may be persisted by the Coordinator (the spawned
reviewer "produces REVs" with `write_paths: []` — the reviewer itself
flagged the ambiguity of governed authorship in a transcribed REV).

**Expected:** the contract states (a) `write_paths` bounds the agent's
own direct writes, not its output (the Coordinator may persist an
executor's production, recording authorship), and (b) for humans it is
informative.

**Impact:** ambiguity in the one field the approver ceiling leans on.

**Recommendation:** doc fix (agents README contract table) — same docs
Bolt.

---

#### F-06 [Minor gap] — A human with several roles cannot be expressed

**Location:** `actors/TEMPLATE-ACTOR.yaml` / `roster.schema.yaml` —
single `role` field.

**Actual:** the maintainer-as-adopter asked to be "Architect AND Tech
Lead"; the actor file models one role. The MainAgent resolved pragmatically
(`role: architect`, noting routing guidance covers the rest) — reasonable,
but the model is not expressed.

**Expected:** the methodology allows one person to hold several roles
(§3.0 role routing); the roster should be able to say it (e.g. a plural
`roles:` in the v2 shape) or document the convention.

**Impact:** lookups by role miss the second hat.

**Recommendation:** open question for the roster v2 shape — deliberately
NOT targeting US-024/US-025 (G35: an open OQ must not block their
remaining lifecycle); target the future v2-hardening scope.

---

### 4.2 — Agent definitions and charters (agents/)

#### F-07 [Major gap] — The shipped reviewer example produces an under-armed reviewer

**Location:** `agents/examples/reviewer/` (agent.yaml + prompt.md), as
instantiated by the test.

**Actual:** the charter the adopter's agent inherited promises an
adversarial reviewer but operationalizes none of the methodology's own
techniques: no AREV protocol awareness (Critique→Defense→Verdict), no
read-the-diff-not-the-summary cardinal rule, no REV severity vocabulary,
no gates verification, and — the genuinely adversarial blind spot — **no
prompt-injection defense for the AI-generated material under review**
(the kit lists prompt-injection as an AI-native gate; a reviewer is the
prime injection target). Compounding it: a spawned agent starts with an
empty context (verified — the test reviewer re-read the methodology from
disk), so **the charter is the only guaranteed context**, yet it carries
no mandatory reading list.

**Expected:** the reviewer example (and TEMPLATE-new-role) operationalize
the role: the REV/AREV protocol references, the read-the-diff rule, the
severity vocabulary, gates verification, an anti-injection stance toward
reviewed content, and a "context to load before acting" section.

**Impact:** every adopter instantiating the example gets a governance
reviewer, not a critical one — "the letter of the contract, not the
spirit of the role" (the spawned reviewer's own verdict about itself).

**Recommendation:** candidate charter-enrichment Bolt under US-023 (the
family owner); applies to all five examples where relevant, deepest for
reviewer.

---

#### F-08 [Minor gap] — Nothing says definitions are role-generic (an actor's name leaked into the blueprint)

**Location:** observed in the test (`squad/critical-reviewer/` carried
the actor's display name and the human's name in description + charter;
the projection faithfully propagated it to the wrapper); no kit doc
states the rule.

**Actual:** the docs establish N:1 reuse ("two architects may share one
definition") and actor-level naming, but never say the inverse rule: **a
definition never carries an actor's name or team-specific references** —
personalization lives in the actor file. Notably, the spawned reviewer
read and even quoted the leaked line without flagging it (the human
caught it) — humans and agents catch different defects.

**Expected:** the rule stated in `agents/README.md` + `squad/README.md`
(and a hint in TEMPLATE-new-role).

**Impact:** a second actor sharing the definition would introduce itself
as the first one and inherit hard-coded team assumptions; N:1 reuse
silently breaks.

**Recommendation:** doc fix — same docs Bolt family as F-03/F-04/F-05.

---

#### F-09 [Minor gap] — `model: inherit` is not projectable and undermines reviewer independence

**Location:** `actors/TEMPLATE-ACTOR.yaml` + `examples/example-agent.yaml`
(`model: inherit`) vs `agents/VERIFICATION.md` (the Claude Code
projection maps `model:` to concrete frontmatter).

**Actual:** `inherit` is not a catalog value — the per-platform
projection cannot represent it (N×4 portability broken at install time).
And for reviewer-class agents it is the wrong default anyway: the
reviewer runs the same model as the producer whose work it questions
("a model reviewing its own work is too complacent" — the kit's own AREV
README). This settles the previously open question on `inherit`
semantics with field evidence.

**Expected:** US-025's per-platform install work defines `inherit`
handling (resolve at projection time to the session's model, per
platform), and the docs recommend pinning a **distinct** model for
reviewer/approver-class agents (model diversity as the cheapest
skepticism lever, aligning with the `high`-risk model-hardening rule).

**Impact:** installs fail or improvise per platform; review credibility
weakened by default.

**Recommendation:** route to US-025 (the per-platform Bolt's SPEC) + one
guidance line in the actors/agents docs.

---

#### F-10 [Minor gap] — Capability tier honesty: T1 declared with no external channel

**Location:** `agents/examples/*/agent.yaml` pattern, observed in the
instantiated reviewer (tier T1, `mcp_servers: []`, web tools denied).

**Actual:** T1 promises read-only external reach; the shipped shape
provides none (the only escape is shell, which the ceiling discourages).
A reviewer that must verify claims against sources cannot.

**Expected:** either the examples declare an honest T0, or the docs show
how a T1 agent gets its read-only channel (an allowlisted docs MCP).

**Impact:** tiers stop meaning anything if the declared tier and the
granted tools diverge.

**Recommendation:** doc/example fix — same docs Bolt family.

---

### 4.3 — The approver ceiling (v1 debt, evidence attached)

#### F-11 [Documented deviation] — The ceiling is declared, not enforced (accepted v1 debt — now with field evidence)

**Location:** ADR-014 §3.6/§4 (the accepted v1 trade-off) — observed: the
wrapper kept `bash: ask` for a reviewer; a future `modes: [approver]`
upgrade would pass the schema with bash and write tools intact.

**Actual:** exactly what ADR-014 §4 lists as v2 follow-up — recorded here
because the test produced the concrete hardening spec: *approver mode ⇒
tier ∈ {T0,T1} + read-only tools without shell + `mcp_servers: []` +
`write_paths: []`*, plus an enablement checklist in the actor file.

**Expected (v2):** the above as schema `allOf` + wrapper-permission
mapping.

**Impact:** none new for v1 (the deviation is governed); the evidence
de-risks the v2 design.

**Recommendation:** attach to the ADR-014 v2-hardening backlog (the
future hardening US inherits this spec); no new artifact now.

---

### 4.4 — Platform and install surface (VERIFICATION)

#### F-12 [Minor gap] — No install-location guidance (nested-install contamination)

**Location:** kit README / onboarding (absent note) — observed: a test
project nested inside another DevFlow repo made the platform resolve the
parent as the project and load the parent's MainAgent (wrong version)
while showing the kit's files.

**Expected:** one installation note: *install the kit at a project root —
never nested inside another repository; the platform may resolve the
parent as the project.*

**Recommendation:** doc fix — same docs Bolt family (or the kit README).

---

#### F-13 [Minor gap] — OpenCode platform notes missing from VERIFICATION.md

**Location:** `agents/VERIFICATION.md` (OpenCode row).

**Actual:** three behaviors the test established are undocumented:
subagents do **not** appear in the Tab picker (primary agents only) — they
are visible via ctrl+X / `opencode agent list` and invoked through the
Coordinator's task tool (which is the spawn topology working as designed);
a session reload is required to register a new agent; custom-agent
registration under headless `opencode run` is unverified (TUI confirmed).

**Recommendation:** VERIFICATION.md additions — natural home in US-025's
per-platform Bolt.

---

#### F-14 [Minor gap] — The projection's permission set is under-specified (drift observed)

**Location:** `agents/VERIFICATION.md` (the OpenCode mapping) — observed:
the projected wrapper gained `list: allow` with no canonical backing in
the definition's tools allowlist (the kit's own 0-drift rule flags it).

**Expected:** the mapping pins the exact permission block derivation
(tool allowlist → permission entries, the deny-set for approver-adjacent
agents) so two projections of the same definition cannot differ.

**Recommendation:** route to US-025's per-platform Bolt (the mapping is
its deliverable).

---

#### F-15 [Minor gap] — The framework-vs-config language boundary is undeclared

**Location:** `actors/roster.yaml` (shipped header prose in English) vs
the adopter's `LANGUAGE` (es-AR in the test) — found by the spawned
reviewer.

**Actual:** the kit ships framework files (READMEs, templates, the
roster skeleton's header comments) in English; when an adopter sets a
different `content_language`, nothing says which shipped text is
framework (stays English) and which is project prose (follows LANGUAGE).
The reviewer flagged the roster header as inconsistent; the sounder
reading is that shipped framework text stays English — but that reading
is nowhere stated.

**Expected:** the boundary stated in the language policy (or the
actors/agents READMEs), with the agent-prompt rule explicit —
maintainer-confirmed during this review:
- shipped framework text (`agents/examples/*/prompt.md`, READMEs,
  templates, skeleton headers) is **English** — copied as starting
  points, superseded on upgrade;
- **the project's live charters (`agents/squad/<id>/prompt.md`) follow
  `content_language`** — they are prose the project writes AND the
  agent's system prompt, so the project language makes the agent think
  and answer in it (the test's MainAgent already did this unprompted:
  the reviewer's charter came out in es-AR);
- structured fields (`agent.yaml` keys, enums, ids) stay English (§3.15
  — the schema is never translated).

**Impact:** adopters may "fix" framework files by translating them —
breaking the §5.16 supersede-on-upgrade model.

**Recommendation:** doc line — same docs Bolt family as F-03/F-04.

---

#### F-16 [Minor gap] — No guidance for the single-operator's independent-review gap

**Location:** kit ONBOARDING / the actors/README single-maintainer
section — found by the spawned reviewer as an improvement.

**Actual:** REV/AREV are optional by design; with one human producing and
approving everything, work can reach BOLT-DONE with no second opinion.
The reviewer's suggestion: a team convention — REV before BOLT-DONE (or
AREV at high/critical) — with a reviewer agent making it cheap.

**Expected:** a recommendation (never a gate) in the single-maintainer
guidance: with a reviewer agent in the squad, ask for its REV before
acceptance.

**Impact:** none normative — adoption-quality guidance.

**Recommendation:** doc line — same docs Bolt family as F-03/F-04.

---

#### F-17 [Minor gap] — Agent-review economics are unmeasured

**Location:** methodology §3.0 review-time budgets (written for humans) —
observed: the spawned reviewer's first REV took several minutes of
reading/thinking (it reconstitutes the methodology from disk on every
spawn — context isolation's cost).

**Expected:** US-025's pilot records agent-review latency/depth as a
datapoint so budgets (and spawn-frequency guidance) can be calibrated for
agent reviewers.

**Impact:** none today; unpriced reviews could surprise adopters at scale.

**Recommendation:** a metrics note in US-025's pilot Bolt — no new
artifact.

---

### 4.5 — Compliant (validated in the field, recorded for the pilot)

#### C-01 [Compliant] — The docs-primary lifecycle works end-to-end
With zero lifecycle instructions in its body, the MainAgent navigated
actors/ + agents/ + VERIFICATION.md + the templates and executed
create → roster → install → register → spawn correctly. US-025 AC-8's
docs-primary bet validated before US-025 exists.

#### C-02 [Compliant] — Never-self-enabled held under grant AND reduction
The agent returned every authority decision to the human (three separate
times), implemented an authority **reduction** faithfully
(executor-only), and restated the safe-default consequence unprompted.

#### C-03 [Compliant] — The rev-2 schema validated by a third party
A human actor file with no `model`/`definition` passed the adopter's own
JSON Schema validation (0 errors), with the v1 approver⇒approves rule and
the agent⇒model discriminator behaving exactly as designed.

#### C-04 [Compliant] — Spawn topology works as a feature
`mode: subagent` + `task: deny` produced precisely the designed
affordance: the reviewer is not casually selectable, only
Coordinator-routed; identities consistent across definition ↔ actor ↔
wrapper (body byte-identical with the charter).

#### C-05 [Compliant] — The REV discipline held unprompted
The spawned reviewer produced tiered, line-cited, routed findings with an
honest strengths section (no rubber-stamp, no inflation); the MainAgent
then paused at the review checkpoint on its own ("findings are draft
until you define the plan") and offered the governed formalization.

#### C-06 [Compliant] — Faithful reporting
An independent disk audit matched every claim in the MainAgent's delivery
report; G34 (no commit without explicit request) stated unprompted.

#### C-07 [Compliant] — Identity, language and independence reflexes
The MainAgent verified `devflow/VERSION` before declaring its version
(sources over prompt); applied the live `LANGUAGE` switch correctly
(prose es-AR, schema English); and the spawned reviewer derived
independence boundaries unprompted (excluded REV from its own grants —
"it would self-approve its own reviews" — and left ADR as the human's
signature).

---

## 5. Summary

The v5.1 DevFlow Agents delivery **works as designed where it was
deployed**: the roster-as-enablement norm, the safe default, the
never-self-enabled rule, the spawn topology and the rev-2 schema all
governed a third-party agent's behavior through kit text alone — the
deployment principle (maintainer ADRs invisible; the kit carries the
norm) is demonstrated. The gaps are concentrated where the norm has
**not yet been deployed** (G07 scoping — US-025.BOLT-005), where texts
under-specify semantics (commit-as-record, approves/write_paths force,
role-generic definitions, tier honesty, `inherit`), and in one genuine
boundary question the schema and the methodology answer differently
(agent-grantable DISC/REV/AREV). Nothing found is architecturally
blocking; three findings are Major — F-01 and F-02 because they sit on the
approval-integrity path, F-07 because every adopter instantiating the
shipped example inherits an under-armed reviewer.

---

## 6. Action plan

> Applies only after `AITL-REV-Approval`. Each destination follows its own
> lifecycle and AITL approval (code → approved Bolt first, T10).

| # | Finding | Severity | Action | Routes to |
|---|---------|----------|--------|-----------|
| 1 | F-01 enum vs human designation | Major | **RESOLVED at routing (maintainer decision, 2026-08-24):** the checkpoint table's owner designation — "Qualified humans" included — is **routing guidance**; the roster grant decides. Any actor, human or agent, may be granted DISC/REV/AREV-* by the team's configurator. The enum stays as shipped; the independence ladder and the critical/regulatory human-only ceiling remain untouched. What remains is the doc note stating this reading | Doc note → **the US-024 docs Bolt** (no OQ) |
| 2 | F-02 kit G07 unscoped | Major | Express the ADR-013 scoping in kit GUARDRAILS | **US-025.BOLT-005** (already planned — this finding is its evidence; no new artifact) |
| 3 | F-03 commit-is-the-record | Minor | Doc line in roster.yaml header + actors/README | **Candidate docs Bolt under US-024** (actors-family semantics, batched with #4/#5) |
| 4 | F-04 human approves semantics | Minor | "Guidance, never restriction" line + schema comment | same docs Bolt as #3 |
| 5 | F-05 write_paths semantics | Minor | Contract table clarification (own-writes bound; Coordinator may persist executor output) | **Candidate docs Bolt under US-023** (agents-family contract, batched with #6/#8) |
| 6 | F-08 role-generic definitions rule | Minor | The rule in agents/README + squad/README + template hint | same docs Bolt as #5 |
| 7 | F-06 multi-role human | Minor | **RESOLVED at routing (maintainer decision, 2026-08-24):** plural **`roles: []`** adopted for the **v2 roster shape** (schema + template + examples + resolution rules together); the single primary `role` stands meanwhile (role routing guidance covers the extra hats) | **ADR-014 §4 v2 backlog** (with F-11; no OQ) |
| 8 | F-07 reviewer charter under-armed | Major | Operationalize the example charters (+ "context to load" in TEMPLATE-new-role) | **Candidate charter Bolt under US-023** |
| 9 | F-09 model: inherit | Minor | Define projection handling + pin-a-distinct-model guidance for reviewers | **US-025** per-platform Bolt SPEC (+1 doc line) — closes the open `inherit` question |
| 10 | F-10 tier honesty | Minor | Honest T0 in examples or show the T1 channel | same docs Bolt as #5 |
| 11 | F-11 ceiling enforcement | Documented deviation | Attach the field-derived allOf spec to the v2 hardening | **ADR-014 §4 backlog** (future hardening US — no new artifact now) |
| 12 | F-12 install-location note | Minor | One-line install warning | same docs Bolt as #3 (or the kit README) |
| 13 | F-13 OpenCode platform notes | Minor | VERIFICATION.md OpenCode row additions | **US-025** per-platform Bolt |
| 14 | F-14 projection permission spec | Minor | Pin the permission-block derivation in the mapping | **US-025** per-platform Bolt |
| 15 | F-15 framework-vs-config language boundary | Minor | One line in the language policy / family READMEs | same docs Bolt as #3 |
| 16 | F-16 single-operator review convention | Minor | Recommendation (never a gate) in the single-maintainer guidance | same docs Bolt as #3 |
| 17 | F-17 agent-review economics | Minor | Record latency/depth in the pilot; calibrate guidance | **US-025** pilot Bolt (metrics note) |

Net new artifacts: **3 candidate Bolts** — **1 under US-024**
(#1/#3/#4/#12/#15/#16 — the enablement-semantics doc pass, now including
the F-01 guidance-reading note) + **2 under US-023** (docs-contract
#5/#6/#10 and charters #8). **Zero OQs** — both boundary questions were
resolved by maintainer decision at routing (rows 1 and 7). Everything
else lands in already-planned work (US-025's Bolts, the ADR-014 v2
backlog — which now carries plural `roles: []` alongside the ceiling
enforcement).

---

## 7. Conclusions

The smoke test is a **pass with homework**: the governance core behaved
exactly as decided (ADR-013/014 deployed through the kit and obeyed by a
model that never saw them), and every gap found has a natural home in
work that is already approved or in small, well-bounded doc/charter
Bolts. Recommendation: approve the findings, open the two OQs, create
the three candidate Bolts after US-025's Bolts land (they touch the same
files — sequencing avoids collisions), and let US-025's SPECs cite this
REV as approved evidence. A second review cycle is warranted only after
US-025 delivers, ideally repeating this same adopter test plus the
end-to-end Bolt cycle the test left pending.

---

## 8. AITL-REV-Approval

> **Avenga DevFlow §2.14, §3.0.** This Review remains a draft until a
> qualified human records `AITL-REV-Approval` (in the `review` frontmatter
> block). Approval makes the findings actionable; it does not approve any
> downstream artifact.

| Field | Value |
|-------|-------|
| **Reviewer** | eugenio.serrano (architect / tech_lead) |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-24T02:14:54-03:00` |
| **review.started_at** | `2026-08-24T10:14:32-03:00` |
| **review.decided_at** | `2026-08-24T10:14:32-03:00` |
| **Findings** | none on the review itself — the 17 findings + §6 routing approved as actionable (reason in the frontmatter `review:` block) |

---

## 9. History

| Date | Change | Author |
|------|--------|--------|
| 2026-08-24 | Initial review (draft) — findings from the OpenCode adopter smoke test, incl. the spawned reviewer's own re-verified findings | eugenio.serrano (agent-drafted) |
| 2026-08-24 | F-15/F-16/F-17 + C-07 added (full log reconciliation); the charter-language rule made explicit in F-15 (maintainer-confirmed) | eugenio.serrano (agent-drafted) |
| 2026-08-24 | AITL-REV-Approval recorded — findings actionable, routing in progress | eugenio.serrano |
| 2026-08-24 | Routing decisions: F-01 resolved (owner designation = guidance; any actor may be granted DISC/REV/AREV — the roster decides; enum stays) · F-06 resolved (plural `roles: []` → v2 backlog). Both OQs dissolved | eugenio.serrano |
| 2026-08-24 | Count reconciliation (cross-model post-approval check): the §5 prose said "two findings are Major" while the finding headers and the §6 routing table — the authoritative severity record, unchanged — say three (F-01, F-02, F-07). The prose and the INDEX corrected to **3 Major · 13 Minor · 1 Documented deviation (+7 Compliant)**; no finding, severity or routing changed | eugenio.serrano (agent-applied) |
