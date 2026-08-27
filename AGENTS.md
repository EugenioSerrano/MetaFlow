# AGENTS.md — Project instructions for AI agents

This repository runs under **Avenga DevFlow**, the AI-assisted SDLC
methodology. You MUST follow it in every task.

- **Source of truth:** `devflow/avenga-devflow/Avenga-DevFlow.md` (v5.0) — the methodology governs. If anything conflicts, it wins.
- **Agent rules (non-negotiable):** `devflow/GUARDRAILS.md` — every `AITL-<CODE>-Approval` is a mandatory checkpoint occupied by an actor — a human by default, a virtual DevFlow Agent only by explicit, valid configuration (§3.0); never skip one, and never self-approve or fabricate a reviewer.
- **Onboarding:** read `devflow/ONBOARDING.md` on your first task in this repository.
- **Framework map:** `devflow/README.md` — folders, flow, cheat sheet.
- **Platform agent definition:** your tool loads its own definition from its
  own location (`CLAUDE.md` at the root, `.agents/skills/`, `.github/agents/`,
  `.opencode/agents/`). That file is the compact orchestration of the
  methodology; this one is the cross-tool entry point that points at it.
- **Language:** prose, filename slugs and analysis/US/TC headings follow
  `devflow/LANGUAGE`; the schema (YAML keys, enums, IDs) is always English.
  `AITL-*-Approval` is never translated.

## No code without an approved Bolt

Every code-related change — source, tests, configuration, infrastructure,
schemas, migrations, build scripts, deployment definitions — requires an
approved Bolt and an approved SPEC. Urgency and size create no exception
(G07). If no Bolt authorizes the work, say so and stop.

The single path, whatever the trigger:

```
Trigger (US | BUG | TC | DISC | REV | AREV | ADR)
  → origin approved  → BOLT (AITL-BOLT-READY-Approval, includes DoR)
  → SPEC (AITL-SPEC-Approval) → V-Bounce → tests/gates
  → MEM + manifest → AITL-MEM-Approval → AITL-BOLT-DONE-Approval
```

## Human checkpoints are not yours to skip

`AITL-<CODE>-Approval` is always a named actor — a human by default, a virtual DevFlow Agent only by explicit, valid configuration — with timestamps and
review-quality evidence. You create the artifact; you never approve it, never
delegate the checkpoint, and never treat "the agent says it is fine" as an
approval. When a checkpoint is missing, name the exact one that is pending and
refuse to advance — even under time pressure, even if the user insists.

---

## Your project's own rules go below the marker

Do **not** append personal preferences or session memory to this file — it is
shared and versioned with the team; use your platform's native memory
mechanism instead. Durable, team-shared agent knowledge goes to
`devflow/agents-data/<agent-name>/` (§5.12), which is never governed evidence.

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
<!-- AVENGA-DEVFLOW:PROJECT-SECTION -->

**If you read nothing else here:** the product this repository builds is
`distribution-kit/` — together with `tools/`, that is the only
thing you edit, and only through an approved Bolt and SPEC. The `devflow/` at
the repository root is the **installed rulebook** that governs the work: its
methodology content is never edited, only its governance records are written
into it. Getting those two backwards is the single mistake this section exists
to prevent.

# This repository builds Avenga DevFlow

> ## ⛔ There are two `devflow/` trees here
>
> This repository **builds** Avenga DevFlow and **is governed by** Avenga
> DevFlow. Those are two different trees and they are never the same version.
>
> | Tree | What it is | Version | You |
> |------|------------|---------|-----|
> | `distribution-kit/` | **The product.** Everything a project copies, laid out exactly as it lands there. | the next release, under construction | **edit this** |
> | `devflow/` (root) | **This repository's own governance** — the Bolts, SPECs, MEMs, ADRs and manifests of the work of building it. | the current release, frozen | **govern through this** |
>
> The root `devflow/` has its **methodology content never edited** — not to
> "fix" it, not to sync it with the kit, not to bump its version — while its
> governance records, `INDEX.md` files included, are written continuously.
> Its divergence from the kit is the work in progress, not a defect.
>
> Everything you change as *product* lives in `distribution-kit/` or
> `tools/`. Project prompts live in the canonical `devflow/prompts/` family
> (living data, ADR-003). Everything you produce as *governance* lives in the root
> `devflow/`. The partition is normative in **ADR-004** (superseding ADR-001/ADR-003).

