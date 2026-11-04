"""Build one run's lineage composition from the calls table and the archives.

SPLIT FROM `composition.py` (2026-11-03, ROADMAP composition step 13). The model, the
statistics and the two file formats live there, because every consumer reads them:
`lineage_report`, and later the report and the website. This module is the PRODUCER, and
it is the only part that needs the verdict path -- `report.assessment_inputs`,
`report.load_calls_as_reported` -- so that import stays out of the consumers' closure.

The reason is mechanical and measured: `triggers.import_closure` walks a module's whole
AST, function-local imports included, so a single `from assaywatch.report import ...`
anywhere in `composition.py` put `report.py` into the `lineage_analysis` rule's
signature, and `pytest -m slow` caught it -- every edit to `report.py` would have reread
2.7M rows of calls for a document that does not depend on it. The same seam
`clustermaps.py` sits on, for the same reason.
"""

from __future__ import annotations

import gzip
import warnings
from collections import defaultdict
from collections.abc import Mapping, Sequence
from datetime import date
from pathlib import Path
from typing import Any

from assaywatch.accession import strip_version
from assaywatch.composition import (
    DIVERGED,
    AssayComposition,
    Cell,
    CompositionRun,
    Options,
    cells_from,
    describe_clusters,
    label_records,
    observed_series,
    pool_small_clusters,
    resolve_species,
    same_mix_series,
    species_years,
    split_change,
)
from assaywatch.drift import GraphRecord
from assaywatch.subcluster import OTHER, UNPLACED, available_flank, flanked_region, window_shape
from assaywatch.taxonomy import Taxonomy

_Placement = tuple[tuple[int, int], list[tuple[int, int]]]


def _place_window(
    seq: str, assay: Any, cfg: Mapping[str, Any], search: Mapping[str, Any]
) -> tuple[tuple[int, int], list[tuple[int, int]]] | None:
    """Where one record's amplicon sits and which stretches are oligo sites, or None when
    this record can carry no product.

    RECOMPUTED from the sequence, not read from the run's tables (2026-11-03, a change to
    the interface the plan approved). Three things were tried: `calls.read_calls` drops the
    amplicon and site columns on purpose, because carrying every column of a 2.7M-row
    table as dicts took 3.6 GB; the per-assay screens under `results/screened/` do hold
    them, but they are a cache keyed by archive and their `assay_id` column goes stale --
    on 2026-11-03 every screen on this machine still carried the ids renamed away on
    2026-11-02, so matching on it found nothing at all. `match.pair_spans` and
    `match.find_sites` need neither, and cost 0.2 ms per record (100 Chlamydia records,
    measured), which is 12 seconds for the largest archive in the registry.

    The search runs at `clustermaps.search_params`, the widest any chemistry may use, so
    composition and the Mode C resolver look for sites identically. Of the candidate
    amplicons the one nearest the assay's own `amplicon_bp` is cut around -- the screen's
    winning pair is not recorded here -- and EVERY candidate site of every oligo is
    masked, which errs toward masking too much: a window must not be defined by sequence
    the assay measures.
    """
    from assaywatch.match import find_sites, pair_spans

    pairs = [(assay.oligos.forward.matching_seq, assay.oligos.reverse.matching_seq)]
    spans = pair_spans(seq, pairs, cfg, **search)
    if not spans:
        return None
    want = assay.amplicon_bp
    span = min(spans, key=lambda s: (abs((s[1] - s[0]) - want) if want else 0, s[0]))
    oligos = [assay.oligos.forward, assay.oligos.reverse, assay.oligos.probe]
    sites = [
        (site.start, site.end)
        for oligo in oligos
        if oligo is not None
        for site in find_sites(oligo.matching_seq, seq, int(search["max_mm"]))
    ]
    return span, sites


def relabel(cells: Sequence[Cell], keep: set[int]) -> list[Cell]:
    """Pool every cluster outside `keep` into `OTHER`, keeping years and counts."""
    totals: dict[tuple[int, int], list[int]] = defaultdict(lambda: [0, 0, 0])
    for c in cells:
        cell = totals[(c.year, c.cluster if c.cluster in keep else OTHER)]
        cell[0] += c.records
        cell[1] += c.detected
        cell[2] += c.recent
    return [Cell(y, k, n, d, rec) for (y, k), (n, d, rec) in sorted(totals.items())]


