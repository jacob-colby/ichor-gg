from pathlib import Path

from smite import smitebrain_parser

FIXTURES = Path(__file__).parent / "fixtures"


def _chiron_build_html():
    return (FIXTURES / "chiron_smitebrain.html").read_text(encoding="utf-8")


def test_parse_build_page_extracts_items():
    result = smitebrain_parser.parse_build_page(_chiron_build_html())

    assert {"name": "Transcendence", "pick_rate": 0.61, "win_rate": 0.49} in result["items"]
    assert {"name": "Jotunn's Revenge", "pick_rate": 0.55, "win_rate": 0.50} in result["items"]


def test_parse_build_page_extracts_aspects_separately_from_items():
    result = smitebrain_parser.parse_build_page(_chiron_build_html())

    assert {"name": "Aspect of the Heroic Tutor", "pick_rate": 0.91, "win_rate": 0.53} in result["aspects"]
    assert not any(a["name"].startswith("Aspect") for a in result["items"])
    assert len(result["items"]) == 2
    assert len(result["aspects"]) == 2


def test_parse_build_page_survives_extra_flex_wrapper_around_icon():
    """Regression test: an icon-centering wrapper div around the <img> that
    also happens to carry class="flex" (an ordinary Tailwind pattern) must
    not cause the tile to be silently dropped. Walking up from the <img> via
    find_parent("div", class_="flex") would incorrectly land on this inner
    wrapper instead of the true tile container, whose sibling "text-xs" stat
    div would then be unreachable."""
    html = """
    <div class="flex gap-1">
      <div class="flex shrink-0 flex-col items-center gap-2">
        <div class="flex items-center justify-center rounded border">
          <a href="/items/transcendence">
            <img alt="Transcendence" src="https://images.smitebrain.com/images/items/icons/transcendence"/>
          </a>
        </div>
        <div class="text-xs text-gray-400">61% pick<br/> 49% win</div>
      </div>
    </div>
    """

    result = smitebrain_parser.parse_build_page(html)

    assert {"name": "Transcendence", "pick_rate": 0.61, "win_rate": 0.49} in result["items"]
    assert len(result["items"]) == 1
    assert result["aspects"] == []
