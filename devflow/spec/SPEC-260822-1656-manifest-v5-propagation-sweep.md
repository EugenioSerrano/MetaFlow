---
id: "SPEC-260822-1656"
title: "Complete the v5 manifest propagation across the kit reference/template tier (A+B+C) with an ADR-005 phrase-family sweep"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
status: "approved"
origin: "US-020"
bolt: "US-020.BOLT-004"
revision: 2
associated_adrs:
  - "devflow/adrs/ADR-008-aitl-approval-precept.md"
  - "devflow/adrs/ADR-005-removal-completeness-phrase-family-sweep.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
prerequisites: ["SPEC-260822-1546", "SPEC-260822-1607", "SPEC-260822-1622"]
risk_class: "medium"
autonomy_level: "L3"
turn_budget: ""
data_classification: "internal"
review_ready_at: "2026-08-22T17:13:42-03:00"
review: # HITL-SPEC-Approval (rev 2) — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "dev_validator"}]
  started_at: "2026-08-22T17:22:49-03:00"
  decided_at: "2026-08-22T17:22:49-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved rev 2: kit-wide location set (every .md under distribution-kit) + complete phrase family incl. bucket D (Manifest family v4 / manifest v4 / v4 schema/example). Allowlist: §5.16 recipe, agents' upgrade notes, artifact review.reviewers {user,role}, methodology v4.2, sev4. §3.12 example must stay GREEN; four-agent sync + G-count 39x5. Ends the partial-sweep regress."
---

<!--
  LANGUAGE POLICY (§3.15): schema in English; prose content_language (en).
  Kit-only (ADR-004); root untouched. This Bolt finishes the v5 manifest
  propagation across the reference/template tier that BOLT-001 (schemas) and
  BOLT-002 (core description) left on v4. It does NOT convert this repo's
  manifests (that runs when the root migrates to v5.0).
-->

# SPEC-260822-1656 — v5 manifest propagation sweep (BOLT-004)

| Field | Value |
|-------|-------|
| **Origin** | [US-020](../functional/user-stories/US-020-manifest-aitl-evolution.md) (approved) |
| **Bolt** | [US-020.BOLT-004](../functional/bolts/US-020.BOLT-004-manifest-v5-propagation-sweep.md) (approved) |
| **ADRs** | ADR-008 (v5 record shape), ADR-005 (phrase-family sweep), ADR-004 (kit-only) |
| **Risk Class** | medium · **Autonomy** L3 |
| **Revision** | 1 · **Prereq:** BOLT-001 + BOLT-002 + BOLT-003, all Done |

---

## 1. Objective

Make the kit **internally consistent on the v5 manifest**: every place that
*describes* the manifest speaks v5, and the reference example an adopter reads
**validates against the v5 schema** the kit ships. BOLT-001 shipped the v5
schemas/templates and BOLT-002 aligned the core §3.12 description, but a whole
reference/template tier — the manifest reference doc, the artifact templates and
the per-folder READMEs, plus the §3.12 embedded example — still describes the
manifest as v4.

**Why:** an adopter reading `metrics/README.md` today is told the deleted
`manifest-v4-*.schema.json` files "remain the contract", and the §3.12 example
they would copy **fails** the v5 schema (no `mode`, `{user,role}` approver). **If
not done:** US-020 ships a v5 schema with v4 documentation around it — a mixed,
self-contradicting kit.

**Discovered by** US-020.BOLT-003's AC-3 kit-wide sweep (rev-1 finding of this Bolt).

**Revision 2 (kit-wide).** BOLT-004's own rev-1 sweep then surfaced that the
*phrase* `Manifest family v4` / `manifest v4` / `v4 schema` — distinct from the
array name (`hitl_approvals`) and the schema filenames (`manifest-v4-*`), both
already **zero** kit-wide — persists ~19× **outside** the reference/template
tier: the **core §3.12** heading + body, the top-level `README`/`GUARDRAILS`,
`bugs/README`, `incidents/TEMPLATE-INCIDENT`, and the `SKILL.md` description. The
rev-1 phrase family and location set were both incomplete. Rev 2 makes the sweep
**kit-wide** with the **complete phrase family**, ending the partial-sweep
regress (the exact pattern ADR-005 exists to kill).

