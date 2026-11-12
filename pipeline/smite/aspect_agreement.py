"""How much of what an aspect's players hold is in the build the aspect toggle
shows. A DIAGNOSTIC: it reads the match store and the shipped notes and feeds
nothing back.

    python -m smite.aspect_agreement      # -> data/Analysis/_aspect_agreement.md

WHY THIS EXISTS (2026-11-11, docs/accuracy-levers-2026-11-11.md lever 5).
`model_audit heldout` scores Conquest's base-kit `core` and cannot see an
aspect build; the frozen reference builds say an aspect build MOVED, never
whether it moved toward anything. Since 2026-11-08 there is a record of what
aspect players buy (`aspect_matches`, `community_aspects` in each Conquest
note), and nothing compared a build with it. STATE.md section 5 names the next
model change for aspects (a build that can change ROLE); this is the
instrument that change would be read on, built first so the change is not its
own judge.

THE FIGURE. For each aspect whose record is `shown` (the store's own 30-match
floor and window rule, read from the note so this agrees with the page):

  target   the six TIER-3 items held in the largest share of that aspect's
           matches, over the windows the entry names. Tier 3 only, because a
           held component is an unfinished build, the cleaning
           `community_target` applies to the god's own record.
  shown    what the toggle gives a reader: the aspect's `core` where one
           ships, else the base `core` (the toggle falls back to it).
  overlap  |shown and target| / 6.

Beside it, the same god's base `core` against the same target, so a shipped
aspect build is read against doing nothing; and the base `core` against the
god's own pooled community target (`community_target`'s scored slots, what
`validate` reads), which is the level agreement runs at when the kit matches.

WHAT IT IS NOT. "Most held" is a share of games, not a slot record: it has no
alternates and no order, so it is not `validate`'s coverage and the two are
not on one scale. It is agreement, so everything STATE.md section 1 says
about agreement applies: a better and unconventional aspect build scores
lower. A thin aspect can be a few players (`aspect_matches`: Mangetsu's 73
matches were 28 players). And it reads the `core`, whose base-kit form reads
win and pick from the god's POOLED record, which for a minority aspect is
mostly other players.

FIRST READING (2026-11-11, main 1a9ca2d5, fingerprint 89eb181b72f1; 79
aspects shown, 11 below the floor). The toggle's build holds 19% of the
aspect players' six; the same gods' base `core` holds 48% of their pooled
community target. Where the aspect is played in another role (38 aspects) it
is 10%, in the base role (41) 28%, and 35 aspects share no item at all. The
six hand overlays that ship a build and have a shown record hold 6% where the
base build holds 0%: Cernunnos and Chronos 1 of 6, Agni, Chiron, Morgan Le Fay
and Ra 0 of 6. The seventh overlay's aspect has no shown record.

FEEDS NOTHING. `scoring`, `assemble`, `recommend`, `build_index` and
`efficiency` do not import this module, and a test holds that.
"""
import argparse
import statistics
import sys
from collections import Counter
from pathlib import Path

from smite import aspect_matches as am
from smite import community_target, recommend, validate

REPO_ROOT = Path(__file__).resolve().parents[2]
REPORT_PATH = REPO_ROOT / "data" / "Analysis" / "_aspect_agreement.md"
FINISHED_TIER = "3"
TARGET_SIZE = 6
ARCHETYPE = "core"


def aspect_target(records: list, names: dict, tiers: dict, size: int = TARGET_SIZE) -> list:
    """The `size` tier-3 items held in the most of these matches, by our
    names. Ties break on the name, so the target is stable. Fewer than `size`
    when the matches do not hold that many distinct finished items."""
    held = Counter()
    for r in records:
        for slug in {s for s in r.get("items") or [] if s}:
            name = names.get(slug)
            if name is not None and str(tiers.get(name)) == FINISHED_TIER:
                held[name] += 1
    return [n for n, _ in sorted(held.items(), key=lambda kv: (-kv[1], kv[0]))[:size]]


def suggested(note: dict, archetype: str, aspect=None) -> list:
    """One shipped build's six: the base kit's, or one aspect's."""
    for b in note.get("builds") or []:
        if (b.get("source") == "suggested" and b.get("archetype") == archetype
                and (b.get("aspect") or None) == aspect):
            return [s.get("name") if isinstance(s, dict) else s
                    for s in b.get("slot_order") or []][:6]
    return []


def overlap(build: list, target: list):
    return len(set(build) & set(target)) / len(target) if target else None


