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

# The per-script caller tests drive scripts that import `requests`. It is in the `dev`
# extra, so CI runs them; without it they skip rather than fail on an ImportError.
needs_requests = pytest.mark.skipif(
    importlib.util.find_spec("requests") is None, reason="requests not installed"
)


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


@needs_requests
def test_check_taxids_does_not_print_the_key_on_an_http_error(monkeypatch):
    mod = load_script("check_taxids")
    monkeypatch.setenv("NCBI_API_KEY", KEY)
    with serve(429) as url:
        monkeypatch.setattr(mod, "EFETCH", url)
        with pytest.raises(SystemExit) as e:
            mod.fetch_taxa([9606], "a@b.c")
    assert_clean(e)
    assert "429" in str(e.value)  # still says what went wrong


@needs_requests
def test_check_taxids_does_not_print_the_key_on_a_refused_connection(monkeypatch):
    mod = load_script("check_taxids")
    monkeypatch.setenv("NCBI_API_KEY", KEY)
    monkeypatch.setattr(mod, "EFETCH", refused_url())
    with pytest.raises(SystemExit) as e:
        mod.fetch_taxa([9606], "a@b.c")
    assert_clean(e)


@needs_requests
def test_resolve_citations_does_not_print_the_key_on_an_http_error(monkeypatch):
    mod = load_script("resolve_citations")
    monkeypatch.setenv("NCBI_API_KEY", KEY)
    with serve(400) as url:
        monkeypatch.setattr(mod, "ESEARCH", url)
        with pytest.raises(SystemExit) as e:
            mod.taxid_lookup("Homo sapiens", "a@b.c")
    assert_clean(e)


@needs_requests
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


@needs_requests
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


@needs_requests
def test_resolve_citations_sends_the_key(monkeypatch):
    mod = load_script("resolve_citations")
    fake = FakeHTTP()
    monkeypatch.setattr(mod.requests, "get", fake)
    monkeypatch.setenv("NCBI_API_KEY", KEY)
    mod.taxid_lookup("Homo sapiens", "a@b.c")
    assert fake.calls[0]["api_key"] == KEY


@needs_requests
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


@needs_requests
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
    """Structural guard for the next one, checked per FUNCTION rather than per file.

    A function that names an NCBI endpoint (directly, or through a module-level
    constant holding one) must mention a key in the same function. The first version
    of this test only asked that the FILE mention `api_key` somewhere, so an import
    line, a comment, or a second unkeyed call in a file that already used the key all
    satisfied it. This is the failure that actually happened: five scripts called
    E-utilities unkeyed because nothing made adding a call site and forgetting the
    key fail.

    Behaviour is tested separately, in the tests above and the transport tests below:
    this one cannot tell that a key is SENT, only that the function that calls NCBI
    knows keys exist.
    """
    import ast

    endpoint = re.compile(
        r"eutils\.ncbi\.nlm\.nih\.gov|ncbi\.nlm\.nih\.gov/pmc/utils/idconv|api\.ncbi\.nlm\.nih\.gov"
    )
    key_marker = re.compile(r"with_api_key|api_key|ncbi_api_key")
    call_sites, offenders = [], []
    for path in sorted([*(ROOT / "assaywatch").glob("*.py"), *(ROOT / "scripts").glob("*.py")]):
        if path.name == "credentials.py":
            continue
        src = path.read_text()
        tree = ast.parse(src)
        constants = {
            t.id
            for node in tree.body
            if isinstance(node, ast.Assign)
            and isinstance(node.value, ast.Constant)
            and isinstance(node.value.value, str)
            and endpoint.search(node.value.value)
            for t in node.targets
            if isinstance(t, ast.Name)
        }
        for fn in ast.walk(tree):
            if not isinstance(fn, ast.FunctionDef | ast.AsyncFunctionDef):
                continue
            body = ast.get_source_segment(src, fn) or ""
            if endpoint.search(body) or any(re.search(rf"\b{c}\b", body) for c in constants):
                call_sites.append(f"{path.name}:{fn.name}")
                if not key_marker.search(body):
                    offenders.append(f"{path.name}:{fn.name}")
    # Not vacuous: the scan has to actually find the known call sites.
    for known in (
        "retrieve.py:http_transport",
        "assemblies.py:datasets_transport",
        "check_taxids.py:fetch_taxa",
    ):
        assert known in call_sites, (known, call_sites)
    assert offenders == [], f"functions that call NCBI without handling an API key: {offenders}"


# --------------------------------------------------------------------------
# Found by the second review: truncation, other kinds of unusable key, the two
# real pipeline transports, and the sibling scripts the first fix missed.
# --------------------------------------------------------------------------


