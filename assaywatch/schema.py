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

IUPAC_RE = re.compile(r"^[ACGTURYSWKMBDHVN]+$")
# `seq_as_written` additionally allows I, which is a real nucleotide rather
# than an ambiguity code and so is kept out of the strict `seq` field.
AS_WRITTEN_RE = re.compile(r"^[ACGTURYSWKMBDHVNI]+$")
DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$")
OLIGO_MIN, OLIGO_MAX = 15, 40
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


class Strict(BaseModel):
    """Base with extra keys forbidden, so a typo like `taxon_nam` fails loudly."""

    model_config = ConfigDict(extra="forbid")


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
        if not OLIGO_MIN <= len(v) <= OLIGO_MAX:
            raise ValueError(f"length {len(v)} outside {OLIGO_MIN}-{OLIGO_MAX} nt")
        return v


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
    # Extra Entrez term ANDed onto the taxon query at retrieval, e.g.
    # `invA[Gene] OR "invasion protein"[Title]`. Without it the whole taxon is
    # fetched, which for E. coli is sixteen million records. Assays with the
    # same taxid and the same query share one retrieval group and one archive.
    query: str | None = None


class Citation(Strict):
    doi: str | None = None
    design_year: int | None = Field(default=None, ge=1985, le=2100)
    n_sequences_at_design: int | None = None
    as_written: str | None = None
    doi_verified: bool = False
    reference: str | None = None

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
    # A nested assay is stored as two entries, `..._round1` and `..._round2`,
    # linked only by this field and by their ids. Nothing yet checks that the
    # round-2 sites lie inside the round-1 product, so the two are reported
    # separately on different denominators — see the review doc.
    nested_round: str | None = None
    notes: list[str] | None = None
    notes_curator: str | None = None


class Assay(Strict):
    id: str = Field(pattern=r"^[A-Za-z0-9][A-Za-z0-9_.-]{2,120}$")
    name: str
    target: Target
    chemistry: Chemistry
    oligos: Oligos
    amplicon_bp: int | None = Field(default=None, ge=AMPLICON_MIN, le=AMPLICON_MAX)
    citation: Citation
    use_context: list[str] = Field(default_factory=list)
    submitted_by: str | None = None
    status: Status = Status.draft
    source: Source | None = None
    needs_review: list[str] | None = None

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
        """`active` is the promise that this assay can be screened and cited."""
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
        if self.submitted_by is None:
            missing.append("submitted_by")
        if self.needs_review:
            missing.append(f"needs_review must be empty (has {self.needs_review})")
        if missing:
            raise ValueError("status=active but missing: " + ", ".join(missing))
        return self
