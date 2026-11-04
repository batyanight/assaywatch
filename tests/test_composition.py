"""Tests for assaywatch.composition (ROADMAP "Lineage composition over time").

Synthetic windows only. Each test pins one rule of the stage at its interface.
"""

from __future__ import annotations

import dataclasses
import random

import pytest

from assaywatch.composition import (
    DIVERGED,
    Cell,
    cells_from,
    cluster_names,
    observed_series,
    organism,
    pool_small_clusters,
    same_mix_series,
    sample_windows,
    species_mix,
    species_years,
    split_change,
    title_tokens,
)
from assaywatch.drift import GraphRecord
from assaywatch.subcluster import OTHER, UNPLACED, Region
from assaywatch.taxonomy import Taxonomy


def _region(acc: str, seq: str, full: bool = True) -> Region:
    return Region(acc, seq, 5 if full else 2, 5, full)


def _distinct(n: int, prefix: str, seed: int) -> list[Region]:
    rng = random.Random(seed)
    return [_region(f"{prefix}{i}.1", "".join(rng.choice("ACGT") for _ in range(40))) for i in range(n)]


# ---- sample_windows (step 3) ----


def test_everything_distinct_and_full_flanked_is_taken_under_the_cap():
    regions = _distinct(6, "A", 1)
    years = [2001, 2001, 2002, 2002, 2003, 2003]
    assert sorted(sample_windows(regions, years, cap=100)) == list(range(6))


def test_a_short_flank_window_is_never_sampled():
    """Finding 2: short-flank windows are assigned by containment, never sampled,
    or a 100 bp assembly cut would define a lineage by less sequence than the rest."""
    regions = [*_distinct(2, "A", 2), _region("S1.1", "ACGT" * 10, full=False)]
    assert 2 not in sample_windows(regions, [2001, 2001, 2001], cap=100)


def test_identical_windows_count_once_whatever_their_order():
    """A clone deposited twenty times is one lineage member, not twenty."""
    seq = "ACGTTGCAAC" * 4
    regions = [_region(f"D{i}.1", seq) for i in range(5)] + _distinct(1, "U", 3)
    years = [2010] * 6
    chosen = sample_windows(regions, years, cap=100)
    assert sum(r.seq == seq for r in (regions[i] for i in chosen)) == 1
    shuffled = list(reversed(regions))
    again = sample_windows(shuffled, years, cap=100)
    assert {regions[i].record_id for i in chosen} == {shuffled[i].record_id for i in again}


def test_quiet_years_are_filled_before_busy_ones():
    """Round-robin across years: three records from each of two quiet years are
    all taken before a busy year gets its fourth."""
    regions = _distinct(100, "B", 4) + _distinct(3, "Q", 5) + _distinct(3, "R", 6)
    years = [2020] * 100 + [2005] * 3 + [2010] * 3
    chosen = sample_windows(regions, years, cap=9)
    by_year = sorted(years[i] for i in chosen)
    assert by_year == [2005] * 3 + [2010] * 3 + [2020] * 3


def test_a_cap_left_over_by_a_quiet_year_goes_to_the_others():
    regions = _distinct(50, "B", 7) + _distinct(1, "Q", 8)
    years = [2020] * 50 + [2005]
    chosen = sample_windows(regions, years, cap=10)
    assert len(chosen) == 10
    assert sum(years[i] == 2005 for i in chosen) == 1


def test_the_sample_does_not_depend_on_input_order():
    """Stable cluster ids rest on this: the same archive, read in any order, must
    sample the same records, so which ones are chosen inside a year comes from a
    hash of the accession, not from file order."""
    regions = _distinct(40, "C", 9)
    years = [2000 + (i % 4) for i in range(40)]
    first = {regions[i].record_id for i in sample_windows(regions, years, cap=12)}
    order = list(range(40))
    random.Random(10).shuffle(order)
    regions2 = [regions[i] for i in order]
    years2 = [years[i] for i in order]
    second = {regions2[i].record_id for i in sample_windows(regions2, years2, cap=12)}
    assert first == second


def test_the_accession_version_does_not_change_the_choice():
    """`.1` and `.2` of one accession are one record; a version bump must not
    reshuffle which records a year contributes."""
    a = _distinct(20, "V", 11)
    b = [Region(r.record_id.replace(".1", ".2"), r.seq, 5, 5, True) for r in a]
    years = [2015] * 20
    pick = lambda rs: {rs[i].record_id.split(".")[0] for i in sample_windows(rs, years, cap=5)}  # noqa: E731
    assert pick(a) == pick(b)


