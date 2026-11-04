# The registry

One YAML file per assay, 218 in all. Each records the oligonucleotide
sequences, target organism, chemistry, product size and source publication.

Entries are not taken on trust:

- **No citation is entered from memory.** A DOI is recorded as unverified and
  only Crossref can promote it. An assay whose citation cannot be confirmed is
  held back, and it is neither screened nor published.
- **Sequences and product sizes are measured, not copied.** Where a measured
  product length disagrees with the published value, the entry keeps the
  measured value and records the difference. A published size is typically a
  band read against a ladder; the measured value is computed from primer binding
  positions.
- **Known problems are recorded in a controlled vocabulary**, not prose, so they
  can be filtered. Nineteen assays carry a flag serious enough to withhold any
  verdict.

**Output:** validated entries and the set of organisms and genes to retrieve.
