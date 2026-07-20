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


def test_parse_item_page_extracts_stats():
    result = wiki_parser.parse_item_page(_deathbringer_html())

    assert result["stats"] == {"Strength": "45", "Critical Chance": "20%"}


def test_parse_item_page_captures_active_effect_when_passive_empty():
    # Items like Bloodforge carry their effect under "Active Effect" with an
    # empty "Passive Effect" — the parser must still capture it.
    html = """
    <table class="infobox">
      <tr><th>Item Type</th><td>Tier 3</td></tr>
      <tr><th>Total Cost</th><td>2550</td></tr>
      <tr><th>Passive Effect</th><td></td></tr>
      <tr><th>Active Effect</th><td>On Use: + Health Shield for 6s.</td></tr>
    </table>
    """
    result = wiki_parser.parse_item_page(html)
    assert "On Use: + Health Shield for 6s." in result["passive"]


def test_parse_item_page_combines_passive_and_active_effects():
    html = """
    <table class="infobox">
      <tr><th>Item Type</th><td>Tier 3</td></tr>
      <tr><th>Passive Effect</th><td>Ability Hit: bonus damage.</td></tr>
      <tr><th>Active Effect</th><td>On Use: dash forward.</td></tr>
    </table>
    """
    result = wiki_parser.parse_item_page(html)
    assert "Ability Hit: bonus damage." in result["passive"]
    assert "dash forward" in result["passive"]


def test_parse_item_page_stat_only_item_has_no_passive():
    # Both effect rows empty (e.g. Titan's Bane / Obsidian Shard — the item is
    # its stats) → no passive key, correctly blank.
    html = """
    <table class="infobox">
      <tr><th>Item Type</th><td>Tier 3</td></tr>
      <tr><th>Passive Effect</th><td></td></tr>
      <tr><th>Active Effect</th><td></td></tr>
    </table>
    """
    result = wiki_parser.parse_item_page(html)
    assert not result.get("passive")


def test_parse_god_page_extracts_image_url():
    result = wiki_parser.parse_god_page(_chiron_html())
    assert result["image_url"] == "/images/thumb/T_Chiron%28S2%29_Default.png/280px-T_Chiron%28S2%29_Default.png?157c1"


def test_parse_item_page_extracts_image_url():
    result = wiki_parser.parse_item_page(_deathbringer_html())
    assert result["image_url"] == "/images/T3_Deathbringer.png?6d7a6"


def test_derive_headshot_url_from_portrait_thumb():
    from smite import wiki_parser
    portrait = "/images/thumb/T_Ullr%28S2%29_Default.png/280px-T_Ullr%28S2%29_Default.png?1914c"
    assert wiki_parser.derive_headshot_url(portrait) == "/images/T_Ullr%28S2%29_Default_Icon.png"


def test_derive_headshot_url_handles_missing():
    from smite import wiki_parser
    assert wiki_parser.derive_headshot_url(None) is None
    assert wiki_parser.derive_headshot_url("/images/no_match_here.png") is None


def test_parse_abilities_captures_description_and_details():
    from bs4 import BeautifulSoup
    html = """
    <h2><span id="Abilities">Abilities</span></h2>
    <table class="wikitable">
      <tr><th><span>1st Ability</span> <span>Training Exercise</span></th></tr>
      <tr><td>Chiron fires a volley that boosts allies and damages enemies.</td></tr>
      <tr><td><ul>
        <li>Cooldown: 14/13/12/11/10</li>
        <li>Cost: 60/65/70/75/80</li>
        <li>Damage: 90/140/190</li>
      </ul></td></tr>
    </table>
    """
    abilities = wiki_parser._parse_abilities(BeautifulSoup(html, "html.parser"))
    a = next(x for x in abilities if x["name"] == "Training Exercise")
    assert a["cooldown"] == [14, 13, 12, 11, 10]
    assert a["cost"] == [60, 65, 70, 75, 80]
    assert "Damage: 90/140/190" in a["details"]
    assert "volley" in a["description"].lower()
    assert "Cooldown: 14" not in a["description"]
