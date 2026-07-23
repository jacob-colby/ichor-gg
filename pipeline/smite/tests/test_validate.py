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


def test_check_thresholds_passes_above_both_floors():
    agg = {"mean_win_weighted": 0.70, "pooled_spearman": 0.40, "pooled_n": 10}
    passed, failures = validate.check_thresholds(agg)
    assert (passed, failures) == (True, [])


def test_check_thresholds_fails_low_win_weighted():
    agg = {"mean_win_weighted": 0.50, "pooled_spearman": 0.40, "pooled_n": 10}
    passed, failures = validate.check_thresholds(agg)
    assert passed is False
    assert any("win-weighted" in f for f in failures)


def test_check_thresholds_fails_low_spearman():
    agg = {"mean_win_weighted": 0.70, "pooled_spearman": 0.20, "pooled_n": 10}
    passed, failures = validate.check_thresholds(agg)
    assert passed is False
    assert any("spearman" in f for f in failures)


def test_check_thresholds_fails_none_spearman():
    agg = {"mean_win_weighted": 0.70, "pooled_spearman": None, "pooled_n": 10}
    passed, failures = validate.check_thresholds(agg)
    assert passed is False
    assert any("spearman" in f and "n/a" in f for f in failures)


def test_check_thresholds_fails_both():
    agg = {"mean_win_weighted": 0.50, "pooled_spearman": 0.20, "pooled_n": 10}
    passed, failures = validate.check_thresholds(agg)
    assert passed is False
    assert len(failures) == 2


def test_tag_audit_flags_mismatches():
    items = [
        {"name": "Divine Ruin", "passive": "Reduces enemy Healing by 40%.", "effect_tags": []},
        {"name": "Mystery", "passive": "Grants Attack Speed.", "effect_tags": ["anti-heal"]},
        {"name": "Clean", "passive": "Reduces enemy Healing by 40%.", "effect_tags": ["anti-heal"]},
    ]
    tags_map = {it["name"]: it["effect_tags"] for it in items}
    issues = validate.tag_audit(items, tags_map)
    kinds = {(i["item"], i["kind"], i["tag"]) for i in issues}
    assert ("Divine Ruin", "possible-missing", "anti-heal") in kinds
    assert ("Mystery", "tag-without-evidence", "anti-heal") in kinds
    assert not any(i["item"] == "Clean" for i in issues)
