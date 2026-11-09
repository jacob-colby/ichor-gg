"""CLI: score SMITE 2 items and (later phases) assemble suggested builds.
Runs offline over local notes — no network. Run after refresh.py.

Phase A: `python -m smite.recommend --efficiency-report` writes a god-agnostic
item efficiency table.
"""
import argparse
import sys
from pathlib import Path

from smite import assemble, hybrid, efficiency, notes, scoring

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_ROOT = REPO_ROOT / "data"
WEIGHTS_PATH = DATA_ROOT / "_weights.yaml"
TAGS_PATH = DATA_ROOT / "_tags.yaml"
BUILDS_ROOT = REPO_ROOT / "data" / "builds"

MODES = ["Conquest", "Joust", "Arena"]

_FLAVOR_BLURB = {
    "core": "Top weighted-score core",
    "model": "The model's own answer — no meta signal",
    "hybrid": "The model's core, corrected where the community is clearly right",
    "crit": "Crit / auto-attack skew",
    "burst": "Ability / burst skew",
    "bruiser": "Lifesteal bruiser skew",
    "anti-tank": "Full-penetration anti-tank skew",
    "attack-speed": "Basic-attack DPS skew",
    "cooldown": "Ability-uptime skew — Cooldown Rate is a rate, not a reduction",
    "strength": "Off-type Strength build — this kit scales on it",
    "intelligence": "Off-type Intelligence build — this kit scales on it",
    "str-int": "Hybrid Strength + Intelligence — this kit scales on both",
}


def _rationale(archetype, rows, profile):
    if profile.get("fun"):
        return (f"For fun — deliberately fights this god's kit "
                f"({_FLAVOR_BLURB.get(archetype, archetype)}). "
                "Scored on gold-value + flavor fit only; not meta-checked.")
    meta = "" if profile.get("suppress_underrated") else " + win/pick"
    text = f"{_FLAVOR_BLURB.get(archetype, archetype)} (efficiency + fit{meta})."
    if profile.get("label"):
        text += f" {profile['label']}."
    if not profile.get("suppress_underrated"):
        underrated = [r["item"] for r in rows if r.get("underrated")]
        if underrated:
            text += " Underrated for this god: " + ", ".join(underrated) + "."
    return text


def note_paths(directory):
    """`*.md` under `directory` in BYTE order of the file name, the same on
    every platform.

    `sorted()` on the paths themselves is not: `WindowsPath` compares
    case-insensitively and `PosixPath` does not, so on Windows "Shield of the
    Phoenix" sorted before "Shield Splitter" and on the Linux runner after it.
    The item pool's order is the summation order of the gold fit, so the two
    platforms' outputs differed in the last ulp, and that was enough to flip a
    2dp `fit` on 10 committed notes and reorder `index.json` (measured
    2026-11-08 by recomputing an untouched main on Windows). On Linux this is
    exactly the order it always produced."""
    return sorted(Path(directory).glob("*.md"), key=lambda p: p.name)


def load_items():
    items_dir = DATA_ROOT / "Items"
    out = []
    for path in note_paths(items_dir):
        frontmatter, _ = notes.read_note(path)
        if frontmatter.get("name"):
            out.append(frontmatter)
    return out


def efficiency_report(items):
    scores, _gold = efficiency.efficiency_scores(items)
    ranked = sorted([it for it in items if it["name"] in scores],
                    key=lambda it: -scores[it["name"]]["score"])
    lines = ["# Item efficiency\n", "| Item | Cost | Tier | Residual | Score |", "|---|---|---|---|---|"]
    for it in ranked:
        s = scores[it["name"]]
        lines.append(f"| {it['name']} | {it['cost']} | {s['tier']} | {s['residual']:+.0f} | {s['score']:.2f} |")
    return "\n".join(lines) + "\n"


def load_gods():
    out = []
    for path in note_paths(DATA_ROOT / "Gods"):
        fm, _ = notes.read_note(path)
        if fm.get("name"):
            out.append(fm)
    return out