---

## 2. Context

The v5 manifest change has two facets — an **array rename**
(`hitl_approvals[]`→`checkpoint_approvals[]`) and an **approver reshape**
(`{user,role}`→`{actor,role,model}` + entry `mode`) — plus a **schema-version /
filename** bump (`manifest-v4-*`→`manifest-v5-*`, `"4.0"`→`"5.0"`). Those landed
in the schemas (BOLT-001) and the core text (BOLT-002/003) but not in the tier
below. This Bolt propagates all three across that tier and **proves completeness
with an ADR-005 phrase-family sweep** over a fixed location set with an explicit
allowlist.

---

## 3. Source inventory (pre-SPEC evidence gate)

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | `US-020.BOLT-004-manifest-v5-propagation-sweep.md` | HITL-BOLT-READY-Approval ✓ |
| Parent US | `US-020-manifest-aitl-evolution.md` | HITL-US-Approval ✓ |
| Prereq Bolts | BOLT-001 (schemas) + BOLT-002 (core desc) + BOLT-003 (§5.16 recipe) | **Done** ✓ |
| ADRs | ADR-008, ADR-005, ADR-004 | accepted ✓ |
| Baseline | branch `5.0`, HEAD `97125e7` (+ BOLT-001/002/003 kit changes in the working tree) | — |

Pre-SPEC evidence gate: **all governed sources approved; prereq Bolts Done.** No
active-ADR conflict (§3.5).

---

## 4. The change to apply — three buckets

### Bucket A — array rename (`hitl_approvals` → `checkpoint_approvals`)
In prose that describes the **current** manifest, rename the approval array. This
is a mechanical string rename; the surrounding meaning is unchanged.

### Bucket B — approver reshape (+ `mode`), so the reference example validates
Where the manifest **approver** or the **§3.12 embedded example** is shown, adopt
the v5 shape: each `checkpoint_approvals[]` entry gains `mode` (`"human"` for the
worked example — no agent approver), and every `decided_by[]` element becomes
`{actor: "human:<user>", role, model: null}`. The **§3.12 embedded example must
validate GREEN** against `manifest-v5-bolt.schema.json`.
**Explicitly NOT changed:** the artifact-level `review.reviewers[].user` contract
stays `{user, role}` — the `user`→`actor` projection happens only at the manifest
boundary (§3.12). The artifact templates' `review:` frontmatter comments
(`reviewers: [] # [{user, role}]`) are correct and are on the allowlist.

### Bucket C — schema filename / version labels
`manifest-v4-*.schema.json` links (files BOLT-001 **deleted**) → `manifest-v5-*`;
"Schema family v4" → v5; `schema_version "4.0"`/`"4.0"` labels → `"5.0"`.

### Bucket D — the `Manifest family v4` / `manifest v4` phrase (rev 2)
Every prose reference to the **current** manifest family by version — `Manifest
family v4`, `Manifest v4`, `manifest v4`, `v4 schema(s)`, `Schema v4 example`,
`manifest v4 entry|update` — reads **v5**. This is the phrase rev 1 missed; it
lives in the core §3.12 (heading + body), the top-level docs, `bugs/README`,
`incidents/TEMPLATE-INCIDENT` and an agent description — not only the
reference/template tier.

---

## 5. Scope — fixed location set (the ADR-005 sweep domain)

