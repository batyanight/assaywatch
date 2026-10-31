"""Accession identity: the one place that decides when two record ids are the same record.

An accession is not a reporting concern, but both helpers lived in `report.py`
and only its four call sites used them. Twenty-odd other sites open-coded
`record_id.split(".")[0]`, which is the same intent with a different answer:
measured on `results/2026-10-20/calls.tsv.gz`, the two disagree on 98 of
1,276,853 distinct record ids, and all 98 are PDB chains (`pdb|9EC3|a` ->
`9EC3_a` here, left whole by the bare split). At every site that joins calls
to esummary metadata, the bare split silently dropped those records - the same
failure mode as the 476 missing PDB-derived calls that `strip_version`'s PDB
branch was written for, one layer down.

So the rule is: anything comparing or joining on a record id calls these, and a
bare `split(".")` on an accession is a bug. A filename stem or a module path is
not an accession and is left alone (`collect.stem_order`, `triggers`).
"""

from __future__ import annotations


def strip_version(accession: str) -> str:
    """`AB123456.2` -> `AB123456`. Leaves anything without a version alone.

    This is the join key between two things NCBI names differently: the FASTA
    header (what screening sees) and the esummary caption (what carries the
    deposit date). Get it wrong and records silently lose their date and drop out
    of the drift denominator, which is how 476 PDB-derived calls went missing.

    PDB chains come back from efetch as `pdb|29WD|T` in the FASTA but as
    `29WD_T` in esummary; both are mapped to the latter so they join.

    Only a numeric tail is a version, so `scaffold.contig` is left whole and
    `NC_001.2.3` loses just the `.3`.
    """
    head = accession.split()[0] if accession.split() else accession
    if head.startswith("pdb|"):
        parts = head.split("|")
        return "_".join(p for p in parts[1:3] if p)
    stem, _, tail = head.rpartition(".")
    return stem if stem and tail.isdigit() else head


def version_of(accession: str) -> int:
    """The `.N` version of an accession, 0 when there is none."""
    tail = accession.split()[0].rpartition(".")[2] if accession.split() else ""
    return int(tail) if tail.isdigit() else 0