# ---- organism: the species name a record's title carries (step 6) ----
#
# The fallback for a record with no taxid. Every title below is a real one from the
# influenza, Chlamydia, coronavirus or haemosporidian archives on 2026-11-03.


def test_the_name_runs_up_to_the_qualifier_that_follows_it():
    cases = {
        "Chlamydia muridarum strain Cm tc0086::Tn chromosome, complete genome": "Chlamydia muridarum",
        "Plasmodium falciparum isolate KZ02-31032026-H1272-Pf cytochrome b (cytb) gene, partial cds": "Plasmodium falciparum",
        "Haemoproteus majoris clone H64/24R/H cytochrome b (cytb) gene, partial cds; mitochondrial": "Haemoproteus majoris",
        "Porcine epidemic diarrhea virus isolate HN230303, complete genome": "Porcine epidemic diarrhea virus",
        "Influenza A virus (A/New Mexico/31/2026(H3N2)) segment 7 matrix protein 2 (M2) and matrix protein 1 (M1) genes": "Influenza A virus",
        "Betacoronavirus sp. isolate BtCoV/Nycteris/DON008B005/BW/2021 RNA-dependent RNA polymerase gene": "Betacoronavirus sp.",
        "Leucocytozoon sp. isolate AE16-EM84-19-2096 cytochrome c oxidase subunit 3 (COX3) gene": "Leucocytozoon sp.",
        "Uncultured Chlamydia sp. clone CU 78/23 16S ribosomal RNA gene, partial sequence": "Chlamydia sp.",
    }
    for title, want in cases.items():
        assert organism(title) == want, title


def test_a_strain_that_is_part_of_the_name_is_kept():
    """ "Human coronavirus 229E" and "Human coronavirus OC43" are different viruses about
    30% apart. Cutting the title at two words pins both at "Human coronavirus", which is
    what held the pan-coronavirus purity at 68% whatever the cut (step 4b)."""
    assert organism("Human coronavirus 229E strain 0349 ORF1ab gene") == "Human coronavirus 229E"
    assert organism("Human coronavirus OC43 strain Seattle/USA/SC9430/2018") == "Human coronavirus OC43"


def test_a_strain_identifier_that_follows_the_name_is_not_part_of_it():
    """Measured on the archives: without this, 639 OC43 records produced 20-odd "species"
    and the coronavirus archive 3,106 distinct names for 700 organisms."""
    cases = {
        "Human coronavirus OC43 HCoVOC43_Fukushima_OR427_2021 ORF1ab gene": "Human coronavirus OC43",
        "Influenza A virus A/canine/Madison/5/2015 M gene": "Influenza A virus",
        "Human coronavirus 229E PREDICT_ZB12057 RNA-dependent RNA polymerase gene": "Human coronavirus 229E",
        "Haemoproteus sp. haplotype OWBM82083_NGS_subdominant cytochrome b": "Haemoproteus sp.",
    }
    for title, want in cases.items():
        assert organism(title) == want, title


def test_an_isolate_code_after_sp_is_not_part_of_the_name():
    """ "Plasmodium sp. AP30" is one unplaced Plasmodium, not a species of its own. Until
    the name stopped at "sp.", 3,186 of the haemosporidian archive's 3,873 names were
    singletons and every cluster of unplaced parasites read as a mixture."""
    cases = {
        "Plasmodium sp. AP30 cytochrome b (cytb) gene, partial cds": "Plasmodium sp.",
        "Leucocytozoon sp. L-ASOT2 cytochrome b gene, partial cds": "Leucocytozoon sp.",
        "Plasmodium sp. PADOM 08 cytochrome b gene": "Plasmodium sp.",
        "Haemoproteus sp. 7 XHu-2020 isolate FALTIN15 cytochrome b": "Haemoproteus sp.",
    }
    for title, want in cases.items():
        assert organism(title) == want, title


