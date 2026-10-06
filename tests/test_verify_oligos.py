"""Tests for the paper-vs-registry oligo check.

The registry's sequences must match the literature, not the lab spreadsheet they
were transcribed from, so this script is the thing that makes that checkable.
Its one real difficulty is telling a printed sequence apart from English text:
every letter of "attach" is an IUPAC code.
"""

import csv
import importlib.util
import re
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("vo", ROOT / "scripts" / "verify_oligos_against_paper.py")
vo = importlib.util.module_from_spec(_spec)
sys.modules["vo"] = vo
_spec.loader.exec_module(vo)


def test_finds_sequences_printed_in_codon_groups():
    """Grizzle 2003 and Briese 2007 both group their sequences; a plain
    run-of-letters pattern finds nothing in exactly the papers that matter."""
    grizzle = "The forward primer (LMBV288F) sequence was 5'-GCG GCC AAC CAG TTT AAC GCA A-3'"
    assert "GCGGCCAACCAGTTTAACGCAA" in vo.printed_oligos(grizzle)
    # Briese prints degenerate codes in lower case inside an upper-case sequence.
    briese = "BUNS-5-U-6 5'-CGGCGCC AGT AGT GTA CTC CAC 947"
    assert "CGGCGCCAGTAGTGTACTCCAC" in vo.printed_oligos(briese)
    mixed = "M940C-R 5'-CTr GCw GCT CTw AGr CTT TTr TAm CC 936"
    assert "CTRGCWGCTCTWAGRCTTTTRTAMCC" in vo.printed_oligos(mixed)


def test_finds_heavily_degenerate_consensus_primers():
    """Regression for the 0.75-with-inosine composition rule, which dropped them.

    Atkins 2009 prints both of these. Under the old rule they scored 0.73 and
    0.71 against a 0.75 threshold, so neither was extracted, and the registry's
    exact copies of them came back as `in-text` - the verdict that means "this
    string is somewhere in the paper", when in fact the paper lists them as its
    primers. A pan-viral consensus primer is degenerate by design, and this
    registry is mostly pan-viral screening, so these cannot be edge cases.
    """
    atkins = (
        "forward primer Astr4380F (5'-GAYTGGRCNCGNTWYGATGGNACIAT-3') and reverse "
        "primer Astr4722R (5'-ARNCKRTCATCNCCATA-3')"
    )
    printed = vo.printed_oligos(atkins)
    assert "GAYTGGRCNCGNTWYGATGGNACIAT" in printed, printed
    assert "ARNCKRTCATCNCCATA" in printed, printed
    # And the registry's stored form, with N where the paper prints inosine,
    # must now read as an exact match rather than as in-text.
    verdict, _ = vo.check("GAYTGGRCNCGNTWYGATGGNACNAT", atkins, printed, 4)
    assert verdict == "exact", verdict


def test_inosine_is_not_counted_as_an_unambiguous_base():
    """The reason the threshold can be 0.65: `I` is common in English, rare in
    oligos, so counting it scores all-caps prose nearly as high as a primer.

    `INDINGS IN BATS IN THAI` is 0.53 unambiguous with inosine counted and 0.26
    without, which is what puts clear air between it and a real primer.
    """
    assert vo.printed_oligos("FINDINGS IN BATS IN THAILAND") == []
    # An inosine-carrying primer still survives, because inosine sits at a few
    # wobble positions rather than throughout.
    assert "GGNAAYCCMTCWGGICA" in vo.printed_oligos("primer 5'-GGNAAYCCMTCWGGICA-3'")


def test_rejects_all_caps_headings():
    """Regression for the PREDICT final report, where the case test alone
    returned 32 'oligos', all of them headings with the spaces lost.

    These survive a case test because English words are built from IUPAC
    letters; they fail the base-composition test, being about 23% unambiguous
    bases against a real oligo's 90-100%.
    """
    for heading in (
        "FINDINGS IN BATS IN THAILAND",
        "HIGH RISK INTERFACES WITH WILDLIFE",
        "VIRUS DETECTION IN ANIMALS AND HUMANS",
    ):
        assert vo.printed_oligos(heading) == [], heading


def test_lower_case_prose_is_not_an_oligo():
    assert vo.printed_oligos("we attach a cat and a tag to that sample") == []


