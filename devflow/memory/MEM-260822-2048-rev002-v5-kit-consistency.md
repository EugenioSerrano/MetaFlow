---
id: "MEM-260822-2048"
title: "Remediate REV-002 — v5.0 kit consistency: 8 findings closed (AITL wording, 26 HITL residues, schema_version, AREV/xref/encoding)"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
bolt: "US-000.BOLT-007"
spec: "SPEC-260822-2032"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "137a5b5"
applied_adrs:
  - "devflow/adrs/ADR-008-aitl-approval-precept.md"
  - "devflow/adrs/ADR-005-removal-completeness-phrase-family-sweep.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "US-000.BOLT-007-rev002-v5-kit-consistency-remediation.json"
diff_ref: ""
review_ready_at: "2026-08-22T20:48:15-03:00"
review: # HITL-MEM-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers:
    - user: "eugenio.serrano"
      role: "dev_validator"
  started_at: "2026-08-22T20:51:11-03:00"
  decided_at: "2026-08-22T20:51:11-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Inspected the kit diff (~30 files), the zone-scoped absence sweep (0 non-allowlisted HITL), the 5-manifest validation, the G36 migrated-HITL check, four-agent parity 39×5, and the kit-only git status. The 8 REV-002 findings are closed and the wording aligns to ADR-008. The F-04 mechanic refinement and the dot-dir self-correction are documented and acceptable; no SPEC revision needed. V-Bounce GREEN — approved."
---

<!--
  LANGUAGE POLICY (§3.15): schema/headings English; prose content_language (en).
  DOGFOODING SPLIT: this MEM is authored under the v4.2 operating methodology
  (root devflow/), so its checkpoints are HITL-* and its manifest is 4.0. It
  edits the v5.0 PRODUCT (distribution-kit/), whose vocabulary is AITL-*.
-->

# MEM-260822-2048 — Remediate REV-002 (v5.0 kit consistency)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | [US-000.BOLT-007](../functional/bolts/US-000.BOLT-007-rev002-v5-kit-consistency-remediation.md) |
| **SPEC**        | [SPEC-260822-2032](../spec/SPEC-260822-2032-rev002-v5-kit-consistency.md) revision 1 |
| **V-Bounce**    | 1 |
| **ADRs**        | ADR-008 (§3.1–§3.4 precept — F-04), ADR-005 (phrase-family sweep — F-01/F-02), ADR-004 (kit-only) |

---

## 1. Executive summary

This V-Bounce closed all eight findings of the approved **REV-002** in the v5.0 kit
(`distribution-kit/`) as one allowlist-aware documentation pass, and it is **GREEN**.
The two substantive fixes: **F-04** aligned the checkpoint-governance wording to the
already-accepted **ADR-008** — the §3.0 charter tables, `GUARDRAILS.md:18` and
`AGENTS.md:7/36` no longer say "human-only / never delegated to AI / always a named
human" but "an actor, **human by default**, a virtual DevFlow Agent only by explicit
valid configuration", with the hard identity rules (no self-approval, safe default,
critical/regulatory ceiling) preserved; and **F-03** corrected the §3.12
self-contradiction so `schema_version` reads `5.0`. The mechanical **F-01** renamed
the **26** non-allowlisted `HITL-*` residues (25 language-policy + T12) to `AITL-*`,
and **F-05/F-06/F-07/F-08** fixed the `§2.15→§3.0` mis-citation (5 places), gave AREV
`cancelled` a home in the README lifecycle table and the INDEX, fixed the mojibake
example comment (now English), and replaced "the Unit" with "release suite". The
**F-02** verification correction proved its worth: the completeness sweep now excludes
the allowlist **by zone**, and it returns **zero** non-allowlisted `HITL` (27 remain,
all allowlist). One surprise during execution — the first sweep script under-matched
because Python's `glob('**')` silently skips dot-directories (`.agents/.github/.opencode`);
the count assertion (24 expected, 21 found) caught it immediately and the run was
completed with `os.walk`. The five manifest examples still validate, a migrated
`HITL-*` manifest still validates (G36), the four agents stay byte-identical in their
shared bodies (G-count 39×5), and the change is kit-only.

---

## 2. Implemented phases

### Phase A — substantive alignment (F-04, F-03)
- **F-04:** in `Avenga-DevFlow.md` the two §3.0 checkpoint-table column headers
  `Human-only checkpoint` → `Human by default`, and a note added after the tables
  stating the ADR-008 precept (virtual agent only by valid config; critical/regulatory
  human; safe default). In `GUARDRAILS.md` the checkpoint-map intro sentence and the
  "(the human stops…)" header parenthetical were reworded to "an actor — a human by
  default…". In `AGENTS.md` lines 7 and 36 the "mandatory human checkpoint" /
  "always a named human" absolutes became "an actor, human by default…". The four
  platform agents already carried the correct AITL wording and were **not** touched.
- **F-03:** the `Avenga-DevFlow.md` §3.12 rule bullet "`schema_version` is exactly
  `4.0` for this family …" was rewritten to `5.0`, clarifying that the manifest family
  carries its own major (bumped on the v4→v5 schema change) and may lead the
  methodology version.

