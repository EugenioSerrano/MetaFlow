---
id: "MEM-260824-0105"
title: "The agents/ examples–squad split — shipped references vs the project's live agents (US-023.BOLT-005, V-Bounce 1)"
date: "2026-08-24"
author: "eugenio.serrano"
llm: "claude-fable-5"
bolt: "US-023.BOLT-005"
spec: "devflow/spec/SPEC-260824-0050-agents-examples-squad-split.md"
spec_revision: 1
v_bounce: 1
execution_outcome: "ready_for_review"
baseline: "7e3eb5e"
applied_adrs:
  - "devflow/adrs/ADR-013-agent-lifecycle-governance.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
manifest: "devflow/metrics/bolts/US-023.BOLT-005-agents-examples-squad-split.json"
diff_ref: ""
review_ready_at: "2026-08-24T01:05:15-03:00"
review: # AITL-MEM-Approval — the go-ahead given in conversation (the forwarded cross-model PASS verdict) and transcribed by the agent (§3.0)
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-24T01:11:07-03:00"
  decided_at: "2026-08-24T01:11:07-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved as Dev-validator with an independent cross-model verification of the package against the disk (PASS on every checklist item): the exact target shape, AC-1/2/3 with the 4-hit sweep (1 fixed in scope — the TEMPLATE-new-role path + the tools/agent-wrappers self-containment leak; 3 allowlisted with owner SPEC-260824-0054 Phase A), byte-identical git renames, the two rule-stating READMEs, the rebuilt two-table INDEX, self-containment 0 hits, no BOM, manifest v_bounces[1] complete. Reviewer reminder carried forward: the 0054 V-Bounce must verify the 3 allowlisted roles/ fixes explicitly (its sweep pattern gains roles/) and record them in its MEM. V-Bounce 1 approved — BOLT-005 Development Completed."
---

# MEM-260824-0105 — The `agents/` examples–squad split (US-023.BOLT-005, V-Bounce 1)

| Field           | Value |
|-----------------|-------|
| **Bolt**        | US-023.BOLT-005 (agents-examples-squad-split) |
| **SPEC**        | [SPEC-260824-0050](../spec/SPEC-260824-0050-agents-examples-squad-split.md) rev 1 |
| **V-Bounce**    | 1 |
| **ADRs**        | ADR-013 (§3.9 examples–squad ship model, §3.5 bounds), ADR-004 (kit-only) |

---

## 1. Executive summary

This V-Bounce delivered the `agents/` family split fixed by ADR-013 §3.9:
the five shipped role definitions moved **byte-identical** (git renames —
history preserved) from `roles/` into **`agents/examples/`**, now
explicitly **read-only references** (a thin `examples/README.md` states
the rule: copied, never edited in place, never referenced by the roster,
never installed); a new **`agents/squad/`** was created as the project's
**live workspace** (its README states the mirror rule: the Coordinator
writes here, it is the only folder the roster's `definition:` pointers
reference, and it ships empty — the kit delivers no live agents);
`TEMPLATE-new-role/` moved to the family root (mirroring `actors/`'s
root-level template); and `roles/README.md`'s content — the definition
contract table, the security rules, producer-first, the two-sides table
and the create-your-own-agent guide — was **absorbed into
`agents/README.md`**, with only the copy-destination paths updated
(`roles/<your-role>/` → `squad/<your-role>/`) and the governance wording
carried **as-is** (its enablement references are rewritten by the next
V-Bounce, SPEC-260824-0054, in this — their final — home, per the F3
sequencing). `agents/INDEX.md` was rebuilt with the two-table shape:
**Examples (shipped)** and **Squad (live)**. The kit-wide `roles/` path
sweep ends **clean**: the only remaining hits are the three `actors/`-family
files explicitly owned by SPEC-260824-0054 Phase A (allowlisted). One
finding beyond the plan: `TEMPLATE-new-role/agent.yaml`'s header still
referenced the maintainer-only `tools/agent-wrappers` generator — a
self-containment leak the earlier alignment missed — fixed together with
its `roles/` path (the Coordinator + VERIFICATION.md mapping is now the
stated projection path). Verification is GREEN: exact target shape,
0 in-scope stale paths, self-containment 0 hits, no BOM.

## 2. Implemented phases

### Phase A — The structural split

