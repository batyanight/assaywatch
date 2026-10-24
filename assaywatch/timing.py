"""Wall-clock instrumentation and run identity for a pipeline run.

Why this module exists
----------------------
The 2026-10-17 run could not answer "how long until this finishes", and then
failed for a reason that had nothing to do with the science.

Two separate problems, both addressed here:

1. **Run identity drifted mid-run.** `RUN_DATE` was `date.today()` evaluated at
   Snakefile parse time. The run started 22:49 and crossed midnight; by 00:17
   the date had rolled over and retrieval re-fired against the new date,
   writing `data/retrieved/runs/2026-10-18.json` (a full 123-group record,
   stamped `run_date: 2026-10-18`) while the parent process still expected
   `results/2026-10-17/calls.tsv.gz`. Every screen was correct and cached; the
   run failed anyway. `resolve_run_date` pins the date once and reuses it for
   the whole run, including a resume after a failure.

2. **Progress was unreadable.** Snakemake's "N of 249 steps" weights a
   one-second validate the same as a 24,000-record poxvirus screen, so the
   percentage said nothing about time remaining. Retrieval printed nothing
   between groups, and the only way to tell slow from stuck was watching a
   directory grow by hand. `RunManifest`, `heartbeat` and `weighted_eta`
   replace that with stage timings, a liveness file and a size-weighted
   estimate.

What is deliberately NOT here
-----------------------------
Nothing in this module may be imported by `assaywatch.screen` or anything it
imports. The screening cache key is a hash of `screen.py` and its full import
graph (`Snakefile:_code_hash`), so instrumenting the screening functions
through this module would invalidate all 246 cached screens on the next run -
about 1.5 hours of recomputation to gain a log line. Screening is instrumented
from the outside instead: the heartbeat watches archive and output sizes, which
costs the screening code nothing and cannot change a call.

Estimates are reported as estimates. `weighted_eta` returns `None` rather than
a number whenever it has no basis for one, because a confident wrong ETA is
worse than no ETA - that is the failure this module exists to correct.
"""

from __future__ import annotations

import json
import os
import threading
import time
from collections.abc import Callable, Iterable
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

__all__ = [
    "MARKER_NAME",
    "RunManifest",
    "Stage",
    "clear_run_marker",
    "directory_bytes",
    "format_duration",
    "heartbeat",
    "resolve_run_date",
    "weighted_eta",
    "write_run_marker",
]

# Lives under .snakemake/ because that is already the workflow's own state
# directory and is already gitignored; a marker in results/ would be mistaken
# for an output and deleted by Snakemake before the rule that needs it.
MARKER_NAME = "assaywatch-run.json"


def format_duration(seconds: float | None) -> str:
    """`3722` -> `1h 02m 02s`. `None` and negatives give `-`, not a fake zero."""
    if seconds is None or seconds < 0:
        return "-"
    seconds = int(round(seconds))
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    if h:
        return f"{h}h {m:02d}m {s:02d}s"
    if m:
        return f"{m}m {s:02d}s"
    return f"{s}s"


# --------------------------------------------------------------------------
# Run identity
# --------------------------------------------------------------------------


