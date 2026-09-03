"""Tests for the passive-text parser.

The parser's job is knowing what it cannot read. Most of these pin a REFUSAL,
because a false "unconditional" overprices an item by its own headline number
while a false "conditional" costs one item's worth of signal.
"""
import pytest

from smite import efficiency, passives, notes, recommend, scoring


def _items():
    return [i for i in (notes.read_note(p)[0]
                        for p in (recommend.DATA_ROOT / "Items").glob("*.md"))
            if i.get("name") and scoring.is_buildable(i)]


def _item(name):
    return notes.read_note(recommend.DATA_ROOT / "Items" / f"{name}.md")[0]


# ── What it reads ─────────────────────────────────────────────────────────

def test_the_adaptive_grant_is_read_as_its_own_good():
    """Eight items grant 20-90 unconditional power the stat line never shows.
    It is one column, not Strength or Intelligence: you get whichever suits
    your build, and the two carry different gold prices, so folding it into
    either would pick a side of a coin the item never makes you flip."""
    grants = passives.unconditional_grants(_item("Daybreak Gavel"))
    assert grants == {passives.ADAPTIVE_KEY: 70.0}    # mean of +60 Str / +80 Int


def test_a_plain_unconditional_grant_is_read_with_its_unit():
    assert passives.unconditional_grants(_item("Deathbringer")) == \
        {"Critical Strike Damage %": 35.0}
    assert passives.unconditional_grants(_item("Shogun's Ofuda")) == \
        {"Attack Speed %": 20.0}


# ── What it refuses, which matters more ───────────────────────────────────

def test_an_on_use_buff_is_not_a_stat():
    """Avatar's Parashu grants +25% Strength for 10s on a 120s cooldown. At
    face value that is a quarter of your power; in practice it is a twelfth of
    the time. The honest discount needs uptime nobody has measured."""
    assert passives.unconditional_grants(_item("Avatar's Parashu")) == {}


def test_a_cap_is_not_a_grant():
    """Bancroft's Talon reads "Caps at +60 Intelligence" and ramps off MISSING
    health, so the 60 arrives only when you are nearly dead. The first version
    of this parser read it as a flat +60 and overpriced the item by its own
    headline number."""
    assert passives.unconditional_grants(_item("Bancroft's Talon")) == {}
    assert passives.is_conditional("Caps at +60 Intelligence")
    assert passives.is_conditional("bonus Intelligence scaled from missing Health")


def test_either_or_branches_are_not_summed():
    """The Cosmic Horror lists three alternatives — Echo above, below and equal
    to Cooldown Rate — of which you get one. The first version summed all
    three and credited the item with 40% Echo and 70 Intelligence."""
    assert passives.unconditional_grants(_item("The Cosmic Horror")) == {}


def test_an_item_with_no_passive_yields_nothing():
    assert passives.unconditional_grants({"name": "x"}) == {}
    assert passives.unconditional_grants({"name": "x", "passive": "   "}) == {}


def test_it_refuses_far_more_than_it_reads():
    """The parser reaches 10 of 129 passives. That ratio is the finding, not a
    shortfall to fix — 56% of passives state no stat and no damage number at
    all, and inventing values for reveals and silences would be worse than
    admitting the gap."""
    survey = passives.survey(_items())
    assert survey["with_passive"] >= 125
    assert survey["adaptive"] == 8
    assert survey["parsed"] <= 15
    assert survey["conditional"] > 90


# ── Wiring ────────────────────────────────────────────────────────────────

def test_pricing_passives_is_off_by_default():
    """Measured at 51.0% -> 50.4% coverage. It prices items more sensibly and
    ranks them worse; see the module docstring for the likeliest reason."""
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    assert weights.get("price_passives") is False
    assert efficiency.PRICE_PASSIVES is False


def test_effective_stats_adds_to_a_stat_the_item_already_lists():
    """A passive granting what the stat line also grants stacks, because the
    game does."""
    base = {"Attack Speed %": 10.0}
    item = {"passive": "+20% Attack Speed for you and allies within 8.8m."}
    assert passives.effective_stats(item, base) == {"Attack Speed %": 30.0}


