# Changelog — Avenga DevFlow

Change log for the documentation framework itself.
This file documents the evolution of the structure, templates,
conventions and flows of Dev Flow.

> **Format:** Each entry includes date, description and affected files.
> Ordered from most recent to oldest.
>
> **Version headings** are `MAJOR.MINOR`, matching `devflow/VERSION`. Three
> historical formats coexist and are preserved as written, never rewritten:
> `[3.0.0]` and `[2.0.0]` predate the move to two-part numbering, and the
> entries below `[2.0.0]` are dated-only because they predate versioning
> altogether. A changelog is a record; correcting its past headings would
> falsify it.

---

## [1.1 kit refresh] — 2026-08-28 — §5.16: reinstalled the repo's own tree from the regenerated MetaFlow 1.1 kit

**Tree refresh with the regenerated kit.** This repository reinstalled its own
`metaflow/` tree from the regenerated distribution kit (`distribution-kit/`,
corrida 20260827-165601): the previous installed tree was renamed to
`metaflowOLD/` and every project artifact was migrated forward per §5.16.
Source and target versions are both **MetaFlow v1.1** — the refresh carries
the kit fixes (BUG-007..025) into the repo's own tree.

- **Project artifacts migrated:** 1 feature US (US-001), 30 TASKs, 31 SPECs,
  25 BUGs, 5 REVs, 4 OQs, 4 BRs, 1 PROC, 13 ID-less `02-analysis/` documents,
  32 MEMs (immutable, byte-for-byte), 3 ADRs (immutable, byte-for-byte).
- **Manifests:** 31 (30 TASK + 1 US) carried across unchanged — schemas
  identical (`manifest-v1-*.schema.json`), no conversion needed (G36).
- **INDEXes rebuilt** from the migrated files (12-functional, 11-adrs,
  13-bugs, 31-reviews, 02-analysis/*: business-context, business-risks,
  domain-model, glossary, introduction, open-questions, personas, process,
  scope, user-journeys, vision); numbering continues from the highest
  migrated ID (next free: US-002, TASK-031, ADR-004, BUG-026, REV-006,
  OQ-005, BR-005, PROC-002).
- **`AGENTS.md` merged** at the `METAFLOW:PROJECT-SECTION` marker: new
  framework block (byte-identical to the previous one) + project section
  preserved byte-for-byte from the last commit (the kit copy had emptied it).
- **`LANGUAGE` preserved:** `en`. **`VERSION`:** 1.1 (written last).
- **Framework files superseded** (README/INDEX/TEMPLATE/schemas/
  GUARDRAILS/ONBOARDING/ai-sdlc/US-000/VERSION + `01-input/` scaffolding —
  identical, no evidence files present) come from the new version; the old
  tree remains at `metaflowOLD/` until the human reviews the migration.

---

## [1.1 migration] — 2026-08-27 — This repository executed §5.16: installed Avenga DevFlow 5.1 → MetaFlow 1.1

**Second migration, to the MetaFlow lineage.** This repository upgraded its
own installed tree from **Avenga DevFlow v5.1** (`metaflowOLD/`, formerly
`devflow/`) to **MetaFlow v1.1** (`metaflow/`): the framework was installed
as `metaflow/` and every project artifact was migrated forward per §5.16.

- **Project artifacts migrated:** 1 feature US (US-001), 24 TASKs
  (renamed from `US-001.BOLT-NNN` → `US-001.TASK-NNN`), 24 SPECs, 19 BUGs,
  4 REVs, 4 OQs, 4 BRs, 1 PROC, 13 ID-less `02-analysis/` documents,
  25 MEMs (immutable, byte-for-byte), 3 ADRs (immutable, byte-for-byte).
- **Checkpoint labels re-expressed:** `AITL-*` → `CP-*` (e.g.
  `AITL-BOLT-READY-Approval` → `CP-TASK-READY-Approval`); actors,
  timestamps and decisions carried across unchanged (G36).
- **Manifests converted 5.0 → 1.0:** 24 TASK manifests
  (`bolt` → `task`, `v_bounces` → `delivery_loops`, `v_bounce` →
  `delivery_loop`) + 1 US manifest (`bolts` → `tasks`); all 25 validated
  against `manifest-v1-*.schema.json`.
- **INDEXes rebuilt** from the migrated files (12-functional, 11-adrs,
  13-bugs, 31-reviews, 02-analysis/*: open-questions, business-risks,
  process, business-context, domain-model, glossary, introduction,
  personas, scope, user-journeys, vision); numbering continues from the
  highest migrated ID (next free: US-002, TASK-025, ADR-004, BUG-020,
  REV-005, OQ-005, BR-005, PROC-002).
- **`LANGUAGE` preserved:** `en`. **`VERSION`:** 1.1 (written last).
- **Framework files superseded** (README/INDEX/TEMPLATE/schemas/
  GUARDRAILS/ONBOARDING/ai-sdlc/US-000/VERSION + old `input/` scaffolding)
  come from the new version; the old tree remains at `metaflowOLD/` until
  the human reviews the migration.

