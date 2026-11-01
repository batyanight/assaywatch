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


def test_the_list_counts_from_the_data_and_says_what_it_leaves_out():
    """`index.md` counts statuses from the data; a hand-written count would be the
    exact failure `scripts/claims.py` exists to prevent.

    It also excludes the assays with no usable status -- `insufficient data` and
    the withheld ones -- so it must say how many it dropped. A list that quietly
    showed 168 of 217 would misrepresent the registry's size."""
    data = {
        "run_date": "2026-10-31",
        "assays": [
            _page(),
            _page(assay_id="B", status="", withheld_reasons=[["x", "y"]]),
            _page(assay_id="C", status="insufficient data"),
            _page(assay_id="D", status="no recent data"),
        ],
    }
    md = site_render.index_page(data)
    assert "**1** stable" in md
    assert "**1** no recent data" in md, "no recent data is a reported state and stays listed"
    assert "2 assays, screened" in md, "only the two listable assays are counted"
    assert "A further 2 assays are not listed" in md
    assert "assays/C/" not in md, "an insufficient-data assay must not be listed"
    assert "assays/B/" not in md, "a withheld assay must not be listed"


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


def test_every_pipeline_node_links_to_a_stage_page_that_exists():
    """The diagram's nodes and the stage pages are written separately and
    nothing but this connects them. A node pointing at a missing page is a box
    that looks clickable and 404s; a stage page no node links to is reachable
    only from the nav. Both are silent in a build."""
    overview = (ROOT / "website" / "pipeline.md").read_text()
    linked = set(re.findall(r'class="aw-node[^"]*" href="([a-z]+)/"', overview))
    pages = {p.stem for p in (ROOT / "website" / "pipeline").glob("*.md")}
    assert linked, "the diagram has no linked nodes"
    assert linked == pages, (
        f"nodes with no page: {sorted(linked - pages)}; pages no node links to: {sorted(pages - linked)}"
    )


def test_every_stage_page_is_in_the_nav_so_it_gets_previous_and_next():
    """Previous and next come from the nav order, declared once in mkdocs.yml.
    A stage page missing from it still builds and still renders, but loses its
    place in the sequence."""
    nav = (ROOT / "mkdocs.yml").read_text()
    for page in sorted((ROOT / "website" / "pipeline").glob("*.md")):
        assert f"pipeline/{page.name}" in nav, f"{page.name} is not in the nav"


def test_a_stage_page_carries_its_prose_and_a_way_back():
    """The content moved out of one long page into twelve. This fails if a move
    dropped a stage's body, or if the theme stops emitting the way back."""
    screen = (ROOT / "website" / "pipeline" / "screen.md").read_text()
    assert "both strands" in screen and "3.0 million" in screen
    built = ROOT / ".site" / "pipeline" / "screen" / "index.html"
    if built.exists():
        html = built.read_text()
        assert 'class="breadcrumb"' in html
        assert "All stages" in html
        assert "Previous" in html and "Next" in html


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
    # The selector must match this theme's DOM. It once read `.md-content`, a
    # Material class that does not exist here, so it matched nothing at all and
    # every DOI opened in the same tab while the test still passed.
    assert "'main a[href]'" in js, "the external-link selector must target this theme's main element"
    theme = (ROOT / "theme" / "main.html").read_text()
    assert '<main id="main"' in theme
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


def test_a_probe_is_not_given_a_three_prime_window():
    """A hydrolysis probe is never extended: its 3' end carries the quencher or
    the minor-groove binder, and it is cleaved by the polymerase's 5'->3'
    exonuclease. There is no catalytic site at its 3' terminus, so the last five
    bases have no special status.

    `config.yaml` agrees in numbers -- `probe_center_penalty` 2.0 over the
    central third, `probe_outer_penalty` 1.0 elsewhere, and no 3' window for
    probes at all. The figure shaded the last five bases of every oligo, which
    drew a region the scorer does not use and implied a mechanism that does not
    exist.
    """
    page = _page(
        oligos={"forward": "ACGTACGTACGT", "probe": "ACGTACGTACGT"},
        positions=[
            dict(
                oligo="probe",
                pos_3prime=6,
                base="G",
                n_mismatch=10,
                detected_with=0,
                evaluable_with=10,
                detected_without=90,
                evaluable_without=90,
                substitutions=[],
                in_3prime_zone=False,
            ),
            dict(
                oligo="forward",
                pos_3prime=2,
                base="G",
                n_mismatch=10,
                detected_with=0,
                evaluable_with=10,
                detected_without=90,
                evaluable_without=90,
                substitutions=[],
                in_3prime_zone=True,
            ),
        ],
    )
    svg = site_svg.mismatch_track(page)
    assert "central third" in svg, "the probe's shaded region must be its central third"
    assert "3\u2032 window" in svg, "the primer must still show its 3' window"
    # A 12-mer probe: central third is indices 4..8, i.e. positions 5..8 from the 3' end.
    # Position 6 is inside it, so its tooltip must say so rather than talk about a 3' window.
    assert "in the central third" in svg


