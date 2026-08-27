---
id: "REV-007"
title: "TestWriter as an out-of-the-box DevFlow Agent — adopter-partition readiness review"
date: "2026-08-26"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
status: "approved"        # draft | approved | closed — findings actionable, routing in progress
scope: "The TestWriter project (devflow/input/source-code/TestWriter — a Copilot agent + 5 skills for manual functional test design) evaluated against the v5.1 adopter partition (distribution-kit): the DevFlow Agent definition contract, the actors/roster activation model, the VERIFICATION.md projection mapping, the TC family (§2.6.1), the OQ protocol, and guardrails G06/G30/G31/G32/G33/G35"
methodology: "Static inspection of the TestWriter source (read-only, per G31) against the v5.1 adopter partition: definition-contract fit (agent.yaml + prompt.md vs agent + skills + references + assets), activation-model fit (the 100%-human fresh-install premise), artifact mapping of every pipeline input and output onto the canonical devflow/ families, guardrail compatibility, and per-platform projection feasibility per devflow/agents/VERIFICATION.md"
reviewed_artifacts:
  - "devflow/input/source-code/TestWriter/ (full tree: README.md, .github/agents/test-design.agent.md, .github/copilot-instructions.md, .github/prompts/design-tests.prompt.md, the 5 SKILL.md files, skills/testing-heuristics/references/ (7 files), skills/test-case-consolidation/assets/testcases-template.csv, context/ (4 files), sample outputs for HU 8547/23638/138124)"
  - "distribution-kit/devflow/agents/ (README.md — the definition contract, examples/README.md, examples/qa/agent.yaml + prompt.md, TEMPLATE-new-role/, VERIFICATION.md — the canonical→wrapper mapping and parity rules)"
  - "distribution-kit/devflow/actors/ (roster.yaml — ships empty, TEMPLATE-ACTOR.yaml, README rules)"
  - "distribution-kit/devflow/tests/test-cases/TEMPLATE-TC.md (the TC contract: source_bolt, covered_acs, manifest, AITL-TC-Approval)"
  - "distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md (§2.6.1 TC cardinality/test-basis/timing, §3.0.1 actor configuration, §5.12 working data)"
  - "distribution-kit/devflow/GUARDRAILS.md (G06, G30, G31, G32, G33, G35) and distribution-kit/devflow/analysis/ (family inventory: glossary, personas, domain-model, business-context, open-questions)"
adrs_checked:
  - "devflow/adrs/ADR-007-devflow-agent-identity-model.md"
  - "devflow/adrs/ADR-010-actor-grammar-and-pure-v5-vocabulary.md"
  - "devflow/adrs/ADR-012-english-all-methodology-artifacts-convention.md"
  - "devflow/adrs/ADR-013-agent-lifecycle-governance.md"
  - "devflow/adrs/ADR-014-actors-roster-is-the-enablement.md"
specs_checked: []
review_ready_at: "2026-08-26T17:52:15-03:00"
review: # AITL-REV-Approval — decision dictated in conversation ("dale ajusta eso y queda APROBADO!") and transcribed by the agent (§3.0)
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "architect"
      model: null
  started_at: "2026-08-26T17:52:15-03:00"
  decided_at: "2026-08-26T17:52:15-03:00"
  findings: []
  acknowledged_without_comment: true # must be true when findings is empty (§3.0)
  acknowledgment_reason: "Approved as Architect/TL after an iterative pre-approval review conducted in conversation: the maintainer steered three refinement passes recorded in History — measured evidence and ADR design questions (F-03), precise routing (US-023.BOLT-006 via G15 · new US-026), the tool-agnosticism scoping decision (F-06: the ADO retrieval does not ship, the input surface is the canonical functional/user-stories/ family, MCP wiring is adopter configuration), and the maintainer-partition clarification on the ADR route (adopters ship no ADRs; the normative contract text is baked into the kit's framework files by US-023.BOLT-006). The §6 action plan is actionable as routed; downstream artifacts follow their own lifecycles — this approval approves none of them (T10)."
tags: ["devflow-agents", "testwriter", "qa", "test-design", "skills", "v5.1", "adopter-partition", "out-of-the-box"]
---

