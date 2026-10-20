#!/usr/bin/env python3
"""Measure CMV gB (UL55) amplicon sizes for the two Prepens round 1/2 pairs.

Fetches real cytomegalovirus UL55 coding sequences from GenBank, maps each
degenerate primer pair with mismatch-tolerant sliding-window alignment, and
prints the amplicon length(s).  Run inside the assaywatch conda env on Mac:

    python scripts/measure_cmv_gb_amplicons.py

Requires: Biopython (in the env).
"""

import os
import sys
from collections import Counter

from Bio import Entrez, SeqIO

# ---------- configuration ----------

Entrez.email = "nightb02@nyu.edu"
key = os.environ.get("NCBI_API_KEY")
if key:
    Entrez.api_key = key

# Prepens et al. 2007 CM-gB primers (registry sequences, verified exact)
PAIRS = {
    "round1": {
        "forward": ("2743s", "CGCAAATCGCAGANKCNTGGTG"),
        "reverse": ("2746as", "TGGTTGCCCAACAGNATYTCRTT"),
        "stored_bp": 320,
        "paper_table": 330,
        "paper_figure": 320,
    },
    "round2": {
        "forward": ("2744s", "TTCAAGGAACTCAGYAARATNAAYCC"),
        "reverse": ("2745as", "CGTTGTCCTCNCCNARYTGNCC"),
        "stored_bp": 230,
        "paper_table": 250,
        "paper_figure": 250,
    },
}

# Max mismatches allowed for a primer hit
MAX_MM = 3

# ---------- IUPAC ----------

IUPAC_SETS = {
    "A": {"A"},
    "C": {"C"},
    "G": {"G"},
    "T": {"T"},
    "R": {"A", "G"},
    "Y": {"C", "T"},
    "S": {"G", "C"},
    "W": {"A", "T"},
    "K": {"G", "T"},
    "M": {"A", "C"},
    "B": {"C", "G", "T"},
    "D": {"A", "G", "T"},
    "H": {"A", "C", "T"},
    "V": {"A", "C", "G"},
    "N": {"A", "C", "G", "T"},
}


def revcomp(seq: str) -> str:
    comp = str.maketrans("ACGTRYSWKMBDHVNacgtryswkmbdhvn", "TGCAYRSWMKVHDBNtgcayrswmkvhdbn")
    return seq.translate(comp)[::-1]


def count_mismatches(seq_window: str, primer: str) -> int:
    """Count mismatches between a sequence window and an IUPAC primer."""
    mm = 0
    for s, p in zip(seq_window, primer, strict=True):
        if s.upper() not in IUPAC_SETS.get(p.upper(), {p.upper()}):
            mm += 1
    return mm


def find_primer_fuzzy(seq: str, primer: str, max_mm: int = MAX_MM):
    """Slide primer along seq, return list of (start, mismatches)."""
    plen = len(primer)
    hits = []
    for i in range(len(seq) - plen + 1):
        mm = count_mismatches(seq[i : i + plen], primer)
        if mm <= max_mm:
            hits.append((i, mm))
    return hits


# ---------- fetch UL55 CDS records ----------


def fetch_ul55_cds(max_records: int = 20):
    """Search for CMV UL55 (gB) coding sequences and return as list of (acc, seq, desc)."""
    # Strategy 1: search for UL55 CDS records directly
    queries = [
        '"Human betaherpesvirus 5"[Orgn] AND UL55[Gene] AND biomol_mrna[PROP]',
        '"Human betaherpesvirus 5"[Orgn] AND "glycoprotein B"[Title] AND 500:5000[SLEN]',
        "cytomegalovirus[Orgn] AND UL55[Gene] AND 500:5000[SLEN]",
    ]
    seen_accs = set()
    records = []

    for query in queries:
        if len(records) >= max_records:
            break
        try:
            handle = Entrez.esearch(db="nucleotide", term=query, retmax=20)
            result = Entrez.read(handle)
            handle.close()
            ids = result.get("IdList", [])
            if not ids:
                continue
            handle = Entrez.efetch(db="nucleotide", id=",".join(ids[:20]), rettype="fasta", retmode="text")
            for rec in SeqIO.parse(handle, "fasta"):
                acc = rec.id.split(".")[0]
                if acc not in seen_accs:
                    seen_accs.add(acc)
                    records.append((rec.id, str(rec.seq).upper(), rec.description))
            handle.close()
        except Exception as e:
            print(f"  Query failed: {e}")

    # Strategy 2: also extract UL55 region from complete genomes
    # Known CMV complete genomes — extract ~3kb around UL55 position
    genomes = {
        "FJ527563": (78000, 82000),  # AD169: UL55 approximately here
        "AY446894": (79000, 83000),  # Merlin
    }
    for acc, (start, end) in genomes.items():
        if acc in seen_accs:
            continue
        try:
            handle = Entrez.efetch(db="nucleotide", id=acc, rettype="fasta", retmode="text")
            rec = SeqIO.read(handle, "fasta")
            handle.close()
            full_seq = str(rec.seq).upper()
            # Try to find UL55 by searching for a conserved gB motif
            # Fall back to the approximate coordinates
            region = full_seq[start:end]
            seen_accs.add(acc)
            records.append(
                (f"{rec.id}:UL55region({start}-{end})", region, f"{rec.description} [extracted UL55 region]")
            )
        except Exception as e:
            print(f"  Genome extract failed for {acc}: {e}")

    return records


