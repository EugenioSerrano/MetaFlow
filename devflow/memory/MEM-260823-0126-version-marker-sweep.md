---
id: "MEM-260823-0126"
title: "V-Bounce 1 — Version-marker sweep 4.2 → 5.0 across distribution-kit/ (REV-004 F-09)"
date: "2026-08-23"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
bolt: "US-000.BOLT-013"
spec: "SPEC-260823-0121"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "1f93ebb"
applied_adrs:
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "US-000.BOLT-013-version-marker-sweep.json"
diff_ref: ""
review_ready_at: "2026-08-23T01:26:25-03:00"
review: # HITL-MEM-Approval — recorded by the human reviewer (§3.0); decision dictated by the human in conversation ("aprobado, ambos!") and transcribed by the agent
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - user: "eugenio.serrano"
      role: "dev_validator"
  started_at: "2026-08-23T01:28:40-03:00"
  decided_at: "2026-08-23T01:28:40-03:00"
  findings: []
  acknowledged_without_comment: true # must be true when findings is empty (§3.0)
  acknowledgment_reason: "Reviewed the V-Bounce 1 package of US-000.BOLT-013: the kit diff (markers only — spot-verified on tests/README.md showing exactly the intended lines), marker greps at zero (all 4.2 families), residue classification (remaining hits = history + section numbers), encoding integrity (0 BOM, 0 mojibake), G-count 39×5, four-agent parity (2 lines/pair), the MEM narrative (incl. the two execution incidents handled transparently) and the validating manifest. Matches SPEC-260823-0121 rev 1 and REV-004 F-09. V-Bounce approved; Bolt → Development Completed."
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs and headings (##) in
  English; prose content_language (en).

  DOGFOODING SPLIT: this V-Bounce ran under v4.2 (root devflow/, ADR-006) — its
  checkpoint is HITL-MEM-Approval, its manifest schema_version 4.0. It edited the
  v5.0 PRODUCT (distribution-kit/, AITL-*). Kit-only (ADR-004); the root tree
  stays v4.2 until the §5.16 migration at release.

  Not a BUG V-Bounce (no strict red/green): mechanical version-marker sweep,
  verified by marker greps + residue classification, not a runtime test.
-->

# MEM-260823-0126 — Version-marker sweep 4.2 → 5.0 (V-Bounce 1)

| Field        | Value |
|--------------|-------|
| **Bolt**     | [US-000.BOLT-013](../functional/bolts/US-000.BOLT-013-version-marker-sweep.md) |
| **SPEC**     | [SPEC-260823-0121](../spec/SPEC-260823-0121-version-marker-sweep.md) rev 1 |
| **V-Bounce** | 1 |
| **ADRs**     | ADR-004 (kit-only) |

---

## 1. Executive summary

This V-Bounce aligned the kit's declared version with its v5 content: every
version **marker** in `distribution-kit/` now reads **5.0** — the `VERSION`
file, the methodology frontmatter, GUARDRAILS' header and Related-Documents
line, the `**Methodology version:**` header of **70** README/INDEX files
(sweep by pattern, not by file list), the four agent definitions (Agent
version line, shared-body heading, and the two `description` frontmatters),
`AGENTS.md` and `ONBOARDING.md` source-of-truth lines, and the
`avenga-devflow/INDEX.md` row. Every **historical** statement ("removed in
v4.2", "DORMANT/RESERVED (v4.2)") and every **section number** ("## 4.2",
"### 4.2") is untouched, proven by the residue classification below. G-count
stays 39×5 and the four agents remain byte-identical except the sanctioned
`agents-data/<agent>/` line (2 diff lines per pair).

Two execution notes, both handled transparently: (1) the bulk header sweep
initially went through a PowerShell `Set-Content` that wrote UTF-8 **with
BOM** and had read the files as ANSI, mangling multi-byte characters
(em-dashes, box-drawing, emoji) into mojibake — this was fully reversed
(mojibake → Windows-1252 bytes → UTF-8, verified by diff showing **only**
the intended lines changed, zero BOMs and zero mojibake left in the kit);
(2) `ONBOARDING.md`'s header is not a README/INDEX file, so the pattern
sweep missed it — caught by the marker grep and fixed with a direct edit.
This is the same "sweep by zone, not by token" lesson, applied to the
sweep's own verification: the **marker grep over the whole kit** (not just
the swept file set) is what caught it.

---

## 2. Implemented phases

### Phase A — file-level markers (M1–M4, M9, M10)

