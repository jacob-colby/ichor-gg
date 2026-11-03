"""What is a typical item's lifesteal worth in SURVIVAL, against a typical
item's health, per role? (2026-11-03)

    python -m smite.lifesteal_value          # the per-role table at both healing bounds

WHY. With healing in the fight (`side_by_side`'s HEALING block), seven
Conquest verdicts moved, all on the survival axis and all toward a
lifesteal-heavy community six (Sun Wukong, Chaac, Mordred, Hua Mulan — Solo;
Ishtar — Carry; Sol — Mid Carry; Ymir — Support). The fit map is why the model
did not buy those items: `Lifesteal` has a weight in the Carry, Hunter and
Sharpshooter maps (0.5) and in NO other, so it is 0 for 19 of 19 Solo gods and
18 of 18 Jungle gods. Efficiency is not the gap — it prices Lifesteal at
47.78 gold a point by regression, a price, not a value to a kit — the fit map
is: an item's 7.5% Lifesteal is invisible to a bruiser's fit.

THE MEASUREMENT. For every god of a role holding a full community six,
`fight_ehp` (both damage types, averaged) on that six plus one typical item's
LIFESTEAL (`scoring.stat_reference`) against the same six plus one typical
item's MAX HEALTH. `ratio` = EHP gained from the lifesteal / EHP gained from
the health, the role's median. A typical health line has a fit weight in
every defensive map; the lifesteal weight that values a typical lifesteal
line the way the combat model does is that weight times `ratio`.

TWO BOUNDS, because an effective-health run is a chain of fights and
lifesteal compounds over the chain (`HEAL_UNTIL`): ONE FIGHT heals inside
the first WINDOW only (the conservative end); CHAINED is the shipped run.
`role_stats` ships the GEOMETRIC MEAN of the two, so it sits between them.

RESULT (OB47, 2026-11-03; `core` cores changed of 101, Conquest / Joust / Arena;
Conquest side-by-side verdicts, 87 judged):

                  Solo LS  Support LS  cores changed   verdicts B / C / T / L / early / withheld
    before          0         0             -           8 / 10 / 14 / 9 / 1 / 45
    one fight     0.18      0.17         7 / 5 / 6      8 / 10 / 13 / 9 / 1 / 46
    SHIPPED       0.52      0.47       14 / 14 / 14     8 / 10 / 14 / 9 / 1 / 45
    chained       1.49      1.25       30 / 33 / 25     8 / 11 / 11 / 9 / 1 / 47

The shipped totals do not move; six verdicts swap places (Atlas, Cerberus,
Ganesha trade-off -> withheld; Kuzenbo, Sobek, Xing Tian the reverse). NONE of
the seven gods that motivated it changes verdict, and the reason is a binding
constraint, not the weight: `max_lifesteal` is a SUSTAIN cap of 1 for a Solo,
Amanita Charm already spends it, and the community's own Solo sixes hold a
median of ONE sustain item (29% hold two or more), so raising the cap is not
evidenced. What the weight changes is WHICH sustain item: Chaac's model and
core, and Sun Wukong's core, swap Amanita Charm for Gluttonous Grimoire.
Leakage-free coverage does not fall at any setting (36.6% / 36.7% before;
36.6% / 37.2% shipped).
"""
import statistics
import sys

from smite import build_quality as bq, scoring, side_by_side as sbs

ROLES = ("Solo", "Jungle", "Support", "Mid", "Carry")


def _ehp(god, names, items_by_name, targets):
    p, m, _ = sbs.fight_ehp(god, names, items_by_name, targets)
    return (p + m) / 2


def role_ratios(gods, items, builds_by_god, heal_until=None):
    """`{role: (median ratio, n)}` — see the module docstring."""
    ib = {it["name"]: it for it in items}
    ref = scoring.stat_reference(items)
    ls, hp = ref.get("Lifesteal", 0.0), ref.get("Max Health", 0.0)
    ib["__LS__"] = {"name": "__LS__", "stats": {"Lifesteal": f"{ls}%"}, "passive": "", "cost": 0}
    ib["__HP__"] = {"name": "__HP__", "stats": {"Max Health": f"{hp}"}, "passive": "", "cost": 0}
    targets = sbs.reference_targets(gods, builds_by_god, ib)
    saved = sbs.HEAL_UNTIL
    if heal_until is not None:
        sbs.HEAL_UNTIL = heal_until
    try:
        out = {}
        for role in ROLES:
            rs = []
            for g in gods:
                if bq.primary_role(g) != role:
                    continue
                six, _ = sbs.community_six(g, builds_by_god.get(g["name"]) or {}, ib)
                if len(six) != 6:
                    continue
                base = _ehp(g, six, ib, targets)
                d_ls = _ehp(g, six + ["__LS__"], ib, targets) - base
                d_hp = _ehp(g, six + ["__HP__"], ib, targets) - base
                if d_hp > 0:
                    rs.append(d_ls / d_hp)
            out[role] = (statistics.median(rs) if rs else 0.0, len(rs))
        return out, {"Lifesteal": ls, "Max Health": hp}
    finally:
        sbs.HEAL_UNTIL = saved


def main(argv=None):
    items, gods, weights, tags_map, builds = sbs.load_inputs()
    one, ref = role_ratios(gods, items, builds, heal_until=sbs.WINDOW)
    chained, _ = role_ratios(gods, items, builds)
    print(f"typical item: {ref['Lifesteal']:.2f}% Lifesteal vs {ref['Max Health']:.0f} Max Health")
    print(f"{'role':8} {'n':>3} {'one fight':>10} {'chained':>9} {'geomean':>8}")
    for r in ROLES:
        a, n = one[r]
        b, _ = chained[r]
        gm = (a * b) ** 0.5 if a > 0 and b > 0 else 0.0
        print(f"{r:8} {n:>3} {a:>10.3f} {b:>9.3f} {gm:>8.3f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
