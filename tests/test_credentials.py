"""Tests for credential lookup, and for every place that uses it.

A key is not authentication here - every NCBI endpoint this project touches is
public - it is a rate limit, 3 requests per second without one and 10 with. So
the thing worth testing is not secrecy in the abstract but two concrete things:
that a key set in ONE place is found by EVERY caller, because the failure that
actually happened was a key speeding up `retrieve.py` and none of the scripts;
and that it never reaches a log, because it rides in the query string of a GET
and `requests` copies the full URL into its exception text.
"""

from __future__ import annotations

import contextlib
import importlib.util
import json
import re
import socket
import sys
import threading
import urllib.error
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from types import SimpleNamespace

import pytest

from assaywatch import credentials
from assaywatch.credentials import (
    NCBI,
    check_ncbi_key,
    describe,
    main,
    ncbi_api_key,
    ncbi_interval,
    read_secret,
    scrub,
    with_api_key,
)

ROOT = Path(__file__).resolve().parents[1]
KEY = "k3y-abcdef0123456789-XYZ"


def load_script(name: str):
    spec = importlib.util.spec_from_file_location(f"s_{name}", ROOT / "scripts" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[f"s_{name}"] = mod
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(autouse=True)
def no_ambient_key(monkeypatch, tmp_path):
    """No test here may depend on the key, or key file, of whoever runs it.

    The environment AND the checkout's own `.secrets/` are both hidden: clearing
    only the variables left any developer who had set up .secrets/ncbi.key as
    the documentation says failing tests that expect "no key".
    """
    for var in ("NCBI_API_KEY", "ELSEVIER_API_KEY", "ELSEVIER_INSTTOKEN"):
        monkeypatch.delenv(var, raising=False)
    empty = tmp_path / "hermetic-root"
    empty.mkdir()
    monkeypatch.setattr(credentials, "ROOT", empty)
    monkeypatch.setenv("NO_PROXY", "127.0.0.1,localhost")
    monkeypatch.setenv("no_proxy", "127.0.0.1,localhost")


def secrets_dir(tmp_path: Path) -> Path:
    d = tmp_path / ".secrets"
    d.mkdir(exist_ok=True)
    return d


# --------------------------------------------------------------------------
# Lookup
# --------------------------------------------------------------------------


def test_environment_wins_over_a_key_file(tmp_path, monkeypatch):
    """Deliberate: a cloud session is configured with environment variables, and
    that is the one route where the key never touches a file, a chat window or a
    diff. The mechanism that leaks least should also be the one that wins."""
    (secrets_dir(tmp_path) / "ncbi.key").write_text("from-the-file")
    monkeypatch.setenv("NCBI_API_KEY", "from-the-environment")
    assert ncbi_api_key(root=tmp_path) == "from-the-environment"


def test_falls_back_to_the_key_file(tmp_path):
    (secrets_dir(tmp_path) / "ncbi.key").write_text("from-the-file\n")
    # A trailing newline is what a text editor leaves behind, and it would be
    # sent as part of the key.
    assert ncbi_api_key(root=tmp_path) == "from-the-file"


def test_no_key_anywhere_is_a_normal_state(tmp_path):
    """Most of this project works without a key, so absence must not raise."""
    assert ncbi_api_key(root=tmp_path) == ""
    assert read_secret(NCBI, root=tmp_path) == ""


def test_an_empty_or_whitespace_env_var_counts_as_unset(tmp_path, monkeypatch):
    """`export NCBI_API_KEY=` is how a key gets accidentally blanked, and
    sending `api_key=` is worse than sending nothing."""
    monkeypatch.setenv("NCBI_API_KEY", "   ")
    assert ncbi_api_key(root=tmp_path) == ""
    assert "api_key" not in with_api_key({"db": "taxonomy"}, root=tmp_path)


def test_with_api_key_adds_the_parameter_only_when_there_is_one(tmp_path, monkeypatch):
    assert with_api_key({"db": "taxonomy"}, root=tmp_path) == {"db": "taxonomy"}
    monkeypatch.setenv("NCBI_API_KEY", "abc123")
    assert with_api_key({"db": "taxonomy"}, root=tmp_path) == {"db": "taxonomy", "api_key": "abc123"}


def test_with_api_key_does_not_mutate_its_argument(tmp_path, monkeypatch):
    """Callers reuse one params literal inside a loop."""
    monkeypatch.setenv("NCBI_API_KEY", "abc123")
    params = {"db": "taxonomy"}
    with_api_key(params, root=tmp_path)
    assert params == {"db": "taxonomy"}


def test_the_interval_matches_ncbis_two_published_limits(tmp_path, monkeypatch):
    assert ncbi_interval(root=tmp_path) == 0.34  # 3/s
    monkeypatch.setenv("NCBI_API_KEY", "abc123")
    assert ncbi_interval(root=tmp_path) == 0.11  # 10/s
    # Never zero: NCBI asks callers to stay under the limit rather than discover
    # it, and a blocked IP affects everyone at the institution.
    assert ncbi_interval(root=tmp_path) > 0


def test_a_directory_where_the_key_file_should_be_is_not_a_key(tmp_path):
    (secrets_dir(tmp_path) / "ncbi.key").mkdir()
    assert ncbi_api_key(root=tmp_path) == ""


# --------------------------------------------------------------------------
# A key file that cannot be used
# --------------------------------------------------------------------------


def test_a_utf8_byte_order_mark_is_not_part_of_the_key(tmp_path):
    """Notepad adds one. Sent verbatim it is three bytes of garbage in the key."""
    (secrets_dir(tmp_path) / "ncbi.key").write_bytes(b"\xef\xbb\xbf" + KEY.encode() + b"\r\n")
    assert ncbi_api_key(root=tmp_path) == KEY


def test_powershell_utf16_is_read_not_crashed_on(tmp_path):
    """Windows PowerShell 5's `echo KEY > file` writes UTF-16LE with a BOM. That
    used to raise UnicodeDecodeError, which is a ValueError and not an OSError,
    so the lookup crashed `retrieve.py` and the very command meant to say whether
    the key took."""
    (secrets_dir(tmp_path) / "ncbi.key").write_bytes(b"\xff\xfe" + (KEY + "\r\n").encode("utf-16-le"))
    assert ncbi_api_key(root=tmp_path) == KEY


def test_undecodable_bytes_are_ignored_but_not_silently(tmp_path):
    (secrets_dir(tmp_path) / "ncbi.key").write_bytes(b"\x80\x81\x82\xff\xfe\xfd")
    assert ncbi_api_key(root=tmp_path) == ""  # never stops a run that works without it
    line = describe(NCBI, root=tmp_path)
    assert "exists but" in line and "not valid" in line and "ignored" in line, line


def test_a_two_line_key_file_is_refused_with_a_reason(tmp_path):
    """Which line is the key is a guess, and a wrong guess is sent to NCBI."""
    (secrets_dir(tmp_path) / "ncbi.key").write_text(f"# my key\n{KEY}\n")
    assert ncbi_api_key(root=tmp_path) == ""
    assert "2 non-blank lines" in describe(NCBI, root=tmp_path)


def test_blank_lines_around_the_key_are_fine(tmp_path):
    (secrets_dir(tmp_path) / "ncbi.key").write_text(f"\n\n{KEY}\n\n")
    assert ncbi_api_key(root=tmp_path) == KEY


def test_describe_never_shows_the_key(tmp_path, monkeypatch):
    monkeypatch.setenv("NCBI_API_KEY", KEY)
    line = describe(NCBI, root=tmp_path)
    assert KEY not in line
    assert str(len(KEY)) in line  # the length is shown, the value is not
    monkeypatch.delenv("NCBI_API_KEY")
    assert "not set" in describe(NCBI, root=tmp_path)
    (secrets_dir(tmp_path) / "ncbi.key").write_text(KEY)
    line = describe(NCBI, root=tmp_path)
    assert KEY not in line and "read from .secrets/ncbi.key" in line


# --------------------------------------------------------------------------
# scrub
# --------------------------------------------------------------------------


def test_scrub_removes_the_raw_and_the_url_encoded_key(tmp_path, monkeypatch):
    odd = "ab/cd+ef=gh12345678"
    monkeypatch.setenv("NCBI_API_KEY", odd)
    text = f"400 for url: https://x/efetch?db=t&api_key=ab%2Fcd%2Bef%3Dgh12345678 and again {odd}"
    out = scrub(text, root=tmp_path)
    assert "ab%2Fcd" not in out and odd not in out, out
    assert out.count("[redacted]") == 2


def test_scrub_covers_every_credential_not_just_ncbi(tmp_path, monkeypatch):
    monkeypatch.setenv("ELSEVIER_API_KEY", "elsevier-key-0123456789")
    (secrets_dir(tmp_path) / "elsevier.insttoken").write_text("insttoken-0123456789")
    out = scrub("a elsevier-key-0123456789 b insttoken-0123456789 c", root=tmp_path)
    assert out == "a [redacted] b [redacted] c"


def test_scrub_leaves_text_alone_when_there_is_no_key(tmp_path):
    assert scrub("nothing to hide here", root=tmp_path) == "nothing to hide here"


def test_scrub_does_not_mangle_text_for_a_very_short_value(tmp_path, monkeypatch):
    """No real credential is 3 characters, and replacing 'the' everywhere would
    wreck the message it was meant to protect."""
    monkeypatch.setenv("NCBI_API_KEY", "the")
    assert scrub("the quick fox", root=tmp_path) == "the quick fox"


# --------------------------------------------------------------------------
# The check command
# --------------------------------------------------------------------------


class FakeResponse:
    def __init__(self, body: str, status: int = 200):
        self._body, self.status = body.encode(), status

    def read(self):
        return self._body

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


def test_check_accepts_a_key_ncbi_accepts(tmp_path, monkeypatch):
    monkeypatch.setenv("NCBI_API_KEY", KEY)
    seen = {}

    def fake(url, timeout):
        seen["url"] = url
        return FakeResponse('{"einforesult": {"dblist": ["pubmed"]}}')

    ok, msg = check_ncbi_key(root=tmp_path, urlopen=fake)
    assert ok is True and "accepted" in msg
    assert f"api_key={KEY}" in seen["url"]  # it really did send the key


def test_check_reports_a_rejection_without_echoing_the_key_back(tmp_path, monkeypatch):
    """NCBI's own error body can repeat the key it rejected."""
    monkeypatch.setenv("NCBI_API_KEY", KEY)
    body = json.dumps({"error": f"API key invalid: {KEY}", "api-key": KEY})
    ok, msg = check_ncbi_key(root=tmp_path, urlopen=lambda url, timeout: FakeResponse(body))
    assert ok is False and KEY not in msg and "[redacted]" in msg, msg


def test_check_treats_an_http_error_as_rejection_and_scrubs_it(tmp_path, monkeypatch):
    monkeypatch.setenv("NCBI_API_KEY", KEY)

    def boom(url, timeout):
        raise urllib.error.HTTPError(url, 400, "Bad Request", {}, _Body(f"bad key {KEY}"))

    ok, msg = check_ncbi_key(root=tmp_path, urlopen=boom)
    assert ok is False and "HTTP 400" in msg and KEY not in msg, msg


class _Body:
    def __init__(self, text):
        self._t = text.encode()

    def read(self):
        return self._t

    def close(self):
        pass


def test_check_says_unknown_not_rejected_when_the_network_is_down(tmp_path, monkeypatch):
    """A dead network is not evidence about the key."""
    monkeypatch.setenv("NCBI_API_KEY", KEY)

    def down(url, timeout):
        raise OSError(f"connection refused for {url}")

    ok, msg = check_ncbi_key(root=tmp_path, urlopen=down)
    assert ok is None and KEY not in msg, msg


def test_check_with_no_key_has_nothing_to_check(tmp_path):
    ok, msg = check_ncbi_key(root=tmp_path, urlopen=lambda *a, **k: pytest.fail("must not call out"))
    assert ok is None and "no NCBI key" in msg


def test_main_exit_status_follows_the_check(tmp_path, monkeypatch, capsys):
    monkeypatch.setenv("NCBI_API_KEY", KEY)
    monkeypatch.setattr(credentials, "check_ncbi_key", lambda **k: (False, "NCBI answered HTTP 400"))
    assert main(["--check"], root=tmp_path) == 1
    assert KEY not in capsys.readouterr().out
    monkeypatch.setattr(credentials, "check_ncbi_key", lambda **k: (None, "could not reach NCBI"))
    assert main(["--check"], root=tmp_path) == 0  # unknown is not a failure


# --------------------------------------------------------------------------
# The report names NCBI's published limit
# --------------------------------------------------------------------------


def test_the_report_names_ncbis_published_limit_not_a_derived_rate(capsys, monkeypatch, tmp_path):
    """Regression for a line that read "9 requests/second" on a valid key.

    The interval is deliberately a shade wider than 1/10 s for margin, so
    printing 1/interval understated a working key and looked like a fault.

    Run against a temporary root: this used to call main() with no root, which
    read the checkout's REAL .secrets/ncbi.key, so the keyless half of this test
    failed on any machine whose owner had done the documented setup.
    """
    monkeypatch.setenv("NCBI_API_KEY", "x" * 36)
    main([], root=tmp_path)
    out = capsys.readouterr().out
    assert "10 requests/second with a key" in out, out
    assert "9 requests" not in out, out

    monkeypatch.delenv("NCBI_API_KEY")
    main([], root=tmp_path)
    out = capsys.readouterr().out
    assert "3 requests/second without a key" in out, out


def test_the_keyless_report_ignores_a_real_key_file_in_the_checkout(capsys, monkeypatch, tmp_path):
    """The failure that was found: a developer who followed the setup instructions
    failed their own test suite. A fresh root must hide the checkout's file."""
    (secrets_dir(tmp_path) / "ncbi.key").write_text(KEY)
    main([], root=tmp_path)
    assert "10 requests/second with a key" in capsys.readouterr().out
    other = tmp_path / "elsewhere"
    other.mkdir()
    main([], root=other)
    assert "3 requests/second without a key" in capsys.readouterr().out


# --------------------------------------------------------------------------
# The key never reaches an error message
# --------------------------------------------------------------------------


@contextlib.contextmanager
def serve(status: int, body: bytes = b"slow down"):
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(status)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *a):
            pass

    srv = HTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    try:
        yield f"http://127.0.0.1:{srv.server_port}/entrez"
    finally:
        srv.shutdown()
        srv.server_close()


