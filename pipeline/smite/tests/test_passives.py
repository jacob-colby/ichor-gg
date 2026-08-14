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
