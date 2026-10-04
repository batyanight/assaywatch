# First full run: review, fixes, and open decisions (2026-10-04)

The first end-to-end run (2026-10-03/04, 65 jobs, 33 min) reported **66 of 113
assays drifting**. That is not plausible for a registry of published assays, so
the report was read before anything new was built. Most of the 66 come from five
causes, none of which is drift. Four are fixed; one needs a decision.

## Fixed

| problem | effect | fix | commit |
|---|---|---|---|
| **Amplicons only searched on the plus strand.** `screen_record` paired a forward site on + with a reverse on −, so a target read the other way was never found. | Every minus-strand gene in a genome record (pox, herpes, adeno, Bd scaffolds) and every antisense deposit became `no_amplicon`, or a `fail` on a chance pair. 79 of 84 fixtures changed call when reverse-complemented. | Both orientations; coordinates stay on the plus strand; an invariance test over every fixture. | `7d3bda0` |
| **Three wrong taxids.** | Bsal (1430836) was *Perigonica* moths: 19 COI barcodes, reported as a coverage gap. Both lyssavirus assays were on 11270 = Rhabdoviridae: their 16% "drift" was the whole family. | 1357716 and 11286. `scripts/check_taxids.py` now checks every taxid against NCBI (ICTV renames recognised). 0 mismatches. | `ec2a05c` |
| **22 assays with no taxid**, reported as "the sequence data does not exist". | Never searched. Includes Ophidiomyces, one of the five assays planned for promotion. | `resolve_citations.py` run once (Phase 0): 21 filled. TINC has no NCBI taxon. Gap table now says "not searched (no taxid)" and skips deprecated assays. | `ec2a05c`, `ed2dde7` |
| **Bacteria had no recent window.** Gene-level nuccore deposits stop around 2012. | E. coli, Salmonella, Shigella, Yersinia, Leptospira: nothing to compare against. | `asm` retrieval groups from NCBI Datasets, 20 complete genomes per release year, cut to the amplicon. | `54715a6` |

## Needs a decision

### 1. Chance primer pairs in long records (`scoring.max_pair_evalue`)

The six-mismatch search budget finds drifted sites, but on a long record it also
finds chance ones: an 18-mer has a ≤6-mismatch site every few kb of random
sequence, so a genome holds hundreds of facing pairs in amplicon range. In the
first run **23.5% of all `fail` calls (67,601) had both primers at ≥5
mismatches**. For Pan-herpes terminase, adenovirus Pan-Pol round 2 and lyssavirus
round 2, essentially none of those had an amplicon length matching any `detect`
call of the same assay (0–1 of thousands), while their lengths spread across the
whole 50–3000 bp range. They are chance pairs, counted as assay failures in the
drift denominator.

Every amplicon now carries `pair_evalue` (`assaywatch/chance.py`): the expected
number of pairs at least this good in a random record of the same length and
composition. Perfect pair in a 5 Mb genome ≈ 6e-12; six-and-six in a genome ≈
1600; five-and-five in a 1 kb gene record ≈ 0.002. Assembly extraction already
uses it (0.01). **Scoring does not** (`max_pair_evalue: null`), because turning it
on turns chance `fail`s into `no_amplicon` and moves drift numbers.

*Recommendation:* set `scoring.max_pair_evalue: 0.01`. The cost is that a real
site degraded to six mismatches in both primers inside a long genome stops
counting as a failure; in a genome that site cannot be told apart from noise
anyway. The 2026-10-04 rerun reports the E-value on every row, so the effect can
be measured before choosing (see "Rerun" below).

### 2. What "drifting" means

`drift.py` describes its question as "is the share falling", and its docstring
assumes "baselines are usually near 100 percent". The rule it applies is
absolute: drifting when the recent upper bound is below 90%. Many baselines are
far from 100%, for reasons that are about scope rather than time:

* the assay targets a narrower lineage than the retrieval taxid (Takehisa 2009
  is for gorilla/chimpanzee SIV, screened against all SIV; Feldman 2006 is
  "Turtles only", screened against all *Mycoplasma*);
