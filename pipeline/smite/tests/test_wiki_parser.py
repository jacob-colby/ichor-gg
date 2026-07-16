# tools/smite/tests/test_wiki_parser.py
from pathlib import Path

from smite import wiki_parser

FIXTURES = Path(__file__).parent / "fixtures"


def _chiron_html():
    return (FIXTURES / "chiron_wiki.html").read_text(encoding="utf-8")


def test_parse_god_page_extracts_infobox_fields():
    result = wiki_parser.parse_god_page(_chiron_html())

    assert result["pantheon"] == "Greek"
    assert result["role"] == "Carry"
    assert result["specializations"] == ["Sharpshooter", "Nuker"]
    assert result["damage_type"] == "physical"
    assert result["release_date"] == "January 27, 2026"


def test_parse_god_page_extracts_base_stats():
    result = wiki_parser.parse_god_page(_chiron_html())

    assert result["base_stats"]["health"] == {"base": 569.48, "per_level": 86.48}
    assert result["base_stats"]["mana"] == {"base": 322.62, "per_level": 48.3}
    assert result["base_stats"]["attack_speed"] == {"base": 1.0, "per_level": 1.51}


def test_parse_god_page_extracts_abilities_with_cooldown_and_cost():
    result = wiki_parser.parse_god_page(_chiron_html())

    names = [a["name"] for a in result["abilities"]]
    assert "Herbal Medicine" in names
    assert "Training Exercise" in names

    training_exercise = next(a for a in result["abilities"] if a["name"] == "Training Exercise")
    assert training_exercise["cooldown"] == [13.0]
    assert training_exercise["cost"] == [55.0, 60.0, 65.0, 70.0, 75.0]


def test_parse_god_page_extracts_aspect():
    result = wiki_parser.parse_god_page(_chiron_html())

    assert len(result["aspects"]) == 1
    assert result["aspects"][0]["name"] == "Aspect of the Heroic Tutor"
    assert "Target Mark now only applies to one target" in result["aspects"][0]["kit_changes"]


def test_parse_god_page_raises_without_infobox():
    try:
        wiki_parser.parse_god_page("<html><body>no infobox here</body></html>")
        assert False, "expected ValueError"
    except ValueError:
        pass


def _deathbringer_html():
    return (FIXTURES / "deathbringer_wiki.html").read_text(encoding="utf-8")


def test_parse_item_page_extracts_infobox_fields():
    result = wiki_parser.parse_item_page(_deathbringer_html())

    assert result["tier"] == 3
    assert result["cost"] == 2900
    assert result["passive"] == "+35% Critical Strike Damage."


def test_parse_item_page_extracts_direct_builds_from_only():
    result = wiki_parser.parse_item_page(_deathbringer_html())

    assert result["builds_from"] == ["Skeggox", "Kopesh"]
    assert "Axe" not in result["builds_from"]
    assert "Sabre" not in result["builds_from"]
