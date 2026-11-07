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

import dataclasses
import gzip
import json
import os
import re
import sys
import warnings
import zlib
from collections import defaultdict
from collections.abc import Callable, Mapping, Sequence
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
    lineage_narrative,
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
    coverage: Mapping[str, Mapping[int, int]] | None,
    sequences: Mapping[str, str],
    titles: Mapping[str, str],
    taxonomy: Taxonomy | None,
    opts: Options,
    *,
    collected: Mapping[str, int] | None = None,
    reference_of: Callable[[str], str | None] | None = None,
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
        [
            available_flank(seq, amp, stop_n_run=opts.stop_n_run, limit=2 * opts.flank_bp)
            for _, seq, amp, _ in spans
        ],
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
    comp = AssayComposition(
        assay_id=assay.id,
        cut=cut,
        left_bp=shape[0],
        right_bp=shape[1],
        clusters=clusters,
        cells=tuple(drawn),
        observed=observed_series(drawn),
        same_mix=same_mix_series(drawn, min_covered=opts.same_mix_min_covered),
        split=split_change(baseline, recent, n_boot=opts.n_boot, seed=opts.boot_seed),
        coverage={k: dict(v) for k, v in (coverage or {}).items()},
        species=tuple(
            species_years(
                [(r.taxid, r.year, titles_by_record[r.record_id]) for r in records if r.evaluable],
                taxonomy if taxonomy is not None else Taxonomy({}, {}),
                design_year=assay.citation.design_year,
            )
        ),
        note="; ".join(notes),
    )
    spikes = lineage_narrative(
        comp,
        records,
        titles=titles_by_record,
        collected=collected or {},
        reference_of=reference_of or (lambda _: None),
        opts=opts,
    )
    return dataclasses.replace(comp, spikes=tuple(spikes))


_FIELD = re.compile(r"^  (TITLE|JOURNAL)\s+(.*)$")


def first_reference(flatfile: str) -> str | None:
    """A GenBank flatfile's first REFERENCE as "title. journal", or None.

    A "Direct Submission" names no study: its JOURNAL line is the submitter's postal
    address, which this page has no business printing. So it reads as absent, as does a
    record with no REFERENCE at all.
    """
    fields: dict[str, list[str]] = {}
    current = None
    inside = False
    for line in flatfile.splitlines():
        if line.startswith("REFERENCE"):
            if inside:
                break
            inside = True
        elif inside and line[:1].strip():
            break
        elif inside:
            m = _FIELD.match(line)
            if m:
                current = m.group(1)
                fields[current] = [m.group(2).strip()]
            elif line.startswith(" " * 12) and current:
                fields[current].append(line.strip())
            else:
                current = None
    title = " ".join(fields.get("TITLE", []))
    journal = " ".join(fields.get("JOURNAL", []))
    if not title or title.lower() == "direct submission":
        return None
    return f"{title}. {journal}" if journal else title


