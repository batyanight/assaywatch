"""Turn `website/data/run.json` into the site's generated pages.

    python -m assaywatch.site_render --data website/data --out website

Pure formatting: it reads the extracted JSON and writes Markdown. It never opens
the calls table, the registry or the archives, so the generated pages are a
function of one committed file and can be rebuilt by anyone who clones the
repository without the 9 GB of archives.

WHAT IT REFUSES TO DO. An assay whose entry carries a blocking `needs_review`
flag gets a page with its reasons and NO status, NO verdict arithmetic and NO
charts drawn in a verdict color -- the same withholding `report.py` applies.
The site is the most-read surface in the project and the assays it withholds a
status for are exactly the ones a confident-looking dashboard would mislead
about.
"""

from __future__ import annotations

import argparse
import html
import json
import re
from functools import lru_cache
from pathlib import Path
from typing import Any
from urllib.parse import quote

from assaywatch import curation, glossary_links, palette, site_svg

ROOT = Path(__file__).resolve().parents[1]

#: What each status means, in one line, shown on every page that prints one.
#: Lifted from `README.md`'s "The drift call" so the two cannot drift apart.
STATUS_MEANING = {
    "declining": "below the threshold, and measurably lower than a baseline that previously exceeded it",
    "low coverage": "below the threshold without a measurable decline"
    " \u2014 applied beyond its design range, or never covering this taxon",
    "watch": "below the threshold with an interval that still spans it",
    "stable": "the recent interval does not fall below the threshold",
    "insufficient data": "too few evaluable records to support an estimate; reported, never flagged",
    "no recent data": "no deposits within the window",
    "no data": "no archive at all",
}


def _pct(x: float | None) -> str:
    return "—" if x is None else f"{100 * x:.1f}%"


def _breakable(assay_id: str) -> str:
    """An entry id that wraps at its underscores rather than mid-word.

    `<wbr>` is an opportunity, not a break: the id stays one word for selection
    and copying, and only splits where a human would split it. Without this the
    browser breaks `ADENOVIRUS_dsDNA_Hexon_gene` after any character, which is
    what made the first column unreadable.
    """
    return assay_id.replace("_", "_<wbr>")


def _chip(status: str) -> str:
    """A status as a colored chip that also says the word.

    Both, always: the palette's one accepted color-vision warning is licensed
    only where a second encoding carries the same information.
    """
    if not status:
        return '<span class="aw-chip aw-chip-none">status withheld</span>'
    slug = status.replace(" ", "-")
    return f'<span class="aw-chip aw-chip-{slug}">{status}</span>'


@lru_cache(maxsize=1)
def _papers() -> dict[str, dict[str, Any]]:
    """The committed Crossref cache, keyed by DOI.

    Read here rather than carried in `run.json` because it is already a
    committed file, so the page stays a function of what is in the repository
    and no re-extraction is needed to pick up a newly resolved title. It covers
    85 of the 120 cited DOIs, so everything that reads it must have a fallback.
    """
    path = ROOT / "docs" / "papers-index.cache.json"
    try:
        raw = json.loads(path.read_text())
    except (OSError, ValueError):
        return {}
    # Keyed in lower case, because `scripts/papers_index.py` lower-cases every
    # DOI it indexes while the registry stores them as the publisher prints
    # them. A case-sensitive lookup matched 85 of the 120 cited DOIs and missed
    # every one containing a capital -- `10.1016/S0166-0934(01)00306-8` and the
    # rest -- which read as "Crossref has no title for these" when the titles
    # were in the file all along. A DOI is case-insensitive by specification, so
    # the lookup must be too.
    return {str(k).lower(): v for k, v in raw.items() if isinstance(v, dict)}


@lru_cache(maxsize=1)
def _taxon_names() -> dict[str, str]:
    """{taxid: scientific name}, from the committed taxonomy cache.

    The same file the scope test walks for ancestry, so the names shown are the
    ones the scoping decision was made with. It covers 98.7% of the 5,346
    taxids this site links to; a scope list can run to hundreds of taxids and a
    bare number tells a reader nothing.
    """
    import gzip

    path = ROOT / "docs" / "taxonomy-cache.json.gz"
    try:
        with gzip.open(path, "rt") as fh:
            return json.load(fh).get("name", {})
    except (OSError, ValueError):
        return {}


