"""Empirical gold-efficiency scoring for SMITE 2 items.

Derives the marginal gold value the game assigns each stat by non-negative
least-squares regression of item cost onto item stats across the whole item
set, then scores each item by the residual between its actual cost and the
cost its raw stats predict. A negative residual (cheaper than predicted) is an
undervalued stat-stick; a large positive residual means you're paying a premium
for a passive — whether that premium is worth it is decided by the effect-tag
layer, not here. See the design spec for the full rationale.
"""


def parse_stat_value(raw):
    """Coerce a raw stats-dict value ('45', '20%', ' 10 ') to float, or None
    if absent/non-numeric. Stat values arrive as strings from YAML, some with
    a trailing % (Critical Chance, Cooldown Rate)."""
    if raw is None:
        return None
    try:
        return float(str(raw).strip().rstrip("%").strip())
    except ValueError:
        return None


import numpy as np
from scipy.optimize import nnls

# The regression's constant term — the gold every item is charged before a
# single stat is counted, ~1111 on the current pool.
#
# IT IS NOT WHY EFFICIENCY PREFERS MULTI-STAT ITEMS, and that is worth having
# written down because it is the obvious suspect and it is wrong. The symptom:
# across the 89 Conquest cores, items carrying 4 stats take 50.4% of the core
# slots off 19.5% of the buildable pool, a 2.58x lift, while 1-stat items take
# none at all. The accusation was that a FIXED charge against a roughly fixed
# tier-3 price (mean cost 2534-2620 whatever the stat count) leaves items with
# more stat columns accruing more value against the same constant.
#
# Measured 2026-08-21, three ways, and all three say the gradient is a real
# property of SMITE 2's pricing rather than an artifact of this fit:
#
# 1. IT IS MASS, NOT COLUMNS. Tier-3 residual regressed on the stat magnitude
#    an item carries — in units of `scoring.stat_reference`, so Health and
#    Strength are commensurable — gives R2 0.371. Adding the COLUMN COUNT as a
#    second regressor raises it to 0.390. Count is a proxy for mass and
#    contributes almost nothing of its own.
#
# 2. DELETING THE INTERCEPT MAKES IT WORSE. Mean tier-3 residual by stat count:
#
#                       1 stat    2      3      4     spread
#        with intercept   +702   +249   +136    -70     772g
#        no intercept    +1131   +365   +126   -267    1398g
#
#    The constant is DAMPING the gradient, not producing it. Refitting without
#    it nearly doubles the spread the accusation was made about.
#
# 3. THE FIT-FREE VERSION IS THE STEEPEST OF ALL. Typical rolls of a stat per
#    1000 gold — pool-median magnitudes, no regression anywhere in it — over
#    tier-3 items: 0.549 / 0.930 / 1.166 / 1.554 by stat count. A 4-stat item
#    carries 67% more raw stat magnitude per gold than a 2-stat one; this fit
#    credits it 24% more. The model is CONSERVATIVE against the raw stat line.
#
# What the multi-stat items give up is passive. Median passive text runs 259 /
# 154 / 157 / 105 characters over the same four bands, and priced at the rates
# of the 42 components that carry no passive at all, tier-3 items cash out at
# 52% / 101% / 103% / 113% of their own cost. The game sells stat mass and
# passive strength against each other, and this model prices passives at zero
# (`PRICE_PASSIVES`, STATE.md 4.5), so it reads one side of that trade.
#
# THE COMMUNITY MAKES THE SAME TRADE. Against the same buildable pool the
# recommender picks from, Obsidian+ Conquest builds lift 4-stat items 2.18x;
# our cores lift them 2.58x. The over-preference is +7.7pp of core share,
# bootstrap 95% CI [+2.9pp, +12.4pp] — real, and about a fifth of what the
# 2.58x reads as against the pool alone. STATE.md 4.11 has the full table and
# the part of this the model does get wrong, which is at the other end.
INTERCEPT_KEY = "_intercept"


def stat_key(name, raw):
    """The regression's column name for a stat, with its unit as part of its
    identity.

    A percentage and a flat amount of the "same" stat are different goods, and
    `parse_stat_value` strips the sign that told them apart. Penetration is the
    case that bites: nine items carry a flat amount and ten carry a percentage,
    so a single column priced `Penetration: 10` and `Penetration: 10%` at the
    same gold. Against a 300-protection target those are worth 10 and 30 — not
    a rounding difference, and the error runs through every build that values
    penetration.

    Keying on the unit rather than special-casing this one stat means the next
    stat to grow a percentage variant is separated on arrival instead of
    silently averaging with its flat namesake for a patch or two."""
    return f"{name} %" if str(raw).strip().endswith("%") else name


def stat_base(key):
    """The plain stat name behind a regression column — `Attack Speed %` ->
    `Attack Speed`.

    The fit map is keyed on the stat's plain name, because `god_fit_score`
    reads the item's own `stats` dict; the regression is keyed on the name
    WITH its unit, because `stat_key` made the unit part of the column's
    identity. Anything comparing the two has to come back through here or it
    will read every percentage stat as absent from every role map."""
    return key[:-2] if key.endswith(" %") else key


