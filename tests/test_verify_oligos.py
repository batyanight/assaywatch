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


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    """No test here may reach NCBI or Europe PMC.

    `main` looks a paper up online when none is held locally, through `vo.get`, so every
    test that runs it for an entry with no matching local paper would otherwise make real
    requests: slow, flaky, and an unannounced load on NCBI from CI.
    """
    monkeypatch.setattr(vo, "get", lambda url, timeout=60: None)


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


def _assay(doi, reference, year):
    from types import SimpleNamespace

    cite = SimpleNamespace(doi=doi, reference=reference, as_written=None, design_year=year)
    return SimpleNamespace(citation=cite)


def test_a_paper_that_only_cites_the_author_is_not_their_paper(tmp_path):
    """Regression: the surname-and-year fallback matched any paper naming both.

    An elephant-herpesvirus paper whose introduction cites "Reid ... 1999" was
    taken for Reid et al. 1999, so the calicivirus primers were checked against
    it and reported `absent`. The fallback is for papers that print no DOI of
    their own; one that prints a DOI is already indexed under it.
    """
    intro = "Caliciviruses were first typed by Reid et al. in 1999 and later by others. "
    (tmp_path / "10.9999_other.paper.2010.txt").write_text(
        intro + "We print 5'-GCGGCCAACCAGTTTAACGCAA-3' and 5'-ATTGCGCTGGAACCTTGTCAA-3'."
    )
    by_doi, everything = vo.index_papers(tmp_path)
    reid = _assay("10.1016/s0166-0934(99)00088-9", "Reid, S. M. et al. 1999", 1999)
    assert vo.local_paper(reid, by_doi, everything) is None


def test_the_fallback_still_finds_an_older_paper_that_prints_no_doi(tmp_path):
    """The fallback's real job: a 1992 paper has no DOI on it, only an author and a year."""
    (tmp_path / "scan-1992.txt").write_text(
        "Reid SM and colleagues, 1992. Primers 5'-GCGGCCAACCAGTTTAACGCAA-3' and "
        "5'-ATTGCGCTGGAACCTTGTCAA-3' are described here."
    )
    by_doi, everything = vo.index_papers(tmp_path)
    reid = _assay("10.1234/not-local", "Reid, S. M. et al. 1992", 1992)
    hit = vo.local_paper(reid, by_doi, everything)
    assert hit is not None and hit[1].name == "scan-1992.txt"


def test_a_short_probe_is_judged_apart_from_a_primer():
    """A 13 nt probe printed alone in a primer table reads `exact`; as a primer it cannot.

    The harvest floor is 14 so that short English runs stay out, which meant a
    published 13 nt MGB probe was never extracted and fell to `in-text`. Probes get
    their own floor (schema.PROBE_MIN); a primer is never harvested that short.
    """
    probe = "CGAGTCGAACAAA"  # 13 nt
    text = (
        "Table 1. Primer F 5'-GCGGCCAACCAGTTTAACGCAA-3' primer R 5'-ATTGCGCTGGAACCTTGTCAA-3' "
        f"probe P 5'-{probe}-3'."
    )
    printed = vo.printed_oligos(text)
    assert probe not in printed  # under the primer floor, so not harvested by default
    as_probe = vo.printed_runs_for(True, probe, text, printed)
    assert vo.check(probe, text, as_probe, 4)[0] == "exact"
    as_primer = vo.printed_runs_for(False, probe, text, printed)
    assert as_primer is printed
    assert vo.check(probe, text, as_primer, 4)[0] != "exact"


def test_the_probe_floor_does_not_let_prose_in():
    """Lowering the harvest floor for probes must not turn English into oligos."""
    prose = "We attach the sample to the washbasin and check that it was marked, then dash back."
    assert vo.printed_oligos(prose, min_len=12) == []


def test_a_probe_of_normal_length_uses_the_ordinary_runs():
    seq = "CGAGTCGAACAAATTT"  # 16 nt: not short, so the primer harvest serves
    text = f"probe 5'-{seq}-3' and primers 5'-GCGGCCAACCAGTTTAACGCAA-3' 5'-ATTGCGCTGGAACCTTGTCAA-3'"
    printed = vo.printed_oligos(text)
    assert vo.printed_runs_for(True, seq, text, printed) is printed