def test_the_flag_actually_changes_the_priced_stats():
    """Off is the default, not the only path — the measurement has to stay
    reproducible."""
    gavel = _item("Daybreak Gavel")
    assert passives.ADAPTIVE_KEY not in efficiency.item_stat_values(gavel)
    efficiency.PRICE_PASSIVES = True
    try:
        assert efficiency.item_stat_values(gavel)[passives.ADAPTIVE_KEY] == 70.0
    finally:
        efficiency.PRICE_PASSIVES = False


# ── Persistent vs transient stacks (shipped OFF — `price_stacks`) ───────────

def _p(text):
    return {"name": "X", "passive": text}


def test_a_farm_stacked_item_is_persistent():
    """Devourer's Gauntlet fills off minion kills and never drops a stack, so
    by mid-game its full-stack value is what you are actually playing with."""
    item = _p("Kill Minion or Jungle Monsters: +1 Stack. Each Stack grants: "
              "+.4 Strength +0.05% Lifesteal At 75 Stacks, gain: +10 Strength +3% Lifesteal")
    assert passives.is_persistent_stacker(item)
    g = passives.persistent_stack_grants(item)
    assert g["Strength"] == pytest.approx(75 * 0.4 + 10)          # 40
    assert g["Lifesteal %"] == pytest.approx(75 * 0.05 + 3)       # 6.75


def test_a_decimal_per_stack_value_is_not_cut_at_its_own_point():
    """"+.4 Strength" contains a period. Splitting the fragment on any "." cut
    it at the decimal and found no grants at all — the whole item read as
    worth nothing."""
    g = passives.persistent_stack_grants(
        _p("Each Stack grants: +.4 Strength Stacks up to 10"))
    assert g["Strength"] == pytest.approx(4.0)


@pytest.mark.parametrize("text", [
    "Per Stack: +8 Intelligence Max 5 Stacks. Stacks last 10s. Stacks fall off one at a time",
    "+1 Stack of: +30 Intelligence Stacks up to 6 times. On Death: Lose 4 Stacks.",
    "Melee hits grants 2 Stacks. Stacks up to 4 times. Buff lasts 2s.",
])
def test_a_transient_stack_is_refused(text):
    """A stack with a duration or a loss clause is worth some fraction of its
    number that depends on uptime nobody has measured. Counting it at face
    value would overprice exactly the items this is meant to help."""
    assert not passives.is_persistent_stacker(_p(text))
    assert passives.persistent_stack_grants(_p(text)) == {}


def test_bare_mana_in_prose_reads_as_max_mana():
    """The stats table says "Max Mana"; passive prose says "+10 Mana". Book of
    Thoth is 50 stacks of it and read as zero until these were reconciled."""
    g = passives.persistent_stack_grants(
        _p("Deal 900 Damage: +1 Mana Infusion Stack (Max 50 Stacks) "
           "Per Mana Infusion Stack: +10 Mana."))
    assert g == {"Max Mana": pytest.approx(500.0)}


def test_mana_regen_is_not_mistaken_for_mana():
    """"Mana Regen" is its own stat. The alias must not double-count it."""
    g = passives.persistent_stack_grants(
        _p("Each Stack grants: +2 Mana Regen Stacks up to 10"))
    assert g == {"Mana Regen": pytest.approx(20.0)}


def test_an_evolve_bonus_is_added_once_on_top_of_the_capped_stacks():
    g = passives.persistent_stack_grants(
        _p("Stacks grant +15 Max Health (max 40 Stacks). At 40 Stacks, "
           "Item evolves and gains: +100 Max Health"))
    assert g["Max Health"] == pytest.approx(40 * 15 + 100)


def test_an_item_with_no_per_stack_line_says_nothing_rather_than_a_fraction():
    """An evolve bonus alone is real but partial. Shipping half an item's
    value is the error this module exists to avoid."""
    assert passives.persistent_stack_grants(
        _p("Stacks up to 40. At 40 Stacks, Item evolves and gains: +100 Max Health")) == {}


def test_a_non_stacking_item_is_untouched():
    assert passives.persistent_stack_grants(_p("+20% Attack Speed")) == {}
    assert passives.persistent_stack_grants(_p("")) == {}


# ── Crit-damage multipliers (shipped ON — `price_crit_multipliers`) ─────────

def test_deathbringers_bonus_is_read_as_unconditional():
    assert passives.crit_damage_bonus(
        _p("+35% Critical Strike Damage.")) == pytest.approx(0.35)


