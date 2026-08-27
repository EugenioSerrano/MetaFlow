---
id: "US-020"
title: "Manifest family v5 — record every checkpoint approval by actor and mode (AITL)"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
status: "approved"
owner: "eugenio.serrano"
unit: "v5.0 — AITL foundation"
story_points: 5
adrs:
  - "devflow/adrs/ADR-008-aitl-approval-precept.md"
  - "devflow/adrs/ADR-007-devflow-agent-identity-model.md"
  - "devflow/adrs/ADR-006-versioning-and-self-development-model.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
sources:
  - "devflow/discovery/DISC-002-devflow-agents-architecture.md"
  - "devflow/discovery/DISC-001-aitl-and-subagent-orchestration.md"
  - "devflow/adrs/ADR-008-aitl-approval-precept.md"
stakeholders: ["maintainer", "adopting-teams"]
tags: ["manifest", "aitl", "schema", "v5.0"]
review_ready_at: "2026-08-22T14:39:46-03:00"
review: # HITL-US-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "functional_analyst"}]
  started_at: "2026-08-22T15:38:08-03:00"
  decided_at: "2026-08-22T15:38:08-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved, story_points 5 confirmed. Scope validated end-to-end with the maintainer: the manifest family evolves to v5 (checkpoint_approvals[] replacing hitl_approvals[], actor+model+mode, schema_version 5.0), AND everything that DESCRIBES the manifest stays consistent — §3.12, G23, the four kit agents' manifest references, and the §5.16 conversion path (v4.0→v5.0, G36, historical HITL-* names preserved). Correctly scoped out: the §0 precept rewrite and the HITL→AITL checkpoint rename (separate US); the field name is neutral so no dependency. Kit-only (ADR-004); the safe default records exactly as today. Decomposable into candidate functional Bolts."
---

