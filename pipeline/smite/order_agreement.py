"""Does our buy ORDER contradict the order the community plays?

THE MEASUREMENT THAT SHIPS WITH `build_order`'s POSITIONAL SIGNAL, AND IT IS A
CLAIM ABOUT AGREEMENT WITH OBSERVED PLAY, NEVER ABOUT OUTCOMES. Nothing in this
repo can say a buy order is good. `calibrate` measures MEMBERSHIP overlap with
the community core and is blind to order — reordering the same six items moves
it exactly 0.0pp. `build_quality` points `combat.py` at a finished six-item
build at level 20 and is equally blind: the same six items at level 20 are the
same numbers whatever sequence bought them. So the usual bar in this repo,
"sweep it and beat control on both leakage-free splits", cannot be met by any
ordering change at all, and a report that implied otherwise would be lying
about which question it answered.

What IS checkable without a quality metric is contradiction. An item this
god's players buy first and we place sixth is a disagreement you can count,
item by item, and it needs no opinion about whether either order wins games.

TWO READINGS, AND THE SECOND IS THE HEADLINE.

  * DISPLACEMENT — |our slot - the community's centroid| for each item we both
    build. Easy to read and it has a confound: our core and theirs share only
    3-4 of 6 items, so our fourth purchase and their fourth slot are not
    strictly the same clock.
  * INVERSIONS — over pairs of items we BOTH build whose community centroids
    differ by at least a slot, how often do we order the pair backwards? This
    is order and nothing else. It cannot be moved by membership, so it is the
    number to quote.

THE AFTER-COUNT IS NOT EVIDENCE FOR THE CHANGE. `build_order` now reads the
same `slot_order` block this module scores it against, so an improvement in
the headline count is a description of the intervention and not a result.
docs/STATE.md section 1 is about exactly this shape of self-agreement.
`held_out` is the check that is not circular: fit the order on the slot PICKS
alone and score it against the ALTERNATES, which that ordering never read.
They are not independent samples — same scrape, same matches — so it is a weak
check and is labelled one. It is also the only one available.

JOUST AND ARENA HAVE NO RECORD AND ARE NOT SCORED AGAINST A BORROWED ONE
in the shipped model. They can be measured against Conquest's here, because
knowing the size of the gap is worth something, but every such row says
BORROWED on its own line: `recommend._build_entry_set` deliberately does not
feed those modes positional data, so a borrowed row is a description of the
heuristic and never a verdict on a build.

IT IS A DIAGNOSTIC. Nothing in `scoring`, `assemble`, `recommend`,
`build_index` or `efficiency` imports it, and a test pins that boundary.

    python -m smite.order_agreement                 # the report
    python -m smite.order_agreement --sweep         # community_weight 0 -> 1
    python -m smite.order_agreement --god Medusa    # one god, both orders
"""
import argparse
import copy
import itertools
import statistics
import sys
from pathlib import Path

from smite import assemble, notes, recommend, scoring

MODES = ("Conquest", "Joust", "Arena")
#: The two archetypes the god page leads with. `core` is the shipped blend,
#: `model` is the meta-free one; every other flavor is a variation on those.
ARCHETYPES = ("core", "model")
#: A pair of items has to disagree by at least this much community centroid
#: before ordering it either way counts as anything. Below a full slot the
#: community itself has not expressed a preference.
MIN_SEPARATION = 1.0
#: "Substantially earlier or later" for the displacement reading. Two slots of
#: six. Reported alongside 3 so the threshold's contribution stays visible.
DISPLACEMENT = 2.0
#: Confidence floor for the "strong" columns: both items reliably bought.
STRONG_MASS = 0.40

CAVEAT = (
    "Agreement with observed play, NOT a claim about outcomes - no instrument "
    "here can score a buy order (see this module's docstring). The headline "
    "count is scored against the same slot_order block build_order now reads, "
    "so read the held-out section for the part that is not circular."
)


# -- The build groups -------------------------------------------------------

def groups(modes=MODES):
    """`(god, mode, note)` for every build note, in a stable order."""
    for path in sorted(recommend.BUILDS_ROOT.glob("*.md")):
        fm, _ = notes.read_note(path)
        if not fm or fm.get("mode") not in modes:
            continue
        yield fm.get("god"), fm.get("mode"), fm


