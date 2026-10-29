"""The one NCBI client: key, pacing, retry, the taxonomy parsers, and the caches.

Why one module. The E-utilities transport lived in `retrieve.py`, the Datasets
transport in `assemblies.py`, and eleven scripts talked to NCBI on their own, five of
them parsing the same `efetch db=taxonomy` XML into five different shapes. Each copy
had its own idea of the rate limit and of what to do on a 429, and a blocked IP
affects everyone at the institution. This module is where those decisions live.

What it owns:
- `eutils(...)` and `datasets(...)`: the two real transports. Both pace to NCBI's
  published limits (10/s with a key, 3/s or 5/s without), retry 429 and 5xx with
  backoff, give up after five attempts, and scrub the key out of every error.
  Their HTTP function and their `sleep` are parameters, so tests drive them without
  a network or a clock.
- `TaxonRecord` and the parsers: one shape for a taxonomy answer, with every field
  the callers wanted (name, rank, NCBI's common name, the lineage with taxids and
  ranks, the other names, the merged-away ids).
- The caches, and this module is their only writer:
  `docs/taxon-records.cache.json` (the assay sheet's name / rank per taxid),
  `docs/taxa-cache.json` (the lineage analysis's taxid -> name map, under `taxa`),
  and `docs/taxonomy-cache.json.gz` (the parent tree the scope test reads, via
  `assaywatch.taxonomy`). The first two are different things and stay two files;
  tests/test_config_keys.py pins their shapes.

Retrieval and assembly logic stay in `retrieve.py` and `assemblies.py`; they import
their transports from here. `taxonomy.py` (the offline tree) stays separate on
purpose: the report imports it, and importing this module there would put the
network stack into the report rule's trigger closure.
"""

from __future__ import annotations

import gzip
import json
import time
import xml.etree.ElementTree as ET
from collections.abc import Callable, Iterable
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

from assaywatch.credentials import ncbi_api_key
from assaywatch.credentials import scrub as _scrub_known
from assaywatch.lineage import load_taxa_cache
from assaywatch.taxonomy import Taxonomy

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
DATASETS = "https://api.ncbi.nlm.nih.gov/datasets/v2"

#: Seconds between E-utilities calls: NCBI allows 10/s with a key and 3/s without.
INTERVAL_WITH_KEY = 0.11
INTERVAL_WITHOUT_KEY = 0.34
#: Datasets allows 5/s without a key.
DATASETS_INTERVAL_WITHOUT_KEY = 0.21
ATTEMPTS = 5
TRANSIENT = frozenset({429, 500, 502, 503, 504})

#: E-utilities: (endpoint such as "esearch", params) -> response body.
Transport = Callable[[str, dict[str, Any]], str]
#: Datasets: (path under DATASETS, query params, Accept header) -> response body.
Fetch = Callable[[str, dict[str, Any], str], bytes]


class NcbiError(RuntimeError):
    """NCBI could not be asked, or answered with an error."""


class HistoryExpired(NcbiError):
    """NCBI's history server dropped the WebEnv between calls; re-search and retry."""


def api_key(*, root: Path | None = None) -> str | None:
    """The NCBI key from `$NCBI_API_KEY` or `.secrets/ncbi.key`, or None."""
    return ncbi_api_key(root=root) or None


# --- transports -----------------------------------------------------------------


def _scrubber(api_key: str | None) -> Callable[[object], str]:
    """`credentials.scrub` knows the keys in the environment and the secrets files;
    a transport also redacts the key it was HANDED, which may be neither."""

    def scrub(text: object) -> str:
        out = _scrub_known(text)
        if api_key and len(api_key) >= 8:
            out = out.replace(api_key, "[redacted]")
        return out

    return scrub


def _pacer(interval: float, sleep: Callable[[float], None]) -> Callable[[], None]:
    last = [0.0]

    def wait() -> None:
        pause = interval - (time.monotonic() - last[0])
        if pause > 0:
            sleep(pause)
        last[0] = time.monotonic()

    return wait