def test_the_scoring_config_still_has_no_three_prime_window_for_probes():
    """If a probe 3' penalty is ever added to the scoring, the figure above
    becomes wrong in the other direction. This fails loudly if that happens."""
    cfg = (ROOT / "config.yaml").read_text()
    assert "probe_center_penalty" in cfg
    assert "probe_outer_penalty" in cfg
    assert "probe_3prime" not in cfg, "scoring gained a probe 3' term; site_svg must be updated"


def test_an_assay_detecting_nothing_still_draws_a_visible_line():
    """Seven assays detect nothing in any year and five are flat zero. With 0%
    mapped to the baseline their series coincided with the axis, which reads as
    a chart that failed to draw rather than as a result."""
    page = _page(
        status="low coverage",
        years=[
            {"year": y, "detected": 0, "evaluable": 40, "share": 0.0, "recent": y > 2023}
            for y in (2019, 2020, 2021, 2022, 2023, 2024)
        ],
    )
    svg = site_svg.year_chart(page)
    assert svg, "a flat-zero assay must still produce a chart"
    ys = {float(v) for v in re.findall(r'cy="([0-9.]+)"', svg)}
    baseline = 230.0 - 38.0  # H - B, where the axis sits
    assert ys, "no points were drawn"
    assert max(ys) < baseline - 4, f"0% is drawn on the axis at y={max(ys)}, not above it"


def test_a_single_year_of_data_is_a_point_not_a_blank_panel():
    """Four assays have exactly one year holding evaluable records. The chart
    returned an empty string for them, so the page showed a heading, a caption
    and nothing between."""
    page = _page(years=[{"year": 2021, "detected": 8, "evaluable": 10, "share": 0.8, "recent": True}])
    svg = site_svg.year_chart(page)
    assert svg.startswith("<svg")
    assert svg.count("<circle") == 1
    assert "<polyline" not in svg, "one point is not a line"
    assert "one year holds every evaluable record" in svg
    assert svg.count(">2021<") == 1, "the single year should be labelled once"


def test_the_curator_note_reaches_the_page_and_is_not_interpreted():
    """For several entries the note is the only place a reader learns that the
    stored oligos are not the cited paper's -- the Victor 1991 entry is the
    clearest case, where the sequences are Wang 1997's and the attribution is
    one Wang made.

    It is escaped rather than passed through markdown: the notes contain primer
    sequences, DOIs, asterisks and underscores, and interpreting them would
    italicise a sequence or swallow a bracket."""
    notes = site_render._curation_notes()
    assert len(notes) > 150, f"only {len(notes)} entries have a curator note; expected most of 218"
    victor = notes.get("E_coli_ETEC_LT_Victor_1991", "")
    assert "not the cited paper" in victor

    page = _page(assay_id="E_coli_ETEC_LT_Victor_1991")
    md = "\n".join(site_render._curation_block(page))
    assert "<details" in md and "as the curator wrote it" in md
    assert "not the cited paper" in md
    # The disclosure says which order the episodes are in, so a reader is never
    # left guessing whether the newest entry is at the top or the bottom.
    assert ("newest first" in md) or ("oldest first" in md)


def test_a_withheld_assay_still_shows_its_curation_record():
    """Those 19 are the entries whose provenance a reader most needs, and the
    page returns early for them."""
    page = _page(
        withheld_reasons=[["not_screenable", "the chemistry is RPA"]], assay_id="E_coli_ETEC_LT_Victor_1991"
    )
    md = site_render.assay_page(page, "2026-10-31")
    assert "Curation record" in md


