"""Cut retrieved archives down to the windows around the sites a screen found, for distribution.

    python -m assaywatch.windows --out windows/            # every group, after a full pipeline run
    python -m assaywatch.windows --out windows/ --group 10292/q620b1275c5

`data/retrieved/` keeps whole records, so re-screening at any setting stays free and
independent checks (BLAST across a site, a spanning audit) remain possible. That is
gigabytes. The distributable keeps, for each record in which any assay of its group
found an amplicon, only the stretches around EVERY pair those assays could build there
(not just the reported best: a second copy of a multicopy target may win under other
penalties), plus `buffer_bp` each side, joined by an N spacer longer than the largest
amplicon so that nothing pairs across two windows. One FASTA record per source
record, under the source accession, so a screen of the window archive gives one row
per (assay, record) as the whole archive did, and the collect and drift steps read it
unchanged.

Beside each `<stem>.fasta.gz` sits `<stem>.windows.tsv.gz`, one row per window: where it
sits in the joined record, where it came from in the source (1-based, inclusive, the
`seq_start`/`seq_stop` an efetch of that range takes), and the source record's length
and base composition. The screener reads the sidecar automatically and scores each
record on the source length and composition, because the chance E-values depend on
both (`screen.window_context`).

Each group directory gets a `manifest.json`: the buffer, the settings that decide
where a site can be found at all, and a signature of each assay's primer pools. Those
are what a window archive cannot answer for. Re-screening one with a looser mismatch
budget, a wider amplicon range, a weaker chance filter or a new or edited primer pair
could find sites outside the windows, and finding none would look like robustness when
it means nothing. So `screen` refuses such a run (`check_against`). Context settings -
penalties, call boundaries, probe scoring, thermo - are free to change, because their
inputs are inside the windows.

Re-screened at the settings it was cut for, a window archive gives the same call,
penalty, E-value, product length and mismatch positions for every scored row as the
whole records did. `no_amplicon` rows keep their call but are labelled
`exclusion: windowed`: why a record gave no amplicon (diverged site, chance pairs only,
truncated deposit) depends on sequence outside the windows, so it is not guessed, and
`drift.count_diverged_as_fail` refuses such rows.

What a window archive does NOT do:
- reproduce rows for records in which no assay of the group found an amplicon. Those
  records are not in it; their calls (`no_amplicon`, `truncated`, ...) are in the
  calls table that ships beside it.
- support surveillance. It is a snapshot of one run's records; new deposits need the
  user's own retrieval.
- let `asm` windows be checked against NCBI: an assembly archive is already cut and
  N-joined, with no contig coordinates kept, so the manifest marks those groups
  `verifiable_by_efetch: false`.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
import sys
from collections import defaultdict, deque
from collections.abc import Iterator
from itertools import islice
from multiprocessing import Pool
from pathlib import Path
from typing import Any

from assaywatch.chance import composition
from assaywatch.fasta import read_fasta
from assaywatch.loci import pair_spans
from assaywatch.schema import Chemistry
from assaywatch.score import config_for, load_config, oligo_pools
from assaywatch.validate import load_assay

FORMAT = 1
SIDECAR_COLUMNS = ["record_id", "offset", "length", "src_start", "src_end", "src_len", "src_comp"]

# (path into the discovery dict, direction). "le": the running value must not exceed the
# archive's, and None means no limit, the loosest of all. "ge": must not fall below it.
_AMPLICON_RULES = {"min_bp": "ge", "max_bp": "le", "declared_tolerance": "le"}
_SCORING_RULES = {
    "max_mismatches_searched": "le",
    "max_ambiguous_per_oligo": "le",
    "max_pair_evalue": "le",
    "max_pairs_per_record": "le",
}
_SCORING_DEFAULTS = {"max_mismatches_searched": 6, "max_pairs_per_record": 5000}


def discovery_settings(cfg: dict[str, Any]) -> dict[str, Any]:
    """The settings that decide whether a site or a pair is found, per chemistry."""
    amp = cfg["amplicon"]
    out: dict[str, Any] = {
        "amplicon": {k: amp.get(k) for k in _AMPLICON_RULES},
        "by_chemistry": {},
    }
    for chem in Chemistry:
        s = config_for(chem, cfg)["scoring"]
        out["by_chemistry"][str(chem)] = {k: s.get(k, _SCORING_DEFAULTS.get(k)) for k in _SCORING_RULES}
    return out


def pair_signature(assay: Any) -> str:
    """Hash of an assay's forward and reverse pools, as matched (tails stripped)."""
    fwd, rev, _ = oligo_pools(assay)
    return hashlib.sha1(repr((sorted(fwd), sorted(rev))).encode()).hexdigest()[:12]