def test_edit_distance_abandons_past_the_cap():
    """The near-match search runs every stored oligo against every printed one,
    so the distance only has to be exact while it is small."""
    assert vo.edit_distance("ACGTACGTACGT", "ACGTACGTACGT", 4) == 0
    assert vo.edit_distance("ACGTACGTACGT", "ACGTACGTACGA", 4) == 1
    assert vo.edit_distance("ACGTACGTACGT", "ACGTACGTACG", 4) == 1  # a dropped base
    assert vo.edit_distance("ACGT", "TTTTTTTTTTTT", 4) > 4


def test_an_extra_base_reads_as_a_one_edit_near_match():
    """The Sarcocystis failure mode: one extra C, which then matched almost
    nothing. A verdict of near:1 carries its own correction."""
    paper = "the primer P-ITSF 5'-GGATCACTCGGTTCGAGGTG-3' was used"
    stored = "GGATCACTCCGGTTCGAGGTG"  # one extra C
    verdict, note = vo.check(stored, paper, vo.printed_oligos(paper), 4)
    assert verdict == "near:1", (verdict, note)
    assert "GGATCACTCGGTTCGAGGTG" in note


def test_inosine_matches_the_registry_n():
    """Papers print inosine as I; the registry stores it as N in `seq`.

    The first full run flagged both PREDICT bocavirus primers as near:1 purely
    because of this, so both sides of the comparison must use one alphabet.
    """
    paper = "PANBOV-F1 5'-TAATGCAYCARGAYTGGGTIGANCC-3'"
    stored = "TAATGCAYCARGAYTGGGTNGANCC"  # the registry's N where the paper prints I
    verdict, _ = vo.check(stored, paper, vo.printed_oligos(paper), 4)
    assert verdict == "exact", verdict


def test_a_match_inside_the_printed_gene_is_not_a_primer_match():
    """Papers print their target sequence, so "appears in the paper" is weaker
    than "appears in the primer table".

    Ibrahim 1992 prints the ystA gene, and the registry's stored forward primer
    sits inside it four bases offset from the primer the table actually lists.
    A plain substring search called that a perfect match.
    """
    paper = (
        "TABLE 3 yst-Pr2a 5'-AATGCTGTCTTCATTTGGAGC-3' "
        "FIG 2 ATGAAAAAGATAGTTTTTGTTCTTGTGTTAATGCTGTCTTCATTTGGAGCATTCGGCCAAGAAACAGTTTCAGGG"
    )
    printed = vo.printed_oligos(paper)
    listed, _ = vo.check("AATGCTGTCTTCATTTGGAGC", paper, printed, 4)
    assert listed == "exact", listed
    shifted, note = vo.check("CTGTCTTCATTTGGAGCATTC", paper, printed, 4)
    assert shifted == "in-text", (shifted, note)


def test_file_text_reads_xml_by_dropping_tags():
    """A publisher JATS deposit must read the same as a fetched fullTextXML."""
    import tempfile

    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "a.xml"
        p.write_text("<article><p>primer 5'-<b>GCGGCCAACCAGTTTAACGCAA</b>-3'</p></article>")
        assert "GCGGCCAACCAGTTTAACGCAA" in vo.printed_oligos(vo.file_text(p))


def test_a_table_less_text_file_does_not_override_a_working_pdf(tmp_path):
    """Regression for the first version of the multi-format index.

    It preferred publisher text over a PDF on the reasoning that structured text
    beats a table pypdf rebuilt from glyph positions. True of a full publisher
    deposit, false of PMC full text served without its `table-wrap` content - so
    merging PMC texts into a papers/ folder of good PDFs would have silently
    replaced readable primer tables with files holding no sequences at all.
    Whichever file yields more oligos wins now.
    """
    doi = "10.1234_test.1"
    rich = "primer F 5'-GCGGCCAACCAGTTTAACGCAA-3' primer R 5'-ATTGCGCTGGAACCTTGTCAA-3'"
    (tmp_path / f"{doi}.txt").write_text("We screened by PCR as described. See Table 1.")
    (tmp_path / f"{doi}.xml").write_text(f"<article><p>{rich}</p></article>")
    by_doi, _ = vo.index_papers(tmp_path)
    text, path = by_doi["10.1234/test.1"]
    assert path.suffix == ".xml", path
    assert len(vo.printed_oligos(text)) == 2


