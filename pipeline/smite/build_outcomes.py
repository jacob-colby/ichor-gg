"""Do matches that hold more of a build win more? Match outcomes against a
six, per god. A DIAGNOSTIC: it reads the match store and the shipped builds
and feeds nothing back.

    python -m smite.build_outcomes                 # newest window, base kit -> data/Analysis/_build_outcomes.md
    python -m smite.build_outcomes --windows all   # every stored window pooled
    python -m smite.build_outcomes --kit any       # aspect matches too

WHY THIS EXISTS (2026-11-11, docs/accuracy-levers-2026-11-11.md). Every other
instrument here grades a build against what the community BUILDS (`validate`,
`calibrate`) or against arithmetic with no movement, crowd control or allies in
it (`build_quality`, `side_by_side`). STATE.md section 2 says what that leaves
out: neither can say a build is BETTER, only more conventional or stronger in a
duel. The match store (`aspect_matches`) holds the one thing those lack, the
team outcome of a match beside the six items held in it, and until this module
nothing read the two together.

THE QUESTION, AND THE STATISTIC. For one god and one reference six (Ichor's
`model` build, the shipped `core`, the community's cleaned six), every stored
match gets an OVERLAP: how many of its six held items are in the reference.
The figure reported is the WITHIN-GOD slope of win on overlap, pooled over
gods:

    slope = sum_g sum_m (k_gm - mean_g k)(w_gm - mean_g w) / sum_g sum_m (k_gm - mean_g k)^2

in win-rate points per shared item. Within-god, because gods differ in win
rate and in how conventional their builds are, and a pooled slope would read
that as an effect. The interval is a percentile bootstrap over GODS
(`BOOTSTRAP_RESAMPLES`, seeded): matches inside one god are not independent
(a thin god can be a few players, `aspect_matches`' Mangetsu count), so the
god is the unit resampled.

WHAT IS HELD FIXED, AND WHY.
  * FINISHED SIXES ONLY (`finished_six`): all six inventory slots hold a
    tier-3 item this repo knows. A match that ends at four items has a lower
    overlap ceiling and loses more often, which is game length, not the build.
    It is a partial control and the report prints its price: the matches kept
    win well above 50%, because winners finish builds.
  * BASE KIT ONLY by default: the builds compared are base-kit builds, and an
    aspect is a different kit (38 of 79 recorded aspects are played in another
    role, measured 2026-11-11).
  * THE NEWEST WINDOW by default: the builds are today's, on today's items.
  * A god needs `MIN_GOD_MATCHES` kept matches (the tier list's floor) or it
    is left out and counted.
Both role readings are printed: every role the god was played in, and the
god's primary role alone (`build_quality.primary_role`).

THE CONTROL (`random_reference`). A random six from the god's own legal pool
(`scoring.is_buildable` and the damage filter, tier 3) gets the same statistic,
averaged over `RANDOM_DRAWS` seeded draws. It is what a reference with no
knowledge of the god scores, so a row is read against it, not against zero.

WHAT IT CANNOT SAY, and the report repeats it:
  * It is observational. Players who build a given six differ from those who
    do not, in rank and in role, and nothing here adjusts for either.
  * `core` reads SmiteBrain's aggregate win rates, which are computed from
    these same matches. Only the `model` row is free of that leak.
  * The outcome is the TEAM's. One build is one of five.
  * Slots are the inventory at the end of the match, not a buy order, and a
    sold item is gone.
  * The feed holds 81-96% of the aggregate's matches (`aspect_matches`).

FEEDS NOTHING. `scoring`, `assemble`, `recommend`, `build_index` and
`efficiency` do not import this module, and a test holds that. A slope that
became a fit signal would be register section 4.4's "different experiment".

TWO READINGS, AND THE SECOND CORRECTS THE FIRST (2026-11-11, fingerprint
89eb181b72f1).

Before the census the store held 40,616 matches over OB44-OB47, 94% of them
aspect players, because the no-aspect feed was a ten-match sample per run.
Pooled over all four windows and both kits, 9,486 finished sixes on 66 gods:
`model` +1.38pp per shared item (95% interval +0.14 to +2.64), `core` +1.50
(+0.41 to +2.57), the community's own six +0.77 (-0.18 to +1.64).

On the census (OB47, base kit; 28,676 base-kit matches, of which 6,603 hold a
finished six, winning 62%):

    reference      every role, 71 gods          primary role, 59 gods
                   6,603 matches                5,360 matches
    model          +0.71pp  (-0.79 to +2.17)    +0.44pp  (-1.37 to +2.23)
    core           +1.96pp  (+0.69 to +3.30)    +2.53pp  (+0.83 to +4.32)
    community      +1.39pp  (+0.55 to +2.29)    +2.82pp  (+1.73 to +4.06)
    random six     -0.03pp  (sd 1.59)           +0.19pp  (sd 1.87)

READ IT THIS WAY. On the kit the builds are made for, the `model` build does
NOT separate from zero, and the first reading's +1.38pp was the wrong sample
(aspect players, four patches). The community's own six does separate, most
clearly in the god's primary role, and so does `core`, which reads the
community's win and pick. So the instrument can see a build that carries
outcome information, and it does not see one in efficiency and fit alone.
That is the same sentence STATE.md section 2 already says about ranking, now
from outcomes instead of agreement. It is also a statement about resolution:
a random six scatters by 1.6 to 1.9pp, so an effect under about 2pp per item
is not visible on one patch's finished sixes, and `model` at +0.4 to +0.7
could be that or nothing.

HELD OUT IN TIME, the reading that removes `core`'s leak: cores rebuilt from
the community record as committed on 2026-11-06 (d1c6f091) and scored on the
3,909 finished-six base-kit matches played after it (57 gods): +0.99pp (-0.64
to +2.54). Not separable either. A build made from three days of a patch
does not measurably predict the next five.
"""
import argparse
import random
import statistics
import sys
from pathlib import Path

