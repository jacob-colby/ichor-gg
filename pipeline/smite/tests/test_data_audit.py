import json

from smite import data_audit


def _clean_item(name="Clean Item", tier=1, cost=650):
    return {
        "name": name,
        "tier": tier,
        "cost": cost,
        "stats": {"Max Health": "200", "Lifesteal": "4%"},
    }


def test_clean_items_have_no_findings():
    items = [_clean_item("A", tier=1, cost=650), _clean_item("B", tier=2, cost=1200)]
    assert data_audit.audit_items(items) == []


def test_blank_cost_flagged():
    items = [dict(_clean_item("Blank Cost Item"), cost=None)]
    findings = data_audit.audit_items(items)
    assert any(f["item"] == "Blank Cost Item" and f["issue"] == "blank-cost" for f in findings)


def test_blank_cost_flags_zero_and_missing():
    items = [
        dict(_clean_item("Zero Cost Item"), cost=0),
        {k: v for k, v in _clean_item("Missing Cost Item").items() if k != "cost"},
    ]
    findings = data_audit.audit_items(items)
    flagged = {f["item"] for f in findings if f["issue"] == "blank-cost"}
    assert flagged == {"Zero Cost Item", "Missing Cost Item"}


def test_null_tier_flagged():
    items = [dict(_clean_item("Null Tier Item"), tier=None)]
    findings = data_audit.audit_items(items)
    assert any(f["item"] == "Null Tier Item" and f["issue"] == "null-tier" for f in findings)


def test_numeric_tier_empty_stats_flagged():
    items = [dict(_clean_item("Empty Stats Item"), stats={})]
    findings = data_audit.audit_items(items)
    assert any(f["item"] == "Empty Stats Item" and f["issue"] == "empty-stats" for f in findings)


def test_glyph_empty_stats_not_flagged():
    items = [dict(_clean_item("Pure Utility Glyph", tier="Glyph"), stats={})]
    findings = data_audit.audit_items(items)
    assert findings == []


def test_bad_stat_value_too_large():
    items = [dict(_clean_item("Overflow Stat Item"), stats={"Max Health": "99999"})]
    findings = data_audit.audit_items(items)
    matches = [f for f in findings if f["item"] == "Overflow Stat Item" and f["issue"] == "bad-stat-value"]
    assert len(matches) == 1
    assert "Max Health" in matches[0]["detail"]
    assert "99999" in matches[0]["detail"]


def test_bad_stat_value_negative():
    items = [dict(_clean_item("Negative Stat Item"), stats={"Physical Power": "-5"})]
    findings = data_audit.audit_items(items)
    matches = [f for f in findings if f["item"] == "Negative Stat Item" and f["issue"] == "bad-stat-value"]
    assert len(matches) == 1
    assert "Physical Power" in matches[0]["detail"]
    assert "-5" in matches[0]["detail"]


def test_bad_stat_value_non_numeric():
    items = [dict(_clean_item("Non Numeric Stat Item"), stats={"Passive": "n/a"})]
    findings = data_audit.audit_items(items)
    assert any(f["item"] == "Non Numeric Stat Item" and f["issue"] == "bad-stat-value" for f in findings)


def test_tier3_cost_outlier():
    items = [dict(_clean_item("Outlier Tier3 Item", tier=3), cost=5000)]
    findings = data_audit.audit_items(items)
    matches = [f for f in findings if f["item"] == "Outlier Tier3 Item" and f["issue"] == "tier3-cost-outlier"]
    assert len(matches) == 1
    assert "5000" in matches[0]["detail"]


def test_tier3_cost_within_range_not_flagged():
    items = [dict(_clean_item("In Range Tier3 Item", tier=3), cost=2600)]
    findings = data_audit.audit_items(items)
    assert not any(f["issue"] == "tier3-cost-outlier" for f in findings)


def test_duplicate_name_flagged():
    items = [_clean_item("Repeated Item", tier=1, cost=650), _clean_item("Repeated Item", tier=2, cost=1200)]
    findings = data_audit.audit_items(items)
    dupes = [f for f in findings if f["item"] == "Repeated Item" and f["issue"] == "duplicate-name"]
    assert len(dupes) == 2