def test_probe_slot_detection():
    from types import SimpleNamespace

    assert vo.is_probe_slot("probe", SimpleNamespace(orientation=None))
    assert vo.is_probe_slot("alt0", SimpleNamespace(orientation="probe"))
    assert not vo.is_probe_slot("alt0", SimpleNamespace(orientation="forward"))
    assert not vo.is_probe_slot("forward", SimpleNamespace(orientation=None))


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


def test_any_base_or_inosine_reads_as_n():
    """Deckers 2009 prints `(b/i)` and `(r/i)` beside `(n/i)`. Read only as
    `(N/I)`, its 4125s came out `absent` and 4125as `near:3`, both exact once
    read - the same false verdict the `(N/I)` fix removed, one letter over.
    """
    paper = "4125s 2 GCGGACTCGGTGAT(b/i)TC(n/i)TGGGA 550 4125as GCTGACGGGTTGATCTTGCT(r/i)AG"
    text = vo.normalise_notation(paper)
    printed = vo.printed_oligos(text)
    for stored in ("GCGGACTCGGTGATNTCNTGGGA", "GCTGACGGGTTGATCTTGCTNAG"):
        verdict, _ = vo.check(stored, text, printed, 4)
        assert verdict == "exact", (stored, verdict, printed)


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


def original_printed_oligos(text: str, min_len: int = 14, max_len: int = 60) -> list[str]:
    """The composition rule as it stood in 50430bb, frozen here.

    It used to be read out of git history, which a shallow clone (CI's default) does not
    have, so the regression guard below was skipped exactly where it should have run.
    """
    out: set[str] = set()
    for m in vo.GROUPED_RE.finditer(text):
        letters = [c for c in m.group(0) if c.isalpha()]
        if not (min_len <= len(letters) <= max_len):
            continue
        if sum(c.isupper() for c in letters) / len(letters) < 0.6:
            continue
        if sum(c.upper() in "ACGTUI" for c in letters) / len(letters) < 0.75:
            continue
        out.add("".join(letters).upper())
    return sorted(out)


def test_the_composition_rule_is_a_superset_of_the_original_over_the_registry():
    """The calibration, kept: every registry oligo the original rule extracted must
    still be extracted. Measured against all 357 distinct oligos, not the papers
    in hand, because 21 papers did not contain the primers that regressed."""
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
    sentence = "primer 5'-{}-3' was used"
    found_by_original = [s for s in sorted(seqs) if s in original_printed_oligos(sentence.format(s))]
    assert len(found_by_original) > 300, "the frozen rule no longer reproduces the original"
    lost = [s for s in found_by_original if s not in vo.printed_oligos(sentence.format(s))]
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
    """With a text that prints ONE oligo: below the floor, where a would-be `absent`
    becomes `no-oligos`. An exact match must still read exact, and so must a reverse
    complement. (The first version of this test used a two-oligo text, which the floor
    never touches, so it could not fail for what it names.)"""
    text = f"forward primer 5'-{SEQ}-3' was used"
    printed = vo.printed_oligos(text)
    assert len(printed) < vo.MIN_PRINTED_FOR_ABSENT, printed
    assert vo.judge(SEQ, text, printed, 4)[0] == "exact"
    rc_text = f"reverse primer 5'-{vo.reverse_complement(SEQ)}-3' was used"
    assert len(vo.printed_oligos(rc_text)) < vo.MIN_PRINTED_FOR_ABSENT
    assert vo.judge(SEQ, rc_text, vo.printed_oligos(rc_text), 4)[0] == "revcomp"


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
    assert "33 nt" in note and "the stored oligo is 30" in note
    # Aligned end to end the three extra bases are INSIDE the run, which is the part that
    # is evidence the stored sequence is wrong; there is nothing at either end.
    assert "3 base(s) inside it that the stored sequence lacks" in note, note
    assert "at the run's 5' end" not in note and "at its 3' end" not in note


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