def core_of(note, archetype):
    """The six items of one suggested archetype for the base kit — a SET's
    worth of names, in whatever order the note happens to carry. Order is
    re-derived here rather than read, so the report is a function of the
    weights and not of when the notes were last regenerated."""
    for b in note.get("builds") or []:
        if (b.get("source") == "suggested" and b.get("archetype") == archetype
                and not b.get("aspect")):
            return [s if isinstance(s, str) else s.get("name")
                    for s in b.get("slot_order") or []]
    return []


def order_at(core, items_by_name, tags_map, weights, positions, strength):
    """`build_order` at one `community_weight`, without touching the file."""
    w = copy.deepcopy(weights)
    w.setdefault("build_order", {})["community_weight"] = strength
    return assemble.build_order(core, items_by_name, tags_map, w, positions)


# -- The two readings -------------------------------------------------------

def displacements(order, positions):
    """`[{item, ours, community, mass, d}]` for every item we both build."""
    rows = []
    for index, name in enumerate(order, start=1):
        if name not in positions:
            continue
        centroid, mass = positions[name]
        rows.append({"item": name, "ours": index, "community": centroid,
                     "mass": mass, "d": index - centroid})
    return rows


def inversions(order, positions):
    """`(inverted, orderable, strong_inverted, strong_orderable, pairs)`.

    A pair is ORDERABLE when both items are ones we build, both appear in the
    community record, and their centroids are at least `MIN_SEPARATION` apart —
    i.e. the community has actually expressed a preference between them. It is
    INVERTED when we buy the one they buy later first.

    Immune to membership by construction: every item counted is in our build
    and in theirs, so nothing here moves when the core changes."""
    rank = {name: i for i, name in enumerate(order, start=1)}
    rows = [(n, *positions[n]) for n in order if n in positions]
    inverted = orderable = strong_inverted = strong_orderable = 0
    pairs = []
    for (an, ac, am), (bn, bc, bm) in itertools.combinations(rows, 2):
        if abs(ac - bc) < MIN_SEPARATION:
            continue
        early, late = ((an, am), (bn, bm)) if ac < bc else ((bn, bm), (an, am))
        bad = rank[early[0]] > rank[late[0]]
        orderable += 1
        inverted += bad
        if min(early[1], late[1]) >= STRONG_MASS:
            strong_orderable += 1
            strong_inverted += bad
        if bad:
            pairs.append((early[0], late[0]))
    return inverted, orderable, strong_inverted, strong_orderable, pairs


# -- Rolling it up ----------------------------------------------------------

def score(archetype, mode, strength, items_by_name, tags_map, weights,
          fit_kwargs=None, test_kwargs=None, borrow=False):
    """One (archetype, mode) at one strength.

    `fit_kwargs` / `test_kwargs` are `scoring.slot_positions` options: the
    record the ORDER is built from and the record it is SCORED against. Equal
    by default, which is the in-sample reading; `held_out` makes them
    disjoint. `borrow` reads Conquest's record for a mode that has none. It
    scores against that record and orders WITHOUT it, because that is what
    ships: `recommend._build_entry_set` passes those modes no positional data
    at all. So a borrowed row is flat across strengths by construction — it
    sizes the gap the heuristic still carries there, and a borrowed row that
    MOVED would be describing a build the site does not produce. Every caller
    that sets it must say BORROWED in the output."""
    fit_kwargs = fit_kwargs or {}
    test_kwargs = test_kwargs if test_kwargs is not None else dict(fit_kwargs)
    agg = {"shared": 0, "d2": 0, "d3": 0, "inv": 0, "orderable": 0,
           "strong_inv": 0, "strong_orderable": 0, "gods_any": set(),
           "gods": set(), "worst": [], "inverted_pairs": []}
    for god, _mode, note in groups((mode,)):
        core = core_of(note, archetype)
        if len(core) < 2:
            continue
        source = recommend.load_build_note(god, "Conquest") if borrow else note
        fit = scoring.slot_positions(source, weights, **fit_kwargs)
        test = scoring.slot_positions(source, weights, **test_kwargs)
        order = order_at(core, items_by_name, tags_map, weights,
                         {} if borrow else fit, strength)
        rows = displacements(order, test)
        agg["shared"] += len(rows)
        agg["d2"] += sum(1 for r in rows if abs(r["d"]) >= DISPLACEMENT)
        agg["d3"] += sum(1 for r in rows if abs(r["d"]) >= 3)
        if rows:
            agg["gods_any"].add(god)
        for r in rows:
            if abs(r["d"]) >= DISPLACEMENT:
                agg["gods"].add(god)
            if r["mass"] >= STRONG_MASS:
                agg["worst"].append({"god": god, **r})
        inv, orderable, sinv, sord, pairs = inversions(order, test)
        agg["inv"] += inv
        agg["orderable"] += orderable
        agg["strong_inv"] += sinv
        agg["strong_orderable"] += sord
        agg["inverted_pairs"] += pairs
    return agg


