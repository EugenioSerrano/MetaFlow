---
id: "SPEC-260824-0050"
title: "The agents/ examples–squad split — shipped references vs the project's live agents"
date: "2026-08-24"
author: "eugenio.serrano"
llm: "claude-fable-5"
status: "approved" # draft | approved | blocked | obsolete — AITL-SPEC-Approval 2026-08-24
origin: "US-023"
bolt: "US-023.BOLT-005"
revision: 1
associated_adrs:
  - "devflow/adrs/ADR-013-agent-lifecycle-governance.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
prerequisites: []
risk_class: "low"
autonomy_level: "L3" # low risk → L3 default (§3.3)
turn_budget: ""
data_classification: "internal"
review_ready_at: "2026-08-24T00:55:21-03:00"
review: # AITL-SPEC-Approval — decision dictated in conversation ("vamos nomas!") and transcribed by the agent (§3.0)
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-24T01:01:08-03:00"
  decided_at: "2026-08-24T01:01:08-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved as Dev-validator after an independent cross-model SPEC review (verdict: ready as-is — frontmatter/G12, source inventory/G13, testable ACs, gates with reasoned n/a, F3 sequencing honored: this SPEC executes first). Authorizes the V-Bounce (revision 1)."
---

# SPEC-260824-0050 — The `agents/` examples–squad split

| Field | Value |
|-------|-------|
| **Origin** | US-023 (revision 3 — approved 2026-08-24) |
| **Bolt** | US-023.BOLT-005 (READY 2026-08-24, risk low) |
| **ADRs** | ADR-013 (§3.9 examples–squad ship model), ADR-004 (kit-only) |
| **Risk Class** | low |
| **Revision** | 1 |

---

## 1. Objective

Split the kit's `agents/` family into **`examples/`** (the five shipped role
definitions as read-only references — copied, never referenced by the roster,
never edited in place) and **`squad/`** (the project's live agents — the
Coordinator's writable workspace and the only folder the roster's
`definition:` pointers reference), per ADR-013 §3.9. Without this split the
kit's shipped definitions double as live definitions: an adopter (or the
Coordinator) editing a shipped file in place would violate the ADR-013 §3.5
bound and leave no clean home for project-created agents.

## 2. Context

US-023 delivered the `agents/` family with the five role definitions under
`roles/`. The v5.1 ship model (ADR-013 §3.9, accepted 2026-08-24) makes the
kit ship **no pre-built role wrappers** and the shipped definitions
**examples only**: the Coordinator scaffolds live agents from
`TEMPLATE-new-role/` + the examples into `squad/` (US-025's create/install
lifecycle consumes this shape). This SPEC executes **before**
SPEC/US-024.BOLT-004, which then rewrites the enablement wording in the
post-split locations.

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | US-023.BOLT-005 | AITL-BOLT-READY-Approval ✓ (2026-08-24T00:49:38) |
| Feature US | US-023 revision 3 | AITL-US-Approval ✓ (2026-08-24T00:40:35) |
| ADR | ADR-013 | AITL-ADR-Approval ✓ (2026-08-24T00:40:35) |
| ADR | ADR-004 | AITL-ADR-Approval ✓ (accepted) |
| Repository baseline | `7e3eb5e` | — |

## 4. Scope

### In scope
- `distribution-kit/devflow/agents/**` — the split, the README/INDEX/
  VERIFICATION reference updates, the kit-wide `roles/` path sweep.

### Out of scope
- The `actors/` reshape and the enablement-mechanism wording
  (US-024.BOLT-004 — executes after; this SPEC moves the old governance
  references **as-is**).
- The MainAgent lifecycle text (US-025); the maintainer-side generator in
  `tools/` (its path config is maintainer tooling, adjusted when US-025's
  work touches it).

## 5. Prerequisites and baseline

- Baseline `7e3eb5e` + the approved working tree (V-Bounce 4 of BOLT-003:
  no wrappers in dotfolders, docs aligned).
