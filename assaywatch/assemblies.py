"""Assembly-level retrieval for bacterial targets: sample genomes per year, keep the loci.

    python -m assaywatch.retrieve registry --email you@example.org   # `asm` groups included

Why this exists. For enteric bacteria, gene-level nuccore deposits (an invA or
ipaH sequence submitted on its own) stop around 2012: since then the same genes
arrive inside whole-genome assemblies, and the nuccore queries exclude WGS
contigs by title because there are millions of them. The drift numbers for
E. coli, Salmonella, Shigella and Yersinia therefore had no recent window at
all. This module fills it from NCBI Datasets instead of Entrez.

What is fetched, per taxon listed under `assemblies.taxa` in config.yaml:

1. The list of GenBank assemblies at the configured levels (complete genome and
   chromosome by default: the locus is never split across contigs, and
   plasmid-borne targets such as ipaH, LT and the O157 hlyA come with the
   assembly), as a compact TSV from the Datasets genome report. The TSV endpoint
   returns at most one page and no continuation token, so release-date windows
   are halved until every window fits in a page.
2. A sample of at most `per_year` assemblies per release year. The order is the
   SHA-1 of the accession, which is arbitrary with respect to strain, lab and
   lineage, and stable: rerunning picks the same genomes, and an incremental
   run only tops up years that are still short.
3. The genomes, downloaded in small batches as zip files and never written to
   disk whole. Each genome is cut down to the windows where one of the group's
   assays could form an amplicon under the screener's own rules (see
   extract_loci), so the archive holds exactly what screening can use and
   stays small.

One record per assembly. The windows of one genome are joined with runs of N
longer than the largest allowed amplicon, so no primer pair can span two
windows, and the screen stage makes one call per genome per assay: the best
amplicon over all copies of the locus, which is the question for a multi-copy
target like ipaH or 16S. The record id is the assembly accession, and the
metadata file gives its release date as `created`, the same meaning `created`
has for nuccore records (the year it reached the public database). The BioSample
collection date is kept in the title: an NCTC strain collected in 1952 and
sequenced in 2018 is a 2018 deposit here, which matches how nuccore records
are dated, but it is not 2018 biology.

Genomes with no candidate amplicon are still listed in the metadata (length 0) so
the sample is traceable, and they count toward their year's quota, so a later
run does not keep sampling past them. A genome missing from the download is
left out instead, so the next run picks it again.
"""

from __future__ import annotations

import csv
import gzip
import hashlib
import io
import json
import math
import os
import time
import zipfile
from collections import Counter
from collections.abc import Callable, Iterator
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
from typing import Any

from assaywatch.chance import composition, pair_evalue
from assaywatch.credentials import scrub
from assaywatch.match import find_sites
from assaywatch.score import max_mismatches_searched

DATASETS = "https://api.ncbi.nlm.nih.gov/datasets/v2"
# (path under DATASETS, query params, Accept header) -> response body
Fetch = Callable[[str, dict[str, Any], str], bytes]

TSV_FIELDS = (
    "accession",
    "assminfo-release-date",
    "assminfo-biosample-collection-date",
    "assminfo-level",
    "organism-name",
    "organism-infraspecific-strain",
)
EARLIEST = date(1990, 1, 1)


class AssemblyError(RuntimeError):
    pass


@dataclass(frozen=True)
class AssemblyMeta:
    accession: str
    release_date: str  # YYYY-MM-DD
    collection_date: str
    level: str
    organism: str
    strain: str

    @property
    def year(self) -> int:
        return int(self.release_date[:4])

    @property
    def order_key(self) -> str:
        """Sampling order: arbitrary with respect to biology, stable across runs.

        A hash, not a random choice, so the same genomes are picked on every run
        and an incremental run only tops up years that are short. Hashing the
        accession without its version keeps a genome in place when NCBI revises
        it. Arbitrary with respect to strain, lab and lineage, which a sort by
        accession or date would not be.
        """
        stem = self.accession.rsplit(".", 1)[0]
        return hashlib.sha1(stem.encode()).hexdigest()


