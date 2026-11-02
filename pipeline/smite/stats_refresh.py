"""Refresh wiki item and god stats unattended, when a patch lands.

    python -m smite.stats_refresh            # refresh if due; always exits 0
    python -m smite.stats_refresh --force    # refresh even if not due
    python -m smite.stats_refresh --dry-run  # fetch + validate, write nothing

WHEN IT RUNS. Daily, from `refresh-data.yml`, right after `smite.patch_feed`.
It is DUE when the game patch the feed recorded is newer than the patch the
item data was scraped under (`_patch.json`: `patch` > `data_patch`), or when
the last successful refresh is `WEEKLY_DAYS` old (wiki editors fix numbers
between patches). Not due, it makes no request at all.

A patch that is due but that the WIKI has not caught up with yet — its
Patch_notes index still names the label we hold — costs one request and
waits. The wiki trails the game by days; scraping 316 pages to learn nothing
new, every morning until it catches up, would be rude for no gain.

THE SOURCE, AND WHY THIS AND NOT THE BROWSER. Measured from a GitHub-hosted
runner on 2026-11-02 (`.github/workflows/probe-stat-sources.yml`):

    wiki.smite2.com, spoofed Chrome UA        403  cf-mitigated=challenge
    wiki.smite2.com, honest bot UA            200  full article HTML
    headless Chromium                         200
    api.php                                   200, but robots.txt says
                                              `Disallow: /*api.php` for `*`

Cloudflare challenges clients that CLAIM to be a browser and cannot run JS;
it does not challenge a client that says what it is. So this is plain
`requests` against the article pages robots.txt allows (`/w/<Page>`), with an
identifying User-Agent and the same 2.5s floor the manual scraper uses. No
browser, no api.php. Parser parity on that HTML was checked on the runner for
Bancroft's Talon, Deathbringer, Mote of Chaos, Chiron, Ullr and Merlin — the
last two being the stance-tab gods whose kits once parsed to empty — and
`tests/fixtures/recorded/` holds those responses. Content is Weird Gloop's,
CC BY-NC-SA; Ichor is non-commercial and every note keeps its `source_url`.

WHY THIS IS SAFE TO RUN UNATTENDED WHEN `refresh --all` IS NOT. The case
against scheduling the scrape (`wiki_watch`, STATE.md §6) is that
`refresh_all` writes each note as it goes, and a silent parse miss
overwrites the only copy: blanking Ullr, Artio and Merlin's kits PASSes every
downstream gate. This path is built around that measurement:

  1. ALL-OR-NOTHING. Every tracked god and item is fetched and parsed into
     memory first. One failure — network, Cloudflare, a parser exception, a
     `ParseCollapse` — and nothing is written. Data is never a mix of two
     patches.
  2. PER-NOTE GUARDS, the same ones the manual path uses
     (`refresh._refuse_god_collapse`, `_refuse_item_collapse`), plus the
     exact Ullr symptom: a god whose scaling-ability count goes from >0 to 0.
     `--allow-shrink` is not offered here: a genuine rework is a human's call.
  3. AGGREGATE CHECKS against the data being replaced (`validate`): counts of
     gods with kits, items with stats, items with a cost, total abilities and
     aspects may not fall by more than `TOLERANCE`; key fields may not go
     null en masse; every stat and base stat must parse as a number.
  4. ATOMIC WRITE. The new Gods/ and Items/ are built in a staging directory
     beside the live ones and swapped in by rename. `data_from` in the patch
     history is set only after the swap succeeds.

Then the daily job's own gates (`validate --check`, `calibrate_combat`) run on
the result before anything is committed; a failing gate fails the job and
commits nothing, which on a runner is a full rollback.

FAILURE NEVER FAILS THE COMMUNITY REFRESH. `main` exits 0 on every path. A
refused refresh prints `::warning::` lines (visible on the run summary) and
leaves the data exactly as it was; the community half of the job proceeds.

WHAT IT DOES NOT DO. It refreshes what is tracked. A brand-new god or item
is still `wiki_watch`'s job to announce and a human's to add (STATE.md §6).
Icons are not touched: every tracked note already has one.
"""
import argparse
import json
import os
import shutil
import sys
import time
import traceback
from datetime import date, timedelta
from pathlib import Path