def _looser(running: Any, archive: Any, rule: str) -> bool:
    if rule == "ge":
        return running is not None and archive is not None and running < archive
    if archive is None:
        return False
    return running is None or running > archive


def check_against(manifest: dict[str, Any], cfg: dict[str, Any], assays: list) -> list[str]:
    """Why this config and these assays cannot be answered from this window archive ([] = they can)."""
    problems: list[str] = []
    if manifest.get("format") != FORMAT:
        return [f"window archive format {manifest.get('format')!r}, this screener reads {FORMAT}"]
    have, want = manifest["discovery"], discovery_settings(cfg)
    for key, rule in _AMPLICON_RULES.items():
        run, arc = want["amplicon"][key], have["amplicon"][key]
        if _looser(run, arc, rule):
            problems.append(f"amplicon.{key} is {run!r}, archive cut at {arc!r}")
    for chem in sorted({str(a.chemistry) for a in assays}):
        run, arc = want["by_chemistry"][chem], have["by_chemistry"].get(chem)
        if arc is None:
            problems.append(f"chemistry {chem} has no settings in the archive manifest")
            continue
        for key, rule in _SCORING_RULES.items():
            if _looser(run[key], arc[key], rule):
                problems.append(f"{chem}: scoring.{key} is {run[key]!r}, archive cut at {arc[key]!r}")
    for a in assays:
        sig = manifest["assays"].get(a.id)
        if sig is None:
            problems.append(f"{a.id} is not in the archive: its sites were never looked for")
        elif sig != pair_signature(a):
            problems.append(f"{a.id}: primer pools differ from the ones the archive was cut for")
    return problems


def merge_spans(spans: list[tuple[int, int]], buffer: int, length: int) -> list[tuple[int, int]]:
    """0-based half-open windows: each span widened by `buffer`, clipped, overlaps merged."""
    merged: list[list[int]] = []
    for lo, hi in sorted((max(0, a - buffer), min(length, b + buffer)) for a, b in spans):
        if merged and lo <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], hi)
        else:
            merged.append([lo, hi])
    return [(lo, hi) for lo, hi in merged]


def spacer_for(assays: list, cfg: dict[str, Any]) -> str:
    """N run longer than the largest amplicon plus the longest oligo: no pair can span two windows."""
    longest = max((len(o) for a in assays for pool in oligo_pools(a) for o in pool), default=0)
    return "N" * (int(cfg["amplicon"]["max_bp"]) + longest + 1)


def sites_by_record(screened_tsv: Path) -> dict[str, list[tuple[int, int]]]:
    """{record_id: [(amplicon_start, amplicon_end), ...]} from one screened archive."""
    out: dict[str, list[tuple[int, int]]] = defaultdict(list)
    with screened_tsv.open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            if row["amplicon_start"] and row["amplicon_end"]:
                out[row["record_id"]].append((int(row["amplicon_start"]), int(row["amplicon_end"])))
    return out


def screened_assays(screened_group: Path) -> set[str]:
    """The assays that screened a group, read from its screens: exactly the `--only` it ran with.

    Every archive of a group must have been screened by the same assays. If they differ,
    some screens are stale (run the pipeline first), and a manifest claiming one set of
    assays for all of them would be false.
    """
    sets = []
    for tsv in sorted(screened_group.glob("*.tsv")):
        with tsv.open() as fh:
            ids = {row["assay_id"] for row in csv.DictReader(fh, delimiter="\t")}
        if ids:
            sets.append((tsv.name, ids))
    if any(ids != sets[0][1] for _, ids in sets):
        detail = "; ".join(f"{name}: {sorted(ids)}" for name, ids in sets)
        raise SystemExit(f"{screened_group}: archives were screened by different assays ({detail})")
    return sets[0][1] if sets else set()


