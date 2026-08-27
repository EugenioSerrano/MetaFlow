---
id: "SPEC-260822-2032"
title: "Remediate REV-002 — v5.0 kit internal consistency (AITL wording, HITL residue, schema_version, AREV/xref/encoding hygiene)"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
status: "approved" # draft | approved | blocked | obsolete
origin: "REV-002"
bolt: "US-000.BOLT-007"
revision: 1
associated_adrs:
  - "devflow/adrs/ADR-008-aitl-approval-precept.md"
  - "devflow/adrs/ADR-005-removal-completeness-phrase-family-sweep.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
prerequisites: []
risk_class: "medium"
autonomy_level: "L3"
turn_budget: "12"
data_classification: "internal"
review_ready_at: "2026-08-22T20:32:13-03:00"
review: # HITL-SPEC-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers:
    - user: "eugenio.serrano"
      role: "dev_validator"
    - user: "eugenio.serrano"
      role: "tech_lead"
  started_at: "2026-08-22T20:36:22-03:00"
  decided_at: "2026-08-22T20:36:22-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Implementation plan reviewed and approved. Every change is alignment to a governing artifact (ADR-008 for F-04, the v5 schema for F-03, §3.15 for F-06) — no new decision. The two embedded decisions confirmed: state the 'human by default' precept now (not deferred), and F-07 example to English. Zone-scoped verification (F-02) accepted as the acceptance method. Dev-validator + tech_lead (charter edits). V-Bounce authorized."
---

<!--
  LANGUAGE POLICY (§3.15): schema in English; prose content_language (en).
  DOGFOODING SPLIT (ADR-004/006): this SPEC is authored under the v4.2 operating
  methodology, so its own checkpoints are HITL-*. It edits the v5.0 PRODUCT
  (distribution-kit/), whose canonical vocabulary is AITL-*. Baseline: 137a5b5.
-->

# SPEC-260822-2032 — Remediate REV-002 (v5.0 kit internal consistency)

| Field | Value |
|-------|-------|
| **Origin** | [REV-002](../reviews/REV-002-v5-kit-consistency-audit.md) (approved) |
| **Bolt** | [US-000.BOLT-007](../functional/bolts/US-000.BOLT-007-rev002-v5-kit-consistency-remediation.md) (approved, HITL-BOLT-READY-Approval 2026-08-22T20:30:01-03:00) |
| **ADRs** | ADR-008 (F-04 target), ADR-005 (sweep discipline + F-02), ADR-004 (kit-only) |
| **Risk Class** | medium · **Autonomy** L3 · **Revision** 1 · **turn_budget** 12 |

---

## 1. Objective

Close the eight REV-002 findings (F-01…F-08) in `distribution-kit/` as one
allowlist-aware documentation pass, plus the F-02 verification-method correction.
Every change is **alignment to an already-governing artifact** — no new decision.

---

## 2. Context (why, and what if not done)

REV-002 (approved) proved the v5.0 kit is structurally sound but carries eight
documentation inconsistencies, two of them substantive: the kit still asserts
"human-only / never delegated to AI" (F-04) in direct contradiction of the
already-accepted **ADR-008** ("human-by-default, agent-by-explicit-configuration",
§3.1–§3.4), and §3.12 states a `schema_version` that contradicts the shipped
schema (F-03). The US-021 sweep also left 26 `HITL-*` residues (F-01) that its
own absence check could not see because the allowlist proxy was the literal token
`HITL-*` (F-02). **If not done:** the flagship v5.0 feature (AITL) ships
self-contradicting — an agent reading the "human-only" wording literally would
refuse a validly-configured virtual approval — and the "kit is fully AITL" claim
stays false. F-04 is also a prerequisite for the later virtual-approver USs.

---

## 3. Source inventory (pre-SPEC evidence gate — PASS)