def test_a_serial_completes_a_virus_name_but_an_isolate_code_does_not():
    """The hard case, and it is only half solvable: "Human coronavirus 229E" carries its
    code in the species name, while "Bovine coronavirus SHG-5" does not, and the two look
    alike. A short letter-and-digit code or a serial is kept, anything else is not."""
    cases = {
        "Bufonid herpesvirus 1 isolate X": "Bufonid herpesvirus 1",
        "Bat coronavirus 1 PREDICT-B56331 RNA-dependent RNA polymerase mRNA": "Bat coronavirus 1",
        "Human coronavirus HKU1 strain Tokyo": "Human coronavirus HKU1",
        # lower case marks an isolate code, not part of a name
        "Pigeon coronavirus rin35 RNA, nearly complete genome": "Pigeon coronavirus",
        "Bovine coronavirus SHG-5 RNA, complete genome": "Bovine coronavirus",
        "Bovine coronavirus Mebus, complete genome": "Bovine coronavirus",
        "Rousettus aegyptiacus bat coronavirus 229E-related isolate 5425": "Rousettus aegyptiacus bat coronavirus",
    }
    for title, want in cases.items():
        assert organism(title) == want, title


def test_a_strain_code_after_a_binomial_is_not_part_of_the_name():
    """Found by running the rule over the Chlamydia archive: "Chlamydia psittaci NO-03"
    and "... YO-02" were two species of their own, both "new since design"."""
    assert organism("Chlamydia psittaci NO-03 16S ribosomal RNA gene") == "Chlamydia psittaci"
    assert organism("Chlamydia psittaci YO-02, complete genome") == "Chlamydia psittaci"


def test_a_name_that_is_itself_a_code_is_kept():
    """The rule above must not empty a title whose organism IS hyphenated and numbered."""
    assert organism("SARS-CoV-2 isolate Wuhan-Hu-1, complete genome") == "SARS-CoV-2"


def test_names_differing_only_in_case_are_one_species():
    mix = species_mix(["Influenza A virus"] * 5 + ["Influenza A Virus"] * 2)
    assert mix == [("Influenza A virus", 7)]


def test_a_title_with_no_organism_is_not_invented():
    assert organism("") == ""
    assert organism("complete genome") == ""
    assert organism("UNVERIFIED: Bufonid herpesvirus 1 isolate X") == "Bufonid herpesvirus 1"


def test_a_flag_about_the_record_is_not_part_of_the_organism():
    """Both found over the coronavirus archive, where each was a named species: "TPA_asm"
    on its own, and a truncated "Mutant Severe acute respiratory syndrome"."""
    assert organism("TPA_asm:Bat coronavirus isolate X RdRp gene") == "Bat coronavirus"
    assert organism("TPA_asm: Bat coronavirus isolate X RdRp gene") == "Bat coronavirus"
    # they stack, and only the first was stripped until this line
    assert (
        organism("MAG TPA_asm: Pigeon coronavirus rin35 RNA, nearly complete genome") == "Pigeon coronavirus"
    )
    assert (
        organism("Mutant Severe acute respiratory syndrome coronavirus 2 isolate Y")
        == "Severe acute respiratory syndrome coronavirus 2"
    )


def test_a_name_stops_before_it_runs_away():
    """A title with no qualifier at all must not become a sentence. Six words, because
    "Severe acute respiratory syndrome coronavirus 2" is six."""
    long = " ".join(f"Word{i}" for i in range(12))
    assert len(organism(long).split()) <= 6


# ---- species_mix and cluster_names (step 6) ----


def test_the_mix_is_counted_commonest_first_with_ties_by_name():
    mix = species_mix(["B virus", "A virus", "B virus", "C virus", "A virus", "B virus"])
    assert mix == [("B virus", 3), ("A virus", 2), ("C virus", 1)]


def test_a_cluster_of_one_species_is_named_for_it_abbreviated():
    assert cluster_names([[("Chlamydia trachomatis", 30)]], ["AB1"], pure_share=0.9) == ["C. trachomatis"]


def test_two_clusters_of_one_species_are_numbered_in_order():
    mixes = [[("Chlamydia trachomatis", 30)], [("Chlamydia psittaci", 9)], [("Chlamydia trachomatis", 4)]]
    names = cluster_names(mixes, ["AB1", "AB2", "AB3"], pure_share=0.9)
    assert names == ["C. trachomatis 1", "C. psittaci", "C. trachomatis 2"]


def test_a_name_that_is_not_a_binomial_is_left_alone():
    mixes = [[("Porcine epidemic diarrhea virus", 10)], [("Plasmodium sp.", 10)], [("Influenza A virus", 10)]]
    names = cluster_names(mixes, ["A", "B", "C"], pure_share=0.9)
    assert names == ["Porcine epidemic diarrhea virus", "Plasmodium sp.", "Influenza A virus"]


