---
id: "SPEC-260823-0121"
title: "Version-marker sweep 4.2 → 5.0 across distribution-kit/ (REV-004 F-09)"
date: "2026-08-23"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved" # draft | approved | blocked | obsolete
origin: "REV-004" # F-09 — the compliant finding that records this release-process step
bolt: "US-000.BOLT-013" # ⚠️ MANDATORY
revision: 1
associated_adrs:
  - "devflow/adrs/ADR-004-repository-partition-v2.md" # kit-only edits
prerequisites: []
risk_class: "low" # mirrors the Bolt
autonomy_level: "L3" # low → L3 default; deterministic doc sweep
turn_budget: "" # platform default (10 loops without green)
data_classification: "internal"
review_ready_at: "2026-08-23T01:23:00-03:00"
review: # HITL-SPEC-Approval — recorded by the human reviewer (§3.0); decision dictated by the human in conversation ("aprobado!") and transcribed by the agent
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - user: "eugenio.serrano"
      role: "dev_validator"
    - user: "eugenio.serrano"
      role: "tech_lead"
  started_at: "2026-08-23T01:23:26-03:00"
  decided_at: "2026-08-23T01:23:26-03:00"
  findings: []
  acknowledged_without_comment: true # must be true when findings is empty (§3.0)
  acknowledgment_reason: "Approved revision 1 against the approved Bolt US-000.BOLT-013, REV-004 (F-09) and ADR-004. The marker patterns (M1..M10) match the tree inventory; the residue classification (history + section numbers + normative text) is correct; no bare-4.2 sweep is defined; parity/G-count invariants set; gates n/a reasoned. Reviewer holds dev_validator and tech_lead (domain owner) — self-assigned, single-operator. V-Bounce authorized."
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs and headings (##) in
  English; prose content_language (en).

  DOGFOODING SPLIT: authored under v4.2 (root devflow/, ADR-006), own checkpoint
  HITL-SPEC-Approval, manifest schema_version 4.0. Implements US-000.BOLT-013 by
  editing the v5.0 PRODUCT (distribution-kit/, vocabulary AITL-*). Kit-only
  (ADR-004); the root tree inherits at the next §5.16 migration.

  ⚠️ DRAFT until HITL-SPEC-Approval. SPEC approval authorizes the V-Bounce; no
  code-run before it (G14).

  ⚠️ NEVER sweep a bare `4.2`: section references ("## 4.2", "§4.2") and
  historical statements ("removed in v4.2") share the shape. Only the marker
  patterns in §4 are replaced; the residue classification in §8 proves it.
-->

# SPEC-260823-0121 — Version-marker sweep 4.2 → 5.0 (REV-004 F-09)

| Field | Value |
|-------|-------|
| **Origin** | REV-004 (approved 2026-08-23 — F-09, compliant; executes the recorded release-process step) |
| **Bolt** | [US-000.BOLT-013](../functional/bolts/US-000.BOLT-013-version-marker-sweep.md) — HITL-BOLT-READY-Approval 2026-08-23T01:21:58 |
| **ADRs** | ADR-004 (kit-only) |
| **Risk / Autonomy** | low / L3 |

---

## 1. Objective

Align the kit's declared version with its v5 content: replace the version
**markers** in `distribution-kit/` from `4.2` to `5.0`, following the
repo's version-bump procedure (marker patterns only — never a bare `4.2`).
Every **historical statement** ("removed in v4.2", "DORMANT/RESERVED
(v4.2)") and every **section number** ("## 4.2", "### 4.2") stays as
written. The root `devflow/` tree stays v4.2 until the §5.16 migration at
release (ADR-004).

If NOT done: the kit distributes content that is v5-major (AITL, manifest
family v5, `HITL-*` legacy, no `H1–H6`) while stamping itself "4.2" — the
last residual inconsistency recorded by REV-004 F-09.

**Scope boundary:** markers only. No rule, checkpoint, guardrail or schema
changes; G-count stays 39.

---

## 2. Context

REV-004 F-09 (compliant) recorded that the version markers are the last
consistency item: the kit's content evolved to v5 (US-020/021 + REV-002/003
remediation), and the maintainer decided to release it as **5.0**. The
repo's version-bump procedure defines the safe marker patterns
(`v4.2`, `Methodology version:** 4.2`, `Agent version:** 4.2`,
`version: "4.2"`) and the check (grep the old version string across the
kit). This SPEC is the mechanical HOW for US-000.BOLT-013; the inventory
was built by a full-kit grep of the current tree.

---

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | `devflow/functional/bolts/US-000.BOLT-013-version-marker-sweep.md` | HITL-BOLT-READY-Approval ✓ 2026-08-23T01:21:58 |
| Origin REV | `devflow/reviews/REV-004-kit-self-containment-consistency-audit.md` | HITL-REV-Approval ✓ 2026-08-23T00:44:14 (closed) |
| Container | `devflow/functional/user-stories/US-000-non-functional.md` | no approval lifecycle ✓ |
| ADR | `devflow/adrs/ADR-004-repository-partition-v2.md` | HITL-ADR-Approval ✓ (accepted) |
| Procedure | repo root `AGENTS.md` "Version bump procedure" | repository convention (marker patterns) |
| Repository baseline | current working tree on branch `5.0` | — |

Pre-SPEC evidence gate: **all governed sources approved** — no draft input.
The edited files are product files in `distribution-kit/`.

---

## 4. Scope — marker patterns (replaced) vs residue (kept)

### Marker patterns (replace `4.2` → `5.0`)

| # | Pattern (exact) | Where | Count (to capture) |
|---|-----------------|-------|--------------------|
| M1 | `4.2` (single line, the whole file) | `devflow/VERSION` | 1 |
| M2 | `version: "4.2"` | methodology frontmatter | 1 |
| M3 | `**Enforcing:** Avenga DevFlow v4.2` | `GUARDRAILS.md:3` | 1 |
| M4 | `(normative source, v4.2)` | `GUARDRAILS.md:478` | 1 |
| M5 | `**Methodology version:** 4.2` | every `README.md` / `INDEX.md` under `distribution-kit/devflow/` (incl. `analysis/**`, `input/**`, `tests/**`, `metrics/`, `avenga-devflow/`, root `devflow/README.md`) — **templates never carry it** | ~60 (capture exact count) |
| M6 | `**Agent version:** 4.2 — implements methodology v4.2` | the four agent definitions | 4 |
| M7 | `# Avenga DevFlow v4.2 (Methodology)` | the four agent definitions (shared-body heading) | 4 |
| M8 | `follows the Avenga DevFlow v4.2 methodology` | `.github/agents/…agent.md` + `.opencode/agents/…md` descriptions | 2 |
| M9 | `(v4.2)` in the source-of-truth line | `AGENTS.md:6`, `ONBOARDING.md:15` | 2 |
| M10 | `Avenga DevFlow v4.2 — the complete methodology` | `avenga-devflow/INDEX.md:13` | 1 |

### Residue (kept as written — never matched by the patterns above)

- Historical: "removed in v4.2" (methodology §4.7, `README.md` Known
  Limitations, `tests/README.md`, `tests/uat/{README,TEMPLATE-UAT}`,
  `analysis/README.md`, ONBOARDING glossary), "DORMANT / RESERVED (v4.2)"
  (`tests/uat/README.md`, `tests/uat/INDEX.md`, `tests/uat/TEMPLATE-UAT.md`),
  "in v4.2 this whole layer is…" (`tests/uat/README.md`).
- Section numbers: `## 4.2 SPEC preparation and approval` (methodology),
  `### 4.2 — [Another domain / Category]` (`reviews/TEMPLATE-REV.md`).
- Normative convention text: "4.x keeps 4.0", "the family major may lead the
  methodology version" (§3.12), "every 4.x methodology version keeps it"
  (`metrics/README.md`), "versions up to 4.1" (§5.16).
- The root `devflow/` tree (ADR-004) — stays v4.2.

---

## 5. Prerequisites and baseline

- Baseline: current working tree on branch `5.0`; the four agent bodies are
  byte-identical except the sanctioned `agents-data/<agent>/` line (parity
  diff = 2 lines per pair) — the pre-edit baseline M6/M7 must preserve.
- No prior SPEC dependency.

---

## 6. Phases

### Phase A — file-level markers (M1–M4, M9, M10)

`devflow/VERSION` → `5.0`; methodology frontmatter `version: "5.0"`;
`GUARDRAILS.md` header and Related-Documents line; `AGENTS.md` and
`ONBOARDING.md` source-of-truth lines; `avenga-devflow/INDEX.md` row.

**Files modified:** `devflow/VERSION`, `devflow/avenga-devflow/Avenga-DevFlow.md`,
`devflow/GUARDRAILS.md`, `AGENTS.md`, `devflow/ONBOARDING.md`,
`devflow/avenga-devflow/INDEX.md`.

### Phase B — `**Methodology version:**` headers (M5)

Replace `**Methodology version:** 4.2` → `**Methodology version:** 5.0` in
**every** `README.md` and `INDEX.md` under `distribution-kit/devflow/` — by
pattern, not by file list (the grep in §4 is the inventory; any header the
grep missed is still covered because the replacement is pattern-based).
Capture the exact count of replaced files for the MEM.

**Files modified:** all `README.md` / `INDEX.md` under `distribution-kit/devflow/`
(~60 — exact count in the MEM).

### Phase C — the four agent definitions (M6, M7, M8), in lockstep

`**Agent version:** 4.2 — implements methodology v4.2` → `**Agent version:**
5.0 — implements methodology v5.0`; `# Avenga DevFlow v4.2 (Methodology)` →
`# Avenga DevFlow v5.0 (Methodology)`; description frontmatter "follows the
Avenga DevFlow v4.2 methodology" → v5.0 (2 files). All four files receive
the identical edits; re-run the parity diff afterwards — must stay at the
sanctioned 2 lines per pair.

**Files modified:** `CLAUDE.md`, `.agents/skills/avenga-devflow/SKILL.md`,
`.github/agents/AvengaDevFlow.agent.md`, `.opencode/agents/AvengaDevFlow.md`.

---

## 7. Acceptance criteria

- **AC-1:** `devflow/VERSION` = `5.0`.
- **AC-2:** `grep "Methodology version:**"` over `distribution-kit/` → every
  header reads `5.0`; zero read `4.2`.
- **AC-3:** the four agents in lockstep: `Agent version:** 5.0 — implements
  methodology v5.0`, heading `# Avenga DevFlow v5.0 (Methodology)`;
  descriptions updated (2 files).
- **AC-4 (residue classification):** every remaining `4.2`/`v4.2` hit in
  `distribution-kit/` is a historical statement or a section number — the
  full list is classified in the MEM.
- **AC-5:** G-count = 39×5; four-agent body parity = 2 lines per pair.
- **AC-6:** `git status` shows only `distribution-kit/` edits + root
  governance records (kit-only, ADR-004).

### AC mapping to source (measurable outcome)

| Source | How this SPEC satisfies it | Verifying test/evidence |
|--------|----------------------------|--------------------------|
| REV-004 F-09 | Phases A/B/C replace every marker | greps AC-1..AC-3 + residue classification AC-4 |
| Bolt §2 completion criteria | markers 5.0, history untouched | AC-4 classification list |
| Repo version-bump procedure | marker patterns only, never a bare sweep | the residue list proves nothing historical changed |

---

## 8. Testing strategy

Documentation product — verification replaces the test suite:

- **Marker greps:** `**Methodology version:** 4.2` → 0;
  `**Agent version:** 4.2` → 0; `# Avenga DevFlow v4.2 (Methodology)` → 0;
  `version: "4.2"` → 0; `**Enforcing:** Avenga DevFlow v4.2` → 0;
  `(normative source, v4.2)` → 0; `follows the Avenga DevFlow v4.2
  methodology` → 0.
- **Residue classification:** the complete post-sweep list of `4.2`/`v4.2`
  hits, each classified `history` or `section-number` (this is the proof the
  sweep never touched a bare occurrence).
- **Invariant checks:** G-count 39×5; four-agent body parity (2 lines per
  pair); `git status` kit-only.
- **Edge cases:** the methodology's `## 4.2` section heading and
  `TEMPLATE-REV.md`'s `### 4.2` must survive untouched (they match only a
  bare `4.2`, which no pattern replaces); the "removed in v4.2" family must
  survive untouched.

