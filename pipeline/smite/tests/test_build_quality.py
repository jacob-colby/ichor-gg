"""Tests for the build-quality diagnostic.

Most of these pin the worked example: Medusa was computed by hand on
2026-08-21 and the module has to reproduce every figure. The rest pin the four
places the arithmetic is easy to get wrong, the caveat the report must print
before any verdict, and the import boundary that keeps this a diagnostic.
"""
import ast
import inspect
import pathlib
import re

import pytest

from smite import (assemble, build_index, build_quality as bq, combat, efficiency,
                   notes, passives, recommend, scoring)


@pytest.fixture(scope="module")
def items_by_name():
    return {it["name"]: it for it in recommend.load_items()}


def _god(name):
    return notes.read_note(recommend.DATA_ROOT / "Gods" / f"{name}.md")[0]


@pytest.fixture(autouse=True)
def printed_stat_lines():
    """Every test reads printed stat lines, whatever another test left on."""
    before = efficiency.apply_pricing_flags({})
    yield
    efficiency.restore_pricing_flags(before)


MEDUSA_COMMUNITY = ["Tyrfing", "Odysseus' Bow", "Silverbranch Bow", "Riptalon",
                    "The Executioner", "Manchu Bow"]
MEDUSA_OURS = ["Berserker's Shield", "Jotunn's Revenge", "Nimble Ring", "Death Metal",
               "Rod of Tahuti", "Soul Gem"]


# ── The worked example ────────────────────────────────────────────────────

def test_medusa_reproduces_the_hand_computation(items_by_name):
    """Computed by hand on 2026-08-21, before the module existed. Every figure
    to 0.1 — a module that differs has misread one of the four traps below."""
    god = _god("Medusa")
    community = bq.profile(god, MEDUSA_COMMUNITY, items_by_name)
    ours = bq.profile(god, MEDUSA_OURS, items_by_name)

    assert community["cost"] == 13750
    assert ours["cost"] == 15400
    assert community["stats"] == {"Attack Speed %": 133.0, "Attack Damage": 80.0,
                                  "Strength": 25.0, "Penetration %": 20.0,
                                  "Lifesteal %": 7.5}

    expect = [
        (community, 70, 352.8, 35.9, 388.6),
        (community, 170, 233.2, 23.7, 256.9),
        (ours, 70, 242.4, 72.4, 314.8),
        (ours, 170, 150.8, 45.1, 195.9),
    ]
    for prof, prot, basic, ability, total in expect:
        assert prof["basic_dps"][prot] == pytest.approx(basic, abs=0.05)
        assert prof["ability_dps"][prot] == pytest.approx(ability, abs=0.05)
        assert prof["total_dps"][prot] == pytest.approx(total, abs=0.1)


def test_medusa_viper_shot_is_skipped_by_the_shared_parser_not_by_special_case(items_by_name):
    """The hand computation excluded Viper Shot. So does the module — because
    its scaling line reads `Damage Scaling Per Tick:`, which
    `damage_value.ability_damage_components` does not accept, and an ability
    with ranks and no scaling is skipped everywhere. No Medusa-shaped rule."""
    counted, dropped = bq.ability_rotation(_god("Medusa"))
    assert [a["name"] for a in counted] == ["Acid Spray", "Lacerate", "Petrify"]
    assert dropped == []
    code = inspect.getsource(bq).split('"""', 2)[2]   # past the module docstring
    assert "Viper" not in code


def test_medusa_per_1000g_divides_by_the_builds_own_gold(items_by_name):
    ours = bq.profile(_god("Medusa"), MEDUSA_OURS, items_by_name)
    assert ours["per_1000g"]["total_dps"][70] == pytest.approx(314.8 / 15.4, abs=0.05)
    assert ours["per_1000g"]["ehp_physical"] == pytest.approx(ours["ehp_physical"] / 15.4)


# ── The four traps ────────────────────────────────────────────────────────

def test_attack_speed_per_level_is_a_percent():
    """Medusa: 1.0 base at 1.4 per level is 1.266 at level 20, not 27.6."""
    assert bq.base_attack_speed(_god("Medusa"), 20) == pytest.approx(1.266)
    assert bq.base_attack_speed(_god("Medusa"), 1) == pytest.approx(1.0)


def test_attack_power_correction_is_combats_not_reimplemented(items_by_name):
    """0.81 on the base only, never on per-level growth — the module calls
    `combat.god_attack_power` rather than carrying its own copy."""
    god = _god("Medusa")
    prof = bq.profile(god, MEDUSA_COMMUNITY, items_by_name)
    assert prof["attack_power"] == pytest.approx(combat.god_attack_power(god, 20))
    assert prof["attack_power"] == pytest.approx(44.4 * 0.81 + 2.4 * 19)
    assert "ATTACK_POWER_SCALE" not in inspect.getsource(bq).split('"""', 2)[2]


def test_flat_and_percent_penetration_are_never_summed(items_by_name):
    """10 flat and 10% are different goods. Against 170 protection the pair is
    worth (170 x 0.9) - 10 = 143 effective, not 150 (as 20 flat) and not
    136 (as 20%)."""
    god = _god("Medusa")
    flat = {"name": "flat", "cost": 1000, "stats": {"Penetration": "10"}, "tier": 3}
    pct = {"name": "pct", "cost": 1000, "stats": {"Penetration": "10%"}, "tier": 3}
    pool = dict(items_by_name, flat=flat, pct=pct)
    both = bq.profile(god, ["flat", "pct"], pool)
    assert both["stats"] == {"Penetration": 10.0, "Penetration %": 10.0}
    expected_prot = combat.effective_protection(170, flat_pen=10, pct_pen=0.10)
    assert expected_prot == pytest.approx(143.0)
    none = bq.profile(god, [], pool)
    ratio = both["basic_dps"][170] / none["basic_dps"][170]
    assert ratio == pytest.approx(combat.mitigation(143.0) / combat.mitigation(170.0))


def test_a_chain_god_swings_at_the_chains_mean(items_by_name):
    """Thanatos's 1 / 0.75 / 1.5 chain averages 1.0833 per swing; the
    multipliers apply to swing time too, so neither the first hit nor the
    sum is the sustained figure."""
    god = _god("Thanatos")
    prof = bq.profile(god, [], items_by_name)
    assert prof["mean_swing"] == pytest.approx(1.0833, abs=1e-3)
    assert prof["raw_basic"] == pytest.approx(combat.god_attack_power(god, 20) * prof["mean_swing"])


# ── What else the profile has to get right ────────────────────────────────

def test_deathbringer_is_the_one_passive_combat_reads(items_by_name):
    assert bq.crit_multiplier_for(["Deathbringer"]) == pytest.approx(1.85)
    assert bq.crit_multiplier_for(["Death Metal"]) == pytest.approx(1.5)