def _taxid_link(taxid: int | str, label: str | None = None) -> str:
    """A taxid as a link that says what it is on hover.

    The title is the taxon name and rank. Without one the generic "opens in a
    new tab" tooltip appeared instead, which beside a list of 300 numbers is
    worse than no tooltip at all.
    """
    tid = str(taxid)
    name = _taxon_names().get(tid, "")
    title = f' title="{html.escape(name, quote=True)}"' if name else ""
    text = label or tid
    return f'<a href="https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id={tid}"{title}>{text}</a>'


@lru_cache(maxsize=1)
def _oligo_names() -> dict[str, dict[str, str]]:
    """{assay id: {role: the name the paper gave this oligo}}.

    All 496 oligos in the registry carry one -- `senseA`, `APVF`, `LT51` -- and
    it is how a reader matches a row here against the table in the paper, or
    against a tube in a freezer. Read from the registry at build time, like the
    curator notes, rather than carried in `run.json`.
    """
    from assaywatch import registry

    out: dict[str, dict[str, str]] = {}
    for f in registry.files(ROOT / "registry"):
        a = registry.load_one(f)
        names = {
            role: getattr(a.oligos, role).name
            for role in ("forward", "reverse", "probe")
            if getattr(a.oligos, role, None) is not None and getattr(a.oligos, role).name
        }
        if names:
            out[a.id] = names
    return out


@lru_cache(maxsize=1)
def _curation_notes() -> dict[str, str]:
    """{assay id: the entry's curator note}, read from the registry at build time.

    Like `_papers`, this reads a committed file rather than carrying the text in
    `run.json`, so a note edited today appears on the next render without
    re-extracting from the archives.

    203 of 218 entries have one, median 2,400 characters. They are the record of
    what was checked and what could not be: which oligo failed to match the
    paper it is cited to, where a sequence actually came from, why an amplicon
    was corrected. For several entries the note is the only place a reader can
    learn that the stored oligos are not the cited paper's.
    """
    from assaywatch import registry

    out: dict[str, str] = {}
    for f in registry.files(ROOT / "registry"):
        a = registry.load_one(f)
        note = (a.source.notes_curator if a.source else None) or ""
        if note.strip():
            out[a.id] = note.strip()
    return out


def _curation_block(a: dict[str, Any]) -> list[str]:
    """The curator note: its own opening sentence in the open, the rest folded
    into one paragraph per dated episode, newest first.

    The notes run to 2,400 characters on average, which is too much to put in
    front of every reader and too important to drop. They already solve the
    summary problem themselves: each opens with a self-contained headline --
    78 of the 203 with an explicit capitalised one such as "OLIGO SOURCE FOUND
    2026-10-23, and it is not the cited paper" -- so the short version is that
    sentence, quoted exactly.

    NOTHING IS PARAPHRASED AND NOTHING IS DROPPED. A curator note records what
    was checked; a summary written here would be a second-hand account of
    evidence, able to lose the one specific that matters. `curation.episodes`
    partitions the text and the split is asserted lossless before it is used.

    Order: newest first where that is safe, which is 42 of the 203. The rest
    are shown as written, because they either carry an undated episode or refer
    to their own layout -- 73 notes say "the above" or "see below", and moving a
    paragraph under one of those makes the record wrong. Which order is in use
    is stated, so a reader is never left guessing.
    """
    note = _curation_notes().get(a["assay_id"], "")
    if not note:
        return []
    eps, reordered = curation.newest_first(note)
    flat = " ".join(note.split())
    lead = eps[0].text if reordered else flat
    if not reordered:
        # The first sentence, ending at a full stop or semicolon. A candidate
        # shorter than 25 characters is extended, so "et al." or "Fig. 1" does
        # not cut it short.
        for m in re.finditer(r"(?<=[.;])\s", flat):
            if m.start() >= 25:
                lead = flat[: m.start() + 1]
                break

    out = ["", "## Curation record\n", f"{html.escape(lead, quote=False)}\n"]
    if len(eps) == 1 and eps[0].text == lead:
        return out

    order = "newest first" if reordered else "in the order the curator wrote it, oldest first"
    body = "".join(
        f"<p>{f'<b>{e.date}</b> ' if e.date else ''}{html.escape(e.text, quote=False)}</p>" for e in eps
    )
    out.append(
        f'<details class="aw-curation"><summary>The full note, as the curator wrote it '
        f"\u00b7 {order}</summary>{body}</details>"
    )
    return out


