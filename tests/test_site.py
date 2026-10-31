"""The website: what it withholds, what it must not invent, and the two places
its pieces can silently fall out of step with each other.

The site is the most-read surface the project has, so the tests that matter are
not "does it render" but "does it say something the report would not".
"""

from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

from assaywatch import palette, site, site_render, site_svg

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "website" / "data" / "run.json"


def _page(**kw):
    """A minimal extracted page; tests override only the field under test."""
    base = dict(
        assay_id="TEST_assay",
        name="A test assay",
        status="stable",
        withheld_reasons=[],
        taxon="Testus testus",
        taxid=1,
        gene="gene",
        chemistry="conventional",
        doi="10.1/x",
        reference="Someone 2020",
        design_year=2020,
        amplicon_bp=100,
        entry_status="active",
        review_flags=[],
        scope_taxids=[],
        exclusivity_taxids=[],
        query="",
        title_requires=[],
        oligos={"forward": "ACGT", "reverse": "TGCA"},
        recent_detected=90,
        recent_evaluable=100,
        recent_ci=[0.82, 0.95],
        baseline_detected=95,
        baseline_evaluable=100,
        baseline_ci=[0.88, 0.98],
        change_ci=[-0.12, 0.02],
        window_months=24,
        recent_from="Oct 2024",
        threshold=0.9,
        note="",
        trend="",
        years=[{"year": 2024, "detected": 90, "evaluable": 100, "share": 0.9, "recent": True}],
        positions=[],
        lineages=[],
        screened_rows=200,
        no_amplicon_rows=100,
        exclusions=[["no_site", 100]],
        out_of_scope=0,
    )
    base.update(kw)
    return base


def test_a_withheld_assay_gets_no_status_and_no_verdict_arithmetic():
    """`report.py` withholds a status from an assay whose entry says the screen's
    output would not be a statement -- `not_screenable`, `do_not_use`. The site is
    far more read than the report, so a dashboard that showed a confident verdict
    where the report shows none would be the worst possible place to disagree.

    The specific damage this prevents is recorded in `report.held_out_reasons`: an
    RPA assay scored by PCR penalties once read "Stable, 100.0%", a false
    all-clear, and an assay identified by a restriction digest read "Declining".
    """
    md = site_render.assay_page(
        _page(status="stable", withheld_reasons=[["not_screenable", "the chemistry is RPA"]]), "2026-10-31"
    )
    assert "status withheld" in md
    assert "not_screenable" in md and "the chemistry is RPA" in md
    # No verdict section, no arithmetic, no charts drawn in a verdict colour.
    # Matching the HEADING rather than the word: the withholding notice itself
    # says "the verdict is withheld", and a substring test on that word passed
    # only until the notice was reworded.
    assert "## Verdict" not in md
    assert "## Predicted detection by deposit year" not in md
    assert "Newcombe" not in md, "the change interval is part of the withheld arithmetic"
    assert "<svg" not in md
    assert "stable" not in md.replace("aw-chip-none", "")


def test_a_status_is_never_carried_by_colour_alone():
    """The palette's one accepted colour-vision warning (stable teal against watch
    amber, dE 7.6 under protanopia) is licensed ONLY where a second encoding says
    the same thing. Every chip therefore writes the status out."""
    for status in palette.VERDICTS:
        chip = site_render._chip(status)
        assert status in chip, f"{status} chip has no text"
        assert "aw-chip" in chip


def test_the_page_prints_the_counts_its_share_is_computed_from():
    """A share without its denominator is the thing this project exists to argue
    against, so the page carries detected, evaluable and the interval, not just a
    percentage."""
    md = site_render.assay_page(_page(), "2026-10-31")
    assert "90" in md and "100" in md
    assert "95% interval" in md
    assert "Newcombe" in md


