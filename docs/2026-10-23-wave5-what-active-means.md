# Wave 5: what `active` should mean (2026-10-23)

Plan item 5.9. **A decision for the maintainer.** This records the evidence and provides
the tool; nothing in the registry was changed.

## The state

```
208 entries: 1 active, 2 deprecated, 205 draft
173 drafts meet every mechanical `active` requirement
100 of those also carry no oligo doubt
```

Every report header tells the reader a draft's numbers are provisional, so the report
disclaims 99.5% of itself — while 173 of those drafts already carry a Crossref-verified
DOI, a taxid and a design year with no open review question, which is everything
`Assay.missing_for_active` asks. They are drafts because no promotion pass has been run.
That is a fact about the queue, not about the entry.

What blocks the other 32:

| blocker | n |
|---|---:|
| `needs_review` has open questions | 19 |
| `citation.design_year` | 13 |
| `citation.doi` | 9 |
| `citation.doi_verified=true` | 9 |
| `target.taxid` | 1 |

## The actual question

`active`'s gate is about **metadata**: a citation that resolves, a taxon to retrieve, a
year to date a baseline from, no unresolved question. It says nothing about whether the
**oligos** are right — and the oligos are what every call in a screen depends on.

Of the 173 eligible drafts, **73 carry a flag in `review.OLIGO_DOUBT`**:

| flag | n |
|---|---:|
| `orientation_inferred` | 27 |
| `oligos_from_secondary_source` | 17 |
| `pairing_is_curator_reading` | 11 |
| `oligos_modified` | 9 |
| `oligos_not_in_cited_paper` | 8 |
| `oligos_read_from_figure` | 7 |
| `thin_evidence` | 5 |

And registry-wide only **87 of 384 oligos** are confirmed against their source paper
(`docs/2026-10-05-hallucination-audit.md`).

So there are two coherent readings, and they are not the same promise:

- **`--tier eligible` (173).** `active` means exactly what the validator checks: the
  citation, taxon and date are verified. Honest, already enforced, and leaves the oligo
  question to `needs_review`, which the report now prints per row (wave 1).
- **`--tier clean` (100).** `active` additionally means no flag doubts the oligos. A
  stronger claim, and the one a lab reading a status would probably assume.

Neither is wrong. What matters is that the report's wording matches whichever is chosen —
it currently says "`draft` is a maintainer sign-off, not a data check", which is true
under either.

For context on what the 100 clean candidates would be asserting: 29 read `Stable`,
23 `Low Coverage`, 15 `Insufficient Data`, 11 `No Recent Data`, 11 `Declining`, 6
`Watch`, 4 are in `Start here`, and 1 is `Not scoreable`. Promotion does not change a
status; it changes how much weight the reader is told to give it.

## The tool

```bash
python scripts/promote.py                        # the picture above
python scripts/promote.py --tier clean           # list the 100
python scripts/promote.py --tier clean --apply   # set status: active on them
```

It **proposes by default**, because `CONTRIBUTING.md` and `CLAUDE.md` both say only a
maintainer sets `active`. `--apply` replaces exactly one line per file — verified on a
copy: 100 files changed, each diff a single `status: draft` → `status: active`, every
comment and key order intact. A YAML round-trip would have reformatted 100 files and
lost the reasoning each entry carries. The copy still validated: 208 valid, 0 problems.

Tests pin that listing writes nothing, that `--apply` changes only the status line, and
that the result still loads.

## Recommendation

`--tier clean`, and say in README what `active` asserts. It is the reading a lab would
assume, it is 100 entries rather than 1, and the 73 it holds back are a worklist with a
named reason each — which is more use than a registry where everything is provisional
for no stated reason. But it is a promise about other people's sequences, so it is
yours to make.
