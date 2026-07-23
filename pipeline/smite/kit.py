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


def kit_stat_overlay(profile, god):
    """Offensive stat weights implied by the kit, or {} when confidence is low
    (< 3 abilities with scaling — sparse scrapes like Ullr's stance kit)."""
    if profile["n_scaling_abilities"] < 3:
        return {}
    out = {}
    dt = god.get("damage_type")
    if dt == "physical" and profile["str_share"] > 0:
        out["Strength"] = round(0.6 + 0.6 * profile["str_share"], 3)
    if dt == "magical" and profile["int_share"] > 0:
        out["Intelligence"] = round(0.6 + 0.6 * profile["int_share"], 3)
    if profile["basic_attack_share"] >= 0.2:
        out["Attack Speed"] = round(0.5 + profile["basic_attack_share"], 3)
        if dt == "physical":
            out["Critical Chance"] = round(0.4 + profile["basic_attack_share"], 3)
    else:
        out["Cooldown Rate"] = 0.6
        out["Penetration"] = 0.8
    return out