def build_assay(
    assay: Any,
    records: Sequence[GraphRecord],
    cfg: Mapping[str, Any],
    sequences: Mapping[str, str],
    titles: Mapping[str, str],
    taxonomy: Taxonomy | None,
    opts: Options,
) -> AssayComposition:
    """One assay's composition, from the very records its graph is built from.

    The window is placed per record by `_place_window`, which says why it recomputes;
    `sequences` and `titles` come from the archive, keyed by unversioned accession. A
    record whose sequence is missing, or which can carry no product, is still COUNTED --
    it is in the graph -- and lands in `unplaced`: leaving it out would break the
    invariant that each year's cells sum to that year's evaluable records, and that
    invariant is the point (finding 4).
    """
    from assaywatch.clustermaps import search_params

    search = search_params(cfg)
    spans = []
    for r in records:
        if not r.evaluable or r.diverged:
            continue
        seq = sequences.get(strip_version(r.record_id))
        placed = _place_window(seq, assay, cfg, search) if seq is not None else None
        if placed is not None:
            spans.append((r, seq, *placed))

    shape = window_shape(
        [available_flank(seq, amp, stop_n_run=opts.stop_n_run) for _, seq, amp, _ in spans],
        flank_bp=opts.flank_bp,
        quantile=opts.shape_quantile,
    )
    regions = [
        flanked_region(
            r.record_id,
            seq,
            amp,
            sites,
            left_bp=shape[0],
            right_bp=shape[1],
            mask_buffer_bp=opts.mask_buffer_bp,
            stop_n_run=opts.stop_n_run,
        )
        for r, seq, amp, sites in spans
    ]
    labels, cut = label_records(regions, [r.year for r, *_ in spans], opts)

    # Pool once, over every year, then apply that one decision to each period, so a
    # cluster cannot be drawn in the panel and pooled away in the split beside it.
    cells = cells_from(records, labels)
    drawn = pool_small_clusters(cells, show=opts.show_clusters)
    keep = {c.cluster for c in drawn}
    recent = relabel(cells_from([r for r in records if r.recent], labels), keep)
    baseline = relabel(cells_from([r for r in records if not r.recent], labels), keep)

    titles_by_record = {r.record_id: titles.get(strip_version(r.record_id), "") for r in records}
    species = {
        rid: resolve_species(r.taxid, titles_by_record[rid], taxonomy)
        for r in records
        if (rid := r.record_id)
    }
    placed_labels = {
        r.record_id: (DIVERGED if r.diverged else labels.get(r.record_id, UNPLACED))
        for r in records
        if r.evaluable
    }
    clusters = describe_clusters(
        drawn,
        {rid: (lab if lab in keep else OTHER) for rid, lab in placed_labels.items()},
        species,
        titles_by_record,
        {r.record_id: r.year for r in records},
        assay.citation.design_year,
        opts,
    )
    evaluable = sum(1 for r in records if r.evaluable)
    unplaced = sum(c.records for c in drawn if c.cluster == UNPLACED)
    diverged = sum(c.records for c in drawn if c.cluster == DIVERGED)
    notes = []
    if not labels and evaluable:
        notes.append("too few windows to cluster: every record is unplaced")
    if unplaced:
        notes.append(f"{unplaced} of {evaluable} records unplaced ({unplaced / evaluable:.0%})")
    if diverged:
        notes.append(f"{diverged} of {evaluable} diverged, with no site to cluster on")
    return AssayComposition(
        assay_id=assay.id,
        cut=cut,
        left_bp=shape[0],
        right_bp=shape[1],
        clusters=clusters,
        cells=tuple(drawn),
        observed=observed_series(drawn),
        same_mix=same_mix_series(drawn, min_covered=opts.same_mix_min_covered),
        split=split_change(baseline, recent, n_boot=opts.n_boot, seed=opts.boot_seed),
        species=tuple(
            species_years(
                [(r.taxid, r.year, titles_by_record[r.record_id]) for r in records if r.evaluable],
                taxonomy if taxonomy is not None else Taxonomy({}, {}),
                design_year=assay.citation.design_year,
            )
        ),
        note="; ".join(notes),
    )


