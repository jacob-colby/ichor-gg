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

import yaml

from smite import combat

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PATH = REPO_ROOT / "data" / "_combat_observations.yaml"

# What the plan called for: reproduce reality within a stated tolerance. 2% is
# tight enough that a wrong penetration order cannot hide inside it — the
# published worked example moves protection from 85 to 75, which is a ~4%
# swing in final damage.
DEFAULT_TOLERANCE = 0.02


def load_observations(path):
    """`(real, examples)`. Rows flagged `example: true` are separated out
    rather than silently scored, so the placeholder file cannot pass."""
    if not path.exists():
        return [], []
    doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    rows = doc.get("observations") or []
    real = [r for r in rows if not r.get("example")]
    examples = [r for r in rows if r.get("example")]
    for r in real:
        r.pop("example", None)
    return real, examples


def report_lines(result, tolerance, examples=0):
    lines = []
    for case in result["cases"]:
        ok = abs(case["rel_error"]) <= tolerance
        lines.append(
            f"  [{'ok ' if ok else 'OFF'}] {case['label'] or '(unlabelled)':44} "
            f"expected {case['expected']:>9,.1f}   model {case['actual']:>9,.1f}   "
            f"{case['rel_error']:+7.1%}")
    if examples:
        lines.append(f"  ({examples} example rows ignored - they are not evidence)")
    return lines


def main(argv=None):
    ap = argparse.ArgumentParser(description="Check combat.py against real numbers")
    ap.add_argument("--file", type=Path, default=DEFAULT_PATH)
    ap.add_argument("--tolerance", type=float, default=DEFAULT_TOLERANCE,
                    help=f"max acceptable relative error (default {DEFAULT_TOLERANCE:.0%})")
    args = ap.parse_args(argv)

    real, examples = load_observations(args.file)
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

    worst = result["worst_rel_error"]
    passed = worst <= args.tolerance
    print(f"\nworst case {worst:.1%} — {'PASS' if passed else 'FAIL'}")
    if not passed:
        print("\nThe model does not reproduce reality within tolerance. Per the plan,")
        print("stop here: B4-B6 inherit every error in this arithmetic. Compare the")
        print("failing cases — if the ones WITHOUT penetration pass and the ones")
        print("WITH it fail, the penetration block is where to look.")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
