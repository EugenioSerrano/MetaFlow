---
id: "SPEC-260822-0018"
title: "Complete the G29 relaxation sweep — remove stale non-functional BUG-route copies"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
status: "approved" # draft | approved | blocked | obsolete
origin: "BUG-001"
bolt: "US-000.BOLT-004" # ⚠️ MANDATORY
revision: 1
associated_adrs:
  - "devflow/adrs/ADR-002-documentation-defect-classification.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
prerequisites: []
risk_class: "low" # mirrors the Bolt
autonomy_level: "L3" # low → L3 default
turn_budget: "" # platform default
data_classification: "internal"
review_ready_at: "2026-08-22T00:18:05-03:00"
review: # HITL-SPEC-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "dev_validator"}]
  started_at: "2026-08-22T00:23:22-03:00"
  decided_at: "2026-08-22T00:23:22-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Reviewed revision 1 against the approved BUG-001, Bolt US-000.BOLT-004, AREV-001 F-01 and ADR-002/ADR-004: the seven-location inventory matches the grep-verified state, the ACs are objectively checkable (RED→GREEN grep, four-agent sync, G-count 39, root untouched), gates correctly classified, edits kit-only per ADR-004. Approved as drafted — authorizes the V-Bounce."
---

<!--
  LANGUAGE POLICY (§3.15): schema in English; prose in content_language (en).
  ⚠️ BUG SPEC (§3.3.1): strict TDD in ONE V-Bounce — reproduction (RED grep
  evidence) → production change → GREEN. Class-1 documentation defect
  (ADR-002): the "test" is a deterministic grep/diff, not a runtime test.
  Kit-only edits (ADR-004); the root devflow/ is untouched.
-->

# SPEC-260822-0018 — Complete the G29 relaxation sweep: remove stale non-functional BUG-route copies

| Field | Value |
|-------|-------|
| **Origin** | [BUG-001](../bugs/BUG-001-stale-bug-route-copies.md) (approved) |
| **Bolt** | [US-000.BOLT-004](../functional/bolts/US-000.BOLT-004-complete-g29-sweep.md) (approved) |
| **ADRs** | [ADR-002](../adrs/ADR-002-documentation-defect-classification.md) (class-1 defect), [ADR-004](../adrs/ADR-004-repository-partition-v2.md) (kit-only) |
| **Risk Class** | low |
| **Revision** | 1 |

---

## 1. Objective

Finish the G29 relaxation started by `US-000.BOLT-002` / `SPEC-260821-0108`:
edit the seven distributable locations that still carry the pre-relaxation
non-functional BUG-approval route so they state the **approved relaxed rule**,
eliminating the self-contradiction BUG-001 (AREV-001 F-01) documented.

**If not implemented:** the kit keeps contradicting itself — the four
auto-loaded agents disagree with themselves (relaxed G29 row vs stale HITL
row), and a strict reader enforces the old rule, re-blocking an approval G29
now permits (the exact blocker SPEC-260821-0108 removed).

---

## 2. Context

`SPEC-260821-0108` relaxed G29 so a non-functional BUG with `severity:
high|medium|low` may be approved by any team member, the author included. Its
sweep searched only for the **new** phrasing and its file inventory omitted
these seven locations; the §3.0 prose match also wraps across a line, so a
single-line grep for it returned nothing. AREV-001 F-01 (Verdict approved)
confirmed the drift and its root cause; BUG-001 (approved) routes the fix
here. Edits land in `distribution-kit/` only (ADR-004); the root `devflow/`
receives them at the next §5.16 migration.

---

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | `devflow/functional/bolts/US-000.BOLT-004-complete-g29-sweep.md` | HITL-BOLT-READY-Approval ✓ (2026-08-22T00:18:05-03:00) |
| BUG | `devflow/bugs/BUG-001-stale-bug-route-copies.md` | HITL-BUG-Approval ✓ (2026-08-22T00:14:36-03:00) |
| AREV evidence | `devflow/adversarial-reviews/AREV-001-role-availability-blockers-sweep/03-VERDICT.md` (F-01) | HITL-AREV-VERDICT-Approval ✓ |
| ADR | `devflow/adrs/ADR-002-documentation-defect-classification.md` | HITL-ADR-Approval ✓ (accepted) |
| ADR | `devflow/adrs/ADR-004-repository-partition-v2.md` | HITL-ADR-Approval ✓ (accepted) |
| Prior work | `devflow/spec/SPEC-260821-0108-relax-non-critical-bug-approval-routing.md` | HITL-SPEC-Approval ✓ (context, not re-run) |
| Repository baseline | branch `4.2`, HEAD `c794948`; working tree carries this session's uncommitted governance artifacts | — |