# Whether unconditional passive grants count as stats. OFF: it prices items
# more sensibly and ranks them worse — see `passives.py` for the numbers and
# the explanation. Flipped by `price_passives` in _weights.yaml.
PRICE_PASSIVES = False

# Whether a PERSISTENT stacker counts at its full-stack value. Strictly
# narrower than PRICE_PASSIVES and independent of it: that flag prices every
# unconditional grant, this one prices only stacks that reach a cap and keep
# it (`passives.persistent_stack_grants`). Four items qualify — Book of Thoth,
# Devourer's Gauntlet, Gauntlet of Thebes and Transcendence — and every
# transient stacker is refused. Flipped by `price_stacks` in _weights.yaml.
PRICE_STACKS = False

# How much of a stacker's cap a real match reaches. 1.0 prices the tooltip;
# lower prices what you play with. Set by `stack_fraction` in _weights.yaml.
STACK_FRACTION = 1.0

# Whether a crit-damage multiplier counts, converted into the equivalent
# Critical Chance the model already prices. One item qualifies — Deathbringer,
# whose +35% this project has measured against the game to the digit and never
# consulted. See `passives.crit_damage_as_chance`. Flipped by
# `price_crit_multipliers` in _weights.yaml.
PRICE_CRIT_MULTIPLIERS = False

# Whether an item that converts one stat into another is priced for it, against
# a REFERENCE build total rather than the core being assembled. Four items
# qualify; three of them reach zero model cores today. See
# `passives.stat_conversions` and docs/plans/2026-08-13-mana-conversion-fit.md.
# Flipped by `price_conversions` in _weights.yaml.
PRICE_CONVERSIONS = False

# `{stat: typical total across a finished build}` the conversions are priced
# against. Measured, not guessed — `passives.measure_conversion_reference`
# re-derives it, and _weights.yaml carries the numbers with that derivation.
CONVERSION_REFERENCE = {}

# Whether an Adaptive Stat grant counts, credited to ONE of the two stats the
# clause offers. Strictly narrower than PRICE_PASSIVES and mutually exclusive
# with it: that flag prices the same grant as its own `Adaptive Power` column
# among 48 other passive grants, this one prices only the adaptive slice and
# prices it into a stat the whole pool already values. Eight buildable items
# qualify. See `passives.adaptive_grants` for which branch and why. Flipped by
# `price_adaptive` in _weights.yaml.
PRICE_ADAPTIVE = False

# Which side of `+X Strength or +Y Intelligence` is priced. `strength` or
# `intelligence`; set by `adaptive_branch` in _weights.yaml.
ADAPTIVE_BRANCH = "strength"


#: Every module global `apply_pricing_flags` owns. The list the save/restore
#: pair walks, so a new switch is covered by adding it in one place.
PRICING_FLAGS = ("PRICE_PASSIVES", "PRICE_STACKS", "STACK_FRACTION",
                 "PRICE_CRIT_MULTIPLIERS", "PRICE_CONVERSIONS",
                 "CONVERSION_REFERENCE", "PRICE_ADAPTIVE", "ADAPTIVE_BRANCH")


def apply_pricing_flags(weights):
    """Set the module's pricing switches from a weights dict.

    These are module globals rather than parameters because `item_stat_values`
    is called from deep inside the fit with no weights in scope. That is fine
    until only ONE caller sets them: `recommend.main` did, and
    `calibrate`/`validate` did not, so every gate measured with every flag OFF
    no matter what _weights.yaml said. A config that the thing measuring it
    cannot see is worse than no config — it reports the shipped number for an
    unshipped model.

    Returns the previous values, as `{global name: value}`, for
    `restore_pricing_flags`. A DICT rather than a tuple because the restore
    contract has to cover every switch: adding a global to this function and
    forgetting it in the return value leaves a sweep silently unable to put the
    module back, and nothing would fail loudly.
    """
    global PRICE_PASSIVES, PRICE_STACKS, PRICE_CRIT_MULTIPLIERS
    global PRICE_CONVERSIONS, CONVERSION_REFERENCE, STACK_FRACTION
    global PRICE_ADAPTIVE, ADAPTIVE_BRANCH
    before = {k: globals()[k] for k in PRICING_FLAGS}
    before["CONVERSION_REFERENCE"] = dict(CONVERSION_REFERENCE)
    w = weights or {}
    PRICE_PASSIVES = bool(w.get("price_passives"))
    PRICE_STACKS = bool(w.get("price_stacks"))
    STACK_FRACTION = float(w.get("stack_fraction", 1.0))
    PRICE_CRIT_MULTIPLIERS = bool(w.get("price_crit_multipliers"))
    PRICE_CONVERSIONS = bool(w.get("price_conversions"))
    CONVERSION_REFERENCE = dict(w.get("conversion_reference") or {})
    PRICE_ADAPTIVE = bool(w.get("price_adaptive"))
    ADAPTIVE_BRANCH = str(w.get("adaptive_branch") or "strength")
    return before


