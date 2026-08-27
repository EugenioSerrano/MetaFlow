---
id: "SPEC-260822-2350"
title: "Make BUG approval never-blocking: keep the recommended-approver descriptions, remove every block, allow the author to approve any BUG"
date: "2026-08-22"
author: "eugenio.serrano"
llm: "claude-opus-4-8"
status: "draft" # draft | approved | blocked | obsolete
origin: "REV-001" # F-02 evidenced the single-maintainer approval blocker; this SPEC completes it and removes the last block
bolt: "US-000.BOLT-010" # ⚠️ MANDATORY
revision: 1
associated_adrs:
  - "devflow/adrs/ADR-004-repository-partition-v2.md"   # kit-only edits
  - "devflow/adrs/ADR-005-removal-completeness-phrase-family-sweep.md" # positive-coverage sweep discipline
prerequisites: []
risk_class: "medium" # mirrors the Bolt
autonomy_level: "L3" # medium → L3 default; deterministic doc sweep
turn_budget: "" # platform default (10 loops without green)
data_classification: "internal"
review_ready_at: "2026-08-22T23:50:52-03:00"
review: # HITL-SPEC-Approval — recorded by the human reviewer (§3.0)
  decision: "approved"
  reviewers:
    - user: "eugenio.serrano"
      role: "dev_validator"
    - user: "eugenio.serrano"
      role: "tech_lead"
  started_at: "2026-08-22T23:54:56-03:00"
  decided_at: "2026-08-22T23:54:56-03:00"
  findings: []
  acknowledged_without_comment: true
  acknowledgment_reason: "Approved revision 1 against the re-affirmed Bolt US-000.BOLT-010, REV-001 (F-02) and ADR-004/ADR-005. The two-sided transformation is correct — recommended-approver descriptions kept, every blocking clause removed (self-approval-on-critical, the §2.16 safeguard, T02's author exclusion), guidance-never-a-gate + author-included stated everywhere, G29 repurposed with the 39-count preserved, the AI self-approval prohibition (G18/G24) explicitly out of scope, kit-only. The §4 location inventory matches the working tree; ACs are objectively checkable. Reviewer holds dev_validator and tech_lead (domain owner) — self-assigned, single-operator. V-Bounce authorized."
---

<!--
  LANGUAGE POLICY (§3.15): YAML keys, status enums, IDs and headings (##) in
  English; prose content_language (en).

  DOGFOODING SPLIT: authored under v4.2 (root devflow/, ADR-006), own checkpoint
  HITL-SPEC-Approval, manifest schema_version 4.0. Implements US-000.BOLT-010 by
  editing the v5.0 PRODUCT (distribution-kit/, vocabulary AITL-*). Kit-only
  (ADR-004); the root tree inherits at the next §5.16 migration.

  ⚠️ DRAFT until HITL-SPEC-Approval. SPEC approval authorizes the V-Bounce; no
  code-run before it (G14).
-->

# SPEC-260822-2350 — BUG approval is never-blocking (descriptions kept, blocks removed)

| Field | Value |
|-------|-------|
| **Origin** | REV-001 (approved — F-02, the single-maintainer approval blocker) |
| **Bolt** | [US-000.BOLT-010](../functional/bolts/US-000.BOLT-010-severity-agnostic-bug-approval.md) — HITL-BOLT-READY-Approval re-affirmed on the corrected scope (2026-08-22T23:43:28) |
| **ADRs** | ADR-004 (kit-only), ADR-005 (positive-coverage sweep) |
| **Risk / Autonomy** | medium / L3 |

---

## 1. Objective

Edit the v5.0 kit (`distribution-kit/`) so that **BUG approval never blocks**,
while **preserving the recommended-approver descriptions**. Concretely:

1. **Keep** every recommended-approver description — functional → Functional
   Analyst; non-functional `critical` → Architect / Tech Lead; non-functional
   `high|medium|low` → any team member.
2. **Remove** every clause that turns a recommendation into a **block**: the
   "self-approval is never permitted on the `critical` route" prohibition, the
   §2.16 "Self-approval safeguard" paragraph, the T02 "(never the BUG's own
   author)" restriction, and any wording that makes a recommended role a
   precondition.
