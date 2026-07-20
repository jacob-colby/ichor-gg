# Validation harness + honest labels + freshness Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Give the recommender a falsifiable validation dashboard (vs community win rates), reframe the efficiency labels honestly + surface the real meta signal, and add a tag-audit report + one-command freshness script.

**Architecture:** Python — a `validate` module (pure metric helpers + a report writer + a tag audit) run from `recommend --all`; `build_index` folds a per-item meta aggregate into `index.json`; a `refresh_and_deploy` orchestration script. Viewer — reframed efficiency labels + a meta badge in the shop.

**Tech Stack:** Python 3.10 (pytest); Vite + React + TS + Vitest. Real viewer typecheck is `npm run build` (`tsc -b`).

**Reference spec:** [2026-07-19-smite-validation-labels-freshness-design.md](../specs/2026-07-19-smite-validation-labels-freshness-design.md)

---

## File Structure
- `tools/smite/validate.py` — metrics + report + tag audit (create).
- `tools/smite/recommend.py` — call validate at the end of `--all` (modify).
- `tools/smite/build_index.py` — per-item `meta` aggregate (modify).
- `tools/smite/refresh_and_deploy.py` — one-command pipeline (create).
- `viewer/src/types.ts` — `Item.meta` (modify).
- `viewer/src/lib/itemFilters.ts` — Efficient/Fair/Premium labels (modify).
- `viewer/src/components/ItemsShop.tsx` — meta badge + help note (modify).
- `viewer/DEPLOY.md` — documented cron line (modify).

---

## PHASE A — validation harness (weakness 2)

### Task A1: metric helpers

**Files:** Create `tools/smite/validate.py`; Test `tools/smite/tests/test_validate.py`

- [ ] **Step 1: Write failing tests** (`test_validate.py`):
```python
from smite import validate


def test_coverage():
    assert validate.coverage(["A", "B", "C"], ["A", "B", "X"]) == 2 / 3
    assert validate.coverage([], []) == 0.0


def test_win_weighted_coverage():
    community = [{"name": "A", "win_rate": 0.6}, {"name": "B", "win_rate": 0.5}, {"name": "C", "win_rate": 0.5}]
    # core includes A only -> 0.6 / 1.6
    assert abs(validate.win_weighted_coverage(["A"], community) - 0.6 / 1.6) < 1e-9
    assert validate.win_weighted_coverage([], []) == 0.0


def test_spearman_monotonic():
    assert abs(validate.spearman([1, 2, 3, 4], [10, 20, 30, 40]) - 1.0) < 1e-9
    assert abs(validate.spearman([1, 2, 3, 4], [40, 30, 20, 10]) + 1.0) < 1e-9
    assert validate.spearman([1], [1]) is None  # too few points
```

- [ ] **Step 2: Run, confirm FAIL**

Run: `cd tools && python -m pytest smite/tests/test_validate.py -v`

- [ ] **Step 3: Implement the helpers** in `tools/smite/validate.py`:
```python
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
    inc = sum(c["win_rate"] for c in community if c.get("win_rate") is not None and c["name"] in set(core))
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
    denom = math.sqrt(sum((rx[i] - mx) ** 2 for i in range(n)) * sum((ry[i] - my) ** 2 for i in range(n)))
    return cov / denom if denom else None
```

- [ ] **Step 4: Run, confirm PASS**

Run: `cd tools && python -m pytest smite/tests/test_validate.py -v`

- [ ] **Step 5: Commit**
```bash
git add tools/smite/validate.py tools/smite/tests/test_validate.py
git commit -m "feat(smite): validation metric helpers (coverage, win-weighted, spearman)"
```

---

### Task A2: report writer + wire into recommend

**Files:** Modify `tools/smite/validate.py`, `tools/smite/recommend.py`; Test `tools/smite/tests/test_validate.py`

- [ ] **Step 1: Write failing test** (append) — exercises `god_metrics` against a tiny synthetic setup using monkeypatched loaders is heavy; instead test the pure aggregation `aggregate` over prebuilt per-god metrics:
```python
def test_aggregate_summarizes_per_god():
    per_god = {
        "A": {"coverage": 1.0, "win_weighted": 1.0, "pairs": [(3, 0.6), (2, 0.5), (1, 0.4)]},
        "B": {"coverage": 0.5, "win_weighted": 0.5, "pairs": [(1, 0.4), (2, 0.5)]},
    }
    agg = validate.aggregate(per_god)
    assert abs(agg["mean_coverage"] - 0.75) < 1e-9
    assert abs(agg["mean_win_weighted"] - 0.75) < 1e-9
    assert agg["pooled_spearman"] is not None  # 5 pooled pairs
```