def _key_windows(key: str, n: int = 6):
    return [key[i : i + n] for i in range(len(key) - n + 1)]


def test_the_check_scrubs_before_it_truncates(tmp_path, monkeypatch):
    """The error body is cut to 200 characters for display. Cutting FIRST can split
    the key across the cut, leaving a prefix that no longer matches the key, so
    `scrub` does not see it and it is printed. Every offset is tried."""
    import io

    monkeypatch.setenv("NCBI_API_KEY", KEY)
    for pad in range(150, 205):
        body = ("x" * pad + f" GET /einfo.fcgi?api_key={KEY} bad request").encode()

        def urlopen(url, timeout=0, _body=body):
            raise urllib.error.HTTPError(url, 400, "Bad Request", {}, io.BytesIO(_body))

        accepted, message = check_ncbi_key(root=tmp_path, urlopen=urlopen)
        assert accepted is False
        leaked = [w for w in _key_windows(KEY) if w in message]
        assert not leaked, (pad, leaked, message[-60:])


def test_a_multi_line_environment_key_is_refused_like_a_multi_line_file(tmp_path, monkeypatch):
    """The environment path had no one-line rule, so a pasted two-line value was
    sent as a header, requests refused it and put the whole value in the error."""
    monkeypatch.setenv("NCBI_API_KEY", f"{KEY}\n# rotated 2026-09")
    assert ncbi_api_key(root=tmp_path) == ""
    assert with_api_key({"db": "x"}, root=tmp_path) == {"db": "x"}
    line = describe(NCBI, root=tmp_path)
    assert "2 non-blank lines" in line and "ignored" in line and KEY not in line, line
    # An unusable environment value falls through to the file, as an unset one does.
    (secrets_dir(tmp_path) / "ncbi.key").write_text("from-the-file\n")
    assert ncbi_api_key(root=tmp_path) == "from-the-file"
    assert "ignored" in describe(NCBI, root=tmp_path)


def test_scrub_still_removes_a_key_that_was_refused_as_multi_line(tmp_path, monkeypatch):
    """Refusing a value must not make its real line printable: the key is on one
    line of the pasted value, and an exception may still carry it."""
    monkeypatch.setenv("NCBI_API_KEY", f"{KEY}\n# a note")
    assert KEY not in scrub(f"error talking to NCBI with {KEY}", root=tmp_path)


@pytest.mark.parametrize(
    "content, fragment",
    [
        ("KEY0123456789abcdef\n".encode("utf-16-le"), "control characters"),  # UTF-16, no BOM
        ("KEY0123456789abcdef\n".encode("utf-16-be"), "control characters"),
        (
            b"\xff\xfe\x00\x00" + "KEY0123456789abcdef\n".encode("utf-32-le"),
            None,
        ),  # UTF-32 WITH a BOM: readable
        (b"", "is empty"),
        (b"\n\n", "is empty"),
        (b"\xef\xbb\xbf", "is empty"),  # a BOM and nothing else
        (b"\xff\xfe\xfd garbage \xc0", "not valid"),
    ],
    ids=["utf16le-no-bom", "utf16be-no-bom", "utf32-with-bom", "empty", "newlines", "bom-only", "garbage"],
)
def test_a_key_file_that_cannot_be_used_says_why_and_is_not_sent(tmp_path, content, fragment):
    (secrets_dir(tmp_path) / "ncbi.key").write_bytes(content)
    value = ncbi_api_key(root=tmp_path)
    line = describe(NCBI, root=tmp_path)
    if fragment is None:
        assert value == "KEY0123456789abcdef" and "read from" in line, (value, line)
        return
    assert value == "", repr(value)
    assert "exists but" in line and fragment in line, line
    assert "\x00" not in line


def test_a_key_path_that_is_a_directory_is_reported_not_called_unset(tmp_path):
    """A Docker bind mount creates a directory where a missing file was mounted."""
    (secrets_dir(tmp_path) / "ncbi.key").mkdir()
    assert ncbi_api_key(root=tmp_path) == ""
    line = describe(NCBI, root=tmp_path)
    assert "exists but cannot be read" in line, line


def test_a_missing_key_file_is_still_just_not_set(tmp_path):
    assert describe(NCBI, root=tmp_path).startswith("NCBI_API_KEY: not set")


