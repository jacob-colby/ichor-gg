"""Data-integrity guard for scraped item + build data. Run after every
regenerate as a CI-style gate: non-zero exit + a readable finding list if
anything is wrong."""
import json
import re
import sys
from collections import Counter
from pathlib import Path

from smite import kit, scoring

REPO_ROOT = Path(__file__).resolve().parents[2]
INDEX_PATH = REPO_ROOT / "viewer" / "public" / "index.json"
TAGS_PATH = REPO_ROOT / "data" / "_tags.yaml"

# The declared effect-tag vocabulary. Nothing else validates these strings, so
# a typo (`sustian`) silently does nothing: `god_fit_score` looks the tag up in
# `offense_tags` and a `tag_bonus` map, misses both, and adds zero. This list
# is what turns that into a finding. Adding a tag means adding it here AND
# writing its provenance block in `data/_tags.yaml`.
KNOWN_TAGS = {
    # what job the item does in a fight
    "burst", "execute", "anti-heal", "protection-shred", "penetration",
    "percent-health", "peel", "wave-clear", "mobility", "sustain",
    "cc-immunity", "aura", "anti-crit", "damage-debuff", "anti-shield",
    "heal-scaling",
    # when the value arrives
    "ability-uptime", "stacking", "ramp", "low-health", "crit-scaling",
    "mitigation", "ward-economy", "active",
}

STAT_VALUE_RE = re.compile(r"-?\d+\.?\d*")
TIER3_COST_MIN = 1800
TIER3_COST_MAX = 4000  # legit tier-3 totals reach ~3700 (e.g. Avatar's Parashu)
STAT_VALUE_MAX = 1000


def _stat_findings(name, stats):
    findings = []
    if not isinstance(stats, dict):
        return findings
    for stat_name, value in stats.items():
        match = STAT_VALUE_RE.search(str(value))
        if match is None:
            findings.append({
                "item": name, "issue": "bad-stat-value",
                "detail": f"{stat_name}={value!r} has no numeric value",
            })
            continue
        num = float(match.group())
        if num < 0 or num > STAT_VALUE_MAX:
            findings.append({
                "item": name, "issue": "bad-stat-value",
                "detail": f"{stat_name}={value!r} out of range",
            })
    return findings


def audit_items(items: list) -> list:
    findings = []
    name_counts = Counter(n for it in items if (n := it.get("name")))

    for it in items:
        name = it.get("name")
        tier = it.get("tier")
        cost = it.get("cost")
        stats = it.get("stats") or {}
        is_numeric_tier = isinstance(tier, (int, float)) and not isinstance(tier, bool)

        # A god's ABILITY MOD is not a purchasable item and its zero cost is not
        # a gap in the data. Vulcan's five Mods (`God Specific`, cost 0, no
        # stats, "Requires level 14", "you can only have one Mod from each
        # set") are a kit upgrade the game grants, and every future god with
        # the same system would add five more permanent findings to a gate
        # whose whole value is that a new finding means something.
        #
        # `scoring.is_buildable` already refuses them for being statless, so
        # nothing downstream can put one in a build. Recognised by the shape
        # rather than by a name list, so the next god's Mods need no edit here.
        # `cost == 0` exactly, never merely falsy. Genie's Lamp reads `-1` on
        # the wiki — a sentinel `wiki_parser._parse_cost` turns into None — and
        # it matches this shape in every other respect, so a `not cost` test
        # swallowed it. It is a different statement: a Mod has no price because
        # it is a kit upgrade, the Lamp has no price we could read. The second
        # one is worth keeping in front of a human.
        is_ability_mod = (it.get("god") and cost == 0 and not stats
                          and not is_numeric_tier)
        if not cost and not is_ability_mod:
            findings.append({
                "item": name, "issue": "blank-cost",
                "detail": f"cost is {cost!r}",
            })

        if tier is None or tier == "":
            findings.append({
                "item": name, "issue": "null-tier",
                "detail": f"tier is {tier!r}",
            })

        if not stats and is_numeric_tier:
            findings.append({
                "item": name, "issue": "empty-stats",
                "detail": f"numeric tier {tier!r} has no stats",
            })

        findings.extend(_stat_findings(name, stats))

        if tier == 3 and (cost is None or not (TIER3_COST_MIN <= cost <= TIER3_COST_MAX)):
            findings.append({
                "item": name, "issue": "tier3-cost-outlier",
                "detail": f"cost {cost!r} outside {TIER3_COST_MIN}-{TIER3_COST_MAX}",
            })

        if name and name_counts[name] > 1:
            findings.append({
                "item": name, "issue": "duplicate-name",
                "detail": f"name appears {name_counts[name]} times",
            })

    findings.sort(key=lambda f: (f["item"] or "", f["issue"]))
    return findings


