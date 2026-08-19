"""Walk the SMITE data + build folders and emit one index.json for the
second-monitor viewer to fetch. Re-run after any refresh, or on demand via
the viewer's "reload data" button — no file-watcher, content only changes
on patch days."""
import json
import shutil
from pathlib import Path

import yaml

from smite import (abilities, damage_value, efficiency, notes, recommend, threat_kit,
                   scoring, snapshots, tierlist)


# Reference targets for the draft's damage overlay (B6), derived rather than
# picked: across the roster a level-20 god carries a median 76 physical / 56
# magical protection with no items, and the median protection item gives 30, so
# three of them is another ~90. "Squishy" and "three-item tank" are therefore
# roughly 70 and 170, and every real enemy sits between them.
SQUISHY_PROTECTION = 70.0
TANK_PROTECTION = 170.0


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
        # What this god's kit does TO you, counted off the ability text. The
        # draft used to grade a comp by `specializations` alone, which is a
        # three-word summary of a whole kit: `Healing` is on 9 gods and 42
        # actually heal, `Crowd Control` on 8 and 80 land hard CC, and nothing
        # labels player-made walls at all. See threat_kit.py.
        god["threat_kit"] = threat_kit.god_threat_kit(god)
        # How much this god's own archetype wants PROTECTIONS, 0..1. The draft
        # applies its defensive stat bonuses in proportion to this.
        #
        # `draft.stat_bonus` is keyed on the ENEMY's damage type and was applied
        # flat, so a Hunter facing a magical comp got Magical Protection at
        # weight 1.0 against Penetration's 0.6 — the draft was answering "they
        # are magical" with "so become tankier", for a god whose entire build
        # is damage. Measured across 10 damage gods vs a 4-tank/4-magical comp:
        # protection items in the core went 12 -> 25, with Apollo and Anhur
        # both gaining Genji's Guard.
        #
        # The role map already knows the answer and is the same map that governs
        # fit, so this is consistency rather than a new opinion: Support and
        # Guardian read 1.0, Solo/Warrior/Brawler 0.5, Carry and Mid 0.0.
        role_map = scoring._role_stat_map(god, weights)
        god["defense_affinity"] = round(max(
            role_map.get("Physical Protection", 0.0),
            role_map.get("Magical Protection", 0.0)), 3)
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

    Items outside the scored pool (non-numeric cost, tier-1 starters, and
    statless items, none of which the regression can price — see
    `efficiency.efficiency_pool`) get `None` for both, never a fabricated zero.

    `comparable` says whether the residual belongs on a ranking against every
    other item. A god-specific item's price IS meaningful — Ashwhorl Acorn
    really does give 3,211 gold of stats for 2,000 — but 86 of the 87 gods
    cannot buy it, so letting it head a global "best value" board answers a
    question nobody asked. It stays visible and priced, and sorts with its
    own kind.
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
                "comparable": not it.get("god"),
            }
        else:
            it["efficiency"] = None
    return items