- Current `agents/` tree: `README.md`, `INDEX.md`, `VERIFICATION.md`,
  `roles/{README.md, TEMPLATE-new-role/, architect/, developer/,
  functional-analyst/, qa/, reviewer/}`.

## 6. Phases

### Phase A — The structural split

**Duration:** ~1h — **Complexity:** Low

Move the five role definition folders `roles/{architect, developer,
functional-analyst, qa, reviewer}/` → `agents/examples/` (content
byte-identical — a relocation, not a rewrite). Move `roles/TEMPLATE-new-role/`
→ `agents/TEMPLATE-new-role/` (the family root, mirroring `actors/`'s
root-level TEMPLATE). Create `agents/squad/` with a `README.md` stating the
live-workspace rules (the Coordinator writes here; the only folder the
roster references; ships empty; agents here follow the same `agent.yaml`
contract). Create a thin `agents/examples/README.md` stating the
copy-never-edit rule (references only — never roster-referenced, never
edited in place; copy into `squad/` via the template). Absorb the rest of
`roles/README.md` (the definition contract reference + the
create-your-own-agent guide + the governance table, **as-is**) into
`agents/README.md`; delete the `roles/` folder.

**Files created:** `agents/squad/README.md` · `agents/examples/README.md`
**Files moved:** the five role folders → `examples/` · `TEMPLATE-new-role/` → root
**Files deleted:** `agents/roles/README.md` (content absorbed) · the `roles/` folder

### Phase B — References

**Duration:** ~45min — **Complexity:** Low

`agents/README.md`: the family map (examples/ · squad/ · TEMPLATE-new-role/
· VERIFICATION.md) + the absorbed contract/guide/governance content.
`agents/INDEX.md`: the examples listed as **shipped** references and a
**squad (live)** section for the project's agents (empty at ship).
`VERIFICATION.md`: path references updated — the projection source is the
live definition (`squad/<id>/agent.yaml`); the examples are the reference
set the maintainer validates against.

### Phase C — Sweep + verification

**Duration:** ~45min — **Complexity:** Low

ADR-005 phrase-family sweep over the whole kit for `roles/` **path**
references (`agents/roles`, `roles/<role-name>`, `roles/TEMPLATE-new-role`)
→ every hit updated or allowlisted (prose uses of the word "roles" — role
taxonomy, "role charter" — are not path references and stay). Evidence:
directory listing of the final `agents/` tree; the sweep result (0 stale
path refs); self-containment grep over changed files (0 maintenance IDs);
no BOM.

## 7. Acceptance criteria

### AC-1: The split shape
**Given** the kit after this V-Bounce, **When** `agents/` is listed,
**Then** it contains exactly `README.md`, `INDEX.md`, `VERIFICATION.md`,
`TEMPLATE-new-role/`, `examples/` (the five references + its README) and
`squad/` (its README only) — and `roles/` does not exist.

### AC-2: The rules stated where the reader is
**Given** the two new READMEs, **When** read, **Then** `examples/README.md`
states copy-never-edit/never-referenced and `squad/README.md` states
live-workspace/only-roster-referenced.

### AC-3: Zero stale paths
**Given** the kit-wide sweep, **When** it runs, **Then** 0 `roles/` path
references remain (allowlisted prose excluded, each with reason).

### AC mapping to source

| Source AC | How this SPEC satisfies it | Verifying evidence |
|-----------|----------------------------|--------------------|
| US-023 rev 3 AC-1 | Phase A creates the examples/ + squad/ shape with TEMPLATE-new-role/ at the root | Directory listing |
| US-023 rev 3 AC-2 | The contract statement carries to agents/README.md; squad/README notes the same contract applies | README diff |
| US-023 rev 3 AC-9 (referenced) | The split completes the ship-model shape the Coordinator projects from | VERIFICATION.md refs |

## 8. Testing strategy