def test_effective_health_is_level_20_base_plus_items(items_by_name):
    """EHP = HP x (1 + prot/100) off the scraped base at level 20 and the
    build's Max Health / protections — `combat.effective_health`, not a
    reimplementation."""
    god = _god("Medusa")
    prof = bq.profile(god, ["Berserker's Shield"], items_by_name)
    health = 569.48 + 86.48 * 19 + 200
    phys = 18.76 + 2.76 * 19 + 40
    assert prof["health"] == pytest.approx(health)
    assert prof["ehp_physical"] == pytest.approx(combat.effective_health(health, phys))
    assert prof["ehp_magical"] == pytest.approx(combat.effective_health(health, 25.3 + 1.38 * 19))


def test_an_ability_without_a_cooldown_is_dropped_and_named(items_by_name):
    """Never imputed — the same rule `damage_value._base_cooldown` applies."""
    god = {"name": "x", "base_stats": {}, "abilities": [
        {"slot": "1st Ability", "name": "has cd", "cooldown": [10, 8],
         "details": ["Damage: 100 | 200", "Damage Scaling: 50% Strength"]},
        {"slot": "2nd Ability", "name": "line only",
         "details": ["Damage: 50 | 60", "Damage Scaling: 50% Strength",
                     "Cooldown: 20 | 15 seconds"]},
        {"slot": "3rd Ability", "name": "no cd",
         "details": ["Damage: 50 | 60", "Damage Scaling: 50% Strength"]},
    ]}
    counted, dropped = bq.ability_rotation(god)
    assert [(a["name"], a["cooldown"], a["base"]) for a in counted] == [
        ("has cd", 8.0, 200.0), ("line only", 15.0, 60.0)]
    assert dropped == ["no cd"]
    prof = bq.profile(god, [], items_by_name)
    assert prof["dropped"] == ["no cd"]
    assert prof["ability_dps"][70] == pytest.approx(
        combat.damage_dealt(200, 70) / 8 + combat.damage_dealt(60, 70) / 15)


def test_an_unknown_item_raises_rather_than_reading_as_a_weaker_build(items_by_name):
    with pytest.raises(KeyError):
        bq.build_totals(["No Such Item"], items_by_name)


# ── Which builds ──────────────────────────────────────────────────────────

def test_community_core_is_the_first_entry_aspect_or_not():
    """Achilles's first community entry carries `Aspect of Prowess`; it is
    still the one `validate._community_slots` scores against, so it is the
    one compared here."""
    note = recommend.load_build_note("Achilles")
    assert note["builds"][0].get("aspect")
    assert bq.community_core(note)[0] == note["builds"][0]["slot_order"][0]["name"]


def test_suggested_core_takes_the_base_kit_model_entry():
    """The contract is WHICH entry is read, not which items are in it.

    This used to assert `suggested_core(note) == MEDUSA_OURS`, which coupled a
    reader to a hand-computation fixture that only happened to match the
    shipped core; `offmap_efficiency` shipping at 0.55 broke it and the reader
    was fine. Same lesson as the three tests decoupled from refresh-owned data
    in `ab26833` — assert the contract, not the current answer."""
    note = recommend.load_build_note("Medusa")
    model = bq.suggested_core(note)
    raw = [b for b in note["builds"]
           if b.get("source") == "suggested" and b.get("archetype") == "model"
           and not b.get("aspect")]
    assert model == [n if isinstance(n, str) else n.get("name")
                     for n in raw[0]["slot_order"]]
    assert len(model) == 6
    # It reads `model`, never the meta-blended `core`, and they differ here.
    assert bq.suggested_core(note, "core") != model
    # An aspect overlay is not the base kit.
    assert bq.suggested_core({"builds": [
        {"source": "suggested", "archetype": "model", "aspect": "X", "slot_order": ["a"] * 6},
    ]}) == []


def test_a_short_or_unknown_build_is_skipped_not_padded(items_by_name):
    god = _god("Medusa")
    note = {"builds": [
        {"source": "community", "slot_order": [{"name": n} for n in MEDUSA_COMMUNITY[:5]]},
        {"source": "suggested", "archetype": "model", "slot_order": MEDUSA_OURS},
    ]}
    assert bq.compare(god, note, items_by_name) is None
    note["builds"][0]["slot_order"].append({"name": "Not An Item"})
    assert bq.compare(god, note, items_by_name) is None


def test_primary_role_collapses_dual_labels():
    assert bq.primary_role({"role": "Solo Jungle"}) == "Solo"
    assert bq.primary_role({"role": "Carry"}) == "Carry"


# ── Distribution ──────────────────────────────────────────────────────────

def _row(god, role, theirs, mine):
    def prof(v):
        return {"total_dps": {70: v, 170: v}, "per_1000g": {"total_dps": {70: v, 170: v},
                "ehp_physical": v, "ehp_magical": v}, "ehp_physical": v, "ehp_magical": v}
    return {"god": god, "role": role, "primary_role": role.split()[0],
            "community": prof(theirs), "ours": prof(mine)}


def test_distribution_counts_ahead_behind_and_level_as_a_ratio():
    """A ratio, so a 400-DPS Carry and a 150-DPS Support weigh the same; a
    delta inside ±0.5% is level rather than a win by rounding."""
    rows = [_row("a", "Carry", 100, 120), _row("b", "Mid", 100, 80),
            _row("c", "Solo", 100, 100.2), _row("d", "Support", 50, 100)]
    d = bq.distribution(rows, "dps_70")
    assert (d["n"], d["ahead"], d["behind"], d["level"]) == (4, 2, 1, 1)
    assert d["quantiles"][0] == pytest.approx(-20.0)
    assert d["quantiles"][100] == pytest.approx(100.0)
    roles = bq.by_role(rows, "dps_70")
    assert list(roles) == ["Carry", "Mid", "Solo", "Support"]
    assert roles["Support"]["ahead"] == 1


def test_flips_names_gods_whose_sign_changes_between_runs():
    a = [_row("x", "Mid", 100, 110), _row("y", "Mid", 100, 90)]
    b = [_row("x", "Mid", 100, 95), _row("y", "Mid", 100, 90)]
    assert [g for g, _, _ in bq.flips(a, b)] == ["x"]


# ── Judged by role ────────────────────────────────────────────────────────

