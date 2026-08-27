# PROMPT-001 — Analysis of the methodology

Analysis of the methodology: deep file-by-file audit of the kit — internal consistency, agent sync, and gaps against schemas, templates and guardrails. Kit only, never the installed tree.

Do a deep, file-by-file analysis of the entire methodology and its agents,
looking for inconsistencies and opportunities for improvement.
But don't overdo it either — don't report findings just to show you found
something.

IMPORTANT — this repo both builds the methodology and is governed by it, and
there are two devflow/ trees. Analyze distribution-kit/: that is the product,
the version under construction, and the only thing this analysis is about. The
devflow/ at the repository root is the previous version installed to govern
this repo — it is not the object of the analysis and its divergence from the
kit is expected, never a finding.

Verify against the repo, never against a summary. And apply these lenses:

1. Normative prose vs. machine contract: compare what the methodology states
   against the `required` fields of the JSON Schemas. That's where the most
   expensive gap lives.
2. Each README against its own template: field names, status enums, declared
   sections vs. actual sections.
3. Multiline greps: a rule split across two lines is invisible to a plain grep.
4. Resolve relative links and § references on disk.
5. Rules an agent enforces but the methodology never states (or vice versa).
6. Sync of the 4 agents with the procedure in AGENTS.md, and the exempt zone
   against the parity matrix.

At the end, 3 scores from 1 to 100, with a per-dimension breakdown and evidence
for each row:
1) internal consistency of the methodology itself
2) consistency of the agents with each other
3) consistency between the agents and the methodology
