---
id: "SPEC-260823-1150"
title: "Version bump sweep 5.0 → 5.1 in the distribution kit (US-000.BOLT-015)"
date: "2026-08-23"
author: "human:eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "approved" # draft | approved | blocked | obsolete
origin: "US-000.BOLT-015"
bolt: "US-000.BOLT-015"
revision: 1 # material revision of this canonical SPEC (matches manifest spec_revisions[])
associated_adrs:
  - "devflow/adrs/ADR-006-versioning-and-self-development-model.md"
prerequisites: []
risk_class: "low"
autonomy_level: "L3" # defaults by risk: low/medium→L3 (§3.3)
turn_budget: ""
data_classification: "internal"
review_ready_at: "2026-08-23T11:50:23-03:00"
review: # AITL-SPEC-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-23T11:52:00-03:00"
  decided_at: "2026-08-23T11:53:30-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Revision 1 approved: pre-SPEC evidence gate clean (Bolt approved, ADR-006 accepted, 0 open OQs, baseline 639d380), carrier inventory matches the live greps (71 headers, 15 v5.0 spots in 8 files, frontmatter L3, schema allowlist), safe patterns only (never bare 5.0), exclusion list complete (schemas/templates/history/sections/root), stop conditions defined. V-Bounce authorized."
---

# SPEC-260823-1150 — Version bump sweep 5.0 → 5.1 in the distribution kit

| Field | Value |
|-------|-------|
| **Origin** | US-000.BOLT-015 (approved 2026-08-23) |
| **Bolt** | [US-000.BOLT-015](../functional/bolts/US-000.BOLT-015-version-bump-5-1-sweep.md) (approved 2026-08-23) |
| **ADRs** | [ADR-006](../adrs/ADR-006-versioning-and-self-development-model.md) |
| **Risk Class** | low |
| **Revision** | 1 |

---

## 1. Objective

Bump every version marker of the distribution kit from **5.0** to **5.1** —
VERSION, the `**Methodology version:**` headers of README/INDEX files, the
GUARDRAILS header/footer, ONBOARDING, the methodology frontmatter, the four
agent definitions (shared heading, `Agent version` line, preamble mentions)
and the kit AGENTS.md source-of-truth line — while leaving the **manifest
family untouched** (`schema_version: "5.0"` in the JSON schemas and their
template examples, per the `<major>.0` convention), templates without version
markers untouched, history statements untouched, and the root maintenance
partition untouched.

If NOT implemented: the kit's markers would say 5.0 while the release line is
5.1 — the exact stale-marker class the version-bump procedure and
US-000.BOLT-013 exist to prevent.

---

## 2. Context

The 5.0 release was merged to `main` (tag v5.0); the repository now develops
the **5.1 line** on the `5.1` branch (ADR-006: branches per version, release
loop). The root README already says 5.1. This SPEC applies the root AGENTS.md
"Version bump procedure" (restored 2026-08-23): update
`distribution-kit/devflow/VERSION`, sweep the markers with the safe patterns
(never a bare `5.0`), keep statements *about* older versions and section
references as written, and keep the manifest family at `schema_version:
"5.0"` (the schema policy: the family major leads the methodology version —
`5.x` keeps `5.0`). Precedent: US-000.BOLT-013 (4.2→5.0 marker sweep, Done).

**Repository baseline:** branch `5.1` @ `639d380`; working tree clean before
this Bolt's governance artifacts.

---

## 3. Source inventory and approval references

Pre-SPEC evidence gate (G13, G35): every governed source is approved; zero
open/in-validation OQs against US-000.

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | `devflow/functional/bolts/US-000.BOLT-015-version-bump-5-1-sweep.md` | AITL-BOLT-READY-Approval ✓ (2026-08-23T11:50) |
| Parent container | `devflow/functional/user-stories/US-000-non-functional.md` | always active, no approval lifecycle |
| ADR-006 | versioning and self-development model | accepted ✓ |
| OQ index | `devflow/analysis/open-questions/INDEX.md` | 0 open / 0 in-validation (G35 ✓) |
| Repository baseline | branch `5.1` @ `639d380` | — |

