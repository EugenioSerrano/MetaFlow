---
id: "SPEC-260824-1101"
title: "The shared lifecycle body in the four MainAgents — the section text, the shared-body cleanup and the byte-sync propagation"
date: "2026-08-24"
author: "eugenio.serrano"
llm: "claude-fable-5"
status: "approved" # draft | approved | blocked | obsolete — AITL-SPEC-Approval 2026-08-24
origin: "US-025"
bolt: "US-025.BOLT-001"
revision: 1
associated_adrs:
  - "devflow/adrs/ADR-013-agent-lifecycle-governance.md"
  - "devflow/adrs/ADR-014-actors-roster-is-the-enablement.md"
  - "devflow/adrs/ADR-004-repository-partition-v2.md"
prerequisites: []
risk_class: "low"
autonomy_level: "L3" # low risk → L3 default (§3.3)
turn_budget: ""
data_classification: "internal"
review_ready_at: "2026-08-24T11:05:19-03:00"
review: # AITL-SPEC-Approval — decision dictated in conversation ("aprobado!") and transcribed by the agent (§3.0)
  decision: "approved" # approved | changes_requested | rejected
  reviewers:
    - actor: "human:eugenio.serrano"
      role: "dev_validator"
      model: null
  started_at: "2026-08-24T11:12:29-03:00"
  decided_at: "2026-08-24T11:12:29-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved as Dev-validator after an independent cross-model SPEC review (verdict: no blocking findings, recommend approval — the payload checked block by block against the real kit, the Phase B old->new strings verified exact on disk, the known-remainder enumeration matched reality hit by hit, every payload cross-reference glob-verified, and the §5.12 anchor confirmed as genuinely shipped kit text). Its four non-blocking observations were adopted pre-stamp in this same revision: (1) placement moved to immediately-before-##-Guardrails; (2) the signs/signs redundancy fixed (never approves its own routing); (3) the living-data anchor named precisely (§5.12 and the roster's living-data rule); (4) the pre-V-Bounce batch is committed first so v_bounces[].git_commit reflects a real baseline. Authorizes the V-Bounce (revision 1)."
---

# SPEC-260824-1101 — The shared lifecycle body in the four MainAgents

| Field | Value |
|-------|-------|
| **Origin** | US-025 (approved 2026-08-24) |
| **Bolt** | US-025.BOLT-001 (READY 2026-08-24, risk low) |
| **ADRs** | ADR-013 (lifecycle governance), ADR-014 (roster enablement), ADR-004 (kit-only) |
| **Risk Class** | low |
| **Revision** | 1 |

---

## 1. Objective

Add one **byte-identical lifecycle section** to the shared body of the
four MainAgents (kit `CLAUDE.md`,
`.agents/skills/avenga-devflow/SKILL.md`,
`.github/agents/AvengaDevFlow.agent.md`, `.opencode/agents/AvengaDevFlow.md`)
so the install/create/delete capability the adopter smoke test achieved by
model diligence (REV-005 C-01) becomes **contract** — identical wording on
every platform — and clean the shared body's pre-existing
maintenance-partition references in the same pass (US-025 AC-9). If not
implemented, every adopter's lifecycle depends on their model's willingness
to walk the family docs, and the quality varies by model.

## 2. Context

