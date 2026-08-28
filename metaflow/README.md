# MetaFlow — Development Flow

**Methodology version:** 1.1

## Purpose

This folder is the **single source of truth** for all project documentation —
business context, analysis, architecture decisions, implementation specs,
reviews, and execution memory. It embodies *Documentation as Code*: the docs
live with the code, are versioned with Git, and are maintained as part of the
normal workflow.

Everything starts in `01-input/` (raw material from the client or legacy system)
and flows through analysis, discovery, functional definition, architecture
decisions, implementation specs, and finally captured knowledge in `22-memory/`.

> **Normative hierarchy:** the methodology in
> [`ai-sdlc/MetaFlow.md`](ai-sdlc/MetaFlow.md) is the
> single source of truth. §2 owns concepts and artifact contracts; §3 owns
> lifecycle, CITL, gates, autonomy and metrics; §4 is an explanatory
> walkthrough; §5 owns structure, locations and names. When repeated text
> appears to diverge, the section that owns that dimension governs.

---

## Folder Map

```
metaflow/
├── 01-input/              ← Raw entry material (read-only, as received)
│   ├── business/           RFPs, BRDs, SOWs, compliance, regulations
│   ├── databases/          Legacy DB schemas, DDL, ER diagrams
│   ├── documentation/      Third-party docs: API manuals, datasheets, vendor PDFs
│   ├── interviews/         Stakeholder conversation transcriptions (INT-NNN)
│   ├── source-code/        Legacy source code and configs
│   └── ui-ux/              Screenshots, mockups, brand guidelines, UX research
│
├── 02-analysis/           ← Domain analysis
│   ├── introduction/       Plain-language feature narratives (derivative, non-governed)
│   ├── vision/             Product vision and strategy
│   ├── business-context/   Business objectives, constraints, market context
│   ├── business-risks/     Pre-execution business risks (BR-NNN)
│   ├── scope/              Scope and phasing decisions per milestone
│   ├── personas/           User archetypes
│   ├── user-journeys/      End-to-end user experience maps
│   ├── glossary/           Ubiquitous language terms
│   ├── domain-model/       Entity definitions, relationships, enums
│   ├── ui/                 Surfaces, patterns, states and parity contracts
│   ├── process/            Business processes (BPMN/Mermaid, PROC-NNN)
│   └── open-questions/     Centralized backlog of analysis questions (OQ-NNN)
│
├── 03-discovery/          ← Need-driven investigations (DISC-NNN, CP-DISC-Approval)
├── 12-functional/         ← User Stories + TASKs (WHAT to build)
│   ├── user-stories/       Feature US (US-NNN) + US-000-non-functional.md container
│   └── tasks/              Functional (US-NNN.TASK-NNN) · non-functional (US-000.TASK-NNN) · Test (TC-NNN.TASK-NNN)
├── 11-adrs/               ← Architecture Decision Records (ADR-NNN, CP-ADR-Approval)
├── 21-spec/               ← One canonical SPEC per TASK (SPEC-YYMMDD-HHmm, CP-SPEC-Approval)
├── 22-memory/             ← One MEM per Delivery Loop (MEM-YYMMDD-HHmm, CP-MEM-Approval)
├── 23-metrics/            ← Manifest family v1 (tasks/ · user-stories/ · test-cases/) + schemas
├── 42-reports/            ← Sprint progress reports (PM; generator planned, tools track)
├── 24-tests/              ← Human-facing verification
│   ├── test-cases/         Test Cases (TC-NNN, CP-TC-Approval)
│   └── uat/                UAT minutes (UAT-NNN) — dormant/reserved
├── 31-reviews/            ← Stakeholder-triggered reviews (REV-NNN, CP-REV-Approval)
├── 32-adv-reviews/← LLM-vs-LLM debates (AREV-NNN: Critique → Defense → Verdict)
├── 13-bugs/               ← Confirmed defects (BUG-NNN, CP-BUG-Approval)
├── 34-incidents/          ← Production incidents & post-mortems (INC-NNN)
├── 33-risks/              ← Risk register (RISK-NNN)
├── 35-retros/             ← Weekly retrospectives (RETRO-NNN)
├── 52-agents-data/        ← Per-agent shared knowledge (each agent creates its own folder)
├── 41-prompts/            ← Project prompts (PROMPT-NNN, copy-paste ready)
├── bin/                ← Compiled tooling executables (optional; replaced on upgrade, §5.16)
├── ai-sdlc/     ← Methodology reference (single source of truth)
├── ONBOARDING.md       ← Onboarding guide for new team members
└── GUARDRAILS.md       ← Agent-enforced rules (CITL stops, naming, traceability)
```