---

## 4. Scope

### In scope (bump 5.0 → 5.1, all under `distribution-kit/`)

| Carrier | Location | Pattern |
|---------|----------|---------|
| VERSION | `devflow/VERSION` | `5.0` → `5.1` |
| README/INDEX headers | 71 files under `devflow/` (templates excluded) | `**Methodology version:** 5.0` → `5.1` |
| GUARDRAILS header + footer | `devflow/GUARDRAILS.md` L3 + L478 | `v5.0` → `v5.1` |
| ONBOARDING | `devflow/ONBOARDING.md` L3 (header) + L15 (`(v5.0)`) | both patterns |
| Methodology frontmatter | `devflow/avenga-devflow/Avenga-DevFlow.md` L3 | `version: "5.0"` → `"5.1"` |
| Methodology INDEX prose | `devflow/avenga-devflow/INDEX.md` L13 | `Avenga DevFlow v5.0` → `v5.1` |
| Four agents (10 spots) | `CLAUDE.md` (L3, L198), `.agents/skills/avenga-devflow/SKILL.md` (L8, L215), `.github/agents/AvengaDevFlow.agent.md` (L3, L32, L243), `.opencode/agents/AvengaDevFlow.md` (L3, L19, L226) | `Agent version:** 5.0`, `implements methodology v5.0`, `# Avenga DevFlow v5.0 (Methodology)`, preamble `follows the Avenga DevFlow v5.0 methodology` |
| Kit AGENTS.md | `AGENTS.md` L6 | `(v5.0)` → `(v5.1)` |

### Out of scope (explicitly NOT swept)

- **Manifest family:** `metrics/manifest-v5-{bolt,us,tc}.schema.json` (`"const": "5.0"`) and `metrics/TEMPLATE-MANIFEST-*.json` (`"schema_version": "5.0"`) — the `<major>.0` convention.
- **`schema_version` statements/examples:** `metrics/README.md` (L46, L183), `TEMPLATE-BOLT.md` L229, `TEMPLATE-US.md` L47+L154, `TEMPLATE-TC.md` L42+L126, methodology §3.12 (L3213/L3219) — family policy, not version markers.
- **History statements and §5.16 examples:** `4.0 → 5.0` conversion examples in the four agents and the methodology (L4713), "versions up to 4.1…", "From 4.2 on…", the root `CHANGELOG.md`, "released v5.0" prose.
- **Templates** (`TEMPLATE-*.md`): never carry the methodology version header.
- **Root maintenance partition** (`devflow/` root tree, root `README.md`, root `AGENTS.md`): stays 5.0 until the next §5.16 migration; root README already 5.1.
- **Section references** (`§2.4.1`, `§4.1`, `§4.10`, `§5.16`): never swept.

---

## 5. Prerequisites and baseline

- Bolt US-000.BOLT-015 approved; ADR-006 accepted; 0 open OQs.
- Baseline greps (RED inventory) recorded in Phase 0 with counts and line
  numbers — the SPEC's carrier table above is the classified result.
- No code, tooling or test suites involved — verification is deterministic
  grep/diff commands.

---

## 6. Phases

Strict evidence ordering per the version-bump procedure: Phase 0 (RED) runs
**before any edit**; Phase 1 is the sweep; Phase 2 is the GREEN verification;
Phase 3 is governance close-out. All in the ONE V-Bounce of US-000.BOLT-015.

### Phase 0 — RED inventory (no production change)

**Duration:** 0.5h total cycle — **Complexity:** Low

Capture, in the repository root, the baseline (this is the RED evidence):

1. **R1 — VERSION:** `Get-Content distribution-kit/devflow/VERSION` → `5.0`.
2. **R2 — headers:** grep `Methodology version:\*\* 5\.0` over `README.md` /
   `INDEX.md` under `distribution-kit/devflow/` (exclude `TEMPLATE*`) →
   **71 files**.