def test_every_mismatch_position_is_drawn_against_its_own_base():
    """The figure this project exists for, and the one that was worst.

    The Bokeh version plotted only the positions carrying a mismatch, so a 23-mer
    with defects at 18, 17, 2 and 1 drew four boxes and a void: nothing said where
    along the oligo they sat, and the bases were never shown. The track must draw
    the WHOLE oligo, so a position is read against the sequence it belongs to.
    """
    page = _page(
        oligos={"forward": "ACGTACGTAC"},
        positions=[
            dict(
                oligo="forward",
                pos_3prime=2,
                base="A",
                n_mismatch=50,
                detected_with=0,
                evaluable_with=50,
                detected_without=50,
                evaluable_without=50,
                substitutions=[["A", "G", 50]],
                in_3prime_zone=True,
            )
        ],
    )
    svg = site_svg.mismatch_track(page)
    # Every base of the oligo is drawn, not just the one that mismatches.
    assert svg.count('class="aw-base"') == 10
    # The mismatching position is marked, and its cost is in the tooltip.
    assert "aw-bar-strong" in svg, "a position where detection falls to 0 must read as severe"
    assert "detected when it differs: 0%" in svg
    assert "5\u2032" in svg or "5\u2032" in svg


def test_a_frequent_but_harmless_position_is_not_coloured_as_a_failure():
    """Bar colour is the COST of a mismatch, never its frequency. A base half the
    records differ at that costs nothing is a polymorphism, and colouring it like
    a failure would point a reader at the wrong position to redesign."""
    page = _page(
        oligos={"forward": "ACGTACGTAC"},
        positions=[
            dict(
                oligo="forward",
                pos_3prime=9,
                base="C",
                n_mismatch=500,
                detected_with=495,
                evaluable_with=500,
                detected_without=500,
                evaluable_without=500,
                substitutions=[],
                in_3prime_zone=False,
            )
        ],
    )
    svg = site_svg.mismatch_track(page)
    assert "aw-bar-weak" in svg
    assert "aw-bar-strong" not in svg


def test_the_figures_need_no_chart_library_and_no_network():
    """Inline SVG with no runtime: this is what removed the three-way version
    problem between the installed renderer, a constant and a CDN script tag."""
    page = _page(
        years=[
            {"year": 2020, "detected": 5, "evaluable": 10, "share": 0.5, "recent": False},
            {"year": 2024, "detected": 9, "evaluable": 10, "share": 0.9, "recent": True},
        ],
        oligos={"forward": "ACGTACGTAC"},
        # One mismatching position, so the track has a mark to carry a tooltip.
        # Without one it correctly draws bases and no titles, which is not what
        # this test is about.
        positions=[
            dict(
                oligo="forward",
                pos_3prime=3,
                base="G",
                n_mismatch=20,
                detected_with=1,
                evaluable_with=20,
                detected_without=80,
                evaluable_without=80,
                substitutions=[["G", "A", 20]],
                in_3prime_zone=True,
            )
        ],
        lineages=[
            {
                "lineage": "Some lineage",
                "taxid": 1,
                "evaluable": 40,
                "detected": 30,
                "share": 0.75,
                "ci": [0.6, 0.86],
            }
        ],
    )
    for svg in (site_svg.year_chart(page), site_svg.mismatch_track(page)):
        assert svg.startswith("<svg")
        assert "<script" not in svg
        assert "http://" not in svg.replace('xmlns="http://www.w3.org/2000/svg"', "")
        assert "<title>" in svg, "every mark needs a native tooltip; nothing is hover-only elsewhere"
    assert "bokeh" not in (ROOT / "mkdocs.yml").read_text().lower()
    assert "bokeh" not in (ROOT / "pyproject.toml").read_text().lower()


def test_every_status_the_pipeline_can_emit_has_a_colour_and_a_meaning():
    """A status added to `drift.STATUS_ORDER` without a colour here would render as
    the neutral grey chip, which MEANS something specific -- no verdict -- so the
    failure would read as a deliberate statement rather than as a gap."""
    from assaywatch.drift import NO_DATA, STATUS_ORDER

    for status in (*STATUS_ORDER, NO_DATA):
        assert status in palette.STATUS_LIGHT, f"{status} has no light colour"
        assert status in palette.STATUS_DARK, f"{status} has no dark colour"
        assert status in site_render.STATUS_MEANING, f"{status} has no one-line meaning"


def test_the_withheld_count_matches_the_registry_rather_than_being_a_literal():
    """`index.md` counts statuses from the data. A hand-written count here would be
    the exact failure `scripts/claims.py` exists to prevent."""
    data = {
        "run_date": "2026-10-31",
        "assays": [_page(), _page(assay_id="B", status="", withheld_reasons=[["x", "y"]])],
    }
    md = site_render.index_page(data)
    assert "**1** stable" in md
    assert "**1** status withheld" in md


