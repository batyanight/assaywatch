"""Registry schema: what a valid assay YAML file looks like.

One pydantic model per YAML block. Pydantic turns a dict loaded from YAML into
typed Python objects and raises a ValidationError listing every field that is
wrong, so a bad file fails with a readable message instead of a KeyError deep
inside the matcher. The same models serve three purposes:

* `validate` CLI and the pre-commit hook: reject bad files before they are committed.
* The pipeline: downstream code works with `Assay` objects, never raw dicts.
* Documentation: `Assay.model_json_schema()` emits JSON Schema for contributors.

Two tiers of strictness, keyed on `status`:

* draft: structure must be right, oligos must be real IUPAC sequences, but
  taxid / DOI / design_year may be null (that is what "draft" means).
* active: everything required for screening must be present: taxid, DOI,
  design_year, and no unresolved review flags.
"""

from __future__ import annotations

import re
from enum import StrEnum
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

from .review import NOTE_REQUIRED, OPEN, ReviewFlag

IUPAC_RE = re.compile(r"^[ACGTURYSWKMBDHVN]+$")
# `seq_as_written` additionally allows I, which is a real nucleotide rather
# than an ambiguity code and so is kept out of the strict `seq` field.
AS_WRITTEN_RE = re.compile(r"^[ACGTURYSWKMBDHVNI]+$")
DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$")
OLIGO_MIN, OLIGO_MAX = 15, 40
# A probe's floor is lower than a primer's. MGB and LNA hydrolysis probes are
# routinely published at 13-14 nt, because the minor-groove binder (or the LNA
# bases) supplies the Tm that length alone does not, so a 15 nt floor would
# refuse an assay for being what its paper says it is. Haynes et al. 2023
# (doi:10.1371/journal.pone.0289159) prints several 13-14 nt probes, which is how
# this came up. 12 is not a considered biophysical limit; it is low enough to
# admit every published probe seen so far and high enough to catch a mistyped
# 3-base "probe". The matcher is safe with it for a structural reason: a probe is
# searched only inside the span between the two primers (score.screen_one), so
# the stretch it can chance-match in is tens to hundreds of bases, not a genome.
# Primers keep OLIGO_MIN, since a primer is searched along the whole record.
PROBE_MIN = 12
# The floor on the part of a tailed oligo that actually binds the target. It is
# one base below OLIGO_MIN because a real published primer sits there: Briese et
# al. 2007 (doi:10.1007/s00705-007-1069-z) Table 1 prints BUN-S3-R as a 6 nt
# cloning tail plus 14 nt of authentic sequence. A 14-mer is short for a primer,
# but this one is anchored on the orthobunyavirus segment terminus — the most
# conserved sequence in the genome — and a tailed primer anneals over its full
# length from round 2 onwards, once the product carries the tail. So the short
# footprint is the first-round specificity only. These floors exist to catch a
# mistyped 3-base "oligo" that would match everywhere, not to overrule a
# published table.
OLIGO_MIN_BINDING = 14
AMPLICON_MIN, AMPLICON_MAX = 50, 3000  # outside this range the matcher's orientation rule misfires


class Status(StrEnum):
    draft = "draft"
    active = "active"
    deprecated = "deprecated"


class Chemistry(StrEnum):
    conventional = "conventional"  # primers only; endpoint PCR or SYBR
    sybr = "sybr"
    hydrolysis_probe = "hydrolysis_probe"
    mgb = "mgb"
    lna = "lna"
    # Recombinase polymerase amplification: primers only, but isothermal at
    # 37-42 C with a recombinase driving strand invasion, not thermal cycling.
    # Listed separately rather than filed under `conventional` because the
    # scoring penalties in config.yaml are calibrated on PCR: RPA uses 30-35mers
    # and its mismatch tolerance is not Taq's. A call on an RPA assay says
    # "the primer sequences still match the deposits", which is the useful
    # question for drift, and nothing more.
    rpa = "rpa"


