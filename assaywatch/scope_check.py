"""The release scope verification as one command: which assays look unjudgeable because of
what a query or scope can see, rather than what was deposited.

    assaywatch scope-check --calls results/<date>/calls.tsv.gz --out results/<date>/scope-check.tsv

One row per assay and flag. NO FLAG IS A VERDICT: each is a reason to read that assay, by the
tests in CONTRIBUTING.md under "Releasing". Two of them over-fire on purpose, on gene queries
under genome-depositing taxa and on bacteria with assembly retrieval (2026-11-01), so a clean
run says little and a flagged one says where to look.

Free-text name search (test 3) stays by hand: `"<name>"[Organism]` resolves to the same taxid
and returns 0 by construction, and a free-text hit needs reading.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import re
import sys
from collections.abc import Callable, Iterable
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

from assaywatch import registry
from assaywatch.accession import strip_version
from assaywatch.taxonomy import Taxonomy, taxonomy_from_config

#: Archive more than this share behind what its query now returns, in unique accessions.
ARCHIVE_BEHIND = 0.10
#: Taxid holding more than this many times what the query sees in the window.
TAXID_OVER_QUERY = 3
_NAMES_TAXID = re.compile(r"txid\d+", re.I)
COLUMNS = ("assay_id", "status", "flag", "detail")


@dataclass(frozen=True)
class Counts:
    """What NCBI and the archive say about one assay. `None` is "could not ask", never zero."""

    query_all: int | None
    query_window: int | None
    taxid_window: int | None
    scope_window: int | None
    archive_accessions: int
    newest_created: str | None


def flags_for(c: Counts, *, query: str | None, window_from: str, scoped: bool) -> list[tuple[str, str]]:
    """Every flag these counts raise, as (flag, detail)."""
    out: list[tuple[str, str]] = []
    if c.query_window == 0 and c.taxid_window:
        out.append(("query_sees_nothing", f"query 0 in the window, taxid {c.taxid_window:,}"))
    elif c.query_window and c.taxid_window and c.taxid_window > TAXID_OVER_QUERY * c.query_window:
        out.append(("taxid_over_query", f"query {c.query_window:,} in the window, taxid {c.taxid_window:,}"))
    if c.query_all and c.archive_accessions < (1 - ARCHIVE_BEHIND) * c.query_all:
        out.append(("archive_behind_query", f"archive {c.archive_accessions:,}, query {c.query_all:,}"))
    if c.newest_created is None or c.newest_created < window_from:
        out.append(
            ("archive_stale", f"newest deposit {c.newest_created or 'none'}, window from {window_from}")
        )
    if query and _NAMES_TAXID.search(query):
        out.append(("query_names_taxid", "NCBI can stop assigning it, the influenza failure"))
    if scoped and c.scope_window == 0:
        out.append(("scope_empty", "no in-scope record in the window"))
    return out


def scope_lineage_flags(scope: Iterable[int], taxonomy: Taxonomy | None) -> list[tuple[str, str]]:
    """A scope taxid that has gained a species parent: NCBI files new records at the parent, and
    `taxonomy.within` drops them, since a parent doesn't sit inside its child (`Orf virus` 10258)."""
    if taxonomy is None:
        return []
    wanted = {taxonomy.canonical(t) for t in scope}
    out = []
    for taxid in sorted(wanted):
        parent = taxonomy.parent.get(taxid)
        if parent and parent not in wanted and taxonomy.rank.get(parent) == "species":
            name = taxonomy.name.get(parent, "")
            out.append(("scope_taxid_gained_parent", f"{taxid} sits under species {parent} {name}".rstrip()))
    return out


def archive_profile(archive: Path) -> tuple[int, str | None]:
    """(unique accessions, newest `created`), since an incremental archive repeats records."""
    seen: set[str] = set()
    newest: str | None = None
    for meta in sorted(archive.rglob("*.meta.tsv.gz")):
        with gzip.open(meta, "rt") as fh:
            header = (fh.readline() or "").rstrip("\n").split("\t")
            if "accession" not in header or "created" not in header:
                continue
            ai, ci = header.index("accession"), header.index("created")
            for line in fh:
                parts = line.rstrip("\n").split("\t")
                if len(parts) > max(ai, ci):
                    seen.add(strip_version(parts[ai]))
                    newest = max(newest or "", parts[ci]) or None
    return len(seen), newest


