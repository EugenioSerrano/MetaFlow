# tools/ — source code for the tools that consume Avenga DevFlow

**This folder is the workshop, not the product.** Here lives the **source code**
of the tools built around the methodology. What ships to a project is the
**built artifact**, delivered into the kit's `devflow/bin/` — never this folder.

The split is the classic one: `tools/` holds the **source**,
`distribution-kit/devflow/bin/` holds the **compiled executables** a project
installs. Keeping them apart is
what stops a project from receiving a compiler's worth of source it will never
build.

```
tools/                          ← source, this repository only, never distributed
├── identity/  clock/  next-id/
├── scaffold/  indexer/  manifest/
├── validator/  status/  reporter/
│       each with its DESIGN.md, and the source that implements it
│
└── (one binary)  build ↓

<project>/devflow/bin/devflow   ← ONE executable, nine subcommands
```

**One binary, not nine.** Every tool below is a subcommand of a single
`devflow` executable:

```
devflow whoami · now · next-id · new · index · manifest · validate · status · report
```

They share the same engine — artifact parsing, manifest reading, and the
derivation rules of §3.12 — so splitting them into separate executables would
mean shipping that engine nine times and keeping nine copies of the
methodology's semantics in sync. One binary also means one thing to build, one
to commit, and one to keep current.

## Why code, and not just the agent reading files

This is the point of the whole folder, and it is about **token economy** as much
as correctness.

Take **G13**, the pre-SPEC evidence gate. To verify it by hand an agent must
open the Bolt, its parent US, every TC, every ADR and every DISC/REV listed in
`sources`, read each one's `review:` block, and compare timestamps. That is a
dozen file reads and a few thousand tokens — **on every SPEC, forever**. The
same check as code is one command and one line of output.

Now multiply: **23 of the 39 blocking rules are fully decidable from the
repository** ([`validator/RULES-G.md`](validator/RULES-G.md)), and a project
runs them on every Bolt, every SPEC revision and every V-Bounce for its whole
life. An agent that navigates `devflow/` to answer questions a command can
answer is spending context on bookkeeping instead of on the work.

There is a second-order effect that matters more than the tokens: **a check that
is cheap actually gets run.** A check that costs a dozen file reads gets skipped
under pressure, and a rule nobody verifies is aspirational rather than
governing.

## The constraint that never changes

> `devflow/reports/README.md`: *"No Python, and no tooling of any kind, is
> required to use this methodology."*

Everything built here is **optional by contract**:

- **Strictly read-only. No tool ever writes to disk.** Not a document, not a
  manifest, not an `INDEX.md`, not a report — nothing. A tool reads, computes
  and **prints**; the agent writes what it was handed. There is no `--fix`, no
  `--write`, no in-place edit, and no exception. This is not a limitation to be
  relaxed once the tools mature: it is what keeps every byte that reaches the
  repository visible in the conversation and in the diff, authored by the agent
  under the same HITL governance as everything else. A tool that writes is a
  tool that can change the repository without anyone watching.
- Its rules are a **projection** of `devflow/GUARDRAILS.md` and the methodology.
  A tool that enforces something the methodology does not state has become a
  second source of truth — a defect, not a feature.
- If every tool disappeared, DevFlow would work exactly as documented, enforced
  by agents and humans following it. 4.0 shipped that state on purpose and the
  contract holds in every release: tooling arrives with the tools track, not
  with the methodology. The canonical tree reserves `devflow/bin/` for it
  (§5.1), and shipping tools must not quietly change the contract.

## The writers are emitters

Four of the tools below produce content — a scaffolded artifact, a manifest
entry, a rebuilt `INDEX.md`, a sprint report. **None of them writes it.** They
compute the content and print it; the agent receives it and writes the file.

That split keeps the whole value and gives up nothing. The hard part is
mechanical and belongs to the tool: knowing the schema, the routing table, the
next free ID, the derivation rules, the exact serialization. The easy part —
putting bytes in a file — belongs to the agent, which is already the only
writer in the flow and already answers for every change at
`HITL-MEM-Approval`.

It also makes the tools trivially testable (input in, text out, no filesystem)
and means a tool can never surprise anyone by having touched something.