Alongside `metaflow/`, the repository root also carries **`AGENTS.md`** — the
cross-tool entry point several agents auto-load — and the **agent definition
for the tool your team uses**, at the location that tool expects (`CLAUDE.md`
at the root, `.github/agents/`, `.opencode/agents/`, `.agents/skills/`). Both
are installed from the MetaFlow distribution (§5.2).

---

## The Complete Flow

```mermaid
flowchart TB

    subgraph P1["📥 INPUT"]
        direction LR
        IN["01-input/<br>interviews · business · DBs<br>source-code · docs · ui-ux"]
    end

    subgraph P2["🔍 UNDERSTAND"]
        direction LR
        AN["02-analysis/<br>domain model · ui · personas<br>journeys · processes"]
        DI["03-discovery/<br>DISC-NNN"]
    end

    subgraph P3["📐 DEFINE"]
        direction LR
        FA["12-functional/<br>feature US + US-000"]
        TC["24-tests/test-cases/<br>TC-NNN"]
        AD["11-adrs/<br>ADR-NNN"]
    end

    subgraph P4["⚡ DELIVERY LOOP"]
        direction LR
        SP["21-spec/<br>one canonical SPEC"]
        CO["src/<br>code + tests"]
        MM["22-memory/<br>one MEM per Delivery Loop"]
        MT["23-metrics/<br>manifest family v1"]
    end

    subgraph P5["🛡️ GOVERN"]
        direction LR
        RV["31-reviews/"]
        AV["32-adv-reviews/"]
        BG["13-bugs/"]
        IC["34-incidents/"]
        RK["33-risks/"]
        RT["35-retros/"]
        TT["24-tests/uat/"]
    end

    %% FORWARD FLOW (each stop is a CITL checkpoint)
    IN --> AN
    IN --> DI
    AN -->|"CP-US-Approval"| FA
    AN --> AD
    DI --> FA
    DI --> AD
    FA -->|"CP-TASK-READY-Approval"| SP
    AD -->|"CP-ADR-Approval"| SP
    TC -->|"CP-TC-Approval"| SP
    SP -->|"CP-SPEC-Approval"| CO
    CO --> MM
    CO --> MT
    MM --> MT

    %% GOVERNANCE
    MT -->|"audit"| RV
    RV -->|"finding → BUG/TASK/DISC/ADR/RISK"| BG
    AV -->|"approved Verdict findings"| BG
    BG -->|"CP-BUG-Approval → dedicated TASK"| FA
    IC -->|"root cause"| BG
    IC -->|"hardening"| FA
    RT -.->|"reads"| MT
    RT -.->|"improves"| RV
    TT -->|"release feedback → new TASKs"| FA

    %% STYLES
    classDef c1 fill:#fef9e7,stroke:#b7950b,stroke-width:2px
    classDef c2 fill:#d5f5e3,stroke:#1e8449,stroke-width:2px
    classDef c3 fill:#d6eaf8,stroke:#2471a3,stroke-width:2px
    classDef c4 fill:#fadbd8,stroke:#c0392b,stroke-width:2px
    classDef c5 fill:#e8daef,stroke:#7d3c98,stroke-width:2px
    class P1 c1
    class P2 c2
    class P3 c3
    class P4 c4
    class P5 c5
```

