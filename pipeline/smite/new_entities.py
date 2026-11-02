"""Add gods and items the wiki has and the vault does not. Unattended.

    python -m smite.new_entities             # discover, add, gate; always exits 0
    python -m smite.new_entities --dry-run   # discover and parse, write nothing
    python -m smite.new_entities --no-gate   # add without the test gate (local use)

WHERE IT RUNS. Daily, from `refresh-data.yml`, after the stats gate has
settled the tracked stats and before the snapshot and recompute. It is the
step `wiki_watch` used to leave to a human: a god on the roster grid, or an
item on the Items index, with no note under `data/`.

WHY THIS IS NOW SAFE WHEN `wiki_watch` SAID IT WAS NOT. The case against an
unattended add (that module's docstring) was that `parse_god_page` degrades
to EMPTY on a shape change, that `merge_god_note` would write the empty kit,
and that no gate saw it: blanking Ullr, Artio and Merlin moved coverage UP and
passed every check. Three things answer it here, and the first is the one
that matters:

  1. COMPLETE OR ABSENT. A new page is parsed in memory and must pass
     `god_problems` / `item_problems` before anything is written: an infobox
     with pantheon, role and damage type; at least `MIN_ABILITIES` named
     abilities; at least one SCALING ability (the exact Ullr symptom, which an
     ability count alone does not catch); a full numeric base-stat block. An
     item needs a tier, a numeric cost and a numeric stat line. Anything less
     is left out and logged — never added half-filled. The old failure mode
     was overwriting a good note with an empty one; a NEW god has no good note
     to lose, so the worst a wrong parse can do here is be refused.
  2. NOTHING IS INVENTED. An item whose passive the catalogue
     (`data/_passive_classes.yaml`) has no entry for is added as UNCATALOGUED:
     valued on its stat line alone, which is what the shipped model already
     does for every passive it does not price, and flagged so the viewer says
     so. If a SHIPPED pricing flag already reprices the new text (an
     `Adaptive Stat:` line, say), the entry names the clause class that flag
     prices — learned from the catalogue's own existing entries, never typed
     in — because the catalogue test requires exactly that claim. A flag the
     catalogue cannot map to one class leaves the item out for a human.
  3. THE SAME GATE AS A STATS REFRESH (`stats_gate`, PR #67), plus the job's
     two numeric gates. All candidates are added, builds recomputed, and the
     suite, `validate --check` and `calibrate_combat` run. Green: kept. A
     check that fails with them and passes without them is ATTRIBUTABLE; each
     candidate is then tried alone against just those checks, the ones that
     trip them are left out with the failing check as the reason, and the
     rest are re-run in full. Anything still attributable after that, or any
     crash, puts the data back exactly as it was (fail closed).

LOGGED IN `data/_new_entities.json`: what was added, what was left out and
why, and what the grid lists with no page yet (the normal state for a god
announced before release — Kumbhakarna, Heimdallr, Maman Brigitte on
2026-11-02). It is committed with the data, so the record is in git.

A god the owner removed (`data/Gods/_removed/`) is never re-added. A re-run
adds nothing twice: a candidate is anything without a note, and a note is the
first thing an add writes.
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import traceback
from datetime import date
from pathlib import Path

import yaml

from smite import notes, refresh, stats_refresh, wiki_parser

DATA_ROOT = refresh.DATA_ROOT
PIPELINE = Path(__file__).resolve().parents[1]
LOG_FILE = "_new_entities.json"
CATALOGUE = "_passive_classes.yaml"

# Every SMITE 2 god page lists a basic attack, a passive and four abilities.
# Stance gods (Ullr, Merlin, Hel) list more; none lists fewer.
MIN_ABILITIES = 6
# Base stats every tracked god carries (90 of 90 on 2026-11-02; mana is
# absent on five, so it is not required). A page missing any did not parse.
REQUIRED_BASE_STATS = ("health", "health_regen", "physical_prot", "magical_prot",
                       "attack_speed", "attack_power", "move_speed")
# Stats no god has at zero. A page that reads them as 0.0 is a placeholder:
# Nox's, the day before release (2026-11-02), parses with every base stat 0.0.
POSITIVE_BASE_STATS = ("health", "attack_speed", "attack_power", "move_speed")
GOD_FIELDS = ("pantheon", "role", "damage_type")
# Bounds the per-run page loads, like `wiki_watch.PROBE_LIMIT`. Past the cap a
# candidate is logged as deferred, never dropped silently.
CANDIDATE_LIMIT = 12

# What the gate snapshots and puts back. Everything an add, or the recompute
# after it, can write.
OWNED_DIRS = ("Gods", "Items", "builds", "Analysis")
OWNED_FILES = (CATALOGUE, "_roster.json")
ICONS = Path("_assets") / "icons"


# -- discovery ----------------------------------------------------------------

_ICON_SRC_RE = re.compile(r"/T(\d)_[^/]*\.png")


def parse_item_index(html: str) -> dict:
    """{page title: tier} for every item the wiki's Items index links with a
    tier icon. The title, not the icon filename, is the page name: the icon
    drops spaces and punctuation the title keeps."""
    from bs4 import BeautifulSoup

    out = {}
    for a in BeautifulSoup(html, "html.parser").select(
            'span[typeof="mw:File"] a[href^="/w/"][title]'):
        img = a.find("img")
        m = _ICON_SRC_RE.search((img.get("src") or "") if img else "")
        if m and a["title"] not in out:
            out[a["title"]] = int(m.group(1))
    return out


def _removed_gods(data_root: Path) -> set:
    return {p.stem.casefold() for p in (data_root / "Gods" / "_removed").glob("*.md")}


def _tracked_item_keys(data_root: Path) -> set:
    return {refresh._icon_key(p.stem) for p in (data_root / "Items").glob("*.md")}


def discover(fetcher, data_root: Path) -> dict:
    """{roster, new_gods, new_items}. Two page loads."""
    roster = refresh.parse_roster_names(fetcher.fetch("Gods"))
    tracked = {p.stem for p in (data_root / "Gods").glob("*.md")}
    removed = _removed_gods(data_root)
    new_gods = [n for n in roster if n not in tracked and n.casefold() not in removed]

    keys = _tracked_item_keys(data_root)
    new_items = []
    for title in parse_item_index(fetcher.fetch("Items")):
        k = refresh._icon_key(title)
        if k in keys or refresh._ICON_VARIANT_SUFFIX_RE.sub("", k) in keys:
            continue
        new_items.append(title)
    return {"roster": roster, "new_gods": new_gods, "new_items": new_items}


# -- completeness ------------------------------------------------------------

def _numeric(value) -> bool:
    return stats_refresh._is_number(value)


def god_problems(parsed: dict) -> list:
    """Why this parse is not a whole god. [] means it is."""
    problems = [f"no {f}" for f in GOD_FIELDS if not parsed.get(f)]
    abilities = parsed.get("abilities") or []
    if len(abilities) < MIN_ABILITIES:
        problems.append(f"{len(abilities)} abilities read (a god page has at least {MIN_ABILITIES})")
    if any(not (a.get("name") or "").strip() for a in abilities):
        problems.append("an ability has no name")
    if abilities and stats_refresh._scaling_count({"abilities": abilities}) == 0:
        problems.append("no ability carries a scaling (the Ullr/Merlin symptom: "
                        "a kit read as names with no numbers)")
    base = parsed.get("base_stats") or {}
    missing = [s for s in REQUIRED_BASE_STATS if s not in base]
    if missing:
        problems.append(f"base stats missing: {missing}")
    for stat, row in base.items():
        vals = row.values() if isinstance(row, dict) else [row]
        if not all(_numeric(v) for v in vals if v is not None):
            problems.append(f"base stat {stat} does not parse: {row!r}")
    zero = [s for s in POSITIVE_BASE_STATS if s in base and not _positive_base(base[s])]
    if zero:
        problems.append(f"base stats read as zero (a placeholder page): {zero}")
    return problems


def _positive_base(row) -> bool:
    from smite import snapshots
    value = row.get("base") if isinstance(row, dict) else row
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return value > 0
    n = snapshots._parse_leading_number(value)
    return n is not None and n > 0


def item_problems(parsed: dict) -> list:
    problems = []
    if parsed.get("tier") in (None, ""):
        problems.append("no tier")
    if parsed.get("cost") is None or not _numeric(parsed.get("cost")):
        problems.append(f"no numeric cost ({parsed.get('cost')!r})")
    stats = parsed.get("stats") or {}
    if not stats:
        problems.append("no stats")
    for stat, value in stats.items():
        if not _numeric(value):
            problems.append(f"stat {stat} does not parse: {value!r}")
    return problems


# -- the passive catalogue -----------------------------------------------------

def _resolve(entry: dict, passive: str):
    """Same rule as `test_passive_catalogue.resolve`."""
    variants = entry.get("variants")
    if not variants:
        return entry
    hits = [v for v in variants if v["match"] in (passive or "")]
    return hits[0] if len(hits) == 1 else None


def _flag_keys(weights: dict) -> list:
    return sorted(k for k, v in weights.items() if k.startswith("price_") and v is True)


def _repriced_by(items: list, weights: dict, flag: str) -> set:
    """Names whose stat line changes under `flag` ALONE."""
    from smite import efficiency
    only = {k: v for k, v in weights.items() if not k.startswith("price_")}
    only[flag] = True
    before = efficiency.apply_pricing_flags({})
    try:
        printed = {it["name"]: efficiency.item_stat_values(it) for it in items}
        efficiency.apply_pricing_flags(only)
        priced = {it["name"]: efficiency.item_stat_values(it) for it in items}
    finally:
        efficiency.restore_pricing_flags(before)
    return {n for n in printed if printed[n] != priced[n]}


def flag_classes(items: list, catalogue: dict, weights: dict) -> dict:
    """{shipped flag: the one class code it prices}, read off the catalogue's
    existing entries: the codes in `priced` on every catalogued item that
    flag alone reprices. A flag whose items disagree, or that reprices
    nothing catalogued, maps to None — it cannot be claimed for a new item."""
    by_name = {it["name"]: it for it in items}
    out = {}
    for flag in _flag_keys(weights):
        codes = set()
        for name in _repriced_by(items, weights, flag):
            entry = (catalogue.get("items") or {}).get(name)
            resolved = _resolve(entry, by_name[name].get("passive")) if entry else None
            if resolved and resolved.get("priced"):
                codes.add(tuple(resolved["priced"]))
        out[flag] = codes.pop()[0] if len(codes) == 1 and len(next(iter(codes))) == 1 else None
    return out


def classify_passive(item: dict, items: list, catalogue: dict, weights: dict, today: str):
    """('none'|'catalogued'|'uncatalogued'|'auto', entry or None, problem or None).

    `items` is the pool INCLUDING `item`. The entry is what to append to the
    catalogue; None when nothing is to be written."""
    from smite import scoring
    passive = (item.get("passive") or "").strip()
    if not passive or not scoring.is_buildable(item):
        return "none", None, None
    existing = (catalogue.get("items") or {}).get(item["name"])
    if existing is not None:
        if _resolve(existing, passive) is None:
            return "none", None, ("the catalogue has an entry but no variant matches this "
                                  "passive text — a human has to classify the rework")
        return "catalogued", None, None
    weights = weights or {}
    hits = [f for f in _flag_keys(weights) if item["name"] in _repriced_by(items, weights, f)]
    if not hits:
        return "uncatalogued", {
            "uncatalogued": True,
            "added": today,
            "note": ("added unattended by smite.new_entities; passive not classified, so the "
                     "model values this item on its stat line alone"),
        }, None
    mapping = flag_classes(items, catalogue, weights)
    codes = [mapping.get(f) for f in hits]
    if None in codes:
        return "none", None, (f"shipped flag(s) {hits} reprice this passive and the catalogue "
                              "does not name one clause class for them")
    codes = sorted(set(codes))
    return "auto", {
        "classes": codes,
        "priced": codes,
        "added": today,
        "auto_classified": True,
        "note": (f"added unattended: {', '.join(hits)} already reprices this text, so the "
                 f"priced clause is {', '.join(codes)}; any other clause is unclassified"),
    }, None


def append_catalogue_entries(path: Path, entries: dict) -> None:
    """Append under `items:`, which is the file's last top-level key, so the
    hand-written comments above are untouched."""
    if not entries:
        return
    text = path.read_text(encoding="utf-8")
    last_key = [m.group(1) for m in re.finditer(r"^([A-Za-z_]+):", text, re.M)][-1]
    if last_key != "items":
        raise ValueError(f"{path.name}: `items:` is not the last top-level key")
    block = yaml.safe_dump(entries, sort_keys=False, allow_unicode=True, width=10_000)
    block = "".join("  " + line if line.strip() else line
                    for line in block.splitlines(keepends=True))
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text + "  # ── Added unattended by smite.new_entities ──\n" + block,
                    encoding="utf-8")


# -- writing -------------------------------------------------------------------

def _slug(name: str) -> str:
    return name.lower().replace(" ", "-").replace("'", "")


def write_god(data_root: Path, cand: dict, today: str) -> None:
    url = refresh.WIKI_BASE + cand["name"].replace(" ", "_")
    fm, block = refresh.god_note_content(cand["name"], cand["parsed"], url, today)
    notes.merge_god_note(data_root / "Gods" / f"{cand['name']}.md", fm, block)


def write_item(data_root: Path, cand: dict, today: str) -> None:
    url = refresh.WIKI_BASE + cand["name"].replace(" ", "_")
    fm = refresh.item_note_content(cand["name"], cand["parsed"], url, today)
    notes.merge_item_note(data_root / "Items" / f"{cand['name']}.md", fm,
                          cand["parsed"].get("passive", "") or "")


def link_components(data_root: Path, new_items: list) -> None:
    """Add each new item to its components' `builds_into`, in name order.
    Only those components: a full relink (`refresh.refresh_builds_into`) also
    rewrites unrelated lists that are stale for other reasons, and a new-item
    add should not carry that churn."""
    for c in new_items:
        for comp in c["parsed"].get("builds_from") or []:
            path = data_root / "Items" / f"{comp}.md"
            fm, body = notes.read_note(path)
            if not fm.get("name"):
                continue
            into = list(fm.get("builds_into") or [])
            if c["name"] not in into:
                fm["builds_into"] = sorted(into + [c["name"]])
                notes.write_note(path, fm, body)


def apply(data_root: Path, cands: list, today: str) -> None:
    """Write `cands` into `data_root`. Each candidate is a whole note plus,
    for an item, at most one catalogue entry."""
    entries = {}
    for c in cands:
        if c["kind"] == "god":
            write_god(data_root, c, today)
        else:
            write_item(data_root, c, today)
            if c.get("catalogue_entry"):
                entries[c["name"]] = c["catalogue_entry"]
        if c.get("community_entry"):
            notes.merge_build_note(data_root / "builds" / f"{c['name']}-Conquest.md",
                                   c["name"], "Conquest", c["community_entry"])
    link_components(data_root, [c for c in cands if c["kind"] == "item"])
    append_catalogue_entries(data_root / CATALOGUE, entries)


def write_roster(data_root: Path, roster: list) -> None:
    body = [{"name": n, "thumb": ""} for n in sorted(roster)]
    (data_root / "_roster.json").write_text(json.dumps(body, indent=2, ensure_ascii=False),
                                            encoding="utf-8")


def fetch_icons(data_root: Path, cands: list) -> None:
    """Cosmetic, best-effort, and outside the gate: an icon is not data."""
    import requests
    for c in cands:
        url = c["parsed"].get("image_url")
        targets = [(url, _slug(c["name"]))]
        if c["kind"] == "god":
            targets.append((wiki_parser.derive_headshot_url(url), _slug(c["name"]) + "-head"))
        for src, slug in targets:
            out = data_root / ICONS / f"{slug}.png"
            if not src or (out.exists() and out.stat().st_size > 1000):
                continue
            try:
                full = src if src.startswith("http") else "https://wiki.smite2.com" + src
                r = requests.get(full, timeout=20, headers={"User-Agent": stats_refresh.USER_AGENT})
                r.raise_for_status()
                out.parent.mkdir(parents=True, exist_ok=True)
                out.write_bytes(r.content)
            except Exception as exc:
                print(f"  [icon skip] {slug}: {exc}")


# -- the gate ------------------------------------------------------------------

def snapshot(data_root: Path, dest: Path) -> None:
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    present = []
    for d in OWNED_DIRS:
        if (data_root / d).is_dir():
            shutil.copytree(data_root / d, dest / d)
            present.append(d)
    for f in OWNED_FILES:
        if (data_root / f).is_file():
            shutil.copy2(data_root / f, dest / f)
            present.append(f)
    (dest / "manifest.json").write_text(json.dumps(present), encoding="utf-8")


def restore(saved: Path, data_root: Path) -> None:
    present = set(json.loads((saved / "manifest.json").read_text(encoding="utf-8")))
    for d in OWNED_DIRS:
        if (data_root / d).exists():
            shutil.rmtree(data_root / d)
        if d in present:
            shutil.copytree(saved / d, data_root / d)
    for f in OWNED_FILES:
        if (data_root / f).exists():
            (data_root / f).unlink()
        if f in present:
            shutil.copy2(saved / f, data_root / f)


GATE_PREFIX = "gate:"
GATES = {"gate:validate": ["smite.validate", "--check"],
         "gate:calibrate_combat": ["smite.calibrate_combat"]}


def run_checks(ids=None) -> set:
    """Failing check ids: pytest node ids plus `gate:*` for the job's two
    numeric gates. `ids` narrows the run. Raises on a suite that gave no
    verdict (`stats_gate.SuiteError`) — fail closed."""
    from smite import stats_gate
    tests = None if ids is None else {i for i in ids if not i.startswith(GATE_PREFIX)}
    gates = GATES if ids is None else {k: v for k, v in GATES.items() if k in ids}
    failed = set()
    if tests is None or tests:
        failed |= stats_gate.run_suite(tests)
    for gid, module in gates.items():
        proc = subprocess.run([sys.executable, "-m", *module], cwd=PIPELINE,
                              stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        print(f"[new entities] {gid} exit {proc.returncode}: "
              + " | ".join(proc.stdout.strip().splitlines()[-1:]))
        if proc.returncode != 0:
            failed.add(gid)
    return failed


def recompute() -> None:
    from smite import stats_gate
    stats_gate.recompute()


def gate(data_root: Path, cands: list, today: str, checks=run_checks,
         recompute=recompute) -> dict:
    """Write `cands`, keep the ones the checks allow. Returns {kept, excluded:
    {name: reason}, preexisting}. On a crash the data is put back as it was
    and the exception propagates — the caller logs it and keeps nothing."""
    saved = Path(tempfile.mkdtemp(prefix="new_entities_"))
    try:
        snapshot(data_root, saved)
        try:
            return _gate(data_root, saved, cands, today, checks, recompute)
        except BaseException:
            restore(saved, data_root)
            try:
                recompute()
            except Exception:
                traceback.print_exc(file=sys.stdout)
            raise
    finally:
        shutil.rmtree(saved, ignore_errors=True)


def _try(data_root, saved, subset, today, checks, recompute, ids=None) -> set:
    restore(saved, data_root)
    apply(data_root, subset, today)
    recompute()
    return checks(ids)


def _gate(data_root, saved, cands, today, checks, recompute) -> dict:
    failed = _try(data_root, saved, cands, today, checks, recompute)
    if not failed:
        return {"kept": cands, "excluded": {}, "preexisting": []}

    restore(saved, data_root)
    recompute()
    failed_old = checks(failed)
    attributable = failed - failed_old
    if not attributable:
        _try(data_root, saved, cands, today, checks=lambda ids: set(), recompute=recompute)
        return {"kept": cands, "excluded": {}, "preexisting": sorted(failed)}

    excluded = {}
    for c in cands:
        hit = _try(data_root, saved, [c], today, checks, recompute, ids=attributable) & attributable
        if hit:
            excluded[c["name"]] = "fails with it, passes without: " + ", ".join(sorted(hit))
    kept = [c for c in cands if c["name"] not in excluded]
    if not excluded:
        # Only the combination fails. No single one can be blamed, so none ships.
        reason = ("the set fails together and no single one alone: "
                  + ", ".join(sorted(attributable)))
        excluded = {c["name"]: reason for c in cands}
        kept = []

    if kept:
        again = _try(data_root, saved, kept, today, checks, recompute) - failed_old
        if again:
            reason = "the remaining set still fails: " + ", ".join(sorted(again))
            excluded.update({c["name"]: reason for c in kept})
            kept = []
    if not kept:
        restore(saved, data_root)
        recompute()
    return {"kept": kept, "excluded": excluded, "preexisting": sorted(failed & failed_old)}


# -- the run ---------------------------------------------------------------------

def community_entries(gods: list, community_fetcher) -> None:
    """Attach SmiteBrain's Conquest build to each new god, best effort. A god
    SmiteBrain has not published yet gets none — the model's own builds do
    not need it, and `refresh --community` fills it in once it exists."""
    if not gods or community_fetcher is None:
        return
    try:
        index = refresh.refresh_god_index(community_fetcher)
    except Exception as exc:
        print(f"  [community] god index unavailable: {exc}")
        index = {}
    for c in gods:
        try:
            html = community_fetcher.fetch(refresh.community_url(c["name"]))
            c["community_entry"] = refresh.community_build_entry(c["name"], html, index.get(c["name"]))
        except Exception as exc:
            print(f"  [community] {c['name']}: no SmiteBrain build yet ({exc})")


def prepare(fetcher, data_root: Path, today: str, limit: int = CANDIDATE_LIMIT) -> dict:
    """Discover, fetch and check. Writes nothing. Returns {roster, ready,
    skipped: [{name, kind, why}], deferred}."""
    from smite import recommend, scoring
    found = discover(fetcher, data_root)
    queue = [("god", n) for n in found["new_gods"]] + [("item", n) for n in found["new_items"]]
    ready, skipped = [], []
    for kind, name in queue[:limit]:
        try:
            html = fetcher.fetch(name)
        except stats_refresh.SourceError as exc:
            # A 404 is the grid leading the wiki; anything else is the source.
            if "HTTP 404" not in str(exc):
                raise
            skipped.append({"name": name, "kind": kind, "why": "no page yet (HTTP 404)"})
            continue
        try:
            parsed = (wiki_parser.parse_god_page if kind == "god" else wiki_parser.parse_item_page)(html)
        except Exception as exc:
            skipped.append({"name": name, "kind": kind, "why": f"does not parse: {exc}"})
            continue
        problems = god_problems(parsed) if kind == "god" else item_problems(parsed)
        if problems:
            skipped.append({"name": name, "kind": kind, "why": "incomplete: " + "; ".join(problems)})
            continue
        ready.append({"kind": kind, "name": name, "parsed": parsed})

    items = [c for c in ready if c["kind"] == "item"]
    if items:
        catalogue = yaml.safe_load((data_root / CATALOGUE).read_text(encoding="utf-8")) or {}
        weights = scoring.load_weights(data_root / "_weights.yaml")
        pool = recommend.load_items() if data_root == DATA_ROOT else _load_items(data_root)
        for c in items:
            fm = refresh.item_note_content(c["name"], c["parsed"], "", today)
            status, entry, problem = classify_passive(fm, pool + [fm], catalogue, weights, today)
            c["passive_status"], c["catalogue_entry"] = status, entry
            if problem:
                skipped.append({"name": c["name"], "kind": "item", "why": problem})
        ready = [c for c in ready if not any(s["name"] == c["name"] for s in skipped)]
    deferred = [n for _, n in queue[limit:]]
    return {"roster": found["roster"], "ready": ready, "skipped": skipped, "deferred": deferred}


def _load_items(data_root: Path) -> list:
    out = []
    for p in sorted((data_root / "Items").glob("*.md")):
        fm, _ = notes.read_note(p)
        if fm.get("name"):
            out.append(fm)
    return out


def _write_log(data_root: Path, today: str, result: dict) -> None:
    path = data_root / LOG_FILE
    try:
        log = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        log = {"added": []}
    log["added"] = log.get("added", []) + [
        {"name": c["name"], "kind": c["kind"], "date": today,
         **({"passive": c["passive_status"]} if c.get("passive_status") not in (None, "none") else {})}
        for c in result.get("kept", [])]
    log["last_run"] = {
        "date": today,
        "status": result["status"],
        "excluded": [{"name": n, "why": w} for n, w in sorted(result.get("excluded", {}).items())],
        "skipped": result.get("skipped", []),
        "deferred": result.get("deferred", []),
        **({"error": result["error"]} if result.get("error") else {}),
    }
    stats_refresh._atomic_write_json(path, log)


def _default_community(data_root: Path):
    if data_root != DATA_ROOT:
        return None
    from smite.cache import CachedFetcher
    return CachedFetcher(DATA_ROOT / "_cache" / "smitebrain")


def run(data_root: Path = DATA_ROOT, fetcher=None, today: str = None, dry_run: bool = False,
        use_gate: bool = True, checks=run_checks, recompute=recompute, icons=fetch_icons,
        community="default") -> dict:
    """status: 'nothing-new', 'dry-run', 'added', 'none-added', 'source-failed',
    'error'. Never raises on a source or gate problem."""
    data_root = Path(data_root)
    today = today or date.today().isoformat()
    fetcher = fetcher or stats_refresh.WikiPageFetcher()
    try:
        prep = prepare(fetcher, data_root, today)
    except stats_refresh.SourceError as exc:
        return {"status": "source-failed", "error": str(exc)}
    result = {"skipped": prep["skipped"], "deferred": prep["deferred"],
              "candidates": [(c["kind"], c["name"], c.get("passive_status")) for c in prep["ready"]]}
    if dry_run:
        return dict(result, status="dry-run")

    # The roster file follows the grid whether or not anything is added: it is
    # the viewer's list of every god, and it is what `wiki_watch` diffs.
    if prep["roster"]:
        write_roster(data_root, prep["roster"])

    cands = prep["ready"]
    community_entries([c for c in cands if c["kind"] == "god"],
                      _default_community(data_root) if community == "default" else community)
    if not cands:
        result["status"] = "nothing-new"
        _write_log(data_root, today, result)
        return result
    try:
        if use_gate:
            g = gate(data_root, cands, today, checks=checks, recompute=recompute)
        else:
            apply(data_root, cands, today)
            g = {"kept": cands, "excluded": {}, "preexisting": []}
    except Exception as exc:
        traceback.print_exc(file=sys.stdout)
        result.update(status="error", error=f"{type(exc).__name__}: {exc}", kept=[],
                      excluded={c["name"]: "gate crashed; nothing kept" for c in cands})
        _write_log(data_root, today, result)
        return result
    result.update(kept=g["kept"], excluded=g["excluded"], preexisting=g["preexisting"],
                  status="added" if g["kept"] else "none-added")
    if g["kept"]:
        icons(data_root, g["kept"])
    _write_log(data_root, today, result)
    return result


def report(result: dict) -> str:
    s = result["status"]
    if s == "source-failed":
        return f"::warning::[new entities] wiki unreachable, nothing added: {result['error']}"
    lines = []
    for c in result.get("kept", []):
        extra = f" (passive {c['passive_status']})" if c.get("passive_status") not in (None, "none") else ""
        lines.append(f"[new entities] added {c['kind']} {c['name']}{extra}")
        if c.get("passive_status") == "uncatalogued":
            lines.append(f"::warning::[new entities] {c['name']}: passive is UNCATALOGUED — valued on "
                         "its stat line only; classify it in data/_passive_classes.yaml")
    if s == "dry-run":
        lines += [f"[new entities] would add {k} {n}" + (f" (passive {p})" if p else "")
                  for k, n, p in result["candidates"]]
    for name, why in sorted((result.get("excluded") or {}).items()):
        lines.append(f"::error::[new entities] left out {name}: {why}")
    for sk in result.get("skipped", []):
        level = "" if sk["why"].startswith("no page yet") else "::warning::"
        lines.append(f"{level}[new entities] not added {sk['kind']} {sk['name']}: {sk['why']}")
    for n in result.get("deferred", []):
        lines.append(f"::warning::[new entities] deferred past the {CANDIDATE_LIMIT}-page cap: {n}")
    for t in result.get("preexisting", []):
        lines.append(f"::warning::[new entities] fails with and without the new entities: {t}")
    if result.get("error"):
        lines.append(f"::error::[new entities] {result['error']}")
    if not lines:
        lines.append("[new entities] nothing new on the wiki")
    return "\n".join(lines)


def _github_outputs(result: dict) -> None:
    out = os.environ.get("GITHUB_OUTPUT")
    if out:
        rejected = bool(result.get("excluded")) or result["status"] == "error"
        with open(out, "a", encoding="utf-8") as fh:
            fh.write(f"rejected={'true' if rejected else 'false'}\n")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Add gods and items the wiki has and data/ does not")
    ap.add_argument("--dry-run", action="store_true", help="discover and parse; write nothing")
    ap.add_argument("--no-gate", action="store_true", help="skip the test gate (local use only)")
    args = ap.parse_args(argv)
    try:
        sys.stdout.reconfigure(errors="replace")
    except Exception:
        pass
    try:
        result = run(dry_run=args.dry_run, use_gate=not args.no_gate)
    except Exception:
        print("::warning::[new entities] unexpected error, nothing added:")
        traceback.print_exc(file=sys.stdout)
        return 0
    print(report(result))
    _github_outputs(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
