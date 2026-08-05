"""Data-integrity guard for scraped item + build data. Run after every
regenerate as a CI-style gate: non-zero exit + a readable finding list if
anything is wrong."""
import json
import re
import sys
from collections import Counter
from pathlib import Path

from smite import scoring

REPO_ROOT = Path(__file__).resolve().parents[2]
INDEX_PATH = REPO_ROOT / "viewer" / "public" / "index.json"

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

        if not cost:
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
    with). This is the coverage/correctness gate for the full roster."""
    items_by_name = {it["name"]: it for it in items}
    conquest_by_god = {}
    for bg in builds:
        if bg.get("mode") == "Conquest":
            conquest_by_god.setdefault(bg.get("god"), bg)

    findings = []
    for god in gods:
        name = god.get("name")
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
    god_findings = audit_gods(gods, builds, items)

    print(f"Item audit: {len(items)} items, {len(item_findings)} finding(s)")
    for f in item_findings:
        print(f"{f['item']}: {f['issue']} - {f['detail']}")
    print(f"God audit: {len(gods)} gods, {len(god_findings)} finding(s)")
    for f in god_findings:
        print(f"{f['god']}: {f['issue']} - {f['detail']}")

    if not item_findings and not god_findings:
        print("no issues found")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