def resolve_run_date(
    config: dict[str, Any],
    state_dir: Path | str,
    *,
    now: datetime | None = None,
    max_age_hours: float = 48.0,
    write: bool = False,
) -> tuple[str, str]:
    """Resolve the run's date. Returns `(run_date, reason)`.

    Read-only by default: this runs at Snakefile parse time, which also happens
    on a dry run, so it must not pin anything. The pin is written separately by
    `write_run_marker` from `onstart`. `write=True` is kept for direct callers
    and tests that want the resolve-and-pin behaviour in one step.

    Resolution order, and why each step is there:

    - `config["run_date"]` wins outright. Re-rendering an old run must be able
      to name its folder explicitly.
    - An existing marker younger than `max_age_hours` is reused, with reason
      `resumed`. This is what fixes the midnight rollover: the second
      Snakemake process of the same run finds the first one's date instead of
      recomputing `date.today()`. It also makes a resume after a failure land
      in the folder the failed run was already filling.
    - Otherwise today's date, with reason `new`, and the marker is written.

    The age cap matters: without it, a marker left behind by an abandoned run
    would silently pin a new run to a stale folder weeks later. With it, the
    worst case is that a run resumed more than two days after it died starts a
    fresh folder, which is visible and harmless.

    `write=False` makes the call side-effect free, for a dry run or a test that
    only wants to know what the date would be.
    """
    explicit = config.get("run_date")
    if explicit:
        return str(explicit), "config"

    now = now or datetime.now()
    marker = Path(state_dir) / MARKER_NAME

    if marker.exists():
        try:
            data = json.loads(marker.read_text())
            started = datetime.fromisoformat(str(data["started"]))
            age_hours = (now - started).total_seconds() / 3600.0
            pinned = str(data["run_date"])
        except (KeyError, ValueError, OSError, json.JSONDecodeError):
            # A corrupt or hand-edited marker must not stop the pipeline; fall
            # through and start a new one.
            pass
        else:
            if 0 <= age_hours <= max_age_hours:
                return pinned, "resumed"

    run_date = now.date().isoformat()
    if write:
        marker.parent.mkdir(parents=True, exist_ok=True)
        _atomic_write_json(marker, {"run_date": run_date, "started": now.isoformat()})
    return run_date, "new"


def write_run_marker(run_date: str, state_dir: Path | str, *, now: datetime | None = None) -> None:
    """Pin `run_date` by writing the marker, unless one already exists.

    Split out from `resolve_run_date` so that the date can be RESOLVED read-only
    at Snakefile parse time (which also happens on a dry run and on `--list`)
    and PINNED only when a real run begins, from `onstart` - a handler Snakemake
    does not fire on a dry run. Without this split, `snakemake -n` wrote a pin
    marker, so the first dry run of a day silently decided that day's folder.

    An existing marker is left untouched: a resumed run must keep the ORIGINAL
    start time, because the age cap in `resolve_run_date` is measured from it.
    Overwriting it here would let a long-lived run repeatedly refresh its own
    marker and never age out.
    """
    marker = Path(state_dir) / MARKER_NAME
    if marker.exists():
        return
    now = now or datetime.now()
    _atomic_write_json(marker, {"run_date": run_date, "started": now.isoformat()})


def clear_run_marker(state_dir: Path | str) -> None:
    """Drop the marker so the next run starts a fresh date. Safe if absent.

    Called on success only. After a FAILURE the marker is deliberately left in
    place, because that is exactly when the next invocation is a resume and
    should reuse the same folder.
    """
    try:
        (Path(state_dir) / MARKER_NAME).unlink()
    except FileNotFoundError:
        pass
    except OSError:
        # Instrumentation must never be the reason a successful run reports
        # failure.
        pass


