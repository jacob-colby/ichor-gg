"""Grid-search the four signal weights against the validation metric — and,
first, measure how much of that metric is the metric grading its own input.

WHY THIS MODULE LEADS WITH A LEAKAGE PROBE

`validate.compute` scores a weight vector two ways, and BOTH targets are also
model inputs:

    pooled_spearman   correlates our blended `total` against community WIN RATE
    mean_coverage     overlap of our 6-item core with the COMMUNITY BUILD

`signal_score` computes `total = w_win*win_rate + w_pick*pick_rate + ...`. So
`win` is the Spearman target verbatim, and `pick` all but determines community
membership (community-slot items average a 0.204 pick rate against 0.117 for
the alternates they beat). Measured on the unconstrained grid:

    weights                  Spearman   coverage
    win 1.00                    1.000      60.7%     <- perfect self-correlation
    pick 1.00                  -0.057      86.3%     <- reproduces the build

Both degenerate corners are a passthrough of the community's own data with
zero modeling content, and both beat every real blend. The objective is
therefore maximised by DELETING the model. The guardrails below are not a
prior on top of a sound objective — they are the only thing standing between
this search and that answer, which is why the guardrail-bound winner always
lands pressed against a constraint (2026-08-05: `pick` at the 0.15 cap).

CONCLUSION, RECORDED SO IT IS NOT RE-LITIGATED: the guardrailed grid cannot
select weights. A point it prefers is preferred because it leaked more of the
target into the input. `grid_results` is kept because the FRONTIER it traces
is informative — it prices the popularity/performance trade-off, and choosing
a point on it is a product decision, not a measurement.

WHAT CAN BE MEASURED HONESTLY

Zero `win` and `pick` and the SIGNAL leakage is gone: no signal derived from
the target enters the score. (Not all of it - see the next section, which is
the exception and its size.) What is left — efficiency and fit — can then be graded
against a real baseline, a random legal 6-item core drawn from the same
candidate pool (median 92 items per god):

    random 6-item core        6.0%
    efficiency + fit         29.0%    4.8x chance

That is the project's actual, leakage-free result: **the model identifies
community-worthy items about 4.8x better than chance.** It is the number to
quote, and the number to move. It is also what showed the day's work was worth
shipping when the headline gate said otherwise — holding the data fixed and
restoring the pre-2026-08-05 rules scores 4.17x against the current 4.81x,
while `mean_coverage` fell 51.0% -> 49.6% over the same change.

IT ZEROES SIGNALS. IT DOES NOT NEUTRALISE COMMUNITY-DERIVED CONSTANTS.

"Nothing derived from the target enters the score" is true of the four SIGNALS
and false of the model's constants, and one shipped flag reaches that
distinction. `passives.measure_conversion_reference` builds `conversion_reference`
by iterating community build entries and skipping every other source; that key
is read by `efficiency.item_stat_values` and `assemble.conversion_args`, and
`price_conversions` ships ON. So a number measured off the community record is
inside every figure this module prints, and zeroing `win` and `pick` does not
touch it.

Audited and measured 2026-09-03 (docs/STATE.md 4.20, full tables under
`conversion_reference` in _weights.yaml). The short version: replacing it with
the community-free analogue - the mean stat line of a tier-3 buildable, from
item data alone - costs 2.6pp on the probe split and 0.6pp at eff 0.45, and
changes no verdict, because every verdict in the register is a delta with the
constant held identical on both arms. `price_conversions` still beats OFF on
the same standard with a community-free reference. Two things bound it: the
community value is NOT a peak in reference magnitude (1.25x and 1.50x both
score higher), and nothing in production re-derives the key, so the 3.1% the
record has drifted under it since 2026-08-14 costs 0.00pp on both splits.

WHY THIS MODULE DOES NOT FIX IT BY SUBSTITUTION. Zeroing a signal is
well-defined; a constant has no zero. Emptying `conversion_reference` does not
remove it, it substitutes 0 - and in the assembly half that is the OPPOSITE of
neutral, since `conversion_score_bonus` then subtracts no reference and credits
a converter with its whole mana. The only available "neutralisation" is to
substitute a different constant, which is a model change, and a `calibrate`
that silently swaps constants reports the number for a model nobody ships -
exactly the defect `efficiency.apply_pricing_flags` exists to close, arriving
from the other side. Whether the MODEL should carry a community-free reference
is a decision for _weights.yaml, not a thing this module should do behind it.

It comes with a matching negative. Within the community's own set the model
cannot rank at all: mean within-god rank correlation -0.02, and measured
separately, efficiency alone -0.03 and fit alone +0.02. The model is a working
FILTER and not a working RANKER, and the gate's headline number conflates the
two.

`model_signal_sweep` is the only part of this module whose winner may be
applied directly. As of 2026-08-05 it declines to pick: everything from ~0.15
to ~0.65 efficiency sits inside one flat plateau whose bootstrap CIs overlap
almost entirely, so the nominal winner moves run to run without meaning
anything. It separates one thing clearly, and it is a floor not a peak:
efficiency-DOMINANT blends are worse, falling off a cliff above 0.75 to 13.3%
at efficiency alone against 26.9% for fit alone. Fit is carrying this model.

Writes Analysis/_calibration.md. Applying any winner to _weights.yaml stays a
deliberate human edit — the weights file is the recommender's opinion surface,
not a cache.

THE CONTROL, AND WHY IT IS A SEPARATE ENTRY POINT

The full run above takes ~7 minutes under `conversion_passes: 3`, so nobody
runs it merely to re-measure the control they are about to compare against —
and a control goes stale on every `chore(data): daily community refresh`. That
has caused or nearly caused a misattribution four times: the delta gets read as
the change when part of it is the data.

`--control` is the cheap half, ~7s: the random-core baseline and coverage at
two FIXED splits. Fixed, not the sweep's argmax, because the argmax moves with
the data and two runs cannot be compared on a number that does.

It also prints an INPUT FINGERPRINT — a short hash over the item set, the god
notes, the effect tags, the COMMUNITY entries of the build notes and the
weights. "Did the baseline move" is only a proxy for "is this the same data";
the fingerprint answers it directly, including in the case where the data moved
and the baseline happened not to. The same fingerprint is stamped into
_calibration.md, so a stale report can be identified as stale without rerunning
anything, and `--control` says so in one line when the two differ.

Only the community half of a build note is hashed. The rest of that file is our
own generated output, so hashing it would make the fingerprint move whenever
`recommend` ran — a change in the model masquerading as a change in the data,
which is exactly the confusion this exists to end.
"""
import argparse
import copy
import hashlib
import json
import math
import random
import re
import statistics

