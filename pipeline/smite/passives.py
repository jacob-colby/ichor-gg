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

That reasoning is `price_passives`', and `price_passives` ships off. The
carve-out at the bottom of this module (`adaptive_grants`, shipped ON as
`price_adaptive`) makes the opposite choice for the opposite reason, and the
argument for it is written next to the code.

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
import statistics

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


def _grants_after(text, cue, window=_GRANT_WINDOW, stop=None):
    """Stat grants in the `window` characters following each `cue` match,
    stopping at the first sentence break — or at `stop`, the cue that starts
    the NEXT clause.

    `stop` is not belt-and-braces. These lines run without punctuation
    ("+.4 Strength +0.05% Lifesteal At 75 Stacks, gain: +10 Strength"), so the
    per-stack read had nothing but the character window keeping the at-cap
    bonus out of it — and it worked only because 60 characters happened to cut
    "+10 Streng" mid-word so the stat pattern's word boundary failed. A shorter
    item name or a reworded passive would have silently multiplied the evolve
    bonus by the stack cap: on a 75-stack item that is 790 Strength instead of
    40, and nothing would have flagged it."""
    out = {}
    for m in cue.finditer(text or ""):
        fragment = text[m.end():m.end() + window]
        if stop:
            fragment = stop.split(fragment)[0]
        fragment = _SENTENCE_BREAK.split(fragment)[0]
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


def persistent_stack_grants(item, fraction=1.0):
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

    # `fraction` is how much of the cap a real match actually reaches. 1.0 is
    # the item's ceiling, which is what this shipped at and what
    # `price_stacks` was measured on. Anything lower prices the state you play
    # with rather than the state on the tooltip - the same move
    # `conversion_reference` makes by pricing a MEDIAN build instead of a
    # maximal one.
    reached = cap * max(0.0, min(fraction, 1.0))
    out = {}
    for key, amount in _grants_after(text, _PER_STACK_CUE, stop=_EVOLVE_CUE).items():
        out[key] = out.get(key, 0.0) + amount * reached
    if not out:
        # No per-stack line found. An evolve bonus alone is real but partial,
        # and shipping half an item's value is the error this module exists to
        # avoid — so say nothing rather than say a fraction.
        return {}
    # The at-cap bonus only exists AT the cap, so it is scaled too rather than
    # granted in full to a build that never gets there.
    for key, amount in _grants_after(text, _EVOLVE_CUE).items():
        out[key] = out.get(key, 0.0) + amount * max(0.0, min(fraction, 1.0))
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


# ── Crit-damage multipliers: the one passive the combat model can price exactly ──
#
# `combat.py` is calibrated against the game to 0.0% over twelve readings, and
# two of those readings exist specifically to pin crit: the multiplier is 1.50
# where two published sources said 1.65, and Deathbringer's +35% ADDS onto it
# to reach 1.85 rather than multiplying to 2.0. Rage + Deathbringer measured 96
# normal and 179 crit, and 96.770 x 1.85 = 179.025.
#
# Nothing has ever asked. `efficiency` prices stat columns and a crit-damage
# bonus is not a stat; `damage_value.item_damage_gain` walks ability components
# and never touches the basic-attack channel crit lives on. So the single item
# whose passive this project knows the exact value of was priced at zero, and
# the gold model called it premium (+470 residual) while 40% of the community
# builds that reach it buy it.
#
# EXPRESSED AS EQUIVALENT CRITICAL CHANCE, deliberately, rather than as a new
# column. A column carried by ONE item is exactly determined — NNLS drives its
# residual to zero and the coefficient is a fit artifact, which is what
# `efficiency.MIN_STAT_CARRIERS` exists to prevent. Critical Chance already has
# many carriers and a fitted price, so converting into it prices the passive in
# a currency the model can already value.
#
# The conversion is exact for the item alone. Expected basic damage at crit
# chance C and multiplier M is 1 + C(M-1). Adding a bonus B moves M to M+B, and
# the extra crit chance C' that would buy the same at the base multiplier is:
#
#     1 + (M-1)(C + C')  =  1 + (M-1+B)C     ->     C' = C * B / (M-1)
#
# For Deathbringer at its own 20% crit and B = 0.35: C' = 0.20 * 0.35 / 0.50 =
# 14 points of Critical Chance, on top of the 20 it lists.
#
# IT IS A FLOOR, and that is the honest caveat. The conversion uses the item's
# OWN crit chance because the gold model is god-agnostic and item-level; in a
# real crit build carrying 60% chance the same passive is worth 42 points, not
# 14. Understating it is the safe direction — the failure being fixed is
# pricing it at zero.
_CRIT_DAMAGE_GRANT = re.compile(
    r"\+\s*([\d.]+)\s*%\s*Critical\s+Strike\s+Damage", re.I)


