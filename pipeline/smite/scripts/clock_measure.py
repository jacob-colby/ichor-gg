"""Register 4.12's B6 measure, committed at last, and the arms that re-open it.

A DIAGNOSTIC. Nothing imports this and it writes nothing to `data/`.

THE METRIC. Where the community's own Conquest items land in a god's damage
ordering, 0 = top. The ordering takes no community input at all, so this is not
the circular number of STATE.md section 1. Entry 12 printed a table and committed
no harness; this definition was recovered by search and reproduces all twelve
published figures and both unscored counts to the digit when run at the commit
that recorded them (59d7362c, flags off):

    order     max(gain against SQUISHY, gain against TANK), descending
    scored    gain > 0 against either target
    rank      1-based position / number of buildable items for that god
    unscored  the mean of the tail, (scored + 1 + pool) / 2 / pool

THE ARMS. A per-second model lets a god cast everything off cooldown AND swing
at full rate, because nothing here has cast times. Rather than choose a charge
and defend it, this measures the families a charge could belong to:

    k    a roster-wide multiplier on the basic-attack channel. Only the ratio
         of the two channels can reorder items, so this spans EVERY roster-wide
         pair of constants, including anything derived from one roster-wide
         pair of intervals. If no k passes, no such constant can.
    T    a per-god charge from the god's own scraped kit: each cast costs T
         seconds of swinging, so swings run at (1 - T * casts per second) of
         full rate, with the item's own Cooldown Rate raising the charge.
         No community input, and T is swept rather than asserted.
    role the clock on for one role and off for the rest.
    share the clock on where `damage_value.basic_attack_shares` is over a
         threshold. The threshold is committed in `smite.scripts.attack_share`,
         ahead of this measurement, and is not swept here.

Reads under the shipped fit by default: the pricing flags applied as
`_weights.yaml` sets them. `--flags-off` is the state entry 12 was recorded in,
and also what `build_index` runs today (STATE.md section 5), so both are reported.

Run from `pipeline/`: `python -m smite.scripts.clock_measure [--flags-off]`.
"""
import argparse
import statistics
import sys
from collections import defaultdict

from smite import (build_index, build_quality as bq, combat, damage_value as dv, efficiency,
                   model_audit as ma, recommend, scoring)

LOW, HIGH = build_index.SQUISHY_PROTECTION, build_index.TANK_PROTECTION
ROLES = ("Carry", "Jungle", "Mid", "Solo", "Support")


def casts_per_second(god, cdr, rank_index=0):
    """Every ability with a scraped cooldown costs casting time, whether or not
    it deals damage: a heal is cast too."""
    total = 0.0
    for ability in god.get("abilities") or []:
        cooldowns = ability.get("cooldown") or []
        if not cooldowns:
            continue
        cd = float(cooldowns[min(rank_index, len(cooldowns) - 1)]) or None
        if cd:
            total += combat.casts_per_second(cd, cdr)
    return total


def parts(god, item, prot, level=1, rank_index=0):
    """The per-second gain split into its two channels, so any arm can be read
    off without another pass. Mirrors `item_damage_gain(per_second=True)`;
    `check_parts` holds the two together."""
    comps = [c for c in dv.ability_damage_components(god) if dv._base_cooldown(god, c, rank_index)]
    if not comps:
        return None
    stats = dv._item_stats(item)
    flat, pct = stats.get("Penetration", 0.0), stats.get("Penetration %", 0.0) / 100.0
    cdr = stats.get("Cooldown Rate", 0.0)
    before = after = 0.0
    for c in comps:
        rank = c["ranks"][min(rank_index, len(c["ranks"]) - 1)]
        base = combat.ability_damage(rank, c["scaling"], {})
        gained = combat.ability_damage(rank, c["scaling"], stats)
        cd = dv._base_cooldown(god, c, rank_index)
        before += combat.damage_dealt(base, prot) * combat.casts_per_second(cd)
        after += (combat.damage_dealt(gained, prot, flat_pen=flat, pct_pen=pct)
                  * combat.casts_per_second(cd, cdr))
    base_hit, gained_hit = dv._basic_attack_pair(god, stats, level)
    rate = dv._base_attack_speed(god)
    crit = min(stats.get("Critical Chance %", 0.0), 100.0) / 100.0
    b0 = combat.attack_dps(base_hit, prot, rate)
    b1 = combat.attack_dps(gained_hit, prot, rate, attack_speed_bonus=stats.get("Attack Speed %", 0.0),
                           crit_chance=crit, flat_pen=flat, pct_pen=pct)
    return {"a": after - before, "b0": b0, "b1": b1,
            "c0": casts_per_second(god, 0.0, rank_index), "c1": casts_per_second(god, cdr, rank_index)}


