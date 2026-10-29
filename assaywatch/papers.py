"""The `papers/` filename convention, in the one direction that is well defined.

A paper on disk is named after its DOI with the characters a filename cannot
hold replaced by underscores, lowercased:

    10.1016/S0166-0934(96)02155-6   ->   10.1016_s0166-0934_96_02155-6.pdf

Going that way is exact. Coming back is not, because three different characters
map onto `_`, and five call sites tried anyway with `stem.replace("_", "/")`:

- `verify_oligos_against_paper.index_papers` indexed such a paper under
  `10.1016/0890-8508/92/90002-f`, which still matches a DOI pattern, so the file
  was filed under a DOI nothing asks for AND counted as "named", which barred it
  from the surname-and-year fallback. Twenty registry entries read
  `no-full-text`, "no local PDF", against papers that were on disk. Fixed
  2026-10-20; measured in isolation, 38 oligos moved off `no-full-text`, 8 of
  them onto a discrepancy verdict, three of those genuine.
- `find_open_access.needed_dois` built its "already held" set the same way and
  so reported 10 of 26 missing papers as missing while they sat in `papers/`.
  That list is what `results/nyu-fetch-list.tsv` is built from.
- `papers_index`, `extract_candidate_oligos` and `import_pmc_fulltext` each had
  their own copy.

So nothing reverse-maps any more. A caller with a DOI forward-maps it and looks
for that name; a caller holding only a filename treats the stem as an opaque
key, never as a DOI.

The WRITING side has to forward-map through the same function, which took until
2026-10-24 to finish. Three fetchers - `fetch_elsevier`, `fetch_europepmc_fulltext`
(which carried its own one-line copy) and `find_open_access` - wrote
`doi.replace("/", "_")`, replacing the slash but not the parentheses, so eleven
Elsevier JATS deposits landed as `10.1016_s0016-5085(98)70589-x.xml`: a name no
reader forward-mapping a DOI can produce. `papers_index` had been taught to accept
both spellings; `verify_oligos_against_paper` compares the canonical stem alone and
so reached those eleven only by the weaker route of the DOI the deposit prints in
its own text. All three fetchers now call `doi_stem` and the eleven files were
renamed. Anything that writes into `papers/` must go through it.

MEASURED over the registry, 2026-10-20: 187 DOIs, 104 distinct, and the only
characters outside `[A-Za-z0-9.-/]` are `(` and `)`, 20 of each. No DOI contains
an underscore and no two DOIs share a stem, so the map is injective on the real
data. `<` and `>` are replaced too, for the old Wiley SICI DOIs that
`import_pmc_fulltext` warned about, though none is in the registry today.
"""

from __future__ import annotations

import json
import os
import re
import unicodedata
import urllib.parse
from collections.abc import Callable
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

from assaywatch.atomic import write_text

# `/` always; `(` and `)` because the registry has 40 of them; `<` and `>`
# against SICI DOIs. Anything else a DOI may legally hold is filename-safe.
UNSAFE_IN_FILENAME = re.compile(r"[/()<>]")


def doi_stem(doi: str) -> str:
    """The `papers/` filename stem for a DOI: lowercased, unsafe characters as `_`.

    Lowercasing is not cosmetic. PMC echoes a DOI in the publisher's casing, so
    the same paper arrives as `10.1128/JCM.00192-08` and is stored in the
    registry as `10.1128/jcm.00192-08`; 60 of the registry's 187 DOIs are not
    already lower case.
    """
    return UNSAFE_IN_FILENAME.sub("_", doi.strip().lower())


def paper_for_doi(doi: str, paper_dir: Path, suffixes: tuple[str, ...] = ()) -> Path | None:
    """The file in `paper_dir` named after this DOI, or None.

    `suffixes` restricts the search (`(".pdf",)` for a PDF-only caller); empty
    means any extension. Compares stems rather than globbing a pattern, because
    a DOI stem contains `.` and would otherwise need escaping.
    """
    if not doi:
        return None
    want = doi_stem(doi)
    for p in sorted(paper_dir.glob("*")) if paper_dir.is_dir() else []:
        if p.stem.lower() == want and (not suffixes or p.suffix.lower() in suffixes):
            return p
    return None


