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

A key that cannot be used
-------------------------
A missing key is a normal state and means "run unkeyed". A key that is present
but cannot be read as a key is different, and quietly treating it as absent would
leave a user who set one up correctly-looking, running at a third of the speed
with no idea why. So it is still treated as absent - a bad key must never stop a
run that works without it - but `describe` says what is wrong with it. The same
rules apply to the environment variable and to the file, because the way a bad key
hurts is the same: it is sent to NCBI, and the header or URL carrying it ends up in
an error message. Handled: a UTF-8 byte-order mark, and the UTF-16 that Windows
PowerShell 5 writes for `echo KEY > file`. Refused, with a reason: bytes that are
not UTF-8, UTF-16 or UTF-32 text; text containing control characters (what UTF-16
or UTF-32 without a byte-order mark looks like once decoded as UTF-8); more than one
non-blank line, because which line is the key is a guess and a wrong guess is sent
to NCBI; an empty file; and a path that exists but cannot be read, such as a
directory or a file this user may not open.
"""

from __future__ import annotations

import argparse
import codecs
import json
import os
import urllib.error
import urllib.parse
import urllib.request
from collections.abc import Callable
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

# (environment variable, filename under .secrets/) per credential.
NCBI = ("NCBI_API_KEY", "ncbi.key")
ELSEVIER = ("ELSEVIER_API_KEY", "elsevier.key")
ELSEVIER_INSTTOKEN = ("ELSEVIER_INSTTOKEN", "elsevier.insttoken")
ALL = (NCBI, ELSEVIER, ELSEVIER_INSTTOKEN)

# Not a credential - it is meant to be sent - but resolved the same way, and for
# the same reason: it must not be committed. Six scripts used to hardcode a real
# address as an argparse default or inside a User-Agent string, which published
# it in a repo that ships an MIT licence and a CITATION.cff.
CONTACT_EMAIL = ("ASSAYWATCH_EMAIL", "email")

EUTILS_INFO = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/einfo.fcgi"


def _single_line(text: str) -> tuple[str, str]:
    """(value, problem) for the text of a key, wherever it came from.

    Exactly one of the two is non-empty, unless the text is blank, when both are.
    """
    # Control characters first, over the whole text: UTF-16 without a byte-order mark
    # decodes as UTF-8 into letters separated by NULs, and splitting that into lines
    # first would report a nonsense line count instead of the real problem.
    if any((ord(c) < 32 and c not in "\r\n\t") or ord(c) == 127 for c in text):
        return "", (
            "contains control characters (usually UTF-16 or UTF-32 text without a byte-order mark, "
            "which PowerShell writes by default)"
        )
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    if len(lines) > 1:
        return (
            "",
            f"has {len(lines)} non-blank lines; a key holds one line and which is the key is a guess",
        )
    return (lines[0] if lines else ""), ""


def _file_value(path: Path) -> tuple[str, str]:
    """(value, problem) for a key file.

    `value` non-empty: usable. `problem` non-empty: the file exists and cannot be
    used, and says why. Both empty: there is no such file, the ordinary case.
    """
    try:
        raw = path.read_bytes()
    except FileNotFoundError:
        return "", ""
    except OSError as e:
        # A directory (a bind mount that created one), or a file this user may not
        # open. Not the ordinary "no key": someone put something there.
        return "", f"cannot be read ({type(e).__name__}: {e.strerror or e})"
    if raw.startswith((codecs.BOM_UTF32_LE, codecs.BOM_UTF32_BE)):
        encoding = "utf-32"  # tested BEFORE UTF-16: its little-endian BOM starts with UTF-16's
    elif raw.startswith((codecs.BOM_UTF16_LE, codecs.BOM_UTF16_BE)):
        encoding = "utf-16"  # what PowerShell 5's `echo KEY > file` writes
    else:
        encoding = "utf-8-sig"  # also strips a UTF-8 byte-order mark
    try:
        text = raw.decode(encoding)
    except UnicodeDecodeError:
        return "", "is not valid UTF-8, UTF-16 or UTF-32 text"
    value, problem = _single_line(text)
    if not value and not problem:
        return "", "is empty"
    return value, problem


def _env_value(env_var: str) -> tuple[str, str]:
    """(value, problem) for a key in the environment; both empty when unset or blank."""
    return _single_line(os.environ.get(env_var, ""))


def read_secret_file(path: Path) -> str:
    """A key from one file, by the same rules as `read_secret`; "" if unusable."""
    return _file_value(path)[0]


def read_secret(spec: tuple[str, str], *, root: Path | None = None) -> str:
    """The credential named by `spec`, or "" if it is not set anywhere usable.

    Never raises and never prints. A missing or unusable credential is a normal
    state - most of this project works without any - so the caller decides
    whether to care, and `describe` says why one was not used. An unusable
    environment value falls through to the file, as an unset one does.
    """
    env_var, filename = spec
    value = _env_value(env_var)[0]
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


def contact_email(*, root: Path | None = None) -> str:
    """The address to identify this client to NCBI, Crossref and Unpaywall, or "".

    `$ASSAYWATCH_EMAIL`, else `.secrets/email`, by the same rules as a
    credential. NCBI asks for a contact so it can warn a caller before blocking
    an IP, and a blocked IP affects everyone at the institution, so an address
    nobody reads is worse than none - but an address in the repository is worse
    still. The pipeline has always taken it on the command line
    (`--config email=...`); this is the same value for the scripts that used to
    carry one in their source.

    Returns "" rather than raising, as the credential readers do. A caller that
    cannot proceed without one should say so itself: see `require_contact_email`.
    """
    return read_secret(CONTACT_EMAIL, root=root)


def require_contact_email(flag: str = "--email", *, root: Path | None = None) -> str:
    """`contact_email()`, or exit with how to set it. For a script that must send one."""
    email = contact_email(root=root)
    if not email:
        raise SystemExit(
            f"No contact address. Pass {flag}, or set $ASSAYWATCH_EMAIL, or write one line "
            "to .secrets/email. NCBI, Crossref and Unpaywall all ask callers to identify "
            "themselves so they can warn you before blocking the IP."
        )
    return email


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
        # What would be sent, plus every line of a raw environment value even when
        # it was refused as unusable: a pasted two-line value contains the real key
        # on one of its lines, and a refusal must not make that line printable.
        raw = [ln.strip() for ln in os.environ.get(spec[0], "").splitlines()]
        for value in {read_secret(spec, root=root), *raw}:
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
    env_value, env_problem = _env_value(env_var)
    if env_value:
        return f"{env_var}: set in the environment ({len(env_value)} chars)"
    path = (root or ROOT) / ".secrets" / filename
    value, problem = _file_value(path)
    note = f" (${env_var} is set but {env_problem}, so it was ignored)" if env_problem else ""
    if value:
        return f"{env_var}: read from .secrets/{filename} ({len(value)} chars){note}"
    if problem:
        return f"{env_var}: .secrets/{filename} exists but {problem}, so it is being ignored{note}"
    if env_problem:
        return f"{env_var}: ${env_var} is set but {env_problem}, so it is being ignored"
    return f"{env_var}: not set (looked in ${env_var} and {path})"


def describe_contact(*, root: Path | None = None) -> str:
    """A line about the contact address, safe to print WITH its value.

    Unlike a credential, this is meant to be sent (NCBI, Crossref and Unpaywall
    ask callers to identify themselves), so the value is shown rather than
    masked - the usual question is "which address will go out", and hiding it
    answers nothing. It is in this report because after 2026-10-21 a pipeline run
    refuses to start without it (Snakefile `require_contact_email`), so it is the
    one line here whose absence stops work rather than merely slowing it.
    """
    env_var, filename = CONTACT_EMAIL
    env_value, _ = _env_value(env_var)
    if env_value:
        return f"contact address: {env_value} (from ${env_var})"
    path = (root or ROOT) / ".secrets" / filename
    value, problem = _file_value(path)
    if value:
        return f"contact address: {value} (from .secrets/{filename})"
    tail = f"; .secrets/{filename} exists but {problem}" if problem else ""
    return (
        f"contact address: NOT SET - a pipeline run will refuse to start. Set ${env_var} or "
        f"write one line to .secrets/{filename}{tail}"
    )


def check_ncbi_key(
    *, root: Path | None = None, urlopen: Callable[..., Any] = urllib.request.urlopen
) -> tuple[bool | None, str]:
    """Ask NCBI whether it accepts the key: (accepted, message), message scrubbed.

    `accepted` is None when there is no key or the question could not be asked.

    Why this exists: five scripts that used to send no key now send one, and if
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
        # Scrub the whole body and only then cut it: truncating first can split the
        # key across the cut, leaving a prefix that no longer matches and is printed.
        detail = scrub(e.read().decode("utf-8", "replace"), root=root)[:200]
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
    print(f"  {describe_contact(root=root)}")
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