def check_parts(gods, items, n=6):
    for god in gods[:n]:
        for item in items[:40]:
            p = parts(god, item, LOW)
            got = dv.item_damage_gain(god, item, LOW, per_second=True)
            want = 0.0 if p is None else p["a"] + p["b1"] - p["b0"]
            assert abs(got - want) < 1e-9, (god["name"], item["name"], got, want)


def k_arm(k):
    return lambda p, rot: 0.0 if p is None else p["a"] + k * (p["b1"] - p["b0"])


def t_arm(t):
    def gain(p, rot):
        if p is None:
            return 0.0
        return p["a"] + max(0.0, 1 - t * p["c1"]) * p["b1"] - max(0.0, 1 - t * p["c0"]) * p["b0"]
    return gain


def rotation(p, rot):
    return rot


def community_names(note):
    entry = next((b for b in note.get("builds") or [] if b.get("source") == "community"), None)
    return [s.get("name") if isinstance(s, dict) else s for s in (entry or {}).get("slot_order") or []]


def load(items, gods):
    rows = []
    for god in gods:
        if not dv.ability_damage_components(god):
            continue
        try:
            note = recommend.load_build_note(god["name"], "Conquest")
        except Exception:
            continue
        names = community_names(note)
        if not names:
            continue
        table = {}
        for it in items:
            if not scoring.is_buildable(it, god):
                continue
            table[it["name"]] = ((parts(god, it, LOW), dv.item_damage_gain(god, it, LOW)),
                                 (parts(god, it, HIGH), dv.item_damage_gain(god, it, HIGH)))
        rows.append({"god": god["name"], "role": bq.primary_role(god), "names": names, "table": table,
                     "share": dv.basic_attack_shares(god)})
    return rows


def god_ranks(row, arm):
    scores = {}
    for name, (lo, hi) in row["table"].items():
        a, b = arm(*lo), arm(*hi)
        if a > 0 or b > 0:
            scores[name] = max(a, b)
    order = {n: i + 1 for i, n in enumerate(sorted(scores, key=lambda n: -scores[n]))}
    pool, scored = len(row["table"]), len(order)
    tail = (scored + 1 + pool) / 2 / pool
    return [order[n] / pool if n in order else tail for n in row["names"]], sum(n not in order for n in row["names"])


def summarise(rows, arm_for):
    """`arm_for(row)` picks the arm per god, so any gate is the same call."""
    acc, unscored = defaultdict(list), 0
    per_god = {}
    for row in rows:
        vals, miss = god_ranks(row, arm_for(row))
        acc[row["role"]] += vals
        per_god[row["god"]] = statistics.fmean(vals)
        unscored += miss
    out = {r: statistics.fmean(acc[r]) for r in ROLES if acc[r]}
    out["ALL"] = statistics.fmean([v for r in ROLES for v in acc[r]])
    out["n"] = {r: len(acc[r]) for r in ROLES}
    return out, unscored, per_god


