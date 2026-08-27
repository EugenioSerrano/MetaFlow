---
id: "ADR-004"
title: "The repository partition and zone table (v2) — two-tree design restated in the active decision log"
date: "2026-08-21"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "accepted" # draft | accepted | rejected | deprecated | superseded
decision_makers: ["architect", "tech_lead"]
sources:
  - "devflow/adrs/_archive/ADR-001-repository-layout-methodology-and-product.md"
  - "devflow/adrs/ADR-003-prompts-family-canonical-home.md"
  - "maintainer direction (2026-08-21)"
supersedes: ["devflow/adrs/_archive/ADR-003-prompts-family-canonical-home.md"]
conflicts_with: []
tags: ["repository-layout", "two-tree", "zones", "governance", "maintainer-adopter"]
nfrs: []
waiver: # Only for gate-override ADRs (§3.6)
  gate: ""
  reason: ""
  owner: ""
  compensating_control: ""
  expires_at: ""
review_ready_at: "2026-08-21T03:26:58-03:00"
review: # HITL-ADR-Approval evidence — filled by the human reviewer (§3.0)
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - user: "eugenio.serrano"
      role: "architect"
  started_at: "2026-08-21T03:29:30-03:00"
  decided_at: "2026-08-21T03:29:30-03:00"
  findings: []
  acknowledged_without_comment: true # must be true when findings is empty (§3.0)
  acknowledgment_reason: "Reviewed the full restatement against ADR-001 (archived) and the current repository: the two-tree design and the maintainer/adopter roles are carried forward in substance, the zone table matches the repository as it stands (Product = distribution-kit/ + tools/; no zone for paths that no longer exist), the 'prompts' topic appears only in the ADR-003 file-path references, and the supersession chain (ADR-001 -> ADR-003 -> ADR-004) is recorded in the INDEX with both predecessors archived. The active decision log is self-contained again. Approved as drafted."
---

# ADR-004 — The repository partition and zone table (v2): two-tree design restated in the active decision log

| Field          | Value |
|----------------|-------|
| **Status**     | draft |
| **Decision-makers** | eugenio.serrano (architect / tech_lead) |
| **Sources**    | ADR-001 (archived — content restated here), ADR-003 (superseded by this ADR), maintainer direction (2026-08-21) |
| **Supersedes** | ADR-003 (in full); in substance also ADR-001 (archived — its complete content is restated here so the active decision log loses nothing) |
| **Conflicts with** | None — this ADR resolves the chain |

---

## 1. Context

This repository **builds** Avenga DevFlow and, at the same time, **is
governed by** Avenga DevFlow. That double role creates a structural
ambiguity that must be resolved once and for all: there are **two different
`devflow/` trees** in this repository, and they are never the same version.

| Tree | What it is | Version | How it is used |
|------|------------|---------|----------------|
| `distribution-kit/` | **The product.** The methodology as it will land in every adopting project. Its `devflow/` subtree is a copy-ready mirror of the target layout. | The next release, under construction | **This is what we edit** — it is the deliverable. |
| `devflow/` (repository root) | **This repository's own governance.** The installed methodology that governs the work of building the next release. | The current release, installed | **This is what governs us** — it is the rulebook, never the deliverable. |

**The two roles.** This repository operates in two roles at once: as the
**maintainer** of the methodology (building the next release in the kit,
while the installed tree governs the work) and as an **adopter** of its own
methodology (governed by the installed release, dogfooding every family it
ships). Every rule below exists to keep those two roles from collapsing into
each other: the referee is never edited while the match is in progress.

**Why v2.** ADR-001 (2026-08-17) established this partition. Its successor
ADR-003 (2026-08-21) superseded it *by reference* — a design mistake: with
ADR-001 archived, the rich content of the two-tree design (context, roles,
failure modes, consequences) left the active decision log. This ADR
**restates the full design in the active log**, with the zone table brought
to the repository's current reality. The supersession chain is recorded in
the INDEX; this document is the single operative statement of the
partition.

