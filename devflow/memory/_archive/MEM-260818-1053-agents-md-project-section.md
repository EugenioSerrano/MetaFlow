---
id: "MEM-260818-1053"
title: "The install step no longer destroys the project section, and no framework text is stranded"
date: "2026-08-18"
author: "eugenio.serrano"
llm: "claude-opus-5[1m]"
bolt: "US-000.BOLT-001"
spec: "SPEC-260817-2110"
spec_revision: 2
v_bounce: 2
execution_outcome: "ready_for_review"
baseline: "67a62ed"
applied_adrs:
  - "devflow/adrs/ADR-001-repository-layout-methodology-and-product.md"
manifest: "US-000.BOLT-001-agents-md-project-section.json"
diff_ref: ""
review_ready_at: "2026-08-18T10:53:55-03:00"
review: # HITL-MEM-Approval — filled by the human reviewer (§3.0)
  decision: "approved"
  reviewers:
    - user: "eugenio.serrano"
      role: "dev_validator"
  started_at: "2026-08-18T10:53:55-03:00"
  decided_at: "2026-08-18T10:57:38-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Inspected the diff of the shipped AGENTS.md, §5.16, G36, the four agent definitions and this repository's own file; the §9 verification output; and the two-path rehearsal. The five findings raised against V-Bounce 1 are each applied and each verified: the token is now the last line so the distributed project section is empty by construction, the handoff is an instruction, the compaction-proof paragraph opens the project section, the install step excludes AGENTS.md with commit-recovery named as the fallback, and the committed-tree precondition is normative. Both migration paths converge to the same file and each is idempotent. No findings."
---

# MEM-260818-1053 — The install step no longer destroys the project section, and no framework text is stranded

| Field           | Value |
|-----------------|-------|
| **Bolt**        | [US-000.BOLT-001](../functional/bolts/US-000.BOLT-001-agents-md-project-section.md) |
| **SPEC**        | [SPEC-260817-2110](../spec/SPEC-260817-2110-agents-md-project-section.md), **revision 2** |
| **V-Bounce**    | 2 |
| **ADRs**        | [ADR-001](../adrs/ADR-001-repository-layout-methodology-and-product.md) — rules 6 and 7 |

---

## 1. Executive summary

This V-Bounce applied the five findings recorded against V-Bounce 1, one of
which changed the design rather than the wording and is what forced SPEC
revision 2 under G15. Revision 1 protected the project section by *recovering*
it from the last commit after the install copy had already destroyed it; the
guarantee therefore rested entirely on the human having committed at exactly
the right moment. Revision 2 makes the install step **exclude `AGENTS.md` from
the copy**, so the file is never destroyed and the merge happens in place, with
recovery from the last commit demoted to an explicitly named fallback for the
project that copies everything anyway. Both paths stay documented, with the
hierarchy stated in the same paragraph, and the precondition the methodology had
never declared — the working tree must be committed before a migration runs — is
now normative rather than assumed.

The other four findings were corrections to the previous V-Bounce's own output.
The marker's explanatory comment had been placed *below* the token, which
stranded 244 bytes of framework text on the project side — the same defect class
this Bolt exists to eliminate, reintroduced at smaller scale by the fix itself.
The explanation now sits above the token, the token is the **last line** of the
shipped file, and the distributed project section is empty by construction, so
no future release can find its own text frozen. The handoff into the project
section was rewritten from a courtesy note into an instruction that explicitly
authorizes the project section to qualify anything above it, including the
source-of-truth line. And this repository's project section now opens with a
compaction-proof paragraph carrying the one fact that must never be lost: the
product is `distribution-kit/`, `tools/` and `prompts/`; the root `devflow/` is
the installed rulebook and is not edited.

All ten acceptance criteria pass, including the two added in revision 2. The
rehearsal was extended to exercise **both** migration paths on a scratch git
repository: the prescribed one never loses the section at any point, the
fallback recovers it byte-identically after a blunt copy destroys it, each is
idempotent under re-application, and — the result worth having — **both
converge to the same file**. AC-2 was also rewritten to verify the general
property instead of one named paragraph, which is the verification gap that let
finding 1 through in the first place.