def test_a_parenthesised_doi_finds_its_file(tmp_path):
    """The papers/ convention writes /, ( and ) all as _, so the stem cannot be
    reversed into a DOI. Rahn 1992 (10.1016/0890-8508(92)90002-F) sat in papers/
    for months while the verifier reported "no local PDF", because the reverse
    mapping produced 10.1016/0890-8508/92/90002-f - still DOI-shaped, so indexed
    under a DOI nothing asks for and marked "named", which also barred the
    surname-and-year fallback."""
    (tmp_path / "10.1016_0890-8508_92_90002-f.txt").write_text(RICH)
    by_doi, everything = vo.index_papers(tmp_path)

    assert vo.doi_stem("10.1016/0890-8508(92)90002-F") == "10.1016_0890-8508_92_90002-f"
    assay = _assay("10.1016/0890-8508(92)90002-F", None, 1992)
    hit = vo.local_paper(assay, by_doi, everything)
    assert hit is not None and hit[1].name == "10.1016_0890-8508_92_90002-f.txt"


def test_a_stem_key_never_shadows_a_real_doi(tmp_path):
    """Stem keys share `by_doi`, which is safe only because a DOI always holds a
    "/" and a filename stem never does."""
    (tmp_path / "10.5555_mine.9.txt").write_text(RICH)
    by_doi, _ = vo.index_papers(tmp_path)
    assert "10.5555/mine.9" in by_doi  # the reverse-mapped name, unchanged
    assert vo.STEM_KEY + "10.5555_mine.9" in by_doi  # and the stem, newly
    # Every stem key is prefixed, so nothing walking by_doi can read one as a DOI:
    # unprefixed stems made extract_candidate_oligos label a file with its own name.
    assert all(k.startswith(vo.STEM_KEY) or "/" in k for k in by_doi)


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


# ==========================================================================
# Added after the second review
# ==========================================================================

# Deckers 2009 (Virol J 6:210), Table 1 as PubMed Central serves it: the printed
# notation is `(n/i)`, `(b/i)`, `(r/i)` and `(y/i)`, four different "X or inosine" positions.
DECKERS_TABLE = """
Table 1  Primers for amplification of the glycoprotein B and UL33 genes
CMV-gBp1
4007s
1
GGTGACGTGGTTGACAT(n/i)TC(n/i)CC
800
4007as
GCAATCGGTTTGTTGTA(n/i)AT(n/i)GC
4125s
2
GCGGACTCGGTGAT(b/i)TC(n/i)TGGGA
550
4125as
GCTGACGGGTTGATCTTGCT(r/i)AG
CMV-gBp2
4524s
1
GGAATCCAGGAT(y/i)TGGT(r/i)CCT
1790
"""


@pytest.mark.parametrize(
    "printed, normalised",
    [
        ("GCGGACTCGGTGAT(b/i)TC(n/i)TGGGA", "GCGGACTCGGTGATNTCNTGGGA"),
        ("GCTGACGGGTTGATCTTGCT(r/i)AG", "GCTGACGGGTTGATCTTGCTNAG"),
        ("GGAATCCAGGAT(y/i)TGGT(r/i)CCT", "GGAATCCAGGATNTGGTNCCT"),
        ("CGTTGTCCTC[i/n]CC[N/I]ARYTG( I / B )CC", "CGTTGTCCTCNCCNARYTGNCC"),
    ],
)
def test_every_x_or_inosine_notation_is_resolved_not_just_n_or_inosine(printed, normalised):
    assert vo.normalise_notation(printed) == normalised


def test_a_genuine_two_base_bracket_is_left_alone():
    """Only the inosine forms are rewritten: `(A/G)` is some other notation entirely."""
    assert vo.normalise_notation("ACGT(A/G)ACGT") == "ACGT(A/G)ACGT"


def test_deckers_table_is_read_whole_and_the_stored_primers_verify_exact():
    """The two registry entries that will be re-cited to Deckers 2009 must read exact
    against it, which they did not while only `(n/i)` was understood: 4125s split at
    `(b/i)` into a 14-mer and 4125as lost its last two bases."""
    text = vo.normalise_notation(DECKERS_TABLE)
    printed = vo.printed_oligos(text)
    assert len(printed) == 5, printed  # five oligos; two carry table text glued on, as real tables do
    for stored in (
        "GGTGACGTGGTTGACATNTCNCC",  # 4007s
        "GCAATCGGTTTGTTGTANATNGC",  # 4007as
        "GCGGACTCGGTGATNTCNTGGGA",  # 4125s
        "GCTGACGGGTTGATCTTGCTRAG",  # 4125as: the paper prints R-or-inosine, the registry keeps R
    ):
        verdict, note = vo.judge(stored, text, printed, 4)
        assert verdict in ("exact", "near:1"), (stored, verdict, note)
    # 4125as is the one that matters most: its last two bases were lost before the fix.
    assert any("GCTGACGGGTTGATCTTGCTNAG" in p for p in printed), printed


