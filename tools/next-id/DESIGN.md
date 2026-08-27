# next-id — the next free sequential number

**Status:** specification.

## The problem

Sequential `NNN` identifiers are claimed against each folder's `INDEX.md`
(§5.15). §2.4 adds two rules that are easy to break by hand:

- **Numbers are never reused.** A rejected, deprecated or superseded artifact
  leaves a gap in the sequence of its parent.
- **Gaps are normal and must not be filled.**

Bolt numbering is scoped to its direct parent — `US-000` carries the shared
sequence for every non-functional Bolt of the project — and widens to four
digits past 999. An agent doing this by hand reads the INDEX, parses every row,
sorts, and hopes.

## What it does

```
devflow next-id BUG                      -> BUG-004
devflow next-id BOLT --parent US-012     -> US-012.BOLT-005
devflow next-id BOLT --parent US-000     -> US-000.BOLT-1003
devflow next-id TC                       -> TC-028
```

**Two sources, cross-checked.** The INDEX is where the number is claimed, but
the filesystem is what actually exists. If the highest ID in the INDEX and the
highest on disk disagree, that is a defect: report it rather than silently pick
one. That single check catches the most common drift in any folder — an
artifact created and never indexed.

## Boundaries

- Reports a number. It never creates the artifact and never writes the INDEX;
  `scaffold` does both.
- Never fills a gap, never reuses, never renumbers.

## Open decision

**Does it reserve the number?** Two agents on two branches asking at the same
moment both get `BUG-004`. Reserving means writing, which turns a read-only
tool into a writer of the file that also allocates IDs.

The alternative is to accept the collision and let it surface as a **merge
conflict in the INDEX** — which is precisely the behaviour §5.15 describes as
intended: *"an ID collision must be visible, never silent."* Leaning toward no
reservation, on the grounds that the methodology already chose this trade-off
deliberately.
