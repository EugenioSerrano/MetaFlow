---
id: "MEM-260823-1349"
title: "Actor vocabulary and four agents — ONBOARDING entry, four-agent byte-identical paragraph and the Actor phrase-family sweep (US-022.BOLT-003)"
date: "2026-08-23"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
bolt: "US-022.BOLT-003"
spec: "devflow/spec/SPEC-260823-1337-actor-vocabulary-agents-sweep.md"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "45d553f"
applied_adrs:
  - "devflow/adrs/ADR-010-actor-grammar-and-pure-v5-vocabulary.md"
  - "devflow/adrs/ADR-005-removal-completeness-phrase-family-sweep.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "devflow/metrics/bolts/US-022.BOLT-003-actor-vocabulary-and-agents-sweep.json"
diff_ref: ""
review_ready_at: "2026-08-23T13:49:00-03:00"
review: # AITL-MEM-Approval — recorded by the human reviewer (§3.0); decision dictated in conversation and transcribed by the agent
  decision: "changes_requested"
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-23T15:28:00-03:00"
  decided_at: "2026-08-23T15:29:03-03:00"
  findings:
    - "Superseded by the producer+approver propagation: the source US-022 was re-approved (material change, G15) and SPEC-1337 rev 2 reframed the four-agent paragraph, the ONBOARDING entry and the actors/ README surface. The V-Bounce 1 sweep fixes remain valid; the reframe landed in V-Bounce 2 (MEM-260823-1408)."
  acknowledged_without_comment: false
  acknowledgment_reason: "changes_requested — superseded by the propagation V-Bounce 2 (MEM-260823-1408). Recorded to complete the review contract (G17/§3.3); the MEM narrative stays immutable."
---

# MEM-260823-1349 — Actor vocabulary, four agents and the sweep (US-022.BOLT-003, V-Bounce 1)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | US-022.BOLT-003 (actor-vocabulary-and-agents-sweep) |
| **SPEC**        | [SPEC-260823-1337](../spec/SPEC-260823-1337-actor-vocabulary-agents-sweep.md) rev 1 |
| **V-Bounce**    | 1 |
| **ADRs**        | ADR-010 (pure v5 vocabulary), ADR-005 (sweep discipline), ADR-004 (kit-only) |

---

## 1. Executive summary

