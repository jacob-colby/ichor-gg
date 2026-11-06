"""An aspect's kit, derived from the god's own note — never typed by hand.

WHAT THIS IS FOR. Seven gods carry a hand-authored overlay under `aspects:` in
`_weights.yaml` (`stats: {Strength: 1.0, Attack Speed: 0.8}` and so on). The
other aspects had nothing, so the viewer's toggle moved nothing for them, and
an eighth typed overlay for a 3%-pick aspect is tuning, which STATE.md §4
exists to prevent. This module derives the aspect's kit instead: it reads the
aspect's `kit_changes` sentence by sentence, decides WHICH abilities each one
changes from the text, takes every NUMBER from lines already in the note, and
returns a copy of the god whose abilities carry the edit. Nothing downstream
is aspect-aware: `scoring.derived_aspect_overlay` runs the ordinary fit map on
that copy and on the base god and keeps the difference. There is no
god-specific constant and no god name anywhere in this file.

EACH SENTENCE GETS ONE OF FOUR VERDICTS, and the verdict is the product:

  derived        the sentence is a substitution the note can price — "<A x>
                 become(s) <B x> instead", where both terms are labelled in
                 the note (below). The edit is applied.
  unpriced       the sentence changes damage, scaling, healing or a stat, and
                 the note carries no number for the aspect version. Nothing is
                 applied and nothing is guessed — the base lines stay.
  no arithmetic  the sentence changes mechanics only (a pull becomes a root,
                 a projectile stops sticking). There is nothing to price.
  unresolved     a substitution whose terms the note does not define exactly
                 once. Refused, with the reason.

THE ONE SUBSTITUTION RULE. "<A noun> ... become(s) <B noun> instead": two
capitalised phrases sharing a tail (`Shingetsu Ranged Attack` /
`Mangetsu Ranged Attacks`, tail `ranged attack`) and differing in a leading
token. A GRANTOR of a term is an ability with a detail line naming the token
and every tail word (`your next Mangetsu Attack becomes a ranged attack`).
The B term's DEFINITION is the B-grantor's own lines labelled with the B token
(`Mangetsu Bonus Damage: 5`, `Mangetsu Bonus Damage Scaling: 30% Strength +
65% Intelligence`), and it must be one definition, not two that disagree.
Each A-grantor loses its A-labelled lines and gains that definition.

TSUKUYOMI, Aspect of Mangetsu (2026-11-05) — the first case, and a NEGATIVE
result for the build, stated rather than nudged:

  "When gaining Shingetsu Ranged Attack, they become Mangetsu Ranged
   Attacks instead."                              derived: Dark Moon Shuriken
                                                  gains Silver Moon Caltrops'
                                                  30% Str + 65% Int term
  "Dark Moon Shuriken no longer sticks to gods."  no arithmetic
  "Piercing Moonlight hits each target only once
   for major damage in an AoE, ..."               unpriced: no aspect numbers

  The kit's Intelligence share moves 0.475 -> 0.496, and the merged fit map
  moves Intelligence 0.2655 -> 0.2694 and Strength 0.9745 -> 0.9706. That
  changes ZERO cores, in any archetype, in any of the three modes. The brief
  pointed at the passive's 15% Str + 30% Int line instead; taking that one
  gives 0.2673 / 0.9727 and also changes zero. TWO separate reasons, both
  measured:
    * the derived change is SMALL. One 30/65 line joins a kit whose scaling
      lines already sum to ~450 / ~410 percent, so the share moves 2pp;
    * the channel is NARROW. `fit_map` gives the role table 0.7 of every
      offensive column (`kit_blend` 0.3) and the Jungle table names no
      Intelligence, so even an UPPER BOUND that rewrites every non-basic line
      of his kit to 1:2 reaches only Intelligence 0.3006.
  Widening the channel does not rescue it: swept as a diagnostic over
  `kit_blend` 0.3-1.0, the derived family moves a build at exactly ONE
  setting (0.7, one item in `core`, a near-tie) and at none of the others.
  STATE.md §4.33 has the refusal that follows; `kit_blend` is NOT retuned.
"""
import copy
import re

from smite import kit

DERIVED = "derived"
UNPRICED = "unpriced"
NO_ARITHMETIC = "no arithmetic"
UNRESOLVED = "unresolved"

_SENTENCE_END = re.compile(r"(?<=[.!?])\s+")
_CAP_RUN = re.compile(r"[A-Z][\w']*(?:\s+[A-Z][\w']*)*")
_BECOME = re.compile(r"\bbecomes?\b")
_INSTEAD = re.compile(r"\binstead\b", re.IGNORECASE)
# Words that mean the sentence changes a number the build could care about.
# A sentence carrying one and no derivable rule is `unpriced`, never silently
# `no arithmetic` — that would read as "nothing to price" when the truth is
# "nothing to price it WITH".
_PRICED = re.compile(
    r"\b(damage|scaling|heals?|healing|shields?|strength|intelligence|"
    r"attack speed|protections?|lifesteal|cooldown|tenacity|pathfinding)\b",
    re.IGNORECASE)


