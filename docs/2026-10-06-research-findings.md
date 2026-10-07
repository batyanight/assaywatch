# N. ceranae, Tasman-PCR and DWV scope — what was established, 2026-10-06/07

Three questions were looked at. Section 1 was resolved on 2026-10-07 and produced two draft
registry entries (`NOSEMA_ceranae_SSU_Martin-Hernandez_2007`, `NOSEMA_apis_SSU_Martin-Hernandez_2007`);
sections 2 and 3 wrote nothing to `registry/`.

**This file replaces an earlier version of itself that was wrong.** That version
named the N. ceranae primer source as "Martin-Hernández et al. 2007, *Journal of
Invertebrate Pathology* 106:98-104, `10.1016/j.jip.2007.06.002`". The journal,
volume and pages were written from memory and are not that DOI's paper. The
correction is below. A companion file, `2026-10-06-session-summary.md`, was
deleted rather than corrected: it claimed the project's gates were passing when
`pytest` had been failing at collection, and reported a verifier figure produced
by a regressed reader.

## 1. N. ceranae — the 218MITOC pair: source found 2026-10-07

The pair is printed in Martín-Hernández et al. 2007, "Outcome of colonization of
*Apis mellifera* by *Nosema ceranae*", *Appl Environ Microbiol* 73:6331-6338,
`10.1128/AEM.00270-07` (Crossref metadata matches; open access, PMC2075036). Read
from its Table 2 (`https://pmc.ncbi.nlm.nih.gov/articles/PMC2075036/table/t2/`),
with the paper's underlined non-template tails in brackets:

    218MITOC-FOR   5'-[CGG]CGACGATGTGATATGAAAATATTAA-3'     product 218-219 bp
    218MITOC-REV   5'-[CCCGG]TCATTCTCAAACAAAAAACCG-3'

The two sequences are identical to Kato et al. 2020's Table 1, which is where this
file first read them. The table's footnote says "CG tails added to primers are
underlined" and the paper's methods say "G or GC tails were added to the 5' end of
all primers in order to make the melting temperatures of each primer set equal."
Table 2 also prints the N. apis pair 321APIS-FOR/REV, which carries 5' tails too.

**What this settles.** The uniform 5' mismatch on every N. ceranae reference (2 bases
forward, 5 reverse, 136 of 152 product-bearing records called `fail` on 5' penalties
alone) is those tails, which by design bind nothing in the target. An earlier version
of this file called it "more consistent with a transcription or table-rendering
difference". That was wrong: nobody had the paper, and the guess was not checked.
The schema already models this (`tail_5prime` in `assaywatch/schema.py`: part of
`seq` as ordered, left out of the matching sequence, because a tail mismatches every
record by design).

**Dead ends, so nobody fetches them again for the primers:**

- Higes et al. 2007, *J Invertebr Pathol* 94:211-217 (`10.1016/j.jip.2006.11.001`),
  "Experimental infection of *Apis mellifera* honeybees with *Nosema ceranae*". Read in
  full; it prints only 16S sequencing primers (MICRO-F, MICROCE-R, INTER-FOR/REV). Its
  only `mitoc` text hits are "mitochondria".
- Higes et al. 2008, *J Invertebr Pathol* 97:76-78 (`10.1016/j.jip.2007.06.002`), the
  PDF in `papers/`: three pages, no oligo-like run, never writes "218MITOC".
- Nabian et al. 2011, *Iran J Parasitol* 6(3):89-95: uses the same pair under the same
  names and describes it as its own design. It is a reuse, not the origin. An earlier
  note in the registry credited it as the designer and pointed at Higes 94:211 as the
  source; both statements were wrong and were corrected.

The DOI is recorded here from Crossref metadata. In the registry it enters as
`doi_verified: false` until `scripts/resolve_citations.py` passes it.

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
