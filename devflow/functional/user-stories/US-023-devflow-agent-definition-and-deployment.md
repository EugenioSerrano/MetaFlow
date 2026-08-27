---
id: "US-023"
title: "DevFlow Agents — canonical definition contract, the shipped Coordinator, role charter templates and per-platform wrapper deployment"
date: "2026-08-23"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved" # draft | approved | deprecated — revision 4 (skills bundle contract, G15, ADR-015) PENDING re-approval; revision 3 (ship model + examples–squad split) re-approved 2026-08-24
owner: "eugenio.serrano" # Functional Analyst (governs this US)
unit: "v5.1 — DevFlow Agents family (definition + deployment)"
story_points: 8 # confirmed at AITL-US-Approval (2026-08-23) — kept as the family's coherent whole (Opus review: split not required; the 4 Bolts slice by independently deliverable outcomes)
adrs:
  - "devflow/adrs/ADR-007-devflow-agent-identity-model.md"
  - "devflow/adrs/ADR-014-actors-roster-is-the-enablement.md"
  - "devflow/adrs/ADR-010-actor-grammar-and-pure-v5-vocabulary.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
  - "devflow/adrs/ADR-015-skills-in-the-agent-definition-contract.md" # revision 4 — the skills bundle
sources:
  - "devflow/discovery/DISC-001-aitl-and-subagent-orchestration.md"
  - "devflow/discovery/DISC-002-devflow-agents-architecture.md"
  - "devflow/adrs/ADR-007-devflow-agent-identity-model.md"
  - "devflow/adrs/ADR-014-actors-roster-is-the-enablement.md"
  - "devflow/functional/user-stories/US-022-actor-concept.md" # the Actor concept these definitions reference (active — the delivered DevFlow Agents foundation)
  - "devflow/adrs/ADR-015-skills-in-the-agent-definition-contract.md" # accepted 2026-08-26 — the skills bundle decision (revision 4)
  - "devflow/reviews/REV-007-testwriter-devagent-readiness.md" # approved 2026-08-26 — F-03/F-04 (the gap and measured evidence behind revision 4)
