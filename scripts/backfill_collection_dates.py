"""Fetch `/collection_date` for every nuccore accession a run screened.

Why this exists: the drift window runs on **deposit date**, the date GenBank took
the record, because that is the only date `esummary` carries. **Collection date**,
when the sample came out of the animal, lives in the flatfile's `source` feature and
nowhere else, so the collection-year lens could only cover the 13 assembly-backed
assays (`docs/journal/2026-10-30-collection-year-lens.md`). This backfills the rest.

Two things make a million-record flatfile fetch affordable. `efetch` takes the whole
batch in one POST, and `seq_start=1&seq_stop=1` asks for a one-base slice, which
strips the sequence but keeps the `source` qualifiers: measured at 53 records/sec and
2.2 KB/record, against ~270 KB/record for whole flatfiles.

Read-only with respect to the pipeline. It writes one gitignored sidecar under
`data/collection-dates/` and touches nothing `scripts/weekly_run.sh` guards, so it is
safe to leave running across a scheduled run.

Resumable, because six hours is long enough to lose: every accession the fetch has
SETTLED is in the sidecar, including the ones that carry no date and the ones NCBI no
longer serves, so a restart asks only for what is genuinely outstanding instead of
re-fetching three quarters of a million records to learn the same nothing.

    python scripts/backfill_collection_dates.py                  # the newest run's calls table
    python scripts/backfill_collection_dates.py --limit 2000     # a probe
"""

from __future__ import annotations

import argparse
import gzip
import re
import sys
import time
from collections.abc import Callable
from pathlib import Path

from assaywatch import ncbi

HERE = Path(__file__).resolve().parents[1]
SIDECAR = HERE / "data" / "collection-dates" / "collection-dates.tsv"
COLUMNS = ("accession", "collection_date", "status")

# A flatfile record ends at `//`; VERSION carries accession.version, which is how the
# calls table spells a record id. LOCUS drops the version and so cannot be joined on.
_VERSION = re.compile(r"^VERSION\s+(\S+)", re.M)
_COLLECTED = re.compile(r'/collection_date="([^"]*)"')


def accessions_of_run(results: Path) -> list[str]:
    """Every distinct nuccore record id in a run's calls table, assemblies excluded.

    An assembly accession (`GCA_`/`GCF_`) already carries its collection date from the
    Datasets metadata the retrieval wrote, so re-fetching it would be work for nothing.
    """
    seen: dict[str, None] = {}
    with gzip.open(results / "calls.tsv.gz", "rt") as fh:
        header = next(fh).rstrip("\n").split("\t")
        col = header.index("record_id")
        for line in fh:
            acc = line.split("\t", col + 1)[col]
            if not acc.startswith(("GCA_", "GCF_")):
                seen.setdefault(acc, None)
    return list(seen)


def newest_run(root: Path) -> Path:
    runs = sorted(p for p in (root / "results").glob("*") if (p / "calls.tsv.gz").exists())
    if not runs:
        raise SystemExit("no run under results/ has a calls.tsv.gz to read accessions from")
    return runs[-1]


def settled(sidecar: Path) -> set[str]:
    """Accessions already answered, so a restart does not ask twice."""
    if not sidecar.exists():
        return set()
    with sidecar.open() as fh:
        first = next(fh, "")
        rows = fh if first.startswith(COLUMNS[0]) else [first, *fh]
        return {ln.split("\t", 1)[0] for ln in rows if ln.strip()}


def parse(flatfile: str) -> dict[str, str]:
    """`{accession.version: collection_date}`, the date empty when the record has none.

    Keyed on every record the page returned, present or absent date, because "NCBI
    served this record and it carries no collection date" is an answer and has to be
    recorded as one.
    """
    out: dict[str, str] = {}
    for block in flatfile.split("\n//"):
        m = _VERSION.search(block)
        if not m:
            continue
        d = _COLLECTED.search(block)
        out[m.group(1)] = d.group(1) if d else ""
    return out


