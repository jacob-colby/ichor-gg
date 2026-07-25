"""Per-refresh item-stat snapshots. Invisible plumbing: banks item cost/tier/
stats to a dated JSON file every refresh so a future patch-notes page can diff
item stats across patches.
"""
import json
from pathlib import Path

from smite.data_audit import STAT_VALUE_RE

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


def _parse_leading_number(value):
    """Parse the leading number out of a stat/cost value ('20%' -> 20.0).
    None or unparseable input yields None (no directional signal)."""
    if value is None:
        return None
    match = STAT_VALUE_RE.search(str(value))
    if match is None:
        return None
    return float(match.group())


def classify_verdict(entry: dict) -> str:
    """Classify a diff_snapshots "changed" entry as buff/nerf/mixed/adjusted
    from the direction of its numeric deltas. Cost is inverted (paying more
    is worse). Signals that can't be parsed (None side, non-numeric string)
    contribute nothing."""
    has_buff = False
    has_nerf = False

    for stat, (old_val, new_val) in (entry.get("stats") or {}).items():
        old_num = _parse_leading_number(old_val)
        new_num = _parse_leading_number(new_val)
        if old_num is None or new_num is None:
            continue
        if new_num > old_num:
            has_buff = True
        elif new_num < old_num:
            has_nerf = True

    cost = entry.get("cost")
    if cost is not None:
        old_cost, new_cost = cost
        old_num = _parse_leading_number(old_cost)
        new_num = _parse_leading_number(new_cost)
        if old_num is not None and new_num is not None:
            if new_num > old_num:
                has_nerf = True  # cost up = worse
            elif new_num < old_num:
                has_buff = True  # cost down = better

    if has_buff and has_nerf:
        return "mixed"
    if has_buff:
        return "buff"
    if has_nerf:
        return "nerf"
    return "adjusted"


def build_patch_report(snapshot_paths, limit: int = 5) -> list:
    """Diff each consecutive pair of snapshots (sorted by filename-stem
    date), newest period first, capped at `limit` periods. Fewer than 2
    snapshots -> []."""
    paths = sorted(snapshot_paths, key=lambda p: Path(p).stem)
    if len(paths) < 2:
        return []

    periods = []
    for old_path, new_path in zip(paths, paths[1:]):
        old = load_snapshot(old_path)
        new = load_snapshot(new_path)
        diff = diff_snapshots(old, new)
        changed = sorted(
            (dict(e, verdict=classify_verdict(e)) for e in diff["changed"]),
            key=lambda e: e["name"],
        )
        periods.append({
            "from": Path(old_path).stem,
            "to": Path(new_path).stem,
            "added": diff["added"],
            "removed": diff["removed"],
            "changed": changed,
        })

    periods.reverse()  # newest first
    return periods[:limit]


def report_from_dir(snapshots_dir: Path = SNAPSHOTS_DIR, limit: int = 5) -> list:
    """Convenience wrapper: glob *.json in snapshots_dir and build the
    report. Missing directory or <2 snapshots -> []."""
    snapshots_dir = Path(snapshots_dir)
    if not snapshots_dir.exists():
        return []
    paths = sorted(snapshots_dir.glob("*.json"))
    return build_patch_report(paths, limit=limit)
