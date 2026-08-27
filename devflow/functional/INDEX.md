# Functional — Index

**Methodology version:** 5.0

Work definition: feature User Stories (approved at `AITL-US-Approval`),
the permanent `US-000-non-functional.md` container (no approval lifecycle),
and the three canonical Bolt types (functional / non-functional / test).
Mandatory structure: User Stories in `user-stories/`, Bolts in `bolts/`.
Integration with external SDLC tools (Azure DevOps, Jira, etc.) is team
configuration — the methodology prescribes no mechanism (see README).

---

> **Source of the next `NNN`.** Feature US numbers are sequential and claimed
> here. Highest ID in use: **US-025** → next free is **US-026**. Gaps stay
> gaps; archived IDs are never reused (§2.4).

## 🟡 Draft feature USs (pending AITL-US-Approval)

| ID | Document | Description |
|----|----------|-------------|
| US-002 | [US-002-sprints-family.md](user-stories/US-002-sprints-family.md) | Sprints family — canonical folder for sprint planning data that feeds reports |
| US-004 | [US-004-tool-clock.md](user-stories/US-004-tool-clock.md) | clock tool — repository time, not developer time |
| US-005 | [US-005-tool-identity.md](user-stories/US-005-tool-identity.md) | identity tool — one canonical human identifier |
| US-006 | [US-006-tool-indexer.md](user-stories/US-006-tool-indexer.md) | indexer tool — keep every INDEX true to its folder |
| US-007 | [US-007-tool-manifest.md](user-stories/US-007-tool-manifest.md) | manifest tool — append to the manifest family without breaking it |
| US-008 | [US-008-tool-next-id.md](user-stories/US-008-tool-next-id.md) | next-id tool — the next free sequential number |
| US-009 | [US-009-tool-reporter.md](user-stories/US-009-tool-reporter.md) | reporter tool — sprint reports from the manifest family |
| US-010 | [US-010-tool-scaffold.md](user-stories/US-010-tool-scaffold.md) | scaffold tool — create an artifact and its manifest in one step |
| US-011 | [US-011-tool-status.md](user-stories/US-011-tool-status.md) | status tool — walk the documents and report their state |
| US-012 | [US-012-tool-validator.md](user-stories/US-012-tool-validator.md) | validator tool — the compiled manifest validator that ships in devflow/bin/ |
| US-013 | [US-013-sprint-reports.md](user-stories/US-013-sprint-reports.md) | Sprint reports — generate reports at any moment, mid-sprint |
| US-017 | [US-017-tooling-distribution-contract.md](user-stories/US-017-tooling-distribution-contract.md) | Tooling distribution contract — how compiled executables ship in devflow/bin/ and survive migrations |
| US-018 | [US-018-adopter-release-notes.md](user-stories/US-018-adopter-release-notes.md) | Adopter-facing release notes — digest in the kit root |
| US-019 | [US-019-operationalize-units-family.md](user-stories/US-019-operationalize-units-family.md) | Operationalize the units/ family — UNIT-NNN records, per-environment approvals, UAT sequence |

## ✅ Approved feature USs

| ID | Document | Description |
|----|----------|-------------|
| US-025 | [US-025-mainagent-agent-lifecycle.md](user-stories/US-025-mainagent-agent-lifecycle.md) | MainAgent agent lifecycle — the Coordinator (AvengaDevFlow per tool) installs/creates/deletes DevFlow Agents: install from `agents/squad/`, create by scaffolding template+examples into squad/ (roster executor-only draft), delete-safe N:1 check; governed by ADR-013 + ADR-014 (accepted 2026-08-24). **Approved 2026-08-24, 8 SP confirmed — 5 candidate Bolts** |
| US-024 | [US-024-unified-actors-roster.md](user-stories/US-024-unified-actors-roster.md) | Unified actors roster — the team map: humans + DevFlow Agents + models, who produces (derived from role) and who approves, resolution rules, validation and **the roster as the enablement (ADR-014)**. **Delivered 2026-08-23, 5 SP — 3 Bolts Done; kept active. Re-approved revision 3 (2026-08-24, roster-as-enablement G15) — retires the AITL-enable ADR template + project-policy.yaml, adds roster.yaml + examples/; BOLT-004 (reshape) candidate** |
| US-023 | [US-023-devflow-agent-definition-and-deployment.md](user-stories/US-023-devflow-agent-definition-and-deployment.md) | DevFlow Agents — true actors: canonical definition contract, the shipped Coordinator, producer-first role charter templates and per-platform wrapper deployment. **Delivered 2026-08-23, 8 SP — 4 Bolts Done; kept active (archival deferred to a future version, maintainer decision). Re-approved revision 3 (2026-08-24, ship model + agents/ examples–squad split, G15) — AC-9/rule #7 to ADR-013 §3.9 (no pre-built wrappers, the Coordinator installs); AC-1/AC-2: `roles/` → `examples/` (shipped references) + `squad/` (live agents); BOLT-005 (the split) candidate** |
| US-020 | [US-020-manifest-aitl-evolution.md](user-stories/US-020-manifest-aitl-evolution.md) | Manifest family v5 — `checkpoint_approvals[]` by actor + mode, `schema_version 5.0` (AITL foundation) |
| US-021 | [US-021-hitl-to-aitl-evolution.md](user-stories/US-021-hitl-to-aitl-evolution.md) | HITL → AITL — concept + guardrails + schema + kit-wide identifier rename to `AITL-<CODE>-Approval` |
| US-016 | [US-016-kit-invariants-audit-tool.md](user-stories/US-016-kit-invariants-audit-tool.md) | Kit-invariants audit tool — four-agent sync, G-count, version-marker + encoding (BOM/mojibake) checks. **Approved 2026-08-23, 5 SP** — first v5-native AITL-US-Approval |
| US-022 | [US-022-actor-concept.md](user-stories/US-022-actor-concept.md) | Actor — producer + approver: the unit of identity (identity model, independence layers, open roles, safe-default) + the `actors/` folder. **Delivered 2026-08-23, 5 SP — 3 Bolts Done; kept active as the DevFlow Agents foundation** |

