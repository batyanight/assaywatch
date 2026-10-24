# The GenBank-availability ceiling: it is 11, not 9 (2026-10-24)

`docs/2026-10-22-lineage-plan-salvage.md` §1 carried a claim from the closed PR #3: if
Lotta 2019's fusiform-gametocyte *Leucocytozoon* sequences were not in GenBank before the
2016-12-31 cutoff, the two Hellgren `fails` rows in `docs/validation-cases.tsv` are
uncatchable by any GenBank screen and every "N of 11" in the project is quoted against a
denominator of 9. It was Phase 0's go/no-go and had never been run. It is run here, with
no network beyond fetching the paper: the archives carry deposition dates.

## What Lotta 2019 actually shows the mismatch on

Lotta et al. 2019, *IJP: Parasites and Wildlife* 9:159 (10.1016/j.ijppaw.2019.05.002,
PMC6526250), Fig. 4: "the primer HaemR2L did not completely match with the mtDNA
sequences obtained using the mtDNA genome amplification protocol used for *L. pterotenuis*
(in part) (GenBank No. KM610046). Indeed, the base pairs at the 3′ end of the primer, as
well as the two last base pair of the 5′, did not match with the cytb gene sequences
obtained from the mtDNA genome of *L. grallariae* (MK103895) nor *L. neotropicalis*
(MK103894)." The two new species' genomes are 2019 deposits. **KM610046 is not**: it is
Lotta et al. 2015's partial mitogenome of *L. pterotenuis*, the same fusiform-gametocyte
lineage, and the paper's own primer-affinity figure is drawn against it.

The partial cytb fragments the Hellgren primers DID amplify from those birds (KM272250 in
2015; MH909275/MH909276 and KY646032 later) are the co-infecting roundish-cell parasite,
which is the paper's point: the nested PCR recovered the wrong one of two parasites in
each sample.

## What GenBank held on 2016-12-31, from the archive on disk

`data/retrieved/195944/all/2026-10-04.meta.tsv.gz` (the Leucocytozoon group, 7,904
records) has 1,530 records created on or before 2016-12-31. Among them, every
Lotta-group mitogenome from before the cutoff, with the call the current screen gives it
for the round the case names (`results/screened/195944/all/2026-10-04.tsv`):

| accession | created | what | `Leucocytozoon_cyt_c_Hellgren_2004` (HaemFL/HaemR2L) |
|---|---|---|---|
| KM610046 | 2014-12-24 | *L. pterotenuis* mtDNA, **the fusiform lineage Fig. 4 is drawn on** | **`fail`**, penalty 4; HaemR2L mismatches at 12 and **2** from the 3′ end |
| KM610045 | 2014-12-24 | *Leucocytozoon* sp. L_GRQUI_01 mtDNA (the *G. quitensis* fusiform parasite, Lotta 2015) | `reduced`, penalty 2 (HaemFL 21,20,8) |
| KT162002 | 2016-05-04 | *Leucocytozoon* sp. MAP-2016a mtDNA | `reduced`, 2.5 |
| KT162003 | 2016-05-04 | *Leucocytozoon* sp. MAP-2016a mtDNA | `reduced`, 1.5 |
| KT162004 | 2016-05-04 | *L. fringillinarum* mtDNA | `fail`, 4 (HaemFL 8,2) |
| KM272250 | 2015-02-09 | 476 bp cytb amplified WITH the Hellgren primers (roundish co-infection) | `no_amplicon` / `no_site` (the fragment is inside the amplicon) |

So the sequence that documents the failure **was in GenBank two years before the
cutoff, with exactly the 3′-end HaemR2L mismatch the paper describes, and the screen
calls it `fail`.** The in-silico route was open. The ceiling is 11.

For the first-round entry (`Pan_hemoparasite_cytochrome_c_Hellgren_2004`, HaemNFI/HaemNR3,
group `5819/q49e818bd88`): KM610046 `reduced` (2), KM610045 `fail` (4.5), KT162004 `fail`
(8), KT162002 `reduced`, KT162003 `detect`. Also visible, also mixed.

## What this does and does not change

- **The denominator stays 11.** Every "5 of 11" in `docs/2026-10-23-baseline.md` and
  `config.yaml`'s header is quoted against a reachable ceiling. The PR's worry was
  reasonable and is answered by the archive, not by argument.
- **The lineage-conditional estimand still cannot name this failure.** KM610046 is taxid
  1587510 (*L. pterotenuis*), two records in the whole archive; KM610045 is
  `Leucocytozoon sp.` (1504291), the unclassified bucket. At `lineage.min_records_per_lineage:
  30` and `group_at_rank: species`, no lineage verdict can form on one or two records.
  The catch the tool actually makes (`low coverage` @2016-12-31 for the Leucocytozoon
  round, credited in the baseline) is the **pooled** call, which is the estimand the M1
  revert was measured on. That is the taxid-resolution ceiling of
  `docs/2026-10-18-recalibration.md`, a different limit from this one, and it still stands.
- **The first-round row is a genuine miss, not a ceiling.** `Pan_hemoparasite` @2016-12-31
  reads `stable` on records that include a `fail` and a `reduced` on the fusiform
  lineage. The scope of that assay is eight avian haemosporidian taxids and its pooled
  share is dominated by Plasmodium/Haemoproteus records the primers match well; two
  Leucocytozoon mitogenomes cannot move it. That is the pan-family dilution the review
  named, and it is correctly counted against the tool.
- **A note is added above the two rows in `docs/validation-cases.tsv`** saying the ceiling
  was checked and the sequences were available. Nothing scored changes: this doc reads
  the archive and the frozen screens, and touches no threshold.

## Method, so it can be repeated without this file

    # the paper
    curl -s 'https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6526250/fullTextXML'
    # the archive's pre-cutoff records
    gzcat data/retrieved/195944/all/2026-10-04.meta.tsv.gz | awk -F'\t' 'NR>1 && $3<="2016-12-31"'
    # the calls on them
    rg 'KM610046|KM610045|KT16200[234]|KM272250' results/screened/195944/all/2026-10-04.tsv
    # first-deposit dates straight from NCBI, for the record
    efetch -db nuccore -id KM610046,KM610045 -format gb | rg '^LOCUS|JOURNAL'

`created` in the meta file is NCBI's `CreateDate`, i.e. first public release, so a
record's later revision (KM610046 was updated 2017-02-13) does not move it past the cutoff.
