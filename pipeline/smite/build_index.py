"""Walk the SMITE data + build folders and emit one index.json for the
second-monitor viewer to fetch. Re-run after any refresh, or on demand via
the viewer's "reload data" button — no file-watcher, content only changes
on patch days."""
import json
import shutil
from pathlib import Path

from smite import abilities, efficiency, notes, scoring, snapshots, tierlist


def _enrich_gods(gods, weights):
    """Attach the derived ability-leveling order to each god so the viewer's
    Info tab doesn't need the kit-scaling parser client-side. Shape:
    {"order": [20 slot names, one per level], "summary": {"max_order": [...],
    "ult_levels": [...]}} — see abilities.py. Heuristic, not scraped data."""
    for god in gods:
        order = abilities.ability_order(god, weights)
        # Gods whose kit didn't scrape any levelable abilities (stance gods:
        # Artio, Merlin, Ullr) get no key at all rather than a fabricated
        # order — the viewer hides the section instead of showing nonsense.
        if order:
            god["ability_order"] = {"order": order,
                                    "summary": abilities.summary(order, weights)}
    return gods


def popular_items(build_entry: dict) -> list:
    """Aggregate one community build entry's `slot_order` (and each slot's
    `alternates`) into a flat "what does this god's playerbase actually buy"
    list of `{name, pick_rate, win_rate}` — items, not an ordered build. An
    item seen more than once (as a slot pick here, an alternate there) is
    deduped, keeping the sighting with the highest pick_rate. Sorted by
    pick_rate descending, then name ascending so ties are deterministic.
    Pure function over a single dict — no disk access — so it's unit-testable
    on its own; see test_build_index.py."""
    best: dict = {}
    for slot in build_entry.get("slot_order") or []:
        if not isinstance(slot, dict):
            continue
        for candidate in [slot, *(slot.get("alternates") or [])]:
            name = candidate.get("name")
            rate = candidate.get("pick_rate")
            if not name or rate is None:
                continue
            if name not in best or rate > best[name]["pick_rate"]:
                best[name] = {"name": name, "pick_rate": rate,
                              "win_rate": candidate.get("win_rate")}
    return sorted(best.values(), key=lambda i: (-i["pick_rate"], i["name"]))


def _attach_popular_items(builds):
    """Attach `popular_items` (see above) to every community build entry so
    the viewer's god page can show the playerbase's most-picked items without
    re-aggregating `slot_order` client-side. Non-community entries (and gods
    with no community data at all) get no key — never a fabricated list."""
    for note in builds:
        for b in note.get("builds", []):
            if b.get("source") == "community":
                b["popular_items"] = popular_items(b)
    return builds


def _enrich_items(items, tags, eff=None):
    """Attach god-agnostic effect_tags + the efficiency verdict to each item.

    Ships the model's working, not just its label. The regression already
    computes a residual per item (`efficiency.efficiency_scores`); shipping
    only the three-bucket `tier` left the viewer able to say "Premium" but not
    *by how much*, which is the number a player actually needs to weigh an
    item's passive against its price.

    `residual` is rounded to whole gold and `predicted_cost` derived back from
    it, so `cost - predicted_cost == residual` holds exactly on screen — a
    surface that shows the arithmetic can't have it fail to add up.

    Items outside the scored pool (non-numeric cost, and tier-1 starters, which
    are passive-priced and deliberately sit out the fit) get `None` for both,
    never a fabricated zero.
    """
    if eff is None:
        eff = {}
        if efficiency.numeric_cost_items(items):
            eff, _ = efficiency.efficiency_scores(items)
    for it in items:
        it["effect_tags"] = tags.get(it["name"], [])
        scored = eff.get(it["name"])
        it["efficiency_tier"] = scored.get("tier") if scored else None
        if scored and isinstance(it.get("cost"), (int, float)):
            residual = round(scored["residual"])
            it["efficiency"] = {
                "predicted_cost": it["cost"] - residual,
                "residual": residual,
                "score": round(scored["score"], 4),
            }
        else:
            it["efficiency"] = None
    return items


def _god_item_scores(gods, builds, items, eff, weights, tags_map) -> dict:
    """Per-god base item scores for the viewer's draft-aware re-rank.

    The viewer is static, so it can't re-run scoring when a comp is entered; it
    instead applies a threat overlay to these shipped totals. Capped at the top
    `draft.score_cap` items per god — a bounded bonus can't promote a god's #60
    item, so shipping the whole matrix would just bloat the index."""
    cap = int((weights.get("draft") or {}).get("score_cap", 40))
    by_god = {}
    for b in builds:
        if b.get("mode") == "Conquest" and b.get("god") not in by_god:
            by_god[b["god"]] = b
    out = {}
    for god in gods:
        rows = scoring.score_god_items(
            god, items, by_god.get(god["name"], {}), eff, weights, tags_map)
        out[god["name"]] = {r["item"]: round(float(r["total"]), 4) for r in rows[:cap]}
    return out


