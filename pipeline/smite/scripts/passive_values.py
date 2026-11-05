"""Per-item passive values, measured once and written to `data/_passive_values.yaml`.

WHY A FILE AND NOT AN IMPORT. `side_by_side`'s docstring states the rule this
obeys: "IT IS A DIAGNOSTIC AND FEEDS NOTHING ... Nothing in `scoring`,
`assemble`, `recommend` or `build_index` imports this module" (register §4.4).
Option (a) needs those numbers inside `efficiency`, and the way to have both is
for the diagnostic to EXPORT and the model to READ DATA — so nothing in the
scoring path imports the simulator, the values are auditable in the repo, and
scoring stays deterministic without running a fight per call.

WHAT A VALUE IS. `side_by_side.passive_contribution` runs the build twice, once
with that one passive switched off and its printed stats kept, and reports the
difference. So the number is "what this passive adds, in this build, against
these targets" — not a gold price. `efficiency` fits the gold price itself; see
`efficiency.PRICE_PASSIVE_SIM`.

THE REFERENCE CONTEXT, which is the assumption this whole arm rests on.
A contribution is build- and target-dependent; an efficiency residual is not.
So each item is measured in EVERY shipped build that holds it — ours and the
community's, all three modes — against the two reference targets
(`reference_targets`: median Mid as squishy, median Support as tank), and the
MEDIAN across those builds is the value. The per-item spread is written beside
it, because for some items it is wide: measured 2026-11-05, Riptalon 1.1x,
Dominance 1.3x, Silverbranch Bow 1.7x and Deathbringer 3.0x (400 to 1204,
tracking the build's crit chance). A reader deciding whether to trust one
number needs the spread next to it.

Items the community holds and we do not are covered for exactly this reason:
The Executioner is in no shipped `core` of ours, and it is the item §4.31 is
about.

THREE COLUMNS, NOT ONE.
  passive_damage         mean of the four DAMAGE_KEYS — all damage, same units
  passive_ehp_physical   kept apart from
  passive_ehp_magical    ...this one, because register §4.17 refuses to
                         collapse the two effective-health channels into a
                         single number and says what the pair bounds instead.
                         Averaging them here would be that refusal ignored.

REFUSED IS AN EXPLICIT ZERO, NOT AN ABSENCE. `passive_sim` marks an item
`not simulated` when its effect depends on something the comparison does not
contain — movement, crowd control, an ally, wards, an enemy shield. Those items
are written with zeros and `status: refused`, so the file says "this passive
contributes nothing HERE, by decision" rather than leaving a gap that reads as
the same thing. An item with no passive text at all is `status: none`, also
zero. Every item in `efficiency_pool` appears, so a missing key is a bug and
not a default.
"""
import argparse
import json
import statistics
import sys
from pathlib import Path

from smite import efficiency, recommend, scoring, side_by_side as sbs

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_PATH = REPO_ROOT / "data" / "_passive_values.yaml"

DAMAGE_KEYS = sbs.DAMAGE_KEYS
SURVIVAL_KEYS = sbs.SURVIVAL_KEYS


def _every_build(builds_by_god):
    """`[(god, [six item names])]` over every build in every note — ours and the
    community's, every mode. An item priced only where WE buy it would be
    missing exactly the community picks §4.31 is about."""
    out = []
    for god_name, note in builds_by_god.items():
        for b in note.get("builds") or []:
            names = [s if isinstance(s, str) else (s or {}).get("name")
                     for s in (b.get("slot_order") or [])]
            names = [n for n in names if n]
            if len(names) >= 2:
                out.append((god_name, names))
    return out


#: Builds sampled per item. A median over 30 observations is already stable —
#: the widest spread in the set moves from 3.0x on 5 shipped cores to 1.6x over
#: 87 builds — and the cost is two fights per observation per target, so an
#: uncapped run is ~40,000 fights. Sampling is DETERMINISTIC (sorted by god then
#: build, every Nth taken) so the committed file is reproducible rather than
#: dependent on dict order.
MAX_SAMPLES = 30


def _even_sample(seq, k):
    """`k` items spread evenly across `seq`, order preserved. Taking the first
    `k` would sample gods alphabetically, which is a sample of A-names."""
    if len(seq) <= k:
        return list(seq)
    step = len(seq) / k
    return [seq[int(i * step)] for i in range(k)]


