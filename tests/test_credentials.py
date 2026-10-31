"""Tests for credential lookup.

A key is not authentication here - every NCBI endpoint this project touches is
public - it is a rate limit, 3 requests per second without one and 10 with. So
the thing worth testing is not security but that a key set in ONE place is
found by EVERY caller, because the failure that actually happened was a key in
the environment speeding up `retrieve.py` and none of the five scripts.
"""

from __future__ import annotations

from assaywatch.credentials import (
    NCBI,
    describe,
    describe_contact,
    ncbi_api_key,
    ncbi_interval,
    read_secret,
    with_api_key,
)


def test_environment_wins_over_a_key_file(tmp_path, monkeypatch):
    """Deliberate: a cloud session is configured with environment variables, and
    that is the one route where the key never touches a file, a chat window or a
    diff. The mechanism that leaks least should also be the one that wins."""
    (tmp_path / ".secrets").mkdir()
    (tmp_path / ".secrets" / "ncbi.key").write_text("from-the-file")
    monkeypatch.setenv("NCBI_API_KEY", "from-the-environment")
    assert ncbi_api_key(root=tmp_path) == "from-the-environment"


def test_falls_back_to_the_key_file(tmp_path, monkeypatch):
    monkeypatch.delenv("NCBI_API_KEY", raising=False)
    (tmp_path / ".secrets").mkdir()
    (tmp_path / ".secrets" / "ncbi.key").write_text("from-the-file\n")
    # A trailing newline is what a text editor leaves behind, and it would be
    # sent as part of the key.
    assert ncbi_api_key(root=tmp_path) == "from-the-file"


def test_no_key_anywhere_is_a_normal_state(tmp_path, monkeypatch):
    """Most of this project works without a key, so absence must not raise."""
    monkeypatch.delenv("NCBI_API_KEY", raising=False)
    assert ncbi_api_key(root=tmp_path) == ""
    assert read_secret(NCBI, root=tmp_path) == ""


def test_an_empty_or_whitespace_env_var_counts_as_unset(tmp_path, monkeypatch):
    """`export NCBI_API_KEY=` is how a key gets accidentally blanked, and
    sending `api_key=` to NCBI is worse than sending nothing."""
    monkeypatch.setenv("NCBI_API_KEY", "   ")
    assert ncbi_api_key(root=tmp_path) == ""
    assert "api_key" not in with_api_key({"db": "taxonomy"}, root=tmp_path)


def test_with_api_key_adds_the_parameter_only_when_there_is_one(tmp_path, monkeypatch):
    monkeypatch.delenv("NCBI_API_KEY", raising=False)
    assert with_api_key({"db": "taxonomy"}, root=tmp_path) == {"db": "taxonomy"}
    monkeypatch.setenv("NCBI_API_KEY", "abc123")
    assert with_api_key({"db": "taxonomy"}, root=tmp_path) == {
        "db": "taxonomy",
        "api_key": "abc123",
    }


def test_with_api_key_does_not_mutate_its_argument(tmp_path, monkeypatch):
    """Callers reuse one params literal inside a loop."""
    monkeypatch.setenv("NCBI_API_KEY", "abc123")
    params = {"db": "taxonomy"}
    with_api_key(params, root=tmp_path)
    assert params == {"db": "taxonomy"}


def test_the_interval_matches_ncbis_two_published_limits(tmp_path, monkeypatch):
    monkeypatch.delenv("NCBI_API_KEY", raising=False)
    assert ncbi_interval(root=tmp_path) == 0.34  # 3/s
    monkeypatch.setenv("NCBI_API_KEY", "abc123")
    assert ncbi_interval(root=tmp_path) == 0.11  # 10/s
    # Never zero: NCBI asks callers to stay under the limit rather than discover
    # it, and a blocked IP affects everyone at the institution.
    assert ncbi_interval(root=tmp_path) > 0


def test_describe_never_shows_the_key(tmp_path, monkeypatch):
    """It exists so a script can report that a key was found without printing it."""
    secret = "s3cr3t-key-value"
    monkeypatch.setenv("NCBI_API_KEY", secret)
    line = describe(NCBI, root=tmp_path)
    assert secret not in line
    assert str(len(secret)) in line  # the length is shown, the value is not
    monkeypatch.delenv("NCBI_API_KEY", raising=False)
    assert "not set" in describe(NCBI, root=tmp_path)


def test_a_directory_where_the_key_file_should_be_is_not_a_key(tmp_path, monkeypatch):
    monkeypatch.delenv("NCBI_API_KEY", raising=False)
    (tmp_path / ".secrets" / "ncbi.key").mkdir(parents=True)
    assert ncbi_api_key(root=tmp_path) == ""


def test_the_report_names_ncbis_published_limit_not_a_derived_rate(capsys, monkeypatch, tmp_path):
    """Regression for a line that read "9 requests/second" on a valid key.

    The interval is deliberately a shade wider than 1/10 s for margin, so
    printing 1/interval understated a working key and looked like a fault.

    `main()` takes no root, so it reads the checkout's own `.secrets/`. The test
    points ROOT at an empty directory: its "no key" half used to fail on any
    machine where the developer had followed the instructions and set a key.
    """
    from assaywatch import credentials
    from assaywatch.credentials import main

    monkeypatch.setattr(credentials, "ROOT", tmp_path)
    monkeypatch.setenv("NCBI_API_KEY", "x" * 36)
    # An explicit argv: main(None) would parse pytest's own sys.argv and exit 2.
    main([])
    out = capsys.readouterr().out
    assert "10 requests/second with a key" in out, out
    assert "9 requests" not in out, out

    monkeypatch.delenv("NCBI_API_KEY", raising=False)
    main([])
    out = capsys.readouterr().out
    assert "3 requests/second without a key" in out, out


# --- the contact address in the one-command report (2026-10-21) --------------
# `python -m assaywatch.credentials` omitted the contact address, yet after the
# Snakefile guard a missing address is the one thing that hard-blocks a run. It
# is in the report now, and unlike a key its VALUE is shown, because it is meant
# to be sent.


def test_contact_line_shows_the_value_from_a_file(tmp_path, monkeypatch):
    monkeypatch.delenv("ASSAYWATCH_EMAIL", raising=False)
    (tmp_path / ".secrets").mkdir()
    (tmp_path / ".secrets" / "email").write_text("lab@example.org\n")
    line = describe_contact(root=tmp_path)
    assert "lab@example.org" in line  # shown, not masked
    assert ".secrets/email" in line


def test_contact_line_shows_the_value_from_the_environment(tmp_path, monkeypatch):
    monkeypatch.setenv("ASSAYWATCH_EMAIL", "env@example.org")
    line = describe_contact(root=tmp_path)
    assert "env@example.org" in line
    assert "ASSAYWATCH_EMAIL" in line


def test_contact_line_says_a_run_will_refuse_when_unset(tmp_path, monkeypatch):
    monkeypatch.delenv("ASSAYWATCH_EMAIL", raising=False)
    line = describe_contact(root=tmp_path)
    assert "NOT SET" in line
    assert "refuse to start" in line  # the consequence, not just the absence


def test_the_report_includes_the_contact_line(tmp_path, monkeypatch, capsys):
    monkeypatch.delenv("ASSAYWATCH_EMAIL", raising=False)
    monkeypatch.delenv("NCBI_API_KEY", raising=False)
    from assaywatch.credentials import main

    main([], root=tmp_path)
    assert "contact address:" in capsys.readouterr().out