def audit_tags(items: list, tags_map: dict) -> tuple:
    """Effect-tag coverage over the god-agnostic buildable pool.

    Returns (findings, reviewed_empty) — the second is a COUNT, not a finding,
    and the distinction is the whole point of this check.

    `recommend --all` has printed a tag warning since the tags file existed,
    and on 2026-08-19 it read "[tags] 1 untagged items: Totem of Death" while
    55 of the 138 buildable items carried no tag at all. Neither number was
    wrong; they answer different questions. That warning tests `name not in
    tags_map` — FILE MEMBERSHIP — and exactly one item was missing. The 55 is
    `len(tags) == 0`, which folds in 54 more sitting at `[]`.

    They are genuinely different states and only one is a defect:

        absent from _tags.yaml   nobody has read this item's passive  -> FINDING
        present as `[]`          read, and no tag was warranted       -> COUNT

    Collapsing them in either direction lies. Reporting only absences (what
    the old warning did) says the pool is covered when 39% of it is untagged;
    reporting every `[]` as a finding would permanently flag Wish-Granting
    Pearl, which has no passive text to judge and never will.

    Reads `_tags.yaml` rather than the index because `build_index._enrich_items`
    writes `tags.get(name, [])` — which collapses absent into `[]` and destroys
    exactly the distinction above before the audit could see it.

    THERE IS DELIBERATELY NO "this tags entry names an item that no longer
    exists" CHECK, though a renamed item silently losing its tags is a real
    risk. It was written, and it is the wrong SHAPE for this gate: it is the
    only check here that needs a closed world over `items`, so any partial view
    turns all 168 entries into findings at once — which is what it did to the
    minimal fixture in `test_main_returns_zero_when_clean`. A gate whose value
    is that a new finding means something cannot have a mode that emits 168 of
    them. The risk is covered upstream anyway, by
    `notes.canonicalise_community_items` at ingest and `audit_item_coverage`
    here."""
    findings = []
    buildable = [it for it in items if scoring.is_buildable(it)]

    reviewed_empty = 0
    for it in sorted(buildable, key=lambda i: i.get("name") or ""):
        name = it.get("name")
        if name not in tags_map:
            findings.append({
                "item": name, "issue": "untagged-item",
                "detail": "buildable but absent from data/_tags.yaml "
                          "(no one has read its passive)",
            })
        elif not (tags_map.get(name) or []):
            reviewed_empty += 1

    for name, tags in sorted(tags_map.items()):
        for tag in (tags or []):
            if tag not in KNOWN_TAGS:
                findings.append({
                    "item": name, "issue": "unknown-tag",
                    "detail": f"{tag!r} is not in KNOWN_TAGS; nothing reads it",
                })

    findings.sort(key=lambda f: (f["item"] or "", f["issue"]))
    return findings, reviewed_empty


MIN_CORE_ITEMS = 5


def _suggested_core(build_group):
    for b in (build_group or {}).get("builds", []):
        if b.get("source") == "suggested" and b.get("archetype") == "core":
            return b
    return None


def audit_gods(gods: list, builds: list, items: list) -> list:
    """Every tracked god must produce a usable Conquest core build: present,
    at least MIN_CORE_ITEMS items, a stamped starter, and no off-damage-type
    item leaking in (reuses the same damage filter the recommender scores
    with). This is the coverage/correctness gate for the full roster.

    It also checks the god's KIT, because every rule above is a check on the
    OUTPUT and the output survives a god whose kit went missing. Blanking the
    abilities of Ullr, Artio and Merlin and recomputing their cores produced
    zero findings here, PASSed `validate --check`, and moved win-weighted
    coverage from 0.5530 to 0.5552 — up (measured 2026-08-29). The reason is
    `kit.kit_stat_overlay`, which returns {} below 3 abilities so god-fit
    falls back silently to the role label and still builds something
    plausible. `refresh.ParseCollapse` refuses to write that note in the first
    place; these two findings are the second line, for a note that got in
    before the guard existed or by way of --allow-shrink."""
    items_by_name = {it["name"]: it for it in items}
    conquest_by_god = {}
    for bg in builds:
        if bg.get("mode") == "Conquest":
            conquest_by_god.setdefault(bg.get("god"), bg)

    findings = []
    for god in gods:
        name = god.get("name")

        abilities = god.get("abilities") or []
        if not abilities:
            findings.append({"god": name, "issue": "no-abilities",
                             "detail": "kit is empty — the wiki page has none, "
                                       "which no god page does"})
        elif kit.scaling_profile(god).get("n_scaling_abilities", 0) == 0:
            # The exact Ullr/Artio/Merlin symptom: tables present, scaling
            # lines not. Below 3 the overlay is {} anyway, but 0 is the one
            # that cannot be a real kit.
            findings.append({"god": name, "issue": "no-scaling-abilities",
                             "detail": f"{len(abilities)} abilities, none carrying "
                                       f"a scaling line"})

        core = _suggested_core(conquest_by_god.get(name))
        if core is None:
            findings.append({"god": name, "issue": "no-build",
                             "detail": "no suggested Conquest core build"})
            continue
        slots = core.get("slot_order") or []
        if len(slots) < MIN_CORE_ITEMS:
            findings.append({"god": name, "issue": "short-build",
                             "detail": f"{len(slots)} items (< {MIN_CORE_ITEMS})"})
        if not core.get("starter"):
            findings.append({"god": name, "issue": "no-starter",
                             "detail": "no starter stamped"})
        for item_name in slots:
            it = items_by_name.get(item_name)
            if it and not scoring.passes_damage_filter(it, god):
                findings.append({
                    "god": name, "issue": "wrong-damage-item",
                    "detail": f"{item_name} ({scoring.item_damage_type(it)}) "
                              f"in a {god.get('damage_type')} build",
                })
    findings.sort(key=lambda f: (f["god"] or "", f["issue"]))
    return findings


