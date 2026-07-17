"""CLI: score SMITE 2 items and (later phases) assemble suggested builds.
Runs offline over local notes — no network. Run after refresh.py.

Phase A: `python -m smite.recommend --efficiency-report` writes a god-agnostic
item efficiency table.
"""
import argparse
import sys
from pathlib import Path

from smite import efficiency, notes

VAULT_ROOT = Path(__file__).resolve().parents[2]
DATA_ROOT = VAULT_ROOT / "04. System" / "Data" / "SMITE"


def load_items():
    items_dir = DATA_ROOT / "Items"
    out = []
    for path in sorted(items_dir.glob("*.md")):
        frontmatter, _ = notes.read_note(path)
        if frontmatter.get("name"):
            out.append(frontmatter)
    return out


def efficiency_report(items):
    scores, _gold = efficiency.efficiency_scores(items)
    ranked = sorted([it for it in items if it["name"] in scores],
                    key=lambda it: -scores[it["name"]]["score"])
    lines = ["# Item efficiency\n", "| Item | Cost | Tier | Residual | Score |", "|---|---|---|---|---|"]
    for it in ranked:
        s = scores[it["name"]]
        lines.append(f"| {it['name']} | {it['cost']} | {s['tier']} | {s['residual']:+.0f} | {s['score']:.2f} |")
    return "\n".join(lines) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description="Score SMITE 2 items and build suggestions")
    parser.add_argument("--efficiency-report", action="store_true",
                        help="write the god-agnostic item efficiency table")
    args = parser.parse_args(argv)

    if args.efficiency_report:
        items = load_items()
        out_dir = DATA_ROOT / "Analysis"
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "_efficiency.md"
        out_path.write_text(efficiency_report(items), encoding="utf-8")
        print(f"Wrote {out_path}")
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
