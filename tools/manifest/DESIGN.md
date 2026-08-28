# manifest — append to the manifest family without breaking it

**Status:** specification.

## The problem

The manifest family has three constraints that a hand edit breaks easily:

- **Append-only.** `spec_revisions[]`, `v_bounces[]` and `hitl_approvals[]` are
  never rewritten; corrections are new entries (§3.12).
- **Monotonic timestamps.** `created_at ≤ review_ready_at ≤ review_started_at ≤
  decided_at`, which §3.12 explicitly says *"no JSON Schema can express"*.
- **Three different shapes.** Bolt, US and TC manifests share `schema_version`
  and `hitl_approvals[]` and nothing else; every schema is
  `additionalProperties: false`, so a missing field and an extra field both
  fail validation (G23).

An agent editing JSON by hand can violate all three and only find out at
validation time — or never, while no validator ships (the tools track
delivers it; `metaflow/bin/` is already part of the canonical tree, §5.1).

## What it does

```
metaflow manifest ready      --ref <artifact>
metaflow manifest started    --ref <artifact>
metaflow manifest approval   --checkpoint HITL-MEM-Approval --v-bounce 2
                            --decision approved --by user:role
metaflow manifest spec-rev   --bolt US-012.BOLT-003 --ref <spec> --sources ...
metaflow manifest vbounce    --bolt US-012.BOLT-003 --spec-revision 2
                            --outcome ready_for_review --mem <ref>
```

Every command **prints the complete updated manifest** to stdout, already
validated against its schema and already checked for monotonicity and ordering.
The agent writes the file. The tool opens the manifest to read it and never to
change it.

That split is what makes the guarantee real: the agent receives a document that
is known-valid, and every byte of it is visible in the diff the human reviews.

## Boundaries

- **Writes nothing to disk.** It emits the updated JSON; the agent saves it.
- Appends. Never rewrites an existing entry, never reorders, never deletes.
- **Never records a decision nobody made.** `approval` requires the decider and
  the decision as explicit input; the tool supplies only `decided_at`, from the
  clock, at the moment the human actually decides. A tool that could invent an
  approval would defeat the entire methodology.
- Refuses a manifest whose `schema_version` is not the current family. A
  repository holds exactly one (§3.12), so an older one means the version
  migration never finished; appending a lifecycle entry would bury that instead
  of surfacing it (§5.16). Converting it forward is the migration's job, not
  this tool's.

## Open note

Token counts and `duration_seconds` come from the agent's own telemetry — the
tool cannot observe them. They are inputs, and when they are unavailable the
tool writes `null`, which the schema already permits, rather than estimate a
value. §3.12 is explicit: *"Token values are provider-reported values, never
estimates."*