def test_every_script_reads_a_key_file_by_the_same_rules(tmp_path):
    """fetch_elsevier had its own read_text().strip(), so the PowerShell UTF-16 file
    the credentials module was fixed for still crashed it, and a Notepad BOM made it
    send a key with an invisible character on the front."""
    mod = load_script("fetch_elsevier")
    clean = "abcdef0123456789abcdef0123456789"
    utf16 = tmp_path / "utf16.key"
    utf16.write_bytes(b"\xff\xfe" + (clean + "\r\n").encode("utf-16-le"))
    bom = tmp_path / "bom.key"
    bom.write_bytes(b"\xef\xbb\xbf" + clean.encode() + b"\n")
    for f in (utf16, bom):
        assert mod.load_secret(f, "ELSEVIER_API_KEY", "elsevier.key") == clean, f.name
    # and it still honours the environment, then the default file
    default = secrets_dir(credentials.ROOT) / "elsevier.key"
    default.write_text("from-the-default-file\n")
    assert mod.load_secret(None, "ELSEVIER_API_KEY", "elsevier.key") == "from-the-default-file"


# ---- the two real pipeline transports -------------------------------------------------


def _stub_requests(monkeypatch, responder):
    """A stand-in `requests` module, installed where the transports import it lazily."""
    import types

    stub = types.ModuleType("requests")

    class RequestException(Exception):  # noqa: N818 - mirrors requests' own name
        pass

    stub.RequestException = RequestException
    calls = []

    def post(url, data=None, timeout=0):
        calls.append({"url": url, "data": dict(data), "headers": {}})
        return responder(calls[-1])

    def get(url, params=None, headers=None, timeout=0):
        calls.append({"url": url, "data": dict(params or {}), "headers": dict(headers or {})})
        return responder(calls[-1])

    stub.post, stub.get = post, get
    monkeypatch.setitem(sys.modules, "requests", stub)
    return calls


def _response(status=200, text="<ok/>"):
    return SimpleNamespace(status_code=status, text=text, content=text.encode())


def _frozen_clock(monkeypatch, module):
    """Sleeps recorded, clock frozen: every call after the first owes the full interval."""
    sleeps = []
    monkeypatch.setattr(module.time, "sleep", sleeps.append)
    monkeypatch.setattr(module.time, "monotonic", lambda: 100.0)
    return sleeps


def test_the_eutilities_transport_sends_the_key_and_waits_the_shared_interval(monkeypatch):
    from assaywatch import retrieve

    calls = _stub_requests(monkeypatch, lambda c: _response())
    sleeps = _frozen_clock(monkeypatch, retrieve)
    monkeypatch.setenv("NCBI_API_KEY", KEY)
    transport = retrieve.http_transport("a@b.c", ncbi_api_key())
    transport("esearch", {"db": "nuccore"})
    transport("esearch", {"db": "nuccore"})
    assert [c["data"].get("api_key") for c in calls] == [KEY, KEY]
    assert sleeps == [ncbi_interval()] == [0.11]  # tied to the shared number, not a copy of it


def test_the_unkeyed_eutilities_transport_sends_no_key_and_waits_longer(monkeypatch):
    from assaywatch import retrieve

    calls = _stub_requests(monkeypatch, lambda c: _response())
    sleeps = _frozen_clock(monkeypatch, retrieve)
    transport = retrieve.http_transport("a@b.c", None)
    transport("esearch", {"db": "nuccore"})
    transport("esearch", {"db": "nuccore"})
    assert all("api_key" not in c["data"] for c in calls)
    assert sleeps == [ncbi_interval()] == [0.34]


def test_the_eutilities_transport_does_not_print_a_key_an_error_body_echoes(monkeypatch):
    from assaywatch import retrieve

    monkeypatch.setenv("NCBI_API_KEY", KEY)
    for status, text in ((400, f'{{"error": "bad", "api-key": "{KEY}"}}'), (400, f"history expired {KEY}")):
        _stub_requests(monkeypatch, lambda c, s=status, t=text: _response(s, t))
        transport = retrieve.http_transport("a@b.c", KEY)
        with pytest.raises((retrieve.RetrievalError, retrieve.HistoryExpired)) as err:
            transport("esearch", {"db": "nuccore"})
        assert KEY not in str(err.value), str(err.value)


def test_a_group_failure_is_printed_without_the_key(monkeypatch, capsys):
    """retrieve.main prints `ERROR taxid/group: ...: {exception}` and Snakemake keeps
    it in .snakemake/log. Driven through main(), over both transports."""
    from assaywatch import retrieve

    monkeypatch.setenv("NCBI_API_KEY", KEY)
    _stub_requests(monkeypatch, lambda c: _response(400, f'{{"api-key": "{KEY}", "error": "invalid"}}'))
    monkeypatch.setattr(retrieve.time, "sleep", lambda s: None)
    retrieve.main([str(ROOT / "registry"), "--taxid", "109871", "--dry-run", "--email", "a@b.c"])
    err = capsys.readouterr().err
    assert "ERROR" in err, "the fixture no longer produces a failing group"
    assert KEY not in err, err