@pytest.mark.parametrize("text", [
    "Critically Strike: +8% Ability Damage for 5s. Max 3 stacks",
    "Critically Strike: +30% Attack Speed for 3s.",
    "On Use: +35% Critical Strike Damage. Cooldown: 45s",
])
def test_a_triggered_crit_passive_is_refused(text):
    """Every crit passive in the pool except Deathbringer's is a trigger with a
    duration. `Critically Strike:` is a condition, not a standing bonus."""
    assert passives.crit_damage_bonus(_p(text)) == 0.0


def test_the_bonus_converts_to_equivalent_critical_chance():
    """Expected basic damage at crit chance C and multiplier M is 1 + C(M-1).
    Adding B moves M to M+B, so the extra chance buying the same at the base
    multiplier is C' = C*B/(M-1). Deathbringer: 0.20 * 0.35 / 0.50 = 14 points,
    on top of the 20 it lists."""
    item = {"name": "Deathbringer", "passive": "+35% Critical Strike Damage.",
            "stats": {"Strength": "45", "Critical Chance": "20%"}}
    assert passives.crit_damage_as_chance(item) == {"Critical Chance %": pytest.approx(14.0)}


def test_a_crit_damage_bonus_on_an_item_with_no_crit_chance_is_worth_nothing():
    """It multiplies a zero. Pricing it would invent value the item cannot
    deliver on its own."""
    item = {"name": "X", "passive": "+35% Critical Strike Damage.",
            "stats": {"Strength": "45"}}
    assert passives.crit_damage_as_chance(item) == {}


def test_conversion_does_not_recurse_through_the_pricing_path():
    """`efficiency.item_stat_values` calls this when the flag is on, so reading
    the item's crit chance back through that function recursed until the stack
    died. It reads the raw stat instead."""
    from smite import efficiency
    item = {"name": "Deathbringer", "passive": "+35% Critical Strike Damage.",
            "stats": {"Strength": "45", "Critical Chance": "20%"}}
    efficiency.PRICE_CRIT_MULTIPLIERS = True
    try:
        values = efficiency.item_stat_values(item)
    finally:
        efficiency.PRICE_CRIT_MULTIPLIERS = False
    assert values["Critical Chance %"] == pytest.approx(34.0)   # its own 20 + 14


# ---- Stat conversion (shipped ON — `price_conversions`) --------------------

REF = {"Max Mana": 500, "Intelligence": 325}


def _conv(passive, stats):
    return {"name": "X", "passive": passive, "stats": stats}


def test_the_percent_conversion_grammar():
    item = _conv("+Strength equal to 3% of Mana from Items.", {"Strength": "35"})
    assert passives.stat_conversions(item) == [("Max Mana", 0.03, {"Strength": 1.0})]
    assert passives.conversion_grants(item, REF) == {"Strength": pytest.approx(15.0)}


def test_the_per_unit_conversion_grammar():
    """`For every 10 Intelligence: +1 Attack Damage +1% Attack Speed` — a
    different sentence shape entirely from the `equal to N%` one."""
    item = _conv("For every 10 Intelligence: +1 Attack Damage +1% Attack Speed",
                 {"Attack Speed": "20%", "Attack Damage": "5"})
    src, rate, per = passives.stat_conversions(item)[0]
    assert (src, rate) == ("Intelligence", 1.0)
    assert per == {"Attack Damage": pytest.approx(0.1), "Attack Speed %": pytest.approx(0.1)}


def test_a_conditional_conversion_clause_is_not_counted():
    """Book of Thoth converts 5% of mana outright AND another 2% only "At 50
    Evolve Stacks". Read as one blob those sum to 7% and overprice the item for
    a build that has not stacked."""
    item = _conv("+Intelligence equal to 5% of Mana from Items. Deal 900 Damage: "
                 "+1 Stack. At 50 Evolve Stacks, Item evolves and gains: Additional "
                 "+Intelligence equal to 2% of Mana from Items",
                 {"Intelligence": "30"})
    assert passives.stat_conversions(item) == [("Max Mana", 0.05, {"Intelligence": 1.0})]


