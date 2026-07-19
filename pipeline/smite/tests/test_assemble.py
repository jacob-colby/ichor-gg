from smite import assemble


def _row(name, total, tags=None):
    return {"item": name, "total": total, "tags": tags or [], "pick": 0.0}


def _items_by_name(*items):
    return {it["name"]: it for it in items}


def test_assemble_core_respects_constraints():
    rows = [_row("A", 0.9), _row("Boots1", 0.85), _row("Boots2", 0.84),
            _row("B", 0.8), _row("C", 0.7), _row("D", 0.6), _row("E", 0.5),
            _row("F", 0.4)]
    ibn = _items_by_name(
        {"name": "Boots1", "stats": {"Movement Speed": "18"}},
        {"name": "Boots2", "stats": {"Movement Speed": "18"}},
        {"name": "A", "stats": {"Strength": "40"}},
        {"name": "B", "stats": {"Strength": "40"}},
        {"name": "C", "stats": {"Strength": "40"}},
        {"name": "D", "stats": {"Strength": "40"}},
        {"name": "E", "stats": {"Strength": "40"}},
        {"name": "F", "stats": {"Strength": "40"}},
    )
    core = assemble.assemble_core(rows, ibn, n=6)
    assert len(core) == 6
    assert len(set(core)) == 6                       # no duplicates
    assert sum(1 for x in core if x.startswith("Boots")) == 1   # exactly one boots
    assert core[0] == "A"                            # highest score first


def test_assemble_core_respects_max_lifesteal():
    rows = [_row("LS1", 0.9, tags=["sustain"]), _row("LS2", 0.85, tags=["sustain"]),
            _row("A", 0.8), _row("B", 0.7), _row("C", 0.6), _row("D", 0.5), _row("E", 0.4)]
    ibn = _items_by_name(
        {"name": "LS1", "stats": {"Strength": "30"}}, {"name": "LS2", "stats": {"Strength": "30"}},
        {"name": "A", "stats": {"Strength": "40"}}, {"name": "B", "stats": {"Strength": "40"}},
        {"name": "C", "stats": {"Strength": "40"}}, {"name": "D", "stats": {"Strength": "40"}},
        {"name": "E", "stats": {"Strength": "40"}},
    )
    one = assemble.assemble_core(rows, ibn, n=6, max_lifesteal=1)
    assert sum(1 for x in one if x in {"LS1", "LS2"}) == 1
    two = assemble.assemble_core(rows, ibn, n=6, max_lifesteal=2)
    assert sum(1 for x in two if x in {"LS1", "LS2"}) == 2


def test_situational_table_reports_missing_tag():
    rows = [_row("A", 0.9), _row("B", 0.8)]
    ibn = _items_by_name(
        {"name": "A", "stats": {"Strength": "40"}},
        {"name": "B", "stats": {"Strength": "40"}},
    )
    table = assemble.situational_swaps(rows, ibn, tags_map={})
    sustain_row = next(r for r in table if r["vs_tag"] == "sustain")
    assert "no anti-heal" in sustain_row["swap"].lower()


def test_situational_table_picks_tagged_item():
    rows = [_row("A", 0.9), _row("Antiheal", 0.5, tags=["anti-heal"])]
    ibn = _items_by_name(
        {"name": "A", "stats": {"Strength": "40"}},
        {"name": "Antiheal", "stats": {"Strength": "30"}},
    )
    table = assemble.situational_swaps(rows, ibn, tags_map={"Antiheal": ["anti-heal"]})
    sustain_row = next(r for r in table if r["vs_tag"] == "sustain")
    assert "Antiheal" in sustain_row["swap"]


def test_situational_table_uses_only_viewer_vs_tags():
    rows = [_row("A", 0.9)]
    ibn = _items_by_name({"name": "A", "stats": {"Strength": "40"}})
    table = assemble.situational_swaps(rows, ibn, tags_map={})
    assert {r["vs_tag"] for r in table} == {"heavy_cc", "magic_heavy", "physical_heavy", "sustain"}


def test_situational_table_skips_items_already_in_core():
    # A qualifying item that's already in the core is not offered as a swap-in;
    # the row reports the core already covers it.
    rows = [_row("Cloak", 0.9, tags=["cc-immunity"])]
    ibn = _items_by_name({"name": "Cloak", "stats": {"Strength": "40"}})
    table = assemble.situational_swaps(rows, ibn, tags_map={"Cloak": ["cc-immunity"]}, core=["Cloak"])
    cc_row = next(r for r in table if r["vs_tag"] == "heavy_cc")
    assert "Cloak" in cc_row["swap"]
    assert "already covers" in cc_row["swap"]