def _profile(dps, ehp, cost=1000.0, burst=None, ehp_magical=None):
    """A profile complete enough for every objective's maximand.

    `ehp_magical` defaults to `ehp` — the two channels equal — so a test that
    is not about the damage mix reads as it did before the pair existed. A
    test that IS about it passes them apart.
    """
    burst = dps if burst is None else burst
    mag = ehp if ehp_magical is None else ehp_magical
    t = cost / 1000.0
    return {
        "items": [], "cost": cost, "stats": {},
        "total_dps": {70: dps, 170: dps}, "burst": {0: burst, 70: burst, 170: burst},
        "ehp_physical": ehp, "ehp_magical": mag,
        "duel": {"physical": {70: ehp * dps, 170: ehp * dps},
                 "magical": {70: mag * dps, 170: mag * dps}},
        "per_1000g": {"total_dps": {70: dps / t, 170: dps / t},
                      "burst": {0: burst / t, 70: burst / t, 170: burst / t},
                      "ehp_physical": ehp / t, "ehp_magical": mag / t},
    }


def _full_row(god, role, theirs, mine):
    return {"god": god, "role": role, "primary_role": role.split()[0],
            "community": theirs, "ours": mine}


def test_a_duel_score_has_no_per_1000g_twin():
    """EHP x DPS already carries the build's gold in both factors; dividing it
    again is not a quantity, so asking raises rather than returning a number
    nobody could interpret."""
    p = _profile(100.0, 3000.0)
    assert bq.metric(p, "duel_physical_70") == pytest.approx(300_000.0)
    with pytest.raises(KeyError, match="no per-1000g twin"):
        bq.metric(p, "duel_physical_70/1000g")


def test_a_duel_score_has_to_name_the_opponents_damage_channel():
    """Its EHP factor is effective health against the reference opponent, so
    an unqualified `duel_70` is a question with two answers. It raises rather
    than quietly returning the physical one, which is what it did until
    2026-08-23."""
    p = _profile(100.0, 3000.0, ehp_magical=1500.0)
    assert bq.metric(p, "duel_physical_70") == pytest.approx(300_000.0)
    assert bq.metric(p, "duel_magical_70") == pytest.approx(150_000.0)
    with pytest.raises(KeyError, match="name the opponent's damage"):
        bq.metric(p, "duel_70")


def test_the_duel_score_is_neutral_when_a_build_trades_ehp_for_damage():
    """The Solo objective's whole point, and the case neither scalar
    describes: double the effective health, halve the damage, score 1.00. The
    reference opponent cancels in ours-over-theirs, so no constant chooses
    this — the algebra does."""
    theirs, mine = _profile(100.0, 3000.0), _profile(50.0, 6000.0)
    assert bq.metric(mine, "duel_physical_70") == pytest.approx(
        bq.metric(theirs, "duel_physical_70"))
    d = bq.distribution([_full_row("g", "Solo", theirs, mine)], "duel_physical_70")
    assert (d["ahead"], d["behind"], d["level"]) == (0, 0, 1)


def test_every_role_objective_names_a_threshold_and_a_maximand():
    """The section exists so a reader can disagree with the CHOICE rather than
    only with the number, which requires every verdict to state both."""
    rows = [_full_row(f"g{i}", role, _profile(100.0, 3000.0), _profile(110.0, 3000.0))
            for i, role in enumerate(bq.ROLE_ORDER)]
    verdicts = bq.role_verdicts(rows)
    assert [v["role"] for v in verdicts] == list(bq.ROLE_ORDER)
    for v in verdicts:
        assert v["maximise"], v["role"]
        assert v["because"], v["role"]
        assert "threshold" in v
    assert bq.ROLE_OBJECTIVES["Solo"]["maximise"][0] == ("duel_physical_70",
                                                         "duel_magical_70")
    # Support scores no damage at all — excluded, not down-weighted.
    assert all("ehp" in key and "dps" not in key and "burst" not in key
               for key in bq.ROLE_OBJECTIVES["Support"]["maximise"][0])


def test_the_duel_score_is_not_applied_outside_solo():
    """It pays full price for effective health, which is correct for a duel
    and is exactly the defect the role split exists to expose on a Carry. A
    metric that hides what it was built to find is worse than the pooled one."""
    assert all(k.startswith("duel_") for k in bq.ROLE_OBJECTIVES["Solo"]["maximise"][0])
    for role, objective in bq.ROLE_OBJECTIVES.items():
        if role != "Solo":
            assert not any(k.startswith("duel") for k in objective["maximise"][0]), role


# ── Both effective-health channels ────────────────────────────────────────

def test_every_objective_with_an_ehp_term_names_both_channels():
    """The defect this pair exists to fix: Solo's duel score and Support's
    effective health per 1000g both read `ehp_physical` alone until
    2026-08-23, so the two roles whose job is durability were scored on half
    the damage in the game. A future objective that grows an EHP term has to
    carry both channels too, which is what this asserts rather than the two
    names."""
    for role, objective in bq.ROLE_OBJECTIVES.items():
        keys = objective["maximise"][0]
        assert isinstance(keys, tuple) and keys, role
        if any("ehp" in k or k.startswith("duel") for k in keys):
            channels = [c for _, c in bq.EHP_CHANNELS]
            assert len(keys) == len(channels), role
            for key, channel in zip(keys, channels):
                assert channel in key, (role, key)
        else:
            assert len(keys) == 1, role


def test_a_mixed_stream_lands_between_the_two_channels():
    """The whole reason the pair is an ANSWER and not a hedge. Effective health
    against a stream that is a share f physical is the weighted HARMONIC mean
    of the two channels, and the ours-over-theirs ratio of two such is monotone
    in f — so no damage mix can score outside the interval the report prints,
    and checking the endpoints is checking everything."""
    def mixed(phys, mag, f):
        return 1.0 / (f / phys + (1 - f) / mag)

    ours, theirs = (4000.0, 2500.0), (3000.0, 3600.0)
    ends = [mixed(*ours, f) / mixed(*theirs, f) for f in (0.0, 1.0)]
    lo, hi = min(ends), max(ends)
    rising = ends[1] >= ends[0]
    previous = None
    for f in (0.0, 0.2, 0.4, 0.5, 0.6, 0.8, 1.0):
        r = mixed(*ours, f) / mixed(*theirs, f)
        assert lo - 1e-9 <= r <= hi + 1e-9, f
        if previous is not None:
            assert (r >= previous - 1e-9) if rising else (r <= previous + 1e-9), f
        previous = r
    # And the arithmetic mean is not the f=0.5 answer it is mistaken for.
    arithmetic = sum(ours) / sum(theirs)
    assert arithmetic != pytest.approx(mixed(*ours, 0.5) / mixed(*theirs, 0.5))
    assert lo <= arithmetic <= hi