def _atomic_write_json(path: Path, payload: Any) -> None:
    """Write via a temp file and rename, so a reader never sees half a file.

    The heartbeat is read by humans (and `tail`) while it is being rewritten
    every few seconds; a partial read showing truncated JSON would look like a
    crash.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(f".{path.name}.part")
    tmp.write_text(json.dumps(payload, indent=2, default=str))
    os.replace(tmp, path)


# --------------------------------------------------------------------------
# Stage timing
# --------------------------------------------------------------------------


@dataclass
class Stage:
    name: str
    started: str
    finished: str | None = None
    seconds: float | None = None
    note: str = ""


@dataclass
class RunManifest:
    """Wall-clock record of one run, written as JSON beside the report.

    Deliberately append-only and crash-tolerant: `write()` is called after
    every change, so a run killed halfway still leaves a manifest showing
    which stage it died in and how long the earlier ones took. That is the
    record the next run's ETA is built from.
    """

    run_date: str
    started: str = field(default_factory=lambda: datetime.now().isoformat())
    finished: str | None = None
    status: str = "running"
    run_date_reason: str = ""
    stages: list[Stage] = field(default_factory=list)
    notes: dict[str, Any] = field(default_factory=dict)
    path: Path | None = None

    # -- stage bookkeeping --------------------------------------------------

    def start_stage(self, name: str, note: str = "") -> Stage:
        stage = Stage(name=name, started=datetime.now().isoformat(), note=note)
        self.stages.append(stage)
        self.write()
        return stage

    def end_stage(self, name: str, note: str = "") -> None:
        """Close the most recent open stage with this name. No-op if none."""
        for stage in reversed(self.stages):
            if stage.name == name and stage.finished is None:
                stage.finished = datetime.now().isoformat()
                stage.seconds = _elapsed(stage.started, stage.finished)
                if note:
                    stage.note = (stage.note + "; " + note).strip("; ")
                break
        self.write()

    def finish(self, status: str, note: str = "") -> None:
        self.finished = datetime.now().isoformat()
        self.status = status
        for stage in self.stages:
            if stage.finished is None:
                stage.finished = self.finished
                stage.seconds = _elapsed(stage.started, stage.finished)
                stage.note = (stage.note + "; interrupted").strip("; ")
        if note:
            self.notes["final"] = note
        self.write()

    @property
    def elapsed_seconds(self) -> float:
        return _elapsed(self.started, self.finished or datetime.now().isoformat())

    # -- persistence --------------------------------------------------------

    def write(self, path: Path | None = None) -> None:
        target = path or self.path
        if target is None:
            return
        self.path = target
        payload = asdict(self)
        payload["path"] = str(target)
        payload["elapsed_seconds"] = self.elapsed_seconds
        _atomic_write_json(Path(target), payload)

    @classmethod
    def load(cls, path: Path) -> RunManifest:
        data = json.loads(Path(path).read_text())
        stages = [Stage(**s) for s in data.get("stages", [])]
        return cls(
            run_date=data["run_date"],
            started=data.get("started", ""),
            finished=data.get("finished"),
            status=data.get("status", "unknown"),
            run_date_reason=data.get("run_date_reason", ""),
            stages=stages,
            notes=data.get("notes", {}),
            path=Path(path),
        )

    # -- reporting ----------------------------------------------------------

    def summary_lines(self) -> list[str]:
        """Human-readable per-stage timing, longest-running stage last."""
        out = [
            f"run {self.run_date} ({self.run_date_reason or 'unknown origin'}) "
            f"- {self.status} after {format_duration(self.elapsed_seconds)}"
        ]
        for stage in self.stages:
            note = f"  [{stage.note}]" if stage.note else ""
            out.append(f"  {stage.name:<22} {format_duration(stage.seconds):>12}{note}")
        return out


@dataclass(frozen=True)
class GroupCost:
    """What one retrieval group's archives cost to screen, by wall clock."""

    taxid: str
    group: str
    archives: int
    seconds: float