def test_situational_table_does_not_repeat_same_item_across_rows():
    # One item qualifies for both magic and physical protection; it must not be
    # offered for both — the second row falls through to covered/none.
    rows = [_row("HybridDef", 0.9)]
    ibn = _items_by_name(
        {"name": "HybridDef", "stats": {"Magical Protection": "40", "Physical Protection": "40"}},
    )
    table = assemble.situational_swaps(rows, ibn, tags_map={})
    swaps_with_item = [r for r in table if "HybridDef" in r["swap"] and "already covers" not in r["swap"]]
    assert len(swaps_with_item) == 1   # claimed by exactly one situation, not both


def test_situational_swaps_include_swap_item_name():
    rows = [_row("A", 0.9), _row("Antiheal", 0.5, tags=["anti-heal"])]
    ibn = _items_by_name(
        {"name": "A", "stats": {"Strength": "40"}},
        {"name": "Antiheal", "stats": {"Strength": "30"}},
    )
    table = assemble.situational_swaps(rows, ibn, tags_map={"Antiheal": ["anti-heal"]})
    sustain = next(r for r in table if r["vs_tag"] == "sustain")
    assert sustain["swap_item"] == "Antiheal"
    cc = next(r for r in table if r["vs_tag"] == "heavy_cc")
    assert cc["swap_item"] is None


def test_assemble_core_require_seeds_minimum_stat_items():
    from smite.assemble import assemble_core
    items = {
        "Crit A": {"name": "Crit A", "stats": {"Critical Chance": "20%"}},
        "Crit B": {"name": "Crit B", "stats": {"Critical Chance": "20%"}},
        "Crit C": {"name": "Crit C", "stats": {"Critical Chance": "20%"}},
        "Pen X": {"name": "Pen X", "stats": {"Penetration": "15"}},
        "Pen Y": {"name": "Pen Y", "stats": {"Penetration": "15"}},
        "Pen Z": {"name": "Pen Z", "stats": {"Penetration": "15"}},
        "Pen W": {"name": "Pen W", "stats": {"Penetration": "15"}},
    }
    # Non-crit items score higher, so without `require` the core would be all pen.
    rows = [{"item": n, "tags": []} for n in
            ["Pen X", "Pen Y", "Pen Z", "Pen W", "Crit A", "Crit B", "Crit C"]]
    core = assemble_core(rows, items, n=6, require={"stat": "Critical Chance", "min": 3})
    crit_in_core = [n for n in core if "Critical Chance" in items[n]["stats"]]
    assert len(crit_in_core) >= 3
    assert len(core) == 6
    assert len(set(core)) == 6  # no dups


def test_assemble_core_require_handles_thin_pool():
    from smite.assemble import assemble_core
    items = {"Crit A": {"name": "Crit A", "stats": {"Critical Chance": "20%"}},
             "Pen X": {"name": "Pen X", "stats": {"Penetration": "15"}},
             "Pen Y": {"name": "Pen Y", "stats": {"Penetration": "15"}}}
    rows = [{"item": n, "tags": []} for n in ["Pen X", "Pen Y", "Crit A"]]
    core = assemble_core(rows, items, n=3, require={"stat": "Critical Chance", "min": 3})
    assert "Crit A" in core and len(core) == 3  # seeds the 1 available, fills rest


def test_build_order_sorts_cheap_early_aura_late():
    from smite.assemble import build_order
    items = {
        "Anti": {"name": "Anti", "cost": 2500, "stats": {}},
        "Aura": {"name": "Aura", "cost": 2500, "stats": {}},
        "Cheap": {"name": "Cheap", "cost": 1000, "stats": {}},
    }
    tags = {"Anti": ["anti-heal"], "Aura": ["aura"], "Cheap": []}
    weights = {"build_order": {"default_stage": 0, "cost_weight": 0.0004,
                               "tag_stage": {"anti-heal": -1, "aura": 1}}}
    order = build_order(["Aura", "Cheap", "Anti"], items, tags, weights)
    # Anti (stage -1+1.0) < Cheap (0.4) < Aura (1+1.0)
    assert order == ["Anti", "Cheap", "Aura"]


def test_flex_slots_are_lowest_scored_core():
    from smite.assemble import flex_slots
    core = ["A", "B", "C", "D", "E", "F"]  # rows are score-desc, so core is too
    rows = [{"item": n} for n in ["A", "B", "C", "D", "E", "F"]]
    assert flex_slots(core, rows, count=2) == ["E", "F"]
    assert set(flex_slots(core, rows, count=2)) <= set(core)
    assert flex_slots(["A"], [{"item": "A"}], count=2) == ["A"]