def crit_damage_bonus(item):
    """The unconditional crit-damage multiplier an item grants, as a fraction.

    0.0 for anything conditional. `Critically Strike: +8% Ability Damage for
    5s` is a trigger with a duration, not a standing bonus, and every crit
    passive in the pool except Deathbringer's is one of those."""
    text = (item.get("passive") or "").strip()
    if not text or is_conditional(text):
        return 0.0
    m = _CRIT_DAMAGE_GRANT.search(text)
    return float(m.group(1)) / 100.0 if m else 0.0


def crit_damage_as_chance(item):
    """`{"Critical Chance %": points}` for a crit-damage passive, or {}.

    Empty unless the item carries crit chance of its own: a crit-damage bonus
    on an item with no crit chance multiplies a zero, and pricing it would be
    inventing value the item cannot deliver by itself."""
    from smite import combat
    from smite.efficiency import parse_stat_value
    bonus = crit_damage_bonus(item)
    if not bonus:
        return {}
    # Read the raw stat rather than calling `efficiency.item_stat_values`:
    # that function is this one's CALLER when the flag is on, and routing back
    # through it recurses until the stack dies.
    chance = parse_stat_value((item.get("stats") or {}).get("Critical Chance")) or 0.0
    if not chance:
        return {}
    base = combat.CRIT_MULTIPLIER - 1.0
    if base <= 0:
        return {}
    return {"Critical Chance %": chance * bonus / base}


# ── Stat conversion: an item whose value is a function of the rest of the build ──
#
# Four items grant a stat computed from a stat you already own. Nothing else in
# the model can see them, because every signal reads an item's `stats` dict in
# isolation and these items' worth is a property of the whole core.
#
#     Transcendence  +Strength equal to 3% of Mana from Items
#     Book of Thoth  +Intelligence equal to 5% of Mana from Items
#     Rod of Tahuti  +Intelligence equal to 25% of your Intelligence from items
#     Nimble Ring    For every 10 Intelligence: +1 Attack Damage +1% Attack Speed
#
# Three of the four reach ZERO model cores. See
# `docs/plans/2026-08-13-mana-conversion-fit.md` for the full scope; the short
# version is that this splits into two problems.
#
#   Conversion off a stat the build stacks ANYWAY (Rod of Tahuti, Nimble Ring,
#   both off Intelligence) is near-deterministic — a mage builds Intelligence
#   whether or not Tahuti is in the core. At the median mage build of 295
#   Intelligence, Tahuti grants +74 against a sheet value of 80: it is priced
#   at roughly HALF what it is worth.
#
#   Conversion off a stat you would only stack BECAUSE of the item
#   (Transcendence, Book of Thoth, both off Max Mana) is self-referential. At a
#   median physical build of 250 Max Mana, Transcendence is a +21% item; at
#   Ullr's actual 1,550-mana community build it is +46.5 Strength, 2.3x sheet.
#
# WHAT IS IMPLEMENTED HERE IS THE FIRST, CONSERVATIVE HALF. The conversion is
# evaluated against a REFERENCE build total rather than the core actually being
# assembled, so it is one pass with no fixed point to converge. That prices the
# deterministic case correctly and the self-referential case conservatively —
# Transcendence gets its +21%, not its +133%. Chasing the rest needs two-pass
# assembly, which the scope deliberately holds back because adding
# Transcendence raises mana's value, which pulls in more mana items, which
# raises Transcendence again.
#
# `+Strength equal to 3% of Mana from Items` and its two siblings.
_CONVERSION_PERCENT = re.compile(
    r"\+\s*(" + "|".join(map(re.escape, _STATS)) + r")\s+equal to\s+([\d.]+)\s*%\s*"
    r"of\s+(?:your\s+)?(Mana|Intelligence|Strength|Health)\b",
    re.I)

