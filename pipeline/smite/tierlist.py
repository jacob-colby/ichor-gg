"""Rank gods and items for the viewer's tier-list page (Phase 4), per game
mode (Task R2: Conquest + Joust).

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


# ── Confidence in a community win rate ──────────────────────────────────────
#
# Every community score we have is ONE ASPECT's win rate, and aspects vary
# enormously in how much they are actually played. Taken raw, the signal is
# worst exactly where the tier list leans hardest on it: win-rate spread across
# aspects picked under 10% of the time measured sd 0.083, against 0.053 for
# those picked 25%+. The extremes at the thin end are mostly sampling noise —
# and because the viewer ranks "biggest disagreement first", that noise was
# being promoted straight to the top of the page. Four of the six gods the home
# page headlined rested on aspects picked 2–5% of the time.
#
# Two guards, both deliberately conservative:
#
#   FLOOR      Below this pick rate the number is a rumour, not a measurement.
#              Such gods go UNRANKED — the same treatment as a god the source
#              never covered — never bucketed low. "No usable data" and "bad"
#              are different facts, which is the rule `assign_tiers` already
#              follows for missing scores.
#
#   SHRINKAGE  What survives the floor is pulled toward 0.5 in proportion to
#              how thin it is: adjusted = 0.5 + (raw - 0.5) * p / (p + K).
#              A 65%-pick aspect keeps ~81% of its distance from even; a
#              5%-pick one keeps ~25%. This is ordinary shrinkage toward the
#              prior — we have no better prior than "a coin flip" — and it
#              costs the confident aspects almost nothing.
#
# Pick rate is a PROXY for sample size, not sample size itself: SmiteBrain
# publishes neither match counts nor an elo band. If a source that reports
# either is ever wired up, this should be replaced by a real confidence
# interval rather than tuned.
MIN_PICK_RATE = 0.05
SHRINKAGE_K = 0.15

# ── The real thing: wins and losses ─────────────────────────────────────────
#
# The god index publishes `matches_won` / `matches_played`, so where we have
# it we can stop proxying confidence and measure it. `wilson_lower_bound` is
# the standard interval for a binomial proportion: it asks "how good can we be
# sure this god is?" rather than "what did the last few games happen to say".
#
# A 62% win rate over 133 matches and one over 2,000 are not the same claim,
# and this is the difference the tier list was previously blind to. It also
# subsumes the pick-rate guard above — that stays only as the fallback for
# notes predating the index scrape.
#
# z = 1.96 is the conventional 95% bound. Raising it punishes small samples
# harder; lowering it toward 1.0 is gentler. It is a knob on how much benefit
# of the doubt a thinly-played god gets, not a correctness dial.
WILSON_Z = 1.96
# Below this many matches the interval is so wide the god is better described
# as unmeasured. Nothing in the current index falls under it (the thinnest is
# 133) — it is a guard against a future patch's fresh data, not a filter.
MIN_MATCHES = 30


def wilson_lower_bound(won, played, z=WILSON_Z):
    """Lower bound of the Wilson score interval for `won` of `played`.

    Returns None when there is no usable sample. Ranking on this rather than
    the raw rate is what makes a big sample outrank a lucky small one — the
    bound rises toward the observed rate as evidence accumulates.
    """
    if not _is_numeric(won) or not _is_numeric(played):
        return None
    if played < MIN_MATCHES or won < 0 or won > played:
        return None
    p = won / played
    denominator = 1 + z * z / played
    centre = p + z * z / (2 * played)
    margin = z * math.sqrt(p * (1 - p) / played + z * z / (4 * played * played))
    return (centre - margin) / denominator


def community_score(entry):
    """One god's community signal, best evidence first.

    Prefers god-level wins/losses from the index — a real denominator, and the
    whole god rather than one aspect of it. Falls back to the aspect win rate
    behind its pick-rate guard, so a note written before the index scrape
    still yields something rather than dropping the god off the comparison.
    """
    if not entry:
        return None
    played = entry.get("god_matches_played")
    won = entry.get("god_matches_won")
    if _is_numeric(played) and _is_numeric(won):
        return wilson_lower_bound(won, played)
    return confident_win_rate(entry.get("aspect_win_rate"), entry.get("aspect_pick_rate"))


def confident_win_rate(win_rate, pick_rate):
    """A win rate discounted by how much the aspect is actually played.

    Returns None when there is no usable signal — no win rate, no pick rate,
    or a pick rate under `MIN_PICK_RATE` — so the caller leaves the entry
    unranked rather than ranking it badly.

    A missing pick rate is treated as unusable rather than as confident: the
    older notes predate pick-rate scraping, and assuming confidence for data
    we can't check is the failure this function exists to prevent.
    """
    if not _is_numeric(win_rate) or not _is_numeric(pick_rate):
        return None
    if pick_rate < MIN_PICK_RATE:
        return None
    return 0.5 + (win_rate - 0.5) * (pick_rate / (pick_rate + SHRINKAGE_K))


def _suggested_core(god_name, builds, mode="Conquest"):
    """The god's suggested `mode` 'core' archetype entry, or None."""
    for group in builds:
        if group.get("god") != god_name or group.get("mode") != mode:
            continue
        for entry in group.get("builds", []):
            if entry.get("source") == "suggested" and entry.get("archetype") == "core":
                return entry
    return None


