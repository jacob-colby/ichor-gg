from smite import efficiency


def test_parse_stat_value_plain_number():
    assert efficiency.parse_stat_value("45") == 45.0


def test_parse_stat_value_percent_suffix():
    assert efficiency.parse_stat_value("20%") == 20.0


def test_parse_stat_value_whitespace():
    assert efficiency.parse_stat_value(" 10 ") == 10.0


def test_parse_stat_value_none_returns_none():
    assert efficiency.parse_stat_value(None) is None


def test_parse_stat_value_non_numeric_returns_none():
    assert efficiency.parse_stat_value("Aura") is None


import pytest


def _item(name, cost, **stats):
    return {"name": name, "cost": cost, "stats": {k: str(v) for k, v in stats.items()}}


def test_fit_gold_values_recovers_planted_coefficients():
    # cost = 20*Strength + 30*Intelligence exactly, no intercept.
    items = [
        _item("A", 2000, Strength=100),
        _item("B", 3000, Intelligence=100),
        _item("C", 2600, Strength=40, Intelligence=60),
        _item("D", 1000, Strength=50),
        _item("E", 1500, Intelligence=50),
    ]
    gold, stat_names = efficiency.fit_gold_values(items)
    assert gold["Strength"] == pytest.approx(20.0, abs=0.5)
    assert gold["Intelligence"] == pytest.approx(30.0, abs=0.5)
    assert set(stat_names) == {"Strength", "Intelligence"}


def test_fit_gold_values_coefficients_never_negative():
    items = [
        _item("A", 100, Strength=50, Intelligence=50),
        _item("B", 100, Strength=50, Intelligence=10),
        _item("C", 100, Strength=10, Intelligence=50),
    ]
    gold, _ = efficiency.fit_gold_values(items)
    assert all(v >= 0 for v in gold.values())


def test_fit_gold_values_ignores_items_with_missing_cost():
    # Real data has component items with cost: null (e.g. Evil Eye). They carry
    # no cost signal and must be excluded from the fit, not crash it.
    items = [
        _item("A", 2000, Strength=100),
        _item("B", 1000, Strength=50),
        {"name": "NoCost", "cost": None, "stats": {"Strength": "40"}},
    ]
    gold, stat_names = efficiency.fit_gold_values(items)
    assert gold["Strength"] == pytest.approx(20.0, abs=1.0)


def test_tier1_starters_excluded_from_gold_fit_and_scoring():
    # Starters (tier 1) are passive-priced: their gold buys an ability/adaptive
    # passive, not their token stats. Regressing 600g onto "1 Health Regen"
    # would poison the gold-per-stat fit, so tier-1 items must sit out both the
    # fit and the scored set (they keep their cost for display/audit).
    core = [
        {"name": "A", "tier": 3, "cost": 3000, "stats": {"Strength": "60"}},
        {"name": "B", "tier": 3, "cost": 2000, "stats": {"Strength": "40"}},
        {"name": "C", "tier": 2, "cost": 1200, "stats": {"Intelligence": "45"}},
    ]
    starter = {"name": "S", "tier": 1, "cost": 600, "stats": {"Health Regen": "1"}}
    gold_without, _ = efficiency.fit_gold_values(core)
    gold_with, _ = efficiency.fit_gold_values(core + [starter])
    assert gold_with == gold_without  # the starter did not perturb the fit
    scores, _ = efficiency.efficiency_scores(core + [starter])
    assert "S" not in scores  # tier-1 starter is not scored
    assert {"A", "B", "C"} <= set(scores)  # real items still scored


def test_components_stay_in_the_fit_and_sharpen_it():
    """A tier-2 component is scored and does move the fit — it is the evidence
    that lets a stat's price be identified apart from the bundles it always
    ships in. Narrowing this pool to finished items only cost the validation
    gate 3.3 points of coverage; see `efficiency_pool`."""
    finished = [
        {"name": "A", "tier": 3, "cost": 3000, "stats": {"Strength": "60"}},
        {"name": "B", "tier": 3, "cost": 2000, "stats": {"Strength": "40"}},
    ]
    component = {"name": "Sickle", "tier": 2, "cost": 1200, "stats": {"Strength": "10"}}
    assert component in efficiency.efficiency_pool(finished + [component])
    scores, _ = efficiency.efficiency_scores(finished + [component])
    assert "Sickle" in scores