3. **State everywhere** that the routing is **guidance, never a gate**, and that
   **any qualified team member, the BUG's own author included, may record
   `AITL-BUG-Approval` at any severity** (the dedicated Bolt's
   `AITL-BOLT-READY-Approval` follows the same rule).

If NOT done: a single-maintainer team stays blocked on a self-authored
`critical` non-functional BUG (no valid approver exists), and the summary-table
`AITL-BUG-Approval` rows keep reading as hard gates — the REV-001 F-02 blocker,
surviving at `critical`.

**Scope boundary:** the **AI/agent self-approval prohibition (G18/G24, ADR-008)
is untouched** — a *human* author approving their own BUG is a different axis
from an *AI* approving its own work. Kit-only (ADR-004); root inherits via §5.16.

---

## 2. Context

US-014.BOLT-001 made role routing "guidance, never a gate" (operability
fallback). SPEC-260821-0108 relaxed the non-functional route for
`high|medium|low` to "any team member, author included" but **deliberately kept
`critical` strict** (its §14, "the user's explicit decision"). BOLT-010
(HITL-BOLT-READY re-affirmed) reverses **only the blocking** aspect of that §14
decision: the `critical → Architect/Tech Lead` text stays as a **recommendation**,
it simply stops being a gate, and the author is no longer excluded. This SPEC is
the mechanical HOW; the location inventory (§4) was built by a full-kit
multiline sweep of the current tree.

---

## 3. Source inventory and approval references

| Source | Ref | Approval |
|--------|-----|----------|
| Bolt | `devflow/functional/bolts/US-000.BOLT-010-severity-agnostic-bug-approval.md` | HITL-BOLT-READY-Approval ✓ re-affirmed 2026-08-22T23:43:28 |
| Origin REV | `devflow/reviews/REV-001-hitl-checkpoint-role-inventory.md` | HITL-REV-Approval ✓ (closed) |
| Container | `devflow/functional/user-stories/US-000-non-functional.md` | no approval lifecycle ✓ |
| ADR | `devflow/adrs/ADR-004-repository-partition-v2.md` | HITL-ADR-Approval ✓ (accepted) |
| ADR | `devflow/adrs/ADR-005-removal-completeness-phrase-family-sweep.md` | HITL-ADR-Approval ✓ (accepted) |
| Prior decision reversed (blocking aspect) | `devflow/spec/_archive/SPEC-260821-0108-relax-non-critical-bug-approval-routing.md` §14 | approved (Done) |
| Repository baseline | current working tree on branch `5.0` | — |

Pre-SPEC evidence gate: **all governed sources approved** — no draft input. The
edited files are product files in `distribution-kit/`; their exact current texts
are captured in §4.

---

## 4. Scope — exact location inventory

All under `distribution-kit/`. **Two-sided change per site:** KEEP the
recommended-approver description; REMOVE the block; ensure the never-a-gate +
author-included framing is present.

### 4a. Blocking clauses to REMOVE (verbatim targets)

| # | File:line | Clause to remove / rewrite |
|---|-----------|----------------------------|
| B1 | `GUARDRAILS.md:62` (G29) | "…severity never downgrades the `critical` route… **Self-approval is never permitted on the `critical` route.**" → G29 repurposed (§5, count stays 39) |
| B2 | `GUARDRAILS.md:234` (T02) | "Architect/Tech Lead when `severity: critical` **(never the BUG's own author)**" → remove the author exclusion; severity approver is a recommendation |
| B3 | `Avenga-DevFlow.md:131–132` (§1) | "…otherwise by any team member, the BUG's own author included **(self-approval is not permitted on the `critical` route)**." → drop the parenthetical |
| B4 | `Avenga-DevFlow.md:1278–1281` (§2.16 "Self-approval safeguard") | delete the paragraph — the author may approve any severity; replace with a one-line "guidance, never a gate; author included" note |
| B5 | `Avenga-DevFlow.md:1445–1449` (§3.0 narrative) | rewrite the "Self-approval is permitted at non-critical severities; on the `critical` route a different person is the recommendation…" clause → author may approve at every severity; recommendation retained, never a gate |
| B6 | `Avenga-DevFlow.md:2668–2669` (§3.0 "Who:" bullet) | "…the BUG's own author included **(self-approval is not permitted on the `critical` route)**." → drop the parenthetical |
| B7 | `bugs/README.md:176–177` (item 9) | "…self-approval is never permitted on the `critical` route." → remove; author may approve any severity |
| B8 | `bugs/TEMPLATE-BUG.md:139` (§8) | "Self-approval is never permitted on the `critical` route." → remove |
| B9 | `US-000-non-functional.md:69–70` (item 5) | "…the BUG's own author included — **self-approval is never permitted on the `critical` route**" → remove the dash-clause |