def restore_pricing_flags(before):
    """Put back what `apply_pricing_flags` returned."""
    globals().update(before)


def item_stat_values(item):
    """`{column name: float}` for one item — the canonical read of its stats.

    The single place raw stat dicts are turned into regression columns, so the
    matrix, the prediction and the shipped gold table cannot disagree about
    what a column means."""
    out = {}
    for name, raw in (item.get("stats") or {}).items():
        val = parse_stat_value(raw)
        if val is not None:
            out[stat_key(name, raw)] = val
    if PRICE_PASSIVES:
        from smite import passives
        out = passives.effective_stats(item, out)
    if PRICE_STACKS:
        from smite import passives
        for key, amount in passives.persistent_stack_grants(item, STACK_FRACTION).items():
            out[key] = out.get(key, 0.0) + amount
    if PRICE_CRIT_MULTIPLIERS:
        from smite import passives
        for key, amount in passives.crit_damage_as_chance(item).items():
            out[key] = out.get(key, 0.0) + amount
    if PRICE_CONVERSIONS and CONVERSION_REFERENCE:
        from smite import passives
        for key, amount in passives.conversion_grants(item, CONVERSION_REFERENCE).items():
            out[key] = out.get(key, 0.0) + amount
    if PRICE_ADAPTIVE and not PRICE_PASSIVES:
        # `and not PRICE_PASSIVES` because `effective_stats` above prices the
        # SAME clause, as its own `Adaptive Power` column. Running both counts
        # the grant twice, at two different prices, on 29 items. The broad flag
        # wins the tie: it is the one already in the register with numbers, and
        # silently overriding it would make its measurement unreproducible.
        from smite import passives
        for key, amount in passives.adaptive_grants(item, ADAPTIVE_BRANCH).items():
            out[key] = out.get(key, 0.0) + amount
    return out


# Fewest items that must carry a stat before it earns a regression column.
#
# A column carried by ONE item is exactly determined: NNLS can always choose
# the coefficient that drives that item's residual to zero, so the column
# explains nothing and the residual it produces is an artifact of the fit
# rather than a measurement. It is the same defect the statless-item rule in
# `scoring.is_buildable` closed — an arithmetic that cannot mean anything —
# and it arrived the same way, through new data: Agility Greaves (2500 gold,
# `Movement Speed: 5`) was the only carrier of Movement Speed, and NNLS priced
# it at 299 gold per point, ~13x Strength, purely to land on 2500 exactly.
#
# The distortion is not confined to that item. Every coefficient is fit
# jointly, so an unidentified column bends the intercept and its neighbours
# too. Dropping it: coverage 52.6% -> 53.4%, win-weighted 54.8% -> 55.5%.
#
# Set at 2, not higher, deliberately. A dropped column also means every item
# carrying that stat loses credit for it and reads as overpriced, so this
# should only reach columns that are degenerate rather than merely thin.
# Raising it to 4 (which additionally drops Pathfinding, 2 carriers) measured
# identically, so there is no evidence for going further.
MIN_STAT_CARRIERS = 2


def collect_stat_names(items):
    """Every distinct stat column that parses to a number on at least
    MIN_STAT_CARRIERS items, sorted for deterministic column order."""
    counts = {}
    for item in items:
        for key in item_stat_values(item):
            counts[key] = counts.get(key, 0) + 1
    return sorted(k for k, n in counts.items() if n >= MIN_STAT_CARRIERS)


def _stat_matrix(items, stat_names):
    """Rows = items, columns = stat_names then a trailing all-ones intercept
    column. Absent/non-numeric stats are 0."""
    rows, costs = [], []
    for item in items:
        values = item_stat_values(item)
        row = [values.get(s, 0.0) for s in stat_names]
        row.append(1.0)  # intercept
        rows.append(row)
        costs.append(float(item["cost"]))
    return np.array(rows, dtype=float), np.array(costs, dtype=float)


def numeric_cost_items(items):
    """Items whose cost is a usable number — the only ones that can train the
    regression. Component items sometimes have cost: null on the wiki."""
    return [it for it in items if isinstance(it.get("cost"), (int, float))]


