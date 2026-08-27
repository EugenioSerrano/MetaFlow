# Changelog — Avenga DevFlow

Change log for the documentation framework itself.
This file documents the evolution of the structure, templates,
conventions and flows of Dev Flow.

> **Format:** Each entry includes date, description and affected files.
> Ordered from most recent to oldest.
>
> **Version headings** are `MAJOR.MINOR`, matching `devflow/VERSION`. Three
> historical formats coexist and are preserved as written, never rewritten:
> `[3.0.0]` and `[2.0.0]` predate the move to two-part numbering, and the
> entries below `[2.0.0]` are dated-only because they predate versioning
> altogether. A changelog is a record; correcting its past headings would
> falsify it.

---

## [5.0 migration] — 2026-08-23 — This repository executed §5.16: installed devflow 4.2 → 5.0

**First migration to a v5-major release.** This repository upgraded its own
installed `devflow/` from 4.2 to the released **v5.0** kit — the release loop
run for real: the product (the kit) closed 5.0 with REV-004 remediation
(US-000.BOLT-011/012/013, all Done) and the maintenance partition now runs
on the released version while the kit moves to the 5.1 line.

- **Installed content updated:** the v5.0 kit — AITL checkpoints
  (`AITL-<CODE>-Approval`), manifest family v5 schemas, the post-REV-004
  texts (self-containment: no `US-015`/`ADR-010` leaks; legacy set = the
  pre-v5 `HITL-*` prefix only), and 5.0 version markers throughout.
- **AGENTS.md invariant PASS:** the install step excluded `AGENTS.md`; the
  framework block was replaced at the marker and the project section (empty)
  survived byte for byte.
- **Manifests converted 4.0 → 5.0, lossless (G36):** 47 manifests (30 Bolt +
  17 US) — `hitl_approvals[]` → `checkpoint_approvals[]`,
  `{user, role}` → `{actor: "human:<user>", role, model: null}`,
  `created_by` → `human:<user>`, each `runs[]` gained `agent: null`,
  checkpoint names re-expressed `HITL-*` → `AITL-*`, `schema_version`
  `"5.0"`. Timestamps, decisions, comments and subjects crossed untouched.
  All 47 validate against the v5 schemas.
- **181 project files copied forward** (ADRs, BUGs, DISCs, REVs, AREVs,
  USs, Bolts, SPECs, MEMs, prompts, `_archive/`); `input/` verified
  identical (9/9 files, framework-only — no project input existed);
  framework files superseded from the v5.0 kit.
- **INDEXes rebuilt** from the migrated files (functional, adrs, bugs,
  discovery, reviews, adversarial-reviews, prompts) with the §3.15 v5
  vocabulary and AITL naming.
- **Governance records reconciled:** the full `devflowOLD` walk reports
  copied/superseded/unresolved counts that sum to the total; `devflowOLD/`
  awaits human review before deletion.
- Files: `devflow/` (installed tree from the v5.0 kit), `AGENTS.md` (merge
  at marker), `CHANGELOG.md` (this entry), 47 converted manifests in
  `devflow/metrics/`, 181 migrated documents across `devflow/`.

---

## [4.2 migration] — 2026-08-21 — This repository executed §5.16: installed devflow 4.1 → 4.2

**First real execution of the release migration.** This repository upgraded
its own installed `devflow/` from 4.1 to 4.2 using the kit built by the 4.2
release — the first time §5.16 ran outside a scratch rehearsal.

- **AGENTS.md invariant PASS:** the install step excluded `AGENTS.md`, the
  framework block was merged at the marker, and the project section survived
  byte for byte (`git diff AGENTS.md` = 0 after the merge) — the guarantee
  built by US-000.BOLT-001 held in production.
- **Installed content updated:** G29 relaxation (non-critical non-functional
  BUGs approvable by any team member, author included), the new
  `devflow/prompts/` family (PROMPT-NNN, living data) with the first prompt
  registered (`PROMPT-001-methodology-analysis.md`), §5.15 routing rows and
  the 4.2 version markers throughout.
- **Governance records reconciled:** ADRs, SPECs, MEMs, Bolts, manifests,
  USs and INDEXes were copied forward from the old tree; INDEX version
  headers bumped to 4.2.
- **ADR-001 superseded by ADR-003** (root `prompts/` retired from the
  Product zone; the canonical prompts home is `devflow/prompts/`); ADR-001
  archived under `adrs/_archive/`.
- **Root `prompts/` retired:** `prompts/analysis.txt` removed by
  US-000.BOLT-003 (Done) — its content lives as `PROMPT-001`.
- Files: `devflow/` (installed tree), `AGENTS.md` (merge at marker),
  `CHANGELOG.md` (this entry), `devflow/adrs/ADR-003-…`,
  `devflow/adrs/_archive/ADR-001-…`, `devflow/prompts/PROMPT-001-…`,
  `devflow/functional/bolts/US-000.BOLT-003-…`,
  `devflow/spec/SPEC-260821-0320-…`, `devflow/memory/MEM-260821-0323-…`.

---

## [4.2] — 2026-08-17 — Repository reorganization, self-hosted governance, CHANGELOG out of the distributable

**Avenga DevFlow v4.2.** No schema change — 4.x keeps `schema_version: "4.0"`.
This release is structural: the distribution becomes a folder that mirrors the
target layout, the framework's changelog stops travelling to adopting projects,
and this repository starts governing its own development with the methodology
it publishes. Nothing in the lifecycle, the HITL chain, the guardrails or the
manifest family changes.

### The distribution becomes `distribution-kit/`

The boundary between what ships and what does not was a paragraph in
`AGENTS.md` — *"neither this file nor `tools/` is distributed"* — that a reader
had to know before they could tell the two apart. It is now a folder boundary.

- `devflow/` and the five files under `agents/` moved into
  `distribution-kit/`, each at **the exact path it occupies in an adopting
  project**: `AGENTS.md` and `CLAUDE.md` at the kit root,
  `.agents/skills/avenga-devflow/SKILL.md`, `.github/agents/`,
  `.opencode/agents/`. Adoption is now one copy of the folder's contents
  instead of five copies to five destinations.
- **Nothing that is not distributed may live in the kit.** The five
  `readme.txt` files were removed: their installation paths are now expressed
  by the layout itself, and the knowledge that was not a path — the Codex
  frontmatter/folder-name rule, the Visual Studio 2026 tool-vocabulary caveat,
  OpenCode's `permission: ask` default, the personal-vs-project scopes — moved
  to `README.md` → *Adopting it on a project*, together with the warning that
  `cp -r kit/*` silently skips the three dotted folders.
- Files: `README.md` (adoption section rewritten), `AGENTS.md`, `.gitignore`,
  `tools/BUILD.md` (build output path, checksum path), `tools/README.md`
  (source/artifact split, the `chmod +x` commands).

### `CHANGELOG.md` leaves the distributable (§5.1, §5.3, §5.16)

Up to 4.1 every adopting project received `devflow/CHANGELOG.md` — 185 KB of
the framework's own development history, entries about agent synchronization
and version bumps, none of it about the project holding it. Agents then wrote
project entries into it, mixing two records that were never the same document.

- The file now lives only at the **repository root** of the methodology, and
  the canonical tree carries a root `CHANGELOG.md` annotated as **the
  project's own — DevFlow ships none**. Where a project records its
  methodology upgrades is unchanged in substance and explicit in wording: its
  own changelog, at its own root.
- **The migration path is closed, not left dangling.** A project upgrading
  from 4.1 or earlier holds a `devflow/CHANGELOG.md` that the new version does
  not replace. Rather than let it fall to **unresolved** on every upgrade
  forever, the *superseded* disposition now reads "replaces **or removes**",
  and §5.16 gains the rescue step: if the project wrote its own entries there,
  they move to the repository-root `CHANGELOG.md` before the file is
  discarded. Moving them preserves the record; dropping them would be the G36
  violation.
- G36 and the "never rewritten" table are untouched: they already said
  `CHANGELOG.md` without a `devflow/` prefix, so they now point at the root
  file and keep meaning exactly what they meant.
- Files: `avenga-devflow/Avenga-DevFlow.md` (§5.1 tree, §5.3 root-files table,
  §5.16 never-copied-forward list, *superseded* disposition, the two
  upgrade-record instructions, new rescue paragraph), `devflow/README.md`
  (folder map), `avenga-devflow/README.md`, the four agent definitions
  (framework-shaped-file list + a new bullet beside the `LANGUAGE` exception).

### The repository adopts its own methodology

Until 4.1, `AGENTS.md` and `README.md` both declared that applying DevFlow to
DevFlow would be a category error. That is reversed: from this release the
repository is a governed project like any other, and the box that forbade it
is replaced by the one that explains the two trees.

- **Two `devflow/` trees, never the same version.** `distribution-kit/` is the
  product under construction (4.2); the root `devflow/` is the installed
  previous version that governs this repository (4.1), together with the
  `CLAUDE.md` and `.opencode/agents/` definitions in use here. The root tree is
  never hand-edited — its only writer is the release migration.
- **The release loop is the test §5.16 never had.** When a version closes, the
  repository upgrades itself through the ordinary procedure — `devflow/` →
  `devflowOLD/`, install the kit, migrate, reconcile, human review — and that
  migration is where the next version begins. The upgrade path now runs on a
  real repository with real artifacts at every release instead of being
  documented and never executed.
- **What counts as a code change here.** The product of this repository is
  documentation, so a change to `distribution-kit/`, `tools/` or `prompts/`
  needs an approved Bolt and SPEC exactly as source code would (G07). With no
  runtime to test, a Bolt's expected evidence is the verification procedures
  themselves: the four-agent sync diff, the G-rule count, the version-marker
  sweep.
- `AGENTS.md` is now both this repository's DevFlow entry point and its
  authoring contract; the four-agent synchronization procedure, the preamble
  parity matrix and the version bump survive intact, with kit paths.
- Files: `AGENTS.md` (rewritten in two parts), `README.md` (opening box,
  reading order, *Working on the methodology*), `prompts/analysis.txt`.

### Version bump

`4.1` → `4.2` across `distribution-kit/`: `devflow/VERSION`, the
`**Methodology version:**` header of 69 `README.md`/`INDEX.md` files
(templates carry none), `GUARDRAILS.md` header and footer, `ONBOARDING.md`, the
methodology frontmatter and `avenga-devflow/INDEX.md`, the four agent
definitions (`# Avenga DevFlow v4.2 (Methodology)` heading + `**Agent
version:**` line + two frontmatter descriptions), `distribution-kit/AGENTS.md`
and the root `README.md`.