def test_efficiency_scores_flags_underpriced_as_undervalued():
    items = [
        _item("A", 2000, Strength=100),
        _item("B", 2000, Strength=100),
        _item("C", 2000, Strength=100),
        _item("Fair", 2000, Strength=100),
        _item("Underpriced", 1000, Strength=100),
    ]
    scores, _gold = efficiency.efficiency_scores(items)
    assert scores["Underpriced"]["tier"] == "undervalued"
    assert scores["Underpriced"]["score"] > scores["Fair"]["score"]


def test_efficiency_scores_flags_passive_heavy_as_premium():
    items = [
        _item("A", 2000, Strength=100),
        _item("B", 2000, Strength=100),
        _item("C", 2000, Strength=100),
        _item("D", 2000, Strength=100),
        _item("PassiveHeavy", 3000, Strength=5),
    ]
    scores, _ = efficiency.efficiency_scores(items)
    assert scores["PassiveHeavy"]["tier"] == "premium"
    assert scores["PassiveHeavy"]["score"] < 0.5


def test_efficiency_scores_returns_score_in_unit_range():
    items = [_item("A", 2000, Strength=100), _item("B", 1000, Strength=100)]
    scores, _ = efficiency.efficiency_scores(items)
    for s in scores.values():
        assert 0.0 <= s["score"] <= 1.0


def test_efficiency_scores_skips_null_cost_items():
    # Component items with cost: null cannot get a residual; they must be absent
    # from the result, not crash it.
    items = [
        _item("A", 2000, Strength=100),
        _item("B", 1000, Strength=50),
        {"name": "NoCost", "cost": None, "stats": {"Strength": "40"}},
    ]
    scores, _ = efficiency.efficiency_scores(items)
    assert "NoCost" not in scores
    assert "A" in scores and "B" in scores


# ── Units are part of a stat's identity ───────────────────────────────────

def test_percent_and_flat_of_the_same_stat_are_priced_separately():
    """Penetration ships both ways. Regressed into one column, `10` and `10%`
    are charged the same gold — against a 300-protection target they're worth
    10 and 30. The split is not cosmetic: it moves every build that values
    penetration."""
    flat = {"name": "Flat", "cost": 2000, "tier": 3, "stats": {"Penetration": "20"}}
    pct = {"name": "Pct", "cost": 3000, "tier": 3, "stats": {"Penetration": "20%"}}
    # Two carriers each, so MIN_STAT_CARRIERS keeps both columns and this test
    # measures the flat/percent split rather than the identifiability floor.
    flat2 = {"name": "Flat2", "cost": 1000, "tier": 3, "stats": {"Penetration": "10"}}
    pct2 = {"name": "Pct2", "cost": 1500, "tier": 3, "stats": {"Penetration": "10%"}}
    names = efficiency.collect_stat_names([flat, pct, flat2, pct2])
    assert names == ["Penetration", "Penetration %"]
    assert efficiency.item_stat_values(flat) == {"Penetration": 20.0}
    assert efficiency.item_stat_values(pct) == {"Penetration %": 20.0}


def test_stat_key_leaves_unambiguous_stats_alone():
    assert efficiency.stat_key("Strength", "40") == "Strength"
    assert efficiency.stat_key("Lifesteal", "7.5%") == "Lifesteal %"


def test_predicted_cost_reads_the_same_columns_the_fit_wrote():
    """A price looked up under the bare name would silently read the wrong
    column — the failure mode the split exists to prevent."""
    pct = {"name": "Pct", "cost": 3000, "tier": 3, "stats": {"Penetration": "10%"}}
    gold = {"Penetration": 1.0, "Penetration %": 50.0, efficiency.INTERCEPT_KEY: 100.0}
    assert efficiency.predicted_cost(pct, gold) == 100.0 + 10 * 50.0


