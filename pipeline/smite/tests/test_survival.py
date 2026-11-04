"""The side-by-side's SURVIVAL block (2026-11-04): survival is measured so
that killing faster can never score as worse survival.

Hand-computed off the TOY god (81 a swing at 100% Strength, 1.0 swings/s,
2000 health, no protection), the way `test_fight.py` and `test_healing.py`
are, plus one property checked on the frozen reference builds.
"""
import pytest

from smite import model_audit as ma, side_by_side as sbs
from smite.tests.test_fight import armed, text
from smite.tests.test_side_by_side import item, target, toy_god


def _ehp(names, items, tg):
    return sbs.fight_ehp(toy_god(), names, items, {"squishy": tg})[:2]


# ── The rule, by hand ─────────────────────────────────────────────────────

def test_survival_lifesteal_drips_at_the_fights_capped_damage_rate():
    # The pre-run (one 10s window): swings at t = 0..9 deal 10 x 81 = 810,
    # under the target's 2000 health, so 81 a second is stealable and 10%
    # lifesteal heals 8.1 a second. The enemy hits 100 at t = 0, 1, 2 ...
    # and each hit first credits the time since the last. After the hit at
    # t = n the bar holds 2000 - 100 (n + 1) + 8.1 n, which reaches zero at
    # n = 1900 / 91.9 = 20.7: the hit at t = 21 kills, after 21 credits.
    items = {"LS": item("LS", stats={"Strength": "0", "Lifesteal": "10%"})}
    tg = armed(target(), phys_dps=100.0)
    s = sbs.Sim(toy_god(), ["LS"], items, tg, window=sbs.EHP_RUN_CAP, enemy="physical",
                takedowns=True, survival=81.0)
    s.run_window(until_dead=True)
    assert s.heal_by_item["Lifesteal"] == pytest.approx(8.1 * 21)
    assert _ehp(["LS"], items, tg)[0] == pytest.approx(2000 + 8.1 * 21)


def test_a_fight_holds_one_targets_health_to_steal_from():
    # A 400-health target: the window deals 810, but a fight holds one god's
    # 400 health, so 40 a second is stealable and 10% heals 4.0 a second —
    # spread over the fight, not front-loaded into the 4s it takes to kill.
    # Zero at 96 n = 1900, n = 19.8: 20 credits.
    items = {"LS": item("LS", stats={"Strength": "0", "Lifesteal": "10%"})}
    assert _ehp(["LS"], items, armed(target(base_health=400.0), phys_dps=100.0))[0] \
        == pytest.approx(2000 + 4.0 * 20)


def test_a_takedown_heal_is_held_until_the_bar_reaches_zero():
    assert "Kill a God: Heal +15% of Slain God's Max Health" in text("The Reaper")
    # 400-health target, killed on the fifth swing of each fight (t = 4 and
    # t = 14); the enemy hits 100 at t = 0, 1, 2 ... with no lifesteal.
    # The Reaper's 15% x 400 = 60 per kill and 7.5% = 30 per assist (t = 5,
    # 15) are HELD: 180 in all. The hit at t = 19 takes the bar to zero, the
    # 180 lands, and the hits at t = 20 and 21 take it. Absorbed 2000 + 180 —
    # what an instant heal gives whenever it is not wasted on a full bar.
    items = {"The Reaper": item("The Reaper", {"Strength": "0"})}
    tg = armed(target(base_health=400.0), phys_dps=100.0)
    s = sbs.Sim(toy_god(), ["The Reaper"], items, tg, window=sbs.EHP_RUN_CAP, enemy="physical",
                takedowns=True, survival=0.0)
    s.run_window(until_dead=True)
    assert s.kill_times == [4.0, 14.0] and s.kills == 2
    assert s.heal_by_item["The Reaper"] == pytest.approx(180.0)
    assert _ehp(["The Reaper"], items, tg)[0] == pytest.approx(2180.0)


def test_a_kill_at_full_health_is_not_wasted():
    # A 50-health target dies to each fight's first swing (t = 0, 10, 20),
    # before the enemy's hit at the same instant: the old rule landed the
    # first kill's 15% x 50 = 7.5 on a full bar and lost it. Held, every
    # heal lands: kills at 0 and 10 (15.0) and assists at 5 and 15 (2 x 3.75)
    # are spent when the hit at t = 19 empties the bar; the kill at t = 20
    # adds 7.5 more before that instant's hit. 30 in all.
    items = {"The Reaper": item("The Reaper", {"Strength": "0"})}
    tg = armed(target(base_health=50.0), phys_dps=100.0)
    s = sbs.Sim(toy_god(), ["The Reaper"], items, tg, window=sbs.EHP_RUN_CAP, enemy="physical",
                takedowns=True, survival=0.0)
    s.run_window(until_dead=True)
    assert s.kill_times[:3] == [0.0, 10.0, 20.0]
    assert s.heal_by_item["The Reaper"] == pytest.approx(30.0)
    assert _ehp(["The Reaper"], items, tg)[0] == pytest.approx(2030.0)


