---
id: "ADR-003"
title: "The prompts family is the canonical home — root prompts/ retires from the Product zone"
date: "2026-08-21"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "superseded" # draft | accepted | rejected | deprecated | superseded
decision_makers: ["architect", "tech_lead"]
sources:
  - "devflow/functional/user-stories/US-003-prompts-family.md"
  - "devflow/adrs/ADR-001-repository-layout-methodology-and-product.md"
  - "maintainer direction (2026-08-21)"
supersedes: ["devflow/adrs/_archive/ADR-001-repository-layout-methodology-and-product.md"]
conflicts_with: []
tags: ["repository-layout", "prompts", "zones", "governance"]
nfrs: []
waiver: # Only for gate-override ADRs (§3.6)
  gate: ""
  reason: ""
  owner: ""
  compensating_control: ""
  expires_at: ""
review_ready_at: "2026-08-21T03:15:06-03:00"
review: # HITL-ADR-Approval evidence — filled by the human reviewer (§3.0)
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - user: "eugenio.serrano"
      role: "architect"
  started_at: "2026-08-21T03:17:55-03:00"
  decided_at: "2026-08-21T03:17:55-03:00"
  findings: []
  acknowledged_without_comment: true # must be true when findings is empty (§3.0)
  acknowledgment_reason: "Reviewed the zone-table amendment against the post-migration state: the 4.2 family (US-003) is installed and dogfooded (PROMPT-001), the root prompts/ holds no distributable content, and the retired-zone row with the Bolt requirement for the leftover file preserves governance. Rules 1-6 of ADR-001 carry forward by reference (ADR-001 archived under adrs/_archive/). Approved as drafted."
---

# ADR-003 — The prompts family is the canonical home: root prompts/ retires from the Product zone

