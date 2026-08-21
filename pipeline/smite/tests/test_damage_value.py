"""Tests for the per-god damage valuation (B4/B5).

Most of these pin a NEGATIVE result. Both halves of B4 measured worse than the
presence-based fit they were meant to replace, so what needs protecting is that
they stay off and that the measurement stays reproducible.
"""
import pytest

from smite import combat, damage_value as dv, kit, notes, recommend, scoring


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
    """An item carrying no stat this god's kit reads adds nothing.

    Book of Thoth used to be the example and no longer is: Thanatos's ABILITIES
    take nothing from Intelligence, but his scraped basic attack reads
    "100% Strength + 20% Intelligence + 100% Attack Damage", so 30 Intelligence
    really is worth 3.25 damage a swing against 100 protection. That number is
    the mechanic, not a leak — see `item_damage_gain`. A pure-protection item
    is the honest zero."""
    thanatos = _god("Thanatos")
    assert dv.item_damage_gain(thanatos, _item("Breastplate of Valor"),
                               100) == pytest.approx(0.0, abs=1e-9)
    assert dv.item_damage_gain(thanatos, _item("Book of Thoth"), 100) > 0.0


# ── The basic attack is half of a carry's kit, and it counts ──────────────

def test_attack_damage_items_are_worth_something_at_all():
    """The gap this closes. `ability_damage_components` skips the Basic Attack
    slot, so Attack Damage — which 84 of 89 basic attacks take at 100% and no
    ability in the roster scales on — contributed exactly 0.0 to the only
    damage path that reaches a recommendation. 12 items carry it."""
    medusa = _god("Medusa")
    qins = _item("Qin's Blade")          # 30 Attack Damage, 25% Attack Speed
    assert dv._item_stats(qins).get("Attack Damage") == 30.0
    assert dv.item_damage_gain(medusa, qins, 70) > 0.0


def test_critical_chance_is_priced_and_scales_with_level():
    """Crit multiplies the whole swing, base Attack Power included, so it is
    the one term whose value depends on the attacker's level — which is why
    `level` now reaches the arithmetic instead of being accepted and ignored."""
    medusa = _god("Medusa")
    rage = _item("Rage")                 # 30 Strength, 20% Critical Chance
    early = dv.item_damage_gain(medusa, rage, 70, level=1)
    late = dv.item_damage_gain(medusa, rage, 70, level=20)
    assert late > early > 0.0


def test_attack_speed_still_buys_nothing_and_that_is_the_open_half():
    """The honest state after this change. `combat.attacks_per_second` exists
    and is calibrated; nothing calls it, so a pure-attack-speed item is still
    worth exactly zero damage. Odysseus' Bow and The Executioner are both in
    Medusa's community build and both score 0.0 here."""
    medusa = _god("Medusa")
    for name in ("Odysseus' Bow", "The Executioner"):
        assert dv.item_damage_gain(medusa, _item(name), 70) == pytest.approx(0.0, abs=1e-9)


def test_the_swing_is_one_mean_multiplier_hit_not_the_whole_chain():
    """Counting the chain's SUM would hand Thanatos 3.25x the basic-attack
    weight of a single-swing god for a chain that also takes 3.25x as long."""
    thanatos = _god("Thanatos")
    stats = {"Attack Damage": 100.0}
    base, gained = dv._basic_attack_pair(thanatos, stats, 1)
    chain = combat.attack_chain_multipliers(thanatos)
    assert gained - base == pytest.approx(100.0 * (sum(chain) / len(chain)))


# ── The clock, and the negative result it produced ────────────────────────

def test_per_second_is_the_only_setting_that_prices_attack_speed():
    """Odysseus' Bow is 45% Attack Speed and nothing else, and it is in
    Medusa's community build. Per rotation it is worth exactly zero damage;
    per second it is worth something. Same for The Executioner."""
    medusa = _god("Medusa")
    for name in ("Odysseus' Bow", "The Executioner"):
        item = _item(name)
        assert dv.item_damage_gain(medusa, item, 70) == pytest.approx(0.0, abs=1e-9)
        assert dv.item_damage_gain(medusa, item, 70, per_second=True) > 0.0


def test_per_second_is_the_only_setting_that_prices_cooldown_rate():
    """34 items carry Cooldown Rate and it buys no modelled damage anywhere in
    this repo unless the ability channel is on a clock. Held against the same
    item minus its Cooldown Rate, so nothing else can account for the gap."""
    god = {"name": "T", "base_stats": {"attack_speed": {"base": 1.0}},
           "abilities": [{"slot": "1st Ability", "name": "a", "cooldown": [10.0],
                          "details": ["Damage: 100",
                                      "Damage Scaling: 100% Strength"]}]}
    plain = {"stats": {"Strength": "50"}}
    hasted = {"stats": {"Strength": "50", "Cooldown Rate": "25"}}
    assert (dv.item_damage_gain(god, hasted, 0.0)
            == dv.item_damage_gain(god, plain, 0.0))
    assert (dv.item_damage_gain(god, hasted, 0.0, per_second=True)
            > dv.item_damage_gain(god, plain, 0.0, per_second=True))