def test_channel_verdict_is_a_property_of_the_whole_interval():
    """`ahead` means ahead at EVERY mix, so one endpoint inside the dead band
    is not ahead. `mix` is not a tie — it is the report having no answer."""
    assert bq.channel_verdict([+5.0, +5.0]) == "ahead"
    assert bq.channel_verdict([-5.0, -5.0]) == "behind"
    assert bq.channel_verdict([+30.0, -30.0]) == "mix"
    assert bq.channel_verdict([-30.0, +30.0]) == "mix"
    assert bq.channel_verdict([+5.0, +0.1]) == "level"     # interval meets the band
    assert bq.channel_verdict([-5.0, -0.1]) == "level"
    assert bq.channel_verdict([+0.1, -0.1]) == "level"
    assert bq.channel_verdict([+5.0]) == "ahead"           # a single-channel objective
    assert bq.channel_verdict([float("nan"), +5.0]) == "ahead"
    assert bq.channel_verdict([float("nan")]) == "level"


def test_a_build_ahead_on_one_channel_and_behind_on_the_other_is_neither():
    """The counted case. Ours buys physical protection, theirs magical: it is
    a large win against one enemy team and a large loss against the other, and
    the honest verdict is that this comparison does not name the enemy team."""
    theirs = _profile(100.0, 3000.0, ehp_magical=6000.0)
    mine = _profile(100.0, 6000.0, ehp_magical=3000.0)
    rows = [_full_row("g", "Support", theirs, mine)]
    v = bq.role_verdict(rows, "Support", bq.ROLE_OBJECTIVES["Support"])
    assert (v["ahead"], v["behind"], v["level"], v["mix"]) == (0, 0, 0, 1)
    assert v["n"] == 1
    assert [g for _, g, _ in bq.mix_dependent_builds(rows, [v])] == ["g"]
    # Both ends are printed and neither is averaged away.
    assert bq.median_span(v) == "-50.0% … +100.0%"


def test_the_report_names_every_mix_dependent_build():
    """A count alone reads as a rounding error; these are the builds where the
    report has no answer at all, so it names them. An empty list is the
    measurement, which the other branch asserts."""
    theirs = _profile(100.0, 3000.0, ehp_magical=6000.0)
    mine = _profile(100.0, 6000.0, ehp_magical=3000.0)
    rows = [_full_row("Disputed", "Support", theirs, mine)]
    text = "\n".join(bq.role_verdict_lines(rows, bq.threshold_probe(rows)))
    assert "mix-dependent" in text
    assert "**Disputed** (Support)" in text
    assert "vs a physical opponent +100.0%" in text
    assert "vs a magical opponent -50.0%" in text

    agreed = [_full_row("Agreed", "Support", _profile(100.0, 3000.0),
                        _profile(100.0, 3300.0))]
    text = "\n".join(bq.role_verdict_lines(agreed, bq.threshold_probe(agreed)))
    assert "every build's verdict holds at every damage mix" in text


def test_a_role_with_no_ehp_term_cannot_be_mix_dependent():
    """Printing a 0 there would read as a measurement rather than as 'not
    applicable' — three of the five roles maximise a pure damage quantity,
    whose channel is determined by the god doing the damage."""
    rows = [_full_row("m", "Mid", _profile(100.0, 3000.0), _profile(110.0, 3000.0))]
    verdicts = bq.role_verdicts(rows)
    text = "\n".join(bq._verdict_table(verdicts, bq.threshold_probe(rows)))
    assert "– (no EHP term)" in text
    assert len(next(v for v in verdicts if v["role"] == "Mid")["keys"]) == 1


def test_a_threshold_reads_the_channel_its_named_attacker_deals():
    """The other half of the rule and the reason the thresholds keep ONE
    channel: a threshold names its attacker, so the channel is derived from
    that attacker's `damage_type` instead of picked. Hard-coded to
    `ehp_magical` until 2026-08-23 — right by coincidence for the Carry floor
    and wrong for a physical burster."""
    assert bq.ehp_against("physical")({"ehp_physical": 1.0, "ehp_magical": 9.0}) == 1.0
    assert bq.ehp_against("magical")({"ehp_physical": 1.0, "ehp_magical": 9.0}) == 9.0
    # An unlabelled attacker reads the SMALLER channel: a floor on the worse
    # case is still a floor, and inventing a damage type would not be.
    assert bq.ehp_against(None)({"ehp_physical": 1.0, "ehp_magical": 9.0}) == 1.0

    def carry(name, damage_type, phys, mag, burst):
        row = _full_row(name, "Carry", _profile(100.0, phys, ehp_magical=mag, burst=burst),
                        _profile(100.0, phys, ehp_magical=mag, burst=burst))
        row["damage_type"] = damage_type
        return row

    # The roster's largest burst belongs to the physical god, so the floor is
    # read on physical effective health and separates the build that is thin
    # there — which the magical reading would have missed entirely.
    rows = [carry("burster", "physical", 5000.0, 5000.0, 4000.0),
            carry("thin", "magical", 1000.0, 9000.0, 10.0)]
    probe = bq.threshold_probe(rows)["carry_survival"]
    assert probe["channel"] == "physical"
    assert (probe["n"], probe["failed"]) == (4, 2)


def test_the_kill_thresholds_reference_follows_each_attacker():
    """Its reference is a squishy's effective health, and which channel that
    squishy is read on is decided by the attacker's damage type — one
    reference per channel, never one averaged reference nobody is measured
    against."""
    def mid(name, damage_type, burst):
        row = _full_row(name, "Mid", _profile(100.0, 2000.0, ehp_magical=8000.0, burst=burst),
                        _profile(100.0, 2000.0, ehp_magical=8000.0, burst=burst))
        row["damage_type"] = damage_type
        return row

    rows = [mid("phys", "physical", 3000.0), mid("mag", "magical", 3000.0)]
    kill = bq.threshold_probe(rows)["kill_threshold"]
    # Reference is the median community EHP on each channel: 2000 physical,
    # 8000 magical. A 3000 burst clears the first and fails the second.
    assert kill["reference"] == (2000.0, 8000.0)
    assert (kill["n"], kill["failed"]) == (4, 2)


def test_a_role_with_no_recorded_objective_is_named_not_given_someone_elses():
    rows = [_full_row("g", "Adjacent", _profile(100.0, 3000.0), _profile(110.0, 3000.0))]
    verdict = next(v for v in bq.role_verdicts(rows) if v["role"] == "Adjacent")
    assert verdict["maximise"] is None and verdict["n"] == 1