def _pct(n, d):
    return f"{100 * n / d:.1f}%" if d else "n/a"


def table_lines(items_by_name, tags_map, weights, strengths):
    """The before/after table: every (archetype, mode) at each strength."""
    shipped = (weights.get("build_order") or {}).get("community_weight", 0.0)
    lines = ["## Contradiction count, per mode",
             "",
             f"`community_weight` ships at {shipped}. Joust and Arena are SCORED against "
             "CONQUEST's record because they have none of their own, and ORDERED without it, "
             "because that is what ships (`recommend._build_entry_set`). Those rows are flat "
             "across strengths on purpose: they size the gap the heuristic still carries in "
             "180 of the 270 build groups, and are not a verdict on a build.",
             "",
             "| archetype | mode | weight | orderable pairs | inverted | strong | "
             "shared items | disp>=2 | disp>=3 | gods with >=1 |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for archetype in ARCHETYPES:
        for mode in MODES:
            borrow = mode != "Conquest"
            for strength in strengths:
                a = score(archetype, mode, strength, items_by_name, tags_map, weights,
                          borrow=borrow)
                label = f"{mode} (BORROWED)" if borrow else mode
                lines.append(
                    f"| {archetype} | {label} | {strength:.2f} | {a['orderable']} | "
                    f"{a['inv']} ({_pct(a['inv'], a['orderable'])}) | "
                    f"{a['strong_inv']}/{a['strong_orderable']} | {a['shared']} | "
                    f"{a['d2']} ({_pct(a['d2'], a['shared'])}) | "
                    f"{a['d3']} ({_pct(a['d3'], a['shared'])}) | "
                    f"{len(a['gods'])} of {len(a['gods_any'])} |")
    return lines


def held_out(items_by_name, tags_map, weights, strengths, archetype="core"):
    """The one non-circular reading available.

    Order the core using ONLY the community's top pick at each slot, then score
    it against ONLY the alternates — sightings the ordering never read. Same
    scrape and same matches, so the two halves are not independent and this is
    a weak check; it is the only one there is. Conquest alone: it is the only
    mode with a record, and a borrowed one would score a heuristic against
    somebody else's data twice over."""
    fit = {"include_alternates": False}
    test = {"include_picks": False}
    return [(strength,
             score(archetype, "Conquest", strength, items_by_name, tags_map, weights,
                   fit_kwargs=fit, test_kwargs=test))
            for strength in strengths]


def held_out_lines(results):
    lines = ["## Held out: ordered on slot picks, scored on the alternates",
             "",
             "The only reading here that is not scored against its own input. Weak — the "
             "two halves come from one scrape of one set of matches — and reported as the "
             "check that exists rather than the check one would want.",
             "",
             "| weight | orderable pairs | inverted | strong |", "|---|---|---|---|"]
    for strength, a in results:
        lines.append(f"| {strength:.2f} | {a['orderable']} | "
                     f"{a['inv']} ({_pct(a['inv'], a['orderable'])}) | "
                     f"{a['strong_inv']}/{a['strong_orderable']} |")
    return lines


def offender_lines(items_by_name, tags_map, weights, archetype="core", limit=10):
    """Worst displacements and most repeated inversions at `community_weight`
    0 — the problem as it stood, by name. Fixed at 0 on purpose: this section
    is the diagnosis, and quoting it at the shipped strength would report the
    residue instead."""
    a = score(archetype, "Conquest", 0.0, items_by_name, tags_map, weights)
    worst = sorted(a["worst"], key=lambda r: -abs(r["d"]))[:limit]
    counts = {}
    for pair in a["inverted_pairs"]:
        counts[pair] = counts.get(pair, 0) + 1
    lines = [f"## Where it came from ({archetype}, Conquest, weight 0.00)",
             "",
             f"Worst displacements, community mass >= {STRONG_MASS:.2f}:",
             "",
             "| god | item | ours | community | mass | displacement |",
             "|---|---|---|---|---|---|"]
    for r in worst:
        lines.append(f"| {r['god']} | {r['item']} | {r['ours']} | {r['community']:.2f} | "
                     f"{r['mass']:.2f} | {r['d']:+.2f} |")
    lines += ["", "Most repeated inversions (the community buys the first before the "
                  "second; we did the reverse):", ""]
    for (early, late), n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:limit]:
        lines.append(f"* {n}x  {early}  before  {late}")
    return lines


