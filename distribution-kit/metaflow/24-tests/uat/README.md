# UAT (User Acceptance Testing — per Unit / Milestone)

**Methodology version:** 1.1

> ⛔ **DORMANT / RESERVED.** The UNIT/UAT approval-and-release layer was
> **removed from the active flow in the previous lineage** — `CP-UAT-Approval` is **not an
> active checkpoint** in this release. The governed flow ends at TASK
> acceptance (`CP-TASK-DONE-Approval`); release and customer acceptance
> follow the adopting team's own process. This folder and its template are kept
> **dormant** for a redesigned model planned in a future version. The
> text below describes the future (reserved) UAT process, not an active gate.

## Purpose

This folder records the **UAT minutes** for checkpoint
**`CP-UAT-Approval`** (MetaFlow §3.0). UAT validates the full scope
of a **Unit** or **Milestone** against the business acceptance criteria
derived from [`../../02-analysis/`](../../02-analysis/) (vision outcomes, process
rules, domain invariants), with explicit stakeholder sign-off.

It is the **human close** of the full cycle: not just "TASK accepted" but
"a coherent slice of value delivered and accepted by the business".

**Sequence (§3.11, §4.6–§4.8):** UAT runs on a Unit that is technically
approved and deployed in staging — the staging `CP-UNIT-Approval` is a
**precondition** of `CP-UAT-Approval`. Once UAT passes, it is a
**precondition** of the production `CP-UNIT-Approval` and release:
staging UNIT → UAT → production UNIT.

> `CP-UNIT-Approval` is **reserved** (pending `units/` governance, §3.11
> entry 14): the sequence above is the intended rule and becomes blocking
> once the Unit recording artifact exists. In the previous lineage this whole layer is
> **dormant/reserved** (see the banner above) — not an active checkpoint.

> UAT lives in `24-tests/` (not in `02-analysis/`) because it is a
> *verification artifact*. The *acceptance criteria themselves* are
> derived upstream in analysis (vision + business-context + domain-model
> + process) and on each User Story in [`../../12-functional/`](../../12-functional/).

---

## What goes here

- One `UAT-NNN-<description>.md` per UAT session (N21 naming).
- Results of every AC executed.
- List of agreed adjustments → new TASKs.
- Stakeholder sign-off (name + date) — `CP-UAT-Approval`.

## What does NOT go here

- Automated tests → live with the code.
- Per-TASK acceptance (`CP-TASK-DONE-Approval`) → recorded in the
  TASK's manifest (`checkpoint_approvals[]`).
- Technical decisions → `11-adrs/`.

---

## How to draft with AI

Before the UAT session:

1. Ask the agent to read the Unit's TASKs (their MEMs and manifests) and
   the relevant [`../../02-analysis/process/`](../../02-analysis/process/) and
   [`../../02-analysis/vision/`](../../02-analysis/vision/) files.
2. Ask for a **draft AC list** mapped to vision outcomes and process rules.
3. The facilitator validates and locks the AC list before the session.

During the session, fill the template live. Afterwards, the UAT minutes in
`24-tests/uat/` are the evidence of `CP-UAT-Approval` — the TASK manifest
deliberately carries **no** UAT data (§3.12).

---

## Index

See **[INDEX.md](INDEX.md)** for the UAT listing.

---

## Lifecycle

| Status | Meaning |
|--------|---------|
| `draft` | AC list prepared, session not yet held |
| `approved` | All ACs passed, stakeholders signed off (`CP-UAT-Approval`) |
| `approved-with-observations` | Passed with minor adjustments → new TASKs created |
| `rejected` | Critical ACs failed → rework required before re-test |

> **Status vs decision (§3.0):** `review.decision` uses the universal
> review-contract enum `approved | changes_requested | rejected` — UAT has
> no exemption. `approved-with-observations` is a **document status**, not
> a decision value: it is the lifecycle label for `review.decision:
> approved` with non-empty `findings[]`, where every finding routes to a
> new TASK.

---

## Language

YAML keys, status enums, IDs, and template section headings stay in **English**
(the schema). All prose — descriptions, context, rationale, findings — goes in
the project's `content_language`, declared in
[`../../LANGUAGE`](../../LANGUAGE) (see §3.15).
