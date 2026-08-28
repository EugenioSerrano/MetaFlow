# Onboarding — MetaFlow

**Methodology version:** 1.1

> **Getting started.** Everything you need to know about how we work here and
> how to take your first TASK. If it is not in this document, it is in the
> source of truth.

## 1. What this is

MetaFlow is the project's AI-assisted development methodology: the **AI
generates**, the **human governs** through mandatory approval checkpoints
(CITL — an actor, human by default) at every step.

- **Source of truth:** [`ai-sdlc/MetaFlow.md`](ai-sdlc/MetaFlow.md) (v1.1)
- **Rules the agent enforces:** [`GUARDRAILS.md`](GUARDRAILS.md) (CITL stops, naming, traceability)

---

## 2. Reading order by role (5–10 min each path)

| Role | Read this | Why |
|------|-----------|-----|
| **Everyone** | `02-analysis/introduction/` (if present) → `README.md` → §0 of `MetaFlow.md` → `GUARDRAILS.md` (checkpoint map + blocking rules) | The plain-language story of each feature first (no jargon, not a source of truth), then the flow, the mandatory human stops, and what is forbidden |
| **Stakeholder / PO** | `02-analysis/vision/` + `12-functional/INDEX.md` | Review and contribute to USs and ACs; signs `CP-TASK-DONE-Approval` on every `feature` TASK (without it the TASK is not Done); does not write |
| **Functional Analyst** | `01-input/` + `02-analysis/README.md` + `12-functional/` | Create and approve USs, BUGs and functional TASKs |
| **Developer / Dev-validator** | `11-adrs/INDEX.md` + `21-spec/README.md` + `22-memory/README.md` + `23-metrics/README.md` + `24-tests/test-cases/` | Run Delivery Loops, approve SPECs and MEMs, maintain manifests |
| **Architect / Tech Lead** | `11-adrs/` + `33-risks/` | Approve ADRs, non-functional TASKs, and `critical`-severity non-functional BUGs (lower severities may be approved by any team member, author included) and promotions |
| **QA / QA Automation** | `24-tests/` + `13-bugs/` + `31-reviews/` | Design TCs, report BUGs, create Test TASKs |

---

## 3. The one TASK path

All work follows the **same single path**. Every stop is a named human
approval (`CP-<CODE>-Approval`) — none is skipped. Terms in **bold** are
defined in the glossary (§4).

```mermaid
flowchart LR
    ORIGEN["Trigger<br>US · BUG · TC · DISC · REV · AREV · ADR"] -->|"origin approved"| TASK["TASK<br>functional · non-functional · test"]
    TASK -->|"CP-TASK-READY-Approval<br>(includes DoR)"| SPEC["SPEC<br>1 canonical per TASK"]
    SPEC -->|"CP-SPEC-Approval"| VB["Delivery Loop<br>AI generates + runs tests"]
    VB --> MEM["MEM + manifest<br>delivery_loops[] entry"]
    MEM -->|"CP-MEM-Approval<br>the Dev who executed the TASK"| ACC["CP-TASK-DONE-Approval<br>TASK = Done"]
```

Golden rules of the path:

- **No code without an approved TASK** — not a typo, not a config value (G07; its one scope-out: the agent lifecycle within `metaflow/51-agents/` + `metaflow/53-actors/` is operational config — living data).
- **One Delivery Loop = one MEM** — previous MEMs are immutable history; if you request changes, the next attempt is a new Delivery Loop with a new MEM.
- **The agent never self-approves** — `CP-MEM-Approval` is signed by the Dev-validator who executed the TASK (one approver, any risk; QA/Sec/domain reviewers optional).
- **An artifact without its manifest does not exist** — every US, TASK and TC has a JSON manifest in `23-metrics/` that validates against its `manifest-v1*.schema.json`.

---

## 4. Minimal glossary (what you will see on day 1)

