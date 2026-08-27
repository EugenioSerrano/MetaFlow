---
id: "MEM-260822-1726"
title: "Kit-wide v5 manifest propagation sweep (A+B+C+D) — BOLT-004"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
bolt: "US-020.BOLT-004"
spec: "SPEC-260822-1656"
spec_revision: 2
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "97125e7"
applied_adrs:
  - "devflow/adrs/ADR-008-aitl-approval-precept.md"
  - "devflow/adrs/ADR-005-removal-completeness-phrase-family-sweep.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "US-020.BOLT-004-manifest-v5-propagation-sweep.json"
diff_ref: "" # uncommitted working tree at MEM time
review_ready_at: "2026-08-22T17:26:42-03:00"
review: # HITL-MEM-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "dev_validator"}]
  started_at: "2026-08-22T17:34:40-03:00"
  decided_at: "2026-08-22T17:34:40-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Inspected the kit-wide diff (A+B+C+D), the comprehensive ADR-005 phrase-family sweep (zero residuals outside the allowlist), the §3.12 example validating GREEN against the v5 schema, four-agent sync + G-count 39x5, allowlist intact, and the rev-2 manifest. V-Bounce GREEN against rev 2. Closes the kit-wide v5 manifest propagation."
---

<!--
  LANGUAGE POLICY (§3.15): schema/headings English; prose content_language (en).
  Kit-only product surface (ADR-004); root governance records (SPEC/manifest/
  this MEM) stay on the 4.2 maintenance partition — HITL-* naming, schema 4.0.
-->

# MEM-260822-1726 — Kit-wide v5 manifest propagation sweep (BOLT-004)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | [US-020.BOLT-004](../functional/bolts/US-020.BOLT-004-manifest-v5-propagation-sweep.md) |
| **SPEC**        | [SPEC-260822-1656](../spec/SPEC-260822-1656-manifest-v5-propagation-sweep.md) revision 2 |
| **V-Bounce**    | 1 |
| **ADRs**        | ADR-008 (v5 record shape), ADR-005 (phrase-family sweep), ADR-004 (kit-only) |

---

## 1. Executive summary

This V-Bounce finished propagating the v5 manifest change across the whole kit —
the last work item of US-020 — after BOLT-001 shipped the v5 schemas and BOLT-002
aligned the core §3.12 description. It ran in two scopes within one cycle. Under
**SPEC rev 1** (reference/template tier) it renamed the approval array
(`hitl_approvals[]`→`checkpoint_approvals[]`) across the manifest reference doc,
the artifact templates and the folder READMEs (bucket A), reshaped the §3.12
embedded example + `metrics/README.md` approver prose to the v5
`{actor,role,model}`+`mode` shape so the example **validates against the v5
schema** (bucket B), and fixed the broken `manifest-v4-*.schema.json` links +
`Schema family v4` / `schema_version "4.0"` labels (bucket C). That rev-1 sweep
then surfaced a further gap — the *phrase* `Manifest family v4` / `manifest v4` /
`v4 schema/example` (distinct from the array name and the schema filenames)
persisted ~20× kit-wide, including the **core §3.12 heading itself**, the
top-level `README`/`GUARDRAILS`, `bugs/README`, `incidents/TEMPLATE-INCIDENT`,
`avenga-devflow/INDEX.md` and an agent description. Per the maintainer's
decision, **SPEC rev 2** broadened the sweep to **every `.md` under
`distribution-kit/`** with the **complete phrase family** (bucket D). The final
result is GREEN: the comprehensive ADR-005 phrase-family sweep returns **zero**
residual v4 manifest references outside the explicit allowlist, the §3.12 example
still validates GREEN against the real v5 schema, four-agent sync holds (G-count
39×5), and the change is kit-only (root framework untouched). US-020 is now fully
delivered across all four Bolts.

---

## 2. Implemented phases

### Phase A — array rename (bucket A, rev 1)
`hitl_approvals`→`checkpoint_approvals` in the 12 prose files that describe the
current manifest (manifest reference `metrics/README.md`, `TEMPLATE-BOLT/MEM/US/TC/REV`,
and the `memory/reports/reviews/tests/tests-uat/tests-test-cases` READMEs), via an
EOL-preserving scripted string replacement. The §5.16 conversion recipe and the
four agents' Upgrade-Protocol notes were left untouched (they name the v4 source).

### Phase B — approver reshape + example validation (bucket B, rev 1)
The §3.12 embedded example (Avenga-DevFlow.md) had the new array name but v4-shaped
entries with no `mode`; each entry was reshaped to `mode:"human"` +
`decided_by:[{actor:"human:<user>",role,model:null}]` (six entries, anchored by
their unique `decided_at`), and the canonical-identity line updated
(`decided_by[].user`→`decided_by[].actor`). `metrics/README.md`'s approver prose
was updated to `{actor,role,model}`. The artifact-level `review.reviewers[].user`
contract was deliberately **left `{user,role}`** (the `user`→`actor` projection is
a manifest-boundary concern, §3.12).

