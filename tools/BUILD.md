# Building the `metaflow` binary

**Status:** specification. No code exists yet — this describes what we are about
to build and the constraints the build itself has to satisfy.

## What you need

Go. Nothing else.

```powershell
winget install GoLang.Go     # then open a new terminal so PATH is picked up
```

| | |
|---|---|
| **Go toolchain** | the only requirement — compiler, linker, test runner, formatter and dependency manager are one download |
| C compiler | not needed. We build with `CGO_ENABLED=0` |
| Windows SDK / Xcode / cross-toolchains | not needed, **not even to produce the macOS and Linux binaries** |
| Anything on the target machine | nothing. That is the point of choosing Go |

Cross-compilation is part of the toolchain, not an add-on: the six binaries the
methodology ships all come out of one machine, whichever machine that is.

## The source lives in the workshop, the binary ships with the product

`tools/` is where the toolchain is designed and built. `distribution-kit/` is
what gets copied into a project. That boundary already governs this folder
(`tools/README.md`), and the build honours it:

- The Go module is **`tools/`** — self-contained, so the methodology repository
  does not become a Go module at its root and the distributed `metaflow/` never
  sits inside one.
- The compiled binaries land in **`distribution-kit/metaflow/bin/`**, because
  that is the folder that travels with the methodology.

Source in the workshop, artifact in the product. Nothing else crosses.

## Layout

```
tools/
├── go.mod
├── BUILD.md                    this file
├── README.md                   why the toolchain exists, and its constraints
├── cmd/
│   └── metaflow/
│       └── main.go             flag parsing and subcommand dispatch, nothing else
├── internal/
│   ├── repo/                   locate the metaflow/ root, walk artifact folders
│   ├── artifact/               frontmatter parsing and the shared artifact model
│   ├── manifest/               the three v1 manifest shapes
│   ├── vocab/                  §3.15 status vocabulary and the emoji convention
│   ├── rules/                  the G/W/N/T predicates
│   └── <one package per subcommand>
├── clock/       DESIGN.md
├── identity/    DESIGN.md
├── indexer/     DESIGN.md
├── manifest/    DESIGN.md
├── next-id/     DESIGN.md
├── reporter/    DESIGN.md
├── scaffold/    DESIGN.md
├── status/      DESIGN.md
└── validator/   DESIGN.md + RULES-G.md
```

**One invariant worth keeping:** every subcommand package under `internal/` has
a spec folder of the same name holding its `DESIGN.md`, and vice versa. A
package with no spec, or a spec with no package, is drift — and it is cheap to
check, so eventually the build should check it.

The specs stay in their own folders rather than beside the code because they are
prose for humans and the packages are code for the compiler. They are read at
different moments by different readers.

## The build

```powershell
$env:CGO_ENABLED = 0
foreach ($t in 'windows/amd64','windows/arm64','darwin/amd64','darwin/arm64','linux/amd64','linux/arm64') {
  $os, $arch = $t.Split('/')
  $ext = if ($os -eq 'windows') { '.exe' } else { '' }
  $env:GOOS = $os; $env:GOARCH = $arch
  go build -trimpath -ldflags="-s -w" -o "../distribution-kit/metaflow/bin/metaflow-$os-$arch$ext" ./cmd/metaflow
}
```

Three flags, three reasons — none of them cosmetic:

| Flag | What it prevents |
|------|------------------|
| `CGO_ENABLED=0` | A binary linked against the build machine's system C library. Without it, a Linux build can carry a glibc dependency and fail on a different distro. With it, the binary is fully static and runs anywhere its OS/arch matches |
| `-trimpath` | Absolute build paths baked into the binary. Without it every committed executable would carry `C:\GitHubRepos\MetaFlow\...` inside it, and the same source built by two people would differ byte for byte |
| `-ldflags="-s -w"` | Debug symbols and the DWARF table. These binaries are committed to a git repository; carrying symbols nobody uses inflates every clone, forever |

## Reproducible by construction

