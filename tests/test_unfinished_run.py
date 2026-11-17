"""The guard against pinning a new run date over an unfinished split run.

On 2026-11-17 a launch on the Air with no `run_date` pinned a new date and ran a
whole new run, although the intent was to finish 2026-11-15, whose Air half had
ended with `status: success` and so cleared the pin. `unfinished_run` is the
check the Snakefile makes before it lets a launch pin a new date
(docs/journal/2026-11-17-composition-on-the-air.md, "Mistake 1").
"""

from assaywatch.timing import unfinished_run


def _run(results, name, *, finished=False):
    folder = results / name
    folder.mkdir(parents=True)
    if finished:
        (folder / "report.html").write_text("<html></html>")


def test_the_latest_earlier_run_without_a_report_is_unfinished(tmp_path):
    _run(tmp_path, "2026-11-10", finished=True)
    _run(tmp_path, "2026-11-15")
    assert unfinished_run(tmp_path, before="2026-11-17") == "2026-11-15"


def test_a_finished_latest_run_lets_a_new_date_through(tmp_path):
    # An older unfinished folder is history, not a split run waiting for its second half.
    _run(tmp_path, "2026-10-23")
    _run(tmp_path, "2026-11-10", finished=True)
    assert unfinished_run(tmp_path, before="2026-11-17") is None


def test_only_folders_named_as_a_date_count(tmp_path):
    """results/ also holds screened/, benchmarks/ and hand-named copies such as
    2026-10-28.partial-stopped or 2026-10-24-anchorfdr; none of them is a run."""
    _run(tmp_path, "2026-11-10", finished=True)
    for name in ("screened", "benchmarks", "2026-11-12.partial-stopped", "2026-11-12-anchorfdr"):
        _run(tmp_path, name)
    assert unfinished_run(tmp_path, before="2026-11-17") is None


def test_the_new_date_itself_and_later_dates_are_not_the_previous_run(tmp_path):
    _run(tmp_path, "2026-11-10", finished=True)
    _run(tmp_path, "2026-11-17")
    _run(tmp_path, "2026-11-20")
    assert unfinished_run(tmp_path, before="2026-11-17") is None


def test_no_results_folder_means_no_previous_run(tmp_path):
    assert unfinished_run(tmp_path / "absent", before="2026-11-17") is None
