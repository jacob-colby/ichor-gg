"""The 2026-09-03 claim vocabulary: four kinds beyond item membership.

`test_expert_review` pins the gate itself. This file pins the kinds that let it
hold more than "should this item be in the core": an ORDER, a matchup SWAP, a
build's COMPOSITION and an item PAIRING. Each reads only from the shipped index
and each can go `holds` — a kind that cannot fail is decoration, so every kind
here has a test that makes it fail.
"""
import pytest

from smite import expert_review
from smite.tests.test_expert_review import _index


def _rich_index(core, swaps=None, items=None, god="Ullr", role="Carry", mode="Conquest"):
    """One god with a core, its situational-swap rows and an item table."""
    entry = {"source": "suggested", "archetype": "core", "slot_order": list(core),
             "situational_swaps": list(swaps or [])}
    return {"builds": [{"god": god, "mode": mode, "builds": [entry]}],
            "gods": [{"name": god, "role": role}],
            "items": list(items or [])}


def _swap(vs, item):
    return {"vs_tag": vs, "swap": f"{item} — label", "swap_item": item}


def _covered(vs, item):
    return {"vs_tag": vs, "swap": f"core already covers label ({item})", "swap_item": None}


# buy-order -------------------------------------------------------------------

def _order(*names):
    return {"god": "Ullr", "mode": "Conquest", "claim": "buy-order",
            "detail": {"order": list(names)}}


def test_buy_order_clears_when_the_named_items_appear_in_that_order():
    index = _rich_index(["Transcendence", "Other", "Heartseeker", "More"])
    verdict, _ = expert_review.check(_order("Transcendence", "Heartseeker"), index)
    assert verdict == "clear"


def test_buy_order_holds_when_the_order_is_reversed():
    """The order is the least-evidenced part of the output — `build_order` is a
    tag-and-cost heuristic with no build-path data behind it — so an expert is
    the only instrument that can grade it."""
    index = _rich_index(["Heartseeker", "Other", "Transcendence"])
    verdict, why = expert_review.check(_order("Transcendence", "Heartseeker"), index)
    assert verdict == "holds"
    assert "Heartseeker" in why


def test_buy_order_is_partial_when_the_present_items_are_ordered_but_one_is_absent():
    index = _rich_index(["Transcendence", "Other", "Heartseeker"])
    verdict, why = expert_review.check(
        _order("Transcendence", "Hydra's Lament", "Heartseeker"), index)
    assert verdict == "partial"
    assert "Hydra's Lament" in why


def test_buy_order_holds_rather_than_falling_silent_when_the_items_leave_the_core():
    """An ordering claim whose items vanish has no subject. Reading that as
    `unchecked` would let a resolved claim stop being checked without a word;
    reading it as `holds` makes `--check` go red so a human looks."""
    index = _rich_index(["A", "B", "Transcendence"])
    verdict, why = expert_review.check(_order("Transcendence", "Heartseeker"), index)
    assert verdict == "holds"
    assert "fewer than two" in why


def test_buy_order_needs_at_least_two_items():
    with pytest.raises(ValueError, match="order"):
        expert_review.check(_order("Transcendence"), _rich_index(["Transcendence"]))


# situational-swap ------------------------------------------------------------

def _situ(vs, *items):
    return {"god": "Ullr", "mode": "Conquest", "claim": "situational-swap",
            "detail": {"vs": vs, "items": list(items)}}


def test_situational_swap_clears_when_the_row_names_the_item():
    index = _rich_index(["A"], swaps=[_swap("heavy_cc", "Avatar's Parashu")])
    assert expert_review.check(_situ("heavy_cc", "Avatar's Parashu"), index)[0] == "clear"


def test_situational_swap_clears_when_the_core_already_covers_it_with_the_item():
    """The row carries no `swap_item` in that case; the name is in the prose."""
    index = _rich_index(["Avatar's Parashu"], swaps=[_covered("heavy_cc", "Avatar's Parashu")])
    assert expert_review.check(_situ("heavy_cc", "Avatar's Parashu"), index)[0] == "clear"