def test_main_scrubs_whatever_a_group_raises_not_only_what_the_transports_raise(monkeypatch, capsys):
    """Defence in depth at the print itself: a corrupt genome zip, malformed XML, a
    library error - none of those pass through a transport's own scrubbing."""
    from assaywatch import retrieve

    monkeypatch.setenv("NCBI_API_KEY", KEY)
    _stub_requests(monkeypatch, lambda c: _response())  # main() builds a transport; keep it hermetic

    def explode(*a, **k):
        raise RuntimeError(f"something broke while using {KEY}")

    from assaywatch import assemblies

    monkeypatch.setattr(retrieve, "retrieve_taxon", explode)
    monkeypatch.setattr(assemblies, "retrieve_assemblies", explode)  # imported inside main
    retrieve.main([str(ROOT / "registry"), "--taxid", "109871", "--dry-run", "--email", "a@b.c"])
    err = capsys.readouterr().err
    assert "ERROR" in err and "something broke" in err
    assert KEY not in err, err


def test_the_datasets_transport_sends_the_key_as_a_header_and_waits(monkeypatch):
    from assaywatch import assemblies

    calls = _stub_requests(monkeypatch, lambda c: _response())
    sleeps = _frozen_clock(monkeypatch, assemblies)
    transport = assemblies.datasets_transport(KEY)
    transport("genome/taxon/1/dataset_report", {}, "text/tab-separated-values")
    transport("genome/taxon/1/dataset_report", {}, "text/tab-separated-values")
    assert [c["headers"].get("api-key") for c in calls] == [KEY, KEY]
    assert sleeps == [0.11]

    calls.clear()
    sleeps.clear()
    unkeyed = assemblies.datasets_transport(None)
    unkeyed("p", {}, "x")
    unkeyed("p", {}, "x")
    assert all("api-key" not in c["headers"] for c in calls)
    assert sleeps == [0.21]  # Datasets allows 5/s unkeyed, a different limit from E-utilities' 3/s


def test_the_datasets_transport_does_not_print_a_key_an_error_body_echoes(monkeypatch):
    from assaywatch import assemblies

    monkeypatch.setenv("NCBI_API_KEY", KEY)
    _stub_requests(monkeypatch, lambda c: _response(400, f'{{"api-key": "{KEY}"}}'))
    monkeypatch.setattr(assemblies.time, "sleep", lambda s: None)
    with pytest.raises(assemblies.AssemblyError) as err:
        assemblies.datasets_transport(KEY)("genome/x", {}, "application/json")
    assert KEY not in str(err.value), str(err.value)


def test_master_sheet_paces_a_failed_chunk_too(monkeypatch):
    """The same defect check_submission had: the sleep was only on the success path,
    so a 429 was followed by the next request at once."""
    mod = load_script("master_sheet")
    sleeps = []

    def boom(url, timeout=0):
        raise urllib.error.HTTPError(url, 429, "Too Many Requests", {}, None)

    monkeypatch.setattr(mod.urllib.request, "urlopen", boom)
    monkeypatch.setattr(mod.time, "sleep", sleeps.append)
    assert mod.fetch_taxa(list(range(1, 151)), "a@b.c") == {}  # three chunks of 50
    assert sleeps == [0.34, 0.34, 0.34]


def test_check_through_the_real_urllib_path_against_a_local_server(tmp_path, monkeypatch):
    """The other check tests inject a fake `urlopen`, so the real HTTP path, including
    how urllib raises on a 4xx and what the body of that exception holds, had never run
    under test. A local server stands in for NCBI: accepted, rejected with an HTML page
    that echoes the request line, and rejected with a JSON error in a 200."""
    monkeypatch.setenv("NCBI_API_KEY", KEY)
    page = lambda pad: ("x" * pad + f" GET /einfo.fcgi?api_key={KEY}").encode()  # noqa: E731

    with serve(200, b'{"einforesult": {"dblist": ["pubmed"]}}') as url:
        monkeypatch.setattr(credentials, "EUTILS_INFO", url)
        accepted, message = check_ncbi_key(root=tmp_path)
        assert accepted is True and "accepted" in message

    for pad in (0, 120, 160, 190):
        with serve(400, page(pad)) as url:
            monkeypatch.setattr(credentials, "EUTILS_INFO", url)
            accepted, message = check_ncbi_key(root=tmp_path)
        assert accepted is False and "HTTP 400" in message, message
        assert not [w for w in _key_windows(KEY) if w in message], (pad, message)

    with serve(200, b'{"error": "API key invalid"}') as url:
        monkeypatch.setattr(credentials, "EUTILS_INFO", url)
        accepted, message = check_ncbi_key(root=tmp_path)
        assert accepted is False and "API key invalid" in message