def datasets_transport(api_key: str | None, timeout: int = 300) -> Fetch:
    """The real transport. Datasets allows 5 requests/s without a key, 10 with one."""
    import requests

    min_interval = 0.11 if api_key else 0.21
    state = {"last": 0.0}

    def call(path: str, params: dict[str, Any], accept: str) -> bytes:
        headers = {"Accept": accept}
        if api_key:
            headers["api-key"] = api_key
        for attempt in range(5):
            wait = min_interval - (time.monotonic() - state["last"])
            if wait > 0:
                time.sleep(wait)
            state["last"] = time.monotonic()
            try:
                resp = requests.get(f"{DATASETS}/{path}", params=params, headers=headers, timeout=timeout)
                body = resp.content
            except requests.RequestException as e:
                if attempt == 4:
                    raise AssemblyError(f"{path}: {scrub(e)}") from e
                time.sleep(2**attempt)
                continue
            if resp.status_code in (429, 500, 502, 503, 504):
                time.sleep(2**attempt)
                continue
            if resp.status_code >= 400:
                raise AssemblyError(
                    f"{path}: HTTP {resp.status_code} {scrub(body.decode('utf-8', 'replace'))[:200]!r}"
                )
            return body
        raise AssemblyError(f"{path} failed after 5 attempts")

    return call


# --------------------------------------------------------------------------
# Listing
# --------------------------------------------------------------------------


def _report_page(
    fetch: Fetch, taxid: int, levels: list[str], lo: date, hi: date, page: int
) -> list[AssemblyMeta]:
    params = {
        "filters.assembly_source": "genbank",
        "filters.assembly_level": levels,
        "filters.exclude_atypical": "true",
        "filters.first_release_date": lo.isoformat(),
        "filters.last_release_date": hi.isoformat(),
        "page_size": page,
        "table_fields": list(TSV_FIELDS),
    }
    body = fetch(f"genome/taxon/{taxid}/dataset_report", params, "text/tab-separated-values")
    rows = list(csv.reader(io.StringIO(body.decode()), delimiter="\t"))
    out = []
    for r in rows[1:]:  # header row first
        if len(r) < 4 or not r[0]:
            continue
        r = r + [""] * (len(TSV_FIELDS) - len(r))
        out.append(AssemblyMeta(r[0], r[1][:10], r[2], r[3], r[4], r[5]))
    return out


def list_assemblies(
    fetch: Fetch, taxid: int, levels: list[str], since: date | None, until: date, page: int = 1000
) -> list[AssemblyMeta]:
    """Every assembly released in [since, until], splitting date windows that fill a page.

    The TSV endpoint returns at most one page and no continuation token, so a
    window that comes back full may be hiding more. There is no way to ask for
    "the next page", so instead a full window is bisected by date and both halves
    re-requested, until every window comes back short of the page size — at which
    point it is known to be complete. A window that fills a page and cannot be
    split any further (one single day) is an error rather than silent truncation.
    """
    out: dict[str, AssemblyMeta] = {}
    stack = [(since or EARLIEST, until)]
    while stack:
        lo, hi = stack.pop()
        rows = _report_page(fetch, taxid, levels, lo, hi, page)
        if len(rows) >= page:
            if lo >= hi:
                raise AssemblyError(f"taxid {taxid}: more than {page} assemblies released on {lo}")
            mid = lo + (hi - lo) // 2
            stack += [(lo, mid), (mid + timedelta(days=1), hi)]
            continue
        for m in rows:
            out[m.accession] = m
    return sorted(out.values(), key=lambda m: (m.release_date, m.accession))


def sample_per_year(
    assemblies: list[AssemblyMeta], per_year: int, taken: Counter, today: date | None = None
) -> list[AssemblyMeta]:
    """Up to `per_year` per release year, minus what earlier runs already took.

    The year still in progress gets a quota in proportion to how much of it has
    passed. Otherwise a weekly run in January would fill the whole year's quota
    from January releases, and the most recent window would be the least
    representative part of the sample.
    """
    today = today or date.today()
    elapsed = (today.timetuple().tm_yday) / (366 if today.year % 4 == 0 else 365)
    by_year: dict[int, list[AssemblyMeta]] = {}
    for m in assemblies:
        by_year.setdefault(m.year, []).append(m)
    picked = []
    for year, ms in sorted(by_year.items()):
        quota = per_year if year < today.year else max(1, math.ceil(per_year * elapsed))
        room = max(0, quota - taken.get(year, 0))
        picked += sorted(ms, key=lambda m: m.order_key)[:room]
    return picked


# --------------------------------------------------------------------------
# Download and extraction
# --------------------------------------------------------------------------