def test_a_conversion_into_a_stat_the_item_does_not_sell_is_skipped():
    """AMPLIFY ONLY. Rod of Tahuti turns Intelligence into more Intelligence,
    which anyone who bought it for the Intelligence wants. Nimble Ring turns it
    into ATTACK DAMAGE, worth market price only to a god who both stacks
    Intelligence and auto-attacks — and the gold model is god-agnostic. Priced
    in full it read -869 residual and reached 52 cores against 3 community
    builds in 87."""
    ring = _conv("For every 10 Intelligence: +1 Attack Damage +1% Attack Speed",
                 {"Intelligence": "35", "Attack Speed": "20%"})
    grants = passives.conversion_grants(ring, REF)
    assert "Attack Damage" not in grants          # not on its sheet
    assert grants["Attack Speed %"] == pytest.approx(32.5)


def test_a_non_converting_item_yields_nothing():
    assert passives.stat_conversions(_conv("+20% Attack Speed", {})) == []
    assert passives.conversion_grants(_conv("", {}), REF) == {}


def test_a_missing_reference_prices_nothing_rather_than_guessing():
    item = _conv("+Strength equal to 3% of Mana from Items.", {"Strength": "35"})
    assert passives.conversion_grants(item, {}) == {}
    assert passives.conversion_grants(item, {"Max Mana": 0}) == {}


def test_the_reference_is_measured_over_builds_that_carry_the_stat():
    """45 of 87 gods are physical and carry zero Intelligence, so a median over
    every build is 0 — which would price Rod of Tahuti and Nimble Ring at
    nothing, the two items this exists to fix."""
    items = [{"name": "Mana", "stats": {"Max Mana": "300"}},
             {"name": "Int", "stats": {"Intelligence": "100"}},
             {"name": "Plain", "stats": {"Strength": "40"}}]
    builds = [
        {"builds": [{"source": "community",
                     "slot_order": [{"name": "Int"}, {"name": "Mana"}]}]},
        {"builds": [{"source": "community",
                     "slot_order": [{"name": "Plain"}, {"name": "Mana"}]}]},
    ]
    ref = passives.measure_conversion_reference(builds, items)
    assert ref["Intelligence"] == 100        # not 50 — the zero build is excluded
    assert ref["Max Mana"] == 300


def test_stack_fraction_prices_the_state_you_reach_not_the_tooltip():
    """`fraction` is how much of the cap a real match gets to. Kept
    parameterised after the conservative-pricing hypothesis was tested and
    refuted — see `stack_fraction` in _weights.yaml — because the sweep is
    cheap to re-run and the next hypothesis will want it."""
    item = _p("Kill Minion: +1 Stack. Each Stack grants: +.4 Strength "
              "At 75 Stacks, gain: +10 Strength")
    full = passives.persistent_stack_grants(item)
    assert full["Strength"] == pytest.approx(75 * 0.4 + 10)
    half = passives.persistent_stack_grants(item, 0.5)
    # Both the per-stack total and the at-cap bonus scale: a build that never
    # reaches the cap never evolves either.
    assert half["Strength"] == pytest.approx(75 * 0.4 * 0.5 + 10 * 0.5)


def test_stack_fraction_defaults_to_the_cap_and_clamps():
    item = _p("Each Stack grants: +1 Strength Stacks up to 10")
    assert passives.persistent_stack_grants(item)["Strength"] == pytest.approx(10)
    assert passives.persistent_stack_grants(item, 2.0)["Strength"] == pytest.approx(10)
    assert passives.persistent_stack_grants(item, -1)["Strength"] == pytest.approx(0)


# ── The adaptive carve-out (shipped ON — `price_adaptive`) ─────────────────

def test_the_branch_is_taken_as_printed_not_as_the_mean():
    """`unconditional_grants` records the mean of the two branches because it
    prices the grant as its own god-agnostic column. This function exists to
    make the other choice, so it must take a side."""
    item = _p("Adaptive Stat: +55 Strength or +90 Intelligence "
              "(based on highest item stat).")
    assert passives.adaptive_grants(item, "strength") == {"Strength": 55.0}
    assert passives.adaptive_grants(item, "intelligence") == {"Intelligence": 90.0}
    assert passives.unconditional_grants(item)[passives.ADAPTIVE_KEY] == pytest.approx(72.5)


def test_an_item_with_no_adaptive_clause_gets_nothing():
    assert passives.adaptive_grants(_p("+20% Attack Speed")) == {}
    assert passives.adaptive_grants(_p("")) == {}
    assert passives.adaptive_grants({}) == {}


