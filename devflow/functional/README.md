# Functional (Work Definition)

**Methodology version:** 5.1

## Purpose

This folder contains the **work definition** artifacts: User Stories and
Bolts that define WHAT must be delivered, BEFORE deciding how to implement
it (→ Spec).

A feature User Story captures business rules, acceptance criteria and
expected behaviour. It does not define implementation (→ Spec).
The folder name reflects the location of User Stories and Bolt work
definitions; it does **not** imply that every Bolt has a functional outcome
or Functional Analyst ownership (§5.9).

### Key role in the flow

Functional documents are the **primary source** for creating Specs.
Each User Story contains its **Bolts** already defined and prioritised, so
that when a Spec is generated the team (or AI agent) can take approved
stories and Bolts directly as unambiguous input.

```
Origin (US | BUG | TC | DISC | REV | AREV | ADR)
  → approved origin → BOLT (AITL-BOLT-READY-Approval)
  → SPEC (AITL-SPEC-Approval) → V-Bounce → MEM + manifest
```

Reference: Avenga DevFlow §2.4, §2.6, §3.2, §3.11.

---

## The three canonical Bolt types

| Type | Parent | Created by | AITL-BOLT-READY-Approval owner | Delivers |
|------|--------|-----------|---------------------------|----------|
| **functional** | An approved feature `US-NNN` | Functional Analyst | Functional Analyst | A slice of user-/business-visible behavior covering identified ACs |
| **non-functional** | The permanent `US-000-non-functional.md` container | Developer, Architect, or Tech Lead | Architect or Tech Lead¹ | A demonstrable technical outcome (debt, refactor, hardening, infra, tooling) |
| **test** | One approved `TC-NNN` | QA / QA Automation Engineer | QA Lead, QA Automation Lead, Architect, or Tech Lead | QA Automation code for exactly one approved TC (`TC-NNN.BOLT-NNN`) |

> ¹ Except: the dedicated Bolt of a non-functional BUG mirrors its parent
> BUG's routing — Architect/Tech Lead recommended when `severity: critical`,
> otherwise any team member — guidance, never a gate: any qualified team
> member, the Bolt's own author included, may approve it at any severity (§2.16).

> BUG and hotfix are **conditions, not types** — a BUG-driven or hotfix Bolt
> remains functional or non-functional (§3.8).

### Orthogonal taxonomies (never confuse with Bolt type)

| Dimension | Field | Values |
|-----------|-------|--------|
| Bolt type | `bolt_type` | `functional` · `non-functional` · `test` — parentage and core AITL routing |
| Work category | `work_category` | `feature` · `refactor` · `infra` · `hardening` · `debt` · `qa_automation` — reporting and acceptance routing |
| Service class | `service_class` | `regulatory` · `incident_hotfix` · `feature_value` · `debt_hardening` — priority and capacity |

`feature` uses `bolt_type: functional`; `refactor/infra/hardening/debt` use
`bolt_type: non-functional` (under US-000); `qa_automation` uses
`bolt_type: test` (under an approved TC).

---

## What documents belong here?

- **Feature User Stories (US)** with acceptance criteria (Given/When/Then) —
  approved at `AITL-US-Approval`.
- **The permanent `US-000-non-functional.md` container** — no approval
  lifecycle.
- **Bolts** — atomic decomposition of work into implementable units
  (sizing: 1 hour to 1 working day of **active delivery time**).
- Business rules and functional constraints.
- User / operator flows.
- State definitions and transitions at the functional level.
- Interaction requirements (UI controls, indicators).

---

## Organisation and naming convention

The folder follows a **mandatory structure** with two subfolders:

| Subfolder | Contains | Naming convention | Example |
|-----------|----------|-------------------|---------|
| `user-stories/` | Feature USs + `TEMPLATE-US.md` + `US-000-non-functional.md` | `US-NNN-<description>.md` | `US-001-payment-processing.md` |
| `bolts/` | Bolts + `TEMPLATE-BOLT.md` | `US-NNN.BOLT-NNN-<description>.md` · `US-000.BOLT-NNN-<description>.md` · `TC-NNN.BOLT-NNN-<description>.md` | `US-001.BOLT-003-auth-endpoint.md` |

> **The parent prefix (`US-NNN` / `TC-NNN`) is mandatory** for traceability
> across the entire methodology (ADRs, SPECs, MEMs, BUGs, Bolt manifests).
> The dot notation (`US-NNN.BOLT-NNN`) visually separates the parent from
> the Bolt number. Descriptions use kebab-case. `BOLT-NNN` is sequential
> within its direct parent.

### US-000 — Non-functional container

`US-000-non-functional.md` is the **permanent traceability parent for every
Bolt whose primary outcome is non-functional**: infrastructure, refactors,
hardening, CI/CD, dependency upgrades, database maintenance, developer
tooling (§3.2).

**Scaling (§2.6, §3.2, §5.4):** US-000 accumulates all non-functional Bolts of the
project. To keep it navigable as it grows, group the `INDEX.md` listing by
`work_category` (`infra` / `refactor` / `hardening` / `debt` — never
`qa_automation`, which is test-only and belongs to a TC, §3.8);
`Done` Bolts with their complete package (Bolt + SPEC +
MEMs) are moved to the folder's `_archive/` subfolder by the standard
archiving mechanism (§5.4) — periodically, manually, without rewriting
references (IDs stay immutable). No sub-Bolt-types or internal US hierarchy
are introduced — the container remains flat and its Bolts individually
approved.