def coverage_lines(weights):
    """How much of each build the record can speak to at all. A buy order whose
    positions are 3-of-6 evidence and 3-of-6 tags-and-cost should say so."""
    counts = []
    for _god, _mode, note in groups(("Conquest",)):
        core = core_of(note, "core")
        if not core:
            continue
        pos = scoring.slot_positions(note, weights)
        counts.append(sum(1 for n in core if n in pos))
    if not counts:
        return []
    hist = {k: counts.count(k) for k in range(0, 7)}
    return ["## How much of a build the record can place", "",
            f"Conquest, `core`, {len(counts)} gods. Items per six-item build carrying a "
            "community position:", "",
            "| positions from the record | gods |", "|---|---|"] + \
           [f"| {k} of 6 | {v} |" for k, v in sorted(hist.items()) if v] + \
           ["", f"Mean {statistics.mean(counts):.2f} of 6. The rest keep the heuristic, and "
            "`community_ordered` on each build names which is which.",
            "", "Joust and Arena: 0 of 6 on every god, by decision — see "
            "`recommend._build_entry_set`."]


def god_lines(god_name, items_by_name, tags_map, weights, archetype="core"):
    note = recommend.load_build_note(god_name, "Conquest")
    core = core_of(note, archetype)
    if not core:
        return [f"{god_name}: no {archetype} build in Conquest"]
    pos = scoring.slot_positions(note, weights)
    shipped = (weights.get("build_order") or {}).get("community_weight", 0.0)
    before = order_at(core, items_by_name, tags_map, weights, pos, 0.0)
    after = order_at(core, items_by_name, tags_map, weights, pos, shipped)
    lines = [f"## {god_name} — {archetype}, Conquest", "",
             "| # | heuristic only | shipped | community centroid | mass |",
             "|---|---|---|---|---|"]
    for i, name in enumerate(after):
        centroid, mass = pos.get(name, (None, 0.0))
        c = f"{centroid:.2f}" if centroid is not None else "— no record"
        lines.append(f"| {i + 1} | {before[i]} | {name} | {c} | {mass:.2f} |")
    return lines


# -- Output -----------------------------------------------------------------

def emit(lines, out=None):
    """Every path out prints the caveat first. `build_quality` does the same
    thing for the same reason: the number is not the finding, the number under
    its caveat is."""
    body = "\n".join([f"> {CAVEAT}", ""] + list(lines)) + "\n"
    if out:
        out.write_text(body, encoding="utf-8")
        return out
    print(body)
    return None


def build_parser():
    ap = argparse.ArgumentParser(description="Buy-order agreement with the community record")
    ap.add_argument("--god", help="one god, both orders side by side")
    ap.add_argument("--archetype", default="core", help="core (default) or model")
    ap.add_argument("--sweep", action="store_true",
                    help="community_weight 0.00 -> 1.00 instead of 0.00 and shipped")
    ap.add_argument("--out", help="write the report to this path instead of stdout")
    return ap


def main(argv=None):
    args = build_parser().parse_args(argv)
    items = recommend.load_items()
    items_by_name = {it["name"]: it for it in items}
    tags_map = scoring.load_tags(recommend.TAGS_PATH)
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    shipped = (weights.get("build_order") or {}).get("community_weight", 0.0)

    if args.god:
        emit(god_lines(args.god, items_by_name, tags_map, weights, args.archetype))
        return 0

    strengths = ([0.0, 0.25, 0.50, 0.75, 1.0] if args.sweep else sorted({0.0, shipped}))
    lines = table_lines(items_by_name, tags_map, weights, strengths)
    lines += [""] + held_out_lines(held_out(items_by_name, tags_map, weights, strengths))
    lines += [""] + coverage_lines(weights)
    lines += [""] + offender_lines(items_by_name, tags_map, weights)
    emit(lines, Path(args.out) if args.out else None)
    return 0


if __name__ == "__main__":
    sys.exit(main())
