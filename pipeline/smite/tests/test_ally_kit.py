"""`ally_kit`: the gate that keeps an ally-dependent item off a god whose kit
cannot buff, heal or shield an allied god (2026-11-04).

The NAMED cases here are pins, not targets: a wiki rewording that drops one of
them out of the qualifying set, or flips a rejection case in, should turn a test
red rather than silently change a shipped build.

The roster SIZE is not pinned (2026-11-14). It was, at 31 base / 37 with
aspects, and that pin rejected the wiki stats refresh on every daily run from
2026-11-10: the wiki filled in Nox's Aspect of Silent Night ("Shadow Step
provides a Magical Shield to Nox and a ally"), a real ally shield, and the
count went to 38 for a correct reason. An exact count cannot tell that from a
parser regression, so it blocks a correct patch as readily as a bad one. What
it stood for is held instead by the named gods below plus a sanity range.
"""
import pytest

from smite import ally_kit, assemble, efficiency, notes, recommend, scoring


def _gods():
    return {g["name"]: g for g in recommend.load_gods()}


def _items():
    return recommend.load_items()


# ── the item half: the TRIGGER, not the recipient ────────────────────────────

def test_the_gated_items_include_the_four_that_demand_an_ally_buff():
    """A superset, not an equality (2026-11-14). The item half is derived from
    live text precisely so that an item a refresh discovers with the same
    trigger is gated "the moment it arrives, with no hand edit" (`ally_kit`'s
    docstring). An exact set would turn that arrival into a red test, and since
    `stats_gate` rejects a refresh on a red test, it would freeze every item
    and god stat until someone edited this line. The four named items must stay
    gated; the size bound is a reader-collapse alarm, since the trigger phrase
    is rare and a regex that started matching "ally" alone would gate dozens."""
    gated = ally_kit.ally_dependent_items(_items())
    assert {"Lotus Sickle", "Soul Locket", "Eros' Bow", "Rod of Asclepius"} <= gated
    assert len(gated) <= 10, sorted(gated)


def test_a_new_item_with_the_trigger_is_gated_with_no_hand_edit():
    new = {"name": "Unreleased Charm (fixture)", "passive":
           "If your Ability Buffed, Healed, or Shielded another Allied God, gain a stack."}
    assert ally_kit.requires_allied_god(new)


def test_ally_directed_items_that_need_nothing_of_your_kit_are_not_gated():
    """`_passive_classes.yaml`'s `D1 ally-directed` is the WRONG predicate: all
    three of these land their value on allies while the ITEM does the buffing,
    so they stay available to everyone."""
    by_name = {i["name"]: i for i in _items()}
    for name in ("Triton's Conch", "Chandra's Grace", "Amanita Charm",
                 "Shogun's Ofuda", "Stampede", "Heartwood Charm"):
        assert not ally_kit.requires_allied_god(by_name[name]), name


def test_lotus_sickle_is_gated_on_its_own_passive_text():
    sickle = next(i for i in _items() if i["name"] == "Lotus Sickle")
    assert "Buffed, Healed, or Shielded another Allied God" in sickle["passive"]
    assert ally_kit.requires_allied_god(sickle)


# ── the god half ─────────────────────────────────────────────────────────────

def test_the_named_pair_from_the_defect_report():
    """Ra buffs allied gods with Solar Blessing; Agni has no ally effect at
    all. This is the case Jacob named."""
    g = _gods()
    assert ally_kit.buffs_allied_god(g["Ra"])
    assert not ally_kit.buffs_allied_god(g["Agni"])


def test_roster_shape():
    """Properties, not counts (see the module docstring). An aspect only ever
    ADDS to a kit for this gate, so the base set sits inside the aspect set.
    The range is a parser-collapse alarm, not a pin: 31 / 38 of 95 on
    2026-11-14, and either bound moving means the reader broke, not that a
    patch landed. A count anywhere inside it is a patch's business, and the
    named cases in this file say whether the reader still reads."""
    gods = recommend.load_gods()
    base = {g["name"] for g in gods if ally_kit.buffs_allied_god(g)}
    with_aspects = {g["name"] for g in gods
                    if ally_kit.buffs_allied_god(g, include_aspects=True)}
    assert base <= with_aspects, sorted(base - with_aspects)
    assert 20 <= len(base) <= 50, len(base)
    assert 20 <= len(with_aspects) <= 55, len(with_aspects)
    # Most of the roster cannot buff an ally; a reader that says most can has
    # started accepting the minion / gold / wall clauses the rejection tests name.
    assert len(with_aspects) < len(gods) * 0.6, (len(with_aspects), len(gods))


