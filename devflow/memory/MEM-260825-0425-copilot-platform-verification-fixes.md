---
id: "MEM-260825-0425"
title: "The Copilot platform verification fixes — spawn tool, execution-evidence rule and the VERIFICATION.md Copilot-row batch (US-025.BOLT-006, V-Bounce 1)"
date: "2026-08-25"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
bolt: "US-025.BOLT-006"
spec: "SPEC-260825-0417"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review" # ready_for_review | failed | blocked | cancelled
baseline: "b3ddb4e" # git commit of the repository baseline used by this V-Bounce
applied_adrs:
  - "devflow/adrs/ADR-013-agent-lifecycle-governance.md"
  - "devflow/adrs/ADR-014-actors-roster-is-the-enablement.md"
manifest: "devflow/metrics/bolts/US-025.BOLT-006-copilot-platform-verification-fixes.json"
diff_ref: "" # working tree — the changes are uncommitted (G34: no commit without explicit request)
review_ready_at: "2026-08-25T04:25:34-03:00"
review: # AITL-MEM-Approval — decision dictated in conversation ("aprobado!") and transcribed by the agent (§3.0)
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-25T04:28:18-03:00"
  decided_at: "2026-08-25T04:28:18-03:00"
  findings: []
  acknowledged_without_comment: true # must be true when findings is empty (§3.0)
  acknowledgment_reason: "Approved as Dev-validator after inspecting the diff of the 3 kit files, the deterministic checks (sync diff 0 drift, G-count 39/39, frontmatter parse, greps, test-folder hash sync), the MEM narrative and the validated Bolt manifest; an independent cross-check by a second model (Opus) was invited and its precision note on the body-size wording was applied before signing. V-Bounce 1 complete."
---

# MEM-260825-0425 — The Copilot platform verification fixes (US-025.BOLT-006, V-Bounce 1)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | US-025.BOLT-006 (AITL-BOLT-READY-Approval 2026-08-25) |
| **SPEC**        | [SPEC-260825-0417](SPEC-260825-0417-copilot-platform-verification-fixes.md) (revision 1 — AITL-SPEC-Approval 2026-08-25) |
| **V-Bounce**    | 1 |
| **ADRs**        | ADR-013 (lifecycle governance), ADR-014 (roster enablement) |

---

## 1. Executive summary

This V-Bounce delivered the REV-006 routing under US-025.BOLT-006: the
three kit files that make the GitHub Copilot platform surface of the agent
lifecycle work and document it correctly. The Copilot Coordinator's
frontmatter now includes the platform's canonical `agent` alias in its
`tools:` list, which turns the body's spawn-topology claim ("Only your
tools include the `agent` alias") from a declaration into configuration —
an installed role agent becomes agent-invocable, closing the shipped
defect REV-006 F-01 observed in the smoke test, where the Coordinator
silently self-executed every delegated review. The platform docs gained
the execution-evidence rule (an author stamp must trace to a real spawn;
a stamp without execution is a false claim — REV-006 F-02) and the four
Copilot-row facts the test established (spawn requires the `agent` tool;
role wrappers are user-invocable by default; validate the roster after an
agent edit because the edit tool can write TAB indentation; the 30k
prompt cap documented by GitHub applies to the cloud agent, while the
full agent body (≈68.9k chars; file total ≈69.6k) was verified loading in
VS Code). All deterministic gates
passed: the four-agent sync diff shows exactly the sanctioned two
agents-data path lines of divergence (the shared methodology body is
byte-identical), the G-count reads 39/39 in all four agent files, the
modified frontmatter parses as valid YAML with `agent` present, and every
new documented fact greps at its expected location. The three changed
files were synced byte-for-byte into the adopter test project
(`C:\GitHubRepos\AvengaDevFlow-test\copilot`), so the acceptance demo
(AC-4, the live spawn probe) can now be run by the human in a fresh VS
Code session. One self-correction happened during the V-Bounce: my first
frontmatter comment referenced maintenance-partition IDs (US-/BOLT-),
which violates US-025 AC-9 (the kit files carry no maintenance-partition
references) — the comment was rewritten to be self-contained before the
checks ran. No deviations from the SPEC remain; the live spawn probe is
the only evidence pending, and it is a human-run acceptance demo by
design.

---

## 2. Implemented phases

### Phase A — The Coordinator spawn tool