---

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | n/a — documentation product, no runtime | n/a |
| SAST / SBOM | n/a | n/a |
| Perf-smoke (p95/p99) | n/a | n/a |
| Prompt-injection scan | n/a | n/a |
| Secret-leak scan | pass — text-only edits | pass |
| Hallucination lint | pass — every edited string resolves on disk | pass |
| IP / license provenance | n/a | n/a |
| PII / DLP | n/a | n/a |
| Dependency-confusion | n/a | n/a |
| Test-first evidence | n/a — documentation-only; marker greps + residue classification are the evidence (§8) | n/a |
| Behavioral reproducibility | pass — re-running the greps from the SPEC + captured tree reproduces the results | pass |
| Bolt-manifest validation | pass — Bolt manifest validates against `manifest-v4-bolt.schema.json` | pass |

> Each gate ends `pass` / `waived` (ADR-NNN) / `n/a` (with reason) (§3.6).

---

## 10. Security and data

- Text-only edits to distributed documentation; `data_classification: internal`.
- No secrets, no new dependencies, no runtime surface.

---

## 11. Monitoring and observability

n/a — documentation product; the "observability" is the marker-grep and
residue-classification evidence in §8.

---

## 12. Migration, compatibility and rollback

- **Migration:** n/a — no schema, config or runtime change. The root tree
  keeps v4.2 until the §5.16 migration at release.
