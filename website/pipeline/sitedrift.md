# site drift

For flagged assays, finds **which base** is responsible.

For each oligonucleotide position it compares detection in records with a
mismatch at that position against records without one, groups records that share
a mismatch pattern, and finds the degenerate base that would cover most of the
observed variation.

This stage gives the output you can act on directly: the base to substitute in a
redesigned primer.
