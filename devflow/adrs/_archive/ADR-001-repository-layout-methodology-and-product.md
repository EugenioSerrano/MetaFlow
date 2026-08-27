---
id: "ADR-001"
title: "Two-tree repository: the root devflow governs the work, distribution-kit is the only editable methodology"
date: "2026-08-17"
author: "eugenio.serrano"
llm: "claude-opus-5[1m]"
status: "superseded" # draft | accepted | rejected | deprecated | superseded
decision_makers: ["architect"] # Roles that participated in the decision
sources: [] # REVs, DISCs, previous ADRs, interviews that motivated this decision
supersedes: [] # ADRs this one replaces (§3.5 conflict resolution may supersede several)
conflicts_with: [] # ADRs whose decisions this ADR contradicts (optional; must be resolved by a superseding ADR before it governs a SPEC — §2.8)
tags: ["repository-layout", "self-hosting", "dogfooding", "governance"]
nfrs: [] # NFRs governed by this ADR (performance, security, availability, etc.)
waiver: # Only for gate-override ADRs (§3.6)
  gate: ""
  reason: ""
  owner: ""
  compensating_control: ""
  expires_at: "" # YYYY-MM-DD — mandatory, no open-ended waivers
review_ready_at: "2026-08-17T21:01:55-03:00" # When this exact version is submitted for review (§3.0)
review: # HITL-ADR-Approval evidence — filled by the human reviewer (§3.0)
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - user: "eugenio.serrano"
      role: "architect"
  started_at: "2026-08-17T21:01:55-03:00"
  decided_at: "2026-08-17T21:03:18-03:00"
  findings: []
  acknowledged_without_comment: true # must be true when findings is empty (§3.0)
  acknowledgment_reason: "Reviewed across several rounds before this revision: the reviewer requested a step-by-step walkthrough of the AGENTS.md release-time flow, then required that the Decision bind no specific methodology version, then confirmed the product zone covers tools/ and prompts/. Each point was applied to the draft and re-submitted; this revision adds rule 7 (repository zone partition) and resolves the INDEX.md read-only ambiguity. Approved as drafted, no findings outstanding."
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs, and section
  headings (##) stay in English (the schema). ADR titles and prose —
  context, decision, consequences — go in the project's content_language
  (declared in devflow/LANGUAGE). `HITL-ADR-Approval` is never translated.
  See devflow/README.md -> Language policy.

  ⚠️ HITL-ADR-Approval: An ADR remains a DRAFT until an Architect or
  Tech Lead records HITL-ADR-Approval (§2.8, §3.5). A draft ADR cannot
  govern a SPEC, establish an NFR, authorize an exception, or be treated
  as an accepted decision. No approval is inherited from related artifacts.

  ⚠️ ADR CONFLICTS (§2.8): Before approval, check the decision log for
  active ADRs that contradict this one. If any exists, do NOT approve
  this ADR as-is: declare the conflict via `conflicts_with` and create
  the superseding ADR that explicitly overrides them. A SPEC whose
  `sources` include mutually exclusive active ADRs is blocked by the
  pre-SPEC evidence gate (§2.4.1) until the conflict is resolved.
-->

# ADR-001 — Two-tree repository: the root devflow governs the work, distribution-kit is the only editable methodology

| Field          | Value |
|----------------|-------|
| **Status**     | accepted |
| **Decision-makers** | eugenio.serrano (architect) |
| **Sources**    | None (first ADR; codifies the layout already established in the repository's `AGENTS.md`) |
| **Supersedes** | None |
| **Conflicts with** | None — first ADR of this decision log |

---

## 1. Context

This repository **builds** Avenga DevFlow and, at the same time, **is
governed by** Avenga DevFlow. That double role creates a structural
ambiguity that must be resolved once and for all: there are **two
different `devflow/` trees** in this repository, and they are never the
same version.

| Tree | What it is | Version | How it is used |
|------|------------|---------|----------------|
| `distribution-kit/` | **The product.** The methodology as it will land in every adopting project. Its `devflow/` subtree is a copy-ready mirror of the target layout. | The next release, under construction | **This is what we edit** — it is the deliverable. |
| `devflow/` (repository root) | **This repository's own governance.** The installed methodology that governs the work of building the next release. | The current release, frozen | **This is what governs us** — it is the rulebook, never the deliverable. |

This ADR fixes the **relationship**, never a pair of version numbers: the
root tree always holds the released version that governs, the kit always
holds the next one under construction. Every release shifts both forward by
one and this ADR keeps applying unchanged. *(Illustration only, from the
moment this was written: the root held 4.1 while the kit built 4.2.)*

The root `devflow/` is the installed methodology that any adopting project
runs — save for whatever the release in construction has already removed from
the distributable, a transient difference each release migration resolves.
Editing it would be editing the referee while the
match is in progress: the version that governs us must stay stable and
unchanged, so the governance rules themselves are never moved under the
work they are supposed to control.

At the same time, the product methodology is never finished: the next
version is always being built, and building it is itself governed work. That means the
governance documents that record this effort — User Stories, Bolts,
SPECs, MEMs, ADRs, manifests, and the rest — are created **inside the
root `devflow/`**, following the very methodology those documents
describe. This is self-hosting ("dogfooding"): we deliver the next
version of the methodology by running the current version of the
methodology on itself.

The failure modes this ADR prevents are real and expensive:
- editing the root `devflow/` as if it were the product, silently
  diverging the rulebook from the installed version and breaking the
  §5.16 release migration;
- syncing or "fixing" the root tree to match the kit, which erases the
  record of work in progress;
- creating governance documents anywhere but the root `devflow/`,
  which would orphan them from the methodology's folder map;
- editing `distribution-kit/` without an approved Bolt, which would
  violate G07 for product changes just as it would for source code;
- installing the kit over the repository root as a plain copy, which would
  overwrite this repository's own `AGENTS.md` — the file carrying the
  authoring contract and the two-tree map — with the generic one the kit
  ships to adopting projects.

---

## 2. Alternatives considered

### Alternative A — Single tree: edit the installed methodology in place (❌ Rejected)

| Aspect   | Detail |
|----------|--------|
| **Pros** | One `devflow/` only; no two-tree mental model to keep; edits land "directly" in the methodology. |
| **Cons** | The rulebook becomes the work item: governance rules drift while they are being changed, so nothing is stable enough to govern anything. The installed version and the product version are indistinguishable. There is no clean copy-ready mirror for adopters (the kit must be assembled from a dirty tree). The §5.16 migration loses its source of truth: there is no frozen release to migrate away from, and no clean next version to migrate onto. This alternative is fundamentally unsound and was rejected from the start. |

### Alternative B — Two trees: root `devflow/` governs, `distribution-kit/` is the editable product (✅ Selected)

| Aspect   | Detail |
|----------|--------|
| **Pros** | The governing methodology stays frozen and trustworthy; the product is a clean, copy-ready mirror; the divergence between the two trees *is* the visible work in progress; governance documents live exactly where the methodology's folder map puts them; the §5.16 migration has a clear source (the installed release) and a clear target (the kit). |
| **Cons** | Two trees must never be manually synced; a contributor can accidentally edit the wrong tree (mitigated by this ADR, by `AGENTS.md`'s explicit two-tree table, and by the release-loop procedure which is the only path that replaces the root tree). |

### Alternative C — Keep the product in a separate repository

| Aspect   | Detail |
|----------|--------|
| **Pros** | Hard isolation between rulebook and product; no accidental cross-edits. |
| **Cons** | The governance history and the product history split into two repos, breaking atomic traceability (a SPEC revision in the root tree and the kit change it produced would live in different histories); the release migration (§5.16) must copy across repositories; adoption and review become more complex for no real gain. The two-tree layout inside one repository already achieves the isolation that matters: the separation is logical, not physical. |

### Alternative D — Keep the product on a dedicated branch of the same tree

| Aspect   | Detail |
|----------|--------|
| **Pros** | One tree in the working copy; branch names mark the product work. |
| **Cons** | Branch switching and merges make "which version am I looking at" a question that must be asked constantly; the kit's clean mirror layout still has to be extracted from a working tree that also contains governance; review diffs mix governance documents with product documents. More operational friction than Alternative B with no compensating benefit. |

---

## 3. Decision

We adopt **Alternative B**: this repository keeps two trees, with these
binding rules:

1. **The root `devflow/` is the governing tree.** It is the installed
   Avenga DevFlow release, exactly as it runs in any adopting project. This
   rule names no version: it binds whichever release the root tree currently
   holds. Its **methodology content** is
   **never edited** — not to "fix" it, not to sync it with the kit, not to
   bump its version — while its governance records, `INDEX.md` files included,
   are written continuously (rule 3, and the zone table in rule 7). Its divergence from the kit is the work in progress,
   not a defect to correct. The only exception is the §5.16 release
   migration, which replaces the root `devflow/` tree when a version closes:
   rename it to `devflowOLD/`, install the kit's `devflow/` in its place, run
   the §5.16 migration, reconcile every file, human review, and the human
   deletes `devflowOLD/`. **The migration is never a blanket copy of the kit
   over the repository root** — the files that live outside `devflow/` are
   governed by rule 6.

2. **`distribution-kit/` is the product tree.** Every methodology file
   that is *edited* — the methodology source, the guardrails, the agent
   definitions, the templates, the schemas, the folder map — is edited
   **only** in `distribution-kit/`. Together with `tools/` and
   `prompts/`, it holds every product change. These files are the **only
   methodology files that may be touched**, and touching them requires
   the full governance path: approved Bolt → approved SPEC → V-Bounce →
   MEM → approvals, exactly as any code change would (G07).

3. **The root `devflow/` is where governance documents are created.**
   As we use the methodology to deliver the next version, every document
   produced by that use — US, BUG, Bolt, SPEC, MEM, ADR, DISC, REV,
   AREV, TC, RISK, INC, RETRO, manifests — is created **inside the root
   `devflow/`**, in the canonical folders of the **installed** layout and
   following the **installed** templates — whichever release the root tree
   currently holds, never a fixed version. The root tree is a governed
   work area, not a static archive: it is read-only for *methodology
   content*, but it is written continuously with governance records.

4. **The two trees never converge until a release.** There is no
   intermediate state where the root tree partially reflects the kit.
   The release loop (§5.16) is the only mechanism that replaces the root
   tree, and it operates as a single, human-reviewed transaction. The
   AGENTS.md "two trees" table is the operational memory of this decision
   for agents; this ADR is its governing record.

5. **Product edits never bypass governance.** A change to
   `distribution-kit/`, `tools/` or `prompts/` is a product change and
   needs the same approved Bolt + approved SPEC lifecycle as source
   code. "It is just documentation" is not an exception: this repository's
   product *is* documentation.

6. **The files the kit installs outside `devflow/` have their own rule.**
   The platform agent definitions (`CLAUDE.md`, `.opencode/agents/`, and any
   other this repository installs) are pure framework: they carry nothing
   this repository authored, and the release migration **overwrites** them.
   `AGENTS.md` is the exception, because the methodology itself invites the
   project to extend it: everything **above** its project-section marker
   comes from the kit and is replaced on migration; everything **below** the
   marker belongs to this repository — the two-tree map, the release loop,
   the definition of a code change here, the four-agent synchronization
   procedure, the preamble parity matrix and the version bump procedure —
   and **survives every migration untouched**. On that one file the release
   loop is a **merge at the marker, never a copy**. The invariant is
   checkable: the text above the marker must be byte-identical to the kit's
   `AGENTS.md`, so any divergence means either someone customized where they
   must not, or the kit moved and the merge is pending.

7. **Every path in the repository belongs to exactly one zone.** Nothing
   falls outside this table, and an agent that cannot place a path in it
   stops and asks rather than guessing:

   | Zone | Paths | Rule |
   |------|-------|------|
   | **Product** | `distribution-kit/`, `tools/`, `prompts/` | Changed only through the full lifecycle: approved Bolt → approved SPEC → V-Bounce → MEM (G07). |
   | **Governance** | the root `devflow/`: the artifact folders **and their `INDEX.md` files** | Written continuously as the record of governed work — creating an artifact and registering it in its INDEX is one act. The **methodology content** of that same tree (normative source, `GUARDRAILS.md`, `ONBOARDING.md`, templates, schemas, folder `README.md`, `VERSION`, `LANGUAGE`) is read-only, and only the release migration replaces it. |
   | **Repository surface** | the root `README.md`, `CHANGELOG.md`, `.gitignore`, and the project section of the root `AGENTS.md` | Never edited on their own: they enter the scope of whichever Bolt makes them change, and are delivered with it. The single exception is the `CHANGELOG.md` entry that records a release. |
   | **Never edited by hand** | the root `CLAUDE.md`, `.opencode/`, and every other installed platform agent definition | Pure framework, carrying nothing this repository authored. Only the release migration replaces them (rule 6). |

   The `INDEX.md` files deserve their explicit place here because they are the
   one thing that is *shipped by the framework* and yet *must be written by
   the project*: they are where the next sequential `NNN` is claimed. Reading
   rule 1 without this table would freeze them, and every new artifact would
   go unregistered.

---

## 4. Consequences

**Positive:**
- The governing methodology is always a known, stable, unmodified
  version; agents and humans can rely on it while building the next one.
- `distribution-kit/` stays a clean mirror: an adopter copies its
  contents wholesale and nothing extra lands in their repository.
- The divergence between the two trees is a first-class status signal:
  it shows exactly how much of the next version has been delivered and what
  remains.
- Governance documents are created exactly where the installed
  methodology's folder map expects them, keeping every scanning tool and
  INDEX consistent.
- Self-hosting (dogfooding) is explicit: the next version of the
  methodology is delivered *through* the current version, which is the
  strongest possible test of the methodology itself.

**Trade-offs:**
- The same text exists in two places (the installed release and the kit) and
  must
  never be manually synced; the only sanctioned reconciliation is the
  release migration.
- Contributors must consciously pick the right tree for each edit; the
  two-tree table in `AGENTS.md` and this ADR are the guardrails for that
  choice.
- One file is neither purely framework nor purely project-authored: the root
  `AGENTS.md`. It is the only file the release loop must **merge** rather
  than replace, and the only place where a careless copy destroys governance
  content. The marker makes the merge mechanical, but it remains the step
  with the least margin for error in the whole release loop.
- A change that should update the installed rulebook *and* the product
  cannot be done in one edit: the product side goes through the normal
  Bolt→SPEC→V-Bounce lifecycle, and the rulebook side only via release
  migration. This slowness is intentional — it is what keeps governance
  stable.

**Technical debt:**
- None introduced by this decision; it is a structural rule. The known
  future cost is the release migration itself (§5.16), which is a
  deliberate, human-reviewed operation, not accumulated debt.

---

## 5. Applicable NFRs

This ADR does not define or govern non-functional requirements; it
defines a repository-structure rule. The NFR table is therefore not
applicable (no performance, security, availability or scalability
constraints are introduced).

---

## 6. References

- `AGENTS.md` (repository root) — Part 1 "This repository runs Avenga
  DevFlow" and Part 2 "What you are editing (the product)": the two-tree
  table, the definition of a code change, and the release loop.
- `devflow/avenga-devflow/Avenga-DevFlow.md` — installed methodology
  as installed, the governing source of truth; §5.16 defines the release
  migration that is the only path that replaces the root tree.
- `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md` — the
  product under construction.
- `devflow/GUARDRAILS.md` — G07 (no code-related change without an approved
  Bolt) is the enforcement projection of rules 2 and 5. **Rule 6 has no
  enforcement projection in the installed release**: extending G36 so that a
  migration may not destroy the project section of `AGENTS.md` is product
  work for the version under construction, and until it lands, rule 6 is
  enforced by this ADR
  and by `AGENTS.md` alone.
- Related ADRs: none (first ADR).

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
| **review_ready_at** | `2026-08-17T21:01:55-03:00` |
| **review.started_at** | `2026-08-17T21:01:55-03:00` |
| **review.decided_at** | `2026-08-17T21:03:18-03:00` |
| **Findings** | none — `acknowledged_without_comment: true`; reason recorded in the frontmatter `review:` block |
