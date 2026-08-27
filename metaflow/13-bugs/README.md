# Bugs (Confirmed Defects)

**Methodology version:** 1.1

## Purpose

This folder contains **confirmed defects** (`BUG-NNN`), documented with
observation, evidence, affected context, reproduction conditions, expected
and actual result, impact, severity, and known links (§2.16).

A BUG is **not a work authorization** — it never authorizes code by itself.
Every approved BUG receives **exactly one dedicated TASK**, which then goes
through the standard SPEC → Delivery Loop → MEM lifecycle.

Bugs feed **Defect escape rate** (§3.7.3) and, when caused by a deployment,
**D4 Change Fail Rate** after causal classification (computed at deployment
level from CI/CD and incidents, not from BUG documents).

---

## What goes here

- Defects confirmed with reproduction evidence and root-cause analysis.
- Bugs extracted from reviews (`REV-NNN`) or approved adversarial verdicts
  (`AREV-NNN`).
- Defects caught by CI gates, QA, UAT or production monitoring.
- Race conditions, logic errors, data inconsistencies.
- Regressions identified by automated test suites.

## What does NOT go here

- **Production incidents** (service disruption) → `34-incidents/`
  (`INC-NNN`). An incident *may produce* a BUG when the root cause is
  confirmed, but the incident timeline and response live there.
- **Risk of something breaking** → `33-risks/` (`RISK-NNN`).
- **Architectural decision on how to prevent** → `11-adrs/`
  (`ADR-NNN`, linked back here).

---

## Naming convention

```
BUG-NNN-short-description-in-kebab-case.md
```

---

## Lifecycle

```mermaid
flowchart LR
    START(( )) --> Draft
    Draft -->|"CP-BUG-Approval"| Approved
    Approved -->|"dedicated TASK created"| InFix["in-fix<br>(Delivery Loop: red → green)"]
    InFix -->|"MEM approved"| Fixed
    Fixed -->|"verified in review / deploy"| Closed
    Fixed -->|"regression or incomplete fix"| InFix
    Closed --> END(( ))

    style START fill:#000,stroke:#000,color:#000
    style END fill:#000,stroke:#000,color:#000
```

