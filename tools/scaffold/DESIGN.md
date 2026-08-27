# scaffold — create an artifact and its manifest, correctly, in one step

**Status:** specification. Highest leverage after the validator.

## The problem

Creating one governed artifact today costs an agent: read the folder README,
read the `TEMPLATE-*`, read the INDEX to find the next number, read the routing
table to place the file, read the matching `TEMPLATE-MANIFEST-*.json`, then
write two files with consistent frontmatter. Every artifact, every time.

And **G33** makes the paired manifest mandatory — *"an artifact without its
manifest does not exist"* — which means the expensive second half is exactly
the half most likely to be skipped under pressure.

## What it does

```
devflow new bug   --title "Race condition on invoice download"
devflow new bolt  --parent US-012 --type functional
devflow new tc    --source-bolt US-012.BOLT-003
devflow new spec  --bolt US-012.BOLT-003
```

For each, it **prints** two things: the filled document and — for a US, Bolt or
TC — its paired manifest, each with the path it belongs at per §5.15. The agent
writes both. The tool touches nothing.

What it fills is **only the mechanically derivable frontmatter**: `id` from
`next-id`, `author` from `identity`, `date` and any timestamp from `clock`,
`llm` from the caller, plus the manifest's origin decisions that already exist
at that moment.

**That makes G33 practically unbreakable**: the manifest arrives in the same
output as the document, so forgetting it takes deliberate effort rather than a
lapse of attention.

## Boundaries

- **Writes nothing.** It emits text; the agent creates the files.
- Fills what is derivable. It leaves every prose field, every `status` beyond
  the template default, and the entire `review:` block **empty** — those are
  authorship and judgement, not derivation.
- Never sets an approval, a decision or a `decided_at`.
- **Refuses when the parent is not approved.** Creating a functional Bolt under
  a draft US is G01; a Test Bolt under a draft TC is G03. The tool should not
  be the thing that makes a blocking violation convenient.

## The INDEX row

It emits that too — the row for the new artifact, ready to be placed in the
folder's `INDEX.md`. The agent adds it in the same pass that creates the files,
so nothing is left stale, and `indexer --check` remains the safety net that
catches whatever bypassed the tool entirely.
