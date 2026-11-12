"""`build_outcomes`: the statistic on synthetic matches, the filters, and the
import boundary. Nothing here reads the committed store's numbers; they move
every day."""
import ast
import json
import random
from pathlib import Path

import pytest

from smite import aspect_matches as am
from smite import build_outcomes as bo

PIPELINE = Path(__file__).resolve().parents[1]

SIX = ["A", "B", "C", "D", "E", "F"]
OTHERS = ["G", "H", "I", "J", "K", "L"]
TIERS = {n: "3" for n in SIX + OTHERS}
TIERS["Component"] = "2"
NAMES = {n.lower(): n for n in TIERS}


def _record(items, placement=1, aspect=None, role="Mid"):
    return {"m": "0" * 16, "t": "2026-11-05T00:00:00.000Z", "aspect": aspect, "role": role,
            "rank": 5000, "placement": placement, "items": [i and i.lower() for i in items],
            "starter": None, "relic": None, "enemies": []}


def test_a_finished_six_is_six_known_tier_three_items():
    assert bo.finished_six(_record(SIX), NAMES, TIERS) == SIX
    assert bo.finished_six(_record(SIX[:5] + [None]), NAMES, TIERS) is None
    assert bo.finished_six(_record(SIX[:5] + ["Component"]), NAMES, TIERS) is None
    assert bo.finished_six(_record(SIX[:5] + ["Unknown"]), NAMES, TIERS) is None


def test_a_seventh_slot_is_not_read():
    """Vulcan's Aspect of Fortification returns seven or eight slots."""
    assert bo.finished_six(_record(SIX + ["Component"]), NAMES, TIERS) == SIX


def test_the_filters_keep_base_kit_and_the_asked_role():
    records = [_record(SIX), _record(SIX, aspect="aspect-of-x"), _record(SIX, role="Jungle"),
               _record(SIX, placement=None)]
    assert len(bo.god_rows(records, NAMES, TIERS, "Mid", kit="base", role="any")) == 2
    assert len(bo.god_rows(records, NAMES, TIERS, "Mid", kit="any", role="any")) == 3
    assert len(bo.god_rows(records, NAMES, TIERS, "Mid", kit="base", role="primary")) == 1


def _matches(rng, n, base, per_item):
    """`n` matches, each holding a random number of the reference six, winning
    with probability `base + per_item * overlap`."""
    rows = []
    for _ in range(n):
        k = rng.randint(0, 6)
        held = frozenset(SIX[:k] + OTHERS[: 6 - k])
        rows.append((held, 1 if rng.random() < base + per_item * k else 0))
    return rows


def test_a_planted_effect_is_recovered_and_its_interval_excludes_zero():
    rng = random.Random(1)
    parts = [bo.moments(_matches(rng, 400, 0.35, 0.04), frozenset(SIX)) for _ in range(30)]
    slope, low, high = bo.slope_with_interval(parts)
    assert slope == pytest.approx(0.04, abs=0.008)
    assert low > 0 and low < slope < high


def test_no_effect_reads_as_an_interval_that_spans_zero():
    rng = random.Random(2)
    parts = [bo.moments(_matches(rng, 400, 0.5, 0.0), frozenset(SIX)) for _ in range(30)]
    slope, low, high = bo.slope_with_interval(parts)
    assert low < 0 < high and abs(slope) < 0.01


def test_the_slope_is_within_god_so_a_strong_conventional_god_is_not_an_effect():
    """One god always wins and always holds the six; another never does
    either. Pooled naively that is a perfect slope; within god there is no
    variation in overlap at all, so nothing to read."""
    strong = [(frozenset(SIX), 1)] * 50
    weak = [(frozenset(OTHERS), 0)] * 50
    parts = [bo.moments(strong, frozenset(SIX)), bo.moments(weak, frozenset(SIX))]
    assert bo.pooled_slope(parts) == 0.0


def test_one_god_gets_no_interval():
    slope, low, high = bo.slope_with_interval([bo.moments(_matches(random.Random(3), 50, 0.5, 0.0),
                                                          frozenset(SIX))])
    assert low is None and high is None


def test_the_random_reference_sits_at_zero_when_no_item_matters():
    rng = random.Random(4)
    rows_by_god = {f"g{i}": _matches(rng, 300, 0.5, 0.0) for i in range(20)}
    pools = {g: SIX + OTHERS for g in rows_by_god}
    mean, sd = bo.random_reference(rows_by_god, pools, draws=50)
    assert abs(mean) < 0.01 and sd < 0.02


def test_the_feed_spelling_of_brawlers_beat_stick_resolves_to_our_item():
    names = bo.slug_names()
    assert names["brawlers-ruin"] == names["brawlers-beat-stick"]


def test_every_alias_points_at_a_live_item_and_shadows_none():
    plain = am.item_name_lookup()
    for alias, target in bo.SLUG_ALIASES.items():
        assert target in plain and alias not in plain


def test_compute_runs_on_a_small_store(tmp_path):
    """End to end on a store written the way `aspect_matches` writes it."""
    meta = {"division": "obsidian", "aspects": {},
            "windows": {"ob47": {"start": "2026-11-03T00:00:00.000Z", "end": "2026-11-09T00:00:00.000Z"}}}
    am.save_json(tmp_path / am.META_FILE, meta)
    rng = random.Random(5)
    lines = []
    for i in range(60):
        k = rng.randint(0, 6)
        rec = _record(SIX[:k] + OTHERS[: 6 - k], placement=1 if rng.random() < 0.3 + 0.07 * k else 2)
        rec["m"] = f"{i:016x}"
        rec["t"] = f"2026-11-05T{i % 24:02d}:{i:02d}:00.000Z"
        lines.append(json.dumps(rec))
    (tmp_path / "ob47").mkdir()
    (tmp_path / "ob47" / "testgod.jsonl").write_text("\n".join(lines) + "\n", encoding="utf-8")
    items = [{"name": n, "tier": t, "stats": {"Strength": "10"}, "cost": 2500} for n, t in TIERS.items()]
    god = {"name": "Testgod", "role": "Mid", "damage_type": "physical"}
    note = {"builds": [{"source": "suggested", "archetype": "model", "slot_order": SIX},
                       {"source": "suggested", "archetype": "core", "slot_order": SIX}]}
    out = bo.compute(items, [god], {}, {"Testgod": note}, root=tmp_path, names=NAMES)
    assert out["matches"] == 60 and out["gods"] == 1 and out["windows"] == ["ob47"]
    assert out["table"]["model"]["slope"] > 0
    assert out["table"]["model"]["low"] is None            # one god: no interval
    assert out["table"]["community"]["gods"] == 0          # no community entry in the note
    assert bo.table_lines(out)[0].startswith("**Windows ob47")


def test_nothing_in_the_model_imports_this():
    for mod in ("scoring", "assemble", "recommend", "build_index", "efficiency"):
        tree = ast.parse((PIPELINE / f"{mod}.py").read_text(encoding="utf-8"))
        names = {a.name for n in ast.walk(tree) if isinstance(n, (ast.Import, ast.ImportFrom))
                 for a in n.names}
        assert not names & {"build_outcomes", "smite.build_outcomes"}