from smite import notes, refresh, snapshots, wiki_parser

DATA_ROOT = refresh.DATA_ROOT
WIKI_BASE = refresh.WIKI_BASE
STATE_FILE = "_stats_refresh.json"
WEEKLY_DAYS = 7
USER_AGENT = "ichor-gg/1.0 (+https://github.com/jacob-colby/ichor-gg; patch-day stats refresh)"
MIN_INTERVAL = 2.5
RETRIES = 3
# How far a coverage count may fall before the refresh is refused: the larger
# of an absolute and a relative slack. A patch can remove an item or two; it
# does not strip stats from a dozen.
TOLERANCE_ABS = 2
TOLERANCE_REL = 0.02
# Fields whose mass disappearance means the page shape moved, not the game.
GOD_KEY_FIELDS = ("pantheon", "role", "damage_type")
ITEM_KEY_FIELDS = ("tier",)


class SourceError(Exception):
    """The source could not be read. Nothing is written."""


class ValidationError(Exception):
    """The source was read but the result is not fit to replace what we have."""


# -- fetching ---------------------------------------------------------------

class WikiPageFetcher:
    """Plain HTTP for robots-allowed wiki article pages, with an honest UA.

    A Cloudflare challenge is a SourceError, never page content: its body is
    42KB of HTML that `parse_*_page` would reject with "no infobox", which
    would read as a parser problem rather than as the source being shut."""

    def __init__(self, session=None, min_interval: float = MIN_INTERVAL,
                 retries: int = RETRIES, sleep=time.sleep):
        import requests
        self.session = session or requests.Session()
        self.session.headers["User-Agent"] = USER_AGENT
        self.min_interval = min_interval
        self.retries = retries
        self.sleep = sleep
        self._last = 0.0
        self.requests = 0

    def fetch(self, page: str) -> str:
        url = WIKI_BASE + page.replace(" ", "_")
        last_exc = None
        for attempt in range(self.retries):
            wait = self.min_interval - (time.time() - self._last)
            if wait > 0:
                self.sleep(wait)
            try:
                self.requests += 1
                resp = self.session.get(url, timeout=30)
            except Exception as exc:
                last_exc = exc
            else:
                if resp.headers.get("cf-mitigated"):
                    raise SourceError(f"{page}: Cloudflare challenge "
                                      f"(cf-mitigated={resp.headers['cf-mitigated']})")
                if resp.status_code == 200:
                    return resp.text
                last_exc = SourceError(f"{page}: HTTP {resp.status_code}")
                if resp.status_code not in (429, 500, 502, 503, 504):
                    raise last_exc
            finally:
                self._last = time.time()
            self.sleep(2 ** attempt * self.min_interval)
        raise SourceError(f"{page}: {last_exc}")


# -- when to run ------------------------------------------------------------