| Source | Ref | Status |
|--------|-----|--------|
| Bolt | `US-000.BOLT-007-rev002-v5-kit-consistency-remediation.md` | HITL-BOLT-READY-Approval ✓ |
| Origin | `REV-002-v5-kit-consistency-audit.md` | approved ✓ |
| ADR | `ADR-008-aitl-approval-precept.md` | accepted ✓ |
| ADR | `ADR-005-removal-completeness-phrase-family-sweep.md` | accepted ✓ |
| ADR | `ADR-004-repository-partition-v2.md` | accepted ✓ |
| Parent | `US-000-non-functional.md` | active container (no approval) ✓ |

No active-ADR conflict. No open OQ against US-000 (G35). **Baseline:** `137a5b5`.

---

## 4. Repository baseline

The eight findings and their exact locations are as verified in REV-002 §4 against
commit `137a5b5`. Line numbers below are the SPEC's implementation anchors; the
executor re-confirms each token before editing (a preceding edit can shift lines).

---

## 5. The changes (RED → GREEN), per finding

> All paths are under `distribution-kit/`. **Do not touch** the §4a allowlist zones
> (§5.7). Every edit preserves surrounding wording; only the named token/clause changes.

### 5.1 F-04 — align checkpoint-governance wording to ADR-008 ("human by default")

Replace every **unqualified** "human-only / never delegated to AI / always a named
human" assertion with ADR-008's precept. Keep the hard identity rules intact (no
self-approval, safe default, never fabricate a human, critical/regulatory ceiling).

- **`devflow/avenga-devflow/Avenga-DevFlow.md`** — the two §3.0 checkpoint tables
  (~lines 1400 and 1418): change the column header `| Human-only checkpoint |` →
  `| Approver actor |`; change each cell value from `✅` to `human by default¹`.
  After the second table, add footnote:
  `> ¹ A virtual DevFlow Agent may occupy the checkpoint only by explicit, valid`
  `> configuration with independence (ADR-008 §3.2–§3.4); \`critical\`/\`regulatory\``
  `> stay human (§3.3 ceiling). Absent/invalid config → human-only, and no AI-signed`
  `> approval is possible (safe default).`
- **`devflow/GUARDRAILS.md`** — the checkpoint-map intro (~line 18):
  `is human-only (never delegated to AI), and requires a named reviewer …` →
  `is occupied by an actor — a human by default, a virtual DevFlow Agent only by`
  `explicit, valid configuration (ADR-008 §3.2); absent/invalid config → human-only,`
  `no AI-signed approval possible — and requires a named reviewer …` (keep the rest
  of the sentence and the "§3.0" pointer). Adjust the section header parenthetical
  `(the human stops the agent MUST respect)` → `(the actor stops the agent MUST respect)`.
- **`AGENTS.md`** (framework block, above the marker):
  - line 7: `every \`AITL-<CODE>-Approval\` is a mandatory human checkpoint; never skip or delegate one` →
    `every \`AITL-<CODE>-Approval\` is a mandatory checkpoint occupied by an actor — a human by default, a virtual DevFlow Agent only by explicit, valid configuration (ADR-008); never skip one, never self-approve or fabricate a reviewer`.
  - line 36: `\`AITL-<CODE>-Approval\` is always a named human, with timestamps …` →
    `\`AITL-<CODE>-Approval\` is always a named actor — a human by default, a virtual DevFlow Agent only by explicit, valid configuration — with timestamps …` (keep "You create the artifact; you never approve it, never delegate the checkpoint…" — it is about self-approval and stays correct).

> The four platform agents' AITL sections already read "human by default, virtual
> agent only by explicit valid configuration" (verified) — **not edited**.

### 5.2 F-01 — rename the 26 non-allowlisted `HITL-*` → `AITL-*`

In the **language-policy sentence** at each location below, the token `HITL-*` /
`HITL-*-Approval` becomes `AITL-*` / `AITL-*-Approval` (rest of the sentence
unchanged):

