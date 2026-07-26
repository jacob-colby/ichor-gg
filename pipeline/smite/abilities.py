"""Ability upgrade order: derives a 20-level ability-point sequence from each
god's parsed damage scaling. No source scrapes a real leveling order, so this
is a heuristic — label it as such wherever it's shown. Reuses kit.py's
scaling-line regex rather than re-parsing 'Damage Scaling: N% <Stat>' text a
second time. See the 2026-07-25 site-polish design spec, section D."""
from smite import kit

_DEFAULTS = {"ult_levels": [5, 9, 13, 17], "early_points": 1, "max_levels": 20}
_ABILITY_RANK_CAP = 5  # SMITE convention (abilities have 5 ranks) — not a config knob.


def _cfg(weights):
    cfg = dict(_DEFAULTS)
    cfg.update((weights or {}).get("abilities") or {})
    return cfg


def _slot_kind(slot):
    s = str(slot or "").strip().lower()
    if s == "passive":
        return "passive"
    if "basic attack" in s:
        return "basic"
    if "ultimate" in s:
        return "ultimate"
    return "ability"


def _non_ult_abilities(god):
    """Ability dicts that take level-up points, in kit order. Basic Attack and
    Passive never take points; only the first Ultimate slot is treated as the
    ultimate (a couple of scrapes carry a stray duplicate)."""
    return [ab for ab in (god.get("abilities") or [])
            if ab.get("slot") and _slot_kind(ab.get("slot")) == "ability"]


def _ultimate_slot(god):
    for ab in god.get("abilities") or []:
        if ab.get("slot") and _slot_kind(ab.get("slot")) == "ultimate":
            return ab["slot"]
    return "Ultimate"


def _ability_scaling_total(ability):
    """Sum of every 'Damage Scaling: N% <Stat>' percent in this ability's
    detail lines, via kit.py's regex — the ranking signal for which ability
    gets maxed first. Malformed detail text never raises; it just scores 0."""
    total = 0.0
    try:
        for detail in ability.get("details") or []:
            text = str(detail)
            if "scaling" not in text.lower():
                continue
            for m in kit._SCALING_LINE.finditer(text):
                total += float(m.group(1))
    except Exception:
        return 0.0
    return total


def _fallback_order(god, max_levels):
    """Last-resort, never-raise order: cycle through whatever slots the god's
    kit has, in kit order. Only reached when there isn't even a single
    levelable (non-ult, non-passive, non-basic) ability to build an order
    from — real scrapes with no scaling data still go through the normal
    path, which degrades gracefully to plain slot order on its own."""
    slots = [ab.get("slot") for ab in (god.get("abilities") or []) if ab.get("slot")]
    if not slots:
        return [""] * max_levels
    return [slots[i % len(slots)] for i in range(max_levels)]


def ability_order(god, weights=None):
    """A `max_levels`-entry list of ability slots — one per character level —
    representing the order points would be spent leveling up.

    Priority: (1) the ultimate at every configured `ult_levels`; (2) one
    `early_points` point in every other ability, for utility; (3) remaining
    points go to the ability with the highest parsed damage scaling first
    (kit.py), maxing it out (5 ranks) before moving to the next, tied by kit
    slot order. A god whose scaling can't be parsed still gets a valid order
    — the ranking's tie-break degrades to plain slot order. Never raises.
    """
    cfg = _cfg(weights)
    max_levels = int(cfg["max_levels"])
    try:
        non_ult = _non_ult_abilities(god)
        non_ult_slots = [ab["slot"] for ab in non_ult]
        if not non_ult_slots:
            return _fallback_order(god, max_levels)
        ult_slot = _ultimate_slot(god)

        order = [None] * max_levels
        ult_levels = [int(lvl) for lvl in cfg["ult_levels"] if 1 <= int(lvl) <= max_levels]
        for lvl in ult_levels:
            order[lvl - 1] = ult_slot

        open_positions = [i for i in range(max_levels) if order[i] is None]

        early_points = max(int(cfg["early_points"]), 0)
        counts = {slot: 0 for slot in non_ult_slots}
        pos_i = 0
        for _round in range(early_points):
            for slot in non_ult_slots:
                if pos_i >= len(open_positions):
                    break
                order[open_positions[pos_i]] = slot
                counts[slot] += 1
                pos_i += 1

        scaling = {ab["slot"]: _ability_scaling_total(ab) for ab in non_ult}
        ranked = sorted(non_ult_slots, key=lambda s: (-scaling.get(s, 0.0), non_ult_slots.index(s)))

        # Drain the highest-ranked ability to its rank cap before the next
        # one gets any point beyond its early one ("maxed first").
        for slot in ranked:
            while counts[slot] < _ABILITY_RANK_CAP and pos_i < len(open_positions):
                order[open_positions[pos_i]] = slot
                counts[slot] += 1
                pos_i += 1

        # More points than every ability's cap can hold (e.g. non_ult count
        # isn't a clean divisor of max_levels) — spill onto the ranked order
        # again rather than leave a level unfilled.
        i = 0
        while pos_i < len(open_positions):
            slot = ranked[i % len(ranked)]
            order[open_positions[pos_i]] = slot
            counts[slot] += 1
            pos_i += 1
            i += 1

        # Defensive only — the loops above always fill every open position.
        for idx, v in enumerate(order):
            if v is None:
                order[idx] = ult_slot
        return order
    except Exception:
        return _fallback_order(god, max_levels)


def summary(order, weights=None):
    """Compact {"max_order": [...], "ult_levels": [...]} for the UI's one-line
    heuristic readout ("max 1st -> 2nd -> 3rd", "ult at 5/9/13/17"), derived
    from an already-computed `order` list rather than re-deriving the ranking.

    Ranked by each ability's *second* occurrence (when it started pulling
    ahead of the others), not its last — a leftover point that spills past
    every ability's rank cap always lands on the final open level, which
    would otherwise make the top-ranked ability look last."""
    cfg = _cfg(weights)
    ult_levels = [int(lvl) for lvl in cfg["ult_levels"]]
    order = order or []
    ult_slots = {order[lvl - 1] for lvl in ult_levels if 1 <= lvl <= len(order)}
    occurrences = {}
    for i, slot in enumerate(order):
        if slot and slot not in ult_slots:
            occurrences.setdefault(slot, []).append(i)

    def _rank_key(slot):
        idxs = occurrences[slot]
        return idxs[1] if len(idxs) > 1 else float("inf")

    max_order = sorted(occurrences, key=_rank_key)
    return {"max_order": max_order, "ult_levels": ult_levels}
