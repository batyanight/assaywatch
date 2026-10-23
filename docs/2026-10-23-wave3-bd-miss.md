# Wave 3: why the Bd failure is missed (2026-10-23)

`CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004` as of 2017-03-31 is a documented
failure (`docs/validation-cases.tsv`, Mutnale 2018) that the tool calls `stable`. Three
earlier explanations were tested and failed: a statistics problem (wave 1 changed no
verdict), a denominator problem in the recent window (wave 2: the `diverged` records
were 2014 JAM81 mRNAs, not ITS), and "the data is not in GenBank". The last is half
true, and the other half is the finding.

## Source

Mutnale et al. 2018, *Sci Rep*, doi:10.1038/s41598-018-28304-1, PMC6031667. Full text
and supplement from Europe PMC (`/PMC6031667/fullTextXML`, `/supplementaryFiles`).
Their own sequences are GenBank **MG252074-MG252130**. Supplementary **Table S1** lists
33 accessions included in the TaqMan-probe-site analysis; **Table S2** lists 17 for the
qPCR reverse-primer site. Not entered into `registry/` or `papers/`; read for this
investigation only.

## Every record is in the archive, and almost every one is dropped

| set | listed | in the Bd archive | deposited before 2017-03-31 | screen call |
|---|---:|---:|---:|---|
| Mutnale's own, MG252074-MG252130 | 57 | 57 | 0 (2018) | 57 `truncated` |
| Table S1, probe site | 33 | 33 | 29 | 30 `truncated`, 3 `detect` |
| Table S2, reverse-primer site | 17 | 17 | 11 | 17 `truncated` |

Retrieval is not the problem. The records are deposited ITS sequences of 241-470 bp
made with other primers, and **none of the truncated ones contains the Boyle forward
primer site**: the deposits begin downstream of it. The reverse site is present in all
of them, mostly with 0-1 mismatches.

## Where the deposits begin relative to the probe

Placing the probe by its offset from the reverse site (97 nt upstream, from a
full-amplicon reference, MW147112.1), the 33 Table S1 records split four ways:

| probe region in the deposited record | records |
|---|---:|
| cut by the record start: only 4-10 of its 15 nt deposited | 24 |
| entirely upstream of the record start | 3 |
| present, with the offset shifted (see below) | 3 |
| present, full amplicon in the record | 3 |

Many studies trimmed at the same point — the reverse site sits at position 88 in record
after record, including Mutnale's own 57, whose deposits begin 9 nt into the probe. For
27 of the 33, GenBank does not hold the whole probe site, so no in-silico screen can
judge the probe on them, whatever its statistics.

## The records that do carry evidence, and why it was discarded

**Three records carry a real probe-site deletion and were deposited years before the
as-of date:**

| accession | haplotype | deposited | gapped alignment of the probe |
|---|---|---|---|
| AB435217 | JP07 | 2009-11-03 | 1 substitution + 2-nt deletion at the probe's 3' end |
| JN870747 | CN07 | 2012-02-21 | 1 substitution + 2-nt deletion at the probe's 3' end |
| AB723981 | JP45 | 2013-06-04 | 1 substitution + 2-nt deletion at the probe's 3' end |

(`assaywatch.gapped.align`, cost 3 in each case.) A two-base deletion at the 3' end of
a 15-mer MGB probe is the end the minor-groove binder is conjugated to; that site should
not report. The tool threw this evidence away **twice**:

1. **Amplicon-level, not site-level.** Each record contains the reverse primer and the
   probe site but starts after the forward primer, so it is `truncated` and leaves the
   denominator as a fact "about the deposit, not the assay". But the part of the record
   that is present is the part that fails. Whether the forward primer was sequenced says
   nothing about whether the probe binds.
2. **Ungapped.** `README.md`: "Gaps are not modelled." Even in a full-length record,
   ungapped matching sees this deletion as a run of shifted mismatches rather than a
   deletion at the probe's 3' end.

**The three full-span records are the Brazilian haplotypes BR11, BR15, BR21** (Schloegel
2012, JQ582896/914/932). Each has one A:A mispair 2 nt from the probe's 3' end, scored at
1.0 and called `detect`. By unmodified-DNA nearest-neighbour thermodynamics (primer3,
`config.yaml` `thermo_conditions`) it costs **-1.3 C** on a 48.8 C duplex, so `detect`
agrees with the thermodynamics the pipeline has. primer3 does not model the MGB moiety,
and whether the conjugate sharpens a 3'-proximal mismatch into lost signal is exactly
what this pipeline cannot say. No number is claimed for it here. Note that
`docs/validation-cases.tsv` also records Longo 2013 finding no probe-site polymorphism
in the divergent Brazilian strain LFT001_01.

## What this means

- **The Bd @2017 miss is not a statistics problem and not a denominator problem.** It
  is two modelling choices: scoring only records that hold the whole amplicon, and
  matching without gaps.
- **The `fails` label is sound but rests on less sequence evidence than its note
  implies.** "30 GenBank ITS haplotypes with TaqMan probe-site mutations": for 27 of the
  33 Table S1 records the deposited sequence does not contain the whole probe site. The
  strong sequence evidence is the three 3'-end deletions above. The wet-lab evidence (33
  qPCR positives vs 119 by nested PCR) does not by itself separate sequence mismatch
  from the nested protocol's greater sensitivity. This is for the maintainer to weigh;
  the label is not changed here.
- **Tier-2 could not have caught this by tuning anything.** Every threshold, window or
  denominator switch operates on records the screen has already discarded.

## The fix this points to (proposed, not built)

**Site-level coverage alongside amplicon-level calls.** For each oligo, judge every record
that contains that oligo's binding site — truncated or not — with a gapped alignment, and
report the share of those sites that would fail. An amplicon needs all three sites in
one deposited record; a site needs only itself. For Bd that turns three discarded
records into the signal the validation case describes.

It belongs beside `sitedrift.py`, which already reports per-position drift but only on
scored amplicons. Open questions for its design doc:

- how to locate a site in a truncated record without the partner primer to anchor it
  (the reverse site anchors the probe here; a lone probe needs its own credibility test,
  and the archive-scale multiplicity problem from wave 2 applies with force to a 15-mer);
- `gapped.py` is a measurement spike today, documented as never scored; using it to
  score is a decision, with `scripts/indel_check.py`'s finding (indels explain under 1%
  of evaluable records for all but three assays) as the prior evidence;
- how a site-level failure share enters a verdict, if at all, versus being reported
  beside it as degeneracy and thermodynamics are.
