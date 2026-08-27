---
id: "ADR-005"
title: "Removal completeness is proven by a phrase-family sweep over a fixed location set, never by grepping the edited location"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-5"
status: "accepted"
decision_makers: ["architect", "tech_lead"]
sources:
  - "devflow/adversarial-reviews/AREV-003-v42-close-removal-traces-sweep/03-VERDICT.md"
  - "devflow/adversarial-reviews/AREV-001-role-availability-blockers-sweep/03-VERDICT.md"
  - "devflow/bugs/BUG-001-stale-bug-route-copies.md"
  - "devflow/bugs/BUG-002-risk-based-approver-count-residuals.md"
supersedes: []
conflicts_with: []
tags: ["verification", "removal-sweep", "maintainer-internal", "partial-sweep-pattern"]
nfrs: ["removal-completeness"]
waiver:
  gate: ""
  reason: ""
  owner: ""
  compensating_control: ""
  expires_at: ""
review_ready_at: "2026-08-22T03:10:36-03:00"
review: # HITL-ADR-Approval evidence — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers: [{user: "eugenio.serrano", role: "architect"}]
  started_at: "2026-08-22T03:13:53-03:00"
  decided_at: "2026-08-22T03:13:53-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Accepted. The decision is correctly scoped to the maintainer's partition (root devflow/, governing this repository's Bolts in both trees) and adds no rule to the distributable kit — consistent with ADR-002's precedent and ADR-004's partition. The evidence base is three approved findings (AREV-001/AREV-003 Verdicts, BUG-001, BUG-002) establishing the partial-sweep pattern as systemic. The mechanism is sound: the completion criterion becomes an absence assertion over a named location set instead of a property of the edited location, with a phrase-family (multiline) grep and an explicit legitimate-homonym allowlist to prevent over-removal. Alternative C (propagating the standard into the kit for adopters) is correctly deferred until the standard is exercised here. Immutable from now on; first application is BUG-002's dedicated Bolt."
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs and section headings
  stay in English (the schema); prose follows content_language (en).
  `HITL-ADR-Approval` is never translated.

  ⚠️ This ADR is a DRAFT until an Architect / Tech Lead records
  HITL-ADR-Approval. A draft ADR cannot govern a SPEC.

  ⚠️ SCOPE: maintainer-internal, like ADR-002 — it governs how Bolts in THIS
  repository verify a removal. It does NOT add a rule to the distributable
  kit; propagating this standard to adopters is a separate decision and a
  separate Bolt (see §4, out of scope).
-->

# ADR-005 — Removal completeness: phrase-family sweep over a fixed location set

| Field          | Value |
|----------------|-------|
| **Status**     | **accepted** (immutable — a new decision requires a superseding ADR) |
| **Decision-makers** | Architect / Tech Lead (maintainer) |
| **Sources**    | AREV-003 (Verdict FAIL, F-01), AREV-001 (Verdict FAIL, F-06), BUG-001, BUG-002 |
| **Supersedes** | None |
| **Conflicts with** | None — ADR-002 (defect classification) and ADR-004 (repository partition) are complementary |

---

## 1. Context

The methodology is documentation, and every rule it states is **repeated across
many surfaces by design**: the normative section, the GUARDRAILS row, the
GUARDRAILS checkpoint map, the four agent definitions, the folder READMEs,
ONBOARDING and the templates. That redundancy is what makes the kit usable —
and it is exactly what makes a *removal* dangerous: deleting a rule means
deleting every copy of it, in files a diff never shows you, because the defect
is the **absence of an edit**, not a bad edit.

Three occurrences establish the pattern:

| # | Removal | Sweep verified | Residuals left | Found by |
|---|---------|----------------|----------------|----------|
| 1 | G29 BUG-route relaxation (SPEC-260821-0108) | the rows it edited | stale `Developer≠author` copies | AREV-001 → **BUG-001** |
| 2 | Role-as-gate blockers (US-014.BOLT-001) | the checkpoint tables | two auxiliary TC prose texts | AREV-003 F-02 |
| 3 | Risk-based approver counts (US-014.BOLT-003) | the two numeric min-approver tables | 8+ carriers, incl. the four auto-loaded agents | AREV-003 → **BUG-002** |

Every one of those Bolts **passed its own acceptance grep**. The criterion was
phrased as a property of the location being changed ("the tables are
consistent", "no risk-based count survives" — checked where it had just
edited), so the grep could only confirm the edit it had already made. Nothing
in the criterion forced it to look where it had *not* edited.

Two aggravating factors are now documented:

