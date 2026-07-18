"""CLI: score SMITE 2 items and (later phases) assemble suggested builds.
Runs offline over local notes — no network. Run after refresh.py.

Phase A: `python -m smite.recommend --efficiency-report` writes a god-agnostic
item efficiency table.
"""
import argparse
import sys
from pathlib import Path

from smite import assemble, efficiency, notes, scoring

VAULT_ROOT = Path(__file__).resolve().parents[2]
DATA_ROOT = VAULT_ROOT / "04. System" / "Data" / "SMITE"
WEIGHTS_PATH = DATA_ROOT / "_weights.yaml"
TAGS_PATH = DATA_ROOT / "_tags.yaml"
BUILDS_ROOT = VAULT_ROOT / "03. Workspaces" / "Gaming" / "SMITE 2" / "Builds"

MODES = ["Conquest", "Joust"]

_FLAVOR_BLURB = {
    "core": "Top weighted-score core",
    "crit": "Crit / auto-attack skew",
    "burst": "Ability / burst skew",
    "bruiser": "Lifesteal bruiser skew",
    "anti-tank": "Full-penetration anti-tank skew",
}


def _rationale(archetype, rows, profile):
    meta = "" if profile.get("suppress_underrated") else " + win/pick"
    text = f"{_FLAVOR_BLURB.get(archetype, archetype)} (efficiency + fit{meta})."
    if profile.get("label"):
        text += f" {profile['label']}."
    if not profile.get("suppress_underrated"):
        underrated = [r["item"] for r in rows if r.get("underrated")]
        if underrated:
            text += " Underrated for this god: " + ", ".join(underrated) + "."
    return text


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


def load_gods():
    out = []
    for path in sorted((DATA_ROOT / "Gods").glob("*.md")):
        fm, _ = notes.read_note(path)
        if fm.get("name"):
            out.append(fm)
    return out


def load_build_note(god_name, mode="Conquest"):
    fm, _ = notes.read_note(BUILDS_ROOT / f"{god_name}-{mode}.md")
    return fm or {"builds": []}


def _stamp_community_starter(path, starter):
    """Set `starter` on the community entry of a Build note (role-based, so the
    community build shows the same recommended starter as the suggested ones)."""
    if not starter:
        return
    fm, body = notes.read_note(path)
    if not fm:
        return
    changed = False
    for b in fm.get("builds", []):
        if b.get("source") == "community":
            b["starter"] = starter
            changed = True
    if changed:
        notes.write_note(path, fm, body)


def god_report(god, items, god_build, weights, tags_map):
    eff_scores, _ = efficiency.efficiency_scores(items)
    rows = scoring.score_god_items(god, items, god_build, eff_scores, weights, tags_map)
    lines = [f"# {god['name']} — item scoring\n",
             "| Item | Total | Qual | Eff | Win | Pick | Fit | Tier | Tags | Flag |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        flag = "**UNDERRATED**" if r["underrated"] else ""
        tags = ", ".join(r["tags"])
        lines.append(f"| {r['item']} | {r['total']:.2f} | {r['quality']:.2f} | {r['efficiency']:.2f} | "
                     f"{r['win']:.2f} | {r['pick']:.2f} | {r['fit']:.2f} | {r['tier']} | "
                     f"{tags} | {flag} |")
    return "\n".join(lines) + "\n"


def build_suggested_entries(god, items, god_build, weights, tags_map, mode="Conquest"):
    eff_scores, _ = efficiency.efficiency_scores(items)
    items_by_name = {it["name"]: it for it in items}
    starter = scoring.pick_starter(god, weights)
    entries = []
    for flavor in [None] + scoring.eligible_flavors(god, weights):
        profile = scoring.resolve_profile(weights, mode, flavor)
        rows = scoring.score_god_items(god, items, god_build, eff_scores, weights, tags_map, profile)
        core = assemble.assemble_core(rows, items_by_name, n=6, max_lifesteal=profile["max_lifesteal"])
        swaps = assemble.situational_swaps(rows, items_by_name, tags_map, core=core)
        archetype = flavor or "core"
        entries.append({
            "source": "suggested",
            "archetype": archetype,
            "slot_order": core,
            "situational_swaps": swaps,
            "rationale": _rationale(archetype, rows, profile),
            **({"starter": starter} if starter else {}),
        })
    return entries


def main(argv=None):
    parser = argparse.ArgumentParser(description="Score SMITE 2 items and build suggestions")
    parser.add_argument("--efficiency-report", action="store_true",
                        help="write the god-agnostic item efficiency table")
    parser.add_argument("--all", action="store_true",
                        help="write a per-god scoring report for every god")
    parser.add_argument("--report-only", action="store_true",
                        help="write reports but do not modify Build notes")
    args = parser.parse_args(argv)

    if args.all:
        items = load_items()
        weights = scoring.load_weights(WEIGHTS_PATH)
        tags_map = scoring.load_tags(TAGS_PATH)
        untagged = [it["name"] for it in items if it["name"] not in tags_map]
        if untagged:
            print(f"[tags] {len(untagged)} untagged items: {', '.join(sorted(untagged))}")
        out_dir = DATA_ROOT / "Analysis"
        out_dir.mkdir(parents=True, exist_ok=True)
        for god in load_gods():
            build = load_build_note(god["name"])
            (out_dir / f"{god['name']}.md").write_text(
                god_report(god, items, build, weights, tags_map), encoding="utf-8")
            if not args.report_only:
                for mode in MODES:
                    # Conquest uses the community build note for win/pick lookups;
                    # Joust has no community data (SmiteBrain is Conquest-only).
                    mode_build = build if mode == "Conquest" else {"builds": []}
                    entries = build_suggested_entries(god, items, mode_build, weights, tags_map, mode)
                    notes.merge_suggested_entries(
                        BUILDS_ROOT / f"{god['name']}-{mode}.md", god["name"], mode, entries)
                # Conquest has the community build note; stamp the same
                # role-based starter onto its community entry.
                _stamp_community_starter(BUILDS_ROOT / f"{god['name']}-Conquest.md",
                                         scoring.pick_starter(god, weights))
        print("Wrote per-god scoring reports")
        return 0

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
