---
id: "MEM-260822-1647"
title: "v4.0→v5.0 manifest conversion in §5.16 + validating worked example (BOLT-003)"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
bolt: "US-020.BOLT-003"
spec: "SPEC-260822-1622"
spec_revision: 2
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "97125e7"
applied_adrs:
  - "devflow/adrs/ADR-008-aitl-approval-precept.md"
  - "devflow/adrs/ADR-006-versioning-and-self-development-model.md"
  - "devflow/adrs/ADR-005-removal-completeness-phrase-family-sweep.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "US-020.BOLT-003-manifest-migration-path.json"
diff_ref: "" # uncommitted working tree at MEM time
review_ready_at: "2026-08-22T16:47:37-03:00"
review: # HITL-MEM-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "dev_validator"}]
  started_at: "2026-08-22T16:50:20-03:00"
  decided_at: "2026-08-22T16:50:20-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Inspected the kit diff (§5.16 + the four agents), the AC-4 schema-validation output (GREEN good / RED bad / RED v4-under-v5), four-agent byte-sync + G-count 39x5, and the rev-2 manifest. V-Bounce GREEN against the rev-2 AC; the kit-wide sweep is correctly routed to US-020.BOLT-004."
---

<!--
  LANGUAGE POLICY (§3.15): schema/headings English; prose content_language (en).
  Kit-only product surface (ADR-004); root governance records (SPEC/manifest/
  this MEM) stay on the 4.2 maintenance partition — HITL-* naming, schema 4.0.
-->

# MEM-260822-1647 — v4.0→v5.0 manifest conversion in §5.16 (BOLT-003)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | [US-020.BOLT-003](../functional/bolts/US-020.BOLT-003-manifest-migration-path.md) |
| **SPEC**        | [SPEC-260822-1622](../spec/SPEC-260822-1622-manifest-conversion-v5.md) revision 2 |
| **V-Bounce**    | 1 |
| **ADRs**        | ADR-008 (record shape), ADR-006 (version/migration), ADR-005 (sweep), ADR-004 (kit-only) |

---

## 1. Executive summary

This V-Bounce documented, in the kit's §5.16 Methodology Upgrade Protocol, **how a
manifest converts from `schema_version "4.0"` to `"5.0"`** when a project (or the
root) later upgrades to v5.0 — the last piece of US-020 that BOLT-001 (schemas) and
BOLT-002 (description) deliberately left for this Bolt. The `4.0`→`5.0` recipe was
added to `Avenga-DevFlow.md` §5.16 alongside the existing `3.0`→`4.0` example
(rename `hitl_approvals[]`→`checkpoint_approvals[]`; per-entry `mode:"human"`;
`decided_by` `{user,role}`→`{actor:"human:<user>",role,model:null}`; historical
`HITL-*` names **preserved** under G36; `schema_version "5.0"`), the reconstruction
table row was updated, and the four platform agents' Upgrade-Protocol conversion
lines were aligned byte-identically. The rule was proven correct with a **worked v4
manifest converted by the recipe that validates GREEN against the real v5 Bolt
schema** (BOLT-001), while a fabricated non-conforming variant is rejected RED. The
outcome is GREEN against the narrowed rev-2 acceptance criteria; there were **no
build/test suites** (documentation Bolt) beyond the schema validation. One material
surprise drove a SPEC revision: AC-3's original *kit-wide* absence assertion
surfaced that the v5 manifest change was only **partially propagated** by BOLT-001/002
— the manifest reference doc, several templates and folder READMEs are still on v4.
That finding is out of this Bolt's scope; AC-3 was narrowed (rev 2) to this Bolt's
edited surface and the kit-wide sweep was routed to a new **US-020.BOLT-004**.

---

## 2. Implemented phases

### Phase A — §5.16 conversion recipe (Avenga-DevFlow.md)

Added a `4.0`→`5.0` conversion paragraph immediately after the existing `3.0`→`4.0`
worked example in the §5.16 lossless-conversion narrative: the approval array is
renamed, each entry gains a `mode` (`"human"` — every v4 approval was a human;
agents did not exist in v4) and a richer approver (`{user,role}` →
`{actor:"human:<user>", role, model:null}`), historical `HITL-*` checkpoint names
are preserved verbatim (G36 — never rewritten to `AITL-*`), and `schema_version`
becomes `"5.0"`. The §5.16 reconstruction table row for the approval array was
updated from `hitl_approvals[]` to `checkpoint_approvals[]` with the actor
projection note (reviewers as `human:<user>` actors, `mode: human`). This mirrors
the same lossless discipline the `3.0`→`4.0` example already illustrates.

### Phase B — the four agents' Methodology Upgrade Protocol

Applied two byte-identical edits to each of the four platform agent definitions
(`CLAUDE.md`, `.agents/skills/avenga-devflow/SKILL.md`,
`.github/agents/AvengaDevFlow.agent.md`, `.opencode/agents/AvengaDevFlow.md`): (1)
a one-line `4.0`→`5.0` note inserted into the conversion paragraph (rename +
`mode:"human"` + `{user,role}`→`{actor:"human:<user>",role,model:null}` + preserved
`HITL-*`, G36); (2) the reconstruction line `the review: contract →
hitl_approvals[]` updated to `checkpoint_approvals[]` (reviewers as `human:<user>`
actors, `mode: human`). Byte-sync verified afterward (both edited lines appear 4×
identically; G-count 39 across all four).