def build_index(repo_root: Path) -> dict:
    data_root = repo_root / "data"
    gods_dir = data_root / "Gods"
    items_dir = data_root / "Items"
    builds_dir = repo_root / "data" / "builds"

    def _all(dir_path: Path) -> list:
        if not dir_path.exists():
            return []
        return [notes.read_note(p)[0] for p in sorted(dir_path.glob("*.md"))]

    tags_map = scoring.load_tags(data_root / "_tags.yaml")
    # One fit, reused: the tier list's "ours" item score has to be the same
    # continuous signal the item verdicts came from, not a second independent
    # regression. This used to run twice under a comment claiming it didn't.
    raw_items = _all(items_dir)
    eff, gold_values = ({}, {})
    if efficiency.numeric_cost_items(raw_items):
        eff, gold_values = efficiency.efficiency_scores(raw_items)
    items = _enrich_items(raw_items, tags_map, eff)
    weights = scoring.load_weights(data_root / "_weights.yaml")
    builds = _all(builds_dir)
    gods = _all(gods_dir)
    _enrich_gods(gods, weights)
    _attach_item_meta(items, builds)
    _attach_popular_items(builds)
    index = {"gods": gods, "items": items, "builds": builds,
             # The fitted marginal gold price of each stat, plus the fit's
             # `_intercept` — what every item costs before a single stat is
             # counted. Both are needed for a receipt to add up to
             # predicted_cost. Rounded to 2dp — these are prices, not weights.
             "item_gold_values": {k: round(v, 2) for k, v in sorted(gold_values.items())},
             "god_item_scores": _god_item_scores(gods, builds, items, eff, weights, tags_map),
             "draft": weights.get("draft", {}),
             "starters": weights.get("starters", []),
             "roster": _load_roster(data_root),
             "data_updated": _data_updated(gods, builds),
             "tierlist": tierlist.build_tierlist(gods, builds, items, eff),
             # Read snapshots under the vault being indexed, not the module-level
             # default — otherwise a tmp-vault caller (tests) would pick up the
             # real store once snapshots start accumulating.
             "patch_notes": snapshots.report_from_dir(data_root / "Analysis" / "snapshots")}
    data_patch = _load_data_patch(data_root)
    if data_patch:
        index["data_patch"] = data_patch
    return index


def _data_updated(gods, builds) -> str:
    """The most recent last_verified across gods + community builds — the real
    'data scraped on' date, so a rebuild alone doesn't churn the timestamp."""
    dates = [str(g.get("last_verified")) for g in gods if g.get("last_verified")]
    for note in builds:
        for b in note.get("builds", []):
            if b.get("source") == "community" and b.get("last_verified"):
                dates.append(str(b["last_verified"]))
    return max(dates) if dates else ""


def _load_data_patch(data_root: Path):
    """The scraped current SMITE 2 patch string (e.g. "Open Beta 39") from
    data/_patch.json (written by refresh.refresh_patch_version), or None if
    that file doesn't exist or is unreadable/malformed — the viewer omits
    the `data_patch` key entirely rather than showing a fabricated patch."""
    import json
    path = data_root / "_patch.json"
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        patch = data.get("patch") if isinstance(data, dict) else None
        return patch if isinstance(patch, str) else None
    except Exception:
        return None


def _load_roster(data_root: Path) -> list:
    """Full SMITE 2 god roster (name + optional thumb) for the dev add-god
    modal — includes gods not yet tracked. Optional; empty if not fetched."""
    import json
    path = data_root / "_roster.json"
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except Exception:
        return []


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


def _copy_icons(repo_root: Path, out_path: Path) -> None:
    """Copy every icon file next to the generated index.json so the viewer
    never has to reach outside its own public/ folder — a symlink would be
    fragile on Windows, and Vite's dev server doesn't serve arbitrary
    filesystem paths outside the project by default."""
    src_dir = repo_root / "data" / "_assets" / "icons"
    if not src_dir.exists():
        return
    dest_dir = out_path.parent / "icons"
    dest_dir.mkdir(parents=True, exist_ok=True)
    for icon_path in src_dir.glob("*.png"):
        shutil.copy2(icon_path, dest_dir / icon_path.name)


def write_index(repo_root: Path, out_path: Path) -> None:
    index = build_index(repo_root)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    # Frontmatter fields like `last_verified: 2026-07-16` round-trip through
    # yaml.safe_load as datetime.date objects, which json.dumps can't
    # serialize on its own — stringify anything json doesn't natively support.
    out_path.write_text(json.dumps(index, indent=2, default=str), encoding="utf-8")
    _copy_icons(repo_root, out_path)


if __name__ == "__main__":
    repo_root = Path(__file__).resolve().parents[2]
    write_index(repo_root, repo_root / "viewer" / "public" / "index.json")
    print("Wrote viewer/public/index.json")
