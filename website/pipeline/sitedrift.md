# site drift

For flagged assays, identifies **which base** is responsible.

For each oligonucleotide position it compares detection among records carrying
a mismatch at that position against records that do not, groups records sharing
a mismatch pattern, and identifies the degenerate base that would cover most of
the observed variation.

This stage produces the directly actionable output: the base to substitute in a
redesigned primer.
