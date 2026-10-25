"""Is a questionable amplicon the assay's locus at all? Measures, decides nothing.

    python scripts/measure_locus_identity.py <assay_id> [<assay_id> ...]

The evidence behind `docs/2026-10-25-locus-identity-design.md`, kept so the numbers
in it can be re-run rather than quoted. For one assay it takes the interiors of the
amplicons found in records that `detect` - trimming 20 bp off each end so the primer
sites themselves cannot contribute - and scores every failing record's interior as
its best ungapped identity, both strands, against five of them.

Measured 2026-10-25: chance pairs land at 0.32-0.44 and real loci at 0.60 and
above, on conventional assays as well as probe ones. The ceiling is
RETROVIRUS_RNA_polymerase_SIV_Takehisa_2009, whose genuinely divergent failures sit
at 0.63-0.65, so 0.70 would discard real drift.

Two things it cannot do, both recorded in the design doc. An assay with a short
amplicon has too little interior to judge: RANAVIRUS_..._MCP_Pallister_2007 is 57 bp
and leaves 17 after trimming, so it returns nothing rather than a weak number. And
the `chance`/`genuine` split printed here is a crude stand-in - probe absent with
both primers past `reduced_max` - which mis-binned six lyssavirus rows that are
really chance pairs on one marginal anchor. Read the amplicon lengths beside it: a
real locus gives one length, and those six gave 143 to 1791 bp.

Reads only the latest screen per group and the archives; writes nothing.
"""

import csv
import glob
import gzip
import os
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from assaywatch.accession import strip_version

root = "/Users/batya/assaywatch"


def rc(s):
    return s.translate(str.maketrans("ACGTNRYSWKMBDHV", "TGCANYRSWMKVHDB"))[::-1]


def latest(pat):
    d = {}
    for fp in glob.glob(pat):
        g = os.path.dirname(fp)
        if g not in d or os.path.basename(fp) > os.path.basename(d[g]):
            d[g] = fp
    return list(d.values())


def rows_for(assay, calls=None):
    """Rows for one assay, from the run's collected calls table.

    NOT from globbing results/screened/*/*/: that directory keeps the screens of
    ORPHAN groups, which no live assay retrieves any more and which are therefore
    never rescreened. Measured 2026-10-25: the Rhabdoviridae orphan group
    11270/all still holds a screen dated 2026-10-03, eleven days before
    amplicon.declared_tolerance shipped, and its 46,404 rows carry amplicon
    lengths of 51-2996 bp against a declared 373 - lengths the current screener
    cannot produce. Reading it as current inflated this measurement's chance-pair
    counts about a hundredfold. collect_calls is what the report uses, so it is
    what a measurement quoted beside the report must use.
    """
    path = calls or (root + "/results/2026-10-25/calls.tsv.gz")
    op = gzip.open if str(path).endswith(".gz") else open
    out = []
    with op(path, "rt") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            if r["assay_id"] == assay and r["call"] in ("detect", "reduced", "fail"):
                out.append(r)
    return out


def seqs_for(accs):
    want = {strip_version(a) for a in accs}
    got = {}
    for fp in glob.glob(root + "/data/retrieved/*/*/*.fasta.gz"):
        if not want - got.keys():
            break
        try:
            fh = gzip.open(fp, "rt")
        except OSError:
            continue
        with fh:
            acc = None
            buf = []
            for ln in fh:
                if ln.startswith(">"):
                    if acc in want and acc not in got:
                        got[acc] = "".join(buf)
                    acc = strip_version(ln[1:].split()[0])
                    buf = []
                else:
                    buf.append(ln.strip())
            if acc in want and acc not in got:
                got[acc] = "".join(buf)
    return got


def interior(seq, s, e, trim):
    try:
        a, b = int(s), int(e)
    except (TypeError, ValueError):
        return None
    if a > b:
        a, b = b, a
    amp = seq[max(0, a) : b].upper()
    if len(amp) <= 2 * trim + 20:
        return None
    return amp[trim:-trim]


def ident(a, b):
    """Best ungapped identity of the shorter against the longer, both strands."""
    if not a or not b:
        return 0.0
    best = 0.0
    for t in (b, rc(b)):
        if len(a) > len(t):
            a, t = t, a
        for off in range(0, len(t) - len(a) + 1):
            m = sum(1 for x, y in zip(a, t[off : off + len(a)], strict=False) if x == y)
            best = max(best, m / len(a))
    return best


for assay in sys.argv[1:]:
    rs = rows_for(assay)
    if not rs:
        print(f"\n=== {assay}: no rows")
        continue
    seqs = seqs_for([r["record_id"] for r in rs])
    det = []
    fails = []
    for r in rs:
        s = seqs.get(strip_version(r["record_id"]))
        if not s:
            continue
        it = interior(s, r.get("amplicon_start"), r.get("amplicon_end"), 20)
        if not it or len(it) > 3000:
            continue
        (det if r["call"] in ("detect", "reduced") else fails).append((r, it))
    if not det:
        print(f"\n=== {assay}: no reference interiors")
        continue
    refs = [it for _, it in random.Random(0).sample(det, min(5, len(det)))]

    def score(it, refs=refs):
        return max(ident(it, rf) for rf in refs)

    ds = [score(it) for _, it in random.Random(1).sample(det, min(40, len(det)))]
    fs = []
    for r, it in random.Random(2).sample(fails, min(60, len(fails))):
        probeless = (r.get("probe_site") or "-") in ("-", "")
        try:
            hi = float(r["fwd_penalty"]) > 3.0 and float(r["rev_penalty"]) > 3.0
        except (ValueError, KeyError):
            hi = False
        fs.append((score(it), "chance" if (probeless and hi) else "genuine"))

    def st(v):
        v = sorted(v)
        return f"n={len(v):3d} min={v[0]:.2f} p50={v[len(v) // 2]:.2f} max={v[-1]:.2f}" if v else "n=0"

    print(f"\n=== {assay}")
    print(f"  detect/reduced interiors : {st(ds)}")
    print(f"  fail, chance-pair shaped : {st([x for x, k in fs if k == 'chance'])}")
    print(f"  fail, genuine shaped     : {st([x for x, k in fs if k == 'genuine'])}")
    gen = [x for x, k in fs if k == "genuine"]
    ch = [x for x, k in fs if k == "chance"]
    for thr in (0.50, 0.55, 0.60, 0.70):
        lost = sum(1 for x in gen if x < thr)
        kept = sum(1 for x in ch if x >= thr)
        print(f"    threshold {thr:.2f}: genuine LOST {lost}/{len(gen)}, chance KEPT {kept}/{len(ch)}")
    # the low genuine tail, with its penalties, to see whether it is really genuine
    low = [
        (x, r)
        for (x, k), (r, _it) in zip(fs, random.Random(2).sample(fails, min(60, len(fails))), strict=True)
        if k == "genuine" and x < 0.60
    ]
    for x, r in sorted(low)[:6]:
        print(
            f"    low genuine: id={x:.2f} {r['record_id']:14s} fwd={r['fwd_penalty']:>4} rev={r['rev_penalty']:>4} probe={(r.get('probe_site') or '-')[:10]:10s} bp={r.get('amplicon_bp')}"
        )