def test_a_text_match_for_allied_god_would_have_been_far_too_narrow():
    """The crude probe that found the defect searched for "allied god" and
    found 2 of the 25 gods the item reached. These eight say it some other
    way, and every one of them really does buff, heal or shield an ally."""
    g = _gods()
    for name in ("Yemoja", "Athena", "Khepri", "Hades", "Baron Samedi",
                 "Cupid", "Aphrodite", "Gilgamesh"):
        assert ally_kit.buffs_allied_god(g[name]), name


def test_the_ally_effect_is_read_from_the_description_too():
    """`detail_kinds` alone finds 24 gods; these eight state the ally effect
    only in the ability description, which carries no kinds."""
    g = _gods()
    for name in ("Ares", "Charon", "Ganesha", "Horus", "Ix Chel",
                 "Hachiman", "Apollo", "Artio"):
        assert ally_kit.buffs_allied_god(g[name]), name
        assert any(where == "description"
                   for _, where, _ in ally_kit.ally_evidence(g[name])), name


# ── an ally word near a benefit word is not an ally buff ─────────────────────

def test_allies_who_are_not_being_buffed_do_not_qualify():
    """Summoned minions (Anubis), gold pickups (Danzaburou) and "I gain a
    resource when an ally is hit" (Cu Chulainn) all put an ally word next to a
    benefit word without buffing anybody."""
    g = _gods()
    for name in ("Anubis", "Danzaburou", "Cu Chulainn"):
        assert not ally_kit.buffs_allied_god(g[name], include_aspects=True), name


def test_the_ferry_and_the_wall_are_not_cited_as_evidence():
    """Charon and Ganesha both qualify, but NOT on these clauses: being
    ferried makes allies "take 50% of the damage you take", and Ganesha's
    walls are scenery. A gate that accepted either would accept Danzaburou's
    coins next."""
    g = _gods()
    charon = " ".join(c for _, _, c in ally_kit.ally_evidence(g["Charon"]))
    assert "50% of the damage" not in charon
    ganesha = " ".join(c for _, _, c in ally_kit.ally_evidence(g["Ganesha"]))
    assert "ally walls" not in ganesha


# ── aspects are a different kit ──────────────────────────────────────────────

def test_an_aspect_can_be_the_only_thing_that_qualifies_a_god():
    """These gods buff an ally only with their aspect selected. Hercules and
    Chronos are the two of them that ship an aspect variant, so they are the
    two where the distinction changes a build."""
    g = _gods()
    for name in ("Hercules", "Chronos", "Bastet", "Fenrir", "Jormungandr", "Nut"):
        assert not ally_kit.buffs_allied_god(g[name]), name
        assert ally_kit.buffs_allied_god(g[name], include_aspects=True), name


def test_nox_silent_night_shields_an_ally():
    """The clause that took the old roster pin from 37 to 38 (2026-11-14), when
    the wiki replaced Aspect of Silent Night's "Coming Soon" with its kit text.
    Held as TEXT, not off Nox's live note, so it passes on the stats either
    side of that refresh: the property is that the reader reads this shape of
    sentence as an ally shield, and the gate keeping Nox's aspect build
    eligible follows from it."""
    nox = {"name": "Nox (fixture)", "abilities": [], "aspects": [{
        "name": "Aspect of Silent Night",
        "kit_changes": ("Flame of the Night provides Damening and a Magical "
                        "Shield. Shadow Step provides a Magical Shield to Nox "
                        "and a ally, fears when exiting an ally, but deals no "
                        "damage."),
    }]}
    assert not ally_kit.buffs_allied_god(nox)
    assert ally_kit.buffs_allied_god(nox, include_aspects=True)
    (evidence,) = ally_kit.ally_evidence(nox)
    assert evidence[0] == "Aspect of Silent Night"
    assert "Magical Shield to Nox and a ally" in evidence[2]