- `devflow/avenga-devflow/Avenga-DevFlow.md:3354` and `:3378`
- `CLAUDE.md:668`, `.agents/skills/avenga-devflow/SKILL.md:685`, `.github/agents/AvengaDevFlow.agent.md:713`, `.opencode/agents/AvengaDevFlow.md:696`
- `AGENTS.md:16`, `devflow/README.md:367`, `devflow/ONBOARDING.md:150`, `devflow/tests/test-cases/README.md:104`, `devflow/tests/test-cases/TEMPLATE-TC.md:33`, `devflow/functional/user-stories/TEMPLATE-US.md:39`
- the 13 analysis templates: `business-context/TEMPLATE-BUSINESS-CONTEXT.md:17`, `business-risks/TEMPLATE-BR.md:17`, `domain-model/entities/TEMPLATE-ENTITY.md:19`, `domain-model/enumerations/TEMPLATE-ENUM.md:19`, `domain-model/relationships/TEMPLATE-RELATIONSHIP.md:17`, `glossary/TEMPLATE-GLOSSARY.md:17`, `introduction/TEMPLATE-INTRODUCTION.md:47`, `open-questions/TEMPLATE-OQ.md:28`, `personas/TEMPLATE-PERSONA.md:22`, `process/TEMPLATE-PROCESS.md:20`, `scope/TEMPLATE-SCOPE.md:19`, `ui/TEMPLATE-UI.md:18`, `user-journeys/TEMPLATE-JOURNEY.md:20`

Plus **T12** — `devflow/GUARDRAILS.md:245`: `each artifact's \`HITL-*\` decision` →
`each artifact's \`AITL-*\` decision`.

Total: 25 + 1 = **26** tokens. `TEMPLATE-ADR.md` (already `AITL-ADR-Approval`) is the
reference form.

### 5.3 F-03 — correct §3.12 `schema_version`