### How to read it

Five phases, top to bottom. **Solid arrows** = forward flow. **Dashed arrows** = feedback loops.
Every forward stop is governed by a named CITL checkpoint (see [CITL Checkpoints](#checkpoints-checkpoint-in-the-loop--citl)).

| Phase | What happens |
|-------|-------------|
| **📥 Input** | Raw material lands here. Read-only. Everything starts from this. |
| **🔍 Understand** | `02-analysis/` extracts domain knowledge. `03-discovery/` researches material unknowns (DISC). |
| **📐 Define** | `12-functional/` defines WHAT (feature US / US-000 + TASKs). `11-adrs/` decides HOW. `24-tests/test-cases/` defines the independent verification contracts (TC). |
| **⚡ Delivery Loop** | One canonical SPEC per TASK → AI generates the intended-final change + tests → one MEM + manifest v1 entry → human review. |
| **🛡️ Govern** | Reviews, adversarial reviews, bugs, incidents, risks and retros feed the flow. |

### One path into Delivery Loop

All work follows the **same single path** — regardless of whether it originates
from a feature, a defect, a review finding, or a QA Automation need:

```
Trigger (US | BUG | TC | DISC | REV | AREV | ADR)
  → origin approved (CP-US-Approval | CP-BUG-Approval | CP-TC-Approval | CP-DISC-Approval | CP-REV-Approval | CP-AREV-VERDICT-Approval | CP-ADR-Approval)
  → TASK (CP-TASK-READY-Approval — includes DoR)
  → SPEC (CP-SPEC-Approval)
  → Delivery Loop → 24-tests/gates
  → MEM + manifest v1 update
  → CP-MEM-Approval → CP-TASK-DONE-Approval
```

| Step | What happens |
|------|-------------|
| **Trigger** | A feature US, a confirmed BUG, an approved TC, or approved DISC/REV/AREV conclusions or ADR evidence identify work to be done. |
| **Origin approval** | Feature US → `CP-US-Approval`; BUG → `CP-BUG-Approval` (before its dedicated TASK); TC → `CP-TC-Approval` (before it governs); DISC/REV/AREV conclusions and ADRs carry their own approvals before governing a TASK. |
| **TASK** | One of three types: `functional` (feature US), `non-functional` (`US-000`), `test` (`TC-NNN.TASK-NNN`). Approved individually at `CP-TASK-READY-Approval`. |
| **SPEC** | One canonical SPEC per TASK (`task` field mandatory). The agent runs the pre-SPEC evidence gate; a human approves at `CP-SPEC-Approval`. |
| **Delivery Loop** | AI generates the intended-final change, runs tests until green (BUGs: strict red→green TDD inside the same Delivery Loop), then creates exactly one MEM and updates the manifest. |
| **Review** | The executing Dev-validator approves the MEM at `CP-MEM-Approval` (one approver, any risk; QA/Sec/domain reviewers optional). |
| **Acceptance** | `CP-TASK-DONE-Approval` marks the TASK `Done`. Release and promotion follow the adopting team's own process (§4.6). |

**No code change happens without an approved TASK.** Every SPEC references a
TASK; every Delivery Loop produces exactly one MEM; previous MEMs are immutable
history.

---

## Delivery Loop: The Execution Micro-Cycle

Every TASK is executed through **Delivery Loop** — the core execution pattern:

```mermaid
flowchart LR
    SPEC["📐 SPEC<br>CP-SPEC-Approval"] --> AI["🤖 AI Agent<br>generates intended-final<br>code + tests<br>& runs tests"]
    AI --> GATES["🔒 CI Gates<br>pass | waived (ADR) | n/a"]
    GATES -->|"fail"| AI
    GATES -->|"pass"| ARTIFACTS["📝 AI creates exactly one MEM<br>+ appends delivery_loops[] entry"]
    ARTIFACTS --> HUMAN["👤 CP-MEM-Approval<br>executing Dev-validator reads<br>diff + test evidence + MEM + manifest"]
    HUMAN -->|"changes requested"| NB["New Delivery Loop<br>new MEM"]
    NB --> SPEC
    HUMAN -->|"approved"| DONE["✅ Delivery Loop approved<br>TASK: Development Completed"]
```

**Key principles:**
- The AI agent generates the **intended-final** artifacts by default (code, tests, config, docs) and **runs its own tests** until green or a stop condition.
- After execution, the agent creates **exactly one MEM** and updates the TASK manifest in `metaflow/23-metrics/tasks/` — **before** human review.
- The human reviewer receives the **complete package**: code + 24-tests/gates + MEM + manifest.
- `CP-MEM-Approval` is recorded by the **Dev-validator who executed the TASK** (one approver, any risk; QA/Sec/domain reviewers optional); the agent never self-approves.
- `changes_requested` preserves the MEM as immutable history; the next execution is a new Delivery Loop with a new MEM.
- Every US, TASK and TC produces a manifest in `metaflow/23-metrics/` that validates against its `manifest-v1*.schema.json`.

---

## Checkpoints (Actor-in-the-Loop — CITL)

An approved checkpoint is **non-negotiable** — the approver is an **actor**, a
**human by default** and a virtual MetaFlow Agent only by explicit, valid
configuration (with no or invalid config this is pure Human-in-the-Loop; **no
AI-signed approval is possible**). Checkpoints are named
`CP-<CODE>-Approval`; the legacy checkpoint prefix is invalid.
Every approval requires a named reviewer (a human by default), review timestamps
and review-quality evidence (see [GUARDRAILS.md](GUARDRAILS.md) for the full map).

| Checkpoint | Owner | Validates |
|-----------|-------|-----------|
| `CP-US-Approval` | Functional Analyst | Feature US + ACs approved; only then decomposable |
| `CP-BUG-Approval` | Functional Analyst (functional) / Architect-TL recommended if `severity: critical` else any team member (non-functional) — guidance, never a gate: any qualified member, the author included, may approve at any severity | BUG confirmed; only then its dedicated TASK |
| `CP-TC-Approval` | QA + domain owner | TC approved as independent verification contract |
| `CP-TASK-READY-Approval` | Functional Analyst (functional) / Architect-TL (non-functional; except a non-functional BUG's dedicated TASK, which mirrors its parent BUG's severity routing) / QA Lead · QA Automation Lead · Architect · TL (test) | TASK approved (includes DoR) |
| `CP-ADR-Approval` | Architect / Tech Lead | ADR accepted and immutable |
| `CP-SPEC-Approval` | Dev-validator + domain owners | One-TASK implementation plan approved |
| `CP-MEM-Approval` | Dev-validator who executed the TASK (one approver, any risk; QA/Sec/domain optional) | MEM + Delivery Loop approved |
| `CP-TASK-DONE-Approval` | PO/PM (functional) · technical owner (non-functional) · QA Lead / QA Automation Lead (test) | TASK `Done` |
| `CP-DISC-Approval` · `CP-REV-Approval` · `CP-AREV-{CRITIQUE,DEFENSE,VERDICT}-Approval` | Qualified humans | Conditional: mandatory once triggered |

No TASK moves forward without its **required checkpoints signed with
review-quality evidence** (coverage by TASK type in GUARDRAILS.md).

---

## Quick Start — Daily Workflow

Already have a configured project? Here's the day-to-day flow:

```mermaid
flowchart LR
    A["📋 Pick approved TASK"] --> B["📐 Prepare SPEC<br>(evidence gate)"]
    B --> C["✍️ CP-SPEC-Approval<br>SPEC-YYMMDD-HHmm"]
    C --> D["🤖 AI Agent<br>Delivery Loop"]
    D --> E["📝 MEM + manifest<br>delivery_loops[] entry"]
    E --> F["✅ CP-MEM-Approval<br>diff + evidence"]
```

### Cheat Sheet

| You need to... | Do this |
|---------------|---------|
| Research something unknown | Create `DISC-NNN` in `03-discovery/` → `CP-DISC-Approval` |
| Define business behavior | Create feature US in `12-functional/user-stories/` → `CP-US-Approval` |
| Define a technical outcome | Create non-functional TASK under `US-000` (no US approval needed) |
| Make a technical decision | Create `ADR-NNN` in `11-adrs/` → `CP-ADR-Approval` |
| Implement a TASK | `CP-TASK-READY-Approval` → `SPEC-YYMMDD-HHmm` → `CP-SPEC-Approval` → Delivery Loop → MEM + manifest |
| Verify a TASK independently | Create `TC-NNN` in `24-tests/test-cases/` → `CP-TC-Approval` |
| Automate QA | Create Test TASK `TC-NNN.TASK-NNN` from the approved TC |
| Document a defect | Create `BUG-NNN` in `13-bugs/` → `CP-BUG-Approval` → dedicated TASK → TDD in one Delivery Loop |
| Review quality | Create `REV-NNN` in `31-reviews/` → `CP-REV-Approval` |
| Run an adversarial debate | Create `AREV-NNN/` in `32-adv-reviews/` (3 sequential phase approvals) |
| Log a risk | Create `RISK-NNN` in `33-risks/` |
| Store raw material | Drop in `01-input/` (business, databases, documentation, interviews, source-code, ui-ux) |

---

## Traceability Rules

Every document references the documents it depends on:

- A **DISC** references the `01-input/` material it analyzed and carries `CP-DISC-Approval`.
- A **feature US** references the raw inputs / analysis evidence and carries `CP-US-Approval`.
- A **BUG** carries `CP-BUG-Approval` and references its exactly-one dedicated TASK; the TASK references the BUG.
- A **TC** references exactly one approved source TASK (+ US/ACs or governing technical sources) and carries `CP-TC-Approval`.
- A **TASK** references its parent (approved feature US, `US-000`, or one approved TC) and carries `CP-TASK-READY-Approval`.
- A **SPEC** references exactly one approved TASK; its `sources` lists every governed artifact actually used.
- An **ADR** references its motivating sources and carries `CP-ADR-Approval`.
- A **REV** / **AREV** references the artifacts it audits; findings are governed only after their approvals.
- A **MEM** references its TASK, canonical SPEC revision, Delivery Loop number and manifest `delivery_loops[]` entry.
- The **manifest family** validates against the `manifest-v1*.schema.json` schemas and records each artifact's lifecycle CITL decisions and step timings (minimal projection).

---

## Golden Rules

1. **Read the folder's README** before creating any document.
2. **Use the template** (`TEMPLATE-*.md`) as your starting point.
3. **The methodology governs** — `ai-sdlc/MetaFlow.md` is the single source of truth; §2/§3 own the rules, §4 is a walkthrough, §5 owns locations.
4. **No code without an approved TASK** — no exceptions; urgency and size create none (the one scope-out, G07: the agent lifecycle within `metaflow/51-agents/` + `metaflow/53-actors/` is operational config — living data).
5. **Every approval is a named human checkpoint** — `CP-<CODE>-Approval`, with timestamps and review-quality evidence. The agent never self-approves.
6. **One canonical SPEC per TASK; exactly one MEM per Delivery Loop** — previous MEMs are immutable history.
7. **An artifact without its manifest does not exist** — every US, TASK and TC has a manifest in `metaflow/23-metrics/` that validates against its `manifest-v1*.schema.json`.
8. **A failed gate cannot be overridden without an ADR** approved through `CP-ADR-Approval` (owner + compensating control + expiry); the gate records `waived`, never `pass`.
9. **The reviewer reads the diff and the test evidence**, not the agent's self-summary.
10. **Mermaid for every diagram** (BPMN allowed for business processes); never ASCII art or embedded images as diagram substitutes.

---

## Starting a New Project

1. Install the distribution: the entire `metaflow/` folder, `AGENTS.md` at the
   repository root, and the agent definition for your tool at the location it
   expects.
2. Drop all raw material into `01-input/` organized by subfolder.
3. Process `01-input/` into `02-analysis/` (AI-assisted; Functional Analyst governs).
4. Create feature USs and stop at `CP-US-Approval`; technical work goes under `US-000`.
5. Define and approve candidate TASKs (`CP-TASK-READY-Approval`) — functional, non-functional, and (from approved TCs) test.
6. Draft and approve Test Cases (`CP-TC-Approval`) before the implementation SPEC.
7. Create ADRs (`11-adrs/`) as technical decisions are made (`CP-ADR-Approval`).
8. For each TASK: SPEC → `CP-SPEC-Approval` → Delivery Loop → MEM + manifest → `CP-MEM-Approval`.
9. Accept TASKs (`CP-TASK-DONE-Approval`); release/promotion follows the team's own process (§4.6).
10. Conduct reviews (`31-reviews/`, `32-adv-reviews/`) as stakeholders trigger them.

---

## Known Limitations & Roadmap

What this version deliberately does **not** cover yet — read before adopting:

| Limitation | Status | Where it is governed |
|------------|--------|----------------------|
| **Unit/UAT approval-and-release layer** | **Removed in the previous lineage** — the reserved UNIT/UAT approval checkpoints and their promotion sequence did not reflect real corporate environment/promotion complexity. The governed flow ends at TASK acceptance; release/promotion follows the team's own process. A redesigned model is planned for a future release. | §4.6 |
| **Multi-repo / shared-monorepo `metaflow/`** | Out of scope — SPEC, manifest and MEM resolve paths against a single repository baseline. To adapt: relocate `metaflow/` and redefine the manifest's repository-relative `ref`/`sources` semantics. | §1 "Repository topology assumption" |
| **Monetary cost** | Deferred — no price catalog, no cost metric. Manifests keep recording provider/model/token usage in `runs[]`, so when pricing returns, costs are computable retroactively over all historical manifests. | §3.12 — `runs[]` keeps the token model; cost stays computable retroactively |
| **Validation tooling** | No validator ships with the methodology — G23/G33 schema and lifecycle validation remains procedural (agents and humans). Tooling arrives with the tools track, not with the methodology: optional by contract, with `metaflow/bin/` reserved in the canonical tree for when it lands (§5.1). | `GUARDRAILS.md` G23/G33, §5.1 — tools track (arrives with `metaflow/bin/`) |
| **Report generation** | Planned — a report template design reference ships with the tooling track, not a generator. The manifest family already records everything a report needs (§3.12 timing contract), so reports stay computable retroactively once the tooling lands. | `42-reports/README.md`, §5.12 |

---

## Language Policy

The schema (YAML keys, enum values, IDs) is always in **English**; validators
and INDEX counters require it. The project's `content_language`, declared in
[`LANGUAGE`](LANGUAGE), governs the prose, the filename `<description>` slugs
(kebab-case ASCII, no accents), ADR titles, and the section headings of
`02-analysis/`, feature User Stories and Test Cases. Headings of every other
artifact family stay in English, and `CP-*-Approval` codes are never
translated (§3.15).

---

## Further Reading

- **`ai-sdlc/MetaFlow.md`** — The full methodology (normative source): Delivery Loop, three TASK types, named CITL checkpoints, Delivery Flow Five metrics, gates, manifest family v1 and governance.
- **`GUARDRAILS.md`** — Agent-enforced rules: CITL stops, blocking/warning guardrails, naming, traceability.
- **`ONBOARDING.md`** — Recommended reading order and role-based map.
- **`23-metrics/README.md`** — Manifest family v1 schemas and lifecycle.
- Every subfolder has its own `README.md` — read it before creating documents there.
