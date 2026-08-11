"""The expert-review replay. See `smite.expert_review` for why it exists —
it is the project's only gate not made of the community's own build data.

These pin the parts that decide a verdict, because a checker that quietly
passes everything would be worse than no checker: it would look like the
non-circular gate STATE.md §5 asks for while measuring nothing.
"""
import io

from smite import expert_review


def _index(cores, gods=None):
    """A minimal index: {(god, mode): [items]} plus optional god rows."""
    builds = []
    for (god, mode), items in cores.items():
        builds.append({"god": god, "mode": mode, "builds": [
            {"source": "community", "slot_order": []},
            {"source": "suggested", "archetype": "core", "slot_order": list(items)},
        ]})
    return {"builds": builds, "gods": gods or [{"name": g, "role": "Carry"}
                                               for g, _ in cores]}


def test_core_for_reads_the_core_archetype_not_a_flavor():
    """A claim about "the build" is about the one the app opens on. Eleven
    flavors ship per god, and letting any of them answer would clear almost
    every item-overweighted claim by accident."""
    index = {"builds": [{"god": "Ra", "mode": "Conquest", "builds": [
        {"source": "suggested", "archetype": "crit", "slot_order": ["Wrong"]},
        {"source": "suggested", "archetype": "core", "slot_order": ["Right"]},
    ]}], "gods": []}
    assert expert_review.core_for(index, "Ra") == ["Right"]


def test_core_for_ignores_a_fun_build():
    index = {"builds": [{"god": "Ra", "mode": "Conquest", "builds": [
        {"source": "suggested", "archetype": "core", "fun": True, "slot_order": ["Joke"]},
    ]}], "gods": []}
    assert expert_review.core_for(index, "Ra") is None


def test_missing_item_holds_when_none_of_the_named_items_arrive():
    index = _index({("Ullr", "Conquest"): ["A", "B", "C"]})
    review = {"god": "Ullr", "mode": "Conquest", "claim": "missing-item",
              "detail": {"items": ["Transcendence", "Heartseeker"]}}
    verdict, _ = expert_review.check(review, index)
    assert verdict == "holds"


def test_missing_item_is_partial_when_some_arrive():
    """The honest middle. Ullr's real claim named four items and three now
    appear; reporting that as "clear" would overstate the fix and reporting it
    as "holds" would hide a real change."""
    index = _index({("Ullr", "Conquest"): ["Heartseeker", "B", "C"]})
    review = {"god": "Ullr", "mode": "Conquest", "claim": "missing-item",
              "detail": {"items": ["Transcendence", "Heartseeker"]}}
    verdict, why = expert_review.check(review, index)
    assert verdict == "partial"
    assert "Transcendence" in why


def test_missing_item_clears_only_when_every_named_item_arrives():
    index = _index({("Ullr", "Conquest"): ["Transcendence", "Heartseeker"]})
    review = {"god": "Ullr", "mode": "Conquest", "claim": "missing-item",
              "detail": {"items": ["Transcendence", "Heartseeker"]}}
    assert expert_review.check(review, index)[0] == "clear"


def test_item_overweighted_counts_across_the_scoped_population():
    """"It shows up on everything" is a claim about a population. Checking one
    build could clear it while the item still sat in thirty others."""
    gods = [{"name": n, "role": "Support"} for n in ("A", "B", "C", "D")]
    index = _index({(n, "Conquest"): ["Eye of Providence"] for n in ("A", "B", "C", "D")},
                   gods=gods)
    review = {"claim": "item-overweighted",
              "detail": {"items": ["Eye of Providence"], "scope": "support-solo"}}
    verdict, why = expert_review.check(review, index)
    assert verdict == "holds"
    assert "4/4" in why


def test_item_overweighted_clears_when_the_item_is_gone_everywhere():
    gods = [{"name": n, "role": "Support"} for n in ("A", "B")]
    index = _index({(n, "Conquest"): ["Something Else"] for n in ("A", "B")}, gods=gods)
    review = {"claim": "item-overweighted",
              "detail": {"items": ["Eye of Providence"], "scope": "support-solo"}}
    assert expert_review.check(review, index)[0] == "clear"


def test_an_unknown_claim_kind_is_never_silently_passed():
    """`narrative` claims are prose. Giving them a verdict would let the report
    fill with green marks that mean nothing was checked."""
    verdict, why = expert_review.check({"claim": "narrative", "detail": {}}, _index({}))
    assert verdict == "unchecked"
    assert "not evaluated" in why


def test_a_claim_about_a_god_with_no_build_is_unchecked_not_clear():
    """Absence of a build is absence of evidence. Reading it as "clear" would
    let deleting a god resolve every complaint about it."""
    review = {"god": "Nobody", "mode": "Conquest", "claim": "missing-item",
              "detail": {"items": ["A"]}}
    assert expert_review.check(review, _index({}))[0] == "unchecked"


def test_only_a_resolved_claim_coming_back_counts_as_a_regression():
    """An open claim that still holds is a to-do item in its normal state. A
    resolved one that comes back means a shipped fix was undone, and that is
    the only thing worth failing a build over."""
    index = _index({("Ullr", "Conquest"): ["A"]})
    still_open = {"god": "Ullr", "mode": "Conquest", "claim": "missing-item",
                  "status": "open", "detail": {"items": ["Transcendence"]}}
    was_fixed = {"god": "Ullr", "mode": "Conquest", "claim": "missing-item",
                 "status": "resolved", "detail": {"items": ["Transcendence"]}}
    rows = [(r, expert_review.check(r, index)[0], "") for r in (still_open, was_fixed)]
    back = expert_review.regressions(rows)
    assert back == [was_fixed]


def test_the_report_refuses_to_present_itself_as_a_score():
    """One reviewer, claims chosen because they looked wrong. A percentage off
    this sample would be meaningless and would get quoted anyway."""
    out = io.StringIO()
    expert_review.report([{"claim": "narrative", "detail": {}}], _index({}), out=out)
    assert "NOT a score" in out.getvalue()


def test_the_shipped_register_parses_and_every_claim_kind_is_known():
    """The YAML is hand-edited, so a typo'd claim kind must fail here rather
    than silently becoming an unchecked row in the report."""
    reviews = expert_review.load_reviews()
    assert reviews, "the shipped register should not be empty"
    known = set(expert_review.CHECKABLE) | {"narrative"}
    for r in reviews:
        assert r.get("claim") in known, r.get("claim")
        assert r.get("quote"), "a claim without the reviewer's own words can drift"
        assert r.get("status") in ("open", "resolved", "rejected"), r.get("status")