stakeholders: ["maintainer", "adopting-teams"]
tags: ["devflow-agents", "coordinator", "charters", "wrappers", "mcp", "capabilities", "v5.1"]
review_ready_at: "2026-08-26T18:06:08-03:00" # revision 4 (skills bundle contract, G15, ADR-015) — AC-2 gains the optional skills: field; AC-12/AC-13 added; rule #9 added; BOLT-006 added
review: # AITL-US-Approval (revision 4) — PENDING. Prior approvals (revisions 1–3) kept in the manifest checkpoint_approvals[] + §7 history.
  decision: ""
  reviewers: []
  started_at: ""
  decided_at: ""
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: ""
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs stay in English
  (the schema). Section headings (##) and prose follow the project's
  content_language (en, devflow/LANGUAGE; ADR-012).
  `AITL-*-Approval` codes are never translated.

  ⚠️ AITL-US-Approval (§2.6, §3.0): a feature US remains DRAFT until a
  Functional Analyst records AITL-US-Approval. Only then may it be
  decomposed into candidate functional Bolts. US-000 is outside this
  lifecycle. Approval is never inherited from related artifacts.

  ⚠️ Manifest v5 (§3.12, G33): manifest JSON in
  devflow/metrics/user-stories/US-023-devflow-agent-definition-and-deployment.json
  — created with this document (schema_version "5.0"; story_points 8
  proposed).

  ⚠️ SCOPE DEVIATION (DISC-002 rec #3): DISC-002 recommended "one registry
  US". This family splits it into three independently deliverable outcomes:
  US-022 (Actor concept — the foundation), US-023 (DevFlow Agent definition
  + deployment — this US) and US-024 (roster). Same content, better slicing
  (§2.4 split rule); the deviation is intentional and recorded here.
-->

# US-023 — DevFlow Agents: definition contract, Coordinator, charters, deployment

| Field          | Value |
|----------------|-------|
| **Unit**       | v5.1 — DevFlow Agents family (definition + deployment) |
| **ADRs**       | ADR-007 (identity model), ADR-014 (precept + approver ceiling + Coordinator-never-signs — carried from ADR-008), ADR-010 (actor grammar), ADR-004 (kit-only) |
| **Status**     | approved (AITL-US-Approval 2026-08-23) |
| **Story points** | 8 (confirmed) |

**As a** methodology maintainer, **I want** the kit to define what a
DevFlow Agent **is** — a **true actor, like a human team member**: a
governed identity (id) with a role charter that defines **what it
produces**, a model, tools and capabilities as attributes, sharing the
methodology's generic context and tooling — and to ship the **Coordinator**
plus per-role charter templates, deployed as generated wrappers to the four
platforms, **so that** adopting teams can build their own role agents that
the Coordinator orchestrates as actors who **take the baton and write
documents, write code and review everything** inside the approved flow (the
producer side of the Actor, US-022, made operative), with approvals as one
of their roles under the independence floor — and with authority enforced
by structured fields, never by prompt prose.

## 1. Acceptance criteria

- `AC-1` — **Given** the kit's `devflow/agents/` folder (G30-sanctioned by this US),
  **When** a maintainer inspects it, **Then** it contains **`examples/`** (the five
  example role definitions — `functional-analyst`, `architect`, `developer`, `qa`,
  `reviewer` — **read-only references: copied, never referenced by the roster and
  never edited in place**), **`squad/`** (the project's **live agents** — the
  folder the Coordinator writes when it creates an agent, and the only folder the
  roster's `definition:` pointers reference, ADR-013 §3.9), and a README — per
  DISC-002 §5.5 (the roster schema + example live in the `actors/` folder, US-024;
  the folders are disambiguated in the READMEs). **Each role charter
  template enumerates the productive outputs of its role** (functional
  analyst → US, architect → ADR, developer → SPEC + code, QA → TC/tests)
  and emphasizes `modes: [executor]` — the Actor as producer + approver
  (US-022, re-approved) becomes operative here: role agents are first
  defined by what they PRODUCE. **The Coordinator is not a folder or a
  generated sub-agent**: it is the Avenga DevFlow platform agent itself
  (CLAUDE.md, SKILL.md, AvengaDevFlow.agent.md, AvengaDevFlow.md),
  **evolved** to act as the orchestrator (ADR-007 §3.4 — the shared body
  carries the "never signs" paragraph; each preamble declares the
  platform spawn topology). **The family root also carries a generic
  `TEMPLATE-new-role/` for project-defined roles** (the open archetype,
  ADR-007 §3.3) so each team can configure its own agents — the Coordinator
  scaffolds from the template + the examples into `squad/` — and the
  family has an **`agents/INDEX.md`** listing the examples (shipped) and
  the project's squad (live), like every other family. *(Revised — G15,
  revision 3: `roles/` splits into `examples/` (shipped references) +
  `squad/` (the project's live agents), per ADR-013 §3.9.)*
- `AC-2` — **Given** the canonical definition contract, **When** a DevFlow Agent is
  defined, **Then** its definition file (`agents/squad/<id>/agent.yaml` for the
  project's live agents; the `examples/` share the same contract)
  carries exactly the fields: `id` (kebab-case identity), `role`,
  `description` (when the Coordinator should delegate to it), `model` (the
  agent's own declaration, constrained to the platform catalog), `modes`
  (`executor` | `approver` — **`executor` (production) is the first-class
  default**; `approver` is a configured second role), `approves`
  (checkpoint classes it may sign; empty = executor-only), `capabilities`
  (tier T0–T3, least-privilege `tools` allowlist, named `mcp_servers`),
  `escalation` triggers, `write_paths` (G30/G31 mirror), and an **optional
  `skills:` list** (the declared skills bundle, ADR-015) — plus the
  charter body (the system prompt: **who I am, WHAT I PRODUCE**, what I
  check, how I decide, when I escalate) — per DISC-002 §5.1. *(Revised —
  G15, revision 4: the contract gains the optional `skills:` declaration,
  ADR-015 §3.2.)*
- `AC-3` — **Given** a role agent spawned by the Coordinator for a V-Bounce, **When**
  the flow executes, **Then** the agent **takes the baton and produces** its
  role's artifacts — documents (US, ADR, SPEC), code, tests — inside the
  approved flow, returning control via the spawn result (state = files);
  approvals are one of its roles (approver mode, when configured, under the
  independence floor), **never its definition** — the executor side of the
  Actor (US-022, re-approved) is operative here, exactly as a human team
  member would take the task, do the work and hand it back for review.
- `AC-4` — **Given** the identity model (ADR-007), **When** authority is expressed,
  **Then** it lives in **structured fields** (`modes` / `approves` /
  `capabilities`), never in charter prose — an agent with `approves: []`
  can never sign, no matter what its prompt says; and its **productive
  mandate** (what it writes and does) is the role charter, which defines
  the agent as a producer, not as an approver.
- `AC-5` — **Given** the Coordinator, **When** the kit ships it, **Then** it is the
  one DevFlow Agent that comes with the methodology: it resolves the
  roster, **delegates production** to role agents (executor mode — they
  write the documents, code and tests of each V-Bounce), spawns approver
  agents for enabled checkpoints, enforces the escalation floor, records
  evidence — and **never signs** any checkpoint (ADR-014 §3.5 separation of
  duties). **Its identity is the Avenga DevFlow platform agent itself,
  evolved** (ADR-007 §3.4): there is **no `agents/coordinator/` folder and
  no generated coordinator sub-agent** — the orchestrator identity (never
  signs + the per-platform spawn topology) lives in the four platform
  agent files (CLAUDE.md, SKILL.md, AvengaDevFlow.agent.md,
  AvengaDevFlow.md), and the generator produces only role agents.
- `AC-6` — **Given** spawn topology, **When** executors run, **Then** approver
  agents are spawnable **only by the Coordinator (or invoked by a human)**,
  never from an executor's subtree — enforced natively per platform
  (Claude Code `Agent(...)` allowlist, OpenCode `permission.task`, Copilot
  tool omission, Codex role config + parent instruction) — DISC-002 §5.2.
- `AC-7` — **Given** capability tiers, **When** an agent acts as **approver**, **Then**
  it runs at **T0 (repo-only; at most T1 with pinned trusted sources)**, no
  write paths, no transactional MCPs — the injection-forged-approval
  defense (ADR-014 §3.6, DISC-002 §5.4). Executor agents may be as capable
  as the project dares (T1–T3); approval integrity never depends on an
  executor's capability tier.
- `AC-8` — **Given** MCP access, **When** an agent declares MCP servers, **Then**
  each server is **named and allowlisted** in the agent's definition
  (`mcp_servers: []` by default); there is no implicit or unrestricted MCP
  exposure (DISC-002 §4.2, §5.4).
- `AC-9` — **Given** the example definitions in `devflow/agents/examples/`,
  the project's live agents in `agents/squad/` and the per-platform install
  mapping, **When** they change, **Then** the
  kit ships **no pre-built role wrappers**: the platform folders
  (`.claude/agents/`, `.opencode/agents/`, `.github/agents/`,
  `.codex/agents/`) ship empty or absent, and the **Coordinator installs
  the wrappers into the adopting project** at adoption time (ADR-013 §3.9;
  the operational capability is US-025). The maintainer-side wrapper
  generator + **N×4 parity check** remain a generation-validation invariant
  in `tools/` (the four-agent sync philosophy extended to N roles × 4
  platforms; US-016 automates it), **never a shipped artifact**.
  *(Revised — G15, revision 3: the original "generated and committed to the
  kit / no build step" ship model is superseded by ADR-013 §3.9; DISC-002
  §5.5's "no adoption-time build" is refined by that decision. See §7
  history.)*
- `AC-10` — **Given** the platform verification status, **When** wrappers are
  generated, **Then** Claude Code receives full native coverage (model +
  tools + MCP + hooks + allowlists); Codex (open invocation issues
  #14579/#15250) and Copilot (env-dependent `model` / `mcp-servers`) are
  **re-verified against current docs** at implementation and use documented
  fallbacks, recorded per platform (DISC-002 rec #6, §7 #1).
- `AC-11` — **Given** the kit partition (ADR-004), **When** this US executes, **Then**
  only `distribution-kit/` and `tools/` change; the root `devflow/`
  governance stays untouched.
- `AC-12` — **Given** the canonical definition contract (ADR-015, revision 4),
  **When** a definition carries skills, **Then** its folder MAY contain a
  `skills/` area (`skills/<skill-name>/SKILL.md` + optional `references/` +
  `assets/`) declared in `agent.yaml` via the optional `skills:` list under
  **strict symmetry** — an undeclared skill folder fails validation exactly
  like a declared skill without its folder (tooling-enforced in v1, the
  install act refusing an asymmetric definition; schema in v2) — while the
  two-file pair alone remains a complete, valid definition and the five
  shipped examples conform unchanged (ADR-015 §3.1–§3.2). *(New — G15,
  revision 4.)*
- `AC-13` — **Given** a definition with declared skills and the per-platform
  install mapping, **When** the Coordinator copies, installs, deletes or
  parity-checks it, **Then** the **definition folder is the atomic unit**
  (skills travel with the pair — installing the wrapper while leaving
  declared skills behind fails the act); `VERIFICATION.md` carries a
  **skills projection row per platform** (surfaces re-verified against
  current docs at implementation time), projected skill files carry a
  provenance marker and enter the **N×4 parity check** like wrapper files;
  and on a platform with no usable skills surface the install resolves by
  the **never-silent fallback** — inline-with-warning under that platform's
  size cap, or degraded-with-explicit-notice; a silent partial install is
  prohibited (ADR-015 §3.3–§3.5). *(New — G15, revision 4.)*

> ACs are verifiable functional criteria only; the non-functional
> constraints (approval-integrity, independence, safe-default) live in
> ADR-014 (carrying ADR-008's precept).

## 2. Bolts

Tentative decomposition (detailed as candidate Bolts after
`AITL-US-Approval`):

| # | Bolt | Type | Layer | Description | Est. active delivery |
|---|------|------|-------|-------------|----------------------|
| 1 | US-023.BOLT-001 | functional | Kit docs | The definition contract (`agent.yaml` fields + charter structure), the Coordinator definition + charter, the five role charter templates — **each enumerating its role's productive outputs (FA→US, architect→ADR, developer→SPEC+code, QA→TC/tests) and emphasizing `modes: [executor]`** (the producer + approver reframe) — the `devflow/agents/` family (G30-sanctioned) | 3–4h |
| 2 | US-023.BOLT-002 | functional | Tooling | The wrapper generator in `tools/` (canonical → 4 platform wrappers) + the N×4 parity check, integrated with the US-016 audit tool | 4h |
| 3 | US-023.BOLT-003 | functional | Deployment | Generate + commit the per-platform wrappers; per-platform verification notes (Claude full coverage; Codex/Copilot re-verified against current docs with recorded fallbacks) | 3–4h |
| 4 | US-023.BOLT-004 | functional | Smoke | Minimal spawn smoke test on the pilot platform (Claude Code): wrapper files load, a role agent spawns with its declared model/tools, control returns (DISC-002 §7 #7) | 2h |
| 5 | US-023.BOLT-005 | functional | Kit docs | **The agents/ examples–squad split (ADR-013 §3.9, revision 3):** rename `roles/` → `examples/` (read-only references); create `agents/squad/` (the project's live agents — the Coordinator's writable workspace, the only folder the roster references) with its README; move `TEMPLATE-new-role/` to the family root; the create-your-own guide + the definition contract to `agents/README.md`; update `agents/INDEX.md` (examples shipped + squad live) and VERIFICATION.md path references; ADR-005 phrase-family sweep for `roles/`; self-containment | 2–3h |
| 6 | US-023.BOLT-006 | functional | Kit docs | **The skills-bundle contract (ADR-015, revision 4):** `agents/README.md` gains the `skills/` structure, the `skills:` contract field and the strict-symmetry rule; `examples/README.md` + `squad/README.md` rewritten folder-atomically (copy/install/delete/parity operate on the whole definition folder); `VERIFICATION.md` gains the per-platform skills projection rows, the parity extension to projected skill files (provenance markers) and the never-silent fallback policy; the four Coordinator platform preambles' install act updated; the content-never-authority and tool-agnosticism invariants (ADR-015 §3.6–§3.7) stated where the contract lives | 3–4h |

> Plausibility (§2.6): 8 SP → 4+ Bolts. One coherent family (contract →
> generator → deployment → smoke), each outcome independently demonstrable.
> The full flow + red-team pilot is a separate, later US.

## 3. Business rules

| # | Rule | Condition | Action |
|---|------|-----------|--------|
| 1 | Coordinator never signs | Any checkpoint | The Coordinator routes, spawns, records, enforces — approval is never its decision (ADR-014 §3.5) |
| 2 | Approver ceiling | An agent acts as approver | Capability tier T0 (at most T1 pinned); no write paths; no transactional MCPs (ADR-014 §3.6) |
| 3 | Structured authority | An agent is defined | `modes`/`approves`/`capabilities` fields govern; charter prose carries judgment, never authority (ADR-007) |
| 4 | **Agents are producers first** | A role agent is chartered | Its charter defines **what it produces** (documents, code, tests); `approves` is a structured secondary attribute — the agent is an actor that does the work, and *may also* approve (US-022 producer+approver reframe); it is never defined as a mere approver |
| 5 | Charters are templates | Adopter instantiates a role agent | The kit's charter templates are copied, never edited in place (DISC-002 §5.5) |
| 6 | G30 sanction | The `agents/` folder lands | Sanctioned in the kit by this US; the root `devflow/` is never touched (ADR-004) |
| 7 | No pre-built role wrappers shipped | The kit ships | The kit ships only the 4 MainAgents + the canonical definitions + templates + the install mapping; the Coordinator installs the role wrappers into the adopting project (ADR-013 §3.9; US-025). Parity N×4 stays a maintainer generation-validation invariant (US-016), never a shipped artifact |
| 8 | Spawn topology | An executor spawns an agent | Approver agents are reachable only via the Coordinator's spawn list (or human invocation); executors never spawn their own approver |
| 9 | Skills are content, never authority | A definition carries `skills/` | No SKILL.md, reference or asset grants authority, tools, MCP servers, tier or spawn — authority stays in structured fields (ADR-015 §3.6). Kit-shipped example skills name no MCP servers, external tools or vendor schemas — integrations are the adopting team's configuration (ADR-015 §3.7) |

## 4. User flows

```mermaid
flowchart TB
    H["Human operator"] -->|talks to| C["Coordinator<br/>(ships with the kit)<br/>routes · spawns · records · NEVER signs"]
    C -->|"spawn: take the baton<br/>execute the Bolt"| DEV["developer-agent<br/>executor · produces SPEC + code + tests<br/>T1+"]
    C -->|"spawn: approve MEM"| QA["qa-agent<br/>approver · T0/T1 · approves: [MEM]"]
    C -.->|escalation floor| H
    R[("roster.yaml<br/>(US-024)")] --- C
    DEV -->|"structured result + files<br/>(control returns)"| C
    QA -->|decision + evidence| C
    C -->|checkpoint_approvals[] entry| M[("manifest")]
    DEF["agents/squad/&lt;id&gt;/agent.yaml<br/>(live — created from examples/ + TEMPLATE-new-role)"] -->|generated + parity N×4| W["wrappers: .claude · .opencode · .github · .codex"]
```

## 5. Impact

- **Creates:** the `devflow/agents/` family in the kit (contract,
  Coordinator, charter templates), the wrapper generator in `tools/`, the
  deployed per-platform wrappers (the roster lives in `actors/`, US-024) —
  and, from revision 4, the **skills-bundle contract** in the definition
  family (ADR-015: `skills/` area, `skills:` field, folder-atomic
  lifecycle, projection + parity + fallback).
- **Depends on:** US-022 (the Actor concept the definitions reference —
  producer + approver — active, the delivered DevFlow Agents foundation), US-016 (the audit
  tool that automates the N×4 parity check), ADR-007/008 (approved — the
  substance), ADR-010 (actor grammar), ADR-015 (accepted — the skills
  bundle, revision 4).
- **Precedes:** US-024 (the roster lists the agents this US defines), the
  Claude Code pilot US (full flow + red-team AC).
- **Makes operative:** the **producer side** of the Actor (US-022) — role
  agents are chartered by what they produce (documents, code, tests) and
  take the baton inside the approved V-Bounce flow, like human team
  members; approvals are one of their roles, never their definition.
  Consistent with the US-022 reframe: **no autonomous initiative** — the
  production happens inside the approved flow, with the human governing at
  every checkpoint (option A of the reframe, not option B).
- **Does NOT include:** the roster contents/validation (US-024), the
  roster enablement (US-024/ADR-014), the pilot flow and
  red-team (later US).
- **Risk:** platform contract drift (Codex/Copilot gaps) — controlled by
  re-verification at implementation (AC 9) and the parity check; wrapper
  drift between the canonical definitions and the four projections —
  controlled by the N×4 parity invariant.

## 6. SDLC tool alignment

Maintainer-internal (the methodology dogfoods itself); no external tracker.

## 7. AITL-US-Approval

> **Avenga DevFlow §2.6, §3.0.** This feature US remains a draft until a
> Functional Analyst records `AITL-US-Approval` (recorded in the `review`
> frontmatter block), confirming that the US and its ACs faithfully
> represent the evidence in its sources. Only then may it be decomposed
> into candidate functional Bolts. US-000 is outside this lifecycle.

| Field | Value |
|-------|-------|
| **Approver** | eugenio.serrano (functional_analyst) |
| **Decision** | **approved** (initial, 2026-08-23T15:50:52) + **re-approved** (delivered-state, no coordinator folder, 2026-08-23T17:30:48) + **re-approved (revision 3, ship model + agents/ examples–squad split, G15, 2026-08-24T00:40:35)**: AC-9 + rule #7 aligned to ADR-013 §3.9; AC-1/AC-2 split `roles/` into `examples/` (shipped references) + `squad/` (live agents); BOLT-005 added |
| **review_ready_at** | initial `2026-08-23T15:48:00-03:00` · re-approval `2026-08-23T17:29:00-03:00` · revision 3 `2026-08-23T18:45:04-03:00` |
| **review.started_at** | initial `2026-08-23T15:49:00-03:00` · re-approval `2026-08-23T17:29:30-03:00` · revision 3 `2026-08-24T00:40:35-03:00` |
| **review.decided_at** | initial `2026-08-23T15:50:52-03:00` · re-approval `2026-08-23T17:30:48-03:00` · revision 3 `2026-08-24T00:40:35-03:00` |
| **Story points** | **8** (confirmed) |
| **Findings** | none — acknowledged_without_comment (reason in the frontmatter `review:` block) |

## 8. Manifest creation (mandatory)

Manifest at
`devflow/metrics/user-stories/US-023-devflow-agent-definition-and-deployment.json`
(`schema_version 5.0`; `us` block; `story_points: 8` proposed → confirmed
at approval; empty `bolts` / `checkpoint_approvals`). Validates against
`manifest-v5-us.schema.json`.
