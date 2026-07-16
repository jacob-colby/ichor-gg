from pathlib import Path

from smite import smitebrain_parser

FIXTURES = Path(__file__).parent / "fixtures"


def _chiron_build_html():
    return (FIXTURES / "chiron_smitebrain.html").read_text(encoding="utf-8")


def test_parse_build_page_extracts_top_pick_per_core_slot_in_order():
    result = smitebrain_parser.parse_build_page(_chiron_build_html())

    assert result["items"] == [
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
