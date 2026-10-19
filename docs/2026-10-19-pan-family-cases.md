# Pan-family validation cases: what the lineage override is actually catching

**Date:** 2026-10-19
**Evidence:** `results/2026-10-17/calls.tsv.gz`, ancestry scope (`73285ed`), renamed IDs.
**Code:** `lineage.require_working_baseline`, **on** since the mechanism column
landed (see the end of this file).

## The 21 pan-family cases

11 disagree, 7 agree, 1 weaker, 2 undecided. The lineage override drives 10 of
the 11 disagreements and 5 of the 6 caught failures. For each override case, here
are the lineage that fired and its whole history before `as_of`:

| case | expect | lineage that fires | recent | all records before `as_of` |
|---|---|---|---:|---:|
| Pan-CoV Lan round1, 2020 | works | MERS-CoV | 0/121 | 0/558 |
| Pan-CoV Lan round1, 2021 | partial | MERS-CoV | 0/112 | 0/663 |
| Pan-CoV round2, 2024 | partial | HCoV-HKU1 | 0/33 | 0/82 |
| Pan-flavivirus NS5 r1/r2, 2017 | works | Zika virus | 0/262 | 1/284 |
| Pan-flavivirus NS5 r1, 2018 | partial | Yellow fever virus | 0/95 | 2/172 |
| Pan-herpes polymerase r2, 2018 | works | Human betaherpesvirus 5 | 0/52 | 0/403 |
| Enterovirus VP3/VP1 r2, 2018 | works | Poliovirus 3 / CVA16 | 0/125 | 0/409 |
| Polyomavirus VP1 Johne, 2019 | partial | Betapolyomavirus hominis | 0/294 | 0/759 |
| Paramyxovirinae Tong r1, 2024 | works | Human respirovirus 3 | 0/323 | 1/763 |
| Paramyxovirinae r2, 2019 | **fails** (caught) | Human respirovirus 3 | 0/234 | 0/371 |
| Papillomavirus L1 Forslund, 2011 | **fails** (caught) | HPV16 | 0/79 | 0/150 |
| Pan-hemoparasite Hellgren, 2016 | **fails** (caught) | *Plasmodium falciparum* | 0/132 | 0/952 |
| Pan-Plasmodium Hellgren, 2016 | **fails** (caught) | *P. falciparum* / *P. floridense* | 0/135 | 0/959 |
| CDV P gene Scagliarini, 2021 | **fails** (caught) | *Morbillivirus canis* | 59/75 | 152/185 |

Two findings:

1. **Almost every override fires on a lineage the assay never detected at any point
   in its history.** That is a coverage gap, which `low coverage` already means.
   It isn't drift. The pooled check excludes this case (`require_working_baseline`,
   2026-10-14: "a fall from a baseline that never cleared it is not drift"), but
   the lineage override ignored that.
2. **Three of the five "caught" failures are caught for the wrong reason.** Hellgren
   and Pan-Plasmodium are avian haemosporidian primers. They fire on human malaria
   (*P. falciparum*), and under the gate on chimpanzee (*P. reichenowi*) and lizard
   (*P. floridense*) parasites. Lotta 2019's failure is missed *Leucocytozoon*
   lineages. Forslund's FAP primers are a cutaneous set, and they fire on HPV16, a
   mucosal alpha type. Only CDV 2021 is caught on its actual target, with a real
   fall that fits Halecker adapting the assay to current variants.

The `works` claims are about specific taxa, too: Perez-Ramirez 2020 tested WNV
lineages 1 and 2, Usutu and JEV; Wacharapluesadee 2020 tested SARS-CoV-2. The tool
judges every lineage in the family and lets the worst one decide.

## The per-lineage working-baseline gate

With `lineage.require_working_baseline: true`, a lineage that was measured in some
earlier year (at least `min_records_for_coverage` records) and stayed below the
threshold in every one of them cannot drive `declining`. If it fails under a pooled
`stable`/`watch`, the assay becomes `low coverage` and the note names the lineage.
A lineage with **no** earlier measured year can still drive `declining`, because
that is the emerging-lineage failure the tool exists to catch (2009 pandemic H1N1
against the 2003 Matrix assay). An earlier version that excused every
lineage without a working year would have hidden it.