def test_two_items_missing_name_are_not_duplicates_of_each_other():
    missing_name_item = {k: v for k, v in _clean_item("placeholder").items() if k != "name"}
    items = [dict(missing_name_item), dict(missing_name_item)]
    findings = data_audit.audit_items(items)
    assert not any(f["issue"] == "duplicate-name" for f in findings)


def test_stat_value_boundary_1000_clean_1001_flagged():
    clean = dict(_clean_item("Boundary Stat Clean"), stats={"Max Health": "1000"})
    flagged = dict(_clean_item("Boundary Stat Flagged"), stats={"Max Health": "1001"})
    findings = data_audit.audit_items([clean, flagged])
    assert not any(f["item"] == "Boundary Stat Clean" for f in findings)
    assert any(f["item"] == "Boundary Stat Flagged" and f["issue"] == "bad-stat-value" for f in findings)


def test_tier3_cost_boundary_1800_and_4000_clean():
    items = [
        dict(_clean_item("Tier3 Min Boundary", tier=3), cost=1800),
        dict(_clean_item("Tier3 Max Boundary", tier=3), cost=4000),
    ]
    findings = data_audit.audit_items(items)
    assert not any(f["issue"] == "tier3-cost-outlier" for f in findings)


def test_tier3_cost_boundary_1799_and_4001_flagged():
    items = [
        dict(_clean_item("Tier3 Below Min", tier=3), cost=1799),
        dict(_clean_item("Tier3 Above Max", tier=3), cost=4001),
    ]
    findings = data_audit.audit_items(items)
    outliers = {f["item"] for f in findings if f["issue"] == "tier3-cost-outlier"}
    assert outliers == {"Tier3 Below Min", "Tier3 Above Max"}


def test_malformed_stats_type_does_not_crash():
    items = [dict(_clean_item("Malformed Stats Item"), stats=["not", "a", "dict"])]
    findings = data_audit.audit_items(items)
    assert not any(f["issue"] == "bad-stat-value" for f in findings)


def test_findings_are_sorted_by_item_then_issue():
    items = [
        dict(_clean_item("Zeta Item"), cost=None, tier=None),
        dict(_clean_item("Alpha Item"), cost=None),
    ]
    findings = data_audit.audit_items(items)
    keys = [(f["item"], f["issue"]) for f in findings]
    assert keys == sorted(keys)


# --- audit_gods -----------------------------------------------------------

def _mag_god(name="Mage"):
    return {"name": name, "damage_type": "magical"}


_GODS_ITEMS = [
    {"name": "Staff", "tier": 3, "cost": 3000, "stats": {"Intelligence": "70"}},
    {"name": "Boots", "tier": 3, "cost": 2000, "stats": {"Max Health": "100"}},
    {"name": "Sword", "tier": 3, "cost": 2400, "stats": {"Strength": "40"}},
]


def _core_build(god="Mage", slots=None, starter="Conduit Gem", mode="Conquest"):
    if slots is None:
        slots = ["Staff", "Boots", "Staff", "Boots", "Staff"]
    entry = {"source": "suggested", "archetype": "core", "slot_order": slots}
    if starter is not None:
        entry["starter"] = {"base": starter}
    return {"god": god, "mode": mode, "builds": [entry]}


def test_audit_gods_clean_build_has_no_findings():
    findings = data_audit.audit_gods([_mag_god()], [_core_build()], _GODS_ITEMS)
    assert findings == []


def test_audit_gods_flags_missing_build():
    findings = data_audit.audit_gods([_mag_god()], [], _GODS_ITEMS)
    assert [f["issue"] for f in findings] == ["no-build"]


def test_audit_gods_flags_short_build():
    build = _core_build(slots=["Staff", "Boots", "Staff", "Boots"])  # 4 < 5
    findings = data_audit.audit_gods([_mag_god()], [build], _GODS_ITEMS)
    assert any(f["issue"] == "short-build" for f in findings)


def test_audit_gods_flags_missing_starter():
    build = _core_build(starter=None)
    findings = data_audit.audit_gods([_mag_god()], [build], _GODS_ITEMS)
    assert any(f["issue"] == "no-starter" for f in findings)