def load_build_note(god_name, mode="Conquest"):
    fm, _ = notes.read_note(BUILDS_ROOT / f"{god_name}-{mode}.md")
    return fm or {"builds": []}


def community_record(god, god_build, mode, weights):
    """`(community entry, borrowed_from)` for one god in one mode.

    The mode's own entry when it has one. Otherwise, if the mode declares
    `borrow_community`, the source mode's entry and that mode's name — Joust
    and Arena have no community data (SmiteBrain is ranked Conquest only), so
    both the Hybrid and the starter/relic pick read Conquest's and say so.
    `(None, None)` when there is nothing to read."""
    entry = next((b for b in (god_build or {}).get("builds", []) if b.get("source") == "community"),
                 None)
    borrow = ((weights.get("modes") or {}).get(mode.lower(), {}) or {}).get("borrow_community")
    if entry or not borrow:
        return entry, None
    source_mode = borrow.get("from", "Conquest")
    source = load_build_note(god["name"], source_mode)
    entry = next((b for b in (source or {}).get("builds", []) if b.get("source") == "community"),
                 None)
    return entry, (source_mode if entry else None)


def opening_choices(god, god_build, weights, mode, items_by_name):
    """`(starter, relic)` stamped on every build of one god in one mode — the
    community's most-picked starter path and base relic (`scoring.pick_starter`
    has the rule and its evidence), borrowed from Conquest where the mode has no
    record, and never an item the mode's shop lacks."""
    entry, borrowed_from = community_record(god, god_build, mode, weights)
    excluded = set(scoring.resolve_profile(weights, mode).get("excluded_items") or ())
    starter = scoring.pick_starter(god, weights, entry, items_by_name, excluded, borrowed_from)
    relic = scoring.pick_relic(entry, items_by_name, excluded, borrowed_from)
    return starter, relic


def _stamp_community_choices(path, starter, relic):
    """Set `starter` and `relic` on the community entry of a Build note, so the
    community build shows the same opening as the suggested ones. A `relic`
    left over from an earlier stamp is removed when there is none now."""
    fm, body = notes.read_note(path)
    if not fm:
        return
    changed = False
    for b in fm.get("builds", []):
        if b.get("source") != "community":
            continue
        for key, value in (("starter", starter), ("relic", relic)):
            if value and b.get(key) != value:
                b[key] = value
                changed = True
            elif not value and key in b:
                del b[key]
                changed = True
    if changed:
        notes.write_note(path, fm, body)


