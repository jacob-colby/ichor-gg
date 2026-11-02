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

WHICH PATCH A PERIOD BELONGS TO, AND WHY MOST PERIODS ARE NOT A PATCH. A
snapshot is dated by the refresh that banked it, not by the game, so a diff
between two snapshots is a patch only if the ITEM DATA was re-scraped under a
different patch between them. `data/_patch_history.json` records two dates per
label and they must not be confused:

    first_seen  when the GAME moved to this patch. Written unattended by
                `patch_feed` (Steam announcements) on the daily job, or by
                `record_patch` when a wiki refresh sees a label first.
    data_from   when Ichor's wiki-sourced item data was first scraped under
                this patch (`record_patch`, called by the wiki refresh only).
                Absent = item data has never been pulled under this patch.

Periods are attributed by `data_from` (`data_history`), never by
`first_seen`. Measured on the shipped store: OB41 and OB42 both landed inside
the 2026-08-01 -> 2026-08-29 period, so attributing by game date turns it into
"Open Beta 40 to Open Beta 42" and highlights 67 dataset additions as patch
additions — the exact falsehood the paragraph below describes. Items were last
scraped under OB40 (`last_verified: 2026-08-01`) and the period changed zero
items. A row with no `source` key predates this split and was written by the
wiki refresh, so its `first_seen` is its `data_from`. Each period carries
`patch_from`/`patch_to` and `crosses_patch`. A period that does NOT cross a patch is Ichor's data catching
up with the game (a hand-run `refresh --kind item`, a wiki correction, a
hotfix shipped under the same label), and the page says so instead of calling
it a patch. The only period in the store on 2026-11-02 is one of those:
2026-08-01 -> 2026-08-29, 67 "added" items that entered the DATASET in August
(starter components, relics, god-specific items), all within Open Beta 40.
Calling them new items, which the page did, was false.

HOW HIGHLIGHTS ARE CHOSEN (`highlights_for`). Automatic, no hand curation,
at most `HIGHLIGHT_LIMIT` per period, in this order:
  1. removed items, always (a removed item breaks every build that held it);
  2. added items, only when the period crosses a patch (otherwise "added"
     means "newly scraped", see above);
  3. changed items whose verdict is buff/nerf/mixed, by MAGNITUDE: the largest
     relative move of any one stat or of cost, |new-old|/|old|, with a stat
     that appears or disappears counting as 1.0. Ties break by name.
`adjusted` items (no numeric direction, e.g. reworded passive) never
highlight; they stay in the full list. Magnitude is relative on purpose: +10
Physical Power is huge on a 20-power component and noise on a 60-power
tier-3, and cost and stats are on different scales. It is a size, not a value
judgement, and it is not weighted by how many builds hold the item; that
would be a model input leaking into a changelog.

OFFICIAL LINKS. Two sources, and the hand-written one wins. `patch_feed`
stores the URL a Steam announcement gives (or a smite2.com URL quoted in its
body) as `official_url` on the history row; `data/_patch_links.yaml` maps a
label to a hand-verified URL and overrides it (`patch_links`). Both are
filtered to `is_official_url`: https on `OFFICIAL_HOSTS`, or a Steam news URL
for SMITE 2's app id. A Steam announcement counts as official because only the
developer can post to an app's announcement feed; `patch_feed` reads that feed
only, never Steam's external-news feeds. A URL built from a pattern is a guess
and is never written. A patch with no verified URL ships no link.
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
PATCH_HISTORY_PATH = DATA_ROOT / "_patch_history.json"
PATCH_LINKS_PATH = DATA_ROOT / "_patch_links.yaml"
HIGHLIGHT_LIMIT = 5
OFFICIAL_HOSTS = ("smite2.com", "www.smite2.com",
                  "hirezstudios.com", "www.hirezstudios.com")
STEAM_APP_ID = 2437170
# Steam hosts are official only on these paths: SMITE 2's own news pages, and
# the announcement-redirect form GetNewsForApp returns in its `url` field.
STEAM_NEWS_PATHS = {
    "store.steampowered.com": (f"/news/app/{STEAM_APP_ID}/",),
    "steamcommunity.com": (f"/games/{STEAM_APP_ID}/announcements/",
                           f"/app/{STEAM_APP_ID}/eventcomments/"),
    "steamstore-a.akamaihd.net": ("/news/externalpost/steam_community_announcements/",),
}


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


def _relative_move(old, new) -> float:
    """|new-old|/|old| for two stat/cost values; 1.0 when a side is missing or
    the old value is zero; 0.0 when either side has no number."""
    if old is None or new is None:
        return 1.0 if (old is None) != (new is None) else 0.0
    a, b = _parse_leading_number(old), _parse_leading_number(new)
    if a is None or b is None:
        return 0.0
    if a == b:
        return 0.0
    return 1.0 if a == 0 else abs(b - a) / abs(a)