def _paper(a: dict[str, Any]) -> tuple[str, str, str, str]:
    """(title, authors) for an assay's cited paper, each "" when unknown.

    Titles arrive from Crossref with the publisher's own line breaks and runs of
    spaces in them, which land in the middle of a heading if they are not
    collapsed.
    """
    rec = _papers().get((a["doi"] or "").lower(), {})
    title = " ".join((rec.get("title") or "").split())
    names = rec.get("authors") or []
    n = rec.get("n_authors") or len(names)
    if not names:
        authors = ""
    elif n == 1:
        authors = names[0]
    elif n == 2:
        authors = f"{names[0]} and {names[1]}"
    elif n <= 4:
        authors = ", ".join(names[:-1]) + f" and {names[-1]}"
    else:
        # Past four, naming them all buries the title it sits under.
        authors = f"{names[0]} and {n - 1} others"
    journal = " ".join((rec.get("journal") or "").split())
    year = rec.get("year") or a["design_year"] or ""
    return title, authors, journal, str(year)


def assay_page(page: dict[str, Any], run_date: str) -> str:
    out: list[str] = []
    a = page
    # A withholding reason beats a status, wherever the status came from. The
    # extractor already blanks it, so this is belt and braces -- but it is the
    # one invariant on this page that would do real damage if it broke, and it
    # costs a line to make it true here rather than assumed.
    status = "" if a["withheld_reasons"] else a["status"]
    title, authors, journal, year = _paper(a)

    # The paper leads, because that is what the entry rests on and what a reader
    # checks it against. Where Crossref has no title for the DOI -- 35 of the 120
    # cited papers -- the assay's own descriptive name takes the heading, which is
    # always present, rather than leaving a page with no title.
    out.append(f"# {title or a['name']}\n")
    byline = " \u00b7 ".join(x for x in (authors, journal, year) if x)
    if byline:
        out.append(f'<p class="aw-byline">{byline}</p>\n')
    if a["doi"]:
        out.append(f'<p class="aw-doi"><a href="https://doi.org/{a["doi"]}">doi:{a["doi"]}</a></p>\n')
    if a["reference"]:
        # The stored reference verbatim. Folded away when the heading already
        # carries the title, because otherwise the page opens by saying the
        # same sentence twice; shown plainly when it does not, since then it
        # is the only description of the paper on the page.
        if title:
            out.append(f'??? quote "Full citation"\n    {a["reference"]}\n')
        else:
            out.append(f'<p class="aw-citation">{a["reference"]}</p>\n')

    out.append(f'<p class="aw-assay-line">{_chip(status)} <span class="aw-id">{a["assay_id"]}</span></p>\n')
    if title:
        # The assay's own name says what the entry is; the heading now says what
        # the paper is, and those are different sentences.
        out.append(f"**{a['name']}**\n")

    # What this assay is, before any number about it.
    rows = [
        (
            "Target",
            f"{a['taxon']}"
            + (f" ({_taxid_link(a['taxid'], label='taxid ' + str(a['taxid']))})" if a["taxid"] else ""),
        ),
        ("Gene", a["gene"] or "—"),
        ("Chemistry", a["chemistry"]),
        ("Amplicon", f"{a['amplicon_bp']} bp" if a["amplicon_bp"] else "—"),
        ("Registry status", a["entry_status"]),
    ]
    out.append("| | |\n|---|---|")
    out += [f"| {k} | {v} |" for k, v in rows]
    out.append("")

    # Oligos, 5'->3', as stored.
    if a["oligos"]:
        names = _oligo_names().get(a["assay_id"], {})
        out.append("## Oligos\n")
        out.append("| role | name | sequence (5'→3') | length |\n|---|---|---|---|")
        for role, seq in a["oligos"].items():
            # The name the paper gave it, which is how a reader matches this row
            # to the paper's own table or to a tube in a freezer.
            out.append(f"| {role} | {names.get(role, '—')} | `{seq}` | {len(seq)} nt |")
        out.append("")

    if a["withheld_reasons"]:
        out.append(_withheld_block(a))
        out.append(_scope_block(a))
        out += _curation_block(a)
        out += _contribute_block(a, run_date)
        return "\n".join(out) + "\n"

    out.append(_verdict_block(a, run_date))
    out.append(_charts_block(a))
    out.append(_scope_block(a))
    out.append(_denominator_block(a))
    out += _curation_block(a)
    out += _contribute_block(a, run_date)
    return "\n".join(out) + "\n"


def _withheld_block(a: dict[str, Any]) -> str:
    """Why this assay has no status. Not a caveat on a verdict: instead of one."""
    lines = [
        '!!! warning "No status is reported for this assay"',
        "",
        "    A property of this entry would render a predicted-detection figure",
        "    misleading: a chemistry this scoring does not model, or a readout other",
        "    than amplification. The sequences were screened and still appear in the",
        "    tables below that do not depend on a verdict. The verdict is withheld",
        "    deliberately, rather than presented with a caveat attached.",
        "",
    ]
    for flag, note in a["withheld_reasons"]:
        lines.append(f"    - **`{flag}`** — {note}" if note else f"    - **`{flag}`**")
    return "\n".join(lines) + "\n"