def _parse_fna(text: str) -> list[tuple[str, str]]:
    contigs, rid, chunks = [], None, []
    for line in text.splitlines():
        if line.startswith(">"):
            if rid is not None:
                contigs.append((rid, "".join(chunks)))
            rid, chunks = line[1:].split(None, 1)[0], []
        elif line:
            chunks.append(line.strip())
    if rid is not None:
        contigs.append((rid, "".join(chunks)))
    return contigs


def iter_genomes(fetch: Fetch, accessions: list[str], batch: int = 10) -> Iterator[tuple[str, list]]:
    """(accession, [(contig id, sequence)]) for each accession; missing ones yield an empty list."""
    for i in range(0, len(accessions), batch):
        chunk = accessions[i : i + batch]
        body = fetch(
            f"genome/accession/{','.join(chunk)}/download",
            {"include_annotation_type": "GENOME_FASTA"},
            "application/zip",
        )
        found: dict[str, list] = {}
        with zipfile.ZipFile(io.BytesIO(body)) as zf:
            for name in zf.namelist():
                if not name.endswith(".fna"):
                    continue
                # Keyed without the version: NCBI may serve GCA_x.2 for a request
                # for GCA_x.1, and that is still the genome that was asked for.
                acc = name.split("/")[-2].rsplit(".", 1)[0]
                found.setdefault(acc, []).extend(_parse_fna(zf.read(name).decode()))
        for acc in chunk:
            yield acc, found.get(acc.rsplit(".", 1)[0], [])


def extract_loci(
    contigs: list[tuple[str, str]], pairs: list[tuple[str, str]], cfg: dict[str, Any]
) -> tuple[str, int]:
    """The genome cut to its candidate amplicons, joined by N spacers; (sequence, n windows).

    `pairs` are (forward, reverse) primer sequences, one per assay. A window is
    kept wherever the screener could build an amplicon: forward and reverse
    sites facing each other on opposite strands (either orientation), within
    the configured size range, each within the screener's mismatch budget. The
    window runs `record_min_overhang_bp` past both ends, so the probe search and
    every scoring rule see exactly the bases they would see in the whole genome.

    Single oligo hits are not enough to keep a window: a short MGB probe, or a
    primer at a six-mismatch budget, has chance sites every few kilobases of
    any genome. Even facing pairs are common by chance in a genome (several
    hundred per Yersinia chromosome at six mismatches each), so a pair is kept
    only if its E-value (chance.py) is at most `assemblies.max_pair_evalue`:
    distinguishable from chance in a record of that length. The cost is that a
    real site degraded to five or six mismatches in both primers is dropped,
    but in a genome such a site cannot be told apart from noise anyway.

    The spacer is longer than the largest amplicon, so nothing pairs across two
    windows.
    """
    amp = cfg["amplicon"]
    lo_bp, hi_bp = int(amp["min_bp"]), int(amp["max_bp"])
    pad = int(amp.get("record_min_overhang_bp", 0))
    # The pre-cut sees only oligo pairs, with no chemistry, so it searches at the
    # LARGEST budget any chemistry may use and lets screening apply each assay's own
    # (see score.max_mismatches_searched).
    max_mm = max_mismatches_searched(cfg)
    # Chance pairs are everywhere in a genome (chance.py); a window is kept only
    # around a pair that is distinguishable from chance in a record this long.
    max_e = float((cfg.get("assemblies") or {}).get("max_pair_evalue", 0.01))
    longest = max((len(o) for pair in pairs for o in pair), default=0)
    spacer = "N" * (hi_bp + longest + 1)
    pieces = []
    for _, seq in contigs:
        seq = seq.upper()
        comp = composition(seq)
        sites: dict[str, dict[str, list]] = {}

        def on(oligo: str, strand: str, seq=seq, sites=sites) -> list:
            # find_sites scans both strands at once; do it once per oligo.
            if oligo not in sites:
                found = find_sites(oligo, seq, max_mm)
                sites[oligo] = {st: [x for x in found if x.strand == st] for st in "+-"}
            return sites[oligo][strand]

        spans = []
        for fwd, rev in pairs:
            # Both orientations, as in score.screen_record: the locus may sit on either strand.
            for f_strand, r_strand in (("+", "-"), ("-", "+")):
                r_sites = on(rev, r_strand)
                if not r_sites:
                    continue
                for f in on(fwd, f_strand):
                    for r in r_sites:
                        lo, hi = (f.start, r.end) if f_strand == "+" else (r.start, f.end)
                        facing = r.start > f.start if f_strand == "+" else f.start > r.start
                        if not (facing and lo_bp <= hi - lo <= hi_bp):
                            continue
                        e = pair_evalue(
                            fwd,
                            rev,
                            f.n_mismatches + f.n_ambiguous,
                            r.n_mismatches + r.n_ambiguous,
                            len(seq),
                            cfg,
                            comp,
                        )
                        if e <= max_e:
                            spans.append((max(0, lo - pad), min(len(seq), hi + pad)))
        spans.sort()
        merged: list[list[int]] = []
        for lo, hi in spans:
            if merged and lo <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], hi)
            else:
                merged.append([lo, hi])
        pieces += [seq[lo:hi] for lo, hi in merged]
    return spacer.join(pieces), len(pieces)


