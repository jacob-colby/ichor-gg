"""Turn scored item rows into a suggested build: a constrained core plus a
situational-swap table. Greedy-with-rules, not optimization — transparent and
debuggable. vs_tag values match the viewer's archetype taxonomy so the existing
chip-highlighting works unchanged."""
from smite import scoring
from smite.efficiency import parse_stat_value


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


def assemble_core(rows, items_by_name, n=6, max_lifesteal=1, require=None,
                  stat_caps=None, coherence=0.0, stat_reference=None):
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

    if not coherence:
        # The original path, kept exactly: rows arrive sorted by -total, so
        # walking them once IS picking the best remaining item every time.
        for r in rows:
            if len(core) >= n:
                break
            _try_add(r["item"])
        return core

    # With coherence on, an item's worth depends on what is already in the
    # core, so the ranking is no longer fixed and has to be recomputed each
    # slot. Ties fall back to the row order, which is the score order, so this
    # degrades to the loop above as the multiplier flattens.
    remaining = [r for r in rows if r["item"] not in used]
    while len(core) < n and remaining:
        best_index = None
        best_score = None
        for index, r in enumerate(remaining):
            item = items_by_name.get(r["item"], {})
            score = r["total"] * coherence_multiplier(
                item, core_totals, stat_reference, coherence)
            if best_score is None or score > best_score:
                best_index, best_score = index, score
        r = remaining.pop(best_index)
        # A rejected candidate is dropped, not retried: every guard here is
        # monotone (boots taken, lifesteal spent, stat capped), so nothing that
        # fails now can start passing once the core has grown.
        _try_add(r["item"])
    return core


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