### In scope (kit) — location set = every `.md` under `distribution-kit/` (rev 2)
The ADR-005 sweep domain is the **whole kit**: every `.md` under
`distribution-kit/` — the methodology `Avenga-DevFlow.md`, `GUARDRAILS.md`,
`ONBOARDING.md`, the top-level `README.md`, every folder `README`/`TEMPLATE-*`,
and the four platform agents (`CLAUDE.md`, `SKILL.md`, `AvengaDevFlow.agent.md`,
`AvengaDevFlow.md`) — minus the allowlist below.

Rev 1 already cleared the reference/template tier for buckets A/C and reshaped the
§3.12 example (B). Rev 2 adds **bucket D** (the `Manifest family v4` phrase)
everywhere it remains — the core §3.12 heading + body, `README`, `GUARDRAILS`,
`bugs/README`, `incidents/TEMPLATE-INCIDENT`, and the `SKILL.md` description — plus
relabelling the §3.12 example `Schema v4 example` → `Schema v5 example`.

**Care in `Avenga-DevFlow.md`:** the §5.16 conversion recipe legitimately names
the v4 source (`3.0`→`4.0`, `4.0`→`5.0`, `hitl_approvals`); it is allowlisted and
edited line-by-line, never by a blanket file replace.

**Four-agent sync (AC-6):** any edit that lands in a shared methodology body
region keeps the four agents byte-identical and G-count 39×5. Platform-specific
frontmatter (e.g. `SKILL.md`'s `description:`) is not byte-synced across agents
and is fixed per file.

### Allowlist — v4 references that MUST remain (legitimate v4-source naming)
- `Avenga-DevFlow.md` **§5.16** conversion recipe — `hitl_approvals`, `{user,role}`,
  `schema_version "4.0"` name the v4 source being converted (BOLT-003).
- The **four agents'** Upgrade-Protocol conversion notes (`CLAUDE.md`,
  `.agents/skills/avenga-devflow/SKILL.md`, `.github/agents/AvengaDevFlow.agent.md`,
  `.opencode/agents/AvengaDevFlow.md`) — same v4-source naming (BOLT-003).
- Every artifact template `review:` frontmatter `reviewers: [] # [{user, role}]`
  — the artifact review contract stays `{user, role}` in v5.
- Historical `HITL-*` checkpoint names everywhere — the `HITL-*`→`AITL-*` rename
  is a **separate US**, out of scope here.
- The **methodology version** `v4.2` (the operating maintenance partition — not a
  manifest reference), and the migration examples `3.0`→`4.0` / `4.0`→`5.0`.
- Incident **severity** codes `sev1`–`sev4` (not a manifest version).
- The §5.16 conversion recipe + the four agents' Upgrade-Protocol notes naming the
  *v4 source* being converted (G36).

### Out of scope
- The v5 schemas/templates JSON (BOLT-001); the core §3.12 structure prose +
  §5.16 recipe (BOLT-002/003); the `HITL-*`→`AITL-*` rename (separate US); the
  root `devflow/` (ADR-004); converting this repo's actual manifests.

---

## 6. Phases

- **Phase A — mechanical rename (bucket A)** across the 12 prose files. ~1h.
- **Phase B — reshape (bucket B):** the §3.12 example entries + `metrics/README.md`
  approver prose + line ~1589; then validate the example against the v5 schema. ~1h.
- **Phase C — schema labels (bucket C):** links + "Schema family v4" +
  `schema_version` labels across the reference/template docs. ~0.5h.
- **Phase D — Verification (GREEN):** the ADR-005 phrase-family sweep (§8) + the
  example validation + four-agent sync/G-count regression guard. ~0.5h.

---

## 7. Acceptance criteria

- **AC-1 (A complete):** across the in-scope location set, no prose describing the
  current manifest calls the array `hitl_approvals[]`; it reads
  `checkpoint_approvals[]`.
- **AC-2 (B — shape + validates):** the §3.12 embedded example shows `mode` +
  `{actor,role,model}` on every approval entry and **validates GREEN** against
  `manifest-v5-bolt.schema.json`; `metrics/README.md` approver prose and the
  canonical-identity line name the v5 shape. The artifact `review.reviewers[].user`
  contract is unchanged (`{user, role}`).