The five role folders → `examples/` (git mv, content untouched);
`TEMPLATE-new-role/` → the family root; `squad/` created with its README;
`examples/README.md` created (the copy-never-edit rule);
`roles/README.md` absorbed into `agents/README.md` and removed (with it,
the `roles/` folder).

### Phase B — References

`agents/README.md` rewritten as the family's single reference: what lives
here (examples/ · squad/ · TEMPLATE-new-role/ · INDEX · VERIFICATION), the
Coordinator section, the absorbed definition contract + security rules +
producer-first + two-sides + create-guide (steps now target `squad/`), and
the Rules section (wrappers projected from `squad/`). `agents/INDEX.md`
rebuilt: Examples table (shipped, read-only note) + Squad table (empty,
with the how-it-grows note) + Coordinator + Notes. `VERIFICATION.md`
needed no change (0 `roles/` references — verified).

### Phase C — Sweep + verification (GREEN)

Kit-wide `roles/` path sweep → 4 hits: 3 in `actors/`
(`example.yaml` pointer, `INDEX.md` row, `TEMPLATE-ACTOR.yaml`
placeholder) **allowlisted — owned by SPEC-260824-0054 Phase A** (the
actors/ reshape); 1 in `agents/TEMPLATE-new-role/agent.yaml` — in scope,
fixed (path → `squad/`, plus the `tools/agent-wrappers` self-containment
leak found next to it). Final state verified: shape exact, self-containment
0 hits over the changed files, no BOM, git renames (R) preserved.

## 3. Files created

| File | Purpose |
|------|---------|
| `distribution-kit/devflow/agents/examples/README.md` | The read-only-reference rules at the point of reading (copy, never edit in place, never roster-referenced, never installed) |
| `distribution-kit/devflow/agents/squad/README.md` | The live-workspace rules (the Coordinator writes here; the only roster-referenced folder; ships empty; same contract) |

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `distribution-kit/devflow/agents/README.md` | Rewritten as the family's single reference — absorbed the definition contract, security rules, producer-first and create-guide from the removed `roles/README.md`; paths now target `squad/`; governance wording carried as-is for SPEC-260824-0054 to rewrite |
| `distribution-kit/devflow/agents/INDEX.md` | Rebuilt with the Examples (shipped) + Squad (live) tables and the projected-from-squad wording |
| `distribution-kit/devflow/agents/TEMPLATE-new-role/agent.yaml` | Header: copy destination → `agents/squad/<your-role>/`; the maintainer-only `tools/agent-wrappers` reference (self-containment leak) → the Coordinator + `agents/VERIFICATION.md` mapping |

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
| `agents/roles/{architect,developer,functional-analyst,qa,reviewer}/` (×5, agent.yaml + prompt.md each) | `agents/examples/<same>/` | The split — shipped definitions become read-only references (byte-identical moves, git history preserved) |
| `agents/roles/TEMPLATE-new-role/` | `agents/TEMPLATE-new-role/` | The generic template at the family root, mirroring `actors/` |

## 6. Files deleted

| File | Reason |
|------|--------|
| `distribution-kit/devflow/agents/roles/README.md` (and with it the `roles/` folder) | Content absorbed into `agents/README.md`; the folder's two concerns now have their own homes (`examples/`, `squad/`) |

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| The five definitions moved byte-identical (no rewrite) | The SPEC's separation of concerns: this Bolt is structure; the enablement wording belongs to SPEC-260824-0054 |
| The governance table + step 6 carried as-is (old AITL-enable wording) | Rewritten by SPEC-260824-0054 in this, their final, home — avoids editing the same text twice (F3 sequencing) |
| The `tools/agent-wrappers` reference fixed although not in the plan | Found adjacent to the in-scope path fix; it is a self-containment leak (maintainer-partition reference in a kit file) — fixing it is this Bolt's self-containment evidence, recorded here |
| The 3 `actors/` sweep hits allowlisted, not fixed | They belong to SPEC-260824-0054 Phase A (the actors/ reshape owns those files) — fixing them here would cross Bolt scopes |
| An extra stale phrase observed, left for 0054 | `agents/README.md`'s governance table row 1 still says "run the generator" (pre-ship-model wording) — it sits in the exact table SPEC-260824-0054 Phase C rewrites; noted so its V-Bounce catches it |

