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


def collect_stat_names(items):
    """Every distinct stat that parses to a number somewhere in the item set,
    sorted for deterministic column order."""
    names = set()
    for item in items:
        for stat, raw in (item.get("stats") or {}).items():
            if parse_stat_value(raw) is not None:
                names.add(stat)
    return sorted(names)


def _stat_matrix(items, stat_names):
    """Rows = items, columns = stat_names then a trailing all-ones intercept
    column. Absent/non-numeric stats are 0."""
    rows, costs = [], []
    for item in items:
        stats = item.get("stats") or {}
        row = [parse_stat_value(stats.get(s)) or 0.0 for s in stat_names]
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
    scored set."""
    return [it for it in numeric_cost_items(items) if it.get("tier") != 1]


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
    for stat, raw in (item.get("stats") or {}).items():
        val = parse_stat_value(raw)
        if val is not None:
            total += val * gold_values.get(stat, 0.0)
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