### Phase C — verification (GREEN)

Built the AC-4 worked example: a realistic v4 Bolt manifest
(`hitl_approvals[]`, `decided_by:[{user,role}]`, `HITL-*` checkpoints incl. SPEC
with `subject.revision` and MEM with `subject.v_bounce`), converted by the §4 rule
into a v5 manifest, and validated with `jsonschema` (draft 2020-12) against the real
`manifest-v5-bolt.schema.json`. The converted manifest validates GREEN; a fabricated
variant (which rewrites `HITL-*`→`AITL-*` **and** forges `mode:"virtual"` on a human
approval) is rejected RED; the untouched v4 source is correctly rejected under the
v5 schema (proving the schema is v5-only). Evidence in §9.

---

## 3. Files created

| File | Purpose |
|------|---------|
| _(none in the repository)_ | The AC-4 worked example (v4 source, v5 conversion, bad variant, validator) was built in the OS temp scratchpad as throwaway verification evidence (W21); it is not part of the product and is not committed. Its output is transcribed in §9. |

---

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md` | §5.16: added the `4.0`→`5.0` conversion paragraph after the `3.0`→`4.0` example; updated the reconstruction-table approval-array row to `checkpoint_approvals[]` with the actor projection. |
| `distribution-kit/CLAUDE.md` | Methodology Upgrade Protocol: `4.0`→`5.0` note + `hitl_approvals`→`checkpoint_approvals` on the reconstruction line. |
| `distribution-kit/.agents/skills/avenga-devflow/SKILL.md` | Same two edits (byte-identical). |
| `distribution-kit/.github/agents/AvengaDevFlow.agent.md` | Same two edits (byte-identical). |
| `distribution-kit/.opencode/agents/AvengaDevFlow.md` | Same two edits (byte-identical). |
| `devflow/spec/SPEC-260822-1622-manifest-conversion-v5.md` | Governance record (root, 4.2): revised to rev 2 (AC-3 narrowed, §5 BOLT-004 routing, §17 revision history); rev-2 `HITL-SPEC-Approval` recorded. |
| `devflow/metrics/bolts/US-020.BOLT-003-manifest-migration-path.json` | Governance record (root, 4.2): appended `spec_revisions[1]` (rev 2), rev-2 `HITL-SPEC-Approval`, and this V-Bounce entry. |

---

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
| _(none)_ | | |

---

## 6. Files deleted

| File | Reason |
|------|--------|
| _(none)_ | | |

---

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| `mode:"human"` for converted v4 entries (derived, not `null`) | Every v4 approval was recorded by a human; agents did not exist in v4. The safe default is `human`, not "unknown" (ADR-008 safe-default invariant). |
| `decided_by` `user`→`actor:"human:<user>"` + `model:null` | Matches the v5 approver shape (ADR-007/008) exactly and losslessly; the `human:` prefix makes the actor kind explicit. |
| Historical `HITL-*` names preserved in the recipe (never `AITL-*`) | G36 — recorded decisions are never rewritten during migration; new v5 approvals adopt `AITL-*` only after the separate rename US ships. The v5 schema enum still lists `HITL-*`, which the worked example confirms. |
| Keep the `3.0`→`4.0` example and add `4.0`→`5.0` | §5.16 documents the general lossless rule with a per-major example; both now illustrate it. |
| Narrow AC-3 to this Bolt's edited surface (rev 2) rather than expand the V-Bounce | The kit-wide gap is out of BOLT-003's §5 scope; absorbing it silently would violate the SPEC scope (G15). Routing it to BOLT-004 keeps each Bolt independently deliverable and gives the sweep a proper ADR-005 phrase-family AC. |

---

## 8. Deviations and assumptions

- **Material finding → SPEC rev 2 (G15).** AC-3 rev 1 asserted "no `hitl_approvals`
  anywhere in the kit". The sweep proved that false: `metrics/README.md` (the
  manifest reference) is entirely v4 (schema filenames, "Schema family v4",
  `schema_version "4.0"`, `{user,role}`), the §3.12 embedded example has the new
  array name but v4-shaped entries **without `mode`** (it would fail the v5 schema),
  ~12 files still reference `hitl_approvals`, and ~6 files link to the deleted
  `manifest-v4-*.schema.json`. This is a BOLT-001/002 propagation gap, out of scope
  here. AC-3 was narrowed to this Bolt's edited surface (§5.16 + the four agents'
  upgrade lines) and the kit-wide sweep (buckets A+B+C) routed to **US-020.BOLT-004**.
  The edits made under rev 1 are unchanged; the V-Bounce completes against rev 2 (no
  G16 span).
- **Assumption:** the artifact-level `review.reviewers[].user` stays `{user,role}` in
  v5 (the `user`→`actor` projection happens only at the manifest boundary, §3.12
  lines 1601–1602). Confirmed from the post-BOLT-002 §3.12 text — so the ~14 template
  `reviewers: # [{user,role}]` frontmatter comments are correct and are **not** part
  of BOLT-004's sweep.