- [ ] **Step 2: Run, confirm FAIL**

Run: `cd tools && python -m pytest smite/tests/test_validate.py -k aggregate -v`

- [ ] **Step 3: Implement** `god_metrics`, `aggregate`, `write_report`, `main` in `validate.py`:
```python
def _community_slots(build_note):
    for b in build_note.get("builds", []):
        if b.get("source") == "community":
            return b.get("slot_order", [])
    return []


def god_metrics(god, items, build_note, weights, tags_map, eff_scores, items_by_name):
    profile = scoring.resolve_profile(weights, "Conquest", None)
    rows = scoring.score_god_items(god, items, build_note, eff_scores, weights, tags_map, profile)
    score = {r["item"]: r["total"] for r in rows}
    core = assemble.assemble_core(rows, items_by_name, n=6, max_lifesteal=profile["max_lifesteal"])
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
    lines = ["# Recommender validation (vs SmiteBrain community win rates)", "",
             "Agreement is a proxy — win rate is popularity-biased and Conquest-only.", "",
             f"**Mean coverage:** {agg['mean_coverage']:.0%}  ·  "
             f"**Win-weighted coverage:** {agg['mean_win_weighted']:.0%}  ·  "
             f"**Pooled rank corr:** {agg['pooled_spearman']:.2f} (n={agg['pooled_n']})"
             if agg["pooled_spearman"] is not None else
             f"**Mean coverage:** {agg['mean_coverage']:.0%}  ·  **Win-weighted coverage:** {agg['mean_win_weighted']:.0%}",
             "", "| God | Coverage | Win-weighted | Community items |", "|---|---|---|---|"]
    for name in sorted(per_god):
        m = per_god[name]
        lines.append(f"| {name} | {m['coverage']:.0%} | {m['win_weighted']:.0%} | {m['n']} |")
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv=None):
    per_god, agg = compute()
    out = recommend.DATA_ROOT / "Analysis" / "_validation.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    write_report(per_god, agg, out)
    print(f"Wrote {out}  (coverage {agg['mean_coverage']:.0%}, "
          f"win-weighted {agg['mean_win_weighted']:.0%})")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
```
Confirm the real symbols during implementation: `recommend.load_items/load_gods/load_build_note`, `recommend.WEIGHTS_PATH/TAGS_PATH/DATA_ROOT`, `scoring.score_god_items` row key `"total"`/`"item"`, `assemble.assemble_core` signature. Adjust if any differ.

- [ ] **Step 4: Wire into `recommend --all`** — in `recommend.py`'s `--all` branch, after the per-god loop / `print("Wrote per-god scoring reports")`, add:
```python
        from smite import validate
        per_god, agg = validate.compute(items=items, weights=weights, tags_map=tags_map)
        validate.write_report(per_god, agg, out_dir / "_validation.md")
        print(f"Validation: coverage {agg['mean_coverage']:.0%}, win-weighted {agg['mean_win_weighted']:.0%}")
```
(`items`, `weights`, `tags_map`, `out_dir` are already in scope there.)

- [ ] **Step 5: Run tests + a live smoke** — `cd tools && python -m pytest smite/tests/test_validate.py -v` then `python -m smite.validate` and open `04. System/Data/SMITE/Analysis/_validation.md` to eyeball real numbers.

- [ ] **Step 6: Commit**
```bash
git add tools/smite/validate.py tools/smite/recommend.py tools/smite/tests/test_validate.py
git commit -m "feat(smite): validation report vs community win rates, wired into recommend --all"
```

---

## PHASE B — honest labels + meta signal (weakness 3)

### Task B1: per-item meta in build_index

**Files:** Modify `tools/smite/build_index.py`; Test `tools/smite/tests/test_build_index.py`

