import pytest

from smite import scoring


def test_only_tier3_can_take_one_of_the_six_core_slots():
    # Tier 3 is buildable. Components (1/2) are purchase-path steps, and
    # relics get their own slot from the game, so neither competes here.
    # Every fixture carries a stat, because a statless item is excluded outright.
    st = {"stats": {"Strength": "40"}}
    assert scoring.is_buildable({"tier": 3, **st}) is True
    assert scoring.is_buildable({"tier": 2, **st}) is False
    assert scoring.is_buildable({"tier": 1, **st}) is False
    assert scoring.is_buildable({"tier": None, **st}) is False
    assert scoring.is_buildable({"tier": "Relic", **st}) is False
    assert scoring.is_buildable({"tier": "Glyph", **st}) is False


def test_a_statless_item_is_not_buildable_at_any_price():
    """Every signal is blind to it. Efficiency is cost minus a prediction summed
    over stats, and fit is a weighted read of stats, so a statless item's
    numbers are artefacts — and they were being compared against items where
    they mean something.

    Blink Rune found this: cost 0, no stats, and therefore maximally
    "undervalued" by construction. It had reached 262 shipped build slots.
    Blinking Abyss is the mirror at 2600 gold, reading as maximally premium."""
    assert scoring.is_buildable({"tier": "Relic", "cost": 0, "stats": {}}) is False
    assert scoring.is_buildable({"tier": "Relic", "cost": 2600, "stats": {}}) is False
    assert scoring.is_buildable({"tier": 3, "cost": 3000}) is False


def test_a_statted_paid_relic_does_take_a_core_slot():
    """CORRECTED 2026-08-19. This asserted the opposite, on a docstring that
    said excluding relics by tier was "what the game actually says". It is not:
    the game gives a free slot to the BASE relic, and an upgraded one is bought
    with gold and takes one of the six like anything else.

    The community data was saying so the whole time — Shell of Rebuke appears
    62 times across the tracked six-item builds — and the old rule made the
    model structurally unable to recommend it. See is_buildable's docstring for
    what that cost the measurement."""
    aegis = {"tier": "Relic", "cost": 2500,
             "stats": {"Physical Protection": "15", "Magical Protection": "15"}}
    assert scoring.is_buildable(aegis) is True


def test_load_weights_missing_file_returns_defaults(tmp_path):
    w = scoring.load_weights(tmp_path / "nope.yaml")
    assert w["signals"]["efficiency"] == 0.35
    assert w["signals"]["win"] == 0.30
    assert w["signals"]["pick"] == 0.15
    assert w["signals"]["fit"] == 0.20


def test_load_weights_file_overrides_defaults(tmp_path):
    p = tmp_path / "_weights.yaml"
    p.write_text("signals:\n  efficiency: 0.5\n", encoding="utf-8")
    w = scoring.load_weights(p)
    assert w["signals"]["efficiency"] == 0.5
    # unspecified keys fall back to defaults
    assert w["signals"]["win"] == 0.30


def test_load_tags_missing_file_returns_empty(tmp_path):
    assert scoring.load_tags(tmp_path / "nope.yaml") == {}


def test_load_tags_reads_mapping(tmp_path):
    p = tmp_path / "_tags.yaml"
    p.write_text("Brawler's Ruin:\n  - anti-heal\n", encoding="utf-8")
    assert scoring.load_tags(p) == {"Brawler's Ruin": ["anti-heal"]}


def _god(name, damage_type, role, specs):
    return {"name": name, "damage_type": damage_type, "role": role, "specializations": specs}


def test_item_damage_type_from_primary_stat():
    assert scoring.item_damage_type({"stats": {"Strength": "40"}}) == "physical"
    assert scoring.item_damage_type({"stats": {"Intelligence": "70"}}) == "magical"
    assert scoring.item_damage_type({"stats": {"Physical Protection": "50"}}) == "neutral"


def test_item_damage_type_basic_attack_stats_are_physical():
    # Basic-attack items (attack speed / crit / raw attack damage) are physical
    # even without a literal Strength stat — a mage never builds them.
    assert scoring.item_damage_type({"stats": {"Attack Speed": "15", "Attack Damage": "20"}}) == "physical"
    assert scoring.item_damage_type({"stats": {"Critical Chance": "20%"}}) == "physical"
    # A hybrid converter that also carries Intelligence stays magical.
    assert scoring.item_damage_type({"stats": {"Intelligence": "30", "Attack Speed": "10"}}) == "magical"
    # Pure utility/protection stays neutral (buildable by anyone).
    assert scoring.item_damage_type({"stats": {"Cooldown Rate": "10"}}) == "neutral"


def test_passes_damage_filter_excludes_mismatched_offense():
    phys_god = _god("Ullr", "physical", "Hunter", ["Hunter"])
    int_item = {"stats": {"Intelligence": "70"}}
    str_item = {"stats": {"Strength": "40"}}
    neutral_item = {"stats": {"Physical Protection": "50"}}
    assert scoring.passes_damage_filter(str_item, phys_god)
    assert not scoring.passes_damage_filter(int_item, phys_god)
    assert scoring.passes_damage_filter(neutral_item, phys_god)  # neutral always passes


def _scaling_god(name, damage_type, role, specs, str_pct, int_pct, n=4):
    """A god whose abilities carry real scaling lines, so `kit.scaling_profile`
    reads a genuine str/int split rather than the empty default."""
    abilities = [{"name": f"A{i}", "slot": f"Ability {i}",
                  "details": [f"Damage Scaling: {str_pct}% Strength + {int_pct}% Intelligence"]}
                 for i in range(n)]
    return {"name": name, "damage_type": damage_type, "role": role,
            "specializations": specs, "abilities": abilities}


def test_a_measured_hybrid_scaler_may_build_off_type_items():
    """Neith is labelled physical and takes 55% of her ability damage off
    Intelligence. The label was a hard gate, so her entire community build —
    six Intelligence items — was invisible, scoring a structural 0%."""
    neith = _scaling_god("Neith", "physical", "Carry Mid", ["Nuker"], 45, 55)
    artemis = _scaling_god("Artemis", "physical", "Carry", ["Sharpshooter"], 100, 0)
    int_item = {"stats": {"Intelligence": "70"}}
    assert scoring.off_type_share(neith) > 0.5
    assert scoring.passes_damage_filter(int_item, neith)
    # A genuinely pure-Strength carry keeps the strict gate.
    assert scoring.off_type_share(artemis) == 0.0
    assert not scoring.passes_damage_filter(int_item, artemis)


def test_hybrid_scaling_needs_enough_parsed_abilities():
    """A share computed from one or two abilities is an artifact of a thin
    scrape and must not unlock off-type items.

    This guard used to be what the three stance gods hit, because the parser
    could not see their kits at all — a real bug the threshold was quietly
    absorbing. That is fixed at the source now
    (`wiki_parser._section_tables`); the guard remains for a genuinely thin
    scrape, which is what it was for."""
    thin = _scaling_god("Thin", "physical", "Jungle", ["Bruiser"], 40, 60, n=2)
    assert scoring.off_type_share(thin) == 0.0
    assert not scoring.passes_damage_filter({"stats": {"Intelligence": "70"}}, thin)