def test_a_mixed_cluster_carries_its_modal_share_so_the_name_is_not_read_as_the_whole():
    """The 2,000-window coronavirus cluster was 15% its modal organism. A legend entry
    reading "Human coronavirus" would have been a false statement about 85% of it."""
    mix = [("Plasmodium falciparum", 38), ("Plasmodium vivax", 32), ("Plasmodium sp.", 30)]
    assert cluster_names([mix], ["AB1"], pure_share=0.9) == ["P. falciparum 38%"]


def test_a_cluster_with_no_named_species_falls_back_to_its_representative():
    assert cluster_names([[]], ["MT581450"], pure_share=0.9) == ["unnamed (MT581450)"]


# ---- title_tokens: what else a cluster holds (step 6) ----


def _hcov(strain, n):
    return [f"Human coronavirus {strain} strain {i} ORF1ab gene, complete genome" for i in range(n)]


def test_a_token_frequent_here_and_rare_elsewhere_is_distinguishing():
    mine, other = _hcov("229E", 10), _hcov("OC43", 10)
    tokens = title_tokens(mine, other, name="Human coronavirus", min_share=0.2, min_lift=2.0, top=5)
    assert "229E" in tokens and "OC43" not in tokens


def test_a_token_in_every_cluster_is_not_distinguishing():
    mine, other = _hcov("229E", 10), _hcov("OC43", 10)
    tokens = title_tokens(mine, other, name="Human coronavirus", min_share=0.2, min_lift=2.0, top=5)
    for everywhere in ("strain", "ORF1ab", "gene", "complete", "genome"):
        assert everywhere not in tokens, everywhere


def test_the_name_s_own_words_are_not_tokens():
    mine, other = _hcov("229E", 10), ["Bat coronavirus isolate 1 RdRp gene"] * 10
    tokens = title_tokens(mine, other, name="Human coronavirus 229E", min_share=0.2, min_lift=2.0, top=5)
    assert not {"Human", "coronavirus", "229E"} & set(tokens)


def test_a_rare_token_is_not_promoted_by_lift_alone():
    mine = _hcov("229E", 10) + ["Human coronavirus 229E isolate oddity XYZ99 gene"]
    tokens = title_tokens(
        mine, _hcov("OC43", 10), name="Human coronavirus", min_share=0.2, min_lift=2.0, top=5
    )
    assert "XYZ99" not in tokens


def test_with_nothing_to_compare_against_no_token_distinguishes():
    assert title_tokens(_hcov("229E", 10), [], name="x", min_share=0.2, min_lift=2.0, top=5) == []


def test_a_record_qualifier_is_never_a_token():
    """Found by the test below on its first run: this cluster's depositors wrote "clone"
    where the others wrote "isolate", so "clone" scored a perfect lift and outranked the
    lineage code. A submitter's habit is not a fact about the lineage."""
    mine = [f"Plasmodium relictum lineage SGS1 clone {i} cytb gene" for i in range(10)]
    other = [f"Plasmodium vivax isolate {i} cytb gene" for i in range(10)]
    tokens = title_tokens(mine, other, name="Plasmodium relictum", min_share=0.2, min_lift=2.0, top=5)
    assert "clone" not in tokens and "SGS1" in tokens


def test_tokens_are_ordered_by_how_well_they_separate_and_capped():
    mine = [f"Plasmodium relictum lineage SGS1 clone {i} cytb gene Austria" for i in range(10)]
    other = [f"Plasmodium vivax lineage VIV01 isolate {i} cytb gene Brazil" for i in range(10)]
    kw = {"name": "Plasmodium relictum", "min_share": 0.2, "min_lift": 2.0}
    # "lineage" and "cytb" are in both and separate nothing; the cap takes the first.
    assert title_tokens(mine, other, top=5, **kw) == ["Austria", "SGS1"]
    assert title_tokens(mine, other, top=1, **kw) == ["Austria"]


# ---- the same-mix line (step 7) ----
#
# Direct standardisation: each year's detection recomputed on the whole period's
# lineage mix. Every number below is computed by hand in the test.


#: Two lineages 100 records each, so each weighs 0.5 over the period. A detects always,
#: B never, and the MIX swings from 80/20 to 20/80 between the two years.
_MIX_SWING = [
    Cell(2020, 0, 80, 80),
    Cell(2020, 1, 20, 0),
    Cell(2021, 0, 20, 20),
    Cell(2021, 1, 80, 0),
]


def test_the_observed_share_is_the_year_s_own_arithmetic():
    assert observed_series(_MIX_SWING) == {2020: 0.8, 2021: 0.2}