## What is here

Each tool has a folder with its own `DESIGN.md`: the problem it solves anchored
to a `§` or a `G`, what it does, an interface sketch, its boundaries, and the
decisions still open. The designs ship as the track's specification; the
implementations land through the track's own delivery.

| Tool | What it solves | Why it matters |
|------|----------------|----------------|
| [`identity/`](identity/DESIGN.md) | One canonical human identifier across `author`, `created_by`, `reviewers[].user` and `owner` | **G29, G18 and G24 compare those strings.** `eugenio.serrano` vs `Eugenio Serrano` makes self-approval pass silently |
| [`clock/`](clock/DESIGN.md) | Repository time, not developer time — proposes `devflow/LOCATION` beside `LANGUAGE` | The naming rules already warn that SPEC/MEM filename ordering breaks across time zones. Convention today; enforceable with this |
| [`next-id/`](next-id/DESIGN.md) | The next free `NNN`, cross-checking the INDEX against the filesystem | §2.4: never reuse, gaps stay gaps. The cross-check catches an artifact created and never indexed |
| [`scaffold/`](scaffold/DESIGN.md) | Create an artifact **and its manifest** in one step | **Makes G33 structural** — the manifest stops being a step that can be skipped |
| [`indexer/`](indexer/DESIGN.md) | Rebuild and reconcile every `INDEX.md` against its folder | The INDEX allocates IDs; when it drifts, IDs collide. Required by §5.16 on every migration |
| [`manifest/`](manifest/DESIGN.md) | Append to the manifest family without breaking append-only, monotonicity or the schema | Three constraints a hand edit breaks, and no validator ships yet — the tools track delivers it |
| [`validator/`](validator/DESIGN.md) | The rules engine — batch for CI, **query for the agent** | The query mode is where the tokens are saved: ask before acting, not after. [39 rules classified](validator/RULES-G.md): 23 `full`, 12 `partial`, 4 `none` |
| [`status/`](status/DESIGN.md) | Walk a folder and report the `status` each document already records | Answering *"which BUGs are still draft?"* costs one file read per document today. It also surfaces the two states the methodology derives rather than stores — the Bolt's development state and the MEM's review state — without writing either |
| [`reporter/`](reporter/DESIGN.md) | Read the manifest family, emit `REPORT-YYYY-Www.html` | `reports/README.md` already specifies every derivation; only the generator is missing |

**Rough order.** `identity`, `clock` and `next-id` are foundations the others
call. `scaffold` and `manifest` are the writers. `status`, `indexer` and
`validator` share one derivation engine and are best built together —
`status` derives and prints, `indexer` persists what it derives, `validator`
judges it against the rules. `validator` is the one worth building first for
its own sake. `reporter` is the consumer, and needs nothing the others do not
already establish.

Specifications live next to the code that implements them, and both live next to
the methodology they project. When a guardrail changes, the rule, its coverage
decision and its implementation move in the same commit.

## How a tool reaches the agent: binary first, MCP later, never MCP-only

An MCP server is the obvious alternative to a command-line binary, and it is
tempting for one good reason. The decision is to build the **binary first** and
treat MCP as a thin wrapper added later — because of a constraint that is easy
to miss.

**The validator has three consumers, and MCP serves one of them:**

| Consumer | Speaks MCP |
|----------|------------|
| Pre-commit hook | No |
| **CI** — where §3.6 declares the `Bolt-manifest validation` gate | **No** |
| The agent | Yes |

MCP is an agent-to-tool protocol; CI does not speak it. And the validator
*must* run in CI, because that is where the methodology already places the
gate. **So the binary is required either way.** Starting with MCP means
building the binary afterwards anyway, and maintaining two entry points from
day one — which is how a second source of truth begins.

**What MCP genuinely adds is discovery**, and that is not a small thing: it is
the same token problem these tools exist to solve. With a binary, the agent has
to *know* the tool exists and how to call it — which means reading something.
With MCP, tools arrive in its list with schemas and no reading at all.

**What it costs** is the failure mode. The GitHub Copilot agent's own
frontmatter already records it:

