# reporter — sprint reports from the manifest family

**Status:** specification. Planned with the tooling track — not bound to a
methodology release.

## The problem

`devflow/reports/README.md` already specifies what a report must show and which
derivation produces each number. `TEMPLATE-REPORT.html` already shows the target
shape. What is missing is the thing in between: **nothing in `devflow/` reads a
manifest and emits a report.**

A generator was built and hardened during the 4.0 cycle and then pulled before
release, together with the decision about where delivery tooling lives. This is
its replacement, built here and shipped as an executable in `devflow/bin/`.

## What it does

Read `metrics/user-stories/`, `metrics/bolts/` and `metrics/test-cases/`,
compute the metrics from the §3.12 timing contract, and **print** a
self-contained `REPORT-YYYY-Www.html` to stdout, together with the filename it
should carry. The agent writes it — the tool never creates the file, exactly
like every other tool here.

The derivations are already written down in `reports/README.md` — Bolt and US
lead time, review queue time, active review time, rework, spec drift,
first-pass approval, HITL coverage, and AI usage per provider and model. The
tool implements that table; it does not invent metrics.

## Boundaries

**It writes nothing.** The HTML goes to stdout; the agent saves it under
`reports/`. Everything else is already stated in the methodology:

- **Reports are derivative** (§5.5 class, §5.12): never citable as the source of
  a SPEC, Bolt, ADR, US, TC or BUG. **G28** blocks it.
- **State the limits, never invent.** Gates, tests, DORA, deployments and cost
  are deliberately outside the manifest (§3.12). A report says so rather than
  estimating around the gap.
- **Assert one `schema_version`.** A repository holds a single manifest family
  (§3.12); a manifest declaring another is an unfinished migration (§5.16), and
  the report says so instead of aggregating it into the statistics.
- **The latest decision governs, never the first.** `hitl_approvals[]` is
  append-only, so a `changes_requested` followed by an `approved` is approved.

## Two things a generated report must not do

1. **Never carry the design-reference banner.** `TEMPLATE-REPORT.html` opens
   with a red block declaring it fictional example data. That marker belongs to
   the template alone — a real report carrying it is worse than one with no
   banner, because it teaches readers to ignore the warning.
2. **Never derive a velocity metric from story points.** §2.6 and W18 forbid
   it, and `reports/README.md` now names *"Story points delivered"* explicitly
   as **not** a report metric. Forecasting stays on throughput and Bolt Lead
   Time (§4.3).