def test_an_ability_with_no_scraped_cooldown_is_dropped_from_both_sides():
    """241 of 253 damage abilities carry a cooldown. The other 12 are dropped
    rather than imputed — but `before` and `after` must walk the same filtered
    list, or the delta is taken across two different kits."""
    god = {"name": "T", "base_stats": {"attack_speed": {"base": 1.0}},
           "abilities": [
               {"slot": "1st Ability", "name": "timed", "cooldown": [10.0],
                "details": ["Damage: 100", "Damage Scaling: 100% Strength"]},
               {"slot": "2nd Ability", "name": "untimed",
                "details": ["Damage: 100", "Damage Scaling: 100% Strength"]}]}
    stats = {"Strength": 50.0}
    assert len(dv.ability_damage_components(god)) == 2
    assert dv._base_cooldown(god, {"name": "untimed"}) is None
    # 50 Strength through one 10s ability + one 1.0/s swing, no mitigation.
    gain = dv.item_damage_gain(god, {"stats": {"Strength": "50"}}, 0.0,
                               per_second=True)
    assert gain == pytest.approx(50.0 / 10.0 + 50.0 * 1.0)


def test_attack_speed_per_level_is_not_applied():
    """`attack_speed.per_level` reads 1.4 for 49 gods, which cannot be a flat
    rate — 27 swings a second at level 20. "Cannot be anything else" is an
    inference and not a source, and applying it would scale up the channel
    already known to be over-weighted."""
    medusa = _god("Medusa")
    assert medusa["base_stats"]["attack_speed"]["per_level"] == 1.4
    assert dv._base_attack_speed(medusa) == 1.0


def test_the_clock_ships_off():
    """Measured 2026-08-21 and it fails its own pre-registered criterion:
    Carries improve a lot, Mids degrade more, and the roster-wide leakage-free
    B6 diagnostic gets worse. Numbers under `damage_per_second` in
    _weights.yaml. If someone turns this on, it should be because they
    re-measured."""
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    assert weights.get("damage_per_second") is False


# ── The negative result, pinned ───────────────────────────────────────────

def test_both_b4_halves_ship_off():
    """They made the gate worse — 48.4% coverage to 44.9% with magnitude on.
    If someone turns these on, it should be because they re-measured.

    `damage_fit_blend` stays at 0.0 for a different reason now: its gain was
    entirely the Attack Damage column, which `attack_damage_fit` took over.
    What is left of it peaks at 0.30 on the probe split and then falls BELOW
    control (37.7% at full strength, worse on 11 gods against better on 7)."""
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    assert weights.get("magnitude_fit") is False
    assert weights.get("damage_fit_blend") == 0.0


# ── The carve-out, which ships ON ─────────────────────────────────────────

def test_the_fit_map_has_no_attack_damage_column_of_its_own():
    """The hole `attack_damage_fit` exists to fill, asserted at the source
    rather than quoted. Neither the role table nor the kit overlay ever names
    Attack Damage, so every god's merged fit map scores it at exactly 0.0 —
    while their own basic-attack scaling says it is worth real damage."""
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    gods = recommend.load_gods()
    for god in gods:
        base = scoring._role_stat_map(god, weights)
        overlay = kit.kit_stat_overlay(kit.scaling_profile(god), god,
                                       include_off_type=True)
        assert base.get("Attack Damage", 0.0) == 0.0, god["name"]
        assert "Attack Damage" not in overlay, god["name"]

    measured = [g for g in gods
                if dv.stat_weights(g).get("Attack Damage", 0.0) > 0]
    assert len(measured) == 78, len(measured)


def test_attack_damage_fit_credits_the_measured_weight():
    """A pure scale, because the value it blends against is zero — which is
    why the shipped strength is 1.0 rather than an argmax off a flat plateau."""
    medusa = _god("Medusa")
    role_map = {"Attack Speed": 1.3, "Strength": 0.8}
    weight = dv.stat_weights(medusa)["Attack Damage"]

    off = dv.attack_damage_fit(medusa, role_map, 0.0)
    assert off == role_map
    assert "Attack Damage" not in off

    full = dv.attack_damage_fit(medusa, role_map, 1.0)
    assert full["Attack Damage"] == pytest.approx(weight * 1.3)
    half = dv.attack_damage_fit(medusa, role_map, 0.5)
    assert half["Attack Damage"] == pytest.approx(full["Attack Damage"] / 2)
    # Everything else is left exactly alone.
    assert {k: v for k, v in full.items() if k != "Attack Damage"} == role_map


def test_attack_damage_fit_is_silent_on_a_god_it_cannot_measure():
    assert dv.attack_damage_fit({"abilities": []}, {"Strength": 1.0}, 1.0) ==            {"Strength": 1.0}


def test_the_two_halves_do_not_double_count_attack_damage():
    """`blend_stat_values` used to own every offensive stat. Now that the
    Attack Damage column has its own flag, the blend must not also move it —
    with both on, that would apply the same measurement twice."""
    medusa = _god("Medusa")
    role_map = {"Attack Speed": 1.3, "Strength": 0.8}
    blended = dv.blend_stat_values(medusa, role_map, 1.0)
    assert blended.get("Attack Damage", 0.0) == 0.0
    assert blended["Strength"] != role_map["Strength"]     # still a live knob


def test_the_carve_out_ships_on_at_full_strength():
    """Positive on both leakage-free splits at every strength, and the only
    thing in register entry 4 whose paired CI excludes zero (probe 38.7% ->
    40.6%, [+0.34%, +3.52%]; best 39.6% -> 40.5%). Numbers under
    `attack_damage_fit` in _weights.yaml."""
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    assert weights.get("attack_damage_fit") == 1.0


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
