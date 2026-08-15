"""Turn scored item rows into a suggested build: a constrained core plus a
situational-swap table. Greedy-with-rules, not optimization — transparent and
debuggable. vs_tag values match the viewer's archetype taxonomy so the existing
chip-highlighting works unchanged."""
from smite import scoring
from smite.efficiency import parse_stat_value, stat_key


def _amount(raw):
    """A stat's magnitude, percent sign or not. 0 when unparseable, so a
    malformed value can't silently look like a cap-filling contribution."""
    return parse_stat_value(raw) or 0.0


def _is_boots(item):
    return "Movement Speed" in (item.get("stats") or {})


def _is_lifesteal(item, tags):
    stats = item.get("stats") or {}
    return "sustain" in (tags or []) or any("Lifesteal" in s for s in stats)


def coherence_multiplier(item, core_totals, stat_reference, strength):
    """How much of this item's stat line is still worth buying, given what the
    core already holds. 1.0 = nothing here is duplicated; lower = more of it is.

    This is the only place the recommender scores a build rather than an item.
    Every other signal — efficiency, win, pick, fit — is computed for one item
    against one god and knows nothing about the other five slots, so the core
    was six independent arg-maxes and the sixth pick could not tell that the
    first five had already bought its whole stat line. Measured on the shipped
    builds: Anubis's core carried Penetration on 6 slots of 6 where his own
    playerbase carries it on 4, and Cernunnos — whose community build is a
    basic-attack carry, Attack Speed on 5 slots — was handed 4 Penetration
    items and one Attack Speed.

    Diminishing returns, not a cap. `stat_caps` in `assemble_core` is the hard
    version of this idea and it was measured to change 0 of 261 cores, because
    a hard cap only fires when a stat is *completely* wasted and no real build
    gets there. The soft version fires where the waste actually happens: the
    third Penetration item is not worthless, it is just worth less than the
    first, and that is enough to lose a slot to an item bringing something new.

    Each stat is measured in typical rolls of itself — `scoring.stat_reference`
    gives the pool median, so 250 Health and 40 Strength are commensurable —
    and weighted by how much of the item that stat IS, so a token 5 Strength
    on a protection item cannot drag the whole item's verdict. `strength` 0
    makes this a no-op, which is what keeps it tunable rather than baked in."""
    stats = item.get("stats") or {}
    weighted, total = 0.0, 0.0
    for stat, raw in stats.items():
        amount = _amount(raw)
        if not amount:
            continue
        # A stat with no reference is one no other item carries; treat this
        # item as its own yardstick rather than skipping it, so a unique stat
        # counts as exactly one roll instead of silently weighing nothing.
        ref = stat_reference.get(stat) or amount
        share = amount / ref
        held = core_totals.get(stat, 0.0) / ref
        weighted += share * (1.0 / (1.0 + held))
        total += share
    if not total:
        return 1.0
    return (1.0 - strength) + strength * (weighted / total)