def search_settings(assays: list, cfg: dict[str, Any]) -> dict[str, Any]:
    """The loosest search any of these assays' chemistries runs: what the cut must cover."""
    scoring = [config_for(a.chemistry, cfg)["scoring"] for a in assays]
    evalues = [s.get("max_pair_evalue") for s in scoring]
    return {
        "pairs": sorted({(f, r) for a in assays for f in oligo_pools(a)[0] for r in oligo_pools(a)[1]}),
        "max_mm": max(int(s.get("max_mismatches_searched", 6)) for s in scoring),
        "max_e": float("inf") if any(e is None for e in evalues) else max(float(e) for e in evalues),
        "lo_bp": int(cfg["amplicon"]["min_bp"]),
        "hi_bp": int(cfg["amplicon"]["max_bp"]),
    }


def cut_archive(
    fasta: Path,
    sites: dict[str, list[tuple[int, int]]],
    search: dict[str, Any],
    cfg: dict[str, Any],
    buffer: int,
    spacer: str,
    out_fasta: Path,
    out_sidecar: Path,
    workers: int = 1,
    chunk_bp: int = 20_000_000,
) -> dict[str, int]:
    """Write the window archive and its sidecar for one source archive; return counts.

    `sites` are the amplicons the screen reported, one per (assay, record): only the best.
    The cut keeps a window around EVERY pair the search could build in those records
    (`loci.pair_spans`), because a later screen at tighter discovery settings or with other
    penalties may pick a different pair - a second copy of a multicopy target, say - and it
    has to be inside a window. The reported sites are kept too, so the reported calls are
    reproducible whatever the search finds. A record with no reported amplicon for any
    assay has no pair at these settings and is left out.
    """
    counts = {"records": 0, "windows": 0, "window_bp": 0, "source_bp": 0}
    with gzip.open(out_fasta, "wt") as fa, gzip.open(out_sidecar, "wt", newline="") as sc:
        w = csv.writer(sc, delimiter="\t", lineterminator="\n")
        w.writerow(SIDECAR_COLUMNS)
        batches = _candidate_batches(fasta, sites, chunk_bp)
        for rid, src_len, comp, windows, cut in _cut_results(batches, search, cfg, buffer, workers):
            pieces, offset = [], 0
            for (lo, hi), piece in zip(windows, cut, strict=True):
                if pieces:
                    offset += len(spacer)
                w.writerow([rid, offset, hi - lo, lo + 1, hi, src_len, comp])
                pieces.append(piece)
                offset += hi - lo
            fa.write(f">{rid}\n{spacer.join(pieces)}\n")
            counts["records"] += 1
            counts["windows"] += len(windows)
            counts["window_bp"] += sum(hi - lo for lo, hi in windows)
            counts["source_bp"] += src_len
    return counts


# The search is a full scan of each candidate record, as costly as a screen, so it runs
# in a process pool the way screen.py does: batches of records in archive order, a
# bounded number in flight, results written by the parent. Set once per worker.
_CUT: tuple[dict[str, Any], dict[str, Any], int] | None = None


def _init_cut(search: dict[str, Any], cfg: dict[str, Any], buffer: int) -> None:
    global _CUT
    _CUT = (search, cfg, buffer)


def _cut_batch(batch: list[tuple[str, str, list]]) -> list[tuple[str, int, str, list, list[str]]]:
    if _CUT is None:  # not an assert: `python -O` strips those, and this
        # runs inside a multiprocessing worker, where the resulting
        # AttributeError on None is the hardest kind of failure to trace.
        raise RuntimeError("_init_cut was not called in this worker")
    search, cfg, buffer = _CUT
    out = []
    for rid, seq, reported in batch:
        found = pair_spans(seq.upper(), cfg=cfg, **search)
        windows = merge_spans(reported + found, buffer, len(seq))
        comp = ",".join(str(x) for x in composition(seq))
        out.append((rid, len(seq), comp, windows, [seq[lo:hi] for lo, hi in windows]))
    return out


def _candidate_batches(fasta: Path, sites: dict[str, list], target_bp: int) -> Iterator[list]:
    batch, bp = [], 0
    for rid, seq in read_fasta(fasta):
        reported = sites.get(rid)
        if not reported:
            continue
        batch.append((rid, seq, reported))
        bp += len(seq)
        if bp >= target_bp:
            yield batch
            batch, bp = [], 0
    if batch:
        yield batch


