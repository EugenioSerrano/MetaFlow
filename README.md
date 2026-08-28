# MetaFlow

**The AI-native SDLC methodology.** Version **1.1**.

The AI agent generates the intended-final code, tests and design; the human
governs through named, non-negotiable CITL checkpoints. Work is sliced into
**TASKs** (1 hour to 1 working day of active delivery) and executed through
the **Delivery Loop** — approved SPEC → autonomous generation and verification
→ mandatory implementation memory (MEM) → human approval.

> ## Two partitions, and that is deliberate
>
> This repository **builds** MetaFlow and **is governed by** MetaFlow. Those
> are two different trees, and they are never the same version:
>
> | Tree | What it is | Version |
> |------|------------|---------|
> | [`metaflow/`](metaflow/) | **The governance of this repository.** The installed MetaFlow tree — **where we use MetaFlow today**. The ADRs, USs, TASKs, SPECs, MEMs and manifests of the work of building this methodology — the same artifacts any adopting project keeps. | **1.1** — the operating methodology |
> | [`distribution-kit/`](distribution-kit/) | **The product.** Everything a project copies, laid out exactly as it has to land in an adopting repository. **The next version** of the kit — this is what changes when the methodology changes. | **1.1** (next version line) |
>
> **The release loop.** When a version closes, this repository upgrades its own
> root through the ordinary §5.16 procedure — install the kit, migrate,
> reconcile — and that migration is where the next version begins. Every
> release therefore runs the upgrade path a real adopter runs, on a real
> repository with real artifacts in it.
>
> **The rule that keeps the two apart:** nothing edits the root `metaflow/`
> except that migration. Methodology work happens in `distribution-kit/`,
> generated from `input-kit/` by the transformation pipeline (`src/` —
> engine, `mapping.json` dictionary and tests).
>
> To **use** MetaFlow on a project, start at *Adopting it* below. To **change**
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
| `metaflow/` — the whole folder | `<your-repo>/metaflow/` | Always — the documentary root: methodology, guardrails, templates, folder structure |
| `AGENTS.md` | `<your-repo>/AGENTS.md` | Always — cross-tool entry point, auto-loaded from the root by several agents |
| `CLAUDE.md` | `<your-repo>/CLAUDE.md` | Claude Code |
| `.agents/skills/MetaFlow/SKILL.md` | same path | OpenAI Codex |
| `.github/agents/MetaFlow.agent.md` | same path | GitHub Copilot |
| `.opencode/agents/MetaFlow.md` | same path | OpenCode |

The four agent definitions share their methodology sections **verbatim** — they
differ only in the platform wrapper. Keep the one for the tool your team uses
and delete the other three.

### Platform notes

- **Claude Code.** `CLAUDE.md` at the repository root is the whole
  installation; it is loaded automatically at the start of every session.
- **OpenAI Codex.** The folder name must match the `name:` field in the SKILL
  frontmatter (`MetaFlow`), and that frontmatter is mandatory — without it
  Codex rejects the file with a parse error and the skill never loads.
  Codex discovers project skills by walking up from the working directory to
  the repository root, so `.agents/skills/` resolves from any subfolder. For a
  personal install use `~/.agents/skills/MetaFlow/`; CLIs predating the
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

After that: set `metaflow/LANGUAGE` to your project's content language, drop
raw material into `metaflow/01-input/`, and follow `metaflow/README.md` →
*Starting a New Project*.

MetaFlow ships **no `CHANGELOG.md`**. Your repository's own changelog, at its
root, is where methodology upgrades get recorded (§5.16).

**No tooling is required.** The methodology is enforced by agents and humans
following it; everything under `tools/` is optional by contract — if the
tooling is absent, MetaFlow works exactly as documented.

---

## Reading order

These are the 1.1 documents — the version being built. Inside an adopting
project the same files sit under `metaflow/`.

| Document | What it is |
|----------|------------|
| [`metaflow/README.md`](distribution-kit/metaflow/README.md) | Framework map: folders, full flow, cheat sheet |
| [`metaflow/ai-sdlc/MetaFlow.md`](distribution-kit/metaflow/ai-sdlc/MetaFlow.md) | **The normative source.** §2 owns concepts, §3 owns lifecycle and CITL, §4 is a walkthrough, §5 owns structure |
| [`metaflow/GUARDRAILS.md`](distribution-kit/metaflow/GUARDRAILS.md) | What an agent must block (G01–G39) or warn about (W01–W21), plus naming and traceability |
| [`metaflow/ONBOARDING.md`](distribution-kit/metaflow/ONBOARDING.md) | Role-based path, minimal glossary, FAQ |

Every subfolder carries its own `README.md`; read it before creating documents
there.

---

## Working on the methodology

**Changes to MetaFlow are governed by MetaFlow.** The thing being built is
[`distribution-kit/`](distribution-kit/); the governance of building it lives
in the root [`metaflow/`](metaflow/), exactly as in any adopting project. A
change starts from an approved origin (US, BUG, TC, DISC, REV, ADR), gets a
TASK and a SPEC, runs a Delivery Loop, and ends with a MEM and its manifest.
No edit to the methodology reaches the kit outside that path.

Read [`AGENTS.md`](AGENTS.md) first. It is this repository's MetaFlow entry
point and its authoring contract, and it carries the two-partition model in
its project section.

[`tools/`](tools/) holds the **source code of the tools built around the
methodology** — validator designs, agent-wrapper tooling and the
classification of the 39 blocking rules by whether a tool can decide them.
The folder is **never distributed**: what reaches a project is what the kit
ships in `metaflow/`. Everything built there stays **optional by contract**:
`metaflow/` must remain runnable with no toolchain at all.

[`CHANGELOG.md`](CHANGELOG.md) at the repository root is the history of the
framework itself, and the same file records this repository's own methodology
upgrades.

---

## Known limitations

Read these before adopting — the full table, with where each one is governed,
is in [`metaflow/README.md`](distribution-kit/metaflow/README.md) → *Known
Limitations & Roadmap*.

---

**MetaFlow is the proprietary methodology and framework of Eugenio Serrano**,
developed by the research team to systematize AI-assisted software
development. It is based on *AI-Driven Development Life Cycle: Reimagining
Software Engineering* (Raja SP, AWS).
