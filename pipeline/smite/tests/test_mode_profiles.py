"""Pins on the shipped mode profiles (`modes.*` in data/_weights.yaml)."""
import pytest

from smite import recommend, scoring


def _modes():
    return scoring.load_weights(recommend.WEIGHTS_PATH)["modes"]


def test_joust_does_not_penalise_wave_clear():
    """2026-11-03: Joust is one lane plus jungle; the wave is how towers fall.

    The old -0.15 read it as "no second wave to matter". Neutral, not
    positive — neither sign is measured in a mode with no community record.
    """
    joust = _modes()["joust"]
    assert joust["tag_bonus"].get("wave-clear", 0) == 0


def test_joust_borrows_conquest_record_for_wave_clear_items():
    """The borrow rejection shared the penalty's mistaken reason and went with it."""
    reject = _modes()["joust"]["borrow_community"]["reject_tags"]
    assert "wave-clear" not in reject
    assert "mobility" in reject


def test_arena_still_prices_wave_clear_up():
    assert _modes()["arena"]["tag_bonus"]["wave-clear"] > 0


# ── Team-level tags (2026-11-03) ──────────────────────────────────────────

def test_team_share_is_one_carrier_in_n_plus_duplicates_at_their_value():
    assert scoring.team_share(3, 0.25) == pytest.approx(1 / 3 + 2 / 3 * 0.25)
    assert scoring.team_share(5, 0.25) == pytest.approx(0.2 + 0.8 * 0.25)
    assert scoring.team_share(None, 0.25) == 1.0
    assert scoring.team_share(1, 0.0) == 1.0


def test_the_modes_anti_heal_and_aura_bonus_is_scaled_by_the_team_share():
    w = scoring.load_weights(recommend.WEIGHTS_PATH)
    raw = w["modes"]["joust"]["tag_bonus"]
    p = scoring.resolve_profile(w, "Joust")
    cal = {**w["team_tags"]["share"]["joust"], **w["team_tags"]["derived"]["joust"]}
    assert p["team_shares"] == {"anti-heal": cal["anti-heal"], "aura": cal["aura"]}
    assert p["tag_bonus"]["anti-heal"] == pytest.approx(raw["anti-heal"] * cal["anti-heal"])
    assert p["tag_bonus"]["aura"] == pytest.approx(raw["aura"] * cal["aura"])
    assert p["tag_bonus"]["sustain"] == raw["sustain"]          # not a team tag
    assert p["team_tag_bonus"] == {"anti-heal": raw["anti-heal"], "aura": raw["aura"]}


def test_a_flavor_or_aspect_bonus_on_a_team_tag_is_not_scaled():
    w = scoring.load_weights(recommend.WEIGHTS_PATH)
    p = scoring.resolve_profile(w, "Arena", aspect_overlay={"tag_bonus": {"aura": 0.3}})
    assert p["tag_bonus"]["aura"] == 0.3


def test_conquest_has_no_team_tag_bonus_to_scale():
    w = scoring.load_weights(recommend.WEIGHTS_PATH)
    assert scoring.resolve_profile(w, "Conquest")["team_tag_bonus"] == {}


def test_the_index_ships_what_the_static_builds_assumed():
    from smite import build_index
    w = scoring.load_weights(recommend.WEIGHTS_PATH)
    t = build_index.team_config(w)
    assert t["tags"] == ["anti-heal", "aura"]
    assert t["modes"]["Joust"]["team_size"] == 3
    assert t["modes"]["Joust"]["bonus"]["anti-heal"] == w["modes"]["joust"]["tag_bonus"]["anti-heal"]


def test_without_a_calibrated_share_the_formula_applies():
    w = scoring.load_weights(recommend.WEIGHTS_PATH)
    w["team_tags"].pop("share")
    p = scoring.resolve_profile(w, "Arena")
    share = scoring.team_share(5, w["team_tags"]["duplicate_value"])
    assert p["tag_bonus"]["anti-heal"] == pytest.approx(w["modes"]["arena"]["tag_bonus"]["anti-heal"] * share)


def test_the_calibrated_shares_put_static_cores_near_one_in_n():
    """Pinned as a property, ±0.08 around 1/N, not as counts."""
    from smite import efficiency
    w = scoring.load_weights(recommend.WEIGHTS_PATH)
    efficiency.apply_pricing_flags(w)
    items, tags = recommend.load_items(), scoring.load_tags(recommend.TAGS_PATH)
    gods = recommend.load_gods()
    for mode, n_team in (("Joust", 3), ("Arena", 5)):
        held = n = 0
        for g in gods:
            for e in recommend.build_suggested_entries(g, items, {"builds": []}, w, tags, mode):
                if e["archetype"] == "core":
                    n += 1
                    held += any("anti-heal" in (tags.get(x) or []) for x in e["slot_order"])
        assert abs(held / n - 1 / n_team) < 0.08, (mode, held, n)


# ── Derived team-tag shares (2026-11-04) ──────────────────────────────────
# Joust's anti-heal share is derived from its 1-in-N target, not swept
# (`recommend`, "Team-tag shares derived from their target").

def test_a_derived_share_is_refused_rather_than_guessed_when_missing():
    w = scoring.load_weights(recommend.WEIGHTS_PATH)
    w["team_tags"].pop("derived")
    with pytest.raises(KeyError, match="recommend --all"):
        scoring.resolve_profile(w, "Joust")
    scoring.resolve_profile(w, "Arena")          # not derived: its swept share stands


@pytest.fixture(scope="module")
def fresh_derivation():
    from smite import efficiency
    w = scoring.load_weights(recommend.WEIGHTS_PATH)
    efficiency.apply_pricing_flags(w)
    return recommend.derive_team_shares(recommend.load_gods(), recommend.load_items(), w,
                                        scoring.load_tags(recommend.TAGS_PATH))


def test_the_shipped_derived_share_is_not_stale(fresh_derivation):
    """data/_team_shares.json is what `recommend --all` derived on THIS data
    and THIS model. Stale means the builds were made with another share."""
    import json
    shipped = json.loads(recommend.TEAM_SHARES_PATH.read_text(encoding="utf-8"))
    for mode, tags in fresh_derivation.items():
        for tag, d in tags.items():
            assert shipped[mode][tag]["share"] == pytest.approx(d["share"], abs=1e-9), \
                "stale: run `python -m smite.recommend --all`"
            assert shipped[mode][tag]["holding"] == d["holding"]


def _ties_at(costs, share):
    return sum(1 for c in costs.values() if c is not None and c == share)


def test_the_derived_share_holds_the_target_count(fresh_derivation):
    d = fresh_derivation["joust"]["anti-heal"]
    assert d["target"] == round(d["seats"] / 3)
    # Exactly the target, plus any seat tied with the target seat's cost.
    assert d["target"] <= d["holding"] < d["target"] + _ties_at(d["costs"], d["share"])
    assert d["holding"] == sum(1 for c in d["costs"].values() if c is not None and c <= d["share"])


def test_the_count_moves_one_seat_per_step_of_the_target(fresh_derivation):
    """The cliff, gone: as the target k moves, the count the derived share
    gives is k (k + its exact ties), never a role-sized block."""
    costs = fresh_derivation["joust"]["anti-heal"]["costs"]
    ranked = sorted(c for c in costs.values() if c is not None)
    for k in range(1, len(ranked) + 1):
        share = ranked[k - 1]
        count = sum(1 for c in ranked if c <= share)
        assert k <= count < k + _ties_at(costs, share), (k, count)
