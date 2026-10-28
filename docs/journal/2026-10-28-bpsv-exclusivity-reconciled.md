# BPSV's cross-reaction and Zhao's exclusivity panel were never in conflict: the probe was

2026-10-28. `target.exclusivity_taxids` was built yesterday so a published specificity
claim could be screened instead of being represented by whatever happened to be on disk.
The first claim it tested is the one that motivated it, and the answer reconciles two
numbers this registry has carried in contradiction since 2026-10-24.

## The two numbers

The BPSV entry's `cross_reactive` flag says, from a hand screen of 2026-10-24 over 92
complete *Parapoxvirus* genomes:

> screened, 61 of 64 Orf virus genomes score reduced (95.3% detection), which exact
> matching did not show

Zhao et al. 2013, the design paper, says the opposite in its own words: the three
species-specific assays "demonstrated the specificities to the available parapox DNA
respectively", with no cross-reaction. The entry recorded the disagreement as the kind this
project exists to surface.

## What the pipeline says now that it fetches the neighbour

The 2026-10-27 run screened BPSV against the whole orf virus and pseudocowpox archives,
retrieved for the claim. By call:

| taxon | screened | evaluable | calls |
|---|---|---|---|
| orf virus (10258) | 2,498 | 85 | 82 `reduced`, 3 `fail` |
| pseudocowpox virus (129726) | 178 | 15 | 1 `reduced`, 14 `fail` |
| BPSV, its own target (129727) | 128 | 20 | 20 `detect` |

**Both numbers are right, about different questions.** The amplicon forms in 82 of 85
evaluable orf virus records — the hand screen's cross-reaction is still there — and the
assay is predicted to **detect none of them**, because `drift.reduced_not_detected_for:
[hydrolysis_probe, mgb]` has shipped since: a mismatched hydrolysis probe is not a
detection, and detection IS the probe for this assay. The 2026-10-24 screen predates that
switch and counted `reduced` as a detection, which for a TaqMan assay reports the primers
and says nothing about the reporter.

So Zhao's panel and this pipeline now agree, and they agree for the reason Zhao gives:
"the specificity of the probe plays a major role for the differentiation ... the primers
used in these assays may not be species-specific but are genus-specific". The primers are
genus-specific, exactly as the paper says; the probe is what separates the species.

## Which is why the table prints both columns

An exclusivity table that printed only "0% detected" would make a published claim look
confirmed by the number that says least. The new section prints **detected, amplified and
evaluable** side by side:

| assay | status | claimed taxon | predicted detected | amplified | evaluable | share |
|---|---|---|---|---|---|---|
| `BPSV_dsDNA_RPO147_J6R_TaqMan_Zhao_2013` | insufficient data | orf virus (10258) | 0 | 82 | 85 | 0% |
| `BPSV_dsDNA_RPO147_J6R_TaqMan_Zhao_2013` | insufficient data | pseudocowpox virus (129726) | 0 | 1 | 15 | 0% |

`amplified` is `detect` + `reduced`: a product forms, whatever the probe then does. On a
gel that is a band.

## Two things the section had to fix to be worth printing

**It exists at all.** The predicted-cross-reactivity table lives inside the flagged-assay
detail block, and BPSV is `insufficient data` — 9 evaluable records of its own. So on the
first run after the feature shipped, its 2,692 off-target calls were computed and
invisible. An assay whose neighbour had to be fetched is usually an assay too thin to
flag, which makes a status-independent section the only place the claim can appear.

**The denominator is evaluable records, not everything screened.** Dividing by the whole
archive read the orf virus claim as "0 of 2,498", where 2,413 of those records are short
fragments holding no product for anything. That is a reassuring number assembled from the
wrong rows, and it is the same mistake the inclusivity arm was corrected for on
2026-10-04.

Both are pinned in `tests/test_exclusivity.py` with these numbers.

## One operational finding, recorded because it will shape the next week's work

Re-rendering this report should have been a report job, and it started screening instead.
The run was stopped and the report rendered directly from `results/2026-10-27/calls.tsv.gz`,
which is the same table either way because nothing affecting a call had changed.

**The diagnosis written here first was wrong and is corrected in
`2026-10-28-screen-signature-projection.md`.** It said the signature hashes the whole of
`registry/`; it does not, and never did — it hashes each GROUP's own assay files. What was
true is that it hashed each entry's whole YAML, so a note or a `conditions` block
invalidated the groups holding that entry: 312 of 494 cached screens, after 192 entries
were curated. `signature.screen_key` now hashes only the screen-relevant fields, which
takes the same two days of curation from 444 archive rescreens to 47.

**One status did move, and for a good reason.** `CALICIVIRUS_ssRNA_Helicase_Reid_1999`
appears in the report for the first time (`no recent data`), because changing its flag
from `oligo_sequence_uncertain` to `oligos_modified` removed the OPEN flag that had been
holding it out of the status tables. 19 `no recent data` becomes 20; nothing else moves.
