# Avenga DevFlow

**The AI-native SDLC methodology of Avenga LATAM.** Version **5.1**.

> **Versions at a glance.** The **product** is **5.1** — developed on the `5.1` branch and **released by merging to `main`**, so `main` always carries the latest released version and each release is tagged (`vN`). The **maintainer partition** that governs this repository — the root [`devflow/`](devflow/) and the agent definitions (`CLAUDE.md`, …) — operates under **5.0** (the previous stable) and advances only at the next version's §5.16 migration. In-progress vs released is told by branch-vs-`main`, not by version text. See [ADR-006](devflow/adrs/ADR-006-versioning-and-self-development-model.md).

The AI agent generates the intended-final code, tests and design; the human
governs through named, non-negotiable approval checkpoints. Work is sliced
into **Bolts** (1 hour to 1 working day of active delivery) and executed
through **V-Bounce** — approved SPEC → autonomous generation and verification
→ mandatory implementation memory → human approval.

> ## Two `devflow/` trees, and that is deliberate
>
> This repository **builds** Avenga DevFlow and **is governed by** Avenga
> DevFlow. Those are two different trees, and they are never the same version:
>
> | Tree | What it is | Version |
> |------|------------|---------|
> | [`distribution-kit/`](distribution-kit/) | **The product.** Everything a project copies, laid out exactly as it has to land there. This is what changes when the methodology changes. | **5.1** |
> | [`devflow/`](devflow/) | **The governance of this repository.** The ADRs, Bolts, SPECs, MEMs and manifests of the work of building this methodology — the same artifacts any adopting project keeps. | **5.0** — the operating methodology (previous stable); advances at the next §5.16 |
>
> **The release loop.** When a version closes, this repository upgrades its own
> root through the ordinary §5.16 procedure — rename `devflow/` to
> `devflowOLD/`, install the kit, migrate, reconcile — and that migration is
> where the next version begins. Every release therefore runs the upgrade path
> a real adopter runs, on a real repository with real artifacts in it. It is the
> only honest test §5.16 can get.
>
> **The rule that keeps the two apart:** nothing edits the root `devflow/`
> except that migration. Methodology work happens in `distribution-kit/`.
>
> To **use** DevFlow on a project, start at *Adopting it* below. To **change**
> the methodology, read [`AGENTS.md`](AGENTS.md) first.

---

## Adopting it on a project

Everything a project needs is in [`distribution-kit/`](distribution-kit/), laid
out exactly as it has to end up in your repository. Copy its **contents** to
your repository root:

```bash
cp -a distribution-kit/.  <your-repo>/      # bash — the trailing /. is what includes the dotted folders
robocopy distribution-kit <your-repo> /E    # Windows
```

> `cp -r distribution-kit/* <your-repo>/` **silently skips** `.agents/`,
> `.github/` and `.opencode/`. Use one of the two forms above.

| What lands | Where | When |
|------------|-------|------|
| `devflow/` — the whole folder | `<your-repo>/devflow/` | Always — the documentary root: methodology, guardrails, templates, folder structure |
| `AGENTS.md` | `<your-repo>/AGENTS.md` | Always — cross-tool entry point, auto-loaded from the root by several agents |
| `CLAUDE.md` | `<your-repo>/CLAUDE.md` | Claude Code |
| `.agents/skills/avenga-devflow/SKILL.md` | same path | OpenAI Codex |
| `.github/agents/AvengaDevFlow.agent.md` | same path | GitHub Copilot |
| `.opencode/agents/AvengaDevFlow.md` | same path | OpenCode |

The four agent definitions share their methodology sections **verbatim** — they
differ only in the platform wrapper. Keep the one for the tool your team uses
and delete the other three.

### Platform notes

- **Claude Code.** `CLAUDE.md` at the repository root is the whole
  installation; it is loaded automatically at the start of every session.
- **OpenAI Codex.** The folder name must match the `name:` field in the SKILL
  frontmatter (`avenga-devflow`), and that frontmatter is mandatory — without
  it Codex rejects the file with a parse error and the skill never loads.
  Codex discovers project skills by walking up from the working directory to
  the repository root, so `.agents/skills/` resolves from any subfolder. For a
  personal install use `~/.agents/skills/avenga-devflow/`; CLIs predating the
  move to `.agents/skills/` use `~/.codex/skills/`. `~/.codex/config.toml` is
  where a skill is enabled or disabled.
- **GitHub Copilot.** VS Code and Visual Studio 2026 both detect the file
  automatically, but the `tools:` list in its frontmatter is VS Code-specific
  and is **not portable**: VS 2026 uses a different tool vocabulary
  (`code_search`, `readfile`, `editfiles`, `getwebpages`,
  `runcommandinterminal`), so the declared tools will not resolve there.
  Adjust the list before use — the agent's own frontmatter documents this too.