> Archived feature USs (US-003, US-014, US-015 — all child Bolts Done) live in
> [`user-stories/_archive/`](user-stories/_archive/).

## ⛔ Deprecated feature USs

| ID | Document | Reason |
|----|----------|--------|
| US-001 | [US-001-team-roster.md](user-stories/US-001-team-roster.md) | **deprecated (2026-08-23)** — never approved (draft); superseded by the DevFlow Agents family: US-022 (Actor concept) + US-024 (unified actors roster absorbs its ACs as a special case) |

## Permanent container (US-000)

| ID | Document | Description |
|----|----------|-------------|
| US-000 | [US-000-non-functional.md](user-stories/US-000-non-functional.md) | Non-functional container — always active, no approval lifecycle |

---

## Bolts

> **Source of the next `NNN`.** Sequential Bolt numbers are scoped to their
> parent and come from these tables (N02–N04). Check the highest `BOLT-NNN`
> under the same parent before creating a new one; archived IDs are never
> reused.

### Functional Bolts (`US-NNN.BOLT-NNN`)

| ID | Document | Parent US | State |
|----|----------|-----------|-------|
| US-020.BOLT-001 | [US-020.BOLT-001-manifest-schemas-v5.md](bolts/US-020.BOLT-001-manifest-schemas-v5.md) | US-020 | Done |
| US-020.BOLT-002 | [US-020.BOLT-002-manifest-text-and-agents.md](bolts/US-020.BOLT-002-manifest-text-and-agents.md) | US-020 | Done |
| US-020.BOLT-003 | [US-020.BOLT-003-manifest-migration-path.md](bolts/US-020.BOLT-003-manifest-migration-path.md) | US-020 | Done |
| US-020.BOLT-004 | [US-020.BOLT-004-manifest-v5-propagation-sweep.md](bolts/US-020.BOLT-004-manifest-v5-propagation-sweep.md) | US-020 | Done |
| US-021.BOLT-001 | [US-021.BOLT-001-aitl-concept-and-precept.md](bolts/US-021.BOLT-001-aitl-concept-and-precept.md) | US-021 | Done |
| US-021.BOLT-002 | [US-021.BOLT-002-aitl-guardrails-scoping.md](bolts/US-021.BOLT-002-aitl-guardrails-scoping.md) | US-021 | Done |
| US-021.BOLT-003 | [US-021.BOLT-003-aitl-schema-enum.md](bolts/US-021.BOLT-003-aitl-schema-enum.md) | US-021 | Done |
| US-021.BOLT-004 | [US-021.BOLT-004-aitl-identifier-sweep.md](bolts/US-021.BOLT-004-aitl-identifier-sweep.md) | US-021 | Done |
| US-022.BOLT-001 | [US-022.BOLT-001-actor-concept-core.md](bolts/US-022.BOLT-001-actor-concept-core.md) | US-022 | Done |
| US-022.BOLT-002 | [US-022.BOLT-002-actors-folder.md](bolts/US-022.BOLT-002-actors-folder.md) | US-022 | Done |
| US-022.BOLT-003 | [US-022.BOLT-003-actor-vocabulary-and-agents-sweep.md](bolts/US-022.BOLT-003-actor-vocabulary-and-agents-sweep.md) | US-022 | Done |
| US-023.BOLT-001 | [US-023.BOLT-001-devflow-agent-contract-and-charters.md](bolts/US-023.BOLT-001-devflow-agent-contract-and-charters.md) | US-023 | Done |
| US-023.BOLT-002 | [US-023.BOLT-002-wrapper-generator-and-parity.md](bolts/US-023.BOLT-002-wrapper-generator-and-parity.md) | US-023 | Done |
| US-023.BOLT-003 | [US-023.BOLT-003-wrapper-deployment.md](bolts/US-023.BOLT-003-wrapper-deployment.md) | US-023 | Done |
| US-023.BOLT-004 | [US-023.BOLT-004-spawn-smoke-test.md](bolts/US-023.BOLT-004-spawn-smoke-test.md) | US-023 | Done |
| US-023.BOLT-005 | [US-023.BOLT-005-agents-examples-squad-split.md](bolts/US-023.BOLT-005-agents-examples-squad-split.md) | US-023 | Done |
| US-024.BOLT-001 | [US-024.BOLT-001-roster-schema-and-validation.md](bolts/US-024.BOLT-001-roster-schema-and-validation.md) | US-024 | Done |
| US-024.BOLT-002 | [US-024.BOLT-002-aitl-enable-adr-template.md](bolts/US-024.BOLT-002-aitl-enable-adr-template.md) | US-024 | Done |
| US-024.BOLT-003 | [US-024.BOLT-003-us001-absorption.md](bolts/US-024.BOLT-003-us001-absorption.md) | US-024 | Done |
| US-024.BOLT-004 | [US-024.BOLT-004-roster-as-enablement-reshape.md](bolts/US-024.BOLT-004-roster-as-enablement-reshape.md) | US-024 | Done |
| US-025.BOLT-001 | [US-025.BOLT-001-mainagent-lifecycle-body.md](bolts/US-025.BOLT-001-mainagent-lifecycle-body.md) | US-025 | Development Completed (V-Bounce 1 MEM approved 2026-08-24; acceptance batched with the US-025 closure) |
| US-025.BOLT-002 | [US-025.BOLT-002-per-platform-lifecycle.md](bolts/US-025.BOLT-002-per-platform-lifecycle.md) | US-025 | Development Completed (V-Bounce 1 MEM approved 2026-08-24 — AC-9 complete; acceptance batched with the US-025 closure) |
| US-025.BOLT-003 | [US-025.BOLT-003-delete-safe-consistency.md](bolts/US-025.BOLT-003-delete-safe-consistency.md) | US-025 | Development Completed (V-Bounce 1 MEM approved 2026-08-24 — AC-4 covered; acceptance batched with the US-025 closure) |
| US-025.BOLT-005 | [US-025.BOLT-005-kit-g07-scoping.md](bolts/US-025.BOLT-005-kit-g07-scoping.md) | US-025 | Development Completed (V-Bounce 1 MEM approved 2026-08-24 — REV-005 F-02 closed at six surfaces; acceptance batched with the US-025 closure) |
| US-025.BOLT-004 | [US-025.BOLT-004-lifecycle-pilot.md](bolts/US-025.BOLT-004-lifecycle-pilot.md) | US-025 | In Development (AITL-BOLT-READY-Approval + SPEC-260824-1502 approved 2026-08-24 — the pilot awaiting execution) |
| US-025.BOLT-006 | [US-025.BOLT-006-copilot-platform-verification-fixes.md](bolts/US-025.BOLT-006-copilot-platform-verification-fixes.md) | US-025 | Done (AITL-BOLT-DONE-Approval 2026-08-25 — the Copilot Coordinator spawn tool + the execution-evidence rule + the VERIFICATION.md Copilot-row batch; AC-4 spawn probe passed live) |
| US-025.BOLT-007 | [US-025.BOLT-007-kit-self-containment-f14-fix.md](bolts/US-025.BOLT-007-kit-self-containment-f14-fix.md) | US-025 | Done (AITL-BOLT-DONE-Approval 2026-08-25 — BUG-005 fix: the F-14 finding reference removed from VERIFICATION.md, TDD red/green; kit self-containment restored) |

