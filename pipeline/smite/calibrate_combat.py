"""CLI: check `combat.py` against real in-game numbers.

The gate on workstream B. Reads `data/_combat_observations.yaml`, runs each
case through the damage model, and reports per-case and worst-case error.

It is deliberately hard to pass by accident:

  * an empty file is a FAIL, not a pass — "no observations" must never read as
    "verified". A model nobody checked is exactly the state this exists to end.
  * example rows are ignored and reported as such, so the shipped placeholder
    cannot be mistaken for evidence.
  * the verdict is the WORST case, not the mean. An average hides the one
    penetration case that disproves the whole block.

Usage:
    python -m smite.calibrate_combat [--tolerance 0.02] [--file PATH]
"""
import argparse
import sys
from pathlib import Path

import re

import yaml

from smite import combat, notes

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PATH = REPO_ROOT / "data" / "_combat_observations.yaml"

# What the plan called for: reproduce reality within a stated tolerance. 2% is
# tight enough that a wrong penetration order cannot hide inside it — the
# published worked example moves protection from 85 to 75, which is a ~4%
# swing in final damage.
DEFAULT_TOLERANCE = 0.02


# ── Planning a run ────────────────────────────────────────────────────────
# The point of `--plan` is that a level-1 observation needs no guesswork about
# the target's protections. Three facts make it fully determined:
#
#   * no god has base Strength or Intelligence — checked across all 87, every
#     point of power comes from items. At level 1 with an empty inventory your
#     power is exactly 0, so an ability's damage is its flat rank-1 value with
#     no scaling term at all.
#   * every god's base protections are scraped, so a level-1 target's
#     protections are a number we already hold rather than something to read
#     off a screen that does not show it.
#   * item stats are scraped too, so buying exactly ONE item keeps the whole
#     thing determined while introducing penetration.
#
# So each planned case names a setup and the damage this model expects. Play
# it, write down what the game showed, and the gate does the rest.

_RANK1 = re.compile(r"^Damage:\s*([\d.]+)")
_SCALING = re.compile(r"([\d.]+)%\s+(Strength|Intelligence)")


def _first_damaging_ability(god):
    """The god's first CLEAN damaging ability: one whose damage is exactly a
    flat rank value plus stat scaling, and nothing else.

    The filter matters more than it looks. Thanatos's Death Scythe reads
    "Damage: 95" and "Damage Scaling: 85% Strength" — and also "Gods take 12.5%
    of their Max Health as bonus Physical Damage", which against a real target
    adds a term this model knows nothing about. An observation taken with it
    would show a large error and indict the mitigation formula for something
    that was never the formula's fault. His Soul Reap has no such line, so that
    is what gets suggested.

    Recognising the extra lines is possible because B1 recovered the wiki's
    colour coding: a damage-coloured detail that is not `Damage:` or `Damage
    Scaling:` is exactly the sort of hidden term to avoid.

    Returns (name, damage, damage_type, scaling) or None.
    """
    for a in god.get("abilities") or []:
        if "Basic Attack" in (a.get("slot") or ""):
            continue
        if not a.get("damage_type"):
            continue
        base = scaling = None
        extra = False
        kinds = a.get("detail_kinds") or []
        details = a.get("details") or []
        for kind, line in zip(kinds + [None] * len(details), details):
            line = line.strip()
            m = _RANK1.match(line)
            if m and base is None:
                base = float(m.group(1))
                continue
            if line.startswith("Damage Scaling:"):
                scaling = {stat: float(pct) / 100 for pct, stat in _SCALING.findall(line)}
                continue
            if kind in ("physical", "magical"):
                extra = True          # some other damage term we can't model
        if base is not None and not extra:
            return a["name"], base, a["damage_type"], scaling or {}
    return None


def _prot(target, damage_type):
    key = "physical_prot" if damage_type == "physical" else "magical_prot"
    return ((target.get("base_stats") or {}).get(key) or {}).get("base")


