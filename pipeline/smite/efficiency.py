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


def fit_gold_values(items):
    """NNLS fit of cost onto stats. Returns (gold_values, stat_names) where
    gold_values maps each stat name (plus INTERCEPT_KEY) to its non-negative
    marginal gold value. Non-negative because a stat cannot rationally have a
    negative gold price; NNLS also tames collinear-stat coefficient blowups."""
    items = numeric_cost_items(items)
    stat_names = collect_stat_names(items)
    A, b = _stat_matrix(items, stat_names)
    coef, _ = nnls(A, b)
    gold = {name: float(coef[i]) for i, name in enumerate(stat_names)}
    gold[INTERCEPT_KEY] = float(coef[-1])
    return gold, stat_names
