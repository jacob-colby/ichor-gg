"""Threat classification off ability text — see threat_kit.py.

Every test here is written against a failure the naive version actually had.
"""
from smite import threat_kit


def _ability(description, details=None, name="X", slot="1st Ability"):
    return {"slot": slot, "name": name, "description": description,
            "details": details or []}


def test_health_is_not_healing():
    """`\\bHeal\\w*` matches "Health", which appears in most ability text in the
    game. It reported 124 healing abilities against a true 38."""
    a = _ability("Deal damage based on the target's max Health",
                 ["Health %: 8%", "Max Health Restore: 0"])
    assert "heal" not in threat_kit.classify_ability(a)


def test_anti_heal_is_not_healing():
    """The text that most reliably contains the word "Heal" is ANTI-heal.
    Odin's Ring of Spears says "Enemies in the area cannot Heal" — counting it
    would have the draft buy anti-heal against the gods who bring anti-heal."""
    for text in ["Enemies in the area cannot Heal",
                 "Reduces enemy Healing for a duration",
                 "Enemies hit are Slowed and have Reduced Healing"]:
        assert "heal" not in threat_kit.classify_ability(_ability(text)), text
    # And the detail row spelling of the same thing.
    a = _ability("Slam the ground", ["Healing Reduction: -25%"])
    assert "heal" not in threat_kit.classify_ability(a)


def test_real_healing_still_counts():
    assert "heal" in threat_kit.classify_ability(
        _ability("Immediately Heal yourself and gain Attack Speed"))
    # Named only in a detail row, which is where many secondary effects live.
    assert "heal" in threat_kit.classify_ability(
        _ability("Call down rain", ["Heal: 16 | 18 | 20"]))


def test_a_wall_is_created_not_merely_mentioned():
    """`\\bwall\\b` alone matches 171 abilities, virtually all of them describing
    how a PROJECTILE behaves. Requiring a creation verb takes it to four, which
    is the true count."""
    for text in ["Fires a projectile that stops on walls and enemy gods",
                 "Damages all enemies, and passes through walls",
                 "Bounces off walls, but stops on enemy gods"]:
        assert "wall" not in threat_kit.classify_ability(_ability(text)), text
    assert "wall" in threat_kit.classify_ability(
        _ability("Create a Wall that Knocks Back enemies on creation"))
    assert "wall" in threat_kit.classify_ability(
        _ability("Slam Mjolnir down creating a fissure"))


def test_hard_cc_excludes_slows():
    """Slows are counted separately on purpose: every third ability in the game
    applies one, so folding them into the CC signal would make it a constant."""
    slow_only = threat_kit.classify_ability(
        _ability("Creates a field of ice that deals Damage and Slows"))
    assert "slow" in slow_only and "hard_cc" not in slow_only
    stun = threat_kit.classify_ability(
        _ability("Enemies in front of you are Stunned"))
    assert "hard_cc" in stun


def test_god_kit_counts_abilities_and_ships_zeros():
    """Zeros ship rather than being omitted — the viewer distinguishes
    "measured none" from "not measured", and a missing key reads as the
    second."""
    god = {"abilities": [
        _ability("Create a Wall that Knocks Back enemies"),
        _ability("Enemies in front are Stunned and Slowed"),
    ]}
    kit = threat_kit.god_threat_kit(god)
    assert kit == {"hard_cc": 2, "slow": 1, "heal": 0, "shield": 0, "wall": 1}


def test_a_god_with_no_abilities_is_all_zeros_not_an_error():
    assert threat_kit.god_threat_kit({}) == {
        "hard_cc": 0, "slow": 0, "heal": 0, "shield": 0, "wall": 0}


def test_the_four_wall_gods_are_the_four_wall_gods():
    """An integration check against the real scrape. The class exists because
    NO wiki label describes it, so there is nothing else to cross-check it
    against — and if a patch adds a fifth wall god this should be seen, not
    silently absorbed."""
    from smite import recommend
    gods = recommend.load_gods()
    walls = sorted(g["name"] for g in gods
                   if threat_kit.god_threat_kit(g)["wall"] > 0)
    assert walls == ["Cabrakan", "Odin", "Thor", "Ymir"], walls


def test_measured_healers_strictly_contain_the_labelled_ones():
    """The label is precise and incomplete; the measurement is the wider net.
    If a labelled healer ever measured zero healing abilities that would be a
    parser regression, not a data quirk."""
    from smite import recommend
    gods = recommend.load_gods()
    labelled = [g for g in gods if "Healing" in (g.get("specializations") or [])]
    assert labelled, "expected some gods to carry the Healing label"
    for god in labelled:
        assert threat_kit.god_threat_kit(god)["heal"] > 0, god["name"]
