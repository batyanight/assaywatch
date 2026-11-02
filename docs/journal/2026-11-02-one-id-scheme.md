# Every assay id follows one scheme, and the repository restarts from one commit (2026-11-02)

**Finding.** Ids, names and `target.gene` had grown in several styles, and some ids
named an author other than the one the entry cites: four of them, now
`Coronaviridae_RdRp_Quan_2010_round1`, `Caliciviridae_helicase_Neill_1995`,
`Apicomplexa_23S_Zhu_2000` and `Vairimorpha_bombi_18S_Klee_2006`, each carried a
different author's name before today. An id that disagrees with its own
citation sends a reader to the wrong paper.

**The scheme.** `<Taxon>_<gene>_<FirstAuthor>_<Year>[_<qualifier>][_roundN]`, built
from the entry's own fields: `target.taxon_name` (parenthetical dropped), a short
form of `target.gene`, the first author and year of `citation.reference`. A
qualifier appears only where two entries would otherwise collide, and is the
paper's own word where it has one (`_aquatic`, `_cladeIIab`, `_Mix7`) or else the
published name of the oligo that tells them apart (`_ARS16V`). Every round of a
nest carries `_roundN`, round 1 included, and `source.nested_family` is set to the
nest's base. Unpublished pending entries read `_unpublished`. All 227 entries
(220 live, 7 pending) were renamed; `name` is now `<taxon> — <gene> (<author>
<year>[, qualifier])[, nested round N]`, and `target.gene` was normalised to the
locus (positional detail a curator measured, such as ON563414.2 coordinates, kept).

**Checked after the rename.** The 34 protocols and 31 families assemble exactly as
before; every entry validates; the 2026-11-01 calls table was remapped in place
(3,519,074 rows, none unmapped; the original kept beside it as
`calls.tsv.gz.pre-rename`, run state only) and the website extract from it is
identical in counts (219 assays, 17 withheld). The run's reports were regenerated
from the remapped table and replace the two earlier example runs under `docs/`.

**One gene was wrong.** Three entries citing Hellgren et al. 2004 said
"cytochrome c". The paper's methods say the primers "were designed within the 5'
end of the cytochrome b gene"; corrected, with a dated note on each.

**Removed from the schema.** `citation.as_written`, a free-text copy of a citation
string. Three entries used it as their only reference and now carry it as
`citation.reference`. The four tools that fell back to it read `reference` only.

**Old ids.** `local/rename-mapping.tsv` maps every earlier id to its current one,
chains collapsed so each old id resolves in one step. It is a maintainer-only file
and not in the repository; `scripts/report_diff.py`, `retrospective.py` and
`lineage_override_audit.py` read it when present and treat its absence as "no
renames", so a fresh clone runs them unchanged.

**A validator rule.** An entry whose text names a source list is refused, in
`registry/` and `pending/` alike (`registry.names_a_source_list`). Every entry cites
its own paper.

**History.** The repository was restarted from the cleaned tree as a single commit,
on the 2026-10-31 reasoning (`journal/2026-10-31-repository-recreated.md`): a
rewrite leaves old objects fetchable by SHA, a fresh repository leaves none. This
time both earlier GitHub repositories were deleted rather than kept private. The
earlier history survives only on the maintainer's machine, outside the repository:
a git bundle taken today and the bare mirror taken on 2026-10-31.

**Also changed today.** Each round's standalone figure on a protocol page is now
taken on the protocol's own records, scope and recent window
(`nested.round_calls`), rather than copied from the round's own assessment. On the
*C. trachomatis* protocol that shows the genus round 1 detecting **0 of 39** recent records, which its genus-wide figure (41.2%)
had hidden. Not yet investigated.

**Later the same day.** `Sarcocystis_18S_5_8S_Kutkiene_2010_ShortITS1R` moved to
`pending/` as `Sarcocystis_18S_5_8S_unpublished`. Its forward primer P-ITSF is
Kutkienė et al. 2010's (Table 1, pair 7), but the reverse primer ShortITS1R is in
neither that paper nor the group's 2007 and 2020 papers held locally, so the pair has
no published source. Its sibling, P-ITSF/P-ITSR, stays live.
A sweep for the same mistake (`scripts/verify_oligos_against_paper.py` over every live
entry against the local papers, then the `oligo_source_unresolved` and
`oligos_not_in_cited_paper` flags) found three more, each with one primer in its cited
paper and a partner printed nowhere: the two Rebelo 2011 16S-23S pairs (16-23-R1 and
16-23-F3) and the van Kuppeveld 1992 16S pair (MycoRev1). All three moved to `pending/`
with `_unpublished` ids; 216 assays are live. The other flagged entries were checked
and have a published source (a later design paper, a figure, or a shifted copy of a
printed primer). The test fixtures' degenerate-primer slot moved from the van Kuppeveld
pair to `Reptarenavirus_GP_Aqrawi_2015`; every edited-site fixture record is unchanged. Separately, a page whose
product length varies (no single `amplicon_bp`) printed "Amplicon: —"; it now shows
the measured `amplicon_bp_range` and a per-species size table.
