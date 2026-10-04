"""Fetch nucleotide records for a target taxon from NCBI and archive them.

    python -m assaywatch.retrieve registry --email you@example.org
    python -m assaywatch.retrieve registry/CHYTRID_Bd_*.yaml --email ... --dry-run

One retrieval group at a time. A group is a (taxid, query) pair: assays with
the same target taxon and the same `target.query` share one archive. Without a
query the group is the whole taxon, which is right for Bd (nine thousand
records) and absurd for E. coli (sixteen million, nearly all whole-genome
shotgun contigs). A gene-targeted query such as `invA[Gene]` keeps the
archive to the records that can carry the amplicon, which is also the only
set the drift statistic should be computed over: a contig that does not cover
the locus is not evidence about the assay.

Three E-utilities calls per group, in this order, because each one answers a
question the next one needs:

1. `esearch` on nuccore for `txid<taxid>[Organism:exp]`, with the configured
   length filter and, on an incremental run, a date range. Returns a count and
   a WebEnv/query_key handle, so the IDs never have to be moved around.
2. `esummary` over that handle, in pages. This is where the deposit dates come
   from. The drift question is "has coverage fallen *since* the assay was
   designed", so every record needs a year; FASTA headers do not carry one and
   full GenBank flatfiles are an order of magnitude more data to move. The
   summary gives accession, creation date, update date, length and title.
3. `efetch` over the same handle in FASTA, in pages, written straight to a
   gzip file without being held in memory.

Incremental by default. The manifest records the date of the last successful
run per taxon, and the next run asks only for records added or modified since
(`datetype=mdat`), which is the field that changes when a submitter revises a
sequence. Revised records matter: a correction can turn a mismatch into a
match. Pass `--full` to ignore the manifest and re-fetch everything, which is
what you want after changing the length filter or the query suffix.

Nothing is deduplicated across runs at fetch time. Each run's archive is a
complete, self-describing snapshot of what that query returned on that day,
which is what makes a past report reproducible; the scoring stage is
responsible for taking the newest version of each accession.

Politeness and rate limits are not optional: NCBI allows 3 requests per second
without an API key and 10 with one, and asks for a contact address. `--email`
is required, `NCBI_API_KEY` is read from the environment if set, and the
client sleeps between calls either way.

The HTTP transport is injectable (`transport=`) so the whole stage can be
tested against canned responses without touching the network; see
tests/test_retrieve.py.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
import sys
import time
import xml.etree.ElementTree as ET
from collections.abc import Callable
from dataclasses import asdict, dataclass, field
from datetime import date
from pathlib import Path
from typing import Any

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
Transport = Callable[[str, dict[str, Any]], str]


class RetrievalError(RuntimeError):
    pass


class TooManyRecords(RetrievalError):
    """The taxon is larger than the configured cap and has not been opted in."""


class HistoryExpired(RetrievalError):
    """NCBI's history server dropped the WebEnv between calls; re-search and retry."""


@dataclass
class RecordMeta:
    """What the scorer needs about a record beyond its sequence."""

    uid: str
    accession: str
    created: str  # YYYY-MM-DD; first appearance in GenBank
    updated: str  # YYYY-MM-DD; last revision
    length: int
    title: str

    @property
    def year(self) -> int | None:
        return int(self.created[:4]) if self.created[:4].isdigit() else None


@dataclass
class TaxonRun:
    """One retrieval group fetched on one day. Serialised into the manifest."""

    taxid: int
    taxon_name: str | None
    run_date: str
    query: str
    mode: str  # full | incremental
    since: str | None
    n_available: int
    n_fetched: int
    fasta: str | None = None
    metadata: str | None = None
    assays: list[str] = field(default_factory=list)
    note: str = ""
    group: str = "all"  # directory under the taxid; `all` or a hash of assay_query
    assay_query: str | None = None


# --------------------------------------------------------------------------
# HTTP
# --------------------------------------------------------------------------