def test_an_unknown_branch_is_an_error_not_a_silent_default():
    """A typo in `adaptive_branch` must not quietly price the other stat for
    every gate that reads the file."""
    item = _p("Adaptive Stat: +55 Strength or +90 Intelligence.")
    with pytest.raises(ValueError):
        passives.adaptive_grants(item, "power")


def test_the_flag_prices_the_branch_into_a_real_regression_column():
    """Into Strength/Intelligence, which the whole pool constrains — not into
    a column only these items carry. See MIN_STAT_CARRIERS for the defect that
    rules out."""
    item = {"name": "Omen Drum", "cost": 2800, "tier": 3, "stats": {"Echo": "30"},
            "passive": "Adaptive Stat: +55 Strength or +90 Intelligence "
                       "(based on highest item stat)."}
    before = efficiency.apply_pricing_flags(
        {"price_adaptive": True, "adaptive_branch": "strength"})
    try:
        assert efficiency.item_stat_values(item) == {"Echo": 30.0, "Strength": 55.0}
        efficiency.apply_pricing_flags(
            {"price_adaptive": True, "adaptive_branch": "intelligence"})
        assert efficiency.item_stat_values(item) == {"Echo": 30.0, "Intelligence": 90.0}
        efficiency.apply_pricing_flags({})
        assert efficiency.item_stat_values(item) == {"Echo": 30.0}
    finally:
        efficiency.restore_pricing_flags(before)


def test_price_passives_supersedes_it_rather_than_double_counting():
    """Both flags read the SAME clause. `price_passives` prices it as an
    `Adaptive Power` column; running both would count the grant twice, at two
    different prices, on 29 items."""
    item = {"name": "Omen Drum", "cost": 2800, "tier": 3, "stats": {"Echo": "30"},
            "passive": "Adaptive Stat: +55 Strength or +90 Intelligence "
                       "(based on highest item stat)."}
    before = efficiency.apply_pricing_flags(
        {"price_passives": True, "price_adaptive": True})
    try:
        values = efficiency.item_stat_values(item)
        assert values == {"Echo": 30.0, passives.ADAPTIVE_KEY: pytest.approx(72.5)}
        assert "Strength" not in values
    finally:
        efficiency.restore_pricing_flags(before)


def test_the_flag_ships_on_and_the_gates_can_see_it():
    """A flag only `recommend.main` applies is a flag that measures nothing —
    `apply_pricing_flags` exists because that bug has happened here before."""
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    assert weights.get("price_adaptive") is True
    assert weights.get("adaptive_branch") == "strength"
    before = efficiency.apply_pricing_flags(weights)
    try:
        assert efficiency.PRICE_ADAPTIVE is True
        assert efficiency.ADAPTIVE_BRANCH == "strength"
    finally:
        efficiency.restore_pricing_flags(before)


def test_every_adaptive_item_is_priced_not_just_the_buildable_eight():
    """The regression pool keeps components on purpose (`efficiency_pool`), and
    17 of the 29 clause-carriers are in it. Pricing only the tier-3 eight would
    leave the same unexplained cost in the intercept for the other nine."""
    items = [i for i in (notes.read_note(p)[0]
                         for p in (recommend.DATA_ROOT / "Items").glob("*.md"))
             if i.get("name")]
    carriers = [i for i in items if passives.adaptive_grants(i)]
    assert len(carriers) == 29
    priced = [i for i in efficiency.efficiency_pool(items) if passives.adaptive_grants(i)]
    assert len(priced) == 17
    assert sum(1 for i in priced if i.get("tier") == 3) == 8


def test_only_the_standing_clause_counts_when_an_item_has_two():
    """Daybreak Gavel grants +60/+80 outright AND another +13/+16 "for 8s per
    Stack". Both are written in the adaptive grammar; only the first is a
    standing grant, and the `Adaptive Stat:` cue is what separates them."""
    gavel = _item("Daybreak Gavel")
    assert "+13 Strength or +16 Intelligence" in gavel["passive"]
    assert passives.adaptive_grants(gavel, "strength") == {"Strength": 60.0}
    assert passives.adaptive_grants(gavel, "intelligence") == {"Intelligence": 80.0}


# ── "% of all Stats from Items" (catalogue class A2) ───────────────────────