- **OpenCode.** The project location overrides a personal install at
  `<user>/.config/opencode/agents/`; both `agents` and `agent` are accepted as
  the folder name. The definition ships with `permission.edit` and
  `permission.bash` set to `ask`, so OpenCode prompts before each file write
  and each shell command — change them to `allow` in the frontmatter if your
  team prefers unattended execution.

After that: set `devflow/LANGUAGE` to your project's content language, drop raw
material into `devflow/input/`, and follow `devflow/README.md` → *Starting a
New Project*.

DevFlow ships **no `CHANGELOG.md`**. Your repository's own changelog, at its
root, is where methodology upgrades get recorded (§5.16).

**No tooling is required.** The methodology is enforced by agents and humans
following it; everything under `tools/` and `devflow/bin/` is optional by
contract — if the tooling is absent, DevFlow works exactly as documented.

---

## Reading order

These are the 5.1 documents — the version being built. Inside an adopting
project the same files sit under `devflow/`.

| Document | What it is |
|----------|------------|
| [`devflow/README.md`](distribution-kit/devflow/README.md) | Framework map: folders, full flow, cheat sheet |
| [`devflow/avenga-devflow/Avenga-DevFlow.md`](distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md) | **The normative source.** §2 owns concepts, §3 owns lifecycle and HITL, §4 is a walkthrough, §5 owns structure |
| [`devflow/GUARDRAILS.md`](distribution-kit/devflow/GUARDRAILS.md) | What an agent must block (G01–G39) or warn about (W01–W21), plus naming and traceability |
| [`devflow/ONBOARDING.md`](distribution-kit/devflow/ONBOARDING.md) | Role-based path, minimal glossary, FAQ |

Every subfolder carries its own `README.md`; read it before creating documents
there.

---

## Working on the methodology

**Changes to DevFlow are governed by DevFlow.** The thing being built is
[`distribution-kit/`](distribution-kit/); the governance of building it lives in
the root [`devflow/`](devflow/), exactly as in any adopting project. A change
starts from an approved origin (US, BUG, TC, DISC, REV, ADR), gets a Bolt and a
SPEC, runs a V-Bounce, and ends with a MEM and its manifest. No edit to the
methodology reaches the kit outside that path. **Language:** every methodology
artifact of this repository — the maintenance partition and the kit alike —
is written in English, commit and PR messages included (ADR-011, ADR-012).

Read [`AGENTS.md`](AGENTS.md) first. It is both this repository's DevFlow entry
point and its authoring contract, and it carries the three procedures that
belong to building a methodology rather than an application:

- **Four-agent synchronization.** The methodology body of the four agent
  definitions is byte-identical by procedure, not by tooling. Changing shared
  content is a four-step process with a verification diff.
- **Preamble parity matrix.** The platform preamble is exempt from that rule,
  so each capability is recorded as either equivalent across the four or
  divergent for a stated reason.
- **Version bump.** Every `README.md` and `INDEX.md` in the kit's `devflow/`
  carries a `**Methodology version:**` header; templates never do.

[`tools/`](tools/) holds the **source code of the tools built around the
methodology** — currently a validator design and the classification of all 39
blocking rules by whether a tool can decide them. The folder is **never
distributed**: what reaches a project is the compiled executable that ships in
the kit's `devflow/bin/`. The motivation is as much token economy as
correctness — an agent that navigates `devflow/` to answer what a command can
answer spends its context on bookkeeping. Everything built there stays
**optional by contract**: `devflow/` must remain runnable with no toolchain at
all.

[`CHANGELOG.md`](CHANGELOG.md) at the repository root is the history of the
framework itself, and the same file records this repository's own methodology
upgrades. From 4.2 on, the distribution ships no `CHANGELOG.md` of its own.

---

## Known limitations

Read these before adopting: `HITL-UNIT-Approval` and the `units/` folder are
reserved; multi-repo and shared-monorepo `devflow/` are out of scope; report
generation is planned for the next version; and no validation tooling ships.
The full table, with where each one is governed, is in
[`devflow/README.md`](distribution-kit/devflow/README.md) → *Known Limitations
& Roadmap*.

---

**Avenga DevFlow is the proprietary methodology and framework of Avenga
LATAM**, developed by the research team to systematize AI-assisted software
development. It is based on *AI-Driven Development Life Cycle: Reimagining
Software Engineering* (Raja SP, AWS) and on the delivery-performance evidence
synthesized in *Accelerate* / DORA.
