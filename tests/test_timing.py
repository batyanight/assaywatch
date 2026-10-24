"""Tests for assaywatch.timing.

The case that matters most is the midnight rollover, because that is the
failure this module was written for: the 2026-10-17 run started at 22:49,
crossed midnight, and split its outputs across two date folders.
"""

import json
import os
import time
from datetime import datetime, timedelta

import pytest

from assaywatch.timing import (
    MARKER_NAME,
    RunManifest,
    clear_run_marker,
    directory_bytes,
    format_duration,
    heartbeat,
    resolve_run_date,
    weighted_eta,
    write_run_marker,
)

# -- run identity ----------------------------------------------------------


def test_explicit_run_date_wins_and_writes_no_marker(tmp_path):
    assert resolve_run_date({"run_date": "2026-01-01"}, tmp_path) == ("2026-01-01", "config")
    assert not (tmp_path / MARKER_NAME).exists()


def test_a_run_crossing_midnight_keeps_one_date(tmp_path):
    """The 2026-10-17 regression, as a test. `write=True` is the resolve-and-pin
    shorthand; the Snakefile reaches the same state via resolve + write_run_marker."""
    start = datetime(2026, 10, 17, 22, 49)
    first, reason = resolve_run_date({}, tmp_path, now=start, write=True)
    assert (first, reason) == ("2026-10-17", "new")

    # A later process of the SAME run, after midnight, must not invent a new date.
    after_midnight = datetime(2026, 10, 18, 0, 17)
    assert resolve_run_date({}, tmp_path, now=after_midnight) == ("2026-10-17", "resumed")


def test_stale_marker_beyond_the_age_cap_starts_a_new_date(tmp_path):
    start = datetime(2026, 10, 17, 22, 49)
    resolve_run_date({}, tmp_path, now=start, write=True)
    much_later = start + timedelta(hours=72)
    date_str, reason = resolve_run_date({}, tmp_path, now=much_later, max_age_hours=48)
    assert reason == "new"
    assert date_str == "2026-10-20"


def test_corrupt_marker_does_not_stop_the_run(tmp_path):
    (tmp_path / MARKER_NAME).write_text("{not json")
    date_str, reason = resolve_run_date({}, tmp_path, now=datetime(2026, 5, 4, 9, 0))
    assert (date_str, reason) == ("2026-05-04", "new")


def test_resolve_is_read_only_by_default(tmp_path):
    """Parse-time resolution (the default) must not pin, so a dry run cannot."""
    resolve_run_date({}, tmp_path, now=datetime(2026, 5, 4))
    assert not (tmp_path / MARKER_NAME).exists()


def test_write_run_marker_pins_then_is_a_no_op(tmp_path):
    first = datetime(2026, 10, 17, 22, 49)
    write_run_marker("2026-10-17", tmp_path, now=first)
    assert (tmp_path / MARKER_NAME).exists()
    # A later process must not overwrite the original start time, or a
    # long-lived run would refresh its own marker and never age out.
    write_run_marker("2026-10-17", tmp_path, now=datetime(2026, 10, 18, 0, 17))
    data = json.loads((tmp_path / MARKER_NAME).read_text())
    assert data["started"] == first.isoformat()


def test_resolve_then_pin_reproduces_the_midnight_fix(tmp_path):
    """The parse-time/onstart split, end to end."""
    start = datetime(2026, 10, 17, 22, 49)
    rd, reason = resolve_run_date({}, tmp_path, now=start)
    assert (rd, reason) == ("2026-10-17", "new")
    write_run_marker(rd, tmp_path, now=start)  # onstart of the first process

    after = datetime(2026, 10, 18, 0, 17)
    rd2, reason2 = resolve_run_date({}, tmp_path, now=after)  # parse time of the resume
    assert (rd2, reason2) == ("2026-10-17", "resumed")


def test_clear_marker_is_idempotent(tmp_path):
    resolve_run_date({}, tmp_path, now=datetime(2026, 5, 4))
    clear_run_marker(tmp_path)
    clear_run_marker(tmp_path)  # must not raise
    assert not (tmp_path / MARKER_NAME).exists()


# -- manifest --------------------------------------------------------------


def test_manifest_records_stages_and_survives_a_round_trip(tmp_path):
    path = tmp_path / "run-timing.json"
    m = RunManifest(run_date="2026-10-17", run_date_reason="new", path=path)
    m.start_stage("retrieve")
    m.end_stage("retrieve", note="123 groups")
    m.start_stage("screen")
    m.finish("success")

    back = RunManifest.load(path)
    assert back.status == "success"
    assert [s.name for s in back.stages] == ["retrieve", "screen"]
    assert back.stages[0].note == "123 groups"
    # An open stage at finish() is closed, not left dangling.
    assert all(s.finished for s in back.stages)
    assert "interrupted" in back.stages[1].note