# ---- which file holds a DOI, independent of file order -----------------------------------


def _papers(tmp_path, files: dict[str, str]):
    for name, body in files.items():
        (tmp_path / name).write_text(body)
    return vo.index_papers(tmp_path)[0]


REVIEW = (
    "A review of the field. This article doi:10.7777/review.1 . Related work: doi:10.9999/smith.2010 . "
    + RICH
    + " primer 5'-CCTTGGTTAAGGCCTTGGAACCTT-3' primer 5'-GGAACCTTGGTTAAGGCCTTGGAA-3'"
)
PAPER = "Smith et al. This article doi:10.9999/smith.2010 . " + RICH


@pytest.mark.parametrize(
    "review_name, paper_name",
    [("a_review.txt", "b_smith2010.txt"), ("b_review.txt", "a_smith2010.txt")],
    ids=["review-sorts-first", "paper-sorts-first"],
)
def test_the_paper_holds_its_own_doi_whichever_file_sorts_first(tmp_path, review_name, paper_name):
    """The first fix made an unnamed claim only fill an empty slot, so the first-sorted
    file kept the DOI: a review that sorted ahead of the paper it reprints took its
    place. The file that prints the DOI EARLIER now wins, in either order."""
    by_doi = _papers(tmp_path, {review_name: REVIEW, paper_name: PAPER})
    assert by_doi["10.9999/smith.2010"][1].name == paper_name
    assert by_doi["10.7777/review.1"][1].name == review_name


def test_an_erratum_that_cites_another_doi_first_still_holds_its_own(tmp_path):
    by_doi = _papers(
        tmp_path,
        {
            "a_paper.txt": "doi:10.1111/aaa.1 " + RICH,
            "b_erratum.txt": "Erratum to doi:10.1111/aaa.1 . This article doi:10.2222/bbb.2 . " + RICH,
        },
    )
    assert by_doi["10.1111/aaa.1"][1].name == "a_paper.txt"
    assert by_doi["10.2222/bbb.2"][1].name == "b_erratum.txt"


def test_equal_offsets_keep_the_incumbent(tmp_path):
    claims, by_doi = {}, {}
    vo.claim(by_doi, claims, "10.1/x", "first", Path("a.txt"), 2, named=False, offset=5)
    vo.claim(by_doi, claims, "10.1/x", "second", Path("b.txt"), 9, named=False, offset=5)
    assert by_doi["10.1/x"][1].name == "a.txt"
    vo.claim(by_doi, claims, "10.1/x", "third", Path("c.txt"), 0, named=False, offset=4)
    assert by_doi["10.1/x"][1].name == "c.txt"  # earlier wins even with fewer oligos


def test_text_dois_records_the_first_occurrence_only():
    out = vo.text_dois(
        "x doi:10.1234/a.1 y doi:10.1234/b.2 z doi:10.1234/a.1 " + "q" * 5000 + " 10.9999/late.1"
    )
    assert list(out) == ["10.1234/a.1", "10.1234/b.2"]
    assert out["10.1234/a.1"] < out["10.1234/b.2"]


# ---- main() really goes through judge(), and the floor does not touch exact ----------------


def _verify(tmp_path, paper_text, capsys, extra=()):
    reg, d = _one_entry_registry(tmp_path)
    papers = tmp_path / "papers"
    papers.mkdir(exist_ok=True)
    (papers / "10.1128_aem.02897-13.txt").write_text(paper_text)
    out = tmp_path / "v.tsv"
    rc = vo.main(["--registry", str(reg), "--pdf-dir", str(papers), "--tsv", str(out), *extra])
    rows = list(csv.DictReader(out.open(), delimiter="\t"))
    return rc, rows, capsys.readouterr().out, d


