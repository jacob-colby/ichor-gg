"""`aspect_kit` and the derived aspect overlay (2026-11-05, STATE.md §4.33).

The pins at the bottom are the register entry's revisit-if conditions in
executable form. When one turns red, the negative result it records may no
longer hold — read §4.33 before "fixing" the test.
"""
import ast
import inspect

import pytest

from smite import aspect_kit, recommend, scoring

MANGETSU = ("When gaining Shingetsu Ranged Attack, they become Mangetsu Ranged Attacks "
            "instead. Dark Moon Shuriken no longer sticks to gods. Piercing Moonlight hits "
            "each target only once for major damage in an AoE, before returning to his "
            "casting location.")


def _gods():
    return {g["name"]: g for g in recommend.load_gods()}


def _weights():
    return scoring.load_weights(recommend.WEIGHTS_PATH)


def _god(abilities, kit_changes, damage_type="physical"):
    """A god nobody plays, so nothing below can pass on a name."""
    return {"name": "Nobody", "damage_type": damage_type, "role": "Jungle",
            "abilities": abilities,
            "aspects": [{"name": "Aspect of Nothing", "kit_changes": kit_changes}]}


SYNTHETIC = [
    {"slot": "Basic Attack", "name": "Swing",
     "details": ["Damage Scaling: 100% Strength + 100% Attack Damage"]},
    {"slot": "1st Ability", "name": "Lantern",
     "details": ["After casting, your next Ember Strike becomes a ranged attack",
                 "Damage: 50 | 100", "Damage Scaling: 80% Strength"]},
    {"slot": "2nd Ability", "name": "Glacier",
     "details": ["After casting, your next Frost Strike becomes a ranged attack",
                 "Damage: 40 | 80", "Damage Scaling: 20% Strength",
                 "Frost Bonus Damage: 9", "Frost Bonus Damage Scaling: 10% Strength + 90% Intelligence"]},
]


# ── parsing ──────────────────────────────────────────────────────────────────

def test_mangetsu_reads_as_three_sentences_with_one_substitution():
    s = aspect_kit.sentences(MANGETSU)
    assert len(s) == 3
    assert aspect_kit.substitution(s[0]) == ("Shingetsu", "Mangetsu", ("ranged", "attack"))
    assert aspect_kit.substitution(s[1]) is None
    assert aspect_kit.substitution(s[2]) is None


def test_a_sentence_without_instead_is_not_a_substitution():
    # Ah Puch's "Corpse Explosion becomes Wraith Call" renames an ability; it
    # states no shared term whose numbers could be carried across.
    assert aspect_kit.substitution("Corpse Explosion becomes Wraith Call, which haunts gods.") is None
    assert aspect_kit.substitution("Thor's hammer becomes heavier.") is None


def test_each_mangetsu_sentence_gets_its_verdict():
    variant, edits = aspect_kit.apply(_gods()["Tsukuyomi"],
                                      {"name": "Aspect of Mangetsu", "kit_changes": MANGETSU})
    assert [e["verdict"] for e in edits] == [aspect_kit.DERIVED, aspect_kit.NO_ARITHMETIC,
                                             aspect_kit.UNPRICED]
    assert edits[0]["abilities"] == ["Dark Moon Shuriken"]
    assert edits[2]["abilities"] == ["Piercing Moonlight"]


def test_the_numbers_come_from_the_note_not_from_this_file():
    """The added lines are Silver Moon Caltrops' own Mangetsu lines, read off
    the live note — whatever the wiki prints there is what the Shuriken gets."""
    god = _gods()["Tsukuyomi"]
    caltrops = next(a for a in god["abilities"] if a["name"] == "Silver Moon Caltrops")
    expected = [d for d in caltrops["details"] if d.startswith("Mangetsu ") and ":" in d]
    variant, edits = aspect_kit.apply(god, god["aspects"][0])
    assert edits[0]["added"] == expected
    shuriken = next(a for a in variant["abilities"] if a["name"] == "Dark Moon Shuriken")
    assert shuriken["details"][-len(expected):] == expected
    # the base god is untouched
    base = next(a for a in god["abilities"] if a["name"] == "Dark Moon Shuriken")
    assert not any(d.startswith("Mangetsu ") for d in base["details"])


def test_the_rule_works_on_a_god_and_terms_it_has_never_seen():
    god = _god(SYNTHETIC, "When gaining Ember Ranged Attack, they become Frost Ranged Attacks instead.")
    variant, edits = aspect_kit.apply(god, god["aspects"][0])
    assert edits[0]["verdict"] == aspect_kit.DERIVED
    lantern = next(a for a in variant["abilities"] if a["name"] == "Lantern")
    assert lantern["details"][-1] == "Frost Bonus Damage Scaling: 10% Strength + 90% Intelligence"


def test_a_term_defined_twice_differently_is_refused_not_averaged():
    abilities = SYNTHETIC + [{"slot": "3rd Ability", "name": "Snowfall",
                              "details": ["your next Frost Strike becomes a ranged attack",
                                          "Frost Bonus Damage Scaling: 50% Strength"]}]
    god = _god(abilities, "When gaining Ember Ranged Attack, they become Frost Ranged Attacks instead.")
    _, edits = aspect_kit.apply(god, god["aspects"][0])
    assert edits[0]["verdict"] == aspect_kit.UNRESOLVED
    assert "2 scaling definitions" in edits[0]["reason"]