from smite import assemble, efficiency, recommend, scoring, validate

# Draws per god for the random-core baseline, and the seed that fixes it.
# Deterministic so the baseline in a report is reproducible from the report.
BASELINE_DRAWS = 200
BASELINE_SEED = 20260805
BOOTSTRAP_RESAMPLES = 2000

# The two splits `--control` reports, held FIXED for all time. The first is the
# leakage probe's `model only` corner; the second is the split §1 of docs/STATE.md
# quotes alongside it. Deliberately NOT the sweep's argmax — that moves with the
# data, and a control has to be a number two runs can be compared on.
CONTROL_SPLITS = ((0.70, 0.30), (0.45, 0.55))

# Hex characters kept from the sha256. 12 is ~2e-14 collision odds over the
# handful of dataset states anyone compares, and short enough to read aloud.
FINGERPRINT_LEN = 12
_REPORT_FINGERPRINT_RE = re.compile(r"^_Input fingerprint:\s*`([0-9a-f]+)`")


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


class _Fixture:
    """The inputs every evaluation shares, loaded once. Loading dominates the
    cost of a sweep (~3s against ~0.07s per evaluation), so hoisting it is the
    difference between a 30-minute grid and a 30-second one."""

    def __init__(self, items=None, weights=None, tags_map=None, gods=None,
                 builds_by_god=None):
        self.items = items if items is not None else recommend.load_items()
        self.weights = weights if weights is not None else scoring.load_weights(
            recommend.WEIGHTS_PATH)
        self.tags_map = tags_map if tags_map is not None else scoring.load_tags(
            recommend.TAGS_PATH)
        self.gods = gods if gods is not None else recommend.load_gods()
        self.builds_by_god = builds_by_god if builds_by_god is not None else {
            g["name"]: recommend.load_build_note(g["name"]) for g in self.gods}
        # Applied once here as well as inside `validate.compute`, because
        # `random_core_baseline` fits its own gold values and would otherwise
        # depend on whether a probe happened to run first. A baseline computed
        # against a different model than the thing it baselines is not one.
        efficiency.apply_pricing_flags(self.weights)

    def evaluate(self, signals):
        """(per_god, agg) for one signal vector."""
        w = copy.deepcopy(self.weights)
        w["signals"] = dict(signals)
        return validate.compute(items=self.items, weights=w, tags_map=self.tags_map,
                                gods=self.gods, builds_by_god=self.builds_by_god)