def test_holding_the_mix_fixed_flattens_a_fall_that_was_only_the_mix():
    """The whole point of the panel. Observed detection falls from 80% to 20% while
    neither lineage's own detection moved at all: A detects everything in both years and
    B nothing. On the period's 50/50 mix both years read 0.5."""
    assert same_mix_series(_MIX_SWING, min_covered=0.8) == {2020: 0.5, 2021: 0.5}


def test_a_real_fall_within_a_lineage_survives_standardisation():
    cells = [
        Cell(2020, 0, 50, 50),
        Cell(2020, 1, 50, 25),
        Cell(2021, 0, 50, 25),
        Cell(2021, 1, 50, 25),
    ]
    # weights 0.5/0.5; 2020 = .5*1.0 + .5*0.5 = 0.75, 2021 = .5*0.5 + .5*0.5 = 0.5
    assert same_mix_series(cells, min_covered=0.8) == {2020: 0.75, 2021: 0.5}


def test_an_unchanging_mix_leaves_the_year_as_it_was():
    cells = [Cell(2020, 0, 50, 40), Cell(2020, 1, 50, 10), Cell(2021, 0, 50, 30), Cell(2021, 1, 50, 20)]
    assert same_mix_series(cells, min_covered=0.8) == observed_series(cells)


def test_a_year_missing_too_much_of_the_mix_is_not_drawn():
    """A year holding one lineage of a two-lineage assay says nothing about the other,
    and standardising over it would invent the missing half."""
    cells = [*_MIX_SWING, Cell(2022, 0, 10, 10)]
    assert 2022 not in same_mix_series(cells, min_covered=0.8)


def test_the_weights_of_a_drawn_year_are_renormalised_over_what_is_present():
    cells = [Cell(2020, 0, 90, 45), Cell(2020, 1, 10, 10), Cell(2021, 0, 90, 90)]
    # weights: A 180/190, B 10/190. 2021 holds only A, covering 94.7% of the weight,
    # so it is drawn at A's own rate.
    out = same_mix_series(cells, min_covered=0.9)
    assert out[2021] == 1.0
    assert out[2020] == pytest.approx((180 / 190) * 0.5 + (10 / 190) * 1.0)


def test_other_and_diverged_are_strata_like_any_other():
    """A record the clustering could not place is still a record the graph counted, so it
    carries weight; dropping it would make the line disagree with the graph."""
    cells = [
        Cell(2020, 0, 50, 50),
        Cell(2020, UNPLACED, 50, 0),
        Cell(2021, 0, 50, 50),
        Cell(2021, UNPLACED, 50, 0),
    ]
    assert same_mix_series(cells, min_covered=0.8) == {2020: 0.5, 2021: 0.5}


def test_an_empty_year_or_an_empty_assay_yields_no_point():
    assert same_mix_series([], min_covered=0.8) == {}
    assert observed_series([]) == {}
    cells = [*_MIX_SWING, Cell(2022, 0, 0, 0), Cell(2022, 1, 0, 0)]
    assert 2022 not in same_mix_series(cells, min_covered=0.8)
    assert 2022 not in observed_series(cells)


# ---- the mix / within split (step 8) ----
#
# Kitagawa: mix = sum (w_r - w_b)(p_r + p_b)/2, within = sum (p_r - p_b)(w_r + w_b)/2.
# Both parts are worked by hand in each test.


def test_a_change_that_was_only_the_mix_is_all_mix():
    """Baseline 80/20 of a lineage that always detects and one that never does, recent
    20/80: the share falls 0.8 -> 0.2 and not one lineage's own detection moved."""
    base = [Cell(2020, 0, 80, 80), Cell(2020, 1, 20, 0)]
    recent = [Cell(2025, 0, 20, 20), Cell(2025, 1, 80, 0)]
    s = split_change(base, recent, n_boot=0, seed=0)
    assert (s.baseline_share, s.recent_share) == (0.8, 0.2)
    assert s.change == pytest.approx(-0.6)
    assert s.mix == pytest.approx(-0.6)
    assert s.within == pytest.approx(0.0)


def test_a_change_inside_the_lineages_is_all_within():
    base = [Cell(2020, 0, 50, 50), Cell(2020, 1, 50, 25)]
    recent = [Cell(2025, 0, 50, 25), Cell(2025, 1, 50, 25)]
    s = split_change(base, recent, n_boot=0, seed=0)
    assert s.change == pytest.approx(-0.25)
    assert s.mix == pytest.approx(0.0)
    assert s.within == pytest.approx(-0.25)


