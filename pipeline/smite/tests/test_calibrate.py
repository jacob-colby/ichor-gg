import math

import pytest

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


@pytest.fixture
def stub_baseline(monkeypatch):
    """`control` measures the baseline off the real 226-item pool. These tests
    are about the control's SHAPE — the fixed splits, the fingerprint, the
    stale-report line — so the measurement is stubbed and the timing stays in
    milliseconds."""
    monkeypatch.setattr(calibrate, "random_core_baseline",
                        lambda fx, **kw: fx.random_core_baseline())


class _StubFixture:
    """Enough of `_Fixture` for the fingerprint and the control.

    `control` is exercised against a stub rather than the real data because the
    real thing loads 226 item notes and 89 gods, and a control that costs a
    test-suite-visible five seconds would get marked slow and skipped."""

    def __init__(self, items=None, gods=None, tags_map=None, builds_by_god=None,
                 weights=None, coverage=0.30):
        self.items = items if items is not None else [{"name": "Deathbringer",
                                                       "cost": 3000}]
        self.gods = gods if gods is not None else [{"name": "Ullr"}]
        self.tags_map = tags_map if tags_map is not None else {"Deathbringer": ["crit"]}
        self.builds_by_god = builds_by_god if builds_by_god is not None else {
            "Ullr": {"builds": [{"source": "community",
                                 "slot_order": [{"name": "Deathbringer",
                                                 "win_rate": 0.55}]}]}}
        self.weights = weights if weights is not None else {
            "signals": {"efficiency": 0.35, "win": 0.30, "pick": 0.15, "fit": 0.20}}
        self._coverage = coverage
        self.seen = []

    def random_core_baseline(self, _fx=None, **_kw):
        return {"mean": 0.057, "per_god": {}, "pool_median": 99}

    def evaluate(self, signals):
        self.seen.append(dict(signals))
        return {}, {"mean_coverage": self._coverage, "mean_win_weighted": 0.0,
                    "pooled_spearman": None, "pooled_n": 0}


def test_fingerprint_is_stable_across_dict_and_file_ordering():
    """Two loads of the same data must fingerprint identically, or the check
    cries wolf on every run and gets ignored."""
    a = _StubFixture()
    b = _StubFixture(weights={"signals": {"fit": 0.20, "pick": 0.15,
                                          "win": 0.30, "efficiency": 0.35}})
    assert calibrate.input_fingerprint(a) == calibrate.input_fingerprint(b)


def test_fingerprint_moves_when_any_control_input_moves():
    base = calibrate.input_fingerprint(_StubFixture())
    moved = {
        "items": _StubFixture(items=[{"name": "Deathbringer", "cost": 3100}]),
        "gods": _StubFixture(gods=[{"name": "Ullr"}, {"name": "Ares"}]),
        "tags": _StubFixture(tags_map={"Deathbringer": ["crit", "burst"]}),
        "community": _StubFixture(builds_by_god={
            "Ullr": {"builds": [{"source": "community",
                                 "slot_order": [{"name": "Deathbringer",
                                                 "win_rate": 0.61}]}]}}),
        "weights": _StubFixture(weights={"signals": {"efficiency": 0.40, "win": 0.30,
                                                     "pick": 0.15, "fit": 0.15}}),
    }
    for label, fx in moved.items():
        assert calibrate.input_fingerprint(fx) != base, label


def test_fingerprint_ignores_our_own_generated_builds():
    """Only the COMMUNITY half of a build note is data. Hashing the suggested
    builds too would make `recommend` moving a core read as the dataset
    changing, which is the exact confusion the fingerprint exists to end."""
    base = _StubFixture()
    with_ours = _StubFixture(builds_by_god={
        "Ullr": {"builds": [{"source": "community",
                             "slot_order": [{"name": "Deathbringer",
                                             "win_rate": 0.55}]},
                            {"source": "model", "flavor": "core",
                             "items": ["Transcendence"]}]}})
    assert calibrate.input_fingerprint(base) == calibrate.input_fingerprint(with_ours)


