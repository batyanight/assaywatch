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

from assaywatch import palette, site, site_render

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "website" / "data" / "run.json"


_BOKEH_ID = re.compile(r'(data-root-id="|id="|const docs_json = |"id":\s*")[A-Za-z0-9_-]{4,}')


def _normalise(md: str) -> str:
    """Markdown with Bokeh's per-render identifiers flattened."""
    md = re.sub(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", "UUID", md)
    return re.sub(r"\bp\d{3,}\b", "PID", md)


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
    # No verdict, no arithmetic, no charts drawn in a verdict colour.
    assert "The verdict" not in md
    assert "Detection by deposit year" not in md
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


def test_bokeh_version_matches_the_script_tag_the_site_loads():
    """The charts are embedded with `components()`, which emits no loader: BokehJS
    comes from the CDN tag in mkdocs.yml. If the two versions drift, every chart on
    218 pages silently fails to render, and nothing else would catch it."""
    from assaywatch import site_charts

    mk = (ROOT / "mkdocs.yml").read_text()
    assert f"bokeh-{site_charts.BOKEH_VERSION}.min.js" in mk, (
        f"mkdocs.yml does not load BokehJS {site_charts.BOKEH_VERSION}"
    )


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
        # Bokeh mints a fresh UUID and element id on every render, so the two
        # texts never compare equal byte for byte. Normalising them is not a
        # weakening of the test: what it is for is catching markdown rendered
        # from an older extract, and every number, label and sentence still has
        # to match exactly.
        assert _normalise(on_disk.read_text()) == _normalise(
            site_render.assay_page(page, data["run_date"])
        ), f"{on_disk.name} is stale; re-run `python -m assaywatch.site_render`"


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
        assert "The expensive stage" in html, "stage prose is missing from the built page"