def sentences(text):
    """The aspect's `kit_changes` split into sentences, stripped."""
    return [s.strip().strip("'\"") for s in _SENTENCE_END.split(str(text or "").strip())
            if s.strip()]


def _singular(word):
    word = word.lower()
    return word[:-1] if word.endswith("s") and not word.endswith("ss") else word


def substitution(sentence):
    """`(token_a, token_b, tail)` for "<A tail> ... become(s) <B tail>
    instead", else None. `tail` is the shared trailing words, lower-case and
    singular — `("ranged", "attack")` for Tsukuyomi."""
    if not _INSTEAD.search(sentence):
        return None
    m = _BECOME.search(sentence)
    if not m:
        return None
    after = _CAP_RUN.findall(sentence[m.end():])
    if not after:
        return None
    b = after[0].split()
    if len(b) < 2:
        return None
    tail = tuple(_singular(w) for w in b[1:])
    for run in reversed(_CAP_RUN.findall(sentence[:m.start()])):
        a = run.split()
        if len(a) == len(b) and tuple(_singular(w) for w in a[1:]) == tail and a[0] != b[0]:
            return a[0], b[0], tail
    return None


def _names_token(line, token, tail):
    words = [_singular(w) for w in re.findall(r"[A-Za-z']+", line)]
    return (re.search(rf"\b{re.escape(token)}\b", line) is not None
            and all(t in words for t in tail))


def _grantors(god, token, tail):
    """Abilities with a detail line naming the term — the token and every
    tail word. The Basic Attack slot is never a grantor."""
    return [ab for ab in god.get("abilities") or []
            if "basic attack" not in str(ab.get("slot") or "").lower()
            and any(_names_token(str(d), token, tail) for d in ab.get("details") or [])]


def _labelled(ability, token):
    """This ability's `<token> ...: value` lines — a term's own numbers."""
    return [str(d) for d in ability.get("details") or []
            if str(d).partition(":")[1] and str(d).startswith(token + " ")]


def _has_scaling(lines):
    return any("scaling" in l.lower() and kit._SCALING_LINE.search(l) for l in lines)


def ability_names(god, sentence):
    """Abilities of this god the sentence names, in kit order."""
    low = sentence.lower()
    return [ab["name"] for ab in god.get("abilities") or []
            if ab.get("name") and ab["name"].lower() in low]


def apply(god, aspect):
    """`(variant, edits)` — a deep copy of `god` with every DERIVED sentence
    applied to its abilities, and one record per sentence:
    `{sentence, verdict, abilities, reason, added}`. `variant` is `god`'s
    copy unchanged when nothing derives."""
    variant = copy.deepcopy(god)
    edits = []
    for s in sentences((aspect or {}).get("kit_changes")):
        named = ability_names(god, s)
        sub = substitution(s)
        if sub:
            edits.append(_substitute(variant, s, sub, named))
        elif _PRICED.search(s):
            edits.append({"sentence": s, "verdict": UNPRICED, "abilities": named,
                          "reason": "changes a priced quantity and the note carries "
                                    "no number for the aspect version", "added": []})
        else:
            edits.append({"sentence": s, "verdict": NO_ARITHMETIC, "abilities": named,
                          "reason": "mechanics only", "added": []})
    return variant, edits


def _substitute(variant, sentence, sub, named):
    token_a, token_b, tail = sub
    record = {"sentence": sentence, "abilities": named, "added": [],
              "substitution": [token_a, token_b, " ".join(tail)]}
    grant_a = _grantors(variant, token_a, tail)
    grant_b = _grantors(variant, token_b, tail)
    defs = {tuple(_labelled(ab, token_b)) for ab in grant_b}
    defs = {d for d in defs if _has_scaling(d)}
    if not grant_a:
        return {**record, "verdict": UNRESOLVED,
                "reason": f"no ability grants a {token_a} {' '.join(tail)}"}
    if len(defs) != 1:
        return {**record, "verdict": UNRESOLVED,
                "reason": f"{len(defs)} scaling definitions of {token_b} "
                          f"{' '.join(tail)} in the note (need exactly 1)"}
    (lines,) = defs
    b_names = {ab["name"] for ab in grant_b}
    changed = []
    for ab in grant_a:
        if ab["name"] in b_names:
            continue
        own = set(_labelled(ab, token_a))
        ab["details"] = [d for d in ab.get("details") or [] if str(d) not in own] + list(lines)
        changed.append(ab["name"])
    if not changed:
        return {**record, "verdict": UNRESOLVED,
                "reason": f"every {token_a} grantor already grants {token_b}"}
    return {**record, "verdict": DERIVED, "abilities": changed, "added": list(lines),
            "reason": f"{token_a} {' '.join(tail)} takes {token_b}'s lines from "
                      f"{', '.join(sorted(b_names))}"}