- [ ] **Step 1: Write failing test** (append to `test_build_index.py`):
```python
def test_build_index_adds_per_item_meta(tmp_path, monkeypatch):
    # Uses the real vault; assert an item that appears in community builds carries
    # meta {win_avg, gods}. Deathbringer/Transcendence appear widely.
    from smite import build_index
    from pathlib import Path
    result = build_index.build_index(Path(__file__).resolve().parents[3])
    metaed = [i for i in result["items"] if i.get("meta")]
    assert metaed, "expected some items to carry community meta"
    m = metaed[0]["meta"]
    assert 0.0 <= m["win_avg"] <= 1.0 and m["gods"] >= 1
```

- [ ] **Step 2: Run, confirm FAIL**

Run: `cd tools && python -m pytest smite/tests/test_build_index.py -k per_item_meta -v`

- [ ] **Step 3: Implement** — in `build_index.build_index(vault_root)`, after both `items` and the build notes are loaded, compute a per-item meta aggregate from Conquest community entries and attach it. Read the existing function to get the exact variable names (the items list and the builds list) and insert before the return:
```python
    from collections import defaultdict
    wins = defaultdict(list)
    for note in builds:  # builds = the list of build-note dicts already loaded
        if note.get("mode") != "Conquest":
            continue
        for b in note.get("builds", []):
            if b.get("source") != "community":
                continue
            for slot in b.get("slot_order", []):
                wr = slot.get("win_rate") if isinstance(slot, dict) else None
                if wr is not None:
                    wins[slot["name"]].append(wr)
    for it in items:
        vals = wins.get(it["name"])
        if vals:
            it["meta"] = {"win_avg": round(sum(vals) / len(vals), 3), "gods": len(vals)}
```
Adapt `builds`/`items` to the actual local names in `build_index`.

- [ ] **Step 4: Run, confirm PASS** + full suite

Run: `cd tools && python -m pytest smite/tests/test_build_index.py -v` then `cd tools && python -m pytest smite/tests/ -q -m "not live"`

- [ ] **Step 5: Commit**
```bash
git add tools/smite/build_index.py tools/smite/tests/test_build_index.py
git commit -m "feat(smite): per-item community meta (avg win% + god count) in index"
```

---

### Task B2: reframe efficiency labels + types

**Files:** Modify `viewer/src/lib/itemFilters.ts`, `viewer/src/types.ts`; Test `viewer/src/lib/itemFilters.test.ts`

- [ ] **Step 1: Update the failing test** — in `itemFilters.test.ts`, change the `efficiencyLabel` expectations:
```typescript
  it("maps tiers to stat-value labels", () => {
    expect(efficiencyLabel("undervalued").text).toBe("Efficient");
    expect(efficiencyLabel("premium").text).toBe("Premium");
    expect(efficiencyLabel("fair").text).toBe("Fair");
    expect(efficiencyLabel(null).text).toBe("—");
    expect(EFFICIENCY.length).toBe(4);
  });
```

- [ ] **Step 2: Run, confirm FAIL**

Run: `cd viewer && npx vitest run src/lib/itemFilters.test.ts`

- [ ] **Step 3: Implement** — in `itemFilters.ts`, change the `EFFICIENCY` label text (keys unchanged):
```typescript
export const EFFICIENCY: EfficiencyMeta[] = [
  { key: "undervalued", text: "Efficient", cls: "bg-under/20 text-under" },
  { key: "fair", text: "Fair", cls: "bg-line text-muted" },
  { key: "premium", text: "Premium", cls: "bg-premium/20 text-premium" },
  { key: "untiered", text: "—", cls: "bg-line text-muted" },
];
```
Add `meta` to the `Item` type in `types.ts`:
```typescript
  effect_tags?: string[];
  efficiency_tier?: string | null;
  meta?: { win_avg: number; gods: number };
```

- [ ] **Step 4: Run, confirm PASS**

Run: `cd viewer && npx vitest run src/lib/itemFilters.test.ts`

- [ ] **Step 5: Commit**
```bash
git add viewer/src/lib/itemFilters.ts viewer/src/types.ts viewer/src/lib/itemFilters.test.ts
git commit -m "feat(viewer): reframe efficiency labels to stat-value (Efficient/Fair/Premium)"
```

---

### Task B3: meta badge + help note in the shop

**Files:** Modify `viewer/src/components/ItemsShop.tsx`; Test `viewer/src/components/ItemsShop.test.tsx`

