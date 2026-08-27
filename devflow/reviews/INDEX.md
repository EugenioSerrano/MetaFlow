# Reviews — Index

**Methodology version:** 5.0

Open structured examinations (`REV-NNN`): evaluate code, architecture,
tests, US and documentation against ADRs and standards. Findings remain
draft until `AITL-REV-Approval`; approved findings are routed to
BUG / BOLT→SPEC / DISC / ADR / RISK — reviews never fix, only classify.

---

## 🟡 Draft (pending AITL-REV-Approval)

| ID | Document | Scope | Findings | Status |
|----|----------|-------|----------|--------|
| —  | —        | —     | —        | draft  |

## ✅ Approved (findings actionable — routing in progress)

| ID | Document | Scope | Findings | Status |
|----|----------|-------|----------|--------|
| REV-007 | [REV-007-testwriter-devagent-readiness.md](REV-007-testwriter-devagent-readiness.md) | TestWriter (Copilot agent + 5 skills for manual functional test design, `devflow/input/source-code/TestWriter/`) evaluated against the v5.1 adopter partition: can it ship as an out-of-the-box DevFlow Agent (dormant on fresh install, roster-activated)? Verdict: yes, with one methodology addition. **Approved 2026-08-26** — routing: skills in the definition contract (F-03/F-04) → maintainer-partition ADR + US-023.BOLT-006 (normative text baked into the kit's framework files); the port → new US-026 (test-designer example: per-Bolt TC cadence F-09, read-surface/bundling/CSV-projection/generalization F-07/F-10/F-11/F-12); the ADO retrieval does not ship by maintainer decision (tool-agnosticism, F-06 — the input surface is the canonical `functional/user-stories/` family, MCP wiring is adopter configuration); 5 Compliant validations; zero OQs | 2 Major · 6 Minor + 5 Compliant | approved |
| REV-006 | [REV-006-copilot-adopter-smoke-test.md](REV-006-copilot-adopter-smoke-test.md) | The v5.1 DevFlow Agents kit as a fresh adopter experiences it on GitHub Copilot (VS Code): spawn probes → the fabricated-attribution incident → the reviewer's direct invocation → 30k-cap verification. **Approved 2026-08-25** — routing: 1 net-new Bolt (US-025.BOLT-006: spawn tool + execution-evidence rule + VERIFICATION.md Copilot-row batch) + 4 confirmations attaching to REV-005's routed destinations (charter Bolt US-023 · docs Bolt US-024 · ADR-014 v2 backlog) + 9 Compliant validations; zero OQs | 2 Major · 7 Minor + 9 Compliant | approved |
| REV-005 | [REV-005-devflow-agents-adopter-smoke-test.md](REV-005-devflow-agents-adopter-smoke-test.md) | The v5.1 DevFlow Agents kit as a fresh adopter experiences it (OpenCode smoke test: team config → install → spawn → the spawned reviewer's own REV). **Approved 2026-08-24** — routing: 3 candidate Bolts (US-024 docs · US-023 contract docs · US-023 charters) + evidence into US-025's Bolts and the ADR-014 v2 backlog; both boundary questions resolved by maintainer decision at routing (any actor may be granted DISC/REV/AREV — the roster decides; plural `roles: []` → v2), zero OQs | 17 (3 Major · 13 Minor · 1 Documented deviation) + 7 Compliant validations | approved |

## 🏁 Closed (all findings routed)

| ID | Document | Closed date |
|----|----------|-------------|
| REV-004 | [REV-004-kit-self-containment-consistency-audit.md](REV-004-kit-self-containment-consistency-audit.md) | 2026-08-23 — F-01 → US-000.BOLT-011 (Done) · F-02..F-08 → US-000.BOLT-012 (Done) · F-09 → US-000.BOLT-013 (Done) |
| REV-003 | [REV-003-user-to-actor-identity-vocabulary.md](REV-003-user-to-actor-identity-vocabulary.md) | 2026-08-22 — routed to ADR-010 (supersedes ADR-009) + US-000.BOLT-008 & US-000.BOLT-009 (both Done) |
| REV-002 | [REV-002-v5-kit-consistency-audit.md](REV-002-v5-kit-consistency-audit.md) | 2026-08-22 — all 8 findings closed via US-000.BOLT-007 (Done) |
| REV-001 | [REV-001-hitl-checkpoint-role-inventory.md](REV-001-hitl-checkpoint-role-inventory.md) | 2026-08-21 |

---

**Last updated:** 2026-08-26 (REV-007 approved — TestWriter → out-of-the-box DevFlow Agent readiness review; routing: maintainer ADR + US-023.BOLT-006 · new US-026)
