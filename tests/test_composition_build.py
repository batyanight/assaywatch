"""`composition_build.build` end to end, on a two-clade archive built here.

ROADMAP "Lineage composition over time" step 12. The fixture is generated rather than
committed: the sequences are random under a fixed seed, so the archive, the calls table
and the deposit years are all written from one description and there is nothing to keep
in step with by hand. Step 5's note put this fixture in `make_fixtures.py`; it lives
beside its only test instead, because `make_fixtures.py` writes the committed
`tests/fixtures/*.fasta` that `test_score.py` reads, and this needs neither.

The shape: ONE assay, two sequence clades about 10% apart in their flanks, with the
lineage MIX swinging between an early and a late deposit year while detection inside each
clade stays put -- the case the whole stage exists to tell apart (step 7).
"""

from __future__ import annotations

import gzip
import json
import random
from datetime import date
from pathlib import Path

import pytest
import yaml

from assaywatch import registry
from assaywatch.composition import DIVERGED, TSV_COLUMNS, UNPLACED, read_summary, write
from assaywatch.composition_build import build
from assaywatch.groups import group_slug
from assaywatch.iupac import reverse_complement
from assaywatch.subcluster import OTHER

ROOT = Path(__file__).resolve().parents[1]
ASSAY = "Encephalitozoon_cuniculi_PTP_Xiao_2001"
CFG = yaml.safe_load((ROOT / "config.yaml").read_text())


def _mutate(seq: str, n: int, rng: random.Random) -> str:
    out = list(seq)
    for _ in range(n):
        i = rng.randrange(len(out))
        out[i] = rng.choice([b for b in "ACGT" if b != out[i]])
    return "".join(out)


def _fixture(tmp_path: Path) -> tuple[Path, Path, Path]:
    """Write a registry, an archive and a calls table. Returns their three paths."""
    rng = random.Random(5)
    assay = registry.load_one(ROOT / "tests" / "fixtures" / "registry" / f"{ASSAY}.yaml")
    fwd = assay.oligos.forward.matching_seq
    rev = reverse_complement(assay.oligos.reverse.matching_seq)
    reg = tmp_path / "registry"
    reg.mkdir()
    (reg / f"{ASSAY}.yaml").write_text(
        (ROOT / "tests" / "fixtures" / "registry" / f"{ASSAY}.yaml").read_text()
    )

    #: Two clades: one flank root each, 10% apart, and members 0.3% from their root.
    base = "".join(rng.choice("ACGT") for _ in range(600))
    roots = [_mutate(base, 60, rng), _mutate(base, 60, rng)]
    #: year -> how many records of clade 0 and clade 1. The mix swings; detection does not.
    plan = {2018: (24, 2), 2025: (3, 23)}
    group = tmp_path / "retrieved" / str(assay.target.taxid) / group_slug(assay.target.query)
    group.mkdir(parents=True)
    calls = [
        (
            "assay_id",
            "record_id",
            "call",
            "amplicon_start",
            "amplicon_end",
            "fwd_site",
            "rev_site",
            "exclusion",
        )
    ]
    meta = []
    fasta = []
    n = 0
    for year, counts in plan.items():
        for clade, count in enumerate(counts):
            for _ in range(count):
                acc = f"AB{n:05d}"
                n += 1
                flank = _mutate(roots[clade], 2, rng)
                interior = "".join(rng.choice("ACGT") for _ in range(120))
                seq = flank[:300] + fwd + interior + rev + flank[300:]
                start = 300
                end = start + len(fwd) + len(interior) + len(rev)
                # clade 0 detects, clade 1 fails: within-clade detection never changes
                call = "detect" if clade == 0 else "fail"
                calls.append(
                    (
                        ASSAY,
                        f"{acc}.1",
                        call,
                        str(start),
                        str(end),
                        f"{start}-{start + len(fwd)}+",
                        f"{end - len(rev)}-{end}-",
                        "",
                    )
                )
                meta.append(
                    (
                        str(n),
                        acc,
                        f"{year}-05-01",
                        f"{year}-05-01",
                        str(len(seq)),
                        f"Fixture organism isolate {acc} clade{clade} PTP gene",
                    )
                )
                fasta.append((f"{acc}.1", seq))
    # one diverged record, which has no site to cluster on, and one with no sequence
    for acc, call, excl in (("ZZ00001", "fail", "diverged"), ("ZZ00002", "detect", "")):
        calls.append((ASSAY, f"{acc}.1", call, "0", "0", "", "", excl))
        meta.append(("9", acc, "2025-05-01", "2025-05-01", "400", "Fixture oddity isolate"))
    with gzip.open(group / "2026-01-01.fasta.gz", "wt") as fh:
        for rid, seq in fasta:
            fh.write(f">{rid}\n{seq}\n")
    with gzip.open(group / "2026-01-01.meta.tsv.gz", "wt") as fh:
        fh.write("uid\taccession\tcreated\tupdated\tlength\ttitle\n")
        for row in meta:
            fh.write("\t".join(row) + "\n")
    calls_path = tmp_path / "2026-01-01" / "calls.tsv"
    calls_path.parent.mkdir()
    calls_path.write_text("\n".join("\t".join(r) for r in calls) + "\n")
    return calls_path, reg, tmp_path / "retrieved"


