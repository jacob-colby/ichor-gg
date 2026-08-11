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
        for key, amount in passives.persistent_stack_grants(item).items():
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
        scores[name] = {"residual": resid, "z": z, "score": score, "tier": tier}
    return scores, gold