# --------------------------------------------------------------------------
# The stage
# --------------------------------------------------------------------------


def cut_parameters(cfg: dict[str, Any]) -> dict[str, Any]:
    """Every setting `extract_loci` reads besides the primer pairs.

    A genome archive is the genome CUT to the windows these settings keep, so changing
    any of them changes what an archive holds. `retrieve_assemblies` records them beside
    the archives and re-cuts when they differ, and the Snakefile hashes them into the
    retrieve rule's params so that changing one reruns retrieval at all: before this,
    only a change to the primer pairs did either, so raising `max_mismatches_searched`
    left old genomes cut at the old budget and cut new ones at the new, in one group.
    """
    amp = cfg["amplicon"]
    return {
        "max_mismatches": max_mismatches_searched(cfg),
        "min_bp": int(amp["min_bp"]),
        "max_bp": int(amp["max_bp"]),
        "overhang_bp": int(amp.get("record_min_overhang_bp", 0)),
        "max_pair_evalue": float((cfg.get("assemblies") or {}).get("max_pair_evalue", 0.01)),
    }


def taken_per_year(out_dir: Path) -> tuple[Counter, set[str]]:
    """Per-year counts and accessions already sampled by earlier runs of this group."""
    years: Counter = Counter()
    seen: set[str] = set()
    for meta in sorted(out_dir.glob("*.meta.tsv.gz")):
        with gzip.open(meta, "rt") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                if row["accession"] in seen:
                    continue
                seen.add(row["accession"])
                if row["created"][:4].isdigit():
                    years[int(row["created"][:4])] += 1
    return years, seen