def reference_lookup(
    transport: Callable[[str, dict[str, Any]], str] | None, cache: Path, *, max_failures: int
) -> Callable[[str], str | None]:
    """`reference_of` for `lineage_narrative`: one record's first REFERENCE, cached.

    Gzipped JSON like `.year-counts.json.gz`, accession -> text, with "" for a record read
    and found to name no study: that is an answer. A failure is not, so it stays uncached
    and reads as absent, and after `max_failures` in a row this stops asking, as
    `retrieve.AskLimit` does for the counts. `transport=None` is offline: the cache only.
    One base is asked for, since the references come with any slice and a whole assembly's
    flatfile is megabytes.
    """
    from assaywatch.retrieve import AskLimit

    store: dict[str, str] = {}
    if cache.exists():
        try:
            with gzip.open(cache, "rt") as fh:
                store = {str(k): str(v) for k, v in json.load(fh).items()}
        except (OSError, EOFError, zlib.error, ValueError):
            store = {}  # A corrupt cache is a cold cache.
    limit = AskLimit(max_failures)

    def look(accession: str) -> str | None:
        if accession in store:
            return store[accession] or None
        if transport is None or limit.tripped:
            return None
        try:
            text = transport(
                "efetch",
                {
                    "db": "nuccore",
                    "id": accession,
                    "rettype": "gb",
                    "retmode": "text",
                    "seq_start": 1,
                    "seq_stop": 1,
                },
            )
        except Exception as exc:  # noqa: BLE001 - any transport failure is "could not ask"
            limit.failed(exc)
            return None
        limit.consecutive = 0
        store[accession] = first_reference(text) or ""
        cache.parent.mkdir(parents=True, exist_ok=True)
        # Whole or not at all: a process killed mid-write must not leave a truncated cache.
        partial = cache.with_name(cache.name + f".{os.getpid()}.tmp")
        with gzip.open(partial, "wt") as fh:
            json.dump(store, fh, sort_keys=True)
        os.replace(partial, cache)
        return store[accession] or None

    return look


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
    taxon = retrieved / str(assay.target.taxid)
    # `asm` is the genomes `assemblies.taxa` adds, cut to the loci with `windows.buffer_bp`
    # of flank. They are real records in the graph, and without them Yersinia yst read
    # "every record is unplaced" on 35 of its 37. Short windows go by containment.
    groups = [g for g in (taxon / group_slug(assay.target.query), taxon / "asm") if g.is_dir()]
    fastas = [f for g in groups for f in sorted(g.glob("*.fasta.gz"))]
    metas = [m for g in groups for m in sorted(g.glob("*.meta.tsv.gz"))]
    for fasta in fastas:
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
    for meta in metas:
        with gzip.open(meta, "rt") as fh:
            header = (fh.readline() or "").rstrip("\n").split("\t")
            if "accession" not in header:
                continue
            ai = header.index("accession")
            ti = header.index("title") if "title" in header else None
            for line in fh:
                parts = line.rstrip("\n").split("\t")
                if len(parts) <= ai or ti is None or len(parts) <= ti:
                    continue
                base = strip_version(parts[ai])
                if base in wanted:
                    titles.setdefault(base, parts[ti])
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
    reference_of: Callable[[str], str | None] | None = None,
) -> CompositionRun:
    """Every assay's lineage composition for one run.

    Reads the calls table and the assessment inputs through `report`, so the records are
    the ones the graph counts and the scope filter, patent exclusion and `reduced` rule
    are the verdict's own (ROADMAP composition, decision A). `coverage` is the retrieval
    coverage of step 17, carried through untouched until that step fills it.

    Report-only: this returns a document and changes no status.
    """
    from assaywatch.drift import graph_records
    from assaywatch.metadata import read_collection_years
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
    # The calls table is the largest thing this stage holds (3.17 GB peak on the 2026-11-01
    # run) and nothing below reads it. Each assay's records go the same way once used.
    taxonomy = inputs["taxonomy"]
    del calls, inputs
    # Once for the run: this walks every `asm` archive. Null `report.collection_sidecar` is
    # the normal case today, and leaves only the assembly records' own dates.
    sidecar = (cfg.get("report") or {}).get("collection_sidecar")
    collected = read_collection_years(
        retrieved,
        {r.record_id for rows in records.values() for r in rows},
        sidecar=Path(sidecar) if sidecar else None,
    )

    out: dict[str, AssayComposition] = {}
    total = len(records)
    for i, assay_id in enumerate(sorted(records), start=1):
        rows = records.pop(assay_id)
        print(f"composition {i}/{total} {assay_id}: {len(rows)} records", file=sys.stderr, flush=True)
        assay = assays.get(assay_id)
        if assay is None:
            continue
        wanted = {strip_version(r.record_id) for r in rows}
        seqs, titles = _archive(retrieved, assay, wanted)
        out[assay_id] = build_assay(
            assay,
            rows,
            cfg,
            _coverage_for(coverage, assay_id),
            seqs,
            titles,
            taxonomy,
            opts,
            collected=collected,
            reference_of=reference_of,
        )
    return CompositionRun(run_date=run_date, assays=out)


def _coverage_for(coverage: Mapping[str, Any] | None, assay_id: str) -> dict[str, dict[int, int]]:
    """One assay's rows of `retrieve --year-counts`, with years as ints."""
    rows = ((coverage or {}).get("assays") or {}).get(assay_id) or {}
    return {k: {int(y): int(n) for y, n in (v or {}).items()} for k, v in rows.items()}


def main(argv: list[str] | None = None) -> int:
    import argparse

    from assaywatch.composition import write
    from assaywatch.score import load_config

    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("calls", type=Path, help="Calls table (TSV.GZ) of one run")
    ap.add_argument("--registry", type=Path, default=Path("registry"))
    ap.add_argument("--retrieved", type=Path, default=Path("data/retrieved"))
    ap.add_argument("--config", type=Path, default=None)
    ap.add_argument("--run-date", default=None)
    ap.add_argument("--out", type=Path, required=True, help="where composition.tsv/.json go")
    ap.add_argument(
        "--coverage",
        type=Path,
        help="coverage.json from `assaywatch retrieve --year-counts`: the retrieval-coverage series",
    )
    ap.add_argument(
        "--email",
        default=None,
        help="contact for NCBI, to read a spike batch's REFERENCE; without it, the cache only",
    )
    args = ap.parse_args(argv)

    cfg = load_config(args.config)
    coverage = None
    if args.coverage is not None and args.coverage.exists():
        coverage = json.loads(args.coverage.read_text())
    transport = None
    if args.email:
        from assaywatch.credentials import ncbi_api_key
        from assaywatch.retrieve import http_transport

        transport = http_transport(args.email, ncbi_api_key() or None)
    reference_of = reference_lookup(
        transport,
        Path(cfg.get("retrieved_dir", "data/retrieved")) / ".references.json.gz",
        max_failures=int((cfg.get("composition") or {}).get("coverage_max_failures", 5)),
    )
    run = build(
        args.calls,
        args.registry,
        args.retrieved,
        cfg,
        run_date=args.run_date,
        coverage=coverage,
        reference_of=reference_of,
    )
    tsv, js = write(run, args.out)
    placed = sum(1 for a in run.assays.values() if any(c.id >= 0 for c in a.clusters))
    print(
        f"{tsv} and {js}: {len(run.assays)} assays, {placed} with at least one cluster",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