def held_dois(dois: list[str] | set[str], paper_dir: Path) -> set[str]:
    """The subset of `dois` (lowercased) whose paper is in `paper_dir`.

    Forward-mapped, so the answer does not depend on recovering a DOI from a
    filename. Reads the directory once rather than per DOI.
    """
    stems = {p.stem.lower() for p in paper_dir.glob("*")} if paper_dir.is_dir() else set()
    return {d.strip().lower() for d in dois if doi_stem(d) in stems}


# After mapping, a stem should hold only these. Anything else either cannot be
# written portably (`:` on Windows, from the old SICI DOIs) or has no business in
# a filename (`%`, `;`).
SAFE_STEM = re.compile(r"^[a-z0-9._-]+$")


def unstorable_reason(doi: str) -> str | None:
    """Why this DOI cannot be stored under the papers/ convention, or None.

    Reversibility used to be the test: `import_pmc_fulltext` asked whether
    turning every `_` back into `/` returned the DOI, because readers inferred a
    DOI from a filename. None does now, so the question is no longer "can it be
    read back" but "does the name identify it, and can it be written".

    Two ways it cannot:

    - The stem is ambiguous. A DOI holding `_` maps to the same stem as one
      holding `/` or `(` in that position, so the name no longer names one paper.
      No registry DOI contains `_` (checked over all 187 on 2026-10-20), so this
      refuses a hypothetical rather than anything in hand.
    - The stem holds a character that does not belong in a filename: `%`, `;`,
      or the `:` of a SICI DOI such as
      `10.1002/(SICI)1096-9071(199908)58:4<363::AID-JMV7>3.0.CO;2-2`.
    """
    if not doi or not doi.strip():
        return "empty DOI"
    if "_" in doi:
        return (
            "contains an underscore, which the filename convention also produces, "
            "so the stem would be ambiguous"
        )
    stem = doi_stem(doi)
    if not SAFE_STEM.fullmatch(stem):
        bad = sorted({c for c in stem if not SAFE_STEM.fullmatch(c)})
        return f"maps to a stem holding {''.join(bad)!r}, which does not belong in a filename"
    return None


# A supplement held beside its article: `<doi stem>.supp.<ext>`. Both readers
# that identify a file by its name have to agree on this marker. When only
# `papers_index` knew it, `verify_oligos_against_paper` read the stem whole:
# `10.1371_journal.pone.0207365.supp` still matches a DOI pattern, so the
# supplement was filed under a DOI nothing cites, and three Hermes entries kept
# reading `no-oligos` against a table that was on disk.
SUPPLEMENT_SUFFIX = ".supp"


# Every extension `papers/` may hold, and it lives here for the same reason
# SUPPLEMENT_SUFFIX does: both readers that identify a paper by its filename have
# to agree on it. When only `verify_oligos_against_paper` knew the list and
# `papers_index` globbed `*.pdf` alone, the index reported four papers held as
# `.txt` and twelve as publisher `.xml` as never obtained - its legend says
# "blank means the paper still needs to be obtained" - so the one durable record
# of what this project has read understated it by sixteen papers, and a reader
# went looking for Santiago 2003 behind a paywall it is not behind.
#
# A PDF is what a browser download gives; `.xml` is a publisher's own JATS
# deposit, and `.txt` is what `scripts/import_pmc_fulltext.py` writes from
# PubMed Central's open-access full text.
#
# No format is better than the others, which took a wrong turn to learn. The
# first version preferred publisher text over a PDF on the reasoning that
# structured text beats a table pypdf has to rebuild from glyph positions. That is
# true of the text a publisher deposits in full, and not of PMC full text as served
# through an MCP tool, which comes back flattened and often (not always: Prepens
# 2007 and Deckers 2009 kept their primer tables) without its tables - so preferring
# it would let a table-less text file override a PDF whose primer table extracts
# perfectly well. `index_papers` picks between them on what they actually yield
# instead.
PAPER_SUFFIXES = (".pdf", ".xml", ".txt")


def identity_stem(path: Path) -> str:
    """The stem that says WHICH paper a file belongs to, `.supp` marker removed.

    A supplement is not a different paper, so it answers to its article's stem.
    Which of the two is held is a separate question, answered by the real
    filename (`papers_index` prints it as `suppl`).
    """
    stem = path.stem
    if stem.lower().endswith(SUPPLEMENT_SUFFIX):
        stem = stem[: -len(SUPPLEMENT_SUFFIX)]
    return stem