def retrieve_assemblies(
    taxid: int,
    cfg: dict[str, Any],
    fetch: Fetch,
    *,
    pairs: list[tuple[str, str]],
    taxon_name: str | None = None,
    assays: list[str] | None = None,
    full: bool = False,
    dry_run: bool = False,
    run_date: str | None = None,
):
    """Fetch one `asm` group. Returns a TaxonRun; writes nothing when dry_run."""
    from assaywatch.retrieve import TaxonRun, archive_stem, last_run_date, load_manifest

    a = cfg.get("assemblies") or {}
    levels = list(a.get("levels") or ["complete_genome", "chromosome"])
    per_year = int(a.get("per_year", 20))
    run_date = run_date or date.today().isoformat()
    out_dir = Path(cfg.get("retrieved_dir", "data/retrieved")) / str(taxid) / "asm"

    since_text = None if full else last_run_date(load_manifest(cfg), taxid, "asm")
    # The archives hold only the windows the assays of the day could amplify.
    # When the taxon's primer pairs change (an assay added or edited), the old
    # cuts may lack the new locus, so every genome is cut again.
    signature = hashlib.sha1(repr(sorted(pairs)).encode()).hexdigest()[:12]
    sig_file = out_dir / "pairs.sha1"
    # ...and when the settings the cut depends on change (see `cut_parameters`). A group
    # cut before these were recorded has no `cut.json`; it is ADOPTED at the current
    # settings rather than re-cut, because its true settings are unknowable and a
    # mass re-download of every assembly on upgrade would be the worse error.
    cut = cut_parameters(cfg)
    cut_file = out_dir / "cut.json"
    recut = sig_file.exists() and sig_file.read_text().strip() != signature
    if cut_file.exists():
        recut = recut or json.loads(cut_file.read_text()) != cut
    elif sig_file.exists() and not dry_run:
        cut_file.write_text(json.dumps(cut, sort_keys=True) + "\n")
    taken, seen = (Counter(), set()) if full or recut else taken_per_year(out_dir)

    # The whole history is listed every run, not just releases since the last
    # one: the listing is cheap (about twenty requests for E. coli), it catches
    # assemblies whose release date NCBI back-fills, and it is what lets a genome
    # that failed to download be picked again. `seen` keeps it incremental.
    listed = list_assemblies(fetch, taxid, levels, None, date.fromisoformat(run_date))
    listed = [m for m in listed if m.accession not in seen]
    picked = sample_per_year(listed, per_year, taken, date.fromisoformat(run_date))

    run = TaxonRun(
        taxid=taxid,
        taxon_name=taxon_name,
        run_date=run_date,
        query=f"Datasets genome/taxon/{taxid}: GenBank {'+'.join(levels)}, {per_year} per release year",
        mode="incremental" if seen else "full",
        since=since_text,
        n_available=len(listed),
        n_fetched=0,
        assays=assays or [],
        group="asm",
        assay_query=None,
    )
    if recut:
        run.mode = "full"
        run.note = "primer pairs or cut settings changed since the last cut: re-cutting every genome"
    if not picked or dry_run:
        years = Counter(m.year for m in picked)
        span = f"{min(years)}-{max(years)}" if years else "-"
        run.note = "nothing new" if not picked else f"dry run: would fetch {len(picked)} ({span})"
        return run

    out_dir.mkdir(parents=True, exist_ok=True)
    stem = archive_stem(out_dir, run_date)
    fasta_path, meta_path = out_dir / f"{stem}.fasta.gz", out_dir / f"{stem}.meta.tsv.gz"
    fasta_tmp, meta_tmp = out_dir / f".{stem}.fasta.gz.part", out_dir / f".{stem}.meta.tsv.gz.part"
    by_acc = {m.accession: m for m in picked}
    n_with_locus = n_missing = 0
    try:
        with gzip.open(fasta_tmp, "wt") as fh, gzip.open(meta_tmp, "wt") as mh:
            mh.write("uid\taccession\tcreated\tupdated\tlength\ttitle\n")
            for acc, contigs in iter_genomes(fetch, list(by_acc), int(a.get("batch", 10))):
                m = by_acc[acc]
                if not contigs:
                    # Not in the download. Left out of the metadata, so it does not
                    # use up its year's quota and the next run picks it again.
                    n_missing += 1
                    continue
                seq, n_win = extract_loci(contigs, pairs, cfg)
                if seq:
                    n_with_locus += 1
                    fh.write(f">{acc} {m.organism} {m.strain} loci={n_win}\n")
                    for i in range(0, len(seq), 80):
                        fh.write(seq[i : i + 80] + "\n")
                collected = m.collection_date or "missing"
                title = f"{m.organism} {m.strain}; {m.level}; {n_win} loci; collected {collected}"
                mh.write(f"{acc}\t{acc}\t{m.release_date}\t{m.release_date}\t{len(seq)}\t{title}\n")
    except BaseException:
        fasta_tmp.unlink(missing_ok=True)
        meta_tmp.unlink(missing_ok=True)
        raise
    if n_missing == len(picked):
        # Nothing came back: write no archive (an empty one would be screened and
        # recorded as a run), and let the next run try again.
        fasta_tmp.unlink(missing_ok=True)
        meta_tmp.unlink(missing_ok=True)
        raise AssemblyError(f"taxid {taxid}: none of {len(picked)} requested genomes were in the download")
    if recut:
        # The old cuts are superseded; keep them out of screening, not deleted.
        for old in out_dir.glob("*.fasta.gz"):
            old.rename(old.with_name(old.name + ".superseded"))
        for old in out_dir.glob("*.meta.tsv.gz"):
            old.rename(old.with_name(old.name + ".superseded"))
        stem = archive_stem(out_dir, run_date)
        fasta_path, meta_path = out_dir / f"{stem}.fasta.gz", out_dir / f"{stem}.meta.tsv.gz"
    os.replace(meta_tmp, meta_path)
    os.replace(fasta_tmp, fasta_path)
    sig_file.write_text(signature + "\n")
    cut_file.write_text(json.dumps(cut, sort_keys=True) + "\n")
    run.n_fetched = len(picked) - n_missing
    run.fasta, run.metadata = str(fasta_path), str(meta_path)
    # Keep the re-cut message: it was overwritten here, so the run record said only how
    # many genomes carried a locus and never that every genome had been cut again.
    run.note = (
        f"{run.note}; " if recut else ""
    ) + f"{n_with_locus} of {run.n_fetched} genomes carry a candidate amplicon"
    if n_missing:
        run.note += f"; {n_missing} not in the download, retried next run"
    return run
