"""Validation harness: how well do our suggested builds and item scores agree
with SmiteBrain's community win rates? Writes Analysis/_validation.md and a
tag-audit report. Agreement is a proxy (win rate is popularity-biased,
Conquest-only) — a falsifiable dashboard, not ground truth."""
import math

from smite import recommend, scoring, efficiency, assemble


def coverage(core, community_names):
    ci = set(community_names)
    if not ci:
        return 0.0
    return len(set(core) & ci) / len(ci)


def win_weighted_coverage(core, community):
    total = sum(c["win_rate"] for c in community if c.get("win_rate") is not None)
    if not total:
        return 0.0
    inc = sum(c["win_rate"] for c in community
              if c.get("win_rate") is not None and c["name"] in set(core))
    return inc / total


def spearman(xs, ys):
    n = len(xs)
    if n < 2:
        return None

    def ranks(v):
        order = sorted(range(n), key=lambda i: v[i])
        r = [0.0] * n
        i = 0
        while i < n:
            j = i
            while j + 1 < n and v[order[j + 1]] == v[order[i]]:
                j += 1
            avg = (i + j) / 2.0
            for k in range(i, j + 1):
                r[order[k]] = avg
            i = j + 1
        return r

    rx, ry = ranks(xs), ranks(ys)
    mx, my = sum(rx) / n, sum(ry) / n
    cov = sum((rx[i] - mx) * (ry[i] - my) for i in range(n))
    denom = math.sqrt(
        sum((rx[i] - mx) ** 2 for i in range(n)) * sum((ry[i] - my) ** 2 for i in range(n))
    )
    return cov / denom if denom else None


def _community_slots(build_note):
    for b in build_note.get("builds", []):
        if b.get("source") == "community":
            return b.get("slot_order", [])
    return []


def god_metrics(god, items, build_note, weights, tags_map, eff_scores, items_by_name):
    profile = scoring.resolve_profile(weights, "Conquest", None)
    rows = scoring.score_god_items(god, items, build_note, eff_scores, weights, tags_map, profile)
    score = {r["item"]: r["total"] for r in rows}
    core = assemble.assemble_core(rows, items_by_name, n=6,
                                  max_lifesteal=scoring.god_max_lifesteal(god, weights, profile))
    community = [c for c in _community_slots(build_note)
                 if c.get("name") in score and c.get("win_rate") is not None]
    names = [c["name"] for c in community]
    return {
        "coverage": coverage(core, names),
        "win_weighted": win_weighted_coverage(core, community),
        "pairs": [(score[c["name"]], c["win_rate"]) for c in community],
        "n": len(community),
    }


def aggregate(per_god):
    vals = list(per_god.values())
    cov = [v["coverage"] for v in vals] or [0.0]
    www = [v["win_weighted"] for v in vals] or [0.0]
    pooled = [p for v in vals for p in v["pairs"]]
    xs = [p[0] for p in pooled]
    ys = [p[1] for p in pooled]
    return {
        "mean_coverage": sum(cov) / len(cov),
        "mean_win_weighted": sum(www) / len(www),
        "pooled_spearman": spearman(xs, ys),
        "pooled_n": len(pooled),
    }


def compute(items=None, weights=None, tags_map=None):
    items = items if items is not None else recommend.load_items()
    weights = weights if weights is not None else scoring.load_weights(recommend.WEIGHTS_PATH)
    tags_map = tags_map if tags_map is not None else scoring.load_tags(recommend.TAGS_PATH)
    eff_scores, _ = efficiency.efficiency_scores(items)
    items_by_name = {it["name"]: it for it in items}
    per_god = {}
    for god in recommend.load_gods():
        build = recommend.load_build_note(god["name"])
        if not _community_slots(build):
            continue  # no community data (e.g., not yet scraped)
        per_god[god["name"]] = god_metrics(god, items, build, weights, tags_map, eff_scores, items_by_name)
    return per_god, aggregate(per_god)


