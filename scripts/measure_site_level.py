#!/usr/bin/env python3
"""How much evidence the amplicon-level rule discards, and how much of it is judgeable.

    python scripts/measure_site_level.py --assay CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004

Phase 1 of the Bd-miss plan (`docs/2026-10-23-wave3-bd-miss.md`, "the fix this points
to"). **Measures only. Changes no call, no verdict and no config.**

THE QUESTION. A record is scored only if it holds the whole amplicon, so a deposit that
stops short of one primer is `truncated` and leaves the denominator entirely - a fact
"about the deposit, not the assay". The Bd case is three records that carry the probe
site with a 1-substitution-plus-2-nt-deletion at its 3' end, deposited years before the
as-of date, discarded twice over: once for being amplicon-level and once because
`match.py` is ungapped. So: of the records the amplicon rule discards, how many actually
carry a judgeable oligo site, and how many of those would fail?

WHY THIS CANNOT BE REPLAYED, measured rather than assumed. No `no_amplicon` row in
`results/2026-10-26/calls.tsv.gz` carries any site coordinate - `fwd_site`, `rev_site`
and `probe_site` are empty on all 1,789,100 of them, because there is no winning
amplicon to write them from. So the population can be COUNTED from the table by
exclusion class, but nothing about where its sites sit can be read off it. This script
therefore re-finds the sites from the archives.

HOW A PROBE SITE IS LOCATED WITHOUT ITS AMPLICON. The design doc names this as the first
open question, and the answer used here is the one the Bd investigation used: anchor on
whichever primer IS credible, and place the probe by its measured offset from that
anchor in a full-amplicon reference. This script takes the offset from the assay's own
detecting records rather than from one hand-picked reference, so the anchor is the
assay's own geometry. Where an assay has no detects, it is skipped and said so.

WHAT IS DELIBERATELY NOT DONE. No verdict is computed, no failure share is reported as a
coverage figure, and nothing is written to `results/`. The multiplicity problem wave 2
found applies with force to a 15-mer probe, and a site-level failure share would need its
own credibility test before it could mean anything. This counts what is reachable.
"""

from __future__ import annotations

import argparse
import collections
import csv
import gzip
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from assaywatch.accession import strip_version
from assaywatch.chance import composition, site_evalue
from assaywatch.fasta import read_fasta
from assaywatch.gapped import align
from assaywatch.groups import group_slug
from assaywatch.match import find_sites
from assaywatch.score import load_config, score_probe
from assaywatch.validate import iter_files, load_assay

REPO = Path(__file__).resolve().parents[1]
REACHABLE = ("truncated", "diverged", "no_pair")


def archives_for(assay, retrieved: Path) -> list[Path]:
    """The FASTA archives of this assay's retrieval group."""
    slug = group_slug(assay.target.query)
    d = retrieved / str(assay.target.taxid) / slug
    return sorted(d.glob("*.fasta.gz")) if d.is_dir() else []


def wanted_rows(calls: Path, assay_id: str) -> dict[str, str]:
    """Unversioned accession -> exclusion label, for the rows the amplicon rule discards."""
    out = {}
    with gzip.open(calls, "rt") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            if r["assay_id"] == assay_id and r["call"] == "no_amplicon" and r["exclusion"] in REACHABLE:
                out[strip_version(r["record_id"])] = r["exclusion"]
    return out