### Non-functional Bolts (`US-000.BOLT-NNN`)

| ID | Document | State |
|----|----------|-------|
| US-000.BOLT-007 | [US-000.BOLT-007-rev002-v5-kit-consistency-remediation.md](bolts/US-000.BOLT-007-rev002-v5-kit-consistency-remediation.md) | Done |
| US-000.BOLT-008 | [US-000.BOLT-008-adr009-actor-identity-grammar-sweep.md](bolts/US-000.BOLT-008-adr009-actor-identity-grammar-sweep.md) | Done |
| US-000.BOLT-009 | [US-000.BOLT-009-adr010-hitl-vocabulary-purge.md](bolts/US-000.BOLT-009-adr010-hitl-vocabulary-purge.md) | Done |
| US-000.BOLT-010 | [US-000.BOLT-010-severity-agnostic-bug-approval.md](bolts/US-000.BOLT-010-severity-agnostic-bug-approval.md) | Done |
| US-000.BOLT-011 | [US-000.BOLT-011-kit-self-containment.md](bolts/US-000.BOLT-011-kit-self-containment.md) | Done |
| US-000.BOLT-012 | [US-000.BOLT-012-kit-consistency-residue.md](bolts/US-000.BOLT-012-kit-consistency-residue.md) | Done |
| US-000.BOLT-013 | [US-000.BOLT-013-version-marker-sweep.md](bolts/US-000.BOLT-013-version-marker-sweep.md) | Done |
| US-000.BOLT-014 | [US-000.BOLT-014-input-scaffolding-evidence-clarification.md](bolts/US-000.BOLT-014-input-scaffolding-evidence-clarification.md) | Done |
| US-000.BOLT-015 | [US-000.BOLT-015-version-bump-5-1-sweep.md](bolts/US-000.BOLT-015-version-bump-5-1-sweep.md) | Done |
| US-000.BOLT-017 | [US-000.BOLT-017-english-commit-messages-readme.md](bolts/US-000.BOLT-017-english-commit-messages-readme.md) | Done |

