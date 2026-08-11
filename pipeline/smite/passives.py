"""Numbers hiding in item passive text.

The largest disclosed gap in the model. Every signal reads an item's `stats`
dict; its `passive` is prose nothing has ever parsed. 129 of 130 buildable
items have one, so "the model cannot see passives" means it is partly blind to
almost every item it ranks.

WHAT THIS EXTRACTS, AND WHAT IT DELIBERATELY DOES NOT

Surveying the corpus first was the point, because it says how much is even
reachable:

    grants a named stat with a number     49 of 129   (38%)
    states a damage number                 8          ( 6%)
    neither                               72          (56%)

So a passive DSL cannot reach most of them, and pretending otherwise would
mean inventing values for heals, shields, reveals and silences that no source
quantifies. This module takes only the slice where the passive is doing the
same job the `stats` dict does — granting a stat, unconditionally — and leaves
the rest to the disclosure on the method page.

THE ADAPTIVE-STAT ITEMS ARE THE PRIZE

Eight items read `Adaptive Stat: +X Strength or +Y Intelligence (based on
highest item stat)`. That is an unconditional grant of 20 to 90 power, and it
is invisible: Daybreak Gavel is 2500 gold for 300 Max Health on paper, so the
gold model rated it overpriced by 955. All eight were rated premium, with
residuals from +493 to +1097 — the model telling you that you are overpaying
for items whose main value it never counted.

They are priced as their own column rather than folded into Strength or
Intelligence. The grant is genuinely one good — you get whichever suits your
build — and the two stats carry different gold prices, so choosing one would
mean picking a side of a coin the item never makes you flip.

CONDITIONAL GRANTS ARE EXCLUDED, ON PURPOSE

Thirty-three of the 49 are conditional: `On Use: +25% Strength ... Cooldown:
120s`, `Hit enemy Gods: +8 Attack Damage, stacks to 8`, `Over 75% Health: +30
Strength`. A ten-second buff on a two-minute cooldown is not worth what the
number says, and the honest discount depends on uptime nobody has measured.
Counting them at face value would overprice exactly the items the model
currently underprices, which is not an improvement — it is a different error.
`unconditional_grants` returns nothing for them and `CONDITIONAL_MARKERS`
records how they are recognised.

MEASURED, AND IT DOES NOT HELP. Shipped OFF (`price_passives`).

    pricing                       coverage   win-weighted
    passives invisible (shipped)     51.0%         53.3%
    adaptive grants only             50.4%         52.5%
    percent grants only              50.4%         52.7%
    all unconditional                50.1%         52.4%
    credited at scoring only         50.4%         52.8%

The extraction is right and the prices it produces are visibly better. Every
Adaptive Stat item stopped reading "premium": Daybreak Gavel's residual went
from +955 to +95, Archmage's Gem from +789 to -68. Those were plainly wrong
before and are plainly reasonable now. The recommender still got worse.

The likeliest reason, and it is the same lesson `efficiency_pool` records from
the component experiment: the residual is not trying to be an accurate price.
It is useful BECAUSE it is a systematic under-model. Items whose stat line
understates their value are exactly the items with strong passives — and the
community builds those, so the win-rate signal already carries that
information. Making efficiency "correct" here removed the very disagreement
that made it worth 0.35 of the blend, and left it saying what win rate was
saying already.

That is a hypothesis, not a proof. What is certain is the gate, and the gate
says leave it off.

Kept because the parse is real and useful outside scoring: it is the only
place that can tell a reader an item grants +70 power the model never counted.
"""
import re

# The stat vocabulary the gold model already prices, longest first so
# "Critical Strike Damage" wins over "Critical Strike".
_STATS = sorted(
    ("Strength", "Intelligence", "Attack Speed", "Critical Strike Damage",
     "Critical Chance", "Penetration", "Cooldown Rate", "Lifesteal",
     "Max Health", "Max Mana", "Physical Protection", "Magical Protection",
     "Health Regen", "Mana Regen", "Attack Damage", "Plating", "Dampening",
     "Tenacity", "Echo", "Pathfinding"),
    key=len, reverse=True)

# `Adaptive Stat: +55 Strength or +90 Intelligence (based on highest item stat)`
_ADAPTIVE = re.compile(
    r"Adaptive Stat:\s*\+\s*([\d.]+)\s+Strength\s+or\s+\+\s*([\d.]+)\s+Intelligence",
    re.I)

# A bare `+20% Attack Speed` style grant anywhere in the text.
_GRANT = re.compile(r"\+\s*([\d.]+)\s*(%?)\s*(" + "|".join(map(re.escape, _STATS)) + r")\b")

