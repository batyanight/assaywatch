"""Turn `website/data/run.json` into the site's generated pages.

    python -m assaywatch.site_render --data website/data --out website

Pure formatting: it reads the extracted JSON and writes Markdown. It never opens
the calls table, the registry or the archives, so the generated pages are a
function of one committed file and can be rebuilt by anyone who clones the
repository without the 9 GB of archives.

WHAT IT REFUSES TO DO. An assay whose entry carries a blocking `needs_review`
flag gets a page with its reasons and NO status, NO verdict arithmetic and NO
charts drawn in a verdict colour -- the same withholding `report.py` applies.
The site is the most-read surface in the project and the assays it withholds a
status for are exactly the ones a confident-looking dashboard would mislead
about.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from assaywatch import palette, site_svg

ROOT = Path(__file__).resolve().parents[1]

#: What each status means, in one line, shown on every page that prints one.
#: Lifted from `README.md`'s "The drift call" so the two cannot drift apart.
STATUS_MEANING = {
    "declining": "below the threshold, measurably lower than a baseline that once cleared it",
    "low coverage": "below the threshold, but not measurably lower than before"
    " — an assay used beyond its design, or one that never covered this taxon",
    "watch": "below the threshold with an interval that still covers it",
    "stable": "the recent interval does not fall below the threshold",
    "insufficient data": "too few evaluable records to say anything; reported, never flagged",
    "no recent data": "nothing was deposited in the window",
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
    """A status as a coloured chip that also says the word.

    Both, always: the palette's one accepted colour-vision warning is licensed
    only where a second encoding carries the same information.
    """
    if not status:
        return '<span class="aw-chip aw-chip-none">status withheld</span>'
    slug = status.replace(" ", "-")
    return f'<span class="aw-chip aw-chip-{slug}">{status}</span>'


def assay_page(page: dict[str, Any], run_date: str) -> str:
    out: list[str] = []
    a = page
    # A withholding reason beats a status, wherever the status came from. The
    # extractor already blanks it, so this is belt and braces -- but it is the
    # one invariant on this page that would do real damage if it broke, and it
    # costs a line to make it true here rather than assumed.
    status = "" if a["withheld_reasons"] else a["status"]
    out.append(f"# {a['assay_id']}\n")
    out.append(f"{_chip(status)}\n")
    out.append(f"**{a['name']}**\n")

    # The header block: what this assay is, before any number about it.
    rows = [
        (
            "Target",
            f"{a['taxon']}"
            + (
                f" ([taxid {a['taxid']}](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id={a['taxid']}))"
                if a["taxid"]
                else ""
            ),
        ),
        ("Gene", a["gene"] or "—"),
        ("Chemistry", a["chemistry"]),
        ("Amplicon", f"{a['amplicon_bp']} bp" if a["amplicon_bp"] else "—"),
        ("Designed", str(a["design_year"]) if a["design_year"] else "—"),
        ("Paper", f"[{a['doi']}](https://doi.org/{a['doi']})" if a["doi"] else "—"),
        ("Registry status", a["entry_status"]),
    ]
    out.append("| | |\n|---|---|")
    out += [f"| {k} | {v} |" for k, v in rows]
    out.append("")

    if a["reference"]:
        out.append(f'!!! quote "The paper"\n    {a["reference"]}\n')

    # Oligos, 5'->3', as stored.
    if a["oligos"]:
        out.append("## Oligos\n")
        out.append("| role | sequence (5'→3') | length |\n|---|---|---|")
        for role, seq in a["oligos"].items():
            out.append(f"| {role} | `{seq}` | {len(seq)} nt |")
        out.append("")

    if a["withheld_reasons"]:
        out.append(_withheld_block(a))
        out.append(_scope_block(a))
        return "\n".join(out) + "\n"

    out.append(_verdict_block(a, run_date))
    out.append(_charts_block(a))
    out.append(_scope_block(a))
    out.append(_denominator_block(a))
    return "\n".join(out) + "\n"


def _withheld_block(a: dict[str, Any]) -> str:
    """Why this assay has no status. Not a caveat on a verdict: instead of one."""
    lines = [
        '!!! warning "No status is reported for this assay"',
        "",
        "    Something about this assay means a predicted-detection figure would",
        "    mislead you — a chemistry this scoring does not model, or a readout that",
        "    is not simply amplification. The sequences were still screened and still",
        "    appear in the tables below that do not depend on a verdict. What is",
        "    missing is the verdict, and it is missing on purpose rather than shown",
        "    with a warning attached.",
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
        "## The verdict, and the numbers behind it\n",
        f"**{a['status']}** — {meaning}\n",
        "Everything the call was made from, so you can check it yourself:\n",
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
            f"Trend across deposit years: {a['trend']}. Shown for context; it does not feed the verdict.\n"
        )
    lines.append(
        f"From the {run_date} run. A status tells you where to look rather than what is "
        "true — [what the output is worth](../what-the-output-is-worth.md) explains how "
        "often these calls are right.\n"
    )
    return "\n".join(lines)


def _charts_block(a: dict[str, Any]) -> str:
    lines = ["## Detection by deposit year\n"]
    lines += [
        "How much of the deposited sequence this assay is predicted to detect, by the year",
        "each record was deposited. The shaded band is the recent window; the dashed line is",
        "the threshold. Marker size is the number of records behind each point, because 100%",
        "of three records and 100% of three thousand are not the same claim.\n",
        site_svg.year_chart(a),
        "",
        "## Where the mismatches sit\n",
        "Each oligo drawn base by base, 5\u2032 to 3\u2032, with the 3\u2032 window shaded \u2014 a mismatch",
        "there is the one that fails a reaction. Bar height is the share of records differing",
        "at that position; bar colour is what that costs, measured as the fall in detection",
        "between records that differ there and records that do not:",
        "",
        '<span class="aw-key"><span class="aw-key-swatch aw-bar-strong"></span> detection falls '
        "25 points or more</span>",
        '<span class="aw-key"><span class="aw-key-swatch aw-bar-mid"></span> falls 10 to 25</span>',
        '<span class="aw-key"><span class="aw-key-swatch aw-bar-weak"></span> little or no cost '
        "\u2014 variation the assay tolerates</span>",
        "",
        "Hover any bar for the counts. A tall grey bar is a polymorphism; a short red one is a",
        "design problem.\n",
        site_svg.mismatch_track(a)
        or '<p class="aw-empty">No position carried a mismatch in enough records to report.</p>',
    ]
    if a["lineages"]:
        lines += [
            "",
            "## By lineage\n",
            "A single pooled percentage hides the clade you may actually care about: published",
            "misses are nearly always specific to one lineage, and a clade that is 5% of deposits",
            "can be 100% of the cases in one region. Lineages with too few records to say anything",
            "are left out.\n",
            site_svg.lineage_chart(a),
        ]
    return "\n".join(lines)


def _scope_block(a: dict[str, Any]) -> str:
    lines = ["\n## Scope — what this assay is judged against\n"]
    if a["scope_taxids"]:
        ids = ", ".join(
            f"[{t}](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id={t})"
            for t in a["scope_taxids"]
        )
        lines.append(
            f"This entry declares **`scope_taxids`**: {ids}. A record counts toward the "
            "denominator when its taxid, or any ancestor, is in that set. Records outside it "
            "are screened and reported but kept out of the statistics.\n"
        )
    else:
        lines.append(
            "This entry declares no `scope_taxids`, so every record retrieved for its target "
            "taxid counts toward the denominator. Where an assay was designed for a narrower "
            "set than its taxid covers, that reads as low coverage rather than as drift — "
            "see [scoping](../scoping.md).\n"
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
            "A retrieval query is a scientific claim about the population the assay is being "
            "judged against, and it can go stale silently — see [scoping](../scoping.md).\n"
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
        "\n## What reached the statistics\n",
        f"{a['screened_rows']:,} records were screened for this assay and **{reached:,} "
        f"({pct:.0f}%)** were evaluable, meaning both primers landed in the right orientation "
        f"and size range. {a['no_amplicon_rows']:,} produced no amplicon at all.\n",
        "This matters because a record with one drifted primer counts as a failure while a "
        "record with both drifted leaves the denominator entirely. The bias is known, measured "
        "and not obviously fixable — see [known limitations](../what-the-output-is-worth.md).\n",
    ]
    if a["exclusions"]:
        lines.append("| why a record was not evaluable | records |\n|---|---|")
        lines += [f"| `{k}` | {v:,} |" for k, v in a["exclusions"][:8]]
        lines.append("")
    return "\n".join(lines)


def index_page(data: dict[str, Any]) -> str:
    """The filterable list of every assay."""
    assays = data["assays"]
    counts: dict[str, int] = {}
    for a in assays:
        key = a["status"] or "status withheld"
        counts[key] = counts.get(key, 0) + 1
    order = [
        "declining",
        "low coverage",
        "watch",
        "insufficient data",
        "no recent data",
        "no data",
        "stable",
        "status withheld",
    ]
    summary = " · ".join(f"**{counts[s]}** {s}" for s in order if s in counts)

    lines = [
        "---",
        "hide:",
        "  - toc",
        "---\n",
        "# Every assay\n",
        f"{len(assays)} assays, screened on {data['run_date']}. {summary}.\n",
        "A status tells you where to look, not what is true. Click a column to sort, or type to filter.\n",
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
    (assays_dir / "index.md").write_text(index_page(data))
    (out / "stylesheets").mkdir(parents=True, exist_ok=True)
    (out / "stylesheets" / "palette.css").write_text(palette.css_variables() + _CHIP_CSS)
    _glossary(out)
    return len(data["assays"])


def _glossary(out: Path) -> None:
    """The site's glossary IS the repository's `GLOSSARY.md`, copied at build time.

    Not rewritten for the web and not summarised: the project's rule is that the
    glossary is the vocabulary used in code, comments and commit messages, so a
    second edited copy would be a second vocabulary. Only a short header is added,
    saying where it came from and that it is generated.
    """
    src = ROOT / "GLOSSARY.md"
    body = src.read_text()
    header = (
        "<!-- Generated by assaywatch.site_render from GLOSSARY.md. Edit that file. -->\n"
        '!!! info "This page is the repository\'s `GLOSSARY.md`, verbatim"\n'
        "    These are the words used in the code, the comments and the commit\n"
        "    messages, not a separate set written for the website. Edit\n"
        "    [`GLOSSARY.md`](https://github.com/batyanight/assaywatch/blob/main/GLOSSARY.md)\n"
        "    and this page follows.\n\n"
    )
    # The file opens with its own `# Glossary` heading, which becomes the page title.
    first, _, rest = body.partition("\n")
    (out / "glossary.md").write_text(f"{first}\n\n{header}{rest.lstrip()}")


_CHIP_CSS = """
.aw-chip { display: inline-block; padding: 0.08rem 0.5rem; border-radius: 0.8rem;
  font-size: 0.72rem; font-weight: 600; letter-spacing: 0.01em; white-space: nowrap;
  max-width: 100%; overflow: hidden; text-overflow: ellipsis; vertical-align: top;
  color: var(--aw-chip-ink); }
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
