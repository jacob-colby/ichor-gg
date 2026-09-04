"""Why do four items that reach no core move forty cores?

A DIAGNOSTIC, not a model change. Nothing here is imported by the pipeline and
nothing here writes to `data/`. It exists to answer STATE.md §5's handoff from
§4.21: `price_stat_multipliers` prices five items, none of them enters a core,
and 40 of 90 Conquest model cores change anyway.

THE SEPARATION THIS MAKES. A pricing flag has exactly two inputs into
everything downstream of `efficiency.efficiency_scores`:

    (1) the fitted gold table  — intercept and per-stat prices, GLOBAL
    (2) `item_stat_values`     — the priced items' own stat lines, LOCAL

and every residual is `cost - intercept - sum(price_s * stat_s)`. For any item
the flag does not price, `stat_s` is unchanged, so its residual can only move
through (1). That makes the two separable by construction: run the flag's
fitted prices against the flag-off stat lines (REFIT), and the flag-on stat
lines against the flag-off prices (LOCAL).

Two more arms split what "the refit" actually does, because `efficiency_scores`
does not hand assembly a residual — it hands it a min-max normalised score,
`(hi - residual) / span`, whose `hi` and `span` are taken over the whole pool.
So one item's residual moving rescales every other item's score without any
price moving at all. NORM isolates that.

    OFF     flag off, prices fit off          the control
    ON      flag on,  prices fit on           the treatment
    REFIT   flag off, prices fit ON           (1) alone
    LOCAL   flag on,  prices fit OFF          (2) alone
    NORM    flag off, prices fit off,         (3) alone: hi/lo/span/mean/std
            hi/lo/span/mean/std taken from ON  from the ON pool, prices untouched

`--passes N` overrides `conversion_passes` so the convergence loop's own
contribution can be held out (N=1 is one pass, no re-pricing against the core).
"""
import argparse
import copy
import json
from collections import Counter

import numpy as np

from smite import assemble, efficiency, hybrid, recommend, scoring

MODES = ("Conquest", "Joust", "Arena")


# ── the four arms ────────────────────────────────────────────────────────────

def fit_table(items, weights, flag_on):
    """The NNLS gold table with `price_stat_multipliers` forced on or off, every
    other pricing flag left exactly as _weights.yaml ships it."""
    w = copy.deepcopy(weights)
    w["price_stat_multipliers"] = bool(flag_on)
    before = efficiency.apply_pricing_flags(w)
    try:
        gold, names = efficiency.fit_gold_values(items)
    finally:
        efficiency.restore_pricing_flags(before)
    return gold, names


def scores_for(items, weights, *, flag_on, gold, renorm_from=None):
    """`efficiency_scores` with the stat lines chosen by `flag_on` and the gold
    table chosen by `gold`, which are normally the same arm and here are not.

    `renorm_from` replaces the min-max constants (hi, span, mean, std) with
    another arm's, so the same residuals can be re-expressed on another pool's
    scale. That is the only way to see channel (3) on its own."""
    w = copy.deepcopy(weights)
    w["price_stat_multipliers"] = bool(flag_on)
    before = efficiency.apply_pricing_flags(w)
    real_fit = efficiency.fit_gold_values
    efficiency.fit_gold_values = lambda _items: (dict(gold), None)
    try:
        eff, gold_values = efficiency.efficiency_scores(items)
    finally:
        efficiency.fit_gold_values = real_fit
        efficiency.restore_pricing_flags(before)
    if renorm_from is not None:
        hi, span = renorm_from["hi"], renorm_from["span"]
        mean, std = renorm_from["mean"], renorm_from["std"]
        for row in eff.values():
            row["score"] = (hi - row["residual"]) / span
            row["z"] = (row["residual"] - mean) / std
            row["span"] = span
    return eff, gold_values


def norm_constants(eff):
    """The min-max constants `efficiency_scores` derived for one arm."""
    vals = np.array([r["residual"] for r in eff.values()], dtype=float)
    hi, lo = float(vals.max()), float(vals.min())
    return {"hi": hi, "lo": lo, "span": (hi - lo) or 1.0,
            "mean": float(vals.mean()), "std": float(vals.std()) or 1.0}


# ── cores ────────────────────────────────────────────────────────────────────

def _model_and_core(god, items, god_build, weights, tags_map, mode, eff, items_by_name,
                    gold_values, aspect_overlay=None, passes=None):
    """The `core` and `model` cores for one god in one mode — `recommend`'s own
    two calls, with everything the archetype/hybrid path adds left out."""
    profile = scoring.resolve_profile(weights, mode, None, aspect_overlay=aspect_overlay)
    rows = scoring.score_god_items(god, items, god_build, eff, weights, tags_map, profile)
    n_passes = weights.get("conversion_passes", 1) if passes is None else passes
    shared = dict(
        passes=n_passes, n=6,
        max_lifesteal=scoring.god_max_lifesteal(god, weights, profile),
        stat_caps=weights.get("stat_caps"),
        economy=profile.get("economy"),
        **assemble.coherence_args(items, weights),
        **assemble.conversion_args(weights, eff, gold_values),
        **assemble.overflow_args(weights, eff, gold_values))
    core, _ = assemble.assemble_core_converged(rows, items_by_name, **shared)
    model_rows = sorted(rows, key=lambda r: (-r["quality"], r["item"]))
    model, _ = assemble.assemble_core_converged(model_rows, items_by_name,
                                                score_key="quality", **shared)
    return core, model


