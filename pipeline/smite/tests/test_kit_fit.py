"""`kit_fit`: does a god's kit use an item well (2026-11-03)."""
from smite import kit_fit, recommend
from smite.tests.test_side_by_side import toy_god


def _items():
    return {i["name"]: i for i in recommend.load_items()}


def _gods():
    return {g["name"]: g for g in recommend.load_gods()}


def test_lotus_sickle_needs_a_kit_that_helps_an_ally():
    it = _items()["Lotus Sickle"]
    assert "Ability Buffed, Healed, or Shielded another Allied God" in it["passive"]
    assert kit_fit.item_needs(it) == {"ally_support"}


def test_agni_cannot_use_lotus_sickle_and_ra_can():
    """The case that held Lotus Sickle at [] (data/_tags.yaml)."""
    g = _gods()
    assert not kit_fit.capabilities(g["Agni"])["ally_support"]
    assert kit_fit.capabilities(g["Ra"])["ally_support"]
    ok, why = kit_fit.fits(g["Agni"], _items()["Lotus Sickle"], 1.0, 0.0)
    assert not ok and "needs ally_support" in why


def test_an_aura_for_nearby_allies_is_met_by_melee_or_ally_support():
    it = _items()["Shogun's Ofuda"]
    assert kit_fit.item_needs(it) == {"near_allies"}
    melee = toy_god(melee=True)
    ranged = toy_god(melee=False)
    assert kit_fit.fits(melee, it, 1.0, 0.0)[0]
    assert not kit_fit.fits(ranged, it, 1.0, 0.0)[0]


def test_anti_heal_needs_no_capability_only_stat_fit():
    it = _items()["Toxic Blade"]
    assert kit_fit.item_needs(it) == set()
    assert kit_fit.fits(toy_god(), it, 0.5, 0.4)[0]
    ok, why = kit_fit.fits(toy_god(), it, 0.3, 0.4)
    assert not ok and why[0].startswith("stat fit")


def test_the_floor_is_the_least_fit_item_already_in_the_core():
    assert kit_fit.fit_floor({"A": 0.9, "B": 0.4, "C": 0.7}, ["A", "B", "C", "Gone"]) == 0.4
    assert kit_fit.fit_floor({}, []) == 0.0
