"""Tell someone the wiki moved. Do not touch the data.

WHY THIS EXISTS RATHER THAN A SCHEDULED SCRAPE. Ravana shipped and the site
did not know, because nothing on any schedule reads the wiki: the daily job
pulls SmiteBrain only, and `refresh --all` re-pulls what is ALREADY tracked,
so scheduling it would not have found him either. The missing piece is not a
scrape, it is a NOTIFICATION.

WHY NOT SCHEDULE THE SCRAPE ANYWAY. Because the parser's failure mode is
silent and destructive, and none of the gates can see it:

    `parse_god_page` raises on exactly one thing, a missing infobox. Every
    other shape change degrades to empty. `notes.merge_god_note` then
    REPLACES the note's frontmatter, and the note is the only copy.

    Measured 2026-08-29: blanking the kits of Ullr, Artio and Merlin — the
    three gods this actually happened to (STATE.md §7, `_section_tables`) —
    and recomputing their cores moves win-weighted coverage 0.5530 -> 0.5552,
    UP, leaves `validate --check` PASSing, and produces zero `data_audit`
    findings. A gate on those numbers is a gate on nothing.

So the asymmetry runs one way. Automated and wrong: the site silently serves a
god whose kit is empty, cores shift, and the only detector is a human noticing
a build looks off — for Ullr that took a Masters player. Manual and late: a god
is missing for a few days, which is self-announcing and costs one command. Be
wrong toward missing data, never toward wrong data.

WHAT IT WATCHES, AND WHY NOT A COUNT. Three signals — roster NAMES, the patch
string, and whether an untracked god's page is actually there. Not a count:
the roster grid leads the wiki's own content. On 2026-08-29 it listed 92 gods,
of which Hachiman and Hel are placeholder pages reading "There is currently no
text in this page". A count-based detector would have filed both as work.

    python -m smite.wiki_watch                 # exit 1 if there is something to do
    python -m smite.wiki_watch --out issue.md  # ...and write the issue body
"""
import argparse
import json
import sys
from pathlib import Path

from smite import refresh, wiki_parser
from smite.browser_fetch import BrowserFetcher

# An untracked roster entry costs one page load to classify. Bounded so a
# wiki-side accident (the grid picking up a category page, say) cannot turn a
# two-request job into a hundred-request one against Cloudflare. Anything past
# the cap is REPORTED as unprobed, never silently dropped.
PROBE_LIMIT = 12

READY = "ready"
NO_PAGE = "no-page"
UNPROBED = "unprobed"
# An infobox but no abilities. Distinct from NO_PAGE on purpose: NO_PAGE is
# the wiki being slow, this is the wiki being SHAPED differently than the
# parser expects — the loudest thing this job can find, because it is the
# failure mode that used to reach the data silently.
HALF_PARSED = "half-parsed"


def _tracked_gods(data_root: Path) -> set:
    return {p.stem for p in (data_root / "Gods").glob("*.md")}


def _recorded_roster(data_root: Path) -> list:
    path = data_root / "_roster.json"
    if not path.exists():
        return []
    try:
        return [g["name"] for g in json.loads(path.read_text(encoding="utf-8"))]
    except (ValueError, KeyError, TypeError):
        return []


def _recorded_patch(data_root: Path):
    path = data_root / "_patch.json"
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8")).get("patch")
    except ValueError:
        return None


def probe_god(name: str, wiki_fetcher, force: bool = False) -> dict:
    """Is this roster entry a god we could actually scrape?

    The distinction the report is built on. A name on the grid means the wiki
    editors have made a slot; it does not mean there is a page behind it."""
    try:
        html = wiki_fetcher.fetch(refresh.WIKI_BASE + name.replace(" ", "_"),
                                  force=force)
        parsed = wiki_parser.parse_god_page(html)
    except Exception as exc:
        return {"name": name, "state": NO_PAGE, "abilities": 0, "why": str(exc)}
    n = len(parsed.get("abilities") or [])
    return {"name": name, "state": READY if n else HALF_PARSED, "abilities": n,
            "role": parsed.get("role"),
            "why": "" if n else "infobox parsed, zero abilities read"}


def survey(wiki_fetcher, data_root: Path = None, force: bool = False,
           probe_limit: int = PROBE_LIMIT) -> dict:
    """Compare the live wiki to what the vault records. Writes nothing."""
    data_root = data_root or refresh.DATA_ROOT

    live = refresh.parse_roster_names(
        wiki_fetcher.fetch(refresh.WIKI_BASE + "Gods", force=force))
    recorded = _recorded_roster(data_root)
    tracked = _tracked_gods(data_root)

    untracked_names = [n for n in live if n not in tracked]
    probes = [probe_god(n, wiki_fetcher, force=force)
              for n in untracked_names[:probe_limit]]
    probes += [{"name": n, "state": UNPROBED, "abilities": 0,
                "why": f"past the {probe_limit}-probe cap"}
               for n in untracked_names[probe_limit:]]

    patch_live = refresh.scrape_patch_version(wiki_fetcher, force=force)
    patch_recorded = _recorded_patch(data_root)

    return {
        "roster_live": live,
        "roster_recorded": recorded,
        "roster_new": [n for n in live if n not in recorded],
        # A god leaving the grid is not a routine event, and if it happens the
        # roster file and the notes disagree with the wiki in a way no other
        # check here would mention.
        "roster_gone": sorted(set(recorded) - set(live)),
        "tracked_gone": sorted(tracked - set(live)),
        "untracked": probes,
        "patch_live": patch_live,
        "patch_recorded": patch_recorded,
    }


