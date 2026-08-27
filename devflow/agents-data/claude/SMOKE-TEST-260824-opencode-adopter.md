# Smoke test — kit v5.1 as a fresh adopter (OpenCode), 2026-08-24

> **Working notes (§5.12 — `agents-data/`, G32: never citable as governed
> evidence).** Live findings log of the maintainer's first adopter-style
> smoke test of the v5.1 kit: a clean project with the kit copied in,
> OpenCode as the platform, DeepSeek V4 Flash as the MainAgent's model.
> Each finding names its proposed destination; acting on one re-routes it
> into the proper governed artifact (a SPEC, an OQ, a BUG, a README fix).
> Test run by the maintainer; notes kept by Claude at the maintainer's
> request ("segui anotando todo y despues vemos si hay que arreglar algo").

## Context

- Kit state under test: the uncommitted v5.1 batch — ADR-013/014 accepted,
  US-023 rev 3 / US-024 rev 3 / US-025 approved, BOLT-005 (agents/
  examples–squad split) and BOLT-004 (roster-as-enablement reshape,
  V-Bounces 1+2) executed. **US-025's Bolts NOT executed** — the
  MainAgents carry no lifecycle instructions yet and the kit GUARDRAILS
  G07 is not yet scoped (that is US-025.BOLT-005). The test therefore
  measures the **docs-primary baseline**: what a MainAgent achieves from
  the shipped docs alone.
- Test flow so far: version identity → language switch (es-AR) → "help me
  configure my first DevFlow Agent" → pivot to a real team: the maintainer
  as human Architect/TL + a deliberately critical reviewer agent.

## Findings

### F-01 · Nested test folder → wrong MainAgent loaded (environment, resolved)
The first test folder lived INSIDE the maintainer repo; OpenCode resolved
the project at the git root and loaded the **maintainer's** 5.0 MainAgent
as the system prompt while the workspace showed the kit's 5.1 files. The
agent noticed the discrepancy and said "los archivos mandan" (good
instinct), but the test was invalid. Moving the folder out of the repo
fixed it.
**Destination:** an installation note in the kit (README/onboarding):
"install the kit at a project root — never nested inside another repo; the
platform may resolve the parent as the project". Also a US-025
verification note (per-platform project-resolution behavior).

### F-02 · Version self-identification verifies sources (good pattern)
In the clean environment the agent did not trust its prompt header: it
read `devflow/VERSION` (+ LANGUAGE) before answering "5.1". Exactly the
verify-don't-trust reflex the methodology wants.
**Destination:** none (works). Possibly codify in the MainAgent body via
US-025 ("identify your version from devflow/VERSION").

### F-03 · Language policy applied live
`LANGUAGE` switched to `es-AR` mid-test; the agent picked it up, answered
and planned prose in Spanish, kept schema/IDs in English, and offered
English where relevant. §3.15 works as shipped.
**Destination:** none (works).

### F-04 · Docs-primary path VALIDATED (the US-025 AC-8 bet)
With zero lifecycle instructions in its body, the MainAgent autonomously
walked: `actors/` (README → roster.yaml → schema → TEMPLATE → INDEX →
the three examples) → `agents/` (README → squad/ → TEMPLATE-new-role →
examples/reviewer → **VERIFICATION.md**) → §3.0.1 → the GUARDRAILS naming
rules → its own platform skill for the wrapper format — and produced a
correct install plan (squad path, roster listing, INDEX, wrapper with
`task: deny`, schema validation step). The shipped mapping + docs are
self-sufficient.
**Destination:** evidence for US-025's SPECs (the docs-primary path is the
primary path, the body instructions formalize it).

