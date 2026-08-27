# Metrics (Manifest Family v5)

**Methodology version:** 5.0

## Purpose

This folder stores the **manifest family** — one machine-readable JSON file
per **User Story**, per **Bolt**, and per **Test Case** — as the mechanical
traceability, timing, and AI-usage record of each artifact's lifecycle (see
§3.12 of [`../avenga-devflow/Avenga-DevFlow.md`](../avenga-devflow/Avenga-DevFlow.md)).

The manifest family records **only**:

1. the artifact (US, Bolt, or TC), its documentary sources and its
   AI-generation usage;
2. every material revision of the canonical SPEC (Bolt manifests), including
   its sources and AI-generation usage;
3. every V-Bounce, the SPEC revision executed, its code-generation usage,
   outcome and mandatory MEM (Bolt manifests);
4. the AITL decisions directly associated with that artifact's lifecycle;
5. the **timing of every step** (`created_at`, `review_ready_at`,
   `review_started_at`, `decided_at`) so lead times, queue times and review
   latencies are measurable.

It is **not** a duplicate project-management system, test report, deployment
log, DORA database or cost ledger. Tests, gates, DORA, deployment, incidents,
costs, AREV phases and review evidence live in their own artifacts.

Unlike `memory/` (narrative MEM documents), this folder contains
**machine-readable JSON** designed to be validated and aggregated
automatically by tooling — e.g. the sprint reports in `devflow/reports/`,
whose generator is planned with the tooling track. Recording the manifests
correctly is what makes those reports computable retroactively, so nothing
here waits on that tooling.

---

## Manifest family — the three levels

| Level | Manifest | Folder | Covers | Schema |
|-------|----------|--------|--------|--------|
| **User Story** | `US-NNN-<description>.json` | `user-stories/` | story points, approval timing, child Bolts (ACs live in the US document, not the manifest) | [`manifest-v5-us.schema.json`](./manifest-v5-us.schema.json) |
| **Bolt** | `US-NNN.BOLT-NNN-<description>.json` / `TC-NNN.BOLT-NNN-<description>.json` | `bolts/` | SPEC revisions, V-Bounces, MEMs, AITL, tokens, timing | [`manifest-v5-bolt.schema.json`](./manifest-v5-bolt.schema.json) |
| **Test Case** | `TC-NNN-<description>.json` | `test-cases/` | covered ACs, approval timing, Test Bolts | [`manifest-v5-tc.schema.json`](./manifest-v5-tc.schema.json) |

All three share `schema_version: "5.0"` — the `<major>.0` of the family:
every 4.x methodology version keeps it, and a schema change means a new
major (§3.12). `US-000`
is a container, not a feature US: it has **no** US manifest.

**One family per repository.** `schema_version` names the family that
`devflow/VERSION` declares by its **major**, so a repository never holds two
at once. Within the same major, version upgrades leave manifests untouched —
no conversion, no field added. When the methodology is upgraded **across a
major**, every manifest is re-routed and converted forward as part of the
migration — lossless: the new schema's fields arrive as `null`
where the value was never captured, and every recorded value crosses untouched
(§3.12, §5.16). A manifest declaring a `schema_version` from another family is
an unfinished migration, not legacy evidence.

---

## Files in this folder

| File | Role |
|------|------|
| [`manifest-v5-bolt.schema.json`](./manifest-v5-bolt.schema.json) | **Normative JSON Schema** (draft 2020-12) for Bolt manifests. Strict: `additionalProperties: false` — unknown fields fail validation. |
| [`manifest-v5-us.schema.json`](./manifest-v5-us.schema.json) | **Normative JSON Schema** for User Story manifests. |
| [`manifest-v5-tc.schema.json`](./manifest-v5-tc.schema.json) | **Normative JSON Schema** for Test Case manifests. |
| [`TEMPLATE-MANIFEST-BOLT.json`](./TEMPLATE-MANIFEST-BOLT.json) | Example Bolt manifest (**functional** Bolt, origin `AITL-US-Approval` recorded at creation). Copy the example matching your Bolt type and replace values. |
| [`TEMPLATE-MANIFEST-BOLT-NONFUNCTIONAL.json`](./TEMPLATE-MANIFEST-BOLT-NONFUNCTIONAL.json) | Example Bolt manifest (**non-functional** Bolt under `US-000`): `checkpoint_approvals[]` starts with **no origin decision** — US-000 has no approval lifecycle. |
| [`TEMPLATE-MANIFEST-BOLT-TEST.json`](./TEMPLATE-MANIFEST-BOLT-TEST.json) | Example Bolt manifest (**Test** Bolt under an approved `TC-NNN`): origin `AITL-TC-Approval` recorded at creation, QA-side approvers. |
| [`TEMPLATE-MANIFEST-US.json`](./TEMPLATE-MANIFEST-US.json) | Example User Story manifest. |
| [`TEMPLATE-MANIFEST-TC.json`](./TEMPLATE-MANIFEST-TC.json) | Example Test Case manifest. |