@pytest.mark.skipif(not DATA.exists(), reason="website/data/run.json is not present")
def test_the_extract_still_describes_the_registry_it_was_taken_from():
    """`run.json` snapshots each entry's descriptive fields -- gene, taxon,
    chemistry, amplicon -- alongside the run's results. Edit an entry and the
    snapshot is stale until it is re-extracted, and the site then renders the
    old value with no indication that it is old.

    That happened: seven entries had their `gene` filled in and every page went
    on showing an em dash, because the pages are built from the extract rather
    than from the registry. A reader cannot tell the difference, so this fails
    the build instead.
    """
    from assaywatch import registry

    data = json.loads(DATA.read_text())
    live = registry.load(ROOT / "registry")
    stale = []
    for a in data["assays"]:
        entry = live.get(a["assay_id"])
        if entry is None:
            continue
        for field, got in (
            ("gene", a["gene"]),
            ("taxon", a["taxon"]),
            ("chemistry", a["chemistry"]),
        ):
            want = {
                "gene": entry.target.gene or "",
                "taxon": entry.target.taxon_name or "",
                "chemistry": entry.chemistry.value,
            }[field]
            if got != want:
                stale.append(f"{a['assay_id']}.{field}: extract {got!r} != registry {want!r}")
    assert not stale, (
        f"{len(stale)} field(s) differ between website/data/run.json and the registry; "
        f"re-run `assaywatch site extract`: {stale[:4]}"
    )


def test_splitting_a_curator_note_into_episodes_never_loses_text():
    """The split is what makes the dated paragraphs possible, and it runs over
    an audit record. Reproducing the note exactly, ignoring whitespace, is the
    property that makes reordering safe; the renderer refuses to reorder when it
    does not hold."""
    from assaywatch import curation, registry

    notes = [
        n
        for f in registry.files(ROOT / "registry")
        if (n := ((registry.load_one(f).source.notes_curator or "") if registry.load_one(f).source else ""))
    ]
    assert len(notes) > 150
    bad = [n[:60] for n in notes if not curation.split_is_lossless(n, curation.episodes(n))]
    assert not bad, f"{len(bad)} notes do not survive the split: {bad[:2]}"


def test_a_note_that_refers_to_its_own_order_is_not_reordered():
    """73 notes say "the above" or "see below". Moving a paragraph under one of
    those makes the record say something false, which is worse than showing it
    oldest-first."""
    from assaywatch import curation

    # Two or more consecutive capitalised words, which is how every curator has
    # marked an episode; a single acronym mid-sentence must not split the text.
    safe = "OLIGO FOUND 2026-10-20, a thing happened here. SOURCE RESOLVED 2026-10-23, it was settled."
    eps, reordered = curation.newest_first(safe)
    assert reordered and eps[0].date == "2026-10-23"

    risky = safe + " LATER CONFIRMED 2026-10-25, the above still holds."
    eps, reordered = curation.newest_first(risky)
    assert not reordered, "a note containing a back-reference must keep its original order"


def test_a_taxid_link_says_what_the_taxon_is_on_hover():
    """A scope list can run to hundreds of bare numbers. Without a title the
    generic "opens in a new tab" tooltip appeared instead, which beside 300
    taxids is worse than none. Names come from the same taxonomy cache the
    scope test walks for ancestry, so the tooltip and the scoping decision
    agree about what a taxid is."""
    names = site_render._taxon_names()
    assert len(names) > 20000, f"the taxonomy cache yielded only {len(names)} names"
    link = site_render._taxid_link(10368)
    assert 'title="Human betaherpesvirus 6"' in link
    assert "wwwtax.cgi?id=10368" in link
    assert ">10368</a>" in link
    # A taxid the cache does not know still links, just without a tooltip.
    unknown = site_render._taxid_link(999999999)
    assert "title=" not in unknown and "999999999" in unknown


@pytest.mark.skipif(not DATA.exists(), reason="website/data/run.json is not present")
def test_most_taxids_on_the_site_resolve_to_a_name():
    """98.7% when this was written. A large fall means the cache has drifted
    away from the registry and most tooltips have quietly gone missing."""
    data = json.loads(DATA.read_text())
    names = site_render._taxon_names()
    need = {str(a["taxid"]) for a in data["assays"] if a["taxid"]}
    need |= {str(t) for a in data["assays"] for t in a["scope_taxids"]}
    need |= {str(t) for a in data["assays"] for t in a["exclusivity_taxids"]}
    have = len(need & set(names))
    assert have / len(need) > 0.95, f"only {have} of {len(need)} taxids resolve to a name"