def efficiency_pool(items):
    """The items eligible for gold-value modeling: numeric-cost, non-starter.
    Tier-1 starters are passive-priced — their gold buys an ability/adaptive
    passive, not their token stats — so regressing cost onto their tiny stats
    poisons the gold-per-stat fit and skews every item's residual. They keep
    their cost in the data (display/audit) but sit out both the fit and the
    scored set.

    Components stay IN, and that is deliberate. It looks wrong — a finished
    item's cost includes its components', so one set of coefficients is being
    asked to describe two pricing regimes — and it was changed to
    finished-items-only on exactly that reasoning, supported by five-fold
    cross-validation on held-out finished items:

        no components   197g mean held-out cost error
        16 components   357g
        all 64          385g

    The validation gate then said the opposite, and the validation gate wins:

                        coverage   win-weighted
        with components   48.4%       50.6%
        finished only     45.1%       47.7%

    The cross-validation measured the wrong objective. Nothing downstream needs
    to predict an item's price; it needs the *residual* to rank items in a way
    that tracks whether they are actually good. A model that predicts cost
    perfectly has a residual of zero everywhere and says nothing. Components
    are what let individual stat prices be identified apart from the bundles
    they always appear in, and that identification is what makes the residuals
    rank well — which is why scraping the missing 41 of them moved the gate
    from 47%/49% to 48.4%/50.6% on its own.

    STATLESS ITEMS ARE EXCLUDED, and that is a different rule from the one
    above rather than an exception to it. A row with no stats is all zeros
    against the intercept, so it carries no information about what any stat
    costs — it only drags the intercept toward its own price. Blink Rune (0
    gold) and Blinking Abyss (2600 gold) were doing exactly that, and the
    intercept moved 1099 -> 1042 once they left.

    The visible half of the same bug: a statless item's residual is its cost
    minus the intercept, which is not a measurement of anything, and the Items
    page was sorting on it. Four of the top six "best value" items in the game
    were artifacts, led by Blink Rune at "worth 1099g, -1,099g" for an item
    with no stats at all. Leaving the pool means they ship unscored, which is
    the true statement.

    God-specific items STAY. Their stats and price are real evidence about
    what stats cost even though only one god can buy them, and removing them
    costs a lot: the leakage-free measure falls 4.89x -> 4.20x. What they are
    not is *comparable* on a global value ranking, which is a display concern
    and is handled in `build_index._attach_efficiency`.

    THEY ARE ALSO A LOT OF LEVERAGE FOR FOUR ITEMS, which is worth knowing
    before adding a fifth. Recovering Briskberry Acorn's stats (2026-08-09 —
    they were stranded in its passive text, see
    `wiki_parser._stats_from_prose`) put ONE more god-locked item in this pool
    and repriced the whole game: Pathfinding -59.9%, Health Regen -27.0%,
    Mana Regen -20.0%, Strength -7.8%, Max Health -6.1%, intercept +4.2%. A
    god-specific item is balanced around being unavailable to 86 gods, so it
    is deliberately overloaded for its price, and the fit reads that as stats
    being cheap for everyone.

    Measured both ways, and the honest answer is that it does not resolve:

                                    eff 0.7 : fit 0.3    eff 0.45 : fit 0.55
        Briskberry statless (before)        30.0%                  32.1%
        in the pool (shipped)               33.1%                  30.5%
        out of the pool                     29.9%                  32.0%

    The sign FLIPS with the split and every interval overlaps every other
    ([28.3%, 38.1%] against [25.7%, 34.3%] on the first column). So this is
    not evidence for changing the rule, and the rule is unchanged — the 4.89x
    -> 4.20x measurement above was made on stronger ground than this one.
    Do not quote the 33.1% as an improvement; it is one arm of a sign-flipping
    comparison inside its own noise.

    If you are about to narrow this pool again: measure it, and measure it
    with `calibrate.random_core_baseline` rather than `mean_coverage` — see the
    leakage probe in calibrate.py.
    """
    return [it for it in numeric_cost_items(items)
            if it.get("tier") != 1 and (it.get("stats") or {})]


def fit_gold_values(items):
    """NNLS fit of cost onto stats. Returns (gold_values, stat_names) where
    gold_values maps each stat name (plus INTERCEPT_KEY) to its non-negative
    marginal gold value. Non-negative because a stat cannot rationally have a
    negative gold price; NNLS also tames collinear-stat coefficient blowups."""
    items = efficiency_pool(items)
    stat_names = collect_stat_names(items)
    A, b = _stat_matrix(items, stat_names)
    coef, _ = nnls(A, b)
    gold = {name: float(coef[i]) for i, name in enumerate(stat_names)}
    gold[INTERCEPT_KEY] = float(coef[-1])
    return gold, stat_names


def predicted_cost(item, gold_values):
    total = gold_values.get(INTERCEPT_KEY, 0.0)
    for key, val in item_stat_values(item).items():
        total += val * gold_values.get(key, 0.0)
    return total


