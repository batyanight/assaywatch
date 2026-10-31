# Scoping: what an assay is compared against

Every percentage on this site is a fraction, and the interesting argument is
almost never about the numerator. It is about which sequences belong in the
denominator.

If that set is wrong, the tool still produces a clean, confident number — just
about the wrong population. This page explains how the comparison set is chosen
for each assay, and how I have seen it go wrong.

---

## The default: everything under the target organism

Each entry names an NCBI taxid and usually a gene-level search. Together these
define the archive of records that assay is screened against, and by default
every record in it counts.

For a species-specific assay against a well-defined target, that is the right
answer and needs no further thought.

## When an assay is narrower than its organism

A pan-family consensus PCR and a species-specific TaqMan can sit under the same
taxid and mean entirely different things.

An assay designed for the gorilla and chimpanzee lineages of SIV, screened
against all of SIV, will appear to fail on most records. It has not failed. It
is being asked a question it never claimed to answer.

So an entry can declare the taxa its design paper actually claims — the smallest
set of groups covering that range. A record then counts if it belongs to one of
those groups **or anything beneath them** in the taxonomy.

!!! note "Why ancestry rather than an exact list"
    Matching exact taxids alone dropped strain-level and unranked records
    sitting under the listed species — around 90% of in-scope records for every
    scoped assay when I measured it. Walking the taxonomy tree fixes that.

Out-of-scope records are still screened and still reported; they are kept out of
the statistics and counted separately, so nothing vanishes quietly.

This is a curation judgement and it is unfinished. 34 test cases still need
their scope read out of the original paper, and until that is done those rows
are marked rather than guessed.

## Cross-reactivity claims

Many papers state that their assay does *not* amplify particular
near-neighbours. Those organisms are listed separately and fetched deliberately,
then reported as predicted cross-reactivity.

They are never scored. A published specificity claim is something this tool can
comment on from sequence; it is not a performance figure it can grade, and
treating it as one would mix two different questions.

---

## The failure mode worth your attention

A search query is a claim about what population you are judging an assay
against. It can stop being true without anything breaking.

Four influenza entries here used queries naming subtype taxids — the identifiers
NCBI used to assign to H5, H7 and H3 deposits. **NCBI stopped assigning them.**
New deposits go under the parent species instead.

The effect: those archives stopped growing years before I noticed. The newest
H5 deposit was from 2021, the newest H7 from 2020. Seven H3 subtype taxids
combined with hemagglutinin terms returned **zero** records for 2024–2026,
against 95,155 without the subtype restriction.

Nothing raised an error. The reports said *"no evaluable records deposited since
Oct 2021"* beside each assay. That sentence is **true**, and it reads as a fact
about influenza: nothing recent was deposited. It was a fact about my query — I
could not see what had been deposited.

No incorrect verdict was ever published, because the tool declined to judge
those assays and named its cutoff, which is the behaviour you would want. But
four assays sat unjudgeable while the output looked perfectly healthy.

### What fixed it

One broad hemagglutinin search shared across those assays, with each entry
restricting itself to records whose description names its own subtype. The
subtype is written in the record title, and Entrez will not search it —
`H3N2[Title]` and `H3N2[Organism]` both return nothing, while the bare term
works.

The match needs a word boundary on the left, because strain identifiers like
`GKISBBBH74562` contain `H7` as a substring. I found that by checking, not by
assuming.

!!! success "The check that proves a filter is not cheating"
    Narrowing a denominator can always manufacture an improvement, so the test
    has to be directional: with the filter applied, the **percentage should rise
    while the record count falls**, as off-target failures leave. If the
    percentage falls, the filter is removing genuine target records and it is
    wrong.

    All four assays behaved correctly, with no case where it fell. The H5 assay
    reads `declining` at 49.8% without the filter and `stable` at 96.2% with it
    — so the filter prevents a fabricated decline on an assay in active use.

### What does not catch this

I built a check for other stale queries and then measured it honestly enough to
tell you it mostly does not work. It lists archives whose newest deposit is over
18 months old, loudest when a sibling archive of the same organism is current.
Run across the registry it produced four candidates and **all four were fine** —
a narrow gene query under an organism that deposits whole genomes always looks
stale next to a broad one.

It would not have caught the influenza problem either. The old H3 archive held
44,627 records against a query returning 44,633. They agreed, because the query
was working perfectly and returning a population that had stopped growing.
**Comparing a query against itself cannot detect a change in how a database
annotates things.**

What it genuinely buys is a short worklist — 13 archives out of 134 worth a
human looking at — and that is all I claim for it.

If you run something similar on your own targets, this is the failure mode I
would watch for: not a query that errors, but one that quietly stops matching
how a database has started labelling things.

---

## Records that never reach the statistics

Separate from scoping, and the most serious limitation here.

A record where one primer has drifted counts as a **failure**. A record where
*both* primers have drifted produces no product at all and leaves the
denominator entirely.

So what gets measured is correlated with what is being measured. Across one full
run, **65.7% of 2.72 million screened records never reached the statistics**.
Every assay page shows that split for its own assay, under "what reached the
statistics".

This probably cannot be fixed without changing what the tool estimates, so
rather than bury it: when you read a percentage here, check how much was
dropped to produce it.