def _verdict_block(a: dict[str, Any], run_date: str) -> str:
    meaning = STATUS_MEANING.get(a["status"], "")
    rec_share = a["recent_detected"] / a["recent_evaluable"] if a["recent_evaluable"] else None
    base_share = a["baseline_detected"] / a["baseline_evaluable"] if a["baseline_evaluable"] else None
    lines = [
        "## Verdict\n",
        f"**{a['status']}** — {meaning}\n",
        "Every value the call was derived from, permitting manual recomputation:\n",
        "| | detected | evaluable | share | 95% interval |",
        "|---|---|---|---|---|",
        f"| recent window ({a['window_months']} months, from {a['recent_from']}) "
        f"| {a['recent_detected']:,} | {a['recent_evaluable']:,} | {_pct(rec_share)} "
        f"| {_pct(a['recent_ci'][0])} – {_pct(a['recent_ci'][1])} |",
        f"| baseline (everything earlier) | {a['baseline_detected']:,} "
        f"| {a['baseline_evaluable']:,} | {_pct(base_share)} "
        f"| {_pct(a['baseline_ci'][0])} – {_pct(a['baseline_ci'][1])} |",
        "",
        f"Change from baseline, Newcombe interval: "
        f"**{_pct(a['change_ci'][0])} to {_pct(a['change_ci'][1])}**. "
        f"Threshold: **{_pct(a['threshold'])}**.\n",
    ]
    if a["note"]:
        lines.append(f"*{a['note']}*\n")
    if a["trend"]:
        lines.append(
            f"Trend across deposit years: {a['trend']}. Reported for context; it is "
            "not an input to the verdict.\n"
        )
    lines.append(
        f"From the {run_date} run. A status indicates where to direct attention rather "
        "than establishing a result; [known limitations](../limitations.md) reports how "
        "often these calls are correct.\n"
    )
    return "\n".join(lines)


def _charts_block(a: dict[str, Any]) -> str:
    lines = ["## Predicted detection by deposit year\n"]
    lines += [
        "The proportion of deposited sequence this assay is predicted to detect, by year of",
        "deposit. The shaded band marks the recent window and the dashed line the threshold.",
        "Marker size encodes the number of records behind each point, since 100% of three",
        "records and 100% of three thousand are not equivalent claims.\n",
        site_svg.year_chart(a),
        "",
        "## Mismatch distribution\n",
        "Each oligonucleotide drawn base by base, 5\u2032 to 3\u2032. The shaded region is the one the",
        "scoring penalizes more heavily, and it differs by oligonucleotide: for a primer the",
        "3\u2032 window, where a mismatch sits in the polymerase\u2019s catalytic site; for a probe the",
        "central third, since a hydrolysis probe is never extended \u2014 its 3\u2032 end carries the",
        "quencher and it is cleaved by exonuclease activity, so what matters is duplex",
        "stability. Bar height is the proportion of records differing at that position; bar",
        "color is the consequence, measured as the fall in detection between records",
        "differing there and those not:",
        "",
        '<span class="aw-key"><span class="aw-key-swatch aw-bar-strong"></span> detection falls '
        "by 25 points or more</span>",
        '<span class="aw-key"><span class="aw-key-swatch aw-bar-mid"></span> falls 10 to 25</span>',
        '<span class="aw-key"><span class="aw-key-swatch aw-bar-weak"></span> little or no effect '
        "\u2014 variation the assay tolerates</span>",
        "",
        "Counts are available on hover. A tall gray bar indicates a tolerated polymorphism; a",
        "short red bar indicates a position of consequence.\n",
        site_svg.mismatch_track(a, _oligo_names().get(a["assay_id"]))
        or '<p class="aw-empty">No position carried a mismatch in enough records to report.</p>',
    ]
    lines += _lineage_block(a)
    return "\n".join(lines)


