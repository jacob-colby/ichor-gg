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