- **AC-3 (C complete):** no in-scope document links to a `manifest-v4-*.schema.json`
  file; "Schema family v4" reads v5; `schema_version` labels read `"5.0"`.
- **AC-4 (ADR-005 sweep clean, kit-wide):** the phrase-family sweep (§8) over
  **every `.md` under `distribution-kit/`**, minus the allowlist, returns
  **zero** residual v4 manifest references for every pattern. Recorded in the MEM
  as an absence.
- **AC-5 (allowlist intact):** the §5.16 recipe, the four agents' upgrade notes and
  every artifact `review:` `{user, role}` comment are **unchanged** (the sweep does
  not touch them).
- **AC-6 (kit-only + four-agent sync):** `git status` shows only
  `distribution-kit/` + governance records; root untouched; four-agent G-count
  **39×5**; any shared methodology-body edit stays byte-identical across the four
  agents (platform frontmatter excepted).
- **AC-7 (manifest):** the BOLT-004 manifest gets its `v_bounces[]` entry and validates.
- **AC-8 (phrase family, rev 2):** no `.md` under `distribution-kit/` contains
  `Manifest family v4` / `Manifest v4` / `manifest v4` / `v4 schema(s)` /
  `Schema v4 example` / `manifest v4 entry|update` describing the current family
  (allowlist excepted). The core §3.12 heading reads `Manifest family v5` and the
  §3.12 example label reads `Schema v5 example`.

---

## 8. Testing strategy — the ADR-005 phrase-family sweep

Deterministic (documentation + one schema validation).

**RED (before):** grep across the location set finds residual v4 references
(≥30 `hitl_approvals`, ≥12 `manifest-v4`, `Schema family v4`, several
`schema_version "4.0"`, `{user,role}` in the §3.12 example); the extracted §3.12
example **fails** v5 validation.

**GREEN (after):** the phrase-family sweep below returns **0** over the location
set minus the allowlist; the §3.12 example **validates GREEN** against the real v5
schema; four-agent G-count 39×5; `git status` kit-only. Record the exact commands
+ counts in the MEM (as an absence, ADR-005).

**Phrase family (each expected 0 outside the allowlist), over every `.md` under
`distribution-kit/`:**
- `hitl_approvals`
- `manifest-v4`
- `Schema family v4`
- `schema_version[ :]"4\.0"` (label form)
- the manifest approver shape `{user, role}` (excluding the artifact `review:`
  frontmatter comments, which are allowlisted)
- **(rev 2)** `Manifest family v4` / `manifest family v4`
- **(rev 2)** `Manifest v4` / `manifest v4`
- **(rev 2)** `v4 schema` / `Schema v4` / `v4 schemas` / `v4 example` /
  `v4 entry` / `v4 update`

**Positive check:** the §3.12 example, extracted and validated with `jsonschema`
(draft 2020-12) against `manifest-v5-bolt.schema.json`, is GREEN; a fabricated
non-conforming variant is RED (reuse the BOLT-003 validation harness pattern).

---

## 9. Quality gates

Documentation/internal → unit/integration, SAST/DAST/SBOM, perf, IP, PII,
dep-confusion, test-first: `n/a`. hallucination-lint (links resolve; the example
validates against the real v5 schema), behavioral-reproducibility (deterministic
sweep), bolt-manifest-validation: `pass`. prompt-injection, secret-leak: `pass`
(no runtime surface).

---

## 10. Security and data

Governance/documentation text only; no runtime boundary. Data `internal`.

---

## 11. Migration, compatibility, rollback

Additive documentation alignment; no behavioral change. Rollback: revert the kit
commit; root untouched.

---

## 12. Risk matrix

