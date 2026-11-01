# The registry

One YAML file per assay; 218 in total. Each records the oligonucleotide
sequences, target organism, chemistry, product size and source publication.

Entries are not accepted on assertion:

- **No citation is entered from memory.** A DOI is recorded as unverified and
  only Crossref can promote it. An assay whose citation cannot be confirmed is
  held and is neither screened nor published.
- **Sequences and product sizes are measured rather than transcribed.** Where
  a measured product length disagrees with the published value, the entry
  retains the measured value and records the discrepancy. A published size is
  typically a band read against a ladder; the measured value is computed from
  primer binding positions.
- **Known problems are recorded in a controlled vocabulary** rather than prose,
  so that they can be filtered. Nineteen assays carry a flag sufficient to
  withhold any verdict.

**Output:** validated entries and the set of organisms and genes to retrieve.