def test_manifest_is_written_after_every_change(tmp_path):
    """A run killed mid-stage still leaves a readable manifest."""
    path = tmp_path / "t.json"
    m = RunManifest(run_date="2026-10-17", path=path)
    m.start_stage("screen")
    on_disk = json.loads(path.read_text())
    assert on_disk["status"] == "running"
    assert on_disk["stages"][0]["name"] == "screen"


def test_summary_lines_mention_each_stage(tmp_path):
    m = RunManifest(run_date="2026-10-17", run_date_reason="new", path=tmp_path / "t.json")
    m.start_stage("retrieve")
    m.end_stage("retrieve")
    m.finish("success")
    text = "\n".join(m.summary_lines())
    assert "retrieve" in text and "2026-10-17" in text


# -- estimates -------------------------------------------------------------


@pytest.mark.parametrize(
    "done,total,elapsed,expected",
    [
        (25, 100, 10, 30.0),  # a quarter done in 10s -> 30s left
        (100, 100, 10, 0.0),  # finished
        (150, 100, 10, 0.0),  # overshoot is clamped, not negative
    ],
)
def test_weighted_eta(done, total, elapsed, expected):
    assert weighted_eta(done, total, elapsed) == expected


@pytest.mark.parametrize("args", [(0, 100, 10), (10, 0, 10), (10, 100, 0), (10, -5, 10)])
def test_weighted_eta_returns_none_rather_than_guessing(args):
    """No basis for a projection must give None, never a confident zero."""
    assert weighted_eta(*args) is None


def test_format_duration():
    assert format_duration(3722) == "1h 02m 02s"
    assert format_duration(62) == "1m 02s"
    assert format_duration(5) == "5s"
    assert format_duration(None) == "-"
    assert format_duration(-1) == "-"


def test_directory_bytes_counts_matching_files(tmp_path):
    (tmp_path / "a.fasta.gz").write_bytes(b"x" * 10)
    (tmp_path / "b.txt").write_bytes(b"y" * 100)
    sub = tmp_path / "sub"
    sub.mkdir()
    (sub / "c.fasta.gz").write_bytes(b"z" * 5)
    assert directory_bytes([tmp_path], "*.fasta.gz") == 15
    assert directory_bytes([tmp_path / "missing"]) == 0


# -- heartbeat -------------------------------------------------------------


def test_heartbeat_writes_and_flags_a_stall(tmp_path):
    path = tmp_path / "hb.json"
    stop = heartbeat(path, lambda: {"units_done": 7, "stage": "screen"}, interval=0.05, stall_after=0.15)
    time.sleep(0.4)
    stop()
    payload = json.loads(path.read_text())
    assert payload["stage"] == "screen"
    # units_done never changed, so it must be reported as stalled.
    assert payload["status"] == "STALLED"


def test_heartbeat_reports_progress_when_units_move(tmp_path):
    path = tmp_path / "hb.json"
    counter = {"n": 0}

    def probe():
        counter["n"] += 1
        return {"units_done": counter["n"]}

    stop = heartbeat(path, probe, interval=0.05, stall_after=1.0)
    time.sleep(0.2)
    stop()
    assert json.loads(path.read_text())["status"] == "progressing"


def test_a_failing_probe_does_not_kill_the_run(tmp_path):
    path = tmp_path / "hb.json"

    def probe():
        raise RuntimeError("boom")

    stop = heartbeat(path, probe, interval=0.05)
    time.sleep(0.15)
    stop()
    assert "probe_error" in json.loads(path.read_text())


# --- per-group screening cost (timekeeping item 7) -------------------------


def _bench(root, taxid, group, stem, seconds, *, mtime=None):
    """Write one Snakemake benchmark file, optionally backdated."""
    p = root / "screen" / taxid / group / f"{stem}.tsv"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(
        "s\th:m:s\tmax_rss\tmax_vms\tmax_uss\tmax_pss\tio_in\tio_out\tmean_load\tcpu_time\n"
        f"{seconds}\t0:00:0{int(seconds) % 10}\tNA\tNA\tNA\tNA\tNA\tNA\tNA\tNA\n"
    )
    if mtime is not None:
        os.utime(p, (mtime.timestamp(), mtime.timestamp()))
    return p


def test_group_cost_sums_archives_and_ranks_slowest_first(tmp_path):
    from assaywatch.timing import read_screen_benchmarks

    _bench(tmp_path, "10241", "all", "2026-10-03", 5.0)
    _bench(tmp_path, "10241", "all", "2026-10-11", 7.0)
    _bench(tmp_path, "11118", "qabc", "2026-10-03", 9.0)
    costs = read_screen_benchmarks(tmp_path)
    assert [(c.taxid, c.archives, c.seconds) for c in costs] == [("10241", 2, 12.0), ("11118", 1, 9.0)]


