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
