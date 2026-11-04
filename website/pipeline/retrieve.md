# retrieve

Fetches nucleotide records from GenBank for each target and archives them.

Assays that share a target and gene search share one archive. 218 assays map
onto **115 archives**, so a shared target is fetched once and not once per
assay. A further 10 archives hold the off-target neighbours that published
specificity claims are checked against, and 20 are orphans left by queries that
have since changed. That makes 145 directories on disk, of which 115 are what
the assays are screened against.

Retrieval is **incremental**. Each archive records when it was last updated and
asks only for records modified since. Complete records are kept, not just the
primer-binding regions, which is what makes re-scoring cheap: a threshold change
re-reads local storage and does not re-query GenBank.

!!! warning "A failure this stage can hide"
    A search is a claim about the population an assay is evaluated against, and
    it can stop being true without raising an error. Four influenza assays used
    searches that named subtype identifiers NCBI had stopped assigning. Those
    archives stopped growing years before anyone noticed, and the reports said
    something true but misleading, "no recent records", about the organism when
    the problem was the search. [Scope and retrieval](../scoping.md) documents the
    case.

**Output:** compressed FASTA archives and a record of each archive's last
retrieval date.
