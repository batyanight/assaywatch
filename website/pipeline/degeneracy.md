# degeneracy

Computed from the oligonucleotide sequences alone, with no sequence database
involved, which is why it derives from the registry rather than the calls
table.

A degenerate primer is a mixture, and the number of distinct molecules in that
mixture dilutes the species matching any given template. This stage reports
pool size per assay and flags extreme cases; the largest in the registry
exceeds 10⁹ combinations.

It is **reported and never scored**. A degenerate base covering the record's
base is counted as a match, which is the purpose of degeneracy.