3. **R3 — `v5.0` carriers:** grep `v5\.0` over the kit (exclude `*.json`,
   exclude `_archive/`) → 15 spots in 8 files: `AGENTS.md` L6 (1),
   `CLAUDE.md` (2), `SKILL.md` (2), `AvengaDevFlow.agent.md` (3),
   `AvengaDevFlow.md` (3), `GUARDRAILS.md` L3+L478 (2), `ONBOARDING.md`
   L3+L15 (2 — one is the `Methodology version` header), `avenga-devflow/INDEX.md`
   L13 (1). (Header files counted in R2 use the header pattern.)
4. **R4 — frontmatter:** grep `version: "5\.0"` → `Avenga-DevFlow.md` L3
   (the only non-schema carrier).
5. **R5 — allowlist baseline:** `schema_version`/`"const": "5.0"`/`5.0` in
   `metrics/README.md`, the 3 schemas, the 5 manifest templates,
   `TEMPLATE-BOLT/US/TC` examples and the §3.12 statements — record the
   locations (they must survive untouched).

**Files created:** none. **Files modified:** none (strictly no edits before
RED is recorded).

---

### Phase 1 — Production change: the sweep (kit only)

**Duration:** 1h total cycle — **Complexity:** Low

Apply the safe patterns — **never a bare `5.0`** (the procedure's trap rule;
a blind replace would corrupt `§5.16`, `4.0 → 5.0` examples and history):

1. `distribution-kit/devflow/VERSION`: `5.0` → `5.1`.
2. All 71 header files: `**Methodology version:** 5.0` → `**Methodology version:** 5.1`.
3. `GUARDRAILS.md`: `**Enforcing:** Avenga DevFlow v5.0` → `v5.1` (L3);
   `(normative source, v5.0)` → `v5.1` (L478 footer).
4. `ONBOARDING.md`: header (L3) and `(v5.0)` (L15) → 5.1.
5. `Avenga-DevFlow.md` frontmatter L3: `version: "5.0"` → `version: "5.1"`.
6. `avenga-devflow/INDEX.md` L13: `Avenga DevFlow v5.0` → `v5.1`.
7. The four agents (10 spots): `**Agent version:** 5.0 - implements
   methodology v5.0` → 5.1 (4×); `# Avenga DevFlow v5.0 (Methodology)` →
   v5.1 (4×); `follows the Avenga DevFlow v5.0 methodology` → v5.1 (2× —
   gh-copilot + open-code preambles). Apply identically to all four
   (four-agent sync; the shared-body edit must stay byte-identical).
8. `distribution-kit/AGENTS.md` L6: `(v5.0)` → `(v5.1)`.

Do **not** touch: schemas, manifest templates, `metrics/README.md`'s
schema_version lines, template `schema_version` examples, §3.12 statements,
`4.0 → 5.0` conversion examples, history statements, root files.

**Files modified:** the carriers enumerated in §4 (about 80 files — 71
headers + 9 others), all under `distribution-kit/`.

---

### Phase 2 — GREEN verification (no further edits)

**Duration:** 0.5h total cycle — **Complexity:** Low

Run and capture:

- **G1 — positive coverage:** the same greps now return the 5.1 forms:
  `Methodology version:\*\* 5\.1` = **71**; `v5\.1` counts per carrier
  matching the RED spot counts; `version: "5.1"` in the frontmatter;
  VERSION = `5.1`; `Agent version:** 5.1` = 4; `# Avenga DevFlow v5.1
  (Methodology)` = 4; `Enforcing:** Avenga DevFlow v5.1` = 1.
- **G2 — absence (ADR-005):** the 5.0 patterns (`v5.0`, `Methodology
  version:** 5.0`, `Agent version:** 5.0`, `version: "5.0"` in .md,
  `Enforcing:** Avenga DevFlow v5.0`, `(v5.0)`) return **zero** in the kit
  outside the allowlist; every remaining `5.0` occurrence is classified
  (schema family / history / section example) and listed.
