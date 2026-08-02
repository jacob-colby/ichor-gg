"""Tests for the damage model.

Where a source published a worked example, that example is the test — a
constant we transcribed correctly is worth less than arithmetic that reproduces
a number somebody else computed.
"""
import pytest

from smite import combat


# ── Mitigation ────────────────────────────────────────────────────────────

def test_mitigation_reproduces_the_published_example():
    """"if an enemy has 100 protections ... 100 / (100 + 100) = 0.5"."""
    assert combat.mitigation(100) == pytest.approx(0.5)
    assert combat.mitigation(0) == pytest.approx(1.0)
    assert combat.mitigation(50) == pytest.approx(2 / 3, rel=1e-3)


def test_effective_health_is_the_same_statement_as_mitigation():
    """The wiki gives EHP; the model uses a multiplier. If those two ever stop
    being inverses, one of them has been edited without the other."""
    for prot in (0, 25, 100, 300):
        assert combat.effective_health(1000, prot) == pytest.approx(
            1000 / combat.mitigation(prot))


def test_protection_debuffs_can_amplify_but_penetration_cannot():
    # A negative protection value is a debuff and does increase damage...
    assert combat.mitigation(-50) > 1.0
    # ...but penetration only ever takes protection to zero.
    assert combat.effective_protection(10, flat_pen=50) == 0.0
    assert combat.damage_dealt(100, 10, flat_pen=50) == pytest.approx(100)


# ── Penetration ───────────────────────────────────────────────────────────

def test_penetration_reproduces_the_published_worked_example():
    """"enemy has 100 protections ... 15% penetration and 10 flat: 15% of 100
    is 15, reducing to 85, then subtract 10, leaving 75"."""
    assert combat.effective_protection(100, flat_pen=10, pct_pen=0.15) == pytest.approx(75)


def test_reductions_apply_before_penetration():
    """Order matters. Percentages alone would not prove it — 100 prot with 10%
    shred and 20% pen is 72 whichever runs first, because they commute. A flat
    term between them is what discriminates: this case gives 54 in the model's
    order and 53 if penetration ran before reduction."""
    # 100 -> (100*0.9 - 10) = 80 -> 80*0.8 = 64 -> -10 flat = 54
    got = combat.effective_protection(100, flat_pen=10, pct_pen=0.20,
                                      flat_reduction=10, pct_reduction=0.10)
    assert got == pytest.approx(54)


def test_penetration_is_capped_and_reductions_are_not():
    # 60 flat penetration is reachable from six items; only 50 applies.
    assert combat.effective_protection(200, flat_pen=60) == pytest.approx(150)
    # 80% is reachable too; only 40% applies.
    assert combat.effective_protection(200, pct_pen=0.80) == pytest.approx(120)
    # Reductions come from abilities, and no source caps them — a cap here
    # would be a rule we invented.
    assert combat.effective_protection(200, flat_reduction=80) == pytest.approx(120)


# ── Crit ──────────────────────────────────────────────────────────────────

def test_deathbringers_passive_lands_exactly_on_double_damage():
    """The corroboration that settled the base multiplier: the wiki says crits
    go from 1.65x to 2x with Deathbringer, and our own scrape of the item reads
    "+35% Critical Strike Damage". If the base constant is ever edited away
    from 1.65 that arithmetic stops being exact, which is the tell."""
    assert combat.CRIT_MULTIPLIER + 0.35 == pytest.approx(2.00)


def test_expected_damage_averages_over_crit_chance():
    raw, prot = 100.0, 0.0
    assert combat.expected_attack_damage(raw, prot, crit_chance=0.0) == pytest.approx(100)
    assert combat.expected_attack_damage(raw, prot, crit_chance=1.0) == pytest.approx(165)
    # 20% crit: 0.8*100 + 0.2*165
    assert combat.expected_attack_damage(raw, prot, crit_chance=0.20) == pytest.approx(113)
    # Out-of-range chance is clamped, not extrapolated.
    assert combat.expected_attack_damage(raw, prot, crit_chance=1.7) == pytest.approx(165)