def test_threshold_probe_reports_a_threshold_that_separates_nobody():
    """Both proposed thresholds are one-sided under this arithmetic, and the
    probe has to say WHICH way and by how much — a threshold nobody fails and
    one everybody fails are equally useless, and only `nearest` distinguishes
    a near miss from an order of magnitude."""
    rows = [_full_row("c", "Carry", _profile(100.0, 3000.0, burst=10.0),
                      _profile(100.0, 3000.0, burst=10.0)),
            _full_row("m", "Mid", _profile(100.0, 3000.0, burst=10.0),
                      _profile(100.0, 3000.0, burst=10.0))]
    probe = bq.threshold_probe(rows)
    carry, kill = probe["carry_survival"], probe["kill_threshold"]
    # One god per population, both sides of each: the Carry floor is measured
    # over Carries, the kill threshold over Mid and Jungle.
    assert (carry["n"], carry["failed"]) == (2, 0)       # 3000 EHP vs a 10 burst
    assert (kill["n"], kill["failed"]) == (2, 2)         # a 10 burst vs 3000 EHP
    assert carry["nearest"] == pytest.approx(300.0)
    assert kill["nearest"] == pytest.approx(10.0 / 3000.0)


def test_threshold_probe_would_report_a_threshold_that_does_bind():
    """It is a measurement, not a constant — on data where the burst reaches
    the health bar it prints a binding threshold instead of the standing one.
    Without this the report's "separates 0 of n" could never change."""
    rows = [_full_row("weak", "Carry", _profile(100.0, 500.0, burst=1000.0),
                      _profile(100.0, 4000.0, burst=1000.0))]
    carry = bq.threshold_probe(rows)["carry_survival"]
    assert (carry["n"], carry["failed"]) == (2, 1)
    assert carry["reference"] == pytest.approx(1000.0)


def test_the_report_says_the_role_split_does_not_escape_the_blind_spot(
        tmp_path, items_by_name):
    """Per-role numbers must not read as though slicing the data got out from
    under the ~90% of the pool this arithmetic cannot price."""
    god = _god("Medusa")
    note = recommend.load_build_note("Medusa")
    row = bq.compare(god, note, items_by_name)
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    blind = bq.passive_blind_spot(recommend.load_items(), [god], {"Medusa": note}, weights)
    out = tmp_path / "report.md"
    bq.write_report([row], [], [row], [], [row], [], blind, "abc123", out,
                    items_by_name=items_by_name)
    text = out.read_text(encoding="utf-8")
    section = text[text.index("## 3. Judged by role"):text.index("## 4.")]
    assert "slicing by role does not escape it" in section
    assert "we cannot currently evaluate a threshold" in section
    # What is unmeasurable is named, not implied.
    for phrase in bq.UNMEASURABLE:
        assert phrase in text, phrase
    # The Carry mechanism section is present in whichever of its two branches
    # the measurement selects, and says which. Asserting the OPEN branch (or
    # the item that used to drive it) would make this test fail the moment the
    # defect is fixed, which is what happened at `offmap_efficiency` 0.55.
    assert ("recorded, not acted on" in section) ^ ("currently closed" in section)
    assert "Mean defensive stats bought at level 20" in section
    assert "excluded as causes" in section


def _carry_row(name, prot, items, theirs_prot=0.0, theirs_items=()):
    theirs, mine = _profile(100.0, 3000.0), _profile(100.0, 3000.0)
    theirs["stats"] = {"Physical Protection": theirs_prot}
    mine["stats"] = {"Physical Protection": prot}
    theirs["items"] = list(theirs_items)
    mine["items"] = list(items)
    return _full_row(name, "Carry", theirs, mine)


def _carry_text(rows, items_by_name):
    return "\n".join(bq.carry_mechanism_lines(rows, items_by_name))


def test_the_carry_section_reports_an_open_surplus_as_open(items_by_name):
    """The branch this section was written for: we buy protection the
    community does not, so it names the items and says it is not acted on."""
    rows = [_carry_row("g1", 40.0, ["Berserker's Shield"]),
            _carry_row("g2", 40.0, ["Berserker's Shield"])]
    text = _carry_text(rows, items_by_name)
    assert "recorded, not acted on" in text
    assert "Berserker's Shield" in text
    assert "currently closed" not in text


def test_the_carry_section_reports_a_closed_surplus_as_closed(items_by_name):
    """And the branch `offmap_efficiency` at 0.55 put it in. A section that
    keeps reading as a live defect after the defect is gone is a stale doc
    with a measurement attached, which is the thing this module exists to
    avoid — so the prose is chosen by the number, not by hand."""
    rows = [_carry_row("g1", 0.0, ["Deathbringer"]),
            _carry_row("g2", 0.0, ["Deathbringer"])]
    text = _carry_text(rows, items_by_name)
    assert "currently closed" in text
    assert "recorded, not acted on" not in text
    # The measurement is still printed, and an empty driver list SAYS so
    # rather than rendering as a missing section.
    assert "Mean defensive stats bought at level 20" in text
    assert "no item carrying a defensive stat holds a Carry core slot" in text
    assert "excluded as causes" in text


def test_the_carry_section_switches_branch_on_the_measurement_alone(items_by_name):
    """One point of mean protection either side of `SURPLUS_EPSILON` flips it,
    so the branch cannot drift away from what it is reporting."""
    closed = [_carry_row("g", 0.0, ["Deathbringer"])]
    opened = [_carry_row("g", 1.0, ["Deathbringer"])]
    assert "currently closed" in _carry_text(closed, items_by_name)
    assert "recorded, not acted on" in _carry_text(opened, items_by_name)




# ── The blind spot ────────────────────────────────────────────────────────

def test_blind_means_passive_text_the_pricing_flags_do_not_read():
    """Deathbringer's passive is priced (crit multiplier), so it is not blind;
    an item with passive prose and no priced grant is; an item with no passive
    is not, whatever the flags say."""
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    items = [
        {"name": "Deathbringer", "tier": 3, "cost": 2900,
         "stats": {"Strength": "45", "Critical Chance": "20%"},
         "passive": "+35% Critical Strike Damage."},
        {"name": "Prose", "tier": 3, "cost": 2500, "stats": {"Strength": "40"},
         "passive": "On hit: something the model cannot read."},
        {"name": "Plain", "tier": 3, "cost": 2000, "stats": {"Strength": "30"}, "passive": ""},
    ]
    gods = [{"name": "g"}]
    builds = {"g": {"builds": [
        {"source": "community", "slot_order": [{"name": "Prose"}, {"name": "Plain"}]},
        {"source": "suggested", "archetype": "model", "slot_order": ["Deathbringer"]},
    ]}}
    blind = bq.passive_blind_spot(items, gods, builds, weights)
    assert blind["buildable"] == 3 and blind["with_passive"] == 2
    assert blind["priced"] == ["Deathbringer"]
    assert blind["blind"] == 1
    assert blind["community"]["blind"] == 1 and blind["community"]["slots"] == 2
    assert blind["community"]["top_blind"] == [("Prose", 1)]
    assert blind["ours"]["blind"] == 0
    assert efficiency.PRICE_ADAPTIVE is False   # flags put back afterwards