def time_value_multiplier(item_cost, gold_before, economy):
    """How much of the match's SCORING WINDOW this item is actually active for.

    The recommender builds one shape of core for every mode. Measured across the
    shipped builds it costs 15,545g in Arena, 15,452g in Joust and 15,472g in
    Conquest - the same build for a 17-minute ticket race and a 35-minute Titan
    push. This is the term that tells them apart.

    IT IS NOT ABOUT AFFORDING THE ITEMS. That was the obvious theory and the
    numbers refute it: gold income scales with match length, so the FRACTION of
    the match spent at each item count is near-identical everywhere (62% / 62%
    / 61% of the match at three items or fewer). Arena's documented 15 gold/sec
    spooling alone funds the entire core by ~16 minutes of a 15-20 minute match,
    before a single kill. You finish six items in every mode.

    IT IS ABOUT WHEN THE GAME IS SCORED.

      Arena  500 tickets falling from 0:00. Every kill and every minion pushed
             scores immediately, so value accrues UNIFORMLY across the match.
             A sixth item bought at minute 16 of 17 is present for almost none
             of the scoring.
      Joust  a Titan, like Conquest - the win happens at the end, so late items
             keep most of their worth. Faster than Conquest, and its income is
             only 90% spooled (the rest is farm, so a losing player may never
             reach six), which is why it decays a little rather than not at all.
      Conquest  the Titan cannot fall early. The sixth item is present for the
             fight that ends the game and is worth full value. No decay.

    `uniformity` is that axis, 0 = purely endgame, 1 = purely uniform. The
    weight is item-specific through COST: an expensive item completes later, so
    it is active for less of the window. That produces a preference for earlier
    power without ever asserting "cheap is good", which the economy data does
    not support.

    Every number lives in `modes.<mode>.economy` in _weights.yaml with its
    source and evidence tier. Returns 1.0 - a no-op - when a mode has no
    economy block, so a mode nobody has researched is left alone.
    """
    if not economy:
        return 1.0
    gpm = economy.get("gold_per_min") or 0
    minutes = economy.get("match_minutes") or 0
    uniformity = economy.get("uniformity", 0.0)
    if gpm <= 0 or minutes <= 0 or uniformity <= 0:
        return 1.0
    finish_gold = gold_before + (item_cost or 0)
    completed_at = max(0.0, (finish_gold - economy.get("start_gold", 0)) / gpm)
    active = max(0.0, 1.0 - completed_at / minutes)
    return (1.0 - uniformity) + uniformity * active


def conversion_score_bonus(item, core_totals, reference, gold_values, span):
    """Score delta for a converter, given what the core ACTUALLY feeds it.

    `price_conversions` values these items against a typical build, which is
    one pass and has no fixed point to converge — see
    `passives.conversion_grants`. The cost of that safety is that a build which
    is NOT typical is priced as if it were: Transcendence gets 3% of a median
    500 mana where Ullr's own community build carries 1,550, and Book of Thoth
    reaches 0 model cores against 22 community builds.

    This is the correction, applied against the core being assembled. It does
    NOT refit the gold model: prices are a property of the game, not of one
    god's build, so the fitted values stand and only the item's own residual
    moves. `efficiency_scores` carries `span` for exactly this — score is
    `(hi - residual) / span`, so a gold delta divides straight into a score
    delta.

    Symmetric on purpose. A converter in a build that feeds it LESS than the
    reference is marked down, not merely left alone; otherwise this is a
    one-way ratchet that only ever argues for more converters.
    """
    from smite import passives
    if not reference or not gold_values or not span:
        return 0.0
    # Asked for EVERY candidate at every slot of every pass, and 222 of the 226
    # items convert nothing — so the cheap cached lookup comes first and the two
    # dict comprehensions below only run for the four that matter. Without this
    # `calibrate` spent most of its time building stat maps to multiply by zero.
    rules = passives.stat_conversions(item)
    if not rules:
        return 0.0
    carried = {stat_key(name, raw) for name, raw in (item.get("stats") or {}).items()
               if parse_stat_value(raw) is not None}
    own = {k: parse_stat_value(v) or 0.0 for k, v in (item.get("stats") or {}).items()}
    delta_gold = 0.0
    for source, rate, per_unit in rules:
        # The item is not in the core yet, so its own contribution to the
        # source stat is added — you own it the moment you buy it.
        actual = core_totals.get(source, 0.0) + own.get(source, 0.0)
        extra = (actual - reference.get(source, 0.0)) * rate
        for stat, per in per_unit.items():
            # Same amplify-only rule the reference pricing uses; see
            # `passives.conversion_grants`.
            if stat not in carried:
                continue
            delta_gold += extra * per * gold_values.get(stat, 0.0)
    # A negative residual is a bargain, so a POSITIVE gold delta raises score.
    return delta_gold / span