def all_cores(items, gods, builds, weights, tags_map, eff, gold_values, passes=None,
              aspects=False):
    """`{(mode, build group): {"core": [...], "model": [...]}}` over every god.

    `aspects` adds the seven aspect-overlay build groups `recommend` also writes.
    Default off, because §4.21 counted 90 — the gods — and this has to be the
    same 90 before it can decompose them."""
    items_by_name = {it["name"]: it for it in items}
    out = {}
    for mode in MODES:
        for god in gods:
            note = builds[mode][god["name"]]
            overlays = [(None, "")]
            aspect_overlay = (weights.get("aspects") or {}).get(god["name"])
            if aspects and aspect_overlay and (god.get("aspects") or []):
                overlays.append((aspect_overlay, " (aspect)"))
            for overlay, suffix in overlays:
                core, model = _model_and_core(
                    god, items, note, weights, tags_map, mode, eff, items_by_name,
                    gold_values, aspect_overlay=overlay, passes=passes)
                out[(mode, god["name"] + suffix)] = {"core": core, "model": model}
    return out


def churn(base, arm, kind="model"):
    """Build groups whose core changed, per mode, comparing as SETS — §4.21
    counted membership, and `build_order` is measured elsewhere."""
    per_mode = Counter()
    changed = []
    for key, sets in base.items():
        if frozenset(sets[kind]) != frozenset(arm[key][kind]):
            per_mode[key[0]] += 1
            changed.append(key)
    return per_mode, changed


def flow(base, arm, kind="model"):
    """Items entering and leaving, Conquest only — §4.21's churn list."""
    delta = Counter()
    for key, sets in base.items():
        if key[0] != "Conquest":
            continue
        before, after = set(sets[kind]), set(arm[key][kind])
        for name in after - before:
            delta[name] += 1
        for name in before - after:
            delta[name] -= 1
    return delta


def top_flow(delta, n=3):
    ordered = sorted(delta.items(), key=lambda kv: (-kv[1], kv[0]))
    ins = [(k, v) for k, v in ordered if v > 0][:n]
    outs = [(k, v) for k, v in ordered[::-1] if v < 0][:n]
    return ins, outs




def affine(eff_base, eff_arm, skip):
    """(gain, offset, max deviation, positions whose efficiency RANK moved) for
    the items the flag does not price.

    A pure renormalisation is affine in the old score with machine-epsilon
    deviation and moves no rank at all; a genuine repricing is neither."""
    names = [n for n in eff_base if n not in skip]
    xs = [eff_base[n]["score"] for n in names]
    ys = [eff_arm[n]["score"] for n in names]
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    gain = (sum((x - mx) * (y - my) for x, y in zip(xs, ys))
            / sum((x - mx) ** 2 for x in xs))
    offset = my - gain * mx
    dev = max(abs(y - (gain * x + offset)) for x, y in zip(xs, ys))
    a = sorted(names, key=lambda n: -eff_base[n]["score"])
    b = sorted(names, key=lambda n: -eff_arm[n]["score"])
    return gain, offset, dev, sum(1 for x, y in zip(a, b) if x != y), len(names)


# ── report ───────────────────────────────────────────────────────────────────

