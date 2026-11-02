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


# Explicit floors keep these logic tests independent of the production defaults
# (which shift as the roster/meta changes); test_check_thresholds_default_floors
# pins the current production values separately.

def test_check_thresholds_passes_above_both_floors():
    agg = {"mean_win_weighted": 0.70, "pooled_spearman": 0.40, "pooled_n": 10}
    passed, failures = validate.check_thresholds(agg, 0.44, 0.30)
    assert (passed, failures) == (True, [])


def test_check_thresholds_fails_low_win_weighted():
    agg = {"mean_win_weighted": 0.30, "pooled_spearman": 0.40, "pooled_n": 10}
    passed, failures = validate.check_thresholds(agg, 0.44, 0.30)
    assert passed is False
    assert any("win-weighted" in f for f in failures)


def test_check_thresholds_fails_low_spearman():
    agg = {"mean_win_weighted": 0.70, "pooled_spearman": 0.20, "pooled_n": 10}
    passed, failures = validate.check_thresholds(agg, 0.44, 0.30)
    assert passed is False
    assert any("spearman" in f for f in failures)


def test_check_thresholds_fails_none_spearman():
    agg = {"mean_win_weighted": 0.70, "pooled_spearman": None, "pooled_n": 10}
    passed, failures = validate.check_thresholds(agg, 0.44, 0.30)
    assert passed is False
    assert any("spearman" in f and "n/a" in f for f in failures)


def test_check_thresholds_fails_both():
    agg = {"mean_win_weighted": 0.30, "pooled_spearman": 0.20, "pooled_n": 10}
    passed, failures = validate.check_thresholds(agg, 0.44, 0.30)
    assert passed is False
    assert len(failures) == 2


def test_check_thresholds_default_floors():
    # Pin the production defaults: win-weighted 0.44; Spearman 0.30 early in
    # SmiteBrain's window (and when its age is unknown), 0.20 from day 8.
    at_floor = {"mean_win_weighted": 0.44, "pooled_spearman": 0.30, "pooled_n": 10}
    assert validate.check_thresholds(at_floor) == (True, [])
    below = {"mean_win_weighted": 0.43, "pooled_spearman": 0.29, "pooled_n": 10}
    passed, failures = validate.check_thresholds(below)
    assert passed is False and len(failures) == 2


def _agg(spearman, age):
    return {"mean_win_weighted": 0.50, "pooled_spearman": spearman,
            "pooled_n": 439, "window_age_days": age}


def test_spearman_floor_early_window_fails_below_030():
    passed, failures = validate.check_thresholds(_agg(0.28, 5))
    assert passed is False and failures == ["spearman 0.28 < 0.3"]


def test_spearman_floor_late_window_passes_at_028():
    # 2026-10-31 / 11-01: day 11 and 12 of the 10-20 window, clean scrapes.
    assert validate.check_thresholds(_agg(0.28, 11)) == (True, [])


def test_spearman_floor_late_window_fails_below_relaxed_floor():
    passed, failures = validate.check_thresholds(_agg(0.19, 12))
    assert passed is False and failures == ["spearman 0.19 < 0.2"]


def test_spearman_floor_boundary_and_unknown_age():
    assert validate.spearman_floor(7)[0] == 0.30
    assert validate.spearman_floor(8)[0] == 0.20
    assert validate.spearman_floor(None)[0] == 0.30
    assert validate.check_thresholds(_agg(0.28, None))[0] is False


def test_spearman_none_fails_late_window():
    passed, failures = validate.check_thresholds(_agg(None, 12))
    assert passed is False and any("n/a" in f for f in failures)


def test_window_age_days_takes_most_common_window():
    def note(start, end):
        return {"builds": [{"source": "community", "god_window_start": start,
                            "god_window_end": end}]}
    builds = {"A": note("2026-10-20", "2026-10-31"), "B": note("2026-10-20", "2026-10-31"),
              "C": note("2026-10-06", "2026-10-31"), "D": {"builds": []}}
    assert validate.window_age_days(builds) == 11
    assert validate.window_age_days({"D": {"builds": []}}) is None


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