def http_transport(email: str, api_key: str | None, timeout: int = 60) -> Transport:
    """The real transport. Imports requests lazily so tests need no network stack."""
    import requests

    min_interval = 0.11 if api_key else 0.34  # 10/s with a key, 3/s without
    state = {"last": 0.0}

    def call(endpoint: str, params: dict[str, Any]) -> str:
        params = {**params, "email": email, "tool": "assaywatch"}
        if api_key:
            params["api_key"] = api_key
        for attempt in range(5):
            wait = min_interval - (time.monotonic() - state["last"])
            if wait > 0:
                time.sleep(wait)
            state["last"] = time.monotonic()
            try:
                resp = requests.post(f"{EUTILS}/{endpoint}.fcgi", data=params, timeout=timeout)
                # Reading the body is where a large efetch page actually fails
                # ("Response ended prematurely"); it has to be inside the try.
                body = resp.text
            except requests.RequestException as e:
                if attempt == 4:
                    raise RetrievalError(f"{endpoint}: {e}") from e
                time.sleep(2**attempt)
                continue
            # 429 and 5xx are transient; everything else is a bug in the query
            # or a blocked network, and retrying will not help.
            if resp.status_code in (429, 500, 502, 503, 504):
                time.sleep(2**attempt)
                continue
            if resp.status_code == 400 and "history" in body.lower():
                raise HistoryExpired(f"{endpoint}: {body[:200]}")
            if resp.status_code >= 400:
                raise RetrievalError(f"{endpoint}: HTTP {resp.status_code} {body[:200]}")
            return body
        raise RetrievalError(f"{endpoint} failed after 5 attempts")

    return call


# --------------------------------------------------------------------------
# Query construction
# --------------------------------------------------------------------------


def build_query(taxid: int, cfg: dict[str, Any], assay_query: str | None = None) -> str:
    """`txid...[Organism:exp]` plus the configured filters plus the assay's own term.

    `Organism:exp` expands down the taxonomy, so a genus-level taxid picks up
    every species under it. That is what a pan-genus assay should be screened
    against, and it is why the registry stores the taxid rather than a name.
    """
    r = cfg.get("retrieve", {})
    parts = [f"txid{taxid}[Organism:exp]"]
    lo, hi = r.get("min_length"), r.get("max_length")
    if lo or hi:
        parts.append(f"{lo or 1}:{hi or 100000000}[SLEN]")
    if r.get("query_suffix"):
        parts.append(f"({r['query_suffix']})")
    if assay_query:
        parts.append(f"({assay_query.strip()})")
    return " AND ".join(parts)


def group_slug(assay_query: str | None) -> str:
    """Directory name for a retrieval group under its taxid: `all`, or a query hash."""
    if not assay_query:
        return "all"
    return "q" + hashlib.sha1(assay_query.strip().encode()).hexdigest()[:10]


# --------------------------------------------------------------------------
# E-utilities calls
# --------------------------------------------------------------------------


def esearch(transport: Transport, query: str, since: str | None, datetype: str = "mdat") -> dict[str, Any]:
    params: dict[str, Any] = {
        "db": "nuccore",
        "term": query,
        "usehistory": "y",
        "retmax": 0,
        "retmode": "xml",
    }
    if since:
        params |= {"datetype": datetype, "mindate": since, "maxdate": "3000/01/01"}
    root = ET.fromstring(transport("esearch", params))
    err = root.findtext("ERROR")
    if err:
        raise RetrievalError(f"esearch: {err}")
    return {
        "count": int(root.findtext("Count") or 0),
        "webenv": root.findtext("WebEnv"),
        "query_key": root.findtext("QueryKey"),
    }


def _text(node: ET.Element, name: str) -> str:
    """Read an esummary <Item Name="..."> value."""
    el = node.find(f"./Item[@Name='{name}']")
    return (el.text or "").strip() if el is not None else ""


def esummary(transport: Transport, handle: dict[str, Any], page: int, retmax: int) -> list[RecordMeta]:
    xml = transport(
        "esummary",
        {
            "db": "nuccore",
            "WebEnv": handle["webenv"],
            "query_key": handle["query_key"],
            "retstart": page * retmax,
            "retmax": retmax,
            "retmode": "xml",
            "version": "1.0",
        },
    )
    out = []
    for doc in ET.fromstring(xml).findall("DocSum"):
        created = _text(doc, "CreateDate").replace("/", "-")[:10]
        updated = _text(doc, "UpdateDate").replace("/", "-")[:10]
        length = _text(doc, "Length")
        out.append(
            RecordMeta(
                uid=doc.findtext("Id") or "",
                accession=_text(doc, "Caption") or _text(doc, "AccessionVersion"),
                created=created,
                updated=updated,
                length=int(length) if length.isdigit() else 0,
                title=_text(doc, "Title"),
            )
        )
    return out


