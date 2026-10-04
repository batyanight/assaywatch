"""Do indel-containing records matter? Measure it before building gapped scoring.

    python scripts/indel_check.py --out results/indel_check/2026-10-04

The screen is ungapped by design (see assaywatch/match.py). This script samples
the calls an indel could plausibly have changed and asks, with a gapped search
(assaywatch/gapped.py), whether one did:

* `fail`: both primers bound, so the binding sites are known. For each oligo,
  is the site near-perfect apart from one single-base indel (one indel, at most
  one mismatch, and at least two edits cheaper than the ungapped placement), and
  would the call clear `reduced_max` if that indel were forgiven?
* `no_amplicon` with one primer found: is there a near-perfect gapped site for
  the missing primer (one indel, at most one mismatch) that pairs with a found
  partner site in orientation and size range?

"Forgiving" is deliberately narrow. A gapped aligner will happily trade two
indels for five mismatches; counting that as an indel problem would blame
indels for sites that are simply diverged. Only a site that is clean except for
one indel counts.

Every hit is also labelled with where the indel sits: within the 3' window
(`primer_3prime_window`, where an indel kills extension whatever the model
says, so these are real failures), and whether it is in a homopolymer run of
three or more in the oligo, the signature of a sequencing artefact
(pyrosequencing, Ion Torrent, nanopore) rather than biology.

Records with neither primer are not sampled: nothing anchors them, and the
group-level retrieval puts many records in an archive that do not cover the
amplicon at all.

Sampling is per (assay, category), up to --per-assay records, with a fixed seed.
Counts are scaled back to each assay's total in that category, and the summary
compares the estimated indel-only failures with the assay's evaluable records
(detect + reduced + fail), which is the denominator the drift numbers use.
"""

from __future__ import annotations

import argparse
import csv
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from assaywatch.fasta import read_fasta  # noqa: E402
from assaywatch.gapped import align, hamming_scan, scan  # noqa: E402
from assaywatch.iupac import reverse_complement  # noqa: E402
from assaywatch.match import find_sites  # noqa: E402
from assaywatch.score import load_config  # noqa: E402
from assaywatch.validate import iter_files, load_assay  # noqa: E402

PAD = 4  # bases either side of a known site searched for a gapped placement


def category(row: dict[str, str]) -> str | None:
    if row["call"] == "fail":
        return "fail"
    if row["call"] == "no_amplicon":
        if row["reason"].startswith("no forward site within"):
            return "no_forward"
        if row["reason"].startswith("no reverse site within"):
            return "no_reverse"
    return None


def sample_calls(screened: Path, per_assay: int, seed: int):
    """Reservoir-sample rows per (assay, category); also count every call."""
    rng = random.Random(seed)
    seen: Counter = Counter()
    totals: Counter = Counter()
    picked: dict[tuple[str, str], list] = defaultdict(list)
    for tsv in sorted(screened.rglob("*.tsv")):
        rel = tsv.relative_to(screened)
        archive = Path(*rel.parts[:-1]) / (rel.name[: -len(".tsv")] + ".fasta.gz")
        with tsv.open(newline="") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                totals[(row["assay_id"], row["call"])] += 1
                cat = category(row)
                if cat is None:
                    continue
                key = (row["assay_id"], cat)
                seen[key] += 1
                item = (archive, row)
                if len(picked[key]) < per_assay:
                    picked[key].append(item)
                else:
                    k = rng.randrange(seen[key])
                    if k < per_assay:
                        picked[key][k] = item
    return picked, seen, totals


def oligo_windows(assay, row, seq):
    """(name, oligo, window, ungapped cost) for each oligo of a `fail` call, oriented like the oligo."""
    s, e = int(row["amplicon_start"]), int(row["amplicon_end"])
    fwd = assay.oligos.forward.matching_seq
    rev = assay.oligos.reverse.matching_seq
    out = []
    w = seq[max(0, s - PAD) : s + len(fwd) + PAD]
    out.append(("forward", fwd, w))
    w = reverse_complement(seq[max(0, e - len(rev) - PAD) : e + PAD])
    out.append(("reverse", rev, w))
    if assay.oligos.probe is not None:
        probe = assay.oligos.probe.matching_seq
        inner = seq[s + len(fwd) : e - len(rev)]
        # Either strand; keep the orientation where the probe fits best.
        best = min((inner, reverse_complement(inner)), key=lambda x: int(scan(probe, x).min()) if x else 99)
        out.append(("probe", probe, best))
    result = []
    for name, oligo, window in out:
        h = hamming_scan(oligo, window)
        result.append((name, oligo, window, int(h.min()) if len(h) else len(oligo)))
    return result


def clean_indel(a, ungapped: int) -> bool:
    """One indel, at most one mismatch, and clearly better than the ungapped site."""
    return a.n_indels == 1 and len(a.mismatches) <= 1 and a.cost <= ungapped - 2