---

## 2. Implemented phases

### Phase A — Marker order and a hard handoff (findings 1 and 2)

The shipped `AGENTS.md` now ends with the bare token line. The human-facing
explanation of the contract moved above it, onto the framework side, so a future
release that improves that wording reaches every adopter instead of being
frozen out by the very boundary it describes. The merge still matches the token
as a prefix, so the token line's own trailing text can vary without breaking
projects already carrying it.

The handoff changed register. It previously said the project section is binding,
which reads as a note about conventions. It now instructs the reader that the
framework block is the methodology's *default*, that the project section may add
constraints, name which tree is the one to edit, or qualify any statement above
it — the source-of-truth line included — and that where the two appear to
disagree about *this* repository, the project section is the one that knows
where it is. The text stays generic, so every adopter receives the same
protection against the failure mode this repository exhibits most sharply.

### Phase B — The install step stops destroying the file (findings 4 and 5)

§5.16 now prescribes three things in order of precedence. The install copy
**excludes `AGENTS.md`** and the new framework block is merged into it in place,
so nothing the project authored is destroyed at any point. Recovery from the
last commit is named explicitly as the **fallback** — it exists because copying
everything is the natural thing to do and that copy will happen, not because it
is the intended route. And the precondition is declared: the working tree is
committed before a migration runs, because the fallback reads from the last
commit and a project that never committed its section has nothing there to
recover.

That ordering matters more than either path alone. Revision 1 documented only
the recovery, which made a human's timing part of the guarantee; a reader could
follow it correctly and still lose everything by having skipped a commit nobody
told them was mandatory.

### Phase C — Enforcement follows the new hierarchy

G36's response text was rewritten to name the exclusion first and the
commit-recovery second, so an agent reading the blocking rule gets the same
precedence as one reading the methodology. The rule count stays at 39.

### Phase D — The four agent definitions, in one synchronized pass

The shared migration bullet was rewritten in all four with the new ordering:
exclude from the copy, merge in place, fall back to the last commit if a blunt
copy already overwrote it, and stop when the marker is missing or duplicated.
Byte-identical across the four, verified by the whole-body diff.

### Phase E — This repository's own file (finding 3)

Recomposed against the new kit file, so the framework block stays byte-identical
by construction. The project section now opens, before any heading, with the
compaction-proof paragraph. The release loop was corrected in the same pass:
step 3 excludes `AGENTS.md` from the install and names the concrete command,
step 4 merges in place and points at the commit only as the fallback.

---

## 3. Files created

| File | Purpose |
|------|---------|
| `devflow/memory/MEM-260818-1053-agents-md-project-section.md` | This implementation memory — the V-Bounce 2 record. Same stable slug as V-Bounce 1's MEM per W06; only the timestamp differs |

---

## 4. Files modified

| File | Description of change |
|------|----------------------|
| `distribution-kit/AGENTS.md` | Marker explanation moved above the token; token is now the last line of the file; handoff rewritten as an instruction that authorizes the project section to qualify the framework block |
| `distribution-kit/devflow/avenga-devflow/Avenga-DevFlow.md` | §5.16: install-step exclusion as the prescribed path, commit-recovery named as the fallback, and the committed-tree precondition declared |
| `distribution-kit/devflow/GUARDRAILS.md` | G36 response reordered to match the new precedence |
| `distribution-kit/CLAUDE.md` | Shared migration bullet rewritten with the new ordering |
| `distribution-kit/.agents/skills/avenga-devflow/SKILL.md` | Same, verbatim |
| `distribution-kit/.github/agents/AvengaDevFlow.agent.md` | Same, verbatim |
| `distribution-kit/.opencode/agents/AvengaDevFlow.md` | Same, verbatim |
| `AGENTS.md` (root) | Recomposed against the new kit block; compaction-proof paragraph opening the project section; release loop steps 3 and 4 corrected |
| `devflow/spec/SPEC-260817-2110-agents-md-project-section.md` | Revision 2 in place (G12): scope, Phase A.2/A.3, new Phase B.4, Phase E, AC-2 generalized, AC-9 and AC-10 added, decisions, risks, revision history |
| `devflow/metrics/bolts/US-000.BOLT-001-agents-md-project-section.json` | `spec_revisions[1]`, the V-Bounce 1 MEM decision, the revision 2 SPEC approval, and this V-Bounce entry |

