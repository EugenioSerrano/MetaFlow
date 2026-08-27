---
id: "US-017"
title: "Tooling distribution contract — how compiled executables ship in devflow/bin/ and survive migrations"
date: "2026-08-21"
author: "eugenio.serrano"
llm: "deepseek/deepseek-v4-flash"
status: "draft" # draft | approved | deprecated
owner: "eugenio.serrano" # Functional Analyst (governs this US)
unit: ""
story_points: 3 # proposed; confirmed at HITL-US-Approval (§2.6)
adrs: []
sources:
  - "distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md"
  - "maintainer product direction (2026-08-21)"
stakeholders: []
tags: ["tools", "bin", "distribution", "release", "kit"]
review_ready_at: ""
review: # HITL-US-Approval — filled by the human reviewer (§3.0)
  decision: ""
  reviewers: []
  started_at: ""
  decided_at: ""
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: ""
---

# US-017 — Tooling distribution contract: how compiled executables ship in devflow/bin/ and survive migrations

| Field          | Value |
|----------------|-------|
| **Unit**       | — |
| **ADRs**       | — |
| **Status**     | draft |
| **Story points** | 3 (proposed) |

**As a** DevFlow maintainer, **I want** a defined contract for how compiled
tooling executables land in `devflow/bin/`, how they are versioned, and how
the release migration replaces them, **so that** adopting projects receive
working, versioned binaries that never leak stale copies across upgrades.

---

## 1. The problem (explained, complete)

### What exists today

- The kit's folder tree declares the destination and its rule:
  `bin/ ← compiled tooling executables (optional by contract; replaced on
  upgrade, never copied forward, §5.16)`.
- `tools/` holds the sources (Go) with a `DESIGN.md` per tool — and the
  maintenance rules state that **`tools/` is never distributed**: what a
  project receives is the compiled executable that ships in the kit's
  `devflow/bin/`, never the folder.
- `US-012` (validator) explicitly promises its compiled executable in
  `devflow/bin/`.
- No binary actually ships in the kit today — `devflow/bin/` exists only in
  the folder tree as a declaration.

### What is missing (the gap)

1. **No build/publish procedure.** Nothing defines how a tool goes from
   `tools/<tool>/` source to a binary inside the kit: the build command,
   reproducibility, who runs it, and when (per Bolt? at release?).
2. **No versioning contract.** A binary in `bin/` has no defined identity:
   is it stamped with the methodology version? With its own tool version?
   Is there a checksum/SBOM manifest next to it? Adopters cannot verify they
   run the binary they think they run.
3. **No migration procedure.** §5.16 says `bin/` is "replaced on upgrade,
   never copied forward" — but there is no operational step that performs
   that replacement: the §5.16 migration must explicitly remove the old
   binaries and place the new ones, and the §5.16 routing/mapping must cover
   the folder (it is in the folder table, but not in the operational
   migration instructions).
4. **No platform contract.** The tools are Go — a compiled binary is
   platform-specific. What platforms ship (linux/amd64? windows? darwin?),
   how the binary is named (GOOS/GOARCH suffix?), and how adopters pick the
   right one is undefined.
5. **No provenance contract.** Distributed executables are third-party
   content from the IP/license gate's perspective: the license and
   third-party dependencies of each shipped binary must be recorded so the
   IP/license-provenance gate can pass.
6. **"Optional by contract" is undefined.** What does it mean for an
   adopter? Can a project omit `bin/` entirely? Do the methodology's
   internal references to tools (e.g. the manifest-validation gate) assume
   the binary exists?

### Why it matters

Without the contract, one of two failures happens: either **nothing ships**
(the tools stay source-only and US-012's promise is unfulfilled) or
**binaries land ad-hoc** with no versioning and no replacement story —
and stale binaries surviving a migration is exactly the failure mode §5.16's
"never copied forward" exists to prevent. This US makes the declaration in
the folder tree operational.

---

## 2. Acceptance criteria

- **Given** a compiled tool, **When** it is published into the kit, **Then**
  it lands in `distribution-kit/devflow/bin/` following the documented
  naming and versioning convention.
- **Given** the release migration, **When** the kit upgrades, **Then**
  `devflow/bin/` is replaced (old binaries removed, new ones placed) per the
  §5.16 operational procedure — never copied forward.
- **Given** a distributed binary, **When** an adopter runs it, **Then** it
  reports its version and works standalone.
- **Given** the toolset, **When** binaries are built, **Then** the procedure
  is documented (reproducible build command per tool) so any maintainer can
  rebuild them.
- **Given** platform support, **When** binaries ship, **Then** the supported
  platforms and the naming convention are defined (e.g. GOOS/GOARCH
  suffix).
- **Given** licensing, **When** a binary ships, **Then** its provenance
  (license + third-party dependencies) is recorded so the IP/license gate
  can pass.
- **Given** an adopting project without tooling needs, **When** it installs
  the kit, **Then** it may omit `bin/` (optional by contract) without
  breaking any methodology reference.

## 3. Notes / to refine before approval

- **Origin:** the kit folder tree's own `bin/` contract (§5.16) + US-012's
  promise of a shipped validator + maintainer direction. The methodology's
  tools are already referenced by gates (§3.6 Bolt-manifest validation,
  §3.12 timestamp ordering) — the contract makes those references
  deliverable.
- **Related backlog:** US-012 (validator — first binary that must ship);
  US-004..011 and US-016 (the other tools, all consumers of this contract);
  US-013 (reports generation may rely on the reporter tool).
- **Open design points:**
  - Version stamp source: the methodology `VERSION` file vs a per-tool
    version (proposal: methodology version — the tools ship with the
    methodology, not independently).
  - Single universal binary vs a platform matrix, and the naming scheme
    (proposal: `devflow/bin/<tool>-<goos>-<goarch>` or a small set of
    platforms).
  - Whether a checksum manifest (e.g. `bin/SHA256SUMS`) ships alongside.
  - Where the build/publish procedure lives: `tools/BUILD.md` (exists today)
    vs a new section in the methodology.
  - Whether CI publishes binaries or the maintainer builds at release time
    (out of scope for the kit, but the contract must not preclude it).
- **Scope note:** this US defines the **contract** (naming, versioning,
  migration, provenance); the actual builds and their ADRs stay with each
  tool's own Bolt.