def _god_item_scores(gods, builds, items, eff, weights, tags_map) -> dict:
    """`{god: {mode: {item: score}}}` — base item scores for the viewer's
    draft-aware re-rank, one table per mode.

    The viewer is static, so it can't re-run scoring when a comp is entered; it
    instead applies a threat overlay to these shipped totals. Capped at the top
    `draft.score_cap` items per god — a bounded bonus can't promote a god's #60
    item, so shipping the whole matrix would just bloat the index.

    THIS USED TO BE CONQUEST-ONLY, under a draft page that has offered a Joust
    toggle the whole time. The toggle switched which build NOTE was displayed
    and left the suggested core scored by Conquest's weights, so none of the
    per-mode work reached the draft at all: `modes.joust.tag_bonus` never
    applied, and Eye of Providence — which that table penalises at -0.25 for
    exactly this reason — sat at slot 4 of Achilles' Joust core. A mode
    selector that changes the label and not the model is worse than no mode
    selector.

    Each mode is scored through its own `resolve_profile`, and against its OWN
    build note rather than Conquest's. Joust and Arena have no community note
    at all (SmiteBrain is Conquest-only), which is harmless here because both
    modes zero the `win` and `pick` weights that would read it — but passing
    Conquest's note in would create a silent dependency on those weights
    staying zero, and they are a config value, not a law.

    All three modes ship, including Arena, which is not a draft mode today: the
    whole table is 92 KB against a 5 MB index, and the alternative is encoding
    a viewer decision in the pipeline.

    A god with a hand-tuned entry under `aspects` in `_weights.yaml` also gets
    a `<mode>:aspect` table, so the draft's aspect toggle moves the build the
    same way the god page's does. Only the 7 gods with an overlay get one —
    the other 65 with an aspect have nothing to score differently, and
    emitting an identical copy would tell the viewer they did."""
    cap = int((weights.get("draft") or {}).get("score_cap", 40))
    by_god_mode = {}
    for b in builds:
        key = (b.get("god"), b.get("mode"))
        if key not in by_god_mode:
            by_god_mode[key] = b
    aspects = weights.get("aspects") or {}
    out = {}
    for god in gods:
        per_mode = {}
        overlay = aspects.get(god["name"])
        for mode in recommend.MODES:
            for suffix, asp in (("", None), (":aspect", overlay)):
                if suffix and not asp:
                    continue
                profile = scoring.resolve_profile(weights, mode, None,
                                                  aspect_overlay=asp)
                rows = scoring.score_god_items(
                    god, items, by_god_mode.get((god["name"], mode), {}), eff,
                    weights, tags_map, profile)
                per_mode[mode.lower() + suffix] = {
                    r["item"]: round(float(r["total"]), 4) for r in rows[:cap]}
        out[god["name"]] = per_mode
    return out