## What governs you here

The source of truth is the root `devflow/avenga-devflow/Avenga-DevFlow.md` —
the **installed** release, not the draft in `distribution-kit/`. The kit is the
*product*, and it becomes governing only when this repository migrates onto it.

`CLAUDE.md` at the root and `.agents/skills/avenga-devflow/SKILL.md`,
`.github/agents/AvengaDevFlow.agent.md` and
`.opencode/agents/AvengaDevFlow.md` are the installed platform definitions in
use here. They are *installed copies*, not
sources: their sources live in `distribution-kit/`, and the release migration
replaces them. Never hand-edit them.

## What counts as a code change here

**The product of this repository is documentation.** A change to
`distribution-kit/` or `tools/` is a product change and needs an
approved Bolt and an approved SPEC, exactly as source code would (G07). Urgency
and size create no exception. If no Bolt authorizes the work, say so and stop.

**Verification replaces the test suite.** This repository has no runtime, so a
Bolt's expected evidence is the checks below — the four-agent sync diff, the
G-rule count, the version-marker sweep — plus whatever its SPEC names. A
V-Bounce that changed shared agent content and did not run the sync diff has no
evidence, the same way an untested code change has none.

## The release loop

When a version closes, this repository upgrades itself through the ordinary
§5.16 procedure. It is **never a blanket copy of the kit over the repository
root** — that would overwrite this very section. The steps:

1. Commit everything; the tree must be clean.
2. `mv devflow devflowOLD`.
3. Install the kit **excluding `AGENTS.md`** — its `devflow/` in place of the
   root one, and the platform agent definitions overwritten from it. Leaving
   that one file out is what keeps this section from ever being destroyed:
   `robocopy distribution-kit . /E /XF AGENTS.md`.
4. **Merge `AGENTS.md` at the marker, in place** — the new version's framework
   block above it, this repository's section from the marker onward, byte for
   byte. If you copied everything anyway and the file was already overwritten,
   take the section from the last commit instead; that is the fallback, and the
   reason step 1 exists.
5. Run the §5.16 migration and reconcile every file, including the ones outside
   `devflow/`.
6. Human review, then the human deletes `devflowOLD/`.

`git diff AGENTS.md` after step 4 must show no change from the marker onward.
That migration is where the next version starts, and it is the only real test
§5.16 gets.

---

# What you are editing (the product)

The normative source is
`distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md`;
`distribution-kit/devflow/GUARDRAILS.md` is its enforcement projection; the four
agent definitions in the kit are its compact orchestration per tool. When any of
them disagree, the methodology governs and the others are corrected — never the
reverse.

**`distribution-kit/` is a mirror of the target layout.** Every file in it goes
to an adopting project, at the exact path it occupies here. Nothing else may
live there — no README, no install notes, no scratch files: an adopter copies
the contents wholesale, so anything extra lands in their repository. Adoption
instructions belong in the root `README.md`.

```
distribution-kit/
├── AGENTS.md                                  → <project>/AGENTS.md
├── CLAUDE.md                                  → <project>/CLAUDE.md
├── devflow/                                   → <project>/devflow/
├── .agents/skills/avenga-devflow/SKILL.md     → same path
├── .github/agents/AvengaDevFlow.agent.md      → same path
└── .opencode/agents/AvengaDevFlow.md          → same path
```

**Neither this file nor `tools/` is distributed.** Project prompts ship as
living data in the canonical `devflow/prompts/` family (ADR-003).
`distribution-kit/AGENTS.md` is the `AGENTS.md` a project gets; this one governs
and maintains the methodology. `tools/` holds the source of the tools built
around DevFlow; what a project receives is the compiled executable that ships in
the kit's `devflow/bin/`, never the folder.

## Maintaining the four agents

