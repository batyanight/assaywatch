# Held-out case collection, 2026-10-24: what went in, what did not, and the gap that stayed open

Wave 4 left `docs/validation-cases-heldout.tsv` empty on purpose, with a collection
target of **15-20 cases, at least 5 with `mechanism: drift`**. This is the first sweep
against it: three passes over the 200 live registry entries, one per third, each
confirming assay identity from printed primer names or sequences before accepting a
paper. **The file has not been scored and must not be until the thresholds are final.**

## Result, and the honest shortfall

| | target | got |
|---|---|---|
| rows | 15-20 | **31** |
| distinct assays | - | 30 |
| distinct papers | - | 17 |
| `mechanism: drift` | >= 5 | **2, and both are inferences rather than the paper's own word** |

So the count is met and **the drift target is not**. That is the finding, not a
bookkeeping note: the drift-shaped literature for these assays is mostly
lineage-coverage literature. Most registry entries are degenerate pan-family consensus
PCRs from before 2010, and when a later paper reports one failing, it almost always
failed on a lineage that already existed when the assay was designed. The development
set has exactly one drift case; the held-out set now has two, both from one in-silico
monkeypox paper, and in both the word drift is mine and not the authors'. **The drift
flag still has almost no ground truth, and no amount of reading these papers will fix
it.** What would: assays designed against a target that demonstrably changed afterwards,
which in this registry means the 2020s entries, and they are too new to have follow-up.

Also worth stating because it limits what the set can price: 8 of the 30 assays already
carry a development-set row, so their thresholds were tuned with those assays in view.
Those rows say `NOT INDEPENDENT` in the `source` field. And the 31 rows are not 31
events: 17 papers, and several papers contribute a whole nested family on one sample set
(Lee 2021 gives six rows, Yang 2022 four, Song 2023 three). Those rows say `ONE EVENT`.
Counting rows as events would overstate the set by roughly a factor of two.

## What the rows are worth, by kind

- **The strongest pair is Lee 2021** (`10.1186/s12985-021-01694-x`): in three Bornean
  elephant calves with sequence-confirmed EEHV1A, the pan-herpes consensus polymerase
  and terminase assays detected nothing while the pan-EEHV polymerase assay made the
  diagnosis. That is four `fails` rows and two `works` rows from one experiment, and the
  pairing is what makes it evidence: the same samples, a specific assay and a
  pan-family assay disagreeing, with the sequence to say who was right.
- **A genuine ring trial**, Fischer 2013 (`10.1371/journal.pone.0058372`): 16
  laboratories, and the original Vazquez-Moron pan-lyssavirus protocol, run by its own
  designer, generally failed on the Nigerian Africa 2 sample. External quality
  assessment reports are the best shape of evidence this project can get and there is
  only one in the whole set.
- **Two independent FAP59/FAP64 failures** (Vanmechelen 2023, Matias 2024), which matter
  because that assay's bench panel is already the project's main scoring calibration set.
- **The three monkeypox rows** (Song 2023, `10.3390/v15122327`) are an in-silico
  alignment study, not a bench result: 5,210 genomes, and the Meyer ATI set has zero
  perfect alignments while the two Kulesh sets have 51 and 72. Treat as a different
  class of evidence from a wet result, closer to what this tool itself computes.

## Leads not promoted, with what each is missing

Paywalled, worth a manual look through the NYU subscription:

| lead | DOI | why it matters |
|---|---|---|
| Furuyama 2018, subpopulation primers for diverse HA genes | 10.1128/jcm.00985-18 | the best candidate anywhere in the sweep for a real H5/H7 **drift** case |
| George 2026, DNA extraction comparison for *P. destructans* | 10.1177/10406387261441588 | almost certainly runs the Shuey qPCR; Lorch is a co-author |
| Babin 2022, specific detection of three bee microsporidia | 10.1016/j.ejop.2022.125935 | right shape for a Martin-Hernandez *Nosema* cross-reactivity case |
| Riaz 2026, invA versus ttrC real-time assays | 10.1016/j.mimet.2026.107471 | head-to-head on genus coverage for Rahn invA |
| Xie 2024, improved pan-alphavirus assay | 10.1002/jmv.29788 | would evaluate the Sanchez-Seco NSP4 rounds |
| Nijhuis 2018, in-silico evaluation of astrovirus PCR assays | 10.1016/j.jcv.2018.09.007 | would cover the Chu 2008 pan-astrovirus primers |
| Thomas 2018, diagnostic tools for *B. salamandrivorans* | 10.1111/tbed.12787 | a published evaluation, but its claim is false POSITIVES, which `works`/`fails`/`partial` cannot express |
| Su 2020, reptilian paramyxovirus in Guangxi | 10.1177/1040638720911023 | no usable full text in Europe PMC |

Rejected on identity, recorded so they are not re-proposed:

- **Drzewnioková 2023** pan-lyssavirus comparison tests Heaton, Pyro and LN34 sets, not
  Vazquez-Moron's.
- **Abdelmalek 2022** compares nine *Helicobacter* 16S sets and its worst performer is
  not the registry's Fox 1998 pair.
- **Stöhr 2015** prints the ranavirus MCP reverse one 3' base longer than the registry
  stores it. A 3'-end difference changes scoring directly, so this is not the same
  oligo until someone decides which form is right.
- The Watanabe-derived pan-coronavirus reverse in Habeebur-Rahman 2025 is 23 nt against
  the registry's 24. **Worth resolving from Watanabe 2010 (10.3201/eid1608.100208)
  directly**, because one of the two is a transcription error.
- **Geiselhardt 2022** also restates that Scagliarini's 2007 CDV set was rebuilt to
  reach post-2007 genotypes, which would be a drift row, but that claim is Geiselhardt
  repeating Halecker 2021, whose DOI is already a development-set row. Recorded here
  rather than entered.

Cheapest unexplored win: the **Usutu NS1 realtime (Jöst 2011)** entry. A literal search
on its stored probe returns three recent papers reusing the exact oligos, which would
test that entry's own `primer_site_polymorphic` flag. Listed, not read.

Four assay families were never searched at all because the passes ran out of time:
`Apicoplast_23S_LSU`, the three *E. coli* entries, `CALICIVIRUS` and `CIRCOVIRUS`.
Apicoplast 23S is the pick of those: plastid 23S primers are widely reused and widely
reported to miss genera.

## For the C2 bench corpus

`docs/bayesian-scoring-plan.md` gates the Bayesian per-record model on 40+
within-family negatives and the registry has 11. This sweep read each paper once for
both purposes, and **13 of the 31 rows sit in a paper that prints a per-type or
per-strain amplification table**: Geiselhardt 2022 (per-genotype Cq, 8 genotypes),
Fieldhouse 2020 (per-specimen BLAST identity), Habeebur-Rahman 2025 (per-clade
assignment), Galvin 2022 (per-species positivity), Song 2023 (per-lineage alignment
breakdown in its Table S2, which is not in the Europe PMC XML and needs the
supplement), Fischer 2013 (every method against every panel sample, the single best
table in the set). Extracting those into `docs/bench-panels/` is the next corpus step,
and Fischer's ring-trial table is where to start.

## Method note, for whoever runs the next pass

Pasting a stored oligo into Europe PMC's full-text search in quotes was by far the most
productive tool: a paper that prints the sequence can have its identity confirmed
without guessing, which is the step that rejected four otherwise attractive candidates
above. Degenerate primers cannot be searched this way, which is exactly why the
pan-family entries are under-represented in what was found. The other productive query
shape was `CITES:<pmid>_MED` against the design paper, filtered on mismatch, false
negative, failed to amplify and redesign.

Every assay searched without result is listed, one line each, in the three raw pass
files kept outside the repo (the scratchpad `heldout-findings-1.md`, `-2.md`, `-3.md`),
so the next sweep does not repeat the work.