#: `For every 10 Intelligence: +1 Attack Damage +1% Attack Speed`
_CONVERSION_PER = re.compile(
    r"For every\s+([\d.]+)\s+(Mana|Intelligence|Strength|Health)\s*:\s*"
    r"((?:\+\s*[\d.]+\s*%?\s*[A-Za-z][A-Za-z ]*?(?=\s*\+|\s*[.;]|$)\s*)+)",
    re.I)

#: The passive says "Mana"; the stats dict says "Max Mana".
_CONVERSION_SOURCE = {"Mana": "Max Mana", "Health": "Max Health",
                      "Intelligence": "Intelligence", "Strength": "Strength"}


#: Parsed conversions, keyed by (name, passive). `conversion_score_bonus` asks
#: for every candidate at every slot of every pass, so with two-pass assembly
#: on, `calibrate` was re-running these regexes roughly 130 items x 6 slots x
#: 3 passes x 87 gods x every weight combination - and 222 of the 226 items
#: parse to nothing. The cache is on the TEXT, not the dict, so a reworded
#: passive re-parses rather than serving a stale answer.
_CONVERSION_CACHE = {}


def stat_conversions(item):
    """`[(source_stat, rate, {granted: amount_per_unit})]` for one item.

    `rate` is the fraction of the source stat converted. An empty list for
    anything that does not convert, which is 217 of the 226 items.
    """
    text = (item.get("passive") or "").strip()
    if not text:
        return []
    key = (item.get("name"), text)
    cached = _CONVERSION_CACHE.get(key)
    if cached is not None:
        return cached
    # Sentence by sentence, skipping any that is conditional. Book of Thoth
    # converts 5% of mana outright AND another 2% only "At 50 Evolve Stacks";
    # read as one blob those sum to 7% and overprice the item for a build that
    # has not stacked. Same rule the rest of this module applies — an
    # unconditional grant is priced, a conditional one is not.
    clauses = [c for c in _SENTENCE_BREAK.split(text) if c and not is_conditional(c)]
    out = []
    for clause in clauses:
      for granted, pct, source in _CONVERSION_PERCENT.findall(clause):
        src = _CONVERSION_SOURCE.get(source.title())
        if src:
            out.append((src, float(pct) / 100.0, {granted: 1.0}))
    # `For every N X: +M Y` is its own grammar and is never gated by a stack
    # count in the pool today, so it reads the whole text.
    for per, source, grants in _CONVERSION_PER.findall(text):
        src = _CONVERSION_SOURCE.get(source.title())
        if not src or float(per) <= 0:
            continue
        fragment = _SENTENCE_BREAK.split(grants)[0]
        per_unit = {}
        for amount, percent, stat in _GRANT.findall(fragment):
            key = f"{stat} %" if percent else stat
            per_unit[key] = per_unit.get(key, 0.0) + float(amount) / float(per)
        if per_unit:
            out.append((src, 1.0, per_unit))
    _CONVERSION_CACHE[key] = out
    return out


