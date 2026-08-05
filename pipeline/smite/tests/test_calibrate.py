import math

from smite import calibrate


def test_weight_grid_respects_guardrails():
    grid = calibrate.weight_grid(step=0.05)
    assert grid, "grid must not be empty"
    for g in grid:
        total = g["efficiency"] + g["win"] + g["pick"] + g["fit"]
        assert abs(total - 1.0) < 1e-9
        assert g["pick"] <= 0.15 + 1e-9                      # popularity capped
        assert g["efficiency"] + g["fit"] >= 0.50 - 1e-9     # intrinsic quality floor
    # The current hand weights satisfy the guardrails and must be in the grid.
    assert {"efficiency": 0.35, "win": 0.30, "pick": 0.15, "fit": 0.20} in grid


def test_guardrails_exclude_the_degenerate_corners():
    """The leakage probe's corners must be unreachable by the grid.

    This is the guardrails' real job — not expressing a prior, but keeping the
    search away from `win only` and `pick only`, which beat every honest blend
    on the objective while containing no model at all."""
    grid = calibrate.weight_grid(step=0.05)
    for corner in ({"efficiency": 0.0, "win": 1.0, "pick": 0.0, "fit": 0.0},
                   {"efficiency": 0.0, "win": 0.0, "pick": 1.0, "fit": 0.0}):
        assert corner not in grid


def test_objective_blends_spearman_and_coverage():
    perfect = {"pooled_spearman": 1.0, "mean_coverage": 1.0}
    useless = {"pooled_spearman": None, "mean_coverage": 0.0}
    assert calibrate.objective(perfect) == 1.0
    assert calibrate.objective(useless) == 0.25   # (0+1)/2 * 0.5 + 0
    assert calibrate.objective(perfect) > calibrate.objective(
        {"pooled_spearman": 0.3, "mean_coverage": 0.6})


def test_within_god_spearman_is_not_pooled():
    """Two gods, each internally ranked backwards, but whose score ranges make
    the POOLED correlation look perfect. Pooling hides the failure; correlating
    inside each god exposes it."""
    # Four gods on separated score/win-rate levels. Between-god variance
    # dominates the pooled statistic; every god is internally backwards.
    per_god = {
        name: {"pairs": [(base + 0.01, wr + 0.02),
                         (base + 0.02, wr + 0.01),
                         (base + 0.03, wr + 0.00)]}
        for name, base, wr in [("Weakest", 0.1, 0.40), ("Weak", 0.3, 0.45),
                               ("Strong", 0.5, 0.50), ("Strongest", 0.7, 0.55)]
    }
    pooled = calibrate.validate.spearman(
        [x for m in per_god.values() for x, _ in m["pairs"]],
        [y for m in per_god.values() for _, y in m["pairs"]])
    assert pooled > 0.8                       # looks excellent
    wg = calibrate.within_god_spearman(per_god)
    assert wg["mean"] == -1.0                 # is in fact exactly backwards
    assert wg["positive"] == 0
    assert wg["n"] == 4


def test_within_god_spearman_skips_thin_gods():
    per_god = {"Thin": {"pairs": [(0.1, 0.5), (0.2, 0.6)]}}
    assert calibrate.within_god_spearman(per_god, min_items=3)["n"] == 0


def test_bootstrap_ci_brackets_the_mean_and_is_deterministic():
    values = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0] * 12
    lo, hi = calibrate.bootstrap_ci(values, resamples=500)
    mean = sum(values) / len(values)
    assert lo < mean < hi
    assert (lo, hi) == calibrate.bootstrap_ci(values, resamples=500)


def test_bootstrap_ci_widens_as_the_sample_shrinks():
    """The CI is the whole point of the leakage-free sweep — a narrow band on
    87 gods and a wide one on 8 must not report the same confidence."""
    spread = [0.0, 0.25, 0.5, 0.75, 1.0]
    wide = calibrate.bootstrap_ci(spread * 2, resamples=500)
    narrow = calibrate.bootstrap_ci(spread * 40, resamples=500)
    assert (wide[1] - wide[0]) > (narrow[1] - narrow[0])


def test_bootstrap_ci_handles_no_values():
    assert calibrate.bootstrap_ci([]) == (0.0, 0.0)


def test_report_names_the_current_weights_and_the_leakage_warning(tmp_path):
    current = {"efficiency": 0.35, "win": 0.45, "pick": 0.05, "fit": 0.15}
    results = [{"signals": dict(current),
                "agg": {"pooled_spearman": 0.55, "mean_coverage": 0.51},
                "per_god": {}, "objective": 0.643}]
    probe = [{"label": "win only (Spearman's target verbatim)",
              "signals": {"efficiency": 0.0, "win": 1.0, "pick": 0.0, "fit": 0.0},
              "agg": {"pooled_spearman": 1.0, "mean_coverage": 0.699},
              "within_god": {"mean": 0.89, "median": 0.97, "positive": 85, "n": 85}}]
    baseline = {"mean": 0.065, "per_god": {}, "pool_median": 92}
    sweep = [{"efficiency": 0.30, "fit": 0.70, "coverage": 0.295, "ci": (0.253, 0.338)},
             {"efficiency": 0.70, "fit": 0.30, "coverage": 0.278, "ci": (0.232, 0.323)}]
    out = tmp_path / "cal.md"
    calibrate.write_report(results, {}, current, out, probe=probe,
                           baseline=baseline, model_sweep=sweep)
    text = out.read_text(encoding="utf-8")
    assert "Leakage probe" in text
    assert "←current" in text                      # the shipped point is findable
    assert "6.5%" in text                          # chance is stated, not implied
    assert "2 of 2 splits have a CI overlapping" in text   # noise is called noise
    assert "NOT a recommendation" not in text      # that line belongs to stdout
    assert "trade-off frontier, not a winner" in text


def test_report_survives_missing_optional_sections(tmp_path):
    """`write_report` is called from tests and ad-hoc scripts without the
    expensive probe/baseline; it must degrade rather than raise."""
    current = {"efficiency": 0.35, "win": 0.45, "pick": 0.05, "fit": 0.15}
    results = [{"signals": dict(current),
                "agg": {"pooled_spearman": None, "mean_coverage": 0.0},
                "per_god": {}, "objective": 0.25}]
    out = tmp_path / "bare.md"
    calibrate.write_report(results, {}, current, out)
    assert "Signal-weight calibration" in out.read_text(encoding="utf-8")
