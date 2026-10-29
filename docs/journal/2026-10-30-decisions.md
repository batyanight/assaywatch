# Four maintainer decisions taken in one sitting, and held-out set 2 spent: 5 of 10 working assays read `declining`

2026-10-30. The roadmap's "Waiting on a maintainer" section had carried four calls for
between one and three days. All four were taken today, batched, so that the build work
behind them could run unattended. This is the record of each, in the order they were taken,
and of what scoring held-out set 2 then said.

## 1. S7b ships: `scoring.mispair_window: 10`

Priced 2026-10-29 (`docs/journal/2026-10-29-s7b-priced.md`), passing all three
pre-registered criteria: tier-2 development set identical case for case, bench 166/179 ->
167/179 on PPRV Nigeria75/1, and no within-family negative gains a band. The reason it was
held a day was the report: 7 flags fall, 5 assays, 6 with no ground truth, and the 7th is
held-out set 2's one false alarm (G2R generic monkeypox, `declining -> stable`), fixed by the
predicted mechanism.

**The decision was taken before set 2's eleven unscored rows were read**, on the bench row
and the separation criterion alone. That ordering matters and is why this entry records the
time order: the value was set in `config.yaml`, then the set was scored (section 2). The
replay over `results/2026-10-27/calls.tsv.gz` was re-run today and reproduces the 2026-10-29
figures exactly (31,237 calls moved; S0 control 0 moved). Shipping it means the next full run
rescreens everything, since `scoring` is in the screen hash; that run is the confirming
rescreen a replay cannot be. `tests/test_score.py` asserted null and now asserts 10.

## 2. The twelve proposed rows accepted as proposed, and set 2 scored

Quackenbush 1998 (`works`, pan-herpes round 2) and the eleven `use`-family rows of
2026-10-29 (`docs/journal/2026-10-29-use-family-cases.md`) were signed off as written. The
file was then run through `scripts/retrospective.py --cases`, once against the shipped
2026-10-27 calls table and once against the S7b replay of it. **Set 2 is spent**: it is a
second development set from today, and the file's header says so.

| | pre-S7b (results/2026-10-27) | S7b replay |
|---|---|---|
| works / agrees | 3 | **4** |
| works / weaker (`low coverage`) | 2 | 2 |
| works / DISAGREES (`declining`) | **5** | **4** |
| fails / agrees | 2 (both credited to `low coverage`) | 2 |
| fails / DISAGREES (`stable`) | 1 | 1 |
| partial / agrees | 1 | 1 |
| documented failures caught | 2/3 (CrI 18%-96%), 0 by `declining` | same |
| PPV of `declining` | 0/5 | 0/4 |
| working assays called `declining` | **5/10 = 50% (CrI 22%-78%)** | 4/10 = 40% (CrI 15%-70%) |

The only row that moves between the columns is the Mills/G2R one, exactly as the pricing
predicted; S7b is otherwise neutral on set 2. So the S7b number that could not be used to
decide is now a measured confirmation, not a fit.

**The finding is the five false alarms, not S7b.** On the development set `declining` has a
PPV of 4/10 and a false-alarm rate of 4/32. On set 2 it is 0/5 and 5/10. The five:

| assay | as of | recent share | the note |
|---|---|---|---|
| G2R generic monkeypox | 2022-11-02 | | the traced mid-window wobble; fixed by S7b |
| `Pan_HERPES_dsDNA_Polymerase_round2` | 2023-10-01 | 80.0% of 446 | change from baseline -10% to -2%; and a Mardivirus lineage at 0% flagged as a coverage gap, not drift |
| `ASTROVIRUS_RdRp_Chu_2008_round2` | 2021-09-27 | 69.4% of 356 | change -23% to -12% |
| `ADENOVIRUS_dsDNA_Hexon_gene` | 2019-12-31 | 63.8% of 384 | change -15% to -4% |
| `ADENOVIRUS_dsDNA_Hexon_gene_round2` | 2019-12-31 | 79.9% of 334 | change -13% to -4% |

Four are pan-family consensus assays whose paper reports them amplifying a novel or
divergent virus from a handful of positives (4 of 775 rodents; 16 of 16 buffalo calves by
nest; EHV typing). A pan-family nest detecting 64-80% of everything GenBank holds for the
family, with a real fall against its baseline, is not contradicted by a paper that found it
working on the samples it had. The `works` label in these rows is about sensitivity on a
field panel; the status is about coverage of deposited diversity. The development set's
`works` rows were mostly species-specific assays, where the two questions coincide; the
`use` family surfaces pan-family assays, where they do not. **The matrix is measuring a
label mismatch as much as a scoring error**, and the honest reading is: for a pan-family
assay a published `works` should probably be scored against `low coverage` as agreement
(the way `partial` already is), or the row should carry `mechanism` and a scope. That is a
proposal for the scoring rule of the matrix, not for `config.yaml`, and it is written here so
that it is taken with set 2 already spent and not as a way of rescuing a number.

The one `fails` disagreement is the Hellgren pan-hemoparasite row at 98.9% `stable`: the
paper's failure is a two-base 3' mismatch against the *L. toddi* clade inside an otherwise
working survey, and that clade is a small share of the family's deposits, so the pooled
share does not see it. The two sibling rows are caught, both as `low coverage`. Zero rows in
either set carry `mechanism: drift`, and that is unchanged.

## 3. `CALICIVIRUS_ssRNA_Helicase_Reid_1999` stays `draft`

Eligible for `active` on the schema's terms since 2026-10-28; the maintainer keeps it
`draft` on `thin_evidence` alone (16 amplifying records of 152,379). Recorded in the
entry's `thin_evidence` note with the condition for revisiting.

**A finding on the way**: `assaywatch.registry.edit()` was tried for that note and
re-emitted the entry's long quoted `notes_curator` scalar as one line of several thousand
characters (ruamel's round-trip preserves quoting but not the folding width). No data was
lost and the change was reverted; the note went in as a text edit. `edit()` is right for
scalar fields and wrong for an entry with hand-wrapped prose until it is given the
width the files were written at. Added to the roadmap under Hygiene.

## 4. Repo visibility

Still the maintainer's; nothing blocks on it.

## Order of work from here

`drift.window_on` step 1 (interface approved 2026-10-30), the 93 `use` rows that did not
reach CONFIRMED, the per-year footprint share, then the drift-mechanism case hunt design.
