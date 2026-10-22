#!/usr/bin/env python3
"""Measure one assay's product size per species from the archive, as `species_sizes` YAML.

    python scripts/measure_species_sizes.py --assay ORTHOPOXVIRUS_dsDNA_ATI_Meyer_1997 \
        --calls results/<date>/calls.tsv.gz

For an assay that identifies the species by product length (one declaring
`amplicon_bp_range`), the length IS the readout, so it belongs in the registry
as measured numbers rather than as prose in a curator note. This prints the
block to paste into the entry; nothing is written for you, because a registry
entry is a human's claim.

It also suggests the `amplicon_bp_range` itself, as the ENVELOPE of every
measured band — the lowest band low and the highest band high, each end taken
separately, not a centre and a spread — plus a fixed `--cushion` on each end for
an indel in a strain not yet deposited. Species A at 300-450 and species B at
350-500 give a range of 300-500 before the cushion. The measured value is what
the registry takes (config.yaml `amplicon:`), and `declared_tolerance` adds its
own margin on top at screen time, so the cushion here is modest headroom, not
the whole safety factor.

By default only records the assay would amplify count (`detect` or `reduced`),
and patent division deposits are always dropped: an ATI product from an
engineered vector is a construct's length, not a species'
(docs/2026-10-19-orthopox-ati-vaccinia.md).

`--include-fail` also counts a `fail`-scored record whose primer sites span a
product. A length is a property of the template rather than of the yield, so if
the table is meant to help someone interpret a band they have in hand, a band
the pipeline would not amplify still belongs in it: Meyer 1997 got a 530 bp
skunkpox product that this pipeline scores `fail` at 551 bp
(docs/2026-10-20-meyer-ati-bench-panel.md). It is not the default because a
`fail` also covers a record whose sites are present and diverged, including
UNVERIFIED and engineered deposits, so the lengths it admits need reading
rather than trusting. Either way the output says how each band's records
scored.

A RefSeq record (NC_/NZ_/NG_) is dropped when a non-RefSeq record of the same
species has both the same record length and the same product length, because
that is the original it copies. Without this, three of ATI's bands looked like
two records when they were one isolate deposited twice, and `--min-records 2`
could not tell the difference. The rule deliberately does not collapse two
non-RefSeq records of equal length: thousands of outbreak genomes share a
length without being the same isolate, and collapsing those cut monkeypox from
12,539 records to 4,704.

One species can have several real sizes — monkeypox clade I sits near 1067 bp
and clade IIb near 1538 — so sizes are clustered rather than reduced to one
range. A distinct length is carried forward only if at least `--min-records`
records and `--min-share` of that species' records have it; the survivors are
then split into clusters wherever consecutive lengths differ by more than
`--gap` bp. Dropping the thin lengths FIRST is what keeps a cluster honest: on
12,539 monkeypox records the rare lengths form a continuum, and clustering them
too chains 1520 through 1590 into one band that swallows variola and vaccinia,
where the real clade IIb band is 1535-1545. Each row carries its record count,
and the comment above the block says what share of the species' records the
reported bands cover, so a thin or incomplete row is visible.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from assaywatch.accession import strip_version  # noqa: E402
from assaywatch.metadata import looks_like_patent  # noqa: E402
from assaywatch.schema import AMPLICON_MAX, AMPLICON_MIN  # noqa: E402
from assaywatch.taxonomy import load_taxonomy  # noqa: E402

AMPLIFIES = ("detect", "reduced")
WITH_FAIL = ("detect", "reduced", "fail")


def archive_facts(retrieved: Path) -> tuple[dict[str, int], set[str], dict[str, str]]:
    """(accession -> taxid, patent-deposit accessions, accession -> record length), unversioned.

    The length is what de-duplicates a RefSeq copy against its GenBank original.
    """
    taxid: dict[str, int] = {}
    patent: set[str] = set()
    length: dict[str, str] = {}
    sidecar = retrieved / ".meta.taxid.backfill.tsv.gz"
    if sidecar.exists():
        with gzip.open(sidecar, "rt") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                if (row.get("taxid") or "").isdigit():
                    taxid[row["accession"]] = int(row["taxid"])
    for meta in sorted(retrieved.rglob("*.meta.tsv.gz")):
        with gzip.open(meta, "rt") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                acc = row.get("accession") or ""
                if (row.get("taxid") or "").isdigit():
                    taxid[acc] = int(row["taxid"])
                if row.get("is_patent") == "1" or looks_like_patent(row.get("title") or ""):
                    patent.add(acc)
                length[acc] = row.get("length") or ""
    return taxid, patent, length


def clusters(
    sizes: Counter, gap: int, min_records: int, min_share: float
) -> list[tuple[int, int, int, list[int]]]:
    """[(lo, hi, n, lengths)], biggest first, for the lengths that clear both floors.

    The floors apply to each distinct length, not to the cluster it lands in;
    see the module docstring for why that ordering matters.
    """
    total = sum(sizes.values())
    dense = [bp for bp in sorted(sizes) if sizes[bp] >= min_records and sizes[bp] / total >= min_share]
    groups, run = [], []
    for bp in dense:
        if run and bp - run[-1] > gap:
            groups.append(run)
            run = []
        run.append(bp)
    if run:
        groups.append(run)
    kept = [(g[0], g[-1], sum(sizes[bp] for bp in g), g) for g in groups]
    return sorted(kept, key=lambda c: -c[2])


def suggested_range(bands: list[tuple[int, int]], cushion: int) -> tuple[int, int]:
    """The amplicon_bp_range to declare over `bands`: envelope, then a cushion.

    `bands` is every kept (lo, hi), across all species. The range is the lowest
    low and the highest high, each end taken SEPARATELY — not a centre and a
    spread. Species A at (300, 450) and species B at (350, 500) give (300, 500);
    the cushion then pads each end for an unobserved indel. Clamped to the
    schema's absolute bounds so the result is always a legal range.
    """
    lo = min(b[0] for b in bands) - cushion
    hi = max(b[1] for b in bands) + cushion
    return max(AMPLICON_MIN, lo), min(AMPLICON_MAX, hi)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--assay", required=True)
    ap.add_argument("--calls", type=Path, required=True)
    ap.add_argument("--retrieved", type=Path, default=ROOT / "data" / "retrieved")
    ap.add_argument("--taxonomy", type=Path, default=ROOT / "docs" / "taxonomy-cache.json.gz")
    ap.add_argument("--gap", type=int, default=12, help="bp; a bigger step starts a new cluster")
    ap.add_argument(
        "--cushion",
        type=int,
        default=10,
        help="bp of headroom added to each end of the suggested amplicon_bp_range, beyond the "
        "outermost measured band. For an unobserved indel in a strain not yet deposited; the "
        "declared_tolerance in config.yaml adds its own margin on top at screen time. A "
        "judgement — the number a curator thinks reasonable — so it is a flag, not a constant.",
    )
    ap.add_argument(
        "--include-fail",
        action="store_true",
        help="also count a fail-scored record whose sites span a product (see the docstring)",
    )
    # 1, not 2: after de-duplication the rare species are one isolate each, and
    # ATI's volepox and skunkpox bands are both confirmed on Meyer's own bench.
    # --min-share still keeps a one-off length out of a well-sequenced species.
    ap.add_argument("--min-records", type=int, default=1)
    ap.add_argument("--min-share", type=float, default=0.02)
    args = ap.parse_args(argv)

    tree = load_taxonomy(args.taxonomy)
    taxid, patent, length = archive_facts(args.retrieved)

    wanted = WITH_FAIL if args.include_fail else AMPLIFIES
    kept_rows: list[tuple[int, int, str, str]] = []  # species, bp, call, accession
    skipped_patent = 0
    with gzip.open(args.calls, "rt") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            if row["assay_id"] != args.assay or row["call"] not in wanted:
                continue
            acc = strip_version(row["record_id"])
            if acc in patent:
                skipped_patent += 1
                continue
            if acc not in taxid or not (row.get("amplicon_bp") or "").isdigit():
                continue
            species = tree.species_of(taxid[acc]) or taxid[acc]
            kept_rows.append((species, int(row["amplicon_bp"]), row["call"], acc))

    # Drop a RefSeq record that copies a non-RefSeq original: same species, same
    # record length, same product length.
    originals = {
        (sp, length.get(acc, ""), bp)
        for sp, bp, _, acc in kept_rows
        if not acc.startswith(("NC_", "NZ_", "NG_"))
    }
    sizes: dict[int, Counter] = defaultdict(Counter)
    calls_per_band: dict[tuple[int, int], Counter] = defaultdict(Counter)
    duplicates = 0
    for sp, bp, call, acc in kept_rows:
        if acc.startswith(("NC_", "NZ_", "NG_")) and (sp, length.get(acc, ""), bp) in originals:
            duplicates += 1
            continue
        sizes[sp][bp] += 1
        calls_per_band[(sp, bp)][call] += 1

    print(f"# measured by scripts/measure_species_sizes.py from {args.calls.name}")
    if args.include_fail:
        print("# --include-fail: a fail-scored record whose sites span a product counts too")
    print(f"# {skipped_patent} patent-division records excluded, {duplicates} duplicate records collapsed")
    print(f"# a length is kept at >= {args.min_records} records and >= {args.min_share:.0%} of the")
    print(f"# species' records; kept lengths cluster where a step exceeds {args.gap} bp")
    # Build the bands first, so the suggested amplicon_bp_range can be printed
    # ABOVE species_sizes — the order the entry declares them, and the range is
    # a precondition of the bands validating.
    blocks: list[tuple[int, int, int, str, str]] = []  # species, lo, hi, name, scored
    thin: list[str] = []
    for species in sorted(sizes, key=lambda s: -sum(sizes[s].values())):
        cs = clusters(sizes[species], args.gap, args.min_records, args.min_share)
        name = tree.name.get(species) or f"taxid {species}"
        for lo, hi, n, lengths in cs:
            mix = Counter()
            for bp in lengths:
                mix.update(calls_per_band[(species, bp)])
            how = ", ".join(f"{c} {k}" for k, c in sorted(mix.items()))
            blocks.append((species, lo, hi, name, how, n))
        n_all = sum(sizes[species].values())
        covered = sum(n for _, _, n, _ in cs)
        if covered < n_all:
            thin.append(f"#   {name}: bands cover {covered}/{n_all} records ({covered / n_all:.0%})")

    # The range is the ENVELOPE of every kept band, each end taken separately:
    # the lowest band low and the highest band high, not a centre and spread.
    # Species A 300-450 and species B 350-500 give 300-500. Then a fixed cushion
    # on each end for an indel not yet deposited. The raw extremes across all
    # credible records are shown too, so a curator sees whether clustering
    # trimmed a length the cushion should instead reach.
    if blocks:
        band_lo = min(lo for _, lo, _, _, _, _ in blocks)
        band_hi = max(hi for _, _, hi, _, _, _ in blocks)
        lo, hi = suggested_range([(b[1], b[2]) for b in blocks], args.cushion)
        raw_lo = min(bp for _, bp, _, _ in kept_rows)
        raw_hi = max(bp for _, bp, _, _ in kept_rows)
        print(f"# amplicon_bp_range: band envelope {band_lo}-{band_hi} + {args.cushion} bp cushion each end")
        if raw_lo < band_lo or raw_hi > band_hi:
            print(
                f"#   raw product extremes across kept records are {raw_lo}-{raw_hi}; clustering "
                "trimmed the difference. Widen --cushion or lower --min-share if a trimmed length is real."
            )
        print("amplicon_bp: null  # mutually exclusive with the range below")
        print(f"amplicon_bp_range: [{lo}, {hi}]")

    print("species_sizes:")
    for species, lo, hi, name, how, n in blocks:
        print(f"- taxid: {species}")
        print(f"  bp: [{lo}, {hi}]")
        print(f"  n_records: {n}")
        print(f"  note: {name}")
        print(f"  # scored: {how}")
    for line in thin:
        print(line)
    print(f"# {len(blocks)} rows over {len(sizes)} species", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