| Term | Definition |
|------|------------|
| **Delivery Loop** | Execution micro-cycle: approved SPEC → the AI generates and runs tests → creates MEM + updates manifest → a human approves. |
| **TASK** | Work unit (sizing: 1h–1d of active delivery, estimated per the AI-native rule §2.4 — review and rework dominate, never manual coding time). Three types: `functional` (under a feature US), `non-functional` (under `US-000`), `test` (under an approved TC, `TC-NNN.TASK-NNN`). |
| **US-000** | Permanent container for technical work (infra, refactors, hardening, CI/CD). Has no approval of its own. |
| **Story points** | Optional Fibonacci value (1\|2\|3\|5\|8\|13) on a feature US: relative functional complexity, confirmed at `CP-US-Approval`. Informational only — never time, never a gate, no velocity. US-000 has none. |
| **TC** | Test Case: independent verification contract, derived from approved intent — never from current code. |
| **SPEC** | Implementation plan for one TASK (one canonical SPEC per TASK; versioned revisions). |
| **MEM** | Narrative record of one Delivery Loop: what was done, files with reasons, test evidence, decisions. |
| **Manifest family** | One mechanical JSON per governed artifact, in three levels: feature US (`23-metrics/user-stories/`), TASK (`23-metrics/tasks/`) and TC (`23-metrics/test-cases/`), each validated by its `manifest-v1*.schema.json`. Created with the document and updated at every step, recording origin, SPEC revisions, Delivery Loops, CITL decisions and step timings (`created_at`, `review_ready_at`, `review_started_at`, `decided_at`). An artifact without its manifest does not exist (G23, G33). US-000 carries none. |
| **Actor** | A member of the team who **produces** the governed artifacts its role owns (FA → US, architect → ADR, developer → SPEC + code, QA → TC/tests) as executor and **participates** in CITL approvals as approver when configured, under the independence floor — a **human by default**, a virtual **MetaFlow Agent** only by explicit, valid configuration (§3.0.1). Recorded `human:<user>` / `agent:<id>`; the model is an attribute of the agent actor, never the identity. CITL is the default case inside CITL (actor = human); with no agents configured every checkpoint is a human approval and **no AI-signed approval is possible** (the safe-default invariant). |
| **CITL checkpoint** | Mandatory human approval with name, timestamps and evidence: `CP-US-Approval`, `CP-TASK-READY-Approval`, `CP-TASK-DONE-Approval`, `CP-SPEC-Approval`, `CP-MEM-Approval`, … (there is no `CP-TASK-Approval`: the TASK has two distinct checkpoints, G05). The legacy checkpoint prefix is invalid (G05). |
| **DoR / DoD** | Definition of Ready (validated inside `CP-TASK-READY-Approval`) / Definition of Done (completion evidence, validated at acceptance). |
| **ADR** | Immutable architecture decision (once approved, it is never edited). |
| **BUG** | Confirmed defect. Requires `CP-BUG-Approval` before its dedicated TASK is created. |
| **DISC / REV / AREV** | Investigation / review / adversarial debate — optional (need-driven), but with mandatory approvals once initiated. |
| **UAT** | User Acceptance Testing. The UAT approval checkpoint was removed in the previous lineage; release/acceptance follows the team's own process until a redesigned model ships in a future version. |
| **`_archive/`** | Per-folder subfolder holding lifecycle-closed documents. Excluded from agent scans for token economy — the agent reads it only if you explicitly ask, or if an active document references an archived artifact (§5.4, W20). |
| **`52-agents-data/`** | Per-agent shared knowledge area, versioned and visible to the whole team. No pre-created subfolders: each agent creates its own `52-agents-data/<agent-name>/` on first use and is responsible for it — durable knowledge only, never temporary data (W21), and never a replacement for `22-memory/` MEMs (§2.12). Not evidence: never citable, no CITL. The `metaflow/` folder structure is canonical — agents may not create new folders (G30) and never write into `01-input/`, which is human-deposited raw evidence (G31, §5.12). |
| **`41-prompts/`** | Project prompts (`PROMPT-NNN-<description>.md`) — versioned, team-shared, copy-paste ready. Living data: created, modified and improved in this folder, no approval and no manifest; never scattered into `52-agents-data/` (§5.12). |
| **`42-reports/`** | Sprint progress reports for project management (`REPORT-YYYY-Www.html`) built from the manifest family — delivery, quality, review latency, CITL coverage and AI usage. **Generation is planned** (tooling track): only a design reference with example data ships today. Derived, never governed: not citable as the source of any artifact (G28, §5.12). |

---

## 5. FAQ

**I found a bug, what do I do?**
Document it in `13-bugs/BUG-NNN.md` → wait for `CP-BUG-Approval` → its
dedicated TASK is created → strict TDD **inside the same Delivery Loop** (red test →
fix → green). It is never fixed under another TASK or directly from a ticket.

