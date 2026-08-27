---
id: "SPEC-260824-1144"
title: "The per-platform lifecycle surface — the four preambles rewritten to the ship model, and the mapping made deterministic (permissions, inherit, platform notes)"
date: "2026-08-24"
author: "eugenio.serrano"
llm: "claude-fable-5"
status: "approved" # draft | approved | blocked | obsolete — AITL-SPEC-Approval 2026-08-24
origin: "US-025"
bolt: "US-025.BOLT-002"
revision: 1
associated_adrs:
  - "devflow/adrs/ADR-013-agent-lifecycle-governance.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
prerequisites:
  - "devflow/spec/SPEC-260824-1101-mainagent-lifecycle-body.md" # executed (V-Bounce 1 MEM approved) — the shared body this SPEC's preambles complement; its section hash is this SPEC's unchanged-gate reference
risk_class: "low"
autonomy_level: "L3" # low risk → L3 default (§3.3)
turn_budget: ""
data_classification: "internal"
review_ready_at: "2026-08-24T11:46:17-03:00"
review: # AITL-SPEC-Approval — decision dictated in conversation ("aprobamos!") and transcribed by the agent (§3.0)
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-24T13:01:28-03:00"
  decided_at: "2026-08-24T13:01:28-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved as Dev-validator after an independent cross-model SPEC review (no blocking findings): the four preamble old-strings verified verbatim on disk, the four new preambles complete the common checklist with the spawn controls preserved, and the reviewer REPRODUCED the pinned hash-gate reference (cd24754c320df93c85339aadcddb1803 on all four files with the §8 convention) — its own earlier finding closed with evidence. The approver decision taken with the reviewer's recommendation: B.1's approver-class deny clause KEPT as a deliberate partial implementation of the REV-005 F-11 v2 spec (wrapper-mapping half; the schema half stays in the ADR-014 v2 backlog — recorded in §14 and the MEM §13 so the future hardening implements only the remainder). F-09 closes with the omission interpretation (§14). The pre-V-Bounce batch is committed first (observation #3). Authorizes the V-Bounce (revision 1)."
---

# SPEC-260824-1144 — The per-platform lifecycle surface

| Field | Value |
|-------|-------|
| **Origin** | US-025 (approved 2026-08-24) |
| **Bolt** | US-025.BOLT-002 (READY 2026-08-24, risk low) |
| **ADRs** | ADR-013 §3.9 (ship model), ADR-004 (kit-only) |
| **Risk Class** | low |
| **Revision** | 1 |

---

## 1. Objective

Rewrite the four MainAgents' **platform preambles** (the only part that
legitimately differs across the four) to the ship-model reality — each
names ITS spawn folder, wrapper format and the projection wiring from
`agents/squad/` — completing US-025 **AC-9** (zero maintenance-partition
references in the four files), and make the shipped mapping
(`agents/VERIFICATION.md`) **deterministic**: the permission-block
derivation, the `model: inherit` rule and the OpenCode platform notes. If
not implemented, the preambles keep describing deleted wrappers and citing
maintainer artifacts, and two projections of the same definition can
legally differ (the field-proven `list: allow` drift, REV-005 F-14).

## 2. Context