<!--
  LANGUAGE POLICY (§3.15): schema in English; prose in content_language (en).
  This US governs a v5.0 PRODUCT change (the kit's manifest family). It is
  itself authored/approved under v4.2 (ADR-006 dogfooding split): this US's
  own manifest is schema_version "4.0"; its DELIVERABLE is the kit's v5.0
  manifest schema. Kit-only edits (ADR-004); root untouched.
-->

> **Naming convention:** `US-020-manifest-aitl-evolution.md` in `user-stories/`.

# US-020 — Manifest family v5: record every checkpoint approval by actor and mode

| Field          | Value |
|----------------|-------|
| **Unit**       | v5.0 — AITL foundation |
| **ADRs**       | ADR-008 (AITL precept), ADR-007 (agent identity), ADR-006 (versioning), ADR-004 (partition) |
| **Status**     | **approved** (HITL-US-Approval 2026-08-22) |
| **Story points** | 5 (confirmed at approval — cross-cutting schema change across 3 manifest levels + templates + methodology text + conversion; never time, §2.6) |

---

**As** the Avenga DevFlow methodology (used by adopting teams), **I want** the
manifest family to record **every checkpoint approval with its actor (a human or
an AI agent) and its mode**, under a **v5.0 schema**, **so that** AITL approvals
are fully auditable and the manifest reflects the v5.0 precept (ADR-008) — while
the safe default (human-only, no config) records exactly as before.

## 1. Acceptance criteria

- **Given** the three manifest schemas (US / Bolt / TC), **When** v5 is applied,
  **Then** the approval array is **`checkpoint_approvals[]`** (replacing
  `hitl_approvals[]`) in all three, and each entry records: `checkpoint`,
  `subject`, **`mode`** (`human | virtual`), **`decided_by`** (`human:<user>`
  **or** `agent:<id>` with its `model`), `decision`, and `decided_at` (+ the
  review timings the family already carries).
- **Given** a human-only approval (the safe default), **When** it is recorded,
  **Then** `mode: human` and `decided_by: human:<user>` — semantically identical
  to today's record (no capability lost at zero config).
- **Given** the manifest change, **When** the schema is versioned, **Then**
  `schema_version` is **`"5.0"`** across the three schemas and the schema files
  are the v5 family (e.g. `manifest-v5-*.schema.json`), each retaining
  `additionalProperties: false` (a missing or extra field still fails, G23).
- **Given** the five manifest templates (`TEMPLATE-MANIFEST-*.json`), **When** v5
  ships, **Then** they reflect the v5 shape and validate against the v5 schemas.
- **Given** the methodology text, **When** v5 ships, **Then** §3.12 (Manifest
  Family) and every G23 reference describe `checkpoint_approvals[]` and
  `schema_version "5.0"`; the four agent definitions' manifest references agree
  (four-agent sync preserved, G-count unchanged).
- **Given** an existing v4.0 manifest, **When** it is migrated (at a §5.16
  upgrade), **Then** the **G36 conversion path is documented**: each
  `hitl_approvals[]` entry becomes a `checkpoint_approvals[]` entry with
  `mode: human`, its historical `HITL-*` checkpoint name **preserved** (history
  not rewritten), no recorded value invented or dropped.
- **Given** the change, **When** verified, **Then** it is **kit-only** (ADR-004;
  `git status` shows only `distribution-kit/` + governance records), a v5 sample
  manifest validates, and the checkpoint identifier value is left **neutral**
  (`checkpoint_approvals` carries no `hitl`/`aitl` in its field name — the
  HITL→AITL rename is a separate US).

> ACs are verifiable functional criteria only; non-functional constraints live in
> the ADRs (§2.7).

## 2. Bolts

| # | Bolt | Type | Layer | Description | Est. active delivery |
|---|------|------|-------|-------------|----------------------|
| 1 | US-020.BOLT-001 | functional | Documentation/Schema | The three schema files v4→v5 (`checkpoint_approvals[]`, `mode`, actor+model, `schema_version "5.0"`) + the five `TEMPLATE-MANIFEST-*.json` | ~3h |
| 2 | US-020.BOLT-002 | functional | Documentation | Methodology §3.12 (Manifest Family) + G23 references + the four agents' manifest references, aligned to v5 (four-agent sync + G-count preserved) | ~3h |
| 3 | US-020.BOLT-003 | functional | Documentation | G36 conversion path v4.0→v5.0 in §5.16 (hitl_approvals→checkpoint_approvals, mode:human, HITL-* names preserved) + a v5 sample/validation check | ~2h |

> Bolts are drafted separately (`TEMPLATE-BOLT.md`), each with its own
> `HITL-BOLT-READY-Approval`. Only after this US is approved. Plausibility (§2.6):
> 5 SP → 2–4 Bolts — the three above fit the band.

---

## 3. Business rules

| # | Rule | Condition | Action |
|---|------|-----------|--------|
| 1 | Neutral field name | always | The array is `checkpoint_approvals[]` (no `hitl`/`aitl` in the name); who signed is in `mode`/`decided_by` |
| 2 | Actor recording | any approval | `decided_by` = `human:<user>` **or** `agent:<id>` (with `model`); `mode` = `human`\|`virtual` (ADR-007/008) |
| 3 | Version bump on manifest change | schema changes | `schema_version → "5.0"` (ADR-006: changing the manifest bumps the product version) |
| 4 | History preserved | migration | v4.0 entries convert to `checkpoint_approvals[]` with `mode: human`; historical `HITL-*` names kept, never rewritten (G36) |
| 5 | Safe default unchanged | no agent config | A human approval records exactly as before — zero capability lost (ADR-008 §3.2) |

---

## 4. User flows

```mermaid
flowchart TB
    A["Checkpoint reached"] --> B{"Actor?"}
    B -->|human default| C["record: mode=human, decided_by=human:user"]
    B -->|virtual (by config)| D["record: mode=virtual, decided_by=agent:id + model"]
    C --> E["checkpoint_approvals[] (schema_version 5.0)"]
    D --> E
```

---

## 5. Impact

- **Consumes / affects:** the manifest schema is consumed by the tooling family
  — **US-007 (manifest tool)** and **US-012 (validator tool)** must handle v5
  (dependency; coordinated or as follow-up, not folded here).
- **Independent of the HITL→AITL rename US:** the field name is already neutral,
  so this US does not depend on the rename sweep.
- **Cross-cutting:** every governed artifact carries a manifest; the change is
  broad but mechanical.
- **Scope boundary:** kit-only (ADR-004). This US's own manifest stays v4.0
  (authored under the v4.2 operating methodology — ADR-006 dogfooding split).

---

## 6. SDLC tool alignment

n/a (methodology self-development).

---

## 7. HITL-US-Approval

> **Avenga DevFlow §2.6, §3.0.** This feature US remains a draft until a
> Functional Analyst records `HITL-US-Approval` (in the `review` frontmatter
> block). Only then may it be decomposed into candidate functional Bolts.

---

## 8. Manifest creation (mandatory)

Manifest created at `devflow/metrics/user-stories/US-020-manifest-aitl-evolution.json`
(`schema_version "4.0"` — operating under v4.2; `us{}`, `story_points: 5`, empty
`bolts`/`hitl_approvals`). Validates against `manifest-v4-us.schema.json` (G33).