- **Compatibility:** n/a.
- **Rollback:** per-file git revert of the marker lines; canonical SPEC
  revision 1 remains valid for a re-run.

---

## 13. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| Blind replace hits a historical statement | 1 | 4 | marker patterns only (never a bare `4.2`); residue classification proves it |
| The four agents drift in lockstep | 2 | 4 | Phase C applies identical edits; parity diff must stay at 2 lines/pair |
| A header in a file the inventory missed | 1 | 2 | Phase B is pattern-based, not file-list-based; the post-sweep grep proves completeness |
| `## 4.2` section heading accidentally matched | 1 | 3 | no pattern contains a bare `4.2`; residue list shows it untouched |

---

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| Sweep by marker pattern, never by bare `4.2` | section numbers and history share the shape — the repo's own version-bump procedure warns about exactly this |
| Include the agents' shared-body heading (`# Avenga DevFlow v4.2 (Methodology)`) | it is the version marker the four-agent sync procedure greps for; leaving it would make the parity check and the marker check disagree |
| Root tree untouched (stays 4.2) | ADR-004 partition; the root receives v5 at the §5.16 migration, where `VERSION` is written last |

---

## 15. Stop conditions

- Any edit that would change a rule, checkpoint, guardrail or schema → stop,
  revise the Bolt/SPEC, re-approve (G15).