Same source + same Go version + those three flags = **identical bytes**, on any
machine. That is not a nice-to-have here. We commit compiled executables to a
repository that other teams copy and run, so the honest question — *"is this
`.exe` really built from that source?"* — has to have an answer that does not
require trusting whoever ran the build.

The answer is a checksum file committed next to the binaries:

```
distribution-kit/metaflow/bin/SHA256SUMS
```

and the verification any reviewer can run:

```powershell
go build -trimpath -ldflags="-s -w" -o metaflow-check.exe ./cmd/metaflow
(Get-FileHash metaflow-check.exe -Algorithm SHA256).Hash
# must match the SHA256SUMS row for this platform
```

A mismatch means the committed binary does not correspond to the committed
source, which is exactly the failure this arrangement exists to make visible.

## Read-only, enforced by a test — not by a promise

`tools/README.md` states the rule: **no tool ever writes to disk.** A rule that
lives only in a README is a rule that erodes the first time someone is in a
hurry. Since the constraint is mechanical, the build should check it
mechanically.

`TestNoWrites` walks the module's own source and fails if any package outside
`cmd/metaflow` references a write path — `os.Create`, `os.WriteFile`,
`os.OpenFile` with a write flag, `os.Remove`, `os.Rename`, `os.MkdirAll`. The
allowance for `cmd/metaflow` is only so it can write to stdout, which is not the
filesystem.

The result is that "this tool cannot modify your repository" stops being
something we assert and becomes something a reviewer can verify in one test run.
For software that will be committed pre-compiled and run inside other people's
projects, that difference is the whole trust story.

## Dependencies: the one real decision

The goal is **standard library only**. A binary that is committed rather than
built from source at install time should have as little third-party code in it
as possible, because every dependency is code that ships to every project
without anyone reading it.

The one place that goal is under pressure is JSON Schema validation. The
manifest family is draft 2020-12 with `additionalProperties: false`, and there
are good Go libraries for it.

**The recommendation is to stay on the standard library**, because the three
schemas are fixed, known and versioned with the methodology — this is not
arbitrary schema validation, it is three specific shapes. Go's own decoder gives
us the hard part directly:

```go
dec := json.NewDecoder(r)
dec.DisallowUnknownFields()   // this is additionalProperties: false
```

Required fields, enums, patterns and the monotonic timestamp rule are then plain
Go on typed structs — and the timestamp rule was never expressible in JSON
Schema anyway (§3.12 says so explicitly), so that code has to exist regardless.

The cost is that the schemas end up described twice: once as JSON in
`metaflow/23-metrics/`, once as structs here. That is a real duplication and it
should be named as such — with a test that loads each `TEMPLATE-MANIFEST-*.json`
and round-trips it through the structs, so the two descriptions cannot silently
diverge.

## Go version

Pin a minimum in `go.mod` and do not chase releases. Since Go 1.21 the toolchain
honours the `go` and `toolchain` directives by fetching the named version
automatically, so a contributor with an older Go still produces the same build
without being told to upgrade anything.

Bumping the pinned version is a deliberate act, and it invalidates every
checksum in `SHA256SUMS` — so it comes with a rebuild of all six binaries in the
same change, never on its own.

## Open decisions

1. **Module path.** Nothing imports this module, so the path is close to
   arbitrary — but it is baked into every import line and changing it later
   touches every file. Worth choosing once, deliberately.
2. **Binary naming.** `metaflow-windows-amd64.exe` in one folder, or
   `bin/windows-amd64/metaflow.exe` so a user adds one directory to `PATH` and
   types `metaflow`. The second is friendlier for humans; the first is simpler
   for an agent resolving a path. The answer depends on how the agent is
   expected to reach the tool — see *How a tool reaches the agent* in
   `tools/README.md`.
3. **CI.** A pipeline that rebuilds all six targets and fails if any checksum
   differs from `SHA256SUMS` would make a stale committed binary impossible.
   Without it, the reproducibility guarantee holds only for whoever bothers to
   check by hand.