def eutils(
    email: str,
    api_key: str | None,
    timeout: int = 60,
    *,
    post: Callable[..., Any] | None = None,
    sleep: Callable[[float], None] = time.sleep,
) -> Transport:
    """The E-utilities transport. `requests` is imported lazily so tests need no network stack."""
    if post is None:
        import requests

        post = requests.post
    wait = _pacer(INTERVAL_WITH_KEY if api_key else INTERVAL_WITHOUT_KEY, sleep)
    scrub = _scrubber(api_key)

    def call(endpoint: str, params: dict[str, Any]) -> str:
        params = {**params, "email": email, "tool": "assaywatch"}
        if api_key:
            params["api_key"] = api_key
        for attempt in range(ATTEMPTS):
            wait()
            try:
                resp = post(f"{EUTILS}/{endpoint}.fcgi", data=params, timeout=timeout)
                # Reading the body is where a large efetch page actually fails
                # ("Response ended prematurely"); it has to be inside the try.
                body = resp.text
            except Exception as e:
                if attempt == ATTEMPTS - 1:
                    raise NcbiError(f"{endpoint}: {scrub(e)}") from e
                sleep(2**attempt)
                continue
            # 429 and 5xx are transient; everything else is a bug in the query
            # or a blocked network, and retrying will not help.
            if resp.status_code in TRANSIENT:
                sleep(2**attempt)
                continue
            if resp.status_code == 400 and "history" in body.lower():
                raise HistoryExpired(f"{endpoint}: {scrub(body)[:200]}")
            if resp.status_code >= 400:
                raise NcbiError(f"{endpoint}: HTTP {resp.status_code} {scrub(body)[:200]}")
            return body
        raise NcbiError(f"{endpoint} failed after {ATTEMPTS} attempts")

    return call


def datasets(
    api_key: str | None,
    timeout: int = 300,
    *,
    get: Callable[..., Any] | None = None,
    sleep: Callable[[float], None] = time.sleep,
) -> Fetch:
    """The Datasets transport: 5 requests/s without a key, 10 with one."""
    if get is None:
        import requests

        get = requests.get
    wait = _pacer(INTERVAL_WITH_KEY if api_key else DATASETS_INTERVAL_WITHOUT_KEY, sleep)
    scrub = _scrubber(api_key)

    def call(path: str, params: dict[str, Any], accept: str) -> bytes:
        headers = {"Accept": accept}
        if api_key:
            headers["api-key"] = api_key
        for attempt in range(ATTEMPTS):
            wait()
            try:
                resp = get(f"{DATASETS}/{path}", params=params, headers=headers, timeout=timeout)
                body = resp.content
            except Exception as e:
                if attempt == ATTEMPTS - 1:
                    raise NcbiError(f"{path}: {scrub(e)}") from e
                sleep(2**attempt)
                continue
            if resp.status_code in TRANSIENT:
                sleep(2**attempt)
                continue
            if resp.status_code >= 400:
                detail = scrub(body.decode("utf-8", "replace"))[:200]
                raise NcbiError(f"{path}: HTTP {resp.status_code} {detail!r}")
            return body
        raise NcbiError(f"{path} failed after {ATTEMPTS} attempts")

    return call


# --- taxonomy -------------------------------------------------------------------


@dataclass(frozen=True)
class TaxonRecord:
    """One answer from `efetch db=taxonomy`, every field a caller has wanted.

    `taxid` is the id NCBI uses NOW; a merged-away id asked for comes back under its
    new id, with the old one in `aka_taxids`. `lineage` runs root to parent as
    (taxid, rank, scientific name).
    """

    taxid: int
    scientific_name: str
    common_name: str
    rank: str
    lineage: tuple[tuple[int, str, str], ...]
    other_names: frozenset[str]
    aka_taxids: tuple[int, ...]

    @property
    def lineage_tail(self) -> tuple[str, ...]:
        """The last two ancestor names, which is what the assay sheet shows."""
        return tuple(n for _, _, n in self.lineage[-2:])

    @property
    def ancestors(self) -> frozenset[int]:
        """Every ranked ancestor plus the taxon itself."""
        return frozenset(t for t, _, _ in self.lineage) | {self.taxid}

    @property
    def lineage_text(self) -> str:
        return "; ".join(n for _, _, n in self.lineage)