def efficiency_scores(items):
    """Returns (scores, gold_values). scores maps item name → dict with:
      residual  actual_cost - predicted_cost (negative => undervalued)
      z         residual z-score across the set
      score     min-max normalized -residual in [0,1] (higher => better value)
      tier      'undervalued' | 'fair' | 'premium' by z threshold
    Only numeric-cost, non-starter items are scored (a residual needs a real
    cost; tier-1 starters are passive-priced and sit out the model). The
    continuous `score` is what the aggregator consumes; `tier` is the report
    label."""
    gold, _ = fit_gold_values(items)
    scored_items = efficiency_pool(items)
    residuals = {it["name"]: it["cost"] - predicted_cost(it, gold) for it in scored_items}
    # What each COLUMN of the item contributed to that prediction, carried on
    # the row so a caller holding one score can charge part of the stat line
    # back without refitting or being handed the gold table separately.
    # `offmap_adjusted_score` is what needs it, and the reason it lives here is
    # that every consumer of this module already calls `efficiency_scores` and
    # not one of them threads `gold` through to `scoring` — a flag that needed
    # threading would have been a silent no-op in `calibrate`, `validate` and
    # `build_index`, which is register §4.10's failure mode exactly.
    stat_gold = {it["name"]: {k: v * gold.get(k, 0.0)
                              for k, v in item_stat_values(it).items()}
                 for it in scored_items}
    vals = np.array(list(residuals.values()), dtype=float)
    mean = float(vals.mean())
    std = float(vals.std()) or 1.0
    lo, hi = float(vals.min()), float(vals.max())
    span = (hi - lo) or 1.0

    scores = {}
    for name, resid in residuals.items():
        z = (resid - mean) / std
        score = (hi - resid) / span  # cheapest-relative → 1.0, most-premium → 0.0
        tier = "undervalued" if z <= -0.5 else "premium" if z >= 0.5 else "fair"
        # `span` is the same for every item and is carried on each so a caller
        # holding one score can convert a GOLD delta into a SCORE delta without
        # refitting: score = (hi - residual) / span, so d(score) = d(gold)/span.
        # `assemble.conversion_score_bonus` is what needs it.
        scores[name] = {"residual": resid, "z": z, "score": score, "tier": tier,
                        "span": span, "stat_gold": stat_gold[name]}
    return scores, gold


# ── Charging an item for stat mass the god cannot use (`offmap_efficiency`) ──
#
# THE HOLE. `efficiency` is god-agnostic: an item's residual is its price
# against the gold value of EVERY stat it carries, whoever is buying. The
# god-specific half is `scoring.god_fit_score`, and that normalises over the
# role map ALONE — numerator and denominator both range over the map, so a
# stat the map does not name appears in neither. It is neither credited nor
# charged. With `magnitude_fit` off the stat term reads only WHICH map stats
# an item carries, so two items with the same on-map stats score the identical
# fit however much else rides along, and the extra mass shows up only in
# `efficiency`, as value.
#
# VERIFIED, not asserted (2026-08-22). Grouping all 9,541 (god, item) pairs by
# god and by identical on-map stat SET, the fit stat term is constant inside
# the group in **1174 of 1174 groups** — fit varies within a class only
# through the effect-tag bonus, which is not a stat charge. Inside those
# classes, mean r(off-map stat mass share, efficiency score) = **+0.441**,
# positive in **856 of 1110** groups and positive in all five roles.
#
# THE ITEM IT WAS FOUND ON. Berserker's Shield (2400g: Physical Protection 40
# · Attack Speed 20% · Max Health 200 · Health Regen 4) is in 17 of 18 model
# Carry cores and 0 of 18 community ones. A Carry's map names exactly one of
# its four stats. Repriced against that one stat at the same 2400g:
#
#     residual  -425g -> +849g      efficiency 0.681 -> 0.210
#     `quality` rank 1-9 of 99-138  ->  84-126 of 99-138
#
# and it leaves all 18 Carry cores. The off-map stats are the whole of what
# buys the slot.
#
# WHY IT IS NOT A BLANKET CHARGE, AND WHY THIS SHIPS OFF UNTIL SWEPT. Off-map
# share correlates NEGATIVELY with core membership roster-wide (-0.175), and
# our cores' mean off-map share (0.235) is within noise of the community's own
# (0.242). The gap lives on ONE role:
#
#     role      pool   our core   community        role      names a defensive stat
#     Carry    0.579      0.254       0.127        Carry      0 of 18 gods
#     Jungle   0.666      0.296       0.315        Jungle     1 of 17
#     Mid      0.656      0.183       0.296        Mid        3 of 22
#     Solo     0.276      0.215       0.221        Solo      18 of 18
#     Support  0.310      0.242       0.252        Support   14 of 14
#
# The right-hand column is the reason: Carry is the only role whose fit map
# names no protection and no health at all, and defensive mass is the cheapest
# mass in the pool. 55% of the off-map mass in our Carry cores is Physical
# Protection, Max Health and Health Regen; in Support cores it is 0%, because
# there those stats are ON the map. So the mechanism is general and the HARM
# is Carry-shaped, which is why the strength is a swept knob rather than a
# structural change to the residual.
#
# IT IS NOT REGISTER §4.11. Off-map share and stat COUNT are near-orthogonal
# (r = +0.129) and neither absorbs the other — partial r(share, core | count)
# -0.210 against a simple -0.175; partial r(count, core | share) +0.248
# against a simple +0.219. The signs are OPPOSITE: count is positively
# associated with core membership (§4.11's effect), share negatively.
#
# IT IS NOT REGISTER §4.3 EITHER. Magnitude-aware fit does not reorder the
# class that decides the Carry core: Berserker's Shield's 20% Attack Speed IS
# the reference magnitude, so its fit is unchanged and it stays first.
#
# THE HONEST CASE AGAINST IT. In that same class the two items the community
# actually buys — Odysseus' Bow (10 of 18) and The Executioner (13 of 18) —
# are the two carrying ZERO off-map mass, and they read +316g and +999g
# OVERPRICED. That premium is passive value `PRICE_PASSIVES` sets to zero
# (STATE.md §4.5). There is an unpriced quantity on both sides of the
# comparison this flag adjusts: our item's off-map mass is free credit,
# theirs is a free debit. Charging one without pricing the other reaches the
# right answer for half the right reason, and that is a real limitation on
# whatever this measures.


