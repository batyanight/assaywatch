"""Accession identity, and the guard that keeps the open-coded version back out.

`strip_version` and `version_of` lived in report.py, where only its own four
call sites used them; twenty-four other sites wrote `record_id.split(".")[0]`
instead. That is not the same function: measured on
`results/2026-10-20/calls.tsv.gz`, the two answers differ on 98 of 1,276,853
distinct record ids, every one a PDB chain, and at a site that joins calls to
esummary metadata the bare split drops those records.
"""

from __future__ import annotations

import re
from pathlib import Path

from assaywatch.accession import strip_version, version_of

ROOT = Path(__file__).resolve().parent.parent


def test_a_numeric_tail_is_a_version_and_nothing_else_is():
    assert strip_version("AB123456.2") == "AB123456"
    assert strip_version("AB123456") == "AB123456"
    assert strip_version("NC_001.2.3") == "NC_001.2"  # only the last .N goes
    assert strip_version("scaffold.contig") == "scaffold.contig"  # not a version


def test_a_fasta_header_is_cut_at_the_first_space():
    assert strip_version("AB123456.1 Bd isolate 5 ITS") == "AB123456"


def test_a_pdb_chain_joins_its_esummary_form():
    """The case the bare split gets wrong: both spellings must map together."""
    assert strip_version("pdb|29WD|T") == strip_version("29WD_T") == "29WD_T"
    assert strip_version("pdb|9EC3|a") == "9EC3_a"


def test_a_pdb_entry_with_no_chain_keeps_just_the_entry():
    assert strip_version("pdb|29WD|") == "29WD"


def test_version_of_reads_the_tail_or_zero():
    assert version_of("AB123456.2") == 2
    assert version_of("AB123456") == 0
    assert version_of("AB123456.1 Bd isolate") == 1
    assert version_of("scaffold.contig") == 0
    assert version_of("") == 0


def test_the_empty_string_survives_both():
    assert strip_version("") == ""


def test_report_still_re_exports_them():
    """Callers importing from report.py keep working; the module only moved."""
    from assaywatch import report

    assert report.strip_version is strip_version
    assert report.version_of is version_of


# The guard. A bare `split(".")` on a record id is the bug this module replaced,
# so it must not come back. Filename stems and module paths are not accessions
# (collect.stem_order, triggers) and are deliberately not matched here.
ACCESSION_SPLIT = re.compile(r"""(?:accession|record_id|\brid\b|\bacc\b)[^\n]{0,30}\.split\(["']\.["']\)""")


def test_no_source_file_splits_an_accession_on_a_dot_any_more():
    offenders = []
    for path in sorted((ROOT / "assaywatch").glob("*.py")) + sorted((ROOT / "scripts").glob("*.py")):
        if path.name == "accession.py":
            continue
        for n, line in enumerate(path.read_text().splitlines(), 1):
            if ACCESSION_SPLIT.search(line):
                offenders.append(f"{path.relative_to(ROOT)}:{n}: {line.strip()}")
    assert not offenders, "use assaywatch.accession.strip_version instead:\n" + "\n".join(offenders)


def test_the_guard_can_actually_see_the_pattern_it_forbids():
    """Without this, a broken regex would make the guard above vacuously pass."""
    assert ACCESSION_SPLIT.search('acc = row["accession"].split(".")[0]')
    assert ACCESSION_SPLIT.search('base = rid.split(".")[0]')
    assert not ACCESSION_SPLIT.search('stem = path.name.split(".")[0]')
