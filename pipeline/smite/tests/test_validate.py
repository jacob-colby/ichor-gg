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