| Field          | Value |
|----------------|-------|
| **Status**     | draft |
| **Decision-makers** | eugenio.serrano (architect / tech_lead) |
| **Sources**    | US-003 (approved — the `devflow/prompts/` family), ADR-001 (superseded by this ADR), maintainer direction (2026-08-21) |
| **Supersedes** | ADR-001 (partially — rule 7's zone table row for `prompts/`; all other rules carry forward unchanged) |
| **Conflicts with** | None — this ADR resolves the only contradiction it introduces |

---

## 1. Context

ADR-001 rule 7 classified three paths as the **Product zone**:
`distribution-kit/`, `tools/` and the root `prompts/`. The root `prompts/`
held the maintainer's prompt content (a single file, `analysis.txt`) and was
declared "not distributed".

In the meantime the methodology itself evolved: **US-003 (approved,
2026-08-21) shipped the canonical `devflow/prompts/` family** in the
distributable — the folder where prompts are created, modified and improved
as living data (PROMPT-NNN numbering, no approval, no manifest, versioned by
git). This repository migrated its installed tree to 4.2 (§5.16, first real
execution) and now dogfoods the family: `PROMPT-001-methodology-analysis.md`
is registered in the installed `devflow/prompts/`.

The root `prompts/` has therefore **lost its product role**: the canonical
home for prompts — the maintainer's included — is the family. Keeping the
root folder in the Product zone would force every future prompt housekeeping
act (create, edit, delete) through the full Bolt lifecycle for a zone that
no longer produces distributable content.

## 2. Alternatives considered

### Alternative A — Keep the root prompts/ in the Product zone (❌ Rejected)

| Aspect   | Detail |
|----------|--------|
| **Pros** | No ADR needed; status quo. |
| **Cons** | The zone no longer holds anything the distributable needs; every housekeeping act on a single leftover file demands the full Bolt lifecycle; the classification contradicts the methodology's own canonical prompts home. Rejected. |

### Alternative B — Retire root prompts/ via this ADR (✅ Selected)

The root `prompts/` retires from the Product zone. Its remaining content
(`prompts/analysis.txt`) is removed through a dedicated Bolt; the prompt
itself already lives in the family as `PROMPT-001`.

| Aspect   | Detail |
|----------|--------|
| **Pros** | One canonical prompts home; the maintainer's prompts follow the same living-data rules the methodology ships; the Product zone shrinks to what actually ships or feeds the kit. |
| **Cons** | ADR-001 must be superseded (immutable), and the zone table must be restated so no rule is lost. The `analysis.txt` file is removed via a Bolt, not by this ADR (ADRs decide; Bolts change files). |

---

## 3. Decision

**ADR-001 is superseded by this ADR.** Its rules 1–6 remain in force
unchanged (two-tree governance, the release loop as the only path that
replaces the root tree, governance records written continuously, no
convergence until release, product edits never bypass governance, and the
kit-installed files' rule). Rule 7's zone table is amended as follows:

| Zone | Paths | Rule |
|------|-------|------|
| **Product** | `distribution-kit/`, `tools/` | Changed only through the full lifecycle: approved Bolt → approved SPEC → V-Bounce → MEM (G07). |
| **Governance** | the root `devflow/`: the artifact folders **and their `INDEX.md` files** | Written continuously as the record of governed work — creating an artifact and registering it in its INDEX is one act. The **methodology content** of that same tree (normative source, `GUARDRAILS.md`, `ONBOARDING.md`, templates, schemas, folder `README.md`, `VERSION`, `LANGUAGE`) is read-only, and only the release migration replaces it. |
| **Repository surface** | the root `README.md`, `CHANGELOG.md`, `.gitignore`, and the project section of the root `AGENTS.md` | Never edited on their own: they enter the scope of whichever Bolt makes them change, and are delivered with it. The single exception is the `CHANGELOG.md` entry that records a release. |
| **Never edited by hand** | the root `CLAUDE.md`, `.opencode/`, and every other installed platform agent definition | Pure framework, carrying nothing this repository authored. Only the release migration replaces them (rule 6). |
| **Retired** | the root `prompts/` | The canonical prompts home is `devflow/prompts/` (the family, US-003). The root folder holds no product content; its remaining file is removed by Bolt and the folder is not recreated. Prompts — the maintainer's included — live in the family as living data. |

The `prompts/` row of the former Product zone is gone; prompts content is no
longer product content. Any future decision to ship prompts as distributable
content would be a new ADR.

## 4. Consequences

**Positive:**
- One canonical prompts home, governed by the family's own rules (living
  data — the maintainer's prompts included).
- The Product zone now contains only what actually ships or feeds the kit
  (`distribution-kit/` and `tools/`).
- The maintainer's prompt housekeeping no longer needs a Bolt per file.

**Trade-offs:**
- ADR-001 is superseded — its zone table now lives in this ADR (rules 1–6
  carry forward by reference, unchanged).
- The one leftover file (`prompts/analysis.txt`) requires a Bolt to be
  removed — deliberate: the file was created as product content and leaves
  the zone governed, not by fiat.

**Technical debt:**
- None. The AGENTS.md project section references to root `prompts/` are
  updated by the Bolt that removes the file (repository surface enters the
  scope of the Bolt that changes it).

---

## 5. Applicable NFRs

None — this ADR defines a repository-zone rule.

---

## 6. References

- `devflow/adrs/_archive/ADR-001-repository-layout-methodology-and-product.md`
  (superseded by this ADR and archived — rules 1–6 carry forward unchanged
  by reference).
- `devflow/functional/user-stories/US-003-prompts-family.md` (approved —
  the canonical prompts family).
- `devflow/prompts/PROMPT-001-methodology-analysis.md` (the migrated
  prompt, living data in the family).

---

## 7. HITL-ADR-Approval

> **HITL-ADR-Approval** (Avenga DevFlow §2.8, §3.0, §3.5). An ADR does not
> become `accepted` — and therefore governing — without the approval of an
> Architect / Tech Lead. This ADR is the **source of truth for its own
> approval** (recorded in the `review` frontmatter block with review
> evidence); when it governs a SPEC revision, its path appears in that
> revision's `sources`. ADR approvals are never copied to the Bolt manifest.

| Field | Value |
|-------|-------|
| **Architect / Tech Lead** | eugenio.serrano |
| **Role** | architect |
| **Decision** | approved |
| **review_ready_at** | `2026-08-21T03:15:06-03:00` |
| **review.started_at** | `2026-08-21T03:17:55-03:00` |
| **review.decided_at** | `2026-08-21T03:17:55-03:00` |
| **Findings** | None — acknowledged_without_comment (reason in frontmatter `review:` block) |