# ── The universal ride-along (`offmap_exempt`) ───────────────────────────────
#
# WHAT IT IS. A stat named here is off EVERY role map and charged to nobody by
# `offmap_efficiency`. It is deliberately NOT a fit weight, and the difference
# is the whole design: a weight says "this role wants this stat, this much",
# which needs a magnitude; an exemption says "this stat is a roster constant,
# so its absence from the maps is not evidence the gods do not want it".
#
# WHY MANA COULD NOT BE A WEIGHT (measured 2026-08-22, at control fingerprint
# `c73b6ea6bdde` — baseline 5.6%, probe 39.1%, best 40.0%). Zero of the 21
# `role_stats` entries names Max Mana or Mana Regen, and the obvious repair is
# to name it. Every route to a NUMBER is closed:
#
#   * THE KIT — the `attack_damage_fit` shape, and the one that should have
#     worked. Ability mana costs and base stats are scraped, game-side and
#     community-free. Over the 78 gods with a full kit and a mana pool:
#
#         role     n  pool@20   MP5  rotation  rot/pool  drain/s  sustain_s
#         Carry   15     1094  3.42       285     0.261    18.49        61s
#         Jungle  15     1094  3.93       320     0.293    18.19        63s
#         Mid     21     1114  3.84       315     0.283    22.73        54s
#         Solo    15     1094  3.73       295     0.270    18.20        68s
#         Support 12     1128  3.73       320     0.284    19.18        62s
#
#     THERE IS NO PER-ROLE SIGNAL IN IT. `rot/pool` spans 0.261-0.293 across
#     five roles on a quantity whose roster range is 0.181-0.338 — a 3pp band
#     inside a 16pp one — and base mana is near-constant (1006-1240, stdev 53).
#     The between-role `sustain_s` range (54-68s) is NARROWER than Solo's own
#     within-role IQR (53-70s). The kit says every role has the same mana
#     economy, which argues for a roster constant and against a role column.
#     The one measure that does single Mid out is `drain/s`, and it assumes
#     100% ability uptime — the clock STATE.md §4.12 turned on refusing. On the
#     clock-free measure Mid is third of five, behind Jungle and Support.
#
#   * THE DAMAGE MODEL cannot price it. Exactly 0 of 89 gods have an ability
#     that scales on Max Mana (the only regex hit in the roster is Apollo's
#     ult COST). `combat.py` contains the string "mana" zero times, so
#     `build_quality` — the non-circular instrument — is blind to mana and
#     cannot adjudicate this either way.
#
#   * THE ONE GAME-STATED EXCHANGE RATE is already refuted. Transcendence
#     (3% -> Strength) and Book of Thoth (5% -> Intelligence) are the only
#     things that turn mana into a stat a map names; that is `conversion_fit`,
#     swept 0.05-1.0, STATE.md §4.9, the two splits moving in OPPOSITE
#     directions.
#
#   * AND THE INTERVENTION HAS ALREADY BEEN MEASURED ONCE, informally. The
#     `mana-stack` flavor comment in _weights.yaml records that Max Mana on a
#     fit overlay at 1.2 selected Genji's Guard and Breastplate of Valor —
#     tank items — because mana in this pool lives on tank items. "Mana is the
#     fuel, not the goal."
#
#   To put mana on the fit map needs an exchange rate between a point of mana
#   and a point of Strength. `attack_damage_fit` had one: both are damage and
#   `stat_weights` measures them in the same unit. Mana has none that is not
#   leakage or already refuted, so any weight written here would be invented.
#
# THE SHARE THAT MOTIVATED THIS IS THE WRONG UNIT, AND BY A FACTOR OF ~5.
# `god_fit_score` runs with `magnitude_fit` off, so its stat term reads
# PRESENCE — `share` is 1.0 whatever the value — and `offmap_efficiency`
# charges GOLD, off `stat_gold`. Neither reads mass. Same community cores,
# same off-map definition, three units:
#
#     role     off-map MASS that is mana   as GOLD   core SLOTS carrying any
#     Carry                        67.7%     15.4%     15 of 108 = 13.9%
#     Jungle                       74.2%     29.7%     42 of 102 = 41.2%
#     Mid                          94.1%     65.3%     48 of 132 = 36.4%
#     Solo                         90.2%     29.6%     24 of 108 = 22.2%
#     Support                      84.9%     24.2%     24 of  84 = 28.6%
#
# The arithmetic is visible in the pool: the median non-zero roll is 250 Max
# Mana against 35 Strength, and the regression prices Max Mana at 1.26 g/pt
# against Strength's 21.81. A median mana roll is 316 gold. Mana is voluminous
# and cheap, so a mass share flatters it and a gold or presence share does not.
#
# WHAT AN EXEMPTION IS WORTH ANYWAY, given all that. The hole §4.15 names is
# real and it is one-sided: `efficiency` prices mana as value and
# `god_fit_score` cannot see it, so charging off-map mass charges an item for
# a stat every build in the game carries. An exemption removes that one-sided
# charge without asserting a magnitude — it needs only the binary the kit
# measurement supports, that mana is a roster constant. The sweep under
# `offmap_exempt` in _weights.yaml is what it is worth.
#
# IT IS INERT WHILE `offmap_efficiency` IS 0.0 — an exemption only subtracts
# from a charge, and with no charge there is nothing to subtract. That is
# pinned by a test rather than assumed; register §4.10 is what happens when a
# setting is applied where nothing reads it.