def test_hybrid_scaling_can_be_switched_off_by_config():
    neith = _scaling_god("Neith", "physical", "Carry Mid", ["Nuker"], 45, 55)
    off = {"hybrid_scaling": {"enabled": False}}
    assert not scoring.passes_damage_filter({"stats": {"Intelligence": "70"}}, neith, off)


def test_hybrid_scaler_also_gets_fit_credit_for_the_off_type_stat():
    """Admitting the item without scoring the stat would be worse than the bug
    it fixes: the item enters the pool and then never wins a slot. The filter
    and the fit map have to move together."""
    weights = scoring.load_weights_default()
    weights["hybrid_scaling"] = {"enabled": True, "min_off_share": 0.30,
                                 "min_abilities": 3}
    neith = _scaling_god("Neith", "physical", "Carry Mid", ["Nuker"], 45, 55)
    artemis = _scaling_god("Artemis", "physical", "Carry", ["Sharpshooter"], 100, 0)
    assert scoring._role_stat_map(neith, weights).get("Intelligence", 0) > 0
    assert "Intelligence" not in scoring._role_stat_map(artemis, weights)


def test_kit_overlay_weights_both_power_stats_by_their_measured_share():
    """Symmetric by construction: Neith's 44.5/55.5 split should rank
    Intelligence ABOVE Strength, which one `damage_type` label cannot say."""
    from smite import kit
    neith = _scaling_god("Neith", "physical", "Carry Mid", ["Nuker"], 45, 55)
    profile = kit.scaling_profile(neith)
    on_only = kit.kit_stat_overlay(profile, neith)
    both = kit.kit_stat_overlay(profile, neith, include_off_type=True)
    assert "Intelligence" not in on_only          # default stays label-gated
    assert both["Intelligence"] > both["Strength"]


def test_god_fit_rewards_role_relevant_stats():
    weights = scoring.load_weights_default()
    sharpshooter = _god("Chiron", "physical", "Carry", ["Sharpshooter"])
    crit_item = {"stats": {"Critical Chance": "20%", "Attack Speed": "15"}}
    off_stat_item = {"stats": {"Magical Protection": "50"}}
    assert scoring.god_fit_score(crit_item, sharpshooter, weights, []) > \
        scoring.god_fit_score(off_stat_item, sharpshooter, weights, [])


def _community_build(*slots):
    # slots: (name, pick_rate, win_rate)
    return {"builds": [{"source": "community",
                        "slot_order": [{"name": n, "pick_rate": p, "win_rate": w}
                                       for (n, p, w) in slots]}]}


def test_lookup_rates_from_community_entry():
    build = _community_build(("Transcendence", 0.9, 0.55))
    assert scoring.lookup_rates(build, "Transcendence") == (0.9, 0.55)
    assert scoring.lookup_rates(build, "Missing") == (0.0, None)


def test_signal_score_combines_all_four_signals():
    weights = scoring.load_weights_default()
    god = _god("Chiron", "physical", "Carry", ["Sharpshooter"])
    item = {"name": "Deathbringer", "stats": {"Critical Chance": "20%", "Strength": "45"}}
    build = _community_build(("Deathbringer", 0.5, 0.6))
    row = scoring.signal_score(item, god, build, eff_score=0.8, weights=weights, item_tags=[])
    w = weights["signals"]
    expected = (w["efficiency"] * row["efficiency"] + w["win"] * row["win"]
                + w["pick"] * row["pick"] + w["fit"] * row["fit"])
    assert row["total"] == pytest.approx(expected)
    assert row["pick"] == 0.5 and row["win"] == 0.6


def test_mark_underrated_flags_top_quality_low_pick():
    weights = scoring.load_weights_default()  # top_quality_frac 0.30, max_pick 0.15
    rows = [
        {"quality": 0.90, "pick": 0.05},  # top-quality + unpicked -> underrated
        {"quality": 0.85, "pick": 0.50},  # top-quality but popular -> no
        {"quality": 0.40, "pick": 0.02},  # unpicked but not top-quality -> no
        {"quality": 0.30, "pick": 0.01},
        {"quality": 0.20, "pick": 0.01},
    ]
    scoring.mark_underrated(rows, weights)
    flags = {r["quality"]: r["underrated"] for r in rows}
    assert flags[0.90] is True
    assert flags[0.85] is False   # popular despite high quality
    assert flags[0.40] is False   # low pick but not top-quality


def test_mark_underrated_empty_is_safe():
    assert scoring.mark_underrated([], scoring.load_weights_default()) == []


def test_score_god_items_excludes_components_relics_and_wrong_damage_type():
    # `_god` builds a fixture with no abilities, so its scaling profile is
    # empty and it keeps the strict damage-type gate (see hybrid_scaling).
    god = _god("Chiron", "physical", "Carry", ["Sharpshooter"])
    items = [
        {"name": "Final", "tier": 3, "stats": {"Strength": "40"}},
        {"name": "Relic", "tier": None, "stats": {"Strength": "40"}},
        {"name": "Component", "tier": 2, "stats": {"Strength": "40"}},
        {"name": "WrongType", "tier": 3, "stats": {"Intelligence": "70"}},
    ]
    build = _community_build()
    eff = {n: {"score": 0.5, "tier": "fair"} for n in ["Final", "Relic", "Component", "WrongType"]}
    rows = scoring.score_god_items(god, items, build, eff, scoring.load_weights_default(), {})
    assert {r["item"] for r in rows} == {"Final"}


def test_eligible_flavors_gates_by_damage_type_and_tokens():
    weights = scoring.load_weights_default()
    weights["flavors"] = {
        "crit": {"damage_types": ["physical"], "match_any": ["Carry", "Sharpshooter"]},
        "burst": {"damage_types": None, "match_any": ["Nuker", "Burst", "Slayer", "Sniper", "Mid"]},
        "bruiser": {"damage_types": None, "match_any": None},
        "anti-tank": {"damage_types": None, "match_any": None},
    }
    chiron = {"name": "Chiron", "damage_type": "physical", "role": "Carry",
              "specializations": ["Sharpshooter", "Nuker"]}
    ra = {"name": "Ra", "damage_type": "magical", "role": "Mid",
          "specializations": ["Sniper", "Healing"]}
    herc = {"name": "Hercules", "damage_type": "physical", "role": "Solo",
            "specializations": ["Tank", "Brawler", "Lockdown"]}
    assert set(scoring.eligible_flavors(chiron, weights)) == {"crit", "burst", "bruiser", "anti-tank"}
    assert set(scoring.eligible_flavors(ra, weights)) == {"burst", "bruiser", "anti-tank"}
    assert set(scoring.eligible_flavors(herc, weights)) == {"bruiser", "anti-tank"}


