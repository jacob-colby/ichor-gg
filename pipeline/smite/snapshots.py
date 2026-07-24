"""Per-refresh item-stat snapshots. Invisible plumbing: banks item cost/tier/
stats to a dated JSON file every refresh so a future patch-notes page can diff
item stats across patches.
"""
import json
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parents[2]
DATA_ROOT = VAULT_ROOT / "04. System" / "Data" / "SMITE"
SNAPSHOTS_DIR = DATA_ROOT / "Analysis" / "snapshots"


def snapshot_of(items: list) -> dict:
    """Map item name -> {cost, tier, stats} for every item with a name."""
    out = {}
    for it in items:
        name = it.get("name")
        if not name:
            continue
        out[name] = {
            "cost": it.get("cost"),
            "tier": it.get("tier"),
            "stats": it.get("stats") or {},
        }
    return out


def write_snapshot(items: list, date: str, snapshots_dir: Path = SNAPSHOTS_DIR) -> Path:
    """Write snapshot_of(items) as JSON to <snapshots_dir>/<date>.json."""
    snapshots_dir.mkdir(parents=True, exist_ok=True)
    out_path = snapshots_dir / f"{date}.json"
    out_path.write_text(
        json.dumps(snapshot_of(items), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    return out_path


def load_snapshot(path: Path) -> dict:
    """Read + parse a snapshot JSON file."""
    return json.loads(Path(path).read_text(encoding="utf-8"))


def diff_snapshots(old: dict, new: dict) -> dict:
    """Compare two snapshot_of() maps: {added, removed, changed}."""
    old_names = set(old)
    new_names = set(new)

    added = sorted(new_names - old_names)
    removed = sorted(old_names - new_names)

    changed = []
    for name in sorted(old_names & new_names):
        old_entry = old[name]
        new_entry = new[name]
        entry = {"name": name}

        if old_entry.get("cost") != new_entry.get("cost"):
            entry["cost"] = [old_entry.get("cost"), new_entry.get("cost")]

        old_stats = old_entry.get("stats") or {}
        new_stats = new_entry.get("stats") or {}
        stat_names = set(old_stats) | set(new_stats)
        stat_changes = {}
        for stat_name in sorted(stat_names):
            old_val = old_stats.get(stat_name)
            new_val = new_stats.get(stat_name)
            if old_val != new_val:
                stat_changes[stat_name] = [old_val, new_val]
        if stat_changes:
            entry["stats"] = stat_changes

        if len(entry) > 1:
            changed.append(entry)

    return {"added": added, "removed": removed, "changed": changed}
