"""What an ENEMY playing an aspect actually builds, as the draft's one input.

DATA, not model weights: this is read off what players bought and shipped in the
index as `enemy_aspects`. The draft board reads it, and only when the reader
turns an enemy's aspect on. With every toggle off the draft is byte-for-byte
what it was.

WHY IT EXISTS (2026-11-09, Jacob). The draft reads each enemy god's STATIC
attributes (`damage_type`, specializations) to decide what threatens you. An
aspect can change those: Tsukuyomi is a physical Jungler, and his Aspect of
Mangetsu is a magical Mid build (see `aspect_matches`). Counting him as physical
mis-prices every magic-protection item against him.

WHAT IS MEASURED, per aspect, over every aspect-equipped match in the store:
  * each match's six items are classified from the items' own stats — an item
    with a physical offensive stat counts physical, one with Intelligence counts
    magical (a hybrid counts both). `tank` when at most `TANK_POWER_ITEMS` of the six carry
    any power at all; otherwise the side with more power items; a tie is `mixed`.
  * `physical` / `magical` / `tank` are the share of matches in each class, and
    `kind` is the class holding at least `DECISIVE` of them, else `mixed`.
  A `mixed` aspect overrides nothing: the board keeps the god's own attributes
  rather than guess.

POOLED ACROSS PATCH WINDOWS (Jacob, 2026-11-09). `aspect_matches.aspect_entry`
takes the newest window, or the last closed one, and needs
`tierlist.MIN_MATCHES` (30) in it — which leaves Tsukuyomi's Mangetsu "below
minimum" at 6 / 21 / 30 / 17 matches per window although 73 matches sit in the
store. The draft's question is a coarse one (which damage type does this
enemy deal), and an aspect's identity rarely changes between patches, so this
pools every window and applies the same 30-match floor to the pooled total. The
note entry's own rule is unchanged.

WHAT IT CANNOT SAY. Matches are not players (a thin aspect can be a few
one-tricks), the store is Obsidian+ only, and inventory slots are not a buy
order — none of which matters for "which damage type", but all of which matter
for anything finer, so nothing finer is exported.
"""
from collections import Counter
from pathlib import Path

from smite import aspect_matches as am
from smite import tierlist

#: Share of an aspect's matches one class must hold to be called its kind.
DECISIVE = 0.6
#: A build with this many power items or fewer, out of six, is a tank build.
TANK_POWER_ITEMS = 2
MIN_MATCHES = tierlist.MIN_MATCHES


#: Offensive stats that say which damage an item serves. Measured 2026-11-09:
#: many physical items carry Attack Damage, Attack Speed or Critical Chance and
#: no Strength (Tyrfing's Strength is the exception, The Executioner's only
#: stat is Attack Speed), so Strength alone read half of the physical builds as
#: tank builds. Penetration, Lifesteal and Cooldown Rate serve both sides and
#: say nothing.
PHYSICAL_STATS = ("Strength", "Attack Damage", "Attack Speed", "Critical Chance")
MAGICAL_STATS = ("Intelligence",)


def _power(stats: dict) -> tuple:
    return any(k in stats for k in PHYSICAL_STATS), any(k in stats for k in MAGICAL_STATS)


def classify(item_names: list, item_stats: dict) -> str:
    """One match's build: physical, magical, tank or mixed."""
    phys = mag = 0
    for name in item_names:
        p, m = _power(item_stats.get(name, {}))
        phys += p
        mag += m
    if max(phys, mag) <= TANK_POWER_ITEMS:
        return "tank"
    return "physical" if phys > mag else "magical" if mag > phys else "mixed"


def build(gods: list, items: list, root: Path = am.STORE_ROOT) -> dict:
    """`{god: {aspect: entry}}` for every aspect with enough pooled matches."""
    meta = am.load_meta(root)
    names = am.item_name_lookup()
    stats = {i["name"]: i.get("stats") or {} for i in items if i.get("name")}
    by_slug = {am.god_slug(g["name"]): g["name"] for g in gods}
    out = {}
    for slug, aspects in sorted((meta.get("aspects") or {}).items()):
        god = by_slug.get(slug)
        if not god or not aspects:
            continue
        aspect_name = {a["value"]: a["name"] for a in aspects}
        kinds, roles = {}, {}
        for recs in am.load_god(root, slug).values():
            for r in recs:
                a = r["aspect"]
                if not a:
                    continue
                kinds.setdefault(a, Counter())[classify([names.get(s, s) for s in r["items"] if s], stats)] += 1
                roles.setdefault(a, Counter())[r["role"]] += 1
        for a, c in kinds.items():
            n = sum(c.values())
            if n < MIN_MATCHES:
                continue
            share = {k: round(c[k] / n, 2) for k in ("physical", "magical", "tank")}
            kind = next((k for k in ("physical", "magical", "tank") if c[k] / n >= DECISIVE), "mixed")
            role, role_n = roles[a].most_common(1)[0]
            out.setdefault(god, {})[aspect_name.get(a, a)] = {
                "matches": n, "kind": kind, **share, "role": role, "role_share": round(role_n / n, 2)}
    return out