@pytest.mark.skipif(not DATA.exists(), reason="website/data/run.json is not present")
class TestAgainstTheCommittedRun:
    """The committed extract is what the published site is built from, so these
    check the artifact rather than the code."""

    @pytest.fixture(scope="class")
    def data(self):
        return json.loads(DATA.read_text())

    def test_the_schema_is_the_one_the_renderer_expects(self, data):
        assert data["schema"] == site.SCHEMA

    def test_every_assay_in_the_run_is_in_the_registry(self, data):
        from assaywatch import registry

        live = set(registry.load(ROOT / "registry"))
        extracted = {a["assay_id"] for a in data["assays"]}
        assert extracted <= live, f"not in registry/: {sorted(extracted - live)}"

    def test_no_page_claims_a_status_its_entry_withholds(self, data):
        for a in data["assays"]:
            if a["withheld_reasons"]:
                assert a["status"] == "", f"{a['assay_id']} has both a status and a withholding reason"

    def test_a_detected_count_never_exceeds_its_denominator(self, data):
        for a in data["assays"]:
            assert a["recent_detected"] <= a["recent_evaluable"], a["assay_id"]
            assert a["baseline_detected"] <= a["baseline_evaluable"], a["assay_id"]
            for y in a["years"]:
                assert y["detected"] <= y["evaluable"], f"{a['assay_id']} {y['year']}"

    def test_the_generated_pages_are_current_for_the_committed_data(self, data):
        """The published site is built in CI from this JSON; if the committed
        markdown was rendered from an older extract, the site and the data would
        disagree and the CI job would be the only thing to notice."""
        page = data["assays"][0]
        on_disk = ROOT / "website" / "assays" / f"{page['assay_id']}.md"
        assert on_disk.exists(), f"{on_disk} was never rendered"
        # Byte for byte. This used to need the per-render ids normalised away,
        # because Bokeh minted a fresh uuid every time; the inline-SVG figures
        # are a pure function of the data, so an exact comparison works and is
        # the stronger check.
        assert on_disk.read_text() == site_render.assay_page(page, data["run_date"]), (
            f"{on_disk.name} is stale; re-run `python -m assaywatch.site_render`"
        )


def test_the_site_quotes_no_undated_registry_count():
    """`scripts/claims.py` polices registry counts in prose. The site's prose pages
    are in its PROSE list; this asserts the list actually covers them, because a
    page added later would otherwise be unpoliced."""
    import importlib.util

    spec = importlib.util.spec_from_file_location("claims", ROOT / "scripts" / "claims.py")
    claims = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(claims)
    covered = {str(p) for p in claims.PROSE}
    for page in sorted((ROOT / "website").glob("*.md")):
        rel = str(page.relative_to(ROOT))
        if page.name == "glossary.md":
            # Generated from GLOSSARY.md, which is itself in PROSE.
            assert "GLOSSARY.md" in covered
            continue
        assert rel in covered, f"{rel} is prose and is not in scripts/claims.py PROSE"


def test_the_glossary_page_is_the_repository_glossary():
    """Two glossaries is two vocabularies. The page is generated from GLOSSARY.md,
    and this fails if someone edits the generated copy instead of the source."""
    page = (ROOT / "website" / "glossary.md").read_text()
    source = (ROOT / "GLOSSARY.md").read_text()
    # Every term heading in the source must survive into the page verbatim.
    terms = re.findall(r"^\*\*(.+?)\*\*", source, re.M)
    assert terms, "GLOSSARY.md has no bolded terms; this test is checking the wrong thing"
    missing = [t for t in terms if f"**{t}**" not in page]
    assert not missing, f"website/glossary.md is stale, missing: {missing[:5]}"