def _efetch(call: ncbi.Transport, ids: list[str], *, sliced: bool) -> str:
    params: dict[str, object] = {
        "db": "nuccore",
        "id": ",".join(ids),
        "rettype": "gb",
        "retmode": "text",
    }
    if sliced:
        params |= {"seq_start": 1, "seq_stop": 1}
    return call("efetch", params)


def fetch_batch(
    call: ncbi.Transport,
    ids: list[str],
    *,
    attempts: int = 3,
    sleep: Callable[[float], None] = time.sleep,
) -> dict[str, str]:
    """One batch, patient with NCBI before ever splitting it.

    "Response ended prematurely" looks structural and is not: the same 200 consecutive
    accessions that failed repeatedly were served at 238 records/sec minutes later. The
    first version of this function treated the error as one unservable record and halved
    the batch to find it, which turned every transient blip into ~200 single-record
    requests and dragged the fetch from 150 records/sec to 2.

    So: retry the whole batch, each retry being another three paced attempts inside the
    transport, and only then split -- in quarters, once, not recursively to singles. A
    lone record that still fails is retried whole, since the one-base slice is the part
    some records refuse; if that fails too it is left out of the page and the caller
    records it as `missing`, meaning "NCBI would not serve it", not "no such accession".
    """
    for attempt in range(attempts):
        try:
            return parse(_efetch(call, ids, sliced=True))
        except ncbi.NcbiError:
            if attempt < attempts - 1:
                sleep(2.0 * (attempt + 1))
    if len(ids) == 1:
        try:
            return parse(_efetch(call, ids, sliced=False))
        except ncbi.NcbiError:
            return {}
    out: dict[str, str] = {}
    step = max(1, len(ids) // 4)
    for i in range(0, len(ids), step):
        out |= fetch_batch(call, ids[i : i + step], attempts=attempts, sleep=sleep)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--results", type=Path, help="a run directory under results/ (default: the newest)")
    ap.add_argument("--batch", type=int, default=200, help="accessions per efetch POST")
    ap.add_argument("--limit", type=int, help="stop after this many accessions (a probe)")
    ap.add_argument("--email", help="contact address (default: .secrets/email)")
    args = ap.parse_args()

    run = args.results or newest_run(HERE)
    wanted = accessions_of_run(run)
    done = settled(SIDECAR)
    todo = [a for a in wanted if a not in done]
    if args.limit:
        todo = todo[: args.limit]
    print(
        f"{run.name}: {len(wanted):,} nuccore accessions, {len(done):,} already settled, "
        f"{len(todo):,} to fetch in batches of {args.batch}",
        flush=True,
    )
    if not todo:
        return 0

    email = args.email or (HERE / ".secrets" / "email").read_text().strip()
    call = ncbi.eutils(email, ncbi.api_key(root=HERE))

    SIDECAR.parent.mkdir(parents=True, exist_ok=True)
    new = not SIDECAR.exists()
    started = time.monotonic()
    dated = blank = missing = 0
    with SIDECAR.open("a") as out:
        if new:
            out.write("\t".join(COLUMNS) + "\n")
        for i in range(0, len(todo), args.batch):
            chunk = todo[i : i + args.batch]
            got = fetch_batch(call, chunk)
            for acc in chunk:
                if acc not in got:
                    # NCBI served the page but not this record: suppressed, removed or
                    # renamed. Settled, so the restart does not ask for it again.
                    out.write(f"{acc}\t\tmissing\n")
                    missing += 1
                elif got[acc]:
                    out.write(f"{acc}\t{got[acc]}\tok\n")
                    dated += 1
                else:
                    out.write(f"{acc}\t\tnodate\n")
                    blank += 1
            out.flush()
            n = i + len(chunk)
            rate = n / max(time.monotonic() - started, 1e-9)
            left = (len(todo) - n) / rate if rate else 0
            print(
                f"  {n:>9,}/{len(todo):,}  {rate:5.1f} rec/s  "
                f"{dated:,} dated / {blank:,} no date / {missing:,} missing  "
                f"eta {left / 3600:.1f} h",
                flush=True,
            )
    return 0


if __name__ == "__main__":
    sys.exit(main())
