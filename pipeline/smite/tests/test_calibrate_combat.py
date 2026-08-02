"""Tests for the combat calibration gate.

The gate's whole job is refusing to say "verified" when nothing was verified,
so most of these are about the ways it could wrongly pass.
"""
import textwrap

import pytest

from smite import calibrate_combat as cc


def _write(tmp_path, body):
    p = tmp_path / "_combat_observations.yaml"
    p.write_text(textwrap.dedent(body), encoding="utf-8")
    return p


def test_no_observations_fails_rather_than_passing_vacuously(tmp_path, capsys):
    """The failure mode that matters. Zero cases means zero error, and a naive
    gate would call that a pass — reporting the model verified when nobody has
    ever checked it."""
    p = _write(tmp_path, "observations: []\n")
    assert cc.main(["--file", str(p)]) == 1
    assert "UNVERIFIED" in capsys.readouterr().out


def test_a_missing_file_is_also_a_failure(tmp_path, capsys):
    assert cc.main(["--file", str(tmp_path / "nope.yaml")]) == 1
    assert "UNVERIFIED" in capsys.readouterr().out


def test_example_rows_are_not_evidence(tmp_path, capsys):
    """The shipped file carries commented examples. If someone uncomments them
    the gate must not accept made-up numbers as a passing calibration."""
    p = _write(tmp_path, """
        observations:
          - label: made up
            example: true
            raw: 1000
            protection: 100
            expected: 500
    """)
    assert cc.main(["--file", str(p)]) == 1
    out = capsys.readouterr().out
    assert "UNVERIFIED" in out and "placeholders" in out


def test_real_observations_within_tolerance_pass(tmp_path, capsys):
    p = _write(tmp_path, """
        observations:
          - label: no penetration
            raw: 1000
            protection: 100
            expected: 500
          - label: with flat penetration
            raw: 1000
            protection: 100
            flat_pen: 25
            expected: 571.4
    """)
    assert cc.main(["--file", str(p)]) == 0
    assert "PASS" in capsys.readouterr().out


def test_one_bad_case_fails_the_run_even_beside_good_ones(tmp_path, capsys):
    """The verdict is the worst case, not the mean — an average would let a
    single disproved penetration case hide behind clean mitigation cases."""
    p = _write(tmp_path, """
        observations:
          - label: fine
            raw: 1000
            protection: 100
            expected: 500
          - label: penetration is wrong
            raw: 1000
            protection: 100
            pct_pen: 0.2
            expected: 400
    """)
    assert cc.main(["--file", str(p)]) == 1
    out = capsys.readouterr().out
    assert "FAIL" in out
    assert "[ok ]" in out and "[OFF]" in out      # both cases are shown
    assert "penetration block is where to look" in out


def test_tolerance_is_configurable(tmp_path):
    p = _write(tmp_path, """
        observations:
          - label: 5 percent off
            raw: 1000
            protection: 100
            expected: 525
    """)
    assert cc.main(["--file", str(p), "--tolerance", "0.02"]) == 1
    assert cc.main(["--file", str(p), "--tolerance", "0.10"]) == 0


def test_the_shipped_file_parses_and_holds_no_real_observations():
    """It ships empty on purpose; this pins that it stays parseable and that
    nobody has quietly added a row without running the gate."""
    real, examples = cc.load_observations(cc.DEFAULT_PATH)
    assert real == []
    assert examples == []