<!--
  LANGUAGE POLICY (ADR-012): prose in English — every methodology artifact
  of this repository is written in English. TestWriter's own content is
  Spanish; quotes from it are translated where needed.

  ⚠️ AITL-REV-Approval (§2.14, §3.0): findings remain DRAFT until a
  qualified human records AITL-REV-Approval. Approval does NOT approve any
  downstream artifact. Code-related outcomes still require an approved Bolt
  (T10 — never REV → SPEC directly).

  TestWriter is read from devflow/input/ (human-deposited raw evidence,
  read-only for agents per G31). This review reads it as the evidence under
  evaluation; nothing was written there.
-->

# REV-007 — TestWriter as an out-of-the-box DevFlow Agent: adopter-partition readiness

| Field           | Value |
|-----------------|-------|
| **Scope**       | TestWriter (Copilot agent + 5 skills for manual functional test design, deposited in `devflow/input/source-code/TestWriter/`) against the v5.1 adopter partition (`distribution-kit/`) |
| **Methodology** | Static inspection: definition-contract fit, activation-model fit, per-artifact input/output mapping, guardrail compatibility, platform-projection feasibility |
| **Criteria**    | ADR-007/010 (identity/grammar), ADR-013 (agent lifecycle), ADR-014 (roster enablement), ADR-012 (language), §2.6.1 (TC family), §3.0.1 (actor configuration), G06/G30/G31/G32/G33/G35, `devflow/agents/VERIFICATION.md` |

---

## 1. Purpose

TestWriter is a working QA agent: a single orchestrating agent definition
(`test-design.agent.md`) that drives a five-stage pipeline of skills —
Azure DevOps retrieval → user-story analysis (with a critical-questions
gate) → deterministic testing heuristics → exploratory scenario generation
→ consolidation into a traceable, Azure-DevOps-importable CSV of manual
functional test cases. It was built outside DevFlow, for GitHub Copilot,
in Spanish, for a specific banking client.

The maintainer wants to know whether the **current v5.1 adopter partition
can host TestWriter as an out-of-the-box DevFlow Agent** — shipped with the
kit, dormant on a fresh install (the team is 100% human by default), and
activated only by an explicit act — or whether the methodology needs new
pieces first. This review answers that question: what maps cleanly, what
needs adaptation, and what does not exist yet in the methodology.

---

## 2. Artifacts reviewed

| Artifact | Files | Notes |
|----------|-------|-------|
| TestWriter agent + global rules | `test-design.agent.md`, `copilot-instructions.md`, `design-tests.prompt.md` | Orchestrator: pipeline order, gates, no-invention rule, persistence rules |
| TestWriter skills | 5 × `SKILL.md` + 7 heuristic reference files + 1 CSV asset | The productive logic lives here, with progressive disclosure (references loaded on demand) |
| TestWriter context bundle | `context/business-rules.md`, `glossary.md`, `roles-permissions.md`, `test-design-config.md` | Project-specific knowledge the pipeline reads before designing |
| TestWriter sample outputs | `output/8547/`, `output/23638/`, `output/138124/` | 01-analysis → 02-heuristic → 03-exploratory → 04-coverage-gaps + final CSV |
| Kit agent system | `agents/README.md`, `examples/`, `TEMPLATE-new-role/`, `VERIFICATION.md`, `actors/` | The definition contract, the activation model, the projection mapping |
| Kit TC family + methodology | `TEMPLATE-TC.md`, `Avenga-DevFlow.md` §2.6.1/§3.0.1/§5.12, `GUARDRAILS.md` | The governed shape TestWriter's output must land in |

---

## 3. Severity legend

| Category | Meaning |
|----------|---------|
| **Compliant** | Already supported by the adopter partition as shipped — porting work only |
| **Documented deviation** | Justified difference, recorded |
| **Minor gap** | Adaptation needed, but inside existing methodology structures |
| **Major gap** | Something the methodology does not have — a new piece or an explicit decision is required |

---

## 4. Findings

### 4.1 — Activation and governance (the 100%-human premise)

#### F-01 [Compliant] — The opt-in activation model already exists; the premise needs zero new machinery

**Location:** `distribution-kit/devflow/actors/roster.yaml` (ships `actors: []`), `agents/examples/README.md`, `agents/squad/` (ships empty), `agents/README.md` ("Create your own agent")

**Actual:** The kit's fresh-install state is exactly the maintainer's
premise: the roster ships empty (100% human, safe default — no AI-signed
approval possible), `examples/` are read-only references never installed
and never referenced by the roster, and `squad/` ships empty. Activating
any agent is already a defined, explicit act: copy the example into
`squad/`, create the actor file from `TEMPLATE-ACTOR.yaml`, list it in
`roster.yaml`, have the Coordinator install the wrapper. For an
executor-only agent this is **living data** (no Bolt, no approval — ADR-013);
granting approver authority is a separate human-only roster act (ADR-014).