def _god_item_damage(gods, items, weights) -> dict:
    """Per-god, per-item damage gained against a squishy and against a tank.

    B5's arithmetic, shipped where a TARGET actually exists. As a global fit
    signal it was useless — measured, and it halved the validation gate,
    because it cannot price defence. What it does that nothing else can is
    reverse an item's ranking depending on who you are hitting: on Scylla,
    Spear of Desolation gains 276 damage against 20 protection and 79 against
    250, while Void Shard climbs from 8.8 to 13.7.

    The draft is the one surface that knows the enemy, so these are the two
    endpoints and the viewer interpolates between them by how tanky the
    entered comp actually is.

    EACH COLUMN is normalised separately, against the best item for that
    target. Sharing one denominator would be the obvious thing and would be
    useless: mitigation shrinks every number against a tank, so every item
    would show a loss and the ranking would never change. What the draft needs
    is the RELATIVE shift — which items move up the order as the enemy hardens
    — and that only survives if each target is scored on its own scale.

    A god whose kit didn't parse gets no entry rather than a fabricated one;
    the overlay simply doesn't fire for them.
    """
    cap = int((weights.get("draft") or {}).get("score_cap", 40))
    out = {}
    for god in gods:
        if not damage_value.ability_damage_components(god):
            continue
        pairs = {}
        for item in items:
            if not scoring.is_buildable(item, god):
                continue
            low = damage_value.item_damage_gain(god, item, SQUISHY_PROTECTION)
            high = damage_value.item_damage_gain(god, item, TANK_PROTECTION)
            if low > 0 or high > 0:
                pairs[item["name"]] = (low, high)
        if not pairs:
            continue
        top_low = max(v[0] for v in pairs.values()) or 1.0
        top_high = max(v[1] for v in pairs.values()) or 1.0
        ranked = sorted(pairs.items(), key=lambda kv: -max(kv[1]))[:cap]
        out[god["name"]] = {n: [round(lo / top_low, 3), round(hi / top_high, 3)]
                            for n, (lo, hi) in ranked}
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
    _attach_item_meta(items, builds, _load_community_items(data_root))
    _attach_popular_items(builds)
    index = {"gods": gods, "items": items, "builds": builds,
             # The fitted marginal gold price of each stat, plus the fit's
             # `_intercept` — what every item costs before a single stat is
             # counted. Both are needed for a receipt to add up to
             # predicted_cost. Rounded to 2dp — these are prices, not weights.
             "item_gold_values": {k: round(v, 2) for k, v in sorted(gold_values.items())},
             "god_item_scores": _god_item_scores(gods, builds, items, eff, weights, tags_map),
             # B6: what each item is worth against a squishy vs a tank, for the
             # one surface that knows who you are actually fighting.
             "god_item_damage": _god_item_damage(gods, items, weights),
             # The viewer re-ranks a core client-side and has to apply the same
             # sustain cap the pipeline applied when it assembled one. It used
             # to hand-copy this rule's conditions into TypeScript, where the
             # two could drift silently; shipping the rule keeps one authority.
             "draft": {**weights.get("draft", {}),
                       "lifesteal_caps": weights.get("lifesteal_caps", [])},
             # The method page states the model's own weights. Shipping them
             # rather than restating them in TSX means the page cannot describe
             # a blend the pipeline stopped using.
             "method": {"signals": weights.get("signals", {}),
                        "kit_blend": weights.get("kit_blend", 0.5),
                        "underrated": weights.get("underrated", {})},
             # Mode order, so the viewer presents Conquest first rather than
             # whatever order the build filenames happened to sort in — which
             # put Arena at the head the moment it was added.
             "modes": list(recommend.MODES),
             "starters": weights.get("starters", []),
             "roster": _load_roster(data_root),
             "data_updated": _data_updated(gods, builds),
             "tierlist": tierlist.build_tierlist(gods, builds, items, eff),
             "community_source": _community_source(builds),
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


def _load_community_items(data_root):
    """The item win/loss table written by `refresh.refresh_item_index`, or {}
    before it has ever run."""
    path = data_root / "_community_items.json"
    if not path.exists():
        return {}
    try:
        return (json.loads(path.read_text(encoding="utf-8")) or {}).get("items") or {}
    except (ValueError, OSError):
        return {}


def _attach_item_meta(items, builds, community_items=None):
    """Per-item community meta.

    Prefers the item index: the item's own record against a real denominator.
    The fallback — the mean of per-god win rates over gods whose community
    build happens to list the item — is unweighted, so an item appearing in
    two builds counted as loudly as one in forty, and it inherits the aspect
    figures the god path already moved away from. `matches` is the tell: where
    it is present the score can be weighed, where it is absent it cannot.
    """
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
        indexed = (community_items or {}).get(it["name"])
        if indexed and indexed.get("matches_played"):
            it["meta"] = {
                "win_avg": round(indexed["win_rate"], 3),
                "matches": indexed["matches_played"],
                "matches_won": indexed.get("matches_won"),
            }
            continue
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


def _community_source(builds):
    """Provenance for the community comparison: which rank band, drawn from
    how many matches, over what window.

    A win rate without its rank band and dates is not a claim anyone can
    check — "the community" means something different in Obsidian+ than in
    Deity, and a fortnight-old window means something different the week a
    patch lands. Every god carries identical values (they come from one index
    fetch), so this belongs to the index rather than repeated 87 times.

    None before the index scrape has ever run, so the viewer can omit the line
    rather than print an empty one.
    """
    for group in builds:
        for entry in group.get("builds", []):
            if entry.get("source") == "community" and entry.get("god_division"):
                return {
                    "division": entry["god_division"],
                    "window_start": entry.get("god_window_start"),
                    "window_end": entry.get("god_window_end"),
                    "matches_analyzed": entry.get("god_matches_analyzed"),
                }
    return None


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