# ---------- main ----------


def main():
    print("CMV gB (UL55) amplicon measurement — Prepens et al. 2007")
    print(f"Mismatch-tolerant search (max {MAX_MM} mismatches)")
    print("=" * 65)

    print("\nFetching UL55/gB sequences from GenBank...")
    records = fetch_ul55_cds()
    print(f"  Got {len(records)} record(s)\n")

    if not records:
        print("ERROR: No UL55 records retrieved. Check NCBI connectivity.")
        sys.exit(1)

    # Collect amplicon sizes across all records
    amplicons_all = {"round1": [], "round2": []}

    for acc, seq, desc in records:
        print(f"--- {acc}  ({len(seq)} bp)")
        print(f"    {desc[:90]}")

        for rnd, pair in PAIRS.items():
            fwd_name, fwd_seq = pair["forward"]
            rev_name, rev_seq = pair["reverse"]

            # Forward on + strand
            fwd_hits = find_primer_fuzzy(seq, fwd_seq)
            # Reverse primer: search for its revcomp on + strand
            rev_rc = revcomp(rev_seq)
            rev_hits = find_primer_fuzzy(seq, rev_rc)

            if fwd_hits or rev_hits:
                best_fwd = min(fwd_hits, key=lambda x: x[1]) if fwd_hits else None
                best_rev = min(rev_hits, key=lambda x: x[1]) if rev_hits else None
                print(
                    f"    {rnd} {fwd_name}: {len(fwd_hits)} hit(s)"
                    + (f", best {best_fwd[1]}mm @{best_fwd[0]}" if best_fwd else "")
                    + f"  |  {rev_name}: {len(rev_hits)} hit(s)"
                    + (f", best {best_rev[1]}mm @{best_rev[0]}" if best_rev else "")
                )

            # Calculate amplicons from all fwd/rev combinations
            for fpos, fmm in fwd_hits:
                for rpos, rmm in rev_hits:
                    amp = rpos + len(rev_seq) - fpos
                    total_mm = fmm + rmm
                    if 50 < amp < 5000:
                        amplicons_all[rnd].append((amp, total_mm, acc))
                        print(f"      AMPLICON: {amp} bp  ({fmm}+{rmm} = {total_mm} mm total)")

            if not fwd_hits and not rev_hits:
                # Check both strands for any near-match to diagnose
                pass

    # ---------- summary ----------
    print("\n" + "=" * 65)
    print("SUMMARY")
    print("=" * 65)

    for rnd in ("round1", "round2"):
        pair = PAIRS[rnd]
        hits = amplicons_all[rnd]
        print(f"\n{rnd} ({pair['forward'][0]} / {pair['reverse'][0]}):")
        print(f"  Stored:        {pair['stored_bp']} bp")
        print(f"  Paper table:   {pair['paper_table']} bp")
        print(f"  Paper figure:  {pair['paper_figure']} bp")

        if hits:
            # Group by amplicon size
            size_counts = Counter(h[0] for h in hits)
            best_mm = {}
            for amp, mm, _acc in hits:
                if amp not in best_mm or mm < best_mm[amp]:
                    best_mm[amp] = mm

            for size, count in size_counts.most_common():
                print(f"  MEASURED:      {size} bp  ({count} record(s), best total mm: {best_mm[size]})")
        else:
            print("  MEASURED:      no hits — try broader search or check primers")

    print()


if __name__ == "__main__":
    main()