def read_screen_benchmarks(
    bench_dir: Path | str,
    *,
    since: datetime | None = None,
    until: datetime | None = None,
) -> list[GroupCost]:
    """Per-group screening cost from Snakemake's `benchmark:` files, slowest first.

    Reads `<bench_dir>/screen/<taxid>/<group>/<stem>.tsv`, each of which holds one
    data row whose `s` column is that archive's wall time, and sums it per
    (taxid, group). A group holding several dated archives is one row.

    WALL TIME IS THE ONLY COLUMN USED, and on macOS it is the only one that
    exists: Snakemake samples with psutil's `memory_full_info()`, which macOS
    refuses for a child process, and its sampler never sets `data_collected`, so
    `max_rss`, `cpu_time` and the rest read `NA` however long the job runs
    (measured 2026-10-22, docs/2026-10-18-pipeline-timekeeping-todo.md). On Linux
    - CI and a cluster - those columns fill in, which is where `mem_mb` and
    `threads` become checkable against what an archive actually costs.

    `since`/`until` filter on each file's MTIME, which is the only timestamp a
    benchmark carries: the files are keyed by archive, not by run date, so a
    cached screen keeps its last measurement and a directory read without a
    window mixes generations. Worse, Snakemake measures `time.time()` deltas,
    which keep advancing while the machine is suspended - the benchmarks written
    on 2026-10-22 span 91 minutes of laptop sleep and are mostly measuring the
    suspension. Passing the current run's own window is therefore not a nicety;
    it is what makes the numbers mean anything.
    """
    bench = Path(bench_dir) / "screen"
    per_group: dict[tuple[str, str], list[float]] = {}
    for tsv in sorted(bench.glob("*/*/*.tsv")):
        try:
            mtime = datetime.fromtimestamp(tsv.stat().st_mtime)
            if since is not None and mtime < since:
                continue
            if until is not None and mtime > until:
                continue
            rows = tsv.read_text().splitlines()
            if len(rows) < 2:
                continue
            seconds = float(rows[1].split("\t")[0])
        except (OSError, ValueError, IndexError):
            continue
        per_group.setdefault((tsv.parent.parent.name, tsv.parent.name), []).append(seconds)
    costs = [
        GroupCost(taxid=taxid, group=group, archives=len(v), seconds=sum(v))
        for (taxid, group), v in per_group.items()
    ]
    # Slowest first, then by name so equal costs do not reorder between runs.
    return sorted(costs, key=lambda c: (-c.seconds, c.taxid, c.group))


def _elapsed(start_iso: str, end_iso: str) -> float:
    try:
        return (datetime.fromisoformat(end_iso) - datetime.fromisoformat(start_iso)).total_seconds()
    except (ValueError, TypeError):
        return 0.0


# --------------------------------------------------------------------------
# Progress and liveness
# --------------------------------------------------------------------------


def directory_bytes(paths: Iterable[Path | str], pattern: str = "*") -> int:
    """Total size of files matching `pattern` under each path.

    Used as the heartbeat's progress signal. Size is the right signal for this
    pipeline because both slow stages are IO-shaped: retrieval grows an archive,
    screening grows a table. A stage that is working makes this number climb.
    """
    total = 0
    for p in paths:
        root = Path(p)
        if not root.exists():
            continue
        if root.is_file():
            total += root.stat().st_size
            continue
        for f in root.rglob(pattern):
            try:
                if f.is_file():
                    total += f.stat().st_size
            except OSError:
                continue
    return total


def weighted_eta(done_units: float, total_units: float, elapsed_seconds: float) -> float | None:
    """Seconds remaining, projected from work completed rather than step count.

    `units` are whatever measures the real cost - here, gzipped archive bytes,
    since screening time scales with sequence volume and not with the number of
    archives. Snakemake's step percentage was useless on the 2026-10-17 run
    precisely because one 756 MB poxvirus group counted as one step out of 249.

    Returns `None` when no honest projection exists (nothing finished yet, no
    work to do, or a nonsensical total). A caller that gets `None` should say
    "unknown", not print a zero.
    """
    if total_units <= 0 or done_units <= 0 or elapsed_seconds <= 0:
        return None
    if done_units >= total_units:
        return 0.0
    rate = done_units / elapsed_seconds
    if rate <= 0:
        return None
    return (total_units - done_units) / rate