Pre-SPEC evidence gate: **all governed sources approved** — no draft input.

---

## 4. Scope

### In scope — the seven stale locations in `distribution-kit/` (grep-verified 2026-08-22)

1. `distribution-kit/CLAUDE.md` line 396 — HITL table `HITL-BUG-Approval` row ("else Developer≠author")
2. `distribution-kit/.agents/skills/avenga-devflow/SKILL.md` line 413 — same row
3. `distribution-kit/.github/agents/AvengaDevFlow.agent.md` line 441 — same row
4. `distribution-kit/.opencode/agents/AvengaDevFlow.md` line 424 — same row
5. `distribution-kit/devflow/README.md` line 248 — checkpoint map ("else Developer≠author")
6. `distribution-kit/devflow/GUARDRAILS.md` line 230 — T02 ("never the artifact's own `owner`/author")
7. `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md` lines 1411–1413 — §3.0 prose ("otherwise to a Developer other than the BUG's own `owner` (self-approval is not permitted…)")

### Out of scope

- The `critical` route and the functional route (unchanged by decision).
- The root `devflow/` tree (frozen — ADR-004; receives change at next migration).
- The broader role-availability policy (US-014) and UNIT/UAT (US-015).
- Historical `CHANGELOG.md` text (not part of the distributable contract).

---

## 5. Prerequisites and baseline

- BUG-001 approved; US-000.BOLT-004 approved (readiness).
- The four agent definitions must be **in sync before the edit** (whole-body
  diff = sanctioned divergence only). If a pre-existing drift is found → stop
  and reconcile first (4-agent rule, AGENTS.md).
- Baseline: branch `4.2`, HEAD `c794948`.

---

## 6. Phases (strict TDD, ONE V-Bounce)

### Phase A — Reproduction (RED evidence)

**Duration:** ~0.25h — **Complexity:** Low

Before any edit, run and record the stale-phrase grep over `distribution-kit/`
(this is the reproduction "test", class-1 defect, ADR-002):

```
rg -n "Developer≠author|other than the BUG'?s own|never the artifact'?s own|other than its author" distribution-kit/
rg -nU "other than the BUG" distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md   # multiline (§3.0 wrap)
```

**Expected RED:** the seven matches of §4 present. Record the output verbatim
in the MEM as red evidence.

### Phase B — Fix (kit edits, four agents synchronized)

**Duration:** ~0.5h — **Complexity:** Low

Apply the relaxed wording at each location, phrased consistently with the
existing relaxed G29 row ("any team member, author included"):

**Files modified:**
- The four agents (`CLAUDE.md` 396, `SKILL.md` 413, `AvengaDevFlow.agent.md` 441, `AvengaDevFlow.md` 424) — the `HITL-BUG-Approval` HITL-table row becomes, **identically**:
  `| \`HITL-BUG-Approval\` | FA (functional) / Architect-TL if severity=critical else any team member, author included (non-functional) | BUG confirmed; only then its dedicated Bolt |`
- `distribution-kit/devflow/README.md` 248 — checkpoint-map row:
  `| \`HITL-BUG-Approval\` | Functional Analyst (functional) / Architect-TL if \`severity: critical\` else any team member, author included (non-functional) | BUG confirmed; only then its dedicated Bolt |`
- `distribution-kit/devflow/GUARDRAILS.md` 230 (T02) — preserve the traceability intent, fix the routing:
  `| T02 | Every BUG carries \`HITL-BUG-Approval\` and references its exactly-one dedicated Bolt; the Bolt references the BUG. For a non-functional BUG, the recorded reviewer matches its \`severity\` route (§2.16): Architect/Tech Lead when \`severity: critical\` (never the BUG's own author), otherwise any team member, the author included |`