def test_god_fit_stat_overlay_and_tag_bonus():
    weights = scoring.load_weights_default()
    god = {"name": "Chiron", "damage_type": "physical", "role": "Carry",
           "specializations": ["Sharpshooter"]}
    crit_item = {"stats": {"Critical Chance": "20%"}}
    base = scoring.god_fit_score(crit_item, god, weights, [])
    boosted = scoring.god_fit_score(crit_item, god, weights, [],
                                    stat_overlay={"Critical Chance": 3.0})
    assert boosted >= base
    penalized = scoring.god_fit_score({"stats": {"Strength": "40"}}, god, weights,
                                      ["wave-clear"], tag_bonus={"wave-clear": -0.15})
    assert penalized >= 0.0


def test_resolve_profile_composes_mode_and_flavor():
    weights = scoring.load_weights_default()
    weights["modes"] = {"joust": {"signals": {"win": 0.0, "pick": 0.0},
                                  "tag_bonus": {"sustain": 0.25}, "label": "Joust profile"}}
    weights["flavors"] = {"bruiser": {"stats": {"Health": 1.0}, "tag_bonus": {"sustain": 0.3},
                                      "max_lifesteal": 2}}
    p = scoring.resolve_profile(weights, "Joust", "bruiser")
    assert p["signals"]["win"] == 0.0 and p["signals"]["pick"] == 0.0
    assert p["signals"]["efficiency"] == weights["signals"]["efficiency"]
    assert p["stat_overlay"] == {"Health": 1.0}
    assert p["tag_bonus"]["sustain"] == 0.3
    assert p["max_lifesteal"] == 2
    assert p["suppress_underrated"] is True
    assert p["label"] == "Joust profile"


def test_score_god_items_profile_suppresses_underrated():
    god = {"name": "Chiron", "damage_type": "physical", "role": "Carry", "specializations": ["Sharpshooter"]}
    items = [{"name": "A", "tier": 3, "stats": {"Strength": "40"}},
             {"name": "B", "tier": 3, "stats": {"Strength": "40"}}]
    eff = {n: {"score": 0.5, "tier": "fair"} for n in ["A", "B"]}
    weights = scoring.load_weights_default()
    profile = {"signals": {**weights["signals"], "win": 0.0, "pick": 0.0}, "suppress_underrated": True}
    rows = scoring.score_god_items(god, items, {"builds": []}, eff, weights, {}, profile=profile)
    assert all(r["underrated"] is False for r in rows)


def test_pick_starter_matches_role_and_damage_type():
    weights = scoring.load_weights_default()
    weights["starters"] = [
        {"base": "Gilded Arrow", "upgrade": "Sharpshooter's Arrow",
         "damage_types": ["physical"], "match_any": ["Carry", "Sharpshooter", "Hunter"], "priority": 10},
        {"base": "Conduit Gem", "upgrade": "Archmage's Gem",
         "damage_types": ["magical"], "match_any": ["Mid", "Nuker", "Mage", "Sniper", "Carry"], "priority": 10},
        {"base": "Bumba's Golden Dagger", "upgrade": "Bumba's Spear",
         "damage_types": None, "match_any": ["Jungle", "Slayer", "Assassin"], "priority": 9},
        {"base": "Death's Toll", "upgrade": "Death's Embrace",
         "damage_types": None, "match_any": None, "priority": 1},
    ]
    phys_carry = {"damage_type": "physical", "role": "Carry", "specializations": ["Sharpshooter"]}
    mag_carry = {"damage_type": "magical", "role": "Carry Mid", "specializations": ["Sharpshooter"]}
    jungler = {"damage_type": "physical", "role": "Jungle", "specializations": ["Slayer"]}
    oddball = {"damage_type": "physical", "role": "Support", "specializations": ["Guardian"]}
    assert scoring.pick_starter(phys_carry, weights)["base"] == "Gilded Arrow"
    assert scoring.pick_starter(mag_carry, weights)["base"] == "Conduit Gem"
    assert scoring.pick_starter(jungler, weights)["base"] == "Bumba's Golden Dagger"
    assert scoring.pick_starter(oddball, weights)["base"] == "Death's Toll"


def test_resolve_profile_composes_aspect_overlay():
    weights = {"signals": {"efficiency": 0.35, "win": 0.30, "pick": 0.15, "fit": 0.20},
               "flavors": {"crit": {"stats": {"Critical Chance": 1.5}, "tag_bonus": {"x": 0.1}}},
               "modes": {"conquest": {}}}
    aspect = {"stats": {"Max Health": 1.0, "Critical Chance": 0.5}, "tag_bonus": {"aura": 0.3}, "max_lifesteal": 2}
    p = scoring.resolve_profile(weights, "Conquest", "crit", aspect_overlay=aspect)
    assert p["stat_overlay"]["Critical Chance"] == 1.5  # flavor wins shared key
    assert p["stat_overlay"]["Max Health"] == 1.0        # aspect contributes
    assert p["tag_bonus"]["aura"] == 0.3 and p["tag_bonus"]["x"] == 0.1
    assert p["max_lifesteal"] == 2                        # flavor has none -> aspect's


def test_resolve_profile_flavor_max_lifesteal_beats_aspect():
    weights = {"signals": {"efficiency": 1}, "flavors": {"f": {"max_lifesteal": 1}}, "modes": {"conquest": {}}}
    p = scoring.resolve_profile(weights, "Conquest", "f", aspect_overlay={"max_lifesteal": 2})
    assert p["max_lifesteal"] == 1


def test_resolve_profile_no_aspect_unchanged():
    weights = {"signals": {"efficiency": 1}, "flavors": {}, "modes": {"conquest": {}}}
    p = scoring.resolve_profile(weights, "Conquest", None)
    assert p["stat_overlay"] == {} and p["max_lifesteal"] == 1


def test_role_map_matches_tokens_in_multiword_roles():
    w = scoring.load_weights_default()
    cern = _god("Cernunnos", "physical", "Carry Jungle", ["Sharpshooter"])
    m = scoring._role_stat_map(cern, w)
    assert m["Attack Speed"] == 1.0          # Sharpshooter, exact match
    assert m["Penetration"] >= 0.8           # Jungle, token match


def test_role_map_drops_opposite_damage_type_offense():
    w = scoring.load_weights_default()
    cern = _god("Cernunnos", "physical", "Carry Jungle", ["Nuker", "Sharpshooter"])
    assert "Intelligence" not in scoring._role_stat_map(cern, w)
    ymir = _god("Ymir", "magical", "Support", ["Brawler", "Tank", "Lockdown"])
    m = scoring._role_stat_map(ymir, w)
    assert "Strength" not in m
    assert m["Physical Protection"] == 1.0
    assert m["Max Health"] == 0.8