### Phase B — sweep + hygiene (F-01, F-05, F-06, F-07, F-08)
- A byte-preserving, count-asserted script renamed the 26 non-allowlisted `HITL-*`
  tokens to `AITL-*` (24 backtick `` `HITL-*-Approval` `` + tests/README `` `HITL-*` `` +
  GUARDRAILS T12), leaving every §4a allowlist zone untouched; the `§2.15/ADR`
  citation → `§3.0/ADR-008` in the methodology and all four agents; the AREV
  `cancelled` row + INDEX bucket added; the mojibake JSON comment replaced with an
  English one; and "the Unit will cover it" → "a later release suite will cover it".

### Phase C — verification (GREEN)
- The zone-scoped absence sweep (F-02), the five-manifest validation, the G36
  migrated-`HITL-*` validation, the four-agent byte diff, the G-count and the kit-only
  `git status` — all recorded in §9.

---

## 3. Files created

| File | Purpose |
|------|---------|
| _(none in the product)_ | This V-Bounce only edits existing kit files. Governance records (MEM/SPEC/Bolt/manifest) live in root `devflow/` per the dogfooding split. |

---

## 4. Files modified

| File(s) | Description of change |
|---------|----------------------|
| `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md` | F-04 (2 table headers → "Human by default" + precept note), F-03 (§3.12 `schema_version` → 5.0), F-01 (2 language-policy tokens), F-05 (§2.15→§3.0) |
| `distribution-kit/devflow/GUARDRAILS.md` | F-04 (checkpoint-map intro reworded to "human by default"), F-01 (T12 token), F-08 ("release suite") |
| `distribution-kit/AGENTS.md` | F-04 (lines 7 & 36 → "an actor, human by default"), F-01 (language-policy token) |
| `distribution-kit/{CLAUDE.md, .agents/skills/…/SKILL.md, .github/agents/AvengaDevFlow.agent.md, .opencode/agents/AvengaDevFlow.md}` | F-01 (language-policy token) + F-05 (§2.15→§3.0) — identical across all four (parity preserved) |
| `distribution-kit/devflow/adversarial-reviews/{README.md, INDEX.md}` | F-06 (AREV `cancelled` lifecycle row + `⛔ Cancelled` INDEX bucket) |
| `distribution-kit/devflow/metrics/TEMPLATE-MANIFEST-BOLT.json` | F-07 (mojibake comment → "Add explicit concurrency handling.") |
| `distribution-kit/devflow/{README.md, ONBOARDING.md, tests/test-cases/README.md, tests/test-cases/TEMPLATE-TC.md, functional/user-stories/TEMPLATE-US.md}` | F-01 (language-policy token) |
| 13 × `distribution-kit/devflow/analysis/**/TEMPLATE-*.md` | F-01 (language-policy token) |

Governance records updated (root, v4.2): `functional/INDEX.md`, `reviews/INDEX.md`,
the Bolt + its manifest, the SPEC, and this MEM.

---

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
| _(none)_ | | |

---

## 6. Files deleted

| File | Reason |
|------|--------|
| _(none)_ | |

---

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| F-04: header → "Human by default" + a precept note (kept the ✅ cells) | Minor refinement of SPEC §5.1 ("Approver actor" + per-cell "human by default¹"): same AC-1 outcome (removes the "human-only" absolute, states the ADR-008 precept) with far lower edit risk — no need to rewrite 13 non-unique `✅` cells across two tables |
| Verify by allowlist **zone**, never by the `HITL-*` token (F-02) | Root cause of the earlier false-GREEN; the zone sweep returned 0 and would have caught the residue in the first place |
| Sweep with count assertions per rule | Catches over/under-match against the allowlist deterministically — it caught the dot-dir glob miss on the spot |
| F-07 example → English | Kit `LANGUAGE` is `en`; the shipped example should model the kit's own language |
| Four platform agents left untouched by F-04 | They already state "human by default, virtual by valid config" (verified); editing them would risk parity |

---

## 8. Deviations and assumptions

- **F-04 mechanic refined vs SPEC §5.1** (documented above, §7): the outcome and AC-1
  are satisfied; the difference is implementation shape, not scope — no SPEC revision
  required (no governed source changed, G15 not triggered).
- **No new decision introduced:** every edit aligns to an already-governing artifact
  (ADR-008, the v5 schema, the §3.15 vocabulary), per the SPEC.
- **Enabling** virtual approvers (registry/roster/Coordinator/pilot) remains out of
  scope (ADR-008 §3.9, later USs) — this Bolt only states the precept correctly.

---

## 9. Verification evidence

### Zone-scoped absence sweep (F-02) — GREEN as an absence
```
HITL in distribution-kit (.md + .json), total: 27  (was 53; 26 residue removed)
Zone-scoped sweep: HITL in .md MINUS allowlist zones
  (schema .json whole-file · G05 rows · §5.16/upgrade "historical/preserved" ·
   "Human-in-the-Loop" defining sentences · H1–H6)
  => NON-ALLOWLISTED RESIDUE: 0   (SWEEP GREEN)
```