# ==============================================================================
# The client half: Crossref, the open-access routes, full text, and storage.
#
# Why here. Six scripts fetched papers, each with its own HTTP call, User-Agent,
# JSON parsing and error habit, and the same four helpers (`pmcid_for`, `doi_of`,
# `paper_text`, `registry_dois`) were written twice each. `curate` needs the whole
# chain in one call (`obtain`), and the chain's decisions - local file first, an
# abstract-length deposit is not full text, a paywalled DOI goes on the human's
# queue - should be made once.
#
# Every network function takes a `Get`, (url, headers) -> (status, content type,
# body), so the tests hand in canned answers and nothing here needs a socket.
# ==============================================================================

#: (url, headers) -> (HTTP status, Content-Type, body). 0 and the reason for a
#: network failure; never raises for an HTTP error status.
Get = Callable[[str, dict[str, str]], tuple[int, str, bytes]]

CROSSREF = "https://api.crossref.org/works/"
UNPAYWALL = "https://api.unpaywall.org/v2/"
OPENALEX = "https://api.openalex.org/works/doi:"
EUROPEPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest"
PMC_CONVERTER = "https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/"
ELSEVIER = "https://api.elsevier.com/content/article/doi/"

#: Below this many characters a Europe PMC deposit is an abstract, not a paper, and
#: cannot confirm or deny a primer (the floor fetch_europepmc_fulltext always used).
FULLTEXT_MIN_CHARS = 6000

# Some publishers serve a free PDF but refuse an unfamiliar User-Agent with a 403:
# an anti-bot rule, not a paywall (Inter-Research's Diseases of Aquatic Organisms
# is one). On a 403 a PDF download is retried once with a browser string. Only
# ever applied to files Unpaywall or OpenAlex already report as open.
BROWSER_UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)


def http(timeout: int = 60) -> Get:
    """The real `Get`, on urllib so the client needs nothing beyond the stdlib."""
    import urllib.error
    import urllib.request

    def get(url: str, headers: dict[str, str]) -> tuple[int, str, bytes]:
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, r.headers.get("Content-Type", ""), r.read()
        except urllib.error.HTTPError as e:
            # 401/403/404 bodies carry the publisher's own explanation; keep them.
            return e.code, e.headers.get("Content-Type", ""), e.read()
        except (urllib.error.URLError, OSError) as e:
            return 0, "", str(getattr(e, "reason", e)).encode()

    return get


def _ua(email: str) -> dict[str, str]:
    return {"User-Agent": f"assaywatch (research tool; {email or 'unset'})"}


def _json(get: Get, url: str, headers: dict[str, str]) -> Any | None:
    status, _ctype, body = get(url, headers)
    if status != 200:
        return None
    try:
        return json.loads(body.decode("utf-8", "replace"))
    except json.JSONDecodeError:
        return None


# --- Crossref -------------------------------------------------------------------


@dataclass(frozen=True)
class Citation:
    """What Crossref says a DOI is: the fields the index and the checks read."""

    doi: str
    title: str
    journal: str
    year: int | None
    volume: str
    authors: tuple[str, ...]

    @property
    def first_author(self) -> str:
        return self.authors[0] if self.authors else ""


def parse_crossref(message: dict[str, Any]) -> Citation:
    # Crossref embeds italics as tags in titles; strip them so the index is plain text.
    title = re.sub(r"<[^>]+>", "", (message.get("title") or [""])[0])
    title = re.sub(r"\s+", " ", title).strip()
    year = None
    for key in ("published-print", "published-online", "issued", "created"):
        parts = ((message.get(key) or {}).get("date-parts") or [[None]])[0]
        if parts and parts[0]:
            year = int(parts[0])
            break
    return Citation(
        doi=(message.get("DOI") or "").lower(),
        title=title,
        journal=(message.get("container-title") or [""])[0],
        year=year,
        volume=message.get("volume") or "",
        authors=tuple(a.get("family", "") for a in (message.get("author") or []) if a.get("family")),
    )


def crossref(doi: str, get: Get, *, email: str) -> Citation | None:
    """Crossref's record for a DOI, or None when it does not resolve."""
    url = CROSSREF + urllib.parse.quote(doi, safe="") + "?mailto=" + urllib.parse.quote(email)
    data = _json(get, url, _ua(email))
    if not data or "message" not in data:
        return None
    return parse_crossref(data["message"])


def _fold(text: str) -> str:
    folded = unicodedata.normalize("NFKD", text)
    folded = "".join(ch for ch in folded if not unicodedata.combining(ch)).lower()
    return re.sub(r"[‐-―−]", "-", folded)