class Strict(BaseModel):
    """Base with extra keys forbidden, so a typo like `taxon_nam` fails loudly."""

    model_config = ConfigDict(extra="forbid")


class ReviewItem(Strict):
    """One review flag, with the one line of prose that makes it actionable.

    The vocabulary, and which flags are open questions rather than recorded
    caveats, live in `assaywatch.review`; read that module's docstring before
    adding a flag.
    """

    flag: ReviewFlag
    # The specifics, in a line: what disagrees with what, which taxon, which
    # sibling entry. Optional, because for a flag like `cross_reactive` the
    # flag is the whole finding and the detail lives in `source.notes_curator`.
    note: str | None = None

    @model_validator(mode="after")
    def note_present_where_it_carries_the_meaning(self) -> ReviewItem:
        if self.flag in NOTE_REQUIRED and not (self.note or "").strip():
            raise ValueError(f"needs_review flag {self.flag.value} requires a note saying what is pending")
        return self

    @property
    def is_open(self) -> bool:
        """True if a human still has to answer something, not merely know it."""
        return self.flag in OPEN


class Oligo(Strict):
    name: str | None = None
    seq: str
    seq_as_written: str | None = None  # keeps inosine if the original had it
    # 5' bases that do not bind the target: a restriction site and clamp on a
    # cloning primer, an M13 or adapter tail. Part of `seq` as ordered, left out
    # of matching_seq, because a tail mismatches every record by design.
    tail_5prime: str | None = None
    orientation: Literal["forward", "reverse", "probe"] | None = None  # only used in `alternates`

    @property
    def matching_seq(self) -> str:
        """The sequence to compare against records.

        `seq_as_written` wins when present: an inosine written as N would match
        G, which inosine barely does, and would be counted as a 4-fold
        degenerate position, which it is not.
        """
        s = (self.seq_as_written or self.seq).upper()
        if self.tail_5prime:
            s = s[len(self.tail_5prime) :]
        return s

    @field_validator("seq_as_written")
    @classmethod
    def as_written_alphabet(cls, v: str | None) -> str | None:
        if v is None:
            return v
        v = v.strip().upper()
        if not AS_WRITTEN_RE.match(v):
            bad = sorted(set(v) - set("ACGTURYSWKMBDHVNI"))
            raise ValueError(f"non-IUPAC characters {bad}")
        return v

    @model_validator(mode="after")
    def as_written_matches_seq(self) -> Oligo:
        """`seq_as_written` is `seq` with inosine restored, nothing else.

        It replaces `seq` for matching, so a shorter or different string here
        would silently change what is screened (a 3-base 'oligo' matches
        everywhere), and the tail is cut from it by length.
        """
        w = self.seq_as_written
        if w is not None and w.replace("I", "N") != self.seq:
            raise ValueError(f"seq_as_written {w} must equal seq {self.seq} with inosine (I) where seq has N")
        return self

    @model_validator(mode="after")
    def tail_is_a_prefix(self) -> Oligo:
        if self.tail_5prime is not None:
            t = self.tail_5prime.strip().upper()
            if not self.seq.startswith(t):
                raise ValueError(f"tail_5prime {t} is not the 5' end of seq {self.seq}")
            if len(self.seq) - len(t) < OLIGO_MIN_BINDING:
                raise ValueError(
                    f"binding part is {len(self.seq) - len(t)} nt after the {len(t)} nt tail, "
                    f"below the {OLIGO_MIN_BINDING} nt floor"
                )
            self.tail_5prime = t
        return self

    @field_validator("seq")
    @classmethod
    def iupac_and_length(cls, v: str) -> str:
        v = v.strip().upper()
        if not IUPAC_RE.match(v):
            bad = sorted(set(v) - set("ACGTURYSWKMBDHVN"))
            raise ValueError(f"non-IUPAC characters {bad}; inosine must be written as N in `seq`")
        # The lower bound depends on the oligo's role, which this validator
        # cannot see; `meets_length_floor` applies it. Here only the absolute
        # floor and the ceiling, so a 3-base string fails on its own terms.
        if not PROBE_MIN <= len(v) <= OLIGO_MAX:
            raise ValueError(f"length {len(v)} outside {PROBE_MIN}-{OLIGO_MAX} nt")
        return v

    @model_validator(mode="after")
    def meets_length_floor(self) -> Oligo:
        """A primer needs OLIGO_MIN nt; a probe needs only PROBE_MIN.

        An alternate states its role in `orientation`, and that decides it. The
        class cannot: `alternates` is `list[Oligo | Probe]`, so a too-short
        forward alternate fails as an Oligo and pydantic then retries it as a
        Probe, which would hand a 13 nt primer the probe floor. Only an oligo
        with no stated orientation (the `probe` field itself) falls back to class.
        """
        if self.orientation is not None:
            is_probe = self.orientation == "probe"
        else:
            is_probe = isinstance(self, Probe)
        floor = PROBE_MIN if is_probe else OLIGO_MIN
        if len(self.seq) < floor:
            role = "probe" if is_probe else "primer"
            raise ValueError(f"length {len(self.seq)} outside {floor}-{OLIGO_MAX} nt for a {role}")
        return self