### F-05 · G07 ambiguity resolved silently (THE finding) 🔴
The kit currently disagrees with itself: the actors/agents READMEs say the
executor lifecycle is living data / the human's configuration act, while
the kit GUARDRAILS **G07 is still unscoped** ("no code change without an
approved Bolt"). The agent followed the READMEs and never mentioned a
Bolt — resolving the conflict **silently** in favor of the READMEs. A
stricter agent could just as legitimately have blocked on G07. Neither
behavior is the bug; the **ambiguity** is.
**Destination:** US-025.BOLT-005 (the kit G07 scoping) — this is its
motivating evidence. Until it lands, agent-lifecycle acts in an adopter
project sit in a normative gray zone.

### F-06 · Never-self-enabled behavior held, twice
Both plans (the QA proposal and the team proposal) returned the authority
decisions (`modes`, `approves`, model) to the human explicitly: "los
campos de autoridad los escribís vos por mi intermedio… yo nunca me
auto-habilito". The ADR-014 §3.8 rule — deployed only as kit text, the ADR
being invisible to adopters — governed the agent's behavior.
**Destination:** none (works — the deployment principle demonstrated).

### F-07 · Independence reasoning emerged unprompted
Choosing the reviewer's `approves`, the agent excluded REV ("it would
self-approve its own reviews") and excluded ADR ("the Architect's
checkpoint — the agent critiques, the human signs"), landing on MEM(/DISC)
as the independent-second-pair-of-eyes grants. Nobody taught it that
mapping; it derived it from the independence floor.
**Destination:** none (works). Worth quoting in US-025's pilot evidence.

### F-08 · Multi-role human not modeled (design gap) 🟡
The maintainer asked to be "Arquitecto **y** TL"; the actor file has a
single `role` field. The agent resolved pragmatically (`role: architect`,
noting TL is covered because role routing is guidance). Real gap: one
person, several roles — the methodology allows it, the actor file does not
express it.
**Destination:** candidate OQ (target: the roster family's v2 — NOT
US-024, to avoid G35 friction on its remaining lifecycle) or a v2-hardening
item (e.g. `roles: []` plural). Decide when the batch closes.

### F-09 · Approver ceiling: declared vs enforced (v2 evidence) 🟡
The reviewer plan honored the ceiling declaratively (`write_paths: []`,
no MCPs, read-only wrapper) but proposed `bash` among the tools — a shell
can write regardless of `write_paths`. The enforcement point is the
platform wrapper (`bash: deny`), not the declaration. Claude's
recommendation passed to the maintainer: `bash: deny` in the reviewer
wrapper; minimal `approves: [MEM]` for the first cycle.
**Destination:** the v2 hardening (schema/wrapper-level ceiling
enforcement) — concrete evidence of the declared/enforced gap ADR-014
already flags as v1 debt.

### F-10 · Platform caveats surfaced by the agent itself
It warned unprompted: restart OpenCode so the new agent registers, and
custom-agent registration under headless `opencode run` is unverified
(TUI confirmed). Exactly the kind of per-platform note VERIFICATION.md
exists for.
**Destination:** US-025 verification notes / VERIFICATION.md OpenCode row
when the lifecycle lands.

### F-11 · The worked examples carried the whole flow
The three examples shipped hours earlier (example-human, example-agent,
example-roster) were the agent's pattern source for the real team — the
example team (arq-juan the human architect + a QA agent) is nearly the
maintainer's actual team. `model: inherit` was proposed with the template
comment's reading ("sigue el modelo de la sesión") — a data point for O-2
(inherit = the session's model), still to be settled in US-025.
**Destination:** none for the examples (they work). O-2 stays routed to
US-025 with this data point.

### F-12 · The human tightened authority below the proposal — honored instantly
The maintainer overrode the agent's `approves: [MEM, DISC]` proposal with
"que no apruebe nada por ahora" → the agent produced `modes: [executor]`,
`approves: []` and explicitly restated the consequence: "cero firmas de
IA: todas las aprobaciones quedan en tus manos (safe default)". The
id/name split also worked as designed (`id: critical-reviewer` kebab
identity + `name: "Juancito el criticon"` free label).
**Destination:** none (works — the authority-is-the-human's-act model
functioning under a REDUCTION, not just a grant).

### F-13 · Charter quality from the examples alone
The generated `prompt.md` follows the producer-first structure ("QUÉ
PRODUZCO"), includes steelman-before-objection, justified severity,
"silence is not complicity, but empty objection is not rigor either", and
a never-do list with rubber-stamp and self-approval. All judgment in
prose, zero authority in prose (the ADR-007 separation). Learned from
`agents/examples/reviewer` + the template with no lifecycle instructions.
**Destination:** none (works). Candidate quote for US-025's pilot evidence.

### F-14 · Executor reviewer with `write_paths: []` — production via the Coordinator (design observation) 🟡
The agent resolved a subtle tension: the reviewer PRODUCES REVs (charter)
but carries `write_paths: []` ("los revisores no escriben — los REVs los
registra el Coordinator"). Reading: the subagent returns findings content;
the Coordinator persists the artifact (spawn result = files by the
parent). Coherent with the spawn model, but the "executor that writes
nothing" pattern is not documented anywhere — an adopter could read
`write_paths: []` as "cannot produce".
**Destination:** a clarifying line in the agents/ or actors/ docs (v2 or
US-025's docs Bolt): an executor's production may be persisted by the
Coordinator; `write_paths` bounds the agent's own writes, not its output.

### F-15 · The actor's name leaked into the reusable definition (real defect + docs gap) 🔴
Spotted by the maintainer: the actor file correctly carries
`name: "Juancito el criticon"`, but the DEFINITION (the N:1 reusable
blueprint) got personalized — `agent.yaml`'s description quotes the
actor's name, and the charter opens "Soy Juancito el criticon… reviso los
artefactos que produce Eugenio". A second actor sharing this definition
would introduce itself as Juancito and believe its job is to review
Eugenio specifically — the reuse property (US-024 rule #9) breaks, and the
team composition gets hard-coded into the blueprint. The agent respected
the structural contract (no `name` field invented in agent.yaml) but let
identity leak into prose. In its defense: **no kit doc states the rule**
("definitions are role-generic — an actor's name and team-specific
references never enter the definition; personalization lives in the actor
file"). 50% agent slip, 50% docs gap.
**Destination:** a doc rule in `agents/README` (+ `squad/README`) — fits
US-025's docs Bolt or a small kit fix; F-15b = whether the test agent
applies the de-personalization correction correctly when asked.

### F-16 · The rev-2 schema fix proven end-to-end by a third party 🏆
The team creation completed and validated with the agent's own Python
script (JSON Schema draft 2020-12): **0 errors — including
`eugenio-serrano.yaml`, a human actor with NO `model` and NO `definition`**
(impossible under the rev-1 schema; the exact case the rev-2 discriminator
fixed). The documented v1 consistency rule also ran (both roster ids
resolve to files; the actor's definition pointer resolves to squad/).
Fresh project, different model, no maintainer help.
**Destination:** none (works). Prime evidence for US-025's pilot.

### F-17 · Operational guardrails held without prompting
G34 stated unprompted ("nada se commiteó — necesito tu pedido explícito");
the wrapper was hardened BEYOND the proposal (`task: deny` + no writes +
no MCPs + `webfetch/websearch: deny`); the restart notice + the headless
`opencode run` caveat repeated at delivery. Open check: whether `bash`
ended up `deny` in the wrapper (promised "read-only", not named).
**Destination:** none (works); the bash check pending — if it stayed
allowed, it joins F-09 (declared vs enforced ceiling).

### F-19 · Disk audit of the delivery (Claude, cross-check) — report faithful
Claude audited the test project on disk
(`C:\GitHubRepos\AvengaDevFlow-test\open-code`): every claim in the
MainAgent's delivery report matched the tree — the human actor file in
perfect rev-2 shape (no model/definition, with the explanatory header),
the roster with both actors (example-roster commenting style), the
executor-only actor, the Squad INDEX row ("live (executor-only)"), the
wrapper with `task/edit/write/webfetch/websearch: deny`. Two nuances:
**`bash: ask`** (not `deny`) — F-09 materialized exactly as predicted (a
reviewer needs no shell; "ask" is a defensible human-in-the-loop middle
ground); and F-15 confirmed at 100% **including the wrapper** (it
inherited the personalization via projection — technically good news: the
definition→wrapper projection is faithful, so the fix belongs at the
source + re-project).
**Destination:** F-09 evidence enriched; F-15 fix = de-personalize the
definition and re-project the wrapper.

### F-15b (pending) · The de-personalization correction
The delivery above predates the F-15 correction — the definition still
carries "Juancito el criticon" (and the charter, "Eugenio"). The
correction instruction goes to the test agent next; how it handles it
(touches only the definition, keeps the actor file, understands the N:1
why) is the measurement.

### F-20 · Registration + first spawn CONFIRMED — the spawn topology works as a feature 🏆
After the OpenCode reload the agent did not appear in the Tab picker; the
MainAgent self-diagnosed with the platform (`opencode agent list` →
critical-reviewer registered as subagent with the exact configured
permissions) and explained correctly: **Tab shows primary agents only;
`mode: subagent` is invoked through the Coordinator via the task tool —
which is precisely the methodology's spawn topology (US-023 AC-6)**: the
picker does not offer what the design says must be routed. It then
spawned the reviewer live (visible via ctrl+X) for its first critical
review — of the very configuration package that created it.
**Destination:** VERIFICATION.md OpenCode row — "subagents do not appear
in the Tab picker; visible via ctrl+X / `opencode agent list`; invoked via
the Coordinator's task tool". Plus US-025 pilot evidence: the full
lifecycle (create → roster → install → register → spawn) achieved
docs-primary, before US-025's Bolts exist.

### F-21 · The reviewer's first REV — DELIVERED, and it out-reviewed the humans 🏆🏆
The spawned reviewer produced a full REV of the team-config package:
tiered findings (alto/medio/bajo/mejora), per-finding routing
(gap→Bolt, risk→operativo, doc→aclarar), line-cited evidence, an honest
strengths section, and a one-line actionable verdict ("commit the tree,
pin a different model, raise the charter to the AREV protocol level").
No rubber-stamp, no inflation. It verified empirically (ran
`git rev-parse` → not a repository) and against governed sources, not
summaries. **Findings that flow back to the MAINTAINER's kit backlog:**

1. 🔴 **approves-enum vs "Qualified human" tension** — `roster.schema.yaml`'s
   enum lets a roster grant REV/AREV-*/DISC to an agent while the
   methodology designates those checkpoints to qualified humans — a
   "false affordance" **we shipped today** and four cross-model review
   passes missed. Resolve: restrict the enum or document the boundary.
2. 🎯 **O-2 RESOLVED BY EVIDENCE** — `model: inherit` is not a catalog
   value and the Claude Code projection cannot represent it (N×4
   portability broken); plus the design smell: the reviewer inherits the
   SAME model as the producer it questions ("a model reviewing its own
   work is too complacent", quoting the kit's own AREV README). US-025
   must define inherit's projection handling; guidance: pin a distinct
   model for reviewer-class agents.
3. **The v2 approver-hardening allOf, specified for us**: approver mode ⇒
   tier ∈ {T0,T1}, read-only tools without bash, `mcp_servers: []`,
   `write_paths: []` — plus an enablement checklist in the actor file.
4. **F-14 independently confirmed** (produces REVs, cannot write —
   governed authorship of a Coordinator-transcribed REV is ambiguous).
5. **The commit-is-the-record doc line confirmed needed** — the test
   workspace has no git repo: the enablement is in effect with no audit
   trail. The kit must say: the human's commit completes/records the act.
6. **The kit's `examples/reviewer` charter produces a "revisor light"** —
   no AREV protocol, no Challenger mandates, no read-the-diff cardinal
   rule, no REV severity vocabulary, no gates verification, and no
   prompt-injection defense for the AI-generated material under review.
   The instantiated agent inherited these gaps from OUR example.
7. **Two semantics gaps in the actor contract docs**: human `write_paths`
   (informative vs restrictive mirror — taken literally, the single
   operator couldn't create Bolts/manifests) and human `approves`
   (descriptive go-to list vs restrictive grant — a literal validator
   would block the only human from US/BUG/TC).
8. Minor: wrapper `list: allow` without canonical backing (a real
   projection drift the 0-drift rule caught); T1 declared with no
   external channel (tier honesty); roster.yaml header prose in English
   under content_language es-AR (framework-vs-config language boundary).

**What it did NOT find: F-15.** It read — and even quoted — the
personalized charter line ("que produce Eugenio") without flagging the
N:1 reusability break. The human caught what the agent missed and vice
versa: the complementarity argument for the human+agent team model,
demonstrated empirically in the first cycle.

**Destination:** items 1–3 + 6 → US-025's SPECs / the v2 hardening / an
OQ for the enum boundary; 4–5 + 7–8 → kit doc fixes (candidates for the
US-025 docs Bolt); the pin-a-model guidance → reviewer-class doc note.
Test-project actions (the adopter's own): init git + commit the package,
pin the reviewer's model, enrich the charter, fix the list drift.

### F-22 · The MainAgent honored the REV pause unprompted — the protocol closes 🏆
Relaying the reviewer's verdict, the MainAgent stopped at the mandatory
review checkpoint on its own: "los hallazgos son borrador hasta que vos
definas el plan" (AITL pause point: after review findings → present →
wait for the human's plan), offered to formalize the review as REV-001
with its `AITL-REV-Approval` and per-finding routing, and presented a
sensible options menu (init git+commit / enrich the charter / pin a
distinct model / run the end-to-end Bolt cycle / formalize REV-001). The
smoke test has now exercised, docs-primary and unprompted: identity,
language policy, the create/install lifecycle, the enablement act, the
safe default, spawn topology, a real subagent review, and the REV
protocol's draft-until-approved discipline.
**Destination:** US-025 pilot evidence (the closing exhibit).

### F-23 · Context isolation confirmed — and the charter is the only guaranteed context
The maintainer asked whether the subagent shares the parent's context.
Evidence says no: the reviewer re-read from disk everything the MainAgent
had already read (GUARDRAILS, the methodology sections, the REV/AREV
READMEs, the INDEXes) — a spawned agent starts fresh with only (1) its
wrapper body as system prompt and (2) the Coordinator's task prompt. The
methodology does not travel; it lives in the repo and each agent
reconstitutes it by reading. **Feature:** true fresh eyes — a reviewer
sharing the parent's context would inherit its blind spots; isolation is
what makes the REV credible. **Cost:** every spawn re-reads (tokens +
latency — the observed "thinking a lot"). **Design lever:** the charter
must CARRY the mandatory reading list ("before reviewing, read GUARDRAILS
+ reviews/README + the AREV protocol") so context reconstitution is
contract, not model diligence — folds into the charter-enrichment fix
(the reviewer's own "alto" finding).
**Destination:** the kit's example charters + TEMPLATE-new-role (a
"context to load" section); US-025 spawn-economics note.

### F-18 (pending) · The end-to-end cycle
Proposed by the MainAgent itself: a minimal non-functional Bolt under
US-000 through the whole chain (Bolt → READY → SPEC → SPEC-Approval →
V-Bounce → MEM → MEM-Approval → BOLT-DONE), with the reviewer agent
producing a critical REV of the package before the human signs — and the
future approver grant correctly described as the human's own actor-file
edit. To run after the restart + /agent registration check.

### F-24 · One malformed wrapper bricks the whole OpenCode session (pre-pilot observation) 🟡
Launching `opencode` in the OLD test folder failed to start entirely:
"Configuration is invalid at .opencode/agents/socrates-agent.md" — a
leftover wrapper (created in a session under the OLD kit) whose permission
block used **booleans and path-arrays** (`read: true`, `edit: false`,
`write: ["…/**"]`) where OpenCode expects `allow/ask/deny` rule configs.
Two takeaways: (1) **the drift class F-14 predicted, observed in the
wild** — the old kit had no permission-derivation spec, so the MainAgent
improvised a plausible-but-invalid format; the NEW kit's VERIFICATION.md
derivation rule (BOLT-002) prevents exactly this. (2) **New failure mode:
a single invalid wrapper makes the whole project session unstartable** —
candidate VERIFICATION.md note (OpenCode row: "an invalid agent file
blocks startup — validate/remove it, the config error names the file")
and extra motivation for the delete-safe contract's orphan-repair path.
**Destination:** a VERIFICATION.md platform note (fits the pilot's
findings routing or a docs Bolt); the F-14 validation recorded as pilot
context.

### F-25 · Pilot LEG 1 (the philosopher squad): the reviewer-class deny clause partially applied 🟡
The second test's MainAgent created three agents (socrates/reviewer,
aristoteles/qa, platon/architect) — authority PERFECT ×3 (executor-only
drafts), four legs consistent, wrappers actor-id-named with VALID enum
permissions (the Socrates-revenge: F-14's derivation rule field-proven
against the old boolean-format brick). ONE real finding: the B.1
reviewer-class override was partially applied to socrates — task/webfetch
deny ✓ but bash/edit/write came out `ask` (the clause says deny), and
`websearch` is missing from the denies. Two-layer root: the DEFINITION's
allowlist is too broad for a reviewer (declares bash/edit/write while its
own charter says "REVs never modify code"), and the projection mapped the
allowlist without the class override. Note: "I am Socrates" in the charter
is COMPLIANT (the definition's own id — a persona-definition; no actor
display names, no human names). Also observed: `model: inherit` ×3 — the
pin-a-distinct-model guidance for reviewer-class not applied/mentioned
(guidance, not rule; soft observation).
**Destination:** the pilot MEM's findings list (BOLT-004) → routes per the
REV protocol (likely: the charter-enrichment Bolt gains "a reviewer's
tools allowlist excludes write-class tools"; the derivation rule's
class-override wording may need sharpening).

## Pending governance (so nothing gets lost while testing)

- `AITL-MEM-Approval` for MEM-260824-0125 (BOLT-004 V-Bounce 2 — the
  examples) — **still pending**.
- `AITL-BOLT-DONE-Approval` ×2 (BOLT-004, BOLT-005).
- US-025: approved, 5 candidate Bolts, none created yet — the test
  findings above feed their SPECs.
- Nothing committed — the whole v5.1 batch is working tree.
