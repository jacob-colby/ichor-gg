"""The Solo/Support Lifesteal fit weights sit inside the healing bracket."""
from smite import lifesteal_value as lv, recommend, scoring, side_by_side as sbs


def test_shipped_lifesteal_weights_are_between_the_one_fight_and_chained_bounds():
    items, gods, weights, tags_map, builds = sbs.load_inputs()
    one, _ = lv.role_ratios(gods, items, builds, heal_until=sbs.WINDOW)
    chained, _ = lv.role_ratios(gods, items, builds)
    rs = scoring.load_weights(recommend.WEIGHTS_PATH)["role_stats"]
    defaults = scoring.load_weights_default()["role_stats"]
    for role in ("Solo", "Support"):
        hp = {**defaults[role], **rs[role]}.get("Max Health")
        lo, hi = one[role][0] * hp, chained[role][0] * hp
        assert lo < rs[role]["Lifesteal"] < hi, (role, lo, rs[role]["Lifesteal"], hi)


def test_a_role_with_no_health_weight_gets_no_lifesteal_weight():
    rs = scoring.load_weights(recommend.WEIGHTS_PATH)["role_stats"]
    for role in ("Jungle", "Mid"):
        assert "Lifesteal" not in (rs.get(role) or {})