def scope_query(scope: Iterable[int]) -> str:
    return "(" + " OR ".join(f"txid{t}[Organism:exp]" for t in sorted(set(scope))) + ")"


def check_assay(
    assay: Any,
    count: Callable[[str, str | None], int | None],
    retrieved: Path,
    cfg: dict[str, Any],
    taxonomy: Taxonomy | None,
    window_from: str,
) -> list[tuple[str, str]]:
    """`count(query, from_date)` is an esearch count, None when it can't ask."""
    from assaywatch.retrieve import build_query

    target = assay.target
    query = build_query(target.taxid, cfg, target.query)
    scope = list(target.scope_taxids or [])
    n, newest = archive_profile(registry.archive_dir(assay, retrieved))
    counts = Counts(
        query_all=count(query, None),
        query_window=count(query, window_from),
        taxid_window=count(f"txid{target.taxid}[Organism:exp]", window_from),
        scope_window=count(scope_query(scope), window_from) if scope else None,
        archive_accessions=n,
        newest_created=newest,
    )
    return flags_for(
        counts, query=target.query, window_from=window_from, scoped=bool(scope)
    ) + scope_lineage_flags(scope, taxonomy)


def window_start(today: date, months: int) -> str:
    """`YYYY-MM-01` the given months before `today`, as `created` dates sort."""
    total = today.year * 12 + today.month - 1 - months
    return f"{total // 12:04d}-{total % 12 + 1:02d}-01"


def statuses(calls: Path | None, registry_dir: Path, retrieved: Path, cfg: dict[str, Any]) -> dict[str, str]:
    """Each assay's status in that run; `report.build` is the verdict path, so it's asked rather
    than re-derived. Takes about 4.5 GB and 5 minutes, so it's only done when `--calls` is given."""
    if calls is None:
        return {}
    from assaywatch import report

    _, _, drifts, _ = report.build(calls, registry_dir, retrieved, cfg, run_date=calls.parent.name)
    return {aid: str(getattr(d, "status", "")) for aid, d in drifts.items()}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--registry", type=Path, default=Path("registry"))
    ap.add_argument(
        "--calls", type=Path, default=None, help="a run's calls table, to print each assay's status"
    )
    ap.add_argument("--retrieved", type=Path, default=Path("data/retrieved"))
    ap.add_argument("--config", type=Path, default=None)
    ap.add_argument("--email", default=None)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args(argv)

    from assaywatch.credentials import contact_email, ncbi_api_key
    from assaywatch.retrieve import esearch, http_transport
    from assaywatch.score import load_config

    cfg = load_config(args.config)
    transport = http_transport(args.email or contact_email() or "", ncbi_api_key() or None)
    today = date.today()
    months = int((cfg.get("drift") or {}).get("recent_window_months", 24))
    window_from = window_start(today, months)

    def count(query: str, since: str | None) -> int | None:
        start = (since or "1900-01-01").replace("-", "/")
        try:
            return int(
                esearch(transport, query, start, datetype="pdat", until=today.strftime("%Y/%m/%d"))["count"]
            )
        except Exception as exc:  # noqa: BLE001 - any transport failure is "could not ask"
            print(f"could not count: {exc}", file=sys.stderr)
            return None

    taxonomy = taxonomy_from_config(cfg)
    status = statuses(args.calls, args.registry, args.retrieved, cfg)
    rows = 0
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, "w", newline="") as fh:
        writer = csv.writer(fh, delimiter="\t", lineterminator="\n")
        writer.writerow(COLUMNS)
        for path in registry.files(args.registry):
            assay = registry.load_one(path)
            for flag, detail in check_assay(assay, count, args.retrieved, cfg, taxonomy, window_from):
                writer.writerow((assay.id, status.get(assay.id, ""), flag, detail))
                rows += 1
    print(f"{args.out}: {rows:,} flags; none is a verdict", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