---

## Naming conventions

```
bolts/US-NNN.BOLT-NNN-<description>.json      (functional and non-functional Bolts)
bolts/TC-NNN.BOLT-NNN-<description>.json      (Test Bolts)
user-stories/US-NNN-<description>.json        (feature User Stories)
test-cases/TC-NNN-<description>.json          (Test Cases)
```

The Bolt manifest filename is the Bolt filename with `.md` replaced by
`.json`; the US and TC manifest filenames are their document filenames with
`.md` replaced by `.json`.

---

## The timing contract (every step, every level)

Every manifest records the timestamp of **each step** of its lifecycle. All
timestamps are RFC 3339 with seconds (`YYYY-MM-DDTHH:mm:ss±HH:MM`, or `Z` for
UTC) and come from the artifact's
own review contract (§3.0) and generation records — never invented, never
estimated.

| Step | Field | Where |
|------|-------|-------|
| Artifact created | `generation.created_at` | artifact object (US/Bolt/TC), SPEC revision, V-Bounce code, MEM |
| Ready for human review | `review_ready_at` | artifact object, each SPEC revision, each V-Bounce |
| Review started by the human | `review_started_at` | artifact object, each SPEC revision, each V-Bounce |
| Decision recorded | `checkpoint_approvals[].decided_at` | approval array |

Fields are **required but nullable** (`null` until the step happens), forcing
the discipline without blocking early lifecycle stages.

**Measurable times (derived at report time, never stored):**

| Metric | Derivation |
|--------|------------|
| Queue time (waiting for human) | `review_started_at` − `review_ready_at` (Time-to-Human-Review, target < 4 h, §3.0) |
| Active review time | `decided_at` − `review_started_at` |
| Total review latency | `decided_at` − `review_ready_at` (informational, no target) |
| Bolt lead time | BOLT-DONE `decided_at` − BOLT-READY `decided_at` (§3.7) |
| US lead time | last child Bolt BOLT-DONE `decided_at` − US `AITL-US-Approval` `decided_at` |
| V-Bounce cycle | MEM approval `decided_at` − code `generation.created_at` |
| AI generation time | `generation.duration_seconds` |

---

## Manifest lifecycle

### User Story (`user-stories/US-NNN-*.json`)

| Moment | Action |
|--------|--------|
| **US creation (draft)** | Copy [`TEMPLATE-MANIFEST-US.json`](./TEMPLATE-MANIFEST-US.json) and fill it — `us` (`id`, `ref`, `sources`, `generation`), `story_points: null`, empty `bolts` and empty `checkpoint_approvals`. Keep every field the template carries (*Complete from the first write*, below). |
| **US ready for review** | Set `us.review_ready_at` when the US enters review. |
| **US review** | Set `us.review_started_at`; append the `AITL-US-Approval` decision; set `story_points` to the confirmed value. |
| **Each child Bolt created** | Append the Bolt's `ref` to `bolts[]`. |

### Bolt (`bolts/*.json`)

| Moment | Action |
|--------|--------|
| **Bolt creation** | Copy the matching `TEMPLATE-MANIFEST-BOLT*.json` and fill it — `bolt` (`id`, `type`, `ref`, `sources`, `generation`), empty `spec_revisions` and empty `v_bounces`. Keep every field the template carries, `bolt.acceptance` included (*Complete from the first write*, below). `checkpoint_approvals[]` carries the **origin decisions that already exist** at this point, one per Bolt type: `AITL-US-Approval` (functional), `AITL-TC-Approval` (test), none (non-functional under US-000). A BUG-driven Bolt additionally carries `AITL-BUG-Approval`. |
| **Bolt ready / review** | Set `bolt.review_ready_at`, then `bolt.review_started_at`; append `AITL-BOLT-READY-Approval`. Only an approved Bolt may enter SPEC generation. |
| **SPEC generation or material revision** | Append one `spec_revisions[]` entry with its sources, repository baseline, generation usage and `review_ready_at`. |
| **SPEC review** | Set the revision's `review_started_at`; append the matching `AITL-SPEC-Approval` decision (with `subject.revision`). |
| **V-Bounce** | Append one `v_bounces[]` entry with its eight required fields: `number`, `spec_revision`, `git_commit`, `execution_outcome`, `code_generation`, `mem` (exactly one), `review_ready_at` and `review_started_at` — the last one `null` until the MEM review begins (§3.12). |
| **MEM review** | Append the matching `AITL-MEM-Approval` decision (with `subject.v_bounce`). |
| **Bolt acceptance** | Set `bolt.acceptance.review_ready_at`, then `bolt.acceptance.review_started_at`; append `AITL-BOLT-DONE-Approval` (the acceptance review is a second review of the same artifact — readiness and acceptance timings coexist, §3.0, §3.12). |