def test_main_reports_no_oligos_for_a_thin_paper_and_excludes_it_from_the_headline(tmp_path, capsys):
    """Drives the whole script: a paper that prints ONE oligo cannot call the others
    absent. A main() that bypassed judge() would report them `absent` and put them in
    the headline denominator."""
    fwd = yaml.safe_load((ROOT / "registry" / "PD_WNS_ITS1_Shuey_2014.yaml").read_text())["oligos"][
        "forward"
    ]["seq"]
    rc, rows, out, _ = _verify(tmp_path, f"Methods. The forward primer was 5'-{fwd}-3'.", capsys)
    verdicts = {r["slot"]: r["verdict"] for r in rows}
    assert rc == 0
    assert verdicts["forward"] == "exact", verdicts
    assert {v for k, v in verdicts.items() if k != "forward"} == {"no-oligos"}, verdicts
    assert "1 of 1 checkable oligos agree" in out, out


def test_a_lost_inline_sequence_reads_no_oligos_not_absent():
    """The avipox paper's reverse primer reads `primer 1R ()`: the name survives and the
    bracket that held the sequence is emptied. The text still prints two other oligos,
    so the floor does not catch it; the empty bracket is the marker."""
    text = (
        "Primer 1F (5'-TCC TTG TAA AAG CGA TAC AGG AA-3') and primer 1R () produce a 234 bp fragment "
        "within which lies the Pox1 probe (5'-CAG CGT GAT GAA GAC GCT AA-3')."
    )
    printed = vo.printed_oligos(text)
    assert len(printed) == 2, printed
    verdict, note = vo.judge("TTGGCCAAGTTGGCCAAGTTGG", text, printed, 4, name="1R")
    assert verdict == "no-oligos" and "EMPTY bracket" in note, (verdict, note)
    # Without the name, or for a name that does not sit before an empty bracket, it is a real absent.
    assert vo.judge("TTGGCCAAGTTGGCCAAGTTGG", text, printed, 4)[0] == "absent"
    assert vo.judge("TTGGCCAAGTTGGCCAAGTTGG", text, printed, 4, name="2R")[0] == "absent"
    assert (
        vo.judge("TTGGCCAAGTTGGCCAAGTTGG", text, printed, 4, name="1F")[0] == "absent"
    )  # 1F has its sequence


def test_short_oligo_names_match_whole_tokens_only():
    text = "Primer 1F was used with primer 1R, see Fig. 11F and T7 promoter; the tag1Fox is unrelated."
    assert [text[i : i + 2] for i in vo.find_name("1F", text)] == ["1F"]  # not inside `11F`, `tag1Fox`
    assert vo.find_name("1f", text) == []  # case-sensitive: short names are too easy to hit otherwise
    assert vo.find_name("F", text) == []  # a single character cannot be searched at all
    assert vo.name_pattern("F") is None
    assert vo.find_name("BornaPCA3(+)", "primer BornaPCA3 was used")  # long names stay loose


# ---- the longer-run note says where the extra bases are -------------------------------------


def test_a_longer_run_with_glue_on_one_end_is_not_offered_as_the_oligo():
    """Table extraction glues a primer name's last letters onto the sequence. The note
    must say the extra bases are at the END of the run, where they may be glue, and not
    present the whole run as 'the paper's own sequence'."""
    glued = "ASGCAATCGGTTTGTTGTANATNGC"  # `...4007as` + the sequence, one substitution from the stored
    stored = "GCAATCGGTTTGTTGTANATNCC"
    verdict, note = vo.check(stored, "", [glued], 4)
    assert verdict == "near:1", (verdict, note)
    assert "2 extra base(s) at the run's 5' end" in note, note
    assert "inside it" not in note
    assert "table text glued on" in note
    # and on the 3' end, in either orientation of the stored sequence
    _, note3 = vo.check(stored, "", ["GCAATCGGTTTGTTGTANATNGCAS"], 4)
    assert "2 extra base(s) at its 3' end" in note3, note3
    _, note_rc = vo.check(vo.reverse_complement(stored), "", [glued], 4)
    assert "2 extra base(s) at the run's 5' end" in note_rc, note_rc