- `devflow/VERSION`: `4.2` → `5.0` (single line).
- Methodology frontmatter: `version: "4.2"` → `version: "5.0"`.
- `GUARDRAILS.md`: `**Enforcing:** Avenga DevFlow v4.2` → `v5.0`;
  `(normative source, v4.2)` → `(normative source, v5.0)`.
- `AGENTS.md` + `ONBOARDING.md`: source-of-truth `(v4.2)` → `(v5.0)`.
- `avenga-devflow/INDEX.md`: "Avenga DevFlow v4.2 — the complete
  methodology" → "v5.0".

### Phase B — `**Methodology version:**` headers (M5)

`**Methodology version:** 4.2` → `**Methodology version:** 5.0` in **70**
files (every README/INDEX under `distribution-kit/devflow/`), by pattern.
Plus the `ONBOARDING.md:3` header caught by the post-sweep marker grep.

### Phase C — the four agent definitions (M6, M7, M8), in lockstep

`**Agent version:** 4.2 — implements methodology v4.2` → `5.0 — implements
methodology v5.0`; `# Avenga DevFlow v4.2 (Methodology)` → `# Avenga DevFlow
v5.0 (Methodology)`; `description` frontmatter "follows the Avenga DevFlow
v4.2 methodology" → `v5.0` (gh-copilot + open-code). Parity re-verified: 2
sanctioned diff lines per pair.

---

## 3. Files created

| File | Purpose |
|------|---------|
| (none) | — this V-Bounce only modified existing kit files |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `distribution-kit/devflow/VERSION` | `4.2` → `5.0` (the single version declaration) |
| `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md` | frontmatter `version: "5.0"` |
| `distribution-kit/devflow/GUARDRAILS.md` | header `v5.0` + Related-Documents `(v5.0)` |
| `distribution-kit/devflow/avenga-devflow/INDEX.md` | row "Avenga DevFlow v5.0" + version header |
| `distribution-kit/devflow/ONBOARDING.md` | version header `5.0` + source-of-truth `(v5.0)` |
| `distribution-kit/AGENTS.md` | source-of-truth `(v5.0)` |
| `distribution-kit/CLAUDE.md`, `.agents/skills/…SKILL.md`, `.github/agents/…agent.md`, `.opencode/agents/…md` | Agent version 5.0, heading `# Avenga DevFlow v5.0 (Methodology)`, descriptions `v5.0` (2 files) |
| 70× `README.md` / `INDEX.md` under `distribution-kit/devflow/` | `**Methodology version:**` header `4.2` → `5.0` (incl. `analysis/**`, `input/**`, `tests/**`, `metrics/`, `adrs/`, `bugs/`, `discovery/`, `reviews/`, `adversarial-reviews/`, `incidents/`, `risks/`, `retros/`, `prompts/`, `agents-data/`, `functional/`, `spec/`, `memory/`, `reports/`, `avenga-devflow/`) |

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
| —    | —        | —      |

## 6. Files deleted

| File | Reason |
|------|--------|
| —    | —      |

---

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| Sweep by marker pattern, never by bare `4.2` | section numbers ("## 4.2") and history ("removed in v4.2") share the shape — the repo's version-bump procedure warns about exactly this |
| Include the agents' shared-body heading in the sweep | it is the marker the four-agent sync procedure greps for; leaving it would make marker checks and parity checks disagree |
| Post-sweep marker grep over the **whole kit**, not just the swept set | caught the ONBOARDING header the README/INDEX-only pattern missed — the "sweep by zone" lesson applied to the sweep itself |
| Reverse the ANSI-read mojibake via 1252→UTF-8 instead of restoring from git | the files carry the previous V-Bounces' edits; a git restore would have lost BOLT-011/012 work; the byte-level reversal is lossless and the diff proves it |

## 8. Deviations and assumptions

- **One deviation from SPEC-260823-0121 rev 1, self-corrected in-run:** the
  M5 pattern was defined as "every README/INDEX"; `ONBOARDING.md` carries the
  same header line and was not in that set — it was fixed by direct edit
  after the marker grep caught it. Net effect: zero `**Methodology version:**
  4.2` headers remain, which is the AC-2 outcome. No SPEC revision needed
  (the outcome is the approved AC; the inventory note is recorded here).
- **Encoding incident (handled, not a deviation of scope):** the bulk
  replacement tooling initially mangled non-ASCII characters (read as ANSI,
  written with BOM); fully reversed byte-exactly, verified by git diff
  showing only the intended lines changed and by zero-BOM/zero-mojibake
  sweeps over the whole kit.