class Probe(Oligo):
    reporter: str | None = None
    quencher: str | None = None
    lna: bool | None = None


class Oligos(Strict):
    forward: Oligo
    reverse: Oligo
    probe: Probe | None = None
    alternates: list[Oligo | Probe] = Field(default_factory=list)


class Target(Strict):
    taxid: int | None = None
    taxon_name: str | None = None
    gene: str | None = None
    genome_type: str | None = None  # free text for now; tighten to an enum once the retrieval rules need it
    # Which taxids are "in scope" for drift assessment. When set, only
    # records whose taxid is in this list, OR a descendant of one, count toward
    # the drift denominator (`drift.scope_taxonomy`, ancestry since 2026-10-19;
    # see docs/2026-10-19-scope-ancestry.md). Out-of-scope records are still
    # retrieved and screened (for cross-reactivity reporting) but do not
    # influence the stable/declining call. Because matching is ancestral, name
    # the smallest set of taxa whose subtrees cover the design paper's stated
    # range -- a genus or a subfamily, not an enumerated species list.
    scope_taxids: list[int] | None = None
    # Extra Entrez term ANDed onto the taxon query at retrieval, e.g.
    # `invA[Gene] OR "invasion protein"[Title]`. Without it the whole taxon is
    # fetched, which for E. coli is sixteen million records. Assays with the
    # same taxid and the same query share one retrieval group and one archive.
    query: str | None = None

    @model_validator(mode="after")
    def query_does_not_begin_with_not(self) -> Target:
        """Reject a query whose NOT has no left operand.

        retrieve.build_query emits `txid<N>[Organism:exp] AND ... AND (<query>)`.
        Entrez handles a NOT *inside* that parenthesised query correctly, but
        silently INVERTS one that starts it: `AND (NOT X)` returns exactly the
        records X matches. No error, no warning, and the archive comes back as
        the precise opposite of the intent.

        Measured on 2026-10-04, counts from esearch:

            txid562 AND (16S[Title])                    15188   A
            txid562 AND (16S[Title] AND ribosomal[..])  14246   B
            txid562 AND (16S[Title] NOT ribosomal[..])    942   = A - B, correct
            txid562 AND (NOT ribosomal[Title])          16733   inverted
            txid562 AND (ribosomal[Title])              16733   the same set

        So a NOT needs something to its left. Give the exclusion its own anchor:

            txid10492[Organism:exp] NOT (txid3432137[Organism:exp] OR ...)

        The fourteen registry queries of the form
        `(...) AND 1:30000[SLEN] NOT "whole genome shotgun"[Title]` are correct
        and unaffected.
        """
        q = (self.query or "").strip()
        if re.match(r"^\(*\s*NOT\b", q, re.IGNORECASE):
            raise ValueError(
                "query starts with NOT, which Entrez silently inverts once build_query "
                "parenthesises it (the archive comes back as exactly the records you meant "
                "to exclude). Put a term to the left of the NOT, e.g. "
                f"'txid{self.taxid}[Organism:exp] NOT (...)'"
            )
        return self