def test_align_to_run_on_simple_cases():
    assert vo.align_to_run("ACGTACGT", "ACGTACGT") == (0, 0, 0, 0)
    assert vo.align_to_run("ACGTACGT", "TTACGTACGTGG") == (0, 2, 2, 0)
    assert vo.align_to_run("ACGTACGT", "ACGTTTACGT")[0] == 2  # two extra bases in the middle
    assert vo.align_to_run("ACGTACGT", "ACGTTTACGT")[3] == 2
    edits, five, three, inside = vo.align_to_run("ACGTACGT", "ACCTACGT")
    assert (edits, five, three, inside) == (1, 0, 0, 0)


# ---- counts per FILE, and the listing -------------------------------------------------------


def test_a_thin_paper_citing_other_dois_is_counted_once(tmp_path, capsys):
    papers = tmp_path / "papers"
    papers.mkdir()
    (papers / "10.1234_thin.1.txt").write_text(
        "Methods only. See doi:10.5555/ref.one, doi:10.5555/ref.two and doi:10.5555/ref.three. " + POOR
    )
    reg, _ = _one_entry_registry(tmp_path)
    vo.main(["--registry", str(reg), "--pdf-dir", str(papers)])
    out = capsys.readouterr().out
    assert "indexed 1 readable papers" in out and "(1 with a DOI)" in out, out
    assert "1 print fewer than 2 oligos" in out, out


def test_the_near_listing_is_in_numeric_order_and_keeps_the_whole_note():
    rows = [
        {"assay_id": "B", "oligo_name": "x", "verdict": "near:10", "note": "ten"},
        {"assay_id": "A", "oligo_name": "y", "verdict": "near:2", "note": "two"},
        {"assay_id": "C", "oligo_name": "z", "verdict": "near:3", "note": "n" * 70 + "TAIL-MARKER"},
    ]
    lines = vo.near_listing(rows)
    order = [ln.split()[2] for ln in lines if "near:" in ln]
    assert order == ["near:2", "near:3", "near:10"], order
    assert any("TAIL-MARKER" in ln for ln in lines), "the end of a long note was cut off"


def test_two_named_files_with_equal_yield_keep_the_first(tmp_path):
    """Ties keep the incumbent, so the result follows the stable file order and does not
    flip on filesystem order."""
    by_doi = _papers(tmp_path, {"10.1234_tie.1.txt": RICH, "10.1234_tie.1.xml": f"<article>{RICH}</article>"})
    assert by_doi["10.1234/tie.1"][1].suffix == ".xml"  # paper_files lists .xml before .txt


def test_main_passes_the_oligo_name_so_a_lost_inline_sequence_is_caught(tmp_path, capsys):
    """judge() can spot `primer 1R ()`, but only if main() hands it the name."""
    d = yaml.safe_load((ROOT / "registry" / "PD_WNS_ITS1_Shuey_2014.yaml").read_text())["oligos"]
    text = (
        f"Methods. Forward primer {d['forward']['name']} 5'-{d['forward']['seq']}-3' and probe "
        f"{d['probe']['name']} 5'-{d['probe']['seq']}-3'; reverse primer {d['reverse']['name']} () was also used."
    )
    _, rows, _, _ = _verify(tmp_path, text, capsys)
    verdicts = {r["slot"]: r["verdict"] for r in rows}
    assert verdicts["forward"] == "exact" and verdicts["probe"] == "exact", verdicts
    assert verdicts["reverse"] == "no-oligos", verdicts


def test_a_supplement_is_evidence_about_its_own_article(tmp_path):
    """`<doi stem>.supp.<ext>` answers to the article's DOI, not to a DOI of its own.

    Where a paper sets its primer table as an image and prints it in the
    supplement - Hermes 2018 and McAloose 2016 both do - the sequences are only
    reachable if the supplement is filed under the article. Reading `.supp` as
    part of the DOI filed it under `10.1371/journal.pone.0207365.supp`, which
    still matches a DOI pattern and which nothing cites, so three entries read
    `no-oligos` against a table that was on disk. `papers_index` already knew
    the convention; the two readers now share it.
    """
    (tmp_path / "10.1234_test.2.txt").write_text("Primers are given in Table S1.")
    (tmp_path / "10.1234_test.2.supp.txt").write_text(
        "Table S1. 5'-GCGGCCAACCAGTTTAACGCAA-3' and 5'-ATTGCGCTGGAACCTTGTCAA-3'."
    )
    by_doi, _ = vo.index_papers(tmp_path)
    assert "10.1234/test.2.supp" not in by_doi
    text, path = by_doi["10.1234/test.2"]
    # Both claims are named, so the one printing the sequences wins on yield.
    assert path.name == "10.1234_test.2.supp.txt", path
    assert len(vo.printed_oligos(text)) == 2