# Anything that makes a grant situational. Deliberately broad: a false
# "conditional" costs us one item's worth of signal, a false "unconditional"
# overprices an item by its full number.
CONDITIONAL_MARKERS = re.compile(
    r"\bOn Use\b|\bHit\b|\bKill\b|\bAssist\b|\bCritically\b|Consumable|\bStack"
    r"|\bWhen\b|\bWhile\b|\bAfter\b|\bOver\b|\bUnder\b|\bevery\b|\bfor \d"
    # Ceilings and ramps. "Caps at +60 Intelligence" is the value at the END of
    # a scale, not a grant — Bancroft's Talon ramps off MISSING health, so the
    # 60 arrives only when you are nearly dead. Reading it as a flat grant
    # would have overpriced the item by its own headline number.
    r"|caps? at|\bscale[ds]?\b|\bramp"
    # Either/or branches. The Cosmic Horror reads "Echo > Cooldown Rate: ...
    # Echo < Cooldown Rate: ... Echo = Cooldown Rate: ...", three alternatives
    # of which you get one; summing them counted the same grant three times.
    r"|[<>]|\bor\b",
    re.I)

# The adaptive grant's own column. Named so it cannot collide with a real stat
# key and so the shipped gold table reads legibly.
ADAPTIVE_KEY = "Adaptive Power"


def is_conditional(text):
    """Whether a passive's grants depend on a trigger, a stack or a threshold."""
    return bool(CONDITIONAL_MARKERS.search(text or ""))


def unconditional_grants(item):
    """`{column: amount}` the passive grants outright, for the gold model.

    Returns `{}` for a conditional passive, an unparsed one, or an item with no
    passive at all — every one of which is a case where the honest answer is
    "no number", not a guess.
    """
    text = (item.get("passive") or "").strip()
    if not text:
        return {}

    out = {}
    adaptive = _ADAPTIVE.search(text)
    if adaptive:
        # Recorded as the mean of the two branches: the item grants one of
        # them and which one is a property of the buyer, not of the item, so
        # the god-agnostic price should sit between rather than on either.
        out[ADAPTIVE_KEY] = (float(adaptive.group(1)) + float(adaptive.group(2))) / 2

    # The adaptive clause is its own sentence; strip it before looking for
    # plain grants so its numbers are not counted twice.
    rest = _ADAPTIVE.sub("", text)
    if not is_conditional(rest):
        for amount, percent, stat in _GRANT.findall(rest):
            key = f"{stat} %" if percent else stat
            out[key] = out.get(key, 0.0) + float(amount)
    return out


# ── Persistent stacks: the end state you actually play with ────────────────
#
# `CONDITIONAL_MARKERS` matches `\bStack`, so every stacking item was excluded
# from `unconditional_grants` alongside on-use buffs and health thresholds.
# That lumped together two things the game treats as opposites:
#
#   PERSISTENT   Devourer's Gauntlet stacks off minion kills to a 75-stack cap
#                and never drops them. By ten minutes it is +40 Strength and
#                +6.75% Lifesteal, and it stays that for the rest of the match.
#   TRANSIENT    Doom Orb's five stacks "last 10s" and "fall off one at a
#                time"; Hastened Fatalis's buff "lasts 2s"; Necronomicon loses
#                four stacks on death.
#
# A transient stack is worth some fraction of its number that depends on uptime
# nobody has measured — the original judgement, and still right. A persistent
# one is a delayed but unconditional grant, and pricing it at zero is part of
# why the gold model calls these items overpriced: Book of Thoth is in 89% of
# some gods' community builds and the recommender's core took it ZERO times.
#
# Any decay marker at all disqualifies an item. The asymmetry is deliberate and
# matches this module: a missed persistent stacker costs one item's signal, a
# transient one counted at full value overprices it by its own headline number.
_STACK_DECAY = re.compile(
    r"lasts?\s*\d|fall off|On Death:\s*Lose|for \d+\s*s\b|expire", re.I)

_STACK_CAP = re.compile(
    r"\(?\s*max(?:imum)?\s*(\d+)\s*stacks?"
    r"|stacks?\s+up\s+to\s+(\d+)"
    r"|at\s+(\d+)\s+(?:\w+\s+)?stacks?", re.I)

#: Where a per-stack grant starts. The grants themselves are read by `_GRANT`
#: from a bounded window after the cue rather than by one heroic pattern —
#: these lines run "+.4 Strength +0.05% Lifesteal" with no separator, and a
#: single regex that tried to span them kept swallowing the next sentence.
_PER_STACK_CUE = re.compile(
    r"(?:each|per)\s+[\w' ]*?stacks?\s*[:,]?\s*(?:grants?\s*[:,]?\s*)?"
    r"|stacks?\s+grants?\s+", re.I)

