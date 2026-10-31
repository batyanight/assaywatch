"""Matcher tests: the search must be exhaustive, not merely usually right.

The prefilter in match.py is an optimisation. These tests hold it to the
standard that it returns exactly what a brute-force scan of every offset
returns, on random sequences and on the pathological cases that broke the
seeded matcher it replaced.
"""

import random

import pytest

from assaywatch.iupac import IUPAC, base_state, compare, reverse_complement
from assaywatch.match import MATCH, MISMATCH, UNKNOWN, _match_tables, find_sites

STATE_VALUE = {"match": MATCH, "mismatch": MISMATCH, "unknown": UNKNOWN}

RNG = random.Random(4242)


def brute_force(oligo: str, record: str, max_mm: int):
    """Every site, found the slow obvious way. The definition the fast path must meet."""
    out = {}
    L = len(oligo)
    for start in range(len(record) - L + 1):
        mm, amb = compare(oligo, record[start : start + L])
        if len(mm) + len(amb) <= max_mm:
            out[(start, "+")] = (tuple(mm), tuple(amb))
    rc = reverse_complement(record)
    n = len(record)
    for start in range(len(rc) - L + 1):
        mm, amb = compare(oligo, rc[start : start + L])
        if len(mm) + len(amb) <= max_mm:
            out[(n - start - L, "-")] = (tuple(mm), tuple(amb))
    return out


def as_dict(sites):
    return {(s.start, s.strand): (s.mismatches, s.ambiguous) for s in sites}


def random_seq(n: int, alphabet: str = "ACGT") -> str:
    return "".join(RNG.choice(alphabet) for _ in range(n))


@pytest.mark.parametrize("trial", range(40))
@pytest.mark.parametrize("max_mm", [0, 2, 6])
def test_matches_brute_force_on_random_data(trial, max_mm):
    """Plant an edited copy of the oligo in a random record and compare exhaustively."""
    oligo = random_seq(RNG.randint(15, 30))
    record = random_seq(300)
    site = list(oligo)
    for _ in range(RNG.randint(0, 8)):
        i = RNG.randrange(len(site))
        site[i] = RNG.choice("ACGT")
    pos = RNG.randrange(50, 200)
    record = record[:pos] + "".join(site) + record[pos + len(site) :]
    assert as_dict(find_sites(oligo, record, max_mm)) == brute_force(oligo, record, max_mm)


@pytest.mark.parametrize("trial", range(20))
def test_matches_brute_force_with_degenerate_oligos_and_records(trial):
    """Degenerate bases on both sides are where a filter is most likely to go wrong."""
    oligo = random_seq(RNG.randint(18, 26), "ACGTACGTRYSWKMN")
    record = random_seq(250, "ACGTACGTACGTRYN")
    assert as_dict(find_sites(oligo, record, 4)) == brute_force(oligo, record, 4)


def test_mismatch_in_every_chunk_is_still_found():
    """The failure mode of the old seeded matcher: edits at both ends of the oligo.

    A seeded search taking one k-mer from each end missed this entirely and
    reported no site. An exact search must find it and charge both mismatches.
    """
    oligo = "CAGTGTGCCATATGTCACGATTC"
    site = "T" + oligo[1:-1] + "A"  # first and last base changed
    assert site[0] != oligo[0] and site[-1] != oligo[-1]
    record = random_seq(80) + site + random_seq(80)
    sites = [s for s in find_sites(oligo, record, 6) if s.strand == "+"]
    assert len(sites) == 1
    assert sites[0].mismatches == (0, len(oligo) - 1)


def test_short_probe_with_a_central_mismatch_is_found():
    """A 15 nt probe edited at its centre has no clean 8-mer anywhere in it."""
    probe = "CGAGTCGAACAAAAT"
    i = len(probe) // 2
    site = probe[:i] + ("T" if probe[i] != "T" else "A") + probe[i + 1 :]
    record = random_seq(60) + site + random_seq(60)
    sites = [s for s in find_sites(probe, record, 6) if s.strand == "+"]
    assert len(sites) == 1 and sites[0].mismatches == (i,)


def test_raising_the_budget_only_adds_sites():
    oligo = "CAGTGTGCCATATGTCACG"
    record = random_seq(200) + "CAGTGTACCATTTGTCACG" + random_seq(200)
    seen = {}
    for budget in range(0, 7):
        sites = as_dict(find_sites(oligo, record, budget))
        for key, mm in seen.items():
            assert sites[key] == mm, "a site moved or changed when the budget grew"
        seen = sites


def test_lookup_table_agrees_with_base_state():
    """match.py's fast table and iupac.base_state must encode the same rule."""
    for oligo_code in IUPAC:
        table = _match_tables(oligo_code)[0]
        for record_code in IUPAC:
            assert table[ord(record_code)] == STATE_VALUE[base_state(oligo_code, record_code)], (
                f"{oligo_code} vs {record_code}"
            )


def test_record_n_is_ambiguous_not_a_mismatch():
    """An undetermined record base is neither evidence of binding nor of drift."""
    oligo = "CAGTGTGCCATATGTCACG"
    record = random_seq(50) + oligo[:5] + "N" + oligo[6:] + random_seq(50)
    sites = [s for s in find_sites(oligo, record, 6) if s.strand == "+"]
    assert len(sites) == 1
    assert sites[0].mismatches == () and sites[0].ambiguous == (5,)


