# How this repository was built

Disclosed because the git history makes it obvious and a reader should not have to
reconstruct it from commit trailers, and because a project that audits itself for
fabricated citations (`docs/2026-10-05-hallucination-audit.md`) has no business being
coy about it.

## The numbers, from the log

Of 330 commits as of 2026-10-23: **306 carry a `Co-Authored-By: Claude` trailer** and
**64 have Claude as the git author**. Regenerate with:

```bash
git log --format='%b' | grep -ci 'co-authored-by: claude'
git log --format='%an' | grep -cx 'Claude'
```

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
  `docs/2026-10-05-hallucination-audit.md` records the incident, the audit that
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
  (`docs/2026-10-23-wave2-diverged-and-patent.md`,
  `docs/2026-10-23-wave1-report-honesty.md`) rather than to quietly correct it.
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
`docs/2026-10-23-baseline.md`, which states what the tool's output is worth. Both are
less flattering than a reader might expect, which is the point.
