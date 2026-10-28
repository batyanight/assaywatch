"""The controlled vocabulary for `Assay.needs_review`.

A review flag is a *filter*: the thing you select on when you want every entry
whose oligos came from a figure, or every entry blocked from `active`. The
specifics of one entry's case are prose, and prose belongs in
`source.notes_curator` (the long record) or in this item's own `note` (the
one-line version a filtered list should show beside the flag).

The field did not start out that way. Before 2026-10-21 it was
`list[str]` with no vocabulary, and it had drifted to 98 distinct strings over
243 instances on 208 entries: 69 of those strings occurred exactly once, and
several were whole sentences wearing underscores
(`SCOPE_HUMMINGBIRD_AVIPOX_CLADE_ONLY_3_OF_1092_GENUS_RECORDS_DETECT`). A list
where two thirds of the values are unique is a prose field, and it cannot be
filtered, counted or audited, which is the only reason to have one.

Two things were learnt while migrating it, and both are encoded here.

**A flag that restates a field goes stale in silence.** `DOI_MISSING`,
`DOI_UNVERIFIED`, `NO_YEAR` and `TAXID_MISSING` said what `citation.doi`,
`citation.doi_verified`, `citation.design_year` and `target.taxid` already say.
At migration, 6 of their 39 instances were wrong: four entries carried
`DOI_MISSING` with a verified DOI on the same entry and two carried `NO_YEAR`
with `design_year: 2011`, because the gap had been filled and nobody cleared
the flag. Those four flags are gone; the gap is derived from the field instead. A
derived answer cannot go stale.

**Not every caveat is a question.** The old field conflated "a human still has
to decide something" with "this is a known, settled property of the entry worth
disclosing". `status: active` refused any non-empty `needs_review`, so
`nested_protocol` or `amplicon_measured_not_published` — permanent, documented,
nothing to resolve — blocked activation forever. 146 of 208 entries were
flagged, so the gate was effectively "almost nothing may ever be active".
`OPEN` below splits the two, and the gate now refuses only open questions.

`docs/needs-review-migration.tsv` records all 243 old values with the flag and
note each became, so the migration is auditable and reversible by reading rather
than by guessing.
"""

from __future__ import annotations

from enum import StrEnum


class ReviewFlag(StrEnum):
    """Every value `needs_review[].flag` may take.

    Adding one is a deliberate act: it must be a category a filter would ask
    for, not one entry's story. If it would only ever apply to a single assay,
    it is a `note` on a broader flag, or it is `curation_decision_pending`.
    """

    # ---- open questions: a human has to answer these, and `active` waits ----

    # The publication these oligos should be cited to is not settled, or no
    # citable source exists (a lab sheet, an anonymous protocol).
    citation_unresolved = "citation_unresolved"
    # Which source the sequences actually came from is not established.
    oligo_source_unresolved = "oligo_source_unresolved"
    # The sequence as entered may itself be wrong: read off an illegible
    # figure, OCR'd, truncated, or of a length the source contradicts.
    oligo_sequence_uncertain = "oligo_sequence_uncertain"
    # No product size is declared, or the declared and published sizes
    # disagree and the disagreement has not been explained.
    amplicon_size_unresolved = "amplicon_size_unresolved"
    # What this assay is meant to detect is not settled: the scope is unstated,
    # or it detects a second taxon and no one has decided whether that taxon
    # deserves its own entry.
    target_scope_unresolved = "target_scope_unresolved"
    # Overlaps another registry entry and a keep-or-merge decision is pending.
    duplicate_entry_unresolved = "duplicate_entry_unresolved"
    # Marked do-not-use at source; a keep-or-delete decision is pending.
    do_not_use = "do_not_use"
    # No evidence either way: never run in the lab, and nothing in silico.
    not_validated = "not_validated"
    # The retrieval query changed after the last fetch, so the numbers
    # currently on this entry describe a different archive.
    retrieval_stale = "retrieval_stale"
    # An open question none of the above names. Requires a `note`; a filter
    # that returns this flag is asking "what has not been decided yet", and a
    # bare `curation_decision_pending` answers nothing. Watch its count: if it
    # grows, the flags above are missing a category.
    curation_decision_pending = "curation_decision_pending"

    # ---- recorded caveats: settled, disclosed, and no bar to `active` -------

    # The registry sequence is a deliberate modification of the published one.
    oligos_modified = "oligos_modified"
    # Read from a citing paper, a second paper, or a mix of sources, rather
    # than from the designer's own table.
    oligos_from_secondary_source = "oligos_from_secondary_source"
    # Read off a figure rather than a table, legibly.
    oligos_read_from_figure = "oligos_read_from_figure"
    # Established that the cited paper prints different sequences, or none.
    oligos_not_in_cited_paper = "oligos_not_in_cited_paper"
    # The reference or DOI was reconstructed from citing papers, or found by a
    # title search, rather than read off the source itself.
    citation_is_indirect = "citation_is_indirect"
    # Strand assignment inferred from coordinates or from the source's labels,
    # not stated by the source.
    orientation_inferred = "orientation_inferred"
    # Which oligos pair together is the curator's reading of a source that
    # listed several in one block without saying.
    pairing_is_curator_reading = "pairing_is_curator_reading"
    # The size is measured from GenBank records because the source gives none.
    amplicon_measured_not_published = "amplicon_measured_not_published"
    # The measured size differs from the published one. The measurement is
    # what the entry carries; the note records both numbers.
    amplicon_disagrees_with_paper = "amplicon_disagrees_with_paper"
    # Several product sizes occur across records; no single size describes it.
    amplicon_multimodal = "amplicon_multimodal"
    # Detects taxa outside the declared target.
    cross_reactive = "cross_reactive"
    # Detects only part of the declared taxon, by design or in fact.
    scope_narrower_than_taxid = "scope_narrower_than_taxid"
    # The retrieval query provably misses records that belong to the target.
    retrieval_scope_incomplete = "retrieval_scope_incomplete"
    # Part of a nested or semi-nested protocol.
    nested_protocol = "nested_protocol"
    # Shares an oligo with another registry entry.
    shares_oligos_with_sibling = "shares_oligos_with_sibling"
    # A multiplex pool, or two protocols, entered as a single assay.
    pooled_as_one_assay = "pooled_as_one_assay"
    # Measured sequence variation at a primer or probe site.
    primer_site_polymorphic = "primer_site_polymorphic"
    # Too few records to support a verdict either way.
    thin_evidence = "thin_evidence"
    # The readout is not an amplicon this pipeline can model: isothermal
    # chemistry, or identification by digest.
    not_screenable = "not_screenable"
    # The gene label, locus boundary or copy number is the curator's best
    # reading of an ambiguous source.
    target_annotation_uncertain = "target_annotation_uncertain"
    # A chemistry detail the source never stated: a reporter, a quencher, the
    # length of a tail.
    chemistry_detail_missing = "chemistry_detail_missing"
    # The paper prints no thermal protocol: no annealing temperature, no cycling.
    # Separate from `chemistry_detail_missing`, which is about the oligo, because
    # this one is the reason `thermo: false` ships -- a mismatch's cost cannot be
    # read without the temperature the reaction ran at. A filter that returns
    # this flag is asking which entries can never support a thermodynamic call.
    conditions_not_printed = "conditions_not_printed"