def _surname_tokens(family: str) -> list[str]:
    return [t for t in re.split(r"[\s\-]+", _fold(family)) if len(t) > 2]


def citation_matches(c: Citation, design_year: int | None, reference: str) -> tuple[bool, str]:
    """The rule that lets a DOI become `doi_verified`: Crossref's first author appears
    in the entry's reference text and the year is within one of `design_year`."""
    year_ok = design_year is None or c.year is None or abs(c.year - design_year) <= 1
    author_ok = bool(c.first_author) and _fold(c.first_author) in _fold(reference)
    return (year_ok and author_ok), f"{c.first_author} {c.year}: {c.title[:70]}"


def citation_problems(c: Citation, citation: dict[str, Any]) -> list[str]:
    """What `check_citations` reports for an entry's `citation:` block against Crossref."""
    ref = (citation.get("reference") or "") or (citation.get("as_written") or "")
    problems: list[str] = []
    family = c.first_author
    if family and ref.strip():
        toks = _surname_tokens(family)
        # A compound surname only needs one distinctive part present.
        if toks and not any(t in _fold(ref) for t in toks):
            problems.append(f"reference does not name Crossref's first author {family!r}: {ref[:110]!r}")
    elif family and not ref.strip():
        problems.append(f"no reference text, though Crossref knows the paper ({family})")
    if c.year:
        years = {int(y) for y in re.findall(r"\b((?:19|20)\d{2})\b", ref)}
        dy = citation.get("design_year")
        candidates = years | ({int(dy)} if dy else set())
        # Online-first publication legitimately straddles two years.
        if candidates and not any(abs(y - c.year) <= 1 for y in candidates):
            problems.append(
                f"no year within 1 of Crossref's {c.year}; reference/design_year give {sorted(candidates)}"
            )
    return problems


def load_index_cache(path: Path) -> dict[str, Citation | None]:
    """`docs/papers-index.cache.json`: {doi: Citation, or None for a DOI that did not resolve}."""
    path = Path(path)
    if not path.exists():
        return {}
    out: dict[str, Citation | None] = {}
    for doi, m in json.loads(path.read_text()).items():
        if m is None:
            out[doi] = None
            continue
        authors = m.get("authors")
        if authors is None:  # an older entry kept only the first author and a count
            authors = [m["first_author"]] if m.get("first_author") else []
        out[doi] = Citation(
            doi=doi,
            title=m.get("title") or "",
            journal=m.get("journal") or "",
            year=m.get("year"),
            volume=m.get("volume") or "",
            authors=tuple(authors),
        )
    return out


def save_index_cache(path: Path, cache: dict[str, Citation | None]) -> None:
    doc: dict[str, Any] = {}
    for doi, c in cache.items():
        doc[doi] = (
            None
            if c is None
            else {
                "title": c.title,
                "journal": c.journal,
                "year": c.year,
                "volume": c.volume,
                "first_author": c.first_author,
                "n_authors": len(c.authors),
                "authors": list(c.authors),
            }
        )
    write_text(Path(path), json.dumps(doc, indent=1, sort_keys=True) + "\n")


# --- where a free copy is -------------------------------------------------------


@dataclass(frozen=True)
class OpenAccess:
    source: str  # "unpaywall" or "openalex"
    is_oa: bool
    oa_status: str = ""
    host_type: str = ""
    version: str = ""
    url_pdf: str = ""
    url_landing: str = ""
    title: str = ""


def unpaywall(doi: str, get: Get, *, email: str) -> OpenAccess | None:
    d = _json(
        get, UNPAYWALL + urllib.parse.quote(doi, safe="") + "?email=" + urllib.parse.quote(email), _ua(email)
    )
    if not d:
        return None
    best = d.get("best_oa_location") or {}
    # Prefer a location that actually offers a PDF; best_oa_location sometimes
    # only has a landing page while another location has the file itself.
    pdf = best.get("url_for_pdf")
    if not pdf:
        for loc in d.get("oa_locations") or []:
            if loc.get("url_for_pdf"):
                best, pdf = loc, loc["url_for_pdf"]
                break
    return OpenAccess(
        source="unpaywall",
        is_oa=bool(d.get("is_oa")),
        oa_status=d.get("oa_status") or "",
        host_type=best.get("host_type") or "",
        version=best.get("version") or "",
        url_pdf=pdf or "",
        url_landing=best.get("url_for_landing_page") or best.get("url") or "",
        title=(d.get("title") or "")[:110],
    )