from smite import aspect_matches as am
from smite import build_quality as bq
from smite import community_target, recommend, scoring, tierlist

REPO_ROOT = Path(__file__).resolve().parents[2]
REPORT_PATH = REPO_ROOT / "data" / "Analysis" / "_build_outcomes.md"

#: The reference builds, in report order. `community` is the cleaned six
#: (`community_target.comparison_six`), the same six `side_by_side` compares.
REFERENCES = ("model", "core", "community")
MIN_GOD_MATCHES = tierlist.MIN_MATCHES
BOOTSTRAP_RESAMPLES = 2000
RANDOM_DRAWS = 200
SEED = 20261111
FINISHED_TIER = "3"

#: Feed spellings the item notes do not carry. The per-match feed names
#: "Brawler's Ruin" (no link, so `aspect_matches._item_slug` slugs the name)
#: where SmiteBrain's own item index and the wiki name Brawler's Beat Stick.
#: Measured 2026-11-11 on the committed store: `brawlers-ruin` 3,678 times and
#: `brawlers-beat-stick` never, while the index lists Brawler's Beat Stick
#: (2,062 matches in OB47) and no Brawler's Ruin. One item, two spellings.
SLUG_ALIASES = {"brawlers-ruin": "brawlers-beat-stick"}


def slug_names(items_root: Path = am.ITEMS_ROOT) -> dict:
    """Feed slug -> our item name, `SLUG_ALIASES` applied."""
    names = am.item_name_lookup(items_root)
    for alias, target in SLUG_ALIASES.items():
        if target in names:
            names[alias] = names[target]
    return names


def finished_six(record: dict, names: dict, tiers: dict):
    """The six held items by our names, or None unless slots one to six all
    hold a tier-3 item this repo knows."""
    held = []
    for slug in (record.get("items") or [])[:6]:
        name = names.get(slug) if slug else None
        if name is None or str(tiers.get(name)) != FINISHED_TIER:
            return None
        held.append(name)
    return held if len(held) == 6 else None


def reference_six(god: dict, note: dict, which: str, items_by_name: dict) -> list:
    """One reference build for one god, or [] when there is no full six."""
    if which == "community":
        entry = next((b for b in note.get("builds") or [] if b.get("source") == "community"), None)
        six = community_target.comparison_six(entry.get("slot_order"), items_by_name, god)[0] \
            if entry else []
    else:
        six = bq.suggested_core(note, which)[:6]
    return six if len(six) == 6 and all(n in items_by_name for n in six) else []


