"""Kit-scaling profiles: parse each ability's 'Damage Scaling: N% <Stat>'
lines into a per-god orientation (Strength vs Intelligence, basic-attack vs
ability) so god-fit reflects the actual kit, not only the archetype label.
Heuristic, not simulation — see the 2026-07-22 design spec."""
import re

_SCALING_LINE = re.compile(
    r"(\d+(?:\.\d+)?)\s*%\s*(Strength|Intelligence|Basic Attack Damage|Attack Damage)",
    re.IGNORECASE)
_CANON = {"strength": "Strength", "intelligence": "Intelligence",
          "basic attack damage": "Basic Attack Damage", "attack damage": "Attack Damage"}


def scaling_profile(god):
    """str/int/basic-attack scaling shares across the god's abilities.
    The Basic Attack slot itself is excluded — every god's basic carries
    ~100% Strength, so it says nothing about the kit. 'Basic Attack Damage' /
    'Attack Damage' references in *other* slots mark basic-attack orientation
    (steroids and on-hit passives like Ymir's Frostbite)."""
    str_t = int_t = basic_t = 0.0
    n = 0
    for ab in god.get("abilities") or []:
        if "basic attack" in str(ab.get("slot") or "").lower():
            continue
        sums = {}
        for detail in ab.get("details") or []:
            text = str(detail)
            if "scaling" not in text.lower():
                continue
            for m in _SCALING_LINE.finditer(text):
                stat = _CANON[m.group(2).lower()]
                sums[stat] = sums.get(stat, 0.0) + float(m.group(1))
        if not sums:
            continue
        n += 1
        str_t += sums.get("Strength", 0.0)
        int_t += sums.get("Intelligence", 0.0)
        basic_t += sums.get("Basic Attack Damage", 0.0) + sums.get("Attack Damage", 0.0)
    dmg = str_t + int_t
    total = dmg + basic_t
    return {
        "str_share": (str_t / dmg) if dmg else 0.0,
        "int_share": (int_t / dmg) if dmg else 0.0,
        "basic_attack_share": (basic_t / total) if total else 0.0,
        "n_scaling_abilities": n,
    }


def kit_stat_overlay(profile, god, include_off_type=False):
    """Offensive stat weights implied by the kit, or {} when confidence is low
    (< 3 abilities with scaling).

    The floor used to be reached by the three STANCE gods, and that was a
    parser bug wearing a confidence threshold's clothes: Ullr, Artio and Merlin
    render their kits inside the wiki's tab wrapper, which `_section_tables`
    walked straight past, so all three arrived here with
    `n_scaling_abilities: 0` and got no kit measurement at all. Fixed at the
    source (see `wiki_parser._section_tables`) — they now measure 4, 4 and 9,
    and Artio turns out to take 54% of her ability damage off Strength while
    labelled magical, which makes her a hybrid scaler the model had no way to
    see. The threshold itself stays: it is a real guard for a genuinely thin
    scrape, it just should never have been load-bearing for a fifth of the
    stance roster.

    `include_off_type` adds the power stat the god's `damage_type` label calls
    useless, weighted by the same formula from its own measured share. It is
    off by default because the damage filter normally forbids those items, so
    the weight would only dilute the denominator. `scoring.is_hybrid_scaler`
    turns it on for the gods whose filter is relaxed, keeping the two in step:
    a stat is admitted and scored, or neither.

    The formula is deliberately the same on both sides. Neith measures 44.5%
    Strength / 55.5% Intelligence, so she gets Strength 0.867 and Intelligence
    0.933 — the ordering her kit actually has, which the single `damage_type`
    label cannot express."""
    if profile["n_scaling_abilities"] < 3:
        return {}
    out = {}
    dt = god.get("damage_type")
    weight = lambda share: round(0.6 + 0.6 * share, 3)
    if profile["str_share"] > 0 and (dt == "physical" or include_off_type):
        out["Strength"] = weight(profile["str_share"])
    if profile["int_share"] > 0 and (dt == "magical" or include_off_type):
        out["Intelligence"] = weight(profile["int_share"])
    if profile["basic_attack_share"] >= 0.2:
        out["Attack Speed"] = round(0.5 + profile["basic_attack_share"], 3)
        if dt == "physical":
            out["Critical Chance"] = round(0.4 + profile["basic_attack_share"], 3)
    else:
        out["Cooldown Rate"] = 0.6
        out["Penetration"] = 0.8
    return out