def load_state(data_root: Path) -> dict:
    try:
        return json.loads((Path(data_root) / STATE_FILE).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def due_reason(data_root: Path, today: str):
    """'patch', 'weekly', or None."""
    data_root = Path(data_root)
    try:
        current = json.loads((data_root / "_patch.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        current = {}
    game = snapshots.patch_number(current.get("patch"))
    data = snapshots.patch_number(current.get("data_patch"))
    if game is not None and (data is None or game > data):
        return "patch"
    last = load_state(data_root).get("last_success")
    if not last or str(last) <= (date.fromisoformat(today) - timedelta(days=WEEKLY_DAYS)).isoformat():
        return "weekly"
    return None


# -- reading what we have ---------------------------------------------------

def _load_dir(directory: Path) -> dict:
    """{name: (path, frontmatter, body)} for every note with a name."""
    out = {}
    for path in sorted(Path(directory).glob("*.md")):
        fm, body = notes.read_note(path)
        if fm.get("name"):
            out[fm["name"]] = (path, fm, body)
    return out


# -- validation -------------------------------------------------------------

def _scaling_count(god_fm: dict) -> int:
    from smite import kit
    try:
        return kit.scaling_profile(god_fm).get("n_scaling_abilities", 0)
    except Exception:
        return 0


def _is_number(value) -> bool:
    if isinstance(value, bool):
        return False
    if isinstance(value, (int, float)):
        return True
    return snapshots._parse_leading_number(value) is not None


def _slack(n_old: int) -> int:
    return max(TOLERANCE_ABS, int(n_old * TOLERANCE_REL))


def coverage(gods: dict, items: dict) -> dict:
    """The counts a parse-shape change would move. `gods` / `items` are
    {name: frontmatter}."""
    return {
        "gods with abilities": sum(1 for g in gods.values() if g.get("abilities")),
        "gods with scaling abilities": sum(1 for g in gods.values() if _scaling_count(g) > 0),
        "gods with base stats": sum(1 for g in gods.values() if g.get("base_stats")),
        "abilities": sum(len(g.get("abilities") or []) for g in gods.values()),
        "aspects": sum(len(g.get("aspects") or []) for g in gods.values()),
        "items with stats": sum(1 for i in items.values() if i.get("stats")),
        "items with a cost": sum(1 for i in items.values() if i.get("cost") is not None),
    }


def validate(old_gods: dict, new_gods: dict, old_items: dict, new_items: dict) -> list:
    """Problems that make the new set unfit to replace the old. [] means fit.
    All four arguments are {name: frontmatter}."""
    problems = []
    if set(new_gods) != set(old_gods):
        problems.append(f"god set changed: missing {sorted(set(old_gods) - set(new_gods))}")
    if set(new_items) != set(old_items):
        problems.append(f"item set changed: missing {sorted(set(old_items) - set(new_items))}")

    before, after = coverage(old_gods, old_items), coverage(new_gods, new_items)
    for key, n_old in before.items():
        if after[key] < n_old - _slack(n_old):
            problems.append(f"{key}: {n_old} -> {after[key]}")

    for kind, old, new, fields in (("god", old_gods, new_gods, GOD_KEY_FIELDS),
                                   ("item", old_items, new_items, ITEM_KEY_FIELDS)):
        for field in fields:
            n_old = sum(1 for fm in old.values() if fm.get(field) is None)
            n_new = sum(1 for fm in new.values() if fm.get(field) is None)
            if n_new > n_old + _slack(len(new)):
                problems.append(f"{kind} {field} null on {n_new} notes (was {n_old})")

    for name, fm in new_gods.items():
        if (old_gods.get(name) and _scaling_count(old_gods[name]) > 0
                and _scaling_count(fm) == 0):
            problems.append(f"{name}: scaling abilities -> 0 (the Ullr symptom)")
        for stat, row in (fm.get("base_stats") or {}).items():
            vals = row.values() if isinstance(row, dict) else [row]
            if not all(_is_number(v) for v in vals if v is not None):
                problems.append(f"{name}: base stat {stat} does not parse: {row!r}")
    for name, fm in new_items.items():
        for stat, value in (fm.get("stats") or {}).items():
            if not _is_number(value):
                problems.append(f"{name}: stat {stat} does not parse: {value!r}")
        cost = fm.get("cost")
        if cost is not None and not _is_number(cost):
            problems.append(f"{name}: cost does not parse: {cost!r}")
    return problems


# -- the run ----------------------------------------------------------------

def _comparable(fm: dict) -> dict:
    return {k: v for k, v in fm.items() if k != "last_verified"}


def scrape(fetcher, old_gods: dict, old_items: dict, today: str):
    """Fetch and parse every tracked note. Returns ({name: (fm, wiki_block)},
    {name: (fm, passive)}). Raises SourceError on the first unreachable page —
    the source is down, and 300 more requests will not change that — and
    ValidationError listing every page that read but did not parse."""
    failures = []
    gods = {}
    for name, (_, old_fm, _) in old_gods.items():
        try:
            parsed = wiki_parser.parse_god_page(fetcher.fetch(name))
            refresh._refuse_god_collapse(name, old_fm, parsed)
            gods[name] = refresh.god_note_content(name, parsed, WIKI_BASE + name.replace(" ", "_"), today)
        except SourceError:
            raise
        except Exception as exc:
            failures.append(f"god {name}: {exc}")
    items = {}
    for name, (_, old_fm, _) in old_items.items():
        try:
            parsed = wiki_parser.parse_item_page(fetcher.fetch(name))
            refresh._refuse_item_collapse(name, old_fm, parsed)
            fm = refresh.item_note_content(name, parsed, WIKI_BASE + name.replace(" ", "_"), today)
            items[name] = (fm, parsed.get("passive", "") or "")
        except SourceError:
            raise
        except Exception as exc:
            failures.append(f"item {name}: {exc}")
    if failures:
        raise ValidationError(f"{len(failures)} page(s) did not parse: " + "; ".join(failures))
    into = refresh.builds_into_map({n: fm.get("builds_from", []) for n, (fm, _) in items.items()})
    for name, (fm, _) in items.items():
        fm["builds_into"] = into[name]
    return gods, items


def _changed(old: dict, new_fm: dict) -> bool:
    return _comparable(old) != _comparable(new_fm)


def _stage(live: Path, staging: Path, old: dict, new: dict) -> int:
    """Copy `live` to `staging` and apply the changed notes there. Returns how
    many notes changed. The note body outside the WIKI block is preserved, the
    same splice `merge_god_note` does for the manual path."""
    shutil.copytree(live, staging)
    n = 0
    for name, (fm, block) in new.items():
        path, old_fm, _ = old[name]
        if not _changed(old_fm, fm):
            continue
        notes.merge_god_note(staging / path.name, fm, block)
        n += 1
    return n


def _swap(pairs) -> None:
    """[(live, staged)] -> staged becomes live. Each live dir is renamed aside
    first, so a failure part-way puts every one back."""
    moved = []
    try:
        for live, staged in pairs:
            backup = live.with_name(live.name + ".bak")
            if backup.exists():
                shutil.rmtree(backup)
            os.replace(live, backup)
            moved.append((live, backup))
            os.replace(staged, live)
    except Exception:
        for live, backup in reversed(moved):
            if live.exists():
                shutil.rmtree(live)
            os.replace(backup, live)
        raise
    for _, backup in moved:
        shutil.rmtree(backup, ignore_errors=True)


def _atomic_write_json(path: Path, body) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(body, indent=2) + "\n", encoding="utf-8")
    os.replace(tmp, path)


def run(data_root: Path = DATA_ROOT, fetcher=None, today: str = None,
        force: bool = False, dry_run: bool = False) -> dict:
    """One refresh. Returns {status, reason, ...}; status is one of
    'not-due', 'waiting-for-wiki', 'unchanged', 'refreshed', 'dry-run',
    'source-failed', 'refused'. Raises only on a bug."""
    data_root = Path(data_root)
    today = today or date.today().isoformat()
    reason = "forced" if force else due_reason(data_root, today)
    if reason is None:
        return {"status": "not-due"}

    current = json.loads((data_root / "_patch.json").read_text(encoding="utf-8"))
    data_n = snapshots.patch_number(current.get("data_patch"))
    fetcher = fetcher or WikiPageFetcher()

    try:
        wiki_patch = None
        html = fetcher.fetch("Patch notes")
        nums = [int(m.group(1)) for m in refresh._PATCH_VERSION_RE.finditer(html)]
        wiki_patch = f"Open Beta {max(nums)}" if nums else None
        if wiki_patch is None:
            return {"status": "refused", "reason": reason,
                    "problems": ["the wiki's Patch_notes index names no patch — "
                                 "cannot say which patch the data would be"]}
        wiki_n = snapshots.patch_number(wiki_patch)
        if reason == "patch" and data_n is not None and wiki_n <= data_n:
            return {"status": "waiting-for-wiki", "reason": reason, "wiki_patch": wiki_patch,
                    "game_patch": current.get("patch")}

        old_gods = _load_dir(data_root / "Gods")
        old_items = _load_dir(data_root / "Items")
        if not old_gods or not old_items:
            return {"status": "refused", "reason": reason,
                    "problems": ["no tracked gods or items to refresh"]}
        gods, items = scrape(fetcher, old_gods, old_items, today)
    except SourceError as exc:
        return {"status": "source-failed", "reason": reason, "error": str(exc)}
    except ValidationError as exc:
        return {"status": "refused", "reason": reason, "problems": [str(exc)]}

    problems = validate({n: v[1] for n, v in old_gods.items()}, {n: v[0] for n, v in gods.items()},
                        {n: v[1] for n, v in old_items.items()}, {n: v[0] for n, v in items.items()})
    if problems:
        return {"status": "refused", "reason": reason, "problems": problems}

    changed_gods = [n for n, (fm, _) in gods.items() if _changed(old_gods[n][1], fm)]
    changed_items = [n for n, (fm, _) in items.items() if _changed(old_items[n][1], fm)]
    result = {"reason": reason, "wiki_patch": wiki_patch, "changed_gods": changed_gods,
              "changed_items": changed_items, "requests": getattr(fetcher, "requests", None)}
    if dry_run:
        return dict(result, status="dry-run")

    if changed_gods or changed_items:
        staging = data_root / ".stats_staging"
        if staging.exists():
            shutil.rmtree(staging)
        staging.mkdir()
        try:
            _stage(data_root / "Gods", staging / "Gods", old_gods, gods)
            _stage(data_root / "Items", staging / "Items", old_items, items)
            _swap([(data_root / "Gods", staging / "Gods"),
                   (data_root / "Items", staging / "Items")])
        finally:
            shutil.rmtree(staging, ignore_errors=True)

    # Only now, with the notes in place, does the history say the data is
    # this patch's. `record_patch` is a no-op when the label already has one.
    history_path = data_root / "_patch_history.json"
    snapshots.record_patch(wiki_patch, today, history_path)
    snapshots.write_current_patch(snapshots.load_patch_history(history_path, fallback=False),
                                  data_root / "_patch.json")
    _atomic_write_json(data_root / STATE_FILE, {
        "last_success": today, "wiki_patch": wiki_patch, "reason": reason,
        "gods_changed": len(changed_gods), "items_changed": len(changed_items)})
    return dict(result, status="refreshed" if (changed_gods or changed_items) else "unchanged")


def report(result: dict) -> str:
    s = result["status"]
    if s == "not-due":
        return "[stats refresh] not due: item data matches the game patch and was checked this week"
    if s == "waiting-for-wiki":
        return (f"[stats refresh] game is on {result['game_patch']}, the wiki still says "
                f"{result['wiki_patch']} — waiting for it to catch up, nothing written")
    if s == "source-failed":
        return f"::warning::[stats refresh] source unreachable, data kept as it was: {result['error']}"
    if s == "refused":
        lines = [f"::warning::[stats refresh] refused, data kept as it was ({len(result['problems'])} problem(s)):"]
        lines += [f"::warning::  - {p}" for p in result["problems"][:25]]
        return "\n".join(lines)
    head = {"unchanged": "checked, no stat changed",
            "refreshed": "refreshed", "dry-run": "dry run, nothing written"}[s]
    out = (f"[stats refresh] {head} ({result['reason']}): wiki {result['wiki_patch']}, "
           f"{len(result['changed_gods'])} god(s) and {len(result['changed_items'])} item(s) changed, "
           f"{result.get('requests')} requests")
    for kind in ("changed_gods", "changed_items"):
        if result[kind]:
            out += f"\n  {kind.split('_')[1]}: " + ", ".join(result[kind][:40]) + (
                " ..." if len(result[kind]) > 40 else "")
    return out


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Refresh wiki item/god stats when a patch lands")
    parser.add_argument("--force", action="store_true", help="refresh even if not due")
    parser.add_argument("--dry-run", action="store_true", help="fetch and validate, write nothing")
    args = parser.parse_args(argv)
    try:
        print(report(run(force=args.force, dry_run=args.dry_run)))
    except Exception:
        # A bug here must not cost the day's community data; the log is the alarm.
        print("::warning::[stats refresh] unexpected error, data kept as it was:")
        traceback.print_exc(file=sys.stdout)
    return 0


if __name__ == "__main__":
    sys.exit(main())