def change_magnitude(entry: dict):
    """(magnitude, headline) for a changed entry: the largest relative move
    across cost and stats, and that move as "Stat old -> new"."""
    moves = []
    if entry.get("cost") is not None:
        old, new = entry["cost"]
        moves.append((_relative_move(old, new), "Cost", old, new))
    for stat, (old, new) in sorted((entry.get("stats") or {}).items()):
        moves.append((_relative_move(old, new), stat, old, new))
    if not moves:
        return 0.0, ""
    mag, stat, old, new = max(moves, key=lambda m: m[0])
    fmt = lambda v: "none" if v is None else str(v)
    others = sum(1 for m in moves if m[0] > 0) - 1
    more = f" (+{others} more)" if others > 0 else ""
    return mag, f"{stat} {fmt(old)} \u2192 {fmt(new)}{more}"


def highlights_for(period: dict, limit: int = HIGHLIGHT_LIMIT) -> list:
    """The biggest changes of one period; the rule is in the module docstring."""
    out = [{"name": n, "group": "items", "change": "removed",
            "headline": "Removed from the shop"} for n in period["removed"]]
    if period.get("crosses_patch"):
        out += [{"name": n, "group": "items", "change": "added",
                 "headline": "New item"} for n in period["added"]]
    ranked = []
    for e in period["changed"]:
        if e["verdict"] == "adjusted":
            continue
        mag, headline = change_magnitude(e)
        ranked.append({"name": e["name"], "group": "items", "change": e["verdict"],
                       "headline": headline, "magnitude": round(mag, 3)})
    ranked.sort(key=lambda h: (-h["magnitude"], h["name"]))
    return (out + ranked)[:limit]


def load_patch_history(path: Path = PATCH_HISTORY_PATH,
                       current_path: Path = None, fallback: bool = True) -> list:
    """[{patch, first_seen}] oldest first. With `fallback`, a missing history
    file reads as the single label in data/_patch.json."""
    path = Path(path)
    try:
        rows = json.loads(path.read_text(encoding="utf-8")) if path.exists() else None
    except (OSError, json.JSONDecodeError):
        rows = None
    if rows is None and not fallback:
        rows = []
    if rows is None:
        cur = Path(current_path) if current_path else path.parent / "_patch.json"
        try:
            d = json.loads(cur.read_text(encoding="utf-8"))
            rows = [{"patch": d["patch"], "first_seen": d["captured"]}]
        except (OSError, json.JSONDecodeError, KeyError, TypeError):
            rows = []
    rows = [r for r in rows if isinstance(r, dict) and r.get("patch") and r.get("first_seen")]
    return sorted(rows, key=lambda r: str(r["first_seen"]))


def patch_number(label):
    """N from "Open Beta N", or None. Labels compare by N, never by string
    ("Open Beta 9" > "Open Beta 10" as strings) or by date."""
    import re
    m = re.fullmatch(r"Open Beta (\d+)", str(label or ""))
    return int(m.group(1)) if m else None


def _save_history(rows: list, path: Path) -> None:
    rows = sorted(rows, key=lambda r: (str(r["first_seen"]), patch_number(r["patch"]) or -1))
    Path(path).write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")


def record_patch(patch: str, captured: str, path: Path = PATCH_HISTORY_PATH) -> bool:
    """The WIKI refresh saw `patch` on `captured`: item data now reflects it.

    Sets `data_from` on that label's row, appending the row if the game-side
    feed never recorded it. Returns True when the file changed. No fallback
    read: the caller has usually just overwritten _patch.json with this label."""
    path = Path(path)
    rows = load_patch_history(path, fallback=False)
    for row in rows:
        if row["patch"] == patch:
            if row.get("data_from") or "source" not in row:
                return False
            row["data_from"] = captured
            _save_history(rows, path)
            return True
    row = {"patch": patch, "first_seen": captured, "data_from": captured, "source": "wiki"}
    n = patch_number(patch)
    later = [r for r in rows if n is not None and (patch_number(r["patch"]) or -1) > n]
    if later:
        # The wiki lags the feed and this is an older label the feed missed.
        # Its game date is unknown; pin it no later than the next patch so
        # the history stays in game order.
        row["first_seen"] = min(captured, min(str(r["first_seen"]) for r in later))
    rows.append(row)
    _save_history(rows, path)
    return True