## 8. Deviations and assumptions

One addition beyond the SPEC's file list (the `tools/agent-wrappers` fix,
recorded above — same file the SPEC already touched, and required by the
self-containment evidence). No other deviations from SPEC-260824-0050
rev 1. Assumption: none — every governed source was approved before
execution.

## 9. Verification evidence

### Shape (RED → GREEN)

```
RED:   agents/ = README · INDEX · VERIFICATION · roles/{README, TEMPLATE-new-role,
       architect, developer, functional-analyst, qa, reviewer}
GREEN: agents/ = README · INDEX · VERIFICATION · TEMPLATE-new-role/ ·
       examples/{README, architect, developer, functional-analyst, qa, reviewer} ·
       squad/{README}          — roles/ no longer exists
```

### Sweep (AC-3)

```
kit-wide grep "roles/" (path family) → 4 hits:
  actors/example.yaml:14        ALLOWLISTED — SPEC-260824-0054 Phase A
  actors/INDEX.md:15            ALLOWLISTED — SPEC-260824-0054 Phase A
  actors/TEMPLATE-ACTOR.yaml:29 ALLOWLISTED — SPEC-260824-0054 Phase A
  agents/TEMPLATE-new-role/agent.yaml:3 → FIXED (in scope)
post-fix in-scope hits: 0
```

### Invariants

```
Self-containment (changed files): grep maintenance IDs + tools/agent-wrappers → 0 hits  PASS
Encoding: no BOM                                                                        PASS
Kit-only (ADR-004): only distribution-kit/devflow/agents/** changed                     PASS
Git: 12 renames (R) + 1 rename-modified (RM) + 1 delete + 2 new READMEs                 PASS
```

### Gates

Documentation/structure Bolt: unit/integration/perf `n/a` (no runtime
surface, per the approved SPEC §9); prompt-injection/secret-leak `pass`
(reviewed content, no injected instructions, no secrets);
hallucination-lint `pass` (every referenced path resolves);
behavioral-reproducibility `pass` (the shape/sweep checks re-run
identically); bolt-manifest-validation `pass` (v_bounces[1] appended,
schema PASS).

## 10. Manual interventions

None — the agent produced everything.

## 11. Evidence links

- **Diff / PR:** none (working tree, uncommitted — part of the v5.1 batch)
- **Commit:** baseline `7e3eb5e`
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-023.BOLT-005-agents-examples-squad-split.json`

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~10min |
| V-Bounce number | 1 |
| Tests created | 0 (documentation/structure; scripted evidence per SPEC §8) |
| AI-generated code | 100% |
| First-pass approval | pending (this MEM) |

## 13. Pending items and stubs

- [ ] SPEC-260824-0054's V-Bounce (US-024.BOLT-004) — executes after this
      MEM's approval: the actors/ reshape (fixes the 3 allowlisted
      pointers) + the enablement wording (rewrites the carried governance
      table, including its stale "run the generator" phrase) + the four
      MainAgents clause.
- [ ] O-2 (`model: inherit` semantics — definition default vs session
      model) — undecided, routed to US-025; never assumed (§2.4.1).
- [ ] AITL-BOLT-DONE-Approval for this Bolt after the MEM approval.

## 14. AITL-MEM-Approval

> **Avenga DevFlow §2.12, §3.0.** This MEM is created by the agent with no
> mutable status and is **never self-approved**. A qualified human (the
> Dev-validator who executed the Bolt) inspects the actual diff,
> test/gate evidence, MEM and manifest, and records `AITL-MEM-Approval`
> here and in the manifest's `checkpoint_approvals[]`.

| Field | Value |
|-------|-------|
| **Reviewers (executing Dev-validator)** | `human:eugenio.serrano` |
| **Roles** | dev_validator |
| **Decision** | **approved** |
| **review_ready_at** | `2026-08-24T01:05:15-03:00` |
| **review.started_at** | `2026-08-24T01:11:07-03:00` |
| **review.decided_at** | `2026-08-24T01:11:07-03:00` |
| **Review evidence** | the git renames + the 3 doc rewrites + 2 new READMEs; the shape listing; the sweep with its allowlist; self-containment; MEM, manifest |
| **Comments** | |
| **Findings** | |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | evidence inspected per the review-evidence column |