def conversion_grants(item, reference):
    """`{column: amount}` the conversion is worth against a REFERENCE build.

    `reference` is `{stat: typical total across a finished build}` — measured,
    not guessed; see `measure_conversion_reference`. An item's own contribution
    to the source stat is included in that total, which is correct: you own it
    once the item is bought.
    """
    from smite.efficiency import parse_stat_value, stat_key
    # The item's own sheet, keyed the way the regression keys it. Read from the
    # raw dict rather than through `efficiency.item_stat_values`, which is this
    # function's CALLER when the flag is on.
    carried = {stat_key(n, raw) for n, raw in (item.get("stats") or {}).items()
               if parse_stat_value(raw) is not None}

    out = {}
    for source, rate, per_unit in stat_conversions(item):
        pool = (reference or {}).get(source, 0.0)
        if pool <= 0:
            continue
        for key, amount in per_unit.items():
            # AMPLIFY ONLY: price a conversion whose output the item already
            # sells you, and skip one that opens a different channel.
            #
            # Rod of Tahuti turns Intelligence into more Intelligence — anyone
            # who bought it for the Intelligence wants that. Nimble Ring turns
            # Intelligence into ATTACK DAMAGE, which is worth its market price
            # only to a god who both stacks Intelligence and auto-attacks, and
            # the gold model is god-agnostic so it cannot tell. Priced in full
            # it read -869 residual, the best bargain in the game, and reached
            # 52 model cores against 3 community builds in 87. The god-aware
            # judgement belongs to `fit`, which already gates on the god's own
            # stat map; efficiency should not pre-empt it.
            if key not in carried:
                continue
            out[key] = out.get(key, 0.0) + pool * rate * amount
    return out


def measure_conversion_reference(builds, items):
    """`{stat: median total across community builds}` — the reference the
    conversions are priced against.

    Median rather than mean: one 1,050-mana outlier would otherwise price
    Transcendence for a build almost nobody runs. Re-derivable so the constants
    in _weights.yaml stay a measurement rather than a number someone typed.

    OVER BUILDS THAT CARRY THE STAT AT ALL, not over every build. 45 of the 87
    gods are physical and carry zero Intelligence, so a median over all of them
    is 0 — which would price Rod of Tahuti and Nimble Ring at nothing, the two
    items this exists to fix. It is also the wrong question: Tahuti is only
    ever bought by a god who builds Intelligence, so the reference it should be
    measured against is a typical INTELLIGENCE build, not a typical build.
    """
    from smite.efficiency import parse_stat_value
    by_name = {i.get("name"): i for i in items or ()}
    totals = {"Max Mana": [], "Intelligence": []}
    for group in builds or ():
        for entry in (group or {}).get("builds", []):
            if entry.get("source") != "community":
                continue
            names = [s.get("name") for s in entry.get("slot_order") or []
                     if isinstance(s, dict)]
            for stat in totals:
                totals[stat].append(sum(
                    parse_stat_value((by_name.get(n, {}).get("stats") or {}).get(stat)) or 0.0
                    for n in names))
    out = {}
    for stat, vals in totals.items():
        carried = [v for v in vals if v > 0]
        if carried:
            out[stat] = statistics.median(carried)
    return out


