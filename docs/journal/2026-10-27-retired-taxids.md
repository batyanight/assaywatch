# Eighteen entries come off taxids NCBI has retired, without re-fetching anything

2026-10-27, late. `scripts/check_taxids.py`'s containment check found these on its first
run, while reporting 4,113 scope escapes that were all false
(`2026-10-27-taxid-containment-and-merged-roots.md`): every one of those children had an
ancestor list carrying a NEW root id, because the registry's root had been merged away.

| old | new | NCBI's name for it | entries |
|---|---|---|---|
| 11232 | 3052342 | *Morbillivirus canis* | 9 CDV |
| 121791 | 3052225 | *Henipavirus nipahense* | 2 Nipah |
| 11051 | 3044782 | *Orthoflavivirus* | 3 pan-flavivirus |
| 10292 | 3044472 | *Orthoherpesviridae* | 4 pan-herpes |

Nothing was broken. Entrez resolves a merged id, so every fetch worked and every report
was right — which is the whole reason this was worth doing on a schedule rather than
when something failed. An entry on a retired id is one taxonomy release from an empty
archive, and the failure mode is silence: a fetch that returns nothing reads exactly
like a taxon with no new deposits.

## The cost was in the archives, not the YAML

`data/retrieved/` is keyed by `target.taxid`, so changing one moves the entry's retrieval
group. Done in order:

1. `scripts/retire_merged_taxids.py --check-ncbi --write` rewrote `target.taxid` on the
   18 entries and appended one dated sentence to each `notes_curator`. The mapping is
   pasted into the script rather than inferred, and `--check-ncbi` re-asks NCBI and
   refuses to run if any pair has moved since.
2. The four archive directories were moved to the new ids: 1.0 MB, 248 KB, 29 MB and
   273 MB, nothing re-downloaded.
3. **The manifest was remapped, not rebuilt.** This is the part worth recording.
   `scripts/rebuild_manifest.py` is the right tool for a LOST manifest and the wrong one
   here: it indexes the archives on disk, one entry per file, which is 497 entries where
   this manifest holds **3,409** — because 2,910 of them are incremental runs that
   fetched nothing. Those entries carry the cursor, the last date each group was *asked*,
   and `last_run_date` reads it to decide what to request next. A rebuild would have set
   every cursor in the project back to the date of its group's newest archive and re-asked
   NCBI for the window in between, across all 132 groups, for no gain. The remap rewrote
   159 runs: taxid, archive paths, and the query string, because the cursor is keyed on
   the query and `txid11232[Organism:exp]` had to become `txid3052342[...]` or the group
   would read as never fetched.

Checked before the run: all five moved groups resolve a cursor of 2026/10/27, so the next
fetch is incremental.

## The run

Every cached screen is stale regardless of this change, because `assaywatch/schema.py` is
in the screen signature's import closure and tonight's `exclusivity_taxids` and
`conditions` blocks are in it. So this run is the confirming rescreen for everything
committed tonight, and the 497 MB of cached screens were set aside as
`results/screened.pre-retired-taxids-2026-10-27` rather than deleted.

<!-- RUN RESULT APPENDED BELOW AFTER report_diff -->