def test_the_two_parts_always_add_up_to_the_change():
    """The identity is the reason this decomposition and not another; a reader who adds
    the two numbers printed beside each other must get the third."""
    rng = random.Random(4)
    for _ in range(50):
        ks = range(rng.randint(1, 5))
        base = [Cell(2020, k, rng.randint(1, 99), 0) for k in ks]
        recent = [Cell(2025, k, rng.randint(1, 99), 0) for k in ks]
        base = [Cell(c.year, c.cluster, c.records, rng.randint(0, c.records)) for c in base]
        recent = [Cell(c.year, c.cluster, c.records, rng.randint(0, c.records)) for c in recent]
        s = split_change(base, recent, n_boot=0, seed=0)
        assert s.mix + s.within == pytest.approx(s.change, abs=1e-12)


def test_a_lineage_seen_in_only_one_period_is_a_mix_change_and_is_named():
    """It has no detection rate in the period where it does not appear, so a within part
    cannot be computed for it, and a lineage that APPEARED is a change in the mix. The
    identity survives, and the cluster is recorded so the report can say so."""
    base = [Cell(2020, 0, 50, 25)]
    recent = [Cell(2025, 0, 50, 25), Cell(2025, 1, 50, 0)]
    s = split_change(base, recent, n_boot=0, seed=0)
    assert s.one_period_clusters == (1,)
    assert s.mix + s.within == pytest.approx(s.change)
    assert s.within == pytest.approx(0.0)
    assert s.mix == pytest.approx(-0.25)


def test_an_empty_period_has_no_split():
    assert split_change([], [Cell(2025, 0, 5, 5)], n_boot=0, seed=0) is None
    assert split_change([Cell(2020, 0, 5, 5)], [], n_boot=0, seed=0) is None
    assert split_change([Cell(2020, 0, 0, 0)], [Cell(2025, 0, 5, 5)], n_boot=0, seed=0) is None


def test_without_a_bootstrap_there_is_no_interval():
    s = split_change([Cell(2020, 0, 9, 3)], [Cell(2025, 0, 9, 6)], n_boot=0, seed=0)
    assert s.mix_ci is None and s.within_ci is None and s.n_boot == 0


def test_the_bootstrap_is_deterministic_under_its_seed():
    base = [Cell(2020, 0, 80, 60), Cell(2020, 1, 20, 5)]
    recent = [Cell(2025, 0, 40, 25), Cell(2025, 1, 60, 20)]
    a = split_change(base, recent, n_boot=200, seed=7)
    b = split_change(base, recent, n_boot=200, seed=7)
    c = split_change(base, recent, n_boot=200, seed=8)
    assert a.mix_ci == b.mix_ci and a.within_ci == b.within_ci
    assert a.mix_ci != c.mix_ci
    assert a.mix_ci[0] <= a.mix_ci[1] and a.within_ci[0] <= a.within_ci[1]


def test_more_records_narrow_the_interval():
    def width(scale):
        base = [Cell(2020, 0, 80 * scale, 60 * scale), Cell(2020, 1, 20 * scale, 5 * scale)]
        recent = [Cell(2025, 0, 40 * scale, 25 * scale), Cell(2025, 1, 60 * scale, 20 * scale)]
        s = split_change(base, recent, n_boot=400, seed=3)
        return s.mix_ci[1] - s.mix_ci[0]

    assert width(20) < width(1)


# ---- species first years, and what is new since the assay was designed (step 9) ----


def _taxonomy() -> Taxonomy:
    """Morbillivirus canis (3052342) with the old id 11232 merged into it and the no-rank
    child 3139435 "canine distemper virus" under it, beside a second species. The shape
    that made a species copy look new to the archive before `species_of` existed."""
    return Taxonomy(
        parent={3052342: 11158, 3139435: 3052342, 1891763: 11158, 10632: 1891763, 11158: 1},
        merged={11232: 3052342},
        rank={3052342: "species", 1891763: "species", 11158: "genus"},
        name={
            3052342: "Morbillivirus canis",
            3139435: "canine distemper virus",
            1891763: "Betapolyomavirus secuhominis",
            10632: "JC polyomavirus",
            11158: "Morbillivirus",
        },
    )


def test_a_merged_taxid_and_its_current_id_are_one_species():
    rows = [(11232, 2015, "x"), (3052342, 2019, "x")]
    got = species_years(rows, _taxonomy(), design_year=2007)
    assert [(s.name, s.first_year, s.records) for s in got] == [("Morbillivirus canis", 2015, 2)]