### 4b. Checkpoint-table rows — ADD "guidance, never a gate; author included" (keep the description) — all currently [NO FALLBACK]

`GUARDRAILS.md:24` · `Avenga-DevFlow.md:1402` · `CLAUDE.md:396` · `SKILL.md:413`
· `AvengaDevFlow.agent.md:441` · `.opencode/AvengaDevFlow.md:424` ·
`devflow/README.md:251` · `bugs/README.md:68` · `bugs/TEMPLATE-BUG.md:135–142` ·
`US-000-non-functional.md:67–72`.

### 4c. Dedicated-Bolt mirror — same treatment (recommendation kept, never a gate, author included)

`Avenga-DevFlow.md:1292` (§2.16 table) · `Avenga-DevFlow.md:1404` & `:2698–2705`
(§3.0 BOLT-READY) · `functional/README.md:42–44` · `functional/bolts/TEMPLATE-BOLT.md:174–176`.

### 4d. G29 inline row in the four agents (repurpose, keep count 39)

`CLAUDE.md:245` · `SKILL.md:262` · `AvengaDevFlow.agent.md:290` · `.opencode/AvengaDevFlow.md:273`.

### 4e. Routing descriptions to KEEP as-is except the never-a-gate/author framing

`Avenga-DevFlow.md:21–23` (§0), `:1273–1276` (§2.16), `:2662–2674` (§3.0 "Who:"
bullet — already [CARRIES] the fallback, only drop B6) · the four agents'
Bug-Fix-Protocol bullet (`CLAUDE.md:526`, `SKILL.md:543`, `agent.md:571`,
`opencode:554`) · `reviews/README.md:189–191` ("that value **decides** who may
approve" → "**recommends** who should approve").

### 4f. Out of scope / no change
- Manifest schemas — confirmed prose-only (the enum lists `AITL-BUG-Approval`
  as a string; no routing/blocking prose). No schema edit.
- The AI self-approval prohibition (G18/G24/ADR-008), handoff and Judge-neutrality
  exceptions in the §3.0 operability-principle list — untouched.
- Root `devflow/` tree (ADR-004). v4.2 (released) — no backport.
- Pure "mention" occurrences with no routing/blocking prose (listed in the Bolt
  inventory) — not edited.

---

## 5. Phases

### Phase A — GUARDRAILS.md (G29 repurpose, T02, checkpoint-map row)

**A.1 — G29 (line 62), repurposed; the violation becomes *blocking*, not the routing. Count stays 39:**

```
| G29 | Block a BUG's `AITL-BUG-Approval` (or its dedicated Bolt's `AITL-BOLT-READY-Approval`) for lack of the recommended-role approver, on account of severity, or by excluding the BUG's own author | ❌ *"Approval routing is guidance, never a gate (§2.16, §3.0). The recommended approver — Functional Analyst (functional); Architect or Tech Lead when `severity: critical`, otherwise any team member (non-functional) — is advice, not a precondition: any qualified team member, the BUG's own author included, may record `AITL-BUG-Approval` at any severity, and the dedicated Bolt's `AITL-BOLT-READY-Approval` follows the same rule. The AI self-approval prohibition (G18/G24) is a different axis and still holds."* |
```

**A.2 — T02 (line 234):** replace "Architect/Tech Lead when `severity: critical` (never the BUG's own author), otherwise any team member, the author included" with:
```
…the recorded reviewer may be any qualified team member, the BUG's own author included; the severity-based approver (Architect/Tech Lead when `severity: critical`) is a recommendation, not a gate
```

**A.3 — checkpoint-map row (line 24):** keep the description, append the framing:
```
| `AITL-BUG-Approval` | Functional Analyst (functional) / Architect or Tech Lead when `severity: critical`, otherwise any team member (non-functional) — recommended only; guidance, never a gate: any qualified team member, the BUG's own author included, may record it at any severity | BUG confirmed, evidenced, classified; only then its one dedicated Bolt may be created. |
```

### Phase B — Avenga-DevFlow.md (§0, §1, §2.16, §3.0 table + narrative)

- **B.1 §1 (131–132):** drop "(self-approval is not permitted on the `critical` route)".
- **B.2 §2.16 (1278–1281):** delete the "Self-approval safeguard" paragraph; replace with: *"The severity-based approver is a recommendation, not a gate: any qualified team member, the BUG's own author included, may record `AITL-BUG-Approval` at any severity (the AI self-approval prohibition, G18/G24, is a separate axis)."*
- **B.3 §3.0 table row (1402):** same shape as A.3.
- **B.4 §3.0 narrative (1445–1449):** rewrite to: *"Self-approval is permitted at every severity; on the `critical` route Architect or Tech Lead is the recommendation, but any qualified team member — the author included — may record it, noting the self-assigned role (the operability principle — role routing never blocks)."*
- **B.5 §3.0 "Who:" bullet (2668–2669):** drop the "(self-approval is not permitted on the `critical` route)" parenthetical; the surrounding fallback (2670–2672) stays.
- **B.6 §2.16 nature/Bolt-table mirror (1292) & §3.0 BOLT-READY (1404, 2698–2705):** mirror text keeps the severity recommendation, adds "guidance, never a gate; the Bolt's own author included".
- **B.7 §0 (21–23):** description stays; no blocking clause present — leave as recommendation (optionally add "recommended"). No self-approval clause to remove.

### Phase C — The four agent definitions (one synchronized pass, parity preserved)

- **C.1 — G29 inline row** (`CLAUDE.md:245`, `SKILL.md:262`, `agent.md:290`, `opencode:273`), applied identically:
```
| G29 | Blocking a BUG's `AITL-BUG-Approval` (or its Bolt's readiness) for lack of the recommended-role approver, on severity, or by excluding the author | ❌ Routing is guidance, never a gate: any qualified member, the author included, may approve any BUG at any severity. AI self-approval (G18/G24) is a separate axis and still holds |
```
- **C.2 — checkpoint-table row** (`CLAUDE.md:396`, `SKILL.md:413`, `agent.md:441`, `opencode:424`), identically:
```
| `AITL-BUG-Approval` | FA (functional) / Architect-TL if `severity: critical` else any team member (non-functional) — recommended only; guidance, never a gate: any qualified member, the author included, may approve at any severity | BUG confirmed; only then its dedicated Bolt |
```
- **C.3 — Bug-Fix-Protocol bullet** (`CLAUDE.md:526`, etc.): keep the routing description; no blocking clause present (no change needed beyond parity re-sync if touched).
- Preserve four-agent body parity (byte-identical shared region) and G-count 39×5.

### Phase D — Other kit artifacts

- **D.1 `devflow/README.md:251`** — checkpoint row, same as C.2 shape.
- **D.2 `bugs/README.md`** — row 68 (as A.3 shape); item 9 (172–179): keep the severity recommendation, remove "self-approval is never permitted on the `critical` route" (176–177), state author-included + guidance.
- **D.3 `bugs/TEMPLATE-BUG.md`** — §8 (135–142): keep the recommendation, remove "Self-approval is never permitted on the `critical` route" (139), add author-included.
- **D.4 `US-000-non-functional.md:67–72`** — keep the recommendation, remove the "self-approval is never permitted on the `critical` route" dash-clause (69–70).
- **D.5 `functional/README.md:42–44` & `functional/bolts/TEMPLATE-BOLT.md:174–176`** — mirror footnote: recommendation kept, add "guidance, never a gate; the Bolt's own author included".
- **D.6 `reviews/README.md:189–191`** — "that value **decides** who may approve it" → "that value **recommends** who should approve it".

### Phase E — Verification suite (deterministic, recorded in the MEM)

Run and capture §7's checks: presence assertions, positive-coverage sweep,
absence sweep, G-count 39×5, four-agent parity, root-untouched, manifest re-validation.

---

## 6. Acceptance criteria

**AC-1 (descriptions kept):** grep confirms the recommended-approver descriptions
still present at every §4b/§4c/§4e location (functional → FA; non-functional
`critical` → Architect/Tech Lead; non-functional `high|medium|low` → any member).

**AC-2 (blocks gone — absence sweep):** zero matches in `distribution-kit/` for
the blocking family (multiline-aware): `self-approval is (never|not) permitted on
the .?critical.? route`, `never the BUG's own author`, the §2.16 "Self-approval
safeguard" heading, and any "severity never downgrades" gate phrasing.

**AC-3 (positive coverage over the complete checkpoint set):** every BUG-route
statement — **including the checkpoint-table rows (B4b) and the mirror (4c)** —
reads as guidance-never-a-gate and states the author is included, at any severity.

**AC-4 (author-inclusive at critical):** grep confirms explicit "author
included" / "the BUG's own author included" applies with **no** severity
exclusion (no "except critical" residue).

**AC-5 (G29 repurposed, count preserved):** `grep -cE '^\| G[0-9]{2} \|'` = **39**
in GUARDRAILS.md and in each of the four agents; G29 now guards *blocking*.

**AC-6 (four-agent parity):** whole-body diff = sanctioned divergence only;
G-count 39×5.

**AC-7 (AI self-approval untouched):** G18/G24 and the §3.0 operability-principle
"only exceptions" list are byte-unchanged except where they intersect the BUG
route; the AI self-approval prohibition remains.

**AC-8 (kit-only):** `git status` shows only `distribution-kit/` files + this
SPEC's governance records (Bolt/manifest/INDEX). No root `devflow/` methodology file.

**AC-9 (manifest validation):** the Bolt manifest validates against
`manifest-v4-bolt.schema.json` (0 errors) after the `spec_revisions[]` /
`v_bounces[]` updates.

---

## 7. Testing strategy

No runtime — verification is the deterministic command set (captured in the MEM):
- **Presence greps (AC-1)** — count the description phrases; expected > 0 at each site.
- **Absence greps (AC-2/AC-4)** — multiline (`rg -U`) for the blocking family; expected **0**.
- **Positive-coverage (AC-3)** — enumerate every BUG-route statement, assert each carries "guidance, never a gate" + "author included".
- **G-count (AC-5)** — `grep -cE '^\| G[0-9]{2} \|'` = 39 ×5.
- **Parity (AC-6)** — the four-agent whole-body diff (CRLF-normalized).
- **Root-untouched (AC-8)** / **manifest (AC-9)** — `git status`; `ConvertFrom-Json` + schema check.
- **Edge cases:** escaped pipe `\|` inside table cells; multiline clauses (B4, B5, B7, B9); CRLF/LF.
- **BUG evidence:** n/a — not a BUG Bolt.

---

## 8. Quality gates

| Gate | Status |
|------|--------|
| Unit / integration | `n/a` — documentation-only, no executable code |
| SAST / SBOM / dependency-confusion / perf-smoke | `n/a` — no code, no runtime, no deps |
| Prompt-injection / secret-leak | `pass` — all text authored here, no external input |
| Hallucination-lint | `pass` — every §-reference and file:line resolves on disk (§4 inventory) |
| IP / license provenance / PII·DLP | `n/a` — internal doc text, no third-party content, no PII |
| Test-first evidence | `n/a` — not a BUG Bolt |
| Behavioral reproducibility | `pass` — deterministic grep/diff/count, idempotent |
| Bolt-manifest-validation | `pass` — 0 errors vs `manifest-v4-bolt.schema.json` |

---

## 9. Security and data

The change **removes** the last review-independence control on `critical`
(security-bearing) non-functional defects — the author may now self-approve a
`critical` BUG. This is the maintainer's accepted decision (BOLT-010
HITL-BOLT-READY re-affirmation). Compensating controls: the Architect/Tech Lead
recommendation is retained (guidance), and every approval records
actor/role/timestamp/evidence (§3.0). The **AI** self-approval prohibition
(G18/G24) is untouched. Data classification: `internal` — doc text only.

