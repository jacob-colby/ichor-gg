"""Spot-check packet: select 10 gods by a fixed rule and dump their numbers.

usage (from pipeline/): PYTHONPATH=. PYTHONIOENCODING=utf-8 python ../docs/audits/2026-11-spot-check_extract.py <dir of side_by_side --json output>
Used for docs/audits/2026-11-spot-check.md. Reads only; writes picked.json beside the input dir.
"""
import glob, json, os, sys
from pathlib import Path
import yaml
from smite import tierlist

SBS = Path(sys.argv[1])
BUILDS = Path("../data/builds")
UNREADABLE = {"not enough simulated", "aspect not simulated"}


def god_record(god):
    text = (BUILDS / f"{god}-Conquest.md").read_text(encoding="utf-8")
    fm = yaml.safe_load(text.split("---")[1])
    for b in fm["builds"]:
        if b.get("source") == "community":
            return b["god_matches_played"], b["god_matches_won"], b["god_win_rate"]
    raise KeyError(god)


rows = []
for f in sorted(SBS.glob("*.json")):
    if f.name.startswith("_"):
        continue
    d = json.loads(f.read_text(encoding="utf-8"))
    played, won, wr = god_record(d["god"])
    d["_slug"] = f.stem
    d["_played"], d["_won"], d["_wr"] = played, won, wr
    rows.append(d)

pick = []
print("## readable per role (verdict, god, matches)")
for role in ["Carry", "Jungle", "Mid", "Solo", "Support"]:
    readable = [d for d in rows if d["role"] == role and d["verdict"] not in UNREADABLE]
    readable.sort(key=lambda d: (-d["_played"], d["god"]))
    print(role, len(readable), [(d["verdict"], d["god"], d["_played"]) for d in readable])
    if len(readable) < 2:
        print("  STOP: fewer than 2 readable")
        continue
    a = [d for d in readable if d["verdict"] == "Ichor better"]
    if a:
        A, why = a[0], "most-played 'Ichor better'"
    else:
        A = max(readable, key=lambda d: (d["damage_axis"] * d["survival_axis"], -d["_played"]))
        why = "no 'Ichor better' god; highest damage x survival axis product"
    b = [d for d in readable if d is not A and d["verdict"] in ("community better", "trade-off")]
    nem = [d for d in b if d["god"] == "Nemesis"]
    B, whyb = (nem[0], "Nemesis rule") if nem else (b[0], "most-played 'community better' or 'trade-off'")
    pick += [(A, why), (B, whyb)]
print("Nemesis:", [(d["verdict"], d["coverage"]) for d in rows if d["god"] == "Nemesis"])

def f0(x):
    return f"{x:,.0f}"

out = []
for d, why in pick:
    i, c = d["ichor"], d["community"]
    out.append(f"\n## {d['god']} — {d['role']}\n")
    out.append(f"Picked by: {why}. God record: {d['_won']}/{d['_played']} won "
               f"({d['_wr']:.1%}). Kit: {d['kit']['kit']}.\n")
    cov = d["coverage"]
    out.append(f"**Verdict: {d['verdict']}.** Damage axis {d['damage_axis']:.3f}, survival axis "
               f"{d['survival_axis']:.3f} (Ichor ÷ community, 6 items; weighted over 2/4/6: "
               f"{d['weighted_axes'][0]:.3f} / {d['weighted_axes'][1]:.3f}). Without the coverage "
               f"rule: {d['verdict_unwithheld']}; six items only: {d['verdict_six_only']}. "
               f"Simulated share Ichor {cov['ichor']:.0%}, community {cov['community']:.0%} "
               f"(gap {cov['gap']:.1%}).\n")
    out.append(f"- Ichor: {', '.join(i['items'])} ({f0(i['gold'])} g)")
    out.append(f"- Community: {', '.join(c['items'])} ({f0(c['gold'])} g)")
    if d["shared"]:
        out.append(f"- Shared: {', '.join(d['shared'])}")
    for s in d["substitutions"]:
        out.append(f"- Community slot {s['slot']}: {s['dropped']} ({s['class']}) → {s['used']}")
    out.append("\n| At 6 items | Ichor | Community | Ichor ÷ community |\n|---|---:|---:|---:|")
    for k, lab in [("burst_squishy", "Burst vs squishy"), ("burst_tank", "Burst vs tank"),
                   ("sustained_squishy", "10s sustained vs squishy"),
                   ("sustained_tank", "10s sustained vs tank"),
                   ("ehp_physical", "Effective health vs physical"),
                   ("ehp_magical", "Effective health vs magical")]:
        out.append(f"| {lab} | {f0(i[k])} | {f0(c[k])} | {i[k]/c[k]:.3f} |")
    out.append("\n| Power at | damage axis | survival axis | Ichor sustained vs squishy | community |\n|---|---:|---:|---:|---:|")
    for n in ["2", "4", "6"]:
        da, sa = d["breakpoint_axes"][n]
        out.append(f"| {n} items | {da:.3f} | {sa:.3f} | {f0(i['breakpoints'][n]['sustained_squishy'])} "
                   f"| {f0(c['breakpoints'][n]['sustained_squishy'])} |")
    out.append("\n| Differing item | Side | Pick | Est. matches | Item win vs god | Wilson LB | Ichor's reason (model) | Best swap |\n|---|---|---:|---:|---|---:|---|---|")
    for x in d["diffs"]:
        cm = x.get("community") or {}
        pr, wr = cm.get("pick_rate"), cm.get("win_rate")
        if pr is not None and wr is not None:
            est = round(pr * d["_played"])
            won = round(wr * est)
            lb = tierlist.wilson_lower_bound(won, est)
            lbs = f"{lb:.3f}" if lb is not None else f"— (n<{tierlist.MIN_MATCHES})"
            wv = f"{wr:.0%} vs {d['_wr']:.0%} ({(wr - d['_wr'])*100:+.1f} pt)"
            prs, ests = f"{pr:.0%}", str(est)
        else:
            prs, ests, wv, lbs = "—", "—", "not in community record", "—"
        m = x.get("model") or {}
        reason = m.get("text", "not scored").replace("|", "/")
        bs = x.get("best_swap")
        bss = (f"for {bs['replaces']}: {bs['damage_axis']:.3f} / {bs['survival_axis']:.3f}"
               if bs else "—")
        out.append(f"| {x['item']} | {x['side']} | {prs} | {ests} | {wv} | {lbs} | {reason} | {bss} |")
    out.append("")
print("\n".join(out))
json.dump([[d["god"], d["_slug"], d["role"], d["verdict"]] for d, _ in pick],
          open(SBS.parent / "picked.json", "w"))