def _mean(values):
    return sum(values) / len(values) if values else 0.0


def _canonical(obj):
    """Order-independent JSON for hashing.

    `sort_keys` is the load-bearing part: a dict that round-trips through YAML
    in a different order is the same data, and a fingerprint that moved for it
    would cry wolf. Lists keep their order because every list hashed here is
    one whose order is data (`slot_order`, a god's abilities). `default=str`
    covers the dates PyYAML hands back; `str` of a date is stable."""
    return json.dumps(obj, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=True, default=str)


def input_fingerprint(fx):
    """Short hash over the inputs a control depends on.

    Contains only things that change when the DATA changes: the item notes, the
    god notes, the effect tags, the community entries of the build notes, and
    the weights. No timestamps, no file mtimes, no paths, no dict ordering — so
    two checkouts of the same data fingerprint identically, and a
    `chore(data): daily community refresh` moves it whether or not it happened
    to move the baseline.

    The build notes are reduced to `_community_slots` on purpose: the suggested
    builds in the same file are our own output, and hashing them would report a
    model change as a data change."""
    payload = {
        "items": fx.items,
        "gods": fx.gods,
        "tags": fx.tags_map,
        "community": {name: validate._community_slots(note)
                      for name, note in fx.builds_by_god.items()},
        "weights": fx.weights,
    }
    return hashlib.sha256(
        _canonical(payload).encode("utf-8")).hexdigest()[:FINGERPRINT_LEN]