def test_a_term_nothing_grants_is_refused():
    god = _god(SYNTHETIC, "When gaining Spark Ranged Attack, they become Frost Ranged Attacks instead.")
    _, edits = aspect_kit.apply(god, god["aspects"][0])
    assert edits[0]["verdict"] == aspect_kit.UNRESOLVED


def test_a_damage_change_with_no_numbers_is_unpriced_never_guessed():
    god = _god(SYNTHETIC, "Lantern deals bonus damage scaling with Strength. Glacier no longer slows.")
    variant, edits = aspect_kit.apply(god, god["aspects"][0])
    assert [e["verdict"] for e in edits] == [aspect_kit.UNPRICED, aspect_kit.NO_ARITHMETIC]
    assert variant["abilities"] == god["abilities"]


def test_no_god_name_appears_in_the_module():
    """Done criterion 1 of the 2026-11-05 brief: no god-specific constant and
    no `if god == ...`. The docstrings narrate Tsukuyomi as the worked case,
    so only the CODE is checked: every identifier and every string literal
    that is not a docstring."""
    tree = ast.parse(inspect.getsource(aspect_kit))
    docstrings = {id(n.value) for n in ast.walk(tree)
                  if isinstance(n, ast.Expr) and isinstance(n.value, ast.Constant)}
    code = " ".join([n.id for n in ast.walk(tree) if isinstance(n, ast.Name)] +
                    [n.value for n in ast.walk(tree) if isinstance(n, ast.Constant)
                     and isinstance(n.value, str) and id(n) not in docstrings])
    for name in _gods():
        assert name not in code, name


# ── the overlay ──────────────────────────────────────────────────────────────

def test_the_derived_overlay_reproduces_the_aspect_kits_own_fit_map():
    god, w, items = _gods()["Tsukuyomi"], _weights(), recommend.load_items()
    d = scoring.derived_aspect_overlay(god, items, w)
    assert d["refused"] is None and d["stats"]
    variant, _ = aspect_kit.apply(god, god["aspects"][0])
    base, _ = scoring.fit_map(god, items, w)
    asp, _ = scoring.fit_map(variant, items, w)
    merged = {**base, **d["stats"]}
    assert set(merged) == set(asp) | set(base)
    for k in merged:
        assert merged[k] == pytest.approx(asp.get(k, 0.0), abs=1e-6), k


def test_mangetsu_moves_weight_toward_intelligence():
    god, w = _gods()["Tsukuyomi"], _weights()
    stats = scoring.derived_aspect_overlay(god, recommend.load_items(), w)["stats"]
    base, _ = scoring.fit_map(god, recommend.load_items(), w)
    assert stats["Intelligence"] > base["Intelligence"]
    assert stats["Strength"] < base["Strength"]
    assert set(stats) == {"Intelligence", "Strength"}


def test_a_hand_overlay_wins_and_the_flag_turns_derivation_off():
    gods, w, items = _gods(), _weights(), recommend.load_items()
    assert scoring.aspect_overlay(gods["Hercules"], items, w) == w["aspects"]["Hercules"]
    assert scoring.aspect_overlay(gods["Tsukuyomi"], items, w)["derived"] is True
    assert scoring.aspect_overlay(gods["Tsukuyomi"], items, {**w, "aspect_derive": False}) is None


def test_family_moves_compares_membership_order_and_archetypes():
    base = [{"archetype": "core", "slot_order": ["a", "b"]}]
    assert not recommend._family_moves(base, [{"archetype": "core", "slot_order": ["a", "b"]}])
    assert recommend._family_moves(base, [{"archetype": "core", "slot_order": ["b", "a"]}])
    assert recommend._family_moves(base, [{"archetype": "core", "slot_order": ["a", "b"]},
                                          {"archetype": "hybrid", "slot_order": ["a", "c"]}])


# ── §4.33's revisit-if conditions ────────────────────────────────────────────

def test_only_tsukuyomi_has_a_derivable_aspect_sentence():
    """REVISIT §4.33 WHEN THIS FAILS. On 2026-11-05 every other aspect's text
    names a change the note carries no number for, or a mechanic. A refresh
    that adds aspect numbers, or a second rule in `aspect_kit`, grows this set
    — and each new member is a god whose aspect family may now ship."""
    derives = {g["name"] for g in recommend.load_gods()
               if any(e["verdict"] == aspect_kit.DERIVED
                      for e in aspect_kit.apply(g, (g.get("aspects") or [{}])[0])[1])}
    assert derives == {"Tsukuyomi"}


def test_the_derived_mangetsu_family_moves_no_build():
    """REVISIT §4.33 WHEN THIS FAILS — it is the negative result itself. The
    derived overlay moves Intelligence fit 0.2655 -> 0.2694 and no six in any
    archetype of any mode, so no aspect family ships for Tsukuyomi. If a
    refresh or a model change makes it move, the family ships on its own
    (that is the gate working); confirm in `viewer/public/index.json` and
    update §4.33 rather than this assertion's direction."""
    god, w = _gods()["Tsukuyomi"], _weights()
    from smite import efficiency
    # Module globals: restore them, or every later test inherits the flags.
    prior = efficiency.apply_pricing_flags(w)
    try:
        entries = recommend.build_suggested_entries(
            god, recommend.load_items(), recommend.load_build_note("Tsukuyomi"), w,
            scoring.load_tags(recommend.TAGS_PATH), "Conquest")
    finally:
        efficiency.restore_pricing_flags(prior)
    assert entries and not any(e.get("aspect") for e in entries)
