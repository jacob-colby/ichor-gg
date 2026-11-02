"""`community_target`: which community slots are a comparison target."""
import inspect
import re

from smite import assemble, build_index, community_target as ct, recommend, scoring

ITEMS = {
    "Deathbringer": {"name": "Deathbringer", "tier": 3, "cost": 2800, "stats": {"Strength": "60"}},
    "Evil Eye": {"name": "Evil Eye", "tier": 2, "cost": 1300, "stats": {"Strength": "20"}},
    "Blinking Abyss": {"name": "Blinking Abyss", "tier": "Relic", "cost": 2600, "stats": {}},
    "Shell of Rebuke": {"name": "Shell of Rebuke", "tier": "Relic", "cost": 2500,
                        "stats": {"Physical Protection": "40"}},
    "Thermal Mod": {"name": "Thermal Mod", "tier": "God Specific", "cost": 0, "stats": {}, "god": "Vulcan"},
    "Briskberry Acorn": {"name": "Briskberry Acorn", "tier": "God Specific", "cost": 2400,
                         "stats": {"Strength": "45"}, "god": "Ratatoskr"},
}


def test_each_slot_lands_in_its_class():
    assert ct.slot_class(ITEMS["Deathbringer"]) == ct.SCORED
    assert ct.slot_class(ITEMS["Evil Eye"]) == ct.UNFINISHED          # a component, even with stats
    assert ct.slot_class(ITEMS["Blinking Abyss"]) == ct.UNSCOREABLE   # statless relic
    assert ct.slot_class(ITEMS["Shell of Rebuke"]) == ct.SCORED       # paid relic WITH stats is scored
    assert ct.slot_class(ITEMS["Thermal Mod"], "Vulcan") == ct.UNSCOREABLE
    assert ct.slot_class(ITEMS["Briskberry Acorn"], "Ratatoskr") == ct.SCORED
    assert ct.slot_class(None) == ct.UNKNOWN


def test_agreement_drops_components_and_sets_unscoreable_apart():
    slots = [{"name": n} for n in ("Deathbringer", "Shell of Rebuke", "Blinking Abyss", "Evil Eye")]
    a = ct.agreement(["Deathbringer", "Other"], slots, ITEMS)
    assert (a["raw_slots"], a["raw_shared"], a["raw_disagree"]) == (4, 1, 3)
    assert (a["target"], a["shared"], a["disagree"]) == (2, 1, 1)
    assert a["unfinished"] == ["Evil Eye"] and a["unscoreable"] == ["Blinking Abyss"]


def test_pooled_reports_the_share_that_was_never_a_disagreement():
    slots = [{"name": n} for n in ("Deathbringer", "Blinking Abyss", "Evil Eye")]
    p = ct.pooled({"G": ct.agreement([], slots, ITEMS)})
    assert p["raw_disagree"] == 3 and p["disagree"] == 1
    assert abs(p["not_a_disagreement"] - 2 / 3) < 1e-9


_IMPORTS = re.compile(r"^[ \t]*(?:from[ \t]+[\w.]+[ \t]+import[ \t]+[^#]*\bcommunity_target\b"
                      r"|(?:from|import)[ \t]+[\w.]*\bcommunity_target\b)", re.M)


def test_the_recommender_never_reads_it():
    """A comparison lens: what the site recommends must not depend on it."""
    for mod in (scoring, assemble, recommend, build_index):
        assert not _IMPORTS.search(inspect.getsource(mod)), mod.__name__