# ── The adaptive grant, on one branch: the narrowest carve-out of them all ──
#
# `unconditional_grants` above already reads this clause, and `price_passives`
# already prices it — as its own `Adaptive Power` column, alongside 48 other
# passive grants. That whole class was measured and shipped OFF (STATE.md 4.5).
# This is the same slice of it that the module docstring calls the prize, taken
# on its own, the way `crit_damage_as_chance` and `conversion_grants` were.
#
# It is the least ambiguous member of the class. Every other passive this
# module can reach needs a judgement — is the trigger frequent, does the stack
# persist, is the conversion self-referential. An Adaptive Stat grant needs
# none: it is a stat, granted unconditionally, on an item that carries it
# nowhere in `stats`. Eight buildable items are affected and ALL EIGHT read
# `premium`, four of them off a one-entry stats dict, so the gold model prices
# a 2500g item off a single stat and then reports that you are overpaying for
# it by ~1000 gold.
#
# WHICH BRANCH — THE ONE DESIGN QUESTION, AND THE ANSWER IS STRENGTH
#
# The clause reads `+X Strength or +Y Intelligence (based on highest item
# stat)`, so which stat you get is a property of the BUYER and the gold model
# is god-agnostic. It cannot be both: a regression column is one good.
#
# Three things settled it, in order of weight.
#
# 1. NO FIXED POINT. `conversion_grants` prices against a reference build
#    precisely so there is nothing to converge (see its block above), and the
#    same discipline applies here. "Whichever branch is cheaper in gold" needs
#    the fitted prices, which are the output of the fit this feeds — so it
#    would have to be iterated. A branch chosen from the item's own text does
#    not.
#
# 2. STRENGTH IS THE CONSERVATIVE BRANCH ON 6 OF THE 8. At the control fit
#    (Strength 18.56 g/pt, Intelligence 12.70 g/pt) the two branches are worth,
#    in gold:
#
#        item                    as Strength   as Intelligence
#        Mercury's Talaria         40 ->  742    70 ->  889
#        Daybreak Gavel            60 -> 1114    80 -> 1016   <- Int cheaper
#        Omen Drum                 55 -> 1021    90 -> 1143
#        Eye of Erebus             35 ->  650    50 ->  635   <- Int cheaper
#        Vital Amplifier           30 ->  557    45 ->  572
#        Sun Beam Bow              20 ->  371    40 ->  508
#        The Executioner           30 ->  557    55 ->  699
#        Brawler's Beat Stick      30 ->  557    45 ->  572
#
#    Strength is the smaller credit on six, and the two that go the other way
#    do so by 9% and 2%. Understating is the safe direction — the failure being
#    fixed is pricing the grant at ZERO, and it is the same call
#    `crit_damage_as_chance` records as "IT IS A FLOOR".
#
# 3. THE CHOICE BARELY MATTERS, WHICH IS ITSELF THE FINDING. The game's
#    Intelligence:Strength branch ratio runs 1.33x to 2.00x and the fit prices
#    Strength at 1.46x Intelligence, so the branches cash out within ~10% of
#    each other on every item above. Both arms were swept anyway; see
#    `adaptive_branch` in _weights.yaml for the numbers.
#
# NOT ITS OWN COLUMN, which is what `price_passives` does and is the "refuse to
# choose" answer. Eight tier-3 carriers plus nine tier-2 ones is above
# `efficiency.MIN_STAT_CARRIERS`, but it is the same defect in weaker form:
# `Adaptive Power` appears on no item that is not in this set, so NNLS can fit
# one coefficient that eats the class's residual without any other item in the
# pool disagreeing. Strength and Intelligence have dozens of carriers and a
# price the whole pool constrains, so pricing INTO one of them values the grant
# at a rate the rest of the game already agreed to.
#
# MEASURED 2026-08-21, AND IT SHIPS ON. Leakage-free coverage against a 5.74%
# random-core baseline: probe split 37.7% -> 38.7%, best split 38.4% -> 39.6%.
# Both branches beat control on both splits and Strength beats Intelligence on
# both. The sweep, the paired bootstrap (both intervals contain zero), the core
# churn and the diagnostic control live under `price_adaptive` in
# _weights.yaml, because those are numbers about the CONFIGURATION.
#
# ONE OF THEM BELONGS HERE, because it is a fact about this extraction rather
# than about the setting: NONE OF THE EIGHT ITEMS ENTERS A MODEL CORE, before
# or after, on either split. The gain is not those items being picked. It is
# that 29 items sat in the regression with ~1000g apiece that no column
# explained, and NNLS was parking it in the intercept — 1111 with the flag off,
# 934 with it on, which reprices Strength 18.56 -> 21.81 and Intelligence
# 12.70 -> 14.77 for every item in the game. This fixes a misprice of the whole
# pool BY WAY OF eight items; it does not fix the eight items.
BRANCHES = ("strength", "intelligence")