def efetch_fasta(transport: Transport, handle: dict[str, Any], page: int, retmax: int) -> str:
    return transport(
        "efetch",
        {
            "db": "nuccore",
            "WebEnv": handle["webenv"],
            "query_key": handle["query_key"],
            "retstart": page * retmax,
            "retmax": retmax,
            "rettype": "fasta",
            "retmode": "text",
        },
    )


# --------------------------------------------------------------------------
# Manifest
# --------------------------------------------------------------------------


def manifest_path(cfg: dict[str, Any]) -> Path:
    return Path(cfg.get("retrieved_dir", "data/retrieved")) / "manifest.json"


def load_manifest(cfg: dict[str, Any]) -> dict[str, Any]:
    p = manifest_path(cfg)
    return json.loads(p.read_text()) if p.exists() else {"runs": []}


def last_run_date(manifest: dict[str, Any], taxid: int, group: str = "all") -> str | None:
    """The most recent successful run for this group, as YYYY/MM/DD for Entrez."""
    dates = [
        r["run_date"]
        for r in manifest["runs"]
        if r["taxid"] == taxid and r.get("group", "all") == group and r["n_fetched"] >= 0
    ]
    return max(dates).replace("-", "/") if dates else None


def write_manifest(cfg: dict[str, Any], manifest: dict[str, Any]) -> None:
    """Replace the manifest atomically, so an interruption can never leave half a file."""
    p = manifest_path(cfg)
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_name(f".{p.name}.part")
    tmp.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    os.replace(tmp, p)


def record_run(cfg: dict[str, Any], run: TaxonRun) -> None:
    """Append one run to the manifest.

    The manifest is long-lived state, not the output of any one pipeline
    step. A workflow manager must never be told it owns this file: Snakemake
    deletes a rule's outputs before running it, which is how the first two
    pipeline runs each erased the fetch history and refetched everything.
    """
    manifest = load_manifest(cfg)
    manifest["runs"].append(asdict(run))
    write_manifest(cfg, manifest)


# --------------------------------------------------------------------------
# The stage
# --------------------------------------------------------------------------


def targets_from_registry(
    paths: list[Path], cfg: dict[str, Any] | None = None
) -> dict[tuple[int, str], dict[str, Any]]:
    """{(taxid, group): {name, query, assays, pairs}} for every registry file that names a taxid.

    Assays sharing a taxid and a `target.query` land in one group and one
    archive; the screen stage then scores each assay only against its own
    group, so a gene-targeted archive is never polluted with another gene's
    `no_amplicon` rows.

    Taxids listed under `assemblies.taxa` in the config also get an `asm`
    group holding every assay on that taxid, whatever its query: those
    archives are cut from whole genomes around the assays' candidate amplicons
    (see assemblies.py), so they only contain loci the group's assays target.
    `pairs` lists each assay's (forward, reverse) primers for that cut.
    """
    from assaywatch.validate import iter_files, load_assay

    asm_taxa = set(((cfg or {}).get("assemblies") or {}).get("taxa") or [])
    out: dict[tuple[int, str], dict[str, Any]] = {}
    for target in paths:
        for path in iter_files(target):
            assay = load_assay(path)
            if assay.status.value == "deprecated" or assay.target.taxid is None:
                continue
            pair = (assay.oligos.forward.matching_seq, assay.oligos.reverse.matching_seq)
            keys = [(assay.target.taxid, group_slug(assay.target.query), assay.target.query)]
            if assay.target.taxid in asm_taxa:
                keys.append((assay.target.taxid, "asm", None))
            for taxid, group, query in keys:
                slot = out.setdefault(
                    (taxid, group),
                    {"name": assay.target.taxon_name, "query": query, "assays": [], "pairs": []},
                )
                slot["assays"].append(assay.id)
                if pair not in slot["pairs"]:
                    slot["pairs"].append(pair)
    return out


def archive_stem(out_dir: Path, run_date: str) -> str:
    """`2026-10-04`, or `2026-10-04_2`, `_3`... if that name is already taken."""
    stem, n = run_date, 1
    while (out_dir / f"{stem}.fasta.gz").exists():
        n += 1
        stem = f"{run_date}_{n}"
    return stem