def test_a_no_rank_child_is_its_species_not_a_species_of_its_own():
    rows = [(3139435, 2011, "x"), (3052342, 2018, "x"), (10632, 2020, "y")]
    got = species_years(rows, _taxonomy(), design_year=2007)
    assert [(s.name, s.first_year) for s in got] == [
        ("Morbillivirus canis", 2011),
        ("Betapolyomavirus secuhominis", 2020),
    ]


def test_new_since_design_means_first_deposited_after_the_design_year():
    rows = [(3052342, 2007, "x"), (1891763, 2008, "y")]
    got = {s.name: s.new_since_design for s in species_years(rows, _taxonomy(), design_year=2007)}
    assert got == {"Morbillivirus canis": False, "Betapolyomavirus secuhominis": True}


def test_without_a_design_year_nothing_is_called_new():
    rows = [(3052342, 2021, "x")]
    assert [s.new_since_design for s in species_years(rows, _taxonomy(), design_year=None)] == [False]


def test_a_record_with_no_taxid_falls_back_to_the_name_in_its_title():
    """Most archive metadata predates the taxid column, so this is the common case, and
    such a row cannot be rolled up to a species: it is named as the depositor wrote it."""
    rows = [(None, 2016, "Chlamydia psittaci strain 84/2334 16S ribosomal RNA gene")]
    got = species_years(rows, _taxonomy(), design_year=1997)
    assert [(s.taxid, s.name, s.new_since_design) for s in got] == [(None, "Chlamydia psittaci", True)]


def test_a_taxid_the_cache_does_not_hold_is_kept_and_named_from_its_title():
    rows = [(999999, 2022, "Bufonid herpesvirus 1 isolate X")]
    got = species_years(rows, _taxonomy(), design_year=2020)
    assert [(s.taxid, s.name) for s in got] == [(999999, "Bufonid herpesvirus 1")]


def test_a_record_with_no_deposit_year_cannot_date_a_species():
    rows = [(3052342, 0, "x"), (3052342, 2014, "x")]
    got = species_years(rows, _taxonomy(), design_year=2007)
    assert [(s.first_year, s.records) for s in got] == [(2014, 1)]
    assert species_years([(3052342, 0, "x")], _taxonomy(), design_year=2007) == []


def test_species_come_back_oldest_first():
    rows = [(1891763, 2020, "y"), (3052342, 2001, "x"), (999999, 2020, "Aaa bbb")]
    got = species_years(rows, _taxonomy(), design_year=2007)
    assert [s.first_year for s in got] == [2001, 2020, 2020]
    assert [s.name for s in got][1:] == ["Aaa bbb", "Betapolyomavirus secuhominis"]


# ---- the panel's cells, and the diverged stratum (step 11) ----


def _rec(rid, year, call="detect", *, evaluable=True, detected=True, diverged=False, recent=True):
    return GraphRecord(rid, year, call, evaluable, detected, recent, None, diverged)


def test_the_three_labels_outside_the_clustering_cannot_collide():
    """`other`, `unplaced` and `diverged` share one label space with the clusters
    `0, 1, ...`, so a collision would silently merge two strata."""
    assert len({OTHER, UNPLACED, DIVERGED}) == 3
    assert all(label < 0 for label in (OTHER, UNPLACED, DIVERGED))


def test_a_diverged_record_is_its_own_stratum_however_it_was_called():
    """Decision 2026-11-02: it has no amplicon coordinates, so no window can be cut from
    it and no cluster can be guessed for it. Under `count_diverged_as_fail` it is counted
    as a failure, so it is in the denominator and must be drawn."""
    records = [_rec("A.1", 2024, "fail", detected=False, diverged=True), _rec("B.1", 2024)]
    cells = cells_from(records, {"A.1": 0, "B.1": 0})
    assert sorted((c.cluster, c.records) for c in cells) == [(DIVERGED, 1), (0, 1)]


def test_a_record_the_clustering_could_not_place_is_unplaced():
    cells = cells_from([_rec("A.1", 2024)], {})
    assert [(c.cluster, c.records) for c in cells] == [(UNPLACED, 1)]


def test_a_record_outside_the_denominator_is_in_no_cell():
    """The panel sits under the graph and shares its denominator: a record with no
    amplicon is not in the graph's evaluable count, so it is not in the panel either."""
    records = [_rec("A.1", 2024), _rec("B.1", 2024, "no_amplicon", evaluable=False, detected=False)]
    cells = cells_from(records, {"A.1": 0, "B.1": 0})
    assert [(c.records, c.detected) for c in cells] == [(1, 1)]