# The CDV arctic variants: each differs by design from its entry's Mueller primer,
# and the paper text held prints only the Mueller primer.
MUELLER_2F = "GCGATACAATTGGGATCAGA"
ARCTIC_2F = "GTGAGACAATTGGGATCAGA"
SIBLING_TEXT = (
    "Primers Mueller-2F 5'-GCGATACAATTGGGATCAGA-3' and Mueller-2R 5'-TGGGTGAGCAACAGGTATCA-3' "
    "amplified the H gene."
)


def test_a_variant_nearest_to_its_own_sibling_reads_sibling_not_near():
    printed = vo.printed_oligos(SIBLING_TEXT)
    assert vo.judge(ARCTIC_2F, SIBLING_TEXT, printed, 4)[0] == "near:2"
    verdict, note = vo.judge(ARCTIC_2F, SIBLING_TEXT, printed, 4, siblings=[("Mueller-2F", MUELLER_2F)])
    assert verdict == "sibling", (verdict, note)
    assert "Mueller-2F" in note


def test_a_sibling_the_paper_does_not_print_explains_nothing():
    """A real transcription error must still surface when the entry has alternates."""
    printed = vo.printed_oligos(SIBLING_TEXT)
    verdict, _ = vo.judge(ARCTIC_2F, SIBLING_TEXT, printed, 4, siblings=[("other", "ACGTACGTACGTACGTACGT")])
    assert verdict == "near:2"


def test_a_sibling_further_away_than_the_printed_run_explains_nothing():
    """If the nearest run is closer than the sibling, the sibling is not why it is near."""
    printed = vo.printed_oligos(SIBLING_TEXT)
    far = "TGGGTGAGCAACAGGTATCA"  # Mueller-2R, printed, but many edits from ARCTIC_2F
    verdict, _ = vo.judge(ARCTIC_2F, SIBLING_TEXT, printed, 4, siblings=[("Mueller-2R", far)])
    assert verdict == "near:2"


def test_a_recorded_modification_reads_modified_when_the_paper_prints_the_original():
    from assaywatch.schema import Oligo

    text = "Primers ARS3V 5'-CATGACKMTGAATTYTGTGACA-3' and ARS7C 5'-ATGTGYCTRTGAGTTGG-3' were used."
    printed = vo.printed_oligos(text)
    o = Oligo(
        name="ARS7C-MOD",
        seq="ATRTGYCKRTGWGTTGG",
        modified_from="ATGTGYCTRTGAGTTGG",
        modification_doi="10.1038/ncomms9147",
    )
    verdict, note = vo.judge(o.seq, text, printed, 4)
    assert verdict.startswith("near:")
    verdict, note = vo.judge_modified(o, verdict, note, text, printed, 4)
    assert verdict == "modified" and "10.1038/ncomms9147" in note


def test_a_modification_whose_original_is_not_printed_keeps_its_verdict():
    from assaywatch.schema import Oligo

    text = "Primers 5'-ATTGCGCTGGAACCTTGTCAAGG-3' and 5'-CCTTGGTTAAGGCCTTGGAACCTT-3' were used."
    printed = vo.printed_oligos(text)
    o = Oligo(name="X", seq="ACTYCTACGGGAGGCAGCAGTA", modified_from="ACTCCTACGGGAGGCAGCAGTA")
    verdict, note = vo.judge(o.seq, text, printed, 4)
    v2, note2 = vo.judge_modified(o, verdict, note, text, printed, 4)
    assert v2 == verdict and "modified_from" in note2


def test_a_modification_doi_needs_the_original_sequence():
    from pydantic import ValidationError

    from assaywatch.schema import Oligo

    with pytest.raises(ValidationError):
        Oligo(seq="ACTYCTACGGGAGGCAGCAGTA", modification_doi="10.1038/ncomms9147")
    with pytest.raises(ValidationError):
        Oligo(seq="ACTCCTACGGGAGGCAGCAGTA", modified_from="ACTCCTACGGGAGGCAGCAGTA")