def retrieve_taxon(
    taxid: int,
    cfg: dict[str, Any],
    transport: Transport,
    *,
    taxon_name: str | None = None,
    assays: list[str] | None = None,
    assay_query: str | None = None,
    full: bool = False,
    dry_run: bool = False,
    run_date: str | None = None,
) -> TaxonRun:
    """Fetch one retrieval group. Returns the run record; writes nothing when dry_run."""
    r = cfg.get("retrieve", {})
    run_date = run_date or date.today().isoformat()
    query = build_query(taxid, cfg, assay_query)
    group = group_slug(assay_query)

    manifest = load_manifest(cfg)
    since = None if full else last_run_date(manifest, taxid, group)
    mode = "incremental" if since else "full"

    handle = esearch(transport, query, since)
    run = TaxonRun(
        taxid=taxid,
        taxon_name=taxon_name,
        run_date=run_date,
        query=query,
        mode=mode,
        since=since,
        n_available=handle["count"],
        n_fetched=0,
        assays=assays or [],
        group=group,
        assay_query=assay_query,
    )

    cap = r.get("max_records_per_taxon")
    allowed = set(r.get("large_taxa_allowed") or [])
    if cap and handle["count"] > cap and taxid not in allowed:
        raise TooManyRecords(
            f"taxid {taxid} ({taxon_name}) group {group} has {handle['count']} records, over the cap "
            f"of {cap}. Add {taxid} to retrieve.large_taxa_allowed in config.yaml to fetch it anyway, "
            "or narrow the assays' target.query."
        )
    if handle["count"] == 0 or dry_run:
        run.note = "nothing new" if handle["count"] == 0 else "dry run"
        return run

    out_dir = Path(cfg.get("retrieved_dir", "data/retrieved")) / str(taxid) / group
    out_dir.mkdir(parents=True, exist_ok=True)
    # Never overwrite an archive. A second run on the same day is incremental
    # and small; writing it over the morning's full fetch would silently
    # replace thousands of records with a handful.
    stem = archive_stem(out_dir, run_date)
    fasta_path = out_dir / f"{stem}.fasta.gz"
    meta_path = out_dir / f"{stem}.meta.tsv.gz"
    # Write under temporary names and rename at the end, so an interrupted
    # fetch can never leave a file that looks like a finished archive.
    fasta_tmp = out_dir / f".{stem}.fasta.gz.part"
    meta_tmp = out_dir / f".{stem}.meta.tsv.gz.part"

    retmax = int(r.get("page_size", 500))
    n_pages = -(-handle["count"] // retmax)

    def refreshed() -> dict[str, Any]:
        """A new history handle for the same query, after NCBI dropped the old one."""
        fresh = esearch(transport, query, since)
        if fresh["count"] != handle["count"]:
            raise RetrievalError(
                f"record count changed from {handle['count']} to {fresh['count']} while fetching; rerun"
            )
        return fresh

    def with_refresh(call, *args):
        nonlocal handle
        try:
            return call(transport, handle, *args)
        except HistoryExpired:
            handle = refreshed()
            return call(transport, handle, *args)

    # Pass 1: metadata. Also measures how big the records are, which decides
    # the efetch page size: 500 ITS fragments are 200 kB, 500 poxvirus
    # genomes are 100 MB, and the second is what drops connections.
    total_bases = 0
    with gzip.open(meta_tmp, "wt") as mh:
        mh.write("uid\taccession\tcreated\tupdated\tlength\ttitle\n")
        for page in range(n_pages):
            for m in with_refresh(esummary, page, retmax):
                total_bases += m.length
                mh.write(f"{m.uid}\t{m.accession}\t{m.created}\t{m.updated}\t{m.length}\t{m.title}\n")

    target_bytes = int(r.get("page_target_bytes", 20_000_000))
    mean_len = max(1, total_bases // max(1, handle["count"]))
    fetch_retmax = min(retmax, max(10, target_bytes // mean_len))  # never above page_size
    fetch_pages = -(-handle["count"] // fetch_retmax)

    n = 0
    with gzip.open(fasta_tmp, "wt") as fh:
        for page in range(fetch_pages):
            chunk = with_refresh(efetch_fasta, page, fetch_retmax)
            n += chunk.count(">")
            fh.write(chunk if chunk.endswith("\n") else chunk + "\n")

    os.replace(meta_tmp, meta_path)
    os.replace(fasta_tmp, fasta_path)
    run.note = "" if fetch_retmax == retmax else f"pages of {fetch_retmax} (mean record {mean_len:,} nt)"

    run.n_fetched = n
    run.fasta = str(fasta_path)
    run.metadata = str(meta_path)
    return run


def main(argv: list[str] | None = None) -> int:
    from assaywatch.score import load_config

    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="+", type=Path, help="registry file(s) or directory")
    ap.add_argument("--email", required=True, help="contact address; NCBI requires one")
    ap.add_argument("--config", type=Path, default=None)
    ap.add_argument("--full", action="store_true", help="ignore the manifest and re-fetch everything")
    ap.add_argument("--dry-run", action="store_true", help="report counts, write nothing")
    ap.add_argument("--taxid", type=int, action="append", help="limit to these taxids")
    ap.add_argument(
        "--run-record",
        type=Path,
        default=None,
        help="write a JSON summary of this run here; the pipeline uses it as the retrieve step's output",
    )
    ap.add_argument(
        "--strict",
        action="store_true",
        help="exit non-zero when a group is skipped for size; by default only transport errors fail the run",
    )
    args = ap.parse_args(argv)

    cfg = load_config(args.config)
    transport = http_transport(args.email, os.environ.get("NCBI_API_KEY"))
    fetch = None  # Datasets transport, created on first `asm` group
    targets = targets_from_registry(args.paths, cfg)
    if args.taxid:
        targets = {k: v for k, v in targets.items() if k[0] in args.taxid}

    n_assays = sum(len(v["assays"]) for v in targets.values())
    print(f"{len(targets)} retrieval groups from {n_assays} assays", file=sys.stderr)
    skipped, errors, done = [], [], []
    for (taxid, group), info in sorted(targets.items()):
        try:
            if group == "asm":
                from assaywatch.assemblies import AssemblyError, datasets_transport, retrieve_assemblies

                fetch = fetch or datasets_transport(os.environ.get("NCBI_API_KEY"))
                try:
                    run = retrieve_assemblies(
                        taxid,
                        cfg,
                        fetch,
                        pairs=info["pairs"],
                        taxon_name=info["name"],
                        assays=info["assays"],
                        full=args.full,
                        dry_run=args.dry_run,
                    )
                except AssemblyError as e:
                    raise RetrievalError(str(e)) from e
            else:
                run = retrieve_taxon(
                    taxid,
                    cfg,
                    transport,
                    taxon_name=info["name"],
                    assays=info["assays"],
                    assay_query=info["query"],
                    full=args.full,
                    dry_run=args.dry_run,
                )
        except TooManyRecords as e:
            # Over the cap is a decision for the config, not a failure of the
            # run: the other groups are still fetched and the run still counts.
            print(f"SKIP  {taxid}/{group}: {e}", file=sys.stderr)
            skipped.append((taxid, group))
            continue
        except RetrievalError as e:
            print(f"ERROR {taxid}/{group}: {e}", file=sys.stderr)
            errors.append((taxid, group))
            continue
        if not args.dry_run:
            record_run(cfg, run)
        done.append(asdict(run))
        label = f"{run.n_fetched} fetched" if run.n_fetched else run.note
        if run.n_fetched and run.note:
            label += f"; {run.note}"
        q = "" if group == "all" else f" [{group}]"
        print(
            f"{taxid:>10}  {str(info['name'])[:34]:<34}{q:<14} {run.mode:<11}  "
            f"{run.n_available:>8} avail  {label}",
            flush=True,
        )
    if skipped:
        print(f"{len(skipped)} groups skipped for size", file=sys.stderr)
    if errors:
        print(f"{len(errors)} groups failed", file=sys.stderr)
    if args.run_record and not args.dry_run:
        args.run_record.parent.mkdir(parents=True, exist_ok=True)
        record = {
            "run_date": date.today().isoformat(),
            "runs": done,
            "skipped": [list(k) for k in skipped],
            "errors": [list(k) for k in errors],
        }
        tmp = args.run_record.with_name(f".{args.run_record.name}.part")
        tmp.write_text(json.dumps(record, indent=2) + "\n")
        os.replace(tmp, args.run_record)
    return 1 if errors or (args.strict and skipped) else 0


if __name__ == "__main__":
    sys.exit(main())