def test_every_pool_role_vocabulary_produces_a_nonempty_map():
    w = scoring.load_weights_default()
    pool = [  # the real scraped vocabulary of all 11 gods
        ("magical", "Mid", ["Nuker", "Burst Damage", "Sniper"]),
        ("physical", "Carry Jungle", ["Nuker", "Sharpshooter", "Lockdown"]),
        ("physical", "Carry", ["Sharpshooter", "Nuker"]),
        ("magical", "Mid Carry", ["Constant Damage"]),
        ("physical", "Solo", ["Tank", "Brawler", "Lockdown"]),
        ("magical", "Mid", ["Nuker", "Burst Damage"]),
        ("magical", "Carry Mid", ["Sharpshooter", "Mobile", "Constant Damage"]),
        ("magical", "Mid", ["Sniper", "Healing", "Buffs"]),
        ("physical", "Jungle", ["Slayer", "Lockdown", "Mobile"]),
        ("physical", "Carry", ["Lockdown", "Burst Damage", "Pressure"]),
        ("magical", "Support", ["Brawler", "Tank", "Lockdown"]),
    ]
    for dt, role, specs in pool:
        m = scoring._role_stat_map(_god("X", dt, role, specs), w)
        assert m, f"empty fit map for role={role} specs={specs}"


def test_role_map_missing_role_and_specs_is_empty_and_fit_survives():
    w = scoring.load_weights_default()
    assert scoring._role_stat_map({"damage_type": "physical"}, w) == {}
    # fit degrades to tag-bonus-only, never raises
    assert scoring.god_fit_score({"stats": {"Strength": "40"}}, {"damage_type": "physical"}, w, []) == 0.0


def test_role_map_uses_max_health_not_health():
    # Items carry 'Max Health' (63 of them); no item has a 'Health' stat key.
    w = scoring.load_weights_default()
    for entry in w["role_stats"].values():
        assert "Health" not in entry, "use 'Max Health' — 'Health' matches no item"


def test_kit_overlay_blends_into_fit_via_score_god_items():
    weights = scoring.load_weights_default()
    int_item = {"name": "Staff", "tier": 3, "stats": {"Intelligence": "70"}}
    cdr_item = {"name": "Pendant", "tier": 3, "stats": {"Cooldown Rate": "10"}}
    eff = {"Staff": {"score": 0.5, "tier": "fair"}, "Pendant": {"score": 0.5, "tier": "fair"}}
    build = {"builds": []}
    kit_god = {"name": "K", "damage_type": "magical", "role": "Mid", "specializations": [],
               "abilities": [
                   {"slot": "1st Ability", "details": ["Damage Scaling: 80% Intelligence"]},
                   {"slot": "2nd Ability", "details": ["Damage Scaling: 70% Intelligence"]},
                   {"slot": "Ultimate", "details": ["Damage Scaling: 120% Intelligence"]},
               ]}
    no_kit_god = {**kit_god, "abilities": []}
    rows_kit = {r["item"]: r for r in scoring.score_god_items(
        kit_god, [int_item, cdr_item], build, eff, weights, {})}
    rows_plain = {r["item"]: r for r in scoring.score_god_items(
        no_kit_god, [int_item, cdr_item], build, eff, weights, {})}
    # A kit that is pure Intelligence scaling should shift fit relative to the
    # role map alone (the blended map differs from the plain role map).
    assert rows_kit["Staff"]["fit"] != rows_plain["Staff"]["fit"]


def test_lifesteal_caps_rule_raises_default_for_matching_god():
    w = scoring.load_weights_default()
    w["lifesteal_caps"] = [{"damage_types": ["physical"], "match_any": ["Carry"],
                            "max_lifesteal": 2}]
    p = scoring.resolve_profile(w, "Conquest", None)
    carry = _god("C", "physical", "Carry", ["Sharpshooter"])
    mage = _god("M", "magical", "Mid", [])
    assert scoring.god_max_lifesteal(carry, w, p) == 2
    assert scoring.god_max_lifesteal(mage, w, p) == 1


def test_explicit_flavor_cap_wins_over_lifesteal_caps_rule():
    w = scoring.load_weights_default()
    w["flavors"] = {"crit": {"stats": {}, "max_lifesteal": 1}}
    w["lifesteal_caps"] = [{"damage_types": ["physical"], "match_any": ["Carry"],
                            "max_lifesteal": 2}]
    p = scoring.resolve_profile(w, "Conquest", "crit")
    carry = _god("C", "physical", "Carry", [])
    assert scoring.god_max_lifesteal(carry, w, p) == 1


def test_fun_profile_zeroes_meta_signals_and_sets_bypass_flags():
    w = scoring.load_weights_default()
    w["flavors"] = {"fun-crit": {"fun": True, "bypass": ["damage_filter", "archetype_fit"],
                                 "stats": {"Critical Chance": 1.5}}}
    p = scoring.resolve_profile(w, "Conquest", "fun-crit")
    assert p["signals"]["win"] == 0.0 and p["signals"]["pick"] == 0.0
    assert p["bypass_damage_filter"] is True
    assert p["archetype_bypass"] is True
    assert p["fun"] is True
    assert p["suppress_underrated"] is True


def test_serious_profile_has_no_bypass():
    p = scoring.resolve_profile(scoring.load_weights_default(), "Conquest", None)
    assert p["bypass_damage_filter"] is False
    assert p["archetype_bypass"] is False
    assert p["fun"] is False


def test_bypass_damage_filter_lets_crit_items_reach_a_magical_god():
    w = scoring.load_weights_default()
    w["flavors"] = {"fun-crit": {"fun": True, "bypass": ["damage_filter", "archetype_fit"],
                                 "stats": {"Critical Chance": 1.5, "Attack Speed": 1.2}}}
    ymir = _god("Ymir", "magical", "Support", ["Tank"])
    crit_item = {"name": "Deathbringer", "tier": 3, "stats": {"Critical Chance": "25%"}}
    eff = {"Deathbringer": {"score": 0.5, "tier": "fair"}}
    fun = scoring.resolve_profile(w, "Conquest", "fun-crit")
    serious = scoring.resolve_profile(w, "Conquest", None)
    fun_rows = scoring.score_god_items(ymir, [crit_item], {"builds": []}, eff, w, {}, fun)
    serious_rows = scoring.score_god_items(ymir, [crit_item], {"builds": []}, eff, w, {}, serious)
    assert [r["item"] for r in fun_rows] == ["Deathbringer"]
    assert serious_rows == []                       # damage filter still guards serious builds
    assert fun_rows[0]["fit"] > 0                   # flavor stats drive fit despite empty role map


# ── Mode item availability ────────────────────────────────────────────────
# Some items are not in every mode's shop. Recommending one produces a build
# the player cannot assemble, which is worse than a mediocre suggestion — they
# go looking for an item that does not exist. Arena has no ward game, so the
# vision items are absent from it.

def _excl_fixture():
    god = {"name": "Hercules", "damage_type": "physical", "role": "Solo"}
    items = [{"name": "Eye of Providence", "tier": 3, "stats": {"Strength": "40"}},
             {"name": "Ordinary Blade", "tier": 3, "stats": {"Strength": "40"}}]
    eff = {n["name"]: {"score": 0.5, "tier": "fair"} for n in items}
    return god, items, eff, scoring.load_weights_default()


