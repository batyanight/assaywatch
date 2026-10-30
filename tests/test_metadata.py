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
    # function's business to guess. See docs/journal/2026-10-19-orthopox-ati-vaccinia.md.
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


# --- collection years for asm records --------------------------------------------------


def _asm_meta(path, rows, with_column):
    header = "uid\taccession\tcreated\tupdated\tlength\ttitle" + ("\tcollected" if with_column else "") + "\n"
    with gzip.open(path, "wt") as fh:
        fh.write(header)
        for acc, created, title, collected in rows:
            line = f"{acc}\t{acc}\t{created}\t{created}\t500\t{title}"
            fh.write(line + (f"\t{collected}" if with_column else "") + "\n")


def test_collection_years_read_the_column_and_fall_back_to_the_title(tmp_path):
    """Archives written before 2026-10-30 carry the collection date only inside the title
    ("...; collected 2010-05-13"); newer ones carry a `collected` column. Both are read,
    the column winning, and only a four-digit year is kept: BioSample dates arrive as full
    dates, year-month, bare years, ranges and "missing", and the lens works in years."""
    from assaywatch.metadata import collection_year, read_collection_years

    old = tmp_path / "1" / "asm"
    old.mkdir(parents=True)
    _asm_meta(
        old / "2026-10-01.meta.tsv.gz",
        [
            (
                "GCA_000000001.1",
                "2020-01-01",
                "Testus coli S1; Complete Genome; 2 loci; collected 2010-05-13",
                "",
            ),
            ("GCA_000000002.1", "2020-01-01", "Testus coli S2; Complete Genome; 2 loci; collected 2011", ""),
            (
                "GCA_000000003.1",
                "2020-01-01",
                "Testus coli S3; Complete Genome; 2 loci; collected missing",
                "",
            ),
            (
                "GCA_000000004.1",
                "2020-01-01",
                "Testus coli S4; Complete Genome; 2 loci; collected 2010/2011",
                "",
            ),
        ],
        with_column=False,
    )
    new = tmp_path / "2" / "asm"
    new.mkdir(parents=True)
    _asm_meta(
        new / "2026-11-01.meta.tsv.gz",
        [
            (
                "GCA_000000005.1",
                "2021-01-01",
                "Testus coli S5; Complete Genome; 2 loci; collected 2012-03",
                "2012-03",
            )
        ],
        with_column=True,
    )
    want = {f"GCA_00000000{i}" for i in range(1, 6)}
    got = read_collection_years(tmp_path, want)
    assert got == {"GCA_000000001": 2010, "GCA_000000002": 2011, "GCA_000000005": 2012}
    # The pure parser, so the rule is stated once and testable without files.
    assert collection_year("2010-05-13") == 2010 and collection_year("2011") == 2011
    assert collection_year("missing") is None and collection_year("not collected") is None
    assert (
        collection_year("2010/2011") is None
    )  # a range is undatable to a year, by decision (Q2, 2026-10-30)
    assert collection_year("") is None and collection_year("13-May-2010") == 2010
    # The month-year form, which the 2026-10-30 nuccore backfill showed is 156 of the
    # first 3,663 dates GenBank served -- the one spelling the first regex missed.
    assert collection_year("Jan-2011") == 2011 and collection_year("Jun-2011") == 2011
    # Still a range, still undatable, even spelled with days and months.
    assert collection_year("01-Apr-2010/30-Jun-2010") is None


def test_the_sidecar_answers_for_nuccore_and_the_archives_fill_the_gaps(tmp_path):
    """`scripts/backfill_collection_dates.py` writes the dates nuccore metadata lacks.

    The archives carry a collection date only for `asm` records, which is 13 assays of 214.
    The sidecar covers every record the run screened, so it is read first and the archives
    answer only where it is silent. A row that settled with no date, or that NCBI would not
    serve, is an answer and must not be mistaken for a gap the archives might fill.
    """
    import gzip

    from assaywatch.metadata import read_collection_years

    sidecar = tmp_path / "collection-dates.tsv"
    sidecar.write_text(
        "accession\tcollection_date\tstatus\n"
        "AB000001.1\t16-Mar-2009\tok\n"
        "AB000002.2\tJan-2011\tok\n"
        "AB000003.1\t\tnodate\n"
        "AB000004.1\t\tmissing\n"
        "GCA_000000009\t1999\tok\n"
    )
    asm = tmp_path / "7777" / "all" / "asm"
    asm.mkdir(parents=True)
    with gzip.open(asm / "a.meta.tsv.gz", "wt", newline="") as fh:
        fh.write("accession\ttitle\tcollected\n")
        fh.write("GCA_000000008.1\tsomething\t2012\n")
        # The sidecar wins where both have an answer.
        fh.write("GCA_000000009.1\tsomething\t2020\n")

    want = {"AB000001.1", "AB000002.2", "AB000003.1", "AB000004.1", "GCA_000000008", "GCA_000000009"}
    got = read_collection_years(tmp_path, want, sidecar=sidecar)
    assert got == {
        "AB000001.1": 2009,
        "AB000002.2": 2011,
        "GCA_000000008": 2012,
        "GCA_000000009": 1999,
    }
    # Keys come back spelled the way the caller asked, version or no version, so a caller
    # holding nuccore record ids can look them up without stripping anything.
    assert read_collection_years(tmp_path, {"AB000001.1"}, sidecar=sidecar) == {"AB000001.1": 2009}
    assert read_collection_years(tmp_path, {"AB000001"}, sidecar=sidecar) == {"AB000001": 2009}
    # No sidecar: unchanged behaviour, archives only.
    assert read_collection_years(tmp_path, want) == {
        "GCA_000000008": 2012,
        "GCA_000000009": 2020,
    }
    # A sidecar that does not exist is not an error; the archives still answer.
    assert read_collection_years(tmp_path, want, sidecar=tmp_path / "nope.tsv") == {
        "GCA_000000008": 2012,
        "GCA_000000009": 2020,
    }
