# The 2026-11-15 run failed on two efetch pages that held only WGS master records

2026-11-17. The Air's run `results/2026-11-15/` failed at 22:47 on 2026-11-16 after
11 h 10 min, all of it in `retrieve`. One retrieval group, taxid 171 (Leptospira)
group `q4a36c8adaa`, the `Leptospira_lipL32_Ahmed_2020` entry, failed on the first
attempt and on all three of Snakemake's restarts with the same error:

    ERROR 171/q4a36c8adaa: RetrievalError: efetch returned an empty page where records were expected

Every other group either fetched or had nothing new. The group had never succeeded
before, so every attempt was a full fetch: 2,897 records.

## Cause

The entry's query, `lipL32[Gene] OR lipL32[All Fields] OR "complete genome"[Title]`,
was the only Leptospira query without `NOT "whole genome shotgun"[Title]`. It matched
WGS master records: summaries with a length of a few hundred and no sequence of their
own. efetch answers a master with an empty line.

`retrieve_taxon` sizes efetch pages from the mean record length. Here that was
497,733 nt, so pages held 40 records. In the history handle's order, 80 masters
(accessions `JBNOBL000000000` through `JBNNYN000000000`) sat together at retstart
1240 and 1280, and filled pages 31 and 32 entirely. Each page came back as 40 bytes,
all `\n`. `check_fasta_page` has raised on an empty page since 2026-10-27, and its
docstring says an empty page "is NCBI failing to answer, never a legitimate
end-of-run". This case shows that a page made only of masters is legitimately empty.

It was not transient. The error repeated across four attempts over 90 minutes, and a
single-page probe gave the same body on two runs. Fetching `JBNOBL000000000` alone by
id returned 1 byte.

## Measurements

Both probes are in `local/diagnose-171-2026-11-17/` on the Air (gitignored). They
reuse `esearch`, `esummary` and `efetch_fasta` from `assaywatch/retrieve.py` with the
run's `config.effective.yaml` and `until=2026/11/15`, and write no archive.

- `probe.py`, the whole group, page by page (8 min 39 s): 73 pages; pages 31 and 32
  empty; 20 more pages short by 1 to 24 records. 2,678 records fetched against 2,897
  summaries.
- `probe2.py`, page 31 only (about 10 s; exits 1 on this failure): all 40 summaries
  titled "whole genome shotgun sequencing project".
- The same query with `NOT "whole genome shotgun"[Title]` appended counts 1,664.

The shortfall matters on its own. With `max_unexplained_shortfall: 0.02` and
`min_shortfall_allowance: 20`, the allowance for 2,897 summaries is 57. The group was
missing 219, so making `check_fasta_page` accept an empty page would only have moved
the failure to the shortfall check.

## Decision

Fixed in the registry, not in the code. The query is now

    (lipL32[Gene] OR lipL32[All Fields] OR "complete genome"[Title]) NOT "whole genome shotgun"[Title]

The parentheses make the exclusion apply to all three terms. It is the form the
flaB group already uses. The new query changes the
group slug, so the next run does a full fetch under the new group. The old group has
no archive and no manifest entry, so nothing is lost or orphaned.

Not changed, by decision: `check_fasta_page` and the shortfall guard still count
WGS masters as missing records. Any other query that matches masters will fail the
same way if they fill a whole efetch page, or if they outnumber the shortfall allowance.

## Verification

`probe3.py`, the whole-group probe run against the edited entry with the same
config and `until` date: count 1,664, mean record 712,052 nt, so 28 records per
efetch page. 60 pages, none empty and none short; 1,664 records fetched against
1,664 summaries. pytest (2,248 passed), the validator, ruff and `check_citations.py`
pass on the change.
