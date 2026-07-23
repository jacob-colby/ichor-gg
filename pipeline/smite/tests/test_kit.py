from smite import kit


def _ability(slot, *details):
    return {"slot": slot, "details": list(details)}


def _god(damage_type, abilities):
    return {"name": "X", "damage_type": damage_type, "abilities": abilities}


def test_scaling_profile_parses_percent_stat_lines():
    god = _god("magical", [
        _ability("Basic Attack", "Damage Scaling: 100% Strength + 20% Intelligence"),
        _ability("1st Ability", "Damage Scaling: 70% Intelligence + 45% Strength"),
        _ability("2nd Ability", "Damage Scaling: 80% Intelligence"),
        _ability("Passive", "Damage Scaling: 175% Basic Attack Damage"),
    ])
    p = kit.scaling_profile(god)
    assert p["n_scaling_abilities"] == 3            # Basic Attack slot excluded
    assert p["int_share"] > p["str_share"]
    assert p["str_share"] + p["int_share"] == 1.0
    assert 0.0 < p["basic_attack_share"] < 1.0      # Frostbite-style 175% BAD


def test_scaling_profile_empty_kit_is_all_zero():
    p = kit.scaling_profile(_god("physical", []))
    assert p == {"str_share": 0.0, "int_share": 0.0,
                 "basic_attack_share": 0.0, "n_scaling_abilities": 0}


def test_overlay_low_confidence_returns_empty():
    # Ullr's stance kit scrapes only 1 scaling ability — fall back to role map.
    god = _god("physical", [_ability("1st Ability", "Damage Scaling: 100% Strength")])
    assert kit.kit_stat_overlay(kit.scaling_profile(god), god) == {}


def test_overlay_ability_kit_boosts_cdr_and_pen():
    god = _god("magical", [
        _ability("1st Ability", "Damage Scaling: 80% Intelligence"),
        _ability("2nd Ability", "Damage Scaling: 70% Intelligence"),
        _ability("Ultimate", "Damage Scaling: 120% Intelligence"),
    ])
    ov = kit.kit_stat_overlay(kit.scaling_profile(god), god)
    assert ov["Intelligence"] > 1.0                 # 0.6 + 0.6 * share=1.0
    assert ov["Cooldown Rate"] == 0.6
    assert ov["Penetration"] == 0.8
    assert "Attack Speed" not in ov


def test_overlay_basic_attack_kit_boosts_attack_speed_and_crit():
    god = _god("physical", [
        _ability("Passive", "Damage Scaling: 175% Basic Attack Damage"),
        _ability("1st Ability", "Damage Scaling: 100% Basic Attack Damage"),
        _ability("2nd Ability", "Damage Scaling: 60% Strength"),
    ])
    ov = kit.kit_stat_overlay(kit.scaling_profile(god), god)
    assert ov["Attack Speed"] > 0.5
    assert ov["Critical Chance"] > 0.4              # physical only
