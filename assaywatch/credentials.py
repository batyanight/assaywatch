"""One place to find a credential, so dropping a key in makes everything faster.

    from assaywatch.credentials import ncbi_api_key
    key = ncbi_api_key()      # "" when there is none

Why this exists
---------------
An NCBI API key is not authentication - every endpoint this project touches is
public and readable without one. It is a rate limit: 3 requests per second
without a key, 10 with. Over a screening run of thousands of records that is
the difference between minutes and most of an hour, and over the whole registry
it is the difference between a run you start and watch and a run you start and
leave.

`assaywatch/retrieve.py` already read `NCBI_API_KEY` from the environment, but
five scripts that call E-utilities did not, so a key set in one place sped up
some of the work and none of the rest. Worse, there was no file option, while
the Elsevier credentials have had one since `scripts/fetch_elsevier.py` was
written. This module gives both, in one order, to every caller.

Where a key is looked for, first hit wins
-----------------------------------------
1. the environment variable, e.g. `NCBI_API_KEY`
2. `.secrets/<name>`, e.g. `.secrets/ncbi.key`

The environment comes first on purpose. A cloud session is configured by
setting environment variables, and that is the only route where the key never
touches a filesystem, a chat window or a diff - so the mechanism that leaks
least is also the one that wins.

`.secrets/` is gitignored in full, so a key file there cannot be committed by
accident.

A key in a URL ends up in error text
------------------------------------
E-utilities takes its key as a query parameter, so the key is in the URL of every
keyed request, and `requests` puts the full URL in the text of the exceptions it
raises. Left alone, a 429 or a refused connection prints the key into a
traceback, and from there into a Snakemake log, a CI log or a chat transcript.
`scrub` removes every credential this module knows about from a piece of text,
and the scripts that make keyed requests pass exception text through it. Nothing
else here prints a key; `describe` reports where one was found and how long it
is, never what it is.

A key file that cannot be used
------------------------------
A missing key is a normal state and means "run unkeyed". A key FILE that exists
but cannot be read as a key is different, and quietly treating it as absent would
leave a user who set one up correctly-looking, running at a third of the speed
with no idea why. So it is still treated as absent - a bad file must never stop a
run that works without it - but `describe` says what is wrong with it. Handled:
a UTF-8 byte-order mark, and the UTF-16 that Windows PowerShell 5 writes for
`echo KEY > file`. Refused, with a reason: bytes that are neither, and a file
with more than one non-blank line, because which line is the key is a guess and
a wrong guess is sent to NCBI.
"""

from __future__ import annotations

import argparse
import codecs
import json
import os
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# (environment variable, filename under .secrets/) per credential.
NCBI = ("NCBI_API_KEY", "ncbi.key")
ELSEVIER = ("ELSEVIER_API_KEY", "elsevier.key")
ELSEVIER_INSTTOKEN = ("ELSEVIER_INSTTOKEN", "elsevier.insttoken")
ALL = (NCBI, ELSEVIER, ELSEVIER_INSTTOKEN)

EUTILS_INFO = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/einfo.fcgi"


def _file_value(path: Path) -> tuple[str, str]:
    """(value, problem) for a key file. Exactly one of the two is non-empty,
    unless the file simply does not exist, when both are empty."""
    try:
        raw = path.read_bytes()
    except OSError:
        # Missing, unreadable, or a directory. All mean "no key", and none is
        # worth a message: a missing key file is the ordinary case.
        return "", ""
    if raw.startswith((codecs.BOM_UTF16_LE, codecs.BOM_UTF16_BE)):
        encoding = "utf-16"  # what PowerShell 5's `echo KEY > file` writes
    else:
        encoding = "utf-8-sig"  # also strips a UTF-8 byte-order mark
    try:
        text = raw.decode(encoding)
    except UnicodeDecodeError:
        return "", "is not valid UTF-8 or UTF-16 text"
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    if len(lines) > 1:
        return (
            "",
            f"has {len(lines)} non-blank lines; a key file holds one line and which is the key is a guess",
        )
    return (lines[0] if lines else ""), ""


def read_secret(spec: tuple[str, str], *, root: Path | None = None) -> str:
    """The credential named by `spec`, or "" if it is not set anywhere usable.

    Never raises and never prints. A missing or unusable credential is a normal
    state - most of this project works without any - so the caller decides
    whether to care, and `describe` says why one was not used.
    """
    env_var, filename = spec
    value = os.environ.get(env_var, "").strip()
    if value:
        return value
    return _file_value((root or ROOT) / ".secrets" / filename)[0]


def ncbi_api_key(*, root: Path | None = None) -> str:
    """The NCBI API key, or "". Raises the E-utilities rate limit 3/s -> 10/s."""
    return read_secret(NCBI, root=root)


def with_api_key(params: dict[str, str], *, root: Path | None = None) -> dict[str, str]:
    """`params` plus `api_key`, when one is set.

    E-utilities takes the key as an ordinary query parameter, so this is the
    whole integration. Returns a copy either way, so a caller can keep reusing
    one params literal in a loop without it accumulating state.

    The key then rides in the URL, so any exception text from the request must
    go through `scrub` before it is shown.
    """
    key = ncbi_api_key(root=root)
    return {**params, "api_key": key} if key else dict(params)