def assemble_core(rows, items_by_name, n=6, max_lifesteal=1, require=None,
                  stat_caps=None, coherence=0.0, stat_reference=None, economy=None,
                  conversion=None, seed_totals=None, score_key="total"):
    """Highest-total items filling n slots: at most one boots, at most
    `max_lifesteal` lifesteal/sustain items, no duplicates. rows must be
    pre-sorted by -total (score_god_items already does). When `require`
    {stat, min} is given, the core is seeded with the top-scored items carrying
    that stat (up to `min`, honoring the same rules) before filling by score.

    `stat_caps` {stat: cap} refuses an item whose only contribution is a stat
    the core has already capped out. Tenacity caps at 50 and the four items
    carrying it give 15 each, so a fourth was buying nothing; Plating and
    Dampening cap at 35 with the same shape. The gold model can't see this —
    no single item comes close to a cap, so pricing a point linearly is right
    at the item level and only wrong once they stack.

    Deliberately narrow: it fires only when the whole contribution is wasted.
    An item that would take Tenacity from 45 to 60 still buys the 5 points
    that fit, and refusing it would be a worse error than allowing the overflow.

    It currently changes nothing — measured across all 261 build notes, zero
    cores differ with it on. Four Tenacity items would have to out-score
    everything else in the pool, and none do. It is kept as a guard rather than
    deleted because the rule is real and cheap: a patch that buffs those items,
    or a defensive flavor that weights them up, would start stacking dead
    stats silently. Do not read it as load-bearing.
    """
    core, used = [], set()
    have_boots = [False]
    lifesteal_count = [0]
    capped_totals = {}
    # Every stat the core holds so far, for `coherence_multiplier`. Separate
    # from `capped_totals`, which only tracks the handful of stats with real
    # in-game caps.
    core_totals = {}
    # Gold committed so far, so `time_value_multiplier` knows when the next
    # purchase actually completes.
    spent = [0]
    _row_tags = {r["item"]: r.get("tags") for r in rows}
    stat_reference = stat_reference or {}

    def _capped_out(item):
        """True when the item has nothing left to offer: every stat it carries
        is a capped one, and all of them are already maxed.

        The "every stat" half matters. An item bringing maxed Tenacity *and*
        40 Strength is not dead weight — the Tenacity is wasted but the item
        is not, and rejecting it would lose the Strength to save nothing."""
        stats = item.get("stats") or {}
        if not stats or not stat_caps:
            return False
        if any(s not in stat_caps for s in stats):
            return False                      # carries something uncapped
        return all(capped_totals.get(s, 0.0) >= stat_caps[s] for s in stats)

    def _try_add(name):
        if name in used or len(core) >= n:
            return False
        item = items_by_name.get(name, {})
        if _is_boots(item):
            if have_boots[0]:
                return False
        is_ls = _is_lifesteal(item, _row_tags.get(name))
        if is_ls and lifesteal_count[0] >= max_lifesteal:
            return False
        if _capped_out(item):
            return False
        # Every guard has passed — only now record the item's effects, so a
        # rejected candidate can't leave the boots flag or a stat total set.
        if _is_boots(item):
            have_boots[0] = True
        if is_ls:
            lifesteal_count[0] += 1
        for stat in (stat_caps or {}):
            raw = (item.get("stats") or {}).get(stat)
            if raw:
                capped_totals[stat] = capped_totals.get(stat, 0.0) + _amount(raw)
        for stat, raw in (item.get("stats") or {}).items():
            core_totals[stat] = core_totals.get(stat, 0.0) + _amount(raw)
        spent[0] += item.get("cost") or 0
        core.append(name)
        used.add(name)
        return True

    if require:
        stat, need = require.get("stat"), require.get("min", 0)
        seeded = 0
        for r in rows:
            if seeded >= need:
                break
            item = items_by_name.get(r["item"], {})
            if stat in (item.get("stats") or {}) and _try_add(r["item"]):
                seeded += 1

    # Stat totals carried in from a previous pass, so a converter can be
    # valued against the build it will actually end up in rather than only
    # against what happens to precede it in this pass's greedy order.
    if seed_totals:
        core_totals.update(seed_totals)

    if not coherence and not economy and not conversion:
        # The original path, kept exactly: rows arrive pre-sorted, so walking
        # them once IS picking the best remaining item every time.
        for r in rows:
            if len(core) >= n:
                break
            _try_add(r["item"])
        return core

    # With coherence or a mode economy on, an item's worth depends on what is
    # already in the core — its stat overlap, and the gold already committed
    # ahead of it — so the ranking is no longer fixed and has to be recomputed
    # each slot. Ties fall back to the row order, which is the score order, so
    # this degrades to the loop above as the multipliers flatten.
    remaining = [r for r in rows if r["item"] not in used]
    while len(core) < n and remaining:
        best_index = None
        best_score = None
        for index, r in enumerate(remaining):
            item = items_by_name.get(r["item"], {})
            # `score_key`, not always "total". The `model` archetype hands in
            # rows sorted by QUALITY — efficiency and fit only, the build the
            # model would pick if it had never seen a win rate — and the walk
            # path honours that ordering for free because it never re-ranks.
            # This path does re-rank, so reading "total" here put win and pick
            # straight back into the one build whose entire point is that they
            # are absent. It shipped that way for Joust and Arena the moment
            # `economy` turned this path on, and stayed invisible only because
            # those modes zero win and pick anyway.
            score = r.get(score_key, r["total"])
            if coherence:
                score *= coherence_multiplier(item, core_totals, stat_reference,
                                              coherence)
            if economy:
                score *= time_value_multiplier(item.get("cost"), spent[0], economy)
            if conversion:
                score += conversion["weight"] * conversion_score_bonus(
                    item, core_totals, conversion["reference"],
                    conversion["gold_values"], conversion["span"])
            if best_score is None or score > best_score:
                best_index, best_score = index, score
        r = remaining.pop(best_index)
        # A rejected candidate is dropped, not retried: every guard here is
        # monotone (boots taken, lifesteal spent, stat capped), so nothing that
        # fails now can start passing once the core has grown.
        _try_add(r["item"])
    return core