def test_cells_count_records_and_detections_per_year_and_cluster():
    records = [
        _rec("A.1", 2024),
        _rec("B.1", 2024, "fail", detected=False),
        _rec("C.1", 2025, "reduced"),
        _rec("D.1", 2025, "fail", detected=False),
    ]
    cells = cells_from(records, {"A.1": 0, "B.1": 0, "C.1": 1, "D.1": 1})
    assert [(c.year, c.cluster, c.records, c.detected) for c in cells] == [
        (2024, 0, 2, 1),
        (2025, 1, 2, 1),
    ]


def test_every_evaluable_record_lands_in_exactly_one_cell():
    """The invariant the panel rests on, at this level: the cells of a year sum to that
    year's evaluable and detected counts."""
    rng = random.Random(12)
    records, labels = [], {}
    for i in range(200):
        rid = f"R{i}.1"
        ev = rng.random() < 0.8
        records.append(
            _rec(
                rid,
                2020 + i % 5,
                "detect" if ev else "no_amplicon",
                evaluable=ev,
                detected=ev and rng.random() < 0.5,
                diverged=ev and rng.random() < 0.2,
            )
        )
        if rng.random() < 0.7:
            labels[rid] = rng.randint(0, 3)
    cells = cells_from(records, labels)
    for year in {r.year for r in records}:
        mine = [r for r in records if r.year == year]
        rows = [c for c in cells if c.year == year]
        assert sum(c.records for c in rows) == sum(1 for r in mine if r.evaluable)
        assert sum(c.detected for c in rows) == sum(1 for r in mine if r.evaluable and r.detected)


def test_only_the_biggest_clusters_are_drawn_and_the_rest_pool_into_other():
    cells = [Cell(2024, k, 10 - k, 0) for k in range(5)]  # 10, 9, 8, 7, 6 records
    pooled = pool_small_clusters(cells, show=2)
    assert sorted((c.cluster, c.records) for c in pooled) == [(OTHER, 8 + 7 + 6), (0, 10), (1, 9)]


def test_diverged_and_unplaced_are_never_pooled_away():
    """They are statements about what the clustering could not do, and the panel's
    sentence states their share; pooling them into "other" would hide exactly that."""
    cells = [
        Cell(2024, 0, 50, 0),
        Cell(2024, 1, 40, 0),
        Cell(2024, DIVERGED, 3, 0),
        Cell(2024, UNPLACED, 2, 0),
    ]
    pooled = pool_small_clusters(cells, show=1)
    assert sorted((c.cluster, c.records) for c in pooled) == [
        (DIVERGED, 3),
        (UNPLACED, 2),
        (OTHER, 40),
        (0, 50),
    ]


def test_pooling_keeps_every_record_and_every_year():
    cells = [Cell(y, k, k + y % 3, 1) for y in (2023, 2024) for k in range(6)]
    pooled = pool_small_clusters(cells, show=2)
    assert sum(c.records for c in pooled) == sum(c.records for c in cells)
    assert sum(c.detected for c in pooled) == sum(c.detected for c in cells)
    assert {c.year for c in pooled} == {2023, 2024}


def test_the_options_defaults_match_the_settings_model():
    """`Options.from_config` carries in-code fallbacks so a hand-built cfg works in a
    test, which is the repo's pattern -- and the hazard `test_settings` was written for:
    six such defaults had drifted from config.yaml before that model existed. Every one
    here must agree with `settings.Composition`, which is the contract."""
    from assaywatch.composition import Options
    from assaywatch.settings import Composition

    model = Composition().model_dump()
    mine = Options.from_config({})
    fields = {f.name for f in dataclasses.fields(Options)}
    assert fields <= set(model), sorted(fields - set(model))
    for key in fields:
        assert getattr(mine, key) == model[key], key
    # The model may hold keys the STAGE does not read, when their reader is elsewhere:
    # `report_min_mix` is read by `report.mix_rows`, which decides what the report names,
    # and `site_max_bytes` by `site.main`, which refuses to write a file over it.
    assert set(model) - fields == {"report_min_mix", "site_max_bytes"}


def test_the_options_read_the_committed_config():
    from assaywatch.composition import Options
    from assaywatch.score import load_config

    assert Options.from_config(load_config()).cut == 0.05
