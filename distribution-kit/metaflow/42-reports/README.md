# Reports (Sprint Progress Reports)

**Methodology version:** 1.1

## Purpose

Self-contained HTML progress reports for **project management**, built from
the manifest family in `23-metrics/` (`tasks/`, `user-stories/`, `test-cases/`).
Each report answers, at end of sprint:

- how much was delivered (US, TASKs) and by whom — as a delivery record,
  never as an individual performance measure (§3.7.1);
- how long each thing took — lead times, review queue times, active review
  times (§3.12 timing contract);
- how healthy the process is — rework, spec drift, first-pass approval rates,
  CITL coverage, time-to-review vs the < 4 h target (§3.0);
- how much AI was used — tokens and duration by provider/model, per level.

Reports are **derived artifacts** (§5.5 class, §5.12): they are **not governed
evidence** — never citable as the source of a SPEC, TASK, ADR, US, TC or BUG.

---

## 🚧 Work in progress — no generator ships yet

> **Read this before using anything in this folder.**

`TEMPLATE-REPORT.html` is currently a **design
reference**, not a fillable template: a self-contained mockup, populated with
example data, that shows the target shape of the report — Executive Summary,
US and TASK Progress, Backlog Status, TASK Detail, Quality & Risks, Project
Gantt and Management View.

**There is no report generator in this repository.** Producing a report from
the manifests is deferred to the tooling track (a `metaflow/bin/` area fed by
a separate tooling project is the direction; `bin/` is now part of the
canonical tree, §5.1). Until then:

- Nothing in `metaflow/` reads the manifests to emit a report.
- The template's numbers are illustrative. **Do not read them as project
  data**, and do not hand-edit it into a real report and circulate it as one.
- No Python, and no tooling of any kind, is required to use this methodology.

**The manifest family is unaffected.** `23-metrics/` is the *source* of a future
report, never its output: the timing contract, the three v5 schemas and their
examples stand exactly as they are, and nothing here changes what an agent
must record (G23, G33, §3.12). A report is a consumer of that data; the
absence of a consumer changes nothing upstream.

---

## Naming and archiving

- Output: `REPORT-YYYY-Www.html` (ISO year + ISO week), one per sprint.
- Old reports move to `_archive/` (§5.4) like any other lifecycle-closed
  document, and once archived they fall under the agent-scan exclusion (W20).
  W20 covers `_archive/` only — an active report in `42-reports/` is readable,
  it is simply never citable as evidence (G28).

---

## What a report is meant to show (from the timing contract)

This is the target contract for whatever eventually produces the report — it
is what the manifest family already makes derivable, not a description of
existing behaviour.

| Metric | Derivation |
|--------|------------|
| US / TASK / TC counts and states | derived from approvals (never stored) |
| ~~Story points delivered~~ | **Not a report metric.** Summing `story_points` per sprint is velocity, and §2.6/W18 forbid deriving any velocity or performance target from them. Forecasting uses throughput and TASK Lead Time (§4.3). |
| TASK lead time | TASK-DONE − TASK-READY `decided_at` |
| US lead time | last child TASK DONE − US `CP-US-Approval` `decided_at` |
| Review queue time | `review_started_at` − `review_ready_at` (Time-to-Human-Review, target < 4 h — §3.0, §3.7.3) |
| Active review time | `decided_at` − `review_started_at` |
| Review latency | `decided_at` − `review_ready_at` (informational, no target) |
| Rework | Delivery Loops per TASK; `changes_requested` rate |
| Spec drift | `spec_revisions[]` per TASK |
| First-pass approval | per §3.7.2: SPEC revisions whose **first** `CP-SPEC-Approval` is `approved` / SPEC revisions reviewed; TASKs whose **first** Delivery Loop is approved / TASKs with a reviewed Delivery Loop. Not the overall approved-to-total ratio — that is a different number |
| CITL coverage | required vs recorded checkpoints per artifact (see model below) |
| AI usage | tokens per provider/model, `duration_seconds` and generation count per level |

## Data limits

The manifests deliberately exclude gates, tests, Delivery Flow, deployments and cost
(§3.12). A report states those limits instead of inventing numbers.

**CITL coverage model:** per TASK, count as *required* the §3.0/§3.12
checkpoints — base (`CP-TASK-READY-Approval`, `CP-TASK-DONE-Approval`),
type origin (`CP-US-Approval` for functional, `CP-TC-Approval` for test),
`CP-BUG-Approval` when the TASK's sources reference a BUG, plus **one
decision per SPEC revision** and **one per Delivery Loop/MEM** — and as *recorded*
the decisions actually present, matched by `subject.revision` /
`subject.delivery_loop`. US and TC manifests count their own single origin
decision. The percentage is required-vs-recorded; review *quality* (findings,
evidence) is not measured here — it lives in the governed artifacts (§3.0).

**And it is narrower than the metric it is named after.** §3.7.3's CITL
Coverage also requires `CP-ADR-Approval` for **every applicable ADR** and
every conditional DISC/REV checkpoint linked to the TASK — approvals that
live in those artifacts and never in the TASK manifest (§3.12), which is why
§3.7.3 has its collector join the governed artifacts by ID and checkpoint.
A report built from the manifest family alone therefore cannot see them, and
would read 100% while an applicable ADR sits unapproved. Label the number for
what it is — **manifest-recorded checkpoint coverage** — and state the
exclusion beside it, exactly as this folder states the gate, Delivery Flow and cost
limits. Reporting it as §3.7.3 CITL Coverage without that join is the same
class of error as reporting TASK lead time as Delivery Flow D2 (W16).

Two rules any future implementation must respect, both learned the hard way:
`checkpoint_approvals[]` is append-only, so the **latest** decision for a checkpoint
governs, never the first (§3.12); and a repository holds a single manifest
family, so a manifest declaring another `schema_version` is an unfinished
migration (§5.16) — the report says so rather than aggregating it (§3.12).

---

## Language

IDs and the fixed `REPORT-YYYY-Www` filename pattern stay in English. The
report's prose (headers, labels, tooltips) follows the project's
`content_language` (§3.15) — the template ships in English and can be
localized per project.