**Why US-000 exists:** every Bolt must have a parent. Without US-000,
technical work would have no governed home and would bypass Bolt
traceability.

**Rules (§2.6, §3.2):**
- US-000 is **always active** — it never closes.
- US-000 is a **container, not an actual User Story**: it has **no
  Acceptance Criteria, approval status, approver, or AITL checkpoint**.
- It is **not a substitute for approved ADRs or quality gates**.
- Every US-000 Bolt requires its own technical `AITL-BOLT-READY-Approval` by an
  Architect or Tech Lead and follows the full SPEC → V-Bounce → MEM →
  manifest lifecycle.
- If in doubt, classify by **primary outcome** (§2.4): business-visible
  behavior → feature US; technical outcome → US-000.
- Non-functional BUGs get their dedicated Bolt under US-000 (after
  `AITL-BUG-Approval`).

See [`user-stories/US-000-non-functional.md`](user-stories/US-000-non-functional.md).

---

## Integration with external SDLC tools (out of scope)

Avenga DevFlow is **agnostic about mechanisms and products**: it prescribes
no MCP server, SDLC tool or sync product — the same way it prescribes no
agent tool or model (§3.13). Integration with external lifecycle tools
(Azure DevOps, Jira, GitHub Projects, or any other) is **team
configuration**: each team builds it as it prefers, and the methodology
neither ships nor endorses a mechanism. Nothing in `devflow/` depends on
such an integration.

Until a team builds one, `INDEX.md` is updated manually and remains the
source of the next `NNN` (§5.15).

---

## User Story structure

The authoritative structure is
[`user-stories/TEMPLATE-US.md`](user-stories/TEMPLATE-US.md); this is what it
contains:

- **Frontmatter** — id, title, date, status, owner, `story_points`,
  stakeholders and traceability.
- **1. Acceptance criteria** — verifiable conditions of completeness
  (Given/When/Then).
- **2. Bolts** — decomposition into atomic work units (3 types, §2.4).
- **3. Business rules** — domain constraints and conditions.
- **4. User flows** — interaction sequences, main and alternative scenarios.
- **5. Impact** — affected modules, dependencies, risks.
- **6. SDLC tool alignment** — associated Work Items, Sprint, Board.
- **7. `AITL-US-Approval`** — the checkpoint that turns the draft into an
  approved US that may be decomposed.
- **8. Manifest creation (mandatory)** — copy
  [`TEMPLATE-MANIFEST-US.json`](../metrics/TEMPLATE-MANIFEST-US.json) to
  `devflow/metrics/user-stories/US-NNN-<description>.json`. It must validate
  against
  [`manifest-v5-us.schema.json`](../metrics/manifest-v5-us.schema.json):
  under **G33**, a US without a valid manifest does not exist. The same rule
  applies to every Bolt (the `Manifest creation (mandatory)` section of
  `TEMPLATE-BOLT.md`).

Problem context, current situation and mockups belong in `analysis/`
(`business-context/`, `user-journeys/`, `ui/` for the surfaces, patterns and
states an AC points at, and `input/ui-ux/` for the raw material) and are
referenced from the US, not restated in it.

### Diagrams and visual elements

Use **Mermaid** for all diagrams, charts and any other visual element
(no ASCII art or embedded images).

---

## Lifecycle

### Feature User Story status

| Status | Meaning |
|--------|---------|
| **draft** | US created but not yet approved. |
| **approved** | `AITL-US-Approval` recorded (Functional Analyst) — ready for Bolt decomposition. |
| **deprecated** | Removed from scope (product decision, priority change). Kept as reference. |

> **US-000 has no status lifecycle** — it is a permanent container, so it sits
> outside the table above. Its frontmatter carries `status: "active"`, a
> deliberate marker meaning "this container is open and accepting Bolts",
> **not** a member of the feature-US enum: US-000 has no
> `AITL-US-Approval`, so it can never be `draft` or `approved`, and it never
> closes, so it can never be `deprecated`. Any validator reading US statuses
> must special-case `US-000` (§2.6, §3.2).

### Bolt status

| Status | Meaning |
|--------|---------|
| **candidate** | Drafted, pending `AITL-BOLT-READY-Approval`. |
| **approved** | `AITL-BOLT-READY-Approval` recorded — may enter SPEC preparation. |
| **deprecated** | Removed from scope. Kept as reference. |

Bolt development state (`In Development` / `Development Completed` / `Done`)
is **derived** from the manifest approvals, never stored as a Bolt field
(§3.12).

### INDEX grouping

INDEX.md groups artifacts by state, earliest state first (§3.15): 🟡 Draft
feature USs (pending `AITL-US-Approval`) / ✅ Approved feature USs /
Permanent container (US-000, no state) / ⛔ Deprecated, plus the Bolts
section (state tracked in each Bolt's manifest approvals, §3.12).

---

## Document index

See **[INDEX.md](INDEX.md)** for the full listing.

---

## Language

YAML keys, status enums, and IDs stay in **English**
(the schema). Feature User Story section headings and all prose —
descriptions, context, rationale, findings — go in the project's
`content_language`; Bolt section headings stay in English. Declared in
[`../LANGUAGE`](../LANGUAGE) (see §3.15).
