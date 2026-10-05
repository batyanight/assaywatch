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
accident. Nothing here ever prints or logs a key; `describe` exists so a script
can tell the user whether a key was found without showing it.
"""

from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# (environment variable, filename under .secrets/) per credential.
NCBI = ("NCBI_API_KEY", "ncbi.key")
ELSEVIER = ("ELSEVIER_API_KEY", "elsevier.key")
ELSEVIER_INSTTOKEN = ("ELSEVIER_INSTTOKEN", "elsevier.insttoken")


def read_secret(spec: tuple[str, str], *, root: Path | None = None) -> str:
    """The credential named by `spec`, or "" if it is not set anywhere.

    Never raises and never prints. A missing credential is a normal state - most
    of this project works without any - so the caller decides whether to care.
    """
    env_var, filename = spec
    value = os.environ.get(env_var, "").strip()
    if value:
        return value
    path = (root or ROOT) / ".secrets" / filename
    try:
        return path.read_text().strip()
    except OSError:
        # Missing, unreadable, or a directory. All mean "no key".
        return ""


def ncbi_api_key(*, root: Path | None = None) -> str:
    """The NCBI API key, or "". Raises the E-utilities rate limit 3/s -> 10/s."""
    return read_secret(NCBI, root=root)


def with_api_key(params: dict[str, str], *, root: Path | None = None) -> dict[str, str]:
    """`params` plus `api_key`, when one is set.

    E-utilities takes the key as an ordinary query parameter, so this is the
    whole integration. Returns a copy either way, so a caller can keep reusing
    one params literal in a loop without it accumulating state.
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


def describe(spec: tuple[str, str], *, root: Path | None = None) -> str:
    """A line about whether a credential was found, safe to print.

    Says where it came from and how long it is, never what it is. The length is
    worth showing because the usual failure is a truncated paste or a file with
    a trailing newline and nothing else, and a length tells those apart from a
    key that is simply absent.
    """
    env_var, filename = spec
    if os.environ.get(env_var, "").strip():
        return f"{env_var}: set in the environment ({len(os.environ[env_var].strip())} chars)"
    path = (root or ROOT) / ".secrets" / filename
    value = read_secret(spec, root=root)
    if value:
        return f"{env_var}: read from .secrets/{filename} ({len(value)} chars)"
    return f"{env_var}: not set (looked in ${env_var} and {path})"


def main() -> int:
    """`python -m assaywatch.credentials` - say which credentials are visible.

    The point of a one-command check is that setting a key and finding out
    whether it took should not be the same step as a long run that might fail
    for ten other reasons. Prints lengths and sources, never values.
    """
    print("credentials visible to this checkout:\n")
    for spec in (NCBI, ELSEVIER, ELSEVIER_INSTTOKEN):
        print(f"  {describe(spec)}")
    key = ncbi_api_key()
    # Print NCBI's published limit and the interval separately. Printing the
    # derived rate instead said "9 requests/second" for a perfectly good key -
    # because the interval is deliberately a shade wider than 1/10 s - which
    # reads like the key is underperforming.
    limit = 10 if key else 3
    print(
        f"\nE-utilities: NCBI allows {limit} requests/second "
        f"{'with' if key else 'without'} a key, and this client waits "
        f"{ncbi_interval():.2f}s between calls to stay just inside it."
    )
    if not key:
        print(
            "\nNo NCBI key. Everything still works, 3x slower. To set one:\n"
            "  - in a cloud session, add NCBI_API_KEY to the environment's settings\n"
            "  - locally, write it to .secrets/ncbi.key (gitignored)\n"
            "Get one at https://www.ncbi.nlm.nih.gov/account/settings/"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