- **G3 — manifest family untouched:** `"const": "5.0"` still present in the
  3 schemas; `"schema_version": "5.0"` still in the 5 manifest templates;
  `metrics/README.md` L46/L183 and the §3.12 statements unchanged
  (byte-compare or grep).
- **G4 — history/examples intact:** the `4.0 → 5.0` conversion examples in
  the four agents and the methodology L4713 still read `4.0` → `5.0`; no
  section reference was altered (spot-check `§5.16`, `§4.1`).
- **G5 — four-agent parity:** shared-body diff = the sanctioned 2 lines per
  pair (the single `devflow/agents-data/<agent>/` path divergence).
- **G6 — G-count:** `grep -cE '^\| G[0-9]{2} \|'` = 39 in GUARDRAILS and in
  each of the four agents (39×5).
- **G7 — scope:** `git status --short` shows only `distribution-kit/` files
  (plus this Bolt's governance artifacts); root `devflow/`, root `README.md`,
  root `AGENTS.md` untouched.
- **G8 — encoding:** no BOM and no mojibake introduced (byte check on
  edited files; the em-dash `—` / `→` / `§` sequences intact).

**Files created:** none. **Files modified:** none (verification only).

---

### Phase 3 — Governance close-out (executor, mandatory)

**Duration:** 0.5h total cycle — **Complexity:** Low

1. MEM (`devflow/memory/MEM-260823-<HHmm>-version-bump-5-1-sweep.md`) with
   RED (Phase 0) and GREEN (Phase 2) evidence recorded separately.
2. `v_bounces[]` entry (number 1, spec_revision 1) appended to
   `devflow/metrics/bolts/US-000.BOLT-015-version-bump-5-1-sweep.json`
   (all eight required fields).
3. Present the package and PAUSE at `AITL-MEM-Approval`.

---

## 7. Acceptance criteria

### AC-1: Every kit version marker reads 5.1

**Given** the distribution kit
**When** grepping the safe patterns (`v5.1`, `Methodology version:** 5.1`,
`Agent version:** 5.1`, `version: "5.1"`, `Enforcing:** Avenga DevFlow v5.1`)
**Then** every carrier enumerated in §4 shows the 5.1 form with the RED
spot counts (71 headers; 15 `v5.1` spots; 4 agent headings; 4 Agent-version
lines; frontmatter; VERSION).

### AC-2: Zero 5.0 residue outside the allowlist

**Given** the swept kit
**When** grepping the 5.0 patterns
**Then** every remaining `5.0` occurrence is classified in the allowlist
(schema family, history, §5.16 conversion examples) and listed — no
unclassified carrier remains.

### AC-3: Manifest family untouched

**Given** the swept kit
**When** checking the schemas and manifest templates
**Then** `schema_version` / `"const"` still reads `"5.0"` in all 3 schemas,
the 5 manifest templates, `metrics/README.md` and the §3.12 statements —
byte-identical.

### AC-4: History and section references intact

**Given** the swept kit
**When** checking the conversion examples and section references
**Then** `4.0 → 5.0` examples and `§5.16`/`§4.1`-style references are
unchanged — the sweep never touched a bare `5.0`.

### AC-5: Four-agent parity and G-count

**Given** the swept agents
**When** running the parity diff and the G-count grep
**Then** shared bodies differ only by the sanctioned `agents-data/<agent>/`
path (2 diff lines per pair) and every file reads 39 G-rows (39×5).

### AC-6: Scope containment

**Given** the V-Bounce execution
**When** running `git status`
**Then** only `distribution-kit/` files and this Bolt's governance artifacts
changed; root tree untouched.

### AC mapping to source (non-functional measurable outcome)

| Source outcome (Bolt §2) | How this SPEC satisfies it | Verifying test/evidence |
|---------------------------|----------------------------|--------------------------|
| Every kit marker reads 5.1 | Phase 1 sweep per carrier | AC-1 (G1 counts) |
| Manifest family untouched | Sweep excludes schemas/templates/family statements by construction | AC-3 (G3) |
| History/sections intact | Safe patterns only; never bare `5.0` | AC-4 (G4) |
| Parity + invariants | Identical agent edits + checks | AC-5 (G5/G6) |
| Kit-only scope | Edit set bounded to `distribution-kit/` | AC-6 (G7) |

---

## 8. Testing strategy

Documentation/version sweep — no unit/integration suites; verification is
deterministic, re-runnable grep/diff commands (ADR-005 discipline).

- **RED evidence (Phase 0, before any edit):** R1–R5 with counts and line
  numbers (71 headers; 15 `v5.0` spots in 8 files; frontmatter L3; allowlist
  locations).
- **GREEN evidence (Phase 2):** G1 positive coverage, G2 absence sweep with
  the classified allowlist, G3 schema family untouched, G4 history/examples
  intact, G5 parity, G6 G-count 39×5, G7 scope, G8 encoding.
- **Edge cases:** templates carrying `schema_version: "5.0"` examples (stay);
  ONBOARDING's two carriers (header + `(v5.0)` prose); gh-copilot/open-code
  preamble descriptions (frontmatter-version trap, 4.1 changelog); the
  avenga-devflow/INDEX.md prose description; GUARDRAILS footer.

---

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | — (no code) | `n/a` — version-marker sweep; verification is grep/diff |
| SAST / SBOM | — | `n/a` — no buildable artifact or dependency graph |
| Perf-smoke (p95/p99) | — | `n/a` — no runtime component |
| Prompt-injection scan | — | `n/a` — static markers, not an externally reachable prompt surface |
| Secret-leak scan | — | `n/a` — no secrets possible in version markers; diff reviewed |
| Hallucination lint | every count and line number in this SPEC matches the file at execution time | `pass` — verified by R1–R5/G1–G8 |
| IP / license provenance | — | `n/a` — no third-party code |
| PII / DLP | — | `n/a` — internal documentation |
| Dependency-confusion | — | `n/a` — no dependencies |
| Test-first evidence | RED inventory recorded before any edit | `pass` — Phase 0 before Phase 1 |
| Behavioral reproducibility | same commands, same output on re-run | `pass` — deterministic greps |
| Bolt-manifest validation | manifest validates at every step | `pass` — validated at creation and after each update |

---

## 10. Security and data

- No auth, secrets, or external surfaces — the sweep edits version strings in
  Markdown/agent files.
- `data_classification: internal` — methodology text; no personal or
  regulated data.
- The G-count and four-agent parity invariants are the security-relevant
  properties being protected (a drifted agent would stop enforcing rules).

---

## 11. Monitoring and observability

- `n/a` — no runtime; observability is the greppable marker state itself
  (G1–G8 evidence).

---

## 12. Migration, compatibility and rollback

- **Migration:** none — the kit is the product under construction on the
  5.1 line; the root tree is NOT migrated (it stays 5.0 until the next
  §5.16 release migration).
- **Compatibility:** adopters copy the kit; markers 5.1 with the manifest
  family at `schema_version: "5.0"` is the intended combination (family
  major leads the methodology version, §3.12).
- **Rollback:** reverse the sweep (restore the 5.0 markers) or `git
  checkout` the affected files from `639d380`; the manifest family was
  never touched.

---

## 13. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| Blind replace corrupts `§5.16`/history/examples | 2 | 4 | Safe patterns only; never bare `5.0`; G2/G4 verify |
| Partial sweep — a carrier missed | 2 | 3 | R2/R3 full-kit greps; G1 positive coverage with counts |
| Agent drift during identical edits | 2 | 3 | Four-agent sync procedure; G5 parity diff |
| Schema family accidentally touched | 1 | 4 | Sweep excludes `.json` by construction; G3 byte check |
| Encoding corruption (BOM/mojibake) | 1 | 2 | UTF-8 tooling; G8 byte check |

---

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| `schema_version` stays `"5.0"` (schemas, manifest templates, metrics/README, §3.12) | The `<major>.0` convention: the manifest family carries its own major; 5.x keeps 5.0 (CHANGELOG 4.1 policy) — the user's explicit scope ("menos los json schemas") |
| Template `schema_version: "5.0"` examples stay | They describe the manifest family, not the methodology version; templates never carry the header marker |
| `4.0 → 5.0` conversion examples and history stay | Statements about older versions are history, never markers (procedure rule 4) |
| gh-copilot/open-code preamble descriptions bumped | The 4.1 changelog records the frontmatter-version trap: descriptions naming the version go stale exactly like markers |
| ONBOARDING has two carriers (header + `(v5.0)` source-of-truth) | Both are current-version stamps; the source-of-truth line mirrors the kit AGENTS.md line |
| avenga-devflow/INDEX.md L13 prose description bumped | It describes the current version of the methodology ("v5.0 - the complete methodology") |

---

## 15. Stop conditions

- **S1 — baseline drift:** the RED inventory at execution time differs from
  this SPEC's counts/line numbers (files changed meanwhile) → stop,
  re-baseline, revise this SPEC (G15).
- **S2 — unclassified 5.0 carrier:** a `5.0` occurrence that fits no
  pattern and no allowlist class → stop and classify with the human before
  touching it.
- **S3 — schema family touched:** any edit lands on a `.schema.json` or a
  manifest template → stop and repair before continuing.
- **S4 — agent drift:** the four shared bodies fail the parity diff after
  the edits → stop and reconcile (drift is a defect, ADR-007).
- Any stop condition → MEM with the blocker + manifest entry, then pause
  (§2.12).

---

## 16. Definition of Done (DoD)

- [ ] All phases implemented (0 RED → 1 sweep → 2 GREEN)
- [ ] All acceptance criteria pass (AC-1..AC-6)
- [ ] RED inventory recorded before any edit; GREEN evidence recorded
- [ ] Sweep follows ADR-006 + the AGENTS.md version-bump procedure
- [ ] Applicable gates pass / n/a with reason (§9)
- [ ] MEM created in `devflow/memory/` (exactly one per V-Bounce)
- [ ] Manifest `v_bounces[]` entry appended (all eight fields)
- [ ] AITL-MEM-Approval recorded (human)

---

## 17. References

- `devflow/functional/bolts/US-000.BOLT-015-version-bump-5-1-sweep.md`
- `devflow/adrs/ADR-006-versioning-and-self-development-model.md`
- Root `AGENTS.md` — "Version bump procedure" (project section)
- `devflow/functional/bolts/US-000.BOLT-013-version-marker-sweep.md` (precedent, Done)
- `devflow/metrics/bolts/US-000.BOLT-015-version-bump-5-1-sweep.json`

---

## 18. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-23 | human:eugenio.serrano | Revision 1 — initial SPEC for US-000.BOLT-015 |

---

## 19. AITL-SPEC-Approval

> **Avenga DevFlow §2.4.1, §3.0.** This SPEC remains a draft until the
> Dev-validator (+ applicable domain owners) records `AITL-SPEC-Approval`
> (in the `review` frontmatter block). Bolt approval (`AITL-BOLT-READY-Approval`)
> authorizes SPEC preparation; **SPEC approval** authorizes the code-run /
> V-Bounce. A material source change invalidates this approval — stop,
> revise, re-approve (G15).

| Field | Value |
|-------|-------|
| **review.reviewers** | Dev-validator + applicable domain owner(s) — minimum one approver |
| **review.decision** | approved / changes_requested / rejected |
| **review_ready_at** | `2026-08-23T11:50:23-03:00` |
| **review.started_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **review.decided_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **Findings** | [findings or acknowledged_without_comment + reason] |