- **The four agent definitions are the worst carrier.** They are auto-loaded on
  every session, so a stale rule there does not merely misinform a reader — it
  actively re-injects the removed behaviour into agent execution. Two of the
  three occurrences left their strongest contradiction precisely there.
- **A literal string is not enough.** The same rule appears as `QA/Sec per
  risk`, `QA *or* Sec`, `QA + Sec`, `(+ QA/Sec for high/critical)`, and
  line-wrapped across two lines. A single-form, single-line grep misses most
  of them.

Human review cannot be the control here: a reviewer reads a diff, and the
residual is in a file the diff does not contain.

---

## 2. Alternatives considered

### Alternative A — Phrase-family sweep over a fixed location set, declared as a SPEC acceptance criterion (✅ Selected)

| Aspect   | Detail |
|----------|--------|
| **Pros** | Turns removal completeness into a **verifiable absence assertion** instead of an inspection; the location set is fixed and reusable, so the next removal Bolt inherits it instead of re-inventing coverage; the explicit allowlist makes over-removal visible; cheap (a grep, not tooling); scoped to the repository, so it takes effect immediately without touching the kit |
| **Cons** | Adds ~10–20 min of verification to every removal Bolt; the location set must be maintained when the kit's file inventory changes; still a manual/agent-run procedure with no CI enforcement |

### Alternative B — Rely on review diligence and a larger review budget

| Aspect   | Detail |
|----------|--------|
| **Pros** | No process change; zero added ceremony |
| **Cons** | **Empirically refuted three times.** The failure mode is an absent edit in an unvisited file; a reviewer inspecting the diff structurally cannot see it. Raising the budget does not change what the diff contains |

### Alternative C — Ship a blocking rule into the kit now (a new G-rule / SPEC-quality requirement for adopters)

| Aspect   | Detail |
|----------|--------|
| **Pros** | Adopters get the same protection; the lesson lands in the product, not only in the maintainer's habits |
| **Cons** | It is a **kit change**, so it needs its own Bolt and SPEC (G07) and re-opens the v4.2 scope again; and it would bind every adopter to a procedure this repository has not yet executed even once. Sequencing it after the first successful application is strictly safer — the standard should be proven here before it is prescribed to others |

> **Also evaluated:** a CI linter that runs the sweep automatically. Correct
> long-term direction, but no tooling track exists yet; recorded as technical
> debt in §4 rather than decided here.

---

## 3. Decision

**We adopt Alternative A.** In this repository, a Bolt whose outcome includes
**removing, renaming or changing a governed rule, checkpoint, route or
vocabulary term** proves completeness by a phrase-family sweep over a fixed
location set, declared in its SPEC as an acceptance criterion. Concretely:

**(1) Enumerate the phrase family before sweeping.** Not the literal string
that was edited — every form the rule takes in prose: notation variants
(`QA/Sec`, `QA *or* Sec`, `QA + Sec`), abbreviated and expanded wording, the
negated form, and semantic paraphrases. Grep with alternation,
case-insensitively, and **multiline** (`rg -U` / `multiline: true`), because
line-wrapped prose defeated an earlier sweep.

**(2) Sweep the fixed location set** — every entry, every time, regardless of
where the edit was made:

| # | Location | Both of |
|---|----------|---------|
| 1 | The four agent definitions (`CLAUDE.md`, `.agents/skills/avenga-devflow/SKILL.md`, `.github/agents/AvengaDevFlow.agent.md`, `.opencode/agents/AvengaDevFlow.md`) | their rule/checkpoint **tables** *and* their step/narrative **prose** |
| 2 | `devflow/avenga-devflow/Avenga-DevFlow.md` | **tables** *and* **narrative** |
| 3 | `devflow/GUARDRAILS.md` | the **G/W/N/T rule rows**, the **checkpoint map rows** *and* the **prose sections** |
| 4 | Every `README.md` (`devflow/` root and every subfolder) | folder maps, tables, diagrams |
| 5 | `devflow/ONBOARDING.md` | role map, glossary *and* FAQ |
| 6 | Every `TEMPLATE-*.md` | frontmatter comments *and* body sections |
| 7 | Every `INDEX.md` | section structure and rows |
| 8 | `devflow/metrics/` schemas and manifest templates | only when the removed term is a schema value |

