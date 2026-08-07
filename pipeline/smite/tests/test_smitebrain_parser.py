import json
from pathlib import Path

import pytest

from smite import smitebrain_parser

FIXTURES = Path(__file__).parent / "fixtures"


def _chiron_build_html():
    return (FIXTURES / "chiron_smitebrain.html").read_text(encoding="utf-8")


def test_parse_build_page_extracts_top_pick_per_core_slot_in_order():
    result = smitebrain_parser.parse_build_page(_chiron_build_html())

    top = [{"name": i["name"], "pick_rate": i["pick_rate"], "win_rate": i["win_rate"]} for i in result["items"]]
    assert top == [
        {"name": "Transcendence", "pick_rate": 0.61, "win_rate": 0.49},
        {"name": "Ninja Tabi", "pick_rate": 0.58, "win_rate": 0.50},
        {"name": "Devourer's Gauntlet", "pick_rate": 0.55, "win_rate": 0.52},
    ]


def test_parse_build_page_excludes_relics_and_starters():
    result = smitebrain_parser.parse_build_page(_chiron_build_html())

    names = [item["name"] for item in result["items"]]
    assert "Purification Beads" not in names
    assert "Bluestone Brooch" not in names


def test_parse_build_page_excludes_lower_pick_rate_core_alternatives():
    result = smitebrain_parser.parse_build_page(_chiron_build_html())

    names = [item["name"] for item in result["items"]]
    assert "Jotunn's Revenge" not in names
    assert "Red Dragon Proxy" not in names


def test_parse_build_page_extracts_aspects_separately_from_items():
    result = smitebrain_parser.parse_build_page(_chiron_build_html())

    assert {"name": "Aspect of the Heroic Tutor", "pick_rate": 0.91, "win_rate": 0.53} in result["aspects"]
    assert {"name": "Aspect of the Other Thing", "pick_rate": 0.09, "win_rate": 0.45} in result["aspects"]
    assert not any(a["name"].startswith("Aspect") for a in result["items"])
    assert len(result["aspects"]) == 2


def test_parse_build_page_survives_extra_flex_wrapper_around_icon():
    """Regression test: an icon-centering wrapper div around the <img> that
    also happens to carry class="flex" (an ordinary Tailwind pattern) must
    not cause the tile to be silently dropped. Walking up from the <img> via
    find_parent("div", class_="flex") would incorrectly land on this inner
    wrapper instead of the true tile container, whose stat div would then be
    unreachable. Exercised here against an Aspect tile, since _parse_aspects
    is the function that anchors off the stat div and walks upward — the
    same shape of risk the original (pre-rewrite) parser guarded against."""
    html = """
    <div class="flex gap-1">
      <div class="flex shrink-0 flex-col items-center gap-2">
        <div class="flex items-center justify-center rounded border">
          <a href="/items/aspect-of-the-heroic-tutor">
            <img alt="Aspect of the Heroic Tutor" src="https://images.smitebrain.com/images/items/icons/aspect-of-the-heroic-tutor"/>
          </a>
        </div>
        <div class="text-xs text-gray-400">91% pick<br/> 53% win</div>
      </div>
    </div>
    """

    result = smitebrain_parser.parse_build_page(html)

    assert {"name": "Aspect of the Heroic Tutor", "pick_rate": 0.91, "win_rate": 0.53} in result["aspects"]
    assert len(result["aspects"]) == 1
    assert result["items"] == []