def test_every_clickable_pipeline_stage_has_a_section_to_open():
    """The diagram's nodes and the page's sections are written by hand in the same
    file, and nothing but this connects them. A node whose `data-stage` has no
    matching section is a box that looks clickable and does nothing; a section with
    no node is unreachable except by deep link. Both are silent in a build."""
    page = (ROOT / "website" / "pipeline.md").read_text()
    nodes = set(re.findall(r'data-stage="([a-z]+)"', page))
    sections = set(re.findall(r"\{:\s*#stage-([a-z]+)", page))
    assert nodes, "the pipeline diagram has no clickable nodes"
    assert nodes == sections, (
        f"nodes without a section: {sorted(nodes - sections)}; "
        f"sections without a node: {sorted(sections - nodes)}"
    )


def test_the_pipeline_page_reads_without_javascript():
    """The stage panels are plain markdown and are only collapsed by script, so the
    page degrades to a full written outline. If the sections were hidden in the
    source instead, a reader without JavaScript -- or with the CDN blocked -- would
    get a diagram and nothing else."""
    page = (ROOT / "website" / "pipeline.md").read_text()
    assert "hidden" not in page.split("<figcaption>")[1], "stage sections must not ship hidden"
    built = ROOT / ".site" / "pipeline" / "index.html"
    if built.exists():
        html = built.read_text()
        for stage in ("screen", "retrieve", "degeneracy"):
            assert f'id="stage-{stage}"' in html
        # Prose, not just the anchors: the point is that a reader without
        # JavaScript gets the written pipeline rather than a diagram and twelve
        # empty headings. Anchored on a term the stage cannot be described
        # without, rather than on a turn of phrase a rewrite will change.
        assert "both strands" in html, "the screen stage's prose is missing from the built page"
        assert "incremental" in html.lower(), "the retrieve stage's prose is missing"


def test_rendering_the_same_data_twice_gives_the_same_bytes():
    """The figures are a pure function of the data, with no random ids and no
    timestamps. That is what lets the staleness check compare exactly, and what
    keeps a rebuild from showing as a diff in every one of 217 files."""
    page = _page(
        years=[{"year": 2024, "detected": 9, "evaluable": 10, "share": 0.9, "recent": True}],
        lineages=[
            {"lineage": "L", "taxid": 1, "evaluable": 40, "detected": 30, "share": 0.75, "ci": [0.6, 0.86]}
        ],
    )
    assert site_render.assay_page(page, "2026-10-31") == site_render.assay_page(page, "2026-10-31")


def test_one_lineage_gets_a_sentence_rather_than_a_chart_of_one_row():
    """70 of the 125 assays with lineage data have exactly one lineage. A forest
    plot there is an axis, a grid, a threshold line and a single dot -- the
    furniture of a comparison with nothing to compare, which is what made the
    section unreadable. With one lineage the pooled figure above has already said
    it, so this says so and draws nothing."""
    page = _page(
        lineages=[
            {
                "lineage": "Only lineage",
                "taxid": 1,
                "evaluable": 165,
                "detected": 165,
                "share": 1.0,
                "ci": [0.977, 1.0],
            }
        ]
    )
    md = "\n".join(site_render._lineage_block(page))
    assert "Only lineage" in md and "165" in md
    assert "<table" not in md, "one lineage must not be drawn as a table"
    assert "<svg" not in md, "one lineage must not be drawn as a chart"


def test_a_lineage_whose_interval_clears_the_threshold_is_not_marked_as_failing():
    """The mark means the WHOLE interval sits below the bar, which is the same
    rule the assay-level flag uses. Marking a lineage that merely has a low point
    estimate would contradict the project's own standard of evidence."""
    page = _page(
        threshold=0.9,
        lineages=[
            {
                "lineage": "Wide but high",
                "taxid": 1,
                "evaluable": 12,
                "detected": 10,
                "share": 0.83,
                "ci": [0.55, 0.95],
            },
            {
                "lineage": "Clearly below",
                "taxid": 2,
                "evaluable": 900,
                "detected": 400,
                "share": 0.44,
                "ci": [0.41, 0.48],
            },
        ],
    )
    md = "\n".join(site_render._lineage_block(page))
    rows = [r for r in md.split("<tr ") if r.startswith('class="aw-lin')]
    assert len(rows) == 2, f"expected two lineage rows, got {len(rows)}"
    wide = next(r for r in rows if "Wide but high" in r)
    low = next(r for r in rows if "Clearly below" in r)
    assert "aw-lin-ok" in wide and "aw-lin-flag" not in wide
    assert "aw-lin-fail" in low and "aw-lin-flag" in low