def parse_taxon_records(xml: str) -> dict[int, TaxonRecord]:
    """{taxid: record}, with each merged-away id keyed to the record it now means."""
    out: dict[int, TaxonRecord] = {}
    for taxon in ET.fromstring(xml).findall("Taxon"):
        tid = int(taxon.findtext("TaxId") or 0)
        lineage = tuple(
            (
                int(t.findtext("TaxId") or 0),
                t.findtext("Rank") or "no rank",
                t.findtext("ScientificName") or "",
            )
            for t in taxon.findall("LineageEx/Taxon")
        )
        other = {
            (el.text or "").strip().lower()
            for el in taxon.findall("OtherNames/*")
            if el.tag != "Name" and el.text and el.text.strip()
        }
        other |= {
            (el.findtext("DispName") or "").strip().lower()
            for el in taxon.findall("OtherNames/Name")
            if (el.findtext("DispName") or "").strip()
        }
        akas = tuple(int(a.text) for a in taxon.findall("AkaTaxIds/TaxId") if a.text)
        rec = TaxonRecord(
            taxid=tid,
            scientific_name=taxon.findtext("ScientificName") or "",
            # NCBI's own common name, or blank. Never invented.
            common_name=taxon.findtext("OtherNames/GenbankCommonName")
            or taxon.findtext("OtherNames/CommonName")
            or "",
            rank=taxon.findtext("Rank") or "no rank",
            lineage=lineage,
            other_names=frozenset(other),
            aka_taxids=akas,
        )
        out[tid] = rec
        for old in akas:
            out[old] = rec
    return out


def taxon_records(taxids: Iterable[int], transport: Transport, batch: int = 100) -> dict[int, TaxonRecord]:
    """Fetch and parse taxonomy records in batches."""
    ids = sorted(set(taxids))
    out: dict[int, TaxonRecord] = {}
    for i in range(0, len(ids), batch):
        chunk = ids[i : i + batch]
        xml = transport("efetch", {"db": "taxonomy", "id": ",".join(map(str, chunk)), "retmode": "xml"})
        out.update(parse_taxon_records(xml))
    return out


def parse_merged(docsum_xml: str) -> dict[int, int]:
    """{old taxid: new taxid} from `efetch db=taxonomy -format docsum`."""
    merged: dict[int, int] = {}
    for doc in ET.fromstring(docsum_xml).iter("DocumentSummary"):
        tid, aka = doc.findtext("TaxId"), doc.findtext("AkaTaxId")
        if tid and aka and aka.isdigit() and int(aka) not in (0, int(tid)):
            merged[int(tid)] = int(aka)
    return merged


def merged_taxids(taxids: Iterable[int], transport: Transport, batch: int = 100) -> dict[int, int]:
    ids = sorted(set(taxids))
    out: dict[int, int] = {}
    for i in range(0, len(ids), batch):
        chunk = ids[i : i + batch]
        xml = transport("efetch", {"db": "taxonomy", "id": ",".join(map(str, chunk)), "rettype": "docsum"})
        out.update(parse_merged(xml))
    return out


def taxids_of_uids(uids: Iterable[str], transport: Transport, batch: int = 500) -> dict[str, int]:
    """{nuccore uid: taxid} via esummary; a uid with no TaxId item is left out."""
    ids = list(dict.fromkeys(uids))
    out: dict[str, int] = {}
    for i in range(0, len(ids), batch):
        chunk = ids[i : i + batch]
        xml = transport("esummary", {"db": "nuccore", "id": ",".join(chunk), "retmode": "xml"})
        for doc in ET.fromstring(xml).findall("DocSum"):
            uid = doc.findtext("Id")
            item = doc.find(".//Item[@Name='TaxId']")
            if uid and item is not None and item.text and item.text.isdigit():
                out[uid] = int(item.text)
    return out