def test_a_kills_refund_lands_at_the_end_of_its_fight_whenever_the_kill_did():
    assert "-1s Cooldown for Non-Ultimate Abilities" in text("Jotunn's Revenge")
    # A 6s ability cast at t = 0; the assist at t = 5 refunds 1s, so it is
    # recast at 5 and due at 11. A kill's refund lands at the end of its
    # fight, t = 10, whether the kill came early (400 health) or late (700),
    # and pulls the recast to 10. No kill, no refund: 11.
    from smite.tests.test_side_by_side import toy_ability
    god = toy_god([toy_ability(cooldown=6)])
    items = {"Jotunn's Revenge": item("Jotunn's Revenge", {"Strength": "0"})}

    def casts(health):
        s = sbs.Sim(god, ["Jotunn's Revenge"], items, armed(target(base_health=health), phys_dps=50.0),
                    window=12.0, enemy="physical", takedowns=True, survival=0.0)
        s.run_window()
        return [t for t, _ in s.casts], s.kill_times
    (early, k_early), (late, k_late) = casts(400.0), casts(700.0)
    assert len(k_early) == len(k_late) == 1 and k_early[0] < k_late[0] < 10.0
    assert early == late == [0.0, 5.0, 10.0]
    assert casts(1e6) == ([0.0, 5.0, 11.0], [])


def test_the_damage_axis_keeps_the_kill_rule():
    # Outside the survival run nothing changed: a kill is booked the instant
    # it happens and lifesteal stops on the corpse (test_healing covers it).
    s = sbs.Sim(toy_god(), [], {}, target(base_health=400.0))
    s.run_window()
    assert s.kill_times == [4.0] and s.kills == 1


# ── The property ──────────────────────────────────────────────────────────

def _monotone_in_strength(survival_on):
    """fight EHP of one lifesteal + kill-heal item as its Strength climbs."""
    saved, sbs.SURVIVAL = sbs.SURVIVAL, survival_on
    try:
        tg = armed(target(base_health=1200.0), phys_dps=250.0, mag_dps=250.0)
        out = []
        for strength in (0, 40, 80, 160, 320, 640):
            items = {"X": item("X", stats={"Strength": str(strength), "Lifesteal": "15%"}),
                     "The Reaper": item("The Reaper", {"Strength": "0"})}
            out.append(_ehp(["X", "The Reaper"], items, tg))
        return out
    finally:
        sbs.SURVIVAL = saved


def test_more_damage_never_lowers_survival_toy():
    figs = _monotone_in_strength(True)
    for a, b in zip(figs, figs[1:]):
        assert b[0] >= a[0] - 1e-6 and b[1] >= a[1] - 1e-6, figs


def test_the_old_kill_rule_fails_the_same_check():
    """Teeth: the rule this block replaced lowers survival as damage rises."""
    figs = _monotone_in_strength(False)
    assert any(b[0] < a[0] - 1e-6 or b[1] < a[1] - 1e-6 for a, b in zip(figs, figs[1:])), figs


@pytest.fixture(scope="module")
def reference():
    frozen = ma.load_frozen()
    return (frozen, {it["name"]: it for it in frozen["items"]}, ma.read_snapshot(),
            ma._targets(frozen["context"]))


def _scaled_ehp(god, names, ibn, targets, k, scale, monkeypatch):
    orig = sbs.Sim.mitigated
    monkeypatch.setattr(sbs.Sim, "mitigated", lambda self, *a, **kw: scale * orig(self, *a, **kw))
    try:
        return sbs.fight_ehp(god, names, ibn, targets, stacks=sbs.stack_state(names, k))[:2]
    finally:
        monkeypatch.setattr(sbs.Sim, "mitigated", orig)


@pytest.mark.parametrize("mode", ma.MODES)
def test_more_damage_never_lowers_survival_on_the_reference_builds(reference, mode, monkeypatch):
    """Every frozen reference god's core and model at 2/4/6 items: multiply
    every damage instance our god deals by 1, 1.5, 3 and 10, holding the
    build, its stats, its cooldowns and the enemy fixed. Fight EHP on both
    channels must never fall."""
    frozen, ibn, snap, targets = reference
    with ma.mode_rules(mode, frozen["context"]["minutes_per_item"].get(mode)):
        for name in ma.reference_names():
            god = frozen["gods"][name]
            for arch in ("core", "model"):
                six = snap[name][mode]["builds"][arch]
                for k in (2, 4, 6):
                    prev = None
                    for scale in (1.0, 1.5, 3.0, 10.0):
                        e = _scaled_ehp(god, six[:k], ibn, targets[mode], k, scale, monkeypatch)
                        if prev is not None:
                            assert e[0] >= prev[0] - 1e-6 and e[1] >= prev[1] - 1e-6, \
                                (name, mode, arch, k, scale, prev, e)
                        prev = e