---

## 10. Monitoring, migration, rollback

- **Monitoring:** the §7 verification suite is the observability; output captured in the MEM.
- **Migration:** none in-repo — lands in `distribution-kit/`; adopters get it at their next §5.16 release migration. v4.2 (released) unchanged.
- **Rollback:** revert the kit commit(s); the root tree is untouched. The SPEC revision is immutable manifest history.

---

## 11. Risk matrix

| Risk | P | I | Mitigation |
|------|---|---|------------|
| Sweep deletes a description instead of de-gating it | 2 | 3 | AC-1 presence assertion (descriptions must remain) |
| A blocking clause is missed (multiline) | 2 | 3 | multiline absence sweep (AC-2); §4a lists the wrapped ones (B4/B5/B7/B9) |
| Sweep touches the AI self-approval rule | 1 | 4 | explicit scope guard (AC-7); G18/G24 out |
| Four-agent drift | 2 | 3 | identical Phase-C text; AC-6 parity |
| G-rule count changes | 1 | 2 | G29 repurposed not deleted; AC-5 = 39×5 |
| Weakened critical review independence | 3 | 2 | accepted by decision; recommendation + recorded evidence as compensating control |

---

## 12. Decisions and trade-offs

| Decision | Reason |
|----------|--------|
| Keep the recommended-approver descriptions | Maintainer's explicit instruction — the routing is useful guidance |
| Remove the block in every case (incl. self-approval-on-critical) | The only way a self-authored `critical` BUG becomes approvable for a solo maintainer (closes REV-001 F-02 fully) |
| G29 repurposed to guard *blocking* (not routing) | Keeps a meaningful blocking rule + the 39-count invariant |
| AI self-approval prohibition untouched | Different axis (human author vs AI approving its own work); ADR-008/G18/G24 stand |
| Kit-only | ADR-004 — the root rulebook advances at release migration |

