import pytest

from smite import scoring


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


def test_score_god_items_excludes_components_and_wrong_damage_type():
    god = _god("Chiron", "physical", "Carry", ["Sharpshooter"])
    items = [
        {"name": "Final", "tier": 3, "stats": {"Strength": "40"}},
        {"name": "Active", "tier": None, "stats": {"Strength": "40"}},
        {"name": "Component", "tier": 2, "stats": {"Strength": "40"}},
        {"name": "WrongType", "tier": 3, "stats": {"Intelligence": "70"}},
    ]
    build = _community_build()
    eff = {n: {"score": 0.5, "tier": "fair"} for n in ["Final", "Active", "Component", "WrongType"]}
    rows = scoring.score_god_items(god, items, build, eff, scoring.load_weights_default(), {})
    names = {r["item"] for r in rows}
    assert names == {"Final", "Active"}   # component + wrong-damage excluded


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
