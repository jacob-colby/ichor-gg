from smite import analysis, scoring


def _items():
    return [
        {"name": f"Item{i}", "tier": 3, "cost": 2500,
         "stats": {"Strength": str(30 + i)}, "passive": ""}
        for i in range(12)
    ] + [{"name": "MetaDarling", "tier": 3, "cost": 2500,
          "stats": {"Magical Protection": "60"}, "passive": "Nearby allies gain 15 Strength."}]


def _god():
    return {"name": "G", "damage_type": "physical", "role": "Carry",
            "specializations": ["Sharpshooter"], "abilities": []}


def _build(community):
    return {"builds": [{"source": "community", "slot_order": community}]}


def test_missed_meta_flags_high_pick_items_we_rank_low():
    items = _items()
    eff = {it["name"]: {"score": 0.9 if it["name"] != "MetaDarling" else 0.1, "tier": "fair"}
           for it in items}
    build = _build([{"name": "MetaDarling", "pick_rate": 0.6, "win_rate": 0.55}])
    out = analysis.god_disagreements(
        _god(), items, build, scoring.load_weights_default(), {}, eff,
        {it["name"]: it for it in items})
    assert [m["item"] for m in out["missed_meta"]] == ["MetaDarling"]
    assert out["missed_meta"][0]["pick"] == 0.6


def test_off_meta_flags_core_items_nobody_picks():
    items = _items()
    eff = {it["name"]: {"score": 0.9, "tier": "fair"} for it in items}
    build = _build([{"name": "Item0", "pick_rate": 0.5, "win_rate": 0.5}])
    out = analysis.god_disagreements(
        _god(), items, build, scoring.load_weights_default(), {}, eff,
        {it["name"]: it for it in items})
    # 6-item core, only Item0 has community pick — the other 5 are off-meta.
    assert len(out["off_meta"]) >= 5