class Citation(Strict):
    doi: str | None = None
    design_year: int | None = Field(default=None, ge=1985, le=2100)
    n_sequences_at_design: int | None = None
    as_written: str | None = None
    doi_verified: bool = False
    reference: str | None = None
    # Does the cited paper DESIGN these oligos, or merely use them?
    #
    # This exists because conflating the two produced a wrong scoping decision
    # on 2026-10-04. The ranavirus MCP oligos were stored under Johnson et al.
    # 2008, a box-turtle and tortoise study, so the assay was scoped away from
    # the fish ranaviruses. They are in fact byte-identical to FV3-54F /
    # FV3-584R of Mao et al. 1997, which Grizzle et al. 2003 shows amplify every
    # ranavirus tested, fish included. The citation named where the sequences
    # were READ FROM; the scope follows from where they were DESIGNED.
    #
    #   True   the cited paper designed them; its claims bound the scope
    #   False  the cited paper used someone else's; find the design paper
    #          before scoping, and say so in source.notes_curator
    #   None   not established yet. The honest default, and the reason this
    #          field is nullable rather than defaulting to True.
    #
    # scripts/audit_provenance.py finds entries where the oligo names disagree
    # with the cited author, which is how the Johnson case would have been
    # caught by inspection.
    oligos_designed_here: bool | None = None

    @field_validator("doi")
    @classmethod
    def doi_shape(cls, v: str | None) -> str | None:
        if v is None:
            return v
        v = v.strip()
        if not DOI_RE.match(v):
            raise ValueError("DOI must look like 10.xxxx/...; strip any https://doi.org/ prefix")
        return v


class Source(Strict):
    spreadsheet: str | None = None
    # PREDICT consensus-PCR panel protocol id (P-001..P-041) when this assay's
    # oligos match that protocol's, per the Anthony et al. 2015 supplement. A
    # stable identifier across the PREDICT literature, so an entry can be
    # cross-referenced to it without relying on free text.
    predict_protocol: str | None = Field(default=None, pattern=r"^P-0\d\d$")
    rows: list[int] | None = None
    positive_control: str | None = None
    # A nested assay is stored as one entry per round, linked by this field and
    # by `nested_family`. Containment checks the declaration: the round-2 sites
    # must lie inside the round-1 product.
    nested_round: str | None = None
    # Which nest this entry belongs to, when the id base cannot say it. The base
    # (the id with any `_roundN` suffix removed) is the default and carries most
    # families; it fails three ways, all of them real here:
    #
    #   * an unrelated entry shares the base. The 440 bp coronavirus consensus
    #     entry sat in Lan 2010's nest and displaced its real round 1, which made
    #     the pair read as DISJOINT and put a false "two assays, not two rounds"
    #     finding in the 2026-10-14 report. Pair Lan's own rounds and they nest
    #     on 6,667 of the 6,671 records both rounds can be judged on.
    #   * a `_round2_2` disambiguator escapes the `_roundN` suffix, so a second
    #     nest on one base can never assemble. Two papers' CMV gB nests were
    #     crossed this way, pairing Deckers' round 1 with Prepens' round 2.
    #   * a nest spans several ids on several taxids, as the Chlamydia 16S nest
    #     does: one genus round 1 feeding three species-specific round 2 entries.
    #
    # Declared here so a curator says which entries belong together; containment
    # remains the check on that declaration, never its source.
    nested_family: str | None = None
    notes: list[str] | None = None
    notes_curator: str | None = None


