# Scope and retrieval

Every proportion reported here is a fraction, and the question that matters is
almost never the numerator. It is which sequences belong in the denominator.

If that set is wrong, the tool still produces a precise figure, about the
wrong population. This page documents how the comparison set is chosen for
each assay, and the failure seen in practice.

---

## Default: all records under the target organism

Each entry names an NCBI taxid and, usually, a gene-level search. Together
these define the archive the assay is screened against. By default every record
in it counts.

For a species-specific assay against a well-defined target this is correct and
needs nothing more.

## Assays narrower than their target taxon

A pan-family consensus PCR and a species-specific hydrolysis-probe assay can
sit under the same taxid while making very different claims.

Take an assay designed for the gorilla and chimpanzee lineages of SIV, screened
against all SIV. It will look like it fails on most records. It has not failed;
it is being judged against a claim it never made.

An entry can therefore declare the taxa its design publication actually
claims: the smallest set of groups covering that range. A record counts if it
belongs to one of those groups **or to any taxon beneath them**.

!!! note "Ancestry rather than an enumerated list"
    Matching exact taxids alone excluded strain-level and unranked records
    beneath the listed species. Measured, that was approximately 90% of in-scope
    records for every scoped assay. Walking down the taxonomy fixes it.

Out-of-scope records are screened and reported. They are left out of the
statistics and counted separately, so nothing is discarded silently.

This is a curation judgement and it is incomplete. 34 validation cases still
need their scope read from the source publication; until then those rows are
marked rather than inferred.

## Published specificity claims

Many publications state that an assay does *not* amplify particular
near-neighbors. Those organisms are listed separately, retrieved on purpose,
and reported as predicted cross-reactivity.

They are never scored. The tool can comment on a published specificity claim
from sequence, but the claim is not a performance figure the tool can assess,
and scoring it as one would mix up two different questions.

---

## Silent failure of a retrieval query

A search query is a claim about the population the assay is being evaluated
against. It can stop being true without producing an error.

Four influenza entries used queries naming subtype taxids, the identifiers
NCBI formerly assigned to H5, H7 and H3 deposits. **NCBI stopped assigning
them**; new deposits are filed under the parent species.

Those archives therefore stopped growing years before anyone noticed. The most
recent H5 deposit was from 2021 and the most recent H7 from 2020. Seven H3
subtype taxids combined with hemagglutinin terms returned **zero** records for
2024–2026, against 95,155 without the subtype restriction.

No error was raised. The reports said *"no evaluable records deposited since
Oct 2021"* beside each assay. That statement is **true**, and it reads as a fact
about influenza deposition. It was a fact about the query: what had been
deposited was not visible to it.

No incorrect verdict was published, because the tool declined to judge those
assays and stated its cutoff, which is what it should do. Even so, four
assays stayed unassessable while the output looked sound.

### Resolution

One broad hemagglutinin search is now shared across those assays, and each
entry limits itself to records whose description names its own subtype.
The subtype appears in the record title and cannot be searched through Entrez:
`H3N2[Title]` and `H3N2[Organism]` both return nothing, while the unqualified
term works.

The match needs a left word boundary, since strain identifiers such as
`GKISBBBH74562` contain `H7` as a substring. This came from measuring, not assuming.

!!! success "Directional verification of the filter"
    Narrowing a denominator can always look like an improvement, so the
    test has to be directional: with the filter applied the **proportion should
    rise while the record count falls**, as off-target failures are removed. A
    falling proportion would mean genuine target records are being
    excluded and the filter is wrong.

    All four assays behaved as required, with no case of a falling proportion.
    The H5 assay reads `declining` at 49.8% without the filter and `stable` at
    96.2% with it, so the filter prevents a spurious decline on an assay
    in current use.

### Limits of automated detection

A check for other stale queries was built and then measured. It lists
archives whose most recent deposit is over 18 months old, weighted toward those
with a current sibling archive for the same organism. Run across the registry
it produced four candidates, **all four of which were correct**: a narrow gene
query under an organism that deposits whole genomes will always look stale
next to a broad one.

It would not have caught the influenza problem. The former H3 archive held
44,627 records against a query returning 44,633. These agree, because the query
was running correctly and returning a population that had stopped growing.
**Comparing a query against itself cannot detect a change in database
annotation practice.**

Its real value is a short worklist, 13 archives of 134 that deserve a manual
look, and that is all that is claimed for it.

If you run a comparable system, this is the failure to watch for:
not a query that errors, but one that stops matching how a database has begun
labeling its records.

---

## Records excluded from the statistics

This is separate from scope, and it is the most serious limitation of the
method.

A record in which one primer has diverged is scored as a **failure**. A record
in which *both* have diverged yields no product and is left out of the
denominator entirely.

Censoring is therefore correlated with the quantity being estimated. On the
2026-10-31 run, **48.4% of 3.04 million screened assay–record pairs did not
reach the statistics**. Each assay page reports the proportion for its own
assay.

This may not be correctable without changing the estimand. Read any proportion
reported here together with the proportion of records excluded to produce it.