def report_fingerprint(path):
    """The fingerprint stamped into a written report, or None.

    None means either "no such report" or "written before this existed"; both
    are the same thing to a reader — the report cannot vouch for its own data."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    for line in text.splitlines():
        m = _REPORT_FINGERPRINT_RE.match(line)
        if m:
            return m.group(1)
    return None


def bootstrap_ci(values, resamples=BOOTSTRAP_RESAMPLES, seed=BASELINE_SEED):
    """Percentile 95% CI for the mean of per-god values. The per-god spread is
    wide (many gods sit at 0% or 100%), so a bare mean invites reading a
    one-point difference as real when the interval is ten points wide."""
    if not values:
        return (0.0, 0.0)
    rng = random.Random(seed)
    n = len(values)
    means = sorted(_mean(rng.choices(values, k=n)) for _ in range(resamples))
    lo = means[int(0.025 * resamples)]
    hi = means[min(resamples - 1, int(0.975 * resamples))]
    return (lo, hi)


def random_core_baseline(fx, draws=BASELINE_DRAWS, seed=BASELINE_SEED):
    """Mean coverage of a RANDOM legal 6-item core, per god, averaged.

    The number every coverage figure should be read against. Coverage has no
    natural zero — a god's candidate pool is ~92 items and the community set is
    ~4.6 of them, so chance is small but not negligible, and "51%" means
    nothing until you know that chance is 6.5%.

    Drawn from the same `score_god_items` pool the recommender picks from, so
    the damage filter, buildability and mode exclusions apply identically."""
    rng = random.Random(seed)
    eff_scores, _ = efficiency.efficiency_scores(fx.items)
    profile = scoring.resolve_profile(fx.weights, "Conquest", None)
    per_god = {}
    for god in fx.gods:
        note = fx.builds_by_god[god["name"]]
        slots = validate._community_slots(note)
        if not slots:
            continue
        rows = scoring.score_god_items(god, fx.items, note, eff_scores,
                                       fx.weights, fx.tags_map, profile)
        names = [r["item"] for r in rows]
        scored = set(names)
        community = [c["name"] for c in slots
                     if c["name"] in scored and c.get("win_rate") is not None]
        if not community or not names:
            continue
        hits = []
        for _ in range(draws):
            pick = set(rng.sample(names, min(6, len(names))))
            hits.append(len(pick & set(community)) / len(community))
        per_god[god["name"]] = _mean(hits)
    return {"mean": _mean(list(per_god.values())), "per_god": per_god,
            "pool_median": statistics.median(
                [len(scoring.score_god_items(g, fx.items, fx.builds_by_god[g["name"]],
                                             eff_scores, fx.weights, fx.tags_map, profile))
                 for g in fx.gods]) if fx.gods else 0}


def exact_random_core_baseline(fx):
    """`random_core_baseline`'s mean, in closed form — no sampling.

    Each community item is drawn with probability `min(6, N)/N` from a god's
    pool of N, so the expected covered fraction is that ratio, whatever the
    community set contains. Averaged over gods, it is exactly what the 200-draw
    sampler estimates.

    IT EXISTS BECAUSE THE SAMPLER MOVES WHEN THE MODEL DOES, and that reads as
    the one thing the baseline is supposed to rule out. The printed figure is
    the tell that the committed `_calibration.md` has gone stale against a data
    refresh — chance cannot depend on a model flag. But `score_god_items`
    returns its rows SORTED BY SCORE, so a pricing change reshuffles the list a
    fixed seed samples from, and the estimate wobbles: 5.73% / 5.59% / 5.65%
    across `price_adaptive` off/Strength/Intelligence on 2026-08-21, against
    5.7391% here for all three and a pool that never changed membership. Read
    this one before concluding the data moved.
    """
    eff_scores, _ = efficiency.efficiency_scores(fx.items)
    profile = scoring.resolve_profile(fx.weights, "Conquest", None)
    ratios = []
    for god in fx.gods:
        note = fx.builds_by_god[god["name"]]
        slots = validate._community_slots(note)
        if not slots:
            continue
        rows = scoring.score_god_items(god, fx.items, note, eff_scores,
                                       fx.weights, fx.tags_map, profile)
        names = {r["item"] for r in rows}
        community = [c["name"] for c in slots
                     if c["name"] in names and c.get("win_rate") is not None]
        if not community or not names:
            continue
        ratios.append(min(6, len(names)) / len(names))
    return _mean(ratios)


def within_god_spearman(per_god, min_items=3):
    """Mean/median rank correlation computed INSIDE each god, not pooled.

    `validate.aggregate` pools every (score, win_rate) pair across all gods,
    which lets a god-level effect masquerade as ranking skill: item A on a
    strong god outranking item B on a weak one says nothing about either
    item. Correlating within a god and then averaging removes that, and the
    two disagree sharply — pooled +0.55 against within-god +0.35 at the
    shipped weights."""
    rhos = []
    for metrics in per_god.values():
        pairs = metrics["pairs"]
        if len(pairs) < min_items:
            continue
        rho = validate.spearman([x for x, _ in pairs], [y for _, y in pairs])
        if rho is not None:
            rhos.append(rho)
    if not rhos:
        return {"mean": None, "median": None, "positive": 0, "n": 0}
    return {"mean": _mean(rhos), "median": statistics.median(rhos),
            "positive": sum(1 for r in rhos if r > 0), "n": len(rhos)}


def leakage_probe(fx):
    """The degenerate corners, to show what the objective actually maximises.

    Each row zeroes the model entirely and hands the metric one of its own
    inputs. If a corner beats the real blends, the objective is grading its
    own input and no interior point it prefers can be trusted."""
    corners = [
        ("win only (Spearman's target verbatim)", {"efficiency": 0.0, "win": 1.0,
                                                   "pick": 0.0, "fit": 0.0}),
        ("pick only (community membership)", {"efficiency": 0.0, "win": 0.0,
                                              "pick": 1.0, "fit": 0.0}),
        ("model only (efficiency + fit)", {"efficiency": 0.7, "win": 0.0,
                                           "pick": 0.0, "fit": 0.3}),
    ]
    out = []
    for label, signals in corners:
        per_god, agg = fx.evaluate(signals)
        out.append({"label": label, "signals": signals, "agg": agg,
                    "within_god": within_god_spearman(per_god)})
    return out


def model_signal_sweep(fx, step=0.05):
    """Leakage-free calibration of the efficiency:fit split.

    `win` and `pick` are held at ZERO, so nothing derived from either target
    enters the score and coverage becomes an honest measurement. This is the
    only sweep in this module whose winner may be applied directly — and it
    reports a bootstrap CI precisely so a winner inside the noise is not
    applied anyway."""
    n = round(1 / step)
    out = []
    for i in range(n + 1):
        e = round(i * step, 2)
        f = round(1.0 - e, 2)
        per_god, agg = fx.evaluate({"efficiency": e, "win": 0.0, "pick": 0.0, "fit": f})
        covs = [m["coverage"] for m in per_god.values()]
        out.append({"efficiency": e, "fit": f, "coverage": agg["mean_coverage"],
                    "ci": bootstrap_ci(covs)})
    return out


def evaluate_grid(items, weights, tags_map, gods, builds_by_god, grid):
    fx = _Fixture(items, weights, tags_map, gods, builds_by_god)
    results = []
    for sig in grid:
        per_god, agg = fx.evaluate(sig)
        results.append({"signals": sig, "agg": agg, "per_god": per_god,
                        "objective": objective(agg)})
    return sorted(results, key=lambda r: -r["objective"])


def logo_winners(results):
    """Per held-out god: the signal combo that wins on the other gods. A top
    pick that flips wildly across folds is overfit — report, don't hide.

    Note what this does and does not check. It is a stability test, not a
    validity test: a leaked objective is leaked identically in every fold, so
    this reports "stable" for a degenerate winner just as confidently as for a
    real one. Read it only after `leakage_probe`."""
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


def _fmt(sig):
    return (f"eff {sig['efficiency']:.2f} · win {sig['win']:.2f} · "
            f"pick {sig['pick']:.2f} · fit {sig['fit']:.2f}")


def write_report(results, logo, current, out_path, probe=None, baseline=None,
                 model_sweep=None, top_n=15, fingerprint=None):
    base = baseline["mean"] if baseline else None
    lines = ["# Signal-weight calibration", "",
             "> **Read the leakage probe before the grid.** Both of this "
             "metric's targets are also model inputs, so the grid's ranking is "
             "partly the metric grading its own input. See `calibrate.py`.", ""]
    if fingerprint:
        # Stamped so a stale report can be identified as stale without rerunning
        # anything: `python -m smite.calibrate --control` prints the fingerprint
        # of the data on disk now and compares it against this line.
        lines += [f"_Input fingerprint: `{fingerprint}` — items, gods, tags, "
                  "community builds, weights. Check it against "
                  "`python -m smite.calibrate --control` before quoting any "
                  "number below._", ""]

    if probe:
        lines += ["## 1. Leakage probe — what the objective actually maximises", "",
                  "Each row deletes the model and hands the metric one of its own "
                  "inputs. A corner that beats the real blends means the objective "
                  "cannot select weights.", "",
                  "| Weights | Spearman (pooled) | Within-god | Coverage |",
                  "|---|---|---|---|"]
        for row in probe:
            a, wg = row["agg"], row["within_god"]
            wg_txt = ("n/a" if wg["mean"] is None
                      else f"{wg['mean']:+.2f} (positive on {wg['positive']}/{wg['n']})")
            lines.append(f"| {row['label']} | {(a['pooled_spearman'] or 0):.3f} | "
                         f"{wg_txt} | {a['mean_coverage']:.1%} |")
        lines += ["", "`win only` scores a perfect Spearman because the score *is* "
                  "the target. `pick only` all but reproduces the community build. "
                  "Neither contains any modeling.", ""]

    if baseline:
        lines += ["## 2. Baseline — what coverage means", "",
                  f"A **random** legal 6-item core, drawn {BASELINE_DRAWS}x per god "
                  f"from the same candidate pool (median {baseline['pool_median']:.0f} "
                  f"items), covers **{base:.1%}** of the community set. Every "
                  "coverage number below is a multiple of that, not of zero.", ""]

    if model_sweep:
        lines += ["## 3. Leakage-free sweep of the model signals", "",
                  "`win` and `pick` held at **zero**, so nothing from the target "
                  "enters the score. This is the only sweep whose winner may be "
                  "applied directly.", "",
                  "| efficiency | fit | coverage | 95% CI | vs chance |",
                  "|---|---|---|---|---|"]
        for row in model_sweep:
            mult = f"{row['coverage'] / base:.1f}x" if base else "—"
            lines.append(f"| {row['efficiency']:.2f} | {row['fit']:.2f} | "
                         f"{row['coverage']:.1%} | "
                         f"[{row['ci'][0]:.1%}, {row['ci'][1]:.1%}] | {mult} |")
        best = max(model_sweep, key=lambda r: r["coverage"])
        overlapping = [r for r in model_sweep if r["ci"][1] >= best["ci"][0]]
        lines += ["", f"Best: efficiency {best['efficiency']:.2f} : fit "
                  f"{best['fit']:.2f} at {best['coverage']:.1%}. "
                  f"**{len(overlapping)} of {len(model_sweep)} splits have a CI "
                  "overlapping it** — treat a winner inside that band as noise "
                  "and leave the shipped split alone.", ""]

    lines += ["## 4. Guardrailed grid — the trade-off frontier, not a winner", "",
              "Guardrails: efficiency+fit ≥ 0.50, pick ≤ 0.15, sum = 1. "
              "Objective = 0.5·norm(Spearman) + 0.5·coverage. The guardrails are "
              "load-bearing: they are what keeps this search away from the "
              "degenerate corners above, so a row pressed against `pick ≤ 0.15` "
              "is the constraint speaking, not the data.", "",
              f"**Current hand weights:** {_fmt(current)}", "",
              "| eff | win | pick | fit | objective | Spearman | coverage |",
              "|---|---|---|---|---|---|---|"]
    for r in results[:top_n]:
        s = r["signals"]
        marker = " ←current" if s == dict(current) else ""
        lines.append(f"| {s['efficiency']} | {s['win']} | {s['pick']} | {s['fit']} "
                     f"| {r['objective']:.3f} | {(r['agg']['pooled_spearman'] or 0):.2f} "
                     f"| {r['agg']['mean_coverage']:.0%}{marker} |")
    lines += ["", "## 5. Leave-one-god-out winners", "",
              "_Stability only. A leaked objective leaks identically in every "
              "fold, so this cannot detect the problem in section 1._", ""]
    lines += [f"- without {g}: {_fmt(w) if w else 'n/a'}" for g, w in logo.items()]
    distinct = {tuple(sorted(w.items())) for w in logo.values() if w}
    lines += ["", f"**Stability:** {len(distinct)} distinct fold-winner(s) across "
              f"{len(logo)} folds — "
              f"{'stable' if len(distinct) <= 3 else 'UNSTABLE, do not apply blindly'}."]
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def control(fx=None, report_path=None):
    """The cheap re-measure: baseline, two fixed splits, and the fingerprint.

    Everything the full run does beyond this — the probe, the 21-point sweep,
    the guardrailed grid, the LOGO folds — costs ~7 minutes and answers a
    different question. A control has to be cheap or it will not be run."""
    fx = fx if fx is not None else _Fixture()
    if report_path is None:
        report_path = recommend.DATA_ROOT / "Analysis" / "_calibration.md"
    # Hashed BEFORE anything is evaluated, so the fingerprint describes the
    # inputs as loaded and cannot pick up a scratch field a scorer left behind.
    fingerprint = input_fingerprint(fx)
    baseline = random_core_baseline(fx)
    splits = []
    for e, f in CONTROL_SPLITS:
        _per_god, agg = fx.evaluate({"efficiency": e, "win": 0.0,
                                     "pick": 0.0, "fit": f})
        splits.append({"efficiency": e, "fit": f,
                       "coverage": agg["mean_coverage"]})
    return {"fingerprint": fingerprint,
            "report_fingerprint": report_fingerprint(report_path),
            "report_path": report_path,
            "baseline": baseline["mean"], "splits": splits}


def format_control(c):
    base = c["baseline"]
    lines = [f"input fingerprint      {c['fingerprint']}",
             f"random-core baseline   {base:.1%}"]
    for row in c["splits"]:
        mult = f"{row['coverage'] / base:.1f}x chance" if base else "n/a"
        lines.append(f"eff {row['efficiency']:.2f} : fit {row['fit']:.2f}     "
                     f"{row['coverage']:.1%}   {mult}")
    stamped = c["report_fingerprint"]
    name = c["report_path"].name
    if stamped is None:
        lines.append(f"{name} carries no fingerprint - it predates this check; "
                     "re-run `python -m smite.calibrate` before quoting it")
    elif stamped == c["fingerprint"]:
        lines.append(f"{name} fingerprint {stamped} - MATCHES, its numbers "
                     "describe this data")
    else:
        lines.append(f"{name} fingerprint {stamped} - DIFFERS from this data. "
                     "Its numbers are a control for a different dataset; the "
                     "figures above are the ones to compare against")
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(prog="smite.calibrate")
    parser.add_argument(
        "--control", action="store_true",
        help="print only the leakage-free control: baseline, two fixed "
             "splits and the input fingerprint (~7s). Re-measure this before "
             "comparing anything against a previously quoted control.")
    args = parser.parse_args(argv)
    if args.control:
        print(format_control(control()))
        return 0
    fx = _Fixture()
    fingerprint = input_fingerprint(fx)
    probe = leakage_probe(fx)
    baseline = random_core_baseline(fx)
    model_sweep = model_signal_sweep(fx)
    results = evaluate_grid(fx.items, fx.weights, fx.tags_map, fx.gods,
                            fx.builds_by_god, weight_grid())
    logo = logo_winners(results)
    out = recommend.DATA_ROOT / "Analysis" / "_calibration.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    write_report(results, logo, fx.weights["signals"], out, probe=probe,
                 baseline=baseline, model_sweep=model_sweep,
                 fingerprint=fingerprint)
    best_model = max(model_sweep, key=lambda r: r["coverage"])
    print(f"Wrote {out}")
    print(f"Input fingerprint: {fingerprint}  (compare with `--control`)")
    print(f"Random-core baseline: {baseline['mean']:.1%}")
    for row in probe:
        print(f"  probe  {row['label']:<40} spearman "
              f"{(row['agg']['pooled_spearman'] or 0):+.3f}  "
              f"coverage {row['agg']['mean_coverage']:.1%}")
    print(f"Leakage-free best split: efficiency {best_model['efficiency']:.2f} : "
          f"fit {best_model['fit']:.2f} -> {best_model['coverage']:.1%} "
          f"[{best_model['ci'][0]:.1%}, {best_model['ci'][1]:.1%}]")
    print(f"Guardrailed grid top: {_fmt(results[0]['signals'])} "
          f"objective {results[0]['objective']:.3f} "
          "(frontier position, NOT a recommendation — see report section 1)")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