def legal_pool(god: dict, items: list, weights: dict) -> list:
    """Tier-3 items the recommender could put in this god's build."""
    return sorted(it["name"] for it in items
                  if str(it.get("tier")) == FINISHED_TIER and scoring.is_buildable(it, god)
                  and scoring.passes_damage_filter(it, god, weights))


def god_rows(records: list, names: dict, tiers: dict, primary_role: str,
             kit: str = "base", role: str = "any") -> list:
    """`(held six, won)` for the matches that pass the filters."""
    out = []
    for r in records:
        if kit == "base" and r.get("aspect"):
            continue
        if role == "primary" and r.get("role") != primary_role:
            continue
        if r.get("placement") not in (1, 2):
            continue
        held = finished_six(r, names, tiers)
        if held is not None:
            out.append((frozenset(held), 1 if r["placement"] == 1 else 0))
    return out


def moments(rows: list, reference) -> tuple:
    """`(sum of cross products, sum of squares)` of overlap against win,
    centred on this god's own means."""
    ks = [len(held & reference) for held, _ in rows]
    ws = [won for _, won in rows]
    mk, mw = statistics.fmean(ks), statistics.fmean(ws)
    return (sum((k - mk) * (w - mw) for k, w in zip(ks, ws)),
            sum((k - mk) ** 2 for k in ks))


def pooled_slope(parts: list) -> float:
    den = sum(b for _, b in parts)
    return sum(a for a, _ in parts) / den if den else 0.0


def slope_with_interval(parts: list, resamples: int = BOOTSTRAP_RESAMPLES, seed: int = SEED):
    """`(slope, low, high)`: the pooled within-god slope and a 95% percentile
    bootstrap over gods. `(0.0, None, None)` with fewer than two gods."""
    if len(parts) < 2:
        return pooled_slope(parts), None, None
    rng = random.Random(seed)
    draws = sorted(pooled_slope(rng.choices(parts, k=len(parts))) for _ in range(resamples))
    return pooled_slope(parts), draws[int(0.025 * resamples)], draws[int(0.975 * resamples) - 1]


def random_reference(rows_by_god: dict, pools: dict, draws: int = RANDOM_DRAWS, seed: int = SEED):
    """`(mean, sd)` of the pooled slope when every god's reference is a random
    six from its own legal pool."""
    rng = random.Random(seed)
    slopes = []
    for _ in range(draws):
        parts = [moments(rows, frozenset(rng.sample(pools[g], 6)))
                 for g, rows in rows_by_god.items() if len(pools[g]) >= 6]
        slopes.append(pooled_slope(parts))
    return statistics.fmean(slopes), (statistics.pstdev(slopes) if len(slopes) > 1 else 0.0)


def load_inputs():
    items, gods = recommend.load_items(), recommend.load_gods()
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    notes_by_god = {g["name"]: recommend.load_build_note(g["name"]) for g in gods}
    return items, gods, weights, notes_by_god


