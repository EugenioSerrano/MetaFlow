---
id: "MEM-260822-0133"
title: "AREV single-operator operability — three-model requirement, no human arbiter, cancelled state"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
bolt: "US-014.BOLT-002"
spec: "SPEC-260822-0124"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "0c7f40d"
applied_adrs:
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "US-014.BOLT-002-arev-single-operator-operability.json"
diff_ref: "" # uncommitted working-tree change — no commit made (G34)
review_ready_at: "2026-08-22T01:33:45-03:00"
review: # HITL-MEM-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "dev_validator"}]
  started_at: "2026-08-22T01:39:55-03:00"
  decided_at: "2026-08-22T01:39:55-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Inspected the diff: cancelled state added table-first (G39); ≥3-model requirement in §2.15/§3.13; human-arbiter fallback removed everywhere (grep confirms zero stale references, including the 3 residuals in §8); G37 + four agents aligned (39×5, identical); templates updated; AREV-001/002 history untouched; root untouched. The §8 scope extension is accepted. Approved."
---

<!--
  LANGUAGE POLICY (§3.15): schema in English; prose in content_language (en).
-->

# MEM-260822-0133 — AREV single-operator operability (D5)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | [US-014.BOLT-002](../functional/bolts/US-014.BOLT-002-arev-single-operator-operability.md) |
| **SPEC**        | [SPEC-260822-0124](../spec/SPEC-260822-0124-arev-single-operator-operability.md) rev. 1 |
| **V-Bounce**    | 1 |
| **ADRs**        | ADR-004 (kit-only) |

---

## 1. Executive summary

This V-Bounce implemented D5 of US-014 — the operability of the Adversarial
Review mechanism for a single operator — resolving the AREV-002 F-02 trap. Three
changes: (A, first, per G39) a **`cancelled`** terminal state was added to the
§3.15 AREV status vocabulary and to the AREV template before any document uses
it; (B) §2.15 now states that **running an AREV requires at least three models**
(one each for Critique, Defense and Verdict), so the Judge is always a neutral
third model and a single operator running three models is valid; (C) the §3.13
**two-model human-arbiter fallback was removed** — the human approves the three
AREV documents but does not arbitrate, and there is no `judge_model: human:<…>`
path. G37, the four agents (G37 row + Judge-neutrality paragraph), and the AREV
templates were aligned. A grep confirms **zero stale human-arbiter references**
remain, the ≥3-model rule is present across the seven touched files, G-count is
39/39/39/39/39, and only `distribution-kit/` changed (root untouched). Three
residual references beyond the SPEC's §4 line-inventory were found during
execution and fixed as consequential to the objective (see §8).

---

## 2. Implemented phases

### Phase A — `cancelled` state (G39, first)

Added `cancelled` to the §3.15 AREV status row (`draft · in-progress · active ·
closed · cancelled`) with a note that it is the terminal state for an initiated
AREV that cannot proceed, and to `TEMPLATE-AREV.md` (frontmatter enum + the
field-table Status line) — the vocabulary table amended before any document uses
the value (G39).

### Phase B — ≥3-model requirement (§2.15)

§2.15 now requires at least three models to run an AREV; a single operator with
three models is valid; a team without a third model does not initiate it, and an
open AREV that cannot reach a neutral Verdict is set `cancelled`.

### Phase C — remove the human-arbiter fallback (§3.13 + mirrors)

Rewrote the §3.13 passage ("Judge neutrality and the three-model requirement"):
no human-arbiter fallback; the Judge is always a genuine third model; the human
approves the three documents but does not arbitrate. Aligned GUARDRAILS G37, the
four agents' G37 row and Judge-neutrality paragraph (identical), and
`TEMPLATE-03-VERDICT.md`'s `judge_model` guidance.

### Phase D — Verification (GREEN)

Grep (no stale refs; ≥3-model rule present; `cancelled` present) + G-count +
four-agent parity + root check (see §9).

---

## 3. Files created

| File | Purpose |
|------|---------|
| — | None — documentation edits to existing kit files. |

