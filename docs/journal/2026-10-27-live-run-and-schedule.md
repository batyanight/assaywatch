# The first full run under today's scoring, the schedule that will run the next one, and two failed runs on the way

2026-10-27, evening. Scoring is part of the screen cache key, so shipping the probe switch
and S3b meant every committed number described a configuration that no longer existed
until a run replaced it. This entry is that run, what it took to get it, and the launchd
job that now runs it every Sunday.

## Two failed runs first

**Run 1 failed at `collect_calls`: 461 of 482 cached screens were stale.** Snakemake's
params trigger should rerun a screen whose config changed, and does when it holds a
metadata record for the output; it held none for these, so it scheduled 9 jobs and
reused 461 screens produced under the old penalty. `collect.py`'s signature guard caught
it — "produced under settings this pipeline no longer uses" — which is exactly the
backstop it was written to be. The screens were set aside, not deleted
(`results/screened.stale-2026-10-27-pre-S3b/`), and the run restarted.

**Run 2 rescreened all 461 and failed at `collect_calls` again, and that one was mine.**
While it ran I edited and committed `settings.py`, `config.yaml` and other modules; the
screen signature hashes `assaywatch.triggers.source_names("screen")` — fifteen modules
including `settings.py` — so by the time `collect_calls` read the fresh screens, every one
carried a signature the pipeline no longer expected. The guard cannot tell an innocent
mid-run edit from a stale cache and should not try. The fix is a rule, now in ROADMAP
and this file: nothing in that closure, and nothing in `registry/`, is touched until a
run reports. A dirty-tree refusal in `scripts/weekly_run.sh` would enforce it and is not
built yet.

**Run 3 rescreened all 461 again, untouched, and completed in 1 h 22 min.** 468 jobs,
2,680,489 call rows, 595 of them records retrieved today that the 2026-10-26 table did
not have.

## What the run says, against the 2026-10-26 run

Headline: **188 assays screened: 42 declining, 34 low coverage, 7 watch, 30 insufficient
data, 19 no recent data, 56 stable** (2026-10-26: 34 / 37 / 12 / 30 / 19 / 56). Start
here: 10 assays, as before. 234 assays appear in both reports; **16 move**:

| from | to | assays |
|---|---|---|
| stable | declining | `INFLUENZA_A_ssRNA_Matrix_gene_recognized_h_2003`, `MONKEYPOX_dsDNA_G2R_generic_TaqMan_Li_2010` |
| watch | declining | `CDV_N_gene_Elia_2006`, `CDV_P_gene_Scagliarini_2007`, `DWVB_polyprotein_Rossi_2024`, `PD_WNS_ITS1_Shuey_2014`, `SBV_polyprotein_Rossi_2024` |
| low coverage | declining | `ARENAVIRUS_ssRNA_S_gene_2`, `PAPILLOMAVIRUS_dsDNA_L1_gene_Forslund_1999`, `PARVOVIRUS_ssDNA_VP1_gene_dependovirus` |
| declining | low coverage | `CIRCOVIRUSES_ssDNA_vertebrate_Rep_Gene_round2`, `DWVA_polyprotein_Rossi_2024` |
| low coverage | stable | `Nipah_N_gene`, `TILV_ssRNA_segment3_ME1_ME2_Kembou_2017` |
| stable | watch | `MONKEYPOX_dsDNA_F3L_MGB_Kulesh_2004` |
| watch | stable | `CMV_UL55_gB_Deckers_2009_round2` |

**The two S3b predictions, checked.** The Forslund FAP assay moves `low coverage` →
`declining`, as the replay said it would: lowering the 3'-window penalty lifts its
earlier years over the threshold, and `require_working_baseline` can then read its
present shortfall as a decline. `Pan_flavivirus_NS5_3_round2` stays `declining` today,
and that is **not** a failed prediction: what the replay showed moving was its
retrospective verdict at **2017-03-31** — a `works` tier-2 case that stopped being a false
alarm — not its 2026 status. The plan's wording ("out of declining") conflated the two,
and this is the correction.

**The probe switch's moves are all here**: influenza Matrix `stable` → `declining` at
6.5% of 30,382 recent records, `CDV_P_gene_Scagliarini_2007` (an `active` entry) into
`declining`, and the MONKEYPOX G2R generic assay — whose primers are exact in only a
fifth of MPXV genomes while its probe is exact in 93% — `stable` → `declining` now that a
mismatched probe is not a find.

## S3b is confirmed on the whole table, not six assays

The replay priced S3b on the 2026-10-26 table; a real rescreen of six assays had agreed
on 280,818 rows. Run 3 is a real rescreen of everything under the shipped config, so the
replay can be checked against it row for row: **2,679,894 shared rows, 8 call
disagreements** — 6 where the real screen found no amplicon at all and 2 where it found a
better candidate (`fail` → `reduced`), on four assays, none a tier-2 case. The 78 small
movers the roadmap listed as unrescreened are among the 2.68 million. The replay boundary
("priced, not proven; candidate selection is frozen") was the right caveat and the
approximation was eight rows in 2.68 million, every one pessimistic.

## The schedule

`profiles/launchd/com.assaywatch.weekly.plist` is installed on this machine as
`~/Library/LaunchAgents/com.assaywatch.weekly.plist`, fired once by hand as a dry run
(`results/weekly-logs/2026-10-27-1958.log`: "dry run finished; nothing was fetched or
written"), then switched to `--live` and reloaded. **It runs Sunday 09:00, lid open.**
This is machine-local state: the other MacBooks are not scheduled, and the README's
"re-screens on a schedule" is true of exactly one laptop.

`docs/example-run-2026-10-27/` is this run's report, site-drift table and TSV, committed
so the output can be read without installing anything; the 2026-10-26 copy stays as the
last run under the old scoring.