class SpeciesSize(Strict):
    """One product-length band this assay gives for one species, as measured.

    For an assay that identifies the species by product length rather than by
    detecting one target, the length IS the readout, so it belongs here as
    numbers rather than in a curator note as prose. Measured from GenBank
    records by scripts/measure_species_sizes.py, never copied from the paper:
    on ATI the paper's stated sizes differ from the measured ones by 1-32 bp
    (see that entry's needs_review).

    A species can have more than one band — monkeypox clade I near 1067 bp and
    clade IIb near 1538 — so several rows may share a taxid. Bands from
    different species may overlap, because they genuinely do, and that is the
    limit of what a length can tell you: on ATI, vaccinia 1587-1615 and cowpox
    1598-1601 are not separable by size, which is why the design paper also ran
    an XbaI digest.
    """

    taxid: int = Field(ge=1)
    # [min, max] observed; equal when every record gave the same length.
    bp: list[int] = Field(min_length=2, max_length=2)
    n_records: int = Field(ge=1)  # records behind this band, so a thin row shows
    note: str | None = None  # the species name as the taxonomy had it, or a clade

    @model_validator(mode="after")
    def band_is_sane(self) -> SpeciesSize:
        lo, hi = self.bp
        if lo > hi:
            raise ValueError(f"species_sizes bp must ascend, got {lo}-{hi}")
        if lo < AMPLICON_MIN or hi > AMPLICON_MAX:
            raise ValueError(f"species_sizes bp {lo}-{hi} outside {AMPLICON_MIN}-{AMPLICON_MAX}")
        return self


