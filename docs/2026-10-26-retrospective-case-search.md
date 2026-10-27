# A new instrument for retrospective cases, 220 candidates, and four of them read

The held-out set was spent on 2026-10-26 (`docs/2026-10-26-heldout-read-m1-rejected.md`),
and the old way of finding cases was already spent before that. So new cases became the
binding constraint on the whole calibration programme. This records a new instrument, the
queue it produced, and what reading the first four rows established.

**Nothing has been added to any case file.** One genuinely new case is proposed at the end
and it needs one specific check first.

## Why a new instrument was needed

`docs/RESUME-HERE.md` records the old seam as exhausted: "every searchable registry oligo
has been tried" over Europe PMC, and the degenerate ones cannot be searched literally at
all. That instrument looked for papers that **print** a registry oligo, which can only
ever find a small and biased subset — a group using someone else's published assay cites
it and does not retype its primers.

`scripts/find_retrospective_cases.py` asks the citation graph instead. Europe PMC's
`CITES:` field gives the papers citing an assay's design paper, and the search phrases are
failure-weighted because the shortfall is specific: the development set holds 32 `works`
rows and one `fails` + `drift` row against a target of five.

> **The API's own filter is not trustworthy, and finding that out shaped the script.**
> Europe PMC's `ABSTRACT:"..."` does not enforce adjacency. On one design paper it took 131
> citing papers to 58, and none of the first three returned abstracts contained any phrase
> at all — it had matched the words separately. The first version trusted it and produced
> 161 rows of which **154 were unconfirmed**, which is the citation list again rather than
> a queue. The loose query is kept because it is lossy only in the safe direction, but the
> decision is now an exact substring check against the returned abstract. Same six design
> papers: 161 rows to 10.

## The queue

`docs/2026-10-26-retrospective-candidates.tsv`. 220 rows, 202 distinct citing papers, 55
of 117 verified design DOIs, 79 open access.

| group | rows | what it could become |
|---|---:|---|
| `miss` | 140 | the scarce `fails` kind, or a clinical sensitivity report |
| `weakened` | 74 | `partial`, or nothing |
| `mismatch` | 6 | the best shot at a `drift` case |
| `redesign` | 3 | indirect: a group redesigning an assay usually says why |

One design DOI is not in Europe PMC and cannot be searched this way.

## Four rows read, and three of them failed

The queue's value is only as good as the triage, so the four most promising rows were read
rather than counted.

**1. An influenza matrix-gene mismatch-tolerance preprint (2026). REJECTED — circular.**
The title was the best in the queue: an evaluation of primer and probe mismatch tolerance
in a matrix-gene RT-qPCR, which is a registry assay. Reading it shows an **in silico**
mismatch count over a couple of dozen hand-picked strains, concluding the assay still
amplifies. No wet-lab outcome. That is the same method AssayWatch uses, so it cannot
validate AssayWatch, and a case built on it would be the tool confirming itself.

**2. A canine morbillivirus redesign paper (2024). UNRESOLVED — identity.**
It reports a widely used CDV primer set it calls PP-I fully matching 15% and 9% of 194
genomes and missing 9 of 28 positive clinical samples. That is exactly the shape of a
`fails` case. But PP-I is not identified as the registry's pair, and the registry's own
numbers disagree: our Barrett pair exact-matches 68% and 25% of 129 near-complete CDV
genomes in our archive, not 15% and 9%. **So PP-I is probably a different primer set**, and
the paper is paywalled. Needs the full text through the proxy, and the measured
disagreement is the reason it is not a case already.

**3. A UK H5N1 epizootic report (2023). UNRESOLVED — identity again.**
It reports a matrix-gene RRT-PCR performing well across 41 infected premises and over a
thousand swabs, and attributes that to an absence of mismatches in its primer and probe
regions. A clean `works` case in shape. But the paper prints no oligo sequences at all, and
leans on a cited protocol for them. Our entry is "Spackman, modified". Needs that protocol
paper to confirm the assay is ours.

> **The common failure across 2 and 3 is worth naming, because it will recur.** A paper
> that reports an assay's performance usually refers to the assay by a local name or a
> citation and does not reprint its oligos. So the citation graph finds the right papers
> and cannot, on its own, confirm that the assay tested is the assay the registry holds.
> **Identity is the bottleneck, not discovery.** The queue has 220 rows; what is scarce is
> the hour per row needed to confirm identity.

**4. A pan-coronavirus head-to-head (2024). THE ONE THAT PAYS, and partly already known.**
It compares three published pan-CoV PCR assays on 141 archived human, wastewater, bat and
avian specimens, and reports detection rates per genus. Two of the three are the PREDICT
pan-CoV protocols the registry holds.

**It is already a case source**, for one assay: `docs/validation-cases.tsv` cites it for
`CORONAVIRUS_ssRNA_RNA_dependent_RNA_polyme_round2` at 2024-03-29 as `partial`. So a
previous session already made the identification, which is useful precedent.

**But it measures three assays and the registry has extracted one.** The second PREDICT
protocol in that comparison corresponds to
`CORONAVIRUS_ssRNA_RNA_dependent_RNA_polyme` — the entry whose 24-mer reverse the
2026-10-24 sweep settled — and **that entry has no case in either set**. Its reported
detection rates in this paper are the lowest of the three assays by a wide margin, on both
human and wastewater specimens, and it is one of the two that missed an entire genus.

## The one new case proposed, and the check it needs

| field | value |
|---|---|
| `assay_id` | `CORONAVIRUS_ssRNA_RNA_dependent_RNA_polyme` |
| `as_of` | 2024-03-29 |
| `expect` | `fails` |
| `mechanism` | coverage |
| source | the 2024 pan-CoV head-to-head, already cited in `docs/validation-cases.tsv` for the sibling round |

**Why it is not written yet.** The paper describes its two PREDICT protocols as *modified
from* their original publications, and prints the primer sequences only in a supplementary
table that the full-text XML does not carry. Writing a `fails` case against an entry on the
strength of an assay name would be the PP-I mistake with the sign reversed. The check is
one table: fetch the supplementary file and compare its two PREDICT primer sets against
`CoV-FWD3`/`CoV-RVS3` and against the P-005 pair.

If they match, this is a documented, wet-lab, genus-level failure of a registry assay — the
scarce kind, and the first new one since the held-out set was spent.

## Where new cases should go

The old held-out file is spent and must not be reused as a held-out set. Cases collected
from here belong in a **fresh** held-out file, and the guard test that pins the old one
should be widened to cover any `validation-cases-heldout*` file, so a new one inherits the
protection rather than needing it remembered. Neither has been done, because there is
nothing yet to put in it.

## Corrections to the record

**Furuyama 2018 is not a retrospective case and should come off the lead list.** The plan
and `docs/RESUME-HERE.md` both carry it as "the best candidate anywhere in the sweep for a
real H5/H7 drift case", and it is the only named lead. Its abstract settles it: the paper
compares LAMP primer designs, and its primer positions are LAMP positions. The registry
holds no LAMP assay. So it reports on primers the registry does not have, and the lead has
been carried for days on a description that does not survive reading the abstract.