- `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md` 1411–1413 (§3.0 prose) — replace "otherwise to a Developer other than the BUG's own `owner` (self-approval is not permitted under this exception)" with "otherwise to any team member, the BUG's own author included (self-approval is permitted at these severities and remains prohibited only on the `critical` route)".

No other lines change. The `agents-data/<agent>/` path line remains the single sanctioned four-agent divergence.

### Phase C — Verification (GREEN)

**Duration:** ~0.25h — **Complexity:** Low

Run and record the full verification set (§8); capture GREEN output in the MEM.

---

## 7. Acceptance criteria

### AC-1: RED evidence recorded
**Given** the unedited kit, **When** the stale-phrase grep (Phase A) runs,
**Then** the seven §4 matches are present and captured in the MEM.

### AC-2: No stale route remains
**Given** the edited kit, **When** grepping `Developer≠author`, `other than
the (BUG|Bolt)'s own`, `never the artifact's own`, `other than its author`
(single-line **and** multiline), **Then** zero matches remain in
`distribution-kit/`.

### AC-3: Relaxed rule present at every location
**Given** the edited kit, **When** grepping the seven locations, **Then** each
states the relaxed non-critical route ("any team member, author included" or
the T02/prose equivalent).

### AC-4: Critical and functional routes unchanged
**Given** the edited kit, **When** grepping "Architect/TL if severity=critical"
/ "Architect or Tech Lead when `severity: critical`" and "Functional Analyst",
**Then** both still appear unchanged in every location that defines them.

### AC-5: Four-agent sync + G-count
**Given** the edited agents, **When** running the whole-body diff (CRLF-normalized)
and `grep -cE '^\| G[0-9]{2} \|'`, **Then** the four agents differ only by the
sanctioned `agents-data/<agent>/` line and each inline G-table counts 39; GUARDRAILS G-count stays 39.

### AC-6: Root untouched
**Given** the completed V-Bounce, **When** `git status --short` runs, **Then**
no root `devflow/` methodology-content file is modified — only
`distribution-kit/` files plus this Bolt's governance records.

### AC-7: Bolt-manifest validation
**Given** the manifest updated for this revision, **When** validated against
`manifest-v4-bolt.schema.json`, **Then** 0 errors.

### AC mapping to source (non-functional)

| Source outcome | How satisfied | Evidence |
|----------------|---------------|----------|
| BUG-001 expected_result (relaxed rule everywhere) | Phase B | AC-2, AC-3 |
| Critical/functional routes preserved | Phase B leaves them intact | AC-4 |
| Four-agent consistency (AREV-001 F-01) | Phase B identical edits | AC-5 |
| Kit-only (ADR-004) | Phases touch `distribution-kit/` only | AC-6 |

---

## 8. Testing strategy

Deterministic command set (no runtime):
- **RED (AC-1):** stale-phrase grep before edit → seven matches (MEM).
- **GREEN (AC-2, AC-3):** stale grep → 0; relaxed-phrase grep → present at all seven.
- **Sync (AC-5):** four-agent whole-body diff (AGENTS.md command) + `grep -cE '^\| G[0-9]{2} \|'` = 39 each.
- **Root check (AC-6):** `git status --short`.
- **Manifest (AC-7):** schema validation.
- **Edge cases:** the §3.0 multiline wrap (use `rg -U`); the escaped pipe `\|` inside table cells; CRLF/LF normalization before the sync diff.
- **BUG evidence:** RED grep (before) and GREEN grep (after) recorded separately in the MEM.

---

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | — | `n/a` — documentation-only, no executable code |
| SAST / SBOM | — | `n/a` — no code, no dependencies |
| Perf-smoke (p95/p99) | — | `n/a` — no runtime |
| Prompt-injection scan | — | `pass` — all text authored here |
| Secret-leak scan | — | `pass` |
| Hallucination lint | — | `pass` — every path/§-reference resolves on disk |
| IP / license provenance | — | `n/a` — no third-party content |
| PII / DLP | — | `n/a` — `internal`, no personal data |
| Dependency-confusion | — | `n/a` — no dependencies |
| Test-first evidence | — | `pass` — grep RED before edit, GREEN after (§3.3.1) |
| Behavioral reproducibility | — | `pass` — deterministic, idempotent grep/diff |
| Bolt-manifest validation | — | `pass` — 0 errors against `manifest-v4-bolt.schema.json` |