- [ ] **Step 1: Update tests** — the existing ItemsShop test asserts "Underrated"/"Overrated"; change to the new labels and add a meta-badge test. Replace the label assertions:
```tsx
    expect(screen.getByText("Efficient", { selector: "span" })).toBeInTheDocument();
    expect(screen.getByText("Premium", { selector: "span" })).toBeInTheDocument();
```
Add a test (give one item `meta`):
```tsx
  it("shows a meta win badge for items that have community meta", () => {
    const withMeta = [
      { ...items[0], meta: { win_avg: 0.55, gods: 4 } },
      items[1],
    ] as unknown as Item[];
    render(<ItemsShop items={withMeta} openItem={undefined} />);
    expect(screen.getByText(/55% avg · 4/)).toBeInTheDocument();
  });
```
(Add `meta?: { win_avg: number; gods: number }` to the test fixture's item type via the `as unknown as Item[]` cast — already used.)

- [ ] **Step 2: Run, confirm FAIL**

Run: `cd viewer && npx vitest run src/components/ItemsShop.test.tsx`

- [ ] **Step 3: Implement** — in `ItemsShop.tsx`:
  1. Add a `MetaBadge` helper near `EffBadge`:
```tsx
function MetaBadge({ meta }: { meta?: { win_avg: number; gods: number } }) {
  if (!meta) return null;
  return <span className="text-[10px] text-muted">{Math.round(meta.win_avg * 100)}% avg · {meta.gods}</span>;
}
```
  2. On the card, add the meta badge next to the efficiency badge — change the card's badge row:
```tsx
            <div className="flex items-center justify-between gap-1">
              <div className="flex items-center gap-1"><EffBadge tier={it.efficiency_tier} /><MetaBadge meta={it.meta} /></div>
              {(it.effect_tags?.length ?? 0) > 0 && (
                <span className="truncate text-[10px] text-blue">{it.effect_tags!.join(" · ")}</span>
              )}
            </div>
```
  3. In `ItemDetail`, add the meta badge next to its `EffBadge` in the header:
```tsx
        <div className="ml-auto flex items-center gap-2"><MetaBadge meta={item.meta} /><EffBadge tier={item.efficiency_tier} /></div>
```
  4. Add a one-line help note above the filter bar:
```tsx
      <div className="mb-2 text-[11px] text-muted">
        Rating = stats-per-gold (not power). <b className="text-ink">Premium</b> items are often worth overpaying for their passive. Avg = community win rate where used.
      </div>
```

- [ ] **Step 4: Run, confirm PASS** + build

Run: `cd viewer && npx vitest run && npm run build`

- [ ] **Step 5: Commit**
```bash
git add viewer/src/components/ItemsShop.tsx viewer/src/components/ItemsShop.test.tsx
git commit -m "feat(viewer): meta win badge + stat-value help note in shop"
```

---

## PHASE C — tag audit + freshness (weakness 6)

### Task C1: tag audit

**Files:** Modify `tools/smite/validate.py`; Test `tools/smite/tests/test_validate.py`

- [ ] **Step 1: Write failing test** (append):
```python
def test_tag_audit_flags_mismatches():
    items = [
        {"name": "Divine Ruin", "passive": "Reduces enemy Healing by 40%.", "effect_tags": []},        # missing anti-heal
        {"name": "Mystery", "passive": "Grants Attack Speed.", "effect_tags": ["anti-heal"]},           # tag w/o evidence
        {"name": "Clean", "passive": "Reduces enemy Healing by 40%.", "effect_tags": ["anti-heal"]},    # ok
    ]
    tags_map = {it["name"]: it["effect_tags"] for it in items}
    issues = validate.tag_audit(items, tags_map)
    kinds = {(i["item"], i["kind"], i["tag"]) for i in issues}
    assert ("Divine Ruin", "possible-missing", "anti-heal") in kinds
    assert ("Mystery", "tag-without-evidence", "anti-heal") in kinds
    assert not any(i["item"] == "Clean" for i in issues)
```

- [ ] **Step 2: Run, confirm FAIL**

Run: `cd tools && python -m pytest smite/tests/test_validate.py -k tag_audit -v`

- [ ] **Step 3: Implement** — append to `validate.py`:
```python
# Precise keywords only (avoid false positives on terse passives).
TAG_KEYWORDS = {
    "anti-heal": ["healing reduc", "reduce healing", "reduced healing", "reduces enemy healing", "anti-heal", "less healing"],
    "sustain": ["lifesteal", "life steal"],
    "aura": ["aura", "nearby allies", "allied gods within", "allies within"],
    "cc-immunity": ["crowd control immun", "cc immun", "unstoppable", "cleanse", "immune to crowd"],
    "mobility": ["movement speed", "dash", "leap"],
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
    lines = ["# Effect-tag audit (keyword heuristic — review, don't auto-apply)", "",
             f"{len(issues)} candidate(s). Keyword scan of item passives vs `_tags.yaml`.", "",
             "| Item | Issue | Tag |", "|---|---|---|"]
    for i in sorted(issues, key=lambda x: (x["kind"], x["item"])):
        lines.append(f"| {i['item']} | {i['kind']} | {i['tag']} |")
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return issues
```
Also call it from `main` (write both reports):
```python
def main(argv=None):
    per_god, agg = compute()
    out_dir = recommend.DATA_ROOT / "Analysis"
    out_dir.mkdir(parents=True, exist_ok=True)
    write_report(per_god, agg, out_dir / "_validation.md")
    items = recommend.load_items()
    tags_map = scoring.load_tags(recommend.TAGS_PATH)
    n = len(write_tag_audit(items, tags_map, out_dir / "_tag_audit.md"))
    print(f"Wrote _validation.md (coverage {agg['mean_coverage']:.0%}) and _tag_audit.md ({n} candidates)")
    return 0
```

- [ ] **Step 4: Run, confirm PASS** + full suite + live smoke

Run: `cd tools && python -m pytest smite/tests/test_validate.py -v` then `python -m smite.validate` and eyeball `Analysis/_tag_audit.md`.

- [ ] **Step 5: Commit**
```bash
git add tools/smite/validate.py tools/smite/tests/test_validate.py
git commit -m "feat(smite): effect-tag audit report (keyword heuristic)"
```

---

### Task C2: freshness script + documented cron

**Files:** Create `tools/smite/refresh_and_deploy.py`; Modify `viewer/DEPLOY.md`

- [ ] **Step 1: Implement `tools/smite/refresh_and_deploy.py`** (orchestration; no unit test — verified by the live run in Task D):
```python
"""One-command patch update: re-scrape everything, recompute, rebuild the index,
then commit the generated data narrowly and push (which triggers the static-host
redeploy). Run from the vault on the canonical git device.

    python -m smite.refresh_and_deploy            # scrape + regen + commit + push
    python -m smite.refresh_and_deploy --no-push  # scrape + regen + commit only
"""
import argparse
import subprocess
import sys

from smite import refresh, recommend, build_index, validate


def _run_git(args, cwd):
    subprocess.run(["git", *args], cwd=cwd, check=True)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Refresh + regenerate + deploy")
    parser.add_argument("--no-push", action="store_true", help="commit but do not push")
    args = parser.parse_args(argv)

    refresh.refresh_all()
    recommend.main(["--all"])
    build_index.write_index(recommend.VAULT_ROOT, recommend.VAULT_ROOT / "viewer" / "public" / "index.json")
    validate.main()

    root = recommend.VAULT_ROOT
    paths = [
        "03. Workspaces/Gaming/SMITE 2/Builds",
        "04. System/Data/SMITE/Gods",
        "04. System/Data/SMITE/Items",
        "04. System/Data/SMITE/Analysis",
        "viewer/public/index.json",
    ]
    _run_git(["add", "--", *paths], root)
    # commit only if there is something staged
    if subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=root).returncode != 0:
        _run_git(["commit", "-m", "chore(smite): scheduled data refresh"], root)
        if not args.no_push:
            _run_git(["push"], root)
        print("refresh_and_deploy: committed" + ("" if args.no_push else " + pushed"))
    else:
        print("refresh_and_deploy: no data changes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```
Note during implementation: confirm `refresh.refresh_all` and `recommend.VAULT_ROOT` exist (they do). This uses a plain `git add -- <paths>` scoped to the generated data (never `git add -A`), matching the narrow-commit hygiene rule; it does not set a git identity (it runs as the invoking user) — the documented cron line (below) is for the canonical device, so this is acceptable for a user-run/opt-in script.

- [ ] **Step 2: Document the cron option** — append to `viewer/DEPLOY.md`:
```markdown
## Keeping data fresh automatically (optional)

`python -m smite.refresh_and_deploy` (run from the vault, in `tools/`) does the
whole patch update: re-scrape → recompute → rebuild `index.json` → commit the
generated data → push (which redeploys the host). Add `--no-push` to stage a
commit without pushing.

To run it weekly, add a cron entry **on your canonical git device only** (the one
that owns vault auto-commits — see Vault Hygiene). Example (Mondays 06:00):

    0 6 * * 1  cd /path/to/obsidian-vault/tools && python -m smite.refresh_and_deploy >> /path/to/refresh.log 2>&1

Scraping needs Python + Playwright working on that device. Not installed by
default — enable it when you're confident the scrape runs headless there.
```

- [ ] **Step 3: Verify import graph** — `cd tools && python -c "import smite.refresh_and_deploy"` (should import cleanly).

- [ ] **Step 4: Commit**
```bash
git add tools/smite/refresh_and_deploy.py viewer/DEPLOY.md
git commit -m "feat(smite): refresh_and_deploy script + documented freshness cron"
```

---

## PHASE D — regenerate + verify

### Task D1: regenerate reports + index, browser-verify, deploy build

**Files:** generated — `Analysis/_validation.md`, `Analysis/_tag_audit.md`, `viewer/public/index.json`

- [ ] **Step 1: Regenerate** — from `tools/`: `python -m smite.recommend --all` (writes `_validation.md` too) then `python -m smite.validate` (writes `_tag_audit.md`) then `python -m smite.build_index` (adds per-item meta). Eyeball `Analysis/_validation.md` (coverage/win-weighted/pooled corr) and `Analysis/_tag_audit.md` (review list). Confirm index items carry `meta`:
```bash
cd .. && python -c "
import json; d=json.load(open('viewer/public/index.json',encoding='utf-8'))
print('items with meta:', sum(1 for i in d['items'] if i.get('meta')))
print('sample:', next((i['name'], i['meta']) for i in d['items'] if i.get('meta')))
"
```

- [ ] **Step 2: Suites + build**

Run: `cd tools && python -m pytest smite/tests/ -q -m "not live"` and `cd ../viewer && npx vitest run && npm run build`.

- [ ] **Step 3: Browser verify** (dev server): open `#/items` → confirm badges read **Efficient / Fair / Premium**, the help note shows, and items used by the community show a **"55% avg · N"** meta badge; open an item's detail and confirm the meta badge there. Confirm the efficiency filter dropdown uses the new labels. Fix + re-verify.

- [ ] **Step 4: Commit generated**
```bash
git add "04. System/Data/SMITE/Analysis/" viewer/public/index.json
git commit -m "chore(smite): regenerate with validation report, tag audit, item meta"
```

---

## Self-Review

**Spec coverage:** #2 validation — helpers (A1), report + recommend wiring (A2), regen (D1). #3 labels — per-item meta in index (B1), label reframe + type (B2), shop badge + help note (B3). #6 — tag audit (C1), refresh_and_deploy + documented cron, no auto-install (C2). All spec sections mapped; freshness ships as script + doc per the confirmed decision.

**Placeholder scan:** none — full code per step. `refresh_and_deploy` is orchestration verified by the live run in D1 (integration), appropriate for a subprocess/git script; the "confirm real symbols" lines are verification instructions, not placeholders.

**Type/name consistency:** `coverage/win_weighted_coverage/spearman` (A1) → used by `god_metrics/aggregate` (A2). `validate.compute/write_report` (A2) called in recommend --all (A2 step 4) and D1. `build_index` per-item `meta {win_avg,gods}` (B1) → `Item.meta` type (B2) → `MetaBadge` in shop (B3). `EFFICIENCY` label text change (B2) reflected in ItemsShop tests (B3). `tag_audit/write_tag_audit` (C1) called from `validate.main` (C1). `refresh_and_deploy` chains `refresh.refresh_all`/`recommend.main`/`build_index.write_index`/`validate.main` (C2). No dangling names.

**Safety:** read-only analysis (reports) + additive index field + label text — no scoring-model change; `refresh_and_deploy` stages only the generated-data paths (never `git add -A`) and is opt-in (no cron auto-installed); `_archive/` untouched; real typecheck via `npm run build` in B3/D1.
