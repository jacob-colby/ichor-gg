"""The hybrid build: the model's core, corrected where the community is clearly right.

Three builds now answer the same question three ways. The **community** build is
what people actually run. The **model** build is what efficiency and kit fit say,
having never seen a win rate. Neither is obviously right: the model can be
confidently wrong about an item nobody plays, and the community can be
confidently wrong about an item that is merely popular.

**The model keeps its convictions; evidence fills its uncertainty.** The top
`protected` slots of the model's core are untouchable. Below that line the model
has no real preference — measured across all 87 gods, the gap between its 6th
and 7th item by quality has a median of 0.000, and a *negative* mean, because
the assembler's boots and lifesteal caps routinely skip higher-quality items.
Those bottom slots are near-arbitrary, and they are exactly where a community
record with real evidence behind it should win.

  PROTECTED  The model's strongest picks are never overridden. Without this the
             hybrid collapses into the community build, which already exists on
             its own.

  EVIDENCE   Popularity is not evidence. A win rate is, but only with a
             denominator behind it — so a candidate is judged on the Wilson
             lower bound of its record, the same statistic the tier list uses,
             and against THIS GOD'S own win rate rather than a fixed bar.

An earlier version also required the model to already rate the candidate within
0.03 of its own pick. That sounded like caution and was actually incoherent: it
only corrected the model where the model was already nearly right, which is
where correction matters least. It fired for one god out of eighty-seven.

Every swap carries the reason it fired. A hybrid that cannot say why it
disagreed with the model is just a third opinion.
"""
from smite import assemble, tierlist


def _config(weights):
    cfg = (weights or {}).get("hybrid") or {}
    return (
        cfg.get("protected", 3),
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


def _reason(name, record, displaced, baseline, borrowed_from=None):
    """Why this swap fired, in the evidence's own terms.

    Names the SOURCE MODE when the record was borrowed. A Joust build reading
    "community 63% win over 44 matches" without saying whose community would
    present Conquest's 30-minute record as if it were measured in Joust, which
    is the one thing this project does not do with unmeasured modes."""
    where = f"{borrowed_from} community" if borrowed_from else "community"
    return (
        f"{where} {record['win_rate']:.0%} win over {record['matches']:,} matches "
        f"(vs {baseline:.0%} on this god), taking the model's weakest slot "
        f"from {displaced}"
    )


def hybrid_core(model_core, rows, community_entry, items_by_name, weights,
                max_lifesteal=1, n=6, reject_tags=None, tags_map=None,
                borrowed_from=None):
    """`(core, swaps)` — the model's core with community corrections applied.

    Returns the model core unchanged (and no swaps) when there is no community
    record to correct it with.

    `reject_tags` exists for BORROWED evidence. SmiteBrain publishes Conquest
    only, so Joust and Arena had no record to correct with and this returned
    the model core untouched for all 89 gods in each — a build the caller then
    declined to emit, which was right. Conquest's record is still the best
    evidence that exists about an item, but it is evidence about a 30-minute
    game with a ward economy, and some of it does not transfer:

      `stacking`      the value arrives too late to collect. Ten items —
                      Transcendence, Book of Thoth, Devourer's Gauntlet, Rage,
                      Gauntlet of Thebes among them. Arena is ~17.5 minutes.
      `ward-economy`  answers a Conquest-only problem. Arena has no wards at
                      all and both modes already price it at -0.25.

    Both lists come from judgements already measured and recorded elsewhere
    (`data/_tags.yaml`, `modes.<mode>.tag_bonus`) rather than from a new
    opinion invented here. A rejected candidate is dropped silently: it is not
    a swap that failed, it is evidence that does not apply.
    """
    protected, min_edge, max_swaps = _config(weights)
    records = community_records(community_entry)
    if not records:
        return list(model_core), []
    reject = set(reject_tags or ())
    tags_map = tags_map or {}

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

    # The model's own ranking of its core, worst first. Only the slots below
    # the protected line are open — the model's top picks are its convictions
    # and stay whatever the community says.
    ranked_core = sorted(model_core, key=lambda name: quality.get(name, 0.0))
    open_slots = ranked_core[:max(0, len(ranked_core) - protected)]

    # Candidates: community picks the model didn't take, best evidence first.
    candidates = [
        (name, rec) for name, rec in records.items()
        if name not in model_core and name in scored and rec["confidence"] is not None
        and not (reject & set(tags_map.get(name) or ()))
    ]
    candidates.sort(key=lambda kv: (-kv[1]["confidence"], kv[0]))

    accepted, displaced_names = [], []
    remaining = list(open_slots)
    for name, rec in candidates:
        if len(accepted) >= max_swaps or not remaining:
            break
        if rec["confidence"] < bar:
            continue                       # not confidently better than the god itself
        accepted.append((name, rec, remaining[0]))
        displaced_names.append(remaining.pop(0))

    if not accepted:
        return list(model_core), []

    # Rebuild through the real assembler rather than editing the list in place,
    # so boots and lifesteal caps hold after the swaps exactly as they did
    # before them. Accepted picks lead; the model's surviving core follows.
    order = ([scored[name] for name, _, _ in accepted]
             + [scored[n] for n in model_core if n not in displaced_names and n in scored]
             + [r for r in rows if r["item"] not in model_core])
    core = assemble.assemble_core(order, items_by_name, n=n, max_lifesteal=max_lifesteal,
                                  stat_caps=(weights or {}).get("stat_caps"),
                                  **assemble.coherence_args(list(items_by_name.values()), weights))

    swaps = [
        {"added": name, "removed": weakest,
         "reason": _reason(name, rec, weakest, baseline, borrowed_from)}
        for name, rec, weakest in accepted
        if name in core          # a pick the constraints rejected is not a swap
    ]
    return core, swaps