def plan_cases(gods_dir, items_dir, attacker, target):
    """Ready-to-run observation setups with the damage this model predicts."""
    def _load(d):
        out = {}
        for p in sorted(Path(d).glob("*.md")):
            fm, _ = notes.read_note(p)
            if fm.get("name"):
                out[fm["name"]] = fm
        return out

    gods, items = _load(gods_dir), _load(items_dir)
    if attacker not in gods or target not in gods:
        return None, f"unknown god: {attacker if attacker not in gods else target}"
    hit = _first_damaging_ability(gods[attacker])
    if not hit:
        return None, f"{attacker} has no ability with a parsed rank-1 damage value"
    name, base, dtype, scaling = hit
    prot = _prot(gods[target], dtype)
    if prot is None:
        return None, f"{target} has no scraped {dtype} protection"

    cases = [{"label": f"no items - {name} rank 1 vs {target} lvl 1",
              "setup": "Level 1. Buy NOTHING. Cast the ability once.",
              "raw": base, "protection": prot, "kwargs": {}}]

    # One item at a time, so raw damage stays computable: power comes only
    # from that item, and penetration only from it too.
    def add(item_name):
        item = items.get(item_name)
        if not item:
            return
        stats = item.get("stats") or {}
        power = sum(ratio * float(str(stats.get(stat, "0")).rstrip("%") or 0)
                    for stat, ratio in scaling.items())
        pen = str(stats.get("Penetration", "") or "")
        kw = {}
        if pen.endswith("%"):
            kw["pct_pen"] = float(pen.rstrip("%")) / 100
        elif pen:
            kw["flat_pen"] = float(pen)
        if not kw:
            return
        cases.append({
            "label": f"{item_name} only - {name} rank 1 vs {target} lvl 1",
            "setup": f"Level 1. Buy ONLY {item_name} ({item.get('cost')}g). Cast the ability once.",
            "raw": base + power, "protection": prot, "kwargs": kw})

    # A passive that fires on the cast would silently change the number being
    # recorded — The Crusher adds 35% of Strength on every ability hit, and
    # Obsidian Shard shreds protections on the first cast, which is precisely
    # the quantity under test. Rank candidates so the cleanest is offered
    # first: no passive at all, then one that cannot trigger on a single cast
    # in an empty practice range (kill/assist and on-use effects).
    def _passive_risk(item):
        passive = (item.get("passive") or "").lower()
        if not passive.strip():
            return 0
        if "ability hit" in passive or "ability cast" in passive:
            return 2
        return 1

    def _best(predicate):
        pool = [n for n, i in items.items()
                if predicate(str((i.get("stats") or {}).get("Penetration", "")))]
        # Risk first, then name, so the choice is deterministic run to run.
        return sorted(pool, key=lambda n: (_passive_risk(items[n]), n))

    for pool in (_best(str.isdigit), _best(lambda p: p.endswith("%"))):
        for n in pool:
            if _passive_risk(items[n]) < 2:
                add(n)
                break

    for c in cases:
        c["predicted"] = combat.damage_dealt(c["raw"], c["protection"], **c["kwargs"])
    return cases, None


def load_observations(path):
    """`(real, examples, pending)`.

    Three buckets, because a calibration file has three kinds of row and
    conflating them lets the gate lie in one direction or the other:

      real      scored, and the verdict is theirs
      example   the shipped placeholders. Never scored - made-up numbers must
                not be able to pass a gate.
      pending   REAL measurements the model does not yet reproduce. Recorded
                because they are evidence and deleting them would lose it,
                reported so they stay visible, but kept out of the verdict so
                one open question does not permanently red-light the terms
                that ARE confirmed. Anything here is a claim on someone's
                attention, not a result to be quietly carried.
    """
    if not path.exists():
        return [], [], []
    doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    rows = doc.get("observations") or []
    examples = [r for r in rows if r.get("example")]
    pending = [r for r in rows if r.get("pending") and not r.get("example")]
    real = [r for r in rows if not r.get("example") and not r.get("pending")]
    for r in real + pending:
        r.pop("example", None)
        r.pop("pending", None)
        r.pop("note", None)
    return real, examples, pending