def refused_url() -> str:
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()  # nothing is listening now
    return f"http://127.0.0.1:{port}/entrez"


def assert_clean(exc: SystemExit):
    assert KEY not in str(exc.value), exc.value
    # `from None`: otherwise the original exception is chained and its traceback,
    # URL and all, is printed beneath ours.
    assert exc.value.__suppress_context__ is True


def test_check_taxids_does_not_print_the_key_on_an_http_error(monkeypatch):
    mod = load_script("check_taxids")
    monkeypatch.setenv("NCBI_API_KEY", KEY)
    with serve(429) as url:
        monkeypatch.setattr(mod, "EFETCH", url)
        with pytest.raises(SystemExit) as e:
            mod.fetch_taxa([9606], "a@b.c")
    assert_clean(e)
    assert "429" in str(e.value)  # still says what went wrong


def test_check_taxids_does_not_print_the_key_on_a_refused_connection(monkeypatch):
    mod = load_script("check_taxids")
    monkeypatch.setenv("NCBI_API_KEY", KEY)
    monkeypatch.setattr(mod, "EFETCH", refused_url())
    with pytest.raises(SystemExit) as e:
        mod.fetch_taxa([9606], "a@b.c")
    assert_clean(e)


def test_resolve_citations_does_not_print_the_key_on_an_http_error(monkeypatch):
    mod = load_script("resolve_citations")
    monkeypatch.setenv("NCBI_API_KEY", KEY)
    with serve(400) as url:
        monkeypatch.setattr(mod, "ESEARCH", url)
        with pytest.raises(SystemExit) as e:
            mod.taxid_lookup("Homo sapiens", "a@b.c")
    assert_clean(e)