def test_a_doi_named_file_beats_a_doi_merely_cited_elsewhere(tmp_path):
    """Standing comes before yield, or an image-table paper loses its own DOI.

    A filename is a statement that this IS the paper. A DOI in running text is
    often just a reference. So the named file wins even printing nothing, which
    is what keeps "the PDF is here and its table is an image" distinct from
    "the PDF is missing".
    """
    (tmp_path / "10.5555_mine.9.txt").write_text("Our assay is described in Table 2.")
    (tmp_path / "someone-else.txt").write_text(
        "We cite 10.5555/mine.9 and print 5'-GCGGCCAACCAGTTTAACGCAA-3' "
        "and 5'-ATTGCGCTGGAACCTTGTCAA-3' of our own."
    )
    by_doi, _ = vo.index_papers(tmp_path)
    _, path = by_doi["10.5555/mine.9"]
    assert path.name == "10.5555_mine.9.txt", path


def test_reads_the_n_or_inosine_notation_as_n():
    """Prepens 2007 and the other Ehlers-lab consensus-primer papers spell an
    ambiguous position out as `(N/I)` - "N or inosine" - inside the sequence.

    The brackets and slash end the run, so without normalisation `printed_oligos`
    returns a fragment and every stored oligo past the first bracket reports
    `absent`. That produced 4 false verdicts on one paper, all 4 of them exact
    matches to the registry once the notation is read.
    """
    paper = "2744s 1 TTCAAGGAACTCAGYAARAT(N/I)AAYCC 250"
    printed = vo.printed_oligos(vo.normalise_notation(paper))
    assert "TTCAAGGAACTCAGYAARATNAAYCC" in printed, printed
    verdict, _ = vo.check("TTCAAGGAACTCAGYAARATNAAYCC", vo.normalise_notation(paper), printed, 4)
    assert verdict == "exact", verdict


def test_the_notation_survives_both_cases_and_bracket_styles():
    """One table in one paper used `(N/I)` and `[n/i]`, so both must work."""
    for token in ("(N/I)", "[n/i]", "(n/i)", "[N/I]", "(I/N)"):
        got = vo.normalise_notation(f"CGTTGTCCTC{token}CCNARYTGNCC")
        assert got == "CGTTGTCCTCNCCNARYTGNCC", (token, got)


def test_the_notation_is_not_silently_collapsed_to_two_bases():
    """The dangerous half: `check`'s substring search strips every non-IUPAC
    character, and N and I are BOTH IUPAC, so an unnormalised `(N/I)` becomes
    the two bases `NI` and shifts the rest of the sequence by one. That is a
    wrong answer rather than a missing one, which is why the normalisation has
    to happen before the text reaches either search.
    """
    raw = "primer 5'-CGTTGTCCTC(N/I)CCNARYTGNCC-3'"
    assert "NI" in vo.NOISE.sub("", raw.upper())
    assert "NI" not in vo.NOISE.sub("", vo.normalise_notation(raw).upper())


# ---------------------------------------------------------------------------
# Tests added after an adversarial review of the verifier changes. Each pins a
# defect that was reproduced, and each was checked against the unfixed code.
# ---------------------------------------------------------------------------

# Registry oligos that the ORIGINAL composition rule extracted and a first
# replacement rule lost. They are inosine-RICH: 0.57-0.64 unambiguous bases
# without inosine, 0.76-0.85 with it.
INOSINE_RICH = {
    "Alpha1R": "KYTCYTCIGTRTGYTTIGTICCIGG",
    "Alpha2R": "GCRAAIARIGCIGCIGCYTYIGGICC",
    "222/RVS": "CICCIGGIGGIAYRWACAT",
    "NPhlebo1NEG": "AARTTRCTIGWIGCYTTIARIGTIGC",
    "NPhlebo2POS": "WTICCIAAICCIYMSAARATG",
}


def test_inosine_rich_primers_are_still_extracted():
    """Dropping inosine from the composition numerator rescued degenerate primers
    and regressed these five, which the original rule found. Either rule passing
    makes the result a superset of both."""
    for name, seq in INOSINE_RICH.items():
        assert seq in vo.printed_oligos(f"primer {name} 5'-{seq}-3' was used"), name


