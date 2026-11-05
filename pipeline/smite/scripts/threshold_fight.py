"""Register 4.13's two thresholds, re-read on the fight layer.

Same definitions as build_quality.threshold_probe, the attacker at ZERO
protection and the channel taken from the attacker's damage type. The only
change is where the damage comes from: side_by_side's burst combo (passives
simulated, one basic attack) and its WINDOW-second run. No new constant.
A DIAGNOSTIC: nothing imports this. See register 4.13 for what it found.
Run from pipeline/: `python -m smite.scripts.threshold_fight`.
"""
import copy
import statistics
from collections import Counter, defaultdict

from smite import build_quality as bq, efficiency, recommend, scoring, side_by_side as sbs

items = recommend.load_items()
gods = recommend.load_gods()
by = {i["name"]: i for i in items}
w = scoring.load_weights(recommend.WEIGHTS_PATH)
efficiency.apply_pricing_flags(w)
notes = {}
for g in gods:
    try:
        notes[g["name"]] = recommend.load_build_note(g["name"], "Conquest")
    except Exception:
        pass
targets = sbs.reference_targets(gods, notes, by)
zero = {"zero": copy.deepcopy(targets["squishy"])}
zero["zero"]["physical_prot"] = 0.0
zero["zero"]["magical_prot"] = 0.0

rows = []
for g in gods:
    note = notes.get(g["name"])
    if not note:
        continue
    ours = bq.suggested_core(note, sbs.ARCHETYPE)
    theirs, _ = sbs.community_six(g, note, by)
    for side, six in (("ours", ours), ("community", theirs)):
        if not six or len(six) != 6:
            continue
        # The attacker's damage at zero protection, as the original probe reads
        # it. Effective health from the real targets: the fight run's EHP reads
        # lifesteal and kill-heals, so a zero-protection copy of the target
        # changes it and must not be the number a floor is checked against.
        p = sbs.power(g, six, by, zero)
        real = sbs.power(g, six, by, targets)
        rows.append({"god": g["name"], "role": bq.primary_role(g), "side": side, "type": g.get("damage_type"),
                     "burst": p["burst_zero"], "window": p["sustained_zero"],
                     "ehp_physical": real["ehp_physical"], "ehp_magical": real["ehp_magical"],
                     "sustained_squishy": real["sustained_squishy"], "sustained_tank": real["sustained_tank"],
                     "burst_squishy": real["burst_squishy"], "burst_tank": real["burst_tank"]})

print("builds:", len(rows), "| flag price_passive_sim:", w.get("price_passive_sim"))
print("sample Medusa ours:", {k: round(v, 1) if isinstance(v, float) else v for k, v in next(r for r in rows if r["god"] == "Medusa" and r["side"] == "ours").items()})


def channel(attack_type):
    return "ehp_physical" if str(attack_type).lower().startswith("phys") else "ehp_magical"


def carry_floor(metric):
    top = max(rows, key=lambda r: r[metric])
    ch = channel(top["type"])
    carries = [r for r in rows if r["role"] == "Carry"]
    fail = [r for r in carries if r[ch] < top[metric]]
    near = min(carries, key=lambda r: abs(r[ch] / top[metric] - 1))
    print(f"  Carry floor on {metric:6}: attacker {top['god']} ({top['side']}) {top[metric]:.0f} {top['type']}; "
          f"fails {len(fail)} of {len(carries)} (ours {sum(r['side']=='ours' for r in fail)}, community {sum(r['side']=='community' for r in fail)}); "
          f"nearest {near['god']} {near['side']} EHP {near[ch]:.0f} = {near[ch]/top[metric]:.2f}x")
    return fail


def kill_threshold(metric):
    ref = {}
    squishy = [r for r in rows if r["side"] == "community" and r["role"] in ("Carry", "Mid")]
    for ch in ("ehp_physical", "ehp_magical"):
        ref[ch] = statistics.median(r[ch] for r in squishy)
    pop = [r for r in rows if r["role"] in ("Mid", "Jungle")]
    passed = [r for r in pop if r[metric] >= ref[channel(r["type"])]]
    ratios = [r[metric] / ref[channel(r["type"])] for r in pop]
    print(f"  kill threshold on {metric:6}: reference EHP phys {ref['ehp_physical']:.0f} mag {ref['ehp_magical']:.0f}; "
          f"passes {len(passed)} of {len(pop)}; ratio median {statistics.median(ratios):.2f} max {max(ratios):.2f}")


print("BURST COMBO, passives simulated, one basic attack")
carry_floor("burst")
kill_threshold("burst")
print(f"WINDOW = {sbs.WINDOW}s run, passives simulated, basic attacks in")
f = carry_floor("window")
print("Carry EHP range, all builds:", {c: (round(min(r[c] for r in rows if r["role"] == "Carry")), round(max(r[c] for r in rows if r["role"] == "Carry"))) for c in ("ehp_physical", "ehp_magical")})
kill_threshold("window")
if f:
    print("  window fails by side and god:", Counter(r["side"] for r in f), sorted({r["god"] for r in f})[:12])
print("MEDIAN attacker, not the single largest (does anything change if the roster's outlier is removed?)")
for metric in ("burst", "window"):
    med = statistics.median(r[metric] for r in rows)
    carries = [r for r in rows if r["role"] == "Carry"]
    print(f"  {metric:6} median {med:.0f}: Carries below it on magical {sum(r['ehp_magical']<med for r in carries)}, physical {sum(r['ehp_physical']<med for r in carries)} of {len(carries)}")
    print(f"         same check against the worst attacker of EACH type: " + str({t: (round(max(r[metric] for r in rows if r['type'] == t)), sum(r[channel(t)] < max(x[metric] for x in rows if x['type'] == t) for r in carries)) for t in ('physical', 'magical')}))
print("Do Carries already differ between the two sides on effective health? (the over-buys-damage premise)")
pairs = defaultdict(dict)
for r in rows:
    if r["role"] == "Carry":
        pairs[r["god"]][r["side"]] = r
for key in ("ehp_physical", "ehp_magical", "sustained_squishy", "sustained_tank", "burst_squishy", "burst_tank"):
    ratios = [p["ours"][key] / p["community"][key] for p in pairs.values() if len(p) == 2]
    print(f"  ours / community {key:13} median {statistics.median(ratios):.3f}  ours higher on {sum(x>1 for x in ratios)} of {len(ratios)}")
