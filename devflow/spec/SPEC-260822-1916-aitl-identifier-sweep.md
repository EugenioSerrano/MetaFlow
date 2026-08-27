---
id: "SPEC-260822-1916"
title: "Kit-wide HITL→AITL sweep — the HITL adjective + every HITL-<CODE>-Approval identifier → AITL, with a declared allowlist"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
status: "approved"
origin: "US-021"
bolt: "US-021.BOLT-004"
revision: 1
associated_adrs:
  - "devflow/adrs/ADR-008-aitl-approval-precept.md"
  - "devflow/adrs/ADR-005-removal-completeness-phrase-family-sweep.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
prerequisites: ["SPEC-260822-1817", "SPEC-260822-1839", "SPEC-260822-1905"]
risk_class: "medium"
autonomy_level: "L3"
turn_budget: "15"
data_classification: "internal"
review_ready_at: "2026-08-22T19:16:34-03:00"
review: # HITL-SPEC-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "dev_validator"}]
  started_at: "2026-08-22T19:18:36-03:00"
  decided_at: "2026-08-22T19:18:36-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved. Final comprehensive kit-wide HITL->AITL sweep (cat 2 adjective + cat 3 ~1119 identifiers + template JSON) under ADR-005 with the declared allowlist (BOLT-001 defining sentences, §5.16 recipe/history, schema enums, G05/G18/G24, agents' upgrade notes, H1-H6). Absence sweep + G36 validation + G-count 39x5 + kit-only. Authorizes the V-Bounce that closes US-021."
---

<!--
  LANGUAGE POLICY (§3.15): schema in English; prose content_language (en).
  Kit-only (ADR-004); root operating methodology stays v4.2. Dogfooding split:
  this SPEC's own checkpoints are HITL-*. The FINAL US-021 sweep: rename the HITL
  adjective (cat 2) + every HITL-<CODE>-Approval identifier (cat 3) to AITL kit-wide,
  minus a declared allowlist. ADR-005 governs (fixed location set + phrase family +
  allowlist, verified as an absence).
-->

# SPEC-260822-1916 — kit-wide HITL→AITL sweep (US-021.BOLT-004)

| Field | Value |
|-------|-------|
| **Origin** | [US-021](../functional/user-stories/US-021-hitl-to-aitl-evolution.md) (approved) |
| **Bolt** | [US-021.BOLT-004](../functional/bolts/US-021.BOLT-004-aitl-identifier-sweep.md) (approved) |
| **ADRs** | ADR-008 (§3.1 rename), ADR-005 (phrase-family sweep), ADR-004 (kit-only) |
| **Risk Class** | medium · **Autonomy** L3 · **Revision** 1 · **turn_budget** 15 |

---

## 1. Objective

The final, comprehensive rename: the pervasive **`HITL` adjective** (cat 2) **and
every `HITL-<CODE>-Approval` identifier** (cat 3, ~1,119) → **AITL**, across the
whole kit, under the ADR-005 discipline, **minus a declared allowlist** of `HITL-*`
that must remain (history / migration source / already-scoped guardrails / schema
history-support). When this lands, **US-021 is delivered and the kit is fully AITL**.

**Why:** BOLT-001–003 stated the precept, scoped the guardrails and widened the
schema; only the mechanical rename remains. **If not done:** the kit is left in a
mixed HITL/AITL state.

---

## 2. Context

BOLT-001 reframed the concept, BOLT-002 scoped G05/G18/G24, BOLT-003 made the
schema accept `AITL-*`. The identifiers (1,119 in `.md` + the 5
`TEMPLATE-MANIFEST-*.json` examples) and the `HITL` adjective remain. The schema
`.json` enums keep `HITL-*` (BOLT-003) — they are allowlisted here.

---

## 3. Source inventory (pre-SPEC evidence gate)

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | `US-021.BOLT-004-aitl-identifier-sweep.md` | HITL-BOLT-READY-Approval ✓ |
| Parent US | `US-021-hitl-to-aitl-evolution.md` | HITL-US-Approval ✓ |
| ADRs | ADR-008 (§3.1), ADR-005, ADR-004 | accepted ✓ |
| Prior Bolts | BOLT-001 (concept), BOLT-002 (guardrails), BOLT-003 (schema) | **Done** ✓ |

Pre-SPEC evidence gate: **all governed sources approved.** No active-ADR conflict.

---

## 4. The rename to apply (RED → GREEN)

- **Cat 3 — identifiers:** every `HITL-<CODE>-Approval` → `AITL-<CODE>-Approval`
  (the 8 core: US, BUG, TC, BOLT-READY, ADR, SPEC, MEM, BOLT-DONE; the
  `DISC`/`REV`/`AREV-CRITIQUE`/`AREV-DEFENSE`/`AREV-VERDICT` variants; and the
  `HITL-<CODE>-Approval` / `HITL-<CANONICAL-…-CODE>-Approval` placeholders) — in
  every `.md` under `distribution-kit/` **and** the five
  `TEMPLATE-MANIFEST-*.json` example values.