def test_situational_swap_clears_when_the_item_is_simply_in_the_core():
    """"Bring X against heavy CC" is satisfied by a build that always brings X."""
    index = _rich_index(["Avatar's Parashu"], swaps=[_swap("heavy_cc", "Other")])
    verdict, why = expert_review.check(_situ("heavy_cc", "Avatar's Parashu"), index)
    assert verdict == "clear"
    assert "in the core" in why


def test_situational_swap_is_partial_when_the_item_is_filed_under_another_matchup():
    index = _rich_index(["A"], swaps=[_swap("heavy_cc", "Other"),
                                      _swap("sustain", "Avatar's Parashu")])
    verdict, why = expert_review.check(_situ("heavy_cc", "Avatar's Parashu"), index)
    assert verdict == "partial"
    assert "sustain" in why


def test_situational_swap_holds_when_the_row_picks_something_else():
    index = _rich_index(["A"], swaps=[_swap("heavy_cc", "Other")])
    verdict, why = expert_review.check(_situ("heavy_cc", "Avatar's Parashu"), index)
    assert verdict == "holds"
    assert "Other" in why


def test_situational_swap_holds_when_the_build_has_no_row_for_that_situation():
    """No advice at all is the objection standing, not an absence of evidence."""
    index = _rich_index(["A"], swaps=[])
    verdict, why = expert_review.check(_situ("heavy_cc", "Avatar's Parashu"), index)
    assert verdict == "holds"
    assert "no heavy_cc row" in why


def test_situational_swap_raises_on_a_situation_the_model_does_not_emit():
    """"Against a tanky comp" is not one of the four situations. Recording it
    would produce a claim nothing can check, and a typo in `vs` must be loud
    for the same reason an unrecognised `last_verdict` is."""
    with pytest.raises(ValueError, match="tanky"):
        expert_review.check(_situ("tanky", "X"), _rich_index(["A"]))


def test_known_situations_are_the_ones_assemble_emits():
    from smite import assemble
    assert set(expert_review.KNOWN_SITUATIONS) == {s[0] for s in assemble._SITUATIONS}


# composition -----------------------------------------------------------------

def _items(**by_name):
    """{name: (stats dict, tags list)} -> item rows."""
    return [{"name": n, "stats": s, "effect_tags": t} for n, (s, t) in by_name.items()]


_PROT = {"Physical Protection": "30"}
_DMG = {"Strength": "40"}


def _comp(detail, god="Ullr"):
    r = {"claim": "composition", "detail": dict(detail)}
    if god:
        r.update(god=god, mode="Conquest")
    return r


def test_composition_holds_when_a_stat_count_exceeds_its_max():
    """"Carries shouldn't buy protections" — the shape STATE.md §5 recorded from
    the model's own diagnosis (Berserker's Shield on 17 of 18 Carry cores)."""
    index = _rich_index(["Shield", "Blade"],
                        items=_items(Shield=(_PROT, []), Blade=(_DMG, [])))
    verdict, why = expert_review.check(
        _comp({"stat": "Physical Protection", "max": 0}), index)
    assert verdict == "holds"
    assert "Shield" in why


def test_composition_clears_when_the_bound_is_met():
    index = _rich_index(["Blade"], items=_items(Blade=(_DMG, [])))
    assert expert_review.check(
        _comp({"stat": "Physical Protection", "max": 0}), index)[0] == "clear"


def test_composition_counts_effect_tags_against_a_min():
    """"Build him as a bruiser" written down as a floor on defensive items."""
    index = _rich_index(["A", "B"], items=_items(A=({}, ["sustain"]), B=({}, [])))
    assert expert_review.check(_comp({"tag": "sustain", "min": 2}), index)[0] == "holds"
    assert expert_review.check(_comp({"tag": "sustain", "min": 1}), index)[0] == "clear"


def test_composition_needs_a_bound_and_a_subject():
    with pytest.raises(ValueError, match="min"):
        expert_review.check(_comp({"stat": "Strength"}), _rich_index(["A"]))
    with pytest.raises(ValueError, match="stat"):
        expert_review.check(_comp({"min": 1}), _rich_index(["A"]))


def _roster(cores_by_god, role="Carry", items=None):
    index = _index({(g, "Conquest"): c for g, c in cores_by_god.items()},
                   gods=[{"name": g, "role": role} for g in cores_by_god])
    index["items"] = list(items or [])
    return index