def test_the_composition_rule_is_a_superset_of_the_original_over_the_registry():
    """The calibration, kept: every registry oligo the original rule extracted must
    still be extracted. Measured against all 357 distinct oligos, not the papers
    in hand, because 21 papers did not contain the primers that regressed."""
    import subprocess

    old_src = subprocess.run(
        ["git", "show", "50430bb:scripts/verify_oligos_against_paper.py"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if old_src.returncode != 0:
        pytest.skip("the original rule is not in this checkout's history")
    ns: dict = {"__name__": "vo_original", "__file__": str(ROOT / "scripts" / "x.py")}
    exec(compile(old_src.stdout, "vo_original", "exec"), ns)  # noqa: S102 - our own repo's history
    seqs = set()
    for f in sorted((ROOT / "registry").glob("*.yaml")):
        o = yaml.safe_load(f.read_text())["oligos"]
        for k in ("forward", "reverse", "probe"):
            if o.get(k):
                seqs.add((o[k].get("seq_as_written") or o[k]["seq"]).upper())
        for a in o.get("alternates") or []:
            seqs.add((a.get("seq_as_written") or a["seq"]).upper())
    seqs = {s for s in seqs if 14 <= len(s) <= 60}
    assert len(seqs) > 300  # the registry really was walked
    lost = [
        s
        for s in sorted(seqs)
        if s in ns["printed_oligos"](f"primer 5'-{s}-3' was used")
        and s not in vo.printed_oligos(f"primer 5'-{s}-3' was used")
    ]
    assert lost == [], lost


@pytest.mark.parametrize(
    "heading",
    [
        "FINDINGS IN BATS IN THAILAND",
        "HIGH RISK INTERFACES WITH WILDLIFE",
        "INITIATION IN TITLE AND IN ITALY",
        "TRANSMISSION AND SPILLOVER RISK IN BATS",
    ],
)
def test_the_wider_rule_still_rejects_all_caps_prose(heading):
    assert vo.printed_oligos(heading) == [], heading


# --- the verdict: judge() is what main() calls ------------------------------

SEQ = "GCGGCCAACCAGTTTAACGCAA"


def test_a_text_that_printed_too_little_cannot_say_absent():
    """The false-finding mechanism `no-oligos` exists to stop. Reaches the verdict
    code itself: the test it replaces only asserted that prose yields no oligos
    and never touched the verdict, so deleting the whole branch passed it."""
    one_run = (
        "The reverse primer was 5'-ATTGCGCTGGAACCTTGTCAAGG-3'. Forward primers are presented in Table 1."
    )
    printed = vo.printed_oligos(one_run)
    assert len(printed) == 1
    verdict, note = vo.judge(SEQ, one_run, printed, 4)
    assert verdict == "no-oligos", (verdict, note)
    assert "1 oligo-like run" in note


def test_a_text_that_printed_a_primer_pair_can_still_say_absent():
    """The other half: this is the finding that catches a misattributed primer,
    and it must survive the floor."""
    text = "Primers 5'-ATTGCGCTGGAACCTTGTCAAGG-3' and 5'-CCTTGGTTAAGGCCTTGGAACCTT-3' were used."
    printed = vo.printed_oligos(text)
    assert len(printed) >= vo.MIN_PRINTED_FOR_ABSENT
    verdict, note = vo.judge(SEQ, text, printed, 4)
    assert verdict == "absent" and f"{len(printed)} oligo-like run" in note


def test_a_stored_sequence_in_the_running_text_is_in_text_not_no_oligos():
    """The text printed no oligo run (the sequence is buried in a gene longer than
    60 bases, so it is not a candidate) but the stored sequence IS in it. Hiding
    that behind `no-oligos` threw away a weaker but real confirmation."""
    gene = "ATGAAAAAGATAGTTTTTGTTCTTGTG" + SEQ + "CATTCGGCCAAGAAACAGTTTCAGGGTTTAAACCC"
    printed = vo.printed_oligos(gene)
    assert printed == []
    verdict, _ = vo.judge(SEQ, gene, printed, 4)
    assert verdict == "in-text"


def test_the_exact_verdict_is_unaffected_by_the_floor():
    text = f"forward primer 5'-{SEQ}-3' and reverse 5'-ATTGCGCTGGAACCTTGTCAAGG-3'"
    assert vo.judge(SEQ, text, vo.printed_oligos(text), 4)[0] == "exact"


# --- the paper's oligo is longer than the stored one ------------------------


def test_a_longer_printed_oligo_is_reported_in_full_not_as_a_truncated_window():
    """Quan 2010 prints a 33-mer; the stored 30-mer lacks three bases. The window
    alone reported the first 30 bases as 'the paper's own sequence', and applying
    that as the fix would store a sequence matching neither the paper nor anything
    else."""
    printed_33 = "GGTCATKATAGCRTCAVMASWWGCNACNACATG"
    stored_30 = "GGTCATKATAGCRTCAVMASWWGCNACATG"
    text = f"consensus primer 5'-{printed_33}-3' for the first PCR; other primer 5'-CGTTGGNACWAAYBTVCCWYTNCARBTRGG-3'"
    verdict, note = vo.judge(stored_30, text, vo.printed_oligos(text), 4)
    assert verdict.startswith("near:"), (verdict, note)
    assert printed_33 in note, note
    assert "33 nt" in note and "longer than the stored 30" in note


# --- the summary ------------------------------------------------------------


def _one_entry_registry(tmp_path):
    reg = tmp_path / "registry"
    reg.mkdir()
    src = ROOT / "registry" / "PD_WNS_ITS1_Shuey_2014.yaml"
    (reg / src.name).write_text(src.read_text())
    return reg, yaml.safe_load(src.read_text())


def test_near_matches_beyond_four_edits_count_in_the_headline(tmp_path, capsys):
    """With --cap above 4, near:N rows for larger N belonged to no bucket and no
    denominator, so the percentage was inflated: this entry read '2 of 2 (100%)'
    for three oligos, one of them six edits from the paper's."""
    reg, d = _one_entry_registry(tmp_path)
    o = d["oligos"]
    papers = tmp_path / "papers"
    papers.mkdir()
    probe = o["probe"]["seq"]
    swapped = "".join(
        {"A": "T", "T": "A", "C": "G", "G": "C"}.get(c, c) if i % 2 == 0 else c for i, c in enumerate(probe)
    )
    assert vo.edit_distance(probe, swapped, 12) >= 5  # beyond the default cap of 4
    (papers / "10.1128_aem.02897-13.txt").write_text(
        f"Methods. Forward {o['forward']['seq']} and reverse {o['reverse']['seq']} with probe {swapped} were used."
    )
    rc = vo.main(
        ["--registry", str(reg), "--pdf-dir", str(papers), "--cap", "12", "--tsv", str(tmp_path / "v.tsv")]
    )
    out = capsys.readouterr().out
    assert rc == 0
    assert re.search(r"near:\d+", out), out
    assert "2 of 3 checkable oligos agree" in out, out
    assert "2 of 2 checkable" not in out


def test_checked_against_names_the_real_file_type(tmp_path):
    """It said `pdf:` for .txt and .xml files, which misdescribes where the
    evidence came from at exactly the point a curator is judging it."""
    reg, d = _one_entry_registry(tmp_path)
    papers = tmp_path / "papers"
    papers.mkdir()
    (papers / "10.1128_aem.02897-13.txt").write_text(
        f"forward {d['oligos']['forward']['seq']} reverse {d['oligos']['reverse']['seq']}"
    )
    out = tmp_path / "v.tsv"
    vo.main(["--registry", str(reg), "--pdf-dir", str(papers), "--tsv", str(out)])
    rows = list(csv.DictReader(out.open(), delimiter="\t"))
    assert {r["checked_against"] for r in rows} == {"txt:10.1128_aem.02897-13.txt"}


# --- which file represents a DOI --------------------------------------------

RICH = "primer F 5'-GCGGCCAACCAGTTTAACGCAA-3' primer R 5'-ATTGCGCTGGAACCTTGTCAAG-3'"
POOR = "We screened by PCR as described. See Table 1."


def test_the_richer_of_two_named_files_wins_whichever_comes_first(tmp_path):
    """Both orders. The earlier tests all put the stronger file first in iteration
    order, so replacing the ranking with 'first one wins' passed them."""
    doi = "10.1234_test.1"
    # xml sorts before txt: poor-first, then rich must DISPLACE it.
    (tmp_path / f"{doi}.xml").write_text(f"<article>{POOR}</article>")
    (tmp_path / f"{doi}.txt").write_text(RICH)
    _, path = vo.index_papers(tmp_path)[0]["10.1234/test.1"]
    assert path.suffix == ".txt", "the richer later file must displace the poorer earlier one"

    # And rich-first, then poor must NOT displace it.
    for f in tmp_path.glob("*"):
        f.unlink()
    (tmp_path / f"{doi}.xml").write_text(f"<article>{RICH}</article>")
    (tmp_path / f"{doi}.txt").write_text(POOR)
    _, path = vo.index_papers(tmp_path)[0]["10.1234/test.1"]
    assert path.suffix == ".xml", "a poorer later file must not displace a richer earlier one"


def test_a_file_that_merely_cites_a_doi_never_displaces_the_paper_that_prints_it(tmp_path):
    """Two unnamed files in a general Downloads folder. A review that cites the
    DOI in its header and reprints more primers must not take that DOI from the
    paper that actually designed them, or an entry is verified against the wrong
    paper and can read `exact` against it."""
    (tmp_path / "a_smith2010.txt").write_text("doi:10.9999/smith.2010 " + RICH)
    (tmp_path / "b_review.txt").write_text(
        "Related to doi:10.9999/smith.2010. "
        + RICH
        + " primer 5'-CCTTGGTTAAGGCCTTGGAACCTT-3' primer 5'-GGAACCTTGGTTAAGGCCTTGGAA-3'"
    )
    by_doi, _ = vo.index_papers(tmp_path)
    assert by_doi["10.9999/smith.2010"][1].name == "a_smith2010.txt"
    assert len(vo.printed_oligos(vo.file_text(tmp_path / "b_review.txt"))) > len(
        vo.printed_oligos(vo.file_text(tmp_path / "a_smith2010.txt"))
    )  # the citer really does print more, so yield alone would have picked it


def test_a_named_file_beats_an_unnamed_one_even_when_it_yields_less(tmp_path):
    """The documented asymmetry, pinned so it cannot change by accident: a DOI in
    running text is never trusted over a filename."""
    (tmp_path / "10.5555_mine.9.txt").write_text(POOR)
    (tmp_path / "downloaded.txt").write_text("doi:10.5555/mine.9 " + RICH)
    assert vo.index_papers(tmp_path)[0]["10.5555/mine.9"][1].name == "10.5555_mine.9.txt"


def test_the_index_says_how_many_papers_printed_too_little(tmp_path, capsys):
    papers = tmp_path / "papers"
    papers.mkdir()
    (papers / "10.1234_a.1.txt").write_text(POOR)
    (papers / "10.1234_b.2.txt").write_text(RICH)
    reg, _ = _one_entry_registry(tmp_path)
    vo.main(["--registry", str(reg), "--pdf-dir", str(papers)])
    out = capsys.readouterr().out
    assert "1 print fewer than 2 oligos" in out, out


# --- the (N/I) notation reaches every reader --------------------------------


def test_the_notation_is_normalised_by_every_way_a_paper_is_read(tmp_path, monkeypatch):
    """normalise_notation was only ever tested by calling it directly. Deleting it
    from any one reader passed the suite while that reader went on producing
    fragments. Each of the four read paths is exercised here."""
    raw = "primer 2744s 5'-TTCAAGGAACTCAGYAARAT(N/I)AAYCC-3' and 2745as 5'-CGTTGTCCTC[n/i]CCNARYTGNCC-3'"
    want_a, want_b = "TTCAAGGAACTCAGYAARATNAAYCC", "CGTTGTCCTCNCCNARYTGNCC"

    txt = tmp_path / "a.txt"
    txt.write_text(raw)
    xml = tmp_path / "b.xml"
    xml.write_text(f"<article><p>{raw}</p></article>")
    for path in (txt, xml):
        got = vo.printed_oligos(vo.file_text(path))
        assert want_a in got and want_b in got, (path.suffix, got)

    monkeypatch.setattr(vo, "pdf_text", lambda p: raw)
    got = vo.printed_oligos(vo.file_text(tmp_path / "c.pdf"))
    assert want_a in got and want_b in got, ("pdf", got)

    monkeypatch.setattr(vo, "get", lambda url, timeout=60: f"<article>{raw}</article>")
    got = vo.printed_oligos(vo.paper_text("PMC1"))
    assert want_a in got and want_b in got, ("pmc", got)
