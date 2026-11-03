"""Self-heals in a god's ABILITIES, read off the ability text (2026-11-03).

WHY. Seven Conquest verdicts moved toward lifesteal-heavy community sixes once
the fight healed (#83), and the god-passive diagnosis found the sustain that
could explain it lives in five of those seven gods' ABILITIES (Sun Wukong's
Somersault Cloud, Mordred's Cruel Strikes, Sol's Radiance, Chaac's Rain Dance,
Hua Mulan's Spear Thrust). `side_by_side`'s clock cast those abilities for
their damage and dropped the heal. This puts the heal in the same channel
(`Sim.heal`), so the enemy team's anti-heal cuts it and overheal is wasted.

WHAT IS READ, per ability, from its detail lines at the LAST rank:
  "Heal: X"                       a flat heal on the cast
  "Heal Per Tick: X"              per tick, times "Heals N times" or "ticks N
                                  times" (else 1)
  "Heal Scaling[ Per Tick]: P% S" P% of stat S added to each heal
  "Self Heal Scaling Per Tick"    the same, explicitly self
and each term X may be a number (`a | b | c` -> the last), "P% Max Health",
"P% Missing Health" or "P% Protections" (the mean of our two).

WHAT IS NOT, and why: a line prefixed "Ally", "Minion" or "Boar" heals
something else; "Shield Health" is a shield, not a heal (shields are their own
item channel); "Healing Reduction" is anti-heal on the TARGET; "Health Regen"
and "Max Health Restore" are left to a later slice. An ability whose text heals
only allies ("Heal allies", with no "you"/"yourself") is skipped.

WHEN IT LANDS. An ability the damage rotation casts (`ability_rotation`)
heals at each of those casts. An ability it does NOT cast — Rain Dance and
Radiance have no parsed damage component, Cruel Strikes none either — is
cast for its heal alone, on the rule Amanita Charm's heal uses: at the first
hit taken, then again on its cooldown (cooldown rate applied). A heal pressed
at full health is wasted, so this is the reading a player would take.

THE ASSUMPTIONS, the same for both builds of a god:
  * the heal lands on every cast, at the cast — conditional heals (Mordred's
    "if Clarent is next in the Attack Chain", Hua Mulan's "Skilled") are
    taken as met, which is the upper end; the report brackets nothing here
    because both builds share the kit;
  * a per-tick heal with no stated tick count is ONE tick — Sun Wukong's
    cloud says "Heal every 0.5 seconds" and gives no duration, so its heal is
    the conservative single tick;
  * all ticks land at the cast. Ticking them over the stated duration would
    let less of each heal be overheal; at the cast is the conservative end.
"""
import re

_NUM = re.compile(r"[\d.]+")
_TERM = re.compile(r"([\d.]+)%\s*(Max Health|Missing Health|Protections|Intelligence|Strength)", re.I)
_TICKS = re.compile(r"Heals?\s+(\d+)\s+times", re.I)
_TICKS_ANY = re.compile(r"ticks\s+(\d+)\s+times", re.I)
_SKIP_PREFIX = ("ally", "minion", "boar", "spring", "soul", "slam health")
_ALLY_ONLY = re.compile(r"\bheal(?:s|ing)?\s+(?:an?\s+)?all(?:y|ies|ied)", re.I)
_SELF = re.compile(r"\byou\b|\byourself\b|\bself\b", re.I)


def _terms(value):
    """`{"flat": x, "max_health": p, "missing_health": p, "protections": p,
    "Intelligence": p, "Strength": p}` off one value string."""
    out = {}
    for pct, what in _TERM.findall(value):
        key = {"max health": "max_health", "missing health": "missing_health",
               "protections": "protections"}.get(what.lower(), what.title())
        out[key] = out.get(key, 0.0) + float(pct) / 100.0
    rest = _TERM.sub("", value).strip(" +")
    nums = _NUM.findall(rest.split("|")[-1]) if rest else []
    if nums:
        try:
            out["flat"] = float(nums[0])   # the LAST rank: "17 | 24 | ... | 45" -> 45
        except ValueError:
            pass
    return out


def self_heal(ability):
    """`{"ticks": n, "per": {terms}}` for one ability, or None."""
    details = ability.get("details") or []
    text = " ".join([ability.get("description") or ""] + details)
    if _ALLY_ONLY.search(text) and not _SELF.search(text):
        return None
    per, ticks, found, per_tick = {}, 1, False, False
    for line in details:
        head, _, value = line.partition(":")
        h = head.strip().lower()
        if not value or not h or h.startswith(_SKIP_PREFIX):
            continue
        if h in ("heal", "heal per tick", "bonus heal"):
            per_tick = per_tick or h == "heal per tick"
            for k, v in _terms(value).items():
                per[k] = per.get(k, 0.0) + v
            found = True
        elif h in ("heal scaling", "heal scaling per tick", "self heal scaling per tick"):
            for k, v in _terms(value).items():
                if k != "flat":
                    per[k] = per.get(k, 0.0) + v
    if not found:
        return None
    m = _TICKS.search(text) or (_TICKS_ANY.search(text) if per_tick else None)
    if m:
        ticks = int(m.group(1))
    return {"ticks": ticks, "per": per}


_COOLDOWN = re.compile(r"^\s*Cooldown:\s*(.+?)\s*seconds?", re.I)


def cooldown(ability):
    """The ability's cooldown at its last rank, in seconds, or None."""
    for line in ability.get("details") or []:
        m = _COOLDOWN.match(line)
        if m:
            nums = _NUM.findall(m.group(1).split("|")[-1])
            if nums:
                return float(nums[0])
    return None


def god_self_heals(god):
    """`{ability name: self_heal}` for every non-basic ability that heals."""
    out = {}
    for a in god.get("abilities") or []:
        slot = a.get("slot") or ""
        if slot.startswith("Basic") or slot.startswith("Passive"):
            continue
        h = self_heal(a)
        if h:
            out[a["name"]] = dict(h, cooldown=cooldown(a))
    return out


def amount(heal, *, max_health, hp, protections, stats):
    """The heal one cast lands, before healing reduction and overheal."""
    p = heal["per"]
    one = (p.get("flat", 0.0) + p.get("max_health", 0.0) * max_health
           + p.get("missing_health", 0.0) * max(0.0, max_health - hp)
           + p.get("protections", 0.0) * protections
           + p.get("Intelligence", 0.0) * stats.get("Intelligence", 0.0)
           + p.get("Strength", 0.0) * stats.get("Strength", 0.0))
    return one * heal["ticks"]