def assemble_core_converged(rows, items_by_name, passes=2, **kwargs):
    """`assemble_core`, re-run until the core it produces stops changing.

    Only meaningful with `conversion`. Pass one prices a converter against a
    TYPICAL build; every pass after prices it against the core pass one
    actually produced, which is the whole point — Transcendence is worth 3% of
    500 mana in the abstract and 3% of 1,550 in the build its own players run.

    IT MAY NOT CONVERGE, and that is why this is a loop with a cap rather than
    a recursion. Adding Transcendence raises the value of mana, which pulls in
    more mana items, which raises Transcendence again; the fixed point can be a
    two-cycle instead of a point. Every core seen is remembered, so a repeat is
    detected as an oscillation and the FIRST core is returned — the
    conservative one, priced against a typical build, which is the answer that
    does not depend on which half of the cycle the loop happened to stop on.

    Returns (core, info) where info records passes run and whether it settled,
    so a caller can report the oscillation instead of hiding it.
    """
    core = assemble_core(rows, items_by_name, **kwargs)
    if not kwargs.get("conversion") or passes < 2:
        return core, {"passes": 1, "converged": True, "oscillated": False}

    first = list(core)
    seen = [frozenset(core)]
    for index in range(2, passes + 1):
        totals = {}
        for name in core:
            for stat, raw in (items_by_name.get(name, {}).get("stats") or {}).items():
                totals[stat] = totals.get(stat, 0.0) + _amount(raw)
        nxt = assemble_core(rows, items_by_name, seed_totals=totals, **kwargs)
        key = frozenset(nxt)
        if key == seen[-1]:
            return nxt, {"passes": index, "converged": True, "oscillated": False}
        if key in seen:
            return first, {"passes": index, "converged": False, "oscillated": True}
        seen.append(key)
        core = nxt
    return first, {"passes": passes, "converged": False, "oscillated": False}


def build_order(core, items_by_name, tags_map, weights):
    """Recommended purchase order for a core (heuristic — we have no real
    build-path data). stage = default + sum(tag_stage for the item's tags) +
    cost*cost_weight; sorted ascending (ties: cost, then name)."""
    cfg = (weights or {}).get("build_order") or {}
    default_stage = cfg.get("default_stage", 0)
    cost_weight = cfg.get("cost_weight", 0)
    tag_stage = cfg.get("tag_stage") or {}

    def stage(name):
        item = items_by_name.get(name, {})
        tags = tags_map.get(name) or []
        s = default_stage + sum(tag_stage.get(t, 0) for t in tags)
        cost = item.get("cost") or 0
        return (s + cost * cost_weight, cost, name)

    return sorted(core, key=stage)


