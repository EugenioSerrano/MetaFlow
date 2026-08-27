# clock — repository time, not developer time

**Status:** specification. Requires a methodology change (see below).

## The problem

W04 forbids inventing a timestamp. §3.12 requires RFC 3339 with seconds and a
zone designator. And the naming rules say something sharper about `SPEC-` and
`MEM-` filenames:

> The `HHmm` of N05/N06 is a **local wall-clock time with no offset**, and must
> be read in the same UTC offset as the artifact's own `generation.created_at`
> — otherwise the alphabetical order of SPEC/MEM filenames stops matching their
> chronological order across time zones.

The methodology already identifies the failure and solves it by **convention**.
With developers in different zones, convention breaks quietly: two MEMs of the
same Bolt sort in the wrong order and nothing complains. `spec/` and `memory/`
have no INDEX precisely because the timestamp *is* the ordering — so when the
offset drifts, the ordering guarantee drifts with it.

## The proposal: `devflow/LOCATION`

A file beside `devflow/LANGUAGE`, holding the project's canonical time zone.
**An IANA zone name, not a fixed offset:**

```
America/Argentina/Buenos_Aires
```

`GMT-3` looks simpler and is wrong: a fixed offset cannot express daylight
saving, so any project in a DST zone gets an hour of misordered filenames twice
a year, every year. The IANA database handles it; a hand-written offset cannot.

Every timestamp written into the repository is then rendered in that zone,
whatever zone the developer happens to sit in.

## What it does

```
devflow now                    -> 260816-1432          (filename stamp, repo zone)
devflow now --rfc3339          -> 2026-08-16T14:32:07-03:00
devflow now --date             -> 2026-08-16
```

## Boundaries

- Always the system clock, converted. It never accepts a supplied time — that
  would reintroduce exactly what W04 forbids.
- Never backdates. §3.12: timestamps are *"written once, in order — never
  invented, never backdated"*.

## Methodology change required

`LOCATION` does not exist yet. Introducing it touches three places:

- **§5.3** — the `devflow/` root files table, beside `VERSION` and `LANGUAGE`.
- **The naming rules**, which today describe the offset problem as a convention
  to be respected rather than a value to be read.
- **§5.16** — the migration must add it to the **single exception** beside
  `LANGUAGE`: an upgrade keeps the project's zone, never the template's.