def test_the_base_kit_is_the_default():
    """The asymmetry matters: asking the aspect question for a base build
    ships an item the player cannot trigger."""
    g = _gods()
    items = _items()
    assert "Lotus Sickle" in ally_kit.excluded_for(g["Hercules"], items)
    assert ally_kit.excluded_for(g["Hercules"], items, include_aspects=True) == frozenset()


# ── the gate where builds are made ───────────────────────────────────────────

def _scored(god_name, profile=None):
    g = _gods()[god_name]
    items = _items()
    eff, _ = efficiency.efficiency_scores(items)
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    tags = scoring.load_tags(recommend.TAGS_PATH)
    prof = profile if profile is not None else scoring.resolve_profile(weights, "Conquest")
    rows = scoring.score_god_items(g, items, {}, eff, weights, tags, prof)
    return {r["item"] for r in rows}


def test_score_god_items_withholds_the_item_from_a_god_who_cannot_trigger_it():
    assert "Lotus Sickle" not in _scored("Agni")
    assert "Eros' Bow" not in _scored("Zeus")


def test_a_qualifying_god_keeps_access():
    names = _scored("Ra")
    assert "Lotus Sickle" in names


def test_a_flavor_cannot_bypass_the_ally_gate():
    """Mirrors `test_excluded_items_survive_a_flavor_bypass`: a fun flavor may
    escape the damage filter, but an item the kit cannot trigger is not a
    daring pick."""
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    prof = dict(scoring.resolve_profile(weights, "Conquest"),
                bypass_damage_filter=True, archetype_bypass=True, fun=True)
    assert "Lotus Sickle" not in _scored("Agni", prof)


def test_the_aspect_variant_profile_reopens_access():
    """`resolve_profile` marks an aspect build, and that is what lets Chronos'
    Time Field aspect keep the two items his base kit cannot trigger — the
    shipped `core` this gate actually moves.

    Chronos and not Hercules, although Hercules is the clearer ally-healer:
    both gated items carry Intelligence, so `passes_damage_filter` already
    refuses them to a Strength god, and his aspect build would prove nothing
    about THIS gate. The two filters stack, and that is the right layering."""
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    base = scoring.resolve_profile(weights, "Conquest")
    asp = scoring.resolve_profile(weights, "Conquest",
                                  aspect_overlay=(weights.get("aspects") or {})["Chronos"])
    assert base["aspect_variant"] is False and asp["aspect_variant"] is True
    assert {"Eros' Bow", "Lotus Sickle"}.isdisjoint(_scored("Chronos", base))
    assert {"Eros' Bow", "Lotus Sickle"} <= _scored("Chronos", asp)


# ── the invariant, over every build that ships ───────────────────────────────

def test_no_suggested_build_offers_an_ally_item_to_a_god_who_cannot_use_it():
    """Done-condition 1, asserted over the whole committed corpus: every mode,
    every archetype, every aspect variant, and the flex slots and situational
    swaps as well as the core. `source: community` entries are observed data,
    never a recommendation, so they are not gated."""
    gods = _gods()
    gated = ally_kit.ally_dependent_items(_items())
    offences = []
    for path in sorted(recommend.BUILDS_ROOT.glob("*.md")):
        fm, _ = notes.read_note(path)
        god = gods.get(fm.get("god"))
        if not god:
            continue
        for entry in (fm.get("builds") or []):
            if entry.get("source") == "community":
                continue
            offered = set()
            for slot in (entry.get("slot_order") or []):
                offered.add(slot["name"] if isinstance(slot, dict) else slot)
            offered |= {s for s in (entry.get("flex_slots") or []) if isinstance(s, str)}
            offered |= {sw["swap_item"] for sw in (entry.get("situational_swaps") or [])
                        if sw.get("swap_item")}
            hits = offered & gated
            if not hits:
                continue
            if not ally_kit.buffs_allied_god(god, include_aspects=bool(entry.get("aspect"))):
                offences.append((fm["god"], fm.get("mode"),
                                 entry.get("archetype"), sorted(hits)))
    assert offences == []