US-025 (approved) makes the Coordinator's lifecycle operational; ADR-013
governs it (executor = living data; approver = the human's roster act);
ADR-014 fixes the enablement. The four MainAgents already carry the
Coordinator identity and the enablement clause (delivered by
US-024.BOLT-004); what they lack is the **how-to-operate** text. This SPEC
adds it as one shared section — the payload is written out in Phase A so
the reviewer sees the exact words that will run inside four system prompts.

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | US-025.BOLT-001 | AITL-BOLT-READY-Approval ✓ (2026-08-24T11:01:48) |
| Feature US | US-025 | AITL-US-Approval ✓ (2026-08-24T00:40:35) |
| ADR | ADR-013 | AITL-ADR-Approval ✓ |
| ADR | ADR-014 | AITL-ADR-Approval ✓ |
| ADR | ADR-004 | AITL-ADR-Approval ✓ |
| REV evidence | REV-005 (C-01/C-02; F-05 context) | AITL-REV-Approval ✓ (2026-08-24T10:14:32) |
| Repository baseline | `bd43d8c` | — |

## 4. Scope

### In scope
- The new lifecycle section in the **shared body** of the four MainAgents
  (byte-identical; placed immediately after "The Coordinator (the
  orchestrator)" paragraph).
- The shared-body cleanup: the Coordinator paragraph's `ADR-008` and
  `US-023 AC-6` mentions → kit-internal wording (US-025 AC-9).

### Out of scope
- The per-platform preambles: their `ADR-007 §3.4` / `US-023 AC-6`
  references and the **stale pre-built-wrapper list**
  (`Agent(architect-agent, …)` in the Claude preamble) → **BOLT-002**.
- The kit GUARDRAILS G07 scoping text → **BOLT-005** (see §14 on the
  transient).
- Per-platform projection details, `inherit` handling, permission-set
  derivation → BOLT-002; delete-safe tooling depth → BOLT-003; the pilot →
  BOLT-004.

## 5. Prerequisites and baseline

- Baseline `bd43d8c` (everything committed; tree clean).
- The four MainAgents carry the enablement clause and the Coordinator
  paragraph (byte-sync verified in the BOLT-004 V-Bounce); `agents/squad/`
  and the reshaped `actors/` exist (BOLT-005/BOLT-004, Done).

## 6. Phases

### Phase A — The lifecycle section (the payload)

**Duration:** ~1.5h — **Complexity:** Low

Insert the following section (English — framework text) into the shared
body of the four files, **immediately before the "## Guardrails (MUST
enforce)" heading** (present in all four; this placement keeps the
"Reference documents" block outside the new section — reviewer
observation #1 adopted). Final wording may receive micro-edits at review;
the **content blocks are contractual**: the identity clause, the three
flows, the four governance rules.