def audit_item_coverage(items: list, builds: list) -> list:
    """Items the community demonstrably builds that we do not have a note for.

    `refresh_all` only re-pulls items that ALREADY have a note, so a new
    patch's items are invisible until someone runs `--refresh <name>` by hand.
    Nothing checked whether that had been done, and it had not: eight tier-3
    items were missing on 2026-08-05, among them Dominance, which appears in
    both Cernunnos's and Jing Wei's community builds. A missing item cannot be
    recommended and silently caps those gods' coverage at whatever is left.

    SmiteBrain's own build data is the right detector because it names items by
    the only standard that matters — someone built them. Alternates count too:
    they are the items that lost a slot, which is exactly the pool the
    recommender is supposed to be choosing differently from.

    `refresh.discover_untracked_items` is the companion check, scanning the
    wiki cache for items no build has reached yet."""
    have = {it.get("name") for it in items}
    referenced = {}
    for group in builds:
        for build in group.get("builds") or []:
            if build.get("source") != "community":
                continue
            for slot in build.get("slot_order") or []:
                if not isinstance(slot, dict):
                    continue
                for entry in [slot] + list(slot.get("alternates") or []):
                    name = entry.get("name")
                    if name and name not in have:
                        referenced.setdefault(name, set()).add(group.get("god"))
    return sorted(
        ({"item": name, "issue": "untracked-item",
          "detail": f"built by {len(gods)} god(s) "
                    f"({', '.join(sorted(g for g in gods if g)[:3])}"
                    f"{'...' if len(gods) > 3 else ''}) but has no note — "
                    f"run: python -m smite.refresh --refresh '{name}' --kind item"}
         for name, gods in referenced.items()),
        key=lambda f: f["item"])


def _load_index() -> dict:
    return json.loads(INDEX_PATH.read_text(encoding="utf-8"))


def _load_tags() -> dict:
    # Separate loader so a test can inject a tags map for its own fixture
    # items, the same way every test here injects `_load_index`. Without it
    # `audit_tags` compares a synthetic index against the real 168-entry file
    # and every fixture item is correctly, uselessly reported as untagged.
    return scoring.load_tags(TAGS_PATH)


def load_items() -> list:
    return _load_index().get("items", [])


def main(argv=None) -> int:
    # Item names can contain non-ASCII characters (curly apostrophes, etc.).
    # A redirected/cron stdout may be on a non-UTF-8 codepage (cp437/cp1252 on
    # Windows), so make encoding failures replace instead of crashing the gate.
    try:
        sys.stdout.reconfigure(errors="replace")
    except Exception:
        pass

    try:
        index = _load_index()
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        print(f"Audit: could not load index.json ({exc})")
        return 1

    items = index.get("items", [])
    gods = index.get("gods", [])
    builds = index.get("builds", [])

    item_findings = audit_items(items) + audit_item_coverage(items, builds)
    tag_findings, reviewed_empty = audit_tags(items, _load_tags())
    god_findings = audit_gods(gods, builds, items)

    print(f"Item audit: {len(items)} items, {len(item_findings)} finding(s)")
    for f in item_findings:
        print(f"{f['item']}: {f['issue']} - {f['detail']}")
    buildable = sum(1 for it in items if scoring.is_buildable(it))
    tagged = buildable - reviewed_empty - sum(
        1 for f in tag_findings if f["issue"] == "untagged-item")
    print(f"Tag audit: {buildable} buildable items, {tagged} tagged, "
          f"{reviewed_empty} reviewed with no tag warranted, "
          f"{len(tag_findings)} finding(s)")
    for f in tag_findings:
        print(f"{f['item']}: {f['issue']} - {f['detail']}")
    print(f"God audit: {len(gods)} gods, {len(god_findings)} finding(s)")
    for f in god_findings:
        print(f"{f['god']}: {f['issue']} - {f['detail']}")

    if not item_findings and not tag_findings and not god_findings:
        print("no issues found")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