def report_lines(result, tolerance, examples=0):
    lines = []
    for case in result["cases"]:
        ok = abs(case["rel_error"]) <= tolerance
        lines.append(
            f"  [{'ok ' if ok else 'OFF'}] {case['label'] or '(unlabelled)':44} "
            f"expected {case['expected']:>7,.0f}   model {case['actual']:>8,.2f}"
            f" -> shows {case['shown']:>6,.0f}   {case['rel_error']:+6.1%}")
    if examples:
        lines.append(f"  ({examples} example rows ignored - they are not evidence)")
    return lines


def main(argv=None):
    ap = argparse.ArgumentParser(description="Check combat.py against real numbers")
    ap.add_argument("--file", type=Path, default=DEFAULT_PATH)
    ap.add_argument("--tolerance", type=float, default=DEFAULT_TOLERANCE,
                    help=f"max acceptable relative error (default {DEFAULT_TOLERANCE:.0%})")
    ap.add_argument("--plan", nargs=2, metavar=("ATTACKER", "TARGET"),
                    help="print ready-to-run observation setups for a matchup")
    args = ap.parse_args(argv)

    if args.plan:
        data = REPO_ROOT / "data"
        cases, err = plan_cases(data / "Gods", data / "Items", *args.plan)
        if err:
            print(err)
            return 1
        print(f"Observation plan: {args.plan[0]} -> {args.plan[1]}")
        print()
        print("Both at LEVEL 1. The target buys nothing, so its protections are")
        print("its scraped base values. No god has base Strength or Intelligence,")
        print("so your power is exactly what your items give and nothing else.")
        print()
        for c in cases:
            print(f"  {c['label']}")
            print(f"    {c['setup']}")
            extra = "".join(f", {k}={v}" for k, v in c["kwargs"].items())
            print(f"    raw {c['raw']:.0f} vs {c['protection']:.2f} protection{extra}")
            print(f"    this model predicts {c['predicted']:.1f}"
                  "  <- record what the game shows")
            print()
        print("Add each as an entry in data/_combat_observations.yaml with the real")
        print("number as `expected`, then run this command with no arguments.")
        return 0

    real, examples, pending = load_observations(args.file)
    if not real:
        print(f"NO OBSERVATIONS in {args.file}")
        if examples:
            print(f"  ({len(examples)} example rows found - those are placeholders, not data)")
        print("\nThe combat model is UNVERIFIED. It reproduces two published worked")
        print("examples, but its penetration block is inferred from community")
        print("guides with SMITE 1 lineage and nothing has checked it against the")
        print("game. Do not ship anything that consumes combat.py until this")
        print("file has real numbers in it - see its header for how to take them.")
        return 1

    result = combat.calibrate_report(real)
    print(f"{result['n']} observations, tolerance {args.tolerance:.0%}\n")
    print("\n".join(report_lines(result, args.tolerance, len(examples))))

    if pending:
        open_report = combat.calibrate_report(pending)
        print(f"\n{len(pending)} PENDING - measured, not reproduced, not scored:")
        print("\n".join(report_lines(open_report, args.tolerance)))
        print("  These are the open questions. They do not gate anything, and")
        print("  they are not allowed to disappear either.")

    worst = result["worst_rel_error"]
    passed = worst <= args.tolerance
    print(f"\nworst case {worst:.1%} - {'PASS' if passed else 'FAIL'} "
          f"({len(pending)} pending)" if pending else
          f"\nworst case {worst:.1%} - {'PASS' if passed else 'FAIL'}")
    if not passed:
        print("\nThe model does not reproduce reality within tolerance. Per the plan,")
        print("stop here: B4-B6 inherit every error in this arithmetic. Compare the")
        print("failing cases — if the ones WITHOUT penetration pass and the ones")
        print("WITH it fail, the penetration block is where to look.")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
