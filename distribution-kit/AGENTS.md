# AGENTS.md — Project instructions for AI agents

This repository runs under **MetaFlow**, the AI-assisted SDLC
methodology. You MUST follow it in every task.

- **Source of truth:** `metaflow/ai-sdlc/MetaFlow.md` (v1.1) — the methodology governs. If anything conflicts, it wins.
- **Agent rules (non-negotiable):** `metaflow/GUARDRAILS.md` — every `CP-<CODE>-Approval` is a mandatory checkpoint occupied by an actor — a human by default, a virtual MetaFlow Agent only by explicit, valid configuration (§3.0); never skip one, and never self-approve or fabricate a reviewer.
- **Onboarding:** read `metaflow/ONBOARDING.md` on your first task in this repository.
- **Framework map:** `metaflow/README.md` — folders, flow, cheat sheet.
- **Platform agent definition:** your tool loads its own definition from its
  own location (`CLAUDE.md` at the root, `.51-agents/skills/`, `.github/51-agents/`,
  `.opencode/51-agents/`). That file is the compact orchestration of the
  methodology; this one is the cross-tool entry point that points at it.
- **Language:** prose, filename slugs and 02-analysis/US/TC headings follow
  `metaflow/LANGUAGE`; the schema (YAML keys, enums, IDs) is always English.
  `CP-*-Approval` is never translated.

## No code without an approved TASK

Every code-related change — source, tests, configuration, infrastructure,
schemas, migrations, build scripts, deployment definitions — requires an
approved TASK and an approved SPEC. Urgency and size create no exception
(G07 — whose one scope-out: the agent lifecycle within `metaflow/51-agents/` +
`metaflow/53-actors/` is operational config — living data, not a code change).
If no TASK authorizes the work, say so and stop.

The single path, whatever the trigger:

```
Trigger (US | BUG | TC | DISC | REV | AREV | ADR)
  → origin approved  → TASK (CP-TASK-READY-Approval, includes DoR)
  → SPEC (CP-SPEC-Approval) → Delivery Loop → 24-tests/gates
  → MEM + manifest → CP-MEM-Approval → CP-TASK-DONE-Approval
```

## Human checkpoints are not yours to skip

`CP-<CODE>-Approval` is always a named actor — a human by default, a virtual MetaFlow Agent only by explicit, valid configuration — with timestamps and
review-quality evidence. You create the artifact; you never approve it, never
delegate the checkpoint, and never treat "the agent says it is fine" as an
approval. When a checkpoint is missing, name the exact one that is pending and
refuse to advance — even under time pressure, even if the user insists.

---

## Your project's own rules go below the marker

Do **not** append personal preferences or session memory to this file — it is
shared and versioned with the team; use your platform's native memory
mechanism instead. Durable, team-shared agent knowledge goes to
`metaflow/52-agents-data/<agent-name>/` (§5.12), which is never governed evidence.

**Read the project section before acting on anything above it.** Everything in
this framework block is the methodology's default. The section below the marker
belongs to this repository and may add constraints, name which tree you are
meant to edit, or qualify any statement above it — the source-of-truth line
included. It is not optional reading: where the two appear to disagree about
*this* repository, the project section is the one that knows where it is.

A methodology upgrade replaces this framework block and preserves your section
byte for byte (§5.16). That is also why nothing of yours belongs above the
marker — it would be overwritten on the next upgrade.

<!-- Everything below the marker that closes this file belongs to the project.
     A migration replaces only what is above it; your section survives byte for
     byte. Add your project's own conventions there. -->
<!-- METAFLOW:PROJECT-SECTION -->