* pan-family degenerate assays never covered the whole family.

SIV Takehisa, for example: 0% recent, 0% baseline, change −1% to −1%. That is
an assay outside its scope, not an assay that drifted.

*Recommendation:* split the status. **Declining** when the Newcombe interval for
the change from baseline lies entirely below zero (and the recent share is under
threshold); **low coverage** when the recent share is under threshold with no
significant change. Separately, a per-assay narrower target taxid for
lineage-specific assays. Both are changes to what the report claims, so neither
was made.

### 3. Registry oligo typos found by the indel check

`scripts/indel_check.py` (69,007 sampled `fail` / one-primer `no_amplicon`
calls) found that a clean single-base indel explains under 1% of evaluable
records for every assay but three, so gapped scoring is off the roadmap. The
three outliers are the same indel at the same position in nearly every record,
which is a transcription error, not biology:

| assay | oligo | registry | every record | effect |
|---|---|---|---|---|
| `SARCOCYSTIS_18S_5_8s_rDNA_long_2010` | reverse | `GCCATTTGCGTTC`**`C`**`AGAAATC` | `GCCATTTGCGTTCAGAAATC` | 98% of evaluable records fail |
| `CIRCOVIRUSES_..._Mankertz_2000_round1` | forward | `GTGTT`**`T`**`CAC...` | `GTGTTCAC...` (incl. AF086834, 1998) | ~1.3% |

Both need checking against the papers before editing the registry.

### 4. Cloning tails

`Canine_distemper_virus_specifi_F_gene_need_to_order_2` has restriction-site
tails in both primers (`GGATGTCGAC…` SalI, `GGATGCGGCCGC…` NotI): 0 of 3,990 CDV
records match. The schema has no field for a 5' tail. Either strip them in the
registry (noting it in `notes_curator`) or add `tail_5prime` to `Oligo` so
`matching_seq` excludes it.

### 5. Five DOIs that resolve to the wrong paper

Left unverified by `resolve_citations.py`: Apicoplast 23S (→ a nematode paper),
Entamoeba 18S (404), Ferlavirus and both Sunshine virus Hyndman 2012 entries
(→ a *Mycoplasma* paper).

### 6. Assembly years

Assemblies are dated by release date, which is what `created` means for nuccore
records too, so the two sources are comparable. But an NCTC strain collected in
1952 and sequenced in 2018 is then 2018 data. The collection date is kept in
each record's title if the drift window should ever use it instead.

## Also done today

* `screen --workers N`: byte-identical output for any N; big archives get more
  cores and start first (`803a768`). 5 min → 1:37 on the flavivirus archive.
* `screen --thermo` / `thermo: true`: per-oligo duplex Tm and ΔTm from primer3,
  never scored (`ef22dca`). Median worst ΔTm on the flavivirus archive: detect
  −5.0 °C, reduced −11.7 °C, fail −16.8 °C.
* `scripts/indel_check.py`, `scripts/check_taxids.py`: registry QA tools.

## Rerun

The cached screens predate the strand fix and the corrected taxids, so the
pipeline was rerun on 2026-10-04 with everything above (log: `snakemake4.txt`).

## Decisions taken (2026-10-04, evening)

All six recommendations accepted. Decisions 1, 2, 4, 5 and 6 are done
(`7ad6306`, `fbde41e`, `d407345`, `880252c`). For decision 3, the papers are not
in PMC, so both entries are flagged `OLIGO_SEQ_SUSPECT` instead of edited
(`6fe0afd`). Bd Boyle 2004 promoted to `active`.

Final rerun (21 min, log `snakemake5.txt`): **134 assays: 27 declining,
37 low coverage, 5 watch, 20 insufficient data, 6 no recent data, 39 stable.**
Boyle 2004 stable. Bsal and Ophidiomyces ITS2 have too few rDNA records to judge
(12 and 196 fetched): for these the coverage gap is the finding.