def _lineage_block(a: dict[str, Any]) -> list[str]:
    """Detection per lineage, as a table rather than a plot.

    A forest plot was the first attempt and it was wrong for this data: **70 of
    the 125 assays with lineage data have exactly one lineage**, so the usual
    page carried an axis, a grid, a threshold line and one dot -- all of the
    furniture of a comparison with nothing to compare. Where there really are
    several, a table with a bar in the share column is denser than dots on an
    axis and needs no axis to read.

    With one lineage there is nothing to say that the pooled figure above has
    not already said, so this says that in a sentence and draws nothing.
    """
    lins = a.get("lineages") or []
    if not lins:
        return []
    out = ["", "## By lineage\n"]
    if len(lins) == 1:
        item = lins[0]
        out += [
            f"Every evaluable record is one lineage, **{item['lineage']}** "
            f"({item['detected']:,} of {item['evaluable']:,} detected, "
            f"{100 * item['share']:.1f}%, 95% interval {100 * item['ci'][0]:.1f}"
            f"\u2013{100 * item['ci'][1]:.1f}%), so splitting by lineage adds nothing to the "
            "figure above. The split matters where an assay spans several clades: a pooled "
            "percentage can look healthy while one lineage fails completely.\n",
        ]
        return out

    out += [
        "Published misses are nearly always specific to one lineage, and a clade that is 5%",
        "of deposits can be 100% of the cases in one region \u2014 so a pooled percentage can look",
        "healthy while one clade fails completely. Worst first. Lineages with too few records",
        f"to say anything are left out, and a lineage whose whole interval sits below "
        f"{100 * a['threshold']:.0f}% is marked.\n",
        '<table class="aw-lineage">',
        "<thead><tr><th>lineage</th><th>detected</th>"
        '<th class="num">records</th><th class="num">share</th>'
        '<th class="num">95% interval</th></tr></thead>',
        "<tbody>",
    ]
    for item in sorted(lins, key=lambda x: x["share"]):
        below = item["ci"][1] < a["threshold"]
        cls = "aw-lin-fail" if below else "aw-lin-ok"
        pct = 100 * item["share"]
        flag = (
            ' <span class="aw-lin-flag" title="the whole interval is below the threshold">below</span>'
            if below
            else ""
        )
        out.append(
            f'<tr class="{cls}"><td>{item["lineage"]}{flag}</td>'
            f'<td class="aw-barcell"><span class="aw-bar" '
            f'style="--aw-thr:{100 * a["threshold"]:.0f}%" '
            f'title="{pct:.1f}% detected; the tick marks the {100 * a["threshold"]:.0f}% threshold">'
            f'<span class="aw-bar-fill" style="width:{pct:.1f}%"></span></span></td>'
            f'<td class="num">{item["evaluable"]:,}</td>'
            f'<td class="num">{pct:.1f}%</td>'
            f'<td class="num">{100 * item["ci"][0]:.1f}\u2013{100 * item["ci"][1]:.1f}%</td></tr>'
        )
    out += ["</tbody>", "</table>", ""]
    return out


#: Scope lists longer than this are folded. Ten fits on two lines at the
#: reading measure; the longest list in the registry is 1,494 taxids.
SCOPE_INLINE_MAX = 10


def _scope_block(a: dict[str, Any]) -> str:
    lines = ["\n## Scope\n"]
    if a["scope_taxids"]:
        taxids = a["scope_taxids"]
        rule = (
            "A record counts toward the denominator when its taxid, or any ancestor, is in "
            "that set. Records outside it are screened and reported but kept out of the "
            "statistics."
        )
        # A scope list runs from one taxid to 1,494, and 18 of the 39 scoped
        # assays carry more than ten. Printed inline, the long ones bury the
        # sentence that explains what the list is for.
        ids = ", ".join(_taxid_link(t) for t in taxids)
        download = (
            f'<a class="aw-download" href="{a["assay_id"]}.scope.txt" download>'
            f"Download {len(taxids):,} taxids as a text file</a>"
        )
        if len(taxids) <= SCOPE_INLINE_MAX:
            lines.append(f"This entry declares **`scope_taxids`**: {ids}. {rule}\n")
            lines.append(f"{download}\n")
        else:
            lines.append(f"This entry declares **`scope_taxids`**: **{len(taxids):,} taxa**. {rule}\n")
            lines.append(
                f'<details class="aw-taxids"><summary>Show all {len(taxids):,} taxids'
                f"</summary><p>{ids}</p>{download}</details>\n"
            )
    else:
        lines.append(
            "This entry declares no scope restriction, so every record retrieved for "
            "its target taxid counts toward the denominator. Where an assay was designed "
            "for a narrower range than its taxid covers, that presents as low coverage "
            "rather than drift; see [scope and retrieval](../scoping.md).\n"
        )
    if a["out_of_scope"]:
        lines.append(f"{a['out_of_scope']:,} screened records fell outside the declared scope.\n")
    if a["exclusivity_taxids"]:
        lines.append(
            f"The paper claims this assay does **not** amplify {len(a['exclusivity_taxids'])} "
            "other taxa. Those are retrieved on purpose and reported as predicted "
            "cross-reactivity; they are never scored.\n"
        )
    if a["query"]:
        lines.append(f"Retrieval query:\n\n```\n{a['query']}\n```\n")
        lines.append(
            "A retrieval query is a claim about the population against which the assay "
            "is evaluated, and it can cease to be accurate without producing an error; "
            "see [scope and retrieval](../scoping.md).\n"
        )
    if a["title_requires"]:
        lines.append(
            f"Records are further restricted to those whose description names "
            f"{' or '.join('`' + t + '`' for t in a['title_requires'])}, because the subtype is "
            "in the record title and Entrez will not query it.\n"
        )
    if a["review_flags"]:
        lines.append("Disclosures on this entry: " + ", ".join(f"`{f}`" for f in a["review_flags"]) + ".\n")
    return "\n".join(lines)