def line(label, s, base=None):
    tail = ""
    if base:
        c1 = "PASS" if s["Carry"] < base["Carry"] else "fail"
        c2 = "PASS" if s["ALL"] <= base["ALL"] else "fail"
        tail = f"  crit1 {c1}  crit2 {c2}"
    return f"{label:20} " + " ".join(f"{r[:5]} {s[r]:.3f}" for r in ROLES) + f"  ALL {s['ALL']:.3f}" + tail


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--flags-off", action="store_true",
                    help="every pricing flag off: entry 12's state, and what build_index runs today")
    args = ap.parse_args(argv)

    items, gods = recommend.load_items(), recommend.load_gods()
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    prior = efficiency.apply_pricing_flags({} if args.flags_off else weights)
    try:
        check_parts(gods, items)
        rows = load(items, gods)
        print(f"flags {'OFF (what build_index ships today)' if args.flags_off else 'ON (the shipped fit)'}"
              f" | gods {len(rows)} | community slots {sum(len(r['names']) for r in rows)}")
        same = lambda arm: (lambda row: arm)
        base, u0, _ = summarise(rows, same(rotation))
        print(line("rotation (shipped)", base), f" unscored {u0}")
        ps, u1, _ = summarise(rows, same(k_arm(1.0)))
        print(line("per second, k=1", ps, base), f" unscored {u1}")
        print("-- k: roster-wide multiplier on the basic channel (spans every roster-wide pair)")
        for k in (0.0, 0.02, 0.05, 0.1, 0.15, 0.2, 0.3, 0.5, 0.7, 0.85):
            s, _, _ = summarise(rows, same(k_arm(k)))
            print(line(f"k={k}", s, base))
        # The fight model's roster-wide intervals (0.4317s between attacks,
        # 3.2432s between casts) read as a charge. They are rates, so there are
        # only two literal readings: one cast costs one swing, or the channels
        # weighted by their share of events.
        for label, k in (("one swing per cast", 1 - 0.4317 / 3.2432), ("event share 7.5:1", 3.2432 / 0.4317)):
            s, _, _ = summarise(rows, same(k_arm(k)))
            print(line(f"{label}", s, base), f" k={k:.3f}")
        print("-- T: seconds of swinging each cast costs, per god, from the god's own kit")
        for t in (0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0):
            s, _, _ = summarise(rows, same(t_arm(t)))
            print(line(f"T={t}", s, base))
        print("-- role gate: the clock on for one role, rotation for the rest")
        for role in ROLES:
            s, _, _ = summarise(rows, lambda row, role=role: k_arm(1.0) if row["role"] == role else rotation)
            print(line(f"{role} only", s, base))
        print("-- share gate: threshold committed in smite.scripts.attack_share, not swept")
        for label, key, cut, status in (("rotation > 0.50", "rotation", 0.50, "THE RULE"),
                                        ("per second > 0.50", "per_second", 0.50, "ineligible"),
                                        ("rotation > 0.226", "rotation", 0.226, "ineligible")):
            picked = lambda row, key=key, cut=cut: bool(row["share"]) and row["share"][key] > cut
            s, u, _ = summarise(rows, lambda row, picked=picked: k_arm(1.0) if picked(row) else rotation)
            on = [r for r in rows if picked(r)]
            print(line(f"{label}", s, base), f" [{status}] unscored {u}")
            print("     selects " + str(len(on)) + ": " + ", ".join(f"{r_} {sum(x['role'] == r_ for x in on)}" for r_ in ROLES)
                  + (" = " + ", ".join(x["god"] for x in on) if len(on) <= 6 else ""))
            if key == "rotation" and cut == 0.50:
                _, _, g0 = summarise(rows, same(rotation))
                _, _, g1 = summarise(rows, lambda row, picked=picked: k_arm(1.0) if picked(row) else rotation)
                for x in on:
                    print(f"       {x['god']:12} {x['role']:7} {g0[x['god']]:.3f} -> {g1[x['god']]:.3f}  {g1[x['god']] - g0[x['god']]:+.3f}")

        # The Carry gate on its own terms, since it passes criterion 2 by
        # construction: does it hold per god and out of sample?
        _, _, g0 = summarise(rows, same(rotation))
        _, _, g1 = summarise(rows, same(k_arm(1.0)))
        carries = [r["god"] for r in rows if r["role"] == "Carry"]
        held = {g for g in carries if ma.split_of(g) == "heldout"}
        better = [g for g in carries if g1[g] < g0[g]]
        print(f"-- Carry, per god: {len(better)} of {len(carries)} improve")
        for g in sorted(carries, key=lambda g: g1[g] - g0[g]):
            mark = " (held-out)" if g in held else ""
            print(f"     {g:15} {g0[g]:.3f} -> {g1[g]:.3f}  {g1[g]-g0[g]:+.3f}{mark}")
        for label, group in (("held-out", [g for g in carries if g in held]),
                             ("tuning", [g for g in carries if g not in held])):
            if group:
                won = sum(g1[g] < g0[g] for g in group)
                print(f"   {label:9} n={len(group):2} {statistics.fmean(g0[g] for g in group):.3f}"
                      f" -> {statistics.fmean(g1[g] for g in group):.3f}, {won} of {len(group)} improve")
        # A role gate must also not be doing its work through the unscored
        # tail, so the same comparison with unscored items left out.
        for label, arm in (("rotation", rotation), ("per second", k_arm(1.0))):
            vals = []
            for row in rows:
                if row["role"] != "Carry":
                    continue
                scores = {}
                for name, (lo, hi) in row["table"].items():
                    a, b = arm(*lo), arm(*hi)
                    if a > 0 or b > 0:
                        scores[name] = max(a, b)
                order = {n: i + 1 for i, n in enumerate(sorted(scores, key=lambda n: -scores[n]))}
                vals += [order[n] / len(order) for n in row["names"] if n in order]
            print(f"   scored items only, / scored: {label:11} {statistics.fmean(vals):.3f} (n={len(vals)})")
    finally:
        efficiency.restore_pricing_flags(prior)
    return 0


if __name__ == "__main__":
    sys.exit(main())