The Copilot Coordinator file `distribution-kit/.github/agents/
AvengaDevFlow.agent.md` had its frontmatter `tools:` array extended with
`'agent'` (placed first, with a two-line comment explaining that this is
the canonical agent→agent invocation alias and that without it the
Coordinator silently self-executes delegated work). The alias is the one
the GitHub custom-agents configuration reference documents ("Allows a
different custom agent to be invoked to accomplish a task"), and it is
the same word the agent body already used in its spawn-topology sentence,
so no body change was needed — the shared methodology body below the
frontmatter remains byte-identical to the other three platforms, per
US-025 AC-1/AC-7/AC-9 and ADR-004. The role wrappers' projection is
untouched: they still omit the `agent` alias, preserving the
executors-cannot-spawn ceiling (ADR-014).

### Phase B — VERIFICATION.md Copilot row + the execution-evidence rule

`distribution-kit/devflow/agents/VERIFICATION.md` received two additions:
(1) a new "Execution evidence (attribution integrity)" paragraph right
after the spawn-topology paragraph, stating that an executor's production
may be persisted by the Coordinator but the persistence act must trace to
a real spawn — stamping another actor's identity on content that actor
never produced is a false claim, and when spawn is unavailable, direct
human invocation is the only legitimate reviewer session; and (2) the
"GitHub Copilot" section's bullets were rewritten to carry the four
verified facts: the spawn tool requirement (with the observed failure
mode), wrapper user-invocable default with the `user-invocable: false`
guidance, the post-edit roster validation note (TAB indentation observed
in the smoke test), and the 30k cap scoped to the cloud agent with the
VS Code full-load verification. `distribution-kit/devflow/agents/README.md`
gained one contract line under the "two sides of an agent" table —
production-vs-persistence: `write_paths` bounds the agent's own direct
writes, not its output, and the persistence act must trace to a real
spawn. Both files are part of the docs-primary projection path
(US-025 AC-8), so the shipped mapping is now self-consistent with the
Coordinator's actual configuration.

### Phase C — Verification evidence

The deterministic checks from SPEC §6-C.1 ran green: the four-agent sync
diff (from the methodology heading to end of file) shows exactly 2
differing lines per comparison, and only the sanctioned
`devflow/agents-data/<agent>/` path line; the G-count sweep reads 39/39
in all four agent files against GUARDRAILS.md; the modified `.agent.md`
frontmatter parses as YAML with `agent` present (27 tools); and greps
confirm the execution-evidence rule and the four Copilot-row facts at
their expected lines. The three changed files were then copied
byte-for-byte into the adopter test project and hash-verified, ready for
the human-run live spawn probe (SPEC AC-4).

---

## 3. Files created

| File | Purpose |
|------|---------|
| (none — the V-Bounce modified three existing kit files; no new files were required) | |

---

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `distribution-kit/.github/agents/AvengaDevFlow.agent.md` | Frontmatter `tools:` array gains the canonical `agent` alias (agent→agent invocation) with a self-contained explanatory comment — the Coordinator's spawn topology becomes configuration-backed; shared body untouched |
| `distribution-kit/devflow/agents/VERIFICATION.md` | New "Execution evidence (attribution integrity)" paragraph after the spawn-topology rule; the GitHub Copilot section bullets rewritten with the four verified platform facts (spawn tool requirement, user-invocable default, roster TAB-validation note, cloud-agent 30k scope) |
| `distribution-kit/devflow/agents/README.md` | One contract line under the two-sides table: production may be persisted by the Coordinator but must trace to a real spawn; `write_paths` bounds the agent's own writes, not its output |

---

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
| —    | —        | —      |

---

## 6. Files deleted

| File | Reason |
|------|--------|
| —    | —      |

---

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| Add `'agent'` rather than `custom-agent`/`Task` | The documented canonical primary alias; identical to the wording the agent body already uses |
| No `agents:` field added to the Coordinator | Platform default is `*` (all invocable) — the minimal change unblocks spawn without over-restricting; an explicit allowlist can be a later hardening (recorded in the SPEC §14) |
| Docs-only treatment for the 30k cap | No defect on VS Code (verified full load); a wording correction, not a code change |
| Execution-evidence rule placed in both VERIFICATION.md and agents/README.md | Both are the docs-primary projection path (US-025 AC-8) and the executor contract home — the rule must reach an adopter reading either |
| Frontmatter comment kept free of maintenance-partition IDs | US-025 AC-9 — the kit files carry no `US-`/`ADR-`/`DISC-`/`BOLT-` references (self-corrected during the V-Bounce after my first draft violated it) |
| Changed files synced individually into the test project (not a wholesale re-copy) | The adopter project holds live team config (roster, actors, DISC-001, REV-001) that a wholesale copy would destroy |

---

## 8. Deviations and assumptions

- **No deviations from the SPEC.** One implementation self-correction
  (the AC-9 comment fix) happened before any check ran and is recorded in
  §7 — it did not change the scope.
- Assumption: the live spawn probe (SPEC AC-4) will be run by the human
  in a fresh VS Code session on the synced test project; its result is
  acceptance evidence, not V-Bounce readiness evidence.
- The V-Bounce changes are uncommitted (G34 — no commit without an
  explicit request); the baseline `b3ddb4e` is the last commit.

---

## 9. Verification evidence

### Build
```
n/a — documentation/config kit, no build
```

### Tests (deterministic checks — SPEC §6-C.1)
```
1) Four-agent sync diff (methodology heading → EOF, CRLF-normalized):
   codex    vs claude:   2 differing lines — only the agents-data/codex/ path line
   ghcopilot vs claude:  2 differing lines — only the agents-data/gh-copilot/ path line
   opencode vs claude:   2 differing lines — only the agents-data/open-code/ path line
   → PASS (0 shared-body drift)

2) G-count sweep (^\| G[0-9]{2} \| per agent file vs GUARDRAILS.md):
   GUARDRAILS: 39 · CLAUDE.md: 39/39 · SKILL.md: 39/39 ·
   AvengaDevFlow.agent.md: 39/39 · AvengaDevFlow.md: 39/39 → PASS

3) Frontmatter parse (PyYAML) of the modified .agent.md:
   YAML parses OK · 'agent' in tools: True · tools count: 27 → PASS

4) Content greps:
   VERIFICATION.md: "Execution evidence" line 50 · "false claim" line 54 ·
   "Agent-initiated spawn requires" line 120 · "user-invocable by default" line 125 ·
   "TAB indentation" line 131 · "cloud agent" line 137 → PASS
   agents/README.md: "real spawn" line 89 · "false claim" line 90 → PASS

5) Test-project sync: SHA-256 of the 3 changed files in distribution-kit
   == the copies in C:\GitHubRepos\AvengaDevFlow-test\copilot → PASS (3/3)
```

### BUG V-Bounce evidence (if applicable)
- n/a — not a BUG-driven Bolt (the defect evidence lives in REV-006)

### Gates
- Unit/integration/SAST/SBOM/perf: n/a (no runtime, docs/config only)
- Prompt-injection scan: n/a (no new executable content)
- Secret-leak scan: pass (no secrets introduced)
- Hallucination lint: pass (every new claim traces to REV-006 evidence or verified platform docs)
- IP/license, PII/DLP, dependency-confusion: n/a (internal docs, no third-party content, no dependencies)
- Test-first evidence: pass (verification-first — the checks were defined in the SPEC before the V-Bounce)
- Behavioral reproducibility: pass (the spawn probe is reproducible on the re-synced test project)
- Bolt-manifest validation: pass (manifest validates against manifest-v5-bolt.schema.json)

---

## 10. Manual interventions

None — the agent produced everything (one self-correction inside the
V-Bounce, §7).

---

## 11. Evidence links

- **Diff / PR:** working tree (uncommitted — G34); the changes are the 3
  kit files listed in §4 + the governance records of this Bolt
- **Commit:** baseline `b3ddb4e` (the V-Bounce changes are not yet committed)
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-025.BOLT-006-copilot-platform-verification-fixes.json`

---

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~0.5h (SPEC + V-Bounce + records, single session) |
| V-Bounce number | 1 |
| Tests created | 0 automated (n/a — docs/config); 5 deterministic checks + 1 pending human probe (AC-4) |
| AI-generated code | 100% (no human fallback) |
| First-pass approval | pending (AITL-MEM-Approval) |

---

## 13. Pending items and stubs

- [ ] **AC-4 — the live spawn probe** (human-run, acceptance demo): fresh
      VS Code session on `C:\GitHubRepos\AvengaDevFlow-test\copilot` →
      delegate a review to `reviewer-copilot` → expect the subagent pill
      (the spawn actually happens). Result feeds `AITL-BOLT-DONE-Approval`.
- [ ] REV-006 routing residue: F-06..F-09 attach to REV-005's already-
      routed destinations (charter Bolt US-023 · docs Bolt US-024 ·
      ADR-014 v2 backlog) — outside this Bolt.
- [ ] Commit the tree when the human requests it (G34).

---

## 14. AITL-MEM-Approval

> **Avenga DevFlow §2.12, §3.0.** This MEM is created by the agent with no
> mutable status and is **never self-approved**. A qualified human (the
> Dev-validator who executed the Bolt; QA/Sec/domain reviewers optional, any risk)
> inspects the actual diff, test/gate evidence, MEM and manifest, and
> records `AITL-MEM-Approval` here and in the manifest's
> `checkpoint_approvals[]`. `approved` completes the V-Bounce (and, if latest,
> marks the Bolt `Development Completed`); `changes_requested` keeps this
> MEM as immutable history and the next execution is a NEW V-Bounce with a
> NEW MEM. `AITL-BOLT-DONE-Approval` is still required for `Done`.

| Field | Value |
|-------|-------|
| **Reviewers (executing Dev-validator; QA/Sec/domain optional)** | `human:eugenio.serrano` |
| **Roles** | dev_validator |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-25T04:25:34-03:00` — set at package submission, before review |
| **review.started_at** | `2026-08-25T04:28:18-03:00` |
| **review.decided_at** | `2026-08-25T04:28:18-03:00` |
| **Review evidence** | diff of the 3 kit files · the 5 deterministic checks (sync diff, G-count, frontmatter, greps, hashes) · MEM narrative · validated Bolt manifest |
| **Comments** | independent second-model cross-check (Opus) invited; its body-size precision note applied before signing |
| **Findings** | none |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | evidence inspected (listed above) — V-Bounce 1 approved |