def data_history(history: list) -> list:
    """[{patch, first_seen}] keyed by when ITEM DATA was first scraped under
    each label — what snapshot periods are attributed by. See the module
    docstring for why game dates are the wrong key here."""
    out = []
    for row in history:
        day = row.get("data_from") or (row.get("first_seen") if "source" not in row else None)
        if day:
            out.append({"patch": row["patch"], "first_seen": str(day)})
    return sorted(out, key=lambda r: r["first_seen"])


def current_patch(history: list) -> dict:
    """The data/_patch.json body derived from history, or None. Deterministic
    in the history, so a run that recorded nothing rewrites nothing.

    `patch` is the game's current label (what the viewer shows next to the
    freshness date — community stats are pulled daily, so they are this
    patch's). `data_patch` is the label the wiki-sourced item and god data
    was scraped under, and is what `wiki_watch` compares against."""
    if not history:
        return None
    newest = max(history, key=lambda r: (patch_number(r["patch"]) or -1, str(r["first_seen"])))
    out = {"patch": newest["patch"], "captured": str(newest["first_seen"])}
    data = data_history(history)
    if data:
        out["data_patch"] = data[-1]["patch"]
    return out


def write_current_patch(history: list, path: Path) -> bool:
    """Write `current_patch(history)` to `path` when it differs. True if written."""
    body = current_patch(history)
    if body is None:
        return False
    path = Path(path)
    try:
        if json.loads(path.read_text(encoding="utf-8")) == body:
            return False
    except (OSError, ValueError):
        pass
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(body, indent=2), encoding="utf-8")
    return True


def patch_at(history: list, day: str):
    """The patch label current on `day` (ISO date), or None if `day` is
    before the first recorded label."""
    label = None
    for row in history:
        if str(row["first_seen"]) <= day:
            label = row["patch"]
    return label


def is_official_url(url) -> bool:
    from urllib.parse import urlparse
    if not isinstance(url, str):
        return False
    u = urlparse(url)
    if u.scheme != "https":
        return False
    if u.hostname in OFFICIAL_HOSTS:
        return True
    return any(u.path.startswith(p) for p in STEAM_NEWS_PATHS.get(u.hostname, ()))


def load_patch_links(path: Path = PATCH_LINKS_PATH) -> dict:
    """{patch label: official notes URL}, verified entries only."""
    import yaml
    path = Path(path)
    if not path.exists():
        return {}
    doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    links = doc.get("links") or {}
    return {str(k): v for k, v in links.items() if is_official_url(v)}


def patch_links(history: list, overrides: dict = None) -> dict:
    """Detected `official_url`s from the history, then the hand-written
    overrides on top. The override wins: it is the only one a person opened."""
    links = {r["patch"]: r["official_url"] for r in history
             if is_official_url(r.get("official_url"))}
    links.update(overrides or {})
    return links


def build_patch_report(snapshot_paths, limit: int = 5, history: list = None,
                       links: dict = None) -> list:
    """Diff each consecutive pair of snapshots (sorted by filename-stem
    date), newest period first, capped at `limit` periods. Fewer than 2
    snapshots -> []. Each period also carries its patch labels,
    `crosses_patch`, `highlights` and (crossing periods only) `official_url`."""
    history = data_history(history or [])
    links = links or {}
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
        frm, to = Path(old_path).stem, Path(new_path).stem
        p_from, p_to = patch_at(history, frm), patch_at(history, to)
        period = {
            "from": frm,
            "to": to,
            "patch_from": p_from,
            "patch_to": p_to,
            "crosses_patch": p_from is not None and p_to is not None and p_from != p_to,
            "added": diff["added"],
            "removed": diff["removed"],
            "changed": changed,
        }
        period["highlights"] = highlights_for(period)
        url = links.get(p_to) if period["crosses_patch"] else None
        if url:
            period["official_url"] = url
        periods.append(period)

    periods.reverse()  # newest first
    return periods[:limit]


def report_from_dir(snapshots_dir: Path = SNAPSHOTS_DIR, limit: int = 5,
                    data_root: Path = None) -> list:
    """Convenience wrapper: glob *.json in snapshots_dir and build the
    report. Missing directory or <2 snapshots -> []. Patch history and links
    are read from `data_root` (default: the snapshots dir's data root)."""
    snapshots_dir = Path(snapshots_dir)
    if not snapshots_dir.exists():
        return []
    root = Path(data_root) if data_root else snapshots_dir.parents[1]
    paths = sorted(snapshots_dir.glob("*.json"))
    history = load_patch_history(root / "_patch_history.json")
    return build_patch_report(
        paths, limit=limit, history=history,
        links=patch_links(history, load_patch_links(root / "_patch_links.yaml")))


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
