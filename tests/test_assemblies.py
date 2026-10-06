"""Assembly retrieval, offline: a fake Datasets service serving synthetic genomes.

The decisions under test: listing survives the one-page TSV limit, the sample
is stable and tops up incrementally, and cutting a genome down to its loci
changes no call the screener would make on the whole genome.
"""

import csv
import gzip
import io
import random
import zipfile
from collections import Counter
from datetime import date

import pytest
from test_score import ASSAYS, CFG, RECORDS

from assaywatch.assemblies import (
    AssemblyMeta,
    extract_loci,
    list_assemblies,
    retrieve_assemblies,
    sample_per_year,
)
from assaywatch.fasta import read_fasta
from assaywatch.report import read_years
from assaywatch.retrieve import record_run, targets_from_registry
from assaywatch.score import screen_record

BD = "CHYTRID_Bd_Internal_transcribes_spa_Boyle_2004"


def random_dna(n, seed):
    rng = random.Random(seed)
    return "".join(rng.choice("ACGT") for _ in range(n))


class FakeDatasets:
    """Serves a list of assemblies (TSV, truncated at page_size like the real one) and their genomes."""

    HEADER = "Assembly Accession\tAssembly Release Date\tCollection\tLevel\tOrganism\tStrain\n"

    def __init__(self, metas, genomes):
        self.metas, self.genomes = metas, genomes
        self.report_calls = 0
        self.downloaded = []

    def __call__(self, path, params, accept):
        if path.endswith("dataset_report"):
            self.report_calls += 1
            lo, hi = params["filters.first_release_date"], params["filters.last_release_date"]
            rows = [m for m in self.metas if lo <= m.release_date <= hi][: params["page_size"]]
            body = self.HEADER + "".join(
                f"{m.accession}\t{m.release_date}\t{m.collection_date}\t{m.level}\t{m.organism}\t{m.strain}\n"
                for m in rows
            )
            return body.encode()
        accs = path.split("/")[2].split(",")
        self.downloaded += accs
        buf = io.BytesIO()
        with zipfile.ZipFile(buf, "w") as zf:
            for acc in accs:
                if acc in self.genomes:
                    fna = "".join(f">{cid} contig\n{seq}\n" for cid, seq in self.genomes[acc])
                    zf.writestr(f"ncbi_dataset/data/{acc}/{acc}_x_genomic.fna", fna)
        return buf.getvalue()


def meta(i, day):
    return AssemblyMeta(f"GCA_{i:09d}.1", day, "2010", "Complete Genome", "Testus coli", f"S{i}")


def test_listing_splits_date_windows_until_each_fits_a_page():
    metas = [meta(i, f"20{10 + i % 12:02d}-{1 + i % 12:02d}-{1 + i % 28:02d}") for i in range(57)]
    fake = FakeDatasets(metas, {})
    got = list_assemblies(fake, 1, ["complete_genome"], None, date(2026, 1, 1), page=5)
    assert {m.accession for m in got} == {m.accession for m in metas}
    assert fake.report_calls > 57 // 5


def test_sample_is_capped_per_year_stable_and_tops_up():
    metas = [meta(i, f"20{20 + i % 3}-06-01") for i in range(30)]
    first = sample_per_year(metas, 4, Counter())
    assert Counter(m.year for m in first) == {2020: 4, 2021: 4, 2022: 4}
    assert first == sample_per_year(list(reversed(metas)), 4, Counter())  # order-independent
    topped = sample_per_year(metas, 4, Counter({2020: 4, 2021: 1}))
    assert Counter(m.year for m in topped) == {2021: 3, 2022: 4}


def _bd_genome(seed):
    """A 'genome': two contigs, a Bd Boyle site in one, a second copy in the other, plus noise."""
    site = RECORDS[f"{BD}__perfect"]
    a = random_dna(40_000, seed) + site + random_dna(30_000, seed + 1)
    b = random_dna(9_000, seed + 2) + site + random_dna(2_000, seed + 3)
    return [("c1", a), ("c2", b), ("plasmid", random_dna(5_000, seed + 4))]


def _pairs(assay):
    return [(assay.oligos.forward.matching_seq, assay.oligos.reverse.matching_seq)]