### Test Case (`test-cases/TC-NNN-*.json`)

| Moment | Action |
|--------|--------|
| **TC creation (draft)** | Copy [`TEMPLATE-MANIFEST-TC.json`](./TEMPLATE-MANIFEST-TC.json) and fill it — `tc` (`id`, `ref`, `sources`, `generation`), `verifies` (source Bolt + source US + covered ACs), empty `test_bolts` and empty `checkpoint_approvals`. Keep every field the template carries (*Complete from the first write*, below). |
| **TC ready / review** | Set `tc.review_ready_at`, then `tc.review_started_at`; append `AITL-TC-Approval`. |
| **Each Test Bolt created** | Append the Test Bolt's `ref` to `test_bolts[]`. |

**Complete from the first write:** every schema is
`additionalProperties: false` **and** lists its lifecycle fields as
`required`, so a **missing** field fails validation exactly like an extra
one (G23). A manifest is therefore written complete from creation, with
`null` wherever the step has not happened yet — never with the field left
out. That is what the `required`-but-nullable pair buys: `null` records
*"not yet"*, an absent field records nothing and is indistinguishable from
an oversight. The easiest to forget are the ones no lifecycle step has
touched at creation time: `review_ready_at` and `review_started_at` at every
level, and the Bolt's `acceptance` object with both of its own. Copy the
matching `TEMPLATE-MANIFEST-*.json` and the shape is already right; the
three `manifest-v5*.schema.json` files remain the contract.

**Append-only rule:** `spec_revisions[]`, `v_bounces[]`, `bolts[]`,
`test_bolts[]` and `checkpoint_approvals[]` are never rewritten. Corrections are
represented by new revisions, new V-Bounces or new decisions. Lifecycle
timestamps (`review_ready_at`, `review_started_at`) are written once, in
order; they are never backdated.

---

## Schema family v5 — structure

The normative contracts are the three `manifest-v5*.schema.json` files.
Key shared structure:

### Common (all three)
- `schema_version` — exactly `"5.0"`.
- Artifact object (`us` / `bolt` / `tc`): `id` (pattern per type), `ref`,
  `sources`, `generation`, `review_ready_at`, `review_started_at`.
- `generation` — `created_at` (ISO 8601), `created_by` (the human who
  initiated/controlled the generation — never the model name),
  `duration_seconds`, `runs[]` (tool/provider/model/tokens). Fully manual
  authoring: `created_by` populated, `runs` empty.
- `checkpoint_approvals[]` — lifecycle decisions with `checkpoint`,
  `subject`, `decision` (`approved` | `changes_requested` | `rejected`),
  `decided_by` (array of `{actor, role, model}`), `decided_at`, `comment`.

### User Story manifest
- `story_points` — confirmed Fibonacci value `1|2|3|5|8|13`, or `null` until
  `AITL-US-Approval` (§2.6).
- `bolts[]` — refs of **every** child Bolt created under this US, BUG-driven
  ones included (a BUG-driven Bolt is still a child of the feature US).
- `checkpoint_approvals[]` — `AITL-US-Approval` decisions only.

### Bolt manifest
- `bolt.type` — `functional` | `non-functional` | `test`; `id` pattern
  enforced per type.
- `spec_revisions[]` — one entry per material revision (revision ≥ 1), with
  `ref`, `sources`, `git_commit`, `generation`, `review_ready_at`,
  `review_started_at`.
- `v_bounces[]` — `number`, `spec_revision`, `git_commit`,
  `execution_outcome` (`ready_for_review` | `failed` | `blocked` |
  `cancelled`), `code_generation`, `mem` (exactly one: `ref` + `generation`),
  `review_ready_at`, `review_started_at`. Internal autonomous retries stay
  inside the V-Bounce and accumulate in `code_generation`.
- `checkpoint_approvals[]` — Bolt-lifecycle decisions only: `AITL-US-Approval`,
  `AITL-BUG-Approval`, `AITL-TC-Approval`, `AITL-BOLT-READY-Approval`,
  `AITL-SPEC-Approval` (subject requires `revision`), `AITL-MEM-Approval`
  (subject requires `v_bounce`), `AITL-BOLT-DONE-Approval`.