---

## 5. Files renamed

| File | New name | Reason |
|------|----------|--------|
| — | — | None |

---

## 6. Files deleted

| File | Reason |
|------|--------|
| — | None |

---

## 7. Implementation decisions

| Decision | Reason |
|----------|--------|
| Keep **both** migration paths documented rather than replacing one with the other | A project that copies everything will exist regardless of what the procedure says; deleting the recovery path would leave that project with no route at all. Naming one prescribed and the other a fallback gives precedence without removing the safety net |
| State the precedence **in the same paragraph**, not in separate sections | Two procedures described apart read as alternatives of equal standing; the risk register records this and the mitigation is proximity |
| Token as the **last line**, explanation above it | Makes the distributed project section empty by construction, which is a stronger guarantee than a rule saying it should be empty. AC-2 can then verify the property rather than an instance |
| Rewrite AC-2 to check the general property | The original AC verified one named paragraph and therefore could not catch the marker's own comment. The finding was in the verification before it was in the artifact |
| Recompose the root file rather than patch it | Same reason as V-Bounce 1: byte-identity of the framework block stays true by construction, and it now also absorbs the kit's changes automatically |
| Extend the rehearsal to both paths and assert they **converge** | Equivalence of outcome is the property that makes the fallback safe to keep. Testing each in isolation would have missed a divergence between them |

---

## 8. Deviations and assumptions

**No deviations from SPEC revision 2.** Every phase landed as specified.

**Assumption carried forward from V-Bounce 1** and re-verified: the adoption
command in the root `README.md` still tells a new adopter to copy everything,
which remains correct for a **fresh install** where no project `AGENTS.md`
exists. The exclusion applies to the *upgrade* path only. Left unchanged
deliberately.

**Observation, not a deviation.** Finding 1 was a defect introduced by the
previous V-Bounce's own fix, and finding 5 was a gap the previous V-Bounce
depended on without noticing. Both were found by the human tracing the merge
byte by byte during review, not by the automated checks — which is the argument
for the review budget existing at all.

**No unresolved risks** carried out of this V-Bounce.

---

## 9. Verification evidence

### Build

```
n/a — no runtime and no build. Verification is the deterministic command set below.
```

### Tests

```
AC-1   token present in the shipped file ......................... 1              PASS
AC-2   token is the LAST line (65 of 65); content after it: ''     empty          PASS
       → the distributed project section is empty by construction, not by rule
AC-3   §5.16 "is merged, never replaced" ......................... 1              PASS
AC-4   G36 covers overwriting the project section ................ 1              PASS
       total G rules (unchanged) ................................. 39             PASS
AC-5   shared-body diff vs claude:  codex 2 | gh 2 | opencode 2 lines             PASS
       G-rule count inline: 39/39 | 39/39 | 39/39 | 39/39                         PASS
AC-6   old Claude "this file (CLAUDE.md...)" phrasing ............ 0              PASS
AC-7   framework block root vs kit ............... identical, 3350 bytes          PASS
AC-9   install-exclusion present:  §5.16 1 | G36 1 | agents 4/4                   PASS
AC-10  committed-tree precondition in the normative text ......... 1              PASS
```

### Migration rehearsal (AC-8) — both paths, scratch git repository