def adaptive_grants(item, branch="strength"):
    """`{stat: amount}` for one item's Adaptive Stat clause, on `branch`.

    `{}` for the 197 items that carry no such clause. The amount is the branch
    as printed, not the mean of the two — `unconditional_grants` records the
    mean because it prices the grant as its own god-agnostic column, and this
    function exists to make the other choice.
    """
    text = (item.get("passive") or "").strip()
    if not text:
        return {}
    match = _ADAPTIVE.search(text)
    if not match:
        return {}
    key = str(branch or "").strip().lower()
    if key not in BRANCHES:
        raise ValueError(f"adaptive_branch must be one of {BRANCHES}, got {branch!r}")
    return ({"Strength": float(match.group(1))} if key == "strength"
            else {"Intelligence": float(match.group(2))})


# ── "% of all Stats from Items": the multiplier on the rest of the build ──
#
# Catalogue class A2 (docs/PASSIVES.md, STATE.md §4.20). Four buildable relics
# read `+7.5% of all Stats from Items` (Agility Greaves, Shell of Rebuke,
# Talisman of Purification) or `+6%` (Time-lock Aegis), and Genie's Lamp reads
# `+0.6% (per Level) of all Stats from Items`. It is the conversion shape with
# SOURCE = EVERY STAT: the item's worth is a function of the build around it,
# which is exactly what `conversion_grants` prices for Transcendence, and it
# was the backlog's "cannot be modelled at all" case only because nothing had
# named the shape.
#
# PRICED AGAINST A POOL-DERIVED REFERENCE, NOT A COMMUNITY ONE. The precedent
# above prices against `conversion_reference`, a median over COMMUNITY builds
# — a community-derived number inside a shipped flag, which the catalogue
# names as a leak and which is its own session (STATE.md §5). This reference
# is `measure_multiplier_reference`: the mean printed stat line of a tier-3
# buildable item, from item data alone, times the five other slots. It is
# god-agnostic on purpose (efficiency is), and the god side is already handled
# downstream — `offmap_efficiency` bills the share of the grant on stats the
# god's map does not name, so a Carry is not credited for the Intelligence
# a pool-mean build carries.
#
# ONE PASS, NO FIXED POINT, the same discipline as `conversion_grants`: the
# grant is X% of a typical build, never of the core being assembled, so
# adding Shell of Rebuke cannot raise the value of Shell of Rebuke.
#
# PREDICTIONS WRITTEN BEFORE THE SWEEP (STATE.md §4.16's trap, deliberately
# not walked into): at the shipped fit the reference is worth 7,133 gold of
# priced stats, so 7.5% is 535 gold and 6% is 428. Residuals should move
# Shell of Rebuke +740 -> ~+205, Talisman +1,022 -> ~+487, Time-lock +946 ->
# ~+518, Agility Greaves +1,566 -> ~+1,031. Shell is the only one of the four
# with a community record (20 of 543 Conquest slots; the other three have 0),
# so leakage-free coverage can move ONLY through Shell, and a move larger
# than 20 slots can account for is something else and must be reported as
# such, not explained. Numbers under `price_stat_multipliers` in _weights.yaml.
#
# THE LAMP IS PARSED AND REACHES NOTHING, and that is pinned by a test rather
# than assumed. Its clause is per-Level, so it needs a level to evaluate; the
# scorer states no level (`build_quality` uses 20, in a diagnostic), so
# `item_stat_values` passes none and the Lamp's grant is zero there. It would
# not matter if it were not: the Lamp has no cost and no printed stats, so it
# has no residual and `scoring.is_buildable` refuses it. Giving it a price is
# writing a constant, which is the one thing this module does not do.
_ALL_STATS_MULTIPLIER = re.compile(
    r"\+\s*([\d.]+)\s*%\s*(\(\s*per\s+Level\s*\)\s*)?of\s+all\s+Stats\s+from\s+Items",
    re.I)


