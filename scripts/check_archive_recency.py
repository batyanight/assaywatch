#!/usr/bin/env python3
"""Which assays' archives have stopped being fed, and which of those look like a broken
retrieval query rather than a quiet taxon. Reads only; never writes, never fetches.

    python scripts/check_archive_recency.py
    python scripts/check_archive_recency.py --months 24 --verbose

WHY THIS EXISTS. On 2026-10-30 four live influenza entries turned out to have archives
that stopped years earlier -- the H5 Tsukamoto group's newest deposit was 2021 and H7's
was 2020 -- because NCBI had stopped assigning the subtype taxids their retrieval queries
named. Nothing complained. The report said "no evaluable records deposited since Oct
2021" beside each assay, which is TRUE and reads as a fact about the taxon: nothing
recent was deposited. It was a fact about the query: we could not see what was deposited.
So the output looked correct while four assays sat unjudgeable, and the entries' own
`retrieval_scope_incomplete` flags filed the symptom as a known limitation.

It was found by hand, by noticing that one verdict was absurd for seasonal influenza and
then reading a deposit-year distribution out of an archive. This script is that reading,
for every assay at once.

WHAT THIS IS WORTH, MEASURED RATHER THAN HOPED. It is a worklist, not a detector. The
sibling heuristic below -- stale while another group of the same taxid is current -- was
written expecting it to isolate broken queries. Run against the registry on 2026-10-30 it
returned four candidates and **all four were fine**, cleared by one `esearch` each:

    group                          archive holds   query returns now
    562/q780c1da66e  E. coli LT              122                  62
    77643/q78359e501c  MTB helicase           25                  25
    548689/qf10852ef3e  EEHV5                 20                  20
    548689/qc0acbc84e8  EEHV6                  6                   6

Three hold exactly what their query can return, so those queries are not blind; they are
narrow gene queries under taxa that deposit whole genomes, which will always look stale
beside a broad sibling. The E. coli group holds MORE than its query now returns, which is
the incremental archive keeping records since revised or withdrawn.

So the sibling signal is weak, and worse, it would not have isolated the influenza case
either: that case appeared alongside these four and not above them. **A count probe does
not save it.** The old H3 archive held 44,627 records against a query that returned
44,633 -- they agreed, because the query was executing perfectly and returning a
population that had stopped growing. No comparison of a query against itself can see an
annotation practice change at the far end.

What the script therefore buys is a SHORT LIST: 13 groups of 134 worth a human's
attention, with the numbers needed to clear each one quickly. That is how the influenza
case was found by hand, and it is the honest claim.

TO CLEAR A CANDIDATE, one command per group: ask how many records its query returns now
and compare with the archive's count printed here. Agreement means the archive holds
everything the query can see, so retrieval is not missing anything and the quiet belongs
to the taxon.

    esearch -db nuccore -query 'txid<TAXID>[Organism:exp] AND (<the entry's target.query>)' \\
      | xtract -pattern ENTREZ_DIRECT -element Count

There is deliberately no flag that does this. It needs the network, it is four calls on
today's registry, and -- as above -- it would have cleared the influenza group too. A
switch that looks like a verdict and cannot deliver one is worse than a documented
command.
"""

from __future__ import annotations

import argparse
import gzip
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from assaywatch import registry  # noqa: E402

# Default staleness floor. Not a scoring number and not tuned: 18 months is simply long
# enough that a seasonal pathogen with any surveillance behind it would have deposited
# something, and short enough to have caught the influenza case (which was 4-5 years
# stale) with room to spare. Pass --months to argue with it.
DEFAULT_MONTHS = 18