def test_the_real_pool_is_mostly_blind():
    """The fact the caveat exists for. Pinned loosely — the exact share moves
    with the item set — but a pool that reads as mostly visible means the
    definition broke, not that passives got priced."""
    items = recommend.load_items()
    gods = recommend.load_gods()
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    builds = {g["name"]: recommend.load_build_note(g["name"]) for g in gods}
    blind = bq.passive_blind_spot(items, gods, builds, weights)
    assert blind["blind_share"] > 0.8
    assert blind["community"]["share"] > 0.6
    assert "Deathbringer" in blind["priced"]


# ── The report ────────────────────────────────────────────────────────────

def test_the_report_states_the_caveat_before_any_verdict(tmp_path, items_by_name):
    """A report that states a winner without the blind spot is worse than no
    report. The caveat and every assumption have to precede the first table.

    The worked-example DPS row and the gold-cost row are read off `row`
    itself rather than hand-copied, because the community build note is live
    data the daily refresh can and does change (it moved Medusa's community
    core between Riptalon and Deathbringer under this exact test) — the
    invariant under test is the ORDERING of caveat before figures, not what
    Medusa's build happens to be today."""
    god = _god("Medusa")
    note = recommend.load_build_note("Medusa")
    row = bq.compare(god, note, items_by_name)
    assert row is not None, "fixture drifted: Medusa no longer has a full community + suggested core"
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    blind = bq.passive_blind_spot(recommend.load_items(), [god], {"Medusa": note}, weights)
    out = tmp_path / "report.md"
    bq.write_report([row], [], [row], [], [row], [], blind, "abc123", out)
    text = out.read_text(encoding="utf-8")
    first_table = text.index("\n|")
    caveat = text.index("READ THIS BEFORE ANY NUMBER BELOW")
    assert caveat < first_table
    for phrase in ("cannot see", "verdict in our favour is the one to distrust",
                   "full ability uptime", "no relic", "single target",
                   "no lifesteal sustain", "no crowd control", "no wave clear"):
        assert phrase in text[:first_table], phrase
    assert "Input fingerprint: `abc123`" in text

    c = row["community"]
    community_line = (f"| COMMUNITY vs squishy (70) | {c['basic_dps'][70]:.1f} | "
                      f"{c['ability_dps'][70]:.1f} | **{c['total_dps'][70]:.1f}** | "
                      f"{c['ehp_physical']:,.0f} | {c['ehp_magical']:,.0f} |")
    cost_line = (f"| {row['god']} | {row['role']} | "
                f"{row['community']['cost']:,.0f} / {row['ours']['cost']:,.0f} |")
    assert community_line in text
    assert cost_line in text


def test_the_report_is_deterministic(tmp_path, items_by_name):
    """Like `_calibration.md`: byte-identical on the same inputs, so its diff
    is a record of what a commit did to the builds."""
    god = _god("Medusa")
    note = recommend.load_build_note("Medusa")
    row = bq.compare(god, note, items_by_name)
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    blind = bq.passive_blind_spot(recommend.load_items(), [god], {"Medusa": note}, weights)
    a, b = tmp_path / "a.md", tmp_path / "b.md"
    bq.write_report([row], [], [row], [], [row], [], blind, "f", a)
    bq.write_report([row], [], [row], [], [row], [], blind, "f", b)
    assert a.read_bytes() == b.read_bytes()


def test_priced_run_restores_the_pricing_flags(items_by_name):
    """The sensitivity run flips the module globals and must put them back —
    and must never price the crit multiplier twice.

    Uses a fixed six-item core rather than Medusa's live build note, because
    the daily community refresh owns that note's contents and this test
    doesn't need it — it needs one item with an Adaptive Stat passive (The
    Executioner) and one with a crit-damage passive (Deathbringer), both
    stable item-data facts. The expected Strength gain is derived from
    `passives.adaptive_grants` itself, the same function `efficiency`
    calls, so a change to the item's passive text moves both sides together
    instead of silently going stale here."""
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    assert weights.get("price_adaptive") and weights.get("price_crit_multipliers"), (
        "this test needs both flags ON in the shipped weights to prove anything")
    god = _god("Medusa")
    community = ["Tyrfing", "Odysseus' Bow", "Silverbranch Bow",
                 "The Executioner", "Deathbringer", "Manchu Bow"]
    note = {"builds": [
        {"source": "community", "slot_order": community},
        {"source": "suggested", "archetype": bq.DEFAULT_ARCHETYPE, "slot_order": MEDUSA_OURS},
    ]}
    builds = {"Medusa": note}
    items = recommend.load_items()

    before_adaptive = efficiency.PRICE_ADAPTIVE
    before_crit = efficiency.PRICE_CRIT_MULTIPLIERS
    unpriced_rows, unpriced_skipped = bq.run([god], items, builds, weights, priced=False)
    priced_rows, priced_skipped = bq.run([god], items, builds, weights, priced=True)
    assert not unpriced_skipped and not priced_skipped

    # PRICE_ADAPTIVE actually took effect: the priced run's Strength gain over
    # the unpriced run equals what `passives.adaptive_grants` prices for this
    # core's own items on the shipped branch.
    branch = str(weights.get("adaptive_branch") or "strength")
    expected_gain = sum(
        passives.adaptive_grants(items_by_name[n], branch).get("Strength", 0.0)
        for n in community)
    assert expected_gain > 0, "fixture drifted: no adaptive-priced item left in this core"
    got_gain = (priced_rows[0]["community"]["stats"]["Strength"]
                - unpriced_rows[0]["community"]["stats"]["Strength"])
    assert got_gain == pytest.approx(expected_gain)

    # Never priced twice: PRICE_CRIT_MULTIPLIERS is forced off for the priced
    # run, so Deathbringer's Critical Chance % must read exactly its raw stat
    # — no `crit_damage_as_chance` top-up stacked on top of `combat`'s own
    # measured 1.85x multiplier.
    assert (priced_rows[0]["community"]["stats"]["Critical Chance %"]
            == unpriced_rows[0]["community"]["stats"]["Critical Chance %"])

    assert efficiency.PRICE_ADAPTIVE == before_adaptive
    assert efficiency.PRICE_CRIT_MULTIPLIERS == before_crit