def test_resolve_citations_does_not_print_the_key_on_a_refused_connection(monkeypatch):
    mod = load_script("resolve_citations")
    monkeypatch.setenv("NCBI_API_KEY", KEY)
    monkeypatch.setattr(mod, "ESEARCH", refused_url())
    with pytest.raises(SystemExit) as e:
        mod.taxid_lookup("Homo sapiens", "a@b.c")
    assert_clean(e)


# --------------------------------------------------------------------------
# Every caller sends the key
# --------------------------------------------------------------------------


class FakeHTTP:
    """Stands in for requests.get: records what was sent."""

    def __init__(self, text="<TaxaSet/>", payload=None):
        self.calls, self.text, self.payload = [], text, payload

    def __call__(self, url, params=None, **kw):
        self.calls.append(dict(params or {}))
        return SimpleNamespace(
            text=self.text,
            status_code=200,
            raise_for_status=lambda: None,
            json=lambda: self.payload or {"esearchresult": {"idlist": []}},
        )


def test_check_taxids_sends_the_key(monkeypatch):
    mod = load_script("check_taxids")
    fake = FakeHTTP()
    monkeypatch.setattr(mod.requests, "get", fake)
    monkeypatch.setattr(mod.time, "sleep", lambda s: None)
    monkeypatch.setenv("NCBI_API_KEY", KEY)
    mod.fetch_taxa([9606], "a@b.c")
    assert fake.calls[0]["api_key"] == KEY
    monkeypatch.delenv("NCBI_API_KEY")
    mod.fetch_taxa([9606], "a@b.c")
    assert "api_key" not in fake.calls[1]


