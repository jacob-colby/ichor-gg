"""Tests for the per-god damage valuation (B4/B5).

Most of these pin a NEGATIVE result. Both halves of B4 measured worse than the
presence-based fit they were meant to replace, so what needs protecting is that
they stay off and that the measurement stays reproducible.
"""
import pytest

from smite import combat, damage_value as dv, notes, recommend, scoring


def _god(name):
    return notes.read_note(recommend.DATA_ROOT / "Gods" / f"{name}.md")[0]


def _item(name):
    return notes.read_note(recommend.DATA_ROOT / "Items" / f"{name}.md")[0]


# ── The valuation itself ──────────────────────────────────────────────────

def test_a_mage_and_an_assassin_value_opposite_stats():
    """The distinction a role table cannot draw. Scylla's abilities scale off
    Intelligence and Thanatos's off Strength, and the weights say so without
    anyone hand-tuning a table."""
    scylla, thanatos = dv.stat_weights(_god("Scylla")), dv.stat_weights(_god("Thanatos"))
    assert scylla["Intelligence"] > scylla["Strength"] * 2
    assert thanatos["Strength"] > thanatos["Intelligence"] * 5


def test_a_god_whose_kit_did_not_parse_gets_no_fabricated_profile():
    """14 of 87 gods, mostly stance gods whose second form is a page we never
    fetch. An empty dict means "use the role table" — inventing a profile from
    one ability would be worse than admitting the gap."""
    assert dv.stat_weights({"abilities": []}) == {}
    assert dv.stat_weights(_god("Anubis")) == {}          # 0 usable abilities
    assert dv.blend_stat_values({"abilities": []}, {"Strength": 1.0}, 1.0) == {"Strength": 1.0}


def test_only_abilities_with_both_a_rank_and_a_scaling_line_count():
    """A rank list with no scaling would read as a flat nuke no stat improves,
    dragging the god's valuation down for a reason that is an artefact of the
    scrape rather than the kit."""
    god = {"abilities": [
        {"slot": "1st Ability", "name": "both",
         "details": ["Damage: 100 | 200", "Damage Scaling: 80% Strength"]},
        {"slot": "2nd Ability", "name": "rank only", "details": ["Damage: 50"]},
        {"slot": "3rd Ability", "name": "scaling only",
         "details": ["Damage Scaling: 90% Strength"]},
    ]}
    parsed = dv.ability_damage_components(god)
    assert [c["name"] for c in parsed] == ["both"]


def test_the_basic_attack_is_counted_at_the_chains_mean_swing():
    """The chain multipliers apply to swing TIME as well as damage, so the mean
    is the honest per-swing figure — taking the first hit would undercount a
    god whose chain ends on a 1.5x, and the max would overcount every god."""
    thanatos = _god("Thanatos")
    assert combat.attack_chain_multipliers(thanatos) == [1.0, 0.75, 1.5]
    values = dv.marginal_damage_per_stat(thanatos)
    abilities_only = sum(c["scaling"].get("Strength", 0.0)
                         for c in dv.ability_damage_components(thanatos))
    mean = sum([1.0, 0.75, 1.5]) / 3
    assert values["Strength"] == pytest.approx(abilities_only + 1.0 * mean)


# ── B5: damage against a target ───────────────────────────────────────────

def test_penetration_and_power_swap_places_as_the_target_hardens():
    """The whole point of B5, and the thing no per-stat weighting can express:
    the better item depends on who you are hitting. Void Shard is pure
    penetration and is the only item here that gains value against a tank."""
    scylla = _god("Scylla")
    power = _item("Rod of Tahuti")
    pen = _item("Void Shard")
    assert dv.item_damage_gain(scylla, power, 20) > dv.item_damage_gain(scylla, power, 250)
    assert dv.item_damage_gain(scylla, pen, 250) > dv.item_damage_gain(scylla, pen, 20)


def test_damage_gain_is_zero_for_an_unparsed_kit_not_a_guess():
    assert dv.item_damage_gain({"abilities": []}, _item("Rod of Tahuti"), 100) == 0.0


def test_an_item_offering_this_god_nothing_gains_nothing():
    """Thanatos scales off Strength; a pure-Intelligence item adds no damage."""
    gain = dv.item_damage_gain(_god("Thanatos"), _item("Book of Thoth"), 100)
    assert gain == pytest.approx(0.0, abs=1e-9)


# ── The negative result, pinned ───────────────────────────────────────────

def test_both_b4_halves_ship_off():
    """They made the gate worse — 48.4% coverage to 44.9% with magnitude on.
    If someone turns these on, it should be because they re-measured."""
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    assert weights.get("magnitude_fit") is False
    assert weights.get("damage_fit_blend") == 0.0


def test_magnitude_changes_the_fit_when_enabled_at_all():
    """Off by default, but not dead code — with a reference supplied, 5 Strength
    and 80 Strength must stop scoring identically. That equality was the
    original complaint, and it is real; it just wasn't what was hurting us."""
    god = {"name": "T", "damage_type": "physical", "role": "Jungle"}
    weights = scoring.load_weights_default()
    small = {"stats": {"Strength": "5"}}
    large = {"stats": {"Strength": "80"}}
    ref = {"Strength": 60.0}

    assert scoring.god_fit_score(small, god, weights, []) == \
           scoring.god_fit_score(large, god, weights, [])
    assert scoring.god_fit_score(small, god, weights, [], stat_reference=ref) < \
           scoring.god_fit_score(large, god, weights, [], stat_reference=ref)


def test_stat_reference_uses_the_median_not_an_outlier():
    items = [{"name": f"i{i}", "tier": 3, "stats": {"Strength": "40"}} for i in range(5)]
    items.append({"name": "freak", "tier": 3, "stats": {"Strength": "400"}})
    assert scoring.stat_reference(items)["Strength"] == pytest.approx(40)