# ── WHAT EARNS A PLACE ON THIS LIST (the rule, derived 2026-08-22) ──────────
#
# Mana was argued case by case. Adding a second stat forces the general form,
# and it is two mechanical tests, neither of which is a judgement about SMITE:
#
#   (i)  NO `role_stats` ENTRY NAMES IT AT ALL. Not "the role that wants it
#        has no entry" — no entry anywhere. A stat named for SOME role and not
#        another has a contrast, and the silence on the second role is then a
#        POSITIVE statement by the same table that spoke about the first. A
#        stat named nowhere has no contrast to be read, so its absence carries
#        no information and charging against it asserts something the table
#        never said.
#
#   (ii) NO INSTRUMENT IN THIS REPO CAN PRICE IT. If `combat.py` can see the
#        stat, then charging it is a hypothesis `build_quality` can check, and
#        the honest move is to check it rather than to exempt it.
#
# Run over every stat the buildable pool carries, the two tests select exactly
# three columns, which is the reason to trust the rule — it is not a filter
# that lets everything through:
#
#     stat                  carriers   g/pt   named by a role map   priced by combat.py
#     Max Health                  52   1.37   YES (6 of 21)         effective_health
#     Physical Protection         39  21.93   YES (6 of 21)         mitigation
#     Magical Protection          37  19.40   YES (5 of 21)         mitigation
#     Intelligence/Strength/...    -      -   YES                   damage
#     Plating / Dampening         13  ~38     no                    plating_multiplier
#     Tenacity                     5  23.70   no                    TENACITY_CAP
#     Echo                         5  21.59   no                    echo_multiplier
#     Attack Damage                9  21.95   no                    basic attack
#     Max Mana                    23   1.26   NO                    NOTHING  <- exempt
#     Mana Regen                  20   5.37   NO                    NOTHING  <- exempt
#     Health Regen                12  76.40   NO                    NOTHING  <- exempt
#
# ATTACK DAMAGE IS THE INSTRUCTIVE ROW. It fails (ii) — the basic attack is
# modelled — and it is the one stat named by no role map that got a WEIGHT
# instead, `attack_damage_fit`, because `damage_value.stat_weights` supplied
# an exchange rate. So the rule has three outcomes, not two: price it if an
# instrument can, weight it if a leakage-free exchange rate exists, exempt it
# only when neither is available. An exemption is the LAST resort and it is
# the weakest of the three, because it says only "do not charge".
#
# THE §4.15 DEFECT STATS FAIL BOTH TESTS AND MUST NOT BE ADDED. Max Health and
# Physical Protection are named by 6 of the 21 entries and by 36 of 89 merged
# god maps, so the Carry map's silence about them is that table declining to
# say for Carry what it says for Solo, Support, Tank, Guardian, Warrior and
# Brawler. And `combat.effective_health` prices both exactly. Charging a Carry
# for them is a claim the non-circular instrument can adjudicate, and does.
#
#
# ── HEALTH REGEN (added 2026-08-22, at control fingerprint `c68c33d49845` — ──
#    baseline 5.6%, probe 39.1%, best 40.0%)
#
# The stat §4.16 left named as the next one to examine: 33% of the off-map
# gold this charge removes from a Solo core and 39% from a Support one, and
# the whole of Solo's -9.4pp, which sparing mana did not move by a digit.
#
# TEST (i) PASSES, and this is the strongest single fact here. Of the 21
# `role_stats` entries, Health Regen is named by ZERO — the same standing as
# Max Mana and Mana Regen, and unlike every defensive stat it gets grouped
# with in §4.15's composition table. Over the 89 merged fit maps (role map +
# kit overlay + `attack_damage_fit`): Health Regen 0 of 89, against Max Health
# 36, Physical Protection 36, Magical Protection 36.
#
# TEST (ii) PASSES. `combat.py` contains the string "regen" ZERO times. Health
# Regen is a RATE — points per 5 seconds — and this repo has no clock; register
# §4.12 refused to invent one, and even the clock it refused was a COMBAT
# clock, while regeneration is mostly what happens between fights. So there is
# no path by which `build_quality`, the only non-circular instrument, could
# ever adjudicate a Health Regen charge either way.
#
# THE GAME HANDS IT OUT AS A CONSTANT. Scraped `base_stats`, community-free,
# at level 20 (88 gods; Xing Tian's page carries no base stats at all):
#
#     role     n   HP@20   HP5@20   HP5 as % of pool   within-role IQR
#     Carry   20    2272     5.57              0.246     0.234-0.249
#     Jungle  21    2438     5.67              0.233     0.227-0.242
#     Mid     20    2247     5.54              0.247     0.249-0.249
#     Solo    14    2472     5.79              0.234     0.228-0.238
#     Support 13    2611     5.91              0.226     0.222-0.232
#     ROSTER  88    2388     5.67              0.238     range 0.208-0.277
#
# HP5 at 20 spans 5.50-6.22 over the whole roster — a 13% band — with 44 of
# the 88 gods on exactly 5.50 and the per-level term taking three distinct
# values in total (0.20 on 67 gods, 0.22 on 16, 0.23 on 5). As a share of the
# health pool the five role means span 0.020pp inside a roster range of
# 0.069pp. There is no per-role number to read off this, which is the same
# conclusion the mana kit table reached and the same reason: a roster constant.
#
# AND THE TILT THAT DOES EXIST POINTS THE WRONG WAY for the story anyone would
# tell from the game — Mid (0.247) and Carry (0.246) regenerate the MOST
# relative to their pool and Support (0.226) the least, so even taken at face
# value this table would not hand Solo or Support a Health Regen column.
#
# WHERE THIS CASE IS WEAKER THAN MANA'S, said plainly. Mana's argument had a
# DEMAND side: ability mana costs are scraped, so `rot/pool` measured what
# each role actually spends. Health regen's demand is incoming damage, which
# is not a property of the kit and is not scraped anywhere — it is positional,
# and reading it off a role would be exactly the invented constant §4.12 and
# §4.13 turned on refusing. So this case rests on test (i), test (ii) and a
# SUPPLY-side constant, with no demand measurement behind it. That is a
# genuinely thinner base than mana had, and it is why the rule above is
# written as two mechanical tests rather than as an argument about SMITE.
#
# WHAT IT COSTS THE §4.15 CORRECTION: 21% of one item's charge, and none of
# the answer. Berserker's Shield carries Health Regen 4 = 306 of the 2400g it
# spends, so against the one stat a Carry's map names its off-map gold goes
# 1457 -> 1151. It is still repriced out of the Carry core; see the sweep
# under `offmap_efficiency` in _weights.yaml. The 12 buildable carriers hold
# 3-6 points each, 9-20% of the item's price.