@pytest.mark.parametrize("name", [r for r in RECORDS if r.startswith(BD)][:12])
def test_extracted_loci_screen_exactly_like_the_whole_genome(name):
    assay = ASSAYS[BD]
    site = RECORDS[name]
    contigs = [("c1", random_dna(20_000, 1) + site + random_dna(20_000, 2)), ("c2", random_dna(8_000, 3))]
    seq, _ = extract_loci(contigs, _pairs(assay), CFG)
    whole = [screen_record(assay, cid, s, CFG) for cid, s in contigs]
    best_whole = min(
        whole, key=lambda c: ({"detect": 0, "reduced": 1, "fail": 2}.get(c.call, 3), c.penalty or 0)
    )
    cut = screen_record(assay, "x", seq, CFG) if seq else None
    if best_whole.call == "no_amplicon":
        assert cut is None or cut.call == "no_amplicon"
    else:
        assert (cut.call, cut.penalty, cut.amplicon_bp) == (
            best_whole.call,
            best_whole.penalty,
            best_whole.amplicon_bp,
        )


def test_windows_are_small_and_never_pair_across_a_spacer():
    assay = ASSAYS[BD]
    genome = _bd_genome(5)
    seq, n = extract_loci(genome, _pairs(assay), CFG)
    assert n == 2  # the two real copies; chance single-oligo sites do not make a window
    assert len(seq.replace("N", "")) < 2 * (len(RECORDS[f"{BD}__perfect"]) + 2 * 100)
    assert screen_record(assay, "g", seq, CFG).call == "detect"


@pytest.fixture
def cfg(tmp_path):
    return {
        **CFG,
        "retrieved_dir": str(tmp_path / "retrieved"),
        "assemblies": {"taxa": [109871], "levels": ["complete_genome"], "per_year": 2, "batch": 3},
    }


def test_retrieve_assemblies_end_to_end_and_incrementally(cfg, tmp_path):
    metas = [meta(i, f"20{18 + i % 4}-03-0{1 + i % 5}") for i in range(12)]
    genomes = {m.accession: _bd_genome(i) for i, m in enumerate(metas) if i % 3}  # every 3rd has no download
    fake = FakeDatasets(metas, genomes)
    pairs = _pairs(ASSAYS[BD])

    run = retrieve_assemblies(109871, cfg, fake, pairs=pairs, assays=[BD], run_date="2026-10-04")
    assert run.group == "asm" and len(fake.downloaded) == 8  # 2 per year x 4 years requested
    missing = [a for a in fake.downloaded if a not in genomes]
    assert missing, "the fixture should leave some picked genomes undownloadable"
    assert run.n_fetched == 8 - len(missing) and "retried next run" in run.note
    recs = dict(read_fasta(run.fasta))
    assert recs and all(acc.startswith("GCA_") for acc in recs)
    with gzip.open(run.metadata, "rt") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    # A genome that was not downloaded is not recorded, so it does not use up its year's quota.
    assert len(rows) == run.n_fetched and not {r["accession"] for r in rows} & set(missing)
    # The report's year join reads it like any nuccore metadata.
    years = read_years(tmp_path / "retrieved")
    assert {years[a.rsplit(".", 1)[0]] for a in recs} <= {2018, 2019, 2020, 2021}
    record_run(cfg, run)

    # The missing genomes become available: the next run retries exactly those.
    fake.genomes.update({a: _bd_genome(3) for a in missing})
    fake.downloaded = []
    retry = retrieve_assemblies(109871, cfg, fake, pairs=pairs, assays=[BD], run_date="2026-10-05")
    assert retry.mode == "incremental" and sorted(fake.downloaded) == sorted(missing)
    assert retry.n_fetched == len(missing)
    record_run(cfg, retry)

    # Nothing new released: the next run fetches nothing.
    again = retrieve_assemblies(109871, cfg, fake, pairs=pairs, assays=[BD], run_date="2026-10-11")
    assert again.n_fetched == 0 and again.note == "nothing new"
    # A new release tops up its year only up to the quota.
    fake.metas = metas + [meta(100, "2026-10-08"), meta(101, "2026-10-09"), meta(102, "2026-10-10")]
    fake.genomes.update({m.accession: _bd_genome(7) for m in fake.metas[-3:]})
    later = retrieve_assemblies(109871, cfg, fake, pairs=pairs, assays=[BD], run_date="2026-10-11")
    assert later.mode == "incremental" and later.n_fetched == 2


