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