**Impact:** None — positive finding. Shipping TestWriter as a sixth
example under `agents/examples/` (e.g. `test-designer/`) inherits the
dormant-by-default + explicit-activation behavior with no new mechanism.
"Examples are references, never a closed enum" is already the written rule.

**Recommendation:** Ship TestWriter as `agents/examples/test-designer/`.
Do not invent a separate activation switch — the roster IS the switch.

---

#### F-02 [Compliant] — TestWriter maps to an executor-only agent; approval authority is never involved

**Location:** `test-design.agent.md` (the agent produces test-case drafts and stops at gates for QA), `TEMPLATE-ACTOR.yaml` (`modes: [executor]`, `approves: []`)

**Actual:** TestWriter produces TC **drafts** and explicitly defers every
decision (critical questions, missing Area Path, schema changes) to the
human QA. In DevFlow terms it is a pure executor: `modes: [executor]`,
`approves: []`. The human QA records `AITL-TC-Approval` on each produced
TC exactly as §2.6.1 already prescribes. The agent never signs anything,
so activating it never weakens the safe default.

**Impact:** None — positive finding. The identity model (ADR-007) and the
actor grammar (ADR-010) absorb the agent as-is: TC manifests record
`created_by: agent:<id>` in `generation`, approvals record `human:<user>`.

**Recommendation:** Charter the example with `modes: [executor]`,
`approves: []`, and note that the QA example agent and a test-designer can
coexist in a roster (the N-actors : 1-definition reuse is already allowed).

---

### 4.2 — The definition contract

#### F-03 [Major gap] — Skills have no home in the canonical DevFlow Agent definition contract

**Location:** `distribution-kit/devflow/agents/README.md` ("one canonical file pair: `agent.yaml` + `prompt.md`"), `VERIFICATION.md` (canonical→wrapper mapping table — no skills row)

**Actual:** The canonical definition contract is exactly two files. All of
TestWriter's productive value lives outside that shape: 5 skills with
`SKILL.md` descriptions, 7 progressive-disclosure reference files
(heuristics loaded only when needed), 1 CSV template asset, and 1 reusable
shortcut prompt. The wrapper mapping projects `id`, `description`,
`model`, `tools`, `mcp_servers` and the charter body — nothing else. There
is no canonical field, no folder convention, no per-platform projection
row and no parity-check coverage for per-agent skills.

**Expected:** A definition contract able to carry a skills bundle, so that
a multi-skill agent ships, copies to `squad/`, installs and stays in
parity like any other definition.

**Impact:** Without this, the only port is inlining everything into
`prompt.md`. Measured on the deposited source: skills + references + asset
= 22,952 chars; agent definition + global instructions + shortcut prompt =
9,597 chars — **~32.5k characters today**, already over the documented
GitHub Copilot cloud-agent 30k prompt cap (VERIFICATION.md) before
translation, generalization and TC-mapping guidance grow it further. An
inlined charter also (a) destroys the progressive-disclosure economy
(every heuristic reference always in context), and (b) makes "add a new
heuristic = drop a file in `references/`" — one of TestWriter's best
design properties — impossible.
This is the single structural blocker for shipping TestWriter (or any
future multi-skill DevAgent) out of the box.

**Recommendation:** Extend the canonical contract with an **optional
`skills/` area inside the definition folder**
(`agents/<examples|squad>/<id>/skills/<skill-name>/SKILL.md` +
`references/` + `assets/`), declared in `agent.yaml` (e.g. a `skills:`
list), with a new VERIFICATION.md mapping row per platform (Copilot
`.github/skills/`, Claude Code `.claude/skills/`, OpenCode/Codex per their
skill surfaces — re-verify each at implementation time) and parity-check
coverage for the projected skill files. This is an ADR-class contract
change plus kit Bolts. Two design questions the ADR must answer
explicitly, not discover late: (1) **the projection fallback on a platform
with no native skills surface** — inline into the wrapper with a size-cap
warning, or install the wrapper degraded with an explicit notice that the
skills were not projected (silent lobotomy is the failure mode to
exclude); (2) **the `skills:` declaration enters the contract's validated
schema** with the same strict discipline the manifest family uses
(`additionalProperties: false` — an undeclared skill folder is a parity
failure, not a tolerated extra).