The four platform definitions in the kit share their methodology sections
**verbatim** — only the platform-specific wrappers differ. There is no build
step: the four copies are kept identical by procedure, not tooling.

When changing any shared content:

1. **Before editing**, search the exact old text across the four — it must
   match in **all 4** (if it doesn't, stop and reconcile the drift first; that
   mismatch *is* a defect).
2. Apply the same change to all four files.
3. **After editing**, search the exact new text — it must again match 4×.
4. **Diff the whole shared body, not just the text you edited.** A grep only
   proves the lines you touched are in sync; it cannot see drift anywhere
   else. From the `# Avenga DevFlow v<version> (Methodology)` heading to end
   of file, the four must be byte-identical except the
   `devflow/agents-data/<agent>/` path — that single line is the only
   sanctioned divergence:

   ```bash
   K=distribution-kit
   for pair in "claude|$K/CLAUDE.md" \
               "codex|$K/.agents/skills/avenga-devflow/SKILL.md" \
               "ghcopilot|$K/.github/agents/AvengaDevFlow.agent.md" \
               "opencode|$K/.opencode/agents/AvengaDevFlow.md"; do
     name="${pair%%|*}"; f="${pair##*|}"
     n=$(grep -n '^# Avenga DevFlow v.* (Methodology)' "$f" | cut -d: -f1)
     tail -n +$n "$f" | tr -d '\r' > "/tmp/$name.body"
   done
   for b in codex ghcopilot opencode; do
     echo "$b: $(diff /tmp/claude.body /tmp/$b.body | grep -c '^[<>]') lines"
   done   # expected: 2 each (one - / one + for the agents-data path)
   ```

   The **platform preamble above that heading is exempt** — tool names,
   thinking mode, todo mechanism and memory wording legitimately differ per
   platform. Exempt from the verbatim rule is not exempt from being correct:
   read it too, since a truncated or half-edited sentence there is still a
   defect, just not a sync defect. Use the parity matrix below.
5. The MEM and the CHANGELOG entry name all four agent files.

**Invariant — every blocking rule is inline in every agent.** The agent file is
auto-loaded on every turn; `GUARDRAILS.md` is a first-task read that context
compaction can lose. A blocking rule the agent cannot see is a blocking rule it
will miss exactly when it matters. So the four agents carry **one row per
`G` rule, with no selection**, and adding a guardrail means adding its row in
the same pass. The count is checkable:

```bash
K=distribution-kit
g=$(grep -cE '^\| G[0-9]{2} \|' $K/devflow/GUARDRAILS.md)
for f in $K/CLAUDE.md $K/.agents/skills/avenga-devflow/SKILL.md \
         $K/.github/agents/AvengaDevFlow.agent.md \
         $K/.opencode/agents/AvengaDevFlow.md; do
  echo "$f: $(grep -cE '^\| G[0-9]{2} \|' "$f") / $g"
done   # every line must read N / N
```

Warnings (`W`), naming (`N`) and traceability (`T`) are **not** duplicated
inline — they shape output rather than block it, so losing them degrades
quality instead of breaking governance.

### Preamble parity matrix (the exempt zone)

The methodology is **agnostic about tools and models** — that is precisely why
there are four agent definitions instead of one. But agnosticism is also what
makes the exempt zone hard to audit: because the four run on four different
tools, any difference between them is ambiguous by default. It may be a
deliberate adaptation, or it may be drift nobody noticed — and the two look
identical in a diff.

This matrix removes that ambiguity. Every capability is either **equivalent**
across the four, or it **diverges for a reason recorded here**.