def test_parse_build_page_stops_scanning_core_slots_at_the_next_heading():
    """Regression test for the <h2> boundary stop in
    _parse_core_recommended_build. On the real page Core is currently the
    last section, so nothing else exercises this line — without this test,
    a later page layout change (e.g. a "Matchups" section added after Core)
    with its own digit-labeled, font-semibold div could be silently mistaken
    for a 4th Core slot, exactly the "scans too much of the page" bug class
    this whole fix round exists to prevent."""
    html = """
    <div class="border-neutral bg-base-300 flex w-full min-w-0 flex-col gap-3 border p-3">
      <div class="flex items-center justify-between">
        <h2 class="border-accent border-l-2 pl-2 text-xl font-semibold text-white">Core</h2>
        <label class="label cursor-pointer gap-2 text-sm text-gray-400">Split by Slot</label>
      </div>
      <div class="flex items-start gap-2">
        <div class="mt-5 flex min-h-4 min-w-4 shrink-0 items-center justify-center font-semibold">1</div>
        <div class="flex gap-1 overflow-x-auto overscroll-x-contain pb-2">
          <div class="flex shrink-0 flex-col items-center gap-2 font-medium">
            <a href="/items/transcendence"><img alt="Transcendence" src="x"/></a>
            <div class="text-xs text-gray-400">61% pick<br/> 49% win</div>
          </div>
        </div>
      </div>
    </div>

    <h2 class="border-accent border-l-2 pl-2 text-xl font-semibold text-white">Matchups</h2>
    <div class="flex items-start gap-2">
      <div class="mt-5 flex min-h-4 min-w-4 shrink-0 items-center justify-center font-semibold">1</div>
      <div class="flex gap-1 overflow-x-auto overscroll-x-contain pb-2">
        <div class="flex shrink-0 flex-col items-center gap-2 font-medium">
          <a href="/items/decoy-item"><img alt="Decoy Item" src="x"/></a>
          <div class="text-xs text-gray-400">99% pick<br/> 99% win</div>
        </div>
      </div>
    </div>
    """

    result = smitebrain_parser.parse_build_page(html)

    assert result["items"] == [{"name": "Transcendence", "pick_rate": 0.61, "win_rate": 0.49}]
    assert "Decoy Item" not in [item["name"] for item in result["items"]]


def test_core_build_dedups_via_next_best_alternative():
    # Slot 1 and slot 2 both top-pick Titan's Bane; slot 2 must fall to its
    # next-best alternative so the build has no duplicate item.
    html = """
    <h2>Core</h2>
    <div class="font-semibold">1</div>
    <div>
      <div class="flex"><img alt="Titan's Bane"><div class="text-xs">40% pick 58% win</div></div>
      <div class="flex"><img alt="Deathbringer"><div class="text-xs">30% pick 55% win</div></div>
    </div>
    <div class="font-semibold">2</div>
    <div>
      <div class="flex"><img alt="Titan's Bane"><div class="text-xs">27% pick 52% win</div></div>
      <div class="flex"><img alt="The Crusher"><div class="text-xs">26% pick 67% win</div></div>
    </div>
    """
    from smite import smitebrain_parser
    result = smitebrain_parser.parse_build_page(html)
    names = [e["name"] for e in result["items"]]
    assert names == ["Titan's Bane", "The Crusher"]   # no duplicate


def test_parse_build_page_captures_per_slot_alternates():
    result = smitebrain_parser.parse_build_page(_chiron_build_html())
    # at least one slot should carry alternates (the lower-pick tiles we used to drop)
    with_alts = [it for it in result["items"] if it.get("alternates")]
    assert with_alts, "expected some slots to have alternates"
    alt = with_alts[0]["alternates"][0]
    assert "name" in alt and "pick_rate" in alt and "win_rate" in alt


# ---------------------------------------------------------------------------
# parse_god_index
#
# The index is a SvelteKit `devalue` payload: one flat array where every value
# inside an object is an INDEX into that array. Decoding it by matching on key
# names works until a real integer collides with a valid index, so the parser
# dereferences properly and these tests pin that.
# ---------------------------------------------------------------------------

def _god_index_fixture():
    path = Path(__file__).parent / "fixtures" / "smitebrain_god_index.json"
    return json.loads(path.read_text(encoding="utf-8"))


def test_parse_god_index_returns_every_god_with_a_denominator():
    rows = smitebrain_parser.parse_god_index(_god_index_fixture())
    assert len(rows) == 87
    assert len({r["god"] for r in rows}) == 87
    assert all(r["matches_played"] > 0 for r in rows)