| | failures caught | `works` agree | weaker | disagreements |
|---|---:|---:|---:|---:|
| gate off (shipped) | 6/12 | 9 | 4 | 14 |
| gate on | 4/12 | 9 | 6 | 14 |

What changes with the gate on:

| case | expect | off | on |
|---|---|---|---|
| Paramyxovirinae Tong r1, 2024 | works | declining (disagrees) | low coverage (weaker) |
| Pan-herpes polymerase r2, 2018 | works | declining (disagrees) | low coverage (weaker) |
| Papillomavirus L1 Forslund, 2011 | fails | declining (agrees) | low coverage (disagrees) |
| Paramyxovirinae r2, 2019 | fails | declining (agrees) | low coverage (disagrees) |

The two lost catches were caught on HPV16 and HPIV-3, lineages never detected. The
`fails` they stand for is a coverage claim: Michael 2011 says FAP's spectrum is
"limited mainly to beta papillomaviruses". The gate gets the mechanism right, but
the case label doesn't encode the mechanism, so the retrospective scores it as
wrong.

Disagreements the gate leaves, all on lineages that did work in some earlier year:
pan-flavivirus NS5 on Usutu (taxid 64286, 14% of 139 recent), which Perez-Ramirez's
panel detected; pan-CoV on infectious bronchitis virus (68% / 84%); enterovirus
round2 on taxid 12074 (80%). These are the real tool-versus-literature
disagreements and should be checked against the records.

## What it needs next (curation, not code)