def test_registry_adds_an_asm_group_only_for_configured_taxa(cfg):
    from test_score import ROOT

    groups = targets_from_registry([ROOT / "registry"], cfg)
    asm = {k: v for k, v in groups.items() if k[1] == "asm"}
    assert list(asm) == [(109871, "asm")]
    assert BD in asm[(109871, "asm")]["assays"] and asm[(109871, "asm")]["pairs"]
    assert not any(k[1] == "asm" for k in targets_from_registry([ROOT / "registry"]))


def test_a_locus_on_the_minus_strand_is_kept():
    from assaywatch.iupac import reverse_complement

    assay = ASSAYS[BD]
    site = reverse_complement(RECORDS[f"{BD}__perfect"])
    seq, n = extract_loci([("c1", random_dna(20_000, 9) + site + random_dna(20_000, 10))], _pairs(assay), CFG)
    assert n == 1 and screen_record(assay, "g", seq, CFG).call == "detect"


def test_current_year_quota_grows_through_the_year():
    metas = [meta(i, f"2026-0{1 + i % 9}-01") for i in range(40)]
    jan = sample_per_year(metas, 12, Counter(), today=date(2026, 1, 15))
    oct_ = sample_per_year(metas, 12, Counter(), today=date(2026, 10, 1))
    import math

    # The year's quota is ceil(12 x the fraction of the year elapsed).
    assert len(jan) == math.ceil(12 * 15 / 365) == 1
    assert len(oct_) == math.ceil(12 * 274 / 365) == 10
    past = sample_per_year([meta(i, "2025-03-01") for i in range(40)], 12, Counter(), today=date(2026, 1, 15))
    assert len(past) == 12


def test_a_newer_version_in_the_download_still_counts(cfg):
    from assaywatch.assemblies import iter_genomes

    m = meta(1, "2020-01-01")
    newer = m.accession.replace(".1", ".2")

    def serves_newer(path, params, accept):
        buf = io.BytesIO()
        with zipfile.ZipFile(buf, "w") as zf:
            zf.writestr(f"ncbi_dataset/data/{newer}/{newer}_x_genomic.fna", ">c1 x\nACGTACGT\n")
        return buf.getvalue()

    got = dict(iter_genomes(serves_newer, [m.accession]))
    assert got[m.accession]  # GCA_x.2 served for GCA_x.1


def test_changed_primer_pairs_recut_every_genome(cfg, tmp_path):
    metas = [meta(i, f"20{18 + i % 2}-03-01") for i in range(4)]
    fake = FakeDatasets(metas, {m.accession: _bd_genome(i) for i, m in enumerate(metas)})
    pairs = _pairs(ASSAYS[BD])
    record_run(cfg, retrieve_assemblies(109871, cfg, fake, pairs=pairs, run_date="2026-10-04"))
    fake.downloaded = []
    same = retrieve_assemblies(109871, cfg, fake, pairs=pairs, run_date="2026-10-05")
    assert same.note == "nothing new" and not fake.downloaded
    other = pairs + [("ACGTACGTACGTACGTAC", "TTGCATTGCATTGCATTG")]
    recut = retrieve_assemblies(109871, cfg, fake, pairs=other, run_date="2026-10-05")
    assert recut.mode == "full" and sorted(fake.downloaded) == sorted(m.accession for m in metas)
    d = tmp_path / "retrieved" / "109871" / "asm"
    assert len(list(d.glob("*.fasta.gz"))) == 1 and list(d.glob("*.superseded"))


# --------------------------------------------------------------------------
# An archive is the genome CUT to the windows the settings keep, so changing a
# setting the cut depends on has to re-cut. Only a change to the primer pairs did.
# --------------------------------------------------------------------------


def _first_run(cfg, run_date="2026-10-04"):
    metas = [meta(i, f"20{18 + i % 4}-03-0{1 + i % 5}") for i in range(8)]
    fake = FakeDatasets(metas, {m.accession: _bd_genome(i) for i, m in enumerate(metas)})
    pairs = _pairs(ASSAYS[BD])
    run = retrieve_assemblies(109871, cfg, fake, pairs=pairs, assays=[BD], run_date=run_date)
    record_run(cfg, run)
    return fake, pairs, run