### Test Bolts (`TC-NNN.BOLT-NNN`)

| ID | Document | Parent TC | State |
|----|----------|-----------|-------|
| —  | —        | —         | —     |

> State is derived, never stored in the manifest: `In Development` ·
> `Development Completed` (latest MEM approved) · `Done`
> (`AITL-BOLT-DONE-Approval`). Candidate Bolts awaiting
> `AITL-BOLT-READY-Approval` are listed with state `candidate`.

> Archived Bolts (US-000.BOLT-001..006, US-003.BOLT-001, US-014.BOLT-001..003,
> US-015.BOLT-001 — all Done) live in [`bolts/_archive/`](bolts/_archive/).

---

## ⛔ Deprecated

| ID | Document | Status |
|----|----------|--------|
| US-000.BOLT-016 | [US-000.BOLT-016-hitl-aitl-doc-vocabulary-normalization.md](bolts/US-000.BOLT-016-hitl-aitl-doc-vocabulary-normalization.md) | **deprecated (2026-08-23)** — pre-SPEC inventory (1585 `HITL-` / 151 files) showed the maintainer partition can't be scrubbed of HITL: bulk is G36-protected (MEM/ADR/`_archive`) or subject-matter (US-021, REV-001, ADR-010, the `aitl-*` family). Reads as AITL per §5.16 `AITL⊇HITL`; manifests + framework already pure v5. `AITL-BOLT-READY-Approval` stands as history; no SPEC/V-Bounce |

---

**Last updated:** 2026-08-25 · **REV-006 APPROVED (the Copilot adopter smoke test — 2 Major · 7 Minor + 9 Compliant) — routed: US-025.BOLT-006 created (candidate) + evidence attached to REV-005's destinations** · BOLT-004 + BOLT-005 DONE (the roster-as-enablement reshape + the agents/ examples–squad split — executed, MEM-approved ×3, accepted, and field-proven by the adopter smoke test, REV-005 approved) · ADR-014 accepted (supersedes ADR-008 with carry-forward) · ADR-013 accepted (lifecycle + ship model) · US-023/US-024 re-approved rev 3 · US-025 approved (8 SP — its 5 Bolts are the next work, with REV-005 as evidence) · MEM-260823-1828 approved (BOLT-003 V-Bounce 4) · **US-024 DELIVERED (2026-08-23 — 3 Bolts Done, kept active)** · **US-023 DELIVERED (2026-08-23 — 4 Bolts Done, kept active)** · US-024 approved (2026-08-23, 5 SP — the team map roster; re-approved Modelo B) · US-023 approved (2026-08-23, 8 SP — DevFlow Agents as true actors, producer-first charters; re-approved delivered-state) · **US-022 delivered (2026-08-23 — 3 Bolts Done; kept ACTIVE as the DevFlow Agents foundation — archival reverted and deferred to a future version/branch, maintainer decision)** · US-022 re-approved (2026-08-23 — producer+approver reframe; SPEC-1335/1336/1337 rev 2; BOLT-001 V-Bounces 1-3 + BOLT-002 V-Bounces 1-2 + BOLT-003 V-Bounces 1-2 executed) · US-022/023/024 drafted (2026-08-23 — DevFlow Agents family: Actor concept / definition+deployment / unified actors roster), US-001 deprecated (absorbed by US-024) · US-016 approved (2026-08-23, 5 SP — first v5-native AITL-US-Approval; +encoding/BOM invariant) · migrated to v5.0 (2026-08-23, §5.16): REV-004 closed, BOLT-007..015 + US-020/021 Bolts Done, US-000.BOLT-014 Done (BUG-004), US-000.BOLT-015 Done (5.1 bump), US-000.BOLT-016 deprecated, 15 draft USs + US-016/020/021 approved