def test_resolve_profile_carries_mode_excluded_items():
    weights = scoring.load_weights_default()
    weights["modes"] = {"arena": {"excluded_items": ["Eye of Providence"]}, "conquest": {}}
    assert scoring.resolve_profile(weights, "Arena")["excluded_items"] == {"Eye of Providence"}
    # A mode that declares none gets an empty set, not None — callers iterate it.
    assert scoring.resolve_profile(weights, "Conquest")["excluded_items"] == frozenset()


def test_score_god_items_drops_items_the_mode_does_not_have():
    god, items, eff, weights = _excl_fixture()
    names = lambda p: {r["item"] for r in scoring.score_god_items(
        god, items, {}, eff, weights, {}, p)}
    # Present when the mode offers it...
    assert names({}) == {"Eye of Providence", "Ordinary Blade"}
    # ...and gone when it does not, without taking the rest of the pool with it.
    assert names({"excluded_items": frozenset(["Eye of Providence"])}) == {"Ordinary Blade"}


def test_excluded_items_survive_a_flavor_bypass():
    """`bypass` lets a fun flavor ignore the damage filter and archetype fit.
    It must not also let it buy an item the mode does not stock — those guards
    say "unusual", this one says "absent"."""
    god, items, eff, weights = _excl_fixture()
    rows = scoring.score_god_items(god, items, {}, eff, weights, {}, {
        "excluded_items": frozenset(["Eye of Providence"]),
        "bypass_damage_filter": True, "archetype_bypass": True, "fun": True})
    assert "Eye of Providence" not in {r["item"] for r in rows}


def test_every_shipped_mode_resolves_a_profile():
    """A mode in MODES with no `modes:` entry silently scores as Conquest —
    including its meta win rates, which describe a different game."""
    from smite import recommend
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    configured = set(weights.get("modes") or {})
    assert {m.lower() for m in recommend.MODES} <= configured


def test_shipped_arena_profile_excludes_the_vision_items():
    """The real config, not a fixture — this is the list a build regression
    would silently drop, and the user cannot buy either item in Arena."""
    from smite import recommend
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    assert scoring.resolve_profile(weights, "Arena")["excluded_items"] == {
        "Eye of Providence", "Eye of Erebus"}
    # Conquest and Joust both keep them; the exclusion is Arena's alone.
    for mode in ("Conquest", "Joust"):
        assert scoring.resolve_profile(weights, mode)["excluded_items"] == frozenset()


def _weight_stat_keys(weights):
    """Every stat name the config asks `god_fit_score` to look for, from all
    three blocks that carry one."""
    keys = set()
    for m in (weights.get("role_stats") or {}).values():
        keys |= set(m or {})
    for block in ("flavors", "aspects"):
        for cfg in (weights.get(block) or {}).values():
            keys |= set((cfg or {}).get("stats") or {})
    return keys


def test_no_weight_names_a_stat_no_item_has():
    """A misspelled stat key is invisible: `god_fit_score` looks it up in the
    item's stats dict, misses, and contributes nothing — the flavor still
    scores, just not the way it reads. The bruiser flavor asked for `Health`
    for months; the real key is `Max Health`, so its headline stat was dead
    weight in the denominator and nothing said so."""
    from pathlib import Path
    from smite import notes, recommend
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    real = set()
    for p in (recommend.DATA_ROOT / "Items").glob("*.md"):
        real |= set((notes.read_note(p)[0].get("stats") or {}))
    unknown = sorted(_weight_stat_keys(weights) - real)
    assert not unknown, f"_weights.yaml names stats no item carries: {unknown}"


# ── Off-type flavors, gated on the god's own scaling ──────────────────────

def test_off_type_flavors_are_gated_on_measured_scaling():
    """The gate is what makes an off-type build an alternative rather than a
    trap. Sol scales 1.00 on Strength despite being magical, so a Strength
    build is real for him; Scylla scales 0.28 and must not be offered one."""
    from pathlib import Path
    from smite import notes, recommend
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    god = lambda n: notes.read_note(recommend.DATA_ROOT / "Gods" / f"{n}.md")[0]

    assert "strength" in scoring.eligible_flavors(god("Sol"), weights)
    assert "strength" not in scoring.eligible_flavors(god("Scylla"), weights)
    # Neith is one of the gods sharing nothing with the community build, and
    # what the community actually runs on her is Intelligence.
    assert "intelligence" in scoring.eligible_flavors(god("Neith"), weights)
    assert "str-int" in scoring.eligible_flavors(god("Neith"), weights)


def test_a_kit_that_does_not_scale_gets_no_off_type_tab():
    """Chiron Mid is a thing people try; his kit scales 0.05 on Intelligence,
    so offering the build would be the model lying to be accommodating."""
    from smite import notes, recommend
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    chiron, _ = notes.read_note(recommend.DATA_ROOT / "Gods" / "Chiron.md")
    assert "intelligence" not in scoring.eligible_flavors(chiron, weights)


def test_requires_scaling_is_skipped_when_the_kit_did_not_parse():
    """14 gods have too few parsed abilities to value. They fall back to the
    role table everywhere else, and here they simply get no off-type tab —
    never one derived from an empty measurement."""
    weights = scoring.load_weights_default()
    weights["flavors"] = {"x": {"requires_scaling": {"Strength": 0.5}}}
    assert scoring.eligible_flavors({"abilities": []}, weights) == []


def test_the_for_fun_build_is_gone():
    """It was explicitly off-class with its meta signals zeroed — a build
    nobody should follow does not deserve a tab. Replaced by focused builds
    that are meant to be played."""
    from smite import recommend
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    assert "fun-crit" not in (weights.get("flavors") or {})
    assert not any(f.get("fun") for f in (weights.get("flavors") or {}).values())


# ── God-specific items ────────────────────────────────────────────────────

def test_a_god_specific_item_is_buildable_only_for_its_owner():
    """Aladdin's Genie's Lamp is in 77% of his community builds and unbuyable
    for the other 85 gods. Scored globally it would leak into everyone's build;
    excluded globally it costs him a slot he always fills."""
    lamp = {"name": "Genie's Lamp", "tier": "God Specific", "god": "Aladdin",
            "stats": {"Intelligence": "40"}}
    aladdin = _god("Aladdin", "magical", "Mid", ["Nuker"])
    anubis = _god("Anubis", "magical", "Mid", ["Nuker"])
    assert scoring.is_buildable(lamp, aladdin) is True
    assert scoring.is_buildable(lamp, anubis) is False
    # No god asked: the god-agnostic question, which the gold model and the
    # item page ask, and the answer must be no.
    assert scoring.is_buildable(lamp) is False


def test_god_specific_owner_is_read_from_the_icon_filename():
    """Nothing else on the page names the owner — the infobox says only
    'God Specific'."""
    from smite import wiki_parser
    assert wiki_parser.god_specific_owner(
        "/images/GodSpecific_Aladdin_Genie%27s_Lamp.png") == "Aladdin"
    assert wiki_parser.god_specific_owner(
        "/images/thumb/GodSpecific_Jing_Wei_Something.png") == "Jing"
    assert wiki_parser.god_specific_owner("/images/T3_Deathbringer.png") is None
    assert wiki_parser.god_specific_owner(None) is None