def test_a_long_scope_list_is_folded_and_a_short_one_is_not():
    """Scope lists run from 1 taxid to 1,494, and 18 of the 39 scoped assays
    carry more than ten. Printed inline the long ones bury the sentence that
    explains what the list is for, so past the threshold the page states the
    count and offers the list."""
    short = _page(scope_taxids=[10368, 10373, 10395])
    md = site_render._scope_block(short)
    assert "aw-taxids" not in md, "three taxids should be inline"
    assert ">10368</a>" in md

    long = _page(scope_taxids=list(range(10000, 10000 + 42)))
    md = site_render._scope_block(long)
    assert "**42 taxa**" in md, "the count must be stated"
    assert "Show all 42 taxids" in md
    assert "aw-taxids" in md
    # Folded, not dropped: every taxid is still on the page.
    assert md.count("wwwtax.cgi?id=") == 42

    # Exactly at the threshold stays inline.
    edge = _page(scope_taxids=list(range(10000, 10000 + site_render.SCOPE_INLINE_MAX)))
    assert "aw-taxids" not in site_render._scope_block(edge)


@pytest.mark.skipif(not DATA.exists(), reason="website/data/run.json is not present")
def test_every_scoped_assay_has_a_downloadable_taxid_list_that_matches_the_page():
    """The download is a real file, not a scripted one, so it works without
    JavaScript and can be fetched with curl. It must hold exactly the taxids the
    page shows -- a list that diverged from the entry would be worse than none,
    because it looks authoritative and is what someone would paste into NCBI."""
    data = json.loads(DATA.read_text())
    scoped = [a for a in data["assays"] if a["scope_taxids"]]
    assert scoped, "no assay declares a scope"
    for a in scoped:
        f = ROOT / "website" / "assays" / f"{a['assay_id']}.scope.txt"
        assert f.exists(), f"{a['assay_id']} declares a scope but has no taxid file"
        got = [int(line) for line in f.read_text().split()]
        assert got == a["scope_taxids"], f"{a['assay_id']}: file and entry disagree"
    # Bare integers, one per line: no header, no names, nothing to strip.
    sample = (ROOT / "website" / "assays" / f"{scoped[0]['assay_id']}.scope.txt").read_text()
    assert all(line.strip().isdigit() for line in sample.splitlines() if line.strip())


def test_an_unscoped_assay_has_no_taxid_file_to_download():
    """179 of the 218 entries declare no scope. An empty file offered for
    download would imply the scope is empty rather than unrestricted."""
    data = json.loads(DATA.read_text()) if DATA.exists() else {"assays": []}
    for a in data["assays"]:
        if not a["scope_taxids"]:
            f = ROOT / "website" / "assays" / f"{a['assay_id']}.scope.txt"
            assert not f.exists(), f"{a['assay_id']} has no scope but has a taxid file"


def test_every_assay_page_offers_a_way_to_correct_it():
    """The registry's weakest claims are the ones no author has seen -- an oligo
    read from a figure, an amplicon measured rather than published, a scope
    inferred -- and the person most able to correct one is whoever designed the
    assay. The route has to be on the page where the error is noticed."""
    md = site_render.assay_page(_page(assay_id="SOME_assay"), "2026-10-31")
    assert "## Corrections" in md
    assert "issues/new?title=SOME_assay" in md, "the issue must be pre-filled with the entry"
    assert "edit/main/registry/SOME_assay.yaml" in md, "the edit link must open this entry"
    assert "blob/main/registry/SOME_assay.yaml" in md
    # The pre-filled body carries the run, so a report says which run it is about.
    assert "2026-10-31" in md


def test_a_withheld_assay_also_offers_the_correction_routes():
    """Those 19 are the entries most likely to be wrong, and their pages return
    early."""
    md = site_render.assay_page(
        _page(assay_id="SOME_assay", withheld_reasons=[["not_screenable", "RPA"]]), "2026-10-31"
    )
    assert "## Corrections" in md and "issues/new?title=SOME_assay" in md


def test_the_mismatch_track_labels_each_row_with_the_oligo_name():
    """The row labels read "forward" and "reverse", which does not match the
    track to the paper's own table or to a tube. The names are in the registry
    for all 496 oligos.

    This test exists because the wiring silently did not happen: the call site
    kept passing no names, the figure kept rendering without them, and nothing
    failed."""
    page = _page(
        assay_id="X",
        oligos={"forward": "ACGTACGTAC"},
        positions=[
            dict(
                oligo="forward",
                pos_3prime=2,
                base="A",
                n_mismatch=5,
                detected_with=0,
                evaluable_with=5,
                detected_without=50,
                evaluable_without=50,
                substitutions=[],
                in_3prime_zone=True,
            )
        ],
    )
    assert "aw-track-name" not in site_svg.mismatch_track(page), "no names given, none drawn"
    svg = site_svg.mismatch_track(page, {"forward": "senseA"})
    assert "aw-track-name" in svg and ">senseA<" in svg