@pytest.fixture
def run(tmp_path):
    calls_path, reg, retrieved = _fixture(tmp_path)
    return build(
        calls_path,
        reg,
        retrieved,
        CFG,
        run_date="2026-01-01",
        today=date(2026, 1, 1),
    )


def test_the_two_clades_come_back_as_two_lineages(run):
    a = run.assays[ASSAY]
    real = [c for c in a.clusters if c.id >= 0]
    assert len(real) == 2, [(c.id, c.name, c.n_records) for c in a.clusters]
    assert {c.n_records for c in real} == {27, 25}
    assert a.cut == 0.05
    assert a.left_bp > 0 and a.right_bp > 0


def test_every_record_the_graph_counts_is_in_a_cell(run):
    """The invariant of finding 4, end to end: each year's cells sum to that year's
    evaluable and detected records, with nothing silently dropped."""

    a = run.assays[ASSAY]
    by_year: dict[int, list] = {}
    for cell in a.cells:
        by_year.setdefault(cell.year, []).append(cell)
    assert set(by_year) == {2018, 2025}
    # 26 records in 2018 (24 detect + 2 fail), 28 in 2025 (3 + 23 + diverged + no-sequence)
    assert sum(c.records for c in by_year[2018]) == 26
    assert sum(c.detected for c in by_year[2018]) == 24
    assert sum(c.records for c in by_year[2025]) == 28
    assert sum(c.detected for c in by_year[2025]) == 4


def test_a_record_with_no_window_is_counted_and_said_so(run):
    a = run.assays[ASSAY]
    labels = {c.cluster for c in a.cells}
    assert DIVERGED in labels and UNPLACED in labels
    assert "diverged" in a.note and "unplaced" in a.note
    assert {c.name for c in a.clusters if c.id == DIVERGED} == {"diverged (no site)"}


def test_the_mix_moved_the_graph_and_the_panel_says_which(run):
    """Detection inside each clade is fixed, so the observed share falls only because the
    mix swung. The same-mix line holds and the split puts it all in the mix part."""
    a = run.assays[ASSAY]
    assert a.observed[2018] > 0.9 and a.observed[2025] < 0.2
    assert abs(a.same_mix[2018] - a.same_mix[2025]) < 0.1
    assert a.split is not None
    assert a.split.change < -0.7
    assert abs(a.split.mix) > abs(a.split.within) * 5


def test_the_clusters_are_named_from_the_titles_and_carry_their_tokens(run):
    """Both clades are "Fixture organism" in their titles, so the two clusters share a
    modal species and are numbered; what separates them is in the titles' other words,
    which is exactly what the tooltip's tokens are for."""
    a = run.assays[ASSAY]
    named = {c.name for c in a.clusters if c.id >= 0}
    # abbreviated, since "Fixture organism" has the shape of a binomial, and numbered
    # because both clusters share it
    assert named == {"F. organism 1", "F. organism 2"}, named
    tokens = {c.id: set(c.title_tokens) for c in a.clusters if c.id >= 0}
    assert {t for ts in tokens.values() for t in ts} >= {"clade0", "clade1"}
    # and each cluster gets the token of its OWN clade, not the other's
    assert all(len(ts & {"clade0", "clade1"}) == 1 for ts in tokens.values()), tokens


def test_the_tsv_has_the_schema_the_plan_named_and_one_row_per_cell(run, tmp_path):
    tsv, _ = write(run, tmp_path / "out")
    lines = tsv.read_text().splitlines()
    assert lines[0].split("\t") == list(TSV_COLUMNS)
    assert len(lines) - 1 == sum(len(a.cells) for a in run.assays.values())
    rows = [dict(zip(TSV_COLUMNS, line.split("\t"), strict=True)) for line in lines[1:]]
    assert {r["assay_id"] for r in rows} == {ASSAY}
    assert all(r["cut"] == "0.05" for r in rows)
    assert sum(int(r["records"]) for r in rows) == 54
    other = [r for r in rows if int(r["cluster_id"]) in (DIVERGED, UNPLACED, OTHER)]
    assert all(r["cluster_name"] in ("diverged (no site)", "unplaced", "other") for r in other)


def test_the_json_round_trips_as_the_same_objects(run, tmp_path):
    _, js = write(run, tmp_path / "out")
    again = read_summary(js)
    assert again == run
    assert json.loads(js.read_text())["run_date"] == "2026-01-01"


def test_a_stratum_that_is_not_a_species_is_never_new_since_design(run):
    """ "diverged", "unplaced" and "other" say what the clustering could not do. A "new
    since design" badge on one would read as a finding about the taxon."""
    a = run.assays[ASSAY]
    assert all(not c.new_since_design for c in a.clusters if c.id < 0)
