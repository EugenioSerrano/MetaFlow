---
id: "US-NNN.TASK-NNN" # or US-000.TASK-NNN / TC-NNN.TASK-NNN
title: ""
date: "YYYY-MM-DD"
author: ""       # human:<user> (git-email local part) | agent:<id> — actor grammar (§3.0)
llm: "" # LLM model used (e.g. "Claude Sonnet", "GPT")
status: "candidate" # candidate | approved | deprecated
owner: "" # Functional Analyst / Architect-TL / QA per type (per §2.4)
us: "" # Parent: approved feature US (functional), US-000 (non-functional), or approved TC (test)
bug: "" # BUG-NNN when BUG-driven — the BUG and TASK reference each other (§2.16)
task_type: "" # functional | non-functional | test — the three canonical types (§2.4)
work_category: "" # feature | refactor | infra | hardening | debt | qa_automation (§3.8)
service_class: "" # regulatory | incident_hotfix | feature_value | debt_hardening (§3.8)
layer: "" # Backend | Frontend | Mobile | Data | Infra | QA-Automation | Full-stack | Documentation
risk_class: "" # low | medium | high | critical (assigned during CP-TASK-READY-Approval — §3.3)
data_classification: "internal" # public | internal | confidential | restricted — ordered, normative definition in §3.6
dependencies: [] # Prior TASKs/artifacts this one depends on
sources: [] # parent US/TC, approved ADRs, DISC/REV/AREV evidence — required, min 1 (§2.4)
review_ready_at: "" # When this version is submitted for review (§3.0)
review: # CP-TASK-READY-Approval — filled by the human reviewer (§3.0)
  decision: "" # approved | changes_requested | rejected
  reviewers: [] # [{actor, role, model}]
  started_at: ""
  decided_at: ""
  findings: []
  acknowledged_without_comment: true # must be true when findings is empty (§3.0)
  acknowledgment_reason: "" # required when acknowledged_without_comment is true
acceptance_review_ready_at: "" # When the TASK is submitted for acceptance (§3.0)
acceptance_review: # CP-TASK-DONE-Approval — filled by the human reviewer (§3.0)
  decision: "" # approved | changes_requested | rejected
  reviewers: [] # [{actor, role, model}]
  started_at: ""
  decided_at: ""
  findings: []
  acknowledged_without_comment: true # must be true when findings is empty (§3.0)
  acknowledgment_reason: "" # required when acknowledged_without_comment is true
risk_history: [] # [{previous_class, new_class, decided_by, reason, decided_at}] — risk cannot be downgraded after the first MEM approval without formal re-review (§3.3)
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs, and section
  headings (##) stay in English (the schema). All prose — descriptions,
  acceptance criteria — goes in the project's content_language (declared
  in metaflow/LANGUAGE).

  ⚠️ TASK = WHAT, never HOW (§2.4): the TASK states the requested outcome,
  scope, exclusions, dependencies, applicable governed sources, and
  expected evidence. No architecture decisions, technologies, endpoints,
  schemas, algorithms, or implementation instructions. Those belong in the
  SPEC (how) and ADRs (constraints).

  ⚠️ THREE AND ONLY THREE TYPES (§2.4): functional (approved feature US) |
  non-functional (US-000) | test (one approved TC). BUG and hotfix are
  conditions, not types. The classification follows the PRIMARY OUTCOME,
  not the layer or technology.

  ⚠️ CP-TASK-READY-Approval (§2.4, §3.0): a TASK remains a CANDIDATE until its
  own approval is recorded (Functional Analyst for functional; Architect or
  Tech Lead for non-functional; QA Lead/QA Automation Lead/Architect/Tech
  Lead for test). Approval includes the DoR. No approval is inherited.

  ⚠️ Manifest v1 (§3.12): when creating this TASK, create its manifest JSON
  in metaflow/23-metrics/tasks/ (schema_version, task, spec_revisions: [] and
  delivery_loops: [] empty; checkpoint_approvals[] carries the origin decisions that
  already exist at this point: CP-US-Approval (functional),
  CP-TC-Approval (test), none (non-functional under US-000), plus
  CP-BUG-Approval when BUG-driven. The manifest is progressively updated
  as each lifecycle step completes). A TASK without a manifest does
  not exist. Validate against manifest-v1-task.schema.json.
-->

