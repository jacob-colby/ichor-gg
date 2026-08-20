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


def load_items():
    items_dir = DATA_ROOT / "Items"
    out = []
    for path in sorted(items_dir.glob("*.md")):
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
    for path in sorted((DATA_ROOT / "Gods").glob("*.md")):
        fm, _ = notes.read_note(path)
        if fm.get("name"):
            out.append(fm)
    return out


def load_build_note(god_name, mode="Conquest"):
    fm, _ = notes.read_note(BUILDS_ROOT / f"{god_name}-{mode}.md")
    return fm or {"builds": []}


def _stamp_community_starter(path, starter):
    """Set `starter` on the community entry of a Build note (role-based, so the
    community build shows the same recommended starter as the suggested ones)."""
    if not starter:
        return
    fm, body = notes.read_note(path)
    if not fm:
        return
    changed = False
    for b in fm.get("builds", []):
        if b.get("source") == "community":
            b["starter"] = starter
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
           flex_count, starter, aspect_name, fun=False, extra=None):
    """One suggested build entry from an already-assembled core.

    Extracted so every archetype is packaged identically — `model` differs from
    `core` only in how its rows were ranked, and that difference has to stay the
    only difference between them.
    """
    flex = assemble.flex_slots(core, rows, count=flex_count)
    ordered = assemble.build_order(core, items_by_name, tags_map, weights)
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
        **(extra or {}),
        **({"fun": True} if fun else {}),
        **({"starter": starter} if starter else {}),
        **({"aspect": aspect_name} if aspect_name else {}),
    }


def _build_entry_set(god, items, god_build, weights, tags_map, mode, eff_scores,
                     items_by_name, starter, flex_count, aspect_overlay, aspect_name,
                     gold_values=None):
    entries = []
    core_rows = core_profile = None
    eligible = scoring.eligible_flavors(god, weights, items)
    for flavor in [None] + eligible:
        cfg = ((weights.get("flavors") or {}).get(flavor) or {}) if flavor else {}
        if cfg.get("fun") and (aspect_overlay is not None
                               or cfg.get("redundant_with") in eligible):
            continue  # fun builds: base kit only, and never beside a serious twin
        profile = scoring.resolve_profile(weights, mode, flavor, aspect_overlay=aspect_overlay)
        rows = scoring.score_god_items(god, items, god_build, eff_scores, weights, tags_map, profile)
        require = cfg.get("require") if flavor else None
        core, _ = assemble.assemble_core_converged(
            rows, items_by_name, passes=weights.get("conversion_passes", 1), n=6,
            max_lifesteal=scoring.god_max_lifesteal(god, weights, profile),
            require=require,
            stat_caps=weights.get("stat_caps"),
            economy=profile.get("economy"),
            **assemble.coherence_args(items, weights),
            **assemble.conversion_args(weights, eff_scores, gold_values))
        archetype = flavor or "core"
        if flavor is None:
            core_rows, core_profile = rows, profile
        entries.append(_entry(archetype, core, rows, items_by_name, tags_map,
                              weights, profile, flex_count, starter, aspect_name,
                              fun=bool(cfg.get("fun"))))

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
            **assemble.conversion_args(weights, eff_scores, gold_values))
        entries.append(_entry("model", model_core, model_rows, items_by_name,
                              tags_map, weights, core_profile, flex_count,
                              starter, aspect_name))

        # And the hybrid: that same core, corrected only where the model is
        # near-indifferent and the community's record is strong enough to
        # override it. `hybrid_core` returns the model core unchanged when
        # there is nothing to correct with — a duplicate build, so it isn't
        # emitted.
        community_entry = next(
            (b for b in (god_build or {}).get("builds", []) if b.get("source") == "community"),
            None)

        # A mode with no community data of its own may BORROW another's. Joust
        # and Arena had none, so this build simply did not exist there — 89 of
        # 89 gods in each got the model core back and nothing was emitted.
        # Conquest's record is still the best evidence about an item; it is
        # just evidence about a different game, so the parts that do not
        # transfer are rejected by tag (see `borrow_community` in
        # _weights.yaml) and the result is labelled as borrowed rather than
        # passed off as this mode's own.
        borrow = ((weights.get("modes") or {}).get(mode.lower(), {}) or {}).get("borrow_community")
        borrowed_from = None
        if not community_entry and borrow:
            source_mode = borrow.get("from", "Conquest")
            source = load_build_note(god["name"], source_mode)
            community_entry = next(
                (b for b in (source or {}).get("builds", []) if b.get("source") == "community"),
                None)
            if community_entry:
                borrowed_from = source_mode
            reject_tags = borrow.get("reject_tags") or []
        else:
            reject_tags = []

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
                                  starter, aspect_name, extra=extra))
    return entries


def build_suggested_entries(god, items, god_build, weights, tags_map, mode="Conquest"):
    eff_scores, gold_values = efficiency.efficiency_scores(items)
    items_by_name = {it["name"]: it for it in items}
    starter = scoring.pick_starter(god, weights)
    flex_count = (weights.get("build_order") or {}).get("flex_count", 2)
    entries = _build_entry_set(god, items, god_build, weights, tags_map, mode, eff_scores,
                               items_by_name, starter, flex_count, None, None, gold_values)
    aspect_overlay = (weights.get("aspects") or {}).get(god["name"])
    god_aspects = god.get("aspects") or []
    if aspect_overlay and god_aspects:
        aspect_name = god_aspects[0].get("name")
        entries += _build_entry_set(god, items, god_build, weights, tags_map, mode, eff_scores,
                                    items_by_name, starter, flex_count, aspect_overlay,
                                    aspect_name, gold_values)
    return entries


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
                # role-based starter onto its community entry.
                _stamp_community_starter(BUILDS_ROOT / f"{god['name']}-Conquest.md",
                                         scoring.pick_starter(god, weights))
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