def _cut_results(
    batches: Iterator[list], search: dict[str, Any], cfg: dict[str, Any], buffer: int, workers: int
) -> Iterator[tuple]:
    if workers <= 1:
        _init_cut(search, cfg, buffer)
        for batch in batches:
            yield from _cut_batch(batch)
        return
    in_flight: deque = deque()
    with Pool(workers, initializer=_init_cut, initargs=(search, cfg, buffer)) as pool:
        for batch in islice(batches, 2 * workers):
            in_flight.append(pool.apply_async(_cut_batch, (batch,)))
        while in_flight:
            done = in_flight.popleft().get()
            nxt = next(batches, None)
            if nxt is not None:
                in_flight.append(pool.apply_async(_cut_batch, (nxt,)))
            yield from done


def build_group(
    taxid: int,
    group: str,
    assays: list,
    cfg: dict[str, Any],
    screened_dir: Path,
    retrieved_dir: Path,
    out_dir: Path,
    buffer: int,
    workers: int = 1,
) -> dict[str, Any]:
    """Cut every archive of one retrieval group that has a screen; write the group manifest."""
    src = retrieved_dir / str(taxid) / group
    scr = screened_dir / str(taxid) / group
    dst = out_dir / str(taxid) / group
    dst.mkdir(parents=True, exist_ok=True)
    spacer = spacer_for(assays, cfg)
    search = search_settings(assays, cfg)
    archives: dict[str, Any] = {}
    for tsv in sorted(scr.glob("*.tsv")):
        fasta = src / f"{tsv.stem}.fasta.gz"
        if not fasta.exists():
            raise SystemExit(f"{tsv} has no archive at {fasta}")
        archives[tsv.stem] = cut_archive(
            fasta,
            sites_by_record(tsv),
            search,
            cfg,
            buffer,
            spacer,
            dst / f"{tsv.stem}.fasta.gz",
            dst / f"{tsv.stem}.windows.tsv.gz",
            workers,
        )
    manifest = {
        "format": FORMAT,
        "taxid": taxid,
        "group": group,
        "buffer_bp": buffer,
        "verifiable_by_efetch": group != "asm",
        "discovery": discovery_settings(cfg),
        "assays": {a.id: pair_signature(a) for a in sorted(assays, key=lambda a: a.id)},
        "archives": archives,
    }
    (dst / "manifest.json").write_text(json.dumps(manifest, indent=1, sort_keys=True) + "\n")
    return manifest


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", type=Path, required=True, help="directory to write the window archives into")
    ap.add_argument("--registry", type=Path, default=Path("registry"))
    ap.add_argument("--config", type=Path, default=None)
    ap.add_argument("--screened", type=Path, default=Path("results/screened"))
    ap.add_argument("--retrieved", type=Path, default=Path("data/retrieved"))
    ap.add_argument("--buffer", type=int, default=None, help="bp kept each side of a site (default: config)")
    ap.add_argument("--workers", type=int, default=1, help="processes for the pair search (default 1)")
    ap.add_argument("--group", action="append", default=None, help="TAXID/GROUP; repeatable (default: all)")
    args = ap.parse_args(argv)

    cfg = load_config(args.config)
    buffer = args.buffer if args.buffer is not None else int((cfg.get("windows") or {})["buffer_bp"])
    if args.group is None:
        groups = sorted((int(d.parent.name), d.name) for d in args.screened.glob("*/*") if d.is_dir())
    else:
        groups = sorted((int(t), g) for t, g in (x.split("/", 1) for x in args.group))
    total: dict[str, int] = defaultdict(int)
    for taxid, group in groups:
        ids = screened_assays(args.screened / str(taxid) / group)
        if not ids:
            continue
        assays = [load_assay(args.registry / f"{aid}.yaml") for aid in sorted(ids)]
        m = build_group(
            taxid, group, assays, cfg, args.screened, args.retrieved, args.out, buffer, args.workers
        )
        for counts in m["archives"].values():
            for k, v in counts.items():
                total[k] += v
        n = sum(c["records"] for c in m["archives"].values())
        print(f"{taxid}/{group}: {n:,} records", file=sys.stderr)
    print(
        f"{total['records']:,} records, {total['windows']:,} windows, "
        f"{total['window_bp'] / 1e6:.1f} Mbp kept of {total['source_bp'] / 1e6:.1f} Mbp",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