# ── Community rates: slot picks and alternates ────────────────────────────

def _rat_build():
    """Ratatoskr's real shape: Thistlethorn Acorn is the community's SECOND
    choice in three separate slots and the winner in none."""
    return {"builds": [{"source": "community", "slot_order": [
        {"name": "Ashwhorl Acorn", "pick_rate": 0.32, "win_rate": 0.53,
         "alternates": [{"name": "Thistlethorn Acorn", "pick_rate": 0.27, "win_rate": 0.48}]},
        {"name": "Jotunn's Revenge", "pick_rate": 0.23, "win_rate": 0.46,
         "alternates": [{"name": "Thistlethorn Acorn", "pick_rate": 0.17, "win_rate": 0.72}]},
        {"name": "Shifter's Shield", "pick_rate": 0.17, "win_rate": 0.65,
         "alternates": [{"name": "Ashwhorl Acorn", "pick_rate": 0.40, "win_rate": 0.20}]},
    ]}]}


def test_lookup_rates_reads_alternates_not_just_slot_winners():
    """The build row used to print "pick 0.00 · meta doesn't buy this" for an
    item the panel below it reported at 27% pick."""
    rates = scoring.lookup_rates(_rat_build(), "Thistlethorn Acorn")
    assert rates == (0.27, 0.48)          # the best of its alternate sightings


def test_lookup_rates_prefers_the_slot_pick_over_a_richer_alternate():
    """Ashwhorl Acorn is slotted at 32% and is also a 40% alternate elsewhere.
    The slot entry has to win: it is the rate the item is graded against, and
    preferring the alternate detaches score from target (rho 0.564 -> 0.453)."""
    assert scoring.lookup_rates(_rat_build(), "Ashwhorl Acorn") == (0.32, 0.53)


def test_lookup_rates_still_reports_nothing_for_an_unbought_item():
    assert scoring.lookup_rates(_rat_build(), "Rod of Tahuti") == (0.0, None)


def test_lookup_rates_agrees_with_the_popular_items_panel_on_what_is_bought():
    """The two derive community rates independently and are rendered on the
    same screen, so they must not drift on the question the build row asks:
    does this god's playerbase buy this item at all?

    They no longer agree on the NUMBER, and deliberately. The panel reports an
    observation — the share of all tracked matches that ended holding the item
    — which is what a reader means by "pick rate". The model reads the same
    sighting conditioned on reaching the slot (see `SLOT_REACH`), because an
    item bought sixth is otherwise divided by a denominator most of which never
    bought a sixth item. Both are correct; they are different quantities. What
    must never drift is the verdict, since only one of them renders the words
    "meta doesn't buy this"."""
    from smite import build_index
    entry = _rat_build()["builds"][0]
    panel = {p["name"]: p for p in build_index.popular_items(entry)}
    for name in ("Thistlethorn Acorn", "Ashwhorl Acorn", "Jotunn's Revenge"):
        pick, _ = scoring.lookup_rates(_rat_build(), name)
        assert (pick > 0) == (panel[name]["pick_rate"] > 0), name
    # For an item with NO slot pick the win rates must still match exactly:
    # both sides are then reading the same best alternate sighting, and this is
    # the case that used to print two different numbers on one screen. (An item
    # WITH a slot pick is allowed to differ — the slot entry is authoritative
    # here by design, while the panel takes the highest-pick sighting.)
    assert (scoring.lookup_rates(_rat_build(), "Thistlethorn Acorn")[1]
            == panel["Thistlethorn Acorn"]["win_rate"])
    # And an item neither of them has ever seen stays unseen in both.
    assert scoring.lookup_rates(_rat_build(), "Rod of Tahuti") == (0.0, None)
    assert "Rod of Tahuti" not in panel


# ── The slot-reach correction ──────────────────────────────────────────────

def _late_slot_build():
    """One item per slot, so each slot's reach factor is exercised alone."""
    return {"builds": [{"source": "community", "slot_order": [
        {"name": f"Slot{i}", "pick_rate": 0.20, "win_rate": 0.5} for i in range(1, 7)
    ]}]}


def test_lookup_rates_conditions_pick_on_reaching_the_slot():
    """The same 20% means something very different first and sixth: nearly
    every match buys a first item, and under a third reach a sixth."""
    rates = {n: scoring.lookup_rates(_late_slot_build(), n)[0] for n in
             (f"Slot{i}" for i in range(1, 7))}
    assert rates["Slot1"] == pytest.approx(0.20)        # reach 1.0, unchanged
    assert rates["Slot6"] == pytest.approx(0.20 / 0.325)
    # Monotone: a later slot's identical raw rate always scores at least as high.
    ordered = [rates[f"Slot{i}"] for i in range(1, 7)]
    assert ordered == sorted(ordered)


def test_lookup_rates_never_reports_a_pick_rate_above_one():
    """`signal_score` blends every axis as [0,1]. A late slot divides by 0.325,
    so an unclamped rate could exceed 1 and let one item out-score a rival that
    is perfect on every other axis at once."""
    build = {"builds": [{"source": "community", "slot_order": [
        {"name": "A", "pick_rate": 0.1}, {"name": "B", "pick_rate": 0.1},
        {"name": "C", "pick_rate": 0.1}, {"name": "D", "pick_rate": 0.1},
        {"name": "E", "pick_rate": 0.1}, {"name": "Late", "pick_rate": 0.9},
    ]}]}
    assert scoring.lookup_rates(build, "Late")[0] == 1.0


def test_lookup_rates_leaves_an_unbought_item_at_zero():
    """Conditioning scales; it must not manufacture a pick out of nothing."""
    assert scoring.lookup_rates(_late_slot_build(), "Never Bought") == (0.0, None)


def test_lookup_rates_picks_the_best_alternate_after_conditioning():
    """"Best sighting" has to mean the slot where players most preferred it,
    not merely the earliest slot it appeared in. Raw, the slot-1 sighting looks
    stronger; conditioned, the slot-6 one is."""
    build = {"builds": [{"source": "community", "slot_order": [
        {"name": "A", "pick_rate": 0.5, "alternates": [{"name": "X", "pick_rate": 0.20, "win_rate": 0.4}]},
        {"name": "B", "pick_rate": 0.4}, {"name": "C", "pick_rate": 0.3},
        {"name": "D", "pick_rate": 0.3}, {"name": "E", "pick_rate": 0.2},
        {"name": "F", "pick_rate": 0.2, "alternates": [{"name": "X", "pick_rate": 0.18, "win_rate": 0.7}]},
    ]}]}
    pick, win = scoring.lookup_rates(build, "X")
    assert win == 0.7                       # the slot-6 sighting won
    assert pick == pytest.approx(0.18 / 0.325)


