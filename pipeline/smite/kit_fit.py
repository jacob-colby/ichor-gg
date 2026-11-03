"""Does a god's KIT use an item well? One check, built once, read by every
caller that needs it (2026-11-03).

WHY IT EXISTS. Two problems turned out to be the same problem:

  * Lotus Sickle (data/_tags.yaml, Jacob 2026-11-03): its passive needs
    "Ability Buffed, Healed, or Shielded another Allied God". Any tag put it
    into Agni's Joust core over Doom Orb, and Agni's kit does none of that, so
    it is held at `[]` "until a kit check exists". This is that check.
  * The draft's team-level tags (`viewer/src/lib/teamTags.ts`): with no
    teammate holding anti-heal, the "you are the carrier" delta pulled an
    anti-heal item onto 93 of 94 Joust boards, because the draft's swap rule
    spends draft evidence and never asks whether the god can use the item.

So this module answers "can this god use this item" from two things the repo
already has, and nothing new is fitted:

  1. CAPABILITIES of a kit, read off its ability TEXT (`capabilities`):
       ally_support  an ability buffs, heals or shields an ALLY — a line
                     naming an ally and a helping verb, and no enemy. 26 of
                     94 kits on Open Beta 46 (Support 8/15, Mid 8/23, Solo
                     7/19, Carry 3/19, Jungle 0/18). Walls and taunts are
                     PEEL, not this, so Ymir and Athena do not pass.
       melee         the basic attack's range is melee (`side_by_side.is_melee`)
  2. NEEDS of an item, read off its passive TEXT (`item_needs`):
       ally_support  the passive TRIGGERS on you helping an ally ("Healed, or
                     Shielded another Allied God", "Ability Healed an Ally",
                     "When you heal with abilities"). Lotus Sickle, Soul
                     Locket, Rod of Asclepius, Heartwood Charm.
       near_allies   the passive helps allies near YOU ("You and allies
                     within 8.8m", "Allies within 8.8m"). Met by ally_support
                     or melee: a ranged damage dealer is the god least often
                     standing in an ally's 8.8m.
  3. STAT FIT (`stat_fits`): the item's fit score for this god with every tag
     bonus removed — the model's own reading of whether the item's stats suit
     the kit — against the LOWEST of the same score over the god's shipped
     core (`fit_floor`): an item that suits the kit at least as well as one
     the model already chose. The median was tried first and passed 5 of 470
     (god, anti-heal item) pairs in Joust — core items are SELECTED for fit,
     so their median is the wrong bar — and the lower quartile left 0 of 23
     Mids able to take Divine Ruin. At the minimum: 64 of 94 gods can take an
     anti-heal item, 54 a team aura (Support 15/15 and 15/15, Solo 18 and 19,
     Carry 18 and 10, Mid 7 and 8, Jungle 6 and 2).

`fits(god, item, ...)` is all three: every need met, and stat fit at or above
the floor. It returns its reasons, so a caller can print why.
"""
import re

from smite import scoring

_ALLY = re.compile(r"\b(?:all(?:y|ies|ied))\b", re.I)
_HELP = re.compile(r"\b(?:heal|heals|healing|shield|shields|protections?|buff|buffs|grant|grants|"
                   r"gain|gains|speed|damage reduction|cleanse|restore)\b", re.I)
_ENEMY = re.compile(r"\benem", re.I)
_TRIGGERED = re.compile(r"(?:Buffed|Healed|Shielded)[^.]{0,40}(?:another Allied|an Ally)|"
                        r"Ability Healed an Ally|heal with abilities|Healing Ability", re.I)
_NEAR_ALLIES = re.compile(r"\ballies (?:within|in range|near)|You and allies", re.I)

CAPABILITIES = ("ally_support", "melee")
#: Which capabilities satisfy a need.
SATISFIES = {"ally_support": ("ally_support",), "near_allies": ("ally_support", "melee")}


def _ability_lines(god):
    for a in god.get("abilities") or []:
        if "Basic Attack" in (a.get("slot") or ""):
            continue
        yield a.get("name"), a.get("description") or ""
        for line in a.get("details") or []:
            yield a.get("name"), line


def capabilities(god):
    """`{capability: evidence or None}` for this kit."""
    from smite.side_by_side import is_melee
    out = {"ally_support": None, "melee": "melee basic attack" if is_melee(god) else None}
    for name, line in _ability_lines(god):
        if _ALLY.search(line) and _HELP.search(line) and not _ENEMY.search(line):
            out["ally_support"] = f"{name}: {line[:80]}"
            break
    return out


def item_needs(item):
    """The capabilities an item's passive needs, off its text."""
    text = item.get("passive") or ""
    needs = set()
    if _TRIGGERED.search(text):
        needs.add("ally_support")
    elif _NEAR_ALLIES.search(text):
        needs.add("near_allies")
    return needs


def stat_fits(god, items, weights, tags_map, eff_scores, mode="Conquest"):
    """`{item: fit}` for this god with every TAG bonus removed — the shipped
    `score_god_items` fit (stat references, adaptive grants, offense tags
    and all), under this mode's profile minus its `tag_bonus`."""
    prof = dict(scoring.resolve_profile(weights, mode))
    prof["tag_bonus"] = {}
    rows = scoring.score_god_items(god, items, {"builds": []}, eff_scores, weights, tags_map, prof)
    return {r["item"]: r["fit"] for r in rows}


def fit_floor(fits_by_item, core_names):
    """The lowest tag-free fit over the god's shipped core (docstring, 3)."""
    vals = [fits_by_item[n] for n in core_names if n in fits_by_item]
    return min(vals) if vals else 0.0


def fits(god, item, fit_value, floor, caps=None):
    """`(ok, reasons)`: every need met by a capability, and tag-free stat fit
    `fit_value` at or above `floor`."""
    caps = capabilities(god) if caps is None else caps
    reasons = []
    for need in sorted(item_needs(item)):
        if not any(caps.get(c) for c in SATISFIES[need]):
            reasons.append(f"needs {need}")
    if fit_value is None or fit_value < floor:
        reasons.append(f"stat fit {fit_value if fit_value is not None else 0:.2f} < core floor {floor:.2f}")
    return not reasons, reasons
