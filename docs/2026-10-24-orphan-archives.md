# The 10 orphan archive groups, identified (2026-10-24)

`scripts/orphan_archives.py` has reported 10 orphan groups, 21 archives, 658 MB for some
days, and `docs/RESUME-HERE.md` has carried the delete-or-keep as a maintainer decision
with nothing but sizes to decide on. This resolves what each group actually is. **Nothing
was deleted.** The script only reports, and so does this.

## What they are

| group | taxon | MB | why it is orphaned |
|---|---|---|---|
| `1387563/all` | *Ophidiomyces ophidiicola* (snake fungal disease) | 530 | its three live entries now retrieve under two query groups, `qdb308affab` and `qe3c757aa37` |
| `1357716/all` | *Batrachochytrium salamandrivorans* | 90 | its live entry now retrieves under `qf659bd13f6` |
| `11270/all` | Rhabdoviridae | 16 | both live L-gene entries now retrieve under `qdb266b171e` |
| `12059/q2b612305e5` | Enterovirus | 10 | **pending**: the two `ENTEROVIRUS_ssRNA_5_UTR_VP4_VP2` rounds |
| `10780/all` | Parvovirus | 10 | **pending**: `PARVOVIRUS_ssDNA_VP1_gene_pan_parvo` |
| `2093/q4185828e3e` | *Mycoplasma* | 1 | its four live entries now carry **no** query, so they retrieve under `all` |
| `11723/qd1f93d8a77` | Simian immunodeficiency virus | 0 | its six live entries now retrieve under `q49bae82c9c` |
| `1170234/all` | Feline morbillivirus | 0 | **pending**: `Feline_Morbillivirus_L_gene` |
| `208294/all` | Seadornavirus | 0 | no entry, live or pending, names this taxid |
| `1430836/all` | *Perigonica* | 0 | **a genus of moths** |

## What that means for the decision

**636 of the 658 MB is superseded pre-query history for taxa the registry still covers.**
Ophidiomyces, *B. salamandrivorans*, Rhabdoviridae, *Mycoplasma* and SIV all have live
entries; what changed is the retrieval query, which is part of the group key, so the old
whole-taxon fetch became unreachable the moment a narrower query was added (and, for
*Mycoplasma*, the moment one was removed). These are not archives of abandoned work. They
are the same taxa, fetched more broadly than the entries now ask for.

That cuts both ways and the size is the whole argument. Re-fetching 530 MB of Ophidiomyces
from NCBI is the expensive direction, and the group would come back only if an entry
dropped its query again. Keeping it costs disk and one line of orphan report.

**`1430836/all` is a moth and should go whatever is decided about the rest.** *Perigonica*
is one of the wrong-taxid artefacts this project already documented - the "three taxids
naming the wrong organism, one of them a genus of moths" in
`scripts/verify_oligos_against_paper.py`'s own docstring. The taxid was corrected; its
archive is the fetch made under the error. `208294/all` (Seadornavirus) is the same shape
minus the error: no entry has ever claimed it. Both are 0 MB, so this is tidiness, not space.

**The three pending groups stay**, which is what the script already advises: 20 MB, and they
are those assays' history for when their DOIs resolve.

## Not done here, and why

Deleting is irreversible without re-downloading, and NCBI rate-limits, so it stays a
maintainer decision rather than something a session does on its own. What was missing was
not the authority but the information: nobody could weigh 530 MB without knowing it was
Ophidiomyces. Now it is on the record.

One thing found on the way, unrelated to deletion: **three LIVE groups have no archive at
all and have never been screened** - `10257/all`, `10258/all` and `129727/all`. Those are
the three parapoxvirus entries added on 2026-10-24. They will be retrieved on the next
pipeline run; the screens behind their entry notes were run by hand against a direct
`efetch`, which the notes say.