---

#### F-04 [Minor gap] — The examples layout, the install act and the copy rule assume the file pair

**Location:** `agents/examples/README.md` ("each an `agent.yaml` + `prompt.md`"), `agents/README.md` steps 1–4 (copy, fill, write prompt, install), `VERIFICATION.md` ("the charter body becomes the wrapper body")

**Actual:** Every rule that moves a definition around — copy example →
`squad/`, Coordinator installs, N×4 parity, "never hand-edit a generated
wrapper" — is written in terms of the two-file pair. A multi-file example
(skills, references, assets) is not contradicted anywhere, but it is not
covered either: nothing says the whole definition **folder** is the unit
of copy/install/parity. The reusable shortcut prompt
(`design-tests.prompt.md`) has a canonical home already
(`devflow/prompts/PROMPT-NNN-*`), but the projection of a prompt into a
platform surface (`.github/prompts/`) is likewise unmapped.

**Expected:** The definition **folder** (pair + optional skills bundle) is
the atomic unit of copy, install, delete and parity.

**Impact:** Ambiguity at install time: a Coordinator following today's
text would project the wrapper and silently leave the skills behind,
shipping a lobotomized agent that references skills that were never
installed.

**Recommendation:** Same ADR/Bolt as F-03: rewrite the copy/install/delete
rules folder-atomically; state that `devflow/prompts/` is the canonical
home of shortcut prompts and that platform prompt surfaces are optional
projections. One consequential detail to carry as an explicit AC of the
port Bolt (not a separate finding): both `agents/README.md` and
`agents/examples/README.md` hard-code "the five example role definitions"
— the wording must change when the sixth example ships, or the kit
contradicts its own inventory.

---

### 4.3 — Input side: where the pipeline reads from

#### F-05 [Compliant] — The user-story-analysis skill is the OQ protocol, already

**Location:** `skills/user-story-analysis/SKILL.md` (explicit / inferred / missing / assumption / open-question; critical questions stop the pipeline), kit `analysis/open-questions/` + G35

**Actual:** The skill's five-way classification and its blocking gate map
one-to-one onto existing methodology: open questions → `OQ-NNN` documents;
"critical questions stop the pipeline before heuristics" → the OQ sunset
rule (G35: an open OQ targeting the US blocks
`AITL-BOLT-READY-Approval` as part of the DoR). TestWriter independently
converged on DevFlow's own gate — the port replaces its ad-hoc
`01-analysis.md` question list with governed `OQ-NNN` artifacts and gains
enforcement instead of losing anything.

**Impact:** None — positive finding, and the strongest integration point:
the ported skill should **create OQs**, not markdown bullet lists.

**Recommendation:** In the ported skill, route critical questions to
`analysis/open-questions/OQ-NNN` (status `open`, `targets: [US-NNN]`) and
let G35 do the blocking. Non-critical questions may stay in the analysis
working notes.

---

#### F-06 [Minor gap] — The retrieval stage does not ship: external-tool integration is adopter configuration; the input surface is the canonical US family

**Location:** `skills/azure-devops-retrieval/SKILL.md` (materializes a work item into `input/<id>.md`), kit G31 (agents never write `devflow/input/`), §2.6.1 + G06 (the test basis is an **approved** US), G33 (a US without a manifest does not exist)

**Actual:** TestWriter's first pipeline stage writes a fetched Azure
DevOps work item to a local `input/` file that the rest of the pipeline
treats as the source of truth. Ported naively, the landing place would be
`devflow/input/` — which G31 forbids agents to write. And even if it
landed elsewhere, a raw ADO work item is not a governed test basis: G06
and §2.6.1 require the approved US/ACs. Shipping this stage would also
couple the kit to one specific external tool, against the methodology's
tool- and model-agnosticism.

**Expected:** The shipped example carries **no external-tool coupling**
— **maintainer decision recorded at this review**: the methodology stays
tool-agnostic, so the kit ships nothing Azure-specific. The ported agent's
input surface is the **canonical US family the methodology already
defines**: approved `US-NNN` documents in `devflow/functional/user-stories/`
(with their ACs and manifests). The `azure-devops-retrieval` skill is
dropped from the port.

**Impact:** Low, and clarifying: the pipeline loses one optional
convenience stage and gains a single governed entry point. Teams whose
backlog lives in ADO/Jira wire their own retrieval as **adopter
configuration** — the existing contract already allows it
(`capabilities.mcp_servers`, named + allowlisted, per adopter) without the
kit shipping any of it.