### Phase C — schema labels (bucket C, rev 1)
`manifest-v4-*.schema.json` links (files BOLT-001 deleted) → `manifest-v5-*`;
`Schema family v4`→v5; `schema_version "4.0"`→`"5.0"` across the reference/template
docs.

### Phase D — kit-wide phrase family (bucket D, rev 2)
The `Manifest family v4` / `Manifest v4` / `manifest v4` / `Schema v4 example` /
`v4 schemas` phrase → v5 across **every `.md` under `distribution-kit/`** (20
replacements in 12 files), with a scripted guard aborting on any `v4.2`/`sev4`
adjacency. This corrected the core §3.12 heading (`## 3.12 Manifest family v5`),
the §3.12 example label (`Schema v5 example`), the top-level `README`/`GUARDRAILS`,
`bugs/README`, `incidents/TEMPLATE-INCIDENT`, `avenga-devflow/INDEX.md`, and the
`SKILL.md` description. `Avenga-DevFlow.md` §5.16 was protected (its v4-source
references are the allowlist).

---

## 3. Files created

| File | Purpose |
|------|---------|
| _(none in the repository)_ | The sweep scripts and validation harness ran from the OS temp scratchpad (W21); not committed. Their results are transcribed in §9. |

---

## 4. Files modified

Kit product surface (all under `distribution-kit/`):

| Area | Files | Change |
|------|-------|--------|
| Manifest reference | `devflow/metrics/README.md` | A+B+C+D — array rename, approver shape, schema links/labels, title `Manifest Family v5` |
| Core methodology | `devflow/avenga-devflow/Avenga-DevFlow.md` | B (§3.12 example reshape + identity line) + D (§3.12 heading/body/example label to v5); §5.16 recipe untouched |
| Methodology index | `devflow/avenga-devflow/INDEX.md` | D — `Manifest family v5` |
| Artifact templates | `TEMPLATE-BOLT/MEM/US/TC/REV.md`, `incidents/TEMPLATE-INCIDENT.md` | A (array) + C (schema labels) + D (`Manifest v5` notes) |
| Folder READMEs | `memory/`, `reports/`, `reviews/`, `tests/`, `tests/uat/`, `tests/test-cases/`, `functional/`, `bugs/` READMEs | A (array) + C (schema labels) + D (phrase) |
| Top-level docs | `devflow/README.md`, `devflow/GUARDRAILS.md` | D — `Manifest family v5` / `manifest v5 entry|update` |
| Agents | `.agents/skills/avenga-devflow/SKILL.md` | D — frontmatter `description` `Manifest family v5` (platform frontmatter; not byte-synced across agents) |
| Governance (root, 4.2) | `spec/SPEC-260822-1656*` (rev 1→2), `metrics/bolts/US-020.BOLT-004*.json`, `functional/INDEX.md`, this MEM | lifecycle records |

---

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
| _(none)_ | | |

---

## 6. Files deleted

| File | Reason |
|------|--------|
| _(none)_ | (the v4 schema JSON files were deleted earlier, in BOLT-001) |

---

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| Broaden to kit-wide (SPEC rev 2) instead of fixing 6 in-tier + deferring | The rev-1 phrase family AND location set were both incomplete; a third partial sweep would repeat the exact anti-pattern ADR-005 exists to kill. One exhaustive pass ends the regress. |
| Scripted, EOL-preserving string replacement for the mechanical buckets | ~90 replacements across ~25 files; a deterministic script with per-file counts + a `v4.2`/`sev4` abort-guard is more reliable than dozens of hand edits, and every change was re-verified by the GREEN sweep + `git diff`. |
| Targeted per-entry Edits for the §3.12 example (bucket B) | Adding `mode` + reshaping `decided_by` is structural, not a string swap; anchoring on each entry's unique `decided_at` kept it precise and protected the surrounding JSON. |
| Keep the artifact `review.reviewers` contract `{user,role}` | §3.12 projects `user`→`actor` only at the manifest boundary; changing the artifact contract is a separate, unapproved change. |
| Allowlist: §5.16 recipe + agents' upgrade notes + `review.reviewers` + `v4.2` + `sev4` | These legitimately name the v4 source, the artifact contract, the methodology version, or an incident severity — none is a current-manifest reference. |

---

## 8. Deviations and assumptions

- **In-cycle SPEC revision (rev 1 → rev 2), finding-driven.** This V-Bounce's own
  rev-1 sweep surfaced the kit-wide `Manifest family v4` phrase gap; the SPEC was
  revised to rev 2 (kit-wide + bucket D) and re-approved before the bucket-D edits.
  The V-Bounce **completes against rev 2**; no MEM was recorded under rev 1, so
  there is **no G16 two-revision span** — rev 2 is a superset that authorises all
  of A/B/C/D.
- **Third partial-sweep finding in the US-020 chain**, now closed: BOLT-003 found
  the reference/template tier; BOLT-004 rev 1 found the `Manifest family v4`
  phrase. The lesson is recorded in the SPEC rev-2 rationale — the ADR-005 phrase
  family must enumerate every synonym of the thing being removed, not a subset.