`devflow/avenga-devflow/Avenga-DevFlow.md:3151-3153`:
`\`schema_version\` is exactly \`4.0\` for this family — the \`<major>.0\` convention: every 4.x methodology version keeps it, and a schema change means a new major.`
→
`\`schema_version\` is exactly \`5.0\` for this family — the \`<major>.0\` convention: the manifest family carries its own major, bumped when the schema changes (the v4→v5 change that added \`checkpoint_approvals[]\` and \`mode\`), so the family major may lead the methodology version.`
The following paragraph (3155-3169, "a schema change means `5.0` … which is exactly
what the normative filenames already say") is already correct and stays.

### 5.4 F-05 — fix the AITL citation `§2.15` → `§3.0`

Replace `(AITL, §2.15/ADR)` → `(AITL, §3.0/ADR-008)` at:
`devflow/avenga-devflow/Avenga-DevFlow.md:3128`, `CLAUDE.md:514`,
`.agents/skills/avenga-devflow/SKILL.md:531`, `.github/agents/AvengaDevFlow.agent.md:559`,
`.opencode/agents/AvengaDevFlow.md:542`.

### 5.5 F-06 — give AREV `cancelled` a home

- `devflow/adversarial-reviews/README.md` — the "AREV lifecycle" table (~423-428):
  add the row `| **cancelled** | The AREV cannot reach a neutral Verdict (no available third model) and is closed unrun (§3.13, G37) |` after the `closed` row.
- `devflow/adversarial-reviews/INDEX.md` — add a terminal bucket after "🏁 Closed":
  `## ⛔ Cancelled (unrun — no neutral Verdict possible)` with the empty placeholder
  row shape used by the other buckets.

### 5.6 F-07 — fix the corrupted example comment

`devflow/metrics/TEMPLATE-MANIFEST-BOLT.json:204`: replace the mojibake Spanish
comment with a correctly-encoded English equivalent (kit `LANGUAGE` is `en`):
`"comment": "Add explicit concurrency handling."` (was the double-encoded
`"Agregar manejo explÃ­cito de concurrencia."`). Re-validate the file against
`manifest-v5-bolt.schema.json`.

### 5.7 F-08 — "the Unit" → "release suite"

`devflow/GUARDRAILS.md:468`: `because the Unit will cover it (§3.6).` →
`because a later release suite will cover it (§3.6).` (matches the methodology's
own wording at `Avenga-DevFlow.md:2413`).

### Allowlist — MUST remain untouched (G36)

The `manifest-v5-*.schema.json` enum `HITL-*`; G05 (`GUARDRAILS.md:61` + the four
agents); G18/G24; the §5.16 migration recipe (`Avenga-DevFlow.md` ~4632-4640 + the
agents' upgrade notes); the `Human-in-the-Loop (HITL)` defining sentences
(`Avenga-DevFlow.md:1372` + agents/README concept intro); `H1–H6`.

---

## 6. Scope

**In scope:** documentation edits inside `distribution-kit/` only (§5).
**Out of scope:** the schema `.json` files; the §4a allowlist; the root `devflow/`
tree (ADR-004); **enabling** virtual approvers (registry/roster/Coordinator/pilot —
later USs, ADR-008 §3.9). This SPEC states the precept correctly; it does not build
the enablement.

---

## 7. Phases

- **Phase A — substantive alignment:** F-04 (§5.1), F-03 (§5.3). ~1h.
- **Phase B — sweep + hygiene:** F-01 (§5.2), F-05 (§5.4), F-06 (§5.5), F-07 (§5.6),
  F-08 (§5.7), allowlist-aware. ~1h.
- **Phase C — verification (GREEN):** the zone-scoped absence sweep (§9) + schema
  validation + four-agent parity + G-count + kit-only. ~0.5h.

Sequence F-04 first (it is the prerequisite for the virtual-approver USs).

---

## 8. Acceptance criteria

- **AC-1 (F-04):** no unqualified "human-only / never delegated to AI / always a
  named human" remains in the §3.0 tables, `GUARDRAILS.md`, or `AGENTS.md`; each now
  states "human by default, virtual agent only by explicit valid config (ADR-008)".
- **AC-2 (F-01):** the zone-scoped sweep (§9) returns **zero** non-allowlisted
  `HITL` in the kit; the 26 named tokens read `AITL-*`; the allowlist zones are
  byte-unchanged.
- **AC-3 (F-03):** `Avenga-DevFlow.md` §3.12 states `schema_version` `5.0`; no
  `exactly \`4.0\`` remains.
- **AC-4 (F-05):** no `§2.15/ADR` AITL citation remains; all five read `§3.0/ADR-008`.
- **AC-5 (F-06):** the AREV README lifecycle table lists `cancelled` and the INDEX has
  a Cancelled bucket — matching `TEMPLATE-AREV.md` and §3.15.
- **AC-6 (F-07):** `TEMPLATE-MANIFEST-BOLT.json` has no mojibake and validates against
  `manifest-v5-bolt.schema.json`.
- **AC-7 (F-08):** `GUARDRAILS.md:468` reads "release suite".
- **AC-8 (history/G36):** a migrated `HITL-*` manifest still validates against the
  unchanged v5 schema; the schema enums still list `HITL-*`.
- **AC-9 (parity + count):** the four agents' shared methodology bodies stay
  byte-identical; G-count **39×5**.
- **AC-10 (kit-only):** `git status` shows only `distribution-kit/` + root governance
  records (this SPEC, MEM, manifest). Root framework untouched (ADR-004).
- **AC-11 (manifest):** the Bolt manifest gets its `v_bounces[]` entry and validates.

---

## 9. Testing strategy — the zone-scoped absence sweep (fixes F-02)

The completeness check **excludes the allowlist by zone, never by the literal token
`HITL-*`** (that proxy is what masked F-01). Method:

1. List every `HITL` occurrence in `distribution-kit/**` (`.md` + `.json`).
2. Exclude, by explicit zone:
   - the three `manifest-v5-*.schema.json` files (whole-file);
   - the G05 rows and the G18/G24 rows (by rule id);
   - the §5.16 migration-recipe section and the agents' "Methodology Upgrade Protocol"
     notes (by section);
   - the `Human-in-the-Loop (HITL)` defining sentences (by exact sentence);
   - `H1–H6`.
3. **Assert: the remainder is empty.** Any leftover `HITL` (including a
   `HITL-*-Approval` placeholder in prose) is residue — before this Bolt it was 26;
   after, it must be 0.

Plus: re-validate the 5 `TEMPLATE-MANIFEST-*.json` against the v5 schemas; validate a
migrated `HITL-*` manifest (AC-8); diff the four agents' shared bodies (byte-identical);
`git status` kit-only. Record before/after counts, the zone list, and the G36 validation
in the MEM.

---

## 10. Quality gates

Documentation/internal → unit/integration, SAST/DAST/SBOM, perf, IP, PII,
dep-confusion, test-first, secret-leak, prompt-injection: `n/a` (no code, no
externally reachable surface). hallucination-lint (refs resolve; `§2.15`→`§3.0`
corrected), behavioral-reproducibility (deterministic sweep),
bolt-manifest-validation: `pass`.

---

## 11. Security and data

No security guarantee changes: F-04 makes the docs *state* ADR-008's precept, it does
not enable delegation (enablement is later USs). History stays valid (schema enums
untouched, G36). Data `internal`.

---

## 12. Migration, compatibility, rollback

No manifest conversion. Rollback: revert the single kit commit; root untouched
(ADR-004). `AITL-*` remains canonical; `HITL-*` history stays valid.

---

## 13. Risk matrix

| Risk | Prob | Impact | Mitigation |
|------|------|--------|------------|
| Sweep touches an allowlist/history zone | 2 | 5 | zone-scoped exclusion (§9); AC-8 validates a migrated HITL-* manifest; allowlist byte-unchanged |
| F-04 wording drifts beyond ADR-008 | 2 | 4 | bounded to ADR-008 §3.1–§3.4 precept; no new rule; identity rules preserved |
| Four-agent drift | 2 | 3 | AC-9 byte-identity + G-count 39×5 |
| Line anchors shifted by a prior edit | 3 | 2 | re-confirm each token before editing (§4) |

---

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| One pass for all 8 findings | Same class (kit doc consistency); they interleave on the same files; one verification |
| F-04 stated as the precept now (not deferred to enablement) | ADR-008 §3.9 makes the charter wording US-021's job; leaving the self-contradiction in shipped v5.0 is worse |
| Verify by zone, not by `HITL-*` token | Root cause of F-02; the token proxy masked exactly the residue |
| F-07 example → English | Kit `LANGUAGE` is `en`; the example should model the kit's own language |

---

## 15. Stop conditions

- The zone-scoped sweep returns non-zero after edits → not GREEN; continue within
  turn_budget (12), else stop + MEM with the residual list.
- An allowlist/history zone changed, or a migrated `HITL-*` manifest fails to validate
  → over-reach; stop, revert that zone.
- Any root `devflow/` framework file in the diff → stop, revert (ADR-004).
- A governed source changes materially (G15) → stop, revise, re-approve.

---

## 16. Definition of Done

- [ ] Phases A–C · AC-1..AC-11 pass
- [ ] GREEN (zone-scoped sweep = 0 non-allowlisted `HITL`; allowlist intact; G36
      validates; 39×5; four-agent parity; kit-only)
- [ ] ADR-008 (F-04) + ADR-005 (sweep) + ADR-004 (kit-only) followed
- [ ] MEM (before/after counts + zone list + G36 validation) · manifest `v_bounces[]` appended
- [ ] HITL-MEM-Approval → then REV-002 findings F-01..F-08 closed

---

## 17. References

- REV-002 (approved) §4 (findings), §6 (routing); US-000.BOLT-007 (approved)
- ADR-008 §3.1–§3.4, §3.9 (F-04); ADR-005 (sweep discipline + F-02); ADR-004 (kit-only)
- `Avenga-DevFlow.md:2413` (F-08 wording), `:1372` (allowlist defining sentence)

---

## 18. HITL-SPEC-Approval

> Draft until the Dev-validator (+ applicable domain owner) records
> `HITL-SPEC-Approval`. A material source change invalidates it — stop, revise,
> re-approve (G15). One V-Bounce never spans two SPEC revisions.

| Field | Value |
|-------|-------|
| **review.reviewers** | eugenio.serrano (dev_validator + tech_lead) |
| **review.decision** | **approved** |
| **review_ready_at** | `2026-08-22T20:32:13-03:00` |
| **review.started_at** | `2026-08-22T20:36:22-03:00` |
| **review.decided_at** | `2026-08-22T20:36:22-03:00` |