# US-NNN.TASK-NNN — [Descriptive title]

> **Naming convention (mandatory):** Files go in `tasks/`:
> `US-NNN.TASK-NNN-<description>.md` (functional),
> `US-000.TASK-NNN-<description>.md` (non-functional),
> `TC-NNN.TASK-NNN-<description>.md` (test).

| Field        | Value |
|--------------|-------|
| **Parent**   | [US-NNN / US-000 / TC-NNN] |
| **Type**     | [functional / non-functional / test] |
| **work_category** | [feature / refactor / infra / hardening / debt / qa_automation] |
| **service_class** | [regulatory / incident_hotfix / feature_value / debt_hardening] |
| **Demo / completion evidence** | [How to verify: curl command, screenshot, specific test] |

---

## 1. Description

[What is delivered in this TASK. One clear sentence — the WHAT, never the
HOW.]

---

## 2. Expected outcome and completion evidence

- **Objective:** [the demonstrable, measurable result]
- **Completion criterion:** [the observable result that demonstrates completion]
- **Expected evidence:** [how completion is verified]
- **Scope:** [what is covered]
- **Exclusions:** [what is explicitly NOT covered]
- **Risks / controls:** [identified risks and their controls]

---

## 3. Covered acceptance criteria

> Reference the ACs of the parent artifact — **never write new ones here**
> (§2.4, §2.6). Functional TASK: the AC ids of its parent US, quoted for
> readability. Non-functional TASK: leave `n/a` — US-000 has no ACs; the
> measurable outcome lives in section 2 and its constraints in the governing
> ADRs. Test TASK: leave `n/a` — the expected results live in the parent TC.

- `AC-N` (US-NNN) — **Given** [context], **When** [action], **Then** [expected result].
- `AC-N` (US-NNN) — **Given** [context], **When** [action], **Then** [expected result].

---

## 4. Dependencies

- **Governing sources:** [approved parent US/ACs, approved TC, approved ADR,
  approved BUG when BUG-driven, DISC/REV/AREV evidence]
- **Previous TASKs:** [TASKs that must be completed first]
- **External:** [APIs, packages, services required]

---

## 5. Does this TASK need splitting?

> Sizing target: **1 hour to 1 working day of active delivery time** — not
> a destructive boundary (§2.4, §3.2). Crossing a day boundary or adding
> Delivery Loops never splits a TASK. Split only for **independently deliverable
> outcomes** that should be governed and accepted separately.
>
> Estimate active delivery with the **AI-native estimation rule (§2.4)**:
> expected Delivery Loops × (agent generation + review budget for the risk_class)
> + SPEC review + acceptance + setup/integration overhead. **Never price code
> creation as human typing time.** Typical low/medium TASKs land in 1–4h; an
> estimate over one day usually signals manual-effort anchoring before it
> signals a split.

| Heuristic | Split? |
|-----------|--------|
| **Independent deliverables** | If it contains several independently acceptable outcomes → split |
| **Layers** | If the TASK spans domain + application + infrastructure + API as separate deliverables → separate |
| **Dependencies** | If TASK B requires TASK A to be finished → they are two distinct TASKs |
| **Testability** | If one part cannot be tested without the other → keep together; if independent → separate |
| **Demo criterion** | If you have more than one demo criterion → possible split (one TASK = one demo) |
| **Risk** | If one part is high risk and another is trivial → separate so the simple part is not blocked |

---

## 6. CP-TASK-READY-Approval

> **MetaFlow §2.4, §3.0.** This TASK remains a **candidate** until a
> qualified human records `CP-TASK-READY-Approval` (recorded in the `review`
> frontmatter block). The approval **includes the DoR**: parent approved,
> relevant ADRs approved, risks identified, context accessible, completion
> evidence defined. Approval authorizes SPEC preparation — it does **not**
> authorize technical execution by itself.

| Field | Value |
|-------|-------|
| **Approver** | Functional Analyst (functional) / Architect or Tech Lead (non-functional¹) / QA Lead, QA Automation Lead, Architect or Tech Lead (test) |
| **Role** | functional_analyst / architect / tech_lead / qa_lead / qa_automation_lead |
| **Decision** | approved / changes_requested / rejected |
| **review_ready_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **review.started_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **review.decided_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **Assigned risk** | low / medium / high / critical |
| **Findings** | [findings or acknowledged_without_comment + reason] |

