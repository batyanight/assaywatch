#!/usr/bin/env python3
"""Score one assay on a bench panel and show the mispair behind each 3'-window mismatch.

    efetch -db nuccore -format fasta -id "$(grep -v '^#' docs/bench-panels/forslund-1999-fap.tsv \
        | tail -n +2 | cut -f1 | paste -sd, -)" 2>/dev/null > panel.fasta
    python scripts/bench_panel.py --panel docs/bench-panels/forslund-1999-fap.tsv \
        --assay registry/PAPILLOMAVIRUS_dsDNA_L1_gene_Forslund_1999.yaml --fasta panel.fasta

A bench panel is a design paper's own test set: one genome per type or strain,
labelled with what the paper saw on the bench (a band or none). It is the only
truth the validation set has below the assay level, so it is where a scoring
rule can be checked type by type, not just assay by assay.

Each 3'-window mismatch is printed as primer:template pairs, one per base the
primer code stands for (a W opposite template G prints A:G/T:G). That is the
mispair identity Kwok et al. 1990 (doi:10.1093/nar/18.4.999) found dominates
the yield loss, which score_primer ignores (see its docstring).

The fetch runs through EDirect. Keep its stderr out of logs: on a failed query
it prints the request URL, API key included.
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
from pathlib import Path

from assaywatch.accession import strip_version
from assaywatch.fasta import read_fasta
from assaywatch.iupac import COMPLEMENT, IUPAC, MISMATCH, base_state, reverse_complement
from assaywatch.score import load_config
from assaywatch.screen import screen_records
from assaywatch.validate import load_assay


def read_panel(path: Path) -> dict[str, dict[str, str]]:
    """accession (unversioned) -> panel row. Lines starting with # are comments."""
    with path.open() as fh:
        rows = csv.DictReader((line for line in fh if not line.startswith("#")), delimiter="\t")
        return {strip_version(r["accession"]): r for r in rows}


def site_window(seq: str, site: str) -> str:
    """The record bases under a site such as '4901-4922+', read 5'->3' as the oligo is.

    Coordinates are 0-based, end-exclusive; a '-' site is reverse-complemented
    so position i lines up with oligo base i.
    """
    start, end = map(int, site[:-1].split("-"))
    win = seq[start:end]
    return reverse_complement(win) if site.endswith("-") else win


def window_mispairs(oligo: str, window: str, w3: int) -> list[tuple[int, str]]:
    """(distance from 3' end, 'P:T/...') for each definite mismatch within w3 of the 3' end.

    The primer pairs with the strand complementary to the record bases it reads
    as, so the template base facing primer base i is COMPLEMENT[window[i]].
    """
    out = []
    for i, (ob, tb) in enumerate(zip(oligo.upper(), window.upper(), strict=True)):
        d = len(oligo) - i
        if d <= w3 and base_state(ob, tb) == MISMATCH:
            template = COMPLEMENT.get(tb, "N")
            out.append((d, "/".join(f"{p}:{template}" for p in IUPAC[ob])))
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--panel", type=Path, required=True)
    ap.add_argument("--assay", type=Path, required=True)
    ap.add_argument("--fasta", type=Path, required=True)
    ap.add_argument(
        "--config",
        type=Path,
        default=None,
        help="scoring config; default config.yaml. For measuring a counterfactual "
        "(a chemistry override, a different reduced_max) without editing the real one",
    )
    args = ap.parse_args(argv)

    cfg = load_config(args.config)
    w3 = cfg["scoring"]["primer_3prime_window"]
    panel = read_panel(args.panel)
    assay = load_assay(args.assay)
    oligos = {"fwd": assay.oligos.forward.matching_seq, "rev": assay.oligos.reverse.matching_seq}
    seqs = {rid.split()[0]: s for rid, s in read_fasta(args.fasta) if strip_version(rid) in panel}
    missing = sorted(set(panel) - {strip_version(a) for a in seqs})
    if missing:
        print(f"not in --fasta: {', '.join(missing)}", file=sys.stderr)

    out = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    out.writerow(["accession", "label", "bench", "call", "penalty", "mispairs_3prime"])
    tally: Counter = Counter()
    for batch in screen_records([assay], list(seqs.items()), cfg):
        for rec in batch:
            for row in rec:
                p = panel[strip_version(row["record_id"])]
                pairs = []
                if row["call"] != "no_amplicon":
                    for k, oligo in oligos.items():
                        win = site_window(seqs[row["record_id"]], row[f"{k}_site"])
                        pairs += [f"{k}{d} {mp}" for d, mp in window_mispairs(oligo, win, w3)]
                out.writerow(
                    [
                        row["record_id"],
                        p["label"],
                        p["bench"],
                        row["call"],
                        row["penalty"],
                        "; ".join(pairs) or "-",
                    ]
                )
                tally[(p["bench"], row["call"])] += 1
    for (bench, call), n in sorted(tally.items()):
        print(f"{bench}\t{call}\t{n}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