```
RUTA PRESCRITA — the install excludes AGENTS.md
   after install:      project section present? ......... YES  (never destroyed)
   after in-place merge: framework 4.3 OK | section intact: YES
   idempotent:                                             YES

RUTA FALLBACK — everything copied anyway, file clobbered
   after cp -a:        project section present? ......... NO — CLOBBERED
   after recovery from HEAD: framework 4.3 OK | recovered: YES
   idempotent:                                             YES

   both paths converge to the SAME file:                   YES

AC-8: PASS
```

### Boundary cases

Unchanged from V-Bounce 1 and re-exercised by the merge function used above:
missing marker on either side and a duplicated marker each return `STOP`; an
empty project section and CRLF input merge correctly.

### Gates

| Gate | Result |
|------|--------|
| Unit / integration | `n/a` — no executable code in scope |
| SAST / SBOM | `n/a` — no code, no dependencies |
| Perf-smoke | `n/a` — documentation change |
| Prompt-injection scan | `pass` — all text authored here |
| Secret-leak scan | `pass` |
| Hallucination lint | `pass` — §5.2, §5.16, G07, G12, G15, G16, G36 and W06 all resolve on disk |
| IP / license provenance | `n/a` |
| PII / DLP | `n/a` — `internal`, no personal data |
| Dependency-confusion | `n/a` |
| Test-first evidence | `n/a` — not a BUG Bolt |
| Behavioral reproducibility | `pass` — both paths idempotent and convergent |
| Bolt-manifest validation | `pass` — 0 errors against `manifest-v4-bolt.schema.json` |

---

## 10. Manual interventions

None.

---

## 11. Evidence links

- **Diff / PR:** none — nothing staged or committed (G34)
- **Commit:** baseline `67a62ed` on branch `4.2`, plus the uncommitted working tree
- **Cumulative Bolt manifest:** `devflow/metrics/bolts/US-000.BOLT-001-agents-md-project-section.json`
- **Previous V-Bounce:** [MEM-260817-2123](MEM-260817-2123-agents-md-project-section.md) — immutable history, `changes_requested` with the five findings this V-Bounce applied

---

## 12. Metrics

| Metric | Value |
|--------|-------|
| AI generation time | ~15 min (10:38 → 10:53 local), including SPEC revision 2 |
| V-Bounce number | 2 |
| Tests created | n/a — 10 acceptance criteria, ~20 deterministic checks, a 2-path × 2-pass rehearsal |
| AI-generated code | 100% — no human fallback |
| First-pass approval | no — V-Bounce 1 returned `changes_requested` with 5 findings |

---

## 13. Pending items and stubs

- [ ] `HITL-BOLT-DONE-Approval` — acceptance routes to Tech Lead + Security (`work_category: hardening`, §3.11)
- [ ] The **G29 solo-maintainer finding** — still unopened; needs its own `OQ-NNN` or retro entry
- [ ] A `tools/` checker for the framework-block byte-identity invariant, out of this Bolt's scope
- [ ] The release migration of this repository, the first real execution of §5.16
- [ ] **28+ uncommitted entries in the working tree** — the only copy of everything above, and the precondition this V-Bounce just made normative

---

## 14. HITL-MEM-Approval

> **Avenga DevFlow §2.12, §3.0.** Created by the agent, never self-approved.
> `risk_class: medium` requires 1 approver: the Dev-validator who executed the
> Bolt (§3.3).

| Field | Value |
|-------|-------|
| **Reviewers (executing Dev-validator)** | eugenio.serrano |
| **Roles** | dev_validator |
| **Decision** | approved |
| **review_ready_at** | `2026-08-18T10:53:55-03:00` |
| **review.started_at** | `2026-08-18T10:53:55-03:00` |
| **review.decided_at** | `2026-08-18T10:57:38-03:00` |
| **Review evidence** | Diff of the shipped `AGENTS.md`, §5.16, G36, the four agent definitions and the root file; §9 verification output; the two-path migration rehearsal |
| **Comments** | All five findings from V-Bounce 1 applied and verified. Both migration paths converge and are idempotent. |
| **Findings** | none |
| **acknowledged_without_comment** | true |
| **acknowledgment_reason** | recorded in the frontmatter `review:` block |
