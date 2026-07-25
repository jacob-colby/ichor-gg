# ichor

A build recommender for **SMITE 2** that scores items with math instead of
copying the meta — then adapts the build to the match you're actually in.

Most build sites tell you what's popular. This one fits a gold-value model to
every item's stats, works out which items are *underpriced for a given god*, and
blends that with win rate, pick rate, and how well an item fits the god's kit.
When the two disagree, it says so.

## What it does

- **Suggested builds** for all 87 tracked gods, per mode (Conquest / Joust) and
  per flavor (core, burst, bruiser, anti-tank…), each with a starter, flex
  slots, and situational swaps.
- **Draft-aware builds** — enter the 4 allies and 5 enemies and the core
  re-ranks live: enemy healers raise anti-heal, a magic-heavy comp raises magical
  protection, and a job a teammate already covers gets deprioritized.
- **Why this item** — every suggestion breaks down into its four signals
  (efficiency, win, pick, fit), so you can disagree with it on the evidence.
- **Tier lists** for gods and items, rankable by *our* score or by community
  win rate — deliberately shown side by side, because they often disagree.
- **Patch notes** — item stat/cost diffs between data refreshes, classified
  buff / nerf / mixed (cost direction inverted, since cheaper is better).
- **Items shop** with an efficiency rating per item: undervalued / fair / premium.

## How the scoring works

1. **Gold value** — a non-negative least-squares fit of item cost onto item
   stats gives a marginal gold price per stat. An item's *efficiency* is the
   residual: what it costs minus what its stats should cost. Cheaper than the
   model predicts → undervalued.
2. **Fit** — role/lane stat maps blended with the god's parsed ability scaling,
   so a stat that a god's kit actually scales with counts for more.
3. **Meta** — high-elo win rate and pick rate from community data.
4. **Blend** — weighted sum (currently efficiency .35 / win .45 / pick .05 /
   fit .15), tuned by grid search against the community win-rate ranking.

Starters sit out the gold-value regression: their price buys a passive, not
their stats, so including them poisons the fit.

All the tuning lives in [`data/_weights.yaml`](data/_weights.yaml) — signal
weights, role stat maps, flavors, lifesteal caps, and the draft overlay.

## Layout

```
pipeline/smite/    Python: scrape -> parse -> score -> assemble -> index
data/              Scraped god/item notes, generated builds, tuning config, icons
viewer/            Vite + React + TypeScript viewer (the site)
docs/              Design specs and implementation plans
```

## Running it

```bash
# viewer (icons are mirrored from data/ automatically)
cd viewer && npm install && npm run dev
```

```bash
# full data refresh: scrape -> recompute -> reindex -> reports -> commit
cd pipeline && python -m smite.refresh_and_deploy
```

Individual stages, from `pipeline/`:

```bash
python -m smite.refresh --all        # re-scrape gods, items, community builds
python -m smite.recommend --all      # recompute suggested builds
python -m smite.build_index          # rewrite viewer/public/index.json
python -m smite.data_audit           # integrity gate (exits non-zero on findings)
python -m smite.validate --check     # quality gate vs community win rates
```

Scraping needs Playwright (`python -m playwright install chromium`); the viewer
needs Node 20+.

## Tests

```bash
cd pipeline && python -m pytest smite/tests -q -m "not live"   # 259
cd viewer && npm test                                           # 133
```

## Honest limitations

- **87 of 89 gods.** Cu Chulainn and Ix Chel have empty wiki pages — there's
  nothing to scrape. They're in the roster and get picked up automatically if
  that changes.
- **Community coverage is partial.** 18 gods and 104 items have no community
  signal; they're shown as *unranked* rather than given an invented tier.
- **Agreement with the meta is modest by design.** The recommender surfaces
  underrated items, so it deliberately diverges from popularity. Current
  validation: win-weighted 0.47, rank correlation 0.36 across 411 pairs.
- **Patch notes need history.** Diffs only exist between data refreshes, so the
  page starts empty and fills in from the first snapshot onward.
- **Threat detection uses wiki tags.** A god who is situationally a healer
  without the `Healing` label won't be counted.

## Credits

Data from [wiki.smite2.com](https://wiki.smite2.com) and
[SmiteBrain](https://smitebrain.com). Suggested builds are heuristic, not
official.

A fan project. Not affiliated with or endorsed by Hi-Rez Studios. SMITE is a
trademark of Hi-Rez Studios, Inc.

## License

Code is MIT (see [LICENSE](LICENSE)). Game data and images belong to Hi-Rez
Studios and are included here for reference under fair use.