def test_a_benchmark_outside_the_run_window_is_not_counted(tmp_path):
    """The whole point of the window: a benchmark is keyed by ARCHIVE, not by run
    date, so a cached screen keeps an old measurement and a bare read mixes
    generations -- and Snakemake's wall clock counts machine sleep, so a stale
    row can be mostly measuring a suspension."""
    from assaywatch.timing import read_screen_benchmarks

    old = datetime(2026, 10, 22, 15, 0, 0)
    _bench(tmp_path, "10241", "all", "2026-10-03", 1180.0, mtime=old)
    _bench(tmp_path, "11118", "qabc", "2026-10-03", 9.0)
    assert len(read_screen_benchmarks(tmp_path)) == 2
    windowed = read_screen_benchmarks(tmp_path, since=datetime(2026, 10, 23, 0, 0, 0))
    assert [c.taxid for c in windowed] == ["11118"]


def test_equal_costs_keep_a_stable_order(tmp_path):
    """A report that diffs between runs over tie order is noise."""
    from assaywatch.timing import read_screen_benchmarks

    _bench(tmp_path, "999", "b", "s", 4.0)
    _bench(tmp_path, "111", "a", "s", 4.0)
    assert [c.taxid for c in read_screen_benchmarks(tmp_path)] == ["111", "999"]


def test_an_unreadable_benchmark_is_skipped_not_fatal(tmp_path):
    from assaywatch.timing import read_screen_benchmarks

    _bench(tmp_path, "10241", "all", "good", 3.0)
    bad = tmp_path / "screen" / "10241" / "all" / "headeronly.tsv"
    bad.write_text("s\th:m:s\n")
    (tmp_path / "screen" / "10241" / "all" / "nonnumeric.tsv").write_text("s\nNA\n")
    costs = read_screen_benchmarks(tmp_path)
    assert [(c.taxid, c.archives) for c in costs] == [("10241", 1)]


# --- screening cost model and worker sizing --------------------------------


def test_cost_scales_with_assays_because_each_one_rescans_the_archive():
    """The term the byte-only rule left out, and it is mechanical rather than
    fitted: an archive is screened against every assay that asked for its group."""
    from assaywatch.timing import screen_core_seconds

    one = screen_core_seconds(100.0, 10_000, assays=1)
    three = screen_core_seconds(100.0, 10_000, assays=3)
    startup = screen_core_seconds(0.0, 0, assays=1)
    # Everything but the fixed start-up cost triples.
    assert three - startup == pytest.approx(3 * (one - startup), rel=1e-9)


def test_a_record_dense_archive_gets_more_than_one_worker():
    """The measured fault: 10 MB holding 190,101 records cost 52 s on the single
    worker the byte rule gave it (`11320/qdf5abd73c1`, 2026-10-23)."""
    from assaywatch.timing import screen_workers

    byte_rule = max(1, min(16, int(10.1 // 25)))
    assert byte_rule == 1
    assert screen_workers(10.1, 190_101, assays=1) > 1


def test_a_record_sparse_archive_is_not_given_every_core():
    """The other direction: 761 MB holding 17,417 records for one assay was given
    16 workers by the byte rule, which on a cluster is 16 CPUs for one core's work."""
    from assaywatch.timing import screen_workers

    assert max(1, min(16, int(761.1 // 25))) == 16
    assert screen_workers(761.1, 17_417, assays=1) < 16


def test_a_tiny_archive_gets_exactly_one_worker():
    """Below the start-up cost an extra worker cannot pay for itself."""
    from assaywatch.timing import screen_workers

    assert screen_workers(0.02, 20, assays=1) == 1
    assert screen_workers(0.0, 0, assays=9) == 1


def test_a_missing_record_count_falls_back_to_the_size_terms():
    """`None` is the honest answer when the manifest has no count, and must not
    crash or silently read as zero-cost."""
    from assaywatch.timing import screen_core_seconds, screen_workers

    with_count = screen_core_seconds(100.0, 50_000, assays=2)
    without = screen_core_seconds(100.0, None, assays=2)
    assert 0 < without < with_count
    assert screen_workers(100.0, None, assays=2) >= 1


def test_workers_never_exceed_the_cap_or_fall_below_one():
    from assaywatch.timing import screen_workers

    cfg = {"screen": {"max_workers": 4}}
    assert screen_workers(100_000.0, 10_000_000, assays=9, cfg=cfg) == 4
    assert screen_workers(0.0, 0, assays=1, cfg=cfg) == 1


def test_the_config_block_overrides_the_fitted_defaults():
    """The constants are config, not code: CLAUDE.md's rule for any fitted number."""
    from assaywatch.timing import screen_core_seconds

    cfg = {"screen": {"cost_startup_s": 0.0, "cost_per_mb_assay": 1.0, "cost_per_record_assay": 0.0}}
    assert screen_core_seconds(10.0, 999_999, assays=2, cfg=cfg) == pytest.approx(20.0)


def test_cost_is_monotonic_in_every_input():
    """A bigger, denser, more-shared archive is never predicted cheaper."""
    from assaywatch.timing import screen_core_seconds

    base = screen_core_seconds(50.0, 1_000, assays=2)
    assert screen_core_seconds(51.0, 1_000, assays=2) > base
    assert screen_core_seconds(50.0, 2_000, assays=2) > base
    assert screen_core_seconds(50.0, 1_000, assays=3) > base