| Capability | Rule across the four |
|------------|----------------------|
| **Tool names** | *Diverge by definition.* Each agent names its own (`WebFetch` / `web_fetch` / `web/fetch` / `webfetch`, and so on). |
| **Frontmatter / loader manifest** | *Diverge by definition.* `claude` has none; `codex` requires `name` + `description`; `gh-copilot` carries `description` + `tools` + MCP comments; `open-code` carries `description` + `mode` + `temperature` + `permission`. The shared methodology body below the heading is unaffected by these differences. |
| **Thinking mode** | *Diverge in wording, equivalent in intent.* No frontmatter declares thinking behaviour (OpenCode's `mode:` is its agent type, not a reasoning config). The preamble prose names each host's native reasoning: `claude` says "use extended thinking" (a capability, no tool), the other three say "use the sequential thinking tool if available" — hedged because the tool's presence is host-specific. The behaviour is identical: thorough, step-by-step reasoning before acting. |
| **Web research** | *Equivalent policy, different reach.* The policy is identical — bounded, never proactive, never recursive. The reach is not: only `claude` has a search tool; the other three fetch a URL already known and say so. **An agent must never carry an instruction for a tool it does not have.** |
| **Debugging** | *Equivalent instruction, translated per tool.* All four run the project's own linter, type-checker and build; platform diagnostics (`read/problems`, IDE panels, whatever the host exposes) are an additional signal, never a replacement. |
| **Reading limits** | *Diverge.* `claude`'s Read tool has its own defaults, so the "2000 lines at a time" guidance applies to the other three only. |
| **Todo mechanism** | *Diverge.* `claude` uses the TodoWrite tool; the other three use the markdown todo-list block and display it to the user. |
| **Git section** | *Equivalent.* The `# Git` preamble block is byte-identical in all four — same rules, same phrasing. |
| **AITL section** | *Equivalent.* The `# AITL` preamble block is byte-identical in all four — same checkpoints, same routing. |
| **Memory** | *Equivalent policy, different wording.* Personal memory → the platform's native mechanism (never a fixed path); durable team knowledge → `devflow/agents-data/<agent>/`; **project instructions → below the `AVENGA-DEVFLOW:PROJECT-SECTION` marker of the root `AGENTS.md`, never the platform definition itself**, which an upgrade overwrites whole. Only the description of the native mechanism differs per platform. |
| **Write / exec gating** | *Diverge.* Only OpenCode's frontmatter supports `permission: edit/bash: ask`; the other three rely on their host's own confirmation model. |

**Adding a fifth agent:** walk this matrix top to bottom. For every row, either
implement the equivalent behaviour in that tool's vocabulary, or add the
divergence with its reason. Do **not** start by copying an existing agent — a
copy inherits whatever that one happens to have too much or too little of,
which is how the first three ended up carrying a "reformulate the query"
instruction without having a search tool.

## Version bump procedure

The methodology version is stamped in `distribution-kit/devflow/VERSION`; in the
`**Methodology version:**` header of **every `README.md` and `INDEX.md` under
`distribution-kit/devflow/`** — templates never carry it, because they are
instantiated into project artifacts; and in the kit's `devflow/GUARDRAILS.md`
(header + footer), `devflow/ONBOARDING.md`, the methodology frontmatter, the
four agent definitions (their `# Avenga DevFlow v<version> (Methodology)`
heading and `**Agent version:**` line), and the two files that state the version
in prose — the root `README.md` (*"Version **X.Y**"*) and
`distribution-kit/AGENTS.md` (the source-of-truth line).

There is no bump script and no marker count to memorise — the criterion above
is the rule and the grep below is the check:

1. Update `distribution-kit/devflow/VERSION` and sweep the markers.
2. Search the **old** version string across `distribution-kit/`.
3. **Never sweep a bare `4.1`.** Section references (`§2.4.1`, `§4.1`, `§4.10`)
   share that shape and a blind replace corrupts dozens of them. The safe
   patterns are `v4.1`, `Methodology version:** 4.1`, `Agent version:** 4.1`
   and `version: "4.1"` — the leading `v` or the label is what distinguishes a
   version marker from a section number.
4. Statements *about* an older version stay as written ("versions up to 4.1
   shipped one") — they are history, not markers.
5. Anything else that still matches is a missed file — fix it before releasing.
6. The MEM and the CHANGELOG's "Version bump" section enumerate the files
   touched.

---

`CHANGELOG.md` at the repository root is the framework's history and also where
this repository records its own methodology upgrades. From 4.2 on, the
distribution ships no `CHANGELOG.md` inside `devflow/`.