#: The at-cap bonus: `At 75 Stacks, gain: +10 Strength`, `At 40 Stacks, Item
#: evolves and gains: +100 Max Health`.
_EVOLVE_CUE = re.compile(
    r"at\s+\d+\s+(?:\w+\s+)?stacks?\s*[,:]?\s*"
    r"(?:item\s+evolves\s+and\s+)?gains?\s*[:,]?\s*", re.I)

#: How far past a cue to read grants. Long enough for the longest real line
#: (Devourer's "+.4 Strength +0.05% Lifesteal") and short enough that the
#: following sentence cannot be absorbed.
_GRANT_WINDOW = 60


#: A sentence break, which is a period followed by space or end — NOT any
#: period. Devourer's Gauntlet grants "+.4 Strength", so splitting on a bare
#: "." cut the fragment at the decimal point and found no grants at all.
_SENTENCE_BREAK = re.compile(r"[.;](?=\s|$)|\bDamage dealt\b")

#: Passive prose says "+10 Mana" where the stats table says "Max Mana". Applied
#: only to grants read here, not to `_GRANT` globally, so the shipped-off
#: `price_passives` path keeps the exact vocabulary it was measured with.
_GRANT_ALIASES = {"Mana": "Max Mana", "Health": "Max Health"}
_ALIAS_GRANT = re.compile(
    r"\+\s*([\d.]+)\s*(%?)\s*(Mana|Health)\b(?!\s*Regen)")


def _grants_after(text, cue, window=_GRANT_WINDOW):
    """Stat grants in the `window` characters following each `cue` match,
    stopping at the first sentence break so a neighbouring clause can't be
    read as part of this one."""
    out = {}
    for m in cue.finditer(text or ""):
        fragment = _SENTENCE_BREAK.split(text[m.end():m.end() + window])[0]
        for amount, percent, stat in _GRANT.findall(fragment):
            key = f"{stat} %" if percent else stat
            out[key] = out.get(key, 0.0) + float(amount)
        # Bare "Mana"/"Health" only where the canonical name did not already
        # claim that span — `_STATS` is longest-first, so "Max Mana" and
        # "Mana Regen" are matched above and must not be counted twice.
        claimed = {s for _, _, s in _GRANT.findall(fragment)}
        for amount, percent, stat in _ALIAS_GRANT.findall(fragment):
            canonical = _GRANT_ALIASES[stat]
            if canonical in claimed:
                continue
            key = f"{canonical} %" if percent else canonical
            out[key] = out.get(key, 0.0) + float(amount)
    return out


def is_persistent_stacker(item):
    """A stacking passive that reaches a cap and keeps it."""
    text = item.get("passive") or ""
    if not re.search(r"stack", text, re.I):
        return False
    if _STACK_DECAY.search(text):
        return False
    return bool(_STACK_CAP.search(text))


def persistent_stack_grants(item):
    """`{column: amount}` this item is worth once its stacks are full.

    cap x per-stack grant, plus any at-cap evolve bonus. Returns `{}` unless
    the cap and the per-stack numbers are both found and no decay clause is
    present, because a half-parsed stack line is a wrong number rather than a
    missing one."""
    if not is_persistent_stacker(item):
        return {}
    text = item.get("passive") or ""
    m = _STACK_CAP.search(text)
    cap = int(next(g for g in m.groups() if g))
    if cap <= 0:
        return {}

    out = {}
    for key, amount in _grants_after(text, _PER_STACK_CUE).items():
        out[key] = out.get(key, 0.0) + amount * cap
    if not out:
        # No per-stack line found. An evolve bonus alone is real but partial,
        # and shipping half an item's value is the error this module exists to
        # avoid — so say nothing rather than say a fraction.
        return {}
    for key, amount in _grants_after(text, _EVOLVE_CUE).items():
        out[key] = out.get(key, 0.0) + amount
    return out

def effective_stats(item, base_values):
    """`base_values` with unconditional passive grants merged in.

    `base_values` is `efficiency.item_stat_values(item)` — the item's own stat
    line, already keyed with units. A passive granting a stat the item also
    lists adds to it, because the game does.
    """
    out = dict(base_values)
    for key, amount in unconditional_grants(item).items():
        out[key] = out.get(key, 0.0) + amount
    return out


def survey(items):
    """Coverage counts for the corpus — what the parser reaches and what it
    leaves behind. Kept as a function so the numbers in this module's docstring
    can be re-derived rather than trusted."""
    total = conditional = parsed = adaptive = 0
    for item in items:
        text = (item.get("passive") or "").strip()
        if not text:
            continue
        total += 1
        if _ADAPTIVE.search(text):
            adaptive += 1
        if unconditional_grants(item):
            parsed += 1
        elif is_conditional(text):
            conditional += 1
    return {"with_passive": total, "parsed": parsed,
            "conditional": conditional, "adaptive": adaptive}