def test_parse_god_index_dereferences_values_rather_than_returning_pointers():
    rows = smitebrain_parser.parse_god_index(_god_index_fixture())
    hades = next(r for r in rows if r["god"] == "Hades")
    # Wins and losses are the point; a pointer would surface as a small int
    # that happens to look like a plausible count, so check the arithmetic.
    assert hades["matches_won"] == 445
    assert hades["matches_played"] == 703
    assert hades["win_rate"] == pytest.approx(445 / 703, abs=1e-6)
    # Type-tagged scalars are unwrapped, not left as ["Date", "..."].
    assert hades["start_time"].startswith("2026-")


def test_parse_god_index_rows_are_god_level_not_aspect_level():
    rows = smitebrain_parser.parse_god_index(_god_index_fixture())
    assert {r["aspect"] for r in rows} == {"None"}


def test_parse_god_index_survives_a_payload_with_no_data():
    assert smitebrain_parser.parse_god_index({}) == []
    assert smitebrain_parser.parse_god_index({"nodes": [None]}) == []
    assert smitebrain_parser.parse_god_index({"nodes": [{"data": "not-a-list"}]}) == []


# ---------------------------------------------------------------------------
# Starters
#
# Scraped now, having been skipped since the first parser — "Relics and
# Starters are alternatives, not a build order". True of the ORDER, but it
# left the app with no community starter at all: the one it showed came from a
# role rule, so every Carry got the same opener regardless of what Carry
# players actually bought.
# ---------------------------------------------------------------------------

def _tile(name, pick, win):
    return (f'<div class="flex"><img alt="{name}">'
            f'<div class="text-xs">{pick}% pick {win}% win</div></div>')


def _page(starter_tiles, core_tiles=""):
    return (
        '<div class="border-neutral bg-base-300 flex"><h2>Starters</h2>'
        + starter_tiles +
        '</div>'
        '<div><div class="flex items-center justify-between"><h2>Core</h2></div>'
        '<div class="font-semibold">1</div><div>' + core_tiles + '</div></div>'
    )


def test_starters_are_ranked_by_pick_rate_and_capped():
    html = _page(_tile("Gilded Arrow", 14, 27)
                 + _tile("Sharpshooter's Arrow", 40, 57)
                 + _tile("Hunter's Cowl", 21, 57)
                 + _tile("Death's Embrace", 11, 59))
    out = smitebrain_parser.parse_build_page(html)["starters"]
    assert [s["name"] for s in out] == ["Sharpshooter's Arrow", "Hunter's Cowl", "Gilded Arrow"]
    assert out[0] == {"name": "Sharpshooter's Arrow", "pick_rate": 0.40, "win_rate": 0.57}


def test_starters_never_reach_into_the_core_section():
    """A forward walk from the heading runs straight into Core — its `h2` sits
    in a different wrapper, so a `break` on the next heading never fires, and
    Tyrfing and Jotunn's Revenge were being reported as starters."""
    html = _page(_tile("Conduit Gem", 25, 50),
                 core_tiles=_tile("Tyrfing", 55, 60) + _tile("Jotunn's Revenge", 44, 58))
    out = smitebrain_parser.parse_build_page(html)["starters"]
    assert [s["name"] for s in out] == ["Conduit Gem"]


def test_starters_dedupe_a_tile_nested_in_its_own_wrapper():
    # The markup nests a tile inside a wrapper that also matches `.flex`, so a
    # naive walk counts each starter twice.
    dup = '<div class="flex">' + _tile("Conduit Gem", 25, 50) + '</div>'
    out = smitebrain_parser.parse_build_page(_page(dup))["starters"]
    assert len(out) == 1 and out[0]["name"] == "Conduit Gem"


def test_starters_absent_section_is_empty_not_an_error():
    html = '<div><div class="flex items-center justify-between"><h2>Core</h2></div></div>'
    assert smitebrain_parser.parse_build_page(html)["starters"] == []