**(3) Declare a legitimate-homonym allowlist.** A sweep will hit occurrences
that are *not* residuals — the same words used by a different, still-valid
concept. Each such hit is enumerated in the SPEC with a one-line reason so the
fix neither over-removes nor silently leaves an unexamined match. (Precedent:
AREV-003 F-06.2 — the escalation and role-description mentions of QA/Sec that
must survive BUG-002's fix.)

**(4) State it as an acceptance criterion, phrased as an absence.** The AC
records the sweep command and its expected result: *zero matches outside the
declared allowlist, across the full location set.* A criterion phrased as a
property of the edited location ("the tables are consistent") does not satisfy
this ADR.

**(5) Re-check the invariants after the sweep:** four-agent byte-sync and the
G-rule count.

**Scope:** maintainer-internal, like ADR-002 — it governs Bolts in this
repository, in both trees (kit and root). It adds **no** rule to the
distributable kit.

---

## 4. Consequences

**Positive:**
- Removal completeness becomes **falsifiable**: the SPEC asserts an absence over
  a named set of files, and the MEM records the command and its zero-match
  output as green evidence.
- The location set is written down once and inherited by every future removal
  Bolt — the coverage question stops being re-derived (and re-under-scoped) per
  Bolt.
- The allowlist converts the over-removal risk into a reviewable list, which is
  what stopped BUG-002's fix from stripping the legitimate QA/Sec escalation
  text.
- The agents' prose is promoted to a first-class sweep target, closing the
  carrier that caused the two worst occurrences.
- **First application: BUG-002's dedicated Bolt** — approving this ADR before
  that SPEC is written means the fix for the third occurrence is itself verified
  by the new standard, rather than risking a fourth.

**Trade-offs:**
- ~10–20 min of extra verification per removal Bolt. Accepted: three defects,
  two of them release-blocking, cost far more than that.
- The sweep is deliberately broad, so it will produce hits that need triage
  (the allowlist). That triage is the point, not overhead to be optimized away.
- The location set is coupled to the kit's file inventory: adding a documentation
  surface means adding a row here, which only a superseding ADR can do.

**Technical debt:**
- No automation. The sweep is run manually or by the agent, so it depends on the
  SPEC actually declaring the AC. A CI/gate linter that executes the sweep from
  a declared phrase family is the natural next step — candidate non-functional
  Bolt under US-000, not decided here.
- **Out of scope, deliberately deferred:** propagating this standard into the
  distributable kit for adopters (Alternative C). Recommended path: apply it
  here first (BUG-002), then a dedicated Bolt ships it as a W-rule or a SPEC
  Quality requirement in a later version. Tracking that decision is a separate
  artifact.

---

## 5. Applicable NFRs

| NFR | Description | Threshold | How it is measured |
|-----|-------------|-----------|-------------------|
| `removal-completeness` | A removal Bolt leaves no residual copy of the removed rule anywhere in the documentation surface | **Zero** matches of the declared phrase family across the §3 location set, outside the declared allowlist | The SPEC's sweep AC; the grep command and its output recorded as green evidence in the Bolt's MEM |
| `four-agent-sync` | The four agent definitions stay byte-identical in their shared body after a removal | Whole-body diff = sanctioned divergence only; G-rule count equal across all four and GUARDRAILS | Diff + `grep -cE '^\| G[0-9][0-9] '` recorded in the MEM |

---

## 6. References

- [AREV-003 Verdict](../adversarial-reviews/AREV-003-v42-close-removal-traces-sweep/03-VERDICT.md) — FAIL; F-01 confirmed 🔴, systemic pattern recorded as action-plan item #3
- [AREV-001 Verdict](../adversarial-reviews/AREV-001-role-availability-blockers-sweep/03-VERDICT.md) — first occurrence
- [BUG-001](../bugs/BUG-001-stale-bug-route-copies.md) (closed) · [BUG-002](../bugs/BUG-002-risk-based-approver-count-residuals.md) (approved) — the two defects this ADR prevents
- Related ADRs: **ADR-002** (how a documentation defect is classified — complementary: ADR-002 says *what kind of defect this is*, ADR-005 says *how a removal proves it did not create one*); **ADR-004** (repository partition — defines the two trees this sweep covers)

---

## 7. HITL-ADR-Approval

> **HITL-ADR-Approval** (Avenga DevFlow §2.8, §3.0, §3.5). An ADR does not
> become `accepted` — and therefore governing — without the approval of an
> Architect / Tech Lead. This ADR is the source of truth for its own approval
> (recorded in the `review` frontmatter block). ADR approvals are never copied
> to the Bolt manifest.

| Field | Value |
|-------|-------|
| **Architect / Tech Lead** | eugenio.serrano |
| **Role** | architect / tech_lead |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-22T03:10:36-03:00` |
| **review.started_at** | `2026-08-22T03:13:53-03:00` |
| **review.decided_at** | `2026-08-22T03:13:53-03:00` |
| **Findings** | none — `acknowledged_without_comment: true` (see frontmatter `acknowledgment_reason`) |