def _archive(retrieved: Path, assay: Any, wanted: set[str]) -> tuple[dict[str, str], dict[str, str]]:
    """The sequences and titles of one assay's retrieval group, keyed by unversioned
    accession, for the records in `wanted`. A window archive holds only the stretches
    around the sites, which is what the mask removes, so it is skipped with a warning --
    the same rule `clustermaps` applies, for the same reason."""
    from assaywatch.fasta import read_fasta
    from assaywatch.groups import group_slug

    seqs: dict[str, str] = {}
    titles: dict[str, str] = {}
    if assay.target.taxid is None:
        return seqs, titles
    group = retrieved / str(assay.target.taxid) / group_slug(assay.target.query)
    if not group.is_dir():
        return seqs, titles
    for fasta in sorted(group.glob("*.fasta.gz")):
        if (fasta.parent / (fasta.name.removesuffix(".fasta.gz") + ".windows.tsv.gz")).exists():
            warnings.warn(
                f"{fasta} is a window archive; a composition window needs whole records, skipped",
                stacklevel=2,
            )
            continue
        for rid, seq in read_fasta(fasta):
            base = strip_version(rid)
            if base in wanted and base not in seqs:
                seqs[base] = seq.upper()
    for meta in sorted(group.glob("*.meta.tsv.gz")):
        with gzip.open(meta, "rt") as fh:
            header = (fh.readline() or "").rstrip("\n").split("\t")
            if "accession" not in header:
                continue
            ai = header.index("accession")
            ti = header.index("title") if "title" in header else None
            for line in fh:
                parts = line.rstrip("\n").split("\t")
                if len(parts) > ai and parts[ai] in wanted and ti is not None and len(parts) > ti:
                    titles.setdefault(parts[ai], parts[ti])
    return seqs, titles


def build(
    calls_path: Path,
    registry: Path,
    retrieved: Path,
    cfg: dict[str, Any],
    *,
    run_date: str | None = None,
    today: date | None = None,
    coverage: Mapping[str, Any] | None = None,
) -> CompositionRun:
    """Every assay's lineage composition for one run.

    Reads the calls table and the assessment inputs through `report`, so the records are
    the ones the graph counts and the scope filter, patent exclusion and `reduced` rule
    are the verdict's own (ROADMAP composition, decision A). `coverage` is the retrieval
    coverage of step 17, carried through untouched until that step fills it.

    Report-only: this returns a document and changes no status.
    """
    from assaywatch.drift import graph_records
    from assaywatch.report import assessment_inputs, load_calls_as_reported, read_dates
    from assaywatch.validate import iter_files, load_assay

    opts = Options.from_config(cfg)
    assays = {}
    for path in iter_files(registry):
        a = load_assay(path)
        if a.status.value != "deprecated":
            assays[a.id] = a
    calls = load_calls_as_reported(calls_path, assays, cfg)
    inputs = assessment_inputs(calls, assays, retrieved, cfg)
    dates = read_dates(retrieved)
    run_date = run_date or calls_path.parent.name
    if today is None:
        try:
            today = date.fromisoformat(run_date[:10])
        except ValueError:
            today = None
    records = graph_records(calls, dates, cfg, today=today, inputs=inputs)

    out: dict[str, AssayComposition] = {}
    for assay_id, rows in sorted(records.items()):
        assay = assays.get(assay_id)
        if assay is None:
            continue
        wanted = {strip_version(r.record_id) for r in rows}
        seqs, titles = _archive(retrieved, assay, wanted)
        out[assay_id] = build_assay(assay, rows, cfg, seqs, titles, inputs["taxonomy"], opts)
    del coverage  # step 17
    return CompositionRun(run_date=run_date, assays=out)


def main(argv: list[str] | None = None) -> int:
    import argparse
    import sys

    from assaywatch.composition import write
    from assaywatch.score import load_config

    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("calls", type=Path, help="Calls table (TSV.GZ) of one run")
    ap.add_argument("--registry", type=Path, default=Path("registry"))
    ap.add_argument("--retrieved", type=Path, default=Path("data/retrieved"))
    ap.add_argument("--config", type=Path, default=None)
    ap.add_argument("--run-date", default=None)
    ap.add_argument("--out", type=Path, required=True, help="where composition.tsv/.json go")
    args = ap.parse_args(argv)

    cfg = load_config(args.config)
    run = build(args.calls, args.registry, args.retrieved, cfg, run_date=args.run_date)
    tsv, js = write(run, args.out)
    placed = sum(1 for a in run.assays.values() if any(c.id >= 0 for c in a.clusters))
    print(
        f"{tsv} and {js}: {len(run.assays)} assays, {placed} with at least one cluster",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
