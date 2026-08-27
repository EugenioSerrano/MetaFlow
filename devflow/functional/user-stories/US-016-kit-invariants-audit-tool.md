---
id: "US-016"
title: "Kit-invariants audit tool — automate four-agent sync, G-count, version-marker and encoding-hygiene (BOM/mojibake) checks"
date: "2026-08-21"
author: "eugenio.serrano"
llm: "claude-opus-4-8" # refined 2026-08-23 (encoding-hygiene scope + HITL→AITL); created 2026-08-21 (see manifest runs[])
status: "approved" # draft | approved | deprecated
owner: "eugenio.serrano" # Functional Analyst (governs this US)
unit: ""
story_points: 5 # proposed (was 3; +encoding invariant + mutating --fix mode); confirmed at AITL-US-Approval (§2.6)
adrs: []
sources:
  - "devflow/memory/MEM-260817-2123-agents-md-project-section.md"
  - "devflow/memory/MEM-260823-0126-version-marker-sweep.md" # evidence: the BOM+mojibake incident during the version sweep
  - "AGENTS.md"
stakeholders: []
tags: ["tool", "invariants", "agents", "version-markers", "encoding", "bom", "mojibake", "release"]
review_ready_at: "2026-08-23T11:09:09-03:00"
review: # AITL-US-Approval — recorded by the human reviewer (§3.0); decision dictated in conversation ("Aprobado!") and transcribed by the agent
  decision: "approved"
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "functional_analyst"
      model: null
  started_at: "2026-08-23T11:13:43-03:00"
  decided_at: "2026-08-23T11:13:43-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved as Functional Analyst; story points confirmed at 5. The encoding-hygiene (BOM/mojibake) invariant and the bounded --fix mode accepted, with input/ detect-only (G31) and never-auto-repair-mojibake as scope guards. Ready to decompose into candidate functional Bolts."
---

# US-016 — Kit-invariants audit tool: automate four-agent sync, G-count, version-marker and encoding-hygiene checks

| Field          | Value |
|----------------|-------|
| **Unit**       | — |
| **ADRs**       | — |
| **Status**     | approved |
| **Story points** | 5 (confirmed at AITL-US-Approval) |

**As a** maintainer of the DevFlow kit, **I want** a single tool that
verifies the distributable's load-bearing invariants automatically, **so
that** a drift in the four agent definitions, the guardrail count, the
version markers or the file encoding is caught by one command instead of a
remembered bash sequence.

---

## 1. The problem (explained, complete)

### The invariants and how they are checked today (all manual)

The AGENTS.md "Maintaining the four agents" procedure and the "Version bump
procedure" define deterministic checks that keep the distributable
consistent. Today they are **manual bash commands** that a maintainer must
remember to run:

1. **Four-agent shared-body byte-identity.** The methodology sections of
   `CLAUDE.md`, `.agents/skills/avenga-devflow/SKILL.md`,
   `.github/agents/AvengaDevFlow.agent.md` and
   `.opencode/agents/AvengaDevFlow.md` must be byte-identical from the
   `# Avenga DevFlow v<version> (Methodology)` heading to EOF, except one
   line: the `devflow/agents-data/<agent>/` path (the only sanctioned
   divergence). The check is a tail-from-heading + `tr -d '\r'` + diff.
   A grep only proves the touched lines are in sync — it cannot see drift
   elsewhere in the shared body.
2. **G-rule count invariant.** Every blocking rule is inline in every
   agent: `grep -cE '^\| G[0-9]{2} \|'` must return the same count in
   `GUARDRAILS.md` and in all four agents (39 today). Adding or removing a
   guardrail without updating all five files silently breaks the model.
3. **Version-marker sweep.** The methodology version is stamped in
   `distribution-kit/devflow/VERSION`, in the `**Methodology version:**`
   header of every README/INDEX under the kit's `devflow/`, in the kit's
   `GUARDRAILS.md` (header + footer), `ONBOARDING.md`, the methodology
   frontmatter, the four agents (heading + `**Agent version:**`), the root
   `README.md` and `distribution-kit/AGENTS.md`. The bump procedure warns
   that a bare version number must never be swept (section numbers share the
   shape).
4. **Status-language lint.** Document `status:` values are schema
   English; a translated value (e.g. `status: abierta`) breaks validators
   and INDEX counters (§3.15 language policy).
5. **Encoding hygiene (BOM + mojibake).** Every text file in the kit must be
   **UTF-8 without BOM**. A UTF-8 BOM (leading bytes `EF BB BF`) is invisible
   and breaks shebangs, strict JSON parsers, YAML frontmatter detection and
   anchored greps. **Mojibake** — content double-encoded through the wrong
   codepage (e.g. `—` → `â€"`, `é` → `Ã©`, box-drawing/emoji mangled) —
   corrupts the actual text. Both are produced by careless read/write steps,
   classically a Windows PowerShell `Set-Content`/`Out-File` that writes
   UTF-8-with-BOM after reading as ANSI.

### Evidence that this is a real gap

- The MEM of `US-000.BOLT-001` (V-Bounce 1) recorded the pending item:
  *"A `tools/` checker for the framework-block byte-identity invariant, out
  of this Bolt's scope."* It was never opened.
- In the session of 2026-08-21 the maintainer ran the sync-diff, the
  G-count and marker checks **by hand three times** across two V-Bounces —
  each time reconstructing the PowerShell equivalent of the AGENTS.md bash
  commands. A drift would be caught only if someone remembers to do this.