Documentation/structure Bolt — scripted evidence instead of test code:
the directory-shape check (AC-1), the sweep count (AC-3), self-containment
grep, BOM check. No unit/integration/E2E (no runtime surface).

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | n/a — documentation/structure Bolt, no runtime surface | n/a |
| SAST / SBOM | n/a — no code | n/a |
| Perf-smoke (p95/p99) | n/a — no runtime | n/a |
| Prompt-injection scan | no injected instructions in moved/created docs | pass expected |
| Secret-leak scan | no secrets in moved/created docs | pass expected |
| Hallucination lint | every referenced path/anchor resolves | pass expected |
| IP / license provenance | kit-original content only | pass expected |
| PII / DLP | internal docs, no personal data | pass expected |
| Dependency-confusion | n/a — no dependencies | n/a |
| Test-first evidence | scripted checks defined before execution (this §8) | pass expected |
| Behavioral reproducibility | the shape/sweep checks re-run identically | pass expected |
| Bolt-manifest validation | v_bounces[1] appended, schema PASS | pass expected |

## 10. Security and data

Internal documentation; no auth surface, no secrets, no personal data. The
split itself is a control: it structurally separates the read-only shipped
references from the writable live workspace (ADR-013 §3.5 bound).

## 11. Monitoring and observability

n/a — documentation family.

## 12. Migration, compatibility and rollback

- **Migration:** relocations only; adopters of prior kits are unaffected
  (the §5.16 upgrade places families by the new structure).
- **Compatibility:** the roster `definition:` pointer convention changes to
  `agents/squad/<id>/…` — stated in the READMEs; US-024.BOLT-004 fixes the
  worked example's pointer.
- **Rollback:** `git revert` of the V-Bounce commit restores `roles/`.

## 13. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| A stale `roles/` path survives | 2 | 2 | The ADR-005 sweep (positive coverage + allowlist with reasons) |
| examples/squad confusion | 1 | 2 | The two thin READMEs state each folder's rule at the point of reading |

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| The five definitions move byte-identical (no rewrite) | This Bolt is structure; the enablement wording is BOLT-004's — one concern per Bolt |
| The governance table moves as-is with its old wording | BOLT-004 (executing after) rewrites it in its final home — avoids editing the same text twice |
| `squad/` ships with only a README | The kit never ships live agents (ADR-013 §3.9); the README makes the empty folder meaningful and keeps it in git |

## 15. Stop conditions

- A kit file references `roles/` in a way that is neither a path to update
  nor allowlistable prose → stop, record in the MEM, ask.
- Any change that would touch the maintainer partition (out of kit scope).

## 16. Definition of Done (DoD)

- [ ] Phases A–C implemented
- [ ] AC-1..AC-3 pass (evidence recorded)
- [ ] Applicable gates pass / n/a per §9
- [ ] MEM created in `devflow/memory/` (exactly one)
- [ ] Manifest `v_bounces[]` entry appended
- [ ] AITL-MEM-Approval recorded

## 17. References

- US-023 revision 3 · US-023.BOLT-005 · ADR-013 §3.9/§3.5 · ADR-004 ·
  MEM-260823-1828 (the ship-model V-Bounce this split completes) ·
  SPEC/US-024.BOLT-004 (executes after this one).

## 18. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-24 | eugenio.serrano (agent-drafted) | Revision 1 |

## 19. AITL-SPEC-Approval

> Draft until the Dev-validator records `AITL-SPEC-Approval` (frontmatter
> `review:` block). SPEC approval authorizes the code-run / V-Bounce (G14).

| Field | Value |
|-------|-------|
| **review.reviewers** | `human:eugenio.serrano` (dev_validator) |
| **review.decision** | **approved** |
| **review_ready_at** | `2026-08-24T00:55:21-03:00` |
| **review.started_at** | `2026-08-24T01:01:08-03:00` |
| **review.decided_at** | `2026-08-24T01:01:08-03:00` |
| **Findings** | none — cross-model review PASS (reason in the frontmatter `review:` block) |