def in_homopolymer(oligo: str, from3: int) -> bool:
    """Is oligo position `from3` (1 = 3' end) inside a run of >= 3 identical bases?"""
    i = len(oligo) - from3
    lo = hi = i
    while lo > 0 and oligo[lo - 1] == oligo[i]:
        lo -= 1
    while hi < len(oligo) - 1 and oligo[hi + 1] == oligo[i]:
        hi += 1
    return hi - lo + 1 >= 3


def indel_labels(oligo, a, cfg):
    d = (a.insertions + a.deletions)[0]
    return {
        "indel_in_3prime_window": d <= cfg["scoring"]["primer_3prime_window"],
        "indel_in_homopolymer": in_homopolymer(oligo, d),
    }


def check_fail(assay, row, seq, cfg):
    """Would this `fail` clear reduced_max if one clean single-base indel were forgiven?"""
    sc = cfg["scoring"]
    findings = []
    total, terminal, any_indel = 0.0, False, False
    for name, oligo, window, ungapped in oligo_windows(assay, row, seq):
        a = align(oligo, window)
        use_gapped = clean_indel(a, ungapped)
        mm = a.mismatches if use_gapped else None
        if use_gapped:
            any_indel = True
            findings.append(
                {
                    "oligo": name,
                    "ungapped_cost": ungapped,
                    "gapped_cost": a.cost,
                    "indels_from_3prime": ",".join(map(str, sorted(a.insertions + a.deletions))),
                    "mismatches_from_3prime": ",".join(map(str, a.mismatches)),
                    **indel_labels(oligo, a, cfg),
                }
            )
        else:
            # Reuse the ungapped mismatch positions the screen reported.
            col = {"forward": "fwd", "reverse": "rev", "probe": "probe"}[name]
            mm = tuple(int(x) for x in row[f"{col}_mm_from_3prime"].split(",") if x)
        if name == "probe":
            L = len(oligo)
            for d in mm:
                pos = L - d
                total += sc["probe_center_penalty"] if L / 3 <= pos < 2 * L / 3 else sc["probe_outer_penalty"]
        else:
            for d in mm:
                terminal |= d == 1
                w3, wmid = sc["primer_3prime_window"], sc["primer_mid_window"]
                total += (
                    sc["primer_3prime_penalty"]
                    if d <= w3
                    else sc["primer_mid_penalty"]
                    if d <= w3 + wmid
                    else sc["primer_5prime_penalty"]
                )
    if not any_indel:
        return None
    in3 = any(o["indel_in_3prime_window"] for o in findings)
    rescued = (
        total <= sc["reduced_max"] and not (terminal and sc.get("terminal_mismatch_fails", True)) and not in3
    )
    return {"rescued_if_indel_forgiven": rescued, "penalty_without_indels": total, "oligos": findings}


