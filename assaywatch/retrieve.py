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
is required; the API key is read from `$NCBI_API_KEY` or `.secrets/ncbi.key`
if either is set (see `assaywatch/credentials.py`), and the client sleeps
between calls either way.

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
from datetime import date, timedelta
from pathlib import Path
from typing import Any

from assaywatch.credentials import ncbi_api_key, scrub
from assaywatch.groups import group_slug as group_slug

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
    taxid: int | None = None  # NCBI taxonomic id; backfilled for existing records
    is_patent: bool = False  # GenBank patent division; see looks_like_patent

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
                    raise RetrievalError(f"{endpoint}: {scrub(e)}") from e
                time.sleep(2**attempt)
                continue
            # 429 and 5xx are transient; everything else is a bug in the query
            # or a blocked network, and retrying will not help.
            if resp.status_code in (429, 500, 502, 503, 504):
                time.sleep(2**attempt)
                continue
            if resp.status_code == 400 and "history" in body.lower():
                raise HistoryExpired(f"{endpoint}: {scrub(body)[:200]}")
            if resp.status_code >= 400:
                raise RetrievalError(f"{endpoint}: HTTP {resp.status_code} {scrub(body)[:200]}")
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


# `group_slug` lives in assaywatch/groups.py so that report-time code (clustermaps.py)
# can name an assay's archive directory without importing this module and its NCBI
# transport into the report's trigger closure. Re-exported here for its existing callers.


# --------------------------------------------------------------------------
# E-utilities calls
# --------------------------------------------------------------------------


