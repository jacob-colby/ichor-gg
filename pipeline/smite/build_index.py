"""Walk the SMITE data + build folders and emit one index.json for the
second-monitor viewer to fetch. Re-run after any refresh, or on demand via
the viewer's "reload data" button — no file-watcher, content only changes
on patch days."""
import json
import shutil
from pathlib import Path

from smite import efficiency, notes, scoring


def _enrich_items(items, tags):
    """Attach god-agnostic effect_tags + efficiency_tier to each item so the
    viewer's tooltips can explain an item without recomputing anything."""
    eff = {}
    if efficiency.numeric_cost_items(items):
        eff, _ = efficiency.efficiency_scores(items)
    for it in items:
        it["effect_tags"] = tags.get(it["name"], [])
        it["efficiency_tier"] = eff.get(it["name"], {}).get("tier")
    return items


def build_index(vault_root: Path) -> dict:
    data_root = vault_root / "04. System" / "Data" / "SMITE"
    gods_dir = data_root / "Gods"
    items_dir = data_root / "Items"
    builds_dir = vault_root / "03. Workspaces" / "Gaming" / "SMITE 2" / "Builds"

    def _all(dir_path: Path) -> list:
        if not dir_path.exists():
            return []
        return [notes.read_note(p)[0] for p in sorted(dir_path.glob("*.md"))]

    items = _enrich_items(_all(items_dir), scoring.load_tags(data_root / "_tags.yaml"))
    weights = scoring.load_weights(data_root / "_weights.yaml")
    builds = _all(builds_dir)
    _attach_item_meta(items, builds)
    return {"gods": _all(gods_dir), "items": items, "builds": builds,
            "starters": weights.get("starters", [])}


def _attach_item_meta(items, builds):
    """Per-item community meta: average per-item win rate + how many gods run it,
    aggregated over Conquest community builds (win rate is per-god, so an average
    is the honest global signal for the items page)."""
    from collections import defaultdict
    wins = defaultdict(list)
    for note in builds:
        if note.get("mode") != "Conquest":
            continue
        for b in note.get("builds", []):
            if b.get("source") != "community":
                continue
            for slot in b.get("slot_order", []):
                wr = slot.get("win_rate") if isinstance(slot, dict) else None
                if wr is not None:
                    wins[slot["name"]].append(wr)
    for it in items:
        vals = wins.get(it["name"])
        if vals:
            it["meta"] = {"win_avg": round(sum(vals) / len(vals), 3), "gods": len(vals)}


def _copy_icons(vault_root: Path, out_path: Path) -> None:
    """Copy every icon file next to the generated index.json so the viewer
    never has to reach outside its own public/ folder — a symlink would be
    fragile on Windows, and Vite's dev server doesn't serve arbitrary
    filesystem paths outside the project by default."""
    src_dir = vault_root / "04. System" / "Data" / "SMITE" / "_assets" / "icons"
    if not src_dir.exists():
        return
    dest_dir = out_path.parent / "icons"
    dest_dir.mkdir(parents=True, exist_ok=True)
    for icon_path in src_dir.glob("*.png"):
        shutil.copy2(icon_path, dest_dir / icon_path.name)


def write_index(vault_root: Path, out_path: Path) -> None:
    index = build_index(vault_root)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    # Frontmatter fields like `last_verified: 2026-07-16` round-trip through
    # yaml.safe_load as datetime.date objects, which json.dumps can't
    # serialize on its own — stringify anything json doesn't natively support.
    out_path.write_text(json.dumps(index, indent=2, default=str), encoding="utf-8")
    _copy_icons(vault_root, out_path)


if __name__ == "__main__":
    vault_root = Path(__file__).resolve().parents[2]
    write_index(vault_root, vault_root / "viewer" / "public" / "index.json")
    print("Wrote viewer/public/index.json")