def write_report(per_god, agg, out_path):
    header = (
        f"**Mean coverage:** {agg['mean_coverage']:.0%}  ·  "
        f"**Win-weighted coverage:** {agg['mean_win_weighted']:.0%}"
    )
    if agg["pooled_spearman"] is not None:
        header += f"  ·  **Pooled rank corr:** {agg['pooled_spearman']:.2f} (n={agg['pooled_n']})"
    lines = [
        "# Recommender validation (vs SmiteBrain community win rates)",
        "",
        "Agreement is a proxy — win rate is popularity-biased and Conquest-only.",
        "",
        header,
        "",
        "| God | Coverage | Win-weighted | Community items |",
        "|---|---|---|---|",
    ]
    for name in sorted(per_god):
        m = per_god[name]
        lines.append(f"| {name} | {m['coverage']:.0%} | {m['win_weighted']:.0%} | {m['n']} |")
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


# Precise keywords only (avoid false positives on terse passives).
TAG_KEYWORDS = {
    "anti-heal": ["healing reduc", "reduce healing", "reduced healing",
                  "reduces enemy healing", "anti-heal", "less healing"],
    "sustain": ["lifesteal", "life steal"],
    "aura": ["aura", "nearby allies", "allied gods within", "allies within"],
    "cc-immunity": ["crowd control immun", "cc immun", "unstoppable", "cleanse", "immune to crowd"],
    "mobility": ["dash", "leap", "teleport", "blink", "charge toward"],
    "protection-shred": ["reduce protection", "protection reduc", "reduced protections", "protection shred"],
    "wave-clear": ["wave clear", "wave-clear"],
    "anti-crit": ["critical strike reduc", "reduce critical", "against critical", "block critical"],
}


def tag_audit(items, tags_map):
    issues = []
    for it in items:
        passive = (it.get("passive") or "").lower()
        tags = set(tags_map.get(it["name"]) or it.get("effect_tags") or [])
        for tag, kws in TAG_KEYWORDS.items():
            has_kw = any(k in passive for k in kws)
            has_tag = tag in tags
            if has_tag and not has_kw:
                issues.append({"item": it["name"], "kind": "tag-without-evidence", "tag": tag})
            elif has_kw and not has_tag:
                issues.append({"item": it["name"], "kind": "possible-missing", "tag": tag})
    return issues


def write_tag_audit(items, tags_map, out_path):
    issues = tag_audit(items, tags_map)
    missing = sum(1 for i in issues if i["kind"] == "possible-missing")
    lines = ["# Effect-tag audit (keyword heuristic — review, don't auto-apply)", "",
             f"{len(issues)} candidate(s), {missing} `possible-missing`. Keyword scan of item "
             "passives vs `_tags.yaml`.", "",
             "- **possible-missing** = a keyword is in the passive but the tag isn't set — the "
             "actionable direction (a likely gap).",
             "- **tag-without-evidence** = tagged but the (often terse) passive lacks the keyword — "
             "usually fine, since tags are curated from game knowledge.", "",
             "| Item | Issue | Tag |", "|---|---|---|"]
    for i in sorted(issues, key=lambda x: (x["kind"], x["item"])):
        lines.append(f"| {i['item']} | {i['kind']} | {i['tag']} |")
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return issues


def main(argv=None):
    per_god, agg = compute()
    out_dir = recommend.DATA_ROOT / "Analysis"
    out_dir.mkdir(parents=True, exist_ok=True)
    write_report(per_god, agg, out_dir / "_validation.md")
    items = recommend.load_items()
    tags_map = scoring.load_tags(recommend.TAGS_PATH)
    n = len(write_tag_audit(items, tags_map, out_dir / "_tag_audit.md"))
    print(f"Wrote _validation.md (coverage {agg['mean_coverage']:.0%}) "
          f"and _tag_audit.md ({n} candidates)")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