#: The items `price_stat_multipliers` gives a stat line to. Genie's Lamp has no
#: cost and no printed stats, so it never reaches the scored pool at all.
PRICED = ("Agility Greaves", "Shell of Rebuke", "Talisman of Purification",
          "Time-lock Aegis", "Genie's Lamp")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--passes", type=int, default=None,
                    help="override conversion_passes (1 disables the convergence loop)")
    ap.add_argument("--aspects", action="store_true",
                    help="include the seven aspect-overlay build groups too")
    ap.add_argument("--json", action="store_true", help="machine-readable dump")
    args = ap.parse_args(argv)

    items = recommend.load_items()
    gods = recommend.load_gods()
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    tags_map = scoring.load_tags(recommend.TAGS_PATH)
    builds = {m: {g["name"]: recommend.load_build_note(g["name"], m) for g in gods}
              for m in MODES}

    gold_off, _ = fit_table(items, weights, False)
    gold_on, _ = fit_table(items, weights, True)
    eff_off, gv_off = scores_for(items, weights, flag_on=False, gold=gold_off)
    eff_on, gv_on = scores_for(items, weights, flag_on=True, gold=gold_on)
    norm_on = norm_constants(eff_on)
    eff_refit, gv_refit = scores_for(items, weights, flag_on=False, gold=gold_on)
    eff_local, gv_local = scores_for(items, weights, flag_on=True, gold=gold_off)
    eff_norm, gv_norm = scores_for(items, weights, flag_on=False, gold=gold_off,
                                   renorm_from=norm_on)

    arms = [("ON", eff_on, gv_on), ("REFIT", eff_refit, gv_refit),
            ("LOCAL", eff_local, gv_local), ("NORM", eff_norm, gv_norm)]
    everything = [("OFF", eff_off, gv_off)] + arms

    base = all_cores(items, gods, builds, weights, tags_map, eff_off, gv_off,
                     passes=args.passes, aspects=args.aspects)
    cores = {"OFF": base}
    for name, eff, gv in arms:
        cores[name] = all_cores(items, gods, builds, weights, tags_map, eff, gv,
                                passes=args.passes, aspects=args.aspects)

    groups = len(base) // len(MODES)
    n_passes = (args.passes if args.passes is not None
                else weights.get("conversion_passes", 1))
    report = {"groups_per_mode": groups, "passes": n_passes,
              "gold": {}, "norm": {}, "affine": {}, "churn": {}, "flow": {},
              "priced_in_cores": {}}

    for key in ("_intercept", "Strength", "Intelligence", "Max Health",
                "Physical Protection", "Magical Protection", "Attack Damage"):
        report["gold"][key] = {"off": gold_off.get(key, 0.0),
                               "on": gold_on.get(key, 0.0)}
    for name, eff, _ in everything:
        n = norm_constants(eff)
        n["argmax"] = max(eff.items(), key=lambda kv: kv[1]["residual"])[0]
        n["argmin"] = min(eff.items(), key=lambda kv: kv[1]["residual"])[0]
        report["norm"][name] = n
    for name, eff, _ in arms:
        gain, offset, dev, ranks, n = affine(eff_off, eff, PRICED)
        report["affine"][name] = {"gain": gain, "offset": offset, "max_dev": dev,
                                  "rank_moves": ranks, "items": n}
        for kind in ("model", "core"):
            per_mode, _ = churn(base, cores[name], kind)
            report["churn"].setdefault(name, {})[kind] = {
                m: per_mode.get(m, 0) for m in MODES}
        ins, outs = top_flow(flow(base, cores[name]))
        report["flow"][name] = {"in": ins, "out": outs}
    for name in cores:
        report["priced_in_cores"][name] = sum(
            1 for sets in cores[name].values()
            for kind in ("model", "core")
            if any(p in sets[kind] for p in PRICED))

    if args.json:
        print(json.dumps(report, indent=2, default=str))
        return 0

    print(f"{groups} build groups per mode, {len(MODES)} modes"
          f"  ·  conversion_passes={n_passes}")
    print("\nFITTED GOLD TABLE")
    for key, pair in report["gold"].items():
        print(f"  {key:22} {pair['off']:>9.2f} -> {pair['on']:>9.2f}")

    print("\nTHE RESIDUAL POOL efficiency_scores NORMALISES ON")
    print(f"  {'arm':6} {'hi':>9}  {'argmax':24} {'lo':>10}  {'argmin':10} {'span':>9}")
    for name, _, _ in everything:
        n = report["norm"][name]
        print(f"  {name:6} {n['hi']:>9.2f}  {n['argmax']:24} {n['lo']:>10.2f}  "
              f"{n['argmin']:10} {n['span']:>9.2f}")
    print(f"  hi is 2500 - intercept in both: {2500 - gold_off['_intercept']:.2f}"
          f" / {2500 - gold_on['_intercept']:.2f} — Agility Greaves' one printed"
          " stat (Movement Speed)\n  has a single carrier, so MIN_STAT_CARRIERS"
          " drops it and the fit sees an all-zero row.")

    print("\nWHAT EACH ARM DOES TO THE ITEMS THE FLAG DOES NOT PRICE")
    for name, _, _ in arms:
        a = report["affine"][name]
        print(f"  {name:6} score = {a['gain']:.4f}*score_off {a['offset']:+.4f}"
              f"   max deviation {a['max_dev']:.1e}"
              f"   efficiency rank moves at {a['rank_moves']:>3} of {a['items']}")

    for kind in ("model", "core"):
        print(f"\n{kind.upper()} CORES CHANGED vs OFF")
        print(f"  {'arm':8} {'Conquest':>9} {'Joust':>7} {'Arena':>7}")
        for name, _, _ in arms:
            c = report["churn"][name][kind]
            print(f"  {name:8} {c['Conquest']:>9} {c['Joust']:>7} {c['Arena']:>7}")

    print("\nCONQUEST MODEL CHURN, ITEMS IN / OUT")
    for name, _, _ in arms:
        f = report["flow"][name]
        print(f"  {name:8} in   " + ("  ".join(f"{k} +{v}" for k, v in f["in"]) or "-"))
        print(f"  {'':8} out  " + ("  ".join(f"{k} {v}" for k, v in f["out"]) or "-"))

    print("\nTHE FALSIFIER: build groups holding any priced item, by arm")
    print("  " + "   ".join(f"{k} {v}" for k, v in report["priced_in_cores"].items()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