---

## 10. Security and data

No security boundary, credential, runtime surface or data path is touched; the
`critical` route (the security-bearing one) stays strict. Data classification
`internal` — documentation text only.

---

## 11. Monitoring and observability

`n/a` — no runtime. The §8 verification suite is the observability; its output
is captured in the MEM.

---

## 12. Migration, compatibility and rollback

- **Migration:** none here; reaches adopters at their next §5.16 migration.
- **Compatibility:** G-count stays 39; checkpoint vocabulary unchanged; no consumer breaks.
- **Rollback:** revert the kit commit(s); root untouched; the SPEC revision is immutable manifest history.

---

## 13. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| A location missed | 2 | 3 | §4 inventory from grep; AC-2 asserts zero stale (single-line + multiline) |
| Four-agent drift introduced | 2 | 3 | Identical text; AC-5 sync diff mandatory |
| Root `devflow/` edited by mistake | 1 | 4 | Kit-only edits; AC-6 `git status` check |
| T02 rewrite breaks its traceability intent | 1 | 2 | New T02 keeps the "reviewer matches severity route" clause; only the routing fact changes |
| Markdown table broken by escaped pipe | 1 | 2 | Edge case in §8; verification reads the row text |

---

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| Phrase all locations as "any team member, author included" | Matches the already-installed relaxed G29 row — one wording everywhere (AREV-001 F-01 / REV-001 F-07 consistency) |
| T02 keeps its structure, only the routing fact changes | Preserves the traceability rule while removing the false "never the author" absolute |
| Kit-only edits | ADR-004 rules 1, 2 — the root rulebook is frozen until migration |
| No new patterns invented for the fix | The relaxed rule already exists and is approved; this only propagates it |

---

## 15. Stop conditions

- Pre-existing four-agent drift before Phase B (sync diff > sanctioned) → stop, reconcile first, record in MEM.
- Any root `devflow/` methodology file appears in the diff → stop, revert, record.
- AC-2 still shows stale matches after Phase B → stop, sweep again (do not assume).
- A governed source changes materially during execution (G15) → stop, revise, re-approve.

---

## 16. Definition of Done (DoD)

- [ ] Phases A–C implemented
- [ ] AC-1..AC-7 pass (RED recorded, GREEN zero stale, routes preserved, sync 39/39/39/39, root untouched, manifest 0 errors)
- [ ] Follows ADR-002 (class-1) and ADR-004 (kit-only)
- [ ] Gates pass / n/a per §9
- [ ] MEM created in `devflow/memory/` (red + green evidence)
- [ ] Manifest `v_bounces[]` entry appended
- [ ] HITL-MEM-Approval recorded

---

## 17. References

- BUG-001 (approved), US-000.BOLT-004 (approved), AREV-001 Verdict (F-01)
- SPEC-260821-0108 / US-000.BOLT-002 (the relaxation this completes)
- ADR-002 (class-1 classification), ADR-004 (kit-only), AGENTS.md (four-agent sync)

---

## 18. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-22 | eugenio.serrano | Initial revision 1 (draft) |

---

## 19. HITL-SPEC-Approval

> **Avenga DevFlow §2.4.1, §3.0.** Draft until the Dev-validator records
> `HITL-SPEC-Approval` (in the `review` block). Bolt approval authorizes SPEC
> preparation; **SPEC approval** authorizes the V-Bounce. A material source
> change invalidates this approval — stop, revise, re-approve (G15).

| Field | Value |
|-------|-------|
| **review.reviewers** | eugenio.serrano (dev_validator) |
| **review.decision** | approved |
| **review_ready_at** | `2026-08-22T00:18:05-03:00` |
| **review.started_at** | `2026-08-22T00:23:22-03:00` |
| **review.decided_at** | `2026-08-22T00:23:22-03:00` |
