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


def test_parse_item_page_falls_back_to_cost_when_total_cost_blank():
    # Starter/base items (e.g. Bluestone Pendant, Vampiric Shroud) populate
    # "Cost" but leave "Total Cost" blank since they don't build up from
    # components — the parser must fall back to "Cost" in that case.
    html = """
    <table class="infobox">
      <tr><th>Item Type</th><td>Tier 1</td></tr>
      <tr><th>Cost</th><td>600</td></tr>
      <tr><th>Total Cost</th><td></td></tr>
      <tr><th>Stats</th><td><b>10</b> Strength <br></td></tr>
    </table>
    """
    result = wiki_parser.parse_item_page(html)
    assert result["cost"] == 600


def test_parse_item_page_prefers_total_cost_over_cost():
    # Regular items have both rows populated: "Cost" is the smaller
    # component-only figure, "Total Cost" is the full build cost — Total
    # Cost must win when present.
    html = """
    <table class="infobox">
      <tr><th>Item Type</th><td>Tier 3</td></tr>
      <tr><th>Cost</th><td>800</td></tr>
      <tr><th>Total Cost</th><td>2600</td></tr>
      <tr><th>Stats</th><td><b>10</b> Strength <br></td></tr>
    </table>
    """
    result = wiki_parser.parse_item_page(html)
    assert result["cost"] == 2600


def test_parse_item_page_captures_glyph_tier_as_string_label():
    # Glyphs (e.g. Blinking Abyss) have an "Item Type" row that just says
    # "Glyph" with no "Tier N" — the parser must capture the label itself
    # rather than leaving tier null.
    html = """
    <table class="infobox">
      <tr><th>Item Type</th><td>Glyph</td></tr>
      <tr><th>Total Cost</th><td>0</td></tr>
    </table>
    """
    result = wiki_parser.parse_item_page(html)
    assert result["tier"] == "Glyph"


def test_parse_item_page_keeps_numeric_tier_for_regular_items():
    html = """
    <table class="infobox">
      <tr><th>Item Type</th><td>Tier 3</td></tr>
      <tr><th>Total Cost</th><td>2600</td></tr>
    </table>
    """
    result = wiki_parser.parse_item_page(html)
    assert result["tier"] == 3


def test_parse_item_page_keeps_numeric_tier_for_starters():
    html = """
    <table class="infobox">
      <tr><th>Item Type</th><td>Tier 1 Starter</td></tr>
      <tr><th>Cost</th><td>600</td></tr>
    </table>
    """
    result = wiki_parser.parse_item_page(html)
    assert result["tier"] == 1


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


ABILITY_HTML = """
<h2><span id="Abilities">Abilities</span></h2>
<table class="wikitable">
  <tr><th><span>1st Ability</span><span>Celestial Beam</span></th></tr>
  <tr><td>
    LINE DAMAGE Notes : Summon a moving beam of intense light, dealing Magical Damage to enemies
    Damage : 95 | 155 Damage Scaling : 105% Intelligence Cooldown : 10 seconds
    Expand Ability Video
    <ul>
      <li>Damage: 95 | 155</li>
      <li>Damage Scaling: 105% Intelligence</li>
      <li>Cooldown: 10 seconds</li>
    </ul>
  </td></tr>
</table>
"""


def _first_ability(html):
    from bs4 import BeautifulSoup
    return wiki_parser._parse_abilities(BeautifulSoup(html, "html.parser"))[0]


def test_ability_description_drops_the_wikis_own_ui_chrome():
    """"Expand Ability Video" is a control on the wiki page, not ability text.
    It shipped as body copy on all 513 abilities."""
    a = _first_ability(ABILITY_HTML)
    assert "Expand Ability Video" not in a["description"]


def test_ability_description_does_not_repeat_the_detail_lines():
    """The wiki spaces colons differently inline than in list items, so the
    subtraction used to match nothing and every ability printed its stat block
    twice — once as prose, once as parsed chips."""
    a = _first_ability(ABILITY_HTML)
    assert "105% Intelligence" not in a["description"]
    assert "10 seconds" not in a["description"]
    # ...while the parsed details keep them.
    assert any("105% Intelligence" in d for d in a["details"])


def test_ability_description_keeps_the_actual_prose():
    a = _first_ability(ABILITY_HTML)
    assert "Summon a moving beam of intense light" in a["description"]


def test_ability_description_strips_the_tagline_up_to_notes():
    """Everything before "Notes:" is a category tagline or the god's own name."""
    a = _first_ability(ABILITY_HTML)
    assert not a["description"].startswith("LINE DAMAGE")
    assert "Notes:" not in a["description"]