- **Cat 2 — adjective:** the standalone `HITL` shorthand naming the current concept
  ("HITL checkpoint(s)", "HITL approval", "HITL Coverage", "HITL decision",
  "HITL chain", "HITL governance", "(HITL)", …) → the AITL equivalent
  ("AITL checkpoint", "AITL Coverage", …).

## 4a. Allowlist — `HITL` / `HITL-*` that MUST remain (do NOT rename)

1. **The AITL definition + safe-default sentences (BOLT-001):** every mention of
   *"Human-in-the-Loop (HITL) is the default case"*, *"pure Human-in-the-Loop"*,
   and the acronym in *"…(HITL)…"* used to **define HITL as AITL's default case** —
   in `Avenga-DevFlow.md` §3.0 opening + foundational principle, the agents' concept
   intro, and the README concept intro. These intentionally name the legacy term.
2. **The §5.16 migration recipe** — `HITL-*` / `hitl_approvals` naming the **v4
   source** and the `3.0→4.0` / `4.0→5.0` history examples (G36: migrated history
   keeps `HITL-*`).
3. **The manifest schema `.json` enums** (`manifest-v5-*.schema.json`) — their
   `HITL-*` entries (BOLT-003 — accept migrated history). **Not edited by this Bolt.**
4. **G05, G18, G24** (GUARDRAILS + the four agents) — they name `HITL-*` as legacy
   on purpose (BOLT-002). **Not re-touched.**
5. **The four agents' "Methodology Upgrade Protocol" notes** — `hitl_approvals` /
   `HITL-*` naming the v4 source being converted.
6. **`H1–H6`** numbered legacy aliases (not `HITL`, but legacy — unchanged).

---

## 5. Scope

### In scope (kit)
- Every `.md` under `distribution-kit/` (concept done in BOLT-001; here: the cat-2
  adjective + cat-3 identifiers that remain) — core methodology, GUARDRAILS
  (non-G05/G18/G24 identifier refs), the four agents, templates, READMEs.
- The five `TEMPLATE-MANIFEST-*.json` example `checkpoint` values.

### Out of scope
- The allowlist (§4a); the schema `.json` files; enabling virtual approvers /
  registry / roster / pilot (later USs); the root `devflow/` (ADR-004).

---

## 6. Phases

- **Phase A — cat 3 (identifiers):** rename `HITL-<CODE>-Approval` → `AITL-*`
  kit-wide (`.md` + template JSON), excluding the allowlist. ~2h.
- **Phase B — cat 2 (adjective):** rename the standalone `HITL` shorthand → AITL,
  excluding the allowlist's defining mentions. ~1.5h.
- **Phase C — Verification (GREEN):** the ADR-005 absence sweep + G36 validation +
  G-count + four-agent sync + kit-only (§8). ~0.5h.

---

## 7. Acceptance criteria

- **AC-1 (identifiers, cat 3):** no `HITL-<CODE>-Approval` remains outside the
  allowlist; the 8 core + DISC/REV/AREV variants + the §3.0 charter table + the
  canonical naming rule read `AITL-*`; the five `TEMPLATE-MANIFEST-*.json` example
  values read `AITL-*`.
- **AC-2 (adjective, cat 2):** no standalone `HITL` concept-shorthand remains
  outside the allowlist (it reads `AITL`).
- **AC-3 (ADR-005 sweep clean):** the phrase-family sweep over the whole kit, minus
  the declared allowlist (§4a), returns **zero** — recorded in the MEM as an absence.
- **AC-4 (allowlist intact):** the BOLT-001 defining sentences, the §5.16 recipe,
  the schema enums, G05/G18/G24, the agents' upgrade notes and `H1–H6` are
  **unchanged** (verified).
- **AC-5 (G36 — history still validates):** a manifest carrying a migrated
  `HITL-*` entry still validates against the (unchanged) v5 schema; the schema
  enums still list `HITL-*`.
- **AC-6 (count + sync):** blocking-rule count **39×5**; four-agent shared regions
  byte-identical; G-count 39×5.
- **AC-7 (kit-only):** `git status` shows only `distribution-kit/` + governance
  records; root untouched.
- **AC-8 (manifest):** the BOLT-004 manifest gets its `v_bounces[]` entry and validates.

---

## 8. Testing strategy

Deterministic (documentation sweep + validation):
- **RED (before):** ~1,119 `HITL-<CODE>-Approval` + the pervasive `HITL` adjective
  across the kit.