> ## The agent lifecycle (you install, create and delete DevFlow Agents)
>
> **You are the MainAgent — AvengaDevFlow, one per tool — and the
> MainAgent IS the Coordinator.** Operating the project's squad is your
> capability, within these rules:
>
> - **Install** — take a live definition (`devflow/agents/squad/<id>/` —
>   `agent.yaml` + `prompt.md`), project it into THIS platform's wrapper
>   following the per-platform mapping in `devflow/agents/VERIFICATION.md`,
>   and place it in this tool's spawn folder (declared in your platform
>   preamble). Then tell the human to reload the session so the agent
>   registers. Never install from `agents/examples/` — an example is
>   copied into `squad/` first.
> - **Create** — on "create me a `<role>` agent": scaffold the definition
>   from `agents/TEMPLATE-new-role/` (or the closest `agents/examples/`
>   reference) into `agents/squad/<id>/` — **keep the definition
>   role-generic** (an actor's name or specific team members never enter
>   it; the charter prose follows the project's `content_language`).
>   Create the actor file (`devflow/actors/<id>.yaml`, from
>   `TEMPLATE-ACTOR.yaml`) and list it in `roster.yaml` as an
>   **executor-only draft** (`modes: [executor]`, `approves: []`); add it
>   to `agents/INDEX.md`; then install it. Remind the human: the authority
>   fields are THEIR configuration act, and their commit of the roster
>   change is the act's record.
> - **Delete** — check `roster.yaml` and the actor files first: a
>   definition referenced by any actor (N:1 reuse) is never broken. Remove
>   the wrapper from the spawn folder (and the `squad/` definition only
>   when unreferenced); keep the roster and `agents/INDEX.md` consistent.
>
> **Governance (non-negotiable):**
>
> - Executor install/create/delete is **living data** — operational
>   configuration of the same class as a roster update or a prompt
>   (§5.12 and the roster's living-data rule): no Bolt, no approval.
> - **Approver authority is the human's act**: you may scaffold and
>   propose, but `modes: [approver]` and a non-empty `approves` are
>   written by a human and recorded by their commit — you never enable
>   your own, or any agent's, approval authority.
> - **Installing never enables approval**: a wrapper in the spawn folder
>   grants nothing; only the schema-valid, human-authored roster entry
>   does. The safe default holds.
> - The lifecycle operates **only within the agent system**
>   (`devflow/agents/` + `devflow/actors/`); the kit's shipped examples
>   and templates are never edited in place.

**Files modified:** the four MainAgent files (one insertion each,
byte-identical).

### Phase B — The shared-body cleanup (US-025 AC-9)

**Duration:** ~20min — **Complexity:** Low

In the shared "The Coordinator (the orchestrator)" paragraph (present in
all four files, byte-identical):
- `(`approves: []`, ADR-008 separation of duties)` →
  `(`approves: []` — separation of duties: the router never approves its
  own routing)` (reviewer observation #2: avoids the signs/signs
  redundancy)
- the trailing `(US-023 AC-6)` → `(the spawn topology)`

The kit's own `US-000` references and the naming table's fictional example
ids (`US-012.BOLT-003-…`) are framework text — untouched.

### Phase C — Byte-sync propagation + verification

**Duration:** ~40min — **Complexity:** Low

Apply Phases A+B identically to the four files; then verify: (1) the new
section extracts to a **single md5 across the four**; (2) the modified
Coordinator paragraph likewise; (3) **G-count 39 × 4** (no guardrail-table
text touched); (4) scoped self-containment — the four files contain **zero
maintenance-partition references** other than the kit's own `US-000` and
the naming-table examples (the per-platform preamble refs remain until
BOLT-002 and are listed in the evidence as the known, routed remainder);
(5) the section's cross-references resolve (`agents/squad/`,
`agents/TEMPLATE-new-role/`, `agents/examples/`, `agents/VERIFICATION.md`,
`actors/roster.yaml`, `TEMPLATE-ACTOR.yaml`, `agents/INDEX.md`); (6) no BOM.

## 7. Acceptance criteria

### AC-1: The section, byte-identical ×4
**Given** the four MainAgents after the V-Bounce, **When** the lifecycle
section is extracted from each, **Then** the four extracts hash
identically, and the section sits immediately before the "## Guardrails
(MUST enforce)" heading in all four.

### AC-2: The contractual blocks present
**Given** the section, **When** read, **Then** it contains the identity
clause (MainAgent ≡ AvengaDevFlow ≡ Coordinator), the three flows
(install / create / delete — with executor-only scaffolding, the
role-generic rule, the reload notice, the N:1 delete check, the
commit-as-record reminder) and the four governance rules (living data /
human authority / installing ≠ enabling / agent-system-only bounds).

### AC-3: The cleanup, with zero collateral
**Given** the shared body, **When** swept, **Then** the Coordinator
paragraph carries no `ADR-`/`US-` maintenance references, the four files'
only remaining maintenance-shaped strings are the kit's own `US-000`, the
naming-table examples and the per-platform preamble refs (BOLT-002's,
listed in the evidence), and **G-count is 39 in all four**.

### AC mapping to source

| Source AC | How this SPEC satisfies it | Verifying evidence |
|-----------|----------------------------|--------------------|
| US-025 AC-1 | The capability lives only in the four MainAgents, byte-identical (role agents untouched) | The single hash ×4; no role-agent file modified |
| US-025 AC-5/AC-6 | The governance block (living data / human authority / installing ≠ enabling) | AC-2 reading check |
| US-025 AC-10 | The identity clause opens the section | AC-2 reading check |
| US-025 AC-9 (partial) | Phase B cleanup + zero new references | AC-3 sweep |

## 8. Testing strategy

Documentation Bolt — scripted evidence: the section-extract hash
comparison ×4, the Coordinator-paragraph hash ×4, the G-count count ×4,
the scoped self-containment sweep with the known-remainder list, the
cross-reference resolution check, BOM check. No unit/integration/E2E (no
runtime surface; the behavioral proof is BOLT-004's pilot).

## 9. Quality gates

| Gate | Threshold | Status |
|------|-----------|--------|
| Unit / integration | n/a — documentation Bolt, no runtime surface | n/a |
| SAST / SBOM | n/a — no code | n/a |
| Perf-smoke (p95/p99) | n/a — no runtime | n/a |
| Prompt-injection scan | the inserted section contains instructions FOR the agent only — no embedded directives that could be triggered by third-party content | pass expected |
| Secret-leak scan | no secrets | pass expected |
| Hallucination lint | every path the section references resolves in the kit | pass expected |
| IP / license provenance | kit-original text | pass expected |
| PII / DLP | internal docs, no personal data | pass expected |
| Dependency-confusion | n/a — no dependencies | n/a |
| Test-first evidence | the §8 checks defined before execution | pass expected |
| Behavioral reproducibility | the hash/sweep checks re-run identically | pass expected |
| Bolt-manifest validation | v_bounces[1] appended, schema PASS | pass expected |

## 10. Security and data

The section runs inside four system prompts — the kit's most sensitive
surface. Mitigations: the payload is reviewed **verbatim** at
`AITL-SPEC-Approval` (this document); the governance block restates the
never-self-enable and installing≠enabling rules at the decision point; the
byte-sync gate prevents per-platform divergence; the prompt-injection gate
checks the inserted text carries no triggerable third-party directives.

## 11. Monitoring and observability

n/a — documentation family (BOLT-004's pilot measures the behavior).

## 12. Migration, compatibility and rollback

- **Migration:** additive text; adopters upgrading get it via the normal
  framework-file supersede (§5.16).
- **Compatibility:** no structural change; the section coexists with the
  enablement clause already shipped.
- **Rollback:** `git revert` of the V-Bounce commit.

## 13. Risk matrix

| Risk | Probability (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|-------------|------------|
| Wording drift between the four | 2 | 3 | The single-hash gate (section + paragraph) |
| The section contradicts the not-yet-scoped kit G07 | 3 | 2 | See §14 — the clause cites §5.12 (already-shipped living-data basis); BOLT-005 closes the letter of G07 next |
| Guardrail-table collateral | 1 | 4 | G-count 39 × 4 gate |

## 14. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| The payload text lives in the SPEC | The reviewer must see the exact words entering four system prompts — micro-edits at review are cheap; post-hoc surprises are not |
| The living-data clause cites §5.12 **and the roster's living-data rule**, not a G07 exception | §5.12 (prompts as living data) and the roster rule (the agents/actors READMEs' living-data row) are already-shipped kit text — the clause stands on existing normative ground (reviewer observation #3: the anchor named precisely); the explicit G07 scoping lands with BOLT-005 immediately after, closing REV-005 F-02's gray zone at the guardrail's letter too |
| The role-generic + content_language rules ride inside the Create flow | REV-005 F-08/F-15: the create moment is where the leak happened in the field — the rule belongs at the point of action, not only in the family docs |
| The preamble cleanup deferred to BOLT-002 | The stale wrapper list and the preamble refs are per-platform surface — one owner per surface, no cross-Bolt file fights |

## 15. Stop conditions

- The four shared bodies differ **before** editing (byte-sync broken
  upstream) → stop, record, ask.
- Any need to touch the guardrail table, a per-platform preamble, or a
  file outside the four → stop (wrong Bolt).

## 16. Definition of Done (DoD)

- [ ] Phases A–C implemented
- [ ] AC-1..AC-3 pass (evidence recorded)
- [ ] Applicable gates pass / n/a per §9
- [ ] MEM created in `devflow/memory/` (exactly one)
- [ ] Manifest `v_bounces[]` entry appended
- [ ] AITL-MEM-Approval recorded

## 17. References

- US-025 · US-025.BOLT-001 (READY) · ADR-013 §3.1–3.6/§3.9 · ADR-014
  §3.8 · REV-005 (C-01/C-02 the field evidence; F-05 the gray zone
  BOLT-005 closes; F-08/F-15 the rules folded into the Create flow) ·
  US-016 (byte-sync discipline) · BOLT-002/003/005 (the sibling owners of
  the excluded surfaces).

## 18. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-24 | eugenio.serrano (agent-drafted) | Revision 1 |

## 19. AITL-SPEC-Approval

> Draft until the Dev-validator records `AITL-SPEC-Approval` (frontmatter
> `review:` block). SPEC approval authorizes the code-run / V-Bounce (G14).

| Field | Value |
|-------|-------|
| **review.reviewers** | `human:eugenio.serrano` (dev_validator) |
| **review.decision** | **approved** |
| **review_ready_at** | `2026-08-24T11:05:19-03:00` |
| **review.started_at** | `2026-08-24T11:12:29-03:00` |
| **review.decided_at** | `2026-08-24T11:12:29-03:00` |
| **Findings** | none blocking — the cross-model review's four observations adopted pre-stamp (reason in the frontmatter `review:` block) |
