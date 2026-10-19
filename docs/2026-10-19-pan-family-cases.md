# Pan-family validation cases: what the lineage override is actually catching

**Date:** 2026-10-19
**Evidence:** `results/2026-10-17/calls.tsv.gz`, ancestry scope (`73285ed`), renamed IDs.
**Code:** `lineage.require_working_baseline` (shipped **off**; tier-2 output with it
off is byte-identical to before).

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