def test_measure_slot_reach_reproduces_the_shipped_constant():
    """The constant is a measurement, so it has to be re-derivable from the
    corpus it was measured on rather than being a number someone typed."""
    builds = [_late_slot_build()]
    assert scoring.measure_slot_reach(builds) == {i: 1.0 for i in range(1, 7)}
    # An empty corpus yields nothing rather than a silent all-1.0 no-op.
    assert scoring.measure_slot_reach([]) == {}


def test_slot_reach_can_be_overridden_from_weights():
    weights = {"slot_reach": {1: 1.0, 2: 0.5}}
    build = {"builds": [{"source": "community", "slot_order": [
        {"name": "A", "pick_rate": 0.3}, {"name": "B", "pick_rate": 0.3},
    ]}]}
    assert scoring.lookup_rates(build, "B", weights)[0] == pytest.approx(0.6)


# ---- The win signal's stand-in for "no record" -----------------------------

def _win_build(*rates, alternates=None):
    slots = [{"name": f"S{i}", "pick_rate": 0.3, "win_rate": r}
             for i, r in enumerate(rates)]
    if alternates:
        slots[0]["alternates"] = list(alternates)
    return {"builds": [{"source": "community", "slot_order": slots}]}


def test_unknown_win_uses_the_gods_own_median():
    """`win` only ever ranks items WITHIN one god, so the number standing in
    for "no data" has to sit inside that god's distribution. A global constant
    compared against a per-god distribution is a units error."""
    build = _win_build(0.60, 0.62, 0.64)
    assert scoring.god_unknown_win_rate(build, {}) == pytest.approx(0.62)


def test_unknown_win_falls_back_when_the_god_has_no_record():
    """No distribution to sit inside, so the global constant is the honest
    answer rather than a fabricated one."""
    assert scoring.god_unknown_win_rate({"builds": []}, {}) == scoring.UNKNOWN_WIN_RATE
    assert scoring.god_unknown_win_rate(None, {}) == scoring.UNKNOWN_WIN_RATE


def test_unknown_win_can_be_switched_back_to_the_flat_constant():
    build = _win_build(0.60, 0.62, 0.64)
    off = {"unknown_win_per_god": False}
    assert scoring.god_unknown_win_rate(build, off) == scoring.UNKNOWN_WIN_RATE


def test_unknown_win_respects_an_explicit_constant_when_per_god_is_off():
    build = _win_build(0.60, 0.62, 0.64)
    assert scoring.god_unknown_win_rate(
        build, {"unknown_win_per_god": False, "unknown_win_rate": 0.55}) == 0.55


def test_measured_win_rates_mirror_what_lookup_rates_hands_out():
    """One rate per ITEM, not per sighting. `lookup_rates` prefers a slot pick
    over an alternate and takes only the best alternate for an unslotted item,
    so a raw sweep of the entry both double-counts and includes sightings no
    item ever receives — and the imputed value would then be drawn from a
    different population than the values it stands in for."""
    build = _win_build(0.40, 0.80, alternates=[
        {"name": "S1", "pick_rate": 0.9, "win_rate": 0.10},   # S1 is slotted: 0.80 wins
        {"name": "Extra", "pick_rate": 0.2, "win_rate": 0.70},
    ])
    rates = scoring.measured_win_rates(build, {})
    assert rates == [0.40, 0.70, 0.80]
    assert 0.10 not in rates          # the alternate sighting of a slotted item


def test_an_unmeasured_item_scores_the_gods_median_not_a_half():
    """The end-to-end effect: `signal_score` is what actually consumes this."""
    build = _win_build(0.60, 0.62, 0.64)
    weights = scoring.load_weights_default()
    row = scoring.signal_score({"name": "Nobody", "stats": {"Strength": "40"}},
                               _god("G", "physical", "Carry", ["Carry"]),
                               build, 0.5, weights, [])
    assert row["win"] == pytest.approx(0.62)


def test_a_flavor_can_require_an_item_the_god_can_actually_build():
    """A mana-stack build is not an option for a god with no mana converter in
    their pool — it is an empty tab. Gated on the SCORED pool, not merely the
    buildable one: `is_buildable` lets a Strength converter through for all 87
    gods and only the damage filter keeps it off a mage."""
    weights = scoring.load_weights_default()
    weights["flavors"] = {"mana-stack": {"requires_item": ["Transcendence"],
                                         "stats": {"Max Mana": 1.0}}}
    items = [{"name": "Transcendence", "tier": 3,
              "stats": {"Strength": "35", "Max Mana": "250"}}]
    physical = _god("Ullr", "physical", "Carry", ["Carry"])
    magical = _god("Ra", "magical", "Mid", ["Mage"])
    assert "mana-stack" in scoring.eligible_flavors(physical, weights, items)
    # A Strength item never reaches a mage's scored pool.
    assert "mana-stack" not in scoring.eligible_flavors(magical, weights, items)


def test_a_requires_item_flavor_is_withheld_when_the_pool_is_unknown():
    """Without `items` the gate cannot be evaluated, so the flavor is withheld
    rather than offered on a guess."""
    weights = scoring.load_weights_default()
    weights["flavors"] = {"mana-stack": {"requires_item": ["Transcendence"]}}
    assert scoring.eligible_flavors(
        _god("Ullr", "physical", "Carry", ["Carry"]), weights) == []


# ── conversion_fit: Max Mana is worth what it converts into ────────────────

_TRANS = {"name": "Transcendence", "cost": 2900, "tier": 3, "stats": {"Strength": "30", "Max Mana": "300"},
          "passive": "+Strength equal to 3% of Mana from Items."}
_THOTH = {"name": "Book of Thoth", "cost": 2800, "tier": 3, "stats": {"Intelligence": "80", "Max Mana": "300"},
          "passive": "+Intelligence equal to 5% of Mana from Items."}


def test_converter_weight_follows_the_target_stat_not_the_converter():
    """The naive gate — "is a converter buildable" — is vacuous: Transcendence
    is physical and Book of Thoth magical, so the damage filter admits exactly
    one of them to all 87 gods. The weight has to come from the target."""
    w = scoring.load_weights_default()
    ullr = _god("Ullr", "physical", "Carry", ["Sharpshooter"])
    ymir = _god("Ymir", "magical", "Support", ["Tank"])
    items = [_TRANS, _THOTH]
    # Ullr sees only Transcendence (physical), and wants the Strength it makes.
    assert scoring.converter_stat_weights(
        ullr, items, {"Strength": 1.0}, w) == {"Max Mana": 1.0}
    # Ymir sees only Book of Thoth, and has no use for the Intelligence it
    # makes — so its mana is worth nothing to him and drops out entirely.
    assert scoring.converter_stat_weights(
        ymir, items, {"Max Health": 0.8, "Physical Protection": 1.0}, w) == {}


def test_converter_weight_reads_percentage_grants():
    """`_GRANT` keys a percentage grant as "Strength %"; the fit map is keyed
    on the bare stat, so the lookup has to strip the suffix or the whole class
    of percentage converters silently scores zero."""
    w = scoring.load_weights_default()
    item = {"name": "Pct", "cost": 2500, "tier": 3, "stats": {"Strength": "40", "Max Mana": "200"},
            "passive": "For every 100 Mana: +2% Strength"}
    got = scoring.converter_stat_weights(
        _god("X", "physical", "Carry", ["Sharpshooter"]), [item], {"Strength": 0.6}, w)
    assert got == {"Max Mana": 0.6}