def _community_entry(god_name, builds, mode="Conquest"):
    """The god's community `mode` build entry, or None."""
    for group in builds:
        if group.get("god") != god_name or group.get("mode") != mode:
            continue
        for entry in group.get("builds", []):
            if entry.get("source") == "community":
                return entry
    return None


def god_rankings(gods, builds, mode="Conquest"):
    """One entry per god: {name, role, damage_type, ours, community}.

    ours = mean of slot_scores[item]["total"] over the god's suggested
    `mode` core entry (None if there's no such entry, or it has no
    slot_scores — e.g. the god was never scraped for that mode at all).
    community = that god's community `mode` entry scored by
    `community_score` — the Wilson lower bound on god-level wins/losses where
    the index scrape supplied them, else the pick-rate-guarded aspect rate.
    None when there is no community entry for that mode, or no usable sample
    in it: unranked, never ranked badly.
    Conquest is the default mode for backwards compatibility with existing
    callers. Deterministic: sorted by name.
    """
    results = []
    for god in gods:
        name = god.get("name")

        ours = None
        core = _suggested_core(name, builds, mode)
        if core:
            totals = [
                v.get("total") for v in (core.get("slot_scores") or {}).values()
                if isinstance(v, dict) and isinstance(v.get("total"), (int, float))
            ]
            if totals:
                ours = sum(totals) / len(totals)

        community = None
        comm_entry = _community_entry(name, builds, mode)
        if comm_entry:
            community = community_score(comm_entry)

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


def _tierlist_for_mode(gods, builds, items, eff_scores, mode):
    """{"gods": [...], "items": [...]} for a single game mode, each entry
    carrying both tier_ours and tier_community so the viewer can switch
    source without recomputing.

    Items are not mode-dependent in the current data model (efficiency is a
    global stat/cost fit; community win-rate meta is aggregated once, over
    Conquest builds only, in build_index._attach_item_meta) — so item
    rankings are identical across modes today. `items`/`eff_scores` are
    still threaded through per-mode so that changes without breaking this
    function's shape."""
    return {
        "gods": assign_tiers(assign_tiers(god_rankings(gods, builds, mode), "ours"), "community"),
        "items": assign_tiers(assign_tiers(item_rankings(items, eff_scores), "ours"), "community"),
    }


def build_tierlist(gods, builds, items, eff_scores):
    """Per-mode tier lists: {"conquest": {...}, "joust": {...}}, each shaped
    like {"gods": [...], "items": [...]} (see `_tierlist_for_mode`).

    Backwards compatibility: the pre-per-mode shape — top-level "gods" and
    "items" keys — is kept alongside the new per-mode map, equal to the
    Conquest entry, so the existing viewer (which reads data.tierlist.gods /
    .items directly) keeps working unmodified.

    Joust's community signal is expected to be sparse: SmiteBrain has no
    Joust win/pick data, so most (real-world, not necessarily all — see
    R2 verification notes) Joust community entries carry no aspect_win_rate,
    surfacing as tier_community: null (unranked), never a fabricated value."""
    conquest = _tierlist_for_mode(gods, builds, items, eff_scores, "Conquest")
    joust = _tierlist_for_mode(gods, builds, items, eff_scores, "Joust")
    return {
        "gods": conquest["gods"],
        "items": conquest["items"],
        "conquest": conquest,
        "joust": joust,
    }