def flex_slots(core, rows, count=2):
    """The `count` least-essential core items — the lowest-scored ones (rows are
    score-descending, so the core's score order is its order in `rows`). Returns
    a subset of `core`."""
    order = [r["item"] for r in rows if r["item"] in set(core)]
    n = min(count, len(order))
    return order[-n:] if n else []


# (vs_tag, needed_tag, protection_stat, human label). protection_stat is used
# instead of a tag for the burst situations (protections are a stat, not a
# passive effect).
_SITUATIONS = [
    ("heavy_cc", "cc-immunity", None, "CC-immunity / cleanse"),
    ("magic_heavy", None, "Magical Protection", "magical protection"),
    ("physical_heavy", None, "Physical Protection", "physical protection"),
    ("sustain", "anti-heal", None, "anti-heal"),
]


def _item_qualifies(name, items_by_name, tags_map, needed_tag, prot_stat, row_tags=None):
    item = items_by_name.get(name, {})
    item_tags = tags_map.get(name) or row_tags or []
    if needed_tag and needed_tag in item_tags:
        return True
    if prot_stat and parse_stat_value((item.get("stats") or {}).get(prot_stat)) is not None:
        return True
    return False


def situational_swaps(rows, items_by_name, tags_map, core=None):
    """For each matchup situation, the best item to bring IN that isn't already
    in the core (and isn't already claimed by an earlier situation, so the four
    rows don't all collapse to the same item). A swap you already build isn't a
    swap — if the core already contains a qualifying item, the row says so
    instead of telling you to add what you have; if the pool has none at all,
    the row says that. vs_tag values match the viewer's archetype taxonomy."""
    core = list(core or [])
    core_set = set(core)
    chosen = set()
    table = []
    for vs_tag, needed_tag, prot_stat, label in _SITUATIONS:
        pick = None
        for r in rows:
            name = r["item"]
            if name in core_set or name in chosen:
                continue
            if _item_qualifies(name, items_by_name, tags_map, needed_tag, prot_stat, r.get("tags")):
                pick = name
                break
        if pick:
            chosen.add(pick)
            table.append({"vs_tag": vs_tag, "swap": f"{pick} — {label}", "swap_item": pick})
            continue
        covered = next((n for n in core
                        if _item_qualifies(n, items_by_name, tags_map, needed_tag, prot_stat)), None)
        if covered:
            table.append({"vs_tag": vs_tag, "swap": f"core already covers {label} ({covered})", "swap_item": None})
        else:
            table.append({"vs_tag": vs_tag, "swap": f"(no {label} available in pool)", "swap_item": None})
    return table

def conversion_args(weights, eff_scores, gold_values):
    """The `conversion` context for `assemble_core`, or {} when off.

    Built in one place so every caller values a converter identically. The
    weight is the EFFICIENCY signal's own weight: this adjusts an item's
    efficiency score, so it enters the blended total exactly as efficiency
    does, rather than as a free-floating bonus with its own scale."""
    w = weights or {}
    if not (w.get("price_conversions") and w.get("conversion_passes", 1) > 1):
        return {}
    span = next((v.get("span") for v in eff_scores.values() if v.get("span")), None)
    if not span:
        return {}
    return {"conversion": {
        "reference": dict(w.get("conversion_reference") or {}),
        "gold_values": gold_values,
        "span": span,
        "weight": (w.get("signals") or {}).get("efficiency", 0.35),
    }}


def coherence_args(items, weights):
    """The `coherence` / `stat_reference` pair for `assemble.assemble_core`.

    Both callers need them and both must agree: the strength is a single
    tunable in _weights.yaml, and the reference magnitudes must be measured
    over the SAME item pool every time or the same build assembles differently
    depending on who asked for it."""
    strength = (weights or {}).get("coherence", 0.0)
    if not strength:
        return {}
    return {"coherence": strength, "stat_reference": scoring.stat_reference(items)}
