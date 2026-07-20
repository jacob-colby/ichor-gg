# SMITE 2: validation harness, honest efficiency labels, data freshness

Status: approved, ready for implementation plan
Date: 2026-07-19

## Problem

Three of the recommender's biggest weaknesses, addressed:
2. **No validation loop** — nothing checks whether suggested builds match what wins.
3. **Efficiency labels mislead** — "Underrated/Overrated" read as power, but they're
   gold-value; the shop makes this prominent.
6. **Data is stale/fragile** — no automated freshness; effect-tag errors are silent.

## Design

### Part A — Validation harness (weakness 2)

`tools/smite/validate.py` scores every buildable item per god (reusing
`scoring.score_god_items`) and compares our ranking to SmiteBrain's per-item
**win rates** from the Conquest community build (the only mode with meta data).
Per god, over the community items that are also in our scored pool:

- **Coverage** = |our suggested `core` ∩ community items| / |community items| —
  did we recommend what the community runs?
- **Win-weighted coverage** = Σ(win_rate of community items we include) /
  Σ(win_rate of all community items) — did we include the *high-win* ones? (a
  68%-win item we miss hurts more than a 51% one).
- **Rank agreement** = Spearman correlation between our `total` score and the
  community `win_rate` over the shared items. Per-god n≈6 is noisy, so the report
  emphasizes the **pooled** correlation across all god-item pairs (~60 points).

Output: `04. System/Data/SMITE/Analysis/_validation.md` — a per-god table
(coverage / win-weighted / local corr) plus an aggregate line (mean coverage,
mean win-weighted, pooled Spearman). Run standalone (`python -m smite.validate`)
and also invoked at the end of `recommend --all` so it refreshes automatically.
Spearman via a small self-contained rank-correlation helper (no new dependency).

This is the falsifiable dashboard the system lacks: every future tuning change is
judged by "did these numbers go up?" **Honest limit:** win rate is itself
popularity-biased, so agreement is a strong proxy, not truth — the report says so.

### Part B — Honest efficiency labels + meta signal (weakness 3)

- **Reframe** the shop badge labels from Underrated/Fair/Overrated to
  **Efficient / Fair / Premium** (keys unchanged: `undervalued`→Efficient,
  `fair`→Fair, `premium`→Premium, `null`→—). Add a one-line help note in the
  shop: *"Rates stats-per-gold, not power — Premium items are often worth
  overpaying for their passive."* The filter dropdown uses the same new labels.
- **Meta badge:** `build_index` computes, per item, an aggregate from the
  community builds — `meta: {win_avg, gods}` = average per-item `win_rate` and the
  count of gods whose community build includes it. The shop card and item detail
  show it as e.g. **"55% avg · 4 gods"** when present. This surfaces the actual
  meta signal next to the (now correctly-scoped) stat-value badge, so "Premium
  stats · 55% avg win" reads correctly instead of "premium = bad".
- Types: `Item` gains `meta?: { win_avg: number; gods: number }`.

### Part C — Tag audit + data freshness (weakness 6)

**Tag audit** (`tools/smite/validate.py`, same module): a keyword scan of each
item's `passive` text against a small tag→keyword map (anti-heal, sustain, aura,
cc-immunity, mobility, protection-shred, wave-clear, anti-crit). Flags two cases:
- **tag without evidence** — item is tagged X but no X-keyword in its passive;
- **possible missing tag** — an X-keyword is present but the item isn't tagged X.

Conservative (only the tags with reliable keywords), written to
`Analysis/_tag_audit.md` as a review list — never auto-applied (tags stay
hand-curated in `_tags.yaml`). Directly surfaces silent errors like the Contagion
anti-heal miss.

**Freshness** — a single orchestration script `tools/smite/refresh_and_deploy.py`
(or a `.bat`) that runs, in order: `refresh --all` → `recommend --all` →
`build_index` → narrow commit (only the generated data paths, via
`recap_common.git_pull_commit_push` per vault hygiene — never `git add -A`) →
push (which triggers the host redeploy). Idempotent; prints a summary.

> **Decision to confirm:** I will **not** auto-install a cron entry. Scraping is
> Cloudflare-gated Playwright and the mini-PC's headless reliability is unverified,
> and standing scheduled config needs your explicit go-ahead + the right device
> and git identity (per CLAUDE.md's one-canonical-device rule). Deliverable: the
> script + a documented crontab line in `viewer/DEPLOY.md` you enable when ready.
> If you'd rather I wire the cron directly, tell me which device + identity.

## Data flow

`recommend --all` → suggested builds → `validate.py` reads community win/pick +
our scores → `_validation.md` + `_tag_audit.md`. `build_index` folds per-item
`meta` (avg win / god count) into `index.json` → shop shows meta badge +
reframed stat-value label. `refresh_and_deploy` chains the whole pipeline for a
one-command patch update.

## Testing

- **Python**: validation metrics on a synthetic god (coverage, win-weighted
  coverage, and the rank-correlation helper against a known-ordering fixture);
  tag audit flags a tagged-but-no-keyword item and a keyword-but-untagged item;
  `build_index` emits `meta` with correct `win_avg`/`gods` for an item across two
  community builds.
- **Viewer (vitest/RTL)**: the efficiency labels render as Efficient/Fair/Premium;
  a card with `meta` shows the "% avg · N gods" badge, one without doesn't.
- **Manual/integration**: run `validate` on the real pool, eyeball `_validation.md`
  (per-god coverage + aggregate) and `_tag_audit.md` (review list); shop shows the
  new labels + meta badges; `npm run build` passes; static preview unaffected.

## Limitations / non-goals

- Validation agreement uses SmiteBrain win rate (single source, popularity-biased,
  Conquest-only) — a proxy, stated in the report; Joust has no meta to validate
  against.
- Tag audit is keyword-heuristic — it surfaces candidates, doesn't judge; terse
  passives will miss some.
- Freshness ships as a script + documented cron line, not an auto-installed job
  (pending the device/identity decision above).
- No changes to the scoring model itself here (that's weaknesses 1/4/5, later).

## Open questions — resolved during design

- Validation metric → coverage + win-weighted coverage + pooled Spearman vs
  community win rate (Conquest only).
- Meta on the global shop → per-item average community win% + god count (win rate
  is per-god, so an average is the honest global signal).
- Freshness → orchestration script + documented cron; auto-install pending your
  device/identity confirmation.