def esearch(
    transport: Transport, query: str, since: str | None, datetype: str = "mdat", until: str | None = None
) -> dict[str, Any]:
    """Count and history handle for `query`, optionally limited to [since, until] by `datetype`.

    `until` pins the upper end of the date range to the run date, so records
    deposited while a long fetch is running do not change the count under it.
    """
    params: dict[str, Any] = {
        "db": "nuccore",
        "term": query,
        "usehistory": "y",
        "retmax": 0,
        "retmode": "xml",
    }
    if since or until:
        params |= {"datetype": datetype, "mindate": since or "1800/01/01", "maxdate": until or "3000/01/01"}
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
    root = ET.fromstring(xml)
    err = root.findtext("ERROR") or root.findtext(".//ERROR")
    if err:
        # NCBI reports a dropped history handle inside a normal 200 response.
        if "query" in err.lower() or "history" in err.lower():
            raise HistoryExpired(f"esummary: {err}")
        raise RetrievalError(f"esummary: {err}")
    out = []
    for doc in root.findall("DocSum"):
        created = _text(doc, "CreateDate").replace("/", "-")[:10]
        updated = _text(doc, "UpdateDate").replace("/", "-")[:10]
        length = _text(doc, "Length")
        taxid_str = _text(doc, "TaxId")
        out.append(
            RecordMeta(
                uid=doc.findtext("Id") or "",
                accession=_text(doc, "Caption") or _text(doc, "AccessionVersion"),
                created=created,
                updated=updated,
                length=int(length) if length.isdigit() else 0,
                title=_text(doc, "Title"),
                taxid=int(taxid_str) if taxid_str.isdigit() else None,
                is_patent="|pat|" in _text(doc, "Extra"),
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


def last_run_date(
    manifest: dict[str, Any],
    taxid: int,
    group: str = "all",
    query: str | None = None,
) -> str | None:
    """The most recent successful run for this group, as YYYY/MM/DD for Entrez.

    When *query* is given, only runs recorded under that same query count.

    Why that matters: the group slug hashes the ASSAY's query alone
    (`groups.group_slug`), but `build_query` also folds in `retrieve.min_length`,
    `max_length` and `query_suffix`. Change a length filter and the slug does not
    move, so the next run would go incremental under a NEW query and ask only for
    records modified since the last run -- permanently missing every older record
    that newly qualifies under the widened filter. This module's docstring said
    to pass `--full` after changing a length filter; nothing enforced it, and the
    records lost that way cannot be recovered by a later incremental run.
    Comparing the recorded query refuses the cursor instead of trusting a note.

    The old filter `r["n_fetched"] >= 0` is gone: a record count is never
    negative, so it excluded nothing and read as a guard against failed runs.
    Failed runs are not in the manifest at all -- `fetch_taxon` raises before
    `record_run` -- which is what actually provides that guarantee.
    """
    runs = [r for r in manifest["runs"] if r["taxid"] == taxid and r.get("group", "all") == group]
    if query is not None:
        runs = [r for r in runs if r.get("query") == query]
    dates = [r["run_date"] for r in runs]
    return max(dates).replace("-", "/") if dates else None


def write_manifest(cfg: dict[str, Any], manifest: dict[str, Any]) -> None:
    """Replace the manifest atomically, so an interruption can never leave half a file."""
    p = manifest_path(cfg)
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_name(f".{p.name}.part")
    tmp.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    os.replace(tmp, p)


def acquire_lock(cfg: dict[str, Any]):
    """Hold an exclusive lock on the retrieval directory until this process exits.

    Two retrievals at once (a scheduled pipeline run and a manual one) would
    pick the same `.part` names and race on the manifest's read-modify-write,
    losing runs from it. The second one now stops with a message instead. The
    lock is released by the OS when the process ends, however it ends.
    Returns the open lock file; keep a reference to it.
    """
    import fcntl

    root = Path(cfg.get("retrieved_dir", "data/retrieved"))
    root.mkdir(parents=True, exist_ok=True)
    # Deliberately not a context manager: held for the life of the process.
    fh = open(root / ".lock", "w")
    try:
        fcntl.flock(fh, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        fh.close()
        raise SystemExit(
            f"another retrieval is running on {root} (lock file {root / '.lock'}); "
            "wait for it to finish, then run again"
        ) from None
    fh.write(f"{os.getpid()}\n")
    fh.flush()
    return fh


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

    if int(r.get("page_size", 500)) < 1:
        raise RetrievalError("retrieve.page_size must be at least 1")
    manifest = load_manifest(cfg)
    since = None if full else last_run_date(manifest, taxid, group, query=query)
    if not full and since is None:
        # No cursor under THIS query. Either the group has never been fetched, or
        # it has been fetched under a different one -- a changed length filter or
        # query_suffix, which the group slug cannot see. Say which, because the
        # two look identical from the outside and the second is the one that
        # would otherwise have silently skipped records.
        prior = last_run_date(manifest, taxid, group)
        if prior is not None:
            prior_queries = sorted(
                {
                    r.get("query", "")
                    for r in manifest["runs"]
                    if r["taxid"] == taxid and r.get("group", "all") == group and r.get("query") != query
                }
            )
            print(
                f"taxid {taxid} group {group}: full fetch, not incremental. The last run "
                f"({prior}) recorded a different query, so an incremental fetch would ask only "
                f"for records modified since then and would permanently miss older records that "
                f"newly qualify.\n  now:    {query}\n  before: " + "\n  before: ".join(prior_queries),
                file=sys.stderr,
            )
    # datetype=mdat, not cdat: the query asks what CHANGED since the last run,
    # not what was created. A submitter revising a sequence can turn a mismatch
    # into a match, so a revision matters as much as a new deposit.
    if since:
        # Overlap the previous run by a few days: NCBI indexes some records
        # after their modification date, and those would otherwise fall into
        # the gap between runs for good. The overlap is re-fetched, and the
        # report keeps one row per accession, so it costs only bandwidth.
        overlap = int(r.get("incremental_overlap_days", 3))
        since = (date.fromisoformat(since.replace("/", "-")) - timedelta(days=overlap)).strftime("%Y/%m/%d")
    until = run_date.replace("-", "/")
    mode = "incremental" if since else "full"

    handle = esearch(transport, query, since, until=until)
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
        fresh = esearch(transport, query, since, until=until)
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

    # Two passes over the same history handle, in this order because each answers
    # something the next one needs: the summaries carry the deposit dates (which
    # FASTA headers do not, and which the whole drift question depends on) and
    # the record lengths, which set a safe efetch page size.
    # Pass 1: metadata. Also measures how big the records are, which decides
    # the efetch page size: 500 ITS fragments are 200 kB, 500 poxvirus
    # genomes are 100 MB, and the second is what drops connections.
    total_bases = n_meta = 0
    try:
        with gzip.open(meta_tmp, "wt") as mh:
            mh.write("uid\taccession\tcreated\tupdated\tlength\ttitle\ttaxid\tis_patent\n")
            for page in range(n_pages):
                for m in with_refresh(esummary, page, retmax):
                    total_bases += m.length
                    n_meta += 1
                    mh.write(
                        f"{m.uid}\t{m.accession}\t{m.created}\t{m.updated}\t{m.length}\t{m.title}"
                        f"\t{m.taxid or ''}\t{'1' if m.is_patent else ''}\n"
                    )

        target_bytes = int(r.get("page_target_bytes", 20_000_000))
        mean_len = max(1, total_bases // max(1, handle["count"]))
        fetch_retmax = min(retmax, max(10, target_bytes // mean_len))  # never above page_size
        fetch_pages = -(-handle["count"] // fetch_retmax)

        n = 0
        for_page_shortfall = 0
        with gzip.open(fasta_tmp, "wt") as fh:
            for page in range(fetch_pages):
                # Checked inside with_refresh, so an expired handle reported in the
                # body of a 200 response is refreshed and retried like any other.
                chunk, k = with_refresh(efetch_checked, page, fetch_retmax)
                # What this page should have held. An empty page already raised in
                # check_fasta_page; this catches a page that came back SHORT, which
                # is the same loss by a smaller amount.
                expected = min(fetch_retmax, handle["count"] - page * fetch_retmax)
                if k < expected:
                    for_page_shortfall += expected - k
                n += k
                fh.write(chunk if chunk.endswith("\n") else chunk + "\n")

        # A shortfall has one legitimate cause -- WGS master records, which have a
        # summary but no sequence -- and one illegitimate one: a page NCBI did not
        # fully answer. Before 2026-10-27 both produced the same note, so the two
        # were indistinguishable, and the run was recorded either way; the
        # incremental cursor then advanced past records that were never written.
        # Tolerate the configured share, refuse the rest, and refuse it HERE,
        # before os.replace, so a rejected run leaves no archive and no manifest
        # entry to skip past.
        shortfall = n_meta - n
        if shortfall > 0:
            tol = float(r.get("max_unexplained_shortfall", 0.02))
            floor = int(r.get("min_shortfall_allowance", 20))
            allowed_short = max(floor, int(tol * n_meta))
            if shortfall > allowed_short:
                raise RetrievalError(
                    f"taxid {taxid} group {group}: {n} records fetched against {n_meta} summaries, "
                    f"a shortfall of {shortfall} over the {allowed_short} allowed "
                    f"({tol:.1%} of {n_meta}, floor {floor}). WGS master records explain a few "
                    f"summaries without sequence; this is too many, so it is treated as pages NCBI "
                    f"did not answer. Nothing was written and the manifest was not advanced. "
                    f"Rerun; if the shortfall is real, raise retrieve.max_unexplained_shortfall."
                )
    except BaseException:
        # Leave nothing that looks like an archive, finished or not.
        meta_tmp.unlink(missing_ok=True)
        fasta_tmp.unlink(missing_ok=True)
        raise

    os.replace(meta_tmp, meta_path)
    os.replace(fasta_tmp, fasta_path)
    run.note = "" if fetch_retmax == retmax else f"pages of {fetch_retmax} (mean record {mean_len:,} nt)"

    run.n_fetched = n
    run.fasta = str(fasta_path)
    run.metadata = str(meta_path)
    if shortfall > 0:
        # Within tolerance, so recorded rather than refused -- but say which pages
        # were short, because "summaries without sequence" alone could not tell a
        # WGS master from a thin page.
        run.note = (run.note + "; " if run.note else "") + (
            f"{shortfall} summaries without sequence (page shortfall {for_page_shortfall})"
        )
    return run


def efetch_checked(transport: Transport, handle: dict[str, Any], page: int, retmax: int) -> tuple[str, int]:
    chunk = efetch_fasta(transport, handle, page, retmax)
    return chunk, check_fasta_page(chunk)


def check_fasta_page(chunk: str) -> int:
    """Records in one efetch page; raises if the page is not FASTA.

    NCBI can answer 200 with an error document instead of sequence. Written to
    the archive, that text was counted as records (by its '>' characters) and
    the run was recorded as a success, so the next run skipped past it.

    An EMPTY body raises too, as of 2026-10-27. It used to return 0: the guard
    above reads `if body and not body.startswith(">")`, which is False for an
    empty string, so an empty page was accepted, contributed 0 to the run's
    record count, and the run was still recorded with today's date -- after
    which the incremental cursor asked only for records modified since, and the
    page's records were gone for good. A page is only ever requested when
    `esearch` said there were records left to fetch, so an empty one is NCBI
    failing to answer, never a legitimate end-of-run.
    """
    body = chunk.lstrip()
    if not body:
        raise RetrievalError("efetch returned an empty page where records were expected")
    if not body.startswith(">"):
        head = body[:200]
        if "history" in head.lower() or "query" in head.lower():
            raise HistoryExpired(f"efetch: {head}")
        raise RetrievalError(f"efetch returned something other than FASTA: {head!r}")
    return sum(1 for line in chunk.splitlines() if line.startswith(">"))


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
    # Bound, not discarded: the lock is held until the process exits.
    _lock = None if args.dry_run else acquire_lock(cfg)
    # Resolved once: the environment variable, else .secrets/ncbi.key. Both the
    # E-utilities and Datasets transports take the same key.
    api_key = ncbi_api_key() or None
    transport = http_transport(args.email, api_key)
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

                fetch = fetch or datasets_transport(api_key)
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
            print(f"SKIP  {taxid}/{group}: {scrub(e)}", file=sys.stderr)
            skipped.append((taxid, group))
            continue
        except Exception as e:  # noqa: BLE001 - one group's failure must not stop the others
            # Transport errors, malformed XML from NCBI, a corrupt genome zip:
            # whatever it is, log it against this group and carry on.
            print(f"ERROR {taxid}/{group}: {type(e).__name__}: {scrub(e)}", file=sys.stderr)
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