| Risk | Prob | Impact | Mitigation |
|------|------|--------|------------|
| Sweep misses a file / pattern (partial rename recurs) | 2 | 4 | ADR-005 fixed location set + phrase family; AC-4 requires 0 over the whole set |
| Over-reach: changes the artifact `review.reviewers` contract | 2 | 3 | Bucket B + allowlist explicitly exclude it; AC-5 checks it intact |
| The §3.12 example still doesn't validate | 1 | 4 | AC-2 validates the extracted example against the real v5 schema |
| Agent-body drift when editing shared regions (rev 2) | 2 | 3 | Bucket D touches the `SKILL.md` description (platform frontmatter, not synced); any shared body edit stays byte-identical; AC-6 re-checks four-agent sync + G-count 39×5 |

---

## 13. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| One Bolt for A+B+C (not three) | The files overlap heavily (`metrics/README.md`, `TEMPLATE-BOLT/US/TC`); splitting would edit them 2–3× |
| Prove completeness by an ADR-005 sweep phrased as an absence | This gap was itself a partial-sweep miss; the absence assertion over a fixed set is the standard that prevents recurrence |
| Keep the artifact `review.reviewers` contract `{user, role}` | §3.12 projects `user`→`actor` at the manifest boundary; changing the artifact contract is a different, unapproved change |
| `mode: "human"` in the worked/§3.12 example | The example has no agent approver; `human` is the safe default (ADR-008) |

---

## 14. Stop conditions

- The §3.12 example fails to validate after reshaping → the reshape is wrong; stop,
  fix, re-validate.
- Any root `devflow/` file appears in the diff → stop, revert, record (root is
  out of scope, ADR-004). Agent edits are limited to bucket D + shared-body sync.
- The sweep still returns non-zero after edits → not GREEN; continue within the
  turn budget, else stop + MEM with the residual list.
- A governed source changes materially (G15) → stop, revise, re-approve.

---

## 15. Definition of Done

- [ ] Phases A–D · AC-1..AC-8 pass
- [ ] GREEN (ADR-005 sweep returns 0 outside the allowlist; §3.12 example validates; kit-only; G-count 39×5)
- [ ] ADR-005 (sweep) + ADR-008 (shape) + ADR-004 (kit-only) followed
- [ ] MEM (sweep evidence as an absence + example validation) · manifest `v_bounces[]` appended
- [ ] HITL-MEM-Approval → then US-020 fully delivered (all four Bolts Done)

---

## 16. References

- US-020, US-020.BOLT-004 (approved); BOLT-001/002/003 (Done)
- ADR-004/005/008; §3.12 (Manifest Family), §5.16 (Upgrade Protocol)
- The v5 schemas (BOLT-001) the §3.12 example validates against
- BOLT-003 rev-2 finding (MEM-260822-1647 §8) — the origin of this Bolt

---

## 17. HITL-SPEC-Approval

> Draft until the Dev-validator records `HITL-SPEC-Approval`. A material source
> change invalidates it — stop, revise, re-approve (G15).

**Revision 1** — approved 2026-08-22T16:59:02-03:00 (eugenio.serrano,
dev_validator). Scoped to the reference/template tier (buckets A/B/C). Its own
sweep then found the `Manifest family v4` phrase persisting kit-wide.

**Revision 2** — broadens the location set to **every `.md` under
`distribution-kit/`** and adds **bucket D** (the complete `Manifest family v4`
phrase family), per the maintainer's decision to end the partial-sweep regress.
The rev-1 edits stand; the V-Bounce completes against rev 2.

| Field | Value (rev 2) |
|-------|-------|
| **review.reviewers** | eugenio.serrano (dev_validator) |
| **review.decision** | **approved** |
| **review_ready_at** | `2026-08-22T17:13:42-03:00` |
| **review.started_at** | `2026-08-22T17:22:49-03:00` |
| **review.decided_at** | `2026-08-22T17:22:49-03:00` |