REPO = "https://github.com/batyanight/assaywatch"


def _contribute_block(a: dict[str, Any], run_date: str) -> list[str]:
    """How to correct this entry, on the page where the error would be noticed.

    Three routes, in increasing order of effort, because the right one depends
    on what the reader has: a note needs only a sentence, an edit needs the
    change, a pull request needs the whole thing. The issue and the edit links
    are pre-filled with the assay id and the run date, so a report arrives
    saying which entry and which run it is about without the reporter having to
    look either up.

    This matters more here than on a normal site. The registry's weakest claims
    are the ones no author has seen -- an oligo transcribed from a figure, an
    amplicon measured rather than published, a scope inferred -- and the person
    most able to correct them is the one who designed the assay.
    """
    aid = a["assay_id"]
    entry = f"registry/{aid}.yaml"
    title = quote(f"{aid}: ")
    body = quote(
        f"Entry: {aid}\n"
        f"Page: https://batyanight.github.io/assaywatch/assays/{aid}/\n"
        f"Run: {run_date}\n\n"
        "What is wrong, and what it should be:\n\n"
    )
    return [
        "",
        "## Corrections\n",
        "If this entry misrepresents the assay, that is a defect and a report is",
        "welcome — particularly from the group that designed it. The sequences,",
        "the product size and the scope are all curated from the paper and can be",
        "wrong.\n",
        '<div class="aw-contribute" markdown="0">',
        f'<a class="aw-cta" href="{REPO}/issues/new?title={title}&body={body}">'
        "<b>Leave a note</b><span>Opens a GitHub issue, pre-filled with this entry "
        "and run. A sentence is enough.</span></a>",
        f'<a class="aw-cta" href="{REPO}/edit/main/{entry}">'
        "<b>Edit the entry</b><span>Opens this assay's YAML in GitHub's editor. Saving "
        "offers to open a pull request for you.</span></a>",
        f'<a class="aw-cta" href="{REPO}/blob/main/{entry}">'
        "<b>Read the entry</b><span>The file behind this page, with every field and "
        "the curator's note.</span></a>",
        "</div>",
        "",
        f"Contributing an assay is documented in [CONTRIBUTING.md]({REPO}/blob/main/CONTRIBUTING.md).\n",
    ]


def _denominator_block(a: dict[str, Any]) -> str:
    """How much of what was screened reached the statistics.

    On the page because the project's first known limitation is that the
    denominator is drift-correlated, and an assay-level share says nothing about
    how much was dropped to compute it.
    """
    if not a["screened_rows"]:
        return ""
    reached = a["recent_evaluable"] + a["baseline_evaluable"]
    pct = 100 * reached / a["screened_rows"] if a["screened_rows"] else 0
    lines = [
        "\n## Records reaching the statistics\n",
        f"{a['screened_rows']:,} records were screened for this assay and **{reached:,} "
        f"({pct:.0f}%)** were evaluable, meaning both primers landed in the right orientation "
        f"and size range. {a['no_amplicon_rows']:,} produced no amplicon at all.\n",
        "This is material because a record with one diverged primer is scored as a "
        "failure while a record with both diverged is excluded from the denominator "
        "entirely. The resulting bias is known, measured, and may not be correctable; "
        "see [known limitations](../limitations.md).\n",
    ]
    if a["exclusions"]:
        lines.append("| why a record was not evaluable | records |\n|---|---|")
        lines += [f"| `{k}` | {v:,} |" for k, v in a["exclusions"][:8]]
        lines.append("")
    return "\n".join(lines)