def heartbeat(
    path: Path | str,
    progress: Callable[[], dict[str, Any]],
    *,
    interval: float = 60.0,
    stall_after: float = 600.0,
) -> Callable[[], None]:
    """Rewrite a liveness file every `interval` seconds until the returned stop() is called.

    `progress` is a callable returning a dict describing the current state. It
    must include a numeric `units_done` for stall detection to work; anything
    else it returns is copied into the file for the reader.

    Why a file and not just log lines: during the 2026-10-17 run, `pgrep` and
    `ps` were unavailable in the sandbox (`sysmond service not found`), so
    there was no way to confirm the pipeline was alive except watching a
    directory by hand. A file with a fresh timestamp answers "is it alive"
    without process inspection, and `stalled_seconds` answers "is it stuck"
    without a human remembering the last size they saw.

    The thread is a daemon and every tick is wrapped: instrumentation must not
    keep a finished pipeline alive, and must not crash a working one.
    """
    path = Path(path)
    stop_event = threading.Event()
    started = time.monotonic()
    state = {"last_units": None, "last_change": started}

    def tick() -> None:
        now = time.monotonic()
        try:
            info = dict(progress())
        except Exception as exc:  # noqa: BLE001 - never let a probe kill the run
            info = {"probe_error": repr(exc)}

        units = info.get("units_done")
        if isinstance(units, (int, float)):
            if state["last_units"] is None or units != state["last_units"]:
                state["last_units"] = units
                state["last_change"] = now
        stalled = now - state["last_change"]

        payload = {
            "written": datetime.now().isoformat(),
            "elapsed": format_duration(now - started),
            "elapsed_seconds": round(now - started, 1),
            "stalled_seconds": round(stalled, 1),
            # A human-readable warning rather than a bare number, because the
            # question being asked at 2am is "is this stuck".
            "status": "STALLED" if stalled >= stall_after else "progressing",
            **info,
        }
        _atomic_write_json(path, payload)

    def loop() -> None:
        tick()
        while not stop_event.wait(interval):
            tick()
        tick()

    thread = threading.Thread(target=loop, name="assaywatch-heartbeat", daemon=True)
    thread.start()

    def stop() -> None:
        stop_event.set()
        thread.join(timeout=interval + 5)

    return stop


def screening_progress(
    retrieved_dir: Path | str,
    screened_dir: Path | str,
) -> Callable[[], dict[str, Any]]:
    """Build a `progress` callable for `heartbeat` covering both slow stages.

    The archive list is discovered on every tick rather than passed in, because
    which archives exist is not known until the retrieve checkpoint has run -
    the probe has to work before, during and after that.

    Screening progress is measured in archive BYTES whose screen output already
    exists, which is the unit `weighted_eta` projects on. Counting archives
    instead would repeat Snakemake's mistake: on the 2026-10-17 run one 756 MB
    poxvirus group was a single archive among hundreds, so an archive count
    sat near 99% for the entire slow part.

    Retrieval has no completion marker, so growth in total archive bytes is its
    only progress signal; that is also what keeps a download-stage stall
    detectable.

    The ETA clock starts when this factory is called, so the projection is
    anchored to the stage it is measuring.
    """
    retrieved_root = Path(retrieved_dir)
    screened_root = Path(screened_dir)
    probe_start = time.monotonic()

    def probe() -> dict[str, Any]:
        total = done = 0
        n_total = n_done = 0
        for archive in retrieved_root.rglob("*.fasta.gz"):
            try:
                size = archive.stat().st_size
            except OSError:
                continue
            n_total += 1
            total += size
            # results/screened/<taxid>/<group>/<stem>.tsv mirrors
            # data/retrieved/<taxid>/<group>/<stem>.fasta.gz
            stem = archive.name[: -len(".fasta.gz")]
            out = screened_root / archive.parent.parent.name / archive.parent.name / f"{stem}.tsv"
            if out.exists():
                n_done += 1
                done += size
        eta = weighted_eta(done, total, time.monotonic() - probe_start)
        return {
            "stage": "screen" if n_done else "retrieve",
            "archives_total": n_total,
            "archives_screened": n_done,
            "bytes_total": total,
            "bytes_screened": done,
            "fraction": round(done / total, 4) if total else None,
            "eta": format_duration(eta),
            "eta_seconds": round(eta, 1) if eta is not None else None,
            # Stall detection keys on retrieval AND screening, so a run stuck
            # mid-download is caught as well as one stuck mid-screen.
            "units_done": done + total,
        }

    return probe