BOLT-001 delivered the shared lifecycle body; its MEM (§13) carries the
verified remainder this SPEC consumes: the preamble references
(`ADR-007 §3.4`, `US-023 AC-6` ×4, `DISC-002 §4.2` in Codex's), Claude's
stale `Agent(architect-agent, …)` list and Codex's stale "role agents live
in `.codex/agents/*.toml`" sentence. REV-005 routes F-09 (`inherit`),
F-13 (OpenCode notes) and F-14 (permission spec) here. The READY approval
pinned two reviewer precisions: the **hash-extraction convention** for the
unchanged-gate, and the **scoped** zero-references claim.

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | US-025.BOLT-002 | AITL-BOLT-READY-Approval ✓ (2026-08-24T11:43:14) |
| Feature US | US-025 | AITL-US-Approval ✓ |
| ADR | ADR-013 / ADR-004 | AITL-ADR-Approval ✓ |
| REV evidence | REV-005 (F-09/F-13/F-14) | AITL-REV-Approval ✓ |
| MEM evidence | MEM-260824-1115 §13 (the remainder list) | AITL-MEM-Approval ✓ (2026-08-24T11:18:48) |
| Repository baseline | `ebf48d0` | — |

## 4. Scope

### In scope
- The four platform preambles (one paragraph each: kit `CLAUDE.md` L41,
  `SKILL.md` L46, `AvengaDevFlow.agent.md`, `AvengaDevFlow.md` L57).
- `distribution-kit/devflow/agents/VERIFICATION.md` (the mapping
  precision + two internal consistency touches).

### Out of scope
- The shared lifecycle body (BOLT-001 — its hash is this SPEC's
  **unchanged** gate); the delete-safe depth (BOLT-003); the kit
  GUARDRAILS (BOLT-005); the pilot (BOLT-004); the examples'
  `capabilities` fields (v2 hardening).

## 5. Prerequisites and baseline

- Baseline `ebf48d0` (BOLT-001's V-Bounce committed; tree clean).
- The BOLT-001 section hash reference: `cd24754c320d…` under the pinned
  convention (§8).

## 6. Phases

### Phase A — The four preambles (exact old → new)

**Duration:** ~1h — **Complexity:** Low

Each preamble keeps its platform's spawn-control statement and gains the
same content checklist (platform-specific values): the spawn **folder**,
the wrapper **format**, the projection wiring ("project live definitions
from `devflow/agents/squad/` … following the mapping in
`devflow/agents/VERIFICATION.md`"), the **reload notice**, and zero
maintenance references. The four old paragraphs (verbatim on disk today)
are replaced as follows:

**Claude (kit `CLAUDE.md`)** — old: the current paragraph citing
`(ADR-007 §3.4)`, the stale
`Agent(architect-agent, developer-agent, fa-agent, qa-agent, reviewer-agent)`
list and `(US-023 AC-6)`. New:

> **Spawn topology (you are the Coordinator):** this agent is the Avenga
> DevFlow platform agent itself — the Coordinator. Your spawn folder is
> **`.claude/agents/`** and the wrapper format is a Markdown agent file
> (`<agent-id>.md`): you project live definitions from
> `devflow/agents/squad/` into it following the mapping in
> `devflow/agents/VERIFICATION.md` (a session reload registers new
> agents). You carry the `Agent` tool; the role-agent wrappers omit it, so
> executors cannot spawn approvers — approver agents are spawnable only
> through you (or by a human) (the spawn topology).

**OpenCode (`AvengaDevFlow.md`)** — old: the current paragraph citing
`(ADR-007 §3.4)` and `(US-023 AC-6)`. New:

> **Spawn topology (you are the Coordinator):** this agent is the Avenga
> DevFlow platform agent itself — the Coordinator. Your spawn folder is
> **`.opencode/agents/`** and the wrapper format is a Markdown agent file
> with a frontmatter `permission` block (`mode: subagent`): you project
> live definitions from `devflow/agents/squad/` into it following the
> mapping in `devflow/agents/VERIFICATION.md` (a session reload registers
> new agents; subagents appear via ctrl+X / `opencode agent list`, not
> the Tab picker). You keep `permission.task` (spawn); the role wrappers
> carry `task: deny` — executors cannot spawn approvers (the spawn
> topology).

**Copilot (`AvengaDevFlow.agent.md`)** — old: the current paragraph citing
`(ADR-007 §3.4)` and `(US-023 AC-6)`. New:

> **Spawn topology (you are the Coordinator):** this agent is the Avenga
> DevFlow platform agent itself — the Coordinator. Your spawn folder is
> **`.github/agents/`** and the wrapper format is a `.agent.md` file: you
> project live definitions from `devflow/agents/squad/` into it following
> the mapping in `devflow/agents/VERIFICATION.md` (a session reload
> registers new agents). Only your tools include the `agent` alias
> (agent→agent invocation); the role wrappers omit it — executors cannot
> invoke approvers (the spawn topology).

**Codex (`SKILL.md`)** — old: the current paragraph citing
`(ADR-007 §3.4)`, the stale "The role agents live in
`.codex/agents/*.toml`", `DISC-002 §4.2` and `(US-023 AC-6)`. New:

> **Spawn topology (you are the Coordinator):** this agent is the Avenga
> DevFlow platform agent itself — the Coordinator. Your spawn folder is
> **`.codex/agents/`** and the wrapper format is a TOML agent file
> (`<agent-id>.toml`): you project live definitions from
> `devflow/agents/squad/` into it following the mapping in
> `devflow/agents/VERIFICATION.md` (a session reload registers new
> agents). Codex has no native per-agent spawn allowlist, so the control
> is instruction-based: you spawn role agents and never delegate the
> spawning of approvers to an executor (the known gaps are recorded in
> `devflow/agents/VERIFICATION.md`) (the spawn topology).

Uniqueness of each old paragraph is asserted per file before editing
(stop condition).

### Phase B — VERIFICATION.md made deterministic

**Duration:** ~1.5h — **Complexity:** Low

**B.1 — The permission-block derivation (F-14).** New subsection after
the mapping table: a wrapper's permission set derives **only** from the
definition's `capabilities.tools` allowlist — each listed tool maps to
its platform permission (per the table); **every tool absent from the
allowlist is explicitly denied** (nothing — `list`, `webfetch`,
`websearch`, `task` included — enters a wrapper without canonical
backing); reviewer/approver-class agents additionally deny
`bash`/`edit`/`write`/`task` and web tools (the approver ceiling at the
wrapper level); two projections of one definition must be
byte-comparable.

**B.2 — `model: inherit` (F-09).** A note on the `model` mapping row:
`inherit` is **not a catalog value** — at projection time the wrapper
**omits the model field entirely**, so each platform natively uses its
session/default model (deterministic and portable across the four).
Guidance line: reviewer/approver-class agents should **pin a distinct
model** from the session's (model diversity — "a model reviewing its own
work is too complacent").

**B.3 — The OpenCode notes (F-13).** In the OpenCode section: the Tab
picker lists **primary agents only** — subagents are visible via ctrl+X /
`opencode agent list` and are invoked through the Coordinator's task tool
(the spawn topology working as designed); a session reload registers new
agents (the headless finding stays as recorded).

**B.4 — Consistency touches.** "How the agents are installed": the
projection source is the **live definitions in `agents/squad/`** (the
canonical contract lives in the family README; the examples are read-only
references). The Claude section's "`Agent(...)` allowlist (the role ids)"
→ "only the Coordinator carries the `Agent` tool" (the id-list era ended
with the ship model).

### Phase C — Verification

**Duration:** ~40min — **Complexity:** Low

(1) **Shared body unchanged** — re-extract the lifecycle section with the
**pinned convention** (§8) from the four files: all four hashes equal
`cd24754c320d…` (the BOLT-001 evidence value). (2) The preamble checklist
×4 — each names its folder, format, `squad/`, `VERIFICATION.md`, the
reload notice. (3) The **scoped** zero-references sweep: the four
MainAgents contain **no maintenance-partition references**; the kit's own
`US-000` and the naming-table's fictional examples
(`US-012.BOLT-003-…`, `TC-027.BOLT-001-…`) stay (framework text).
(4) Stale-text sweep: no `architect-agent` wrapper list, no "role agents
live in `.codex/agents/*.toml`" sentence. (5) VERIFICATION.md carries
B.1–B.4; its cross-references resolve. (6) No BOM.

## 7. Acceptance criteria

### AC-1: The preambles current, per the checklist
**Given** the four files, **When** each preamble is read, **Then** it
names its platform's spawn folder + wrapper format + the `squad/` →
mapping wiring + the reload notice, with zero maintenance references and
no pre-built-era text — and the platform's spawn-control statement is
preserved (Agent tool / permission.task / agent alias /
instruction-based).

### AC-2: The mapping is deterministic
**Given** VERIFICATION.md, **When** a MainAgent projects one definition
twice, **Then** the permission derivation (allowlist-only + explicit
deny-set + the approver-class denies) and the `inherit` omission rule
leave no degree of freedom — the field-proven drift (`list: allow`) would
now violate the written rule.

### AC-3: The shared body untouched
**Given** the pinned extraction (§8), **When** the section hash is
recomputed on the four files, **Then** all four equal `cd24754c320d…`.

### AC mapping to source

| Source AC | How this SPEC satisfies it | Verifying evidence |
|-----------|----------------------------|--------------------|
| US-025 AC-2 | The preamble names the spawn folder + the wiring | AC-1 checklist |
| US-025 AC-7 | Only the preambles differ; the shared body hash-locked | AC-3 |
| US-025 AC-8 | The mapping now projects deterministically (docs-primary, generator still optional, parity still the net) | AC-2 |
| US-025 AC-9 (completion) | The preamble references cleaned — the four files end at zero | The scoped sweep |

## 8. Testing strategy

Scripted evidence (the BOLT-001 pattern): **the pinned hash convention**
— `text[text.index("## The agent lifecycle") : text.index("## Guardrails
(MUST enforce)")]`, md5 over UTF-8 (the exact extraction of BOLT-001's
script; reference value `cd24754c320d…`) — plus the preamble checklist
greps, the scoped sweep, the stale-text sweep, the VERIFICATION content
checks, BOM. No unit/integration/E2E (no runtime surface; BOLT-004
pilots the behavior).

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | n/a — documentation Bolt | n/a |
| SAST / SBOM | n/a — no code | n/a |
| Perf-smoke | n/a — no runtime | n/a |
| Prompt-injection scan | the preamble text instructs the agent only | pass expected |
| Secret-leak scan | no secrets | pass expected |
| Hallucination lint | every referenced path resolves | pass expected |
| IP / license provenance | kit-original text | pass expected |
| PII / DLP | internal docs | pass expected |
| Dependency-confusion | n/a | n/a |
| Test-first evidence | the §8 checks defined before execution | pass expected |
| Behavioral reproducibility | hash/sweep checks re-run identically | pass expected |
| Bolt-manifest validation | v_bounces[1] appended, schema PASS | pass expected |

## 10. Security and data

The preambles are system-prompt text: reviewed verbatim here (Phase A).
The permission-derivation rule (B.1) **is** a security control — it closes
the drift channel a projection had, and encodes the approver ceiling at
the wrapper level (the REV-005 F-09/F-11 line of defense).

## 11. Monitoring and observability

n/a — documentation family.

## 12. Migration, compatibility and rollback

- **Migration:** framework-file supersede on upgrade (§5.16).
- **Compatibility:** existing installed wrappers keep working; the next
  refresh follows the deterministic rule.
- **Rollback:** `git revert` of the V-Bounce commit.

## 13. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| Touching the shared body | 1 | 4 | The pinned-hash unchanged gate (AC-3) |
| Preambles diverging in meaning | 2 | 3 | The common checklist with platform values (AC-1) |
| The deny-set rule breaking an existing wrapper expectation | 1 | 2 | Rule applies at projection; existing wrappers unaffected until refreshed |

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| `inherit` → omit the field (not "write the session model's id") | Writing a resolved id freezes the session's model into the wrapper — wrong on the next session; omission delegates to each platform's native inheritance: deterministic, portable, self-updating |
| The deny-set is explicit, not implicit | The field-proven drift (`list: allow`) happened precisely in the unstated space; explicit denies make two projections byte-comparable |
| The hash convention pinned in §8 | Reviewer finding: a differing extraction boundary yields a different valid hash — the gate must compare like with like (BOLT-001's exact extraction) |
| The preambles keep their spawn-control statements verbatim in spirit | They are the platform-verified security mechanics (VERIFICATION's per-platform sections) — this Bolt updates the lifecycle context around them, not the control |
| B.1's approver-class deny clause = a **deliberate partial implementation** of the REV-005 F-11 v2 spec (its wrapper-mapping half) | The clause is small, sits naturally in the derivation rule, and closes the field-proven `bash`-retention gap at the projection level NOW; the schema half (the `allOf` ceiling enforcement) stays in the ADR-014 v2 backlog — recorded here and in the MEM §13 so the future hardening US implements only the remaining half |
| F-09 closes with the omission interpretation | "Resolve at projection time" is implemented as field-omission (the platform's native inheritance) — the effective model is the session's without freezing an id; F-09 is thereby resolved, not pending (the MEM records the closure) |

## 15. Stop conditions

- Any old preamble paragraph not found exactly once in its file → stop.
- Any need to touch the shared body, a role file, or the guardrails →
  stop (wrong Bolt).

## 16. Definition of Done (DoD)

- [ ] Phases A–C implemented
- [ ] AC-1..AC-3 pass (evidence recorded)
- [ ] Applicable gates pass / n/a per §9
- [ ] MEM created in `devflow/memory/` (exactly one)
- [ ] Manifest `v_bounces[]` entry appended
- [ ] AITL-MEM-Approval recorded

## 17. References

- US-025 · US-025.BOLT-002 (READY) · ADR-013 §3.9 · REV-005 F-09/F-13/F-14
  · MEM-260824-1115 §13 (the remainder) · SPEC-260824-1101 (the shared
  body + the hash reference) · US-016 (byte-sync discipline).

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
| **review_ready_at** | `2026-08-24T11:46:17-03:00` |
| **review.started_at** | `2026-08-24T13:01:28-03:00` |
| **review.decided_at** | `2026-08-24T13:01:28-03:00` |
| **Findings** | none blocking — the cross-model review reproduced the hash-gate reference; B.1 kept per the reviewer's recommendation (reason in the frontmatter `review:` block) |