def test_off_site_links_are_opened_safely_and_internal_ones_are_not_touched():
    """The DOI and taxonomy links leave the site, and a reader following a
    citation should not lose their place in a 217-row table. The rule is applied
    by host rather than by naming particular domains, so a link added later
    behaves the same without anyone remembering this.

    `noopener` is the part that matters beyond convenience: without it the opened
    page can reach back through `window.opener`.
    """
    js = (ROOT / "website" / "javascripts" / "tables.js").read_text()
    assert "awExternalLinks" in js
    assert "noopener" in js and "noreferrer" in js
    assert "host === here" in js, "internal links must stay in the same tab"
    # It must run again after an instant-navigation page swap, or it applies only
    # to the first page a reader lands on.
    assert js.count("document$.subscribe") >= 3


def test_the_paper_leads_the_page_and_its_doi_is_the_link():
    """What an entry rests on is the publication, and that is what a reader
    checks it against, so the paper's own title is the heading and the DOI is
    the thing you click."""
    page = _page(doi="10.1186/1743-422X-6-210", name="An assay name")
    md = site_render.assay_page(page, "2026-10-31")
    head, _, rest = md.partition("\n")
    assert head.startswith("# ")
    assert "doi.org/10.1186/1743-422X-6-210" in rest
    assert "doi:10.1186/1743-422X-6-210" in rest, "the DOI itself is the link text"
    # The entry id is still on the page, but it is not the headline.
    assert "# TEST_assay" not in md


def test_a_paper_with_no_cached_title_still_gets_a_heading():
    """The fallback, which every page used to need and none does now.

    Crossref's cache covers all 120 cited DOIs; a case-sensitive lookup matched
    only 85 of them, because the cache lower-cases its keys and 35 DOIs contain
    a capital. That read as missing data. The fallback stays because a newly
    added entry is uncached until the index is rebuilt."""
    page = _page(
        doi="10.0000/not-in-the-cache",
        name="Readable assay name",
        reference="Someone et al. 2009. A Journal 1:1-2",
    )
    md = site_render.assay_page(page, "2026-10-31")
    assert md.startswith("# Readable assay name")
    assert "aw-citation" in md and "??? quote" not in md


def test_the_citation_is_folded_when_the_heading_already_says_it():
    """Several stored references begin with the paper's full title, so showing
    both opens the page by saying the same sentence twice."""
    page = _page(doi="10.1186/1743-422X-6-210", reference="Deckers, M. et al. High genotypic diversity...")
    md = site_render.assay_page(page, "2026-10-31")
    assert "??? quote" in md
    assert '<p class="aw-citation">' not in md


def test_a_doi_is_looked_up_without_regard_to_case():
    """A DOI is case-insensitive by specification. The registry stores them as
    the publisher prints them and the papers cache lower-cases them, so a
    case-sensitive lookup silently loses every DOI containing a capital -- 35 of
    120 here, which presented as "Crossref has no title for these"."""
    from assaywatch import site_render as sr

    cache = sr._papers()
    assert cache, "the committed papers cache should not be empty"
    assert all(k == k.lower() for k in cache), "the lookup table must be lower-cased"
    title, _, _, _ = sr._paper({"doi": "10.1016/S1386-6532(03)00122-7", "design_year": 2004})
    assert title.startswith("Design and performance testing"), title
    upper, _, _, _ = sr._paper({"doi": "10.1016/s1386-6532(03)00122-7", "design_year": 2004})
    assert upper == title, "the same DOI in either case must resolve to the same paper"


def test_every_cited_paper_on_the_site_has_a_real_title():
    """All 120 cited DOIs are in the committed cache, so no page should be
    falling back to the assay name. This fails if the cache is rebuilt and loses
    entries, or if a new entry is added without rebuilding it."""
    data = json.loads(DATA.read_text()) if DATA.exists() else None
    if data is None:
        pytest.skip("website/data/run.json is not present")
    from assaywatch import site_render as sr

    missing = [a["assay_id"] for a in data["assays"] if a["doi"] and not sr._paper(a)[0]]
    assert not missing, (
        f"{len(missing)} assays cite a DOI with no cached title; "
        f"run `python scripts/papers_index.py`: {missing[:5]}"
    )