---

## 2. Alternatives considered

### Alternative A — Leave the design only in the archive (❌ Rejected)

| Aspect   | Detail |
|----------|--------|
| **Pros** | No new ADR. |
| **Cons** | The two-tree design — the most load-bearing decision of this repository — would live only in `_archive/`, excluded from agent scans (W20), with the operative successor pointing at an archived file. Future agents and reviewers lose the rationale. This is the state the maintainer rejected: the information is effectively lost from the active log. Rejected. |

### Alternative B — Restore ADR-001 from the archive (❌ Rejected)

Move ADR-001 back to the active `adrs/` folder with status `superseded`.

| Aspect   | Detail |
|----------|--------|
| **Pros** | The information is readable again. |
| **Cons** | The operative zone table would live in a narrow amendment while the design lives in the restored ADR-001 — the partition stays fragmented across documents. Rejected. |

### Alternative C — ADR-004 restates the full design in the active log (✅ Selected)

A single, comprehensive superseding ADR carries the entire two-tree design
forward — context, roles, rules 1–7, and the zone table as the repository
stands today.

| Aspect   | Detail |
|----------|--------|
| **Pros** | The active decision log is self-contained: one ADR answers "how is this repository partitioned and why". The zone table matches the current repository — every path belongs to exactly one zone, and nothing references paths that no longer exist. No information is lost: ADR-001's full content is restated, and the archive keeps the original for history. |
| **Cons** | One more ADR; the supersession chain grows (ADR-001 → ADR-003 → ADR-004). Mitigated by the INDEX and by ADR-004 being the single operative document. |

---

## 3. Decision

**This ADR supersedes ADR-003 (in full) and, in substance, ADR-001 (archived).** The two-tree partition of this repository is:

### Rule 1 — The root `devflow/` is the governing tree

It is the installed Avenga DevFlow release, exactly as it runs in any
adopting project. Its **methodology content** is **never edited** — not to
"fix" it, not to sync it with the kit, not to bump its version — while its
governance records, `INDEX.md` files included, are written continuously
(rule 3, and the zone table in rule 7). Its divergence from the kit is the
work in progress, not a defect. The only exception is the §5.16 release
migration: rename it to `devflowOLD/`, install the kit's `devflow/` in its
place, run the §5.16 migration, reconcile every file, human review, and the
human deletes `devflowOLD/`. **The migration is never a blanket copy of the
kit over the repository root.**

### Rule 2 — `distribution-kit/` is the product tree

Every methodology file that is *edited* — the methodology source, the
guardrails, the agent definitions, the templates, the schemas, the folder
map — is edited **only** in `distribution-kit/`. Together with `tools/`, it
holds every product change. Touching them requires the full governance path:
approved Bolt → approved SPEC → V-Bounce → MEM → approvals, exactly as any
code change would (G07).

### Rule 3 — The root `devflow/` is where governance documents are created

Every document produced by the use of the methodology — US, BUG, Bolt, SPEC,
MEM, ADR, DISC, REV, AREV, TC, RISK, INC, RETRO, manifests — is created
**inside the root `devflow/`**, in the canonical folders of the **installed**
layout and following the **installed** templates. The root tree is a
governed work area: read-only for *methodology content*, written
continuously with governance records.

### Rule 4 — The two trees never converge until a release

The release loop (§5.16) is the only mechanism that replaces the root tree,
and it operates as a single, human-reviewed transaction. The AGENTS.md
"two trees" table is the operational memory of this decision for agents;
this ADR is its governing record.

### Rule 5 — Product edits never bypass governance

A change to `distribution-kit/` or `tools/` is a product change and needs
the same approved Bolt + approved SPEC lifecycle as source code. "It is
just documentation" is not an exception: this repository's product *is*
documentation.

### Rule 6 — The files the kit installs outside `devflow/` have their own rule