# ── Plating / Dampening ───────────────────────────────────────────────────

def test_plating_and_dampening_cap_at_35_percent():
    assert combat.flat_reduction_multiplier(10, combat.PLATING_CAP) == pytest.approx(0.90)
    assert combat.flat_reduction_multiplier(35, combat.PLATING_CAP) == pytest.approx(0.65)
    # Stacking past the cap buys nothing — which the gold model currently has
    # no idea about, since it prices every point the same.
    assert combat.flat_reduction_multiplier(80, combat.DAMPENING_CAP) == pytest.approx(0.65)


def test_plating_reduces_attacks_on_top_of_protections():
    # 100 prot halves it; 20 plating takes another 20% off.
    assert combat.damage_dealt(1000, 100, plating=20) == pytest.approx(400)
    # An ability is untouched by Plating.
    assert combat.damage_dealt(1000, 100, dampening=20) == pytest.approx(400)
    assert combat.damage_dealt(1000, 100) == pytest.approx(500)


# ── Damage composition ────────────────────────────────────────────────────

def test_attack_damage_uses_the_gods_own_ratios():
    """84 of 89 gods read 100% Strength + 20% Intelligence + 100% Attack
    Damage, but the ratios are per-god and one god is 60/100/60. Passing the
    god's own scaling has to actually change the answer."""
    stats = {"Strength": 100.0, "Intelligence": 50.0, "Attack Damage": 20.0}
    typical = combat.attack_damage(50, combat.DEFAULT_ATTACK_SCALING, stats)
    assert typical == pytest.approx(50 + 100 + 10 + 20)

    mage_ratios = {"Strength": 0.60, "Intelligence": 1.00, "Attack Damage": 0.60}
    assert combat.attack_damage(50, mage_ratios, stats) == pytest.approx(50 + 60 + 50 + 12)


def test_ability_damage_adds_each_scaling_to_its_own_stat():
    # "Damage: 250" with "Damage Scaling: 85% Strength"
    assert combat.ability_damage(250, {"Strength": 0.85}, {"Strength": 200.0}) == pytest.approx(420)
    # Multi-stat scaling, which 396 abilities carry in some form.
    got = combat.ability_damage(100, {"Strength": 0.80, "Intelligence": 0.55},
                                {"Strength": 100.0, "Intelligence": 100.0})
    assert got == pytest.approx(100 + 80 + 55)


def test_a_stat_the_god_does_not_have_contributes_nothing():
    assert combat.ability_damage(100, {"Intelligence": 0.9}, {}) == pytest.approx(100)


# ── Calibration gate ──────────────────────────────────────────────────────

def test_calibrate_report_measures_error_against_observed_numbers():
    """The gate for the whole workstream. Penetration is inferred, so nothing
    downstream ships until real numbers run through this."""
    report = combat.calibrate_report([
        {"label": "half through 100 prot", "expected": 500.0, "raw": 1000.0, "protection": 100},
        {"label": "same, smaller hit", "expected": 450.0, "raw": 900.0, "protection": 100},
    ])
    assert report["n"] == 2
    assert report["cases"][0]["rel_error"] == pytest.approx(0.0)
    assert report["worst_rel_error"] == pytest.approx(0.0, abs=1e-9)


def test_calibrate_report_surfaces_the_worst_case_not_the_average():
    report = combat.calibrate_report([
        {"expected": 500.0, "raw": 1000.0, "protection": 100},
        {"expected": 250.0, "raw": 1000.0, "protection": 100},   # model says 500
    ])
    assert report["worst_rel_error"] == pytest.approx(1.0)


def test_no_calibration_observations_is_not_a_pass():
    """An empty run must not read as "0% error, model verified"."""
    report = combat.calibrate_report([])
    assert report["n"] == 0