**Recommendation:** In the ported charter, "WHAT I READ" starts at
approved `US-NNN` in `functional/user-stories/`; the shipped definition
declares `mcp_servers: []`. One guidance sentence in the example's charter
protects adopters who build their own import: any externally-fetched
backlog item must land as a **draft US through the normal
`AITL-US-Approval` lifecycle** (G31 and G06 bind adopter-built variants
too — such a variant would also need `write_paths` covering
`functional/user-stories/` + `metrics/user-stories/`). No methodology
change, no ADR.

---

#### F-07 [Minor gap] — The context bundle maps onto several analysis families; the charter must name them or adopters will recreate `context/`

**Location:** `context/business-rules.md`, `glossary.md`, `roles-permissions.md`, `test-design-config.md`; kit `analysis/` family inventory

**Actual:** TestWriter reads a four-file `context/` folder before
designing. In DevFlow those contents split across existing families:
glossary → `analysis/glossary/`; roles and permissions →
`analysis/personas/` (+ `domain-model/` for permission entities); stable
business rules → `analysis/domain-model/` and `analysis/business-context/`
plus the approved USs themselves (note: there is **no** dedicated
business-rules family — `BR-NNN` is business **risks**); the
test-design configuration (title conventions, Area Path fallback,
banca/plataforma declarations) → the project section of `AGENTS.md`
and/or the adopting project's analysis docs. Nothing is missing in the
methodology, but nothing tells the ported agent where to read.

**Expected:** The shipped charter names its governed read surface
explicitly, family by family.

**Impact:** Without the explicit mapping, an adopter (or the agent itself)
will recreate a parallel `devflow/context/` folder — a G30 violation — or
the agent will silently design tests without the project knowledge the
original pipeline depends on.

**Recommendation:** Write the read-surface mapping into the example's
charter ("WHAT I READ": approved US + `analysis/glossary/` +
`analysis/personas/` + `analysis/domain-model/` + project section of
`AGENTS.md`). No methodology change needed.

---

### 4.4 — Output side: what the pipeline produces

#### F-08 [Compliant] — Total test-basis alignment: TestWriter's core rule is G06 verbatim

**Location:** `copilot-instructions.md` ("Never invent business rules, roles, states or data… generate an open question instead of assuming"), kit §2.6.1 test-basis rule + G06

**Actual:** TestWriter's non-negotiable rule — expected results come only
from the HU, its ACs and declared context; gaps become questions, never
assumptions — is the §2.6.1 test-basis rule and G06 stated independently.
Likewise its traceability model ports without translation: `Coverage Tag`
≡ `covered_acs`, `Source HU ID` ≡ `source_us`, `Origin:
Heuristic|Exploratory` + `Technique/Heuristic` ≡ TC content/tags, and the
heuristic-before-exploratory discipline is a quality property DevFlow has
no rule against and every reason to welcome.

**Impact:** None — positive finding. The agent's philosophy needs zero
re-education; only its output format moves (F-11).

**Recommendation:** Preserve the origin/technique labeling in the ported
TC template usage (tags or a per-TC note) — it is measurement gold for
the coverage conversation at `AITL-TC-Approval`.

---

#### F-09 [Major gap — adaptation decision] — Pipeline cadence: TestWriter designs per HU; §2.6.1 binds every TC to one approved Bolt

**Location:** kit `Avenga-DevFlow.md` §2.6.1 ("Every TC references exactly one approved `source_bolt`… Test Cases are drafted after `AITL-BOLT-READY-Approval` and approved before the implementation SPEC is generated"), `TEMPLATE-TC.md` (`source_bolt` mandatory)

**Actual:** TestWriter runs once per HU, as soon as the HU text exists,
and produces the whole coverage set (tens of cases across all ACs).
DevFlow's TC family is Bolt-anchored: a TC is drafted **after** its
product Bolt is approved and **before** that Bolt's SPEC — the
verification contract exists per delivered outcome, not per backlog item.
A direct port that emits Bolt-less TCs fails the template's mandatory
`source_bolt` and violates the timing §2.6.1 prescribes.

**Expected:** The ported pipeline runs inside the window the methodology
already reserves for exactly this work: after `AITL-BOLT-READY-Approval`,
before `AITL-SPEC-Approval`, scoped to that Bolt's ACs.