def test_the_flat_multiplier_is_read_and_needs_no_level():
    shell = _p("+7.5% of all Stats from Items. On Use: Create a field of rebuke "
               "for allies that mitigates 35% Damage. Cooldown: 120s")
    assert passives.all_stats_multiplier(shell) == pytest.approx(0.075)
    aegis = _p("+6% of all Stats from Items. On Use: Become time-locked")
    assert passives.all_stats_multiplier(aegis) == pytest.approx(0.06)


def test_a_per_level_multiplier_needs_a_level_and_is_zero_without_one():
    """Genie's Lamp. The scorer states no level, so `item_stat_values` passes
    none and the Lamp prices at nothing there — pinned, not assumed."""
    lamp = _p("+0.6% (per Level) of all Stats from Items. On Use: Access 3 Wishes")
    assert passives.all_stats_multiplier(lamp) == 0.0
    assert passives.all_stats_multiplier(lamp, level=20) == pytest.approx(0.12)
    assert passives.multiplier_grants(lamp, {"Strength": 100.0}) == {}
    assert passives.multiplier_grants(lamp, {"Strength": 100.0}, level=20) == {
        "Strength": pytest.approx(12.0)}


def test_an_item_without_the_clause_gets_nothing():
    assert passives.all_stats_multiplier(_p("+35% Critical Strike Damage.")) == 0.0
    assert passives.multiplier_grants(_p("+35% Critical Strike Damage."),
                                      {"Strength": 100.0}) == {}
    assert passives.multiplier_grants(_p("+7.5% of all Stats from Items"), {}) == {}


def test_the_grant_is_every_column_of_the_reference_scaled():
    shell = _p("+7.5% of all Stats from Items.")
    ref = {"Strength": 40.0, "Max Health": 500.0, "Pathfinding": 0.0}
    out = passives.multiplier_grants(shell, ref)
    assert out == {"Strength": pytest.approx(3.0), "Max Health": pytest.approx(37.5)}


def test_the_reference_is_the_pool_mean_over_tier_3_items_times_five():
    """Item data only — relics (the items being priced) and components are
    out, zeros count in the mean, and the keys carry the regression's unit."""
    items = [
        {"name": "A", "tier": 3, "cost": 2500, "stats": {"Strength": "40", "Attack Speed": "20%"}},
        {"name": "B", "tier": 3, "cost": 2500, "stats": {"Strength": "20"}},
        {"name": "Relic", "tier": "Relic", "cost": 2500, "stats": {"Physical Protection": "20"}},
        {"name": "Comp", "tier": 2, "cost": 900, "stats": {"Strength": "100"}},
    ]
    ref = passives.measure_multiplier_reference(items)
    assert ref == {"Attack Speed %": pytest.approx(10.0 * 5),
                   "Strength": pytest.approx(30.0 * 5)}
    assert passives.measure_multiplier_reference([]) == {}


def test_the_flag_prices_the_clause_through_item_stat_values_and_is_a_no_op_off():
    from smite import efficiency
    shell = {"name": "Shell of Rebuke", "tier": "Relic", "cost": 2500,
             "stats": {"Magical Protection": "20", "Physical Protection": "20"},
             "passive": "+7.5% of all Stats from Items. On Use: Create a field"}
    ref = {"Strength": 40.0, "Physical Protection": 40.0}
    before = efficiency.apply_pricing_flags({})
    try:
        off = efficiency.item_stat_values(shell)
        efficiency.apply_pricing_flags({"price_stat_multipliers": True,
                                        "multiplier_reference": ref})
        on = efficiency.item_stat_values(shell)
        # Without a reference the flag prices nothing rather than guessing.
        efficiency.apply_pricing_flags({"price_stat_multipliers": True})
        bare = efficiency.item_stat_values(shell)
    finally:
        efficiency.restore_pricing_flags(before)
    assert off == {"Magical Protection": 20.0, "Physical Protection": 20.0}
    assert bare == off
    assert on == {"Magical Protection": 20.0,
                  "Physical Protection": pytest.approx(20.0 + 3.0),
                  "Strength": pytest.approx(3.0)}


def test_the_shipped_reference_is_the_re_derivation_not_a_typed_number():
    """`multiplier_reference` in _weights.yaml is a measurement and a wiki
    refresh can move it; this fails when it has, so it is re-measured rather
    than quietly outliving its data."""
    from smite import recommend, scoring
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    stored = weights.get("multiplier_reference") or {}
    live = passives.measure_multiplier_reference(recommend.load_items())
    assert set(stored) == set(live)
    for key, value in live.items():
        assert stored[key] == pytest.approx(value, abs=0.01), key