### Test Case manifest
- `verifies` — `source_bolt` (the exact product Bolt verified), `source_us`
  (the US under verification) and `covered_acs[]`.
  `source_us` is the **US identifier** (`US-NNN`, or `US-000` for
  non-functional TCs) — it mirrors the TC document's frontmatter; the full
  repository paths of the sources live in `tc.sources`. For a non-functional
  TC (derived from `US-000.BOLT-NNN` + governing technical sources) there
  are no ACs: `covered_acs` is then an empty array and the governing
  sources appear in `tc.sources`.
- `test_bolts[]` — refs of the Test Bolts created from this TC.
- `checkpoint_approvals[]` — `AITL-TC-Approval` decisions only.

---

## Relationship with review evidence

The manifest is the **minimal lifecycle projection** of each approval; the
authoritative review evidence lives in the governed artifact's own
machine-readable `review:` contract (§3.0):

| Artifact field | Manifest projection |
|----------------|---------------------|
| `review_ready_at` | artifact `review_ready_at` (copied) |
| `review.started_at` | artifact `review_started_at` (copied) |
| `review.reviewers` | `checkpoint_approvals[].decided_by` (each as a `human:<user>` / `agent:<id>` actor) |
| `review.decision` | `checkpoint_approvals[].decision` |
| `review.decided_at` | `checkpoint_approvals[].decided_at` |
| `review.findings` | may be summarized in the optional `comment` |

Complete findings and acknowledgment fields are **not** copied to the
manifest. A mismatch between the artifact evidence and its manifest projection
is a validation error; it does not transfer authority to the manifest.

---

## Deliberately outside manifest v5

The following remain in their own artifacts and are never stored in the
manifests:

- test and gate results, TDD evidence and modified-file lists → MEM and CI evidence;
- risk class, autonomy level and data classification → Bolt / SPEC frontmatter;
- DORA metrics, deployment, promotion, UAT and incident data → CI/CD, incidents/, tests/uat/;
- pre-calculated monetary cost;
- AREV phases, selected agents/models and approvals → AREV artifacts;
- PR lists and any state already derivable from the artifacts and AITL decisions.

---

## Derived states (never stored)

These states are defined normatively in §3.12; the table is the projection.

| Artifact | State | Derived from |
|----------|-------|--------------|
| User Story | `draft` → `approved` → `in_progress` → `completed` | US approval; first child Bolt approved; all child Bolts `Done` |
| Bolt | `In Development` / `Development Completed` / `Done` | latest V-Bounce + MEM approval / BOLT-DONE approval |
| Test Case | `draft` → `approved` → `automated` | TC approval; any Test Bolt `Done` |

These states are never duplicated as mutable manifest fields.

---

## Example flow

```
US-012 drafted → US manifest created with the document (draft, §3.12/G33)
   → US-012 approved (AITL-US-Approval) → US manifest updated
   → Bolt created in functional/bolts/ + manifest in metrics/bolts/
     (origin AITL-US-Approval already recorded)
   → AITL-BOLT-READY-Approval appended → SPEC generated → spec_revisions[1]
   → AITL-SPEC-Approval (changes_requested) → revision 2 → approved
   → V-Bounce 1 (spec_revision 2) → tests green → MEM → v_bounces[1]
   → AITL-MEM-Approval (approved) → Bolt = Development Completed
   → AITL-BOLT-DONE-Approval → Bolt = Done → US manifest reflects it
```

See the five `TEMPLATE-MANIFEST*.json` files for complete worked examples.

---

## Relationship with other folders

| Folder | Relationship |
|--------|-------------|
| `functional/user-stories/` | Defines the US → US manifest lives in `metrics/user-stories/` |
| `functional/bolts/` | Defines the Bolt → Bolt manifest lives in `metrics/bolts/` |
| `tests/test-cases/` | Defines the TC → TC manifest lives in `metrics/test-cases/` |
| `spec/` | Each canonical SPEC revision is recorded in `spec_revisions[]` |
| `memory/` | Each V-Bounce MEM is paired with a `v_bounces[]` entry |
| `reports/` | Sprint reports aggregate the whole family |
| `avenga-devflow/` | Methodology §3.12 defines this contract |

---

## Language

JSON keys, enum values, and IDs stay in **English** (the schema). Free-text
fields (`comment`) go in the project's `content_language` (see
[`devflow/README.md`](../README.md) → Language policy, §3.15).