def test_shipped_penetration_columns_disagree_by_a_lot():
    """Guards the real fit: if these ever converge, either the split broke or
    the item data changed shape, and both are worth knowing about.

    The RATIO is not stable and must not be asserted tightly — it is a property
    of the current item set, not of the game. It read 4.5x when the split
    landed (8.63 vs 38.92 gold), and 1.9x after the twelve items the item list
    had never discovered joined the fit (27.1 vs 51.2). What the test defends
    is that the two columns stay far apart, which is the whole reason the
    split exists."""
    from smite import notes, recommend
    items = [notes.read_note(p)[0] for p in (recommend.DATA_ROOT / "Items").glob("*.md")]
    gold, _ = efficiency.fit_gold_values([i for i in items if i.get("name")])
    assert gold["Penetration %"] > 1.5 * gold["Penetration"]


def test_single_carrier_stat_gets_no_column():
    """A stat only one item carries is exactly determined — NNLS can always
    zero that item's residual — so it explains nothing and must not earn a
    column. Found via Agility Greaves, the lone Movement Speed carrier, priced
    at 299 gold/point (~13x Strength) purely to hit its own 2500 cost."""
    lonely = {"name": "Greaves", "cost": 2500, "tier": 3,
              "stats": {"Movement Speed": "5"}}
    shared = [{"name": f"S{i}", "cost": 2000, "tier": 3, "stats": {"Strength": "40"}}
              for i in range(3)]
    names = efficiency.collect_stat_names([lonely] + shared)
    assert "Movement Speed" not in names
    assert "Strength" in names


def test_dropped_column_leaves_the_item_unpriced_rather_than_mispriced():
    """The consequence of the rule, stated so it is a choice and not a
    surprise: the lone carrier loses credit for its stat and reads as
    premium. That is the honest outcome — we cannot price the stat — but it
    is why the floor sits at 2 instead of higher."""
    lonely = {"name": "Greaves", "cost": 2500, "tier": 3,
              "stats": {"Movement Speed": "5"}}
    shared = [{"name": f"S{i}", "cost": 1000 + 500 * i, "tier": 3,
               "stats": {"Strength": str(20 + 20 * i)}} for i in range(4)]
    gold, names = efficiency.fit_gold_values([lonely] + shared)
    assert "Movement Speed" not in gold
    # Predicted from the intercept alone, so it cannot look like a bargain.
    assert efficiency.predicted_cost(lonely, gold) < lonely["cost"]


def test_min_stat_carriers_keeps_thin_but_real_columns():
    """Echo (5 carriers) and Tenacity (6) are thin and genuinely identified.
    The floor must not reach them."""
    items = [{"name": f"E{i}", "cost": 2000, "tier": 3, "stats": {"Echo": "10"}}
             for i in range(efficiency.MIN_STAT_CARRIERS)]
    assert "Echo" in efficiency.collect_stat_names(items)


def test_pricing_flags_come_from_the_weights_the_gate_is_measuring():
    """These are module globals, and only `recommend.main` used to set them —
    so `calibrate` and `validate` scored every off-by-default experiment as OFF
    even when _weights.yaml turned it on. A gate that cannot see the config
    reports the shipped number for an unshipped model."""
    def snapshot():
        return (efficiency.PRICE_PASSIVES, efficiency.PRICE_STACKS,
                efficiency.PRICE_CRIT_MULTIPLIERS, efficiency.PRICE_CONVERSIONS,
                efficiency.PRICE_ADAPTIVE, efficiency.ADAPTIVE_BRANCH,
                dict(efficiency.CONVERSION_REFERENCE))

    before = efficiency.apply_pricing_flags(
        {"price_passives": True, "price_stacks": True,
         "price_crit_multipliers": True, "price_conversions": True,
         "price_adaptive": True, "adaptive_branch": "intelligence",
         "conversion_reference": {"Max Mana": 500}})
    try:
        assert snapshot() == (True, True, True, True, True, "intelligence",
                              {"Max Mana": 500})
        efficiency.apply_pricing_flags({})
        assert snapshot() == (False, False, False, False, False, "strength", {})
        # It returns the prior values so a sweep can restore them.
        prior = efficiency.apply_pricing_flags({"price_stacks": True})
        assert prior == {"PRICE_PASSIVES": False, "PRICE_STACKS": False,
                         "STACK_FRACTION": 1.0, "PRICE_CRIT_MULTIPLIERS": False,
                         "PRICE_CONVERSIONS": False, "CONVERSION_REFERENCE": {},
                         "PRICE_ADAPTIVE": False, "ADAPTIVE_BRANCH": "strength"}
    finally:
        efficiency.restore_pricing_flags(before)


