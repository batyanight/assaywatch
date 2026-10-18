#!/usr/bin/env python3
"""Measure CMV gB (UL55) amplicon sizes for the two Prepens round 1/2 pairs.

Fetches a real cytomegalovirus UL55 reference from GenBank, maps each
degenerate primer pair, and prints the amplicon length(s).  Run inside the
assaywatch conda env on the Mac:

    python scripts/measure_cmv_gb_amplicons.py

Requires: Biopython (in the env).
"""

import re
import sys
from Bio import Entrez, SeqIO

# ---------- configuration ----------

Entrez.email = "nightb02@nyu.edu"
# Use NCBI_API_KEY from env if available
import os
key = os.environ.get("NCBI_API_KEY")
if key:
    Entrez.api_key = key

# Prepens et al. 2007 CM-gB primers (registry sequences, verified exact)
PAIRS = {
    "round1": {
        "forward": ("2743s",  "CGCAAATCGCAGANKCNTGGTG"),
        "reverse": ("2746as", "TGGTTGCCCAACAGNATYTCRTT"),
        "stored_bp": 320,
        "paper_table": 330,
        "paper_figure": 320,
    },
    "round2": {
        "forward": ("2744s",  "TTCAAGGAACTCAGYAARATNAAYCC"),
        "reverse": ("2745as", "CGTTGTCCTCNCCNARYTGNCC"),
        "stored_bp": 230,
        "paper_table": 250,
        "paper_figure": 250,
    },
}

# Accessions to test against — well-known CMV strains with full UL55
# AD169 (FJ527563), Merlin (AY446894), Towne (GU179289)
TEST_ACCESSIONS = ["FJ527563", "AY446894", "GU179289"]

# ---------- IUPAC degenerate matching ----------

IUPAC = {
    "A": "A", "C": "C", "G": "G", "T": "T",
    "R": "[AG]", "Y": "[CT]", "S": "[GC]", "W": "[AT]",
    "K": "[GT]", "M": "[AC]", "B": "[CGT]", "D": "[AGT]",
    "H": "[ACT]", "V": "[ACG]", "N": "[ACGT]",
}

def iupac_to_regex(seq: str) -> str:
    """Convert an IUPAC degenerate oligo to a regex pattern."""
    return "".join(IUPAC.get(c.upper(), c.upper()) for c in seq)

def revcomp(seq: str) -> str:
    """Reverse complement, preserving IUPAC codes."""
    comp = str.maketrans("ACGTRYSWKMBDHVNacgtryswkmbdhvn",
                         "TGCAYRSWMKVHDBNtgcayrswmkvhdbn")
    return seq.translate(comp)[::-1]

def find_primer(seq: str, primer: str) -> list[int]:
    """Return 0-based start positions where primer matches in seq."""
    pat = iupac_to_regex(primer)
    return [m.start() for m in re.finditer(pat, seq, re.IGNORECASE)]

# ---------- main ----------

def measure(accession: str) -> dict:
    """Fetch accession, map both pairs, return amplicon sizes."""
    handle = Entrez.efetch(db="nucleotide", id=accession,
                           rettype="fasta", retmode="text")
    record = SeqIO.read(handle, "fasta")
    handle.close()
    seq = str(record.seq).upper()
    desc = record.description
    results = {"accession": accession, "description": desc, "length": len(seq)}

    for rnd, pair in PAIRS.items():
        fwd_name, fwd_seq = pair["forward"]
        rev_name, rev_seq = pair["reverse"]

        # Forward primer matches on + strand
        fwd_hits = find_primer(seq, fwd_seq)
        # Reverse primer matches on + strand as revcomp
        rev_rc = revcomp(rev_seq)
        rev_hits = find_primer(seq, rev_rc)

        amplicons = []
        for f in fwd_hits:
            for r in rev_hits:
                amp_len = r + len(rev_seq) - f
                if 50 < amp_len < 5000:  # plausible range
                    amplicons.append(amp_len)

        results[rnd] = {
            "fwd_hits": len(fwd_hits),
            "rev_hits": len(rev_hits),
            "amplicons": amplicons,
        }

    return results


def main():
    print("CMV gB (UL55) amplicon measurement — Prepens et al. 2007")
    print("=" * 60)

    all_r1 = []
    all_r2 = []

    for acc in TEST_ACCESSIONS:
        print(f"\nFetching {acc}...")
        try:
            res = measure(acc)
        except Exception as e:
            print(f"  ERROR: {e}")
            continue

        print(f"  {res['description'][:80]}")
        print(f"  Sequence length: {res['length']} bp")

        for rnd in ("round1", "round2"):
            r = res[rnd]
            pair = PAIRS[rnd]
            print(f"\n  {rnd} ({pair['forward'][0]} / {pair['reverse'][0]}):")
            print(f"    Forward hits: {r['fwd_hits']}, Reverse hits: {r['rev_hits']}")
            if r["amplicons"]:
                for amp in r["amplicons"]:
                    print(f"    AMPLICON: {amp} bp")
                if rnd == "round1":
                    all_r1.extend(r["amplicons"])
                else:
                    all_r2.extend(r["amplicons"])
            else:
                print("    No amplicon found")

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)

    for rnd, collected, pair in [("round1", all_r1, PAIRS["round1"]),
                                  ("round2", all_r2, PAIRS["round2"])]:
        print(f"\n{rnd}:")
        print(f"  Stored:        {pair['stored_bp']} bp")
        print(f"  Paper table:   {pair['paper_table']} bp")
        print(f"  Paper figure:  {pair['paper_figure']} bp")
        if collected:
            unique = sorted(set(collected))
            print(f"  MEASURED:      {', '.join(str(x) for x in unique)} bp"
                  f"  (across {len(collected)} hit(s) in {len(TEST_ACCESSIONS)} records)")
        else:
            print("  MEASURED:      no hits")

    print("\nUpdate registry amplicon_bp values to the measured sizes.")
    print("If a size varies across strains, use the modal value and note the range.")


if __name__ == "__main__":
    main()