def all_stats_multiplier(item, level=None):
    """The fraction of the rest of the build's stats this item grants, or 0.0.

    A `(per Level)` clause is multiplied by `level`, and is 0.0 when no level
    is given — the caller has to SAY which level it means. The flat form needs
    none and is the only form the four buildable carriers use."""
    text = (item.get("passive") or "").strip()
    if not text:
        return 0.0
    m = _ALL_STATS_MULTIPLIER.search(text)
    if not m:
        return 0.0
    fraction = float(m.group(1)) / 100.0
    if m.group(2):
        return fraction * level if level else 0.0
    return fraction


def measure_multiplier_reference(items, slots=5):
    """`{column: typical total across the OTHER five slots}` — the reference a
    "% of all Stats from Items" clause is priced against.

    Mean printed stat line over god-agnostic buildable TIER-3 items (relics
    and god-specific items excluded — a relic is the item being priced, and a
    typical build is five tier-3 items around it), keyed the way the
    regression keys columns, times `slots`. Zeros count in the mean: a stat
    carried by 12 of 134 items is worth 12/134 of its typical roll to a
    typical slot, which is what "all Stats from Items" averages over.

    Item data only — no community build enters. Re-derivable so the numbers
    in _weights.yaml stay a measurement rather than something typed."""
    from smite import scoring
    from smite.efficiency import parse_stat_value, stat_key
    pool = [it for it in items or ()
            if scoring.is_buildable(it) and it.get("tier") == 3]
    if not pool:
        return {}
    totals = {}
    for it in pool:
        for name, raw in (it.get("stats") or {}).items():
            val = parse_stat_value(raw)
            if val is not None:
                key = stat_key(name, raw)
                totals[key] = totals.get(key, 0.0) + val
    n = len(pool)
    return {key: round(total / n * slots, 4) for key, total in sorted(totals.items())}


def multiplier_grants(item, reference, level=None):
    """`{column: amount}` a "% of all Stats" clause is worth against `reference`.

    Every column of the reference, scaled — the passive really does grant every
    stat the build carries, and which of them the buyer can use is the god
    side's judgement (`offmap_efficiency`), not this function's. `{}` for the
    133 buildable items without the clause, and for a per-Level clause with no
    level."""
    fraction = all_stats_multiplier(item, level=level)
    if fraction <= 0 or not reference:
        return {}
    return {key: fraction * float(amount) for key, amount in reference.items()
            if float(amount) > 0}


