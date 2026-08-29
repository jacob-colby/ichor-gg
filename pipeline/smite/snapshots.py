"""Per-refresh item-stat snapshots. Invisible plumbing: banks item cost/tier/
stats to a dated JSON file every refresh so a future patch-notes page can diff
item stats across patches.

THE STORE IS A CHANGE LOG, NOT A CALENDAR. `write_snapshot_if_changed` is the
entry point every caller should use, and the reason is `build_patch_report`:
it diffs CONSECUTIVE pairs and caps the report at 5 periods. Item cost/tier/
stats are wiki data, and the scheduled job pulls SmiteBrain only — so an
unconditional daily write banks ~30 byte-identical files a month, and within
five days of any real change that change has been pushed off the report by
five empty periods. The page would then read "Items have moved 0 times across
5 refreshes", which is worse than the empty state it replaced.

    python -m smite.snapshots          # bank today's, if item stats moved
    python -m smite.snapshots --date 2026-08-29
"""
import argparse
import json
import sys
from datetime import date as _date
from pathlib import Path

from smite.data_audit import STAT_VALUE_RE

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_ROOT = REPO_ROOT / "data"
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


def latest_snapshot_path(snapshots_dir: Path = SNAPSHOTS_DIR, exclude_date: str = None):
    """The newest stored snapshot by filename date, or None when the store is
    empty. `exclude_date` skips one stem so a re-run on a day that already
    banked a snapshot compares against the day before it, not against itself."""
    snapshots_dir = Path(snapshots_dir)
    if not snapshots_dir.exists():
        return None
    paths = sorted((p for p in snapshots_dir.glob("*.json") if p.stem != exclude_date),
                   key=lambda p: p.stem)
    return paths[-1] if paths else None


def write_snapshot_if_changed(items: list, date: str,
                              snapshots_dir: Path = SNAPSHOTS_DIR):
    """Bank a snapshot only when item cost/tier/stats differ from the newest
    one already stored. Returns the path written, or None when nothing moved.

    See the module docstring for why the unconditional write is the wrong
    default on a daily schedule."""
    snapshots_dir = Path(snapshots_dir)
    prior = latest_snapshot_path(snapshots_dir, exclude_date=date)
    if prior is not None and load_snapshot(prior) == snapshot_of(items):
        # A same-date file from an earlier run today is now redundant: leaving
        # it in place would put an identical consecutive pair in the store,
        # which is exactly the empty period this function exists to avoid.
        same_date = snapshots_dir / f"{date}.json"
        if same_date.exists():
            same_date.unlink()
        return None
    return write_snapshot(items, date, snapshots_dir)


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


def main(argv=None) -> int:
    """Bank today's item-stat snapshot if item stats moved. This is a step in
    the scheduled refresh rather than something `build_index` does for itself:
    the index READS the store, and a reader that also writes would bank a
    snapshot on every local rebuild, including rebuilds of test vaults."""
    # Imported here, not at module scope: `build_index` imports this module,
    # and `recommend` is the heavier half of the pipeline.
    from smite import recommend

    parser = argparse.ArgumentParser(description="Bank an item-stat snapshot")
    parser.add_argument("--date", default=_date.today().isoformat(),
                        help="snapshot date (default: today)")
    args = parser.parse_args(argv)

    path = write_snapshot_if_changed(recommend.load_items(), args.date)
    if path is None:
        prior = latest_snapshot_path()
        print(f"snapshots: item stats unchanged since {prior.stem} — nothing banked")
    else:
        print(f"snapshots: wrote {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
