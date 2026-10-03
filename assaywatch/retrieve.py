"""Fetch nucleotide records for a target taxon from NCBI and archive them.

    python -m assaywatch.retrieve registry --email you@example.org
    python -m assaywatch.retrieve registry/CHYTRID_Bd_*.yaml --email ... --dry-run

One taxon at a time, driven by the taxids in the registry. Three E-utilities
calls per taxon, in this order, because each one answers a question the next
one needs:

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
    """One taxon fetched on one day. Serialised into the manifest."""

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
            if resp.status_code >= 400:
                raise RetrievalError(f"{endpoint}: HTTP {resp.status_code} {resp.text[:200]}")
            return resp.text
        raise RetrievalError(f"{endpoint} failed after 5 attempts")

    return call


# --------------------------------------------------------------------------
# Query construction
# --------------------------------------------------------------------------


def build_query(taxid: int, cfg: dict[str, Any]) -> str:
    """`txid...[Organism:exp]` plus the configured filters.

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
    return " AND ".join(parts)


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


def last_run_date(manifest: dict[str, Any], taxid: int) -> str | None:
    """The most recent successful run for this taxon, as YYYY/MM/DD for Entrez."""
    dates = [r["run_date"] for r in manifest["runs"] if r["taxid"] == taxid and r["n_fetched"] >= 0]
    return max(dates).replace("-", "/") if dates else None


def record_run(cfg: dict[str, Any], run: TaxonRun) -> None:
    p = manifest_path(cfg)
    p.parent.mkdir(parents=True, exist_ok=True)
    manifest = load_manifest(cfg)
    manifest["runs"].append(asdict(run))
    p.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")


# --------------------------------------------------------------------------
# The stage
# --------------------------------------------------------------------------


def targets_from_registry(paths: list[Path]) -> dict[int, dict[str, Any]]:
    """{taxid: {name, assays}} for every registry file that names a taxid."""
    from assaywatch.validate import iter_files, load_assay

    out: dict[int, dict[str, Any]] = {}
    for target in paths:
        for path in iter_files(target):
            assay = load_assay(path)
            if assay.status.value == "deprecated" or assay.target.taxid is None:
                continue
            slot = out.setdefault(assay.target.taxid, {"name": assay.target.taxon_name, "assays": []})
            slot["assays"].append(assay.id)
    return out


def retrieve_taxon(
    taxid: int,
    cfg: dict[str, Any],
    transport: Transport,
    *,
    taxon_name: str | None = None,
    assays: list[str] | None = None,
    full: bool = False,
    dry_run: bool = False,
    run_date: str | None = None,
) -> TaxonRun:
    """Fetch one taxon. Returns the run record; writes nothing when dry_run."""
    r = cfg.get("retrieve", {})
    run_date = run_date or date.today().isoformat()
    query = build_query(taxid, cfg)

    manifest = load_manifest(cfg)
    since = None if full else last_run_date(manifest, taxid)
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
    )

    cap = r.get("max_records_per_taxon")
    allowed = set(r.get("large_taxa_allowed") or [])
    if cap and handle["count"] > cap and taxid not in allowed:
        raise TooManyRecords(
            f"taxid {taxid} ({taxon_name}) has {handle['count']} records, over the cap of {cap}. "
            f"Add {taxid} to retrieve.large_taxa_allowed in config.yaml to fetch it anyway, "
            "or narrow retrieve.query_suffix."
        )
    if handle["count"] == 0 or dry_run:
        run.note = "nothing new" if handle["count"] == 0 else "dry run"
        return run

    out_dir = Path(cfg.get("retrieved_dir", "data/retrieved")) / str(taxid)
    out_dir.mkdir(parents=True, exist_ok=True)
    fasta_path = out_dir / f"{run_date}.fasta.gz"
    meta_path = out_dir / f"{run_date}.meta.tsv.gz"

    retmax = int(r.get("page_size", 500))
    n_pages = -(-handle["count"] // retmax)

    with gzip.open(meta_path, "wt") as mh:
        mh.write("uid\taccession\tcreated\tupdated\tlength\ttitle\n")
        for page in range(n_pages):
            for m in esummary(transport, handle, page, retmax):
                mh.write(f"{m.uid}\t{m.accession}\t{m.created}\t{m.updated}\t{m.length}\t{m.title}\n")

    n = 0
    with gzip.open(fasta_path, "wt") as fh:
        for page in range(n_pages):
            chunk = efetch_fasta(transport, handle, page, retmax)
            n += chunk.count(">")
            fh.write(chunk if chunk.endswith("\n") else chunk + "\n")

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
    args = ap.parse_args(argv)

    cfg = load_config(args.config)
    transport = http_transport(args.email, os.environ.get("NCBI_API_KEY"))
    targets = targets_from_registry(args.paths)
    if args.taxid:
        targets = {t: v for t, v in targets.items() if t in args.taxid}

    print(
        f"{len(targets)} taxa from {sum(len(v['assays']) for v in targets.values())} assays", file=sys.stderr
    )
    failures = 0
    for taxid, info in sorted(targets.items()):
        try:
            run = retrieve_taxon(
                taxid,
                cfg,
                transport,
                taxon_name=info["name"],
                assays=info["assays"],
                full=args.full,
                dry_run=args.dry_run,
            )
        except RetrievalError as e:
            print(f"SKIP  {taxid}: {e}", file=sys.stderr)
            failures += 1
            continue
        if not args.dry_run:
            record_run(cfg, run)
        label = run.note or f"{run.n_fetched} fetched"
        print(
            f"{taxid:>10}  {str(info['name'])[:40]:<40}  {run.mode:<11}  {run.n_available:>8} avail  {label}"
        )
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