def god_report(god, items, god_build, weights, tags_map):
    eff_scores, _ = efficiency.efficiency_scores(items)
    rows = scoring.score_god_items(god, items, god_build, eff_scores, weights, tags_map)
    lines = [f"# {god['name']} — item scoring\n",
             "| Item | Total | Qual | Eff | Win | Pick | Fit | Tier | Tags | Flag |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        flag = "**UNDERRATED**" if r["underrated"] else ""
        tags = ", ".join(r["tags"])
        lines.append(f"| {r['item']} | {r['total']:.2f} | {r['quality']:.2f} | {r['efficiency']:.2f} | "
                     f"{r['win']:.2f} | {r['pick']:.2f} | {r['fit']:.2f} | {r['tier']} | "
                     f"{tags} | {flag} |")
    return "\n".join(lines) + "\n"


def _entry(archetype, core, rows, items_by_name, tags_map, weights, profile,
           flex_count, starter, aspect_name, fun=False, extra=None, positions=None,
           relic=None):
    """One suggested build entry from an already-assembled core.

    Extracted so every archetype is packaged identically — `model` differs from
    `core` only in how its rows were ranked, and that difference has to stay the
    only difference between them.

    `positions` is this build group's OWN community slot record (see
    `_build_entry_set`); it decides buy ORDER only and never membership, so
    `core` arrives already assembled and leaves with the same six items.
    """
    flex = assemble.flex_slots(core, rows, count=flex_count)
    ordered = assemble.build_order(core, items_by_name, tags_map, weights, positions)
    backed = assemble.community_ordered(ordered, positions, weights)
    swaps = assemble.situational_swaps(rows, items_by_name, tags_map, core=core)
    by_name = {r["item"]: r for r in rows}
    slot_scores = {
        name: {k: round(by_name[name][k], 2)
               for k in ("total", "efficiency", "win", "pick", "fit")}
        for name in ordered if name in by_name
    }
    return {
        "source": "suggested",
        "archetype": archetype,
        "slot_order": ordered,
        "flex_slots": flex,
        "situational_swaps": swaps,
        "rationale": _rationale(archetype, rows, profile),
        "slot_scores": slot_scores,
        # Which of the six got their position from the community record rather
        # than from tags and cost. Absent, never empty, when none did — the
        # page has to be able to tell "no evidence" from "not stamped yet".
        **({"community_ordered": backed} if backed else {}),
        **(extra or {}),
        **({"fun": True} if fun else {}),
        **({"starter": starter} if starter else {}),
        **({"relic": relic} if relic else {}),
        **({"aspect": aspect_name} if aspect_name else {}),
    }


def assemble_flavor_core(god, items, god_build, weights, tags_map, mode, eff_scores,
                         items_by_name, gold_values=None, flavor=None, aspect_overlay=None):
    """`(core, rows, profile)` for one flavor (None = the blended `core`) of
    one god in one mode — the one assembly `_build_entry_set` ships and
    `derive_team_shares` measures."""
    cfg = ((weights.get("flavors") or {}).get(flavor) or {}) if flavor else {}
    profile = scoring.resolve_profile(weights, mode, flavor, aspect_overlay=aspect_overlay)
    rows = scoring.score_god_items(god, items, god_build, eff_scores, weights, tags_map, profile)
    core, _ = assemble.assemble_core_converged(
        rows, items_by_name, passes=weights.get("conversion_passes", 1), n=6,
        max_lifesteal=scoring.god_max_lifesteal(god, weights, profile),
        require=cfg.get("require") if flavor else None,
        stat_caps=weights.get("stat_caps"),
        economy=profile.get("economy"),
        **assemble.coherence_args(items, weights),
        **assemble.conversion_args(weights, eff_scores, gold_values, signals=profile["signals"]),
        **assemble.overflow_args(weights, eff_scores, gold_values, signals=profile["signals"]))
    return core, rows, profile


def _build_entry_set(god, items, god_build, weights, tags_map, mode, eff_scores,
                     items_by_name, starter, flex_count, aspect_overlay, aspect_name,
                     gold_values=None, relic=None):
    entries = []
    core_rows = core_profile = None
    # Buy order reads THIS mode's own community record and nothing else.
    #
    # `god_build` is the note for `mode`, and Joust and Arena notes carry no
    # community entry at all, so this is `{}` for 180 of the 270 build groups
    # and `build_order` falls straight back to the heuristic there. That is a
    # decision and not an omission: the Hybrid may BORROW Conquest's record for
    # item CHOICE (`borrow_community`, and it says `borrowed_from` on the build
    # when it does), but a slot centroid is a claim about WHEN a power spike
    # lands, and both other modes deliberately zero `win` and `pick` on the
    # grounds that Conquest's rates describe a different game. Timing is more
    # mode-specific than choice, not less — Arena's gold spools from 0:00 at
    # 900g/min — so borrowing it would assert something no source here states.
    # The god page already discloses those two modes as "a shortlist rather
    # than a buy order"; this leaves that sentence true.
    positions = scoring.slot_positions(god_build, weights)
    eligible = scoring.eligible_flavors(god, weights, items)
    for flavor in [None] + eligible:
        cfg = ((weights.get("flavors") or {}).get(flavor) or {}) if flavor else {}
        if cfg.get("fun") and (aspect_overlay is not None
                               or cfg.get("redundant_with") in eligible):
            continue  # fun builds: base kit only, and never beside a serious twin
        core, rows, profile = assemble_flavor_core(god, items, god_build, weights, tags_map, mode,
                                                   eff_scores, items_by_name, gold_values,
                                                   flavor, aspect_overlay)
        archetype = flavor or "core"
        if flavor is None:
            core_rows, core_profile = rows, profile
        entries.append(_entry(archetype, core, rows, items_by_name, tags_map,
                              weights, profile, flex_count, starter, aspect_name,
                              fun=bool(cfg.get("fun")), positions=positions, relic=relic))

    # The model's own answer, with the meta switched off.
    #
    # `signal_score` already computes `quality` — efficiency and fit only,
    # renormalized — and every caller until now discarded it. Ranking by it
    # gives the build the model would pick if it had never seen a win rate,
    # which is the honest counterpart to the community's own build. The blended
    # `core` stays exactly as it was: the tier list's per-god score, the draft's
    # baseline and the data audit all read it by name.
    if core_rows is not None:
        max_ls = scoring.god_max_lifesteal(god, weights, core_profile)
        model_rows = sorted(core_rows, key=lambda r: (-r["quality"], r["item"]))
        model_core, _ = assemble.assemble_core_converged(
            model_rows, items_by_name, passes=weights.get("conversion_passes", 1), n=6,
            score_key="quality",
            max_lifesteal=max_ls,
            stat_caps=weights.get("stat_caps"),
            economy=core_profile.get("economy"),
            **assemble.coherence_args(items, weights),
            # `quality`'s own scale, not the blended total's: in Conquest
            # efficiency is 0.35 of `total` but 0.70 of `quality`.
            **assemble.conversion_args(weights, eff_scores, gold_values,
                                       signals=assemble.quality_signals(core_profile["signals"])),
            **assemble.overflow_args(weights, eff_scores, gold_values,
                                     signals=assemble.quality_signals(core_profile["signals"])))
        entries.append(_entry("model", model_core, model_rows, items_by_name,
                              tags_map, weights, core_profile, flex_count,
                              starter, aspect_name, positions=positions, relic=relic))

        # And the hybrid: that same core, corrected only where the model is
        # near-indifferent and the community's record is strong enough to
        # override it. `hybrid_core` returns the model core unchanged when
        # there is nothing to correct with — a duplicate build, so it isn't
        # emitted.
        # A mode with no community data of its own may BORROW another's. Joust
        # and Arena had none, so this build simply did not exist there — 89 of
        # 89 gods in each got the model core back and nothing was emitted.
        # Conquest's record is still the best evidence about an item; it is
        # just evidence about a different game, so the parts that do not
        # transfer are rejected by tag (see `borrow_community` in
        # _weights.yaml) and the result is labelled as borrowed rather than
        # passed off as this mode's own (`community_record`).
        community_entry, borrowed_from = community_record(god, god_build, mode, weights)
        borrow = ((weights.get("modes") or {}).get(mode.lower(), {}) or {}).get("borrow_community")
        reject_tags = (borrow.get("reject_tags") or []) if borrowed_from else []

        hy_core, swaps = hybrid.hybrid_core(model_core, model_rows, community_entry,
                                            items_by_name, weights, max_lifesteal=max_ls,
                                            reject_tags=reject_tags, tags_map=tags_map,
                                            borrowed_from=borrowed_from)
        if swaps:
            extra = {"swaps": swaps}
            if borrowed_from:
                extra["borrowed_from"] = borrowed_from
            entries.append(_entry("hybrid", hy_core, model_rows, items_by_name,
                                  tags_map, weights, core_profile, flex_count,
                                  starter, aspect_name, extra=extra,
                                  positions=positions, relic=relic))
    return entries


# ── Team-tag shares derived from their target (2026-11-04) ────────────────
#
# THE CLIFF. Joust's anti-heal share was a swept constant, and the number of
# `core` cores holding an anti-heal item was a cliff in it (2026-11-04 data,
# 101 cores, 0.01 steps): 19 at 0.56, 22, 25, then 34 at 0.59; 39 at 0.64,
# 44 at 0.65, 50 at 0.66. Nine cores flip between 0.58 and 0.59.
#
# WHY. A core takes its best anti-heal item once the tag bonus closes the
# score gap to the core's weakest item, and in Joust that gap has no
# god-specific term: `win` and `pick` are zeroed, so an item's score is
# efficiency (god-agnostic) plus fit, and fit is the ROLE's stat map plus a
# small kit blend. Every god of a role sees nearly the same gap. The nine at
# 0.59 are six Carries taking Toxic Blade (Toxic Blade 0.448-0.452 against
# their weakest kept item, Golden Blade, at 0.533-0.537) and three Solos
# taking Brawler's Beat Stick or Stygian Anchor; at 0.65-0.66 it is the
# Supports' turn with Stygian Anchor. No threshold or near-tie in assembly is
# involved — holding is monotone in the share for all 101 seats — the gaps
# themselves come in role-sized blocks, so ANY flat bonus moves the count a
# role at a time, and any change to role fit (the per-ability parse moved
# four gods into the Carry block) moves the calibrated point by a block.
#
# THE REDESIGN. The share is no longer a number anyone sets. The target is
# (1/N of cores, N = `team_size`, DOCUMENTED); each seat's COST is the least
# share at which its `core` holds the tag (bisection, `TEAM_SHARE_TOL`); the
# share is the cost of the round(seats/N)-th cheapest seat. Then exactly that
# many cores hold the tag — more only on an exact tie — on every refresh and
# after every model change, and the count moves with the TARGET one core per
# 1/seats. The block structure is still there (it is a fact about the
# scores) but it now decides only WHICH seats carry, by their own small
# differences, not HOW MANY. Derived by `python -m smite.recommend --all`
# into `data/_team_shares.json`, which `scoring.load_weights` reads, so every
# reader of the profile sees the same value as the builds; `test_mode_profiles`
# re-derives it and fails if the file is stale.
#
# Scope: `team_tags.derive` names the (mode, tag) pairs derived this way —
# Joust anti-heal. Arena anti-heal and both auras keep their swept shares
# (STATE.md §5).
TEAM_SHARES_PATH = DATA_ROOT / "_team_shares.json"
TEAM_SHARE_TOL = 1e-4


def _team_seats(gods, weights):
    """`[(seat, god, aspect_overlay)]` — every `core` a mode ships: each god's
    base kit and, where one is tuned, its aspect.

    HAND-TUNED aspects only. A derived overlay (`scoring.aspect_overlay`)
    takes no seat, so deriving an aspect can never move ANOTHER god's Joust
    build through the anti-heal share. Revisit when a derived family ships in
    Joust: until then its core is the base core and a seat would count it
    twice."""
    aspects = weights.get("aspects") or {}
    out = []
    for g in sorted(gods, key=lambda g: g["name"]):
        out.append((g["name"], g, None))
        ov = aspects.get(g["name"])
        if ov and g.get("aspects"):
            out.append((f"{g['name']} @ {g['aspects'][0].get('name')}", g, ov))
    return out


def _with_share(weights, mode, tag, share):
    team = dict(weights.get("team_tags") or {})
    derived = {m: dict(v) for m, v in (team.get("derived") or {}).items()}
    derived.setdefault(mode.lower(), {})[tag] = share
    team["derived"] = derived
    return {**weights, "team_tags": team}


def derive_team_share(gods, items, weights, tags_map, mode, tag, tol=TEAM_SHARE_TOL):
    """`{share, target, seats, holding, costs: {seat: cost | None}}` for one
    (mode, tag) — see the block above. `weights` must already carry the
    pricing flags the builds are made with."""
    eff, gv = efficiency.efficiency_scores(items)
    ibn = {it["name"]: it for it in items}
    seats = _team_seats(gods, weights)

    def holds(god, overlay, share):
        core, _, _ = assemble_flavor_core(god, items, {"builds": []}, _with_share(weights, mode, tag, share),
                                          tags_map, mode, eff, ibn, gv, None, overlay)
        return any(tag in (tags_map.get(x) or []) for x in core)

    costs = {}
    for seat, god, overlay in seats:
        if not holds(god, overlay, 1.0):
            costs[seat] = None
            continue
        lo, hi = 0.0, 1.0
        if holds(god, overlay, 0.0):
            hi = 0.0
        while hi - lo > tol:
            mid = (lo + hi) / 2
            lo, hi = (lo, mid) if holds(god, overlay, mid) else (mid, hi)
        costs[seat] = round(hi, 6)
    n_team = ((weights.get("modes") or {}).get(mode.lower()) or {}).get("team_size")
    target = round(len(seats) / float(n_team))
    ranked = sorted(c for c in costs.values() if c is not None)
    share = ranked[target - 1] if 0 < target <= len(ranked) else 1.0
    holding = sum(1 for seat, god, ov in seats if holds(god, ov, share))
    return {"share": share, "target": target, "seats": len(seats), "holding": holding,
            "team_size": n_team, "costs": costs}


def derive_team_shares(gods, items, weights, tags_map):
    """`{mode: {tag: derive_team_share(...)}}` for every pair `team_tags.derive` names."""
    out = {}
    for mode, tags in sorted(((weights.get("team_tags") or {}).get("derive") or {}).items()):
        mode_name = next(m for m in MODES if m.lower() == mode)
        for tag in tags:
            out.setdefault(mode, {})[tag] = derive_team_share(gods, items, weights, tags_map, mode_name, tag)
    return out


def write_team_shares(derived, path=TEAM_SHARES_PATH):
    import json
    path.write_text(json.dumps(derived, indent=1, sort_keys=True) + "\n", encoding="utf-8")


def build_suggested_entries(god, items, god_build, weights, tags_map, mode="Conquest"):
    eff_scores, gold_values = efficiency.efficiency_scores(items)
    items_by_name = {it["name"]: it for it in items}
    starter, relic = opening_choices(god, god_build, weights, mode, items_by_name)
    flex_count = (weights.get("build_order") or {}).get("flex_count", 2)
    entries = _build_entry_set(god, items, god_build, weights, tags_map, mode, eff_scores,
                               items_by_name, starter, flex_count, None, None, gold_values,
                               relic=relic)
    aspect_overlay = scoring.aspect_overlay(god, items, weights)
    god_aspects = god.get("aspects") or []
    if aspect_overlay and god_aspects:
        aspect_name = god_aspects[0].get("name")
        aspect_entries = _build_entry_set(god, items, god_build, weights, tags_map, mode,
                                          eff_scores, items_by_name, starter, flex_count,
                                          aspect_overlay, aspect_name, gold_values,
                                          relic=relic)
        # A DERIVED overlay ships only if it moves a build. Its weights are
        # real, but a family whose every six matches the base family's tells
        # the toggle's reader the aspect changes their build when it does not
        # (`build_index._god_item_scores` makes the same argument). Tsukuyomi's
        # Mangetsu is that case on 2026-11-05: STATE.md §4.33.
        if not aspect_overlay.get("derived") or _family_moves(entries, aspect_entries):
            entries += aspect_entries
    return entries


def _family_moves(base_entries, aspect_entries):
    """Whether an aspect family differs from its base family anywhere — an
    archetype present on one side only, or any `slot_order` (membership or
    order) that is not identical."""
    base = {e["archetype"]: e["slot_order"] for e in base_entries}
    asp = {e["archetype"]: e["slot_order"] for e in aspect_entries}
    return base != asp


def main(argv=None):
    parser = argparse.ArgumentParser(description="Score SMITE 2 items and build suggestions")
    parser.add_argument("--efficiency-report", action="store_true",
                        help="write the god-agnostic item efficiency table")
    parser.add_argument("--all", action="store_true",
                        help="write a per-god scoring report for every god")
    parser.add_argument("--report-only", action="store_true",
                        help="write reports but do not modify Build notes")
    args = parser.parse_args(argv)

    if args.all:
        items = load_items()
        weights = scoring.load_weights(WEIGHTS_PATH)
        efficiency.apply_pricing_flags(weights)
        tags_map = scoring.load_tags(TAGS_PATH)
        if not args.report_only:
            # Derive the team-tag shares first: every Joust build below reads them.
            derived = derive_team_shares(load_gods(), items, weights, tags_map)
            write_team_shares(derived)
            scoring.attach_team_shares(weights, derived)
            for mode, tags in derived.items():
                for tag, d in tags.items():
                    print(f"[team share] {mode} {tag}: {d['share']:.4f} -> "
                          f"{d['holding']}/{d['seats']} cores (target {d['target']})")
        # Only buildable items need effect tags — a component is never in a
        # build, so listing all 49 of them turns a useful warning into noise
        # nobody reads.
        #
        # Absent from the file and present-as-`[]` are DIFFERENT STATES and
        # this used to print only the first, which is how it reported "1
        # untagged" against a pool where 55 of 138 carried no tag. Both numbers
        # now appear so they cannot contradict each other; `data_audit.audit_tags`
        # is the gate and carries the reasoning.
        buildable = [it["name"] for it in items if scoring.is_buildable(it)]
        untagged = [n for n in buildable if n not in tags_map]
        reviewed_empty = [n for n in buildable
                          if n in tags_map and not (tags_map[n] or [])]
        print(f"[tags] {len(buildable)} buildable · "
              f"{len(buildable) - len(untagged) - len(reviewed_empty)} tagged · "
              f"{len(reviewed_empty)} reviewed, no tag warranted · "
              f"{len(untagged)} never reviewed")
        if untagged:
            print(f"[tags] never reviewed: {', '.join(sorted(untagged))}")
        out_dir = DATA_ROOT / "Analysis"
        out_dir.mkdir(parents=True, exist_ok=True)
        for god in load_gods():
            build = load_build_note(god["name"])
            (out_dir / f"{god['name']}.md").write_text(
                god_report(god, items, build, weights, tags_map), encoding="utf-8")
            if not args.report_only:
                for mode in MODES:
                    # Conquest uses the community build note for win/pick lookups;
                    # Joust has no community data (SmiteBrain is Conquest-only).
                    mode_build = build if mode == "Conquest" else {"builds": []}
                    entries = build_suggested_entries(god, items, mode_build, weights, tags_map, mode)
                    notes.merge_suggested_entries(
                        BUILDS_ROOT / f"{god['name']}-{mode}.md", god["name"], mode, entries)
                # Conquest has the community build note; stamp the same
                # starter and relic onto its community entry.
                _stamp_community_choices(BUILDS_ROOT / f"{god['name']}-Conquest.md",
                                         *opening_choices(god, build, weights, "Conquest",
                                                          {it["name"]: it for it in items}))
        print("Wrote per-god scoring reports")
        from smite import validate
        per_god, agg = validate.compute(items=items, weights=weights, tags_map=tags_map)
        validate.write_report(per_god, agg, out_dir / "_validation.md")
        print(f"Validation: coverage {agg['mean_coverage']:.0%}, "
              f"win-weighted {agg['mean_win_weighted']:.0%}")
        return 0

    if args.efficiency_report:
        items = load_items()
        out_dir = DATA_ROOT / "Analysis"
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "_efficiency.md"
        out_path.write_text(efficiency_report(items), encoding="utf-8")
        print(f"Wrote {out_path}")
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
