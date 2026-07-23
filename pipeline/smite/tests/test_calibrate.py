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


def test_objective_blends_spearman_and_coverage():
    perfect = {"pooled_spearman": 1.0, "mean_coverage": 1.0}
    useless = {"pooled_spearman": None, "mean_coverage": 0.0}
    assert calibrate.objective(perfect) == 1.0
    assert calibrate.objective(useless) == 0.25   # (0+1)/2 * 0.5 + 0
    assert calibrate.objective(perfect) > calibrate.objective(
        {"pooled_spearman": 0.3, "mean_coverage": 0.6})
