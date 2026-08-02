"""Disagreement report: where the community meta and our scores part ways.
Read-only analysis tool — run it, form a hypothesis (tag gap? fit blind spot?
assembly rule?), encode the fix elsewhere, re-validate. Writes
Analysis/_disagreements.md."""
from collections import Counter

from smite import assemble, efficiency, recommend, scoring

PICK_MISSED = 0.10      # community pick rate that makes an item "meta"
RANK_CUT = 10           # our rank below this = we effectively don't suggest it
PICK_OFFMETA = 0.05     # community pick under this = "nobody runs it"


def god_disagreements(god, items, build_note, weights, tags_map, eff_scores, items_by_name):
    profile = scoring.resolve_profile(weights, "Conquest", None)
    rows = scoring.score_god_items(god, items, build_note, eff_scores, weights, tags_map, profile)
    rank = {r["item"]: i + 1 for i, r in enumerate(rows)}
    by_name = {r["item"]: r for r in rows}
    core = assemble.assemble_core(rows, items_by_name, n=6,
                                  max_lifesteal=scoring.god_max_lifesteal(god, weights, profile),
                                  stat_caps=weights.get("stat_caps"))
    community = [c for b in build_note.get("builds", []) if b.get("source") == "community"
                 for c in b.get("slot_order", []) if isinstance(c, dict)]
    missed = []
    for c in community:
        name = c.get("name")
        if (c.get("pick_rate") or 0.0) >= PICK_MISSED and rank.get(name, 10**6) > RANK_CUT:
            missed.append({"item": name, "pick": c.get("pick_rate"), "win": c.get("win_rate"),
                           "rank": rank.get(name), "row": by_name.get(name),
                           "filtered_out": name not in rank})
    comm_pick = {c.get("name"): (c.get("pick_rate") or 0.0) for c in community}
    off_meta = [{"item": n, "pick": comm_pick.get(n, 0.0), "row": by_name[n], "rank": rank[n]}
                for n in core if comm_pick.get(n, 0.0) < PICK_OFFMETA]
    top6 = [r["item"] for r in rows[:6]]
    conflicts = [n for n in top6
                 if n not in core and comm_pick.get(n, 0.0) >= PICK_MISSED]
    return {"missed_meta": missed, "off_meta": off_meta, "constraint_conflicts": conflicts}


def _fmt_row(r):
    if not r:
        return "filtered out (damage filter / not buildable)"
    return (f"total {r['total']:.2f} · eff {r['efficiency']:.2f} · win {r['win']:.2f} "
            f"· pick {r['pick']:.2f} · fit {r['fit']:.2f} · tags: {', '.join(r['tags']) or '—'}")


def write_report(per_god, items_by_name, out_path):
    lines = ["# Meta disagreements (community vs our scores)", "",
             "Hypothesis generator, not a verdict. `missed meta` = community runs it, "
             "we rank it low. `off-meta pick` = we suggest it, community doesn't. "
             "`constraint conflict` = scoring liked it but an assembly rule "
             "(lifesteal cap / boots / crit floor) kept it out of the core.", ""]
    rollup = Counter()
    for god_name in sorted(per_god):
        d = per_god[god_name]
        if not (d["missed_meta"] or d["off_meta"] or d["constraint_conflicts"]):
            continue
        lines.append(f"## {god_name}")
        for m in d["missed_meta"]:
            rollup[m["item"]] += 1
            it = items_by_name.get(m["item"], {})
            lines += [f"- **missed meta:** {m['item']} — community pick {m['pick']:.0%}, "
                      f"win {(m['win'] or 0):.0%}, our rank {m['rank'] or 'filtered'}",
                      f"  - {_fmt_row(m['row'])}",
                      f"  - passive: {(it.get('passive') or '—')[:200]}"]
        for o in d["off_meta"]:
            lines.append(f"- off-meta pick: {o['item']} (our rank {o['rank']}, "
                         f"community pick {o['pick']:.0%})")
        for c in d["constraint_conflicts"]:
            lines.append(f"- **constraint conflict:** {c} — top-6 by score, "
                         f"meta-picked, excluded by assembly rules")
        lines.append("")
    if rollup:
        lines += ["## Cross-god rollup (items we repeatedly miss)", ""]
        lines += [f"- {name} × {n}" for name, n in rollup.most_common() if n > 1]
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv=None):
    items = recommend.load_items()
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    tags_map = scoring.load_tags(recommend.TAGS_PATH)
    eff_scores, _ = efficiency.efficiency_scores(items)
    items_by_name = {it["name"]: it for it in items}
    per_god = {}
    for god in recommend.load_gods():
        build = recommend.load_build_note(god["name"])
        if any(b.get("source") == "community" for b in build.get("builds", [])):
            per_god[god["name"]] = god_disagreements(
                god, items, build, weights, tags_map, eff_scores, items_by_name)
    out = recommend.DATA_ROOT / "Analysis" / "_disagreements.md"
    write_report(per_god, items_by_name, out)
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
