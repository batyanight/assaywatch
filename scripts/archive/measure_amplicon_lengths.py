"""Amplicon length against the assay's declared size. Measures, decides nothing.

    python scripts/measure_amplicon_lengths.py <assay_id> [<assay_id> ...]

The evidence that amplicon length is a DIAGNOSTIC AND NOT A FILTER
(docs/journal/2026-10-25-stale-orphan-screens.md). Measured 2026-10-25 from the run's
collected calls: Orf's chance pairs are all at exactly 62 bp against a declared 68,
one length rather than scatter; OPHIDIOMYCES targetD's span 56-69 against 57 with
63% inside 5 bp, so a length rule would keep most of the rows behind the one wrong
active verdict; and West African mpox's genuine clade-I failures are all 82 bp
against a declared 85, so strict equality would delete the finding the locus work
exists to protect. amplicon.declared_tolerance already does the coarse version of
this job and is the one number in config.yaml with a measured defence.

It reads results/<run>/calls.tsv.gz, never a glob over results/screened/: that
directory keeps ORPHAN group screens written under months-old scoring rules, and
reading them as current is what made length look powerful in the first place.
"""

import collections
import csv
import glob
import gzip
import statistics
import sys
from pathlib import Path

import yaml

# The repo root, from this file's own location, so the script runs from any checkout.
root = str(Path(__file__).resolve().parent.parent)

decl = {}
for f in glob.glob(root + "/registry/*.yaml"):
    y = yaml.safe_load(open(f).read())
    decl[y["id"]] = (
        y.get("amplicon_bp"),
        y.get("amplicon_bp_range"),
        bool((y.get("oligos") or {}).get("probe")),
    )
rows = collections.defaultdict(list)
with gzip.open(root + "/results/2026-10-25/calls.tsv.gz", "rt") as fh:
    for r in csv.DictReader(fh, delimiter="\t"):
        if r["call"] in ("detect", "reduced", "fail"):
            rows[r["assay_id"]].append(r)
for a in sys.argv[1:]:
    rs = rows.get(a) or []
    if not rs:
        print(f"\n=== {a}: no rows")
        continue
    d_bp, d_rng, hasprobe = decl.get(a, (None, None, False))

    def bp(r):
        try:
            return int(r["amplicon_bp"])
        except (ValueError, KeyError, TypeError):
            return None

    det = [bp(r) for r in rs if r["call"] in ("detect", "reduced")]
    det = [x for x in det if x]
    ref = statistics.mode(det) if det else d_bp

    def kind(r):
        probeless = (r.get("probe_site") or "-") in ("-", "")
        try:
            hi = float(r["fwd_penalty"]) > 3.0 and float(r["rev_penalty"]) > 3.0
        except (ValueError, KeyError):
            hi = False
        return "chance" if (probeless and hi) else "genuine"

    groups = collections.defaultdict(list)
    for r in rs:
        v = bp(r)
        if v is None:
            continue
        groups[("detect" if r["call"] in ("detect", "reduced") else kind(r))].append(v)
    print(f"\n=== {a}")
    print(f"  declared amplicon_bp={d_bp} range={d_rng} probe={hasprobe}  modal detect length={ref}")
    for k in ("detect", "genuine", "chance"):
        v = sorted(groups.get(k) or [])
        if not v:
            print(f"  {k:8s} n=0")
            continue
        off = [abs(x - ref) for x in v] if ref else []
        exact = sum(1 for x in v if ref and x == ref)
        within = sum(1 for x in v if ref and abs(x - ref) <= 5)
        print(
            f"  {k:8s} n={len(v):5d}  lengths {v[0]}-{v[-1]}  distinct={len(set(v)):4d}  ==modal {100 * exact / len(v):5.1f}%  within5 {100 * within / len(v):5.1f}%  median|off|={statistics.median(off) if off else '-'}"
        )
