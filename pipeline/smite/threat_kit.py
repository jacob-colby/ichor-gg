"""What an enemy god's KIT actually does to you, read off the scraped ability
text rather than off the wiki's role labels.

`threats.ts` graded a comp by `specializations` alone — the wiki's `Healing`,
`Lockdown`, `Crowd Control`, `Area Control`, `Carry`, `Tank` labels. STATE.md
§5 has carried the consequence as a known gap since the draft shipped: "A god
who is situationally a healer without the `Healing` label is not counted."
The labels are a two-or-three word summary of a whole kit, and the draft was
counter-building against the summary.

Measured on the current scrape, the label misses a lot. `Healing` is on 11 of
89 gods; 24 actually heal. `Crowd Control` is on 22; 71 land at least one hard
crowd-control effect. Nothing at all labels the class this module was written
for: **player-made walls**, which four gods create (Cabrakan, Odin, Thor,
Ymir) and which are answered by a specific item rather than by a stat.

WHAT THIS IS NOT. These counts say a kit *contains* an effect, not how often
it lands, how long it lasts, or whether the player presses the button. A
one-second slow on a 15-second cooldown counts the same as a three-second
stun. That is the same coarseness the labels had, applied to a much better
denominator, and it is the honest ceiling on text classification — the
alternative is per-ability duration parsing, which the scrape supports for
some gods and not others.

EVERY PATTERN IS NEGATION-CHECKED, because the naive version is badly wrong
here. `\\bHeal\\w*` matches "Health", which is in most ability descriptions in
the game; it reported 124 healing abilities against a true 38. And the text
that most reliably contains the word "Heal" is ANTI-heal — "Reduces enemy
Healing", "Healing Reduction: -25%", Odin's "Enemies in the area cannot Heal".
Counting those as healing would have had the draft buy anti-heal against the
gods who bring anti-heal.
"""
import re

# Hard crowd control: an effect that takes the keyboard away, not one that
# slows you down. Slows are counted separately and deliberately — every third
# ability in the game applies one, so folding them in would make the CC signal
# a constant and it would stop discriminating between comps.
_HARD_CC = re.compile(
    r"\b(stun(s|ned|ning)?|root(s|ed|ing)?|silenc(e|es|ed|ing)|taunt(s|ed|ing)?"
    r"|fear(s|ed|ing)?|banish(es|ed|ing)?|knock[\s-]?up(s)?|knock(s|ed)?[\s-]?back"
    r"|cripple(s|d)?|mesmeriz(e|es|ed)|tremble(s|d)?|disarm(s|ed)?"
    r"|intoxicat(e|es|ed)|polymorph(s|ed)?)\b", re.I)

_SLOW = re.compile(r"\bslow(s|ed|ing)?\b", re.I)

# "Heal" the verb, never "Health" the noun. `\w*` on the stem was the bug.
_HEAL = re.compile(r"\b(heal|heals|healed|healing)\b", re.I)

# Anti-heal wears the same vocabulary as healing. Checked against the WHOLE
# clause, so one reduction phrase anywhere in an ability disqualifies it —
# deliberately conservative: under-counting a healer costs a little anti-heal
# that the community pick rate will still argue for, while over-counting sends
# the draft shopping for anti-heal against Odin.
_ANTI_HEAL = re.compile(
    r"(heal(ing)?\s+reduction|reduc\w*\s+\w*\s*heal|cannot\s+heal|anti[\s-]?heal"
    r"|less\s+heal|reduced\s+heal|no\s+heal)", re.I)

_SHIELD = re.compile(r"\b(shield(s|ed|ing)?)\b", re.I)

# Player-made walls. Written narrowly on purpose: `\bwall\b` alone hits 171
# abilities, virtually all of them describing how a PROJECTILE behaves ("stops
# on walls", "passes through walls", "bounces off walls"). Requiring a creation
# verb takes it to four, which is the true count.
_WALL = re.compile(
    r"\b(creat\w*|summon\w*|form(s|ing)?|erect\w*|rais\w*|deploy\w*)\s+"
    r"(a\s+|an\s+)?[\w\s]{0,24}?(wall|fissure|barrier|cage|ring of)", re.I)

_KINDS = ("hard_cc", "slow", "heal", "shield", "wall")


def _ability_text(ability):
    """Description plus every detail line, as one blob.

    The details carry the numbers and often the only mention of a secondary
    effect — Ymir's Frost Breath names the stun in the description, but plenty
    of abilities only name theirs in a `Stun Duration:` detail row."""
    parts = [ability.get("description") or ""]
    parts += [str(d) for d in (ability.get("details") or [])]
    return " ".join(parts)


def classify_ability(ability):
    """The set of threat kinds one ability presents."""
    text = _ability_text(ability)
    kinds = set()
    if _HARD_CC.search(text):
        kinds.add("hard_cc")
    if _SLOW.search(text):
        kinds.add("slow")
    if _HEAL.search(text) and not _ANTI_HEAL.search(text):
        kinds.add("heal")
    if _SHIELD.search(text):
        kinds.add("shield")
    if _WALL.search(text):
        kinds.add("wall")
    return kinds


def god_threat_kit(god):
    """`{kind: n_abilities}` for one god, zeros included.

    Zeros ship rather than being omitted: the viewer distinguishes "measured
    none" from "not measured", and a missing key reads as the second."""
    counts = {k: 0 for k in _KINDS}
    for ability in (god.get("abilities") or []):
        for kind in classify_ability(ability):
            counts[kind] += 1
    return counts