### Rename counts (asserted)
```
F-01a `HITL-*-Approval` → `AITL-*-Approval`: 24 (21 via glob + 3 dot-dir agents via os.walk)
F-01b tests/test-cases/README.md `HITL-*`: 1 · F-01c GUARDRAILS T12 `HITL-*`: 1   (F-01 total 26)
F-05 (AITL, §2.15/ADR) → (AITL, §3.0/ADR-008): 5
F-03 schema_version 4.0→5.0: 1 · F-04 "Human-only checkpoint"→"Human by default": 2 + note
F-08 "the Unit"→"release suite": 1
```

### Manifest validation + G36
```
5/5 TEMPLATE-MANIFEST-*.json validate against manifest-v5-{bolt,us,tc}.schema.json (format-checked)
F-07: TEMPLATE-MANIFEST-BOLT.json comment = "Add explicit concurrency handling." (no mojibake), still valid
AC-8 (G36): a migrated `HITL-US-Approval` checkpoint_approvals entry still validates → YES
```

### Four-agent parity + G-count
```
Shared methodology bodies: only pre-existing exempt-zone lines differ (tool names,
  todo/memory wording, agents-data folder); no HITL/§2.15/human-only/schema_version divergence
G-count: GUARDRAILS 39 · CLAUDE 39 · SKILL 39 · AvengaDevFlow.agent 39 · AvengaDevFlow 39  (39×5)
```

### Spot-checks
```
F-03: "5.0 for this family" 1 · "4.0 for this family" 0
F-04: "Human by default" 3 (Avenga) · "Human-only checkpoint" 0 · "always a named human" 0 (AGENTS)
F-05: "§2.15/ADR" 0 · "§3.0/ADR-008" 5
F-06: AREV README `cancelled` row present · INDEX "⛔ Cancelled" bucket present
```

### Kit-only (ADR-004)
```
git status --short: product edits all under distribution-kit/; the only root/ changes
are this V-Bounce's governance records (REV-002, SPEC, MEM, Bolt+manifest, the two INDEXes).
No root framework file touched.
```

### Gates
- unit/integration, SAST/DAST/SBOM, perf, IP, PII, dep-confusion, test-first,
  secret-leak, prompt-injection: **n/a** (documentation, no code / no reachable surface).
- hallucination-lint (refs resolve; `§2.15`→`§3.0` corrected), behavioral-reproducibility
  (deterministic sweep), bolt-manifest-validation: **pass**.

### BUG V-Bounce evidence
n/a (not a BUG Bolt).

---

## 10. Manual interventions

None on product content — all edits were agent-generated (two count-asserted scripts +
a structured-edit script). No human code fallback. The first F-01 script pass stopped on
its own assertion (dot-dir glob miss); it was re-run with `os.walk` — an agent
self-correction surfaced by the verification, not a manual patch.

---

## 11. Evidence links

- **Diff / PR:** none yet (uncommitted; 5.0 branch). Commit only on explicit user request (G34).
- **Commit:** baseline `137a5b5` (parent of these edits).
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-000.BOLT-007-rev002-v5-kit-consistency-remediation.json`.

---

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~1h (three scripts + verification) |
| V-Bounce number | 1 |
| Tests created | verification suite: zone-scoped absence sweep + 5-manifest validation + G36 check + four-agent diff + G-count |
| AI-generated code | 100% (scripts + edits); no human fallback |
| First-pass approval | pending (this MEM) |

---

## 13. Pending items and stubs

- [ ] On `HITL-MEM-Approval` → **REV-002 findings F-01..F-08 closed**; then
      `HITL-BOLT-DONE-Approval` marks US-000.BOLT-007 `Done`, and REV-002 can close.
- [ ] Commit the kit + governance records when the user asks (G34).
- [ ] (Later USs, ADR-008 §3.9) enabling virtual approvers — the wording is now ready for it.

---

## 14. HITL-MEM-Approval

> **Avenga DevFlow §2.12, §3.0.** Created by the agent, no mutable status,
> **never self-approved**. The executing Dev-validator inspects the kit diff, the
> zone-scoped absence sweep, the manifest/G36 validation, this MEM and the manifest,
> and records `HITL-MEM-Approval` here and in the manifest's `hitl_approvals[]`.

| Field | Value |
|-------|-------|
| **Reviewers (executing Dev-validator; QA/Sec/domain optional)** | eugenio.serrano |
| **Roles** | dev_validator |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-22T20:48:15-03:00` |
| **review.started_at** | `2026-08-22T20:51:11-03:00` |
| **review.decided_at** | `2026-08-22T20:51:11-03:00` |
| **Review evidence** | kit diff (~30 files), zone-scoped sweep = 0, 5-manifest validation, G36, four-agent parity 39×5, kit-only |
| **Comments** | 8 findings closed; wording aligned to ADR-008; F-04 mechanic refinement + dot-dir self-correction accepted |
| **Findings** | none |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | Evidence inspected as above; V-Bounce GREEN |
