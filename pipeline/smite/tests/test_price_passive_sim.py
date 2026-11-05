"""`price_passive_sim` — the flag that prices an item's passive from its
simulated value (option (a), register §4.31 / §4.32).

These pin the four things that would be silent if they broke: the flag is a
no-op at OFF, the columns it adds are the three §4.17 allows, the simulated
value SUPERSEDES the flag-derived grant for the eight dual-priced items, and a
refused passive is an explicit zero rather than a gap.
"""
import pytest

from smite import efficiency, recommend


@pytest.fixture(autouse=True)
def _flags_off():
    """Every test here sets the flag itself. The autouse fixture guarantees the
    module goes back, because `apply_pricing_flags` writes globals and a leaked
    ON would change every later test's fit without failing anything."""
    before = efficiency.apply_pricing_flags({})
    yield
    efficiency.restore_pricing_flags(before)


def _stats(item, **flags):
    """The FIT's view of one item under these flags."""
    before = efficiency.apply_pricing_flags(flags)
    try:
        return efficiency.regression_columns(item)
    finally:
        efficiency.restore_pricing_flags(before)


def _effective(item, **flags):
    """An item's EFFECTIVE STATS under these flags — what `build_quality` and
    `damage_value` feed to damage arithmetic."""
    before = efficiency.apply_pricing_flags(flags)
    try:
        return efficiency.item_stat_values(item)
    finally:
        efficiency.restore_pricing_flags(before)


@pytest.fixture(scope="module")
def items():
    return recommend.load_items()


@pytest.fixture(scope="module")
def by_name(items):
    return {i["name"]: i for i in items}


def test_off_is_a_no_op(by_name):
    """Not "roughly the same" — the identical dict. A flag whose OFF arm moves
    anything cannot be measured against its own control."""
    item = by_name["Deathbringer"]
    assert _stats(item) == _stats(item, price_passive_sim=False)


def test_on_adds_exactly_the_three_columns(by_name):
    item = by_name["Deathbringer"]
    off = _stats(item)
    on = _stats(item, price_passive_sim=True)
    added = set(on) - set(off)
    assert added <= set(efficiency.PASSIVE_SIM_COLUMNS)
    assert "Passive Damage" in added, "Deathbringer's passive is simulated and damaging"


def test_the_two_effective_health_channels_stay_apart():
    """Register §4.17 refuses to collapse them and says what the pair bounds
    instead. A single `Passive EHP` column would be that refusal ignored
    somewhere nobody would look for it."""
    assert "Passive EHP Physical" in efficiency.PASSIVE_SIM_COLUMNS
    assert "Passive EHP Magical" in efficiency.PASSIVE_SIM_COLUMNS
    assert not any(c == "Passive EHP" for c in efficiency.PASSIVE_SIM_COLUMNS)


def test_a_refused_passive_is_an_explicit_zero(by_name):
    """Tekko-Kagi's whole passive is +7% Pathfinding and `passive_sim` refuses
    it under ("no movement",) — §4.30. It must contribute nothing, and the file
    must SAY so rather than omit the item."""
    row = efficiency.passive_sim_values()["Tekko-Kagi"]
    assert row["status"] == "refused"
    assert row["passive_damage"] == 0.0
    on = _stats(by_name["Tekko-Kagi"], price_passive_sim=True)
    assert not any(c in on for c in efficiency.PASSIVE_SIM_COLUMNS)


def test_every_scored_item_is_in_the_file(items):
    """A missing key must be a stale file, not a zero. The generator writes
    every item in `efficiency_pool`, so absence is a bug and this is what says
    so when the pool grows and nobody regenerates."""
    values = efficiency.passive_sim_values()
    missing = sorted(i["name"] for i in efficiency.efficiency_pool(items)
                     if i["name"] not in values)
    assert not missing, f"regenerate data/_passive_values.yaml; missing: {missing[:8]}"


def test_simulated_value_supersedes_the_flag_derived_grant(by_name):
    """THE DOUBLE COUNT, and the one correctness risk §4.32 named.

    The Executioner's adaptive +30 Strength is already in its stat columns via
    `price_adaptive`, while `passive_contribution` switches the WHOLE passive
    off — so its simulated number already contains that grant. With both flags
    on, the adaptive grant must be gone from the stat columns."""
    item = by_name["The Executioner"]
    adaptive_only = _stats(item, price_adaptive=True)
    both = _stats(item, price_adaptive=True, price_passive_sim=True)
    printed = _stats(item)
    # `price_adaptive` adds something on its own...
    assert adaptive_only != printed
    # ...and that something is not also present once the simulated value is.
    for key, val in adaptive_only.items():
        if key in printed:
            continue
        assert key not in both, f"{key} double counted on The Executioner"
    assert "Passive Damage" in both