#: The flags that are open questions. Membership is a property of the flag, not
#: of the entry: whether `oligos_read_from_figure` is a to-do is not something
#: two curators should be able to answer differently on two entries. Everything
#: in `ReviewFlag` and not in here is a recorded caveat.
OPEN: frozenset[ReviewFlag] = frozenset(
    {
        ReviewFlag.citation_unresolved,
        ReviewFlag.oligo_source_unresolved,
        ReviewFlag.oligo_sequence_uncertain,
        ReviewFlag.amplicon_size_unresolved,
        ReviewFlag.target_scope_unresolved,
        ReviewFlag.duplicate_entry_unresolved,
        ReviewFlag.do_not_use,
        ReviewFlag.not_validated,
        ReviewFlag.retrieval_stale,
        ReviewFlag.curation_decision_pending,
    }
)

#: Flags whose whole content is the specifics, so a bare flag says nothing.
NOTE_REQUIRED: frozenset[ReviewFlag] = frozenset({ReviewFlag.curation_decision_pending})

#: Recorded caveats, for callers that want the complement without recomputing it.
CAVEAT: frozenset[ReviewFlag] = frozenset(ReviewFlag) - OPEN

#: Caveats that cast doubt on THE OLIGOS THEMSELVES -- the sequences every call
#: in a screen depends on. A subset of CAVEAT, and the distinction matters: 24 of
#: the 38 assays called `declining` on 2026-10-22 carried one of these, and
#: re-reading a paper to confirm a sequence is a different job from redesigning
#: an assay, so the report's triage list puts entries without them first.
#:
#: Being a caveat is NOT enough to be here. `amplicon_measured_not_published`
#: means the product size was measured on real records instead of quoted from a
#: paper, which is this project's preferred practice ("measure, never quote" --
#: CLAUDE.md), not a doubt; `cross_reactive` is a specificity disclosure about a
#: correct entry; `retrieval_scope_incomplete` is about which records were
#: fetched. Treating every caveat as doubt ranked those three alongside
#: `oligos_not_in_cited_paper`, which is backwards.
OLIGO_DOUBT: frozenset[ReviewFlag] = frozenset(
    {
        ReviewFlag.orientation_inferred,
        ReviewFlag.oligos_modified,
        ReviewFlag.oligos_from_secondary_source,
        ReviewFlag.oligos_not_in_cited_paper,
        ReviewFlag.oligos_read_from_figure,
        ReviewFlag.pairing_is_curator_reading,
        ReviewFlag.thin_evidence,
    }
)
# A strict subset of CAVEAT, asserted in tests/test_review.py. `oligo_source_unresolved`
# and `oligo_sequence_uncertain` are doubts about oligos too, and they are deliberately
# NOT here: both are OPEN questions, so the report holds those entries out of scoring
# altogether and they can never reach a list that ranks scored assays.