---

## 9. Verification evidence

### Build
```
n/a — documentation Bolt (no compilable product in this repository).
```

### Tests
```
n/a — no unit/integration suites. The single deterministic check is the AC-4
schema validation below.
```

### AC-4 worked-example validation (jsonschema draft 2020-12 vs. manifest-v5-bolt.schema.json)
```
=== AC-4: v4->v5 worked-example validation against manifest-v5-bolt.schema.json ===
[PASS] Converted v5 manifest (GOOD): GREEN (valid)  (expected valid)
[PASS] Fabricated non-conforming v5 (BAD): RED (rejected)  (expected rejected)
        - at checkpoint_approvals/0/checkpoint: 'AITL-BOLT-READY-Approval' is not one of [... HITL-* ...]
        - at checkpoint_approvals/0/mode: 'human' was expected
[PASS] Original v4 source under v5 schema: RED (rejected)  (expected rejected)
        - at <root>: Additional properties are not allowed ('hitl_approvals' was unexpected)
        - at <root>: 'checkpoint_approvals' is a required property
        - at schema_version: '5.0' was expected
ALL PASS
```
The GOOD manifest's converted entries show `mode:"human"`, `actor:"human:eugenio.serrano"`,
`model:null`, and preserved `HITL-*` checkpoint names — exactly the §4 rule.

### Four-agent sync (AC-6)
```
G-count per agent: CLAUDE.md 39 · SKILL.md 39 · AvengaDevFlow.agent.md 39 · AvengaDevFlow.md 39
Edited line 1 ("...renames `hitl_approvals[]` → `checkpoint_approvals[]` and reshapes each entry"): 4/4 identical
Edited line 2 ("...the `review:` contract → `checkpoint_approvals[]`"): 4/4 identical
```

### Gates
- prompt-injection, secret-leak, IP/license, PII/DLP, dependency-confusion,
  test-first, unit/integration, SAST/DAST, perf-smoke: **n/a** (documentation/internal, per SPEC §9).
- hallucination-lint (refs resolve; example validates against the real v5 schema),
  behavioral-reproducibility (deterministic), bolt-manifest-validation
  (manifest validates GREEN vs. root v4 schema): **pass**.

### BUG V-Bounce evidence
n/a — not a BUG V-Bounce.

---

## 10. Manual interventions

None. All edits and the worked example were agent-generated; the human role was the
HITL-SPEC-Approval (rev 1 and rev 2) decision and the routing choice for BOLT-004.

---

## 11. Evidence links

- **Diff / PR:** none yet (uncommitted working tree; accumulates with BOLT-001/002).
- **Commit:** baseline `97125e7` (+ BOLT-001/002/003 kit changes in the working tree).
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-020.BOLT-003-manifest-migration-path.json`.

---

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~1.5h across Phases A–C (documentation + one validation) |
| V-Bounce number | 1 |
| Tests created | 1 deterministic validation (3 assertions: GREEN good / RED bad / RED v4-under-v5) |
| AI-generated code | 100% (docs + worked example); no human fallback |
| First-pass approval | pending (this MEM) |

---

## 13. Pending items and stubs

- [ ] **US-020.BOLT-004** — kit-wide v5-propagation sweep (A+B+C): `hitl_approvals`
      →`checkpoint_approvals` across `metrics/README.md`, the artifact templates and
      folder READMEs; reshape the §3.12 embedded example + `metrics/README.md`
      approver prose to `{actor,role,model}`+`mode`; fix broken `manifest-v4-*`
      links + "Schema family v4"/`schema_version "4.0"` labels. With an ADR-005
      phrase-family sweep AC over the full location set.
- [ ] After BOLT-004 Done → US-020 fully delivered (all four Bolts Done).

---

## 14. HITL-MEM-Approval

> **Avenga DevFlow §2.12, §3.0.** This MEM is created by the agent with no mutable
> status and is **never self-approved**. The executing Dev-validator inspects the
> actual diff, the schema-validation evidence, this MEM and the manifest, and records
> `HITL-MEM-Approval` here and in the manifest's `hitl_approvals[]`. `approved`
> completes the V-Bounce and (latest MEM) marks the Bolt `Development Completed`;
> `HITL-BOLT-DONE-Approval` is still required for `Done`.

| Field | Value |
|-------|-------|
| **Reviewers (executing Dev-validator; QA/Sec/domain optional)** | eugenio.serrano |
| **Roles** | dev_validator |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-22T16:47:37-03:00` |
| **review.started_at** | `2026-08-22T16:50:20-03:00` |
| **review.decided_at** | `2026-08-22T16:50:20-03:00` |
| **Review evidence** | Kit diff (§5.16 + four agents), AC-4 validation output (§9), four-agent sync + G-count 39×5, rev-2 manifest (valid) |
| **Comments** | Approved; kit-wide sweep routed to US-020.BOLT-004 |
| **Findings** | none |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | Evidence inspected as above; V-Bounce GREEN against rev-2 AC |