def test_resolve_citations_sends_the_key(monkeypatch):
    mod = load_script("resolve_citations")
    fake = FakeHTTP()
    monkeypatch.setattr(mod.requests, "get", fake)
    monkeypatch.setenv("NCBI_API_KEY", KEY)
    mod.taxid_lookup("Homo sapiens", "a@b.c")
    assert fake.calls[0]["api_key"] == KEY


def test_check_submission_sends_the_key_and_paces_itself(monkeypatch):
    mod = load_script("check_submission")
    import requests

    fake = FakeHTTP()
    sleeps = []
    monkeypatch.setattr(requests, "get", fake)
    monkeypatch.setattr(mod.time, "sleep", sleeps.append)
    monkeypatch.setenv("NCBI_API_KEY", KEY)
    assay = SimpleNamespace(target=SimpleNamespace(taxid=9606, taxon_name="Homo sapiens"))
    res = SimpleNamespace(add=lambda *a, **k: None)
    mod.check_taxon(assay, res, "a@b.c")
    assert fake.calls[0]["api_key"] == KEY
    assert sleeps == [0.11]  # one request per assay was previously unpaced


def test_check_submission_still_paces_when_the_request_fails(monkeypatch):
    """The sleep is in a finally: a failed request is still a request."""
    mod = load_script("check_submission")
    import requests

    sleeps = []

    def boom(*a, **k):
        raise requests.ConnectionError("down")

    monkeypatch.setattr(requests, "get", boom)
    monkeypatch.setattr(mod.time, "sleep", sleeps.append)
    assay = SimpleNamespace(target=SimpleNamespace(taxid=9606, taxon_name="Homo sapiens"))
    mod.check_taxon(assay, SimpleNamespace(add=lambda *a, **k: None), "a@b.c")
    assert sleeps == [0.34]


