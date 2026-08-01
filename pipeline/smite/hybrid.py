"""The hybrid build: the model's core, corrected where the community is clearly right.

Three builds now answer the same question three ways. The **community** build is
what people actually run. The **model** build is what efficiency and kit fit say,
having never seen a win rate. Neither is obviously right: the model can be
confidently wrong about an item nobody plays, and the community can be
confidently wrong about an item that is merely popular.

The hybrid starts from the model and defers to the community in exactly one
situation — where **the model is near-indifferent and the community's evidence is
strong**. Both halves matter:

  INDIFFERENCE  If the model rates a community pick far below its own choice,
                that disagreement is the product; overriding it would just
                reproduce the community build under a different name.

  EVIDENCE      Popularity is not evidence. A win rate is, but only with a
                denominator behind it — so a candidate is judged on the Wilson
                lower bound of its record, the same statistic the tier list
                uses, and not on the raw rate.

Every swap carries the reason it fired. A hybrid that cannot say why it
disagreed with the model is just a third opinion.
"""
from smite import assemble, tierlist


def _config(weights):
    cfg = (weights or {}).get("hybrid") or {}
    return (
        cfg.get("indifference", 0.03),
        cfg.get("min_edge", 0.0),
        cfg.get("max_swaps", 3),
    )


def community_records(community_entry):
    """`{item: {win_rate, pick_rate, matches, confidence}}` from a community entry.

    The source publishes a per-item win rate and pick rate but no per-item
    denominator, so matches are derived as `pick_rate × god_matches_played`.
    That is an estimate and is treated as one: it feeds the Wilson bound, whose
    whole job is to distrust small numbers, so an over-estimate is the only way
    it could mislead — and pick rate cannot exceed 1.
    """
    if not community_entry:
        return {}
    played_total = community_entry.get("god_matches_played")
    if not isinstance(played_total, (int, float)) or played_total <= 0:
        return {}

    out = {}
    for slot in community_entry.get("slot_order") or []:
        if not isinstance(slot, dict):
            continue  # a suggested-style flat name list; no record to read
        name = slot.get("name")
        win, pick = slot.get("win_rate"), slot.get("pick_rate")
        if not name or not isinstance(win, (int, float)) or not isinstance(pick, (int, float)):
            continue
        played = int(round(pick * played_total))
        confidence = tierlist.wilson_lower_bound(int(round(win * played)), played)
        out[name] = {
            "win_rate": win, "pick_rate": pick,
            "matches": played, "confidence": confidence,
        }
    return out


def _reason(name, record, displaced, quality, baseline):
    """Why this swap fired, in the evidence's own terms."""
    gap = abs(quality.get(name, 0.0) - quality.get(displaced, 0.0))
    return (
        f"community {record['win_rate']:.0%} win over {record['matches']:,} matches "
        f"(vs {baseline:.0%} on this god); the model had it within "
        f"{gap:.2f} of {displaced}"
    )


def hybrid_core(model_core, rows, community_entry, items_by_name, weights,
                max_lifesteal=1, n=6):
    """`(core, swaps)` — the model's core with community corrections applied.

    Returns the model core unchanged (and no swaps) when there is no community
    record to correct it with, which is every Joust build.
    """
    indifference, min_edge, max_swaps = _config(weights)
    records = community_records(community_entry)
    if not records:
        return list(model_core), []

    # The bar is THIS GOD'S own win rate, not a fixed number. An item winning
    # 56% on a god who wins 52% overall is evidence; the same 56% on a god who
    # wins 60% overall is below par and must not override anything. A constant
    # threshold cannot tell those apart, and would have let strong gods drag
    # every mediocre item of theirs into the build.
    baseline = community_entry.get("god_win_rate")
    if not isinstance(baseline, (int, float)):
        return list(model_core), []
    bar = baseline + min_edge

    quality = {r["item"]: r.get("quality", 0.0) for r in rows}
    scored = {r["item"]: r for r in rows}

    # The model's own ranking of its core, worst first — the weakest slot is
    # the one a correction should take.
    ranked_core = sorted(model_core, key=lambda name: quality.get(name, 0.0))

    # Candidates: community picks the model didn't take, best evidence first.
    candidates = [
        (name, rec) for name, rec in records.items()
        if name not in model_core and name in scored and rec["confidence"] is not None
    ]
    candidates.sort(key=lambda kv: (-kv[1]["confidence"], kv[0]))

    accepted, displaced_names = [], []
    remaining = list(ranked_core)
    for name, rec in candidates:
        if len(accepted) >= max_swaps or not remaining:
            break
        if rec["confidence"] < bar:
            continue                       # not confidently better than the god itself
        weakest = remaining[0]
        if quality.get(name, 0.0) < quality.get(weakest, 0.0) - indifference:
            continue                       # the model is not indifferent here
        accepted.append((name, rec, weakest))
        displaced_names.append(weakest)
        remaining.pop(0)

    if not accepted:
        return list(model_core), []

    # Rebuild through the real assembler rather than editing the list in place,
    # so boots and lifesteal caps hold after the swaps exactly as they did
    # before them. Accepted picks lead; the model's surviving core follows.
    order = ([scored[name] for name, _, _ in accepted]
             + [scored[n] for n in model_core if n not in displaced_names and n in scored]
             + [r for r in rows if r["item"] not in model_core])
    core = assemble.assemble_core(order, items_by_name, n=n, max_lifesteal=max_lifesteal)

    swaps = [
        {"added": name, "removed": weakest,
         "reason": _reason(name, rec, weakest, quality, baseline)}
        for name, rec, weakest in accepted
        if name in core          # a pick the constraints rejected is not a swap
    ]
    return core, swaps
