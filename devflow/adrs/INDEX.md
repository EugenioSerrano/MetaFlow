# ADRs — Index

**Methodology version:** 5.0

Architecture Decision Records: brief, immutable documents that capture
significant architectural decisions, their context, alternatives considered
and consequences. An ADR becomes governing only after `AITL-ADR-Approval`
(Architect / Tech Lead). Source code is the definitive reference for the
current implementation state; the approved ADR is the governing reference
for the decisions it records.

---

## 🟡 Draft (pending `AITL-ADR-Approval`)

| ID | Document | Description |
|----|----------|-------------|
| —  | —        | —           |

## ✅ Accepted

| ID | Document | Description |
|----|----------|-------------|
| ADR-015 | [ADR-015-skills-in-the-agent-definition-contract.md](ADR-015-skills-in-the-agent-definition-contract.md) | Skills in the DevFlow Agent definition contract — an optional, projected, folder-atomic `skills/` bundle (SKILL.md + references/ + assets/) declared via `agent.yaml` `skills:` with strict symmetry (tooling-enforced in v1, schema in v2); per-platform projection rows + parity extension in VERIFICATION.md; never-silent install fallback; invariants: skills are content never authority, kit-shipped skills are tool-agnostic. Maintainer-partition record (normativity baked into kit framework files via US-023.BOLT-006). Source: REV-007 F-03/F-04 |
| ADR-014 | [ADR-014-actors-roster-is-the-enablement.md](ADR-014-actors-roster-is-the-enablement.md) | The actors roster is the enablement — supersedes ADR-008 whole with full carry-forward (§3.1–3.7: precept, safe default, independence, identity rules, Coordinator-never-signs, approver ceiling, escalation floor); the new mechanism: a schema-valid roster entry is the explicit configuration (no per-project AITL-enable ADR, no policy file); enablement = human configuration act, never self-enabled |
| ADR-013 | [ADR-013-agent-lifecycle-governance.md](ADR-013-agent-lifecycle-governance.md) | Agent lifecycle governance — install/create/delete is operational config (executor = living data, approver = the human's roster configuration act per ADR-014), scoping G07; §3.9 examples–squad ship model (the kit ships MainAgents + examples/templates/mapping; the Coordinator creates live agents in `agents/squad/` and installs the wrappers); base for US-025 |
| ADR-012 | [ADR-012-english-all-methodology-artifacts-convention.md](ADR-012-english-all-methodology-artifacts-convention.md) | Repository convention — every methodology artifact of this repository (maintenance + kit partitions) is written in English (generalizes ADR-011; both active) |
| ADR-011 | [ADR-011-english-commit-messages-repository-convention.md](ADR-011-english-commit-messages-repository-convention.md) | Repository convention — commit and PR messages in this repository are written in English (repository-scoped; other repos keep their own language) |
| ADR-002 | [ADR-002-documentation-defect-classification.md](ADR-002-documentation-defect-classification.md) | Documentation defect classification — BUG vs quality gap routing |
| ADR-004 | [ADR-004-repository-partition-v2.md](ADR-004-repository-partition-v2.md) | Repository partition — kit (product) vs root devflow (maintenance), two trees governed separately |
| ADR-005 | [ADR-005-removal-completeness-phrase-family-sweep.md](ADR-005-removal-completeness-phrase-family-sweep.md) | Removal-completeness discipline — phrase-family sweeps (positive coverage, not token greps) |
| ADR-006 | [ADR-006-versioning-and-self-development-model.md](ADR-006-versioning-and-self-development-model.md) | Versioning and self-development model — branches per version, release loop, §5.16 migration |
| ADR-007 | [ADR-007-devflow-agent-identity-model.md](ADR-007-devflow-agent-identity-model.md) | DevFlow agent identity model — roster, per-platform agent definitions |
| ADR-010 | [ADR-010-actor-grammar-and-pure-v5-vocabulary.md](ADR-010-actor-grammar-and-pure-v5-vocabulary.md) | Actor grammar (`human:<user>` / `agent:<id>`) and pure v5 vocabulary — supersedes ADR-009 |

> Archived (lifecycle closed): ADR-001, ADR-003, ADR-009 → [`_archive/`](_archive/INDEX.md).

## ❌ Rejected

| ID | Document | Reason |
|----|----------|--------|
| —  | —        | —      |

## ⛔ Superseded

| ID | Document | Superseded by |
|----|----------|---------------|
| ADR-008 | [ADR-008-aitl-approval-precept.md](ADR-008-aitl-approval-precept.md) | **ADR-014** (2026-08-24) — the §3.1–3.7 invariants carried forward there; the §3.8 AITL-enable ADR mechanism replaced by the roster enablement |

## ⛔ Deprecated

| ID | Document | Status |
|----|----------|--------|
| —  | —        | —      |

---

**Last updated:** August 2026 (ADR-015 accepted — skills in the agent definition contract, from REV-007; ADR-014 + ADR-013 accepted — roster-as-enablement superseding ADR-008 with carry-forward, and the agent lifecycle with the examples–squad ship model)