def measure(items, gods, builds_by_god, limit_items=None, max_samples=MAX_SAMPLES):
    by_name = {i["name"]: i for i in items}
    gods_by_name = {g["name"]: g for g in gods}
    targets = sbs.reference_targets(gods, builds_by_god, by_name)
    table = sbs.PASSIVES if hasattr(sbs, "PASSIVES") else None

    from smite import passive_sim as ps
    table = [v for k, v in vars(ps).items()
             if isinstance(v, dict) and v and all(hasattr(x, "status") for x in v.values())][0]

    pool = {i["name"] for i in efficiency.efficiency_pool(items)}
    if limit_items:
        pool = {n for n in pool if n in set(limit_items)}

    builds = sorted(_every_build(builds_by_god), key=lambda r: (r[0], tuple(r[1])))
    # Which builds hold each item, capped and evenly sampled, before any fight
    # runs — so the cost is bounded per item rather than by how popular it is.
    holders = {n: [] for n in pool}
    for god_name, names in builds:
        for item in set(names) & pool:
            holders[item].append((god_name, names))
    samples = {n: [] for n in pool}
    for item, rows_for_item in holders.items():
        entry = table.get(item)
        if not entry or entry.status not in ("simulated", "partial"):
            continue
        for god_name, names in _even_sample(rows_for_item, max_samples):
            god = gods_by_name.get(god_name)
            if not god:
                continue
            try:
                d = sbs.passive_contribution(god, names, by_name, targets, item)
            except Exception:
                continue
            dmg = [d[k] for k in DAMAGE_KEYS if d.get(k) is not None]
            samples[item].append({
                "passive_damage": statistics.fmean(dmg) if dmg else 0.0,
                "passive_ehp_physical": d.get("ehp_physical") or 0.0,
                "passive_ehp_magical": d.get("ehp_magical") or 0.0,
            })

    rows = {}
    for name in sorted(pool):
        entry = table.get(name)
        status = entry.status if entry else None
        item = by_name.get(name) or {}
        if status in ("simulated", "partial"):
            obs = samples.get(name) or []
            if not obs:
                # Simulated but in no build at all: no context exists, so there
                # is no honest value. Recorded as such rather than guessed.
                rows[name] = {"status": "no-context", "n": 0,
                              "passive_damage": 0.0,
                              "passive_ehp_physical": 0.0,
                              "passive_ehp_magical": 0.0}
                continue
            row = {"status": status, "n": len(obs)}
            for col in ("passive_damage", "passive_ehp_physical", "passive_ehp_magical"):
                xs = [o[col] for o in obs]
                row[col] = round(statistics.median(xs), 3)
                row[f"{col}_min"] = round(min(xs), 3)
                row[f"{col}_max"] = round(max(xs), 3)
            rows[name] = row
        elif status == "not simulated":
            rows[name] = {"status": "refused", "n": 0, "passive_damage": 0.0,
                          "passive_ehp_physical": 0.0, "passive_ehp_magical": 0.0,
                          "why": (entry.assumptions or ("",))[0] if entry else ""}
        else:
            rows[name] = {"status": "none" if not (item.get("passive") or "").strip()
                          else "absent",
                          "n": 0, "passive_damage": 0.0,
                          "passive_ehp_physical": 0.0, "passive_ehp_magical": 0.0}
    return rows


def main(argv=None):
    ap = argparse.ArgumentParser(description="Measure per-item passive values")
    ap.add_argument("--write", action="store_true", help="write data/_passive_values.yaml")
    ap.add_argument("--items", nargs="*", help="limit to these items (for a quick probe)")
    args = ap.parse_args(argv)

    items = recommend.load_items()
    gods = recommend.load_gods()
    builds_by_god = {}
    for g in gods:
        for mode in recommend.MODES:
            try:
                note = recommend.load_build_note(g["name"], mode)
            except Exception:
                continue
            if mode == "Conquest":
                builds_by_god[g["name"]] = note
            else:
                base = builds_by_god.setdefault(g["name"], {"builds": []})
                base.setdefault("builds", []).extend(note.get("builds") or [])

    rows = measure(items, gods, builds_by_god, limit_items=args.items)
    by_status = {}
    for r in rows.values():
        by_status[r["status"]] = by_status.get(r["status"], 0) + 1
    print(f"items written: {len(rows)}")
    print(f"by status: {dict(sorted(by_status.items()))}")
    wide = [(n, r[f"passive_damage_max"] / r["passive_damage"])
            for n, r in rows.items()
            if r.get("n") and r.get("passive_damage") and r["passive_damage"] > 1]
    wide.sort(key=lambda x: -x[1])
    print("\nwidest damage spreads (max / median):")
    for n, ratio in wide[:8]:
        r = rows[n]
        print(f"  {n:26} n={r['n']:<3} median {r['passive_damage']:8.1f}  "
              f"{r['passive_damage_min']:8.1f}-{r['passive_damage_max']:8.1f}  {ratio:.1f}x")
    if args.write:
        import yaml
        OUT_PATH.write_text(
            "# Generated by `python -m smite.scripts.passive_values --write`.\n"
            "# Per-item passive values for `efficiency.PRICE_PASSIVE_SIM`.\n"
            "# Read the module docstring before editing by hand: the reference\n"
            "# context and the refused-is-an-explicit-zero rule are both there.\n"
            + yaml.safe_dump({"items": rows}, sort_keys=True, default_flow_style=False),
            encoding="utf-8", newline="\n")
        print(f"\nwrote {OUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