def test_control_uses_fixed_splits_not_the_sweep_argmax(stub_baseline):
    """The whole point is a number two runs can be compared on."""
    fx = _StubFixture()
    calibrate.control(fx, report_path=calibrate.recommend.DATA_ROOT / "nope.md")
    assert [(s["efficiency"], s["fit"]) for s in fx.seen] == list(calibrate.CONTROL_SPLITS)
    for signals in fx.seen:
        assert signals["win"] == 0.0 and signals["pick"] == 0.0   # leakage-free


def test_control_reports_a_missing_report_rather_than_raising(tmp_path, stub_baseline):
    c = calibrate.control(_StubFixture(), report_path=tmp_path / "absent.md")
    assert c["report_fingerprint"] is None
    assert "carries no fingerprint" in calibrate.format_control(c)


def test_control_says_plainly_when_the_report_is_stale(tmp_path, stub_baseline):
    fx = _StubFixture()
    report = tmp_path / "_calibration.md"
    report.write_text("# Signal-weight calibration\n\n"
                      "_Input fingerprint: `deadbeef1234` — items._\n", encoding="utf-8")
    text = calibrate.format_control(calibrate.control(fx, report_path=report))
    assert "DIFFERS" in text
    assert "deadbeef1234" in text
    assert calibrate.input_fingerprint(fx) in text


def test_control_says_plainly_when_the_report_is_current(tmp_path, stub_baseline):
    fx = _StubFixture()
    report = tmp_path / "_calibration.md"
    report.write_text("_Input fingerprint: `%s` — items._\n"
                      % calibrate.input_fingerprint(fx), encoding="utf-8")
    assert "MATCHES" in calibrate.format_control(calibrate.control(fx, report_path=report))


def test_control_output_is_ascii(stub_baseline):
    """This text gets pasted into session prompts and read on a cp1252 console;
    an em dash there is a crash, not a typo."""
    c = calibrate.control(_StubFixture(), report_path=calibrate.recommend.DATA_ROOT / "nope.md")
    calibrate.format_control(c).encode("ascii")


def test_control_states_the_baseline_and_both_splits(stub_baseline):
    c = calibrate.control(_StubFixture(coverage=0.30),
                          report_path=calibrate.recommend.DATA_ROOT / "nope.md")
    text = calibrate.format_control(c)
    assert "random-core baseline" in text
    assert "eff 0.70 : fit 0.30" in text
    assert "eff 0.45 : fit 0.55" in text
    assert "x chance" in text                 # never a bare percentage


def test_full_report_stamps_the_fingerprint(tmp_path):
    current = {"efficiency": 0.35, "win": 0.45, "pick": 0.05, "fit": 0.15}
    results = [{"signals": dict(current),
                "agg": {"pooled_spearman": None, "mean_coverage": 0.0},
                "per_god": {}, "objective": 0.25}]
    out = tmp_path / "cal.md"
    calibrate.write_report(results, {}, current, out, fingerprint="c0ffee123456")
    assert calibrate.report_fingerprint(out) == "c0ffee123456"
def test_the_exact_baseline_is_what_the_sampler_estimates():
    """A fixed seed and a pool the model reorders means the printed baseline
    moves when nothing about chance did. The closed form must agree with the
    sampler in the limit — same pools, same answer, no draws."""
    import random

    # Two gods, pools of 10 and 20, four community items each. The closed form
    # is min(6, N)/N averaged over gods: (0.6 + 0.3)/2 = 0.45.
    exact = calibrate._mean([min(6, n) / n for n in (10, 20)])
    assert exact == pytest.approx(0.45)

    rng = random.Random(1)
    community = set(range(4))
    est = [calibrate._mean(
        [len(set(rng.sample(range(n), 6)) & community) / len(community)
         for _ in range(20000)]) for n in (10, 20)]
    assert calibrate._mean(est) == pytest.approx(exact, abs=0.01)


def test_the_exact_baseline_walks_the_same_pool_the_sampler_does():
    """Both read `score_god_items` under the Conquest profile and skip the same
    gods, so a divergence would mean they are baselining different things."""
    import inspect
    exact = inspect.getsource(calibrate.exact_random_core_baseline)
    sampled = inspect.getsource(calibrate.random_core_baseline)
    for shared in ("score_god_items", "_community_slots",
                   'c.get("win_rate") is not None', "resolve_profile"):
        assert shared in exact and shared in sampled
