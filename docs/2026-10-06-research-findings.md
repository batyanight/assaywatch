# N. ceranae, Tasman-PCR and DWV scope — what was established, 2026-10-06/07

Three questions were looked at. Nothing below was written to `registry/`.

**This file replaces an earlier version of itself that was wrong.** That version
named the N. ceranae primer source as "Martin-Hernández et al. 2007, *Journal of
Invertebrate Pathology* 106:98-104, `10.1016/j.jip.2007.06.002`". The journal,
volume and pages were written from memory and are not that DOI's paper. The
correction is below. A companion file, `2026-10-06-session-summary.md`, was
deleted rather than corrected: it claimed the project's gates were passing when
`pytest` had been failing at collection, and reported a verifier figure produced
by a regressed reader.

## 1. N. ceranae — the 218MITOC pair

The two sequences are in hand and their source is NOT.

    218MITOC-FOR   CGGCGACGATGTGATATGAAAATATTAA   (28 nt)
    218MITOC-REV   CCCGGTCATTCTCAAACAAAAAACCG     (26 nt)

Read from **Kato et al. 2020**, *Sci Rep* 10:1118 (`10.1038/s41598-020-57909-8`),
Table 1, which is in `papers/`. Kato's table credits the pair to
"Martin-Hernandez et al. 2007" and that paper is still not in hand.

`papers/10.1016_j.jip.2007.06.002.pdf` was fetched in the belief that it was that
paper. It is not. It is Higes M, Martín-Hernández R, Garrido-Bailón E,
García-Palencia P, Meana A, "Detection of infective *Nosema ceranae*
(Microsporidia) spores in corbicular pollen of forager honeybees", *J Invertebr
Pathol* 97:76-78 (2008) — a three-page short communication with
Martín-Hernández as second author, which prints **no oligo-like run anywhere**
and never writes "218MITOC". Its own methods say only that "Nosema species was
determined by PCR as previously described (Higes et al., 2006)". So it is not the
primer source and cannot settle anything about these sequences. It is worth
keeping only as a provenance dead end, recorded here so nobody fetches it twice.

NO DOI is asserted for the real source. Per the registry rule, a DOI enters only
through `scripts/resolve_citations.py` and `scripts/check_citations.py`.

### The open question these primers raise

`registry/NOSEMA_bombi_SSU_Kato_2020.yaml` already records why the pair is not
entered: on every N. ceranae reference record checked, including RefSeq
XR_002966746.1 which Kato cites, both primers mismatch at their 5' ends — 2 bases
on the forward, the 5 terminal bases on the reverse — so 136 of 152
product-bearing records in a 350-record sample are called `fail` on 5'-end
penalties alone while their 3' ends match.

That pattern is itself informative: a uniform 5'-end mismatch across all
references is more consistent with a transcription or table-rendering difference
than with real drift, since drift does not organise itself at one end of both
primers at once. It cannot be settled without the original paper.

**Next step:** find the real Martin-Hernández 2007, verify its DOI through
Crossref, read its own table, and only then decide whether to enter the pair as
printed or corrected.

## 2. Tasman-PCR (Kwon et al. 2018) — out of scope, kept for review

Kwon et al. 2018, *R Soc Open Sci* 5:180870 (`10.1098/rsos.180870`), in `papers/`.
Read from the paper's Results and its Figure 1 and Table 1.

A triplex PCR that diagnoses the two Tasmanian devil facial tumour clones by
amplifying across tumour-specific **interchromosomal translocations**:

| target | product | breakpoint | what it detects |
|---|---|---|---|
| DFT1-A | 231 bp | Chr2_GL841420 × ChrX_GL867598, blunt end | devil facial tumour clone 1 |
| DFT2-A | 321 bp | Chr4_GL856969 × Chr5_GL861630, AG microhomology | devil facial tumour clone 2 |
| RPL13A | 520 bp | endogenous locus | host amplification control |

Reported performance, the paper's own: 331 of 344 confirmed DFTD tumours positive
(96.2%), 0 of 804 normal devils positive for DFT2-A and 3 (0.4%) faintly positive
for DFT1-A which the authors attribute to contamination, 0 of 27 non-DFTD lesions
positive. None of this was re-checked here.

**Why it does not belong in `registry/` as it stands.** The amplicon spans a
rearrangement in the *host's* genome. There is no pathogen sequence to screen, so
`target.taxid` would have to be *Sarcophilus harrisii* and the drift question —
has coverage fallen as GenBank accumulates strains — has no meaning for a somatic
translocation in a cancer clone. It is also the kind of host-genome marker
`scripts/removed_assays.txt` excludes.

Kept per the maintainer's decision to reassess later. No draft entries were
written: the four drafts an earlier note referred to were never found in this
checkout and may not exist.

## 3. DWV-A / DWV-B — variant node against species

Not resolved, and the decision needs a screen that has not been run.

`DWVA_polyprotein_Rossi_2024` and `DWVB_polyprotein_Rossi_2024` carry
`VARIANT_SCOPE`. Both target NCBI variant nodes: txid 2951794 (DWV-A) and
2498590 (DWV-B). The numbers already in the DWV-A entry's `notes_curator`, from
its 2026-10-06 screen of 1,970 records:

- A-labelled records: 68 of 223 span the site; 39 detect, 7 reduced, 22 fail
- B-labelled: 58 of 737 span; 2 detect, 56 fail
- unlabelled (species *Iflavirus aladeformis*, txid 3047792): 155 of 1,010 span;
  82 detect, 12 reduced, 60 fail, 1 indeterminate

About 80% of DWV deposits carry no A/B label, so a variant-node taxid retrieves
only the labelled minority — and the unlabelled majority is where most of the
detections are. That is the argument for scoping by species.

The argument against: Rossi et al. report by experiment that each test also gives
signal from the other variant's template, so a species-scoped entry would mix two
populations the assay is meant to tell apart, and the detected share would stop
meaning what the paper claims for it.

**What would settle it** is running the DWV-A oligos against the species taxid and
comparing detected-share among spanning records with the variant-node figures
above. That has not been done; the counts quoted here are the existing entry's,
not a new measurement.

## Files added to `papers/` (gitignored, local only)

- `10.1098_rsos.180870.pdf` — Kwon 2018, Tasman-PCR. Useful.
- `10.1016_j.jip.2007.06.002.pdf` — Higes 2008. NOT the N. ceranae primer source;
  see above before spending time on it.