#: Statuses the list does not show: too few evaluable records to support an
#: estimate, and the assays whose entry makes a verdict misleading. 49 of 217.
#:
#: `no recent data` is deliberately NOT here. It is a statement about the
#: taxon's deposition rather than about the assay, and after the influenza
#: episode -- four assays that read "no recent records" because the retrieval
#: query had gone stale, not because nothing was deposited -- it is the status
#: most worth leaving in a reader's way.
#:
#: The excluded assays' PAGES are still generated and still say why. For the
#: withheld ones that reason -- a chemistry the scoring does not model, a
#: readout that is not amplification -- is the only published record of the
#: limitation. What is removed is their place in the table, not the disclosure.
UNLISTED_STATUSES = frozenset({"insufficient data", ""})


def index_page(data: dict[str, Any]) -> str:
    """The filterable list of assays, excluding those with no usable status."""
    every = data["assays"]
    assays = [a for a in every if a["status"] not in UNLISTED_STATUSES]
    unlisted = len(every) - len(assays)
    counts: dict[str, int] = {}
    for a in assays:
        counts[a["status"]] = counts.get(a["status"], 0) + 1
    order = ["declining", "low coverage", "watch", "no recent data", "stable"]
    summary = " · ".join(f"**{counts[s]}** {s}" for s in order if s in counts)

    lines = [
        "---",
        "hide:",
        "  - toc",
        "---\n",
        "# Every assay\n",
        f"{len(assays)} assays, screened on {data['run_date']}. {summary}.\n",
        "A status indicates where to direct attention; it is not a result. Select a "
        "column heading to sort, or filter by typing.\n",
        f"A further {unlisted} assays are not listed: too few evaluable records to "
        "support an estimate, or a property of the entry that would make a verdict "
        "misleading. Each still has a page stating which.\n",
        '<input class="aw-filter" type="text"'
        ' placeholder="filter by organism, gene, assay or chemistry\u2026"'
        ' aria-label="filter assays">\n',
        '<table class="aw-assays">',
        "<thead><tr>"
        '<th scope="col">assay</th>'
        '<th scope="col">status</th>'
        '<th scope="col">gene</th>'
        '<th scope="col">chemistry</th>'
        '<th scope="col" class="num">detected</th>'
        '<th scope="col" class="num">records</th>'
        "</tr></thead>",
        "<tbody>",
    ]
    for a in sorted(assays, key=lambda x: (x["taxon"].lower(), x["assay_id"])):
        share = a["recent_detected"] / a["recent_evaluable"] if a["recent_evaluable"] else None
        status = a["status"] or "withheld"
        slug = status.replace(" ", "-")
        # The organism leads and the entry id sits under it in small type. The id
        # alone used to be the whole cell, and a 44-character underscored string in
        # a narrow column wraps one character per line -- unreadable, and it pushed
        # every other column out of shape.
        lines.append(
            "<tr>"
            f'<td class="aw-assay"><a href="{a["assay_id"]}/">'
            f'<span class="aw-taxon">{a["taxon"] or a["assay_id"]}</span>'
            f'<span class="aw-id">{_breakable(a["assay_id"])}</span></a></td>'
            f'<td><span class="aw-chip aw-chip-{slug}">{status}</span></td>'
            f"<td>{a['gene']}</td><td>{a['chemistry']}</td>"
            f'<td class="num" data-sort="{share if share is not None else -1}">{_pct(share)}</td>'
            f'<td class="num" data-sort="{a["recent_evaluable"]}">{a["recent_evaluable"]:,}</td>'
            "</tr>"
        )
    lines += ["</tbody>", "</table>", ""]
    return "\n".join(lines)


def render(data: dict[str, Any], out: Path) -> int:
    from assaywatch.site import SCHEMA

    if data.get("schema") != SCHEMA:
        raise SystemExit(f"run.json is schema {data.get('schema')}, this renderer expects {SCHEMA}")
    assays_dir = out / "assays"
    assays_dir.mkdir(parents=True, exist_ok=True)
    for page in data["assays"]:
        (assays_dir / f"{page['assay_id']}.md").write_text(assay_page(page, data["run_date"]))
        # A real file rather than a scripted download: it works with
        # JavaScript off, can be fetched with curl, and can be cited. Bare
        # taxids one per line, which is what pastes into NCBI's batch entry
        # and reads with `while read`; the names are on the page.
        if page["scope_taxids"]:
            (assays_dir / f"{page['assay_id']}.scope.txt").write_text(
                "\n".join(str(t) for t in page["scope_taxids"]) + "\n"
            )
    (assays_dir / "index.md").write_text(index_page(data))
    (out / "stylesheets").mkdir(parents=True, exist_ok=True)
    (out / "stylesheets" / "palette.css").write_text(palette.css_variables() + _CHIP_CSS)
    _glossary(out)
    return len(data["assays"])


