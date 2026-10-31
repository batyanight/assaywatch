# How this repository was built

Disclosed because a reader should not have to reconstruct it from commit trailers, and
because a project that audits itself for fabricated citations
(`docs/journal/2026-10-05-hallucination-audit.md`) has no business being coy about it.

## The numbers, from a log this repository no longer contains

**This repository begins at a single commit.** It was recreated from a clean tree on
2026-10-31, before the first release, because the development history contained an
institutional name that should not appear in a published artifact — the registry was
started from a transcribed primer list, and early commits described it by name in
`CLAUDE.md`, `LICENSE-registry` and the README. The tree had been clean of it since
2026-10-23; the history had not. Rewriting in place would have left the old objects
fetchable by commit SHA, so the repository was replaced instead.

The figures below therefore describe a history that is retained privately and cannot be
regenerated here. They were read from it, by the commands given, on the dates given:

- **581 of 640 commits carried a `Co-Authored-By: Claude` trailer, and 64 had Claude as the
  git author** (2026-10-31, the day the history was replaced).
- **306 of 330 carried it** (2026-10-23).

```bash
# against the development history, not against this repository
git log --format='%b' | grep -ci 'co-authored-by: claude'
git log --format='%an' | grep -cx 'Claude'
```

What survives the replacement is the part that was doing the work: `docs/journal/` holds
136 dated session records, written as the sessions happened, including the ones that
record a prediction turning out wrong. Those are files in the tree, not commit messages,
so nothing in the account below rests on the history being present.

Most of the code, the tests, the comments and these documents were written by Claude
(Anthropic) in a Claude Code session, directed by Batya Nightingale, who set the scope,
made the scientific and curation decisions, and is the author of record in
`CITATION.cff`.

## What that does and does not mean for the content

**Every factual claim in this repository is checkable, and the checks are in the
repository.** That is the design, and it is a direct response to how this project can
go wrong:

- **Citations.** `scripts/check_citations.py` verifies every registry DOI against a
  committed Crossref cache, in pre-commit and in CI. It exists because a reference was
  once written from memory and attributed to the wrong authors —
  `docs/journal/2026-10-05-hallucination-audit.md` records the incident, the audit that
  followed (1 real problem in 119 checkable entries) and the gate that now makes it a
  build failure. `.pre-commit-config.yaml` records a separate regeneration that found
  ten fabricated DOIs in a papers index.
- **Oligo sequences.** `CLAUDE.md`'s standing rule is "measure, never quote":
  `scripts/verify_oligos_against_paper.py` compares a stored oligo against the cited
  paper's own table, and `scripts/check_amplicons.py` compares a stored amplicon size
  against sizes measured on real GenBank records. 87 of 384 oligos are confirmed
  against their source paper; the rest are tracked as unconfirmed rather than assumed.
- **Numbers in prose.** The documents in `docs/` quote measurements. Where a figure
  came from a run, the command that produces it is given beside it. Several documents
  exist specifically to record a prediction that turned out wrong
  (`docs/journal/2026-10-23-wave2-diverged-and-patent.md`,
  `docs/journal/2026-10-23-wave1-report-honesty.md`) rather than to quietly correct it.
- **Thresholds.** `config.yaml` annotates every number with its justification or an
  explicit admission that it has none, and `scripts/retrospective.py` reports how well
  those numbers do against documented assay failures, including the direction that
  looks bad (precision, 2 of 9).

**What AI involvement does not excuse, and what remains the human's.** No model decided
what an assay is, which assays belong in the registry, whether a status is defensible,
or what the project claims. `CLAUDE.md` records the decisions as standing constraints —
pathogen assays only, no citation from memory, no scoring numbers in code, only a
maintainer sets `status: active` — and those are the maintainer's, enforced on the
model rather than by it.

## For a reader deciding whether to trust a number

Run the gates. They need no network:

```bash
pytest -q
python -m assaywatch.validate registry
python scripts/check_citations.py
```

Then read `config.yaml`'s header, which states what the thresholds are worth, and
`docs/journal/2026-10-23-baseline.md`, which states what the tool's output is worth. Both are
less flattering than a reader might expect, which is the point.