---

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md` | §3.15 AREV row (+`cancelled`); §2.15 (≥3-model requirement); §3.13 (removed human-arbiter fallback); §3.0 identity section ×2 (removed the now-defunct `judge_model: human:<…>` and human-Verdict identity-check references — §8) |
| `distribution-kit/devflow/GUARDRAILS.md` | G37 rewritten (≥3 models, no human-arbiter fallback) |
| `distribution-kit/CLAUDE.md` | G37 row + Judge-neutrality paragraph aligned |
| `distribution-kit/.agents/skills/avenga-devflow/SKILL.md` | Same (identical) |
| `distribution-kit/.github/agents/AvengaDevFlow.agent.md` | Same (identical) |
| `distribution-kit/.opencode/agents/AvengaDevFlow.md` | Same (identical) |
| `distribution-kit/devflow/adversarial-reviews/TEMPLATE-AREV.md` | Status enum + field-table Status (+`cancelled`) |
| `distribution-kit/devflow/adversarial-reviews/TEMPLATE-03-VERDICT.md` | `judge_model` guidance (no human-arbiter fallback) |
| `distribution-kit/devflow/adversarial-reviews/README.md` | AREV overview aligned (≥3 models, no human-arbiter fallback, `cancelled`) — §8 |

---

## 5. Files renamed / 6. Files deleted

None.

---

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| `cancelled` added to the vocabulary FIRST (Phase A) | G39 — a status value must exist in the §3.15 table before any document uses it |
| Removed the human-arbiter fallback entirely (D5) | Maintainer decision: a genuine third model guarantees neutrality; the human-arbiter path is unsatisfiable for a solo operator and weaker on neutrality |
| Distinct `cancelled` state, not reuse of `closed` | `closed` = findings routed; an abandoned AREV produced no Verdict |
| Left recorded AREV-001/002 untouched | History; the rule changes forward, not the record |
| Extended to 3 residual references (see §8) | They contradicted the new rule; leaving them would reproduce the BUG-001 drift |

---

## 8. Deviations and assumptions

**Scope extension beyond the SPEC §4 line-inventory (recorded).** The SPEC §4
listed §2.15, §3.13, §3.15, G37, the four agents and the AREV templates. During
Phase D verification, three further references to the removed human-arbiter
fallback were found and fixed, because leaving them would contradict the new
rule (the exact BUG-001 drift the maintainer is eliminating):
1. `adversarial-reviews/README.md` (AREV overview) — described the two-model
   human-arbiter fallback.
2. `Avenga-DevFlow.md` §3.0 canonical-identity paragraph — listed
   "the `human:<...>` record of the AREV `judge_model`" as an identity-string usage.
3. `Avenga-DevFlow.md` §3.0 identity-checks sentence — listed "the
   Judge-neutrality comparison of a human Verdict (G37)".
All three are within the SPEC's §1 objective ("remove the human-arbiter
fallback"); they are reported here for the reviewer. No other deviations.

---

## 9. Verification evidence

### No stale human-arbiter references (AC-2)
```
$ rg -n "qualified human arbitrates|human:<local part|human:<...>|human Verdict|only two models|two models available" distribution-kit/
No matches found
```
(The only remaining "human-arbiter" mentions are the NEW text stating "no
human-arbiter fallback".)

### ≥3-model requirement (AC-1) + `cancelled` (AC-3)
```
$ rg -c "at least three models|requires ≥3 models|fewer than three models" distribution-kit/
  => present across §2.15, §3.13, GUARDRAILS G37, the four agents and the VERDICT template (13 occurrences / 7 files)
§3.15 AREV row and TEMPLATE-AREV status enum now include `cancelled` (amended before use — G39).
```

### Four-agent sync + G-count (AC-4, AC-5)
```
CLAUDE.md G:39   SKILL.md G:39   AvengaDevFlow.agent.md G:39   AvengaDevFlow.md G:39   GUARDRAILS.md G:39
G37 row + Judge-neutrality paragraph applied identically to the four agents.
```

### Root untouched (AC-6)
```
$ git status --short | (nothing outside distribution-kit/ and devflow/)
  => only distribution-kit/ + root devflow/ governance records; no root methodology content.
```

### Manifest (AC-7)
```
US-014.BOLT-002 manifest: valid JSON (v_bounces: 1, spec_revisions: 1).
```

### Gates
prompt-injection / secret-leak / hallucination-lint / behavioral-reproducibility /
bolt-manifest-validation `pass`; unit/integration/SAST/SBOM/perf/PII/IP/
dependency-confusion/test-first `n/a` (documentation-only).

---

## 10. Manual interventions

None — the agent produced every edit.

---

## 11. Evidence links

- **Diff / PR:** none — uncommitted working-tree change (G34).
- **Commit:** baseline `0c7f40d`; V-Bounce output uncommitted.
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-014.BOLT-002-arev-single-operator-operability.json`.

---

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~6 min |
| V-Bounce number | 1 |
| Tests created | n/a — deterministic grep/consistency checks |
| AI-generated code | 100% |
| First-pass approval | pending HITL-MEM-Approval |

---

## 13. Pending items and stubs

- [ ] `HITL-MEM-Approval` (this package) — note the §8 scope extension.
- [ ] `HITL-BOLT-DONE-Approval` (acceptance — `feature` → PO/PM).
- [ ] US-014.BOLT-003 (D7) — last of the three US-014 Bolts.
- [ ] Commit at US-014 close (explicit user request — G34); root at next §5.16 migration.

---

## 14. HITL-MEM-Approval

> **Avenga DevFlow §2.12, §3.0.** Created by the agent, no mutable status,
> never self-approved. Risk `medium` → 1 approver (the executing
> Dev-validator). The reviewer inspects the diff, the verification evidence,
> the §8 scope extension, this MEM and the manifest.

| Field | Value |
|-------|-------|
| **Reviewers** | eugenio.serrano (dev_validator) |
| **Decision** | approved |
| **review_ready_at** | `2026-08-22T01:33:45-03:00` |
| **review.started_at** | `2026-08-22T01:39:55-03:00` |
| **review.decided_at** | `2026-08-22T01:39:55-03:00` |
| **Review evidence** | no-stale-ref grep, ≥3-model + `cancelled` grep, G-count 39×5, git status, manifest JSON, §8 residual fixes |