def newest_deposit(group_dir: Path) -> tuple[str | None, int]:
    """(newest `created` date in this group's metadata sidecars, record count).

    Reads each sidecar's own header, because the schema gained `taxid` and `is_patent`
    partway through and older files do not carry them -- 18 of the 19 influenza matrix
    sidecars predate the change. A file without a `created` column contributes its record
    count and no date.
    """
    newest, n = None, 0
    for meta in sorted(group_dir.glob("*.meta.tsv.gz")):
        try:
            with gzip.open(meta, "rt") as fh:
                header = fh.readline().rstrip("\n").split("\t")
                col = header.index("created") if "created" in header else None
                for line in fh:
                    n += 1
                    if col is None:
                        continue
                    row = line.rstrip("\n").split("\t")
                    if col < len(row) and row[col]:
                        if newest is None or row[col] > newest:
                            newest = row[col]
        except (OSError, EOFError) as exc:
            # Narrow on purpose, so no BLE001 suppression is needed: a truncated or
            # unreadable sidecar is a finding about that file, not a reason to abandon the
            # other 133 groups, and anything other than an I/O fault should still raise.
            print(f"  ! unreadable: {meta} ({exc})", file=sys.stderr)
    return newest, n


def months_between(then: str, now: date) -> int:
    """Whole months from an ISO-ish `YYYY/MM/DD` or `YYYY-MM-DD` date to `now`."""
    parts = then.replace("/", "-").split("-")
    y, m = int(parts[0]), int(parts[1]) if len(parts) > 1 else 1
    return (now.year - y) * 12 + (now.month - m)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--registry", type=Path, default=ROOT / "registry")
    ap.add_argument("--retrieved", type=Path, default=ROOT / "data" / "retrieved")
    ap.add_argument(
        "--months", type=int, default=DEFAULT_MONTHS, help=f"staleness floor (default {DEFAULT_MONTHS})"
    )
    ap.add_argument("--verbose", action="store_true", help="one line per group, stale or not")
    args = ap.parse_args(argv)
    today = date.today()

    # group -> the assays that asked for it, and the newest deposit it holds
    groups: dict[tuple[str, str], list[str]] = defaultdict(list)
    for f in registry.files(args.registry):
        a = registry.load_one(f)
        if a.target.taxid is None:
            continue
        groups[(str(a.target.taxid), registry.group_slug(a.target.query))].append(a.id)

    seen: dict[tuple[str, str], tuple[str | None, int]] = {}
    for key in groups:
        d = args.retrieved / key[0] / key[1]
        seen[key] = newest_deposit(d) if d.is_dir() else (None, 0)

    newest_for_taxid: dict[str, str] = {}
    for (taxid, _), (newest, _n) in seen.items():
        if newest and (taxid not in newest_for_taxid or newest > newest_for_taxid[taxid]):
            newest_for_taxid[taxid] = newest

    sibling_gap, quiet, never_fetched = [], [], []
    for key, (newest, n) in sorted(seen.items()):
        taxid, slug = key
        if n == 0:
            never_fetched.append((taxid, slug, groups[key]))
            continue
        if newest is None:
            continue
        age = months_between(newest, today)
        if args.verbose:
            print(f"  {taxid}/{slug}  newest {newest}  {n:>7} records  {age:>3} months  {groups[key][0]}")
        if age < args.months:
            continue
        best = newest_for_taxid.get(taxid)
        if best and months_between(best, today) < args.months:
            sibling_gap.append((taxid, slug, newest, best, n, groups[key]))
        else:
            quiet.append((taxid, slug, newest, n, groups[key]))

    if sibling_gap:
        print(
            f"\nSTALE WHILE A SIBLING IS CURRENT ({len(sibling_gap)}): worth one esearch each. "
            "On 2026-10-30 all four candidates here were fine -- a narrow gene query under a "
            "well-deposited taxon always looks stale beside a broad one. See the module docstring."
        )
        for taxid, slug, newest, best, n, aids in sibling_gap:
            print(f"  {taxid}/{slug}  newest {newest} ({n} records), but another group of {taxid} has {best}")
            for aid in aids:
                print(f"      {aid}")
    if quiet:
        print(f"\nQUIET, NO SIBLING TO COMPARE ({len(quiet)}): a reading, not a finding.")
        for taxid, slug, newest, n, aids in quiet:
            print(f"  {taxid}/{slug}  newest {newest} ({n} records)  {', '.join(aids)}")
    if never_fetched:
        print(f"\nNEVER FETCHED ({len(never_fetched)}): expected before an assay's first run.")
        for taxid, slug, aids in never_fetched:
            print(f"  {taxid}/{slug}  {', '.join(aids)}")
    if not (sibling_gap or quiet or never_fetched):
        print(f"every archive holds a deposit from the last {args.months} months")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