def test_supersede_set_only_names_items_that_are_both(by_name):
    """An item in the supersede set that is NOT flag-priced would have its
    printed stats rebuilt for no reason; one that is not simulated would lose
    its grant and gain nothing. Either way the set has drifted from the code."""
    values = efficiency.passive_sim_values()
    for name in efficiency.PASSIVE_SIM_SUPERSEDES:
        assert name in by_name, f"{name} is not an item any more"
        row = values.get(name)
        assert row is not None and row["status"] in ("simulated", "partial"), \
            f"{name} is in the supersede set but passive_sim does not value it"


def test_a_negative_measured_passive_is_clamped_not_credited():
    """Nine items measured negative in some build — a timing interaction, not a
    refund. A negative column would read as "this item should cost less", which
    is a credit for a passive that did nothing."""
    values = efficiency.passive_sim_values()
    for name, row in values.items():
        for col in ("passive_damage", "passive_ehp_physical", "passive_ehp_magical"):
            assert (row.get(col) or 0.0) >= 0.0 or row.get(f"{col}_min") is not None, \
                f"{name} carries a negative median with no spread recorded"
    # and the clamp itself
    fake = {"name": "__probe__", "stats": {"Strength": "10"}}
    before = efficiency.apply_pricing_flags({"price_passive_sim": True})
    try:
        efficiency._PASSIVE_VALUES = dict(values)
        efficiency._PASSIVE_VALUES["__probe__"] = {
            "status": "simulated", "n": 3, "passive_damage": -50.0,
            "passive_ehp_physical": 0.0, "passive_ehp_magical": 0.0}
        out = efficiency.regression_columns(fake)
        assert "Passive Damage" not in out
    finally:
        efficiency.restore_pricing_flags(before)
        efficiency._PASSIVE_VALUES = None


def test_effective_stats_never_see_the_flag(by_name):
    """THE DEFECT THIS FLAG SHIPPED WITH FOR ONE DAY, pinned.

    `item_stat_values` is read two ways: the regression wants columns, and
    `build_quality`, `damage_value` and `new_entities` read it as an item's
    effective stats. The first version of this flag added its columns there,
    which (a) handed damage arithmetic a "stat" called Passive Damage and (b)
    let the supersede rule delete The Executioner's real adaptive +30 Strength
    from a build's totals. Green at OFF, wrong at ON, and found only when the
    flag was first turned on — by `test_priced_run_restores_the_pricing_flags`.
    """
    for name in ("The Executioner", "Deathbringer", "Tekko-Kagi"):
        item = by_name[name]
        off = _effective(item, price_adaptive=True)
        on = _effective(item, price_adaptive=True, price_passive_sim=True)
        assert on == off, f"{name}: effective stats moved with price_passive_sim"
        assert not any(c in on for c in efficiency.PASSIVE_SIM_COLUMNS)


def test_passive_columns_are_charged_as_off_map_and_that_is_the_rule(by_name, items):
    """`offmap_efficiency` charges gold spent on columns no role map names, and
    no map names the passive columns — so they are charged. That is the
    exemption rule applied, not an accident: test (ii) asks whether any
    instrument here can price the stat, and `passive_sim` is that instrument.
    If someone exempts them, this fails and sends them to the two measured
    arms under `price_passive_sim` in _weights.yaml."""
    before = efficiency.apply_pricing_flags({"price_passive_sim": True})
    try:
        eff, _ = efficiency.efficiency_scores(items)
        row = eff["Deathbringer"]
        assert row["stat_gold"].get("Passive Damage", 0.0) > 0
        role_map = {"Strength": 1.0}
        with_passive = efficiency.offmap_gold(row, role_map)
        stripped = dict(row, stat_gold={k: v for k, v in row["stat_gold"].items()
                                        if k not in efficiency.PASSIVE_SIM_COLUMNS})
        assert with_passive > efficiency.offmap_gold(stripped, role_map)
    finally:
        efficiency.restore_pricing_flags(before)
