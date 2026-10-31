# Step 1 done: the fungal assays are not broken, and one thin real signal is hiding in them

> **Correction, same day, and it reinforces the conclusion.** The rates and row counts below
> were measured by globbing `results/screened/`, which keeps **orphan** group screens that no
> live assay retrieves - and both the Ophidiomyces (`1387563/all`, 530 MB) and
> *B. salamandrivorans* (`1357716/all`, 90 MB) archives are orphans. **None of these three
> assays appears in `results/2026-10-25/calls.tsv.gz`'s artefact list at all**, so most of the
> records reasoned about below are not in the current denominator either. The finding stands
> twice over: nothing is wrong with these entries. The *B. sal* probe-divergence watch item
> also stands, because those five 2024 records were checked individually against their
> sequences rather than counted. See `docs/journal/2026-10-25-stale-orphan-screens.md`.

`docs/RESUME-HERE.md` made this plan step 1 on the strength of a number I computed badly.
After the chance-pair test removed its artefact rows, `Snake_fungus_Ophidiomyces_ophi_IGS`
read 1.4%, `..._ITS2_28S` 31.8% and `B_salamandrivorans_..._Blooi_2013` 25.8% whole-archive,
and I wrote that all three had "a large genuine problem that the artefact was sitting on top
of". **That framing was wrong and is withdrawn.** Those are whole-archive rates over every
record ever deposited; the report scores a recent window, and there the three read:

| assay | report says | baseline |
|---|---|---|
| IGS | no evaluable records since Oct 2024 → **no recent data** | 100% (11) |
| ITS2/28S | 62.5% on 8, below the minimum of 15 → **insufficient data** | 100% (17) |
| *B. sal* | 20.0% on 5, below the minimum → **insufficient data** | 100% (1) |

All three have a 100% baseline and none publishes a drift verdict. **The report's handling is
correct.** What needed diagnosing was not a broken assay but why so few records are evaluable,
and whether the handful of recent failures are real.

## Where the low whole-archive rates came from: chance windows in WGS contigs

For *B. salamandrivorans*, of the records short enough to search directly, the best match to
the 32 nt `STerPROBE` window splits cleanly by call:

    detect    n= 5   probe mismatches 0, 0, 0, 0, 0
    reduced   n= 1   2
    fail      n=25   median 11, max 14

A bimodal split, not a gradient, and the decisive observation is that **it does not follow the
strain**. `JAFDOV010000475` (probe 0 mismatches, `detect`) and `JAFDOV010000431` (probe 11,
`fail`) are both WGS contigs of **strain AMFP15/1**. The same is true across AMFP15/3,
AMFP13/1 and AMFP14/2. One strain cannot carry two ITS loci 11 mismatches apart in a 32 nt
window.

So the 11-14 mismatch "matches" are not the ITS locus. They are the best of roughly ten
thousand 32 nt windows in a 10 kb contig, which is a chance match and lands well short of the
~24 mismatches a uniform random window would give. The contigs in question are the ones whose
primers also chance-paired, which is why the chance-pair test already removes 435 of this
assay's rows. **The apparent catastrophe was an artefact of searching for a locus in records
that do not contain it** - the same root cause as Orf and *Ophidiomyces* targetD, measured here
from the other direction.

The records that genuinely carry the locus are exactly the ones that detect, and they include
the two authoritative references: `KC762295` (AMFP13/1 ITS) and `NR_111867` (CBS 135744,
**from TYPE material**), both at probe mismatch 0.

## The one real signal, and why the report is right not to act on it

Five records deposited **2024-12-06** are different in kind from everything else here. They are
161-165 bp, and they begin and end exactly at the primer sites - they are sequenced amplicons,
not assemblies. Both primers match **perfectly, 0 mismatches**, on the minus strand. The probe
window is present and diverges:

| accession | isolate | probe mismatches | call |
|---|---|---|---|
| `PQ661665` | SNU_Bsal_797 | 2 | reduced |
| `PQ661664` | SNU_Bsal_863 | 6 | fail |
| `PQ661666` | SNU_Bsal_781 | 8 | fail (probe not found) |
| `PQ661667` | SNU_Bsal_773 | 8 | fail (probe not found) |
| `PQ661663` | SNU_Bsal_944 | 12 | fail (probe not found) |

For a hydrolysis-probe qPCR this is the failure mode that matters: the primers would amplify
and the probe would not report, so the well reads negative on a true positive. That is a
candidate **probe-site drift** signal in a serious amphibian pathogen, and it is recent.

**Three reasons it is not yet a finding, all of which the pipeline already respects:**

1. **Five records, one submission, one date, one lab** (SNU, Seoul National University). They
   are not independent observations, and a submission-level sequencing or assembly artefact
   would look exactly like this.
2. **Five is below `min_records_for_drift: 15`**, so the report says "insufficient data" rather
   than declaring drift. That is the threshold doing its job.
3. `max_mismatches_searched: 6` is what decides whether these read as probe-absent (8 and 12)
   or probe-present-and-failing (6), and `config.yaml` already calls that "the most
   consequential number here" and admits it is a guess. The outcome happens not to differ -
   both end as `fail` - but the *reason* recorded does.

**What would turn it into one:** more *B. sal* ITS deposits from an independent source showing
the same probe-window divergence. If they appear, this is a drift case and belongs in the
held-out set, which has exactly one drift ground-truth event today. Worth a standing watch
rather than an entry change.

## Consequences for the plan

- **Step 1 is done** and did not find what it went looking for. Nothing to fix in these three
  entries; `B. sal` gains a watch item, not a correction.
- **It strengthens step 2.** A third independent instance of "the record does not contain the
  locus" - and this one found from the probe side rather than the primer side - says the
  locus-identity test in `docs/journal/2026-10-25-locus-identity-design.md` is aimed at the right
  thing. It also supplies a calibration case that design explicitly asked for: AMFP15/1's two
  contigs are a chance window and a real locus in the same strain, so any identity threshold
  must separate them.
- **The withdrawn claim is a reminder** to score the window the report scores. A whole-archive
  rate over an archive full of WGS contigs is not a verdict and should not be quoted beside
  one.