**Impact:** Decision required — but note the fit is better than it first
looks: §2.6.1's "TCs drafted after BOLT-READY, approved before the SPEC"
window is currently a step with no dedicated tooling; TestWriter **is**
that tooling. What is genuinely lost in the per-Bolt cadence is the
US-level coverage view (`04-coverage-gaps.md` across the whole HU).

**Recommendation:** (i) Bind the pipeline to the Bolt cadence in the
charter (run per approved Bolt, over that Bolt's `covered_acs` slice) —
no methodology change; (ii) route AC-level gaps to `OQ-NNN` (governed)
and keep the residual per-US coverage summary as working data (F-11);
(iii) explicitly reject creating a new US-level "test design dossier"
artifact family — it would duplicate governance the OQ + TC families
already provide.

---

#### F-10 [Minor gap] — Volume ceremony: one manifest + one approval per TC meets a 10–40-case consolidation

**Location:** kit G33 (a TC without its manifest does not exist), `TEMPLATE-TC.md` §11, §2.6.1 ("A TC may contain one coherent scenario with its variants or data sets")

**Actual:** TestWriter's consolidation emits one CSV row-group per
scenario — its sample outputs hold 10–40 cases per HU. Mapped 1:1, that is
10–40 TC documents + manifests + `AITL-TC-Approval` decisions per US:
governance-correct but heavy. §2.6.1 already provides the pressure valve —
a TC may bundle one coherent scenario **with its variants and data sets**,
splitting only when independent outcomes would make pass/fail ambiguous.

**Expected:** The consolidation skill targets variant-rich TCs (one per
coherent scenario family), not one TC per CSV title.

**Impact:** Without this guidance the shipped agent floods the review
queue and the first adopter impression is "DevFlow made my QA slower" —
an adoption killer for exactly the audience this agent targets.

**Recommendation:** Encode the bundling rule in the ported consolidation
skill (equivalence-class variants and data-set rows collapse into their
parent TC's "Alternative / negative paths" and data tables). TC review
budgets remain project-defined; no methodology change.

---

#### F-11 [Minor gap] — The canonical artifact is the TC document; the CSV and the intermediate files become projections and working data

**Location:** `skills/test-case-consolidation/SKILL.md` (CSV as the deliverable), `copilot-instructions.md` (persist 01–04 in `output/<id>/`), kit §5.12 + G32 (agents-data: working area, never citable), `reports/` (derivative by location)

**Actual:** In TestWriter the CSV **is** the deliverable and the four
intermediate files are the audit trail. In DevFlow the deliverable must be
`TC-NNN` documents + manifests (the governed contract), which inverts the
consolidation skill's target. The intermediate artifacts (01-analysis,
02-heuristic, 03-exploratory, 04-coverage-gaps) have a sanctioned home —
`devflow/agents-data/<agent-id>/` — and G32's "never citable as governed
source" is not a loss but the correct semantics: the TC's governed sources
are the US/ACs/Bolt, never the pipeline's own scratch reasoning. The ADO
CSV survives as an optional export **projection** generated from approved
TCs (derivative by location: `reports/`, or agents-data).

**Expected:** Consolidation emits TC documents first; CSV second, clearly
derivative; intermediates under `agents-data/<agent-id>/<us|bolt>/`.

**Impact:** Low — re-targeting work in one skill, plus charter text. The
auditability property TestWriter insists on ("persist artifacts as files,
not chat") is fully preserved, just relocated.

**Recommendation:** Re-target the consolidation skill: primary output =
draft `TC-NNN` documents + manifests; optional CSV projection for import
into the adopter's test-management tool (columns are adopter
configuration, per F-12 — the kit ships no tool-specific schema),
generated only from **approved** TCs (so the exported expected results
are governed, not draft).

---

### 4.5 — Shipping shape

#### F-12 [Minor gap] — Language and client-specific conventions must leave the framework files

**Location:** All TestWriter files (Spanish, voseo); `copilot-instructions.md` + `test-design-config.md` (BE/BI, MB/WB, fixed `HOME` module, `BComplejidad`/`BPrioridadTC`, Area Path); ADR-012 (kit framework files are English)

**Actual:** TestWriter is written in Spanish and hard-codes one client's
conventions: banking segment (BE/BI), platform (MB/WB), a fixed `HOME`
module in every title, proprietary CSV columns, ADO Area Path semantics.
A kit example is a framework file: English (ADR-012), project-neutral.
The 7 heuristic reference files are domain-neutral and port nearly
verbatim (translated); the title-convention and CSV-column specifics are
adopter configuration, not framework.

**Expected:** The shipped example is English and generic; the banking
conventions become the adopting project's context (F-07's read surface),
loaded from analysis docs / `AGENTS.md` project section at run time.

