# The composition cut: the per-assay widest-gap rule was built, measured and replaced

2026-11-03. ROADMAP "Lineage composition over time", step 4b. A record of one
measurement and the design change it forced. The decision is in `ROADMAP.md`; the
number and its justification are in `config.yaml` (drafted in
`docs/composition-config-draft.yaml` until step 12).

## What was being calibrated

The composition stage clusters each assay's records into lineages by sequence, over the
amplicon plus flank with the primer and probe sites masked. The plan, grilled on
2026-11-02, chose the cut **per assay**: the midpoint of the widest gap between
consecutive edge weights of the sample's single-linkage minimum spanning tree, inside
bounds `[cut_min, cut_max] = [0.01, 0.15]` of Mash distance. Step 4b was to calibrate
those bounds on two assays with an answer known from outside the clustering:

- **influenza M** (`Influenza_A_virus_M_Spackman_2002`): record titles carry the
  subtype, so H3N2, H1N1pdm09 and the avian subtypes were to separate;
- **Messmer 16S round 1** (`Chlamydia_16S_Messmer_1997_round1`): expected to stay one
  cluster, since the *C. trachomatis* serovar split lives in ompA and the genome.

Everything below is measured on the 2026-11-01 calls and the archives on disk, at
`kmer_len` 15, `sample_cap` 2000, `mask_buffer_bp` 5, `stop_n_run` 10. The label in
every cross-tab is the organism GenBank prints at the head of the record's title, which
nothing in the clustering sees.

## Finding 1: a symmetric window does not fit an amplicon at a gene's end

Spackman's matrix amplicon sits at the 5' end of segment 7. Over its 89,628 evaluable
records the available flank is **9-23 bp to the left and 886-903 bp to the right**
(p10-p90). At the planned symmetric ±500 bp, **one record of 89,628** was full-flank, so
the sample was one window and there was nothing to cluster.

Fixed by reading the window shape per assay (`subcluster.window_shape`): each side
starts at the `shape_quantile` (0.1) of what the assay's records offer there, capped at
`flank_bp`, and a short side's unused budget passes to the other, to at most
`2 x flank_bp` in all. Influenza M then reads `(9, 886)` with 88.5% of records
full-flank, Messmer `(20, 959)` with 86.9%, pan-coronavirus `(500, 500)` with 93.6%.
Every window within an assay still shares one geometry, which is what Jaccard needs; a
record short of the shape is placed by containment instead of being sampled.

## Finding 2: the widest-gap rule does not survive its own sample size

It worked where the sample was small. Messmer, 76 distinct full-flank windows at the
symmetric window, split at a gap of 0.033-0.047, cut 0.040, into four groups that are
exactly the species the genus pair amplifies: *psittaci*/*abortus* 35, *trachomatis* +
*muridarum* 34, *pecorum* 4, *pneumoniae* 3. (So the plan's expectation of one cluster
was half right: all 32 sampled *trachomatis* windows do sit together, but the assay is a
genus pair and its other species separate.)

At 1,500-2,000 windows it fails, for a reason that has nothing to do with which assay is
chosen. The MST then has 1,999 edges spread over the whole distance range, and the edge
weights are a continuum:

| assay | sampled | median edge | p90 | p99 | max | widest raw gap |
|---|---|---|---|---|---|---|
| influenza M | 2,000 | 0.0035 | 0.0191 | 0.0450 | 0.1227 | 0.0372 at 0.085-0.123 |
| Haemosporida cytb | 1,513 | 0.0025 | 0.0278 | 0.0768 | 0.1532 | 0.0127 at 0.125-0.138 |
| Coronaviridae RdRp | 2,000 | 0.0031 | 0.0510 | 0.2023 | 0.2550 | 0.0087 at 0.117-0.126 |

Two failure modes, both visible above:

- **The widest gap sits in the sparse upper tail and isolates an outlier.** Influenza M
  cut at 0.104 and returned one cluster of 1,999 windows holding every subtype (H3N2
  529, H1N1 463, H5N1 167, H9N2 138) plus one H7N7 window alone. Haemosporida cut at
  0.131 and returned 1,499 + 10 + 3 + 1.
- **Below the tail there is no gap at all.** The pan-coronavirus assay's widest gap over
  2,000 windows is 0.0087, under `min_gap`, so the rule declared "no gap in bounds" and
  one cluster of 2,000 -- across four coronavirus genera.

A continuum of edge weights is what a well-sampled archive looks like, so this is not a
tuning problem. **Also recorded: the influenza check cannot be met by any cut**, because
subtype is a property of HA and NA and the matrix gene is conserved across subtypes. The
~1% H3N2 reading in `docs/journal/2026-10-28-influenza-decomposed.md` comes from the
primer sites, which this window masks on purpose.

## Finding 3: a fixed cut behaves monotonically, and 0.05 is where named taxa separate

Purity is the share of sampled windows whose cluster's modal organism is their own;
completeness is the share of one organism's windows sitting in its own dominant cluster.
Clusters counted at `min_cluster_size` 3.

**Haemosporida cytb (Hellgren HaemF), 1,513 windows, genus labels:**

| cut | clusters | purity | Plasmodium | Haemoproteus | Hepatocystis |
|---|---|---|---|---|---|
| 0.01 | 100 | 84.9% | 14% | 51% | 17% |
| 0.02 | 78 | 91.2% | 35% | 24% | 34% |
| 0.04 | 35 | **93.6%** | 38% | 82% | 48% |
| 0.05 | 24 | 83.1% | 38% | 90% | 97% |
| 0.07 | 10 | 78.3% | 44% | 100% | 99% |
| 0.10 | 5 | 68.0% | 100% | 100% | 100% |

**Coronaviridae RdRp (Watanabe 2010), 2,000 windows:**

| cut | clusters | purity | IBV | PEDV | "Human coronavirus" |
|---|---|---|---|---|---|
| 0.02 | 80 | 68.7% | 42% | 100% | 37% |
| 0.05 | 78 | 68.1% | 94% | 100% | 37% |
| 0.10 | 51 | 64.9% | 100% | 100% | 37% |
| 0.15 | 35 | 62.3% | 100% | 100% | 55% |

**The coronavirus purity column is held down by the label, not the clustering.** "Human
coronavirus" is 265 windows of 229E, OC43, NL63 and HKU1, four viruses far enough apart
that no correct clustering puts them together, so its completeness is pinned near 37% at
every cut. A title prefix is a weak label, and this is the shape of its weakness.

## The decision

`composition.cut: 0.05`, one number for every assay, and the per-assay search deleted
(`Cut`, `widest_gap_cut` and `mst_weights` removed from `subcluster.py` with their
tests; `components_at` now takes a plain float). 0.05 is the level at which the named
taxa separate on all three assays measured -- Haemoproteus 90% and Hepatocystis 97%
complete on cytb, IBV 94% on coronavirus, the four Chlamydia species at 0.040 -- while
above about 0.10 the clusters become genera and the within-genus structure that drift
lives in disappears, and below about 0.02 an assay runs to 80 clusters where a panel can
draw 8.

What the number is not: calibrated on more than three assays, or against anything but
the organism in a record title. The adaptivity the per-assay rule was chosen for was
never delivered by it, and one cut has a property the per-assay one did not -- a cluster
means the same divergence on every panel in the report.
