"""`scripts/backfill_collection_dates.py`: one unservable record must not cost its batch.

Collection date lives only in the flatfile's `source` feature, so the backfill asks for
whole records (sliced to one base) rather than summaries. NCBI does not refuse a single
unslicable record politely: it ends the whole page prematurely, so one bad accession in
a batch of 200 loses all 200. What is pinned here is that the fetch bisects around it,
that a record NCBI serves without a date is recorded as an answer rather than retried
for ever, and that assemblies -- which already carry a collection date from the Datasets
metadata -- are never asked for.
"""

from __future__ import annotations

import gzip
import importlib.util
from pathlib import Path

import pytest

from assaywatch import ncbi

ROOT = Path(__file__).resolve().parents[1]

TWO_RECORDS = """LOCUS       AB000001                 500 bp    DNA     linear   VRL 01-JAN-2009
VERSION     AB000001.1
FEATURES             Location/Qualifiers
     source          1..500
                     /organism="Some virus"
                     /collection_date="16-Mar-2009"
ORIGIN
        1 a
//
LOCUS       AB000002                 400 bp    DNA     linear   VRL 01-JAN-2010
VERSION     AB000002.2
FEATURES             Location/Qualifiers
     source          1..400
                     /organism="Some virus"
ORIGIN
        1 a
//
"""


def _module():
    spec = importlib.util.spec_from_file_location(
        "backfill_collection_dates", ROOT / "scripts" / "backfill_collection_dates.py"
    )
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_parse_keys_on_version_and_keeps_a_dateless_record():
    got = _module().parse(TWO_RECORDS)
    # Keyed on VERSION, because that is how the calls table spells a record id; LOCUS
    # drops the `.1` and could not be joined on.
    assert got == {"AB000001.1": "16-Mar-2009", "AB000002.2": ""}


def test_a_transient_failure_is_retried_whole_and_never_split():
    """The expensive mistake: splitting on an error that would have passed on retry."""
    mod = _module()
    calls: list[int] = []

    def transport(endpoint: str, params: dict) -> str:
        calls.append(len(params["id"].split(",")))
        if len(calls) == 1:
            raise ncbi.NcbiError("efetch: Response ended prematurely")
        return TWO_RECORDS

    got = mod.fetch_batch(transport, ["AB000001.1", "AB000002.2"], sleep=lambda _: None)
    assert got == {"AB000001.1": "16-Mar-2009", "AB000002.2": ""}
    # Both calls asked for the whole batch. Nothing was bisected.
    assert calls == [2, 2]


def test_a_batch_splits_in_quarters_only_after_patience_runs_out():
    mod = _module()
    poison = "AB000002.2"
    calls: list[int] = []

    def transport(endpoint: str, params: dict) -> str:
        ids = params["id"].split(",")
        calls.append(len(ids))
        if poison in ids and "seq_start" in params:
            raise ncbi.NcbiError("efetch: Response ended prematurely")
        if poison in ids:
            # Unsliced, the record some slices refuse comes back like any other.
            return TWO_RECORDS
        return TWO_RECORDS.split("\n//")[0] + "\n//\n"

    got = mod.fetch_batch(transport, ["AB000001.1", poison], attempts=2, sleep=lambda _: None)
    assert got == {"AB000001.1": "16-Mar-2009", "AB000002.2": ""}
    # Two patient attempts at the pair, then its quarters -- here single records. The
    # good one costs a call; the one the slice refuses costs two sliced and one whole.
    assert calls == [2, 2, 1, 1, 1, 1]


def test_a_record_no_route_can_fetch_is_left_out_so_the_caller_can_settle_it():
    mod = _module()

    def transport(endpoint: str, params: dict) -> str:
        raise ncbi.NcbiError("efetch: HTTP 400")

    assert mod.fetch_batch(transport, ["AB000001.1"], sleep=lambda _: None) == {}


def test_accessions_of_a_run_drop_assemblies_and_duplicates(tmp_path: Path):
    run = tmp_path / "2026-10-27"
    run.mkdir()
    rows = [
        "assay_id\trecord_id\tcall",
        "A\tAB000001.1\tdetect",
        "A\tGCA_000001.1\tdetect",
        "B\tAB000001.1\tfail",
        "B\tGCF_000002.1\tfail",
        "B\tAB000003.1\tfail",
    ]
    with gzip.open(run / "calls.tsv.gz", "wt") as fh:
        fh.write("\n".join(rows) + "\n")
    # Assemblies carry their collection date already; asking for them would be work
    # for nothing. Order is the table's, so a resumed run asks in a stable order.
    assert _module().accessions_of_run(run) == ["AB000001.1", "AB000003.1"]


def test_the_rate_is_measured_over_a_window_not_since_the_start():
    """A cumulative average is the wrong number to steer by, and it cost a working run.

    The fetch opens slowly while NCBI works off whatever load preceded it, then recovers.
    Averaged since start, that opening drags the figure down for tens of thousands of
    records: a run that had reached 69 records/sec still showed single digits early, and
    the ETA derived from it read 400+ hours instead of 4.5. The run was killed on that
    reading. The rate now describes the recent past, which is the only part that predicts
    the near future.
    """
    mod = _module()

    # Ten one-second steps of 10 records each: 10/s throughout.
    steady = [(float(i), i * 10) for i in range(11)]
    assert mod.recent_rate(steady) == pytest.approx(10.0)

    # A slow first minute, then fast. The windowed rate must follow the fast part; an
    # average since the start would still be reporting the slow one.
    opening = [(float(i), i) for i in range(60)]  # 1/s
    then = [(60.0 + i, 60 + i * 100) for i in range(1, 11)]  # 100/s
    samples = opening + then
    assert mod.recent_rate(samples, window=10.0) == pytest.approx(100.0, rel=0.2)
    cumulative = samples[-1][1] / samples[-1][0]
    assert cumulative < 20.0  # what the old line would have printed

    # Degenerate inputs must not divide by zero or crash a six-hour job.
    assert mod.recent_rate([]) == 0.0
    assert mod.recent_rate([(1.0, 100)]) == 0.0
    assert mod.recent_rate([(1.0, 100), (1.0, 200)]) == 0.0


def test_settled_reads_back_with_or_without_a_header(tmp_path: Path):
    mod = _module()
    p = tmp_path / "collection-dates.tsv"
    p.write_text("accession\tcollection_date\tstatus\nAB000001.1\t2009\tok\nAB000002.2\t\tnodate\n")
    assert mod.settled(p) == {"AB000001.1", "AB000002.2"}
    p.write_text("AB000001.1\t2009\tok\n")
    assert mod.settled(p) == {"AB000001.1"}
    assert mod.settled(tmp_path / "nothing.tsv") == set()