def test_composition_over_a_role_is_a_population_verdict():
    """Mirrors item-overweighted: one offender in a large roster is partial,
    several is holds, none is clear."""
    items = _items(Shield=(_PROT, []), Blade=(_DMG, []))
    ten = {f"G{i}": ["Blade"] for i in range(10)}
    claim = _comp({"stat": "Physical Protection", "max": 0, "scope": "role:Carry"}, god=None)
    assert expert_review.check(claim, _roster(ten, items=items))[0] == "clear"
    ten["G0"] = ["Shield"]
    verdict, why = expert_review.check(claim, _roster(ten, items=items))
    assert verdict == "partial" and "G0" in why
    ten["G1"] = ["Shield"]
    assert expert_review.check(claim, _roster(ten, items=items))[0] == "holds"


# pairing ---------------------------------------------------------------------

def _pair(item, *partners):
    return {"god": "Ullr", "mode": "Conquest", "claim": "pairing",
            "detail": {"item": item, "with": list(partners)}}


def test_pairing_holds_when_the_item_is_built_without_its_partners():
    index = _rich_index(["Transcendence", "Other"])
    verdict, why = expert_review.check(_pair("Transcendence", "Hydra's Lament"), index)
    assert verdict == "holds"
    assert "Hydra's Lament" in why


def test_pairing_clears_when_all_partners_are_present():
    index = _rich_index(["Transcendence", "Hydra's Lament"])
    assert expert_review.check(_pair("Transcendence", "Hydra's Lament"), index)[0] == "clear"


def test_pairing_is_partial_when_some_partners_are_present():
    index = _rich_index(["Transcendence", "Hydra's Lament"])
    verdict, _ = expert_review.check(
        _pair("Transcendence", "Hydra's Lament", "Jotunn's Revenge"), index)
    assert verdict == "partial"


def test_pairing_is_vacuously_clear_and_says_so_when_the_item_is_gone():
    """"X only alongside Z" says nothing about a build without X. That is the
    coincidence-wearing-the-same-colour case the module docstring warns about,
    so the detail names it rather than letting a plain `clear` stand."""
    index = _rich_index(["Other"])
    verdict, why = expert_review.check(_pair("Transcendence", "Hydra's Lament"), index)
    assert verdict == "clear"
    assert "vacuous" in why


# schema ----------------------------------------------------------------------

def test_the_four_new_kinds_are_checkable():
    for kind in ("buy-order", "situational-swap", "composition", "pairing"):
        assert kind in expert_review.CHECKABLE


def test_a_membership_claim_with_no_items_raises_instead_of_clearing():
    """Pre-existing hole. `detail: {item: [...]}` (singular, a typo) read as an
    empty list, and an empty list of absent items is "all present" — a
    misspelled key cleared the claim."""
    index = _rich_index(["A"])
    for kind in ("missing-item", "item-overweighted"):
        with pytest.raises(ValueError, match="items"):
            expert_review.check({"god": "Ullr", "mode": "Conquest", "claim": kind,
                                 "detail": {"item": ["A"]}}, index)


def test_an_unknown_scope_raises_rather_than_widening_to_the_whole_roster():
    with pytest.raises(ValueError, match="scope"):
        expert_review.check({"claim": "item-overweighted",
                             "detail": {"items": ["A"], "scope": "suport-solo"}},
                            _rich_index(["A"]))


def test_a_role_scope_selects_gods_by_role_substring():
    """`role:Carry` matches "Carry" and "Carry Mid"; the existing
    `support-solo` spelling keeps working for the claim already on file."""
    index = _index({("A", "Conquest"): ["X"], ("B", "Conquest"): ["X"], ("C", "Conquest"): ["X"]},
                   gods=[{"name": "A", "role": "Carry"}, {"name": "B", "role": "Carry Mid"},
                         {"name": "C", "role": "Support"}])
    review = {"claim": "item-overweighted", "detail": {"items": ["X"], "scope": "role:Carry"}}
    verdict, why = expert_review.check(review, index)
    assert verdict == "holds" and "2/2" in why
