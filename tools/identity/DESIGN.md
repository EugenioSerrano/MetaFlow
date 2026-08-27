# identity — one canonical human identifier

**Status:** specification.

## The problem

Five fields across the methodology name a human, and §3.0 already binds all
of them to one string: `review.reviewers[].user`, the manifest's
`generation.created_by` (*"the human who initiated or controlled the
generation — never the model name"*, §3.12) and `hitl_approvals[].decided_by[].user`,
the document `author:` / `owner:` frontmatter, and the `human:<…>` form of the
AREV `judge_model` (§3.13).

This is not cosmetic. **Four blocking rules compare those values:**

- **G29** — a non-functional BUG's reviewer must not be the BUG's own `owner`.
- **G18** — the MEM approver must not be the agent.
- **G24** — a checkpoint may not be delegated to AI.
- **G37** — a human Verdict's arbiter must be neither the Bolt's author nor
  the Challenger's operator (§3.13).

If one artifact records `eugenio.serrano` and another `Eugenio Serrano`, those
comparisons fail silently: self-approval passes as if two different people were
involved. A single resolver is the prerequisite for the rules being checkable
at all.

## What it does

Resolve one identity, in this order, stopping at the first that answers:

1. **Git config `user.email`** — the definition itself (§3.0): its local part
   *is* the identity. `user.name` comes along as the display label only.
2. **GitHub** — the authenticated account, when git config carries no email;
   its account email yields the local part, and the login is a fallback the
   tool reports as such rather than as a resolved identity.
3. **The operating system** — the current user, same caveat.
4. **Ask the human.** Never guess, never synthesize from a path or hostname.

## Interface sketch

```
devflow whoami                 -> eugenio.serrano
devflow whoami --display       -> Eugenio Serrano
devflow whoami --json          -> { "user": "...", "display": "...", "source": "github" }
```

`--json` reports `source` so an agent can tell a resolved identity from a
fallback, and a human can see which one was used.

## Boundaries

- Resolves; never writes an artifact.
- Never invents. An unresolvable identity is a question for the human, not a
  default value.

## The canonical form is already decided

**§3.0 closed it:** the identity string is the **local part of the person's
`git config user.email`** — `eugenio.serrano@avenga.com` → `eugenio.serrano`.
It carries no spaces, accents or display formatting and is compared verbatim,
which is what makes G29, G18/G24 and G37 decidable at all. Every
identity-bearing `TEMPLATE-*.md` states it in its `author:` comment — 28 of
the 31; the three AREV phase templates carry no `author:` at all, because a
phase is attributed to the **model** that produced it
(`challenger_model` / `defender_model` / `judge_model`, W09) and only the
Verdict names a person, through the same string in
`judge_model: human:<…>` (§3.13). `git config user.name` remains the
human-readable label in prose — never an identity field.

So this tool does not choose a form: **it is the single producer of the one
§3.0 defines.** Its job is resolution and consistency, not policy. Where the
resolution chain returns a display name (GitHub, the OS), it derives the local
part from the email or asks — it never records the display name as identity.