- **`MEM-260823-0126` (US-000.BOLT-013 version-marker sweep):** a
  PowerShell `Set-Content` wrote UTF-8-**with-BOM** and read the originals as
  ANSI, mangling em-dashes, box-drawing and emoji into mojibake across the
  kit. It was reversed by hand and caught **only by a post-hoc grep** — there
  was no automated gate. This is exactly the encoding invariant this tool
  should enforce. (It also echoes REV-002 F-07, a mojibake defect in a
  shipped example manifest.)

### Why it matters

The four-agent sync and the G-count are the enforcement backbone: agents
carry every blocking rule inline so that context compaction cannot lose a
G-rule. When the shared body drifts, adopters receive agents that contradict
each other — and the release pipeline has no gate that detects it. Encoding
defects are just as silent and ship straight into the distributable. This
tool turns the manual procedures into a single, CI-able exit-code check —
the safety net the maintainer (and, later, executing agents) needs before
every release.

---

## 2. Acceptance criteria

- **Given** the kit, **When** the audit tool runs, **Then** it verifies the
  four-agent shared-body byte-identity (from the methodology heading to
  EOF, CRLF-normalized) and reports the exact differing lines.
- **Given** the guardrails, **When** the audit tool runs, **Then** it
  compares the G-rule row count of `GUARDRAILS.md` with each of the four
  agents and fails on any mismatch.
- **Given** a version bump, **When** the audit tool runs, **Then** it checks
  the version-marker set (VERSION file, README/INDEX headers, GUARDRAILS
  header/footer, ONBOARDING, methodology frontmatter, the four agents,
  root README, kit AGENTS.md) and reports any file out of sync — sweeping
  only version markers, never bare numbers that could be section
  references.
- **Given** the language policy, **When** the audit tool runs, **Then** it
  lints document `status:` values against the schema-English vocabulary and
  reports violations.
- **Given** encoding hygiene, **When** the audit tool runs, **Then** it
  reports every text file that carries a UTF-8 BOM (leading `EF BB BF`) and
  every file that matches a mojibake signature, each with its path (and, for
  BOM, the offending byte offset).
- **Given** the `--fix` mode, **When** it runs, **Then** it strips BOMs only
  (rewriting UTF-8-without-BOM, idempotent), **never** alters mojibake
  (lossy — it is only ever reported for human repair) and **never** touches
  binary files.
- **Given** `input/` (human-deposited evidence, agents read-only, G31),
  **When** either mode runs, **Then** `input/` is **detect-only** — the tool
  reports issues there but never writes to it, even under `--fix`.
- **Given** any drift, **When** the audit tool runs, **Then** it exits
  non-zero with a precise report (file, line, expected vs actual) — usable
  as a release gate.
- **Given** the tools convention, **When** the tool is built, **Then** it
  lives in `tools/` (source + DESIGN.md) and is **not** distributed to
  adopting projects (same class as the other tools).

## 3. Notes / to refine before approval

- **Origin:** approved MEM `MEM-260817-2123` pending item (the checker for
  the framework-block byte-identity invariant) + AGENTS.md procedures; the
  encoding invariant is evidenced by `MEM-260823-0126` (the BOLT-013
  BOM/mojibake incident).
- **Story-point note:** proposed **5** (was 3). The bump is driven by the
  new **encoding-hygiene** invariant plus the first **mutating `--fix`
  mode** — a capability class beyond the read-only auditor, with its own
  safety rules (no-BOM writer, `input/` exclusion under G31, never repair
  mojibake, skip binaries). Still one bounded tool (§2.6: score the highest
  dimension; not an 8). Plausibility: 5 SP → ~2–4 Bolts (e.g. the read-only
  audit checks as one Bolt, the `--fix` mode as another).
- **Consolidation:** the "strip all BOMs" idea (floated 2026-08-23) is folded
  in here rather than made a standalone tool, to avoid tool sprawl — BOM and
  mojibake are two more kit invariants of the same family. Detection is the
  default; the only safe mutation (`--fix` = BOM strip) is opt-in.
- **Related backlog:** US-012 (validator) checks **manifests** against their
  schemas; this audit checks **kit invariants** (agents/guardrails/version
  markers/encoding). Complementary, no overlap. US-006 (indexer) handles
  INDEX rebuilds — out of this tool's scope unless explicitly added later.
- **Open design points (for the SPEC):**
  - Language: Go (matches the other tools) vs a script — design decision
    for the SPEC / governed by US-017 (tooling distribution contract).
  - Whether the audit runs against `distribution-kit/` only (this repo's
    release concern) or also validates an adopting project's installed
    `devflow/` (same checks, different roots) — the tool should at least
    accept a root argument.
  - Whether the G-count check reads the count from GUARDRAILS or from a
    pinned constant (proposal: derive from GUARDRAILS — single source).
  - The mojibake-signature set (which byte sequences count) — the SPEC pins
    it; detection must not false-positive on legitimate non-ASCII content.
  - Version-marker list must stay in sync with the AGENTS.md version-bump
    procedure (the list is the rule; the tool implements it).
  - CI integration (release gate) is out of this US's kit scope but the
    exit-code contract makes it possible.
- **Scope note:** this US is about the *verification tool*; the version-bump
  procedure itself (the steps a maintainer follows) is not being rewritten
  — the tool just automates the checks it defines.
