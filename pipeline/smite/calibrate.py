"""Grid-search the four signal weights against the validation metric, with
guardrails (efficiency + fit >= 0.50, pick <= 0.15) and a leave-one-god-out
stability check. Writes Analysis/_calibration.md. Applying the winner to
_weights.yaml stays a deliberate human edit — the weights file is the
recommender's opinion surface, not a cache."""
import copy

from smite import recommend, scoring, validate


def weight_grid(step=0.05, min_eff_fit=0.50, max_pick=0.15):
    n = round(1 / step)
    grid = []
    for e in range(n + 1):
        for w in range(n + 1 - e):
            for p in range(n + 1 - e - w):
                f = n - e - w - p
                we, ww, wp, wf = (x * step for x in (e, w, p, f))
                if wp > max_pick + 1e-9 or we + wf < min_eff_fit - 1e-9:
                    continue
                grid.append({"efficiency": round(we, 2), "win": round(ww, 2),
                             "pick": round(wp, 2), "fit": round(wf, 2)})
    return grid


def objective(agg):
    s = agg["pooled_spearman"] if agg.get("pooled_spearman") is not None else 0.0
    return 0.5 * ((s + 1) / 2) + 0.5 * agg["mean_coverage"]


def evaluate_grid(items, weights, tags_map, gods, builds_by_god, grid):
    results = []
    for sig in grid:
        w = copy.deepcopy(weights)
        w["signals"] = dict(sig)
        per_god, agg = validate.compute(items=items, weights=w, tags_map=tags_map,
                                        gods=gods, builds_by_god=builds_by_god)
        results.append({"signals": sig, "agg": agg, "per_god": per_god,
                        "objective": objective(agg)})
    return sorted(results, key=lambda r: -r["objective"])


def logo_winners(results):
    """Per held-out god: the signal combo that wins on the other gods. A top
    pick that flips wildly across folds is overfit — report, don't hide."""
    gods = sorted(results[0]["per_god"].keys()) if results else []
    out = {}
    for g in gods:
        best, best_obj = None, float("-inf")
        for r in results:
            sub = {k: v for k, v in r["per_god"].items() if k != g}
            if not sub:
                continue
            obj = objective(validate.aggregate(sub))
            if obj > best_obj:
                best, best_obj = r["signals"], obj
        out[g] = best
    return out


def write_report(results, logo, current, out_path, top_n=15):
    lines = ["# Signal-weight calibration", "",
             "Guardrails: efficiency+fit ≥ 0.50, pick ≤ 0.15, sum = 1. "
             "Objective = 0.5·norm(Spearman) + 0.5·coverage.", "",
             f"**Current hand weights:** {current}", "",
             "| eff | win | pick | fit | objective | Spearman | coverage |",
             "|---|---|---|---|---|---|---|"]
    for r in results[:top_n]:
        s = r["signals"]
        lines.append(f"| {s['efficiency']} | {s['win']} | {s['pick']} | {s['fit']} "
                     f"| {r['objective']:.3f} | {(r['agg']['pooled_spearman'] or 0):.2f} "
                     f"| {r['agg']['mean_coverage']:.0%} |")
    lines += ["", "## Leave-one-god-out winners", ""]
    lines += [f"- without {g}: {w}" for g, w in logo.items()]
    distinct = {tuple(sorted(w.items())) for w in logo.values() if w}
    lines += ["", f"**Stability:** {len(distinct)} distinct fold-winner(s) across "
              f"{len(logo)} folds — {'stable' if len(distinct) <= 3 else 'UNSTABLE, do not apply blindly'}."]
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv=None):
    items = recommend.load_items()
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    tags_map = scoring.load_tags(recommend.TAGS_PATH)
    gods = recommend.load_gods()
    builds_by_god = {g["name"]: recommend.load_build_note(g["name"]) for g in gods}
    results = evaluate_grid(items, weights, tags_map, gods, builds_by_god, weight_grid())
    logo = logo_winners(results)
    out = recommend.DATA_ROOT / "Analysis" / "_calibration.md"
    write_report(results, logo, weights["signals"], out)
    best = results[0]
    print(f"Wrote {out}\nBest: {best['signals']} objective {best['objective']:.3f}")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