@pytest.mark.skipif(not DATA.exists(), reason="website/data/run.json is not present")
def test_rendered_assay_pages_actually_carry_the_oligo_names():
    """End to end, on the committed pages: the unit test above passed while the
    renderer was still calling the figure without names."""
    data = json.loads(DATA.read_text())
    with_track = [
        a for a in data["assays"] if a["positions"] and site_render._oligo_names().get(a["assay_id"])
    ]
    assert with_track, "no assay has both a mismatch track and named oligos"
    page = ROOT / "website" / "assays" / f"{with_track[0]['assay_id']}.md"
    assert "aw-track-name" in page.read_text(), f"{page.name} draws no oligo names"


def test_no_chart_mark_uses_the_question_mark_cursor():
    """`cursor: help` draws a question mark, which reads as "this needs
    explaining" rather than "this has a tooltip". The marks are not clickable
    either, so `pointer` would be a lie; the default arrow is correct and the
    native tooltip still appears."""
    css = (ROOT / "website" / "stylesheets" / "extra.css").read_text()
    assert "cursor: help" not in css
    assert ".aw-track g { cursor: default; }" in css


def test_the_lineage_bar_has_an_outlined_track_and_a_threshold_tick():
    """Without an edge on the track a 100% bar and a 70% bar look identical --
    there is nothing to read the fill against. The tick marks the threshold the
    table exists to judge against, so a row can be read without crossing to the
    interval column."""
    css = (ROOT / "website" / "stylesheets" / "extra.css").read_text()
    assert "border: 1px solid var(--aw-grid)" in css.split(".aw-bar {")[1].split("}")[0]
    assert ".aw-bar::after" in css, "the threshold tick is missing"

    page = _page(
        threshold=0.9,
        lineages=[
            {"lineage": "A", "taxid": 1, "evaluable": 36, "detected": 36, "share": 1.0, "ci": [0.904, 1.0]},
            {"lineage": "B", "taxid": 2, "evaluable": 40, "detected": 20, "share": 0.5, "ci": [0.35, 0.65]},
        ],
    )
    md = "\n".join(site_render._lineage_block(page))
    assert "--aw-thr:90%" in md, "the tick position must come from the assay's own threshold"
    assert "width:100.0%" in md and "width:50.0%" in md


def test_every_top_level_nav_section_renders_a_real_link():
    """The masthead iterates the nav two levels deep, because Pipeline is itself
    a group: an overview plus twelve stage pages. A section has no url of its
    own, so emitting `child.url` produced an empty link to "." and dropped
    Pipeline out of the navigation entirely -- the page was published and
    reachable, and nothing on the site pointed at it."""
    built = ROOT / ".site" / "index.html"
    if not built.exists():
        pytest.skip("site is not built")
    html = built.read_text()
    nav = re.search(r'<nav class="sections".*?</nav>', html, re.S)
    assert nav, "the masthead has no section nav"
    links = re.findall(r'<a href="([^"]*)"[^>]*>\s*([^<]*)</a>', nav.group(0))
    hrefs = {h for h, _ in links}
    titles = {tt.strip() for _, tt in links}
    assert "pipeline/" in hrefs, f"Pipeline is missing from the nav: {sorted(hrefs)}"
    assert "." not in hrefs, "a section rendered as an empty link"
    assert all(titles), "a nav link has no text"


def test_the_readme_points_at_every_prose_page_on_the_site():
    """Readers arrive from the README. A page the README never mentions is one
    most of them will not find."""
    readme = (ROOT / "README.md").read_text()
    for page in ("scoring", "pipeline", "validation", "limitations", "scoping", "glossary", "assays"):
        assert f"github.io/assaywatch/{page}/" in readme, f"the README does not link to /{page}/"


def test_the_deploy_triggers_on_everything_the_published_page_depends_on():
    """The site is rendered from more than `website/`. The theme is its entire
    appearance, and the registry supplies paper titles, oligo names, curator
    notes and taxon names at render time.

    `theme/**` was missing from the trigger, so a template change built locally,
    passed CI and never deployed: the published page silently kept the previous
    template. Nothing reported a stale deploy, because no deploy had run."""
    wf = (ROOT / ".github" / "workflows" / "site.yml").read_text()
    for path in (
        "website/**",
        "theme/**",
        "mkdocs.yml",
        "registry/**",
        "assaywatch/palette.py",
        "GLOSSARY.md",
    ):
        assert path in wf, f"{path} is not in the site workflow's path filter"