def openalex(doi: str, get: Get, *, email: str) -> OpenAccess | None:
    """OpenAlex's view. Asked alongside Unpaywall because the two disagree in practice:
    for 10.1177/1040638711416846 Unpaywall had no PDF and OpenAlex a direct link."""
    d = _json(
        get, OPENALEX + urllib.parse.quote(doi, safe="") + "?mailto=" + urllib.parse.quote(email), _ua(email)
    )
    if not d:
        return None
    loc = d.get("best_oa_location") or {}
    source = loc.get("source")
    return OpenAccess(
        source="openalex",
        is_oa=bool((d.get("open_access") or {}).get("is_oa")),
        url_pdf=loc.get("pdf_url") or "",
        version=loc.get("version") or "",
        host_type=source.get("type", "") if isinstance(source, dict) else "",
    )


def pmcid_for(doi: str, get: Get, *, email: str, api_key: str | None = None) -> str | None:
    """The PMC id holding this DOI's OPEN full text: NCBI's converter, then Europe PMC."""
    params = {"ids": doi, "format": "json", "tool": "assaywatch", "email": email}
    if api_key:
        params["api_key"] = api_key
    d = _json(get, PMC_CONVERTER + "?" + urllib.parse.urlencode(params), _ua(email))
    for rec in (d or {}).get("records", []):
        if rec.get("pmcid"):
            return rec["pmcid"]
    # Europe PMC indexes some records NCBI's converter misses.
    q = urllib.parse.urlencode(
        {"query": f'DOI:"{doi}"', "format": "json", "pageSize": 5, "resultType": "lite"}
    )
    d = _json(get, f"{EUROPEPMC}/search?{q}", _ua(email))
    for r in ((d or {}).get("resultList") or {}).get("result", []):
        # inPMC/isOpenAccess are strings "Y"/"N" in this API.
        if r.get("pmcid") and (r.get("isOpenAccess") == "Y" or r.get("inPMC") == "Y"):
            return r["pmcid"]
    return None


# --- full text ------------------------------------------------------------------