def test_conversion_fit_off_by_default_leaves_the_map_alone():
    w = scoring.load_weights_default()
    assert w.get("conversion_fit", 0.0) == 0.0
    ullr = _god("Ullr", "physical", "Carry", ["Sharpshooter"])
    rows = scoring.score_god_items(ullr, [_TRANS], {}, {}, w, {})
    w2 = dict(w, conversion_fit=1.0)
    rows2 = scoring.score_god_items(ullr, [_TRANS], {}, {}, w2, {})
    assert rows2[0]["fit"] > rows[0]["fit"]


# ── Paid relics take one of the six ────────────────────────────────────────

def test_a_paid_relic_takes_a_core_slot_and_a_free_one_does_not():
    """The game gives a free slot to the BASE relic only; an upgraded relic is
    bought with gold and occupies one of the six.

    The old rule excluded relics by TIER, justified in the docstring as "what
    the game actually says", which was simply wrong. The community data settles
    it: across the tracked six-item builds Shell of Rebuke appears 62 times and
    the one free relic in the pool (Blink Rune, cost 0) appears zero times."""
    paid = {"name": "Shell of Rebuke", "tier": "Relic", "cost": 2500,
            "stats": {"Magical Protection": "20", "Physical Protection": "20"}}
    free = {"name": "Some Base Relic", "tier": "Relic", "cost": 0,
            "stats": {"Magical Protection": "20"}}
    assert scoring.is_buildable(paid) is True
    assert scoring.is_buildable(free) is False


def test_a_statless_paid_relic_is_still_excluded():
    """Blinking Abyss (2600g, no stats) has 20 community sightings and stays
    out — by the STATLESS rule, not the relic rule. That is a known blindness
    (nothing here can score an item with no stats) rather than a claim about
    the game, and it is the honest place for it to fail."""
    assert scoring.is_buildable(
        {"name": "Blinking Abyss", "tier": "Relic", "cost": 2600, "stats": {}}) is False


def test_a_relic_with_an_unreadable_cost_is_not_assumed_buildable():
    """`cost: None` is a scrape failure, not a price. Defaulting it to buildable
    would let a mis-scraped relic into every build in the game."""
    assert scoring.is_buildable(
        {"name": "Mystery", "tier": "Relic", "cost": None, "stats": {"Strength": "10"}}) is False


def test_the_real_pool_admits_exactly_the_paid_statted_relics():
    from smite import recommend
    items = recommend.load_items()
    relics = [i for i in items if i.get("tier") == "Relic"]
    assert relics, "expected relics in the pool"
    admitted = sorted(i["name"] for i in relics if scoring.is_buildable(i))
    assert admitted == ["Agility Greaves", "Shell of Rebuke",
                        "Talisman of Purification", "Time-lock Aegis"], admitted


# --- offense tags + adaptive fit -------------------------------------------

def _pow_god(name="T", dt="physical"):
    return {"name": name, "damage_type": dt, "role": "Hunter", "specs": []}


def _w(**over):
    w = scoring.load_weights_default()
    w.update(over)
    return w


def test_offense_tags_are_configurable_rather_than_hardcoded():
    """They lived as a set literal in god_fit_score until 2026-08-19, which
    made them the one tag weight not in _weights.yaml."""
    item = {"name": "X", "cost": 2400, "stats": {"Strength": "40"}}
    plain = scoring.god_fit_score(item, _pow_god(), _w(offense_tags={}), ["burst"])
    bonus = scoring.god_fit_score(item, _pow_god(),
                                  _w(offense_tags={"burst": 0.1}), ["burst"])
    assert bonus > plain


def test_offense_tags_sum_only_when_additive_is_on():
    """Flat, an item answering a tank two ways scores what one answering it
    once does — the rule that let Titan's Bane displace Heartseeker."""
    item = {"name": "X", "cost": 2400, "stats": {"Strength": "40"}}
    tags = ["burst", "percent-health"]
    om = {"burst": 0.1, "percent-health": 0.1}
    flat = scoring.god_fit_score(item, _pow_god(),
                                 _w(offense_tags=om, offense_tags_additive=False), tags)
    add = scoring.god_fit_score(item, _pow_god(),
                                _w(offense_tags=om, offense_tags_additive=True), tags)
    one = scoring.god_fit_score(item, _pow_god(),
                                _w(offense_tags=om, offense_tags_additive=False), ["burst"])
    assert flat == one
    assert add > flat


def test_adaptive_fit_is_a_true_no_op_at_zero():
    """It ships off; a non-zero cost while off would be a bug, not a trade."""
    item = {"name": "Omen", "cost": 2800, "stats": {"Echo": "30"}}
    off = scoring.god_fit_score(item, _pow_god(), _w(adaptive_fit=0.0), [],
                                adaptive_grant=72.5)
    bare = scoring.god_fit_score(item, _pow_god(), _w(adaptive_fit=0.0), [])
    assert off == bare


def test_adaptive_fit_credits_the_power_stat_the_god_actually_wants():
    """The grant is one good taken as whichever stat suits, so it lands on the
    higher-weighted of Strength/Intelligence, not on both."""
    item = {"name": "Omen", "cost": 2800, "stats": {"Echo": "30"}}
    on = scoring.god_fit_score(item, _pow_god(), _w(adaptive_fit=1.0), [],
                               adaptive_grant=72.5)
    assert on > 0.0


def test_adaptive_fit_strength_is_a_scale_not_a_switch():
    """It first shipped injecting the grant into `stats`, which cannot scale:
    with `magnitude_fit` off `stat_reference` is None and `share` is 1.0
    whatever the value, so 0.15 and 1.0 produced identical scores. The register
    recorded the resulting sweep as "an exact no-op at every strength", which
    had measured one behaviour five times."""
    item = {"name": "Omen", "cost": 2800, "stats": {"Echo": "30"}}
    fit = lambda s: scoring.god_fit_score(
        item, _pow_god(), _w(adaptive_fit=s), [], adaptive_grant=72.5)
    weak, mid, full = fit(0.15), fit(0.5), fit(1.0)
    assert 0.0 < weak < mid < full, (weak, mid, full)


def test_adaptive_fit_does_not_top_up_a_stat_the_item_really_carries():
    """The grant substitutes for a missing stat. An item that already lists the
    power keeps its own value — crediting both would pay twice for one stat."""
    carries = {"name": "Real", "cost": 2800, "stats": {"Strength": "40"}}
    with_grant = scoring.god_fit_score(carries, _pow_god(), _w(adaptive_fit=1.0), [],
                                       adaptive_grant=72.5)
    without = scoring.god_fit_score(carries, _pow_god(), _w(adaptive_fit=1.0), [])
    assert with_grant == without