class Assay(Strict):
    id: str = Field(pattern=r"^[A-Za-z0-9][A-Za-z0-9_.-]{2,120}$")
    name: str
    target: Target
    chemistry: Chemistry
    oligos: Oligos
    amplicon_bp: int | None = Field(default=None, ge=AMPLICON_MIN, le=AMPLICON_MAX)
    # For an assay whose product size is genuinely a range, not a point, and so
    # cannot be gated by a scalar. ORTHOPOXVIRUS ATI is the case: measured over
    # GenBank records its products run from volepox 542 bp through camelpox 879,
    # ectromelia 1220, monkeypox 1067 (clade I) or ~1538 (clade IIb), variola
    # ~1580 and vaccinia ~1600 to cowpox 1673 bp — declared 540-1700. That
    # spread IS the ATI length polymorphism the assay exists to read, not a
    # defect. Left with no declared size it was the one entry
    # `declared_tolerance` could not constrain at all.
    # [min, max]; mutually exclusive with `amplicon_bp`, and the tolerance is
    # applied outward from each end.
    amplicon_bp_range: list[int] | None = Field(default=None, min_length=2, max_length=2)
    # Measured product length per species, for an assay whose readout is the
    # length. Only meaningful with `amplicon_bp_range`, which is the declaration
    # that the length varies by species; the validator enforces that.
    #
    # SET IN EXACTLY ONE ENTRY, and so is `amplicon_bp_range` above, and so is
    # `Oligo.seq_as_written` on a probe. The 2026-10-20 audit counted these as
    # near-unused schema and they are not dead: the first two are what let
    # ORTHOPOXVIRUS ATI be declared at all (its product IS the readout, 540-1700
    # bp by species) and the third is the Deckers probe's inosine. A field used
    # once by the one entry that needs it is the schema doing its job, not a
    # candidate for removal. The field the audit was right about was
    # `submitted_by`, below.
    species_sizes: list[SpeciesSize] | None = None
    citation: Citation
    use_context: list[str] = Field(default_factory=list)
    # Who contributed this entry, for a genuine third-party submission. Null on
    # 207 of 208 entries, because the registry was bulk-imported by one curator,
    # and so NOT a precondition of `active` - see `active_requires_provenance`.
    submitted_by: str | None = None
    status: Status = Status.draft
    source: Source | None = None
    needs_review: list[ReviewItem] | None = None

    @model_validator(mode="after")
    def review_flags_do_not_repeat(self) -> Assay:
        """One flag, one item: two `cross_reactive` rows are two halves of one note."""
        seen = [i.flag.value for i in self.needs_review or []]
        dupes = sorted({f for f in seen if seen.count(f) > 1})
        if dupes:
            raise ValueError(
                f"needs_review repeats {', '.join(dupes)}; merge the notes into one item per flag"
            )
        return self

    @property
    def open_review(self) -> list[ReviewItem]:
        """The review items that are open questions, in the order given."""
        return [i for i in self.needs_review or [] if i.is_open]

    @model_validator(mode="after")
    def amplicon_range_is_sane(self) -> Assay:
        r = self.amplicon_bp_range
        if r is None:
            return self
        if self.amplicon_bp is not None:
            raise ValueError("give amplicon_bp or amplicon_bp_range, not both")
        lo, hi = r
        if lo >= hi:
            raise ValueError(f"amplicon_bp_range must ascend, got {lo}-{hi}")
        if lo < AMPLICON_MIN or hi > AMPLICON_MAX:
            raise ValueError(f"amplicon_bp_range {lo}-{hi} outside {AMPLICON_MIN}-{AMPLICON_MAX}")
        return self

    @model_validator(mode="after")
    def species_sizes_fit_the_declared_range(self) -> Assay:
        if not self.species_sizes:
            return self
        if self.amplicon_bp_range is None:
            raise ValueError(
                "species_sizes needs amplicon_bp_range: it is the declaration that this assay's "
                "product length varies by species, which is what makes per-species bands mean anything"
            )
        lo, hi = self.amplicon_bp_range
        for s in self.species_sizes:
            if s.bp[0] < lo or s.bp[1] > hi:
                raise ValueError(
                    f"species_sizes band {s.bp[0]}-{s.bp[1]} for taxid {s.taxid} falls outside "
                    f"amplicon_bp_range {lo}-{hi}"
                )
        return self

    @model_validator(mode="after")
    def probe_matches_chemistry(self) -> Assay:
        has_probe = self.oligos.probe is not None
        probe_chem = self.chemistry in {Chemistry.hydrolysis_probe, Chemistry.mgb, Chemistry.lna}
        if probe_chem and not has_probe:
            raise ValueError(f"chemistry {self.chemistry.value} declared but no probe given")
        if has_probe and not probe_chem:
            raise ValueError("a probe is given but chemistry is primers-only; use hydrolysis_probe/mgb/lna")
        return self

    @model_validator(mode="after")
    def active_requires_provenance(self) -> Assay:
        """`active` is the promise that this assay can be screened and cited.

        Every check below is evidence ABOUT THE ASSAY: it has a taxon to
        retrieve, a citation that resolves, a design year to date a baseline
        from, and no unresolved question. `submitted_by` is not - it is who
        contributed the entry - and it was dropped from this gate on 2026-10-21.

        It had become the gate. After S7 split open questions from recorded
        caveats, `submitted_by` blocked 167 of 208 entries and nothing else did,
        including all four remaining ROADMAP Phase 0 candidates, because the
        registry was bulk-imported from one spreadsheet and the literature by
        one curator: 207 of 208 entries leave it null. Filling it with one name
        207 times would be a rubber stamp carrying no information, and the
        audit had already called the field abandoned. The field stays, for
        genuine third-party submissions; it is simply not evidence that an
        assay works.

        What replaces it is judgement, which is where it belonged all along:
        CONTRIBUTING.md says a maintainer also wants the assay screened against
        real records with a defensible result, and only a maintainer sets
        `active`.
        """
        if self.status != Status.active:
            return self
        missing = []
        if self.target.taxid is None:
            missing.append("target.taxid")
        if self.citation.doi is None:
            missing.append("citation.doi")
        if not self.citation.doi_verified:
            missing.append("citation.doi_verified=true")
        if self.citation.design_year is None:
            missing.append("citation.design_year")
        # Open questions only. A recorded caveat is a disclosure, not a defect:
        # `nested_protocol` and `amplicon_measured_not_published` are permanent
        # properties of perfectly good entries, and refusing them here is what
        # made 146 of 208 entries permanently unactivatable before 2026-10-21.
        # See `assaywatch.review`.
        if open_items := self.open_review:
            flags = ", ".join(i.flag.value for i in open_items)
            missing.append(f"needs_review has open questions ({flags})")
        if missing:
            raise ValueError("status=active but missing: " + ", ".join(missing))
        return self
