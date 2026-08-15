import pytest
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


# ---- Mode economy: how much of the scoring window an item is active for ----

ARENA = {"start_gold": 1250, "gold_per_min": 900, "match_minutes": 17.5, "uniformity": 0.6}
JOUST = {"start_gold": 1250, "gold_per_min": 690, "match_minutes": 22.5, "uniformity": 0.3}


def test_no_economy_is_a_no_op():
    """Conquest has no economy block, and a mode nobody has researched must be
    left alone rather than guessed at."""
    assert assemble.time_value_multiplier(2600, 10000, None) == 1.0
    assert assemble.time_value_multiplier(2600, 10000, {}) == 1.0


def test_zero_uniformity_is_a_no_op():
    """Conquest's Titan cannot fall early, so the sixth item is present for the
    fight that ends the game and keeps full value."""
    econ = {**ARENA, "uniformity": 0.0}
    assert assemble.time_value_multiplier(2600, 13000, econ) == 1.0


def test_an_item_bought_later_is_active_for_less_of_the_match():
    early = assemble.time_value_multiplier(2600, 0, ARENA)
    late = assemble.time_value_multiplier(2600, 13000, ARENA)
    assert early > late
    assert 0.0 < late < 1.0                      # a discount, never a ban


def test_a_cheaper_item_completes_sooner_and_weighs_more():
    """The only item-SPECIFIC term. Everything else at a given slot is common
    to all candidates and so cannot change which one is picked."""
    cheap = assemble.time_value_multiplier(2300, 7500, ARENA)
    dear = assemble.time_value_multiplier(3050, 7500, ARENA)
    assert cheap > dear


def test_arena_decays_harder_than_joust():
    """Arena's 500 tickets fall from 0:00, so value accrues uniformly and a
    late item misses most of the scoring. Joust has a Titan like Conquest, so
    its late items keep most of their worth."""
    a = assemble.time_value_multiplier(2600, 10000, ARENA)
    j = assemble.time_value_multiplier(2600, 10000, JOUST)
    assert a < j


def test_an_item_finishing_after_the_match_still_keeps_the_endgame_share():
    """Clamped at the uniformity floor, not at zero: even in Arena the last
    fight happens, so a sixth item is worth (1 - uniformity), never nothing."""
    m = assemble.time_value_multiplier(3000, 99999, ARENA)
    assert m == pytest.approx(1.0 - ARENA["uniformity"])


def test_assemble_core_prefers_earlier_power_under_an_economy():
    """Dear only wins on raw score; under Arena's decay the cheaper item that
    arrives sooner takes the slot."""
    items = {
        "Dear": {"cost": 3050, "stats": {"Strength": "60"}},
        "Cheap": {"cost": 2300, "stats": {"Intelligence": "60"}},
    }
    # A 3% score lead is not enough to survive arriving 750g later: measured
    # across the shipped Arena cores this trade fires 24 times in 87 builds and
    # drops the average item bought by 680g.
    narrow = [{"item": "Dear", "total": 0.520}, {"item": "Cheap", "total": 0.505}]
    assert assemble.assemble_core(narrow, items, n=1) == ["Dear"]
    assert assemble.assemble_core(narrow, items, n=1, economy=ARENA) == ["Cheap"]
    # A big enough lead still wins — this is a discount, not a cost cap.
    clear = [{"item": "Dear", "total": 0.60}, {"item": "Cheap", "total": 0.505}]
    assert assemble.assemble_core(clear, items, n=1, economy=ARENA) == ["Dear"]


def test_economy_still_honours_the_hard_guards():
    items = {
        "Boots1": {"cost": 2000, "stats": {"Movement Speed": "18"}},
        "Boots2": {"cost": 2100, "stats": {"Movement Speed": "18"}},
        "Plain": {"cost": 2500, "stats": {"Max Health": "250"}},
    }
    rows = [{"item": "Boots1", "total": 0.9}, {"item": "Boots2", "total": 0.88},
            {"item": "Plain", "total": 0.1}]
    assert assemble.assemble_core(rows, items, n=2, economy=ARENA) == ["Boots1", "Plain"]


# ---- Two-pass assembly (shipped OFF — `conversion_passes`) -----------------

# The bonus function's own arguments. `weight` is NOT among them — that
# belongs to the caller, which multiplies the bonus by the efficiency signal's
# weight so it enters the blended total exactly as efficiency does.
CONV = {"reference": {"Max Mana": 500}, "gold_values": {"Strength": 20.0},
        "span": 1000.0}
CONV_CTX = {**CONV, "weight": 1.0}


def _converter(cost=2400):
    return {"cost": cost, "stats": {"Strength": "35", "Max Mana": "250"},
            "passive": "+Strength equal to 3% of Mana from Items."}


def test_a_converter_in_a_mana_rich_core_is_marked_up():
    """3% of 1,550 mana is not 3% of a median 500. The one-pass reference
    prices the typical build; this is what corrects a build that is not it."""
    rich = assemble.conversion_score_bonus(_converter(), {"Max Mana": 1300}, **CONV)
    assert rich > 0


def test_a_converter_in_a_mana_poor_core_is_marked_down():
    """Symmetric on purpose — otherwise it is a one-way ratchet that only ever
    argues for more converters."""
    poor = assemble.conversion_score_bonus(_converter(), {}, **CONV)
    assert poor < 0


def test_a_non_converter_gets_no_bonus_either_way():
    plain = {"cost": 2500, "stats": {"Strength": "60"}, "passive": "+20% Attack Speed"}
    assert assemble.conversion_score_bonus(plain, {"Max Mana": 2000}, **CONV) == 0.0


def test_the_bonus_needs_a_reference_a_price_and_a_span():
    item = _converter()
    for missing in ({"reference": {}}, {"gold_values": {}}, {"span": 0}):
        assert assemble.conversion_score_bonus(item, {"Max Mana": 1300},
                                               **{**CONV, **missing}) == 0.0


def test_one_pass_is_the_plain_assembler():
    items = {"A": {"cost": 2500, "stats": {"Strength": "60"}},
             "B": {"cost": 2500, "stats": {"Strength": "50"}}}
    rows = [{"item": "A", "total": 0.9}, {"item": "B", "total": 0.8}]
    core, info = assemble.assemble_core_converged(rows, items, passes=1, n=2)
    assert core == assemble.assemble_core(rows, items, n=2)
    assert info == {"passes": 1, "converged": True, "oscillated": False}


def test_an_oscillating_build_returns_the_conservative_first_pass():
    """Adding a converter raises mana's value, which pulls in more mana items,
    which raises the converter again — the fixed point can be a two-cycle. When
    it is, the answer returned is pass one's, priced against a typical build,
    because that is the one that does not depend on which half of the cycle the
    loop stopped on."""
    calls = {"n": 0}
    real = assemble.assemble_core

    def flapping(rows, items_by_name, **kw):
        calls["n"] += 1
        return ["A", "B"] if calls["n"] % 2 else ["C", "D"]

    assemble.assemble_core = flapping
    try:
        core, info = assemble.assemble_core_converged(
            [], {}, passes=5, conversion=CONV_CTX)
    finally:
        assemble.assemble_core = real
    assert info["oscillated"] is True
    assert info["converged"] is False
    assert core == ["A", "B"]        # pass one's answer, not the cycle's