def offmap_gold(eff_row, role_map, exempt=()):
    """Gold this item spent on stats the god's fit map does not name.

    Read off `stat_gold`, so it is exactly the contribution those columns made
    to the item's own predicted cost — the same arithmetic, not a second one
    that could drift from it.

    `exempt` names stats that are off EVERY map and charged to nobody. See
    `OFFMAP_EXEMPT` below for what earns a place on that list and why it is an
    exemption rather than a fit weight.
    """
    exempt = frozenset(exempt or ())
    return sum(g for key, g in (eff_row.get("stat_gold") or {}).items()
               if not role_map.get(stat_base(key)) and stat_base(key) not in exempt)


def offmap_adjusted_score(eff_row, role_map, strength, exempt=()):
    """`eff_row`'s efficiency score with `strength` of its off-map gold charged
    back to it. 0.0 is the exact control and 1.0 prices the item as if it were
    sold carrying only the stats this god wants.

    The conversion is the one `efficiency_scores` documents on `span`:
    score = (hi - residual) / span, so charging `c` gold moves the score by
    exactly c / span and no refit is needed.

    An EMPTY role map is left alone rather than charged in full. A map can be
    empty legitimately — `archetype_bypass` fun flavors set one deliberately,
    and `_role_stat_map` returns one for unseen role vocabulary — and an empty
    map means "no information about what this god wants", never "this god
    wants nothing". Charging it would collapse every item at once, on the
    gods where the model already knows least."""
    score = eff_row.get("score", 0.5)
    if not strength or not role_map:
        return score
    return max(0.0, min(score - strength * offmap_gold(eff_row, role_map, exempt)
                        / (eff_row.get("span") or 1.0), 1.0))