def compute(items, gods, weights, notes_by_god, root: Path = am.STORE_ROOT, windows="newest",
            kit: str = "base", role: str = "any", names: dict = None) -> dict:
    """Everything one table of the report needs, for one filter setting."""
    items_by_name = {it["name"]: it for it in items}
    tiers = {it["name"]: it.get("tier") for it in items}
    names = names if names is not None else slug_names()
    meta = am.load_meta(root)
    ordered = am.ordered_windows(meta)
    read = ordered[:1] if windows == "newest" else ordered
    rows_by_god, pools, thin, kept_total = {}, {}, [], 0
    for g in gods:
        stored = am.load_god(root, am.god_slug(g["name"]))
        records = [r for w in read for r in stored.get(w, [])]
        rows = god_rows(records, names, tiers, bq.primary_role(g), kit, role)
        if len(rows) < MIN_GOD_MATCHES:
            thin.append(g["name"])
            continue
        rows_by_god[g["name"]] = rows
        pools[g["name"]] = legal_pool(g, items, weights)
        kept_total += len(rows)
    by_god = {g["name"]: g for g in gods}
    table = {}
    for which in REFERENCES:
        parts, by_overlap, n = [], {}, 0
        for name, rows in rows_by_god.items():
            ref = reference_six(by_god[name], notes_by_god[name], which, items_by_name)
            if not ref:
                continue
            ref = frozenset(ref)
            parts.append(moments(rows, ref))
            n += len(rows)
            for held, won in rows:
                cell = by_overlap.setdefault(len(held & ref), [0, 0])
                cell[0] += won
                cell[1] += 1
        slope, low, high = slope_with_interval(parts)
        table[which] = {"slope": slope, "low": low, "high": high, "gods": len(parts), "matches": n,
                        "by_overlap": {k: (v[0] / v[1], v[1]) for k, v in sorted(by_overlap.items())}}
    rand_mean, rand_sd = random_reference(rows_by_god, pools) if rows_by_god else (0.0, 0.0)
    wins = sum(won for rows in rows_by_god.values() for _, won in rows)
    return {"windows": read, "kit": kit, "role": role, "table": table,
            "random": {"mean": rand_mean, "sd": rand_sd},
            "gods": len(rows_by_god), "thin": thin, "matches": kept_total,
            "win_rate": wins / kept_total if kept_total else None}


def _pp(x):
    return "n/a" if x is None else f"{x * 100:+.2f}pp"


def table_lines(result: dict) -> list:
    r = result
    head = (f"**Windows {', '.join(r['windows']) or 'none'} · kit {r['kit']} · role {r['role']}.** "
            f"{r['matches']:,} finished-six matches on {r['gods']} gods "
            f"({len(r['thin'])} gods under {MIN_GOD_MATCHES} and left out)")
    if r["win_rate"] is not None:
        head += f"; the matches kept win {r['win_rate']:.1%}."
    lines = [head, "",
             "| reference six | win rate per shared item | 95% interval | gods | matches | win rate by overlap (n) |",
             "|---|---|---|---|---|---|"]
    for which in REFERENCES:
        t = r["table"][which]
        cells = ", ".join(f"{k}: {wr:.0%} ({n})" for k, (wr, n) in t["by_overlap"].items())
        lines.append(f"| `{which}` | {_pp(t['slope'])} | {_pp(t['low'])} to {_pp(t['high'])} "
                     f"| {t['gods']} | {t['matches']:,} | {cells} |")
    lines.append(f"| a random legal six ({RANDOM_DRAWS} draws) | {_pp(r['random']['mean'])} "
                 f"| sd {r['random']['sd'] * 100:.2f}pp | {r['gods']} | {r['matches']:,} | |")
    return lines + [""]


def report_lines(results: list) -> list:
    lines = ["# Build outcomes: do matches that hold more of a build win more?", "",
             "Generated by `python -m smite.build_outcomes`. A diagnostic that feeds nothing. "
             "The statistic, the filters and what it cannot say are in the module docstring; "
             "the short form:", "",
             "- Observational: who builds a six is not random, and nothing here adjusts for rank or role.",
             "- `core` reads win rates computed from these same matches. Only `model` is free of that.",
             "- Finished sixes only, so the matches kept win more than half the time.",
             "- Read each row against the random-six row, not against zero.", ""]
    for r in results:
        lines += table_lines(r)
    return lines


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--windows", choices=("newest", "all"), default="newest")
    ap.add_argument("--kit", choices=("base", "any"), default="base")
    ap.add_argument("--out", type=Path, default=REPORT_PATH)
    args = ap.parse_args(argv)
    inputs = load_inputs()
    results = [compute(*inputs, windows=args.windows, kit=args.kit, role=role)
               for role in ("any", "primary")]
    args.out.write_text("\n".join(report_lines(results)) + "\n", encoding="utf-8")
    for r in results:
        print(f"[role {r['role']}] {r['matches']:,} matches, {r['gods']} gods")
        for which in REFERENCES:
            t = r["table"][which]
            print(f"  {which:<10} {_pp(t['slope'])}  [{_pp(t['low'])}, {_pp(t['high'])}]")
        print(f"  {'random':<10} {_pp(r['random']['mean'])}  sd {r['random']['sd'] * 100:.2f}pp")
    print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