- A `4.2`/`v4.2` hit after the sweep that is neither history nor a section
  number → stop; classify and extend the inventory, revise the SPEC,
  re-approve.
- Parity diff after Phase C exceeds 2 lines per pair → stop; fix the
  lockstep before proceeding.

---

## 16. Definition of Done (DoD)

- [ ] All Phase A/B/C edits applied
- [ ] AC-1..AC-6 verified (marker greps at zero, residue classification, parity, G-count, git status)
- [ ] `US-000.BOLT-013` manifest valid (`manifest-v4-bolt.schema.json`)
- [ ] MEM created in `devflow/memory/` (exactly one per V-Bounce)
- [ ] Manifest `v_bounces[]` entry appended in `devflow/metrics/bolts/`
- [ ] HITL-MEM-Approval recorded

---

## 17. References

- `devflow/reviews/REV-004-kit-self-containment-consistency-audit.md` (F-09)
- `devflow/functional/bolts/US-000.BOLT-013-version-marker-sweep.md`
- `devflow/adrs/ADR-004-repository-partition-v2.md`

---

## 18. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-23 | eugenio.serrano | Initial draft (revision 1) |
| 2026-08-23 | eugenio.serrano | `HITL-SPEC-Approval` recorded (approved) — V-Bounce authorized |

---

## 19. HITL-SPEC-Approval

> **Avenga DevFlow §2.4.1, §3.0.** This SPEC remains a draft until the
> Dev-validator (+ applicable domain owners) records `HITL-SPEC-Approval`
> (in the `review` frontmatter block). Bolt approval (`HITL-BOLT-READY-Approval`)
> authorizes SPEC preparation; **SPEC approval** authorizes the V-Bounce. A
> material source change invalidates this approval — stop, revise, re-approve
> (G15).

| Field | Value |
|-------|-------|
| **review.reviewers** | eugenio.serrano (dev_validator + tech_lead) |
| **review.decision** | **approved** |
| **review_ready_at** | `2026-08-23T01:23:00-03:00` |
| **review.started_at** | `2026-08-23T01:23:26-03:00` |
| **review.decided_at** | `2026-08-23T01:23:26-03:00` |
| **Findings** | none — `acknowledged_without_comment: true` (see frontmatter) |