def ncbi_interval(*, root: Path | None = None) -> float:
    """Seconds to wait between E-utilities calls: 10/s with a key, 3/s without.

    The same two numbers `assaywatch/retrieve.py` has always used, so a keyed
    run is paced identically whether it goes through the pipeline or a script.
    NCBI asks callers to stay under the limit rather than to discover it, and a
    blocked IP affects everyone at the institution, so the sleep happens even
    when a key is present.
    """
    return 0.11 if ncbi_api_key(root=root) else 0.34


def scrub(text: object, *, root: Path | None = None) -> str:
    """`text` with every credential this module knows about replaced by [redacted].

    Both the raw value and its URL-encoded form are removed, since a key with an
    unusual character appears percent-encoded in a request URL.
    """
    out = str(text)
    for spec in ALL:
        value = read_secret(spec, root=root)
        if len(value) < 8:
            # Replacing a very short string would mangle ordinary text, and no
            # real credential is this short.
            continue
        for form in {value, urllib.parse.quote(value, safe=""), urllib.parse.quote_plus(value)}:
            out = out.replace(form, "[redacted]")
    return out


def describe(spec: tuple[str, str], *, root: Path | None = None) -> str:
    """A line about whether a credential was found, safe to print.

    Says where it came from and how long it is, never what it is. The length is
    worth showing because the usual failure is a truncated paste or a file with
    a trailing newline and nothing else, and a length tells those apart from a
    key that is simply absent. A key file that exists but cannot be used is
    reported with the reason, not passed off as absent.
    """
    env_var, filename = spec
    if os.environ.get(env_var, "").strip():
        return f"{env_var}: set in the environment ({len(os.environ[env_var].strip())} chars)"
    path = (root or ROOT) / ".secrets" / filename
    value, problem = _file_value(path)
    if value:
        return f"{env_var}: read from .secrets/{filename} ({len(value)} chars)"
    if problem:
        return f"{env_var}: .secrets/{filename} exists but {problem}, so it is being ignored"
    return f"{env_var}: not set (looked in ${env_var} and {path})"


def check_ncbi_key(*, root: Path | None = None, urlopen=urllib.request.urlopen) -> tuple[bool | None, str]:
    """Ask NCBI whether it accepts the key: (accepted, message), message scrubbed.

    `accepted` is None when there is no key or the question could not be asked.

    Why this exists: six scripts that used to send no key now send one, and if
    NCBI answers an invalid key with an error where it used to ignore a missing
    one, a mistyped key file turns "three times slower" into "does not work".
    Finding that out should be one cheap request, not a failed screening run.

    NOT YET RUN AGAINST NCBI. It was written where NCBI was unreachable, so the
    exact shape of NCBI's rejection (the HTTP status, and whether the body
    carries an `error` field) is assumed rather than observed: any HTTP error
    status, and any JSON body with an `error` key, count as rejection. Run it
    once from a networked machine; if NCBI's real answer differs, fix it here.
    """
    key = ncbi_api_key(root=root)
    if not key:
        return None, "no NCBI key is set, so there is nothing to check"
    query = urllib.parse.urlencode({"db": "pubmed", "retmode": "json", "tool": "assaywatch", "api_key": key})
    try:
        with urlopen(f"{EUTILS_INFO}?{query}", timeout=30) as resp:
            body = resp.read().decode("utf-8", "replace")
            status = getattr(resp, "status", 200)
    except urllib.error.HTTPError as e:
        detail = scrub(e.read().decode("utf-8", "replace")[:200], root=root)
        return False, f"NCBI answered HTTP {e.code}: {detail}"
    except Exception as e:  # noqa: BLE001 - a dead network is an answer, not a crash
        return None, f"could not reach NCBI ({type(e).__name__}): {scrub(e, root=root)}"
    try:
        error = json.loads(body).get("error")
    except (json.JSONDecodeError, AttributeError):
        error = None
    if error:
        return False, f"NCBI answered HTTP {status} with an error: {scrub(error, root=root)}"
    return True, f"NCBI accepted the key (HTTP {status})"


def main(argv: list[str] | None = None, *, root: Path | None = None) -> int:
    """`python -m assaywatch.credentials` - say which credentials are visible.

    The point of a one-command check is that setting a key and finding out
    whether it took should not be the same step as a long run that might fail
    for ten other reasons. Prints lengths and sources, never values. `--check`
    additionally asks NCBI whether it accepts the key.
    """
    ap = argparse.ArgumentParser(description=main.__doc__)
    ap.add_argument("--check", action="store_true", help="also ask NCBI whether it accepts the key")
    args = ap.parse_args(argv)

    print("credentials visible to this checkout:\n")
    for spec in ALL:
        print(f"  {describe(spec, root=root)}")
    key = ncbi_api_key(root=root)
    # Print NCBI's published limit and the interval separately. Printing the
    # derived rate instead said "9 requests/second" for a perfectly good key -
    # because the interval is deliberately a shade wider than 1/10 s - which
    # reads like the key is underperforming.
    limit = 10 if key else 3
    print(
        f"\nE-utilities: NCBI allows {limit} requests/second "
        f"{'with' if key else 'without'} a key, and this client waits "
        f"{ncbi_interval(root=root):.2f}s between calls to stay just inside it."
    )
    if not key:
        print(
            "\nNo NCBI key. Everything still works, 3x slower. To set one:\n"
            "  - in a cloud session, add NCBI_API_KEY to the environment's settings\n"
            "  - locally, write it to .secrets/ncbi.key (gitignored)\n"
            "Get one at https://www.ncbi.nlm.nih.gov/account/settings/"
        )
    if args.check:
        accepted, message = check_ncbi_key(root=root)
        print(f"\nkey check: {message}")
        if accepted is False:
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
