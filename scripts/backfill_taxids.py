#!/usr/bin/env python3
"""Backfill taxids for existing retrieved records.

For each .meta.tsv.gz file in data/retrieved, extract accessions and fetch their
taxids via NCBI esummary, writing results to a separate .meta.taxid.tsv.gz file
that maps accession -> taxid. Later lookups can join this sidecar against the
main metadata.

The backfill does not rewrite the original .meta.tsv.gz files (which are not
re-fetchable), so it is safe to run and re-run during development.

    python scripts/backfill_taxids.py --email you@example.org [--dry-run]
"""

import argparse
import gzip
import sys
from collections import defaultdict
from pathlib import Path

from assaywatch import ncbi
from assaywatch.score import load_config


def backfill_taxids(cfg: dict, email: str, dry_run: bool = False) -> None:
    """Fetch and store taxids for all existing accessions in retrieved archives."""
    retrieved_dir = Path(cfg.get("retrieved_dir", "data/retrieved"))
    transport = ncbi.eutils(email, ncbi.api_key())

    # Collect all accessions across all groups
    accession_to_uid = {}
    for meta_file in retrieved_dir.rglob("*.meta.tsv.gz"):
        with gzip.open(meta_file, "rt") as f:
            header = f.readline().strip().split("\t")
            uid_idx = header.index("uid")
            acc_idx = header.index("accession")
            taxid_idx = header.index("taxid") if "taxid" in header else -1

            for line in f:
                parts = line.strip().split("\t")
                acc = parts[acc_idx]
                uid = parts[uid_idx]
                # Skip if taxid already present
                if taxid_idx >= 0 and len(parts) > taxid_idx and parts[taxid_idx]:
                    continue
                if acc not in accession_to_uid:
                    accession_to_uid[acc] = uid

    # Resume: accessions already in the sidecar are kept and not refetched.
    backfill_file = retrieved_dir / ".meta.taxid.backfill.tsv.gz"
    acc_to_taxid = {}
    if backfill_file.exists():
        with gzip.open(backfill_file, "rt") as f:
            next(f, None)
            for line in f:
                a, _, t = line.rstrip("\n").partition("\t")
                if t:
                    acc_to_taxid[a] = t
        accession_to_uid = {a: u for a, u in accession_to_uid.items() if a not in acc_to_taxid}
        print(f"{len(acc_to_taxid)} already in sidecar; {len(accession_to_uid)} left to fetch.")

    if not accession_to_uid:
        print("No accessions to backfill.")
        return

    print(f"Found {len(accession_to_uid)} accessions to backfill taxids for.")
    if dry_run:
        print("(dry run: not fetching)")
        return

    # Fetch taxids in batches via esummary
    uid_to_accs = defaultdict(list)
    for acc, u in accession_to_uid.items():
        uid_to_accs[u].append(acc)
    uids_list = list(uid_to_accs)
    failed_batches = []
    batch_size = 500
    for batch_start in range(0, len(uids_list), batch_size):
        batch_uids = uids_list[batch_start : batch_start + batch_size]

        if (batch_start // batch_size) % 100 == 0:
            print(
                f"batch {batch_start // batch_size + 1} of {-(-len(uids_list) // batch_size)}",
                file=sys.stderr,
            )

        try:
            for uid, taxid in ncbi.taxids_of_uids(batch_uids, transport, batch=batch_size).items():
                for acc in uid_to_accs.get(uid, ()):
                    acc_to_taxid[acc] = str(taxid)
        except Exception as e:  # noqa: BLE001 - one batch failing must not lose the others
            print(
                f"Error fetching batch {batch_start // batch_size + 1}: {type(e).__name__}", file=sys.stderr
            )
            failed_batches.append(batch_start // batch_size + 1)
            continue

    # Write backfill sidecar
    tmp = backfill_file.with_name(backfill_file.name + ".part")
    with gzip.open(tmp, "wt") as f:
        f.write("accession\ttaxid\n")
        for acc, taxid in sorted(acc_to_taxid.items()):
            f.write(f"{acc}\t{taxid}\n")

    tmp.replace(backfill_file)
    print(
        f"Wrote {len(acc_to_taxid)} taxids to {backfill_file}; "
        f"{len(uids_list) and sum(1 for u in uids_list for a in uid_to_accs[u] if a not in acc_to_taxid)} accessions still without a taxid; "
        f"{len(failed_batches)} failed batches"
    )


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--email", required=True, help="Contact address for NCBI E-utilities")
    ap.add_argument("--config", type=Path, default=Path("config.yaml"))
    ap.add_argument(
        "--dry-run", action="store_true", help="Do not fetch or write, just show what would happen"
    )
    args = ap.parse_args()

    cfg = load_config(args.config)
    backfill_taxids(cfg, email=args.email, dry_run=args.dry_run)
