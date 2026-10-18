#!/usr/bin/env python3
"""Backfill taxids for existing retrieved records.

For each .meta.tsv.gz file in data/retrieved, extract accessions and fetch their
taxids via NCBI esummary, writing results to a separate .meta.taxid.tsv.gz file
that maps accession -> taxid. Later lookups can join this sidecar against the
main metadata.

The backfill does not rewrite the original .meta.tsv.gz files (which are not
re-fetchable), so it is safe to run and re-run during development.
"""

import gzip
import sys
from pathlib import Path
from collections import defaultdict
import xml.etree.ElementTree as ET
from assaywatch.retrieve import http_transport
from assaywatch.credentials import ncbi_api_key, ncbi_email, ncbi_fetch_delay


def backfill_taxids(cfg: dict, dry_run: bool = False) -> None:
    """Fetch and store taxids for all existing accessions in retrieved archives."""
    retrieved_dir = Path(cfg.get("retrieved_dir", "data/retrieved"))
    api_key = ncbi_api_key()
    email = ncbi_email()
    transport = http_transport(email, api_key)
    
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
    
    if not accession_to_uid:
        print("No accessions to backfill.")
        return
    
    print(f"Found {len(accession_to_uid)} accessions to backfill taxids for.")
    if dry_run:
        print("(dry run: not fetching)")
        return
    
    # Fetch taxids in batches via esummary
    uids_list = list(accession_to_uid.values())
    batch_size = 500
    acc_to_taxid = {}
    
    for batch_start in range(0, len(uids_list), batch_size):
        batch_uids = uids_list[batch_start : batch_start + batch_size]
        uid_list = ",".join(batch_uids)
        
        print(f"Fetching taxids for batch {batch_start // batch_size + 1}...", file=sys.stderr)
        
        try:
            xml = transport(
                "esummary",
                {
                    "db": "nuccore",
                    "id": uid_list,
                    "retmode": "xml",
                },
            )
            root = ET.fromstring(xml)
            
            for doc in root.findall("DocSum"):
                uid = doc.findtext("Id")
                taxid_elem = doc.find(".//Item[@Name='TaxId']")
                if taxid_elem is not None:
                    taxid = taxid_elem.text
                    # Find accession by uid
                    for acc, u in accession_to_uid.items():
                        if u == uid:
                            acc_to_taxid[acc] = taxid
                            break
        except Exception as e:
            print(f"Error fetching batch: {e}", file=sys.stderr)
            continue
    
    # Write backfill sidecar
    backfill_file = retrieved_dir / ".meta.taxid.backfill.tsv.gz"
    with gzip.open(backfill_file, "wt") as f:
        f.write("accession\ttaxid\n")
        for acc, taxid in sorted(acc_to_taxid.items()):
            f.write(f"{acc}\t{taxid}\n")
    
    print(f"Wrote {len(acc_to_taxid)} taxids to {backfill_file}")


if __name__ == "__main__":
    import yaml
    cfg = yaml.safe_load(open("config.yaml"))
    dry_run = "--dry-run" in sys.argv
    backfill_taxids(cfg, dry_run=dry_run)
