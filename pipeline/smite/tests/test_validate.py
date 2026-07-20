from smite import validate


def test_coverage():
    assert validate.coverage(["A", "B", "C"], ["A", "B", "X"]) == 2 / 3
    assert validate.coverage([], []) == 0.0


def test_win_weighted_coverage():
    community = [{"name": "A", "win_rate": 0.6}, {"name": "B", "win_rate": 0.5}, {"name": "C", "win_rate": 0.5}]
    assert abs(validate.win_weighted_coverage(["A"], community) - 0.6 / 1.6) < 1e-9
    assert validate.win_weighted_coverage([], []) == 0.0


def test_spearman_monotonic():
    assert abs(validate.spearman([1, 2, 3, 4], [10, 20, 30, 40]) - 1.0) < 1e-9
    assert abs(validate.spearman([1, 2, 3, 4], [40, 30, 20, 10]) + 1.0) < 1e-9
    assert validate.spearman([1], [1]) is None


def test_aggregate_summarizes_per_god():
    per_god = {
        "A": {"coverage": 1.0, "win_weighted": 1.0, "pairs": [(3, 0.6), (2, 0.5), (1, 0.4)]},
        "B": {"coverage": 0.5, "win_weighted": 0.5, "pairs": [(1, 0.4), (2, 0.5)]},
    }
    agg = validate.aggregate(per_god)
    assert abs(agg["mean_coverage"] - 0.75) < 1e-9
    assert abs(agg["mean_win_weighted"] - 0.75) < 1e-9
    assert agg["pooled_spearman"] is not None
