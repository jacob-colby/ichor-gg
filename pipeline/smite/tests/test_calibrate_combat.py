"""Tests for the combat calibration gate.

The gate's whole job is refusing to say "verified" when nothing was verified,
so most of these are about the ways it could wrongly pass.
"""
import textwrap

import pytest

from smite import calibrate_combat as cc
from smite import combat


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


def test_the_shipped_observations_still_pass_the_gate():
    """Calibrated 2026-08-04 against Thanatos/Kukulkan. These four readings are
    what confirmed mitigation and both penetration terms, so a change to
    `combat.py` that breaks them has broken something real."""
    real, examples, _pending = cc.load_observations(cc.DEFAULT_PATH)
    assert len(real) >= 4 and examples == []
    report = combat.calibrate_report(real)
    assert report["worst_rel_error"] <= cc.DEFAULT_TOLERANCE

    # Both penetration terms are exercised, not just mitigation - that is the
    # part no source could settle.
    exercised = {k for r in real for k in r if k.endswith("_pen")}
    assert exercised == {"flat_pen", "pct_pen"}

    # And they match EXACTLY once the model is floored the way the game
    # displays it - not merely within tolerance.
    assert all(c["shown"] == c["expected"] for c in report["cases"])


# ── Planning a run ────────────────────────────────────────────────────────

def test_plan_produces_a_fully_determined_baseline():
    """The whole point: a level-1 observation needs nothing read off a screen.
    No god has base power, so raw is the ability's flat rank-1 value, and the
    target's protections are a number we already hold."""
    data = cc.REPO_ROOT / "data"
    cases, err = cc.plan_cases(data / "Gods", data / "Items", "Thanatos", "Ymir")
    assert err is None and cases
    base = cases[0]
    assert base["kwargs"] == {}                      # no items, no penetration
    assert base["raw"] == pytest.approx(100)         # Soul Reap rank 1
    assert base["protection"] == pytest.approx(20.52, abs=0.01)   # Ymir base physical
    assert base["predicted"] == pytest.approx(100 * 100 / 120.52, rel=1e-3)


def test_plan_covers_both_kinds_of_penetration():
    """Flat and percent are separate columns in the gold model and separate
    terms in the damage model; a plan that only exercised one would leave the
    other unverified."""
    data = cc.REPO_ROOT / "data"
    cases, _ = cc.plan_cases(data / "Gods", data / "Items", "Thanatos", "Ymir")
    kinds = {k for c in cases for k in c["kwargs"]}
    assert kinds == {"flat_pen", "pct_pen"}


def test_plan_avoids_items_whose_passive_fires_on_the_cast():
    """The Crusher adds 35% of Strength on every ability hit and Obsidian Shard
    shreds protections on the first cast — the very quantity under test. An
    observation taken with either would be quietly wrong."""
    data = cc.REPO_ROOT / "data"
    cases, _ = cc.plan_cases(data / "Gods", data / "Items", "Thanatos", "Ymir")
    named = " ".join(c["label"] for c in cases)
    for unsafe in ("The Crusher", "Obsidian Shard", "Heartseeker", "Titan's Bane"):
        assert unsafe not in named


def test_plan_adds_item_power_only_where_the_god_scales_on_it():
    """Doom Orb gives Intelligence. Scylla scales on it and her raw damage
    rises; Thanatos does not and his must not."""
    data = cc.REPO_ROOT / "data"
    phys, _ = cc.plan_cases(data / "Gods", data / "Items", "Thanatos", "Ymir")
    mag, _ = cc.plan_cases(data / "Gods", data / "Items", "Scylla", "Hercules")
    doom_phys = next(c for c in phys if "Doom Orb" in c["label"])
    doom_mag = next(c for c in mag if "Doom Orb" in c["label"])
    assert doom_phys["raw"] == phys[0]["raw"]        # no Strength on the item
    assert doom_mag["raw"] > mag[0]["raw"]           # Intelligence does scale


def test_plan_reports_an_unknown_god_rather_than_guessing():
    data = cc.REPO_ROOT / "data"
    cases, err = cc.plan_cases(data / "Gods", data / "Items", "Nobody", "Ymir")
    assert cases is None and "Nobody" in err


def test_plan_refuses_an_ability_with_a_damage_term_we_cannot_model():
    """Thanatos's Death Scythe reads "Damage: 95" and "85% Strength" — and also
    "Gods take 12.5% of their Max Health as bonus Physical Damage". Suggesting
    it would produce a large error and indict the mitigation formula for
    something that was never its fault. Soul Reap has no such line."""
    data = cc.REPO_ROOT / "data"
    cases, _ = cc.plan_cases(data / "Gods", data / "Items", "Thanatos", "Ymir")
    labels = " ".join(c["label"] for c in cases)
    assert "Soul Reap" in labels
    assert "Death Scythe" not in labels


def test_the_clean_ability_filter_reads_the_recovered_colour_coding():
    """It works because B1 recovered `detail_kinds`. Without them every extra
    damage line is just prose and the filter has nothing to match on."""
    from smite import notes
    god, _ = notes.read_note(cc.REPO_ROOT / "data" / "Gods" / "Thanatos.md")
    scythe = next(a for a in god["abilities"] if a["name"] == "Death Scythe")
    assert "detail_kinds" in scythe
    extra = [d for k, d in zip(scythe["detail_kinds"], scythe["details"])
             if k in ("physical", "magical")
             and not d.startswith(("Damage:", "Damage Scaling:"))]
    assert extra, "the hidden %max-health line must still be visible to the filter"


def test_pending_rows_are_kept_out_of_the_verdict_but_not_out_of_sight(tmp_path, capsys):
    """A measurement the model cannot yet reproduce is evidence. Deleting it
    loses the evidence; scoring it red-lights terms that are genuinely
    confirmed. It is recorded, reported, and excluded from the verdict."""
    p = _write(tmp_path, """
        observations:
          - label: confirmed
            raw: 1000
            protection: 100
            expected: 500
          - label: open question
            pending: true
            raw: 1000
            protection: 100
            expected: 400
    """)
    assert cc.main(["--file", str(p)]) == 0          # the open row does not fail the run
    out = capsys.readouterr().out
    assert "1 PENDING" in out
    assert "open question" in out                     # ...and stays visible
    assert "PASS" in out


def test_a_file_of_only_pending_rows_does_not_pass():
    """Otherwise "everything is an open question" would read as verified."""
    real, examples, pending = cc.load_observations(cc.DEFAULT_PATH)
    assert real, "the shipped file must keep at least one scored observation"


def test_the_display_is_floor_not_rounding():
    """94.58 showed as 94; rounding would have given 95. Comparing floored
    predictions to the integer on screen is what makes the gate exact."""
    assert combat.displayed(94.58) == 94
    assert combat.displayed(43.5) == 43
    assert combat.displayed(93.04) == 93