def check_missing(assay, row, seq, cat, cfg, max_cost):
    """Is the missing primer there with an indel, paired with a found partner in range?"""
    amp = cfg["amplicon"]
    fwd = assay.oligos.forward.matching_seq
    rev = assay.oligos.reverse.matching_seq
    if cat == "no_reverse":
        partners = [s for s in find_sites(fwd, seq, 6) if s.strand == "+"]
        # The reverse primer's sequence appears on the minus strand: scan the reverse complement.
        costs = scan(rev, reverse_complement(seq))
        n = len(seq)
        hits = [
            (int(c), n - j) for j, c in enumerate(costs.tolist()) if c <= max_cost
        ]  # start on plus strand
        pairs = [
            (c, p.start, st + len(rev))
            for c, st in hits
            for p in partners
            if amp["min_bp"] <= st + len(rev) - p.start <= amp["max_bp"]
        ]
        oligo, missing = rev, "reverse"
    else:
        partners = [s for s in find_sites(rev, seq, 6) if s.strand == "-"]
        costs = scan(fwd, seq)
        hits = [(int(c), j) for j, c in enumerate(costs.tolist()) if c <= max_cost]  # end on plus strand
        pairs = [
            (c, j - len(fwd), p.end)
            for c, j in hits
            for p in partners
            if amp["min_bp"] <= p.end - (j - len(fwd)) <= amp["max_bp"]
        ]
        oligo, missing = fwd, "forward"
    if not pairs:
        return None
    c, s, e = min(pairs)
    # Re-align in a small window to locate the indel(s).
    if missing == "forward":
        window = seq[max(0, s - PAD) : s + len(oligo) + 2 * PAD]
    else:
        window = reverse_complement(seq[max(0, e - len(oligo) - 2 * PAD) : e + PAD])
    a = align(oligo, window)
    if a.n_indels != 1 or len(a.mismatches) > 1:
        return None
    return {
        **indel_labels(oligo, a, cfg),
        "oligo": missing,
        "gapped_cost": a.cost,
        "indels_from_3prime": ",".join(map(str, sorted(a.insertions + a.deletions))),
        "mismatches_from_3prime": ",".join(map(str, a.mismatches)),
        "amplicon_bp": e - s,
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--registry", type=Path, default=ROOT / "registry")
    ap.add_argument("--screened", type=Path, default=ROOT / "results" / "screened")
    ap.add_argument("--retrieved", type=Path, default=ROOT / "data" / "retrieved")
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--per-assay", type=int, default=300)
    ap.add_argument(
        "--max-cost", type=int, default=2, help="edit cost for a missing primer's gapped site (<= 2)"
    )
    ap.add_argument("--max-record-bp", type=int, default=2_000_000, help="skip longer records (genomes)")
    ap.add_argument("--seed", type=int, default=1)
    args = ap.parse_args(argv)

    cfg = load_config()
    assays = {a.id: a for a in (load_assay(p) for p in iter_files(args.registry))}
    picked, seen, totals = sample_calls(args.screened, args.per_assay, args.seed)

    wanted: dict[Path, set[str]] = defaultdict(set)
    for items in picked.values():
        for archive, row in items:
            wanted[archive].add(row["record_id"])
    seqs: dict[tuple[Path, str], str] = {}
    for archive, ids in sorted(wanted.items()):
        for rid, seq in read_fasta(args.retrieved / archive):
            if rid in ids:
                seqs[(archive, rid)] = seq
        print(f"read {archive}: {len(ids)} records wanted", file=sys.stderr)

    args.out.mkdir(parents=True, exist_ok=True)
    flagged = []
    n_checked: Counter = Counter()
    n_hit: Counter = Counter()
    n_rescued: Counter = Counter()
    pos_hist: Counter = Counter()
    for (aid, cat), items in sorted(picked.items()):
        assay = assays.get(aid)
        if assay is None:
            continue
        for archive, row in items:
            seq = seqs.get((archive, row["record_id"]))
            if seq is None or len(seq) > args.max_record_bp:
                continue
            n_checked[(aid, cat)] += 1
            if cat == "fail":
                res = check_fail(assay, row, seq, cfg)
                if res is None:
                    continue
                n_hit[(aid, cat)] += 1
                n_rescued[(aid, cat)] += res["rescued_if_indel_forgiven"]
                for o in res["oligos"]:
                    for d in o["indels_from_3prime"].split(","):
                        pos_hist[(o["oligo"], int(d))] += 1
                    flagged.append(
                        {
                            "assay_id": aid,
                            "category": cat,
                            "record_id": row["record_id"],
                            "archive": str(archive),
                            "rescued_if_indel_forgiven": res["rescued_if_indel_forgiven"],
                            **o,
                        }
                    )
            else:
                res = check_missing(assay, row, seq, cat, cfg, args.max_cost)
                if res is None:
                    continue
                n_hit[(aid, cat)] += 1
                rescued = not res["indel_in_3prime_window"] and 1 not in [
                    int(x) for x in res["mismatches_from_3prime"].split(",") if x
                ]
                n_rescued[(aid, cat)] += rescued
                for d in res["indels_from_3prime"].split(","):
                    if d:
                        pos_hist[(res["oligo"], int(d))] += 1
                flagged.append(
                    {
                        "assay_id": aid,
                        "category": cat,
                        "record_id": row["record_id"],
                        "archive": str(archive),
                        "rescued_if_indel_forgiven": rescued,
                        **res,
                    }
                )

    cols = [
        "assay_id",
        "category",
        "record_id",
        "archive",
        "oligo",
        "ungapped_cost",
        "gapped_cost",
        "indels_from_3prime",
        "mismatches_from_3prime",
        "amplicon_bp",
        "indel_in_3prime_window",
        "indel_in_homopolymer",
        "rescued_if_indel_forgiven",
    ]
    with (args.out / "flagged.tsv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t", extrasaction="ignore")
        w.writeheader()
        w.writerows(flagged)

    # Per assay: estimated indel-only failures as a share of evaluable records.
    rows = []
    for aid in sorted({a for a, _ in seen}):
        evaluable = sum(totals[(aid, c)] for c in ("detect", "reduced", "fail"))
        est = {}
        for cat in ("fail", "no_forward", "no_reverse"):
            k = (aid, cat)
            est[cat] = seen[k] * n_rescued[k] / n_checked[k] if n_checked[k] else 0.0
        detect = totals[(aid, "detect")] + totals[(aid, "reduced")]
        rows.append(
            {
                "assay_id": aid,
                "evaluable": evaluable,
                "working": detect,
                "est_fail_indel_only": round(est["fail"], 1),
                "est_new_amplicons": round(est["no_forward"] + est["no_reverse"], 1),
                "checked": sum(n_checked[(aid, c)] for c in ("fail", "no_forward", "no_reverse")),
                "hits": sum(n_hit[(aid, c)] for c in ("fail", "no_forward", "no_reverse")),
            }
        )
    with (args.out / "per_assay.tsv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]), delimiter="\t")
        w.writeheader()
        w.writerows(rows)
    with (args.out / "indel_position.tsv").open("w") as fh:
        fh.write("oligo\tfrom_3prime\tcount\n")
        for (o, d), c in sorted(pos_hist.items()):
            fh.write(f"{o}\t{d}\t{c}\n")

    tot_ck = sum(n_checked.values())
    print(
        f"checked {tot_ck} sampled calls; {sum(n_hit.values())} with an indel; "
        f"{sum(n_rescued.values())} would change if the indel were forgiven",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
