# The influenza matrix probe fails on H3N2 and H1N1 and works on the avian subtypes

2026-10-27, night. `lineage.sublineage` has carried a worked example for the influenza
matrix assay in a comment since 2026-10-19 and shipped empty, first because nothing had
measured it and then because the lineage layer's numerator was wrong for probe chemistry
(`2026-10-27-influenza-sublineage.md`, and the fix in the same day's `##  Done`). Both
blockers are gone, so the chain is enabled — for this one assay, and on the condition the
config block sets for itself: tier-2 first, because enabling a chain can move a verdict.

    lineage:
      sublineage:
        INFLUENZA_A_ssRNA_Matrix_gene_recognized_h_2003:
          chain: [title]
          title: {pattern: '\((H\d+N\d+)\)'}

Influenza A records carry the subtype in the GenBank title, so a regex labels them with
no taxonomy change: NCBI files 189,538 of them under one name, *Alphainfluenzavirus
influenzae*, and the title splits them into 57 subtypes.

## What the split says, on the corrected numerator

This is a hydrolysis probe, so `reduced` is not a detection (`reduced_not_detected_for`),
and that is what the earlier table did not do. The ordering **inverts**:

| Lineage | N evaluable | Detected | Share |
|---|---|---|---|
| H3N2 | 38,771 | 463 | 1.2% |
| H1N1 | 27,725 | 720 | 2.6% |
| H1N2 | 1,917 | 63 | 3.3% |
| unsubtyped (2955291) | 6,853 | 638 | 9.3% |
| H5N1 | 3,215 | 1,093 | 34.0% |
| H9N2 | 3,208 | 2,126 | 66.3% |
| H7N3 | 551 | 486 | 88.2% |
| H5N8 | 414 | 378 | 91.3% |
| H4N6 | 789 | 755 | 95.7% |
| H5N6 | 437 | 422 | 96.6% |
| H7N9 | 176 | 171 | 97.2% |

Thirty subtypes read 85–100%. The pre-fix table had H3N2 at 99.4% and H5N1 at 87.6%,
which is what counting a mismatched probe as a detection does to a probe assay: it
reports the primers, which are fine, and says nothing about the reporter, which is the
whole assay. **The pooled 6.5% is H3N2 and H1N1**, the two subtypes that dominate the
archive and circulate in people, and the rare avian subtypes it is pooled with are the
ones still being detected.

That is the lineage-conditional estimand doing the job the 2026-10-04 review said a
single population proportion cannot: "6.5% of recent records" reads as an assay that has
collapsed, and the per-subtype table says instead that one probe site has drifted in the
human-circulating lineages while the avian ones still carry the published sequence.

## It moves nothing, which is why it is adopted

Rendered both ways off `results/2026-10-27/calls.tsv.gz`:

- tier-2 (`scripts/retrospective.py --cases docs/validation-cases.tsv`) is **identical
  case for case**: 6/11 documented failures caught, PPV of `declining` 4/10, 4/32 false
  alarms, 2/6 partial gaps named;
- the full report: **0 of 193 statuses move**.

Nothing moves because the pooled verdict was already `declining` and the worst lineage
was already failing — the override had nothing left to overturn. So this is adopted for
what it reports and not for a decision it changes, and it joins the list of mechanisms
that ship beside a verdict rather than into one.

## What is not done here

The other segmented RNA viruses are untouched. A title regex works for influenza A
because subtyping is in the record title by convention; nothing measures that the same
holds for the rest, and the roadmap keeps it conditional on that measurement. The H3N2
per-year table alone — whether the fall is recent or has always been there — is the next
thing to read, and it needs the per-lineage per-year breakdown the report does not print.