**Should I create a DISC or go straight to a US?**
If there is a material unknown to investigate (external API, library, legacy
behavior) → `DISC-NNN`. If you already know what to build → US directly
(business behavior) or a non-functional TASK under `US-000` with its approved
technical source (ADR/DISC/REV).

**Can I edit an approved ADR?**
No. Decisions in an approved ADR are immutable; if the decision changes, you
create a new ADR that supersedes it.

**Who approves my MEM?**
The Dev-validator who executed the TASK — the same developer who took it.
One approver at any risk; QA or Security may be added as optional reviewers, never required.

**Can I touch code without a TASK?**
No. It is a blocker (G07): code, tests, config, IaC, schemas and migrations
require an approved TASK. Urgency and size create no exception. The one
scope-out: the agent lifecycle (installing/creating/deleting MetaFlow Agents
within `metaflow/51-agents/` + `metaflow/53-actors/`) is operational config —
living data, not a code change.

**Can I work on several TASKs at once?**
Ideal WIP: **1 active TASK per person/agent** (§3.2). No multitasking — if you
get blocked, it gets resolved or returned; TASKs are not left half-done.

**Where is my TASK's manifest?**
In `23-metrics/tasks/`, named after the TASK (`US-NNN.TASK-NNN-<desc>.json` or
`TC-NNN.TASK-NNN-<desc>.json`). If it does not exist or does not validate
against `manifest-v1-task.schema.json`, the TASK does not exist. Every US and TC
has its own manifest too (`23-metrics/user-stories/`, `23-metrics/test-cases/`).

**Why does the agent not see my archived documents?**
By design (§5.4, W20). Each folder may keep an `_archive/` subfolder for
lifecycle-closed documents, and agents do **not** search, list or read it
proactively — that is what keeps their token cost down as the project grows.
Treat archived files as generally invisible to the agent: it reads them only
when you explicitly ask, or when an active document explicitly references an
archived artifact. If a task needs archived content, the agent will say so
and ask you first.

**Where do agents store their shared knowledge?**
In `metaflow/52-agents-data/` — a versioned area visible to the whole team
(§5.12). There are no pre-created subfolders: each agent creates its own
`52-agents-data/<agent-name>/` folder on first use and is responsible for its
content. Everything there is **committed to the repository and shared with
everyone**; it holds durable, team-useful knowledge only — **never temporary
data** (that goes to the OS temp directory, W21) and **never a replacement
for `22-memory/`** (one MEM per Delivery Loop stays mandatory, §2.12). It is never
evidence, carries no approvals, and agents do not scan other agents' folders
unless you ask. Agents may **not** create new folders inside `metaflow/`
outside the canonical structure (G30), and they never write into `01-input/`:
that folder is deposited by humans only and is read-only for agents (G31).

---

## 6. Language policy

The **schema** (YAML keys, enums, IDs) is always in
**English** — validators and dashboards require it. The **prose**
(descriptions, decisions, narrative) follows the project's `content_language`,
declared in `metaflow/LANGUAGE` (the language of the raw inputs; see §3.15 of
the methodology). Filename `<description>` slugs follow `content_language`
(kebab-case ASCII, no accents); section headings follow `content_language`
in `02-analysis/`, feature User Stories and Test Cases and stay English
elsewhere; ADR titles and bodies follow `content_language`. `CP-*-Approval`
codes are never translated. Never mix languages within one field.

---

## 7. Developer development plan (§3.14 — skill atrophy mitigation)

If the agent writes everything, juniors never build the skills to review the
agent. This is managed explicitly. **The plan is descriptive only** — it
creates no artifacts and no evidence of these practices is recorded in
`metaflow/` documents (§3.14):

| Practice | Cadence |
|----------|---------|
| Role rotation (Spec-author ↔ Dev-validator ↔ AI-Orchestrator) | ≥1 per quarter |
| AI-review training (common failure modes) | 1-day onboarding module |
| Quarterly skill review | Quarterly |

---

## Deeper reading

- **`ai-sdlc/MetaFlow.md`** — The complete methodology (normative; §2/§3 govern).
- **`GUARDRAILS.md`** — The 39 blockers, 21 warnings, naming and traceability.
- **`README.md`** — Framework map, full flow and cheat sheet.
- Every subfolder has its own `README.md` — read it before creating documents there.