# ── Fields the parser used to discard (B1) ────────────────────────────────
# All of this was already in the cached HTML; nothing here needed a refetch.

def test_parse_god_page_recovers_attack_power():
    """Basic-attack damage. Every god page carries it, the STAT_LABELS
    allowlist dropped it, and without it there is no way to compute what an
    auto-attack hits for."""
    html = """<table class="infobox">
      <tr><th>Attack Power:</th><td>47.57 (+2.21)</td></tr>
      <tr><th>Health Regen:</th><td>1.7 (+0.2)</td></tr>
      <tr><th>Mana Regen:</th><td>(+)</td></tr>
    </table>"""
    stats = wiki_parser.parse_god_page(html)["base_stats"]
    assert stats["attack_power"] == {"base": 47.57, "per_level": 2.21}
    assert stats["health_regen"] == {"base": 1.7, "per_level": 0.2}
    # No-mana gods render an empty "(+)" — absent, never a fabricated zero.
    assert "mana_regen" not in stats


def test_detail_kinds_are_parallel_to_details():
    """`detail_kinds[i]` describes `details[i]`. If the two ever drift, every
    consumer reads the wrong line's meaning, so the invariant is the test."""
    for ability in wiki_parser.parse_god_page(_chiron_html())["abilities"]:
        if "detail_kinds" in ability:
            assert len(ability["detail_kinds"]) == len(ability["details"])


def test_ability_damage_type_comes_from_the_wiki_colour():
    """The colour is the only place the page states physical vs magical per
    ability — `get_text()` used to flatten it away."""
    abilities = wiki_parser.parse_god_page(_chiron_html())["abilities"]
    typed = [a for a in abilities if a.get("damage_type")]
    assert typed, "the fixture carries coloured damage lines"
    assert all(a["damage_type"] == "physical" for a in typed)


def _ability_html(lines):
    rows = "".join(f'<li><span style="color:{c};">{t}</span></li>' for c, t in lines)
    return ('<table class="infobox"><tr><th>Health:</th><td>500 (+80)</td></tr></table>'
            '<div class="mw-heading"><h2 id="Abilities">A</h2></div>'
            '<table class="wikitable">'
            '<tr><th><span>1st Ability</span><span>Test</span></th></tr>'
            f'<tr><td><ul>{rows}</ul></td></tr></table>')


def test_mixed_damage_colours_yield_no_damage_type():
    """An ability that genuinely deals both must not be flattened to whichever
    colour the parser happened to read first."""
    a = wiki_parser.parse_god_page(_ability_html([
        ("#ff5f5f", "Damage: 100"), ("#2ca8fd", "Damage: 50")]))["abilities"][0]
    assert "damage_type" not in a
    assert a["detail_kinds"] == ["physical", "magical"]


def test_unrecognised_colour_is_left_unknown():
    """The wiki has a long tail of god-specific colours. Unknown stays None
    rather than being guessed into a category."""
    a = wiki_parser.parse_god_page(_ability_html([
        ("#123456", "Something bespoke"), ("#4fc253", "Heal: 20")]))["abilities"][0]
    assert a["detail_kinds"] == [None, "heal"]


def test_the_two_damage_colours_never_collide():
    """These two carry the whole physical/magical distinction. Checked against
    every god whose damage type we already store: 290 physical lines and 271
    magical, no overlap in either direction across the 247-page cache."""
    assert wiki_parser._DETAIL_KINDS["#ff5f5f"] == "physical"
    assert wiki_parser._DETAIL_KINDS["#2ca8fd"] == "magical"


def test_shipped_god_notes_carry_the_recovered_fields():
    """Coverage counts, not just "it parses". These were absent for months
    while the parser ran clean, so a silent drop is the failure worth catching:
    87/87 gods have Attack Power and 353 abilities carry a damage type."""
    from smite import notes, recommend
    gods = [notes.read_note(p)[0] for p in (recommend.DATA_ROOT / "Gods").glob("*.md")]
    gods = [g for g in gods if g.get("name")]
    assert len(gods) >= 87
    assert all((g.get("base_stats") or {}).get("attack_power") for g in gods)

    abilities = [a for g in gods for a in (g.get("abilities") or [])]
    typed = [a for a in abilities if a.get("damage_type")]
    assert len(typed) >= 350, f"only {len(typed)} abilities carry a damage type"
    assert {a["damage_type"] for a in typed} == {"physical", "magical"}
    for a in abilities:
        if "detail_kinds" in a:
            assert len(a["detail_kinds"]) == len(a["details"])