---

## 13. Stop conditions

- A root `devflow/` methodology file appears in the diff → **stop**, revert, record in MEM.
- Pre-existing four-agent drift before Phase C → **stop**, reconcile first.
- AC-2 absence sweep still finds a blocking clause, or AC-1 shows a description was lost → **stop**, sweep again; do not paper over.
- G-count ≠ 39 in any of the five files → **stop**, fix the repurpose.
- A governed source changes materially during execution (G15) → stop, revise this SPEC, re-approve.

---

## 14. Definition of Done

- [ ] Phases A–E implemented
- [ ] AC-1..AC-9 pass (presence, absence, positive-coverage, author-inclusive, G-count 39×5, parity, AI-rule untouched, kit-only, manifest 0 errors)
- [ ] MEM created (one per V-Bounce) with the full verification output
- [ ] Manifest `v_bounces[]` appended
- [ ] HITL-MEM-Approval recorded

---

## 15. References

- `devflow/functional/bolts/US-000.BOLT-010-severity-agnostic-bug-approval.md` (the Bolt — WHAT)
- `devflow/reviews/REV-001-hitl-checkpoint-role-inventory.md` (F-02)
- `devflow/spec/_archive/SPEC-260821-0108-relax-non-critical-bug-approval-routing.md` (the twin; §14 blocking aspect reversed)
- ADR-004 (kit-only), ADR-005 (positive-coverage sweep)

---

## 16. Revision history

| Date | Author | Change |
|------|--------|--------|
| 2026-08-22 | eugenio.serrano | Initial revision 1 (draft) — corrected scope: descriptions kept, blocks removed, author-inclusive |

---

## 17. HITL-SPEC-Approval

> **Avenga DevFlow §2.4.1, §3.0.** DRAFT until the Dev-validator (+ applicable
> domain owners) records `HITL-SPEC-Approval` in the `review` block. Bolt
> readiness authorized SPEC preparation; **SPEC approval authorizes the
> V-Bounce**. A material source change invalidates this approval (G15).

| Field | Value |
|-------|-------|
| **review.reviewers** | eugenio.serrano (dev_validator + tech_lead — self-assigned, single-operator) |
| **review.decision** | **approved** |
| **review_ready_at** | `2026-08-22T23:50:52-03:00` |
| **review.started_at** | `2026-08-22T23:54:56-03:00` |
| **review.decided_at** | `2026-08-22T23:54:56-03:00` |
| **Findings** | none — `acknowledged_without_comment: true` (see frontmatter) |
