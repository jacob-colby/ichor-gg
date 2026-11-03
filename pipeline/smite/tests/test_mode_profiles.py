"""Pins on the shipped mode profiles (`modes.*` in data/_weights.yaml)."""
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