def aspect_rows(god: dict, note: dict, stored: dict, slugs_by_aspect: dict, names: dict,
                tiers: dict, items_by_name: dict) -> list:
    """One row per `shown` aspect of this god."""
    rows = []
    base = suggested(note, ARCHETYPE)
    pooled = community_target.split(validate._community_slots(note), items_by_name, god)
    pooled = list(pooled[community_target.SCORED])
    for entry in (note.get("community_aspects") or {}).get("aspects") or []:
        if entry.get("status") != "shown":
            continue
        slug = slugs_by_aspect.get(entry["aspect"])
        records = [r for w in entry.get("windows") or [] for r in stored.get(w, [])
                   if r.get("aspect") == slug]
        target = aspect_target(records, names, tiers)
        if len(target) < TARGET_SIZE or len(base) < 6:
            continue
        own = suggested(note, ARCHETYPE, entry["aspect"])
        rows.append({
            "god": god["name"], "aspect": entry["aspect"], "matches": len(records),
            "role_shift": bool(entry.get("role_shift")),
            "played": (entry.get("role_shift") or {}).get("role") or entry.get("base_role"),
            "ships_aspect_build": bool(own), "target": target,
            "shown": overlap(own or base, target),
            "base": overlap(base, target),
            "base_vs_pooled": overlap(base, pooled),
        })
    return rows


def compute(root: Path = am.STORE_ROOT) -> list:
    items, gods = recommend.load_items(), recommend.load_gods()
    items_by_name = {it["name"]: it for it in items}
    tiers = {it["name"]: it.get("tier") for it in items}
    names = am.item_name_lookup()
    meta = am.load_meta(root)
    rows = []
    for g in gods:
        slug = am.god_slug(g["name"])
        note = recommend.load_build_note(g["name"])
        by_name = {a["name"]: a["value"] for a in (meta.get("aspects") or {}).get(slug) or []}
        rows += aspect_rows(g, note, am.load_god(root, slug), by_name, names, tiers, items_by_name)
    return rows


def _mean(rows, key):
    vals = [r[key] for r in rows if r[key] is not None]
    return statistics.fmean(vals) if vals else None


def _pct(x):
    return "n/a" if x is None else f"{x:.0%}"


def summary(rows: list) -> list:
    """`(label, rows)` groups, in report order."""
    return [("every shown aspect", rows),
            ("played in another role", [r for r in rows if r["role_shift"]]),
            ("played in the base role", [r for r in rows if not r["role_shift"]]),
            ("ships its own aspect build", [r for r in rows if r["ships_aspect_build"]]),
            ("toggle falls back to the base build", [r for r in rows if not r["ships_aspect_build"]])]


def report_lines(rows: list) -> list:
    L = ["# Aspect agreement: the toggle's build against what aspect players hold", "",
         "Generated by `python -m smite.aspect_agreement`. A diagnostic that feeds nothing; the "
         "figure and its limits are in the module docstring. Agreement, not quality.", "",
         "| group | aspects | toggle's build vs aspect players' six | base `core` vs the same six "
         "| base `core` vs the god's pooled target | sharing no item |",
         "|---|---|---|---|---|---|"]
    for label, group in summary(rows):
        L.append(f"| {label} | {len(group)} | {_pct(_mean(group, 'shown'))} | {_pct(_mean(group, 'base'))} "
                 f"| {_pct(_mean(group, 'base_vs_pooled'))} | {sum(1 for r in group if r['shown'] == 0)} |")
    L += ["", "| god | aspect | matches | played | own build | toggle | base | aspect players' six |",
          "|---|---|---|---|---|---|---|---|"]
    for r in sorted(rows, key=lambda r: (r["shown"], r["god"])):
        L.append(f"| {r['god']} | {r['aspect']} | {r['matches']} | {r['played'] or ''}"
                 f"{' (shift)' if r['role_shift'] else ''} | {'yes' if r['ships_aspect_build'] else ''} "
                 f"| {_pct(r['shown'])} | {_pct(r['base'])} | {' · '.join(r['target'])} |")
    return L


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out", type=Path, default=REPORT_PATH)
    args = ap.parse_args(argv)
    rows = compute()
    args.out.write_text("\n".join(report_lines(rows)) + "\n", encoding="utf-8")
    for label, group in summary(rows):
        print(f"{label:<38} {len(group):>3}  toggle {_pct(_mean(group, 'shown')):>4}  "
              f"base {_pct(_mean(group, 'base')):>4}  pooled {_pct(_mean(group, 'base_vs_pooled')):>4}")
    print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