# --- the parent tree the scope test reads -----------------------------------------


def _tree_maps(records: dict[int, TaxonRecord]) -> tuple[dict[int, int], dict[int, str], dict[int, str]]:
    parent: dict[int, int] = {}
    rank: dict[int, str] = {}
    name: dict[int, str] = {}
    for rec in set(records.values()):
        path = [*rec.lineage, (rec.taxid, rec.rank, rec.scientific_name)]
        for (up, _, _), (down, _, _) in zip(path, path[1:], strict=False):
            parent[down] = up
        for t, r, n in path:
            rank[t] = r
            name[t] = n
    return parent, rank, name


def taxonomy_tree(records: dict[int, TaxonRecord], merged: dict[int, int] | None = None) -> Taxonomy:
    """An offline `Taxonomy` built from fetched records and merges."""
    parent, rank, name = _tree_maps(records)
    return Taxonomy(parent, dict(merged or {}), rank, name)


def save_taxonomy_cache(
    path: Path,
    records: dict[int, TaxonRecord],
    *,
    merged: dict[int, int],
    n_requested: int,
    missing: list[int],
    name_keys: Iterable[int] = (),
) -> None:
    """Write the tree `assaywatch.taxonomy.load_taxonomy` reads (`drift.scope_taxonomy`).

    Names are kept only for species, for "unclassified ..." nodes, and for `name_keys`
    (record-level taxids with no species above them, which are lineage keys in their
    own right): every name would quadruple the committed file for nodes nothing
    displays.
    """
    parent, rank, name = _tree_maps(records)
    keep = set(name_keys)
    doc = {
        "description": "NCBI taxonomy parent links and merges; built by scripts/build_taxonomy_cache.py",
        "built": date.today().isoformat(),
        "n_requested": n_requested,
        "parent": {str(k): v for k, v in sorted(parent.items())},
        "rank": {str(k): v for k, v in sorted(rank.items()) if v != "no rank"},
        "name": {
            str(k): v
            for k, v in sorted(name.items())
            if rank.get(k) == "species" or v.startswith("unclassified ") or k in keep
        },
        "merged": {str(k): v for k, v in sorted(merged.items())},
        "missing": sorted(missing),
    }
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(path, "wt") as fh:
        json.dump(doc, fh, separators=(",", ":"))


# --- the two JSON caches --------------------------------------------------------


def load_taxon_records_cache(path: Path) -> dict[int, dict[str, Any]]:
    """`docs/taxon-records.cache.json`: {taxid: {scientific_name, common_name, rank, lineage_tail}}."""
    path = Path(path)
    if not path.exists():
        return {}
    return {int(k): v for k, v in json.loads(path.read_text()).items() if k.isdigit()}


def save_taxon_records_cache(path: Path, records: dict[int, TaxonRecord]) -> None:
    """Merge fetched records into the cache; existing entries for other taxids stay."""
    path = Path(path)
    doc = {str(k): v for k, v in load_taxon_records_cache(path).items()}
    for tid, rec in records.items():
        doc[str(tid)] = {
            "scientific_name": rec.scientific_name,
            "common_name": rec.common_name,
            "rank": rec.rank,
            "lineage_tail": list(rec.lineage_tail),
        }
    path.write_text(json.dumps(doc, indent=1, sort_keys=True) + "\n")


# The reader lives in lineage.py, which is the module that uses the map and sits in
# the report's trigger closure; importing THIS module there would drag the network
# stack (credentials, transports) into every report rerun. Re-exported here so the
# cache's reader and writer are found in one place.
load_taxa_names = load_taxa_cache


def save_taxa_names(path: Path, names: dict[int, str]) -> None:
    doc = {
        "description": "Cached NCBI taxid -> lineage name mappings for lineage-conditional analysis.",
        "taxa": {str(k): v for k, v in sorted(names.items())},
    }
    Path(path).write_text(json.dumps(doc, indent=1) + "\n")