def test_master_sheet_sends_the_key(monkeypatch):
    mod = load_script("master_sheet")
    urls = []

    def fake_urlopen(url, timeout=0):
        urls.append(url)
        return FakeResponse("<TaxaSet/>")

    monkeypatch.setattr(mod.urllib.request, "urlopen", fake_urlopen)
    monkeypatch.setattr(mod.time, "sleep", lambda s: None)
    monkeypatch.setenv("NCBI_API_KEY", KEY)
    mod.fetch_taxa([9606], "a@b.c")
    assert f"api_key={KEY}" in urls[0]


def test_the_verifiers_id_conversion_sends_the_key(monkeypatch):
    mod = load_script("verify_oligos_against_paper")
    urls = []
    monkeypatch.setattr(mod, "get", lambda url, timeout=60: urls.append(url) and None)
    monkeypatch.setenv("NCBI_API_KEY", KEY)
    mod.pmcid_for("10.1/x", "a@b.c")
    assert f"api_key={KEY}" in urls[0]


def test_retrieve_resolves_its_key_through_the_shared_helper(tmp_path, monkeypatch):
    """retrieve.py used to read only the environment variable, so the key FILE
    this module offers worked for every script except the pipeline."""
    src = (ROOT / "assaywatch" / "retrieve.py").read_text()
    assert "ncbi_api_key()" in src and 'os.environ.get("NCBI_API_KEY")' not in src


def test_no_ncbi_call_site_can_be_added_without_the_key():
    """Structural guard for the next one. Every file that names an NCBI endpoint
    must either take the key through `credentials` or accept one as an argument.

    This is the failure that actually happened: five scripts called E-utilities
    unkeyed because nothing made adding a call site and forgetting the key fail.
    """
    endpoint = re.compile(
        r"eutils\.ncbi\.nlm\.nih\.gov|ncbi\.nlm\.nih\.gov/pmc/utils/idconv|api\.ncbi\.nlm\.nih\.gov"
    )
    offenders = []
    for path in [*(ROOT / "assaywatch").glob("*.py"), *(ROOT / "scripts").glob("*.py")]:
        if path.name == "credentials.py":
            continue
        text = path.read_text()
        if endpoint.search(text) and not re.search(r"with_api_key|api_key", text):
            offenders.append(path.name)
    assert offenders == [], f"call NCBI without handling an API key: {offenders}"