| Status      | Meaning |
|-------------|---------|
| **draft**   | Defect reported, pending `CP-BUG-Approval` — no TASK may be created yet. |
| **approved**| `CP-BUG-Approval` recorded (recommended: Functional Analyst for functional; Architect/Tech Lead when `severity: critical`, otherwise any team member for non-functional — guidance, never a gate: any qualified team member, the BUG's own author included, may record it at any severity). Its one dedicated TASK is created. |
| **in-fix**  | Dedicated TASK in execution: reproduction test → red evidence → fix → green, inside ONE Delivery Loop. |
| **fixed**   | Fix Delivery Loop approved (`CP-MEM-Approval`); red→green evidence recorded in the MEM. |
| **closed**  | Fix verified in a subsequent review or deploy cycle. |

> **Reopening has a boundary (§3.11).** `fixed → in-fix` is valid only while
> the TASK has **not** been accepted: an incomplete fix caught before
> `CP-TASK-DONE-Approval` is another Delivery Loop on the same TASK. Once the
> TASK is accepted, acceptance is **never revoked retroactively** — a defect
> found afterwards, including a regression of this same fix, is a **new
> `BUG-NNN`** with its own approval and its own dedicated TASK. The closed
> BUG stays closed; the new one links back to it.

`INDEX.md` reflects status: Draft / Approved + In-fix / Fixed + Closed.

---

## Bug-fix policy: strict TDD, one dedicated TASK

Every bug follows **strict TDD** and, like all work, **must go through its own
dedicated TASK** (§2.16, §3.3.1). No exceptions, not even under hotfix
pressure (§4.10). **A BUG can never be fixed under an unrelated existing
TASK** — not directly from a ticket, not as an untracked addition to another
Delivery Loop.

```
BUG (draft) → CP-BUG-Approval → exactly one dedicated TASK
  → CP-TASK-READY-Approval → one SPEC → CP-SPEC-Approval
  → ONE Delivery Loop: reproduction test (RED evidence) → fix → GREEN
  → MEM (red + green evidence) → CP-MEM-Approval
```

> **Pre-SPEC evidence gate (§3.3.1):** before generating the BUG SPEC, the
> agent verifies `CP-BUG-Approval`, the dedicated TASK's
> `CP-TASK-READY-Approval`, and the functional parent's `CP-US-Approval`
> when applicable. No checkpoint is implied by another.

```mermaid
flowchart LR
    subgraph ORIGIN["Origin"]
        O1["BUG-NNN drafted<br>(Functional Analyst / Developer / QA)"]
        O2{"CP-BUG-Approval"}
        O1 --> O2
    end

    subgraph TASK_STEP["Dedicated TASK"]
        B1["Functional BUG → TASK under<br>the affected approved feature US"]
        B2["Non-functional BUG → TASK under<br>US-000-non-functional.md"]
        B3["BUG and TASK reference each other"]
        O2 -->|"approved"| B1
        O2 -->|"approved"| B2
        B1 --> B3
        B2 --> B3
    end

    subgraph VB["ONE Delivery Loop — strict TDD"]
        V1["Reproduction test written<br>and executed → RED evidence"]
        V2["Only then: production code modified"]
        V3["Targeted + regression suites → GREEN"]
        V1 --> V2 --> V3
    end

    subgraph CLOSE["Close the loop"]
        C1["MEM records red and green<br>evidence separately"]
        C2["Manifest v1: delivery_loops[] entry"]
        C1 --> C2
    end

    B3 --> VB --> CLOSE
```

### Rules

1. **BUG first, approval before TASK.** A BUG remains `draft` until
   `CP-BUG-Approval` confirms the defect, its evidence, its nature
   (functional / non-functional) and its routing. Only then may its one
   dedicated TASK be created.
2. **Exactly one dedicated TASK per approved BUG.** Functional BUG → TASK
   under the affected approved feature US. Non-functional BUG → TASK under
   `US-000-non-functional.md`. The BUG and the TASK reference each other.
   Never reuse an unrelated TASK, never fix from a ticket.
3. **One SPEC per BUG TASK, approved before execution.** The canonical SPEC
   explicitly references the approved BUG and prescribes the single-Delivery Loop
   TDD order. It is generated only after the pre-SPEC evidence gate
   (`CP-BUG-Approval` + `CP-TASK-READY-Approval` + functional parent's
   `CP-US-Approval` when applicable, §3.3.1) and executed only after
   `CP-SPEC-Approval`.
4. **Red before fix.** Production code may not change before objective red
   evidence exists. If the defect cannot be reproduced as an automated test,
   the agent stops, creates the MEM + manifest entry with the blocker, and
   pauses — no fix applied.
5. **Green with regression.** The targeted test and all applicable
   regression suites must pass before the Delivery Loop is submitted for review.
6. **MEM records both.** Red command/result and green command/result are
   recorded separately in the Delivery Loop's MEM; the manifest records the
   Delivery Loop and its MEM reference. A BUG Delivery Loop without both pieces of
   evidence cannot receive approved `CP-MEM-Approval`.
7. **Decomposition.** If the defect contains several independently
   confirmable defects or outcomes, `CP-BUG-Approval` may request
   decomposition into independently traceable BUGs — each approved
   separately, each with its own dedicated TASK.
8. **Additional Delivery Loops are fine, never a new TASK.** Continuation on the
   next day or extra Delivery Loops (changes requested) keep the same TASK —
   elapsed time alone never splits the BUG or its TASK.
9. **Severity-based routing recommendation for non-functional BUGs — guidance,
   never a gate.** A non-functional BUG with `severity: critical` recommends
   `CP-BUG-Approval` from an Architect or Tech Lead; `severity: high`,
   `medium`, or `low` recommends **any team member**. But the recommendation
   never blocks: any qualified team member, the person who drafted it included,
   may record it at **any severity**. The dedicated
   TASK's `CP-TASK-READY-Approval` follows the same rule (§2.16).
   Functional BUGs recommend the Functional Analyst, regardless of
   severity. (The AI self-approval prohibition, G18/G24, is a separate axis.)

---

## Defect escape and Delivery Flow connection

The BUG document captures **where the defect was caught** (`detected_in`),
which feeds **Defect escape rate** (§3.7.3: defects that reached UAT/prod).

Deployment-caused production defects feed **D4 Change Fail Rate** — but Delivery Flow
is computed at **deployment level** from CI/CD deployment events joined to
deployment-caused incidents (`34-incidents/`), never from individual BUG
documents (§3.7.1). The BUG links to the incident (`incident_ref`) when one
exists.

---

## Relations to other folders

| Folder | Relation |
|--------|----------|
| `12-functional/` | The dedicated TASK lives under the affected approved feature US (functional) or `US-000-non-functional.md` (non-functional) |
| `21-spec/` | One canonical SPEC per BUG TASK, referencing the approved BUG |
| `22-memory/` | The fix Delivery Loop produces a MEM (red + green evidence) and updates the manifest |
| `23-metrics/tasks/` | Manifest family v1 `delivery_loops[]` entry; BUG never authorizes code by itself |
| `34-incidents/` | Production incident (`INC-NNN`) may produce a BUG when root cause is confirmed |
| `31-reviews/` | Bugs are often extracted from `REV-NNN` findings |
| `32-adv-reviews/` | An approved Verdict may produce a BUG; AREV is optional and stakeholder-triggered — never automatic |
| `33-risks/` | A pattern of related bugs may warrant a `RISK-NNN` entry |
| `11-adrs/` | Structural fixes may require an `ADR-NNN` |

---

## Index

See **[INDEX.md](INDEX.md)** for the full listing.

---

## Language

YAML keys, status enums, IDs, and template section headings stay in **English**
(the schema). All prose — descriptions, context, rationale, findings — goes in
the project's `content_language`, declared in [`../LANGUAGE`](../LANGUAGE)
(see §3.15).
