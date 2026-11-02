# retrieve

Retrieves nucleotide records from GenBank for each target and archives them.

Assays sharing a target and gene search share one archive: 218 assays map onto
**115 archives**, so a shared target is retrieved once rather than once per
assay. A further 10 archives hold the off-target neighbours that published
specificity claims are checked against, and 20 are orphans left by queries that
have since been changed — 145 directories on disk in total, of which 115 are
what the assays are screened against.

Retrieval is **incremental**. Each archive records when it was last updated and
requests only records modified since. Complete records are retained rather than
only the primer-binding regions, which is what makes re-scoring inexpensive: a
threshold change re-reads local storage rather than re-querying GenBank.

!!! warning "Failure mode concealed by this stage"
    A search is a claim about the population against which an assay is
    evaluated, and it can cease to be true without producing an error. Four
    influenza assays used searches naming subtype identifiers that NCBI ceased
    assigning; those archives stopped growing years before the problem was
    identified, while the reports stated something true and misleading — "no
    recent records" — about the organism rather than about the search.
    [Scope and retrieval](../scoping.md) documents the case.

**Output:** compressed FASTA archives and a record of each archive's last
retrieval date.