def probe_offsets(assay, seqs: dict[str, str], cfg: dict[str, Any], limit: int = 200) -> list[int]:
    """The probe's measured offset from the reverse site, over records that hold both.

    Taken from the assay's OWN geometry rather than from one hand-picked reference
    record, which is the only part of the Bd investigation's method that was not
    reproducible.
    """
    fwd = assay.oligos.forward.matching_seq
    rev = assay.oligos.reverse.matching_seq
    probe = assay.oligos.probe.matching_seq
    mm = int(cfg["scoring"]["max_mismatches_searched"])
    offsets = []
    for seq in list(seqs.values())[:limit]:
        f = [s for s in find_sites(fwd, seq, mm) if s.n_mismatches == 0]
        r = [s for s in find_sites(rev, seq, mm) if s.n_mismatches == 0]
        p = [s for s in find_sites(probe, seq, mm) if s.n_mismatches <= 1]
        if f and r and p:
            offsets.append(p[0].start - r[0].start)
    return offsets


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument(
        "--assay", action="append", default=[], help="assay id; repeatable. default: all probe-bearing"
    )
    ap.add_argument("--calls", type=Path, default=REPO / "results" / "2026-10-26" / "calls.tsv.gz")
    ap.add_argument("--retrieved", type=Path, default=REPO / "data" / "retrieved")
    ap.add_argument("--registry", type=Path, default=REPO / "registry")
    ap.add_argument("--config", type=Path, default=None)
    ap.add_argument("--cap", type=int, default=4000, help="most discarded records to examine per assay")
    args = ap.parse_args(argv)

    cfg = load_config(args.config)
    assays = {a.id: a for a in map(load_assay, iter_files(args.registry))}
    chosen = args.assay or [i for i, a in assays.items() if a.oligos.probe]

    print("Records the amplicon rule discards, and how many carry a JUDGEABLE probe site.")
    print("judgeable = the probe's whole footprint lies inside the deposited sequence.")
    print()
    hdr = f"{'assay':52} {'discarded':>9} {'examined':>8} {'probe in':>8} {'cut':>6} {'outside':>7} {'fails':>6} {'indel':>6}"
    print(hdr)
    print("-" * len(hdr))

    totals: collections.Counter = collections.Counter()
    for aid in chosen:
        assay = assays[aid]
        if not assay.oligos.probe:
            continue
        rows = wanted_rows(args.calls, aid)
        if not rows:
            continue
        archives = archives_for(assay, args.retrieved)
        seqs = {}
        for f in archives:
            for rid, s in read_fasta(f):
                seqs[strip_version(rid.split()[0])] = s
        offs = probe_offsets(assay, seqs, cfg)
        if not offs:
            print(
                f"{aid[:52]:52} {len(rows):>9,} {'-':>8}   no record holds all three sites; offset unmeasurable",
                flush=True,
            )
            totals["skipped"] += 1
            continue
        offset = collections.Counter(offs).most_common(1)[0][0]

        rev = assay.oligos.reverse.matching_seq
        fwd = assay.oligos.forward.matching_seq
        probe = assay.oligos.probe.matching_seq
        mm = int(cfg["scoring"]["max_mismatches_searched"])
        max_e = float(cfg["scoring"].get("max_site_evalue", 0.01))
        seen = inside = cut = outside = failing = indel = 0
        for acc in list(rows)[: args.cap]:
            seq = seqs.get(acc)
            if seq is None:
                continue
            seen += 1
            comp = composition(seq)
            anchor = None
            for oligo in (rev, fwd):
                cands = [
                    s
                    for s in find_sites(oligo, seq, mm)
                    if site_evalue(oligo, s.n_mismatches + s.n_ambiguous, len(seq), comp) <= max_e
                ]
                if cands:
                    anchor = (oligo, sorted(cands, key=lambda s: s.n_mismatches)[0])
                    break
            if anchor is None:
                continue
            oligo, site = anchor
            start = site.start + offset if oligo is rev else site.start - offset
            if start < 0 or start + len(probe) > len(seq):
                if start + len(probe) <= 0 or start >= len(seq):
                    outside += 1
                else:
                    cut += 1
                continue
            inside += 1
            # Judge the probe where it is present. Ungapped first, as the pipeline does.
            found = [s for s in find_sites(probe, seq, mm) if abs(s.start - start) <= 5]
            if not found:
                # Present by geometry but not matchable within the search budget: the
                # strongest form of "this site would fail", and exactly what an ungapped
                # matcher reports for a deletion.
                failing += 1
                # `gapped.align` is the measurement spike built for exactly this
                # question and documented as never scored. Used here to ASK whether an
                # indel explains the failure, not to decide anything.
                if align(probe, seq[max(0, start - 5) : start + len(probe) + 5]).cost <= 3:
                    indel += 1
                continue
            sc = score_probe(found[0], probe, cfg)
            if sc.penalty > cfg["scoring"]["reduced_max"]:
                failing += 1
        # flush=True because this run takes tens of minutes and its stdout is normally
        # redirected to a file, where Python buffers everything and the run looks hung
        # from outside while it is working perfectly well.
        print(
            f"{aid[:52]:52} {len(rows):>9,} {seen:>8,} {inside:>8,} {cut:>6,} "
            f"{outside:>7,} {failing:>6,} {indel:>6,}",
            flush=True,
        )
        for k, v in (
            ("discarded", len(rows)),
            ("examined", seen),
            ("inside", inside),
            ("cut", cut),
            ("outside", outside),
            ("failing", failing),
            ("indel", indel),
        ):
            totals[k] += v
    print("-" * len(hdr))
    print(
        f"{'TOTAL':52} {totals['discarded']:>9,} {totals['examined']:>8,} {totals['inside']:>8,} "
        f"{totals['cut']:>6,} {totals['outside']:>7,} {totals['failing']:>6,} {totals['indel']:>6,}"
    )
    if totals["skipped"]:
        print(f"({totals['skipped']} assays skipped: no record holds all three sites, so no offset)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