def test_cli_prints_one_god(capsys, items_by_name):
    """`main --god` exits 0 and prints that god's own worked example, exits 1
    for a god that isn't compared. The DPS figures are read off `bq.compare`
    in the test rather than hand-copied, since the community build (and so
    the DPS) is live data the daily refresh moves independently of this CLI
    contract."""
    god = _god("Medusa")
    note = recommend.load_build_note("Medusa")
    row = bq.compare(god, note, items_by_name)
    assert row is not None, "fixture drifted: Medusa no longer has a full community + suggested core"
    c = row["community"]
    community_line = (f"| COMMUNITY vs squishy (70) | {c['basic_dps'][70]:.1f} | "
                      f"{c['ability_dps'][70]:.1f} | **{c['total_dps'][70]:.1f}** | "
                      f"{c['ehp_physical']:,.0f} | {c['ehp_magical']:,.0f} |")

    assert bq.main(["--god", "Medusa"]) == 0
    out = capsys.readouterr().out
    assert f"### {row['god']} ({row['role']})" in out
    assert community_line in out
    assert bq.main(["--god", "Nobody"]) == 1


# A figure, as a reader meets one: a decimal, a percentage, a gold amount, or
# an ahead/behind count. The fingerprint (bare hex) and the title carry none.
_FIGURE = re.compile(r"\d+\.\d|\d+%|\d[\d,]*g|DPS|ahead|behind")
_CAVEAT = "READ THIS BEFORE ANY NUMBER BELOW"


def _caveat_precedes_every_figure(text, where):
    figure = _FIGURE.search(text)
    if figure is None:
        return
    caveat = text.find(_CAVEAT)
    assert caveat != -1, f"{where}: prints a figure and never states the blind spot"
    assert caveat < figure.start(), (
        f"{where}: first figure {figure.group()!r} at {figure.start()} precedes the caveat at {caveat}")


def _cli_invocations(parser, tmp_path):
    """One invocation per option the parser knows, discovered from the parser
    itself so a flag added tomorrow is exercised without anyone remembering
    to list it here. An option this cannot drive fails the test rather than
    going quietly untested."""
    base = ["--out", str(tmp_path / "report.md")]
    yield "(no flags)", base
    for action in parser._actions:
        if not action.option_strings or action.dest in ("help", "out"):
            continue
        flag = action.option_strings[-1]
        if action.nargs == 0:
            yield flag, base + [flag]
        elif action.choices:
            for choice in action.choices:
                yield f"{flag} {choice}", base + [flag, str(choice)]
        elif action.dest == "god":
            yield f"{flag} Medusa", base + [flag, "Medusa"]
        elif action.dest == "role":
            # Both shapes: a role whose objective names a threshold and one
            # whose objective is a ratio, because they render different tables.
            for role in ("Carry", "Solo"):
                yield f"{flag} {role}", base + [flag, role]
        elif action.dest == "archetype":
            for archetype in ("model", "core"):
                yield f"{flag} {archetype}", base + [flag, archetype]
        else:
            pytest.fail(f"{flag}: this test does not know a value to drive it with — "
                        "teach it one, so the new path is checked for the caveat")


def test_every_cli_path_states_the_caveat_before_its_first_figure(tmp_path, capsys):
    """`--god Medusa` is the invocation STATE.md §6 recommends and it once
    printed a DPS table with no caveat at all (2026-08-21) — `main` returned
    before the blind spot was measured. The full run's stdout had the same
    fault in a softer form: the ahead/behind counts came first and the blind
    spot after. This drives every path the parser exposes, reads everything
    each one printed or wrote, and requires the caveat before the first
    figure in each."""
    parser = bq.build_parser()
    for where, argv in _cli_invocations(parser, tmp_path):
        for stale in tmp_path.iterdir():
            stale.unlink()
        assert bq.main(argv) == 0, where
        _caveat_precedes_every_figure(capsys.readouterr().out, f"{where} stdout")
        for written in tmp_path.iterdir():
            _caveat_precedes_every_figure(written.read_text(encoding="utf-8"),
                                          f"{where} -> {written.name}")


def test_the_only_way_out_of_the_module_is_the_caveated_sink():
    """Every print and every file write in `build_quality.py` lives inside
    `emit`, which puts the caveat first. A new `--flag` that prints its own
    table cannot bypass the caveat, because it has no way to print."""
    tree = ast.parse(inspect.getsource(bq))
    parents = {}
    for node in ast.walk(tree):
        for child in ast.iter_child_nodes(node):
            parents[child] = node

    def enclosing_function(node):
        while node in parents:
            node = parents[node]
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                return node.name
        return None

    offenders = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        f = node.func
        name = f.id if isinstance(f, ast.Name) else f.attr if isinstance(f, ast.Attribute) else None
        if name not in ("print", "write", "write_text", "write_bytes", "open", "writelines"):
            continue
        if name == "print" and any(k.arg == "file" for k in node.keywords):
            continue   # stderr diagnostics ("Nobody: not compared") carry no figure
        if enclosing_function(node) != "emit":
            offenders.append(f"{name} at line {node.lineno} in {enclosing_function(node)}")
    assert not offenders, offenders


# ── The boundary ──────────────────────────────────────────────────────────

#: An actual import of this module, as opposed to a mention of its name in
#: prose. Tightened 2026-08-22: the check was a bare substring search over the
#: whole source, so a COMMENT naming the diagnostic failed it — which is a
#: false positive, and one that pushes evidence written next to the code it
#: constrains (the rule in CLAUDE.md) into naming the module obliquely instead.
#: `test_the_import_guard_still_catches_a_real_import` pins that the guard did
#: not get weaker in the process.
_IMPORTS_BUILD_QUALITY = re.compile(
    # `from <anything> import ... build_quality ...`, or either form of
    # naming it in the dotted module path itself.
    r"^[ \t]*(?:from[ \t]+[\w.]+[ \t]+import[ \t]+[^#]*\bbuild_quality\b"
    r"|(?:from|import)[ \t]+[\w.]*\bbuild_quality\b)", re.M)


def test_nothing_in_the_model_imports_this():
    """A diagnostic, not a scoring input. Register §4.4 is what happens when a
    damage measure becomes a fit signal; this pins the import boundary.

    An import, not a mention: `efficiency.offmap_gold` cites this module by
    name to record that it is blind to mana (§4.16), which is prose and not a
    dependency."""
    for mod in (scoring, assemble, recommend, build_index, efficiency):
        assert not _IMPORTS_BUILD_QUALITY.search(inspect.getsource(mod)), mod.__name__


def test_the_import_guard_still_catches_a_real_import():
    """The guard above was loosened from a substring search to an import
    match, so pin that every shape of the real thing still trips it — and
    that the prose which motivated the change still does not."""
    for src in ("from smite import build_quality",
                "from smite import scoring, build_quality",
                "import smite.build_quality",
                "    from smite import build_quality",
                "from smite.build_quality import compare"):
        assert _IMPORTS_BUILD_QUALITY.search(src), src
    for src in ("# `build_quality` is blind to mana",
                '"""build_quality cannot adjudicate this."""',
                "# see build_quality.ROLE_OBJECTIVES"):
        assert not _IMPORTS_BUILD_QUALITY.search(src), src


