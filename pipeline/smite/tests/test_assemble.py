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


# ── Stat caps ─────────────────────────────────────────────────────────────

def _capped(name, tenacity):
    return {"name": name, "tier": 3, "cost": 2500, "stats": {"Tenacity": str(tenacity)}}


def test_refuses_an_item_whose_whole_contribution_is_capped_out():
    """Tenacity caps at 50 and the real items give 15 each, so a fourth buys
    nothing. Synthetic here because the rule does not currently fire on real
    data — four Tenacity items never out-score the pool."""
    items = [_capped(f"T{i}", 25) for i in range(4)]
    rows = [{"item": it["name"], "total": 1.0 - i * 0.01, "tags": []}
            for i, it in enumerate(items)]
    by_name = {it["name"]: it for it in items}
    core = assemble.assemble_core(rows, by_name, n=4, stat_caps={"Tenacity": 50})
    # Two items reach the cap exactly; the third and fourth are pure waste.
    assert core == ["T0", "T1"]


def test_allows_an_item_that_only_partly_overflows():
    """45 + 15 wastes 10 and buys 5. Refusing it would be the bigger error."""
    items = [_capped("A", 45), _capped("B", 15)]
    rows = [{"item": "A", "total": 1.0, "tags": []}, {"item": "B", "total": 0.9, "tags": []}]
    core = assemble.assemble_core(rows, {i["name"]: i for i in items}, n=2,
                                  stat_caps={"Tenacity": 50})
    assert core == ["A", "B"]


def test_an_item_carrying_an_uncapped_stat_too_is_still_taken():
    """The guard asks whether EVERY capped stat is maxed. An item that also
    brings Strength is not dead weight just because its Tenacity is."""
    items = [_capped("A", 50),
             {"name": "B", "tier": 3, "cost": 2500,
              "stats": {"Tenacity": "15", "Strength": "40"}}]
    rows = [{"item": "A", "total": 1.0, "tags": []}, {"item": "B", "total": 0.9, "tags": []}]
    core = assemble.assemble_core(rows, {i["name"]: i for i in items}, n=2,
                                  stat_caps={"Tenacity": 50})
    assert core == ["A", "B"]


def test_no_stat_caps_means_no_filtering():
    items = [_capped(f"T{i}", 25) for i in range(3)]
    rows = [{"item": it["name"], "total": 1.0, "tags": []} for it in items]
    core = assemble.assemble_core(rows, {i["name"]: i for i in items}, n=3)
    assert len(core) == 3


def test_a_rejected_item_does_not_consume_the_boots_slot():
    """Latent bug: `have_boots` was set before the lifesteal guard ran, so a
    boots-and-lifesteal item rejected for sustain still burned the boots slot
    and blocked every later boots item. No item is both today; the ordering is
    the fix."""
    both = {"name": "Sustaining Boots", "tier": 3, "cost": 2500,
            "stats": {"Movement Speed": "18", "Lifesteal": "10%"}}
    boots = {"name": "Plain Boots", "tier": 3, "cost": 2500, "stats": {"Movement Speed": "18"}}
    rows = [{"item": "Sustaining Boots", "total": 1.0, "tags": []},
            {"item": "Plain Boots", "total": 0.9, "tags": []}]
    by_name = {i["name"]: i for i in (both, boots)}
    core = assemble.assemble_core(rows, by_name, n=2, max_lifesteal=0)
    assert core == ["Plain Boots"]


# ── Build coherence (shipped OFF — see `coherence` in _weights.yaml) ────────

def _stats(**kw):
    return {"stats": {k.replace("_", " "): str(v) for k, v in kw.items()}}


def test_coherence_multiplier_is_a_no_op_at_zero_strength():
    """The shipped setting. It has to be exactly 1.0, not approximately, or
    every core would drift the moment the term was merely present."""
    item = _stats(Penetration=20)
    assert assemble.coherence_multiplier(item, {"Penetration": 100}, {"Penetration": 20}, 0.0) == 1.0


def test_coherence_multiplier_discounts_a_stat_the_core_already_holds():
    ref = {"Penetration": 20}
    item = _stats(Penetration=20)
    fresh = assemble.coherence_multiplier(item, {}, ref, 1.0)
    third = assemble.coherence_multiplier(item, {"Penetration": 40}, ref, 1.0)
    assert fresh == 1.0                       # nothing held yet
    assert 0.0 < third < fresh                # diminishing, never zero


def test_coherence_multiplier_is_not_dragged_by_a_token_stat():
    """An item that is mostly protections but carries 5 Strength must not be
    judged as a Strength item just because the core is Strength-heavy."""
    ref = {"Strength": 40, "Physical Protection": 50}
    item = {"stats": {"Physical Protection": "60", "Strength": "5"}}
    m = assemble.coherence_multiplier(item, {"Strength": 200}, ref, 1.0)
    assert m > 0.85


def test_coherence_multiplier_handles_a_stat_no_other_item_carries():
    """No reference magnitude means no yardstick. Counting it as zero would
    make a unique stat weigh nothing and silently skew the average."""
    item = _stats(Echo=1)
    assert assemble.coherence_multiplier(item, {}, {}, 1.0) == 1.0


def test_coherence_multiplier_survives_a_statless_item():
    assert assemble.coherence_multiplier({}, {"Strength": 100}, {"Strength": 40}, 1.0) == 1.0


def test_assemble_core_ignores_coherence_when_it_is_off():
    """Off must mean byte-identical to the pre-coherence path, since that is
    what every shipped build was measured against."""
    items = {
        "A": _stats(Penetration=20), "B": _stats(Penetration=20),
        "C": _stats(Strength=40), "D": _stats(Max_Health=200),
    }
    rows = [{"item": n, "total": t} for n, t in
            (("A", 0.9), ("B", 0.85), ("C", 0.6), ("D", 0.5))]
    assert assemble.assemble_core(rows, items, n=3) == ["A", "B", "C"]
    assert assemble.assemble_core(rows, items, n=3, coherence=0.0) == ["A", "B", "C"]


def test_assemble_core_reorders_once_coherence_is_on():
    """B duplicates A's whole stat line; C brings something new at a lower raw
    score. With the term on, C takes the slot."""
    items = {
        "A": _stats(Penetration=20), "B": _stats(Penetration=20),
        "C": _stats(Strength=40),
    }
    rows = [{"item": n, "total": t} for n, t in (("A", 0.9), ("B", 0.85), ("C", 0.6))]
    ref = {"Penetration": 20, "Strength": 40}
    core = assemble.assemble_core(rows, items, n=2, coherence=1.0, stat_reference=ref)
    assert core == ["A", "C"]


def test_assemble_core_still_honours_its_hard_guards_under_coherence():
    """Coherence re-ranks; it must not become a way past the one-boots rule."""
    items = {
        "Boots1": _stats(Movement_Speed=18, Strength=30),
        "Boots2": _stats(Movement_Speed=18, Intelligence=60),
        "Plain": _stats(Max_Health=250),
    }
    rows = [{"item": n, "total": t} for n, t in
            (("Boots1", 0.9), ("Boots2", 0.88), ("Plain", 0.1))]
    core = assemble.assemble_core(rows, items, n=2, coherence=1.0,
                                  stat_reference={"Movement Speed": 18})
    assert core == ["Boots1", "Plain"]
