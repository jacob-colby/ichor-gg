"""Basic-attack share of marginal power, per god. Deliberately prints no B6 figure.

A DIAGNOSTIC: nothing imports this at run time except through
`damage_value.basic_attack_share`, which is where the arithmetic lives.

The share is register 4.12's own discriminator, read on the god's own damage
stat, at rank 1. Run at the commit that recorded it (59d7362c) the PER-SECOND
reading reproduces all five published role medians exactly: Carry 89.3, Jungle
92.5, Solo 90.2, Support 78.8, Mid 60.5. The per-rotation reading matches or
comes close: Carry and Mid exact, Jungle 35.0 against 35.1, Solo 31.8 against
32.6, Support 16.9 against 19.0.

It is item-free coefficient arithmetic, so no pricing flag can reach it.

This prints the distribution and nothing about how a threshold would score,
because a threshold chosen while looking at the metric is the tuning entry 12
refuses. Run from `pipeline/`: `python -m smite.scripts.attack_share`.

THE THRESHOLD, COMMITTED BEFORE THE RULE WAS MEASURED (2026-11-05).

    The clock applies where the PER-ROTATION share is over 0.50.
    Selected on today's roster: Xbalanque (57.1), Nemesis (54.1), Guan Yu (52.9).

Why that reading. The per-second reading assumes full uptime on both channels,
which is the assumption the clock is accused of, so gating the clock on it is
circular. It also cannot discriminate: 86 of 95 gods read over half, including
16 of 24 Mids and the register's named reductios, Agni 72.2 and Ymir 60.7, and
its only sizeable gap (5.3 points) leaves one god below it.

Why that number. Two independent reasons land in the same place. "Over half" is
what "basic attacks dominate marginal power" means, and it coincides with the
largest gap in the whole distribution, 7.2 points between Loki (45.7) and Guan
Yu (52.9). Neither came from the metric.

What this choice is NOT. It is not blind. #113 had already shown the clock
helping Carries and hurting Mids and Jungle, so a Carry-heavy selection was
known to score well, and this one is chosen knowing it selects 1 Carry of 19 and
will probably score worse than the role list it replaces.

Committed with it, measured once each and INELIGIBLE to ship from this PR
whatever they score, because neither was chosen on the principle above:

    per-second share over 0.50    the reading rejected above; 86 gods
    rotation share over 0.226     the largest gap in the BODY of the distribution
                                  (3.0 points, Khepri 21.1 to Danzaburou 24.1); 48
                                  gods, no Mids. "Basics are a quarter of marginal
                                  power" is not domination, and it mostly restates
                                  physical against magical.

The decision, also committed first: entry 12's three criteria unmoved, and if the
rule scores worse for Carry than `damage_per_second_roles: [Carry]` did, the clock
stays OFF for everyone rather than keeping the role list.
"""
import statistics
import sys
from collections import defaultdict

from smite import build_quality as bq, damage_value as dv, kit, recommend

ROLES = ("Carry", "Jungle", "Solo", "Support", "Mid")


def main():
    rows = []
    for god in recommend.load_gods():
        share = dv.basic_attack_shares(god)
        if share is None:
            continue
        rows.append({"god": god["name"], "role": bq.primary_role(god), "label": god.get("role"),
                     "type": god.get("damage_type"), "rot": share["rotation"], "sec": share["per_second"],
                     "kit": kit.scaling_profile(god)["basic_attack_share"]})
    print(f"gods with a share: {len(rows)}")
    for key, label in (("sec", "PER SECOND"), ("rot", "PER ROTATION"), ("kit", "KIT TEXT (kit.scaling_profile)")):
        print(f"\n=== {label} ===")
        print("role      n   min    q1    med    q3    max    >=50%")
        for role in ROLES:
            xs = sorted(100 * r[key] for r in rows if r["role"] == role)
            q = statistics.quantiles(xs, n=4)
            print(f"{role:8} {len(xs):2} {xs[0]:5.1f} {q[0]:5.1f} {statistics.median(xs):6.1f} {q[2]:5.1f} {xs[-1]:6.1f}   {sum(x >= 50 for x in xs):2}/{len(xs)}")
        ordered = sorted(rows, key=lambda r: r[key])
        gaps = sorted(((ordered[i + 1][key] - ordered[i][key], i) for i in range(len(ordered) - 1)), reverse=True)[:5]
        print("largest gaps in the sorted roster:")
        for gap, i in gaps:
            print(f"  {100*gap:5.1f} pts between {ordered[i]['god']} ({ordered[i]['role']}, {100*ordered[i][key]:.1f}) and {ordered[i+1]['god']} ({ordered[i+1]['role']}, {100*ordered[i+1][key]:.1f})  [{sum(1 for r in rows if r[key] > ordered[i][key])} gods above]")
        bins = defaultdict(lambda: defaultdict(int))
        for r in rows:
            bins[min(int(100 * r[key] // 10) * 10, 90)][r["role"]] += 1
        print("histogram, 10-point bins:")
        for b in range(0, 100, 10):
            cells = " ".join(f"{role[:3]} {bins[b][role]:2}" for role in ROLES)
            print(f"  {b:3}-{b+10:<3} {cells}  total {sum(bins[b].values()):2}")
    print("\n=== every god, sorted by per-second share ===")
    print("god              role          type      per-sec  per-rot  kit")
    for r in sorted(rows, key=lambda r: -r["sec"]):
        print(f"{r['god']:16} {str(r['label']):13} {str(r['type'])[:8]:8} {100*r['sec']:7.1f} {100*r['rot']:8.1f} {100*r['kit']:5.1f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
