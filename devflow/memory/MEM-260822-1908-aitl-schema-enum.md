---
id: "MEM-260822-1908"
title: "v5 manifest schemas accept AITL-* checkpoints (keep HITL-* history) (US-021.BOLT-003)"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
bolt: "US-021.BOLT-003"
spec: "SPEC-260822-1905"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "97125e7"
applied_adrs:
  - "devflow/adrs/ADR-008-aitl-approval-precept.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "US-021.BOLT-003-aitl-schema-enum.json"
diff_ref: ""
review_ready_at: "2026-08-22T19:08:56-03:00"
review: # HITL-MEM-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "dev_validator"}]
  started_at: "2026-08-22T19:10:24-03:00"
  decided_at: "2026-08-22T19:10:24-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Inspected the 3 schema files diff + the jsonschema evidence: mixed AITL/HITL GREEN, 5 templates GREEN (no regression), 3 malformed RED, US/TC AITL GREEN; enum stays closed; backward compatible (G36); kit-only. V-Bounce GREEN."
---

<!--
  LANGUAGE POLICY (§3.15): schema/headings English; prose content_language (en).
  Kit-only product surface (ADR-004); root governance records stay 4.2.
-->

# MEM-260822-1908 — v5 schema accepts AITL-* checkpoints (US-021.BOLT-003)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | [US-021.BOLT-003](../functional/bolts/US-021.BOLT-003-aitl-schema-enum.md) |
| **SPEC**        | [SPEC-260822-1905](../spec/SPEC-260822-1905-aitl-schema-enum.md) revision 1 |
| **V-Bounce**    | 1 |
| **ADRs**        | ADR-008 (§3.1 record vocabulary), ADR-004 (kit-only) |

---

## 1. Executive summary

This V-Bounce widened the three v5 manifest schemas to accept the **AITL** approval
vocabulary — the third of US-021's four Bolts, and the structural prerequisite for
BOLT-004's identifier rename. The Bolt schema's `checkpoint` enum gained the seven
`AITL-*` names (14 total, keeping the seven `HITL-*`), and its SPEC/MEM `subject`
conditionals — which require `revision` (SPEC) and `v_bounce` (MEM) — were widened
from `const` to `enum` so they fire for **both** the `HITL-` and `AITL-` forms; the
US and TC schemas' `checkpoint` moved from a single `const` (`HITL-US-Approval` /
`HITL-TC-Approval`) to an `enum` accepting the `AITL-` counterpart too. The change
is **purely additive and backward-compatible** — `HITL-*` stays accepted so migrated
history never fails (G36) — and the enums stay **closed** (explicit lists, not a
regex), so an unknown `AITL-FOO-Approval` is still rejected. Proven GREEN: a worked
Bolt manifest mixing an `AITL-SPEC-Approval` (+`subject.revision`), an
`AITL-MEM-Approval` (+`v_bounce`) and a historical `HITL-US-Approval` validates; the
US/TC schemas accept their `AITL-*`; every existing kit template (all `HITL-*`) still
validates (no regression). RED as designed: `AITL-SPEC-Approval` without
`subject.revision`, `AITL-MEM-Approval` without `v_bounce`, and the unknown
`AITL-FOO-Approval` are all rejected. Kit-only — exactly the three schema files
changed; root untouched.

---

## 2. Implemented phases

### Phase A — the three v5 schemas
- **`manifest-v5-bolt.schema.json`:** `checkpoint` enum 7 → 14 (added the seven
  `AITL-*`); the SPEC conditional `if checkpoint const HITL-SPEC-Approval` →
  `enum ["HITL-SPEC-Approval","AITL-SPEC-Approval"]`; the MEM conditional likewise
  for `*-MEM-Approval`. The `mode`/actor `allOf` unchanged.
- **`manifest-v5-us.schema.json`:** `checkpoint` `const "HITL-US-Approval"` →
  `enum ["HITL-US-Approval","AITL-US-Approval"]`.
- **`manifest-v5-tc.schema.json`:** `checkpoint` `const "HITL-TC-Approval"` →
  `enum ["HITL-TC-Approval","AITL-TC-Approval"]`.

### Phase B — verification
Built and validated worked examples with `jsonschema` (draft 2020-12) against the
edited kit schemas (§9).

---

## 3. Files created / 5. Files renamed / 6. Files deleted

_(none — schema edits only; the validation harness ran from the OS temp scratchpad, W21)_

---

## 4. Files modified

| File | Change |
|------|--------|
| `distribution-kit/devflow/metrics/manifest-v5-bolt.schema.json` | `checkpoint` enum 7→14 (+AITL-*); SPEC/MEM `subject` conditionals `const`→`enum` (both prefixes) |
| `distribution-kit/devflow/metrics/manifest-v5-us.schema.json` | `checkpoint` `const`→`enum` (HITL-US + AITL-US) |
| `distribution-kit/devflow/metrics/manifest-v5-tc.schema.json` | `checkpoint` `const`→`enum` (HITL-TC + AITL-TC) |
| `devflow/spec/SPEC-260822-1905*`, `metrics/bolts/US-021.BOLT-003*.json`, this MEM | Governance records (root, 4.2) |