1. **Record each `fails` case's mechanism** in `docs/validation-cases.tsv` from its
   source: `drift` (lost detection of something it used to detect: CDV 2021,
   influenza 2010) or `coverage` (never detected part of its claimed range: Forslund,
   Hellgren, Pan-Plasmodium, probably Kolesnik's paramyxovirus rows). The
   retrospective then accepts `low coverage` for a coverage-type `fails`. This is a
   rubric for the ground truth, so it comes from the sources, not from what the
   tool outputs.
2. **Curate each pan-family assay's intended range from its design paper** as
   `scope_taxids`: avian haemosporidia for Hellgren (not *P. falciparum*,
   *P. reichenowi*, *P. floridense*), cutaneous HPV genera for FAP, and so on.
   Several of these assays have no `scope_taxids` at all, so they are judged
   against the whole family.
3. **Optionally, tested taxa per case** (e.g. WNV/USUV/JEV for Perez-Ramirez), so a
   `works` claim is compared with the lineages that were actually tested.

Turn the gate on once (1) is in: the gate is right about mechanism, and (1) is
what lets tier-2 see that.

## Step 1 done: mechanism recorded, gate on

Every `fails` row now has a `mechanism` read from its source (`484d595`). Only CDV
2021 is `drift` ("adaption to the new virus variants"). The other 11 are `coverage`:
lineages the primers never matched. `classify()` accepts `low coverage` for a
coverage-type `fails`. Kolesnik's rows were also corrected: the 29.5% they quoted
belongs to Tong's RMH set, and the registry's PAR set detected no ferlavirus at all.

| | failures caught | `works` agree | weaker | disagreements |
|---|---:|---:|---:|---:|
| gate off | 6/12 | 9 | 4 | 14 |
| gate on | 6/12 | 9 | 6 | **12** |

Nothing is lost, so the gate is on. Current statuses on the 2026-10-17 calls: 17 of
213 assays move `declining` -> `low coverage`, none the other way.

Still caught for the wrong lineage: Hellgren and Pan-Plasmodium (on *P. reichenowi*
and *P. floridense*, non-avian parasites new to the archive), and Forslund (on HPV16,
mucosal). Step 2, curated `scope_taxids` from the design papers, is what fixes these.
Two remaining disagreements fire on taxids that only look new: Enterovirus round2 on
taxid 1193974 and Polyomavirus Johne on 1891763, both 0% with no earlier measured
year. NCBI's species reclassifications mint new taxids for records that already
existed under older ones, which defeats the "new lineage" test. Worth checking.

Note: `scripts/retrospective.py` on `results/2026-10-17/calls.tsv.gz` reports
22 undecided rather than 17. Those calls predate the 2026-10-18 rename, so the 12
renamed assays have no rows under their current IDs. The numbers above map the IDs
through `docs/rename-mapping.tsv`. The next screening run writes current IDs.

## Step 2: scope from the design papers

**Hellgren 2004 (avian).** The design paper's title fixes the range: "simultaneous
studies of *Leucocytozoon*, *Plasmodium*, and *Haemoproteus* from avian blood". In
NCBI the avian *Plasmodium* are the subgenera *Haemamoeba* 418104, *Huffia* 418105,
*Novyella* 418110, *Giovannolaia* 418112 and *Bennettinia* 419353. Checked
2026-10-19: every species NCBI places under them is a bird parasite. The reptile
subgenera hold *P. giganteum*, *agamae*, *floridense*.

- Pan_hemoparasite (HaemNFI/HaemNR3): scope = the five subgenera, *Haemoproteus*
  77521, *Parahaemoproteus* 587283, *Leucocytozoon* 195944.
- Pan_Plasmodium (HaemF/HaemR2, from Bensch 2000, "*Plasmodium* and *Haemoproteus*
  ... amplified from birds"): the same without *Leucocytozoon*.
- *Leucocytozoon* (HaemFL/HaemR2L): already targets the genus; unchanged.

Before this, both pan assays were judged mostly on mammalian parasites. On the
2026-10-17 calls, Pan_hemoparasite had 2,240 *Laverania* records (0% detected)
and 1,618 subgenus *Plasmodium* (11%), against about 130 in the avian subgenera
(nearly all detected). Known loss: *Plasmodium* records with no subgenus
("*Plasmodium* sp.", 783 records) are out of scope, because NCBI does not record
their host.

**Validation rows.** Lotta 2019's primer analysis covers the *Leucocytozoon* nested
protocol, with the mismatch shown in HaemR2L. The Pan_Plasmodium row applied that
result to HaemF/HaemR2, a pair Hellgren never uses for *Leucocytozoon* and that
Lotta did not test, so it is retired as a comment with the reason. The
Pan_hemoparasite row stays, as the shared first round of the protocol Lotta found
failing, and its note now says so.

**Forslund FAP: scope unchanged, on purpose.** Forslund 1999 aimed the pair
"primarily" at cutaneous types but tested 75 types and got bands from 65. The
only ones with no band were types 1, 2, 35, 41, 44, 55, 63, 66, 71 and 74, so
**HPV16 was amplified**. The tool's in-silico 0/150 for HPV16, and 47% across
13,481 *Alphapapillomavirus* records, is therefore a disagreement with the design
paper's own bench result, not an out-of-range lineage. Narrowing the scope to
cutaneous genera would hide it. Inosine handling is deliberate in `iupac.py`
(I pairs with A/C/T, weakly with G), so the matcher is not the obvious cause.
Worth a look: score FAP59/64 against the HPV16 reference genome by hand.

**Tier-2 after step 2** (gate on): failures caught **4/11**, `works` agree 9,
weaker 6, disagreements **13** (was 6/12, 12). The drop is the wrong-reason
catches going away. Pan_hemoparasite now reads `stable` (96% of 26). Before its
2016-12-31 cutoff the archive has 1,530 *Leucocytozoon* records, and the
fusiform lineages that show the failure came later (6,374 of 7,904 are from 2017
on). That is a limit of what a sequence-based tool can see, and it now counts
against the tool honestly instead of being covered by a *P. falciparum* lineage.

Of the four failures still caught, two are caught for the documented reason: CDV
2021 (drift on its target) and Paramyxovirinae Tong round1 (a real pooled fall,
-25% to -18%). Paramyxovirinae round2 is a coverage gap on HPIV-3, consistent
with Kolesnik's coverage finding but not on a ferlavirus. Forslund rests on HPV16,
which the design paper amplified.
