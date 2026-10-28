# The seven queued PDFs arrived, and the Hel1 question settles the other way

2026-10-28. Every paper on the Desktop fetch list is now in `papers/`, including two I
renamed out of `~/Downloads` into their `doi_stem` names (Csordas 2004, Tsukamoto 2008).
Three things came out of the re-reads, and only one of them is what the list predicted.

## Hel1's published base is G, so the stored C is a modification

`papers/10.1016_s0890-8508_95_90962-1.pdf` is now a readable 630 KB copy of Neill & Seal
1995, replacing one of 64 KB whose text layer held no nucleotide run at all. Its Materials
and Methods prints:

> Hel1 (5'-GTCCCAGTATTCGGATTTGTCTGCG-3')

Twenty-five bases, identical to the registry's Hel1 except the last, which is **G**.
`scripts/verify_oligos_against_paper.py` reports the same thing from the other end, as
`near:1` — "paper prints GTCCCAGTATTCGGATTTGTCTGCG (1 edit away)".

So **three independent sources print G**: the design paper, Reid 1999's table, and the
OCR'd Elsevier deposit. The stored G was never our transcription error, and the question
the fetch list framed as "confirms or reverses a decision already taken" is reversed. The
published primer carries a single 3'-terminal mismatch against every one of the 16
Caliciviridae records that give its product, and the C-form is a **deliberate
modification**, not a typo fix.

The maintainer's decision today keeps the measured C-form live: over the whole
152,379-record archive the G-form yields no product in any record and the C-form yields 16,
every one at the 357 bp both papers state. An assay stored as published that detects
nothing describes the literature worse than one stored as it works with the departure
disclosed — the 2026-10-23 adjudication's lesson, that the paper wins for a SEQUENCE and
loses for a CORRECTION. The flag changes accordingly, from `oligo_sequence_uncertain` to
`oligos_modified`: nothing about the reading is uncertain any more, which also removes the
only OPEN flag that was keeping this entry out of consideration for `active`.

**What no document on disk can settle**: whether the published G is a typesetting error or
the primer those authors really used. They report the assay amplifying a ~350 bp fragment
from every calicivirus tested at annealing temperatures of 55 °C and 60 °C, which a
3'-terminally mismatched primer would not do.

## The queue's one new CONFIRMED row is not a case

`scripts/check_candidate_identity.py` over the `mismatch`/`redesign` rows now reads **2
CONFIRMED, 1 VARIANT, 10 UNCONFIRMABLE**, against 1 / 1 / 11 on 2026-10-27. The new
CONFIRMED is 10.1016/j.mimet.2008.12.003 on `Salmonella_invA_Rahn_1992` — and reading it
closes the row rather than opening a case.

The queue (and the fetch list) called it "Malorny et al. 2009". It is **Süß, Flekna, Wagner
& Hein**, *J Microbiol Methods* 76:316–319, and it is a methodological study, not a field
report. They built a synthetic 100 bp template flanked by Rahn's primers 139/141, then
designed **eight forward primers and six probes carrying deliberate mismatches** and
measured what each did to quantification. Nothing in it reports the Rahn assay failing on
anything; our oligos are printed because they are the scaffold of someone else's
experiment. Identity CONFIRMED, case NOT, for the same reason two rows closed on 2026-10-27:
the content, not the access.

**It is still evidence, in the place this project actually needs some.** Its finding is
that a small number of mismatches in the primer binding region alters the amplification
curve only slightly, giving a quantification error up to 63%, while mismatches in the probe
region are worse in kind: up to 33% error with more pronounced curve effects. That is a
labelled mismatch→effect dataset on a controlled template, which is what the `reduced`
band asserts without evidence and what C2's priors would be fitted against — the same role
Kwok 1990 and Stadhouders 2010 play in `config.yaml`. Recorded in the Bayesian plan's
corpus section rather than in a verdict.

## The two influenza/E. coli redesign rows close on content too

- **Tsukamoto 2008** (10.1128/jcm.02386-07, the row that had a persistent Europe PMC HTTP
  500) prints **29 oligos** and not one of ours. Expected, and the fetch list said so in
  advance: our stored matrix reverse is a *redesign* of Spackman's with two fixed-base
  substitutions, so a paper reprinting Spackman's original is testing a different primer.
- **Csordas 2004** (10.1111/j.1472-765x.2004.01559.x) prints **12 oligos**, none ours, for
  the E. coli O157 hlyA and Yersinia rows.

Both are now `UNCONFIRMABLE` on content rather than on access, which is the better kind of
closed: no document will change them.

## Also today

The five conditions values that had to be deleted rather than fixed are gone, each with
the reason in its entry: `CMV_UL55_gB_Deckers_2009`'s magnesium (the 46 °C pan-herpes DPOL
mix, where this entry is the 45 °C TaKaRa long PCR), the three Sigrist
`ORTHOBORNAVIRUS_XP_*` magnesiums (the conventional arm's self-mixed Taq buffer, where
these entries are the one-step ToughMix probe assay) and
`LEPTOSPIROSIS_Flagillar_filiment_Prote`'s annealing temperature (three programmes in the
paper, none attributable to the flaB pair). The first attempt at them is itself worth
recording: a quoted `notes_curator` scalar that CONTAINS `'` at a line end cannot be
appended to by searching for the closing quote, and doing so cut one entry's note in half.
A YAML round trip, which `resolve_citations.py` and `retire_merged_taxids.py` already use,
is the way to make a structural registry edit.

## A held-out row proposed, and the file spent a second time

Quackenbush et al. 1998 (*Virology* 246:392–399) is in `papers/` as one of the ten
completeness papers, and it turns out to be a tier-2 candidate rather than a completeness
read: it USES the VanDevanter pan-herpes DPOL nest the registry holds — cites it by name,
and all four oligos occur verbatim in its text — and reports a ~250 bp round-2 product
sequenced from five green turtle fibropapillomas, **53% identical to its nearest relatives
across the 183 bp between TGV and IYG**. A pan-family assay amplifying a herpesvirus half
divergent from anything then known is the clearest `works` reading available. The row is
written into `docs/validation-cases-heldout-2.tsv` marked PROPOSED and awaiting the
maintainer's verdict, with the arguable part stated: the same paper reports tumour-free
skin and two olive ridley turtles as PCR negative, which is a true negative and not a
failure.

**Checking that the row parses scored the whole file, so set 2 is now partially spent and
this is the disclosure.** Three rows, read 2026-10-28:

| case | expect | status | verdict |
|---|---|---|---|
| `Cryptosporidium_18SrDNA_Xiao_1999_round2` | works | watch | agrees |
| `MONKEYPOX_dsDNA_G2R_generic_TaqMan_Li_2010` | works | declining | **DISAGREES** |
| `Pan_HERPES_dsDNA_Polymerase_round2` | works | low coverage | weaker |

**One false alarm in three held-out rows, and it is the informative one.** Mills 2022
validated the G2R generic monkeypox assay on 2022 outbreak clinical specimens across many
sample types, and the shipped config calls that assay `declining`. The development set's
false-alarm rate is 4/32 = 12%; this is 1/3 on three rows, so the interval (95% CrI
4%–82%) says nothing and the point of recording it is that the number exists and was not
chosen. Nothing in `config.yaml` changed because of it, and under the file's own rule
nothing may.

What it does say is where to look next: the G2R generic assay is flagged on sequence while
a clinical validation says it works, which is either the denominator problem this project
already records — 2022 outbreak genomes are a small, recent slice of a large archive — or a
real disagreement worth a journal of its own. That is a measurement, not a tuning
opportunity.
