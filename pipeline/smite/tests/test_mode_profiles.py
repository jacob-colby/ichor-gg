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
    share = scoring.team_share(3, w["team_tags"]["duplicate_value"])
    assert p["team_share"] == pytest.approx(share)
    assert p["tag_bonus"]["anti-heal"] == pytest.approx(raw["anti-heal"] * share)
    assert p["tag_bonus"]["aura"] == pytest.approx(raw["aura"] * share)
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