---

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| Explicit `enum` of both prefixes (not a regex pattern) | Keeps the set **closed** — only the known checkpoints, in either vocabulary; an unknown code (`AITL-FOO-Approval`) is still rejected |
| Widen SPEC/MEM `if` from `const` to `enum` | The `subject` shape (revision / v_bounce) must be required regardless of `HITL-`/`AITL-` prefix |
| Keep `HITL-*` in every enum | ADR-008 §3.1 / G36 — migrated history never invalidated (backward compatible) |
| Leave templates/prose/examples on `HITL-*` | Valid under the widened enum; renaming is BOLT-004's identifier sweep |

---

## 8. Deviations and assumptions

- **Intentional mixed state:** the schema now accepts `AITL-*`, but the kit's
  templates/docs/examples still use `HITL-*` (valid) — BOLT-004 renames the
  identifiers. No SPEC revision needed (rev 1 clean).
- **Root manifests untouched:** the repo's own manifests are root-partition (v4.0,
  `hitl_approvals`); this Bolt edited only the **kit** v5 schemas — no root
  regression possible.

---

## 9. Verification evidence

### Schema validation (jsonschema draft 2020-12, edited kit schemas)
```
=== No regression: kit v5 templates (all HITL-*) ===
  TEMPLATE-MANIFEST-BOLT / -NONFUNCTIONAL / -TEST : GREEN
  TEMPLATE-MANIFEST-US (HITL-US) / -TC (HITL-TC)  : GREEN
=== Bolt: mixed AITL-* + historical HITL-* entry ===
  AITL-SPEC(+revision) + AITL-MEM(+v_bounce) + HITL-US : GREEN
=== Bolt: malformed (RED as designed) ===
  AITL-SPEC-Approval missing subject.revision : RED
  unknown AITL-FOO-Approval                   : RED
  AITL-MEM-Approval missing subject.v_bounce  : RED
=== US / TC ===
  US AITL-US-Approval : GREEN
  TC AITL-TC-Approval : GREEN
ALL PASS
```

### Kit-only (AC-6)
```
git status: only the 3 files —
  distribution-kit/devflow/metrics/manifest-v5-{bolt,us,tc}.schema.json
+ root governance records. Root framework untouched.
```

### Gates
- unit/integration (product), SAST/DAST/SBOM, perf, IP, PII, dep-confusion, test-first: **n/a**.
- hallucination-lint, behavioral-reproducibility (deterministic validation),
  bolt-manifest-validation: **pass**.

### BUG V-Bounce evidence
n/a.

---

## 10. Manual interventions

None. All edits agent-generated; the human role was HITL-SPEC-Approval.

---

## 11. Evidence links

- **Diff / PR:** none yet (uncommitted; 5.0 branch).
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-021.BOLT-003-aitl-schema-enum.json`.

---

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~1h (3 schema files + validation) |
| V-Bounce number | 1 |
| Tests created | schema validation: 5 no-regression + 1 GREEN mixed + 3 RED malformed + 2 US/TC GREEN |
| AI-generated code | 100% (schema + harness); no human fallback |
| First-pass approval | pending (this MEM) |

---

## 13. Pending items and stubs

- [ ] **US-021.BOLT-004** — comprehensive kit-wide sweep: the `HITL` adjective (cat 2)
      + the `HITL-<CODE>-Approval` identifiers (cat 3, ~1,119) → AITL, ADR-005 phrase
      family + allowlist (G05/G18/G24 already scoped in BOLT-002; §5.16 migration
      source; the schema enums now accept the renamed identifiers).
- [ ] On BOLT-004 Done → US-021 delivered (kit fully AITL).

---

## 14. HITL-MEM-Approval

> **Avenga DevFlow §2.12, §3.0.** Created by the agent, no mutable status,
> **never self-approved**. The executing Dev-validator inspects the diff, the
> schema-validation evidence, this MEM and the manifest, and records
> `HITL-MEM-Approval` here and in the manifest's `hitl_approvals[]`.

| Field | Value |
|-------|-------|
| **Reviewers (executing Dev-validator; QA/Sec/domain optional)** | eugenio.serrano |
| **Roles** | dev_validator |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-22T19:08:56-03:00` |
| **review.started_at** | `2026-08-22T19:10:24-03:00` |
| **review.decided_at** | `2026-08-22T19:10:24-03:00` |
| **Review evidence** | 3 schema files diff, worked-example validation (no-regression + GREEN AITL/HITL + RED malformed + US/TC), kit-only, manifest |
| **Comments** | Approved; schema layer of HITL→AITL done |
| **Findings** | none |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | Evidence inspected as above; V-Bounce GREEN |