The bump procedure gains an explicit trap warning: **a bare `4.1` is never
swept.** Section references (`§2.4.1`, `§4.1`, `§4.10`) share that shape, and a
blind replace corrupts dozens of them — the safe patterns all carry a leading
`v` or a label. Statements *about* an older version ("versions up to 4.1
shipped one") are history and stay as written.

Verification after the bump: the four agent bodies diff at 2 lines each (the
single sanctioned `agents-data/` divergence), the G-rule count reads 39/39 in
all four, and no `4.1` version marker remains in the kit.

---

## [4.1] — 2026-08-17 — Schema policy, canonical identity, status vocabulary, tooling groundwork

**Avenga DevFlow v4.1.** No schema change — 4.x freezes
`schema_version: "4.0"` — but the release corrects the texts that tied
`schema_version` to the full `VERSION`, anchors two governance rules the
prose already stated and nothing enforced (archiving closure, status
vocabulary), defines the canonical human identity, turns the OWASP
self-review into a normative conditional gate, removes mechanism-specific
commitments from the distributable (MCP, model products), and prepares the
canonical tree for the tooling track (`devflow/bin/`).

### Archiving only what is closed becomes blocking (§5.4, G38)

§5.4 has always said *"never archive an active, draft, or in-review
document"*, and all four agent definitions carried the sentence. It had no
rule identifier, so it appeared in no enforcement table: **G30** sanctions
the `_archive/` folder and **W20** governs reading it, but nothing governed
the move *into* it. Since `_archive/` is excluded from agent scans and its
contents are treated as generally invisible, archiving an open document was
the one available way to remove work from governance without ever closing
it — a prose-only rule guarding the repository's single invisibility
mechanism.

- The first change of the 4.1 cycle: it was drafted before the version
  bump was decided, landed in the working tree with the 4.0 section as its
  provisional home, and is registered here as part of 4.1.
- **New G38.** Archiving **presupposes** closure and never causes it: the
  move is housekeeping, not a lifecycle step, and grants no approval the
  document does not already hold. The closure set §5.4 listed in prose
  becomes the rule's predicate — `Done` Bolts with their complete package
  (Bolt, SPEC, MEMs), `superseded`/`deprecated` ADRs, closed DISC/REV/AREV
  records with every finding routed, closed BUGs, retired RISKs, completed
  UAT minutes. When closure cannot be established from the document itself,
  the agent does not archive it and asks.
- **Why blocking rather than a `W22` warning.** The G/W split here is
  negotiability, not decidability: 10 of the existing blocking rules are
  only `partial` for a validator and G31 is largely agent-behaviour, so
  partial decidability never forced a warning. §5.4's own register is
  absolute (*"never"*), against W20's conditional *"access it only
  when…"* — the prose had already chosen. A warning the agent may proceed
  past would have made the evasion path sanctioned instead of closed;
  under a blocking rule, an agent that cannot establish closure stops and
  asks, which is the wanted behaviour.
- **The validator's stated non-goal is corrected.** `validator/DESIGN.md`
  read *"`_archive/`: validate structure, never lifecycle"* — the exact
  line that forbade the new check. It now separates two questions:
  lifecycle **progression** checks stay off inside `_archive/` (an archived
  document will never take another step, and flagging it for one is noise),
  while G38 asks the inverted question — was it closed *before* it was
  moved. Classified `partial`: the frontmatter `status` of every archived
  document is decidable, whether a closed REV's findings were each routed
  is prose.
- Files: `avenga-devflow/Avenga-DevFlow.md` (§5.4 criterion),
  `GUARDRAILS.md` (G38 row in GOVERN + rules inventory), the four agent
  definitions (G38 row + archiving bullet + count G01–G38, 38 rows),
  `tools/validator/RULES-G.md` (title, 23/11/4, 61%, ceiling 34 of 38),
  `tools/validator/DESIGN.md`, `tools/README.md`, `README.md`,
  `ONBOARDING.md`.

### Schema evolution policy — `schema_version` is the `<major>.0` of the family (§3.12, §5.16)

The three texts that governed `schema_version` tied it to the full
`VERSION` and mandated a manifest conversion on every bump — a 4.1 upgrade
would have rewritten every manifest with no semantic change, and §3.12's
own words ("e.g. 4.1 or 5.0") made a minor the example of a schema
evolution. Corrected, no new rule:

- `schema_version` follows the **major**: `4.x` keeps `4.0`, a schema
  change means `5.0` — which is what the filenames
  (`manifest-v4*.schema.json`) already said.
- Within the same major, a bump changes documentation, templates and
  structure — **never the manifest family**: no manifest is converted and
  no `schema_version` changes. Across a major, re-routing and lossless
  conversion apply as before.
- G23's `const` and RULES-G's G36 predicate (`declares the schema_version
  of the family VERSION now names`) survive word for word: the family is
  the major. An unfinished migration is now defined as a manifest from
  **another family**, not an older minor.
- Files: `avenga-devflow/Avenga-DevFlow.md` (§3.12 vignette + Schema
  evolution policy, §5.16 "Manifests are migrated, never frozen"),
  `metrics/README.md`.

### Content fixes

- **Quick Start diagram order (1.1):** `devflow/README.md`'s daily-flow
  diagram placed MEM + manifest **after** `HITL-MEM-Approval` — teaching
  the reviewer to approve before the artifact being approved exists,
  contradicting G17, the mandatory post-execution sequence (§3.3) and the
  file's own V-Bounce diagram 50 lines above. Inverted.
- **MEM section enumeration (1.8):** `memory/README.md` announced "14
  numbered sections" and listed 12, merging the four Files sections — an
  agent following the enumeration would omit sections W03 requires. The
  list now matches `TEMPLATE-MEM.md` 1:1, and the self-contradicting
  "numbered" (headings match by keyword, never by number, §3.15) is gone.
- **INDEX dates (1.12):** 9 of the 25 `INDEX.md` files still said May or
  June 2026 — scaffolding that would lie from day one in every project
  that copies it. All 25 now say August 2026 (the `<Month YYYY>` format
  GUARDRAILS already mandates). Added to the version-close checklist:
  version marker and date are the two stamps of a release.
- **Amplify preview URLs (3.j):** two hardcoded preview links removed from
  the methodology (`:184` and the References entry) — the AWS blog URL
  stays.
- Files: `devflow/README.md`, `devflow/memory/README.md`, 9 `INDEX.md`
  files under `devflow/analysis/`, `devflow/avenga-devflow/Avenga-DevFlow.md`.

### Agnosticism — no mechanism, product or model is normative

- **`functional/` detached from MCP and products (1.2a):** the section
  "Synchronisation with SDLC tools (MCP Server) — planned" (with its
  `↕ MCP Server` diagram, Azure DevOps / Jira / GitHub Projects, and a
  `TEMPLATE-US.md` "if MCP sync applies" clause) committed the distributable
  to one mechanism. Replaced by the agnostic statement: integration with
  external SDLC tools is team configuration, out of methodology scope.
  `INDEX.md` and the US template clause aligned. The `gh-copilot`
  frontmatter MCP comments are untouched: they are platform preamble
  (exempt from the shared body) and exactly the team configuration the
  rule describes.
- **AREV model tables by role, not by product (1.2b):** "Suggested model
  (example)" and "Suggested rotations" hardcoded Claude Sonnet 4.7 / Gemini
  2.5 Pro / GPT-5.6 — product versions that age in months, where the only
  normative content is G37's Judge-neutrality constraint. Re-expressed as
  the role pattern (Model A / B / C with the distinction constraint); the
  team fills in its own models.
- **`llm:` examples without versions (1.2c):** 15 templates carried
  versioned model names in format examples; now versionless
  ("Claude Sonnet", "GPT"). Cosmetic — the field stays a free-form exact
  identifier — but the same aging class as 1.2b.
- Files: `devflow/functional/README.md`, `devflow/functional/INDEX.md`,
  `devflow/functional/user-stories/TEMPLATE-US.md`,
  `devflow/adversarial-reviews/README.md`, 15 `TEMPLATE-*.md` files.

### Canonical identity — local part of `git config user.email` (§3.0)

G29, G18 and G24 compare person strings (self-approval routing, the
review↔manifest projection), and the repo coexisted with two forms:
dotted examples in the manifests (`eugenio.serrano`) and `git config
user.name` in the templates (`Eugenio Serrano`). A mismatch passes a
self-approval silently. The identity string for every person field —
`review.reviewers[].user`, manifest `created_by` / `decided_by[].user`,
document `author:` / `owner:` — is now **the local part of the person's
`git config user.email`**: no spaces, accents or display formatting, and
nothing to configure. `user.name` remains the human-readable label in
prose and is never the identity field (G37's `human:<git config
user.name>` record keeps its readable form).

- Files: `avenga-devflow/Avenga-DevFlow.md` (§3.0 review contract),
  28 `TEMPLATE-*.md` files + `US-000-non-functional.md` (author/facilitator
  comments and three approval-table cells), `devflow/memory/README.md`.

### OWASP Top 10 becomes a conditional gate (§3.6)

The four agents' self-review step has said "check against approved ADRs,
naming, OWASP" with no normative anchor — the CHANGELOG recorded it as a
deliberately open item in the 4.0 cycle. Now anchored: **OWASP Top 10
coverage** is a conditional classic gate that applies when the Bolt
exposes or alters an interface reachable from outside the process (public
endpoints, web UIs, auth boundaries), and is `n/a` with a reason in the
SPEC otherwise — the Top 10 is a web catalogue, and a gate that is almost
always `n/a` is noise. The agent step now points at the gate; GUARDRAILS'
conditional-classic-gates projection lists it too.

- Files: `avenga-devflow/Avenga-DevFlow.md` (§3.6), `GUARDRAILS.md`,
  the four agent definitions (V-Bounce Execution step 5, through the
  AGENTS.md four-step sync procedure).

### G39 — the §3.15 status vocabulary is anchored (§3.15, GUARDRAILS, RULES-G)

`validator/DESIGN.md` says it plainly: *"The table is normative and
nothing validates it"* — five vocabularies per family, `stable` where
others use `approved`, and nothing stops an invented value that breaks
validators and INDEX counters silently. New **G39**: a `status` value
outside its family's row — or a stored derived state (Bolt development
state, MEM review state, US/TC progress) — is blocking; a new value enters
the table before it appears anywhere else. Classified `partial` in
RULES-G.md (frontmatter enums are decidable; the family↔status mapping is
prose and the derived-state exclusion is semantic): 23 `full`, 12
`partial`, 4 `none`; ceiling 35 of 39.

- Files: `avenga-devflow/Avenga-DevFlow.md` (§3.15), `GUARDRAILS.md` (G39
  row + rules inventory), the four agent definitions (G39 row + counts
  G01–G39, 39 rows, through the four-step sync), `README.md`,
  `tools/validator/RULES-G.md`.

### `GUARDRAILS.md` — zero-loss compression (482 → 461 lines)

The file had grown to 482 lines. A rule-by-rule audit found **no duplicated
rules**: the 39 `G`, 21 `W`, 23 `N` and 12 `T` are each unique, and the one
pair with real overlap — G18 (self-approving the MEM) ⊂ G24 (delegating a
checkpoint to AI) — stays separate, because G18 carries the human clause
G24 does not (*"AI says it's fine" as approval*) and the two resolve to
different validator signals. What compressed was prose restated between
sections, never a rule row.

- **No rule row, identifier or enforcement table was touched.** The validator
  quotes `GUARDRAILS.md` messages verbatim (`tools/validator/DESIGN.md`) and
  the four agents carry the 39 `G` inline under a 39/39 grep invariant, so a
  reworded row or a merged identifier would cascade into the agents, RULES-G,
  the counts and this changelog. Rows are frozen by contract.
- **Removed, with where each one already lived:** the
  `RULES INVENTORY (approximate)` table (a meta-summary of this file's own
  section headers, carrying nothing unique — and a recurring cascade target:
  it needed an edit for both G38 and G39 in this cycle alone); the risk-
  assignment note under the approver table (a near-verbatim subset of **W14**,
  which additionally carries `risk_history`); the `H1–H6` clause in the
  checkpoint-map intro (**G05**); *"timestamps come from the system clock,
  never invented"* in the naming rules (**W04**, which also gives the exact
  commands); the first sentence of the gates quick-reference (**G21**, now
  pointed at explicitly); and the restatement of the `changes_requested` rule
  inside the AREV note, which now defers to the canonical bullet below it.
- **Four proposed cuts were rejected as lossy**, and the reasoning is worth
  recording because it generalizes. The manifest **projection mapping**
  (`review.reviewers` → `hitl_approvals[].decided_by`, …) reads as a duplicate
  of §3.0, but the four agents carry none of it: `GUARDRAILS.md` is the only
  compact place an agent obtains it, so removing it would push the agent into
  a 4 600-line methodology to do the same job — raising token cost, not
  lowering it. The `US-000` rules keep two clauses that restate the
  normative source (§0, §3.2) for an agent that never opens it (*not a
  substitute for approved ADRs or quality gates*; classify by **primary
  outcome**, with no quick-fix/chore/refactor/hardening/infrastructure
  exception). `STOP-AND-ASK` keeps the manual-intervention clause (*recorded in
  the MEM — not hidden, not punished — measured*). And the V-Bounce notes keep
  *AREV is not a step of this sequence*, the `execution_outcome` enum, and
  *internal autonomous retries never add entries*.
- **The standing principle:** `GUARDRAILS.md` is the enforcement projection an
  agent reads instead of the methodology. Text that restates the normative
  source is doing its job; only text that restates **another part of this same
  file** is redundant. At ~5 lines per rule the file is dense, not bloated.
- Files: `GUARDRAILS.md`.

### New analysis family — `analysis/ui/`, the visual half of the conceptual model (§5.1, §5.15, §5.16)

`analysis/` modelled the domain but not the surface. Entities, relationships
and enumerations were captured before the first User Story; the screens the
product presents were captured nowhere. `input/ui-ux/` held raw mockups and
screenshots, and the analysis derived from them was routed to `user-journeys/`
and `personas/` — which answer questions about *people*, not about *surfaces*.
A User Story whose acceptance criteria referenced a state nobody had
enumerated had nothing to point at.

- **`ui/` is the sibling of `domain-model/`, not of `scope/`.**
  `domain-model/` answers *what things exist and how they relate*; `ui/`
  answers *what the user sees and how it behaves*. Both derive from `input/`,
  both are finished before `functional/`, and a US that needs either one is
  not ready until it exists. `scope/` still decides *what* gets built and in
  which phase; `ui/` documents *how it is presented*.
- **What it holds:** surface inventories, pattern galleries with *when to use*
  and *when not to*, state catalogues (loading, empty, partial, error,
  permission-denied), visual contracts between a surface and its successor,
  parity plans, and annotated references derived from `input/ui-ux/`.
- **No IDs, no approval.** Descriptive kebab-case filenames like `scope/` and
  `vision/`; the family joins the ID-less curated-inventory list in §5.15.
  Citable as context in SPECs, Bolts and ADRs like any other `analysis/`
  family, and carrying no HITL checkpoint — the pre-SPEC evidence gate does
  not wait on it (§2.4.1, G13). **One-way dependency:** a TC may reference a
  document here; a document here never replaces a TC.
- **Why `ui/` and not `ui-ux/`.** A same-basename folder across `input/` and
  `analysis/` has cost this repository before — `analysis/interviews/` versus
  `input/interviews/` produced repeated routing errors until the family was
  consolidated under `input/`. And the name must not invite the content the
  folder rejects: research about people and their flows stays in `personas/`,
  `user-journeys/` and `process/`.
- **§5.16 gains the ID-less relocation rule.** The migration already placed
  every copied artifact by its ID against the routing table rather than by its
  old folder, but a document *without* an ID moved with its folder — so a
  project's UI documents sitting in `scope/` would have landed back in
  `scope/`. Destination is now derived by **family** as well as by ID, which
  makes any future split of one family out of another land correctly without
  special-casing. Projects upgrading to 4.1 move their UI documents into
  `ui/`.
- **`ui/` is a living family, and that one decision settled three findings.**
  A cross-check caught the folder's `status` values sitting in a template
  without a §3.15 row — which **G39 forbids by construction**, since §3.15's
  own preamble requires the row *before* a value appears in a template, a
  README or an INDEX. Fixing it forced the prior question: `analysis/README`
  ties `version` and `superseded` together as *"the same boundary"* — the two
  families replaced as a whole by a numbered successor. `ui/README` calls its
  documents **living documents** edited in place, so `ui/` sits on the other
  side of that boundary: it joins the general `analysis/` row
  (`draft` · `stable` · `deprecated`), and `version` plus the *History* table
  left `TEMPLATE-UI.md` — a version field on a living document sits at `1.0`
  forever and the git log is its history. The `superseded`-only claim for
  `vision/` and `scope/` therefore stays true, untouched.
- **§5.7 and §3.15 were the two normative tables the first pass missed.** The
  §5.1 canonical tree had `ui/`; the folder-purpose table of §5.7 and the
  status-vocabulary table of §3.15 did not. A family present in the tree but
  absent from both is a folder whose documents cannot legally carry a status.
- **One preexisting error surfaced and is corrected:** `analysis/README` listed
  `process/` among the families carrying `version`. Its template lost the field
  in the 4.0 cycle and the list was never updated to match, so the claim had
  been stale for a release; §3.15 says vision and scope carry it alone. The
  list now names two, matching both the methodology and the templates.
- **Reading order and fan-out completed:** `ui/` joins the new-project reading
  order (after `domain-model/`, its sibling half), the US derivation list
  (*surfaces and their states*), §4.1 step 2's enumeration of analysis
  artifacts, and `functional/README`'s pointer for where mockup context lives —
  the one place a US author looks for the contract an AC points at.
- Files: `analysis/ui/README.md`, `INDEX.md` and `TEMPLATE-UI.md` (new); §5.1
  canonical tree, §3.15 status vocabulary, §4.1 step 2, §5.7 folder purpose,
  §5.15 ID-less family list, §5.16 relocation rule; `devflow/README.md` folder
  map; `analysis/README.md` (family table, routing table, flow diagram, reading
  order, US derivation, `version` boundary); `functional/README.md`;
  `input/ui-ux/README.md` routing; `analysis/introduction/README.md`
  (prerequisite and folder tables); the four agent definitions (template
  routing line); `tools/validator/DESIGN.md` (`--framework` markers 67 → 69).

### `analysis/ui/` propagation fixes (migration allowlist, agent projection, INDEX form)

A cross-check of the feature against the migration machinery and the INDEX
convention found four gaps; all corrected:

- **A · The migration allowlist could not pick up ID-less documents.** §5.16
  point 2 selected project files by two signals — an artifact ID, or a
  project-created area — with a single carve-out for `analysis/introduction/`.
  The other ID-less `analysis/` families (business-context, domain-model,
  glossary, personas, scope, ui, user-journeys, vision, §5.15) matched
  neither signal and would have reconciled as **unresolved** — the disposition
  for a `devflowOLD/` file the allowlist does not match, decided by the human
  one by one (§5.16). Nothing was lost, but every UI document of every
  upgrading project became a manual decision. The preexisting hole became
  load-bearing when this release promised *"projects upgrading to 4.1 move
  their UI documents into `ui/`"*: the allowlist now selects ID-less
  `analysis/` documents explicitly. The four agents' copy of the allowlist was
  fixed in the same pass, through the four-step sync.
- **B · The destination rule lived only where the migrating agent does not
  read.** §5.16's new sentence — an ID-less document is placed **by family**,
  not by its old folder — was in the methodology alone; the four agents still
  said "place each file by its ID against the routing table". Since the
  migration is executed by the new agent from its own definition (§5.16), the
  rule that lands UI documents in `ui/` now appears in all four shared bodies,
  through the four-step sync.
- **C · `ui/INDEX.md` copied the wrong family's form.** It used status
  sections (🟡 Draft / ✅ Stable / ⛔ Deprecated) — the structural form of
  `scope/` and `vision/`, the two families on the other side of the boundary
  this feature explicitly chose not to cross. Its §3.15 rowmates
  (business-context, domain-model, glossary, personas, user-journeys,
  introduction) use a single listing with a Status column, and the INDEX
  convention's no-lifecycle list did not name `ui`. The index is now a single
  listing (Kind + Status columns) and `ui` joined the GUARDRAILS list.
- **D · Cosmetic:** `devflow/README.md`'s flow-diagram label for `analysis/`
  now names `ui` alongside domain model, personas, journeys and processes.
- Files: `devflow/avenga-devflow/Avenga-DevFlow.md` (§5.16 allowlist), the
  four agent definitions (allowlist + placed-by-family bullet, through the
  four-step sync), `devflow/analysis/ui/INDEX.md`,
  `devflow/GUARDRAILS.md` (INDEX convention list), `devflow/README.md`.

### Tooling groundwork — `devflow/bin/` and the statements that said 4.x ships nothing (0.8)

4.0 declared "no tooling" in several places; the statements were reworded
to distinguish "not required" from "not shipped", and the canonical tree
reserves `devflow/bin/` for the tools track. **The contract, in positive:**
no methodology release depends on the tools — 4.1 ships none, the track
delivers them when it delivers them, and every release keeps the
optional-by-contract promise:

- **`bin/` enters the canonical tree** (§5.1 + `devflow/README.md` folder
  map) as framework content — the one non-Markdown member of the
  distributable. G30's predicate *"every directory must appear in §5.1 or
  be a sanctioned exception"* now passes by construction, and §5.16 names
  `bin/` explicitly among what *"comes from the new version"* (replaced on
  upgrade, never copied from `devflowOLD/`).
- **Statements reworded from "ships nothing" to "optional by contract":**
  root `README.md` ("No tooling is required" now explains the contract),
  the Validation tooling and Report generation rows of
  `devflow/README.md` Known Limitations, `tools/README.md` (state 4.0
  shipped in / "Nothing here is implemented yet" / Before-the-first-tool
  section, whose three pending edits are now done), `reports/README.md`
  heading and body, §5.12 reports row, `ONBOARDING.md`, `metrics/README.md`.
- Files: `devflow/avenga-devflow/Avenga-DevFlow.md` (§5.1, §5.16, §5.12),
  `devflow/README.md`, `README.md`, `tools/README.md`,
  `devflow/reports/README.md`, `devflow/ONBOARDING.md`,
  `devflow/metrics/README.md`.

### Correction pass after cross-check (counts, frontmatter, judge identity)

A second-pass cross-check (independent agent) found four cascades the first
pass had reported verified:

- **Counts 38→39 completed.** `ONBOARDING.md` ("The 38 blockers"),
  `tools/README.md` (two spots: "23 of the 38 blocking rules" and the
  "[38 rules classified]: 23/11/4" table row) and
  `tools/validator/DESIGN.md` ("all 38 blocking rules: 23/11/4") still said
  38 — RULES-G.md was right, its readers contradicted it. All four now read
  39 with 23 `full` / 12 `partial` / 4 `none`.
- **Frontmatter versions.** `gh-copilot` and `open-code` descriptions still
  said "follows the Avenga DevFlow v4.0 methodology" while their own
  `**Agent version:** 4.1` line sat three lines below. The exempt preamble
  is not exempt from being correct: both now say v4.1.
- **1.2c remainder — 8 more templates.** The first sweep's pattern missed
  versioned examples that were not "Claude Sonnet 4.7": `TEMPLATE-AREV.md`
  ("Claude Opus 4") and seven `analysis/` templates ("Claude Sonnet 4").
  All versionless now.
- **Canonical identity reached the human Judge.** `judge_model` still
  recorded `human:<git config user.name>` in §3.13, G37, the AREV README,
  `TEMPLATE-03-VERDICT.md` and the four agents' Judge-neutrality line —
  while G37's required comparison (neither the Bolt's author nor the
  Challenger's operator) is person-vs-person, exactly the comparison 3.a
  was closing. All now record `human:<local part of git config user.email>`,
  and §3.0's identity-field list names `judge_model` and G37. The historical
  CHANGELOG mention is untouched.
- **Stale tooling statements** that outlived their release: `reporter/DESIGN.md`
  ("Planned for the release after 4.0" — 4.1 is that release) and
  `manifest/DESIGN.md` ("since 4.0 ships no validator") reworded to the
  tooling track. The AREV external-sources table's "Context7 MCP" row
  generalized to "reference documentation servers" (decision 4 — no product
  prescriptions); the inline example mentions stay.
- **Second pass, two more lines.** (a) `tools/README.md`'s `manifest/` row
  still said "4.0 ships nothing that would notice" — the same stale claim
  fixed two files away in `manifest/DESIGN.md`, and it read as current state;
  now says no validator ships yet and the tools track delivers it. (b)
  `tools/validator/DESIGN.md`'s `--framework` spec said "66/66 version
  markers" while the repository holds 67 — an off-by-one that predates 4.1
  (entered the 4.0 cycle) and matters because it is the specification of the
  next validator check: implemented as written, the check would fail on day
  one. Now 67/67.
- Files: `devflow/ONBOARDING.md`, `tools/README.md`,
  `tools/validator/DESIGN.md`, `tools/reporter/DESIGN.md`,
  `tools/manifest/DESIGN.md`, `agents/gh-copilot/AvengaDevFlow.agent.md`,
  `agents/open-code/AvengaDevFlow.md`, `devflow/adversarial-reviews/TEMPLATE-AREV.md`,
  7 `analysis/` `TEMPLATE-*.md` files, `devflow/avenga-devflow/Avenga-DevFlow.md`
  (§3.0, §3.13), `devflow/GUARDRAILS.md` (G37),
  `devflow/adversarial-reviews/README.md`,
  `devflow/adversarial-reviews/TEMPLATE-03-VERDICT.md`, the four agent
  definitions (Judge-neutrality line, through the four-step sync).

### Audit pass — the manifest recipes, plus six cross-reference corrections

A file-by-file consistency review of the distributable, the four agents and
the tools track, running every manifest recipe literally and validating the
result against its schema. **No schema change:** the three
`manifest-v4*.schema.json` files were the part that was right. One cascade
and six isolated fixes.

- **The prose recipes did not produce valid manifests.** Every enumeration of
  what to write into a manifest was a partial list, while the schemas are
  `additionalProperties: false` with their lifecycle fields `required` — so a
  **missing** field fails validation exactly like an extra one (G23), and G33
  then makes the artifact nonexistent. Built literally and validated, five of
  six failed: `metrics/README.md`'s US, Bolt and TC creation rows omitted
  `review_ready_at` / `review_started_at` (and, for the Bolt, the whole
  `acceptance` object); its V-Bounce row omitted `number`, `spec_revision`
  and `git_commit`; and `GUARDRAILS.md`'s mandatory sequence (step 5) plus
  the four agents' V-Bounce step 7 each listed six of the eight fields a
  `v_bounces[]` entry requires. **§3.12 was the only one that was correct,
  because it does not enumerate** — it says *"from the matching manifest
  template"* and *"timing fields `null`"*. The three creation rows now point
  at their template instead of restating its shape; the two `v_bounces[]`
  lists are complete; and a new *Complete from the first write* note in
  `metrics/README.md` states the rule the lists kept losing — a manifest is
  written complete from creation, `null` wherever the step has not happened,
  never with the field left out, because `null` records *"not yet"* and an
  absent field records nothing.
- **`analysis/ui/` propagation, the last spot.** `open-questions/README.md`
  still said *"the only three templates"* carry an *Open questions* section
  and *"every other `analysis/` artifact has no such section"* —
  `TEMPLATE-UI.md` has had one since the family landed. Four now, and the
  folder list in its purpose paragraph gains `ui/` and `scope/`.
- **`tools/identity/DESIGN.md` reopened a closed decision.** It quoted the
  templates as saying *"git config user.name"* — none does; the 28 that carry
  an `author:` field say *"local part of git config user.email (§3.0)"*, and
  the three AREV phase templates carry none — and ended on an *Open
  decision: what is the canonical form?* that §3.0 had already answered
  normatively. The tool does not choose the form; it is the single producer
  of the one §3.0 defines. Its resolution order now starts from git config
  `user.email` instead of a display name, and G37 joins the blocking rules
  that compare identity strings.
- **`reports/`'s HITL coverage was narrower than its name.** The model
  counted only manifest-recorded checkpoints, while §3.7.3 also requires
  `HITL-ADR-Approval` for every applicable ADR and every conditional DISC/REV
  linked to the Bolt — approvals that live in those artifacts, which is
  exactly why §3.7.3 joins them by ID and checkpoint. A manifest-only report
  would read 100% with an applicable ADR unapproved. The exclusion is now
  declared beside the gate, DORA and cost limits the folder already declares.
- **`memory/README.md` contradicted itself on DORA.** Its section-structure
  list described MEM §12 as *"DORA + AI-native + HITL numbers for this
  V-Bounce"*, while the same file states DORA is computed at deployment level
  and *"not from MEMs"* and `TEMPLATE-MEM.md`'s table carries no DORA row.
  The list now matches the template.
- **`business-risks/` INDEX.** The README described two sections (*Active /
  Deprecated*) where the shipped INDEX has three; and the Draft table's
  column read `Probability` where the Stable table and `TEMPLATE-BR.md` use
  `Likelihood`.
- **N23's scope.** *"N23 is the only artifact without a sequential ID"* is
  true of the naming table and false of the repository — the nine ID-less
  `analysis/` families claim no `NNN` either (§5.15). Scoped to the table.
- Files: `devflow/metrics/README.md`, `devflow/GUARDRAILS.md` (V-Bounce
  mandatory sequence, N23 note), `devflow/analysis/open-questions/README.md`,
  `devflow/reports/README.md`, `devflow/memory/README.md`,
  `devflow/analysis/business-risks/README.md` + `INDEX.md`,
  `tools/identity/DESIGN.md`, and the four agent definitions
  (`agents/claude/CLAUDE.md`, `agents/codex/SKILL.md`,
  `agents/gh-copilot/AvengaDevFlow.agent.md`,
  `agents/open-code/AvengaDevFlow.md` — V-Bounce step 7, applied through the
  four-step sync procedure).

### Version bump — 4.0 → 4.1

Markers swept per the AGENTS.md procedure, `devflow/VERSION` written last.
`schema_version` (3 schema `const`, 5 `TEMPLATE-MANIFEST-*.json`, prose in
TEMPLATE-BOLT/US/TC and metrics/README) deliberately stays `"4.0"` per the
new policy. Historical CHANGELOG entries untouched (G36).

- Files: 67 `**Methodology version:**` markers (every `README.md` /
  `INDEX.md` under `devflow/`, `ONBOARDING.md`, `avenga-devflow/README.md`
  + `INDEX.md`), the methodology frontmatter, `README.md` (Version 4.1),
  `agents/project-root/AGENTS.md` (source-of-truth line), `GUARDRAILS.md`
  (header + footer), the four agent definitions (`# Avenga DevFlow v4.1
  (Methodology)` heading + `**Agent version:** 4.1`), `devflow/VERSION`.

---

## [4.0] — 2026-08-15 — Manifest family v4 and sprint reports

**Avenga DevFlow v4.0.** The manifest contract grows from a single
per-Bolt JSON into a **family that covers the whole process** — User
Stories, Bolts and Test Cases — with the **timestamp of every step**, so
lead times, review queue times and review latencies become measurable for
project management. On top of the family, a new `reports/` folder ships
self-contained sprint progress reports for PMs.

### Manifests migrate with the project — one schema family per repository (§3.12, §5.16, G36)

The schema evolution policy is **reversed**: manifests are no longer frozen
under the `schema_version` they were written with. A version upgrade now
converts every `metrics/**/*.json` forward, so a repository holds exactly one
manifest family — the one `devflow/VERSION` declares — the same way it holds
exactly one methodology version. The earlier policy is superseded, not
corrected; the entry below records what it said when it said it.

- No version bump: this lands inside the 4.0 cycle (`VERSION` unchanged).
- **What made the old policy wrong for its own delta.** `3.0` → `4.0` is
  purely additive: eight required-but-nullable timing fields
  (`bolt.review_ready_at`, `bolt.review_started_at`, `bolt.acceptance{...}`,
  and the pair on each `spec_revisions[]` and `v_bounces[]`), plus a widened
  Bolt-id pattern. Nothing is removed and nothing is reinterpreted, so the
  justification recorded in *Methodology upgrade protocol* below — *"rewriting
  one would mean inventing values for fields that did not exist when the work
  happened"* — does not hold: `null` is not an invented value, it is the
  accurate statement that nothing was recorded.
- **The rule that replaces it — lossless or it does not happen (§3.12).**
  Conversion may only add the fields the new schema introduces (as `null`
  where the value was never captured) and apply its renames and relocations.
  Overwriting a recorded value, dropping a recorded field, or inferring one
  nobody observed is blocked by **G36**, which keeps its number and its
  MEM/ADR/HITL/`CHANGELOG` clauses and trades its `metrics/**/*.json` clause
  for this one. A delta that cannot be applied losslessly stops the migration
  and is reported.
- **The gap this closes.** v3 had a single Bolt-level schema; v4 requires
  three. Converting only the Bolt manifests would leave every migrated US and
  TC without one, and **G33** makes an artifact without its manifest
  nonexistent — so a v3 project became formally invalid the moment `VERSION`
  was written. §5.16 now has the migration **reconstruct** the missing levels
  from evidence already in the repository, field by field: frontmatter
  `sources:` / `author:` / `date:` (or the commit that added the document) →
  `sources` and `generation`, with `runs: []` and `duration_seconds: null`;
  the `review:` contract → `hitl_approvals[]` and the review timestamps;
  `story_points`, `source_bolt` / `source_us` / `covered_acs` → their own
  fields; the already-converted Bolt manifests → `bolts[]` / `test_bolts[]`.
  Every one is transcription. A field the repository does not record makes
  that manifest **unresolved** — reported for the human, never guessed.
- **Re-routing is part of it.** A manifest lands where the new version's
  routing table (§5.15) puts its family, not where it sat in `devflowOLD/`:
  the `3.0` → `4.0` move is `metrics/*.json` → `metrics/bolts/`. Reconciliation
  keeps its three dispositions; **copied** now means re-routed *and* converted,
  and **unresolved** additionally covers a manifest whose conversion or
  reconstruction lacks a value nobody recorded.
- **`metrics/manifest-v3.schema.json` is deleted.** No v3 manifest can survive
  a migration, so the legacy schema has no reader. `AGENTS.md`'s version-bump
  sweep loses its exception for the file (CHANGELOG history is now the only
  acceptable match for an old version string).
- **Tooling contracts inverted, not just reworded.**
  `tools/validator/RULES-G.md`'s G36 check previously required *no*
  modification to `metrics/**/*.json` on a `VERSION`-changing commit — it
  would have failed a correct migration. It now checks the **shape** of the
  change: each manifest must be a superset of its pre-commit version, with
  additions confined to the new schema's fields and set to `null`. G23's
  exclusion no longer accepts every `schema_version` present.
  `tools/validator/DESIGN.md` (check 1), `tools/reporter/DESIGN.md` and
  `devflow/reports/README.md` stop filtering by version and report an older
  family as an unfinished migration; `tools/manifest/DESIGN.md` refuses such a
  manifest instead of treating it as frozen evidence.
- **Files:** `devflow/avenga-devflow/Avenga-DevFlow.md` (§3.12 policy, §5.16
  table + two new blocks + report and reconciliation), `devflow/GUARDRAILS.md`
  (G36), the four agent definitions —
  `agents/claude/CLAUDE.md`, `agents/codex/SKILL.md`,
  `agents/gh-copilot/AvengaDevFlow.agent.md`,
  `agents/open-code/AvengaDevFlow.md` — through the `AGENTS.md` four-step sync
  procedure (verified: 37/37 guardrail rows each, shared body 2 diff lines per
  pair for the sanctioned `agents-data/<agent>/` path),
  `devflow/metrics/README.md`, `devflow/reports/README.md`, `AGENTS.md`,
  `tools/validator/RULES-G.md`, `tools/validator/DESIGN.md`,
  `tools/reporter/DESIGN.md`, `tools/manifest/DESIGN.md`, and the deletion of
  `devflow/metrics/manifest-v3.schema.json`.

### Consistency pass (agent audit — manifest contracts, handoff, archiving)

A full-repo audit (Claude) re-verified finding by finding against the live
files and the validation schemas (this repository), fixing under explicit
human direction:

- **The four agent definitions now carry complete manifest field lists
  (X1/X2)** — `agents/claude/CLAUDE.md`, `agents/codex/SKILL.md`,
  `agents/gh-copilot/AvengaDevFlow.agent.md` and
  `agents/open-code/AvengaDevFlow.md`, through the `AGENTS.md` four-step
  sync procedure (both passes verified: shared body byte-identical, 2 diff
  lines per pair, the sanctioned `agents-data/<agent>/` path). They
  enumerated `bolt{...}` without `acceptance` and
  `verifies{source_us,covered_acs}` without `source_bolt` — both fields are
  `required` in their schemas, so an agent following the text produced a
  manifest that G23/G33 reject. Both lists now match the schema and the
  `TEMPLATE-BOLT.md` §8 wording.
- **Bolt   handoff now has a home.** §3.3 already required documenting the
  handoff "in the Bolt's History section", but `TEMPLATE-BOLT.md` has no
  such section, and the four agents carried only the half of the protocol
  that names the incoming executor. `TEMPLATE-BOLT.md` gains a
  `## 9. History` handoff log (date, outgoing, incoming, reason); the four
  agent files record the handoff there; the dead "and in the weekly plan"
  clause — no such artifact exists in the canonical tree — is gone from
  §3.3.
- **`_archive/` is now sanctioned in §5.12**, matching G30 and the four
  agent files' instructions — the §5.12 enumeration of agent-created areas
  listed only `agents-data/` and per-AREV folders. §5.4's mechanism is
  reworded from "manual housekeeping" to HITL: the agent may archive under
  the same human-decision governance as everything else.
- **`TEMPLATE-PROCESS.md` loses `version: "1.0"`** — §3.15 reserves
  `version` for vision and scope alone in `analysis/`.
- **The two manifest-bearing templates without `sources:`** —
  `TEMPLATE-US.md` and `TEMPLATE-BOLT.md` — gain the frontmatter key their
  schemas require (`minItems: 1`), matching the other 16 templates.
  `TEMPLATE-BOLT.md` also gains the `bug:` frontmatter key, closing the
  asymmetry §2.16 requires ("the BUG and Bolt reference each other"): the
  BUG template already carries `bolt:`/`spec:`/`mem:` as structured fields,
  the Bolt template only mentioned the BUG in prose.
- **`analysis/vision/INDEX.md` regains its 🟡 Draft section** — it shipped
  only Stable/Superseded while `scope/INDEX.md` carries all three states
  of its §3.15 vocabulary; GUARDRAILS' "earliest state first" applies.
  GUARDRAILS' no-status-sections exception now names business-context,
  introduction and domain-model alongside glossary, personas and
  journeys.
- **Open Questions index aligns to the 🔴 vocabulary** — an open,
  unanswered OQ is "needs action now", which GUARDRAILS defines as 🔴 (as
  risks/ and incidents/ already do), not 🟡. The 🔴 row in GUARDRAILS now
  names open questions explicitly instead of "(incidents)".
- **Rule-count drift fixed** — `README.md` said "all 36 blocking rules"
  and `tools/README.md` said "36 rules classified: 22 full": both are 37
  and 23 full per `tools/validator/RULES-G.md` (G37 was added after the
  counts were written).
- **READMEs that outran reality:** `functional/README.md` and its INDEX
  described MCP Server synchronisation and an auto-updated INDEX as
  present-day facts; 4.0 distributes no tooling, so both are reworded to
  "planned". `spec/README.md`'s `obsolete` row no longer says "Superseded
  or the feature was cancelled" — the note below already defines it as
  cancellation with no successor. `functional/README.md`'s INDEX-grouping
  list now starts with 🟡 (earliest state first, as the INDEX actually
  is). `metrics/README.md` drops "ACs" from the US manifest's coverage
  (ACs live in the document, not the schema) and adds `source_bolt` to
  the TC manifest's `verifies` description, which silently omitted a
  required field.
- **`AGENTS.md` fixes:** the version bump procedure no longer lists
  `AGENTS.md` itself among version-bearing files (it carries no literal
  version — the four agents' heading and `**Agent version:**` line are
  named instead); the preamble parity matrix gains the missing `# Git`
  and `# HITL` rows (byte-identical in all four, now sanctioned).
- **`devflow/bin/` delivery is future tense where it was stated as fact**
  — `README.md` and `AGENTS.md` say the compiled executable "will ship" in
  `devflow/bin/`, matching `tools/README.md`'s "not done yet".
- No version bump: this lands inside the 4.0 cycle (`VERSION` unchanged).

### Manifest family v4 (§3.12)

- **Three manifest levels**, mirroring the artifact folders:
  - User Stories → `metrics/user-stories/US-NNN-<description>.json`
    (`story_points`, child `bolts[]`, `HITL-US-Approval`).
    US-000 is a container and has no manifest.
  - Bolts → `metrics/bolts/US-NNN.BOLT-NNN-<description>.json` /
    `metrics/bolts/TC-NNN.BOLT-NNN-<description>.json` (migrated from the
    `metrics/` root; structure unchanged from v3 plus timing).
  - Test Cases → `metrics/test-cases/TC-NNN-<description>.json`
    (`verifies` US/ACs, `test_bolts[]`, `HITL-TC-Approval`).
- **Timing contract — the hour of every step:** each artifact, each SPEC
  revision and each V-Bounce records `review_ready_at` and
  `review_started_at` (copied from the artifact's review contract §3.0) in
  addition to the existing `generation.created_at` and the approval
  `decided_at`. All are required-but-nullable. Measurable (derived, never
  stored): queue time (`started − ready`), active review time
  (`decided − started`), total review latency (`decided − ready`, < 4 h
  target), Bolt lead time, US lead time, V-Bounce cycle.
- **Auto-created like Bolt manifests (G33):** every US and TC manifest is
  created by the agent at the same moment the document is created and
  updated at each lifecycle step — an artifact without its manifest does
  not exist. US-000 excluded (no approval lifecycle).
- **Schema family:** `manifest-v4-bolt.schema.json` (Bolt),
  `manifest-v4-us.schema.json`, `manifest-v4-tc.schema.json`, all
  `schema_version: "4.0"`, all strict (`additionalProperties: false`).
  Templates: `TEMPLATE-MANIFEST-BOLT.json` (updated),
  `TEMPLATE-MANIFEST-US.json`, `TEMPLATE-MANIFEST-TC.json`. Existing v3 Bolt
  manifests remain valid historical evidence under the schema evolution
  policy — never migrated retroactively, validators aggregate by
  `schema_version`.
- **Guardrails:** G23 now validates the whole family; new **G33** blocks
  creating/approving/advancing a US or TC without its manifest. T07
  updated. **N09** updated.
- **Migration of references:** `devflow/metrics/` → `devflow/metrics/bolts/`
  in templates (Bolt, SPEC, MEM), folder docs, agents and the methodology.

### Sprint reports — `devflow/reports/` (§5.12)

- **`TEMPLATE-REPORT.html`** — a **design reference**, not a fillable
  template: self-contained HTML (inline CSS, no external resources)
  populated with fictional example data ("Avenga PDP", a project that does
  not exist), showing the target shape of the report — Executive Summary,
  US and Bolt Progress, Backlog Status, Bolt Detail, Quality & Risks,
  Project Gantt and Management View.
- **Report generation deferred to the next version.** A Python 3 generator
  (`Generate-Report.py`, stdlib only) was built and hardened during this
  cycle — it aggregated the three manifest folders, computed every metric
  from the timing contract and rendered `REPORT-YYYY-Www.html` with optional
  `--from`/`--to` filtering — and was then **pulled before release**, together
  with the decision about where delivery tooling should live (a `devflow/bin/`
  area fed by a separate tooling project is the current direction). **4.0
  therefore ships no tooling at all**, and `TEMPLATE-REPORT.html` ships as a
  design reference with example data rather than a fillable template. The
  generator and previous-template fixes recorded in the consistency rounds
  below are history: they describe files no longer in the repository (the
  generator was removed; the fillable template was replaced by the design
  reference). Nothing upstream
  changes — the manifest family is the *source* of a report, never its
  output, so the timing contract keeps everything computable retroactively
  once the tooling lands.
- **Reports are derived, never governed** (§5.5 class): never citable as
  the source of a governed artifact; `_archive/` applies (W20).
- `reports/` added to the §5.1 canonical tree and §5.12; G30 sanction list
  unchanged (reports/ is a canonical folder, not an agent-created one).

### Methodology upgrade protocol — migration is now normative (§5.16)

§5.16 arrived with the policy half — what a migration updates and what it must
never rewrite — but not the mechanical half, so upgrading a project still
required writing an ad-hoc prompt every time, and the correctness of the result
depended on how carefully that prompt was worded. The procedure is now written
down, and the four agents carry it, so the whole instruction collapses to:
rename `devflow/` to `devflowOLD/`, install the new version, say *migrate*.

**What moves is an allowlist of origin, never a file-by-file comparison of the
two folders.** Only two things are copied forward: `input/` in full — every
file and subfolder, byte for byte, never normalized or filtered — and every
file the project created, identified by an artifact ID from the naming table
(§5.15, N01–N23) or by living in a project-created area (`agents-data/<agent>/`,
`adversarial-reviews/AREV-NNN-*/`, any `_archive/`, plus `analysis/introduction/`,
whose narratives carry no ID). **Everything else comes from the new version and
is never copied forward** — READMEs, INDEXes, templates, schemas, `GUARDRAILS.md`,
`ONBOARDING.md`, `avenga-devflow/`, `US-000-non-functional.md`, `CHANGELOG.md`.

Shaping the rule this way, rather than as a classification of every file, is what
makes it survive future versions unchanged: adding or removing framework files
changes nothing about the procedure. It also closes two failure modes by
construction rather than by vigilance — the new methodology cannot be overwritten,
and a file a new version deliberately removed cannot be resurrected. That second
one is already live: `memory/INDEX.md` was deleted in this cycle, and a naive
"copy whatever OLD has and NEW does not" would bring it straight back.

Four rules complete it, each closing a trap the ad-hoc prompt did not cover:

- **`LANGUAGE` is the single exception.** It ships with the framework but is
  configured by the project, so it keeps its old value; taking the new one
  silently reverts the project's `content_language` and the agent starts writing
  prose in the wrong language. `VERSION` is its mirror — new value, written last.
- **A file's destination is derived, never inherited.** Each artifact is placed by
  its ID against the routing table (§5.15), not by where it sat in `devflowOLD/`,
  so a version that relocated a family lands correctly with no special-casing.
- **Indexes are rebuilt after the copy, from the migrated files themselves** — and
  **numbering stays continuous**. The INDEX is where the next free `NNN` is
  claimed, so a rebuild that treats the folder as new hands out a number the
  project already spent. The next number continues from the highest migrated ID,
  gaps stay gaps, no ID is reused or renumbered (§2.4).
- **Reconciliation closes the migration.** Every file and folder in `devflowOLD/`
  gets exactly one disposition — copied, superseded, or unresolved — and the three
  counts must sum to its total file count. A migration that cannot account for
  every file is not finished, and an unresolved file is never resolved by the
  agent's judgement: it is listed and the human decides.

Manifests are copied byte for byte and stay valid under their own
`schema_version`; they are never rewritten into the new schema (§3.12, G36).
Rewriting one would mean inventing values for fields that did not exist when the
work happened, which is what makes a manifest evidence rather than a record.

The protocol lives in §5.16 and, as `## Methodology Upgrade Protocol`, in
`agents/claude/CLAUDE.md`, `agents/codex/SKILL.md`,
`agents/gh-copilot/AvengaDevFlow.agent.md` and
`agents/open-code/AvengaDevFlow.md` — alongside the Bug Fix, Review and Open
Questions protocols, updated through the four-step sync procedure.

### Distribution boundary — what is the methodology, what is a project

The audit round below was run against this repository as if it were a project
using DevFlow. It is not: it is where the methodology is **authored and
distributed**, and `devflow/` here is the artifact that gets copied into real
project repositories. That distinction was never written down anywhere, and
its absence produced a class of defect neither audit could see — including,
during the round itself, a proposal to open a `DISC` in this repository.
Writing the boundary down exposed eight places where the distributable
documentation described **this** repository instead of a project.

**The rule, now explicit:** every sentence inside `devflow/` must be true and
actionable **inside a project**. `devflow/` therefore never mentions the
methodology repository at all — not its `agents/` folder, not its maintenance
procedures, not its root `AGENTS.md`. Referring to that last one is the worst
case: a reader inside a project follows the reference to their own root
`AGENTS.md`, which correctly says *"this repository runs under Avenga
DevFlow"* — the opposite of what they just read.

- **§5 described the wrong repository.** §5 declares itself normative for
  repository structure, and its canonical tree was rooted at `AvengaDevFlow/`
  with the four platform folders under `agents/` — none of which a project
  has. It now shows a **project** tree: `AGENTS.md` and `devflow/` at the
  root, plus the agent definition wherever its tool expects it. The
  "two top-level areas" framing went with it.
- **§3.13 carried the only link in `devflow/` that escaped `devflow/`** —
  ``agents/` pointing at `../../agents/``, which resolves in this repository and breaks in
  every project that copies the folder. Replaced with prose.
- **§3.0 pointed the turn-budget default at `agents/`**, a path no project
  contains; it now points at the agent definition installed for the team's
  tool.
- **§3.15 spoke in the framework's voice** — *"Templates in this repository
  are written with English schema…"*, which inverts meaning once the file is
  read from inside a project.
- **`devflow/README.md`** dropped the `agents/` block from its folder map,
  gained `AGENTS.md` in *Starting a New Project* (it was missing from the
  install step), and lost two *Known Limitations* rows —
  *Four-agent synchronization* and *Agent definitions size* — which are
  framework-maintenance concerns a project neither performs nor can act on.

**`AGENTS.md` was two documents fused into one.** Its first thirteen lines are
project instructions (source of truth, guardrails, onboarding, platform
pointer, language policy); everything below is framework maintenance (the
four-agent sync procedure, the parity matrix, the version bump). Split:

- **`agents/project-root/AGENTS.md`** (new, with its own `readme.txt`) is the
  distributable half, copied to the **root of the project repository**
  alongside `devflow/`. `AGENTS.md` is a cross-tool convention several agents
  auto-load from the repository root, so a project needs one and until now
  received none. The folder is the fifth under `agents/` and the only one
  named after its destination rather than a tool.
- **The root `AGENTS.md`** keeps the maintenance half and now opens with a
  blocking statement that this repository does **not** run Avenga DevFlow: no
  Bolts, SPECs, MEMs, DISCs or ADRs are created here, and `devflow/`'s empty
  `INDEX.md` files are scaffolding to be copied, not an empty backlog.
- **`README.md`** (new, repository root) is the landing page this repository
  never had: what Avenga DevFlow is, the full adoption contract, the reading
  order, and how to work on the methodology itself.
- §5.2 and `devflow/README.md`'s folder map were updated for the fifth folder;
  the version bump procedure gained the two version statements the new files
  introduced (`README.md`, `agents/project-root/AGENTS.md`).

**Every blocking rule is now inline in every agent (36/36).** The agents
carried 23 of 36, and the 13 missing ones included the HITL core — G18
(self-approving a MEM), G24 (delegating a checkpoint), G26 (a draft ADR
governing), G27 (unapproved DISC/REV/AREV findings) — while folder-hygiene
rules were inline. Since the agent file is auto-loaded every turn and
`GUARDRAILS.md` is a first-task read that context compaction can lose, a
blocking rule the agent cannot see is one it will miss exactly when it
matters. `AGENTS.md` now carries the invariant and the command that checks it:
the agent's `G` row count must equal `GUARDRAILS.md`'s. `W`, `N` and `T` stay
out by design — they shape output rather than block it.

**Smaller corrections in the same pass:** G36 gained its anchor in §5.16 (G35
was already cited from §3.2 and §4.4, G36 from nowhere); the section separator
before `# Communication Guidelines` was restored in three of the four agents;
and the G-number ordering in `GUARDRAILS.md` was confirmed **not** to be a
defect — that file groups by lifecycle phase while the agent tables list
numerically, two orderings for two purposes.

**Agent definitions** — `agents/claude/CLAUDE.md`, `agents/codex/SKILL.md`,
`agents/gh-copilot/AvengaDevFlow.agent.md` and
`agents/open-code/AvengaDevFlow.md` — updated through the `AGENTS.md`
four-step sync procedure. Shared body verified byte-identical after every
pass: 2 diff lines per pair, the sanctioned `agents-data/<agent>/` path.

### Consistency fixes (audit round 4 — two-model cross audit, 37 findings)

Two independent full-repository audits, run on two different models, each
verified against the files rather than against the other's report. 37 findings
closed across 59 files. Four of them surfaced during execution, not during
either audit. The pattern the round confirmed: **everything under an explicit
procedure was clean; every finding lived in what had none** — exempt agent
preambles, secondary folder READMEs, INDEX section headers, and the seam
between normative prose and the JSON `required` arrays.

- **AREV is no longer a stage of the V-Bounce.** §2.15 called it standalone
  and ad-hoc-able while §3.3/§4.4 listed it as step 3 of the *Fixed anatomy* —
  and `GUARDRAILS.md` declared that sequence *"no step is skippable"* while
  step 3 was optional. An AREV needs no Bolt, SPEC or US to exist, so it
  cannot be a stage of one. Both anatomies drop to 5 steps, the mandatory
  sequence to 6, and §2.15 gains **"Not a stage of the V-Bounce"**. A
  Bolt-bound AREV now examines the **closed** package (diff + tests + gates +
  MEM + manifest) as a pre-filter for `HITL-MEM-Approval`, and a FAIL routes
  through `changes_requested` — which by the ordinary rule is a **new
  V-Bounce with a new MEM and `v_bounces[]` entry**. That closes a measurement
  hole: AREV-driven rework was invisible to `V-Bounces per Bolt`, `Rework
  Ratio` and `Human Override Rate`, and §3.7.4 reads those numbers to
  diagnose DoR/SPEC quality. No schema change; *"No manifest impact"* intact.
- **`ac_count` removed from the US manifest.** It was `required` in
  `manifest-v4-us.schema.json` under `additionalProperties: false`, absent
  from §3.12 and from all four agents, consumed by nothing, and the only
  field in the family needing manual re-sync with the document body — against
  §3.12's own exclusion of *"duplicated functional metadata … already
  derivable from the artifacts"*. The schema was wrong, not the prose: §3.12
  is now exact as written.
- **Document `status` vocabulary is normative (§3.15).** 19 distinct
  vocabularies across 27 files existed only in templates and folder READMEs;
  §3.15 listed a handful and trailed off in `…`. A full table now owns them,
  ratifying what already worked — SPEC's `blocked`/`obsolete`, UAT's
  `approved-with-observations`, `process/`'s `active`, `analysis/`'s
  `stable` — and separating `status` from the universal `review.decision`
  enum and from derived states, which are never stored.
- **The OQ sunset rule became part of the DoR (new G35).** It blocked
  `HITL-BOLT-READY-Approval` in two READMEs and all four agents while citing
  §3.0, which never mentioned OQs; §2.9 and §3.2 did not list it either. It
  now lives in the DoR of §2.9/§3.2/§4.4, scoped by the OQ's own `targets`
  rather than by a Unit, since `units/` governance is reserved.
- **Methodology version upgrade documented (new §5.16, new G36).** Upgrading a
  project migrates its documentation forward, but nothing said so — and
  nothing bounded it, so a migration could rewrite `metrics/**/*.json`,
  approved MEMs and ADRs, recorded HITL decisions or CHANGELOG history, all
  of which are historical evidence. §5.16 states what is migrated and what
  never is; G36 blocks the destructive half; `VERSION` is updated last.
- **One rule for `INDEX.md` (§5.15).** An INDEX exists where the ID is
  sequential and needs a central allocator — which also makes it the place a
  duplicate claim surfaces as a merge conflict, the intended behaviour. It
  does not exist where the timestamp already assigns and orders: `spec/` and
  now `memory/`, whose `INDEX.md` was **deleted** because it would have been
  edited on every V-Bounce, conflicting on every concurrent branch while
  detecting nothing. The rationale was undocumented, which is why two audits
  read the asymmetry as a defect. §5.15 also states that a folder without a
  README is governed by its parent's.
- **Version markers: a criterion instead of a count.** The 25 `README`/`INDEX`
  files of the `analysis/` subtree carried no `**Methodology version:**`
  header while the six `input/` ones did, and `AGENTS.md`'s "41 markers"
  silently depended on `memory/INDEX.md` existing. All 66 `README`/`INDEX`
  files under `devflow/` now carry it (templates never do — they are
  instantiated into project artifacts), and `AGENTS.md` states the criterion
  and leaves verification to the grep that already did the real work.
- **`BOLT-NNN` widened to four digits past 999** (`[0-9]{3,4}` in
  `manifest-v4-bolt.schema.json`). `US-000` collects every non-functional Bolt
  for a project's whole life and numbers are never reused, so three digits
  were a hard ceiling. The legacy `manifest-v3.schema.json` keeps three, per
  the schema evolution policy. `US-NNN` and `TC-NNN` are unchanged.
- **Preamble parity matrix in `AGENTS.md`.** The methodology is agnostic about
  tools and models, which is exactly what made the exempt zone unauditable: a
  difference between the four agents could be adaptation or drift, and the two
  look alike in a diff. Seven capabilities are now marked equivalent or
  divergent-with-reason, plus the rule for a fifth agent: walk the matrix,
  never copy an existing agent. Two real defects fixed — three agents carried
  *"reformulate the query"* without having a search tool, and only `claude`
  had the tool-agnostic debugging instruction, now translated into each
  vocabulary.
- **`TEMPLATE-REPORT.html` states what it is, inside itself.** The "example
  data, no generator, do not circulate as a real report" warning lived only in
  `reports/README.md` — invisible to anyone opening the self-contained HTML,
  which is the exact failure the README anticipated. It now carries a fixed
  banner.
- **`analysis/process/README.md` no longer teaches a G30 violation.** Its
  *File organization* section proposed `sub-processes/`, `sales/`,
  `operations/` and `collections/` inside `process/`, and named files without
  IDs (`PROC-quoting.md`, against N19). Rewritten flat: a sub-process is a
  process and gets its own `PROC-NNN`; areas group in the slug and the INDEX.
- **Folder documentation reconciled with its own templates and conventions:**
  `risks/README.md` (⛔ → 🏁 for a closed risk, and `severity` →
  `overall_severity`); `analysis/domain-model/README.md` (entities are living
  documents and carry no `version`); four INDEX files whose sections broke the
  emoji vocabulary (`open-questions`, `business-risks`, `process`,
  `input/documentation`, the last of which had invented a lifecycle for raw
  evidence); `reports/README.md` (W20 covers `_archive/`, not active reports;
  *"Story points delivered"* struck as a velocity metric forbidden by
  §2.6/W18; *"First-pass approval"* restored to the §3.7.2 formula);
  `tests/README.md` (UAT owner, and the `source_us: US-000` a non-functional
  TC still records); `bugs/README.md` (`fixed → in-fix` bounded by §3.11);
  `reviews/README.md` (new normative mapping from REV/AREV severities to BUG
  `severity`, which routes its own approval); `open-questions/README.md` (a
  self-contradiction 170 lines apart); `analysis/introduction/` (analysis
  artifacts are not "approved" — they have no checkpoint);
  `input/business/README.md` (raw input reaches `functional/` through
  `analysis/`, never directly).
- **Naming and reference precision:** `HITL-BOLT-Approval` is not a canonical
  code (G05) — replaced in `avenga-devflow/README.md` and `ONBOARDING.md`;
  `tc_id` and `source_test_case` named fields no template has; §3.0 cited
  §2.6.1 for a rule §3.0 itself states; `HITL-UNIT-Approval`'s owner wording in
  §3.11; AREV missing from the *One path* trigger list in `devflow/README.md`,
  `ONBOARDING.md` and all four agents; `TEMPLATE-BOLT.md`'s
  `## 3. Acceptance criteria` renamed *Covered acceptance criteria* with an
  explicit instruction to reference the parent's and never invent new ones;
  `TEMPLATE-BUG.md` gained the `US-000.BOLT-NNN` variant;
  `data_classification` given precedence (the SPEC value is what the PII/DLP
  gate reads); `adversarial-reviews/README.md`'s internal tension about the
  Defender's model resolved (only the Judge is normatively constrained);
  `agents/gh-copilot/readme.txt` now carries the Visual Studio 2026 caveat its
  own frontmatter already documented.
- **Agent definitions** — `agents/claude/CLAUDE.md`, `agents/codex/SKILL.md`,
  `agents/gh-copilot/AvengaDevFlow.agent.md` and
  `agents/open-code/AvengaDevFlow.md` — updated through the `AGENTS.md`
  four-step sync procedure in two passes (shared body) plus the preamble
  fixes: `G01-G36`, the G35 and G36 rows, the OQ protocol rescoped, the
  manifest *key structure* split into Bolt / US / TC (it described only the
  Bolt shape and failed for the other two on both `required` and
  `additionalProperties`), a pointer to the §3.15 status table, ten of
  thirteen template paths corrected to `devflow/analysis/<subfolder>/`, AREV
  added to the triggers, and the restored *non-functional* qualifier on the
  BUG Bolt routing. Shared body verified byte-identical: 2 diff lines per
  pair, the sanctioned `agents-data/<agent>/` path.

### Consistency pass over the 4.0 set

A full re-read of the methodology set after the feature and naming commits
closed the gaps where a v4 rule reached its consumers but not the place
that actually enforces or applies it:

- **`TEMPLATE-US.md` and `TEMPLATE-TC.md` gained their manifest-creation
  instruction** — G33 makes the US and TC manifests mandatory at creation,
  but the two templates an agent opens to create those documents said
  nothing about it, while `TEMPLATE-BOLT.md` carried it in two places. Both
  now mirror the Bolt pattern: a frontmatter-comment warning plus a
  `Manifest creation (mandatory)` section naming the target folder, the
  starting fields, the schema and the example template.
- **The three `metrics/` subfolders now ship** — `bolts/`,
  `user-stories/` and `test-cases/` are declared canonical in §5.1/§5.12
  and required by G33, but being empty they were never tracked by Git and
  would not survive a clone. Each carries a `.gitkeep`.
- **G33 no longer contradicts §3.12 on US-000** — it read "a User Story",
  which literally demanded a manifest for the container that §3.12
  explicitly exempts. Reworded to "feature User Story" with the exemption
  stated, following the G01 precedent.
- **G28 now reaches `reports/`** — §5.12 declares reports non-citable, but
  G28 keys on the `derivative: true` frontmatter marker, which rendered
  HTML cannot carry; the prohibition was therefore prose-only. §5.5 now
  defines membership by location for generated artifacts, and G28 names
  `reports/` explicitly.
- **`memory/README.md`** — one stale manifest path (`metrics/US-NNN...`)
  left over from the v3 flat layout.
- **`ONBOARDING.md`** — glossary rows for the manifest family and
  `reports/`, so the level that users and PMs read describes what v4 added.
- The four agents' condensed **G28/G33** rows were realigned with the two
  corrections above.

### Git ownership rule (G34)

- **No commits without an explicit user request (§3.3):** the agent never
  stages, commits, pushes or opens PRs on its own — version-control actions
  happen only when the human explicitly asks. Artifacts are written to the
  working tree; the human owns the repository history.
- **New blocker G34** in the GOVERN phase table (appended with the next free
  number); propagated to the four agents (summary row + `G01-G34` range
  counters) and ONBOARDING (blocker count 33 → 34). The agents already
  carried the sentence ("You are NEVER allowed to stage and commit files
  automatically") — this anchors it in the normative source and makes it
  enforceable.

### Agent consistency fixes (deep review)

- **I1 — Review duration (4 agents):** the v3 sentence "Review duration
  belongs to telemetry, not the manifest" survived in the agents' review
  budget sections after §3.0/GUARDRAILS were fixed. Now aligned: duration
  derives from the manifest timing contract (`decided_at` −
  `review_started_at`, §3.12), workflow telemetry as fallback.
- **I2 — .env boilerplate vs G07 (4 agents):** the generic "automatically
  create a .env file... proactively" instruction told agents to make a
  configuration change without an approved Bolt. Replaced: never create or
  modify `.env`/config on your own — report the requirement and let the
  human decide (G07).
- **I3 — SPEC origin enum (TEMPLATE-SPEC):** the origin list missed DISC
  and ADR (non-functional Bolts born from an approved ADR/DISC could not
  register their origin). Now `US | BUG | TC | DISC | REV | ADR`.
- **I4 — INDEX hygiene rule (§5.15):** the convention now states *why* an
  INDEX is required (sequential-ID allocation) and makes the existing
  exemptions explicit: timestamp-ID folders (`spec/`), unstructured
  (`input/`), machine-readable (`metrics/`, `reports/`), and subfolders
  covered by their parent's INDEX (`functional/user-stories|bolts` →
  `functional/INDEX.md`).
- **I5 — HITL coverage fidelity (report generator):** the generator now
  computes required/recorded per the §3.0/§3.12 model — base checkpoints
  per type, conditional origin (`HITL-BUG-Approval` when the Bolt's sources
  reference a BUG), one decision per SPEC revision and per V-Bounce/MEM —
  instead of a flat 4 per Bolt. The model is documented in `reports/README`
  "HITL coverage model".
- **Minor:** US lead time formula in `reports/README` fixed to start at
  `HITL-US-Approval` `decided_at`; `turn_budget` in TEMPLATE-SPEC left
  empty (was pre-loaded with 10, overriding the platform default);
  `adrs/INDEX.md` disambiguated ADR-governs-decisions vs code-reflects-
  implementation; AREV FAIL verdict clarified as an internal iteration of
  the same V-Bounce.
- **Cross-verification of the heading unification (Claude):** the
  "30/30 numbered" pass had left three templates mixed —
  `TEMPLATE-ADR` (unnumbered `References`/`HITL-ADR-Approval`) and
  `TEMPLATE-01-CRITIQUE`/`TEMPLATE-03-VERDICT` (unnumbered role-mindset,
  mandates and HITL headings, diverging from the fully numbered
  `TEMPLATE-02-DEFENSE`). All three renumbered sequentially. The
  renumbering of `TEMPLATE-INTRODUCTION` (0→1 start) had also left its
  internal "linked in §6" pointing at the wrong section — now §7
  ("Where to read next"). And `TEMPLATE-DISC` was the only approvable
  template without a human-facing HITL section — added
  `## 11. HITL-DISC-Approval` mirroring the TC/REV pattern.

### Consistency fixes (review findings)

Full-methodology review (Claude) found the v4 rule propagated to consumers
but not to its enforcement points. All findings fixed, schemas untouched:

- **Timing contract contradiction resolved (§3.0, GUARDRAILS):** the old v3
  rule ("`review_ready_at` / `started_at` are **not** copied to the
  manifest") contradicted the v4 schemas where those fields are required.
  §3.0, the GUARDRAILS review-contract section and both review-duration
  statements now state the copy rule and derivation (`decided_at` −
  `review_started_at`).
- **Live gates §3.6:** the per-Bolt universal gate and the Bolt-manifest
  validation gate no longer demand "Manifest Schema v3" — they validate
  against the normative manifest schema (§3.12).
- **Version-neutral sweep:** ~30 live "manifest v3" prose references across
  the methodology, folder docs and the four agents became version-neutral
  ("the manifest", "the Bolt manifest", "the manifest family") so future
  bumps never repeat this class of residue. Historical CHANGELOG entries and
  the legacy `manifest-v3.schema.json` file are untouched.
- **reports/ relocated (§5.11 → §5.12):** the row lived under "V-Bounce
  execution evidence" ("The following three directories" with four rows)
  while every citation pointed to §5.12. Moved; "three" restored.
- **§3.7 metric sources:** the governance-metrics collector now cites the
  manifest timing contract as the indexable source for queue/review times,
  with workflow telemetry as fallback only.
- **Naming unified across the family:** US and TC manifests used
  `approvals[]` while Bolts used `hitl_approvals[]`. Unified to
  `hitl_approvals[]` in both schemas, both templates, `metrics/README.md`,
  the US/TC document templates and the report generator — free only while
  no real manifest exists yet.
- **Timing contract hardened (§3.12):** declared monotonic ordering
  `created_at ≤ review_ready_at ≤ review_started_at ≤ decided_at`
  (violation = validation error).
- **US lead time redefined (metrics/README):** now starts at
  `HITL-US-Approval` `decided_at` (consistent with Bolt Lead Time) instead
  of US `created_at`, which punished early-written stories.
- **§0 Quick Start:** the `HITL-BOLT-READY-Approval` route now mirrors the
  BUG-driven severity exception like the `HITL-BUG-Approval` route.
- **ONBOARDING glossary:** duplicate "Manifest v4" / "Manifest family" rows
  merged into one.
- **§5.15:** `metrics/` and `reports/` explicitly exempted from the
  README+INDEX convention (machine-readable content, inventory = file
  system).
- **§3.12 lifecycle nit:** MEM review timing clarified as living at
  V-Bounce level.
- **Cross-verification pass (Claude over the implementation):** two
  line-wrapped "manifest v3" survivors the line-based sweep missed —
  the §3.6 universal gate ("Manifest Schema ⏎ v3 JSON Schema") and
  `memory/README.md` ("the manifest ⏎ v3") — neutralized. Two
  pre-existing table-rendering defects fixed in passing: the unescaped
  pipe in G16's `blocked\|cancelled` cell and the missing Example cell in
  `reviews/README.md`'s routing table.

### Consistency fixes (cross-model review round)

An external full-repo review (Gemini) cross-verified finding by finding
against the live files (Claude); each confirmed item fixed under explicit
human direction:

- **`TEMPLATE-BOLT.md` frontmatter comment realigned with the 3.1
  resolution:** the 3.1 entry resolved the `hitl_approvals[]`-at-creation
  contradiction in favor of "origin decisions already present" and aligned
  `metrics/README.md` — but the template's own frontmatter comment kept the
  stale "all empty" phrasing, contradicting its own §7 a few sections
  below. The comment now names the origin decisions per type
  (`HITL-US-Approval` functional, `HITL-TC-Approval` test, none for
  US-000, plus `HITL-BUG-Approval` when BUG-driven). Repo-wide sweep
  confirmed no other file carries the stale phrasing; the `hitl_approvals:
  []` comments in `TEMPLATE-US.md`/`TEMPLATE-TC.md` are correct as-is — at
  those levels the origin approval genuinely happens after creation.
- **UAT realigned with the universal review contract (§3.0, W11):** UAT was
  the only approvable artifact whose `review.decision` used a divergent
  enum (`approved-with-observations` instead of `changes_requested`), with
  no documented exemption. Resolved by splitting contract from lifecycle:
  `review.decision` now uses the canonical `approved | changes_requested |
  rejected` (TEMPLATE-UAT frontmatter + HITL table), while
  `approved-with-observations` survives as a **document status** only —
  defined in the template comment and `uat/README.md` as the lifecycle
  label for `review.decision: approved` with non-empty `findings[]`, every
  finding routing to a new Bolt. Follows the existing precedent that
  document statuses are artifact-specific (ADR `superseded`, process
  `active`) while the decision enum is universal. Minor, same folder:
  duplicated "the Bolt / the Bolt" line-break artifact in `uat/INDEX.md`
  removed.
- **`TEMPLATE-PROCESS.md` status enum realigned with its own folder:**
  `process/README.md` documents the deliberate exception (`draft | active |
  deprecated` — processes describe dynamic behaviour in effect, not a
  static reference) and `process/INDEX.md` follows it ("Active processes"),
  but the template still offered the generic `stable`. The frontmatter
  comment now reads `draft | active | deprecated` with a pointer to the
  README note. The other eleven `analysis/` templates keep `stable`
  (`superseded` for vision/scope) — that is the documented general
  convention, only `process/` differs.
- **ADR `supersedes` widened to a list (TEMPLATE-ADR):** §3.5's conflict
  resolution requires one new ADR that "lists the superseded ADRs in
  `supersedes`" — several at once when resolving a conflict — and
  `adrs/README.md` repeats it ("lists them"), but the template declared the
  field as a singular string, making the mandated flow unrecordable.
  Now `supersedes: []`, consistent with the sibling `conflicts_with: []`
  and every other list field in the same frontmatter. Field exists only in
  the template; agents/GUARDRAILS carry prose only — no other file touched.
- **§5.15 mandatory-INDEX enumeration completed (INT, BR, PROC, AREV):**
  the I4 pass of this cycle restated the rule (INDEX required where
  sequential IDs are allocated) but its illustrative list omitted four
  artifact types that §5.15's own routing table assigns sequential IDs —
  `INT-NNN`, `BR-NNN`, `PROC-NNN`, `AREV-NNN` — all four of which already
  keep an INDEX in the repo. The optional clause also contradicted the
  table by naming "`input/` and its subfolders" timestamp/unstructured
  while `interviews/` allocates `INT-NNN`; now reads "`input/` (except
  `interviews/`...)". Enumeration exists only in §5.15 — no duplicates in
  agents or GUARDRAILS.
- **Monetary cost deferred out of 4.0 (deliberate):** `reports/README.md`
  promised an "optional price catalog passed to the generator" that
  `Generate-Report.py` never implemented, while §3.7.2 declared **Cost per
  Bolt** mandatory at team-aggregate — a mandatory metric with no shipped
  tooling. Decision: this version cannot compute prices yet, so every
  price/cost-metric reference is removed rather than half-implemented —
  §3.7.2 row dropped, §4.9 "(Optional) Cost / Token per Bolt" → "(Optional)
  Tokens per Bolt", the unfillable "Cost / Bolt: __ USD" line removed from
  TEMPLATE-RETRO, and the derivation promises trimmed from §3.12,
  `metrics/README.md`, `memory/README.md`, `reports/README.md` and the four
  agents' flow-metrics line. **What stays:** the manifest schemas are
  untouched — `runs[]` keeps recording provider/model and the four token
  categories, so when pricing returns in a future version, costs are
  computable retroactively over all historical manifests. The "cost is
  outside the manifest" exclusion statements (G23, §3.12 list, folder
  READMEs, report note) also stay — that design fact remains true.
- **"< 4 h" badge recalibrated to the metric the spec defines:** §3.0 and
  §3.7.3 define the target as **Time-to-Human-Review** — queue time,
  `review_ready_at` → `review.started_at` — but the report badged "vs <4h"
  (TEMPLATE-REPORT) and raised its watch-list alert (Generate-Report.py)
  against **total** latency (`decided − ready`), and both
  `reports/README.md` (twice) and `metrics/README.md` annotated the target
  on the total-latency row. A deep review legitimately taking 5 active
  hours after a 10-minute pickup read as "over target" — punishing exactly
  the thorough reviews the cardinal rule demands. The badge and the watch
  alert now key on `queue` ("—" when `review_started_at` is absent), total
  latency stays as an informational column, and all four doc annotations
  moved to the queue-time row. The retro template already had it right.
- **Worked manifest examples for all three Bolt types:** the sole Bolt
  manifest example was functional-typed, yet `metrics/README.md` told
  agents to copy it "for a new Bolt" generically — leaving the type-defining
  differences (origin `hitl_approvals[]`: US-Approval / TC-Approval / none;
  `id` patterns `US-000.BOLT-NNN` / `TC-NNN.BOLT-NNN`; approver roles) to
  prose. Added `TEMPLATE-MANIFEST-BOLT-NONFUNCTIONAL.json` (US-000, no
  origin decision, Architect READY + Tech Lead/SRE DONE) and
  `TEMPLATE-MANIFEST-BOLT-TEST.json` (TC-027 parent, `HITL-TC-Approval`
  origin predating Bolt creation, QA-side approvers). All three examples
  validated against `manifest-v4-bolt.schema.json` (per-type id-pattern
  conditionals included) with monotonic step timestamps.
  `metrics/README.md` files table and `TEMPLATE-BOLT.md` §7 now point to
  the example matching the Bolt type.
- **Planning vocabulary unified (§3.2 ↔ §4.3):** the same weekly-planning
  policy was written as "Commit (85%) + Stretch (50%)" in §3.2 (confidence
  notation) and "commit the P85" in §4.3 (percentile notation, with the
  Stretch slice's P50 never re-attached) — not a contradiction, but a
  two-vocabularies gap that invites misreading as two different rules.
  Both lines now use percentile notation (Commit = P85, Stretch = P50) and
  cross-reference each other. No other file carried the numbers.
- **§3.8 mapping constraint completed:** the paragraph fully constrained
  only the `qa_automation ↔ test` pairing and grouped the other five
  categories under a loose "apply only to `functional` or `non-functional`"
  — read alone, it admitted invalid combinations like
  `functional + refactor` that §3.11's acceptance-routing section (270
  lines later) rules out. §3.8 now states the full one-to-one mapping
  (`feature` → functional, `refactor`/`infra`/`hardening`/`debt` →
  non-functional, `qa_automation` ↔ test) with §3.11 as the routing
  restatement. Collateral catch in the same sweep: `functional/README.md`
  listed `qa_automation` among US-000's INDEX grouping categories —
  impossible, Test Bolts belong to TCs — now excluded explicitly.
- **Four-agent sync convention codified (AGENTS.md):** the platform
  definitions share ~85% of their content verbatim and are maintained by
  hand in four copies — this cycle alone needed I1/I2, the G28/G33 row
  realignment, the G34 propagation and the Cost-per-Bolt removal applied
  ×4. Tooling-based fixes (generator, CI diff) are out — the methodology
  ships no tooling beyond report emission — so the implicit discipline is
  now a stated procedure in `AGENTS.md`: shared sections are byte-identical;
  edits grep the old text expecting 4 matches, apply ×4, re-grep the new
  text expecting 4; a pre-edit mismatch is itself a defect to reconcile
  first; CHANGELOG entries name all four files.
- **"Known Limitations & Roadmap" section added to `devflow/README.md`:**
  the version's deliberate boundaries were all stated but scattered across
  4,300 lines — `HITL-UNIT-Approval`/`units/` reserved (§3.11 entry 14),
  multi-repo out of scope (§1 topology assumption), monetary cost deferred
  (this cycle), no validation tooling by design (G23/G33 are procedural),
  four-agent manual sync (AGENTS.md). Now consolidated in one table in the
  framework map, each row pointing to its normative source, so adopters see
  the boundaries before committing rather than by accident.
- **Version bump procedure codified (AGENTS.md):** the bump touches 32+
  files by hand with no verification — a missed file silently announces the
  previous version. Tooling is out by design, so the check is procedural:
  after sweeping the markers, grep the **old** version string repo-wide;
  the only acceptable survivors are CHANGELOG history and the legacy
  `manifest-v3.schema.json` — anything else is a missed file. Documented
  next to the four-agent sync convention.
- **Second-pass corrections on the new manifest examples (cross-model
  re-review):** the non-functional example omitted
  `US-000-non-functional.md` from `bolt.sources`, which §3.12 requires
  verbatim — added. The Test Bolt example had invented its own
  `HITL-TC-Approval` origin decision for TC-027 while
  `TEMPLATE-MANIFEST-TC.json` already records that same approval event
  (QA + Functional Analyst, 2026-08-02) — the Bolt manifest's origin
  decision is a projection of the same event, so it now mirrors the TC
  manifest verbatim. Both re-validated against the schema with monotonic
  timestamps. Also: the `metrics/README.md` example flow now starts at
  "US-012 drafted → US manifest created with the document (draft)" —
  the old wording ("approved → created + updated") kept being misread as
  manifest-after-approval, though the derived-states table on the same
  page already required a pre-approval draft manifest.   Housekeeping:
  `__pycache__/` (generated by running the report generator) deleted and
  gitignored.
- **Agent token-budget rationale recorded (`devflow/README.md`):** a
  cross-model review of agent size (compression opportunities O1–O5,
  ~2k tokens of estimated savings against a ~21k fixed session cost)
  closed with a deliberate no-change decision: the agent file is
  guaranteed in context every turn while `GUARDRAILS.md` is a first-task
  read that context compaction can lose, so the agents' in-context tables
  and reinforced directives are persistence insurance, not redundancy —
  and provider prompt caching amortizes the stable prefix. Documented in
  the "Known Limitations & Roadmap" table so future reviews do not
  re-derive the decision from scratch.

### Language policy localization (analysis/, US, TC, filenames, ADR titles)

Client-facing artifact families may now be fully localized for projects
whose `content_language` is not English, without touching the machine-facing
schema:

- **§3.15 rewritten:** IDs are English and **never translated or renamed**
  (`US-001` stays `US-001`, never `HU-001`); filename `<description>` slugs
  always follow `content_language` in **kebab-case ASCII** (no accents, no
  `ñ`, in any language); section headings follow `content_language` in
  `analysis/` (all subfolders), feature User Stories and Test Cases and
  stay English in every other artifact family; `HITL-*-Approval` codes are
  never translated, even inside a localized heading; ADR titles now follow
  `content_language` like the body (the old "ADR titles stay in English"
  rule is dropped). YAML keys, enum values, manifests, commits, branches
  and PR titles remain English.
- **Methodology notes** added to §2.4.1 (SPEC naming), §2.12 (MEM stable
  slug) and §5.15 (routing table) stating the slug language rule.
- **GUARDRAILS:** W10 rewritten (ADR title + body follow `content_language`);
  N01–N23 gained the slug-language rule (IDs never change; examples stay
  English as framework documentation); W06 notes the slug is in
  `content_language`. W05 untouched — enum values are still never
  translated.
- **The four agents** (`claude`, `codex`, `gh-copilot`, `open-code`):
  Language Policy section updated identically (schema list without
  filenames/ADR titles; slug, headings and ADR-title rules added).
- **Templates** — the framework keeps shipping **English templates**; the
  13 analysis templates (including `TEMPLATE-VISION`, which gains its
  first LANGUAGE POLICY block, with the dual English/Español
  vision-statement placeholders collapsed into a single English one per
  §3.15) plus `TEMPLATE-US` and `TEMPLATE-TC` now instruct translating
  headings and prose at instantiation while keeping keys, enums and IDs
  in English; `TEMPLATE-ADR` drops the English-title rule. The analysis
  templates' "See devflow/LANGUAGE" pointers now point to the real
  "Language Policy" section in `devflow/README.md`.
- **README Language sections** updated in all 14 `analysis/` READMEs
  (including the three `domain-model/` subfolders and `introduction/`,
  which uses a bullet instead of a footer section),
  `functional/README.md`, `tests/README.md`, `tests/test-cases/README.md`
  and `adrs/README.md`; the same rule was propagated to the in-body
  `Language:` bullets of `analysis/README.md`, `open-questions/README.md`,
  `scope/README.md`, `domain-model/README.md`, `glossary/README.md`,
  `personas/README.md`, `process/README.md` and `user-journeys/README.md`,
  and to `agents-data/README.md` and `reports/README.md`; `ONBOARDING.md`
  §6, `AGENTS.md` and the new `devflow/README.md` "Language Policy"
  section aligned. Long lines introduced by the change were re-wrapped to
  the repository width.
- No version bump: this lands inside the 4.0 cycle (`VERSION` unchanged).

### Consistency fixes (audit round — tooling, timing contract, examples)

A full-repo audit (Fable) re-verified finding by finding against the live
files (Claude), which confirmed most items, downgraded three and surfaced
one the audit had missed. Fixed under explicit human direction:

- **`Generate-Report.py` crashed on its own documented command
  (the miss):** `--from`/`--to` were parsed as naive datetimes and compared
  against offset-aware manifest timestamps, raising an uncaught
  `TypeError`. The exact invocation in `reports/README.md` died against the
  repository's own manifest examples. The period filter now compares
  **calendar dates** (`as_date()`), so an RFC 3339 timestamp and a plain
  `--from` date are always comparable, and `--to` is inclusive without the
  previous `+1 day` workaround.
- **Latest decision governs, not the first:** `hitl_approvals[]` is
  append-only, so a checkpoint re-decided after `changes_requested` has
  several entries. `get_decision()`/`get_decision_for()` scanned forward and
  returned the *first* match, so a Bolt whose `HITL-BOLT-DONE-Approval` was
  first `changes_requested` and later `approved` was reported as not-Done
  forever — contradicting §2.12 ("the Bolt's current development state is
  derived from its latest V-Bounce"). Both now scan in reverse.
- **Lead times implemented instead of promised:** `reports/README.md`
  listed *Bolt lead time* and *US lead time* under "What the report
  computes", but neither was computed and the HTML had nowhere to show
  them. Both are now derived per the `metrics/README.md` formulas
  (BOLT-DONE − BOLT-READY; last child Bolt DONE − `HITL-US-Approval`) and
  rendered in a new **Lead times** table.
- **`schema_version` honored (§3.12):** the generator loaded every JSON in
  `metrics/*/`, so a legacy v3 manifest was aggregated in silence into
  statistics labelled "manifest family v4". Non-`4.x` manifests are now
  skipped with a warning on stderr.
- **Report tooling hardening:** `--sprint` is validated against
  `YYYY-Www` (it is interpolated into the output path); the embedded JSON
  escapes `</` so a manifest string containing `</script>` cannot break the
  page; `esc()` no longer renders the value `0` as an empty cell; the
  "US approved without Bolts" watch-list row checks *every* known Bolt, not
  only those inside the reporting period; the per-level column is labelled
  **Generations** (it counts generation events, not artifacts); dead
  helpers (`hh()`, an unused `ok`) removed.
- **The flagship manifest example modelled a G13 violation:** SPEC rev 1
  was generated at 10:42 citing `TC-027` as a governed source, while that
  TC's `HITL-TC-Approval` was recorded at 11:10 — the pre-SPEC evidence
  gate failing in the very example agents copy. `TEMPLATE-MANIFEST-TC.json`
  now places the TC's creation, review and approval inside the window
  between `HITL-BOLT-READY-Approval` (10:25) and the SPEC generation
  (approved 10:38); `TEMPLATE-MANIFEST-BOLT-TEST.json` carries the same
  corrected `decided_at` for its copy of that decision.
- **One Test Bolt, one filename:** `TEMPLATE-MANIFEST-TC.json` listed
  `TC-027.BOLT-001-invoice-download.md` in `test_bolts[]` while
  `TEMPLATE-MANIFEST-BOLT-TEST.json` declared `…-invoice-download-e2e.md`.
  Aligned on the `-e2e` form, including the N04 example in `GUARDRAILS.md`.
- **N05 filename convention applied to the example:** the SPEC in the
  functional example was `SPEC-260802-1030-…` while its rev 1 was generated
  at 10:42. Every other example in the repo (both other Bolt manifests, all
  MEMs) uses the artifact's own creation time, so it is now
  `SPEC-260802-1042-…` in `TEMPLATE-MANIFEST-BOLT.json` and in the copy
  embedded in §3.12.
- **One timestamp notation (the timing contract's own input):** three
  precisions coexisted — the schemas' `format: date-time` (RFC 3339, with
  seconds), `metrics/README.md`'s `YYYY-MM-DDTHH:mm±ZZ`, and
  `YYYY-MM-DDTHH:mmZ` in the HITL tables of 11 templates — with
  `TEMPLATE-MEM.md` and `TEMPLATE-SPEC.md` each contradicting *themselves*
  between frontmatter and HITL table. §3.12 now states RFC 3339 **with
  seconds** and a zone designator explicitly, and the 28 occurrences of the
  seconds-less form were replaced by `YYYY-MM-DDTHH:mm:ss±HH:MM`.
- **G33 made visible from the procedures, not only the templates:**
  "How to add a test case" (`tests/test-cases/README.md`) listed five steps
  and never mentioned the manifest, so an agent following it produced an
  invalid TC; the manifest is now step 3. `functional/README.md` never
  mentioned the US manifest at all: its "Recommended structure" — which
  listed sections `TEMPLATE-US.md` does not have (*Context*,
  *Mockups*) and omitted the ones it does (§7 HITL, §8 Manifest) — was
  replaced by the template's real structure.
- **`process/`'s `active` registered in the cluster's status table:**
  `analysis/README.md` declared the full `analysis/` lifecycle
  (`draft | stable | deprecated | superseded`) and noted
  `open-questions/`'s own vocabulary, but not `process/`'s documented
  substitution of `active` for `stable` — so a validator following the root
  README would reject valid processes.
- **`changes_requested` unified:** the backticked hyphenated form
  (`changes-requested`) survived in `TEMPLATE-AREV.md`,
  `adversarial-reviews/README.md` and four places in the methodology,
  against the enum all three v4 schemas define — the class of mismatch W05
  calls critical for validators. Plain-prose adjectival use is unchanged.
- **Placeholders and fields:** `BOLT-XXX` (UAT, INCIDENT, RETRO) replaced by
  the composite notation N02/N03 require (`US-NNN.BOLT-NNN` /
  `US-000.BOLT-NNN`); PascalCase `…-Title.md` examples in `TEMPLATE-US.md`
  made kebab-case; the HITL table's **Role** row in `TEMPLATE-BOLT.md` held
  `git config user.name` (a name, not a role) and now lists the role
  identifiers; `revisit-on` → `revisit_on` in `open-questions/README.md`;
  `verifies.source_us` in the TC schema gained the `^US-[0-9]{3}$` pattern
  its documentation already claimed.
- **Sources row in `TEMPLATE-UAT.md`:** the row labelled *Bolts* pointed at
  `memory/MEM-…`; it now points at the Bolts, with MEMs listed separately as
  V-Bounce evidence.
- **`adrs/INDEX.md` gained its Draft section** — the ADR lifecycle starts at
  `draft` and every sibling INDEX lists that state, so a draft ADR had no
  possible row.
- **Errata:** `dueDate1` → `dueDate`
  (`domain-model/README.md`); the MEM metrics example summed to 5h but was
  labelled "4h total"; "the three `TEMPLATE-MANIFEST*.json`" are five;
  `categoria` → `categoría` in the Spanish pitch example; a comment in
  `TEMPLATE-INTRODUCTION.md` pointed at "section 2" from inside section 2.
- **Agent definitions:** the four `TEMPLATE-MANIFEST-BOLT.json`-only lines
  now route by Bolt type (functional / US-000 / Test), matching
  `metrics/README.md` and `TEMPLATE-BOLT.md` §7 — the 4.0 cycle created the
  two extra examples precisely because the generic one misled. In the
  platform preamble (outside the verbatim methodology body),
  `open-code/AvengaDevFlow.md` and `gh-copilot/AvengaDevFlow.agent.md`
  carried a truncated bullet ("…understand the content. Use the ") followed
  by an empty one; repaired against the `claude`/`codex` wording, and the
  hyphen/en-dash split in the same paragraph unified. A byte diff confirms
  the shared methodology body of the four agents differs in exactly one
  line — the intentional `agents-data/<agent>/` path.
- No version bump: this lands inside the 4.0 cycle (`VERSION` unchanged).

### Consistency fixes (audit round 2 — decisions applied and cross-model follow-up)

Second pass over the same audit, applying the twelve decisions the human took
on the items the first pass had deliberately left open, plus a follow-up
cross-model review by another model, whose confirmed findings are folded in
here.

- **AREV — the Judge's neutrality was contradicted by its own examples.** The
  rule ("a third model, different from both the implementor and the
  Challenger", "must always be a neutral third party") stands; the two model
  tables were the defect. The *Suggested model* row offered
  `GPT-5.6 / Claude Sonnet 4.7` as Judge with Claude Sonnet 4.7 as
  Implementor, and rotation row 3 offered Claude as Judge while Claude was the
  Challenger. Both now keep the Judge distinct from **both** positions. Added:
  the "3 roles" wording now names them (Implementor, Challenger, Judge) so it
  no longer appears to contradict "the Defender may be the implementor" — the
  Defender is the Implementor defending, not a fourth position — and a
  two-model team is told explicitly to escalate to a human arbiter and record
  it in the VERDICT rather than seat a non-neutral Judge.
- **`BR` prefix collision resolved:** entity-level business rules are now
  `RULE-NN`, numbered per entity file, leaving `BR-NNN` unambiguous for the
  repository-wide Business Risks. `TEMPLATE-ENTITY.md` states the distinction.
- **The three undocumented status enums now carry their rationale**, following
  the precedent of `process/`'s `active` and `uat/`'s
  `approved-with-observations`: `spec/` explains `blocked` (approved but
  externally unexecutable — a state no other artifact has) and `obsolete`
  (terminal with no successor); `retros/` explains `draft | final` (a retro is
  the minute of a dated event, never revised into a newer truth, never
  deprecated by a later retro); `functional/` explains that US-000's
  `status: "active"` is deliberately **outside** the feature-US enum — the
  container has no `HITL-US-Approval`, so it can be neither `draft` nor
  `approved`, and never closes, so it can never be `deprecated`. Validators
  must special-case it.
- **§3.1 no longer advertises metrics that do not exist.** "US scope
  coverage", "total approval rate" and "go-live approval rate" appeared in no
  normative section; two of them are not even derivable, since
  `go-live approval rate` needs deployment data that §3.12 deliberately keeps
  out of the manifests. The bullet now names what §3.7 defines and states that
  nothing outside §3.7 is a metric of this methodology.
- **INDEX convention (new section in `GUARDRAILS.md`).** Columns stay free per
  cluster — a Test Case index and a Bolt index do not need the same ones —
  but the status vocabulary is now fixed, because ⛔ meant two opposite things
  across the repository: *deprecated* in 5 indexes and *closed successfully*
  in 4. The scheme separates them: 🟡 draft/pending/partially resolved,
  🔴 open, 🔄 in progress or superseded, ✅ live and healthy, 🏁 terminal and
  **successful**, ⛔ terminal and **obsolete**, ❌ rejected. Applied to
  `bugs/`, `reviews/`, `risks/`, `incidents/` and `adversarial-reviews/`
  (⛔/✅ → 🏁), `memory/` (⛔ → ❌ for rejected), `adrs/` (📝 → 🟡). The
  `**Last updated:**` footer is now always at the bottom: moved in
  `business-risks/INDEX.md`, added to `open-questions/INDEX.md`, which also
  gained the canonical emoji.
- **One cardinality notation in the domain model:** per-side multiplicity
  (`1`, `0..1`, `1..N`, `0..N`), written for both ends as `<source> — <target>`.
  Pair notation is dropped because `1 — 0..N` and `1 — 1..N` both collapse to
  `1:N`, losing exactly the optionality a domain model exists to pin down.
  Applied to `domain-model/README.md`, `relationships/README.md`,
  `TEMPLATE-ENTITY.md` and `TEMPLATE-RELATIONSHIP.md`.
- **`date:` frontmatter — criterion declared and applied.** A document's
  `date:` carries a time **only when the document records a point-in-time
  event**: `INCIDENT` (detection) and `UAT` (session start) keep it and now
  say why; `PROCESS` and `RETRO` drop to `YYYY-MM-DD`. §3.12 states the rule.
- **`input/` INDEX policy.** The root README claimed "this folder does not
  have an INDEX.md" while two subfolders have one. Replaced by the actual
  criterion — a subfolder carries an INDEX when its files have their own ID
  and are cited individually as evidence (`interviews/` `INT-NNN`,
  `documentation/`), not when the folder is cited as a whole — and
  `databases/` and `source-code/`, which had neither an INDEX nor an
  explanation, now state theirs.
- **`input/` version headers:** the six subfolder READMEs and the two INDEX
  files carried none, silently contradicting AGENTS.md's "every folder's
  header". Added; the marker count is now **41** and `AGENTS.md` says so.
- **`analysis/` frontmatter.** Audited all 13 templates, which corrects one
  audit claim: the LANGUAGE POLICY block is present in **all** of them,
  including `TEMPLATE-VISION.md`. Real gaps fixed: `sources` added to VISION
  (the anti-fabrication rule it was silently escaping), `tags` to GLOSSARY.
  `version` is now carried only by the artifacts replaced *as a whole* by a
  numbered successor — added to SCOPE, removed from ENTITY, kept in VISION and
  PROCESS — with the criterion written in `analysis/README.md`.
- **`gh-copilot` no longer ships another team's MCP servers as defaults.**
  `tools:` keeps only built-in VS Code tools; `dbhub-sqlserver`, `context7`,
  `chrome-devtools`, `playwright`, `pdf-reader` and `ado/*` moved to a
  commented opt-in block with one line each explaining what it is for.
  Declaring a server that is not installed makes the agent fail or prompt, so
  opt-in is the safe default for a distributable template.
- **`AGENTS.md` sync procedure hardened.** A grep only proves the lines you
  edited are in sync; it cannot see drift in text you did not touch. Step 4 is
  now a full byte diff of the shared body from the
  `# Avenga DevFlow v<version> (Methodology)` heading to EOF, with the exact
  command and the expected result (2 differing lines: the intentional
  `agents-data/<agent>/` path). It also states that the platform preamble is
  exempt from the *verbatim* rule but not from being correct — which is where
  the truncated bullet of round 1 actually lived.
- **Review latency now covers every level.** The generator measured
  Time-to-Human-Review for `HITL-BOLT-READY`, `HITL-SPEC` and `HITL-MEM` only,
  while US and TC manifests carry the same `review_ready_at` /
  `review_started_at` contract. `HITL-US-Approval` and `HITL-TC-Approval` are
  now measured too.
- **Misattributed and stale references:** `TEMPLATE-REV.md` cited **G12** for
  the Bolt-first routing rule, which is **T10** (G12 is "no SPEC without a
  `bolt` field", correctly cited in `spec/README.md`); the AREV *Templates*
  table listed the three phase templates but not `TEMPLATE-AREV.md` itself;
  `spec/README.md`'s "Example" was still the pattern
  (`SPEC-YYMMDD-HHmm-brief-topic-description.md`), now a real filename;
  `avenga-devflow/README.md` mandated Mermaid "for every diagram" without the
  BPMN exception W08 and §5.7 grant.
- **Scope claims corrected where the repository contradicted them:**
  `open-questions/README.md` spoke of "the *Open questions* section of every
  artifact" when exactly three templates have one (VISION,
  BUSINESS-CONTEXT, SCOPE) — it now names them and says the other artifacts'
  gaps live in `open-questions/` from the start;
  `TEMPLATE-INTRODUCTION.md` suggested listing raw `INT-NNN` inputs in
  `sources`, against G28 (a derivative narrative restates approved analysis,
  never primary evidence); `TEMPLATE-TC.md` declared `PROC-NNN` traceability
  with no field anywhere to carry it, now marked narrative-only with the
  governing chain spelled out.
- **READMEs realigned with their templates** (same defect fixed in
  `functional/` in round 1): `spec/README.md` listed 17 items against the
  template's 19 sections (it omitted DoD, Revision history and
  `HITL-SPEC-Approval`); `risks/README.md` listed 11 against 6, describing as
  prose sections what the template carries as frontmatter fields;
  `discovery/README.md` listed 9 against 11 (it omitted Scope, Experiments
  performed and `HITL-DISC-Approval`).
- **Naming citations unified:** `BR-NNN.md` / `RISK-NNN.md` short forms in
  `analysis/README.md`, `business-context/README.md`,
  `business-risks/README.md` and `risks/README.md` now use the
  `-<description>` slug form their owning README declares (12 occurrences).
  CHANGELOG history untouched by convention.
- **N05/N06 filename time zone stated.** The `HHmm` of a SPEC/MEM filename is
  a local wall-clock time with no offset; it must be read in the same UTC
  offset as the artifact's `generation.created_at`, or alphabetical order
  stops matching chronological order across time zones. The precise instant
  always lives in the manifest field, never in the filename. N08's example
  also realigned with the `-e2e` Test Bolt filename of N04.
- **Minor:** the empty YAML frontmatter of `devflow/README.md` (a block whose
  only content was a comment) removed; this CHANGELOG's own heading formats
  documented at the top — `MAJOR.MINOR` today, with `[3.0.0]`/`[2.0.0]` and
  the dated-only entries preserved as written, because correcting a record's
  past headings would falsify it.
- **Left open by decision** (documented, not defects): each agent keeps its own
  Memory wording — personal memory is per-platform by design, and the shared
  boundary is the `agents-data/` paragraph, which is byte-identical across the
  four and governed by G30/G32/W21.
- No version bump: this lands inside the 4.0 cycle (`VERSION` unchanged).

### Consistency fixes (audit round 3 — regressions introduced by round 2)

Third pass. The auditor re-reviewed the corrected tree and found seven items,
**four of them defects introduced by round 2 itself** — the expected cost of
touching 71 files, and the reason the round was worth running. It also refuted
two claims round 2 had recorded as auditor errors: both were verified against
`HEAD` instead of against the commit actually audited (`bbb3da4`), where
`git show` confirms `TEMPLATE-VISION.md` had no LANGUAGE POLICY block and 18
files carried the `devflow/LANGUAGE -> Language policy` pointer. Both were
already fixed by `97547c1`. **Method note for future rounds: pin the audited
commit before declaring a finding false.**

- **Stale restatement of the localized language policy.**
  `avenga-devflow/README.md` still claimed "template section headings stay in
  **English**", contradicting §3.15 as localized in `97547c1`. It now states
  the per-family rule: headings of `analysis/`, feature User Stories and Test
  Cases follow `content_language`; every other family, this folder included,
  stays in English. The only surviving stale restatement of that commit.
- **The Judge's two-model fallback lived only in a README** (introduced by
  round 2). The repository's own hierarchy puts §2/§3 in charge of rules, and
  a `grep` for the fallback in the methodology returned nothing — it also left
  `judge_model` undefined for a human arbiter, a field W09 requires. The rule
  now lives in **§3.13**: the Verdict's model must differ from both the
  implementor's and the Challenger's; with only two models available a
  qualified human arbitrates, `judge_model` records
  `human:<git config user.name>`, and the VERDICT states why no third model
  was available. `TEMPLATE-03-VERDICT.md` and the AREV README now point there
  instead of owning the rule.
- **The new INDEX convention was violated by three indexes the same pass
  touched.** "Section order follows the artifact's own lifecycle, earliest
  state first" — yet `functional/INDEX.md` listed Approved before Draft,
  `memory/INDEX.md` Approved before Pending, and
  `adversarial-reviews/INDEX.md` Active before In progress (its enum being
  draft → in-progress → active → closed). All three reordered.
- **Two internal tensions in that convention, also introduced by round 2:**
  it mapped `superseded` to 🔄 while forbidding 🔄 for terminal states — a
  superseded ADR *is* terminal. `superseded` and `deprecated` are now both ⛔
  (the document no longer governs either way; which one it is belongs in the
  section title), 🔄 is strictly work in motion, and `adrs/INDEX.md` follows.
  And `open-questions/INDEX.md` grouped "answered + dropped" under 🏁
  *terminal and successful*, when a dropped OQ is abandonment: split into
  🏁 Answered and ⛔ Dropped.
- **`changes_requested` residue in prose:** `Avenga-DevFlow.md:1407` used the
  hyphenated form without backticks. Correct as an English compound adjective,
  but ambiguous next to an enum value — now the enum, like the other four.
- **`interviews/INDEX.md` had no `INT-NNN` column** — the very identifier that
  justifies this folder having an index at all under the criterion round 2
  wrote into `input/README.md`. Added.
- **The report's JSON contract did not declare its time unit** (introduced by
  round 2). The render divided correctly, but any other consumer had to guess.
  Durations are now self-describing: `lead_times[].avg_ms`,
  `latency[].queue_ms` / `active_ms` / `total_ms`, plus
  `meta.duration_unit: "ms"`. Template updated in lockstep.
- **A round-1 "fix" reverted — it was based on a false premise.** The audit
  reported `reports/_archive/` and `input/business/compliance/` as
  "referenced but not scaffolded", and round 1 created both with a
  `.gitkeep`. Neither needed scaffolding: §5.4 makes `_archive/` a
  **universal, on-demand** mechanism (*"every `devflow/` folder **may**
  contain an `_archive/` subfolder"*), created when a folder actually
  accumulates closed documents — and `input/business/README.md` presents its
  subfolders as an illustrative tree, created as evidence arrives.
  Pre-creating one folder's `_archive/` out of ~26, or one example subfolder
  out of several, singles it out for something that belongs to all of them.
  Both removed; the repository correctly ships **zero** `_archive/` folders.
- **Still open, by decision:** `devflow/README.md` records "**Validation
  tooling** — None ships by design" as a Known Limitation, governed by
  G23/G33. Every defect that survived a reading-based audit across these three
  rounds fell to an executable check instead (running the documented command,
  diffing the agent bodies, comparing the three manifest examples, auditing
  all 13 templates). Shipping a structural validator would therefore **revise
  that documented decision**, not merely add a script — it is left as an
  explicit choice, not an oversight.
- No version bump: this lands inside the 4.0 cycle (`VERSION` unchanged).

### Consistency audit round 4 (2026-08-16)

A full-methodology consistency audit (independent verification of every
finding against the repository) closed 24 defects across the five previous
rounds' blind spots: template-vs-schema contracts, INDEX conventions and the
agent shared body.

**Bolt acceptance review contract (A1).** `HITL-BOLT-DONE-Approval` is a
second review of the same artifact, but the contract offered only one timing
slot (readiness): the acceptance "active review time" was derived as
`decided_at − readiness review_started_at`, a meaningless number, and W11's
"every approvable artifact carries `review_ready_at` and `review:`" had no
second slot. The Bolt now carries `acceptance_review_ready_at` +
`acceptance_review:` (same shape as `review:`) in the template frontmatter,
projected to `bolt.acceptance.review_ready_at` / `review_started_at`; a new
template section "HITL-BOLT-DONE-Approval (acceptance)" holds the routing
table. Files: `functional/bolts/TEMPLATE-BOLT.md` (new §7, manifest section
renumbered to §8), `metrics/manifest-v4-bolt.schema.json` (required
`bolt.acceptance`), the three `metrics/TEMPLATE-MANIFEST-BOLT*.json` examples
(acceptance timing added, monotonic), `avenga-devflow/Avenga-DevFlow.md`
(§3.0 projection prose, §3.12 embedded example + lifecycle table + timing
contract), `GUARDRAILS.md` (review contract section), `metrics/README.md`.

**G20 Unit sequence scoped to its reserved status (A2).** G20 presented the
staging-UNIT → UAT → production-UNIT sequence as an active blocking rule
while `HITL-UNIT-Approval` is `reserved` (§3.11 entry 14) and has no
recording artifact. G20 now marks the sequence as the **intended rule**,
blocking once the Unit artifact exists; `HITL-UAT-Approval` stays active
(recorded in `tests/uat/`). Files: `GUARDRAILS.md` (G20), `tests/uat/README.md`,
the four agent definitions (checkpoint row).

**Manifest schema fixes (A3, A4).** `manifest-v4-us.schema.json` accepted
`US-000` (forbidden: it carries no manifest, §3.12/G33) — pattern now
`^US-(?!000)[0-9]{3}$`, mirroring the Bolt schema. `manifest-v4-tc.schema.json`
omitted the TC's mandatory `source_bolt` (§2.6.1 "every TC references exactly
one approved source_bolt") and let a functional TC validate with zero covered
ACs — `verifies` now requires `source_bolt` and a conditional `minItems: 1`
on `covered_acs` unless the TC is non-functional (`source_us: US-000`).
Files: both schemas, `metrics/TEMPLATE-MANIFEST-TC.json`,
`metrics/README.md`, §3.12 creation row.

**`data_classification` made normative (A5).** The enum and its ordering
existed only in two template comments although the PII/DLP gate (§3.6) and
§1 ("confidential or higher") depend on both. §3.6 now defines
`public < internal < confidential < restricted` normatively; the templates
reference it.

**§3.14 developer plan simplified (B1, B2).** "Manual katas" logged in
`memory/` were a category error (a kata is not a V-Bounce MEM), and the AREV
apprenticeship quota deadlocked against §2.15 ("AREV is never mandatory").
Both removed; the plan is now **descriptive only** — rotation, AI-review
training and quarterly skill review, creating no artifacts and recording no
evidence in `devflow/` documents. Files: §3.14, `ONBOARDING.md` §7.

**Interview transcription placement (B3).** §2.1 lets the AI transcribe
interviews, but G31 forbids agents from writing into `input/`. Clarified:
the AI may produce the transcription, a **human deposits it** into
`input/interviews/`. Files: §2.1, `input/README.md`,
`input/interviews/README.md`.

**`_archive/` sanctioned in G30 (B4).** §5.16 moves "any `_archive/`" as
project-created content, but G30's sanctioned list omitted it — an agent
archiving closed documents was technically violating G30. Added. Files:
`GUARDRAILS.md` (G30), the four agent definitions (G30 row).

**`memory/README.md` structure aligned (C1).** "Recommended structure"
listed 10 items against the template's 14 sections, omitting Files renamed
(§5) and Metrics (§12) and merging two others. Now mirrors
`TEMPLATE-MEM.md` and declares it the authority.

**INDEX consistency (C3, D1, D2, D3, D4).** The GUARDRAILS emoji vocabulary
now applies uniformly: `risks/` maps `open → 🔴`, `mitigated/materialized →
🟡`, `closed → 🏁` (was "✅ Active (open, mitigated)"); `adrs/INDEX.md` section
is "✅ Accepted" (ADR status, not "Active"); `tests/test-cases/`, `tests/uat/`,
`analysis/scope/` and `analysis/vision/` converted from text-enum legends to
emoji sections; `retros/INDEX.md` gained its `draft`/`final` sections. Five
"(Archive)" headers removed (archived documents are excluded from INDEXes,
§5.4). `analysis/vision/` and `analysis/scope/` versioning aligned to §3.15's
numbered-successor rule (`_archive/` instead of the invented
`vision-vYYYY-MM.md` naming).

**INDEX rule covers the curated inventories (E1).** §5.15's "one rule" only
described allocator INDEXes (16 families) and timestamp/machine folders — 9
distributed INDEXes (the 8 `analysis/` families without IDs and
`input/documentation/`) fit neither. Added the **curated inventory** category
(manually maintained list of ID-less documents, never an allocator), and
aligned the rival criteria in `input/README.md` and `analysis/README.md`.

**Reference and scope fixes (F1, F2, G1, H1, I1, J1, K1).**
`ONBOARDING.md` glossary reference fixed (§4, not §2); template-section
references by number replaced with heading keywords in `functional/README.md`
and `tests/test-cases/README.md` (§3.15: numbers are cosmetic);
`open-questions/` sunset rule scoped to the Bolt (G35) in README + INDEX;
`adversarial-reviews/INDEX.md` no longer calls Bolt-bound AREVs "part of the
V-Bounce" (§2.15); `AREV-NNN` added to the SPEC trigger lists and the
functional flow diagram; the US/TC progress states are now defined in §3.12
(they lived only in `metrics/README.md`); the V-Bounce lifecycle row no
longer implies the MEM review timing is written at append time.

**Judge neutrality becomes blocking (3.1).** §3.13's neutrality rule had no
guardrail and no agent carried it — the only rule that makes a Verdict valid
was the one nothing enforced. New **G37**: the Verdict's model must differ
from both the implementor's and the Challenger's; with only two models
available, a qualified human arbitrates (`judge_model: human:<user>`). Files:
`GUARDRAILS.md`, the four agent definitions (G37 row + AREV section + count
G01–G37, 37 rows), `tools/validator/RULES-G.md` (reclassified: G37 `full`,
23/10/4, 62%), `tools/validator/DESIGN.md`, `tools/README.md`, `README.md`,
`ONBOARDING.md`.

**Agent body fixes (3.2, 3.3, 2.3, 2.4, 2.6).** The `HITL-MEM-Approval`
wording now carries §3.3's handoff protocol (the incoming executor approves
a pending MEM; the outgoing cannot). The preambles' "blanket autonomy"
exception — an agent-granted authority §3.0 never defines — is replaced by
"informational pauses are skippable only by an explicit human instruction at
that moment". `codex` and `open-code` memory wording no longer contradict
themselves on `AGENTS.md` (never a memory fallback). Blank-line formatting
before "## 4. Bounded Web Research" unified in `claude`/`codex`. The
preamble parity matrix in `AGENTS.md` gained the two missing rows
(frontmatter/loader manifest, thinking mode).

**Residue cleanup after the round-4 re-audit.** A second independent pass
verified the round above and closed its five own residues: (R1) the
acceptance timestamps of `TEMPLATE-MANIFEST-BOLT-NONFUNCTIONAL.json` and
`TEMPLATE-MANIFEST-BOLT-TEST.json` violated the §3.12 monotonic chain
(`decided_at` 11:30/12:40 vs acceptance started 13:25/12:42) — corrected to
11:15→11:20→11:30 and 12:25→12:30→12:40, all three examples now monotonic
with 10–12 min of active acceptance review; (R2) `functional/INDEX.md`'s
⚙️/🔩 headings — outside the GUARDRAILS emoji vocabulary — became plain
structural headings ("Permanent container (US-000)", "Bolts") and
`functional/README.md` no longer documents them; (R3) §5.15's third
INDEX bullet contradicted the new curated-inventory bullet by routing all of
`input/` except `interviews/` to "without INDEX" — `documentation/` now
excepted explicitly; (R4) the parity matrix's "Thinking mode" row recorded a
divergence that does not exist (`mode:` is OpenCode's agent type, not a
reasoning config) — rewritten to the real divergence (claude "extended
thinking" vs the other three "sequential thinking tool if available");
(R5) `memory/README.md` anchored its structure to §1–§14 template numbers —
the exact practice §3.15 declares cosmetic — re-anchored to heading keywords;
(R6) `avenga-devflow/INDEX.md` dropped its invented ✅/⛔ status sections
(that family has no §3.15 status vocabulary) in favor of a plain curated
inventory. Files: the two Bolt manifest examples, `functional/INDEX.md`,
`functional/README.md`, §5.15, `AGENTS.md`, `memory/README.md`,
`avenga-devflow/INDEX.md`.

**Last 🟢 residue closed after the third pass.** `TEMPLATE-INTRODUCTION.md`
still referenced its own "§7" from the authorship comment — the last
instance of the template-section-number class §3.15 declares cosmetic;
re-anchored to the heading keyword ("Where to read next"). The only
remaining open item is the OWASP self-review criterion in the four agent
definitions, kept deliberately without a normative anchor in §3.6.

### Version bump

- `VERSION` → `4.0`; markers bumped in lockstep in `AGENTS.md`,
  `README.md`, `GUARDRAILS.md` (header + footer), `ONBOARDING.md`,
  methodology frontmatter, `avenga-devflow/README.md` + `INDEX.md`, every
  folder's `**Methodology version:**` header (32 files), and the four agent
  definitions.
- Section references (`§3.3`, `§3.12`...) are section numbers, not version
  markers — untouched.

---

## [3.3] — 2026-08-14 — Risk-proportional non-functional BUG approval

**Avenga DevFlow v3.3.** Architect/Tech Lead approval of every non-functional
BUG regardless of size created unnecessary review load for trivial, low-risk
defects (e.g. a one-line CSS style fix). The fix introduces severity-gated
routing so only `critical`-severity non-functional BUGs (and their dedicated
Bolt) still require Architect/Tech Lead sign-off, while `high`/`medium`/`low`
route to a Developer other than the BUG's own author, preserving segregation
of duties via a self-approval safeguard.

### Severity-gated `HITL-BUG-Approval` for non-functional BUGs (§2.16)

- **Routing key:** the existing `severity` frontmatter field on `BUG-NNN`
  (`critical | high | medium | low`) — no new field introduced.
- **New rule:** for a non-functional BUG, `severity: critical` still routes
  `HITL-BUG-Approval` to an **Architect or Tech Lead** (unchanged). `severity:
  high`, `medium`, or `low` may instead be approved by **a Developer**.
- **Self-approval safeguard:** the approving Developer must not be the same
  person recorded as the BUG's own `owner` (the person who drafted it) —
  self-approval is not permitted under this exception.
- **New blocking guardrail G29** — enforces the safeguard rather than leaving
  it in prose: blocks recording `HITL-BUG-Approval` on a non-functional BUG as
  its own author, mirroring that self-approval on the dedicated Bolt, and
  routing a `severity: critical` non-functional BUG to a Developer. Appended
  with the next free number (G01–G28 are cited across the methodology and the
  four agents, so renumbering was not an option) in the ORIGIN phase table
  where it belongs topically — the same append-at-the-end precedent used for
  W18/W19 in 3.2.
- **`T02` traceability check extended** — the recorded reviewer of a
  non-functional BUG must match its `severity` route and never be the
  artifact's own `owner`/author, making the safeguard auditable.
- **Dedicated Bolt mirrors the same routing:** the ONE dedicated Bolt created
  for a non-functional BUG (§2.16, `bugs/README.md`) has its own
  `HITL-BOLT-READY-Approval` follow the parent BUG's severity — Architect/Tech
  Lead when `critical`, otherwise a Developer other than the Bolt's own
  author.
- **Functional BUGs are completely unaffected:** still always Functional
  Analyst, regardless of severity.
- **Scope boundary — unchanged:** generic non-functional Bolts *not* tied to a
  BUG (created directly from an approved ADR, Discovery conclusion, Review
  finding, tech-debt evidence, or a refactor/infra/hardening/debt
  `work_category`) keep the existing rule — Architect or Tech Lead only.
  Every place that states this general rule (Bolt-type ownership table,
  §3.0 HITL checkpoint table, §3.0 "Levels" section, and their echoes in
  `functional/README.md`, `TEMPLATE-BOLT.md`, `GUARDRAILS.md`, `README.md`)
  gained a short parenthetical/footnote noting the one exception instead of
  being rewritten. SPEC, MEM, ADR, Test Bolt approval and
  `HITL-BOLT-DONE-Approval` are unaffected.

### Propagation

- **`devflow/bugs/README.md`** — lifecycle table's `approved` row rewritten
  severity-conditionally; new Rule 9 states the routing and the self-approval
  safeguard.
- **`devflow/bugs/TEMPLATE-BUG.md`** — §5 classification table and §8
  `HITL-BUG-Approval` prose updated; self-approval safeguard stated
  explicitly.
- **`devflow/functional/bolts/TEMPLATE-BOLT.md`** — `HITL-BOLT-READY-Approval`
  Approver row gained the BUG-driven-Bolt exception parenthetical.
- **`devflow/functional/README.md`** and
  **`functional/user-stories/US-000-non-functional.md`** — ownership table
  and Rule 5 updated in lockstep.
- **`avenga-devflow/Avenga-DevFlow.md`** — every BUG-approval-specific
  restatement (§2.16, §3.0 checkpoint table, §3.0 prose, §3.9 minimum roles,
  §3.11 Levels, §5.12 folder table) rewritten severity-conditionally; every
  generic non-functional-Bolt-approval restatement (Bolt-type ownership
  table, §3.0 Bolt-readiness row, §3.11 Bolt Readiness level) gained the
  exception footnote only.
- **`GUARDRAILS.md`** — HITL checkpoint map's `HITL-BUG-Approval` row
  rewritten severity-conditionally; `HITL-BOLT-READY-Approval` row gained
  the exception parenthetical; new blocking guardrail **G29** in the ORIGIN
  phase table; **T02** extended with the approver-identity check.
- **`ONBOARDING.md`** — Architect/Tech Lead role-table cell now notes the
  severity exception; guardrail summary count updated to 29 blockers.
- **`README.md`** (devflow folder map) — both HITL table rows updated to
  match.
- **All four platform agents** (`claude`, `codex`, `open-code`, `gh-copilot`):
  condensed `HITL-BUG-Approval` and `HITL-BOLT-READY-Approval` table rows and
  the bug-fix workflow step rewritten to the same severity-conditional
  routing, in the existing terse style; **G29** added to each key-blocking-rule
  summary table and the guardrail range counters updated to `G01-G29`.
- **No changes to:** functional BUG/Bolt routing, SPEC/MEM/ADR approval, Test
  Bolt approval, or `HITL-BOLT-DONE-Approval` — all out of scope for this
  change.

### `_archive/` agent access rule refinement (§5.4)

Archiving itself already existed (§5.4 — lifecycle-closed documents move to
each folder's `_archive/` subfolder, agents ignore them for evidence
scanning). This release sharpens the agent-side behavior so archived
documents cost no tokens unless actually needed:

- **Access only on request or explicit reference:** agents must not search,
  list, or read `_archive/` proactively (token economy). They access it only
  when the user explicitly asks, or when an active document explicitly
  references an archived artifact (e.g., an incident linking to the
  deployment that caused it).
- **Transparency to the user:** when a task would require archived content,
  the agent states that `_archive/` files are excluded from its scan and
  asks the user whether to consult them — users should treat archived files
  as generally invisible to agents.
- **New warning W20** — "Search or read `_archive/` proactively without an
  explicit user request or an explicit reference to an archived artifact".
  Appended as the next free warning number (W01–W19 were untouched);
  warning counts updated to 20 in `ONBOARDING.md` and the four agents'
  guardrail range counters (`W01-W19` → `W01-W20`).
- **User-facing awareness in `ONBOARDING.md`** — the exclusion changes what
  users may expect from an agent, so it is stated where users actually read
  rather than only in the normative doc and the agent instructions: a new
  `_archive/` glossary row and a new FAQ entry ("Why does the agent not see
  my archived documents?").
- **No changes to:** archiving criteria, mechanism, INDEX discipline,
  reference immutability, or ID reuse rules — §5.4 and the agents'
  Archiving bullets otherwise unchanged.

### Canonical folder structure, `agents-data/`, and `input/` write protection (§5.12)

Field observation: agents (notably Codex) occasionally improvised new folders
inside `devflow/`, and nothing stopped an agent from writing into `input/`,
whose raw material is human-deposited evidence. This release sanctions one
agent-owned area and closes both holes:

- **New folder `devflow/agents-data/`** — per-agent shared knowledge area,
  versioned with the repository and shared with the whole team. There are
  **no pre-created subfolders**: each agent creates its own
  `agents-data/<agent-name>/` folder on first use (creation is sanctioned by
  G30) and is responsible for everything inside it, free to create files and
  subfolders there. Content is durable, team-useful knowledge; it is never
  governed input (no HITL, no lifecycle, no `review:` contract), agents do
  not scan other agents' folders by default (token economy, same principle
  as `_archive/`), and it is not a substitute for `memory/` MEMs (§2.12).
- **New warning W21** — using `agents-data/` for temporary or disposable
  data. The folder is versioned and team-shared, so temporary data (drafts,
  tool outputs, large intermediates) goes to the OS temp directory and is
  never committed; warning counts updated to 21 (`W01-W20` → `W01-W21`).
- **New blocker G30** — creating a new folder inside `devflow/` outside the
  canonical structure. The only sanctioned agent-created areas are the
  per-agent folders under `agents-data/` — each agent creates its own on
  first use and may freely organize files and subfolders **within** it, the
  carve-out that makes the area usable without reopening the hole G30
  closes — and the per-AREV folders
  `adversarial-reviews/AREV-NNN-<description>/` (§2.15).
- **New blocker G31** — writing, saving, or moving files into `devflow/input/`
  or its subfolders. Agents may still read `input/` as evidence (SPEC
  inventory, analysis); only deposition is human-only (§5.6).
- **New blocker G32** — citing `agents-data/` content as the source or
  justification of a SPEC, Bolt, ADR, US, TC, BUG, MEM, or any HITL
  checkpoint (same class as the G28 derivative-document rule).
- **Propagation:** `agents-data/` added to the **§5.1 canonical tree** (the
  tree G30 measures "canonical" against, so omitting it would have made the
  sanctioned folder read as a G30 violation — same step the 3.1 entry
  performed for `analysis/introduction/`); §5.12 gained the
  canonical-structure rule and the `agents-data/` row (per-agent folders are
  created on first use, each agent responsible for its own); §5.6 states the
  `input/` write protection; new `devflow/agents-data/README.md`;
  `input/README.md` gained the agent write-protection note; folder map in
  `devflow/README.md`; ONBOARDING glossary row + FAQ, blocker count (29 →
  32) and warning count (20 → 21) updated; all four agents gained G30–G32
  rows, the per-agent working-data bullet, and the guardrail range counters
  updated to `G01-G32` / `W01-W21`.
- **Platform-agnostic memory (no hardcoded paths):** the agent `Memory`
  sections no longer name platform memory locations (previously
  `.github/instructions/memory.instruction.md` in gh-copilot and
  `CLAUDE.local.md` / `~/.claude/CLAUDE.md` in claude). Platforms change
  where they keep memory without notice; the methodology defines the *what*
  — personal/session memory → each platform's native mechanism, durable
  shared knowledge → `agents-data/<agent>/`, governed implementation memory
  → `memory/` MEMs — and never the *where*. The principle is recorded
  normatively in **§5.2** (agent definitions), not only repeated in the four
  agent files: without it the agents would assert a methodology rule the
  methodology itself never stated, and a future fifth platform definition
  would have nothing to follow.
- **No changes to:** artifact routing, naming, HITL checkpoints, archiving,
  or any governed-artifact lifecycle — `agents-data/` is strictly outside the
  governed chain.

### Version bump (opening the 3.3 cycle)

- **`VERSION`** normalized to `3.3`; version markers bumped in lockstep in
  `README.md`, `GUARDRAILS.md` (header + footer link), `ONBOARDING.md`,
  `AGENTS.md`, methodology frontmatter, `avenga-devflow/README.md` and
  `avenga-devflow/INDEX.md`, every folder's `**Methodology version:**`
  header (31 files), and the four agent definitions.
- **Section references left untouched** — `§3.2`, `§3.2.1` and similar are
  section numbers, not version markers; the manifest `schema_version` stays
  `"3.0"` (it versions the JSON data contract and did not change).

---

## [3.2] — 2026-08-13 — Story points on feature USs, AI-native Bolt estimation rule

**Avenga DevFlow v3.2.** Two estimation improvements motivated by field
usage: agents were estimating Bolt active delivery time as if code were
written manually, producing estimates far above what an AI-generated
delivery actually costs; and no early complexity signal existed at the US
level before decomposition into Bolts.

### Story points on feature User Stories (§2.6)

- **New `story_points` field** on feature USs — Fibonacci scale (1, 2, 3, 5,
  8, 13) expressing the **relative complexity of the functional scope**
  (number and intricacy of ACs, business rules, flows, integration surfaces,
  unknowns) — never time. The agent may propose the value when drafting the
  US; the Functional Analyst confirms or corrects it as part of
  `HITL-US-Approval` (no new checkpoint).
- **Informational only, by design:** no checkpoint, gate or guardrail
  depends on story points; weekly planning keeps forecasting with throughput
  and Bolt Lead Time (§4.3); no velocity metric or performance target may be
  derived; converting points into hours is invalid. US-000 never carries
  story points.
- **New warning W18** — converting story points into hours, gating any
  checkpoint on them, or deriving a velocity/performance target from them.
- **Scoring rubric in §2.6** — per-value anchor table over the five
  dimensions (ACs, business rules, flows, integrations, unknowns) with three
  application rules: score the **highest dimension, never the average**;
  score relative to approved USs in `functional/INDEX.md` when they exist
  (absolute anchors otherwise), with open OQs targeting the US as objective
  unknowns evidence; and **13 as a splitting signal** proposed before
  `HITL-US-Approval` — the US-level equivalent of the one-day Bolt ceiling —
  which the Functional Analyst may still approve when splitting is not
  viable. Compressed versions in `TEMPLATE-US.md` and the four agents.
- **Expected decomposition bands (§2.6)** — plausibility check relating
  story points to the expected **number** of Bolts (1–2 SP → 1–2 Bolts;
  3–5 → 2–4; 8 → 4+), never to hours (W18). A decomposition far outside its
  band signals re-examining the score or the slicing — it is never a target
  to force. Echoed in `TEMPLATE-US.md` and the four agents.
- `TEMPLATE-US.md` gained the frontmatter field, a summary-table row and the
  governance comments; the methodology §2.6 paragraph is the normative
  anchor.

### AI-native estimation rule for Bolts (§2.4)

- **Problem addressed:** LLM agents anchor Bolt estimates on human-effort
  heuristics (pricing code creation as typing time), inflating active
  delivery estimates several-fold. In DevFlow the dominant cost is human
  review and rework — generation is minutes, and review budgets are already
  normed per risk_class (§3.0).
- **New normative rule in the §2.4 sizing note:** compose the estimate from
  the delivery cycle itself — `expected V-Bounces × (agent generation +
  MEM/V-Bounce review budget for the risk_class) + SPEC review + acceptance
  + setup/integration overhead`. Anchors: most low/medium Bolts land in
  **1–4h** of active delivery; one working day is the ceiling, not the norm;
  an estimate exceeding one day signals manual-effort anchoring before it
  signals a split.
- **DoR bullet updated** — the estimation item now cites the rule.
- **New warning W19** — estimating a Bolt's active delivery time as manual
  coding effort.
- **Calibration loop closed in retros** — new §3.7.4 decision rule and
  `TEMPLATE-RETRO.md` checklist item: estimates drifting ≥ 2× from actual
  active delivery (manifest durations + decomposed Bolt Lead Time) trigger
  recalibration; where story points are used, correlate them against actual
  aggregated Bolt Lead Time per US.
- `TEMPLATE-BOLT.md` estimation guidance added next to the splitting
  heuristics; `TEMPLATE-US.md` Bolts-table note covers the
  `Est. active delivery` column.

### Propagation

- **All four platform agents** (`claude`, `codex`, `open-code`,
  `gh-copilot`): story-points proposal guidance added after the task-routing
  table, Sizing bullet extended with the estimation rule, warning counters
  updated to W01–W19.
- **`ONBOARDING.md`** — glossary: Bolt row cites the estimation rule; new
  Story points row; guardrail summary count updated to 19 warnings.
- **No changes to** manifest v3 / `manifest-v3.schema.json` (story points
  are not traceability evidence), the §3.7 metric catalog (deliberately no
  velocity metric), US-000, or `TEMPLATE-TC.md`.

### Consistency fixes (external cross-review)

An independent cross-document review (Claude Sonnet) flagged three stale `§`
pointers in the methodology — leftovers of an earlier section renumbering —
and two alignment details. All verified and corrected:

- **§2.11 deployment definition** — the label cited §2.14 (= Review); the
  paragraph *is* the definition, so the self-pointer was dropped (the DORA
  baseline citation §3.7.1 already follows in the same sentence).
- **§2.13 spike-Bolt note** — "Why this is not circular" cited §2.5
  (= V-Bounce); the governing "no code without an approved Bolt" rule lives
  in §2.4.
- **§3.0 MEM-approval rule** — "assigned owner in the weekly plan" cited
  §3.9 (= Minimum roles); the weekly plan with owners is §4.3.
- **`README.md` "One path into V-Bounce"** — the trigger list omitted DISC
  and ADR while the four agents list all six origins; diagram and table rows
  aligned to `US | BUG | TC | DISC | REV | ADR` with their origin approvals.
- **`ONBOARDING.md` glossary** — story points range rewritten as the
  discrete Fibonacci scale (1|2|3|5|8|13), not a continuous "1–13".

### Version bump (opening the 3.2 cycle)

- **`VERSION`** normalized to `3.2`; version markers bumped in lockstep in
  `README.md`, `GUARDRAILS.md` (header + footer link), `ONBOARDING.md`,
  `AGENTS.md`, methodology frontmatter, `avenga-devflow/README.md` and
  `avenga-devflow/INDEX.md`, every folder's `**Methodology version:**`
  header (31 files), and the four agent definitions.
- **Section references left untouched** — `§3.1`, `§3.3.1` and similar are
  section numbers, not version markers; the manifest `schema_version` stays
  `"3.0"` (it versions the JSON data contract, and the manifest structure
  did not change).

---

## [3.1] — 2026-08-11 — `analysis/introduction/`, Claude Code agent, consistency fixes

**Avenga DevFlow v3.1.** Incremental release: a new plain-language entry
point for the analysis phase, a fourth platform agent, and a consistency
pass across the framework.

### New folder `analysis/introduction/`

- **Plain-language feature narratives** — one document per feature, written
  as a jargon-free story for someone joining the project. README + INDEX +
  `TEMPLATE-INTRODUCTION.md`.
- **Derivative documents** (`derivative: true`): written *last* in the
  analysis phase, derived from `vision/`, `scope/`, `domain-model/`,
  `process/`, `glossary/`, `open-questions/` and `discovery/`. Never a
  source of truth, never governed input, outside the HITL chain — where a
  narrative and an artifact disagree, the artifact wins.
- **Methodology §5.5 added (Derivative narrative documents)** — the
  normative anchor for this document class, filling the previously vacant
  §5.5 slot (numbering of §5.6–§5.15 unchanged). Also added: `introduction/`
  to the §5.1 canonical tree, a row in the §5.7 analysis table, a row in the
  §5.15 artifact routing summary (descriptive filename, no ID), and a note
  in §4.1 step 2 (may be derived once the feature's artifacts exist in
  draft).
- **Cross-references updated** — `README.md` folder map,
  `analysis/README.md` (subfolder table, flow diagram, write-last /
  read-first note), `ONBOARDING.md` reading order ("Everyone" starts at
  `analysis/introduction/` when present).

### New agent `agents/claude/`

- **`CLAUDE.md`** — AvengaDevFlow agent definition for Claude Code,
  regenerated from `gh-copilot/AvengaDevFlow.agent.md` with platform
  adaptations (WebFetch/WebSearch tools, TodoWrite task tracking, Claude
  Code memory files `CLAUDE.local.md` / `~/.claude/CLAUDE.md`), plus a
  "Derivative Documents" section covering `analysis/introduction/`.
- **`readme.txt`** — installation: copy to the repository root as
  `CLAUDE.md`; Claude Code loads it automatically.
- `AGENTS.md`, `README.md` and methodology §5.1/§5.2 updated to list the
  four platform agents.

### Consistency fixes

- **`agents/codex/` description corrected** in `README.md` and methodology
  §5.2: the folder ships `SKILL.md` (no `config.toml`).
- **`analysis/introduction/INDEX.md`** — removed a project-specific document
  reference left over from a real project; replaced with the standard
  placeholder row used by the other analysis INDEXes.
- **`analysis/introduction/README.md`** — governance rule now cites G13 +
  G27 (approved-artifacts-only) and the new §5.5.
- **Version alignment** — `VERSION` normalized to `3.1`;
  methodology frontmatter, `GUARDRAILS.md`, `ONBOARDING.md`, `AGENTS.md`,
  `avenga-devflow/INDEX.md`, all folder `**Methodology version:**` headers
  and the four agent definitions bumped to 3.1 (historical mentions of
  3.0.0 in this changelog and in methodology prose kept as-is). The
  manifest `schema_version` stays `"3.0"`: it versions the JSON data
  contract, not the methodology, and the manifest structure did not change.
- Existing agents (`gh-copilot`, `open-code`, `codex`) re-versioned to
  3.1 with `Introduction` added to their template catalogs.

### Consistency audit — corrections

A full cross-document audit (section references, links and paths, normative
contradictions, agent drift) was run before release. Findings applied:

**Normative source (`avenga-devflow/Avenga-DevFlow.md`)**

- **§3.6 — E2E/contract gate scoping disambiguated.** The same test types
  were listed both as a per-Bolt conditional gate ("when the change crosses
  component boundaries") and under "Unit / Milestone level gates, NOT per
  Bolt", with nothing distinguishing them. Now explicit: the per-Bolt gate
  covers boundary crossings **within the Bolt's scope**; the Unit-level suite
  covers **cross-Bolt** regressions, and neither substitutes for the other —
  a boundary-crossing Bolt may not record its gate `n/a` because the Unit
  will cover it.
- **§3.12 — `hitl_approvals[]` at Bolt creation.** The lifecycle table said
  the array starts empty while `TEMPLATE-BOLT.md` said the origin decisions
  are already present. Resolved in favor of the template's intent (origin
  approvals genuinely precede the Bolt): the manifest is created with
  `HITL-US-Approval` (functional), `HITL-TC-Approval` (test) and
  `HITL-BUG-Approval` (BUG-driven) already recorded; a US-000 Bolt has no
  origin approval and starts empty. `metrics/README.md` aligned.
- **Four misdirected `§` pointers repaired** (leftovers of an earlier
  renumbering): repository-topology note (pointed at §2.8 = ADR), file
  overlap between active Bolts (§2.3 = Unit → §2.4.1), escalation
  consequences (§2.6 = User Stories) and schema-evolution policy (§2.15 =
  Adversarial Review). The last three were self-references inside the
  governing section and were dropped rather than renumbered.
- Stale "not covered by v3.0.0" replaced with "not covered by this version".

**`GUARDRAILS.md`**

- **G20 completed with the release sequence** — it required only
  `HITL-UNIT-Approval` to release a Unit, omitting that §3.11 puts
  `HITL-UAT-Approval` before the production UNIT approval and requires
  **both**. An agent enforcing the old text could clear a production release
  with no business sign-off.
- **AI-native gates section** now also lists the per-Bolt conditional classic
  gates and states that the Unit-level suite never substitutes them.
- `bolt_class` removed from the G23 denylist (a v2 concept the methodology no
  longer defines), aligning G23 with the §3.12 exclusion list.
- G27 range citation normalized to `§2.13–§2.15`.

**`ONBOARDING.md`**

- Glossary pointer corrected from §4 (End-to-end process) to **§2**.
- Stakeholder/PO row now names `HITL-BOLT-DONE-Approval` — their
  highest-frequency checkpoint, previously unmentioned in their reading path.

**Templates and indexes**

- **Nine templates** (ADR, BUG, BOLT, US, DISC, REV, AREV 01/02/03) shipped
  `findings: []` together with `acknowledged_without_comment: false` — the
  exact state W11 declares invalid. Aligned with the compliant default
  already used by SPEC/MEM/TC/UAT.
- **`functional/INDEX.md`** gained Bolt tables (functional / non-functional /
  test). `functional/bolts/` has no INDEX of its own, so there was no source
  for the next `BOLT-NNN` despite the naming rule requiring one.

**Agent definitions (all four)**

- **`Derivative Documents (analysis/introduction/)` back-ported** to
  `gh-copilot`, `open-code` and `codex`. They had been told to *write*
  introduction narratives without being told these are never governed input —
  and `ONBOARDING.md` puts that folder first in every role's reading path, so
  the gap was reachable in normal use.
- HITL coverage targets now carry the "plus `HITL-ADR-Approval` and all
  conditional DISC/REV/AREV approvals" clause; without it an agent could
  report 100% coverage with an unapproved ADR.
- L4 autonomy states it is **reserved for sandboxed experiments**, not merely
  ADR-gated.
- `HITL-BOLT-READY-Approval` row restored Architect / Tech Lead as valid
  approvers for Test Bolts.
- Template catalog adds `TEMPLATE-US.md` and notes that domain-model
  templates live one level deeper than the catch-all glob reaches.
- `analysis/introduction/` added to the first-session reference documents.

**Completeness pass on the `derivative` concept**

A second review flagged that §5.5 introduced a concept the enforcement layer
did not know about. Closed:

- **New blocking rule G28** — citing a derivative document (`derivative: true`,
  i.e. anything in `analysis/introduction/`) as the source of a SPEC, Bolt,
  ADR, User Story or Test Case. Until now the rule existed only as prose in
  §5.5; G13 covered it indirectly and only for SPECs, leaving ADRs, USs and
  TCs unguarded. Added to GUARDRAILS and to all four agents; rule counters
  updated to G01–G28 repo-wide.
- **New naming rule N23** — introduction narratives (`<feature-description>.md`,
  descriptive, no ID). It was the only artifact class whose naming lived
  outside the N table, defined only in §5.15 and the folder README. The table
  now notes it is the sole artifact without a sequential ID, because nothing
  may reference it as evidence.
- `introduction/README.md` — the governance paragraph cited G13 + G27, neither
  of which is about derivative documents; now cites G28 and §5.5.
- **Six source READMEs** (`vision/`, `scope/`, `glossary/`, `domain-model/`,
  `process/`, `open-questions/`) gained a "Feeds the introduction narrative"
  note. The write-last rule was only visible from `analysis/README.md` and
  from the target folder, never from where the work actually happens.
- `introduction/README.md` and `INDEX.md` dropped their
  `**Methodology version:**` header — they were the only two files in the
  eleven `analysis/` subfolders carrying one.

**Platform-specific**

- **`codex/SKILL.md` gained its mandatory YAML frontmatter** (`name`,
  `description`). Without it the Codex parser rejects the file outright —
  the skill was not loading at all. `readme.txt` rewritten in English with
  the current paths (`.agents/skills/` project scope, `~/.agents/skills/`
  personal) and a note about the legacy `~/.codex/skills/` location.
- **`gh-copilot`** — body referenced `fetch_webpage` and `get_errors`, which
  are not valid `tools:` entries; replaced with the declared `web/fetch` and
  `read/problems`. Removed `vscode/memory` (no such documented tool) and the
  unrecognized `version:` frontmatter key. MCP-dependent tools annotated as
  optional, plus a note that Visual Studio 2026 reads the same file with a
  different tool vocabulary. Memory section now warns against writing
  personal preferences into the shared `AGENTS.md`.
- **`open-code`** — one-word `description` replaced with a functional one
  (OpenCode uses it for routing); the deliberate `permission: ask` mode
  documented inline; `readme.txt` adds the project-scoped
  `.opencode/agents/` path so the definition travels with the repo.
- **`claude/CLAUDE.md`** — removed a sentence about markdown todo lists left
  orphaned by the switch to TodoWrite; diagnostics step now points at the
  project's own linter/type-checker (the IDE-only phrasing was a no-op in a
  bare CLI session); added the §5.5 `deprecated` rule for stale narratives
  and a search-reformulation fallback.

---

## [3.0.0] — 2026-08-02 — Methodology rewrite: named HITL checkpoints, three Bolt types, minimal manifest v3

**Avenga DevFlow v3.0.0.** This release is a deep rewrite of the methodology
and the full documentary implementation. The methodology document
(`avenga-devflow/Avenga-DevFlow.md`) was redesigned (v17 → v18 → v19, final
`Avenga-DevFlow.md`) and every folder, template and agent definition was
aligned to it, with each folder audited by an independent reviewer subagent.

### Methodology at a glance (v3)

- **Named HITL checkpoints** — `HITL-<CODE>-Approval` for every artifact
  (US, BUG, TC, BOLT-READY, BOLT-DONE, ADR, SPEC, MEM, DISC, REV,
  AREV-CRITIQUE/DEFENSE/VERDICT, UNIT, UAT). Legacy numbered aliases
  (H1–H6) are invalid. Approvals are never inherited.
- **Three and only three Bolt types** — `functional` (approved feature US),
  `non-functional` (`US-000` container), `test` (one approved TC,
  `TC-NNN.BOLT-NNN`). BUG and hotfix are conditions, not types.
  `work_category` and `service_class` are orthogonal taxonomies.
- **One canonical SPEC per Bolt** — revised in place (`spec_revisions[]`);
  one V-Bounce never spans two SPEC revisions. Pre-SPEC evidence gate:
  blocking report if any governed source is unapproved.
- **Exactly one MEM per V-Bounce** — stable kebab-case slug, no mutable
  status (derived from `HITL-MEM-Approval`), immutable after decision,
  mandatory even on blocked/failed V-Bounces. Approved by the Dev-validator
  who executed the Bolt (+QA/Sec for high/critical).
- **Bolt Manifest v3 (minimal)** — `schema_version: "3.0"`, `bolt`,
  `spec_revisions[]`, `v_bounces[]`, `hitl_approvals[]`. Deliberately
  excludes gates, tests, DORA, deployment, cost, AREV, risk, autonomy and
  data classification. Validated by `manifest-v3.schema.json` (normative
  JSON Schema, draft 2020-12).
- **DORA Five** — D1 Deployment Frequency, D2 Change Lead Time,
  D3 Failed Deployment Recovery Time, D4 Change Fail Rate,
  D5 Deployment Rework Rate. Computed at deployment level from CI/CD +
  incidents. No universal "Elite" thresholds; Bolt Lead Time is a separate
  flow metric, never D2.
- **Strict TDD in ONE V-Bounce for BUGs** — reproduction test → red
  evidence → production change → green. One dedicated Bolt per approved
  BUG (never reuse an unrelated Bolt).
- **AREV optional for ALL risk classes** — stakeholder-triggered; three
  sequential phase approvals; manual agent/model selection between phases;
  no manifest impact.
- **Test Cases as independent verification contracts** — derived from
  approved intent, never from code as oracle (test-basis rule);
  `HITL-TC-Approval` before governing a SPEC or originating Test Bolts.
- **Review contract** — every approvable artifact carries
  `review_ready_at` + `review{}` (decision, reviewers, started_at,
  decided_at, findings, acknowledged_without_comment, acknowledgment_reason)
  as machine-readable metadata.
- **`devflow/LANGUAGE` file** — the project's `content_language` is declared
  once there (like `VERSION`); prose follows it, schema is always English.
- **Sizing doctrine** — 1 hour to 1 working day of *active delivery time*,
  not a destructive boundary; crossing a day never splits a Bolt.

### Documentary implementation (all folders aligned + audited)

- **`avenga-devflow/`** — Methodology rewritten as single source of truth;
  README + INDEX aligned.
- **`metrics/`** — New normative `manifest-v3.schema.json` (draft 2020-12,
  strict `additionalProperties: false`); `TEMPLATE-MANIFEST.json` converted
  from a v2 schema into a validating v3 example; README rewritten.
- **`GUARDRAILS.md`** — Rewritten from v2 (17 blocking) to v3 (27 blocking
  G01–G27 organized by lifecycle phase + 17 warnings W01–W17 + N01–N22 +
  T01–T12), with the HITL checkpoint map, review contract, coverage by Bolt
  type and risk rubric. Audited and corrected (BPMN allowance, primary-
  outcome classification, min approvers at HITL-MEM-Approval).
- **`README.md` (root)** — v3 flow, HITL map, cheat sheet, language via
  `LANGUAGE`.
- **`ONBOARDING.md`** — Rewritten (approach A: role-based reading order,
  one Bolt path, minimal glossary, FAQ, dev plan). Readability-reviewed by
  subagent.
- **`AGENTS.md` (root)** — New bootstrap pointing every AI tool at the
  methodology, GUARDRAILS and the platform agents.
- **`agents/`** — `gh-copilot/AvengaDevFlow.agent.md` updated to v3
  (versioned 3.0.0, HITL pause enforcement, manifest v3, tools de-duped);
  `open-code/AvengaDevFlow.md` and `codex/SKILL.md` regenerated from it
  with platform-specific adaptations (webfetch/web_fetch, AGENTS.md memory,
  no Copilot-specific residue). All audited.
- **`analysis/`** — 36 files aligned: H5→HITL-UAT-Approval, OQ sunset rule
  at readiness (`HITL-BOLT-READY-Approval`), Functional Analyst as governor,
  `LANGUAGE` references, pre-existing mojibake repaired, `indexing`/templates
  consistent.
- **`functional/`** — Three Bolt types, `work_category`/`service_class`,
  US-000 as container (no ACs, no approval), `HITL-US-Approval`/
  `HITL-BOLT-READY-Approval` review contracts, manifest v3 creation guidance,
  `risk_history`. Templates rewritten.
- **`spec/`** — One canonical SPEC per Bolt, pre-SPEC evidence gate,
  `HITL-SPEC-Approval`, BUG single-V-Bounce TDD, security/data + AC mapping
  + stop conditions sections, gates table with AI-native gates enumerated.
- **`memory/`** — MEM without mutable status, stable slug + collision rule,
  `execution_outcome`, baseline, renamed files, evidence links, complete
  HITL-MEM-Approval record, metrics sourced from manifest v3/telemetry,
  INDEX.md created.
- **`bugs/`** — BUG lifecycle (draft → approved → in-fix → fixed → closed),
  dedicated Bolt rule, `HITL-BUG-Approval` review contract, red/green
  evidence, `HITL-BOLT-READY-Approval` + `HITL-SPEC-Approval` in the chain.
- **`adrs/`** — `HITL-ADR-Approval` (no H6), draft → accepted lifecycle,
  waiver with reason/owner/compensating control/expiry, review contract,
  NFRs governed inside ADRs. Methodology §3.11 "status = accepted" fixed.
- **`adversarial-reviews/`** — Three sequential phase approvals, no
  modular depth (all initiated AREVs run 3 phases), no manifest impact,
  manual model selection, review contract per phase.
- **`reviews/`** — `HITL-REV-Approval` (no H2), findings draft until
  approval, Bolt-first (G12→T10 citation fixed), comparison table v3.
- **`discovery/`** — Need-driven investigation, `HITL-DISC-Approval`,
  spike rule, analysis-first flows, research_question/scope/experiments.
- **`incidents/`** — DORA Five mapping (no D3=CFR/D4=MTTR), referential
  links (no manifest DORA writes), no single-model attribution, severity
  sev1–sev4.
- **`risks/`** — risk_class at `HITL-BOLT-READY-Approval`, Bolt frontmatter +
  `risk_history`, AREV optional, escalation/no-downgrade rule.
- **`retros/`** — DORA Five opener, internal baselines (no Elite bands),
  §3.7.4 decision rules checklist, improvement Bolts as hardening under
  US-000.
- **`tests/`** — Test Cases as verification contracts (source_bolt,
  functional/non-functional, test-basis rule, `HITL-TC-Approval`),
  UAT with `HITL-UAT-Approval` (no H5, no manifest UAT data). `owner`
  added repo-wide to US/BUG/BOLT/TC templates.
- **`input/`** — Read-only evidence semantics, provenance + impact
  assessment (§5.6), analysis-first flows, interviews aligned to §3.4.

### Key non-goals / decisions

- **No regression-eval Bolt / model-change ADR** for AREV phase switching
  (§3.13 is manual agent/model selection).
- **No micro-Bolt** concept — G05 remains blocking; urgency/size create no
  exception.
- **No modular AREV depth** (standard/light removed) — §2.15 mandates all
  three phases once initiated.
- **Manifest v3 stays minimal** — review evidence and DORA live in their
  artifacts; the manifest is a traceability/AI-usage record.
- **VERSION bumped to 3.0.0**; `devflow/LANGUAGE` added (content `en`).

---

## [2.0.0] — 2026-06-08 — First Stable Version

**Avenga DevFlow reaches its first formally versioned release.** This
baseline consolidates the complete methodology as it stands after 16
pre-release iterations (2026-05-01 to 2026-06-08).

### Methodology at a glance

- **5 phases:** Input → Understand → Define → V-Bounce → Govern
- **18 artifact types** with naming conventions (US, BOLT, SPEC, MEM,
  ADR, REV, BUG, RISK, INC, RETRO, AREV, DISC, OQ, PROC, TC, UAT, INT, BR)
- **6 HITL checkpoints:** H1 (DoR) → H2 (V-Bounce approval) → H3 (Bolt
  acceptance) → H4 (Promotion) → H5 (UAT) → H6 (ADR ratification)
- **V-Bounce micro-cycle:** AI generates 100% code + tests → gates →
  MEM → manifest → human review
- **~180 guardrail rules** across 10 categories (Bolt, SPEC, MEM, Manifest,
  HITL, Naming, Reviews, Bugs, Traceability, General)
- **Bolt Manifest v3 (Accumulative)** schema with iteration-level timing,
  full HITL H1-H6 blocks, AI-native gates, adversarial review tracking,
  DORA metrics, and cost fields
- **Bilingual contract:** English schema + project `content_language` for prose

### Structure

- `devflow/` — 18 folders covering the full SDLC
- `analysis/` — 10 subfolders for AI-assisted domain analysis (vision,
  business-context, business-risks, scope, personas, user-journeys,
  glossary, domain-model, process, open-questions)
- `functional/` — User Stories (US-NNN) + Bolts (US-NNN.BOLT-NNN)
- `spec/` — Implementation specifications (SPEC-YYMMDD-HHmm)
- `memory/` — Execution logs (MEM-YYMMDD-HHmm)
- `metrics/` — Bolt Manifest v3 JSON per Bolt
- `adrs/` — Architecture Decision Records
- `reviews/` — Formal internal audits (REV-NNN)
- `adversarial-reviews/` — 3-phase debate protocol (AREV-NNN)
- `bugs/` — Defect tracking with TDD-first policy (BUG-NNN)
- `risks/` — Project risk register (RISK-NNN)
- `incidents/` — Blameless post-mortems (INC-NNN)
- `retros/` — Weekly retrospectives with DORA tracking (RETRO-NNN)
- `discovery/` — External/legacy system analysis (DISC-NNN)
- `tests/` — UAT minutes (UAT-NNN) + manual test cases (TC-NNN)
- `input/` — Raw material (interviews, docs, source code, databases, UI/UX)

### Changes in this release

- **`analysis/business-risks/`** — Business risks extracted to own folder
  with `BR-NNN` naming, TEMPLATE-BR.md, README and INDEX
- **`analysis/relationships/`** — Removed `relationships.md` (content
  merged into README)
- **GUARDRAILS** — Added N19 (BR-NNN) to naming conventions table
- **Cross-references** — Updated all `business-risks.md` links across
  `analysis/README.md`, `business-context/README.md`, `risks/README.md`
- **Version infrastructure** — Added `VERSION` file, version to README,
  main methodology doc, GUARDRAILS, ONBOARDING, and `methodology_version`
  to manifest schema
- **Encoding fixes** — Cleaned corrupted Unicode characters in
  `relationships/README.md`

---

## [2026-06-08] — Bolt Manifest v3 (Accumulative)

**Motivation.** The v2 schema was extended with adversarial review fields,
full DORA slice per iteration, cost tracking, and H5/H6 HITL checkpoints.
The manifest title was bumped to v3 to reflect these non-backward-compatible
additions.

**Key changes from v2:**

- `adversarial_review` block per iteration (required/ran/arev_id/verdict).
- `dora` block per iteration (caused_failure, incident_id, mttr_minutes,
  code_origin).
- `cost` block per iteration (llm_usd, infra_usd, review_minutes_cost_usd,
  total_usd).
- `hitl.H5_uat` and `hitl.H6_adr` checkpoints added.
- `gates` expanded with AI-native gates (prompt_injection, secret_leak,
  hallucination_lint, ip_provenance, pii_dlp, dependency_confusion,
  test_first, behavioral_reproducibility, mutation).
- `traceability` at bolt level (prs, tests, incidents).

---

## [2026-05-26] — Hardening v2 after critical review (autonomy, risk, prompts, models)

Changes derived from the critical review of the methodology, maintaining the
premise of simplicity for onboarding (more tables, less prose, modular
artifacts).

### Main document `avenga-devflow/Avenga DevFlow.md`

- **§0 Quick Start** — 5 steps to get started + 6 non-negotiables (signed
  manifest, H1–H6 non-delegable, no override without ADR, diff review,
  versioned prompts, 1-day cap per Bolt).
- **Foundational Principle reformulated** — From "100% AI" to "draft
  intended-final; humans steer and may patch as a legitimate fallback".
- **V-Model** — Qualified as inspiration, not formal derivation.
- **"When Avenga DevFlow fits — and when it does not"** — Lists for
  strong-fit / use-with-care / do-not-adopt.
- **§3.0 HITL** — Review quality evidence mandatory
  (review_minutes, comments, findings, acknowledged_without_comment+reason,
  under_budget). Review budget table by risk_class × H1–H4.
  HITL Coverage per bolt_class (normal · hotfix with H3 retro-signed in 24h
  · infra/refactor/hardening with TL instead of PO).
- **§3.3 V-Bounce** — Test-first CI proxy. `spec_amendments[]` with formal
  process. Risk_class rubric (low/medium/high/critical) with AREV and min.
  approvers. Autonomy levels L1–L4 (Suggest / Bounded / Autonomous /
  Self-directed) with defaults per risk.
- **§3.6 AI-native gates** — Added: IP/license provenance scan, PII/DLP,
  dependency-confusion, test-first, behavioral reproducibility (replaces
  "determinism"). Mutation testing moved to Unit (not per Bolt). Override
  requires ADR with owner + expiry date.
- **§3.7 Metrics** — D2 decomposed (ai|review|wait|deploy time); D3 CFR
  sliced by model_version/autonomy_level; D4 MTTR sliced
  ai_generated vs human_authored; D1 paired with first-pass quality.
  Spec Drift redefined (agent_questions + spec_amendments). Manual
  Intervention Rate and Cost per Bolt promoted to mandatory.
  Approval-without-Comment Rate added. Override Rate with empirical
  bands per risk.
- **§3.11 H3 routing** — Table by `bolt_type` (feature→PO ·
  refactor→TL · infra→TL+SRE · hardening→TL+Sec · debt→TL).
- **§3.12 Bolt Manifest v2** — Extended schema: `bolt_type`, `bolt_class`,
  `risk_class`, `autonomy_level`, `data_classification`, `agent.{id, model}`,
  decomposed timing, `hitl.*` with review-quality per checkpoint,
  `manual_intervention`, `spec_amendments[]`, gates `{value, threshold, status}`
  with all new AI-native gates, `dora.slice` for D3/D4, `cost`
  (llm + infra + review_minutes_cost).
- **§3.13 (new) Agent & model change control** — Single agent definition
  per IDE in `agents/`. Material changes to the agent and model upgrades
  require a common ADR (`TEMPLATE-ADR.md`) with regression-eval.
- **§3.14 (new) Developer development plan** — Onboarding and training
  plan for the developer-under-AI role.
- **V-Bounce diagram (§4)** — Includes CI GATES node with fail→AI and
  pass→HR flows, feedback HR→RF→G and approve→AP.
- **§5 folder mapping** — Added `analysis/uat/`, `incidents/`, `retros/`.
- **References** — Added NIST AI RMF 100-1, EU AI Act 2024/1689,
  Schuett (2026) Adversarial Coding, GitHub Copilot Workspace, Anthropic
  "Building effective agents".

### New folders and templates

- `incidents/` — README + INDEX + `TEMPLATE-INCIDENT.md` (blameless
  post-mortems, feed D3/D4, cycle closure in Bolt manifest in `devflow/metrics/`).
- `retros/` — README + INDEX + `TEMPLATE-RETRO.md` (weekly cadence,
  mandatory opening with DORA Four + HITL Coverage).
- `analysis/uat/` — README + INDEX + `TEMPLATE-UAT.md` (H5 sign-off
  records per Unit/Milestone with stakeholder signatures).
  > **Note:** Later moved to `tests/uat/` in the 2026-05-21 release.

### `devflow/README.md`

- Folder tree and mapping table `folder → ID → template` updated
  with `incidents/`, `retros/`, `analysis/uat/`.

---

## [2026-05-25] — Rename to "Avenga DevFlow" + HITL/DORA hardening

- **Renamed the methodology** from "Avenga AI-Native-SDLC Dev Flow" to
  **"Avenga DevFlow"**. Folder `avenga-sdlc/` → `avenga-devflow/`. Main
  document `Avenga AI-Native-SDLC.md` → `Avenga DevFlow.md`.
- **Translated to English** all content in `avenga-devflow/` (README,
  INDEX and main document).
- **§3.0 HITL Charter** — Table of 6 non-skippable human checkpoints
  (H1 DoR · H2 V-Bounce · H3 Bolt acceptance · H4 Promotion · H5 UAT · H6 ADR)
  with named approver, timestamp and operational rules.
- **§3.6 AI-native quality gates** — Mandatory gates: prompt-injection,
  secret-leak, hallucination lint, mutation testing, determinism check,
  Bolt manifest validation.
- **§3.7 DORA-first metrics** — Restructured in 3 layers: (1) DORA Four
  (Deployment Frequency, Lead Time for Changes, Change Failure Rate, MTTR),
  (2) AI-native flow metrics, (3) HITL governance metrics
  (HITL Coverage 100% / Human Override Rate 10-30%).
- **§3.12 Bolt Manifest** — JSON schema v1 (Bolt manifest in `devflow/metrics/`) as the single
  source of truth for HITL + DORA mechanical evidence.
- **§5 folder mapping** corrected — `analysis/process/` (previously typo
  `proccess/`), removed `other-docs/`, added `vision/` and `business-context/`.
- **Renamed folder typo** `analysis/proccess/` → `analysis/process/`.
- **Templates with HITL signature blocks**:
  - `TEMPLATE-BOLT.md` → H1 DoR sign-off block.
  - `TEMPLATE-SPEC.md` → §7 H2 V-Bounce technical approval.
  - `TEMPLATE-MEM.md` → H3 Bolt Acceptance + H4 Promotion blocks.
  - `TEMPLATE-ADR.md` → H6 Ratification block.
- **New READMEs** for `analysis/business-context/`, `analysis/vision/`,
  `input/databases/`, `input/source-code/`.
- **New template** `analysis/process/TEMPLATE-PROCESS.md`.
- **Consolidated `other-docs/`** into `input/documentation/` (raw
  third-party docs live with the rest of the input material).
- **Housekeeping**: `README.md`, `ONBOARDING.md`, `analysis/README.md`,
  `analysis/process/README.md` and `input/interviews/README.md` updated
  to reflect the new naming and folder mapping.

---

## [2026-05-21] — `analysis/personas/` and `analysis/user-journeys/`; explicit boundary with `risks/`

**Motivation.** A US written by the AI is only useful if it has **who**
and **why**. Without concrete personas the stories remain as *"as a
user I want…"* (generic, invalid); without journeys the team cannot see the
end-to-end user experience across channels (BPMN only shows the
internal/operational side). Furthermore, a typical interview contains
**both** business risks (market, regulation, adoption) and execution
risks (technical, team, dependencies). Without a clear routing rule the AI
piles them in one place and they get lost.

**Changes.**

- **New folder `analysis/personas/`** (README + INDEX + TEMPLATE-PERSONA).
  One file per end-user archetype (`<PersonaName>.md`, PascalCase).
  3–5 personas is the sweet spot.
- **New folder `analysis/user-journeys/`** (README + INDEX +
  TEMPLATE-JOURNEY). One file per end-to-end journey with stages,
  touchpoints, emotions, moments of truth and metrics. Emotional diagram
  in Mermaid `journey`.
- **Risk boundary documented in 4 places** so the AI can auto-route
  findings from a single interview:
  - `analysis/README.md` — new section *"Risks: where they live"* and
    new table *"One interview → many artifacts"* with explicit row for
    business risks (→ `business-context/business-risks.md`) vs
    project risks (→ `../risks/RISK-NNN.md`).
  - `risks/README.md` — rewritten in English, with section *"Boundary with
    `analysis/business-context/business-risks.md`"* and routing rules
    for the agent.
  - `analysis/business-context/README.md` — boundary note in the
    *Business risks* row with link to the cross-cutting register.
  - `avenga-devflow/Avenga DevFlow.md` §5 — *Risks* row clarifies that
    business risks live inside `business-context/` and feed the register;
    fixed interviews path (`input/interviews/`, not
    `analysis/interviews/`); added rows for personas and journeys.
- **`devflow/README.md`** — folder tree, mapping table and Quick Start
  updated (fan-out from interviews to personas / journeys / domain-model /
  process / business-context / risks).

**Routing rule (summary for the AI).** When ingesting an interview:

| Finding                                         | Goes to |
|-------------------------------------------------|---------|
| Who uses the product (archetype)                | `analysis/personas/<Name>.md` |
| How they experience it end-to-end               | `analysis/user-journeys/<goal>.md` |
| Business risk (market, regulation, adoption)    | `analysis/business-context/business-risks.md` |
| Execution risk (technical, team, dependencies)  | `risks/RISK-NNN.md` |
| Both at the same time                           | Both places, cross-linked |

**Files created.**

- `analysis/personas/README.md`
- `analysis/personas/INDEX.md`
- `analysis/personas/TEMPLATE-PERSONA.md`
- `analysis/user-journeys/README.md`
- `analysis/user-journeys/INDEX.md`
- `analysis/user-journeys/TEMPLATE-JOURNEY.md`

**Files modified.**

- `analysis/README.md` (table, Mermaid, reading order, AI workflow,
  routing table, section *Risks: where they live*, relationships table).
- `risks/README.md` (rewritten in English with boundary section).
- `analysis/business-context/README.md` (note in *Business risks* row).
- `avenga-devflow/Avenga DevFlow.md` (§5 — 3 new rows + interviews
  correction + note in Risks).
- `devflow/README.md` (tree, mapping table, Quick Start).

---

## [2026-05-21] — `tests/` folder at root level; UAT moved out of `analysis/`

**Motivation.** UAT is a **human verification** artifact, not a business
analysis artifact. Keeping it inside `analysis/` mixed "understanding what
to build" with "validating what was built". Additionally, an explicit home
was needed for manual/exploratory test cases (automated tests continue to
live alongside the code, generated and executed by the agent in each
V-Bounce — §1, §2.1, §3.0).

**Changes.**

- **New root folder `tests/`** with `README.md` clarifying the boundary:
  *automated tests with the code; here only human-facing*.
- **`analysis/uat/` → `tests/uat/`** (README, INDEX, TEMPLATE-UAT). Internal
  paths updated (`../../analysis/vision/`, etc.).
- **New subfolder `tests/test-cases/`** with README + INDEX + `TEMPLATE-TC.md`
  for manual procedures (exploratory, walkthroughs, manual regression,
  pre-UAT).
- **Methodology (§3.11, §5):** references to `analysis/uat/` updated
  to `tests/uat/`; new row in §5 table for `tests/test-cases/`.
- **`devflow/README.md`:** folder tree and prefix table updated.
- **`analysis/README.md`:** removed `uat/` row; cross-reference note
  to `tests/uat/`; Mermaid diagram updated.

**Usage impact.**

- UAT records (UAT-NNN) are now created in `tests/uat/`.
- Bolt manifests in `devflow/metrics/` continue to reference UAT-NNN by id, not by
  path — no migration required.
- Any prior reference to `analysis/uat/` must be rewritten as
  `tests/uat/`.

---

## [2026-05-10] — Adversarial Debate Protocol (Adversarial Reviews)

- **New folder `adversarial-reviews/`** — Structured review protocol in 3 phases with different LLM models:
  - **Phase 1 — CRITIQUE (Challenger):** A model different from the implementer reviews the code in read-only mode and documents findings with severity.
  - **Phase 2 — DEFENSE (Defender):** The implementer model responds finding-by-finding (ACCEPT/REBUT/PARTIAL) with evidence.
  - **Phase 3 — VERDICT (Judge):** A third model arbitrates impartially, assigns final severity and issues verdict (PASS/CONDITIONAL PASS/FAIL).
- **Structure per AREV:** Each adversarial review creates a folder (`AREV-NNN-description/`) with up to 3 documents (01-CRITIQUE.md, 02-DEFENSE.md, 03-VERDICT.md).
- **Modular depth:** Complete (3 phases), Standard (Critique + Verdict), or Light (Critique only) depending on Bolt risk.
- **3 types of AREV:** Bolt-bound (linked to the V-Bounce), thematic (focus on security, architecture, performance, etc. with external sources like Context7/OWASP), or ad-hoc (exploratory on any part of the code).
- **Templates with "Spirit of the role"** — Detailed instructions so each LLM knows exactly how to act: attitude, mental checklist, pitfalls to avoid, evaluation criteria.
- **Finding routing** — Confirmed findings from the VERDICT are routed to the correct artifact (BUG/SPEC/DISC/ADR/RISK); discarded findings remain as audit trail.
- **Updated SDLC methodology** — Adversarial Review added as optional step in the V-Bounce anatomy (between AI generation and human review). New concept 2.14 in the glossary.
- **Updated main README** — `adversarial-reviews/` added to folder structure, prefix table, SDLC mapping and cheat sheet.

**Affected files:**
- `devflow/adversarial-reviews/README.md` (nuevo)
- `devflow/adversarial-reviews/INDEX.md` (nuevo)
- `devflow/adversarial-reviews/TEMPLATE-AREV.md` (nuevo)
- `devflow/adversarial-reviews/TEMPLATE-01-CRITIQUE.md` (nuevo)
- `devflow/adversarial-reviews/TEMPLATE-02-DEFENSE.md` (nuevo)
- `devflow/adversarial-reviews/TEMPLATE-03-VERDICT.md` (nuevo)
- `devflow/avenga-sdlc/Avenga AI-Native-SDLC.md`
- `devflow/README.md`
- `devflow/CHANGELOG.md`

> **Reference:** Inspired by [Adversarial Coding — Using Competing Models as Code Reviewers](https://www.subaud.io/adversarial-coding-competing-models-reviewers/) (Court Schuett, 2026), extended with Challenger → Defender → Judge pattern.

## [2026-05-06] — Documentation quality standards + LLM field + mandatory timestamp

- **Problem detected:** Different LLM models produce documents with widely varying levels of detail (Claude generates detailed and self-contained SPECs/MEMs; other models may generate telegraphic documents of few lines without sufficient context).
- **New quality standard in `spec/README.md`** — Section "Minimum quality standard (MANDATORY)" with minimum content rules, anti-patterns vs. correct approach table, and completeness metrics.
- **New quality standard in `memory/README.md`** — Same structure: rules, anti-patterns and completeness guiding questions.
- **Improved SPEC and MEM templates** — HTML comments `⚠️ MANDATORY` in key sections (Context, Phases, Executive Summary, Files, Decisions) explaining the minimum expected level of detail. SPEC checklist expanded with 3 new items.
- **`llm` field added to ALL templates** (12 files) — Traceability of which model generated each artifact. Affected templates: SPEC, MEM, ADR, DISC, US, BOLT, REV, RISK, BUG, INTERVIEW, ENTITY, GLOSSARY.
- **System timestamp rule** — Explicit instructions in READMEs, templates and agents: `YYMMDD-HHmm` MUST be obtained with `Get-Date -Format "yyMMdd-HHmm"` (PowerShell) or `date +"%y%m%d-%H%M"` (Bash). NEVER invent.
- **Agents updated** (`gh-copilot/AvengaDevFlow.agent.md` + `open-code/AvengaDevFlow.md`) — New sections: "Documentation Quality Standards (MANDATORY)", "Timestamp Rule (MANDATORY)", "LLM Field Rule (MANDATORY)" with comparative examples of telegraphic vs. explanatory style.

**Affected files:**
- `devflow/spec/README.md`
- `devflow/spec/TEMPLATE-SPEC.md`
- `devflow/memory/README.md`
- `devflow/memory/TEMPLATE-MEM.md`
- `devflow/adrs/TEMPLATE-ADR.md`
- `devflow/discovery/TEMPLATE-DISC.md`
- `devflow/functional/TEMPLATE-US.md`
- `devflow/functional/TEMPLATE-BOLT.md`
- `devflow/reviews/TEMPLATE-REV.md`
- `devflow/risks/TEMPLATE-RISK.md`
- `devflow/bugs/TEMPLATE-BUG.md`
- `devflow/analysis/interviews/TEMPLATE-INTERVIEW.md` *(later removed — interviews have no formal template; see `input/interviews/README.md`)*
- `devflow/analysis/domain-model/TEMPLATE-ENTITY.md`
- `devflow/analysis/glossary/TEMPLATE-GLOSSARY.md`
- `devflow/agents/gh-copilot/AvengaDevFlow.agent.md`
- `devflow/agents/open-code/AvengaDevFlow.md`

## [2026-05-02] — New subfolder `analysis/domain-model/`

- **Created `domain-model/` folder** inside `analysis/` — human-readable representation of the domain model:
  - `README.md` — purpose, structure, workflow and lifecycle
  - `TEMPLATE-ENTITY.md` — template with YAML frontmatter + property/relationship/rule/example tables
  - `INDEX.md` — domain entity index
  - `entities/` — one `.md` per entity (PascalCase)
  - `relationships.md` — centralised view of all relationships with Mermaid ER diagram
  - `enums.md` — catalogue of statuses, codes and reusable value sets
- **Updated `analysis/README.md`** — added `domain-model/` to structure, flow diagram and work steps
- **Flow:** `domain-model/` (editable, readable) → feeds → `functional/` (User Stories) and `adrs/` (modelling decisions)

## [2026-05-02] — New folder `analysis/` (Domain Analysis)

- **Created `analysis/` folder** with main README and initial subfolders:
  - `interviews/` — Stakeholder interview transcriptions (README + INDEX)
  - `bpmn/` — Business processes in BPMN/Mermaid notation (README + INDEX)
  - `glossary/` and `domain-model/` were added in later iterations
- **Updated `input/README.md`** — Transcriptions now go in `analysis/interviews/`, not in input/
- **Updated main README** — Added `analysis/` to folder structure, flow, diagram and SDLC mapping table
- **Updated flow diagram** — New ANALYSIS node between SDLC and DISC/FA

## [2026-05-02] — Naming synchronisation and template improvements

- **Renamed TEMPLATE-FA.md → TEMPLATE-US.md** — aligned with methodology (User Story)
- **Improved TEMPLATE-US** — free file organisation (no imposed backend/frontend subfolders), analyst's decision
- **Improved TEMPLATE-BOLT** — Verbose DoR and DoD with checklists, explanations and typical examples; reordered sections (Description → Acceptance criteria → Tasks → DoR → DoD)
- **Removed cryptic references** — DoR/DoD taken out of frontmatter and summary table, now standalone sections with detailed guidance

## [2026-05-02] — Branding and SDLC ↔ Dev Flow linkage

- **Renamed framework** from "devflow" to "Avenga AI-Native-SDLC Dev Flow" in main README and CHANGELOG
- **Added section 5** in `Avenga AI-Native-SDLC.md` — "Dev Flow: documentary implementation of the methodology" with mapping table and link to README
- **Added metrics section** in `TEMPLATE-MEM.md` (Lead Time, Bounces, Tests, % AI-generated)

## [2026-05-01] — Evolutionary improvements (low priority)

- **Created `risks/` folder** with README, INDEX and TEMPLATE-RISK for the project Risk Register
- **Created CHANGELOG.md** (this file) for framework meta-governance
- **Added DORA metrics section** in `memory/README.md`
- **Enriched `reviews/README.md`** with finding destination diagram
- **Added Quick Start** to the main README

## [2026-05-01] — Template improvements (post-analysis of real examples)

- **Created TEMPLATE-BOLT** in `functional/` — template for Bolts was missing
- **Improved TEMPLATE-SPEC** — scope ✅/❌, build baseline, phases per bolt, tech stack
- **Improved TEMPLATE-FA** — 1 US = 1 doc, bolts with layer, links to subfolders
- **Improved TEMPLATE-REV** — findings H-NNN with severity, legend, location/impact
- **Improved TEMPLATE-MEM** — executive summary, phases, post-implementation verifications
- **Improved TEMPLATE-DISC** — severity in gaps (🔴/🟡/🟢), tech stack
- **Improved TEMPLATE-ADR** — sources, supersede, alternatives in table
- **Improved TEMPLATE-BUG** — metadata table, severity emojis

## [2026-05-01] — Medium priority improvements

- **Translated Avenga SDLC to Spanish** — entire document rewritten
- **Updated Bolts** — timebox from 2h to 1 day (was 2-8h), measured in total cycle time
- **V-Bounce redefined** as AI agent cycle (not human)
- **Created 7 templates** (DISC, ADR, SPEC, REV, BUG, MEM, FA) with YAML frontmatter
- **Added NFRs section** in `adrs/README.md`
- **Integrated `other-docs/`** in the main flow diagram
- **Added bug flow diagram** in `bugs/README.md`

## [2026-05-01] — High priority improvements

- **Integrated `bugs/`** in the main flow diagram (third subgraph with TDD)
- **Resolved naming conflict** SPEC-FIX-BUG-NNN → unified to SPEC-YYMMDD-HHmm-fix-bug-NNN
- **Created mapping table** SDLC ↔ Dev Flow (20 rows) in main README
- **Populated INDEX.md** of `avenga-sdlc/` with the existing document
- **Cleaned up HTML artifacts** (`{=html}`, `<!-- -->`, `**\`) from SDLC

## [2026-05-01] — Initial analysis

- Complete analysis of the framework's 16 documents
- Identified 6 inconsistencies, 8 missing pieces, 15 improvement opportunities
- Classification by priority: 5 high, 5 medium, 5 low
