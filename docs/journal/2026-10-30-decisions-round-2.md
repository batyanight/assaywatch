# Five more decisions, and a fetch that taught us what "premature" means

2026-10-30, a second sitting after `docs/journal/2026-10-30-decisions.md`. Five calls,
taken one at a time, with the measurement that each one turned on.

## 1. The whole 2026-10-30 stack goes to `main`

Six branches, seven commits, no merge commits, every branch tip an ancestor of the last,
so `main` fast-forwarded to the tip in one push. **`scoring.mispair_window: 10` is now on
`main`**, which is what makes the next scheduled run S7b's confirming rescreen rather
than a repeat of the old scoring.

One cost, worth recording because it was avoidable: a fast-forward carries no merge
event, so GitHub closed only the PR whose base was `main` and left the other five OPEN
with nothing to merge and no way to retarget ("There are no new commits between base
branch `main` and head branch ..."). They were closed with a comment naming the commit
that landed. Merging the six bottom-up through the UI would have produced five MERGED
labels instead of five CLOSED ones. Same commits either way.

## 2. The pan-family false alarms are a scope problem, not a scoring-rule problem

Four of set 2's five false alarms are pan-family consensus nests. The proposal on the
table was to score a pan-family `works` against `low coverage` as agreement, the way
`partial` already is, which would have taken set 2 from 5/10 false alarms to about 1/10.

**Rejected.** It declares a real disagreement to be agreement, by a rule proposed after
seeing which rows it would rescue, and it would apply forever -- including to the
pan-family assays where `low coverage` is the warning a user wants.

What is wrong instead is that two different scopes were being compared. `target.scope_taxids`
in the registry is the **claim**: "the smallest set of taxa whose subtrees cover the design
paper's stated range". A case row's `scope_taxid` is the **evidence**: the lineage whose
positives the paper actually had. Pan_HERPES claims 866 taxa and demonstrates a handful.

**Decided**: fill `scope_taxid` for every row whose assay carries more than one
claim-scope taxid -- **34 rows over 17 assays and 34 distinct source papers**
(`docs/2026-10-30-scope-worksheet.tsv`): 17 in the development set, 10 in held-out set 1,
7 in held-out set 2. The first count of this population was 24 and was wrong, because it
read two of the three case files; held-out set 1 was missed and a test that all three
share one header is what caught it.

The population is a property of the registry, readable without looking at a single
verdict, which is what keeps it from being "the rows whose numbers were inconvenient".
It is dominated by rows that can move AGAINST us: **11 of the 34 are `fails` rows**, six of
them the ones held-out set 1 added, and scoping a `fails` row to a well-covered lineage can
turn a catch into a miss. The Hellgren miss may well stay a miss once scoped.

Three conditions attach. The agreement rule does not change. The pooled verdict stays
printed beside every scoped one, because a pan-family assay scored on one lineage cannot
test whether its broad coverage has eroded -- which is a thing this tool exists to detect.
And set 2's scoped numbers are a **re-description, not a score**, since the mechanism was
chosen after the set was read; a scoped matrix is first genuinely scored on set 3.

## 3. The repository is public

Scanned before the switch, not after: the API key (both the environment value and the
file) appears in **zero** commits, no 32-hex token exists anywhere outside caches and
hashes, and no `papers/` PDF or `.secrets/` path was ever committed. The registry is
CC-BY and `papers/` is gitignored by contents, so the licensing was already in place.

This unlocks Actions minutes and branch protection. **Branch protection must wait until
after a fast-forward push**, since a review requirement rejects one.

## 4. The collection-date backfill, and the mistake inside it

Approved in full: fetch `/collection_date` for all 1,243,065 nuccore accessions rather
than the recent window only. What the build measured, in the order it was learned:

| | |
|---|---|
| Records carrying a collection date | **75%** (753/1000, 153/200) |
| `rettype=gb` with `seq_start=1&seq_stop=1` | 2.2 KB/record, source feature intact |
| `rettype=gb` whole | 14.4 KB/record |
| `rettype=ft` | 323 rec/s and **no `source` feature at all** -- unusable |
| Throughput, batches of 200 sliced | **~150 rec/s** |
| Throughput with the first retry policy | **2.1 rec/s** |

That last row is the lesson. `efetch` answers an oversized or unlucky request with
"Response ended prematurely", which reads exactly like one unservable record in the
batch, so the first version halved the batch to find it. The error is **transient**: the
same 200 consecutive accessions that failed repeatedly were served at 238 records/sec
minutes later. Halving turned every blip into ~200 single-record requests and cost a
factor of 70. The fetch is now patient with the whole batch -- three tries, each itself
three paced attempts inside the transport -- and splits in quarters once, never
recursively to singles.

A second false lead, recorded so it is not chased again: a long run of early accessions
returns zero dates, which looks like the slice dropping qualifiers and is not. Those are
patent-era deposits that genuinely carry no `/collection_date`.

Still owed before the lens can use any of this: `metadata.collection_year()` matches
year-only, and GenBank writes four spellings -- `2010`, `Jun-2011`, `16-Mar-2009`,
`2013-12-27`.

## 5. The drift-mechanism search goes to a fresh session

Still zero rows with `mechanism: drift` in either set, which remains the honest gap in
the validation: the tool's premise is temporal decay and no case demonstrates it. The
design is settled (`docs/journal/2026-10-30-design-grilled.md`, Q5-Q6) and the strict bar
stands -- the paper must show the same lineage changing over time at primer sites. The
first implementation attempt was interrupted and could not be reproduced in the same
session, so the route is a new session on this task alone, working from that journal.