**Impact:** Low but mandatory — shipping client-specific vocabulary in the
kit would leak one adopter's conventions into every install.

**Recommendation:** Generalize during the port: parameterize the title
convention and export columns as project config the charter reads; keep
the heuristics catalog (the durable value) intact.

---

#### F-13 [Compliant] — Orchestration, escalation and MCP needs all fit the existing topology

**Location:** `test-design.agent.md` (single orchestrator, skills are not agents; stop-and-ask gates), kit `VERIFICATION.md` (spawn topology; Copilot `mcp-servers` not honored in IDEs), `agent.yaml` contract (`capabilities.mcp_servers` named + allowlisted, tiers)

**Actual:** TestWriter's pipeline is intra-agent skill sequencing — no
agent spawns another, so the spawn topology is untouched: the role wrapper
carries no `Agent`/`task` tool and needs none. Its stop-and-ask gates
(critical questions, missing Area Path, schema-change confirmation) map
directly to the definition's `escalation:` triggers. Its one external
dependency (`ado-remote-mcp`) fits the contract as a named, allowlisted
MCP at T1 (read-only external), and the skill's own written fallback
("if the MCP is unavailable, ask the QA to paste the HU — never fail the
pipeline") already handles the platforms where MCP is not honored
(Copilot IDEs, per VERIFICATION.md).

**Impact:** None — positive finding. One caution to encode: skills must
never be modeled as separate sub-agents "to be more DevFlow" — that would
put executor spawning where the topology forbids it.

**Recommendation:** Charter the pipeline as internal skill sequence. The
shipped example declares `mcp_servers: []` (per the F-06 decision: no
external-tool coupling ships); the contract's allowlist capacity remains
available to adopters who wire their own integrations as their own
configuration.

---

## 5. Summary

The adopter partition is **structurally ready for the premise and for
most of the agent**: the dormant-by-default, explicitly-activated,
100%-human-out-of-the-box model already exists (roster ships empty,
examples are read-only, executor activation is living data) and TestWriter
slots in as a pure executor whose philosophy (no invention, approved
intent as the only oracle, questions instead of assumptions) is G06 and
the OQ protocol stated independently.

**One thing** does not exist yet and is genuinely new methodology work:
**skills as part of the DevFlow Agent definition contract** — the
file-pair contract cannot carry TestWriter's 5-skill, 7-reference,
1-asset architecture, and inlining it breaks the Copilot 30k cap and the
progressive-disclosure economy (F-03/F-04). The Azure DevOps retrieval
stage is **out of scope by maintainer decision** (F-06): the methodology
stays tool-agnostic, the shipped agent reads approved `US-NNN` from the
canonical `functional/user-stories/` family, and external-tool
integrations remain adopter configuration. One adaptation is required but
needs no new methodology: binding the pipeline to the per-Bolt TC cadence
§2.6.1 already prescribes (F-09). The rest is porting work: read-surface
mapping, TC-first output with the CSV as projection, variant bundling,
generalization and translation (F-07, F-10, F-11, F-12).

---

## 6. Action plan

> Applies only after `AITL-REV-Approval`. Each destination follows its own
> lifecycle and AITL approval (code → approved Bolt first, T10).

| # | Finding | Severity | Action | Routes to |
|---|---------|----------|--------|-----------|
| 1 | F-03, F-04 | Major + Minor | Extend the canonical definition contract with an optional per-definition `skills/` bundle: `agent.yaml` declaration (schema-validated), folder-atomic copy/install/delete/parity rules, per-platform projection rows in VERIFICATION.md, projection-fallback policy | ADR — **maintainer-partition decision record**: adopters ship no ADRs, so the ADR governs this repo's change only (the ADR-013/014 pattern) — + G15 re-revision of **US-023** (the US-023.BOLT-005 precedent) → new **US-023.BOLT-006**, which **bakes the normative contract text into the kit's framework files** (`agents/README.md`, `examples/README.md`, the agent.yaml schema, `VERIFICATION.md`, the Coordinator platform preambles) — the adopter receives the rule there, never as an ADR |
| 2 | F-06 | Minor (decided) | Maintainer decision recorded at this review: no external-tool coupling ships (tool-agnosticism). Drop the retrieval stage; the input surface is approved US-NNN in `functional/user-stories/`; shipped `mcp_servers: []`; one charter sentence binds adopter-built imports to the draft-US → AITL-US-Approval route (G31/G06) | **US-026** charter Bolt (no ADR, no methodology change) |
| 3 | F-09 | Major (adaptation) | Bind the ported pipeline to the per-Bolt TC cadence (§2.6.1 window: after BOLT-READY, before SPEC); AC gaps → OQ-NNN; reject a new US-level artifact family | New feature US — **US-026** (test-designer example agent; next free number, `functional/INDEX.md`) → charter Bolt |
| 4 | F-07, F-10, F-11, F-12 | Minor | Port work: charter read-surface mapping, variant-rich TC bundling, TC-first output + CSV projection from approved TCs, generalization + English translation, "five examples" wording update in both READMEs (F-04 AC) | Same **US-026** → port Bolts |
| 5 | F-01, F-02, F-05, F-08, F-13 | Compliant | No action — recorded as evidence that the activation model, actor identity, OQ protocol, test-basis rule and spawn topology absorb the agent as designed | — |

---

## 7. Conclusions

**Yes, with one addition.** The current adopter partition supports the
governance side of TestWriter-as-a-DevAgent completely — activation,
identity, approvals, test basis, open questions — and the premise
("fresh install is 100% human; using it is an explicit act") is already
the kit's shipped behavior, not something to build. What blocks shipping
it out of the box today is exactly one structural gap: the definition
contract cannot carry skills (F-03/F-04 — and it will block every future
multi-skill DevAgent, not just this one). The ADO-retrieval convenience
is resolved by maintainer decision, not by new methodology: it does not
ship (tool-agnosticism), the agent reads the canonical US family, and
external integrations stay adopter configuration (F-06). Recommended
order: route #1 (skills contract ADR + US-023.BOLT-006) first — it is
the reusable enabler; the port itself (#2–#4, US-026) becomes a normal
feature US once #1 lands.

---

## 8. AITL-REV-Approval

> **Avenga DevFlow §2.14, §3.0.** This Review remains a draft until a
> qualified human records `AITL-REV-Approval` (in the `review` frontmatter
> block). Approval makes the findings actionable; it does not approve any
> downstream artifact. The V-Bounce checkpoint is `AITL-MEM-Approval`
> (recorded in the Bolt manifest's `checkpoint_approvals[]`) — a REV and a
> V-Bounce approval are different events.

| Field | Value |
|-------|-------|
| **Reviewer** | eugenio.serrano (Architect/TL) |
| **Decision** | approved |
| **review_ready_at** | `2026-08-26T17:52:15-03:00` |
| **review.started_at** | `2026-08-26T17:52:15-03:00` |
| **review.decided_at** | `2026-08-26T17:52:15-03:00` |
| **Findings** | acknowledged_without_comment — the reviewer steered three pre-approval refinement passes in conversation (see History and the frontmatter acknowledgment_reason); the §6 action plan is actionable as routed |

---

## 9. History

| Date | Change | Author |
|------|--------|--------|
| 2026-08-26 | Initial review (draft) — TestWriter → out-of-the-box DevAgent readiness, 13 findings (3 Major · 5 Minor · 5 Compliant) | @eugenio.serrano |
| 2026-08-26 | Draft refined pre-approval: measured char counts replace the estimate in F-03 (+ two ADR design questions: projection fallback, schema-validated `skills:`), "five examples" wording carried as F-04 AC, `write_paths` note for the retrieval variant in F-06, precise routing in §6 (US-023.BOLT-006 via G15 re-revision · new US-026) | @eugenio.serrano |
| 2026-08-26 | Maintainer scoping decision recorded pre-approval (tool-agnosticism): the ADO retrieval stage does not ship — F-06 reframed Major→Minor (decided); the agent's input surface is the canonical `functional/user-stories/` family; external integrations remain adopter configuration. §5/§6/§7 and F-13 aligned; counts now 2 Major · 6 Minor · 5 Compliant | @eugenio.serrano |
| 2026-08-26 | §6 route 1 clarified: the ADR is a maintainer-partition decision record (adopters ship no ADRs — the ADR-013/014 pattern); US-023.BOLT-006 bakes the normative contract text into the kit's framework files | @eugenio.serrano |
| 2026-08-26 | AITL-REV-Approval recorded (approved — decision dictated in conversation, transcribed by the agent) | @eugenio.serrano |
