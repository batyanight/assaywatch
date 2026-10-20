"""assaywatch.metadata reads deposit titles and the patent-division flag from the archive."""

import gzip

from assaywatch.metadata import looks_like_patent, read_patent_accessions

# What GenBank gives a patent-division deposit as its title, and an ordinary one.
PATENT = "JP 2021522784-A/5: SYNTHETIC CHIMERIC VACCINIA VIRUS"
KOREAN = "KR 1020250052416-A/4: CHIMERIC POXVIRUSES"
NATURAL = "Orthopoxvirus vaccinia strain CEPHR_IRE_2026_486, complete genome"
ENGINEERED = "UNVERIFIED: Mutant Orthopoxvirus vaccinia isolate MVA-syn4-contig1_pilon genomic sequence"


def test_looks_like_patent_reads_the_citation_not_the_subject():
    assert looks_like_patent(PATENT)
    assert looks_like_patent(KOREAN)
    # The other title form that names the patent (152 archived records, 2026-10-20).
    assert looks_like_patent("Patent application sequence for WO 2026009883-A/7")
    assert not looks_like_patent(NATURAL)
    # The class no pattern can catch: a patent record titled with the invention
    # name. Only the is_patent column sees these; the fallback undercounts by
    # about 3%. See the module comment in assaywatch/metadata.py.
    assert not looks_like_patent("Modified Microbial Nucleic Acid")
    assert not looks_like_patent("RESEQUENCING PATHOGEN MICROARRAY")
    # Engineered but deposited normally: not a patent record, and not this
    # function's business to guess. See docs/2026-10-19-orthopox-ati-vaccinia.md.
    assert not looks_like_patent(ENGINEERED)
    assert not looks_like_patent("")


def _archive(tmp_path, header, rows):
    d = tmp_path / "10245" / "all"
    d.mkdir(parents=True)
    with gzip.open(d / "2026-01-01.meta.tsv.gz", "wt") as fh:
        fh.write("\t".join(header) + "\n")
        for r in rows:
            fh.write("\t".join(r) + "\n")
    return tmp_path


def test_the_is_patent_column_wins_over_the_title(tmp_path):
    """A fresh retrieval records GenBank's own flag; the title is not consulted."""
    root = _archive(
        tmp_path,
        ["uid", "accession", "created", "updated", "length", "title", "taxid", "is_patent"],
        [
            ["1", "PC415960.1", "2025-01-29", "2025-01-29", "26077", PATENT, "10245", "1"],
            ["2", "PZ835181.1", "2026-08-19", "2026-08-19", "190000", NATURAL, "10245", ""],
            # A patent-shaped title that GenBank did not flag: the column decides.
            ["3", "XX000001.1", "2026-01-01", "2026-01-01", "1000", KOREAN, "10245", ""],
        ],
    )
    got = read_patent_accessions(root, {"PC415960", "PZ835181", "XX000001"})
    assert got == {"PC415960"}


def test_an_archive_without_the_column_falls_back_to_the_title(tmp_path):
    root = _archive(
        tmp_path,
        ["uid", "accession", "created", "updated", "length", "title", "taxid"],
        [
            ["1", "PC415960.1", "2025-01-29", "2025-01-29", "26077", PATENT, "10245"],
            ["2", "PZ835181.1", "2026-08-19", "2026-08-19", "190000", NATURAL, "10245"],
            ["3", "PV358350.1", "2025-04-01", "2025-04-01", "26000", ENGINEERED, "10245"],
        ],
    )
    assert read_patent_accessions(root, {"PC415960", "PZ835181", "PV358350"}) == {"PC415960"}


def test_only_the_accessions_asked_for_come_back(tmp_path):
    root = _archive(
        tmp_path,
        ["uid", "accession", "created", "updated", "length", "title", "taxid", "is_patent"],
        [["1", "PC415960.1", "2025-01-29", "2025-01-29", "26077", PATENT, "10245", "1"]],
    )
    assert read_patent_accessions(root, set()) == set()
    assert read_patent_accessions(root, {"PZ835181"}) == set()