This V-Bounce made every kit surface that names the Actor concept speak one
consistent vocabulary and verified it mechanically. The **ONBOARDING §4
Minimal glossary** gained the "Actor" row (the kit's actual vocabulary
surface — a deviation from the SPEC's `analysis/glossary/glossary.md`
assumption, recorded below, because the kit ships no glossary content file:
the business glossary is per-project, created from the template). The four
platform agents gained a **byte-identical "The Actor (unit of identity)"**
paragraph in their shared methodology region (right after the Core
principle), stating human-by-default, the executor/approver/neither
relationship, the grammar and the independence layers — the sync check
confirms the shared bodies are byte-identical with only the sanctioned
`agents-data/<agent>/` path divergence (2 diff lines per agent), and the
G-count holds at 39×5. The **Actor phrase-family sweep** (ADR-005), run
last over the location set (methodology + ONBOARDING + README +
`actors/` README), found **three stale operative mentions** of the old
paradigm — "human-in-the-loop as validator" (§1 V-Bounce description) and
"proof that human-in-the-loop is real" (§3.7.2/§3.7.3 governance metrics)
— which were corrected to the AITL vocabulary ("actor-in-the-loop as
validator"; "human-by-default governance is real"); the re-run confirms
**absence outside the allowlist**, which keeps exactly the four legitimate
mentions: two safe-default descriptions ("pure Human-in-the-Loop" zero-
config behavior), the ADR-008 §3.1 default-case naming (HITL as the default
case inside AITL) and one third-party bibliographic citation (G36). The
sweep therefore earned its keep: it caught three real misses the US-021
identifier sweep could not see (lower-case descriptive phrases). All
verification is GREEN; kit-only confirmed.

## 2. Implemented phases

### Phase A — ONBOARDING entry

Added the "Actor" row to ONBOARDING §4 Minimal glossary (before the "AITL
checkpoint" row): the unit of identity in the AITL loop (human by default /
DevFlow Agent by explicit valid configuration), the grammar forms
(`human:<user>` / `agent:<id>`; model as attribute), the HITL default-case
and the safe-default invariant, with the pointer to §3.0.1. Deviation:
SPEC-1337 named `analysis/glossary/glossary.md` as the glossary home, but
the kit ships no glossary content file (the folder holds README +
TEMPLATE + INDEX; business glossaries are created per project). The kit's
actual vocabulary surface is ONBOARDING §4 — the entry landed there,
preserving the AC-7 intent (the vocabulary defines Actor consistently with
the pure-v5 vocabulary).

### Phase B — The four platform agents

Added the identical paragraph "**The Actor (unit of identity):** …" right
after the "Core principle" line in each of the four agents' shared
methodology region (CLAUDE.md, SKILL.md, AvengaDevFlow.agent.md,
AvengaDevFlow.md). The paragraph compresses §3.0.1: human-by-default, HITL
as default case, no-AI-signed-approval safe default, the
executor/approver/neither relationship (Coordinator never signs), the
grammar, and the independence ladder (actor floor → model hardening at
high → human ceiling at critical/regulatory). Byte-identical by
construction (same text, same relative position in the shared body).

### Phase C — The Actor phrase-family sweep (runs last)

Applied the ADR-005 phrase-family discipline to the Actor vocabulary family
("Actor", "Actor-in-the-Loop", "human-by-default,
agent-by-explicit-configuration"; competitors: "Human-in-the-Loop"/
"human-in-the-loop" outside the allowlist, "the human governs", "the human
is the governor", "HITL is the load-bearing") over the fixed location set:
methodology, ONBOARDING, kit README, `actors/` README (BOLT-002 output).
**Findings:** three stale operative mentions corrected in place — §1
"human-in-the-loop as validator" → "actor-in-the-loop as validator — a
human by default…", §3.7.2/§3.7.3 "proof that human-in-the-loop is real"
→ "proof that human-by-default governance is real". **Allowlist (4):**
methodology §1 safe-default description ("pure Human-in-the-Loop: every
checkpoint is a human approval"), §3.0 default-case naming ("HITL is the
default case of AITL", required by ADR-008 §3.1), the bibliographic
citation (G36 — third-party reference, never rewritten), README safe
default ("pure Human-in-the-Loop; no AI-signed approval is possible").
Re-run: **absence confirmed** outside the allowlist.

### Phase D — Verification (GREEN)

Ran the checks: ONBOARDING row present; paragraph present in all four
agents; four-agent shared-body byte-identity (tail from the
`# Avenga DevFlow v5.1 (Methodology)` heading, CR-stripped, diffed against
CLAUDE.md — exactly 2 diff lines per agent, the sanctioned
`agents-data/<agent>/` path); G-count 39 in GUARDRAILS + all four agents;
sweep absence; encoding clean (no BOM, 0 replacement chars in the touched
files); `git status` kit-only.

## 3. Files created

| File | Purpose |
|------|---------|
| — | none (edits within existing files) |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `distribution-kit/devflow/ONBOARDING.md` | New "Actor" row in §4 Minimal glossary (the kit's vocabulary surface — deviation from the SPEC's glossary.md assumption recorded above) |
| `distribution-kit/CLAUDE.md` | "The Actor (unit of identity)" paragraph in the shared methodology region (byte-identical) |
| `distribution-kit/.agents/skills/avenga-devflow/SKILL.md` | Same paragraph, byte-identical |
| `distribution-kit/.github/agents/AvengaDevFlow.agent.md` | Same paragraph, byte-identical |
| `distribution-kit/.opencode/agents/AvengaDevFlow.md` | Same paragraph, byte-identical |
| `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md` | Sweep fixes: §1 "actor-in-the-loop as validator"; §3.7.2 + §3.7.3 "human-by-default governance is real" (stale operative mentions corrected) |

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
| — | — | — |

## 6. Files deleted

| File | Reason |
|------|--------|
| — | — |

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| The "Actor" entry lands in ONBOARDING §4, not in `analysis/glossary/glossary.md` | The kit ships no glossary content file (business glossaries are per-project from TEMPLATE-GLOSSARY); ONBOARDING §4 IS the kit's vocabulary surface. AC-7 intent preserved; deviation recorded |
| Paragraph placed right after "Core principle" in the shared body | The first statement of the AITL concept in the agents; byte-identity by construction (same anchor line in all four) |
| The paragraph compresses §3.0.1 rather than duplicating it | Agents carry the operative summary; the normative depth lives in the methodology (single source) |
| Sweep fixes use pure-v5 vocabulary ("actor-in-the-loop as validator", "human-by-default governance is real") | ADR-010 pure-v5 vocabulary rule: the operative descriptions must speak AITL; HITL survives only as the named default case / history |
| The bibliographic citation is allowlisted, not rewritten | G36 — third-party references are history; rewriting them would falsify the record |

## 8. Deviations and assumptions

**Deviation (SPEC-1337 §4/§6):** the glossary home was specified as
`distribution-kit/devflow/analysis/glossary/glossary.md`, which does not
exist in the kit (the folder ships README + TEMPLATE + INDEX; business
glossaries are created per project from the template). The "Actor" entry
was placed in the kit's actual vocabulary surface — ONBOARDING §4 Minimal
glossary — preserving the AC-7 intent (the vocabulary defines Actor
consistently with ADR-010). No other deviations.

## 9. Verification evidence

### Presence (RED → GREEN)

```
RED:   ONBOARDING "Actor" row        → ABSENT
       agent Actor paragraph (4x)    → ABSENT
GREEN: ONBOARDING row                → PRESENT (line 69)
       paragraph in CLAUDE/SKILL/agent.md/AvengaDevFlow.md → PRESENT (4x)
```

### Four-agent byte-identity (US-016 discipline)

```
tail from '# Avenga DevFlow v5.1 (Methodology)' + CR-strip + diff vs CLAUDE:
  codex : 2 diff lines | ghcopilot : 2 | opencode : 2
  The single diff pair = the sanctioned `devflow/agents-data/<agent>/` path. PASS
```

### G-count invariant

```
GUARDRAILS 39 · CLAUDE.md 39 · SKILL.md 39 · AvengaDevFlow.agent.md 39 ·
AvengaDevFlow.md 39   → 39×5 PASS
```

### Sweep (ADR-005 — absence outside the allowlist)

```
Findings fixed (3): §1 'human-in-the-loop as validator' → 'actor-in-the-loop
as validator'; §3.7.2 + §3.7.3 'human-in-the-loop is real' → 'human-by-default
governance is real'.
Re-run remaining (4, all allowlisted): §1 safe-default 'pure HITL' · §3.0
default-case naming (ADR-008 §3.1) · bibliographic citation (G36) · README
safe-default 'pure HITL'. ABSENCE CONFIRMED. PASS
```

### Kit-only + encoding

```
git status -- distribution-kit: 6 modified + actors/ new — all kit paths. PASS
No BOM, 0 replacement chars in all touched files. PASS
```

### Gates

Documentation Bolt: unit/integration, SAST/SBOM, perf, IP, PII,
dep-confusion, test-first → `n/a` (no runtime, no dependencies, no personal
data). prompt-injection, secret-leak → `pass` (no runtime surface).
hallucination-lint → `pass` (the §3.0.1 pointer resolves).
behavioral-reproducibility → `pass` (deterministic checks).
bolt-manifest-validation → `pass` (manifest updated, JSON valid).

## 10. Manual interventions

None — the agent produced everything.

## 11. Evidence links

- **Diff / PR:** none (working tree, uncommitted)
- **Commit:** baseline `45d553f`
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-022.BOLT-003-actor-vocabulary-and-agents-sweep.json`

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~15min |
| V-Bounce number | 1 |
| Tests created | 0 (documentation Bolt — deterministic presence/invariant/sweep checks instead) |
| AI-generated code | 100% |
| First-pass approval | pending (this MEM) |

## 13. Pending items and stubs

- [ ] US-023/US-024 (the agents/ family definitions and the roster) —
      later USs
- [ ] The adopters' business glossaries may copy the "Actor" term from
      ONBOARDING §4 if their ubiquitous language needs it

## 14. AITL-MEM-Approval

> **Avenga DevFlow §2.12, §3.0.** This MEM is created by the agent with no
> mutable status and is **never self-approved**. A qualified human (the
> Dev-validator who executed the Bolt) inspects the actual diff,
> test/gate evidence, MEM and manifest, and records `AITL-MEM-Approval`
> here and in the manifest's `checkpoint_approvals[]`.

| Field | Value |
|-------|-------|
| **Reviewers (executing Dev-validator)** | `human:eugenio.serrano` |
| **Roles** | dev_validator |
| **Decision** | approved / changes_requested / rejected |
| **review_ready_at** | `2026-08-23T13:49:00-03:00` |
| **review.started_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **review.decided_at** | `YYYY-MM-DDTHH:mm:ss±HH:MM` |
| **Review evidence** | diff of ONBOARDING + 4 agents + methodology sweep fixes; byte-sync proof (2 diff lines); G-count 39×5; sweep allowlist report; kit-only status; MEM, manifest |
| **Comments** | |
| **Findings** | |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | evidence inspected per the review-evidence column |