def test_audit_gods_flags_wrong_damage_item():
    # Sword (Strength -> physical) has no place in a magical god's core build.
    build = _core_build(slots=["Staff", "Boots", "Sword", "Boots", "Staff"])
    findings = data_audit.audit_gods([_mag_god()], [build], _GODS_ITEMS)
    wrong = [f for f in findings if f["issue"] == "wrong-damage-item"]
    assert wrong and wrong[0]["detail"].startswith("Sword")


def test_audit_gods_only_considers_conquest_core():
    # A non-Conquest build must not satisfy the coverage check.
    joust = _core_build(mode="Joust")
    findings = data_audit.audit_gods([_mag_god()], [joust], _GODS_ITEMS)
    assert [f["issue"] for f in findings] == ["no-build"]


# --- main -----------------------------------------------------------------

def _index(items=None, gods=None, builds=None):
    return {"items": items or [], "gods": gods or [], "builds": builds or []}


def test_main_returns_nonzero_when_item_findings_exist(monkeypatch):
    monkeypatch.setattr(
        data_audit, "_load_index",
        lambda: _index(items=[dict(_clean_item("Broken Item"), cost=None)]),
    )
    assert data_audit.main([]) == 1


def test_main_returns_nonzero_when_god_findings_exist(monkeypatch):
    monkeypatch.setattr(
        data_audit, "_load_index",
        lambda: _index(gods=[_mag_god()], builds=[], items=_GODS_ITEMS),
    )
    assert data_audit.main([]) == 1  # no-build for the god


def test_main_returns_zero_when_clean(monkeypatch):
    monkeypatch.setattr(
        data_audit, "_load_index",
        lambda: _index(
            items=[_clean_item("Clean Item Two", tier=1, cost=650)] + _GODS_ITEMS,
            gods=[_mag_god()],
            builds=[_core_build()],
        ),
    )
    assert data_audit.main([]) == 0


def test_main_returns_one_when_index_missing(monkeypatch):
    def _raise():
        raise FileNotFoundError("index.json not found")

    monkeypatch.setattr(data_audit, "_load_index", _raise)
    assert data_audit.main([]) == 1


def test_main_returns_one_when_index_corrupt(monkeypatch):
    def _raise():
        raise json.JSONDecodeError("bad json", "", 0)

    monkeypatch.setattr(data_audit, "_load_index", _raise)
    assert data_audit.main([]) == 1


def test_a_gods_ability_mod_is_not_a_blank_cost_finding():
    """Vulcan's five Mods are `God Specific`, cost 0, statless and level-gated
    — a kit upgrade the game grants, not an item anyone buys. Flagging them
    would add five permanent findings to a gate whose entire value is that a
    new finding means something, and every future god with the system would
    add five more."""
    mods = [{"name": "Thermal Mod", "tier": "God Specific", "cost": 0,
             "stats": {}, "god": "Vulcan"}]
    assert data_audit.audit_items(mods) == []


def test_a_statless_zero_cost_item_with_no_owner_is_still_flagged():
    """Blink Rune is nobody's ability mod. The exemption keys on the OWNER, so
    the failure that put a free statless item into 262 build slots still
    reports."""
    found = data_audit.audit_items(
        [{"name": "Blink Rune", "tier": "Relic", "cost": 0, "stats": {}}])
    assert [f["issue"] for f in found] == ["blank-cost"]


def test_an_unreadable_price_is_not_the_same_as_no_price():
    """Genie's Lamp matches the ability-mod shape in every respect except one:
    its cost is None, from the `-1` sentinel on the wiki, not 0. A Mod has no
    price because it is a kit upgrade; the Lamp has no price WE COULD READ.
    The second is worth keeping in front of a human, so the exemption tests
    `cost == 0` exactly rather than merely falsy."""
    lamp = [{"name": "Genie's Lamp", "tier": "God Specific", "cost": None,
             "stats": {}, "god": "Aladdin"}]
    assert [f["issue"] for f in data_audit.audit_items(lamp)] == ["blank-cost"]


def test_a_god_specific_item_that_costs_real_gold_is_unaffected():
    """Ratatoskr's acorns are bought. Only the zero-cost statless shape is
    exempt, so a genuinely missing price on a real item still reports."""
    acorn = [{"name": "Briskberry Acorn", "tier": "God Specific", "cost": 0,
              "stats": {"Strength": "45"}, "god": "Ratatoskr"}]
    assert [f["issue"] for f in data_audit.audit_items(acorn)] == ["blank-cost"]