# ── Where the off-map charge lands (STATE.md §4.18) ────────────────────────

def test_offmap_charge_reads_the_map_scoring_itself_built():
    """The composition has to be measured against `scoring.fit_map`, not
    against a private rebuild of it. §4.15's whole finding is the two halves of
    `quality` disagreeing about what a god wants; a diagnostic with a third
    opinion would be the same defect with a bigger surface."""
    src = inspect.getsource(bq.offmap_charge)
    assert "scoring.fit_map(" in src
    assert '"stat_gold"' in src, "the gold must be efficiency's own column"


def test_offmap_charge_bills_only_what_the_map_does_not_name():
    god = _god("Susano")
    items = recommend.load_items()
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    role_map, _ = scoring.fit_map(god, items, weights,
                                  scoring.resolve_profile(weights, "Conquest", None))
    row = {"god": god["name"], "primary_role": "Jungle",
           "ours": {"items": ["Tekko-Kagi"]}}
    charge = bq.offmap_charge([row], [god], items, weights)
    billed = charge["Jungle"]["stats"]
    # Tekko-Kagi is Strength 35 / Attack Speed 20% / Penetration 10, and a
    # Jungle map names Strength and Penetration but not Attack Speed.
    assert set(billed) == {"Attack Speed"}
    assert role_map.get("Strength") and role_map.get("Penetration")
    assert not role_map.get("Attack Speed")
    assert billed["Attack Speed"] == pytest.approx(charge["Jungle"]["gold"])


def test_offmap_charge_bills_nothing_for_an_exempted_stat():
    """The exemption is subtracted here too, so the section never reports gold
    that no god is actually charged."""
    god = _god("Susano")
    items = recommend.load_items()
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    spared = {**weights, "offmap_exempt": list(weights["offmap_exempt"]) + ["Attack Speed"]}
    row = {"god": god["name"], "primary_role": "Jungle", "ours": {"items": ["Tekko-Kagi"]}}
    assert bq.offmap_charge([row], [god], items, spared)["Jungle"]["gold"] == 0.0


def test_no_exempted_stat_may_be_one_combat_can_price():
    """§4.16 test (ii), enforced instead of restated. An exemption says only
    "do not charge"; if `combat.py` reads the stat then charging it is a
    hypothesis THIS report can check, and the honest move is to check it. Echo
    is why this test exists — it passes test (i) (named by no role map) and
    fails here, and the check it demanded came back against the exemption
    (STATE.md §4.18)."""
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    for stat in weights.get("offmap_exempt") or ():
        assert stat not in bq.COMBAT_PRICED, (
            f"{stat} is priced by combat.py; check the charge with this report "
            "rather than exempting it")
    assert "Echo" in bq.COMBAT_PRICED and "Echo" not in weights["offmap_exempt"]


def test_combat_priced_names_are_stats_the_pool_actually_carries():
    """A typo in `COMBAT_PRICED` would silently make a stat look unpriced,
    which is half of what admits it to the exempt list."""
    carried = {efficiency.stat_base(k)
               for it in recommend.load_items() if scoring.is_buildable(it)
               for k in efficiency.item_stat_values(it)}
    assert set(bq.COMBAT_PRICED) <= carried


def test_the_charge_section_states_the_standing_of_every_stat_it_bills():
    """A stat cannot appear in the composition table without the two tests'
    answer for it beside it — that is the whole point of the section."""
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    charge = {"Jungle": {"n": 1, "gold": 900.0,
                         "stats": {"Echo": 500.0, "Attack Speed": 400.0}}}
    text = "\n".join(bq.offmap_charge_lines(charge, weights))
    for stat in charge["Jungle"]["stats"]:
        assert text.count(stat) >= 2, stat
    assert "nowhere" in text, "a stat named by no role map must be marked as such"
    assert "Carry, Constant, Hunter, Pressure, Sharpshooter" in text


def test_stat_standing_reads_the_shipped_role_table():
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    named, priced, exempt = bq.stat_standing("Echo", weights)
    assert named == [] and priced == "echo_multiplier" and exempt is False
    named, priced, exempt = bq.stat_standing("Max Mana", weights)
    assert named == [] and priced is None and exempt is True
    named, _, _ = bq.stat_standing("Physical Protection", weights)
    assert len(named) == 6, "the defect stats have a contrast; they are not exemptible"


# ── Plating: priced on the target, unreadable on the build (STATE.md §4.19) ─

def test_plating_and_dampening_are_target_side_only():
    """`combat.py` names both, so `COMBAT_PRICED` lists them — but neither
    reaches the build being judged, which is what test (ii) actually asks
    about. Pinned as a pair so the report's third answer cannot be lost."""
    for stat in bq.TARGET_SIDE_ONLY:
        assert stat in bq.COMBAT_PRICED
    assert set(bq.TARGET_SIDE_ONLY) == {"Plating", "Dampening"}
    _named, priced, _exempt = bq.stat_standing(
        "Plating", scoring.load_weights(recommend.WEIGHTS_PATH))
    assert "on the target only" in priced


def test_nothing_in_the_pipeline_ever_supplies_a_plating_value():
    """The claim `TARGET_SIDE_ONLY` rests on, driven off the modules instead of
    asserted. `damage_dealt` takes `plating=`/`dampening=` and every caller
    leaves them at the signature default, and `effective_health` has no term
    for either — so a build's own Plating is worth 0.0 to this report.

    If someone wires either into the buyer's side, this fails, and §4.19 has
    to be re-argued against an instrument that can finally check it."""
    import smite

    pkg = pathlib.Path(smite.__file__).parent
    callers = []
    for path in sorted(pkg.glob("*.py")):
        if path.name == "combat.py":
            continue
        for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
            if not isinstance(node, ast.Call):
                continue
            for kw in node.keywords:
                if kw.arg in ("plating", "dampening"):
                    callers.append(f"{path.name}:{node.lineno} {kw.arg}=")
    assert not callers, f"a caller now supplies a flat reduction: {callers}"
    sig = inspect.signature(combat.effective_health)
    assert list(sig.parameters) == ["health", "protection"]


def test_the_charge_section_marks_a_target_side_row():
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    charge = {"Solo": {"n": 1, "gold": 900.0,
                       "stats": {"Plating": 600.0, "Attack Speed": 300.0}}}
    text = "\n".join(bq.offmap_charge_lines(charge, weights))
    assert "on the target only" in text
    assert "§4.19" in text
