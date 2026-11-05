"""What is left of the movement question, read off the pages of the tree this runs in.

A DIAGNOSTIC: nothing imports this. The upper bound counts movement refusals as
simulated, which values movement at nothing and only stops the coverage rule
withholding, so it bounds that and not a movement dimension. Register 4.30.
Run from pipeline/: `python -m smite.scripts.movement_bound`.
"""
import glob
import json
from collections import Counter

from smite import build_quality as bq, passive_sim as ps, recommend, side_by_side as sbs

table = [v for k, v in vars(ps).items() if isinstance(v, dict) and v and all(hasattr(x, "status") for x in v.values())][0]
movement = {n for n, e in table.items() if e.status == "not simulated"
            and any("movement" in str(a).lower() for a in (e.assumptions or ()))}
print("refused for movement:", len(movement), sorted(movement)[:14], "...")

items = recommend.load_items()
by = {i["name"]: i for i in items}
gods = recommend.load_gods()
TK = "Tekko-Kagi"
hold = Counter()
total = Counter()
for g in gods:
    try:
        note = recommend.load_build_note(g["name"], "Conquest")
    except Exception:
        continue
    role = bq.primary_role(g)
    total[role] += 1
    for arch in ("model", "core"):
        six = bq.suggested_core(note, arch) or []
        if TK in six:
            hold[(arch, role)] += 1
    theirs, _ = sbs.community_six(g, note, by)
    if TK in (theirs or []):
        hold[("community", role)] += 1
roles = ("Carry", "Jungle", "Mid", "Solo", "Support")
print("Tekko-Kagi in Conquest builds, by role:")
for arch in ("model", "core", "community"):
    print(f"  {arch:10} " + "  ".join(f"{r} {hold[(arch, r)]}/{total[r]}" for r in roles) + f"  total {sum(hold[(arch, r)] for r in roles)}")

READ = ("Ichor better", "trade-off", "community better")
pages = [json.load(open(p, encoding="utf-8")) for p in glob.glob("../viewer/public/side_by_side/*.json") if not p.endswith("_meta.json")]


def share_after(side):
    """Simulated gold share if every movement refusal counted as simulated."""
    gold = sum((by.get(n) or {}).get("cost") or 0 for n in side["items"])
    extra = sum((by.get(p["item"]) or {}).get("cost") or 0 for p in side["passives"]
                if p.get("status") != "simulated" and p["item"] in movement)
    return gold, extra


# The bound adds gold shares, so hold it to the page's own figure first.
for d in pages:
    for side in ("ichor", "community"):
        s = d[side]
        gold = sum((by.get(n) or {}).get("cost") or 0 for n in s["items"])
        missing = sum((by.get(p["item"]) or {}).get("cost") or 0 for p in s["passives"] if p.get("status") == "not simulated")
        drift = abs((1 - missing / gold) - d["coverage"][side]) if gold else 0
        if drift > 0.05:
            print(f"  note: {d['god']} {side}: gold-share reading is {drift:.2f} from the page's coverage")

blockers = Counter()
gain = Counter()
direction = Counter()
carry_dir = Counter()
loss = Counter()
checked = 0
off = 0
for d in pages:
    role = d.get("role")
    i, c = d["coverage"]["ichor"], d["coverage"]["community"]
    gi, xi = share_after(d["ichor"])
    gc, xc = share_after(d["community"])
    i2 = min(1.0, i + (xi / gi if gi else 0))
    c2 = min(1.0, c + (xc / gc if gc else 0))
    was_ok, _ = sbs.coverage_check(i, c)
    now_ok, _ = sbs.coverage_check(i2, c2)
    if d.get("verdict") == "not enough simulated":
        for side in ("ichor", "community"):
            for p in d[side]["passives"]:
                if p.get("status") != "simulated":
                    blockers[(role, p["item"], "movement" if p["item"] in movement else "other")] += 1
    if not was_ok and now_ok:
        gain[role] += 1
        direction[d.get("verdict_unwithheld")] += 1
        if role == "Carry":
            carry_dir[d.get("verdict_unwithheld")] += 1
    if was_ok and not now_ok:
        loss[role] += 1
print("coverage-blocker occurrences on 'not enough simulated' gods:")
for role in roles:
    rows = [(n, kind, c) for (r, n, kind), c in blockers.items() if r == role]
    mv = sum(c for n, kind, c in rows if kind == "movement")
    print(f"  {role:8} movement {mv:2} other {sum(c for n, kind, c in rows if kind != 'movement'):2}   " + ", ".join(f"{n} {c}" for n, kind, c in sorted(rows, key=lambda r: -r[2])[:4]))
print("UPPER BOUND, if a movement dimension made every movement refusal count as simulated:")
print("  gates opened by role:", {r: gain[r] for r in roles}, "total", sum(gain.values()))
print("  gates closed by role:", {r: loss[r] for r in roles}, "total", sum(loss.values()))
print("  what those newly open verdicts would read:", dict(direction))
print("  Carry only:", dict(carry_dir))