def test_the_restore_contract_covers_every_switch():
    """`before` is a dict keyed by global name precisely so a switch added to
    `apply_pricing_flags` and forgotten in the return value fails here rather
    than leaving some sweep silently unable to put the module back."""
    import re
    import inspect
    src = inspect.getsource(efficiency.apply_pricing_flags)
    assigned = set(re.findall(r"^    ([A-Z_]+) = ", src, re.M))
    assert assigned == set(efficiency.PRICING_FLAGS)
    assert set(efficiency.apply_pricing_flags({})) == set(efficiency.PRICING_FLAGS)


def test_validate_applies_the_flags_before_fitting():
    """The regression path is what every gate goes through."""
    import inspect
    from smite import validate
    src = inspect.getsource(validate.compute)
    assert "apply_pricing_flags" in src
    assert src.index("apply_pricing_flags") < src.index("efficiency_scores(items)")


# ── offmap_efficiency (STATE.md §4.15) ────────────────────────────────────

def test_stat_base_strips_the_unit_the_regression_added():
    """The fit map is keyed on the plain name and the regression on the name
    with its unit. Anything comparing the two goes through `stat_base`, or it
    reads every percentage stat as absent from every role map."""
    assert efficiency.stat_base("Attack Speed %") == "Attack Speed"
    assert efficiency.stat_base("Penetration %") == "Penetration"
    assert efficiency.stat_base("Strength") == "Strength"


def test_efficiency_scores_carry_a_stat_gold_decomposition():
    """`stat_gold` has to reconstruct the item's own predicted cost, or the
    charge `offmap_adjusted_score` computes is not the one the residual used."""
    items = [_item("A", 2000, Strength=100), _item("B", 3000, Intelligence=100),
             _item("C", 2500, Strength=50, Intelligence=50)]
    for it in items:
        it["tier"] = 3
    scores, gold = efficiency.efficiency_scores(items)
    for it in items:
        row = scores[it["name"]]
        assert sum(row["stat_gold"].values()) + gold[efficiency.INTERCEPT_KEY] == \
            pytest.approx(efficiency.predicted_cost(it, gold))


def test_offmap_gold_counts_only_columns_the_map_does_not_name():
    row = {"stat_gold": {"Strength": 700.0, "Attack Speed %": 400.0,
                         "Physical Protection": 800.0}}
    assert efficiency.offmap_gold(row, {"Strength": 1.0, "Attack Speed": 1.3}) == 800.0
    # And the percentage column is matched through its base name, not skipped.
    assert efficiency.offmap_gold(row, {"Strength": 1.0}) == 1200.0
    assert efficiency.offmap_gold(row, {}) == 1900.0


def test_offmap_adjusted_score_is_an_exact_no_op_at_zero():
    row = {"score": 0.681, "span": 4000.0,
           "stat_gold": {"Physical Protection": 800.0}}
    assert efficiency.offmap_adjusted_score(row, {"Strength": 1.0}, 0.0) == 0.681


def test_offmap_adjusted_score_moves_with_its_strength():
    """Register §4.10's failure mode: a strength that is applied where nothing
    reads it measures one behaviour n times. This pins that it varies."""
    row = {"score": 0.8, "span": 1000.0, "stat_gold": {"Max Health": 200.0}}
    m = {"Strength": 1.0}
    assert efficiency.offmap_adjusted_score(row, m, 0.5) == pytest.approx(0.7)
    assert efficiency.offmap_adjusted_score(row, m, 1.0) == pytest.approx(0.6)


def test_offmap_adjusted_score_clamps_into_the_unit_range():
    row = {"score": 0.2, "span": 100.0, "stat_gold": {"Max Health": 900.0}}
    assert efficiency.offmap_adjusted_score(row, {"Strength": 1.0}, 1.0) == 0.0


def test_offmap_adjusted_score_leaves_an_empty_map_alone():
    """An empty map means "no information about what this god wants", never
    "this god wants nothing" — `archetype_bypass` flavors set one deliberately
    and `_role_stat_map` returns one for unseen role vocabulary. Charging it
    would collapse every item at once, on the gods the model knows least."""
    row = {"score": 0.7, "span": 1000.0, "stat_gold": {"Max Health": 400.0}}
    assert efficiency.offmap_adjusted_score(row, {}, 1.0) == 0.7