The platform agent definitions (`CLAUDE.md`, `.opencode/agents/`, and any
other this repository installs) are pure framework: they carry nothing this
repository authored, and the release migration **overwrites** them.
`AGENTS.md` is the exception: everything **above** its project-section
marker comes from the kit and is replaced on migration; everything **below**
the marker belongs to this repository — the two-tree map, the release loop,
the definition of a code change here, the four-agent synchronization
procedure, the preamble parity matrix and the version bump procedure — and
**survives every migration untouched**. On that one file the release loop is
a **merge at the marker, never a copy**. The invariant is checkable: the
text above the marker must be byte-identical to the kit's `AGENTS.md`
(verified in the first real migration, 2026-08-21).

### Rule 7 — Every path in the repository belongs to exactly one zone

| Zone | Paths | Rule |
|------|-------|------|
| **Product** | `distribution-kit/`, `tools/` | Changed only through the full lifecycle: approved Bolt → approved SPEC → V-Bounce → MEM (G07). |
| **Governance** | the root `devflow/`: the artifact folders **and their `INDEX.md` files** | Written continuously as the record of governed work — creating an artifact and registering it in its INDEX is one act. The **methodology content** of that same tree (normative source, `GUARDRAILS.md`, `ONBOARDING.md`, templates, schemas, folder `README.md`, `VERSION`, `LANGUAGE`) is read-only, and only the release migration replaces it. |
| **Repository surface** | the root `README.md`, `CHANGELOG.md`, `.gitignore`, and the project section of the root `AGENTS.md` | Never edited on their own: they enter the scope of whichever Bolt makes them change, and are delivered with it. The single exception is the `CHANGELOG.md` entry that records a release. |
| **Never edited by hand** | the root `CLAUDE.md`, `.opencode/`, and every other installed platform agent definition | Pure framework, carrying nothing this repository authored. Only the release migration replaces them (rule 6). |

The zone table is the complete map: every path in the repository belongs to
exactly one zone, and an agent that cannot place a path in it stops and asks
rather than guessing. The `INDEX.md` files are the one thing that is
*shipped by the framework* and yet *must be written by the project* — they
are where the next sequential `NNN` is claimed.

---

## 4. Consequences

**Positive:**
- The governing methodology is always a known, stable, unmodified version;
  agents and humans can rely on it while building the next one.
- `distribution-kit/` stays a clean mirror; the two-tree divergence is a
  first-class status signal; self-hosting (dogfooding) is explicit — the
  maintainer role and the adopter role stay distinct but both real.
- The active decision log is self-contained: this ADR alone answers how the
  repository is partitioned and why. The zone table matches the repository
  as it stands — every path resolvable, no zone for paths that no longer
  exist.
- Nothing is lost: ADR-001's full content is restated here; the archive
  keeps the original for history.

**Trade-offs:**
- The supersession chain grows (ADR-001 → ADR-003 → ADR-004); the INDEX
  records it, and this ADR is the single operative document.
- ADR-003 is superseded shortly after acceptance — a consequence of the
  "carry forward by reference" design mistake, corrected here explicitly
  rather than papered over.

**Technical debt:**
- None. The first real §5.16 migration (2026-08-21) validated rules 1, 2,
  5, 6 and the AGENTS.md marker merge in production.

---

## 5. Applicable NFRs

None — this ADR defines repository-structure rules.

---

## 6. References

- `devflow/adrs/_archive/ADR-001-repository-layout-methodology-and-product.md`
  (archived — full content restated in this ADR).
- `devflow/adrs/_archive/ADR-003-prompts-family-canonical-home.md`
  (superseded by this ADR — its amendment is absorbed into the current zone
  table).
- Root `AGENTS.md` — project section (operational memory of the partition).

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
| **review_ready_at** | `2026-08-21T03:26:58-03:00` |
| **review.started_at** | `2026-08-21T03:29:30-03:00` |
| **review.decided_at** | `2026-08-21T03:29:30-03:00` |
| **Findings** | None — acknowledged_without_comment (reason in frontmatter `review:` block) |