def flatten_xml(xml: str) -> str:
    """JATS XML -> text with table structure kept legible: cells ` | `, rows newlines.

    Without that a primer name and its sequence arrive fused ("2743sCGCAAATCGCAGA..."),
    which is exactly the failure that makes an extracted sequence unusable.
    """
    text = re.sub(r"<(table-wrap|table)\b", r"\n<\1", xml)
    text = re.sub(r"</t[dh]>", " | ", text)
    text = re.sub(r"</tr>", "\n", text)
    text = re.sub(r"</(p|title|caption|sec|abstract|table-wrap)>", "\n", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = text.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    text = re.sub(r"&#x?[0-9A-Fa-f]+;", " ", text)
    text = re.sub(r"[ \t]+", " ", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def europepmc_fulltext(pmcid: str, get: Get, *, email: str = "") -> str | None:
    """Europe PMC's open-access full text as flattened text, or None if there is none."""
    status, _ctype, body = get(f"{EUROPEPMC}/{pmcid}/fullTextXML", _ua(email))
    xml = body.decode("utf-8", "replace") if status == 200 else ""
    if "<article" not in xml:
        return None
    return flatten_xml(xml)


def elsevier_pdf(doi: str, get: Get, *, key: str, inst_token: str | None = None) -> tuple[int, str, bytes]:
    """(status, content type, body) from Elsevier's article API. The body of an error is
    Elsevier's JSON envelope; `elsevier_error` reads it."""
    headers = {"X-ELS-APIKey": key, "Accept": "application/pdf", "User-Agent": "assaywatch-fetch/1.0"}
    if inst_token:
        headers["X-ELS-Insttoken"] = inst_token
    return get(ELSEVIER + urllib.parse.quote(doi, safe="/") + "?httpAccept=application/pdf", headers)


def elsevier_error(body: bytes) -> str:
    try:
        st = json.loads(body.decode("utf-8", "replace"))["service-error"]["status"]
        return f"{st.get('statusCode')}: {st.get('statusText')}"
    except (ValueError, KeyError, TypeError, AttributeError):
        txt = body.decode("utf-8", "replace").strip().replace("\t", " ").replace("\n", " ")
        return txt[:200]


# --- storing and queueing -------------------------------------------------------


def store(doi: str, content: str | bytes, paper_dir: Path, *, kind: str) -> Path:
    """Write a paper under its `doi_stem` name, whole or absent. `kind` is pdf, txt or xml."""
    if f".{kind}" not in PAPER_SUFFIXES:
        raise ValueError(f"kind must be one of {PAPER_SUFFIXES}, not {kind!r}")
    path = Path(paper_dir) / f"{doi_stem(doi)}.{kind}"
    if isinstance(content, str):
        write_text(path, content)
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_name(f".{path.name}.part")
        tmp.write_bytes(content)
        os.replace(tmp, path)
    return path


QUEUE_HEADING = "## Queued by `assaywatch curate` (needs a human and a proxy)"


def queued(fetch_list: Path) -> set[str]:
    """Every DOI on the fetch list, by the one form the list always renders: a doi.org link."""
    fetch_list = Path(fetch_list)
    if not fetch_list.exists():
        return set()
    return set(re.findall(r"https://doi\.org/(10\.\S+?)\)", fetch_list.read_text()))


def queue_for_human(doi: str, reason: str, fetch_list: Path) -> None:
    """Append a DOI to `papers/papers-fetch-list.md`, once, under the curate heading."""
    fetch_list = Path(fetch_list)
    if doi in queued(fetch_list):
        return
    text = fetch_list.read_text() if fetch_list.exists() else "# Fetch list\n"
    if QUEUE_HEADING not in text:
        text = text.rstrip("\n") + f"\n\n{QUEUE_HEADING}\n\n"
    line = f"- [{doi}](https://doi.org/{doi}) — {reason} ({date.today().isoformat()})\n"
    head, _, tail = text.partition(QUEUE_HEADING + "\n")
    tail = tail.lstrip("\n")
    write_text(fetch_list, head + QUEUE_HEADING + "\n\n" + line + tail)


# --- obtain: the chain curate runs ---------------------------------------------


def _download_pdf(url: str, get: Get, email: str) -> bytes | None:
    status, ctype, body = get(url, {**_ua(email), "Accept": "application/pdf,*/*"})
    if status == 403:
        status, ctype, body = get(url, {"User-Agent": BROWSER_UA, "Accept": "application/pdf,*/*"})
    if status == 200 and body.startswith(b"%PDF"):
        return body
    return None


def obtain(
    doi: str,
    paper_dir: Path,
    get: Get,
    *,
    email: str,
    fetch_list: Path,
    elsevier: tuple[str, str | None] | None = None,
    api_key: str | None = None,
) -> tuple[Path | None, str]:
    """The paper for a DOI as a file in `paper_dir`, and how it got there.

    Order: a file already there; Europe PMC's open full text (stored as `.txt`, and
    only if longer than an abstract); a PDF that Unpaywall or OpenAlex says is free;
    Elsevier's API for a 10.1016 DOI when a key is given. When nothing works the
    DOI goes on the fetch list for a human and the answer is (None, "queued: ...").
    Never raises for a missing paper.
    """
    paper_dir = Path(paper_dir)
    local = paper_for_doi(doi, paper_dir) if paper_dir.is_dir() else None
    if local is not None:
        return local, "local"
    reasons: list[str] = []

    pmcid = pmcid_for(doi, get, email=email, api_key=api_key)
    if pmcid:
        text = europepmc_fulltext(pmcid, get, email=email)
        if text and len(text) >= FULLTEXT_MIN_CHARS:
            return store(doi, text, paper_dir, kind="txt"), f"europepmc:{pmcid}"
        reasons.append(f"{pmcid} is abstract-length" if text else f"{pmcid} has no full text")
    else:
        reasons.append("not in PMC")

    for route in (unpaywall, openalex):
        oa = route(doi, get, email=email)
        if oa and oa.url_pdf:
            pdf = _download_pdf(oa.url_pdf, get, email)
            if pdf:
                return store(doi, pdf, paper_dir, kind="pdf"), oa.source
            reasons.append(f"{oa.source} PDF link did not serve a PDF")
    if not any("PDF link" in r for r in reasons):
        reasons.append("no open-access PDF known")

    if elsevier and doi.lower().startswith("10.1016/"):
        status, _ctype, body = elsevier_pdf(doi, get, key=elsevier[0], inst_token=elsevier[1])
        if status == 200 and body.startswith(b"%PDF"):
            return store(doi, body, paper_dir, kind="pdf"), "elsevier"
        reasons.append(f"Elsevier {status}: {elsevier_error(body)}")

    reason = "; ".join(reasons)
    queue_for_human(doi, reason, fetch_list)
    return None, f"queued: {reason}"