def test_exactly_four_buildable_items_carry_the_flat_clause_and_the_lamp_the_per_level_one():
    from smite import recommend, scoring
    items = recommend.load_items()
    flat = sorted(it["name"] for it in items
                  if scoring.is_buildable(it) and passives.all_stats_multiplier(it) > 0)
    assert flat == ["Agility Greaves", "Shell of Rebuke",
                    "Talisman of Purification", "Time-lock Aegis"]
    lamp = next(it for it in items if it["name"] == "Genie's Lamp")
    assert passives.all_stats_multiplier(lamp) == 0.0
    assert passives.all_stats_multiplier(lamp, level=20) == pytest.approx(0.12)
    assert not scoring.is_buildable(lamp)


# ── Flat on-hit damage (catalogue class B1, unconditional members) ─────────

def test_the_flat_on_hit_grant_is_read_from_both_grammars():
    tyrfing = _p("Attacks deal +15 bonus Physical Damage. On God hit: Increase bonus "
                 "Damage by +15 for 4s Stacks once, +1 Stack per 4 Levels (Max 6 Stacks)")
    assert passives.on_hit_flat_damage(tyrfing) == 15.0        # the ramp is not counted
    golden = _p("Attacks deal bonus Physical Damage. Damage = +10 + 20% of your Item "
                "Protections Damages all Enemies within 2.5m")
    assert passives.on_hit_flat_damage(golden) == 10.0         # the protections term is not
    bragi = _p("Attack Hit: +10 (+3 per Level) bonus Magical Damage. Structures and "
               "Bosses take half damage from Bragi's Harp")
    assert passives.on_hit_flat_damage(bragi) == 10.0          # the per-Level term is not
    assert passives.on_hit_grants(tyrfing) == {"Attack Damage": 15.0}


def test_a_gated_or_scaled_on_hit_clause_is_refused():
    for text in (
        "Ability Used: Your next Attack deals bonus Magical Damage Damage = 80% of your "
        "Intelligence Cooldown: 2s",                                   # Polynomicon, per cast
        "Every fourth Attack Hit: Trigger Chain Lightning. Damage = 15 (+60% Attack Damage) "
        "Physical Damage",                                             # Odysseus', a rate
        "Attack Hit: +Bonus Physical Damage. Bonus Damage = +2% Target Base Health",  # Qin's
        "Store 25% of your Lifesteal healing as bonus Magical Damage on your next Attack.",
        "On Attack Hit: 25% bonus Physical Damage to Enemies within 1.92m of the target",
        "+35% Critical Strike Damage.",
    ):
        assert passives.on_hit_flat_damage(_p(text)) == 0.0, text
        assert passives.on_hit_grants(_p(text)) == {}


def test_price_on_hit_lands_in_the_attack_damage_column_and_is_a_no_op_off():
    from smite import efficiency
    tyrfing = {"name": "Tyrfing", "tier": 3, "cost": 2400,
               "stats": {"Strength": "25", "Attack Damage": "25", "Attack Speed": "10%"},
               "passive": "Attacks deal +15 bonus Physical Damage. On God hit: +15 for 4s"}
    before = efficiency.apply_pricing_flags({})
    try:
        off = efficiency.item_stat_values(tyrfing)
        efficiency.apply_pricing_flags({"price_on_hit": True})
        on = efficiency.item_stat_values(tyrfing)
    finally:
        efficiency.restore_pricing_flags(before)
    assert off == {"Strength": 25.0, "Attack Damage": 25.0, "Attack Speed %": 10.0}
    assert on == {"Strength": 25.0, "Attack Damage": 40.0, "Attack Speed %": 10.0}


def test_exactly_three_items_in_the_whole_item_set_carry_a_flat_on_hit_clause():
    """The survey the flag rests on, re-run rather than trusted: no component
    carries one, so the regression pool sees only these three."""
    from smite import recommend
    carriers = sorted((it["name"], passives.on_hit_flat_damage(it))
                      for it in recommend.load_items() if passives.on_hit_flat_damage(it) > 0)
    assert carriers == [("Bragi's Harp", 10.0), ("Golden Blade", 10.0), ("Tyrfing", 15.0)]