def test_partly_covered_record_code_is_ambiguous_but_disjoint_is_a_mismatch():
    """R where the primer wants A could be A; S never can be."""
    oligo = "CAGTGTGCCATATGTCACG"
    i = oligo.index("A")
    amb = random_seq(40) + oligo[:i] + "R" + oligo[i + 1 :] + random_seq(40)
    mis = random_seq(40) + oligo[:i] + "S" + oligo[i + 1 :] + random_seq(40)
    a = [s for s in find_sites(oligo, amb, 6) if s.strand == "+"][0]
    m = [s for s in find_sites(oligo, mis, 6) if s.strand == "+"][0]
    assert a.mismatches == () and a.ambiguous == (i,)
    assert m.mismatches == (i,) and m.ambiguous == ()


def test_degenerate_oligo_is_never_worse_than_a_concrete_one():
    """Widening an oligo base can only turn mismatches into matches."""
    concrete = "CAGTGTGCCATATGTCACG"
    for i, base in enumerate(concrete):
        if base != "C":
            continue
        degenerate = concrete[:i] + "Y" + concrete[i + 1 :]  # Y covers C and T
        for record_base in "ACGT":
            record = random_seq(30) + concrete[:i] + record_base + concrete[i + 1 :] + random_seq(30)
            c = [s for s in find_sites(concrete, record, 6) if s.strand == "+"][0]
            d = [s for s in find_sites(degenerate, record, 6) if s.strand == "+"][0]
            assert d.n_mismatches <= c.n_mismatches


def test_minus_strand_coordinates_point_at_the_real_window():
    oligo = "CAGTGTGCCATATGTCACG"
    record = random_seq(100) + reverse_complement(oligo) + random_seq(100)
    sites = [s for s in find_sites(oligo, record, 0) if s.strand == "-"]
    assert len(sites) == 1
    s = sites[0]
    assert reverse_complement(record[s.start : s.end]) == oligo
    assert s.window == oligo


def test_oligo_longer_than_record_returns_nothing():
    assert find_sites("CAGTGTGCCATATGTCACG", "ACGTACGT") == []


def test_a_run_of_ns_is_not_a_binding_site():
    """Regression: N-gaps in scaffolds made every offset a perfect site for every oligo.

    Undetermined bases are free when scoring a site but are not evidence that a
    site exists, so they count against the search budget.
    """
    oligo = "CAGTGTGCCATATGTCACG"
    record = random_seq(200) + "N" * 5000 + random_seq(200)
    assert [s for s in find_sites(oligo, record, 6) if record[s.start] == "N"] == []


def test_a_site_with_a_few_ns_is_still_found():
    oligo = "CAGTGTGCCATATGTCACG"
    site = oligo[:3] + "NNN" + oligo[6:]
    record = random_seq(60) + site + random_seq(60)
    s = [x for x in find_sites(oligo, record, 6) if x.strand == "+"][0]
    assert s.mismatches == () and s.ambiguous == (3, 4, 5)


def test_uncertain_bases_spend_the_search_budget():
    oligo = "CAGTGTGCCATATGTCACG"
    site = "NNNN" + oligo[4:]
    record = random_seq(60) + site + random_seq(60)
    assert [x for x in find_sites(oligo, record, 3) if x.strand == "+" and x.start == 60] == []
    assert [x for x in find_sites(oligo, record, 4) if x.strand == "+" and x.start == 60]


def test_packed_search_equals_brute_force_on_messy_records():
    """The block-packed, pruned search is exact: every budget, every character class."""
    import random

    from assaywatch.iupac import base_state

    rng = random.Random(2026)
    record_alphabet = "ACGTACGTACGTacgtUNRYSWKMBDHV-*X"
    for trial in range(150):
        L = rng.randint(8, 30)
        oligo = "".join(rng.choice("ACGTACGTRYNIS") for _ in range(L))
        rec = "".join(rng.choice(record_alphabet) for _ in range(rng.randint(0, 400)))
        # Plant a near-copy so there is something to find.
        if len(rec) > L + 10 and trial % 2:
            p = rng.randint(0, len(rec) - L)
            plant = "".join(c if c in "ACGT" else "A" for c in oligo)
            rec = rec[:p] + plant + rec[p + L :]
        for budget in (0, 2, 6, 12):
            want = set()
            up = rec.upper()
            for strand, seq in (("+", up), ("-", reverse_complement(up))):
                for s in range(len(seq) - L + 1):
                    states = [
                        base_state(oligo[i], seq[s + i]) if seq[s + i] in IUPAC else "mismatch"
                        for i in range(L)
                    ]
                    if sum(st != "match" for st in states) <= budget:
                        start = s if strand == "+" else len(seq) - s - L
                        mm = tuple(i for i, st in enumerate(states) if st == "mismatch")
                        want.add((start, strand, mm))
            got = {(x.start, x.strand, x.mismatches) for x in find_sites(oligo, rec, budget)}
            assert got == want, (oligo, rec, budget)