- **GREEN (after):** the ADR-005 absence sweep returns **zero** non-allowlisted
  `HITL-<CODE>-Approval` and **zero** non-allowlisted standalone `HITL`; the
  allowlist zones are unchanged (§4a); a migrated `HITL-*` manifest validates
  against the v5 schema (G36, AC-5); the schema enums still hold `HITL-*`; G-count
  **39×5**; four-agent sync; `git status` kit-only. Record the before/after counts,
  the residual allowlist inventory, and the G36 validation in the MEM.

**Boundary note (ripgrep lacks look-around):** the sweep matches the identifier form
`HITL-[A-Z][A-Z-]*-Approval` explicitly (cat 3) and standalone `HITL` not followed
by `-[A-Z]` (cat 2); allowlist zones are excluded by file (schemas), by rule
(G05/G18/G24), by section (§5.16 recipe, agents' upgrade notes) and by the defining
sentences (BOLT-001).

---

## 9. Quality gates

Documentation/internal → unit/integration, SAST/DAST/SBOM, perf, IP, PII,
dep-confusion, test-first: `n/a`. hallucination-lint (refs resolve),
behavioral-reproducibility (deterministic), bolt-manifest-validation: `pass`.
prompt-injection, secret-leak: `pass`.

---

## 10. Security and data

The rename does not change any guarantee (the guardrails, the schema and the
precept already carry the AITL semantics). Renaming identifiers keeps history valid
(schema still accepts `HITL-*`). Data `internal`.

---

## 11. Migration, compatibility, rollback

`AITL-*` is the new canonical vocabulary; `HITL-*` history stays valid (schema +
allowlist). Rollback: revert the kit commit; root untouched.

---

## 12. Risk matrix

| Risk | Prob | Impact | Mitigation |
|------|------|--------|------------|
| Over-broad sweep renames allowlisted `HITL-*` (history/migration/schema) | 3 | 5 | §4a allowlist by file/rule/section/sentence; AC-4 verifies each zone unchanged; AC-5 validates a migrated HITL-* manifest |
| Incomplete sweep leaves stray `HITL` | 2 | 3 | ADR-005 absence assertion over the whole kit (AC-3) |
| Four-agent drift / rule-count change | 2 | 3 | AC-6: G-count 39×5 + byte-identical shared regions |
| Renamed identifiers fail schema | 1 | 4 | BOLT-003 already accepts `AITL-*`; AC-5/validation |

---

## 13. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| One comprehensive sweep (cat 2 + cat 3 together) | They interleave on the same lines; one ADR-005 pass is cleaner |
| Rename the TEMPLATE-MANIFEST JSON examples to `AITL-*` | Adopters copy them; they should show the new canonical vocabulary (schema accepts both) |
| Keep the schema enum `.json` `HITL-*` | BOLT-003 — history support; renaming would drop migrated-history acceptance |
| Allowlist the BOLT-001 defining sentences | They intentionally name HITL as AITL's default case (ADR-008 §3.1) |

---

## 14. Stop conditions

- AC-4 finds an allowlisted zone changed → over-reach; stop, revert that zone.
- AC-5 finds a migrated `HITL-*` manifest no longer validates → stop, fix.
- The sweep returns non-zero after edits → not GREEN; continue within turn_budget
  (15), else stop + MEM with the residual list.
- Any root `devflow/` file in the diff → stop, revert.
- A governed source changes materially (G15) → stop, revise, re-approve.

---

## 15. Definition of Done

- [ ] Phases A–C · AC-1..AC-8 pass
- [ ] GREEN (zero non-allowlisted HITL; allowlist intact; G36 history validates; 39×5; kit-only)
- [ ] ADR-008 (§3.1) + ADR-005 (sweep) + ADR-004 (kit-only) followed
- [ ] MEM (before/after counts + allowlist inventory + G36 validation) · manifest `v_bounces[]` appended
- [ ] HITL-MEM-Approval → then **US-021 delivered** (kit fully AITL)

---

## 16. References

- US-021, US-021.BOLT-004 (approved); BOLT-001/002/003 (Done)
- ADR-008 §3.1 (rename); ADR-005 (phrase-family sweep, allowlist as an absence)
- BOLT-001 defining sentences (allowlist); §5.16 recipe (allowlist); BOLT-003 schema (allowlist)

---

## 17. HITL-SPEC-Approval

> Draft until the Dev-validator records `HITL-SPEC-Approval`. A material source
> change invalidates it — stop, revise, re-approve (G15).

| Field | Value |
|-------|-------|
| **review.reviewers** | eugenio.serrano (dev_validator) |
| **review.decision** | **approved** |
| **review_ready_at** | `2026-08-22T19:16:34-03:00` |
| **review.started_at** | `2026-08-22T19:18:36-03:00` |
| **review.decided_at** | `2026-08-22T19:18:36-03:00` |