def _edited(cfg, path, value):
    import copy

    new = copy.deepcopy(cfg)
    node = new
    for key in path[:-1]:
        node = node.setdefault(key, {})
    node[path[-1]] = value
    return new


def test_cut_parameters_name_every_setting_extract_loci_reads(cfg):
    from assaywatch.assemblies import cut_parameters

    cut = cut_parameters(cfg)
    assert set(cut) == {"max_mismatches", "min_bp", "max_bp", "overhang_bp", "max_pair_evalue"}
    assert cut["max_mismatches"] == 6
    assert (
        cut_parameters(_edited(cfg, ("scoring", "by_chemistry"), {"mgb": {"max_mismatches_searched": 9}}))[
            "max_mismatches"
        ]
        == 9
    )


def test_the_cut_settings_are_recorded_beside_the_archives(cfg, tmp_path):
    import json

    from assaywatch.assemblies import cut_parameters

    _first_run(cfg)
    recorded = json.loads((tmp_path / "retrieved" / "109871" / "asm" / "cut.json").read_text())
    assert recorded == cut_parameters(cfg)


@pytest.mark.parametrize(
    "path, value",
    [
        (("scoring", "by_chemistry"), {"conventional": {"max_mismatches_searched": 8}}),
        (("scoring", "max_mismatches_searched"), 7),
        (("amplicon", "max_bp"), 2999),
        (("amplicon", "min_bp"), 51),
        (("amplicon", "record_min_overhang_bp"), 101),
        (("assemblies", "max_pair_evalue"), 0.05),
    ],
    ids=["override-budget", "base-budget", "max_bp", "min_bp", "overhang", "pair-evalue"],
)
def test_changing_a_cut_setting_re_cuts_every_genome(cfg, tmp_path, path, value):
    """Run 2 would otherwise report 'nothing new', leaving genomes cut at the old budget
    beside any new ones cut at the new."""
    fake, pairs, first = _first_run(cfg)
    first_downloads = sorted(fake.downloaded)
    fake.downloaded = []
    changed = _edited(cfg, path, value)
    run = retrieve_assemblies(109871, changed, fake, pairs=pairs, assays=[BD], run_date="2026-10-05")
    assert run.mode == "full" and "re-cutting every genome" in run.note, (run.mode, run.note)
    assert sorted(fake.downloaded) == first_downloads  # every genome fetched again
    d = tmp_path / "retrieved" / "109871" / "asm"
    assert list(d.glob("*.superseded")), "the old cuts are set aside, not deleted"


def test_unchanged_cut_settings_do_not_re_cut(cfg):
    fake, pairs, _ = _first_run(cfg)
    fake.downloaded = []
    again = retrieve_assemblies(109871, cfg, fake, pairs=pairs, assays=[BD], run_date="2026-10-05")
    assert again.note == "nothing new" and fake.downloaded == []


def test_a_group_cut_before_settings_were_recorded_is_adopted_not_re_cut(cfg, tmp_path):
    """No `cut.json` (an archive from before this existed): its real settings are
    unknowable, and re-downloading every assembly on upgrade would be worse than
    trusting it. It is adopted at the current settings, and a later change then re-cuts."""
    import json

    fake, pairs, _ = _first_run(cfg)
    d = tmp_path / "retrieved" / "109871" / "asm"
    (d / "cut.json").unlink()
    fake.downloaded = []
    dry = retrieve_assemblies(
        109871, cfg, fake, pairs=pairs, assays=[BD], dry_run=True, run_date="2026-10-05"
    )
    assert not (d / "cut.json").exists(), "a dry run writes nothing"
    assert dry.mode != "full" or "re-cutting" not in dry.note
    adopted = retrieve_assemblies(109871, cfg, fake, pairs=pairs, assays=[BD], run_date="2026-10-05")
    assert "re-cutting" not in adopted.note and fake.downloaded == []
    assert json.loads((d / "cut.json").read_text())["max_mismatches"] == 6
    changed = _edited(cfg, ("scoring", "max_mismatches_searched"), 8)
    run = retrieve_assemblies(109871, changed, fake, pairs=pairs, assays=[BD], run_date="2026-10-06")
    assert "re-cutting every genome" in run.note