---

## 9. Verification evidence

### Marker greps (over `distribution-kit/`, after the sweep)

```
**Methodology version:** 4.2      → 0   (was 71: 70 README/INDEX + ONBOARDING)
**Agent version:** 4.2            → 0   (was 4)
# Avenga DevFlow v4.2 (Methodology) → 0 (was 4)
version: "4.2"                    → 0   (was 1)
**Enforcing:** Avenga DevFlow v4.2 → 0  (was 1)
(normative source, v4.2)          → 0   (was 1)
follows the Avenga DevFlow v4.2 methodology → 0 (was 2)
Avenga DevFlow v4.2 — the complete methodology → 0 (was 1)
```

### Residue classification (every remaining `4.2`/`v4.2` hit, all kept)

| Hit | Classification |
|-----|----------------|
| methodology `## 4.2 SPEC preparation and approval` | section number |
| `reviews/TEMPLATE-REV.md` `### 4.2 — [Another domain / Category]` | section number |
| methodology "removed in v4.2" (§4.7), README "Removed in v4.2", tests/README "removed in v4.2" ×2, analysis/README "in v4.2" ×2, ONBOARDING "removed in v4.2", uat README/TEMPLATE "removed from the active flow in v4.2", "DORMANT / RESERVED (v4.2)" ×3, "In v4.2 this whole layer is" | history |

### Encoding integrity

```
UTF-8 BOM in distribution-kit/  → 0 files
mojibake sequences (â€/â›/â”)   → 0
git diff per file              → only the intended lines (spot-verified on
                                 tests/README.md, README.md, adrs/README.md)
```

### Invariant checks

```
G-count         → 39 in GUARDRAILS + 39 in each of the four agents (39×5)
Four-agent body parity → 2 sanctioned diff lines per pair (codex/ghcopilot/opencode)
git status      → 83 modified files, all in distribution-kit/ (SPEC inventories)
VERSION file    → "5.0"
```

### Gates

All applicable gates `pass` or `n/a` with reason (SPEC-260823-0121 §9):
secret-leak pass, hallucination-lint pass, behavioral-reproducibility pass,
bolt-manifest validation pass; product-code gates `n/a` (documentation
product).

---

## 10. Manual interventions

None — the agent produced the entire change. (The in-run encoding
self-correction was agent-executed and verified by diff.)

---

## 11. Evidence links

- **Diff / PR:** working tree diff of the kit files (not committed — the
  human owns repository history, G34).
- **Commit:** baseline `1f93ebb` (HEAD before this V-Bounce).
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-000.BOLT-013-version-marker-sweep.json`.

---

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~6 min (marker edits + sweep + encoding fix + verification) |
| V-Bounce number | 1 |
| Tests created | 0 (documentation product — deterministic greps instead, §9) |
| AI-generated code | 100% of the edit (human fallback: none) |
| First-pass approval | pending HITL-MEM-Approval |

---

## 13. Pending items and stubs

- **Release (this Bolt is the last consistency item):** commit + tag + the
  §5.16 migration of the root tree onto the kit (where `VERSION` is written
  last — the root already anticipates v5.0 in its governance records).
- The root `devflow/` tree stays v4.2 until that migration (ADR-004).

---

## 14. HITL-MEM-Approval

> **Avenga DevFlow §2.12, §3.0.** This MEM is created by the agent with no
> mutable status and is **never self-approved**. A qualified human (the
> Dev-validator who executed the Bolt) inspects the actual diff, the marker
> greps, the residue classification, this MEM and the manifest, and records
> `HITL-MEM-Approval` here and in the manifest's `hitl_approvals[]`.
> `approved` completes the V-Bounce (and, if latest, marks the Bolt
> `Development Completed`); `changes_requested` keeps this MEM as immutable
> history and the next execution is a NEW V-Bounce with a NEW MEM.
> `HITL-BOLT-DONE-Approval` is still required for `Done`.

| Field | Value |
|-------|-------|
| **Reviewers (executing Dev-validator)** | `eugenio.serrano` — dev_validator |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-23T01:26:25-03:00` — package submitted |
| **review.started_at** | `2026-08-23T01:28:40-03:00` |
| **review.decided_at** | `2026-08-23T01:28:40-03:00` |
| **Review evidence** | diff of the kit files + marker greps at zero + residue classification + encoding integrity (0 BOM / 0 mojibake) + G-count 39×5 + parity + manifest validation |
| **Comments** | none |
| **Findings** | none |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | see frontmatter |
