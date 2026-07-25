"""Rank gods and items for the viewer's tier-list page (Phase 4).

Two independent signals per subject:
  ours       our continuous score (efficiency model for items, mean
             suggested-core slot score for gods) — always available where the
             underlying model produced a number.
  community  wiki-derived signal (item.meta.win_avg / god aspect_win_rate) —
             partial coverage; missing on purpose for the rest, never
             backfilled or zero-filled.

`assign_tiers` buckets by percentile of the *ranked* subset (entries that
have a numeric score for that key) so bucket sizes track the data present,
not an assumed total. Entries without a score for that key are left
unranked (`tier_<key>` = None) rather than dumped into the bottom bucket —
"no data" and "worst score" are different facts and must stay visually
distinct in the viewer.
"""
import math


def _suggested_conquest_core(god_name, builds):
    """The god's suggested Conquest 'core' archetype entry, or None."""
    for group in builds:
        if group.get("god") != god_name or group.get("mode") != "Conquest":
            continue
        for entry in group.get("builds", []):
            if entry.get("source") == "suggested" and entry.get("archetype") == "core":
                return entry
    return None


def _community_conquest_entry(god_name, builds):
    """The god's community Conquest build entry, or None."""
    for group in builds:
        if group.get("god") != god_name or group.get("mode") != "Conquest":
            continue
        for entry in group.get("builds", []):
            if entry.get("source") == "community":
                return entry
    return None


def god_rankings(gods, builds):
    """One entry per god: {name, role, damage_type, ours, community}.

    ours = mean of slot_scores[item]["total"] over the god's suggested
    Conquest core entry (None if there's no such entry, or it has no
    slot_scores).
    community = that god's community Conquest entry's aspect_win_rate
    (None if there's no community entry, or it lacks the field).
    Deterministic: sorted by name.
    """
    results = []
    for god in gods:
        name = god.get("name")

        ours = None
        core = _suggested_conquest_core(name, builds)
        if core:
            totals = [
                v.get("total") for v in (core.get("slot_scores") or {}).values()
                if isinstance(v, dict) and isinstance(v.get("total"), (int, float))
            ]
            if totals:
                ours = sum(totals) / len(totals)

        community = None
        comm_entry = _community_conquest_entry(name, builds)
        if comm_entry:
            community = comm_entry.get("aspect_win_rate")

        results.append({
            "name": name,
            "role": god.get("role"),
            "damage_type": god.get("damage_type"),
            "ours": ours,
            "community": community,
        })

    results.sort(key=lambda e: e["name"] or "")
    return results


def item_rankings(items, eff_scores):
    """One entry per item: {name, tier, efficiency_tier, ours, community}.

    ours = eff_scores.get(name, {}).get("score") (None if unscored — e.g.
    tier-1 starters are deliberately excluded from the efficiency model).
    community = item["meta"]["win_avg"] (None if no meta).
    Deterministic: sorted by name.
    """
    results = []
    for item in items:
        name = item.get("name")
        ours = (eff_scores.get(name) or {}).get("score")
        community = (item.get("meta") or {}).get("win_avg")
        results.append({
            "name": name,
            "tier": item.get("tier"),
            "efficiency_tier": item.get("efficiency_tier"),
            "ours": ours,
            "community": community,
        })

    results.sort(key=lambda e: e["name"] or "")
    return results


def _is_numeric(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def assign_tiers(entries, key):
    """Return NEW entry dicts with an added f"tier_{key}" field.

    Entries with a numeric entries[i][key] are ranked (descending, higher =
    better) and bucketed by percentile of that ranked subset: top 10% -> S,
    next 20% -> A, next 40% -> B, remainder -> C. Bucket boundaries use
    ceiling on the cumulative fraction so a single ranked entry lands in S
    and every ranked entry gets a bucket.

    Entries whose key is missing/non-numeric get tier_<key> = None
    (unranked) — never bucketed as C, never treated as zero.

    Ties are broken by name for a deterministic, stable order.
    """
    tier_key = f"tier_{key}"

    ranked = [e for e in entries if _is_numeric(e.get(key))]
    unranked = [e for e in entries if not _is_numeric(e.get(key))]

    ranked_sorted = sorted(ranked, key=lambda e: (-e[key], e.get("name") or ""))
    n = len(ranked_sorted)
    s_cut = math.ceil(n * 0.10)
    a_cut = math.ceil(n * 0.30)
    b_cut = math.ceil(n * 0.70)

    result = []
    for rank, entry in enumerate(ranked_sorted):
        if rank < s_cut:
            tier = "S"
        elif rank < a_cut:
            tier = "A"
        elif rank < b_cut:
            tier = "B"
        else:
            tier = "C"
        result.append({**entry, tier_key: tier})

    for entry in sorted(unranked, key=lambda e: e.get("name") or ""):
        result.append({**entry, tier_key: None})

    return result


def build_tierlist(gods, builds, items, eff_scores):
    """{"gods": [...], "items": [...]}, each entry carrying both tier_ours
    and tier_community so the viewer can switch source without recomputing."""
    return {
        "gods": assign_tiers(assign_tiers(god_rankings(gods, builds), "ours"), "community"),
        "items": assign_tiers(assign_tiers(item_rankings(items, eff_scores), "ours"), "community"),
    }