> ¹ Except: the dedicated TASK of a non-functional BUG mirrors its parent
> BUG's routing — Architect/Tech Lead recommended when `severity: critical`,
> otherwise any team member — guidance, never a gate: any qualified team
> member, the TASK's own author included, may approve it at any severity (§2.16).

By signing I declare that: (a) parent and covered ACs are verifiable,
(b) relevant ADRs are approved, (c) risks are identified, (d) context is
available for the agent, (e) completion evidence is clear. Replicated in
the TASK manifest (`checkpoint_approvals[]`).

---

## 7. CP-TASK-DONE-Approval (acceptance)

> **MetaFlow §2.9, §3.0.** `Development Completed` (latest MEM
> approved) is **not** `Done`. TASK `Done` requires acceptance: a qualified
> human records `CP-TASK-DONE-Approval` (recorded in the
> `acceptance_review` frontmatter block). The acceptance review follows the
> same contract as readiness (`acceptance_review_ready_at` +
> `acceptance_review`); its timing is projected to the manifest as
> `task.acceptance.review_ready_at` / `task.acceptance.review_started_at`
> (§3.12).

| Field | Value |
|-------|-------|
| **Approver** | per `work_category` — see routing below |
| **Role** | product_owner / project_manager / tech_lead / sre / security / qa_lead / qa_automation_lead |
| **Decision** | approved / changes_requested / rejected |
| **acceptance_review_ready_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **acceptance_review.started_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **acceptance_review.decided_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **Findings** | [findings or acknowledged_without_comment + reason] |

By signing I declare that the approved Delivery Loop output satisfies the
TASK's completion evidence (§2.9, §3.0). Replicated in the TASK manifest
(`checkpoint_approvals[]`, decision `CP-TASK-DONE-Approval`).

**Acceptance routing** — who signs `CP-TASK-DONE-Approval` depends
on `work_category` (§3.11):

| work_category | Acceptance approver | Demo form |
|---------------|---------------------|-----------|
| `feature`   | PO / PM           | Business demo |
| `refactor`  | Tech Lead         | Before/after diff + test parity |
| `infra`     | Tech Lead + SRE   | Deployment evidence + perf-smoke |
| `hardening` | Tech Lead + Sec   | Fixed control + regression test |
| `debt`      | Tech Lead         | Metric/maintainability improvement |
| `qa_automation` | QA Lead / QA Automation Lead | Approved TC automated with execution evidence |

---

## 8. Manifest creation (mandatory)

> ⚠️ **MANDATORY** — When this TASK is created, also create its manifest
> JSON in `metaflow/23-metrics/tasks/` with the same name (`.md` → `.json`):
> task-level fields (`schema_version: "1.0"`,
> `task{id,type,ref,sources,generation,review_ready_at,review_started_at,acceptance{review_ready_at,review_started_at}}`)
> and empty `spec_revisions` / `delivery_loops`, with the required origin
> decisions already taken in `checkpoint_approvals[]`. A TASK without a manifest
> **does not exist** (§0). Validate against
> [`metaflow/23-metrics/manifest-v1-task.schema.json`](../../23-metrics/manifest-v1-task.schema.json);
> use the example matching the TASK type:
> [`TEMPLATE-MANIFEST-TASK.json`](../../23-metrics/TEMPLATE-MANIFEST-TASK.json) (functional),
> [`TEMPLATE-MANIFEST-TASK-NONFUNCTIONAL.json`](../../23-metrics/TEMPLATE-MANIFEST-TASK-NONFUNCTIONAL.json) (US-000),
> [`TEMPLATE-MANIFEST-TASK-TEST.json`](../../23-metrics/TEMPLATE-MANIFEST-TASK-TEST.json) (Test TASK).
> The agent appends `spec_revisions[]`, `delivery_loops[]` and
> CITL decisions as the lifecycle progresses (§3.12).

---

## 9. History

> Handoff log (§3.3): the handoff is documented here — date, outgoing
> executor, incoming executor, reason. After a recorded handoff, the
> **incoming** executor is the Dev-validator who reviews and approves the
> pending MEM of the previous Delivery Loop; the outgoing executor cannot.

| Date | Outgoing executor | Incoming executor | Reason |
|------|-------------------|-------------------|--------|
|      |                   |                   |        |