- **Assumption (unchanged):** the artifact `review.reviewers[].user` stays
  `{user,role}` in v5 (§3.12 projection). Confirmed intact (AC-5).

---

## 9. Verification evidence

### Build / Tests
```
n/a — documentation Bolt. The deterministic checks are the sweep + the schema
validation below.
```

### Comprehensive ADR-005 phrase-family sweep — GREEN (as an absence)
```
bucket D residuals (Manifest/family/Schema/example v4, excl. v4.2 & sev4): NONE
bucket A/C residuals (manifest-v4 / Schema family v4 / schema_version "4.0"):  NONE
hitl_approvals: only in the allowlist —
  distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md  (§5.16 recipe, lines 4624/4628)
  distribution-kit/{CLAUDE.md, .agents/.../SKILL.md, .github/.../AvengaDevFlow.agent.md, .opencode/.../AvengaDevFlow.md}  (Upgrade-Protocol notes)
```
Rev-1 mechanical counts: 69 (buckets A/C + metrics B). Rev-2 (bucket D): 20 across 12 files.

### §3.12 embedded example validates against the real v5 schema — GREEN
```
§3.12 example vs manifest-v5-bolt.schema.json: GREEN (valid)
  6 entries, schema_version 5.0, mode:human, actor:human:<user>, model:null, HITL-* names preserved
core §3.12 lines: "## 3.12 Manifest family v5", "family **v5**", "Schema v5 example", "outside manifest v5"
```

### Four-agent sync + kit-only (AC-6)
```
G-count: CLAUDE 39 · SKILL 39 · AvengaDevFlow.agent 39 · AvengaDevFlow 39
"## Manifest Family v5" heading: present in all four
Agent bodies unchanged by this Bolt (only SKILL.md frontmatter description edited)
git status: only distribution-kit/ + root governance records; root framework untouched
```

### Allowlist intact (AC-5)
```
artifact review.reviewers "# [{user, role}]": preserved in 13 template files (14 occurrences)
§5.16 conversion recipe + agents' Upgrade-Protocol notes: unchanged
```

### Gates
- unit/integration, SAST/DAST/SBOM, perf, IP, PII, dep-confusion, test-first: **n/a** (documentation/internal, SPEC §9).
- hallucination-lint (links resolve; example validates against the real v5 schema),
  behavioral-reproducibility (deterministic sweep), bolt-manifest-validation
  (manifest validates GREEN vs. root v4 schema): **pass**.

### BUG V-Bounce evidence
n/a — not a BUG V-Bounce.

---

## 10. Manual interventions

None. All edits were agent-generated (scripted mechanical buckets + targeted §3.12
Edits). The human role was HITL-SPEC-Approval (rev 1 + rev 2) and the rev-2 scope
decision.

---

## 11. Evidence links

- **Diff / PR:** none yet (uncommitted; accumulates with BOLT-001/002/003).
- **Commit:** baseline `97125e7` (+ BOLT-001..004 kit changes in the working tree).
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-020.BOLT-004-manifest-v5-propagation-sweep.json`.

---

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~2h across Phases A–D (two SPEC revisions in one cycle) |
| V-Bounce number | 1 |
| Tests created | 1 deterministic schema validation (§3.12 example) + the phrase-family sweep |
| AI-generated code | 100% (docs + scripts); no human fallback |
| First-pass approval | pending (this MEM) |

---

## 13. Pending items and stubs

- [ ] On acceptance → **US-020 fully delivered** (BOLT-001/002/003/004 all Done); the v5 manifest family + its describing text, migration path and kit-wide consistency are complete.
- [ ] (Separate US) the `HITL-*`→`AITL-*` checkpoint rename across the kit.

---

## 14. HITL-MEM-Approval

> **Avenga DevFlow §2.12, §3.0.** This MEM is created by the agent with no mutable
> status and is **never self-approved**. The executing Dev-validator inspects the
> diff, the sweep + schema-validation evidence, this MEM and the manifest, and
> records `HITL-MEM-Approval` here and in the manifest's `hitl_approvals[]`.
> `approved` completes the V-Bounce and (latest MEM) marks the Bolt
> `Development Completed`; `HITL-BOLT-DONE-Approval` is still required for `Done`.

| Field | Value |
|-------|-------|
| **Reviewers (executing Dev-validator; QA/Sec/domain optional)** | eugenio.serrano |
| **Roles** | dev_validator |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-22T17:26:42-03:00` |
| **review.started_at** | `2026-08-22T17:34:40-03:00` |
| **review.decided_at** | `2026-08-22T17:34:40-03:00` |
| **Review evidence** | Kit diff (A+B+C+D), comprehensive ADR-005 sweep (§9), §3.12 example validation, four-agent sync + G-count 39×5, allowlist intact, rev-2 manifest |
| **Comments** | Approved; closes the kit-wide v5 manifest propagation |
| **Findings** | none |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | Evidence inspected as above; V-Bounce GREEN against rev 2 |