# ── Flat bonus damage on every basic attack: the attack channel's own unit ──
#
# Catalogue class B1 (docs/PASSIVES.md, STATE.md §4.20), the flat unconditional
# members only. Three buildable items read it — Tyrfing ("Attacks deal +15
# bonus Physical Damage"), Bragi's Harp ("Attack Hit: +10 (+3 per Level) bonus
# Magical Damage") and Golden Blade ("Attacks deal bonus Physical Damage.
# Damage = +10 + 20% of your Item Protections") — and the survey behind that
# list ran over all 226 items: no component carries one (Bumba's Spear is a
# percentage splash to OTHER enemies), and every other on-hit clause in the
# pool is gated (Odysseus' every-fourth-hit, Silverbranch's every-third,
# Hydra's and Polynomicon's per-cast, Kinetic Cuirass's after-being-hit) or
# scaled off something the item does not carry (Qin's off the target's
# health, Gluttonous off lifesteal healing).
#
# THE EXCHANGE RATE NEEDS NO CLOCK. A basic attack scales 100% Attack Damage on
# 84 of 89 gods (`combat.DEFAULT_ATTACK_SCALING`, MEASURED off the scrape), so
# +N flat damage on every hit is +N Attack Damage on the same hit — the Attack
# Damage column is itself per hit, and that is the whole conversion. It is the
# same move `crit_damage_as_chance` makes: express the passive in a currency
# the regression already prices, into a column with many carriers (11, range
# 10–60 at 21.95 g/pt), never as a single-class column of its own.
#
# WHAT IS DELIBERATELY NOT PRICED, and each is a floor rather than a guess:
#   * Bragi's per-Level term (+3/level, +57 at level 20). The scorer states no
#     level — the same rule `all_stats_multiplier` applies to Genie's Lamp —
#     so the flat +10 is priced and the ramp is not. Priced at 20 the item
#     would land at +70, above the column's fitted maximum of 60 (the range
#     guard, PASSIVES.md §1).
#   * Golden Blade's "+20% of your Item Protections", a reference-build term
#     of exactly the shape §4.21 just measured and could not attribute.
#   * Tyrfing's ramp ("On God hit: +15 for 4s, stacks"), which is class C2.
#   * Damage TYPE. Bragi's bonus is magical on a physical attacker and is
#     read as the same currency. Against the roster's base protections at 20
#     (median physical 76, magical 56) a magical point is worth ~13% MORE than
#     a physical one, so 1:1 understates it; a stated mix would be §4.17's
#     constant, so the symmetric reference `build_quality` already declares
#     is used instead.
#   * Golden Blade's 2.5m area — single target is the floor.
#
# PREDICTIONS WRITTEN BEFORE THE SWEEP, at the shipped fit (Attack Damage
# 21.95 g/pt), and the refit will move them by some tens of gold as §4.21's
# did: Tyrfing +164 -> ~-165, Golden Blade +58 -> ~-162, Bragi's Harp +275 ->
# ~+55. Unlike §4.21's four relics, two of the three already carry Attack
# Damage, so the grant lands in a column they are already in rather than
# opening twenty. THE FALSIFIER: the three hold 13 + 2 + 1 = 16 of the 543
# Conquest community slots (Tyrfing, Golden Blade, Bragi's), so coverage can
# move only through a core one of them enters or leaves; a god whose coverage
# moves with none of the three entering or leaving its core is not this
# mechanism, and is reported, not explained. Numbers under `price_on_hit` in
# _weights.yaml.
_ON_HIT_FLAT = re.compile(
    r"\bAttacks?\s+(?:deal|Hit:?)\s*\+\s*(\d+(?:\.\d+)?)\s*"
    r"(?:\(\s*\+\s*[\d.]+\s*per\s+Level\s*\)\s*)?bonus\s+(?:Physical|Magical)\s+Damage",
    re.I)
#: Golden Blade's grammar: the number is in the next clause.
_ON_HIT_FLAT_NEXT = re.compile(
    r"\bAttacks\s+deal\s+bonus\s+(?:Physical|Magical)\s+Damage\.\s*Damage\s*=\s*\+\s*(\d+(?:\.\d+)?)",
    re.I)


def on_hit_flat_damage(item):
    """Flat bonus damage on every basic-attack hit, unconditional, or 0.0.

    Read clause by clause so Tyrfing's later "On God hit" ramp and Golden
    Blade's area do not make the standing grant conditional; a clause that is
    itself conditional ("Ability Used: Your next Attack deals ...") is refused
    by `is_conditional` and never reaches the pattern. A per-Level term is
    ignored — the flat part is the floor."""
    text = (item.get("passive") or "").strip()
    if not text:
        return 0.0
    m = _ON_HIT_FLAT_NEXT.search(text)
    if m and not is_conditional(text[:m.start()]):
        return float(m.group(1))
    for clause in _SENTENCE_BREAK.split(text):
        m = _ON_HIT_FLAT.search(clause)
        if not m:
            continue
        # The cue itself reads "Attack Hit:", and `CONDITIONAL_MARKERS` lists
        # `Hit` because "Hit enemy Gods: +8 Attack Damage for 10s" is a
        # trigger with a duration. An on-EVERY-hit grant is the attack channel's
        # own unit, not a trigger, so the cue is removed before the clause is
        # judged; anything conditional left over still refuses it.
        rest = clause[:m.start()] + clause[m.end():]
        if is_conditional(rest):
            continue
        return float(m.group(1))
    return 0.0


def on_hit_grants(item):
    """`{"Attack Damage": N}` for a flat on-hit passive, or {}."""
    amount = on_hit_flat_damage(item)
    return {"Attack Damage": amount} if amount > 0 else {}
