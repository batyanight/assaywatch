# Scope and retrieval

Every proportion reported here is a fraction, and the substantive question is
almost never the numerator. It is which sequences belong in the denominator.

Where that set is wrong the tool still produces a precise figure, about the
wrong population. This page documents how the comparison set is determined for
each assay, and the failure mode observed in practice.

---

## Default: all records under the target organism

Each entry names an NCBI taxid and, usually, a gene-level search. Together
these define the archive against which the assay is screened; by default every
record in it counts.

For a species-specific assay against a well-defined target this is correct and
requires no further specification.

## Assays narrower than their target taxon

A pan-family consensus PCR and a species-specific hydrolysis-probe assay may
sit under the same taxid while making entirely different claims.

An assay designed for the gorilla and chimpanzee lineages of SIV, screened
against all SIV, will appear to fail on most records. It has not failed; it is
being evaluated against a claim it never made.

An entry may therefore declare the taxa its design publication actually
claims — the smallest set of groups covering that range. A record counts if it
belongs to one of those groups **or to any taxon beneath them**.

!!! note "Ancestry rather than an enumerated list"
    Matching exact taxids alone excluded strain-level and unranked records
    beneath the listed species — approximately 90% of in-scope records for
    every scoped assay when measured. Traversing the taxonomy resolves this.

Out-of-scope records are screened and reported; they are excluded from the
statistics and counted separately, so nothing is discarded silently.

This is a curation judgement and it is incomplete. 34 validation cases still
require their scope to be read from the source publication; until then those
rows are marked rather than inferred.

## Published specificity claims

Many publications state that an assay does *not* amplify particular
near-neighbours. Those organisms are listed separately, retrieved deliberately,
and reported as predicted cross-reactivity.

They are never scored. A published specificity claim is something this tool can
comment on from sequence; it is not a performance figure the tool can assess,
and treating it as one would conflate two distinct questions.

---

## Silent failure of a retrieval query

A search query is a claim about the population against which an assay is being
evaluated. It can cease to be true without producing an error.

Four influenza entries used queries naming subtype taxids — the identifiers
NCBI formerly assigned to H5, H7 and H3 deposits. **NCBI ceased assigning
them**; new deposits are filed under the parent species.

Those archives consequently stopped growing years before the problem was
identified. The most recent H5 deposit was from 2021 and the most recent H7
from 2020. Seven H3 subtype taxids combined with hemagglutinin terms returned
**zero** records for 2024–2026, against 95,155 without the subtype
restriction.

No error was raised. The reports stated *"no evaluable records deposited since
Oct 2021"* beside each assay. That statement is **true**, and reads as a fact
about influenza deposition. It was a fact about the query: what had been
deposited was not visible to it.

No incorrect verdict was published, because the tool declined to judge those
assays and stated its cutoff, which is the desired behaviour. Four assays
nevertheless remained unassessable while the output appeared sound.

### Resolution

A single broad hemagglutinin search is shared across those assays, with each
entry restricting itself to records whose description names its own subtype.
The subtype appears in the record title and is not searchable through Entrez:
`H3N2[Title]` and `H3N2[Organism]` both return nothing, while the unqualified
term succeeds.

The match requires a left word boundary, since strain identifiers such as
`GKISBBBH74562` contain `H7` as a substring. This was established by
measurement rather than assumption.

!!! success "Directional verification of the filter"
    Narrowing a denominator can always produce an apparent improvement, so the
    test must be directional: with the filter applied the **proportion should
    rise while the record count falls**, as off-target failures are removed. A
    falling proportion would indicate that genuine target records are being
    excluded and the filter is incorrect.

    All four assays behaved as required, with no case of a falling proportion.
    The H5 assay reads `declining` at 49.8% without the filter and `stable` at
    96.2% with it; the filter therefore prevents a spurious decline on an assay
    in current use.

### Limits of automated detection

A check for other stale queries was implemented and then measured. It lists
archives whose most recent deposit is over 18 months old, weighted toward those
with a current sibling archive for the same organism. Run across the registry
it produced four candidates, **all four of which were correct** — a narrow gene
query under an organism depositing whole genomes will always appear stale
beside a broad one.

It would not have detected the influenza problem. The former H3 archive held
44,627 records against a query returning 44,633. These agree, because the query
was executing correctly and returning a population that had stopped growing.
**Comparing a query against itself cannot detect a change in database
annotation practice.**

Its actual value is a short worklist — 13 archives of 134 warranting manual
review — and no more than that is claimed for it.

For anyone operating a comparable system, this is the failure mode to monitor:
not a query that errors, but one that ceases to match how a database has begun
labelling its records.

---

## Records excluded from the statistics

Distinct from scope, and the most serious limitation of the method.

A record in which one primer has diverged is scored as a **failure**. A record
in which *both* have diverged yields no product and is excluded from the
denominator entirely.

Censoring is therefore correlated with the quantity being estimated. Across one
complete run, **65.7% of 2.72 million screened records did not reach the
statistics**. Each assay page reports this proportion for its own assay.

This may not be correctable without changing the estimand. Any proportion
reported here should be read together with the proportion of records excluded
to produce it.