> *"Declaring a server that is not installed makes the agent fail or prompt on
> first use, so this is **opt-in, not opt-out**."*

That collides with the promise in `devflow/reports/README.md` that no tooling is
required. A missing binary means the agent simply reads files instead; a
declared-but-missing MCP server means it fails or interrupts. The worse failure
mode lands on exactly the constraint that matters most. Configuration is the
other cost: `.mcp.json`, Claude Desktop config, VS Code settings and OpenCode
config are four different surfaces — the per-platform fragmentation the
methodology is deliberately agnostic about.

**The shape, then:** one binary that *is* the whole implementation, and later a
thin MCP wrapper that shells out to it and carries no logic of its own. CI and
pre-commit use the binary; agents with MCP configured get native discovery;
agents without it invoke the binary through the shell. **One implementation,
one place where the rules live.**

**And discovery has a cheap interim answer** that needs no protocol: a
`## Tooling` section in the four agents' shared body, beside the other
protocols, listing the commands and stating the fallback explicitly —

> *If `devflow/bin/` has the tool, use it. If it is absent, do the same work by
> reading the files.*

Roughly fifteen lines of shared body, works on all four platforms with nothing
to configure, and it makes the *optional by contract* behaviour explicit
instead of implied.

**Order:** binary → `## Tooling` section in the agents → MCP once the tools are
stable and the per-platform configuration cost is worth paying.

## Delivery: the binaries are committed

**Decision: built executables are committed into `devflow/bin/` and travel with
the repository**, like every other part of `devflow/`. Not downloaded, not
installed by a script, not fetched from a package manager.

What that buys is the thing the whole design is aiming at — **clone and it
runs**:

- **No install step at all.** A Go binary is native machine code with its
  runtime linked inside it. Nothing on the machine has to exist first: no .NET
  runtime, no JVM, no Node, no Python.
- **It sidesteps Gatekeeper and SmartScreen.** macOS blocks unsigned binaries
  carrying `com.apple.quarantine`, and Windows warns on files carrying the Mark
  of the Web — but **both marks are applied by downloaders**, not by
  `git clone`. A binary that arrives through the repository carries neither, so
  it runs without a signing certificate and without `xattr -d`. That alone is
  worth several hundred dollars a year in certificates not bought.

What it costs, stated plainly so nobody is surprised later:

- **Weight, permanently.** Git stores binaries without delta compression, so
  every released version stays in history forever and every developer pays for
  it on clone. Three things keep it small: it is **one binary, not nine** (all
  the tools are subcommands); commit **only the targets the team actually
  uses**, not all six; and build with `-ldflags="-s -w"`, which strips debug
  symbols and cuts roughly a third.
- **Revisit when it hurts.** If the repository starts to feel heavy, or the
  team spreads across more platforms, the alternatives are a gitignored
  `devflow/bin/` fed by an install script, or distribution through
  brew/scoop/winget with only a version pin committed. Neither is needed now.

**The Windows gotcha, because this team builds on Windows.** Git on Windows
does not track the Unix executable bit, so a binary committed from Windows
arrives on Linux and macOS **without `+x`** and fails with *permission denied*.
Set it explicitly at commit time:

```bash
git update-index --chmod=+x distribution-kit/devflow/bin/devflow-linux-amd64
git update-index --chmod=+x distribution-kit/devflow/bin/devflow-darwin-arm64
```

This is the kind of thing that gets discovered by the first person on a Mac,
two weeks after the release.

## Before the first tool ships

Delivering built artifacts into `devflow/bin/` is a **methodology change**, not
just a build step. The methodology side of that change is already in place —
a capability the tree reserves (§5.1), not a promise tied to any release:

- `devflow/bin/` now exists in §5.1's canonical tree and in the folder map of
  `devflow/README.md` — G30's predicate *"every directory must appear in §5.1
  or be a sanctioned exception"* passes by construction.
- The §5.16 migration procedure now names `bin/` explicitly among the content
  that *"comes from the new version"*: an upgrade replaces the executables
  with the new release's, and they are never copied forward from
  `devflowOLD/`.

What remains is the tools track's own work: the implementations, the build,
and the decision of which targets are committed (see *Delivery* above).
