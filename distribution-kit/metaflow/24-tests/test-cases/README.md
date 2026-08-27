# Test Cases (independent verification contracts)

**Methodology version:** 1.1

## Purpose

This folder holds **Test Cases (`TC-NNN`)** — implementation-independent
verification contracts derived from **approved intent**, never from the
current code (§2.6.1). Each TC defines preconditions, input data, steps or
stimulus, expected results, covered ACs or technical constraints, and the
evidence needed to determine pass or fail.

> Automated tests (unit, integration, contract, e2e) live next to the
> code and are generated + executed by the AI agent in every Delivery Loop.
> See [`../README.md`](../README.md) for the boundary.

---

## What goes here

- **Verification contracts** for functional work: derived from the approved
  feature US/ACs and the exact approved functional TASK.
- **Verification contracts** for non-functional work: derived from the
  exact approved non-functional TASK plus its governing ADRs.
- **QA-Automation-ready TCs** — an approved TC may originate 1..n Test
  TASKs (`TC-NNN.TASK-NNN`) when automation has independently deliverable
  outcomes (§2.6.1).

## What does NOT go here

- Automated tests → with the code.
- UAT sign-off minutes → [`../uat/`](../uat/).
- Per-TASK acceptance (`CP-TASK-DONE-Approval`) → recorded in the
  TASK's manifest (`checkpoint_approvals[]`).

---

## Test-basis rule (MANDATORY, §2.6.1)

The expected behavior of a Test Case must be derived from **approved
intent**, never from the current implementation:

- A functional TC is based on the approved feature US/ACs and the exact
  approved functional TASK whose outcome it verifies.
- A non-functional TC is based on the exact approved non-functional TASK and
  its approved ADRs or other governed technical sources.
- A BUG-related TC also references the approved BUG and its expected
  behavior.

Existing code, tests, configuration, schemas and runtime behavior may be
inspected **only** to understand interfaces, setup, data, feasibility and
regression surface — they are **contextual evidence, not the test oracle**
(G06). When implementation behavior conflicts with the approved test basis,
the conflict is reported and routed through the BUG/02-analysis/ADR lifecycle —
never silently normalized to the code.

---

## Lifecycle

| Status | Meaning |
|--------|---------|
| `draft` | Drafted, pending `CP-TC-Approval` — cannot govern a SPEC or originate Test TASKs. |
| `approved` | `CP-TC-Approval` recorded (QA + applicable domain/technical owner). |
| `deprecated` | Replaced by an automated test or no longer relevant. |

> **Cardinality (§2.6.1):** every TC references exactly **one approved
> `source_task`**; a functional TC records one `source_us` and one or more
> `covered_acs`; a non-functional TC records `source_us: US-000` plus every
> governing ADR or other technical source.

---

## How to add a test case

1. Copy [TEMPLATE-TC.md](TEMPLATE-TC.md) to `TC-NNN-short-title.md`.
2. Fill in preconditions, steps, expected results, source TASK and
   traceability — derived from approved intent, never from current code.
3. Create the manifest — **mandatory** (the template's `Manifest creation`
   section, G33): copy
   [`TEMPLATE-MANIFEST-TC.json`](../../23-metrics/TEMPLATE-MANIFEST-TC.json) to
   `metaflow/23-metrics/test-cases/TC-NNN-short-title.json`. It must validate
   against
   [`manifest-v1-tc.schema.json`](../../23-metrics/manifest-v1-tc.schema.json):
   **a TC without a valid manifest does not exist.**
4. Stop at `CP-TC-Approval` (QA + domain owner) before the TC governs a
   SPEC or originates Test TASKs, and record that decision in the manifest.
5. Add the entry to [INDEX.md](INDEX.md).
6. Cross-link from the User Story / TASK / process it verifies.

---

## File naming

`TC-NNN-short-title.md` — e.g. `TC-001-checkout-with-coupon.md`.

---

## Language

YAML keys, status enums, and IDs stay in **English**
(the schema). Section headings and all prose — descriptions, context,
rationale, findings — go in the project's `content_language`, declared in
[`../../LANGUAGE`](../../LANGUAGE) (see §3.15). `CITL-*` codes are never
translated.