def actionable(result: dict) -> bool:
    """Is there something a human should do? A roster entry with no page is
    NOT actionable — Hachiman and Hel would otherwise file a ticket a day
    until whenever the wiki gets round to writing them up."""
    return bool(
        [p for p in result["untracked"] if p["state"] in (READY, UNPROBED, HALF_PARSED)]
        or result["roster_gone"] or result["tracked_gone"]
        or (result["patch_live"] and result["patch_live"] != result["patch_recorded"])
    )


def report_markdown(result: dict) -> str:
    ready = [p for p in result["untracked"] if p["state"] == READY]
    no_page = [p for p in result["untracked"] if p["state"] == NO_PAGE]
    unprobed = [p for p in result["untracked"] if p["state"] == UNPROBED]
    half = [p for p in result["untracked"] if p["state"] == HALF_PARSED]

    lines = [
        f"The wiki lists **{len(result['roster_live'])}** gods. "
        f"`data/_roster.json` records **{len(result['roster_recorded'])}**, and "
        f"`data/Gods/` tracks **{len(result['roster_live']) - len(result['untracked'])}** "
        f"of the live roster.",
        "",
    ]

    if ready:
        lines += ["## Ready to add", ""]
        for p in ready:
            lines.append(f"- **{p['name']}** — page parses, {p['abilities']} abilities"
                         + (f", role {p['role']}" if p.get("role") else ""))
        lines += [
            "",
            "```bash",
            "cd pipeline && python -m smite.refresh --roster",
            *[f"python -m smite.refresh --refresh '{p['name']}' --kind god" for p in ready],
            *[f"python -m smite.refresh --refresh-builds '{p['name']}'" for p in ready],
            "python -m smite.recommend --all && python -m smite.build_index",
            "```",
            "",
            "Run it locally, not here. The scrape overwrites god notes wholesale "
            "and no gate in this repo can see a kit that silently parsed to "
            "empty — see `smite/wiki_watch.py` for the measurement.",
            "",
        ]

    if half:
        lines += [
            "## The parser could not read these",
            "",
            *[f"- **{p['name']}** — {p['why']}" for p in half],
            "",
            "A god page with an infobox and no abilities is a PARSER problem, not "
            "a wiki-is-slow problem. This is the shape `wiki_parser._section_tables` "
            "got wrong for Ullr, Artio and Merlin. Fix the parser; do not add the "
            "god around it.",
            "",
        ]

    if no_page:
        lines += ["## Listed, but not there yet", ""]
        for p in no_page:
            lines.append(f"- {p['name']} — {p['why']}")
        lines += ["", "No action. The roster grid leads the wiki's own content.", ""]

    if unprobed:
        lines += ["## Not probed", ""]
        for p in unprobed:
            lines.append(f"- {p['name']} — {p['why']}")
        lines.append("")

    if result["roster_gone"] or result["tracked_gone"]:
        lines += ["## Off the roster", ""]
        for n in result["roster_gone"]:
            lines.append(f"- {n} — in `_roster.json`, not on the wiki")
        for n in result["tracked_gone"]:
            lines.append(f"- {n} — tracked under `data/Gods/`, not on the wiki")
        lines.append("")

    if result["patch_live"] and result["patch_live"] != result["patch_recorded"]:
        lines += [
            "## Patch",
            "",
            f"Wiki says **{result['patch_live']}**, `data/_patch.json` says "
            f"**{result['patch_recorded']}**. Item stats may have moved; a full "
            "`refresh_and_deploy` is what banks the snapshot that makes patch "
            "notes say so.",
            "",
        ]

    return "\n".join(lines).rstrip() + "\n"


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Watch wiki.smite2.com for roster/patch changes")
    parser.add_argument("--out", help="write the report markdown here")
    parser.add_argument("--force", action="store_true", help="bypass the local cache")
    args = parser.parse_args(argv)

    # God names and this report both carry non-ASCII. A redirected or cron
    # stdout may be on a non-UTF-8 codepage; same guard as `data_audit.main`.
    try:
        sys.stdout.reconfigure(errors="replace")
    except Exception:
        pass

    fetcher = BrowserFetcher(refresh.DATA_ROOT / "_cache" / "wiki")
    result = survey(fetcher, force=args.force)
    report = report_markdown(result)

    print(report)
    if args.out:
        Path(args.out).write_text(report, encoding="utf-8")

    if not actionable(result):
        print("wiki_watch: nothing to do")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