def _glossary(out: Path) -> None:
    """The site's glossary IS the repository's `GLOSSARY.md`, copied at build time.

    Not rewritten for the web and not summarized: the project's rule is that the
    glossary is the vocabulary used in code, comments and commit messages, so a
    second edited copy would be a second vocabulary. Only a short header is added,
    saying where it came from and that it is generated.
    """
    src = ROOT / "GLOSSARY.md"
    body = src.read_text()
    header = (
        "<!-- Generated by assaywatch.site_render from GLOSSARY.md. Edit that file. -->\n"
        '!!! info "Reproduced verbatim from the repository\'s `GLOSSARY.md`"\n'
        "    These are the terms used in the source code, comments and commit\n"
        "    messages, rather than a separate vocabulary written for this site.\n"
        "    Edits to\n"
        "    [`GLOSSARY.md`](https://github.com/batyanight/assaywatch/blob/main/GLOSSARY.md)\n"
        "    propagate here.\n\n"
    )
    # The file opens with its own `# Glossary` heading, which becomes the page title.
    first, _, rest = body.partition("\n")
    # The one thing the web copy adds: each term gets an anchor, and the first
    # mention of another term inside a definition becomes a link to it. The text
    # is untouched -- see assaywatch.glossary_links for why that restraint
    # matters when `call`, `site` and `probe` are themselves defined terms.
    linked, n, ambiguous = glossary_links.crosslink(rest.lstrip())
    note = (
        "    Terms are cross-linked: the first mention of another defined term in a\n"
        f"    definition links to it ({n} links).\n"
    )
    if ambiguous:
        # Stated on the page rather than only in the code, so a reader who
        # notices that one word is never a link can find out why.
        note += (
            "    "
            + ", ".join(f"`{a}`" for a in ambiguous)
            + (" is" if len(ambiguous) == 1 else " are")
            + " defined by more than one entry and so\n"
            "    deliberately not linked.\n"
        )
    note += "\n"
    (out / "glossary.md").write_text(f"{first}\n\n{header[:-1]}{note}{linked}")


_CHIP_CSS = """
.aw-chip { display: inline-block; padding: 0.08rem 0.5rem; border-radius: 0.8rem;
  font-size: 0.72rem; font-weight: 600; letter-spacing: 0.01em; white-space: nowrap;
  max-width: 100%; overflow: hidden; text-overflow: ellipsis; vertical-align: top;
  color: var(--aw-chip-ink); }
/* Amber and the lifted dark olive need near-black text, the rest white; the
   choice is measured per color in assaywatch/palette.py. */
.aw-chip-declining { color: var(--aw-chip-ink-declining); }
.aw-chip-low-coverage { color: var(--aw-chip-ink-low-coverage); }
.aw-chip-watch { color: var(--aw-chip-ink-watch); }
.aw-chip-stable { color: var(--aw-chip-ink-stable); }
.aw-chip-declining { background: var(--aw-chip-declining); }
.aw-chip-low-coverage { background: var(--aw-chip-low-coverage); }
.aw-chip-watch { background: var(--aw-chip-watch); }
.aw-chip-stable { background: var(--aw-chip-stable); }
.aw-chip-insufficient-data { background: var(--aw-chip-insufficient-data); }
.aw-chip-no-recent-data { background: var(--aw-chip-no-recent-data); }
.aw-chip-no-data, .aw-chip-withheld, .aw-chip-none { background: var(--aw-ink-muted); }
.aw-filter { width: 100%; padding: 0.5rem 0.7rem; margin: 0.6rem 0 1rem;
  border: 1px solid var(--aw-grid); border-radius: 0.3rem; background: transparent;
  color: var(--aw-ink); font-size: 0.92rem; }
table.aw-assays { width: 100%; font-size: 0.86rem; }
table.aw-assays th { cursor: pointer; user-select: none; white-space: nowrap; }
table.aw-assays td:first-child { font-family: var(--md-code-font-family); font-size: 0.8rem; }
p.aw-empty { color: var(--aw-ink-muted); font-style: italic; }
"""


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", type=Path, default=ROOT / "website" / "data")
    ap.add_argument("--out", type=Path, default=ROOT / "website")
    args = ap.parse_args(argv)
    data = json.loads((args.data / "run.json").read_text())
    n = render(data, args.out)
    print(f"{n} assay pages into {args.out / 'assays'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
