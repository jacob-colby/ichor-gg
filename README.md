# ichor

A build recommender for **SMITE 2** that shows its working — what every item
costs against what its stats are worth, what this god's players actually buy
instead, and how the build changes for the match you're in.

Most build sites hand you six icons. This one fits a gold-value model to every
item's stats, works out which are underpriced for a given god's kit, blends that
with community win and pick rates, and prints the reasoning next to the answer
so you can disagree with it on the evidence.

## What it does

- **Suggested builds** for all 87 tracked gods, per mode (Conquest / Joust /
  Arena) and per flavor (core, burst, bruiser, anti-tank, attack-speed,
  cooldown, strength, intelligence, hybrid…), each with a starter, flex slots
  and situational swaps.
- **Draft-aware builds** — enter the allies and enemies and the core re-ranks
  live: enemy healers raise anti-heal, a magic-heavy comp raises magical
  protection, and a job a teammate already covers gets deprioritized.
- **Why this item** — every suggestion breaks down into its four signals
  (efficiency, win, pick, fit), with the community's own rate for the same item
  beside it.
- **A tier list built from real match outcomes** — the Wilson lower bound on
  each god's wins over matches, so a 62% record over 133 games doesn't outrank a
  58% one over 2,000. Nothing this site models enters the order.
- **Items shop** with a value rating per item: what its stats are worth at the
  fitted per-stat gold prices, against what it costs.
- **Patch notes** — item stat/cost diffs between data refreshes, classified
  buff / nerf / mixed (cost direction inverted, since cheaper is better).

## How the scoring works

1. **Gold value** — a non-negative least-squares fit of item cost onto item
   stats gives a marginal gold price per stat. An item's *efficiency* is the
   residual: what it costs minus what its stats should cost.
2. **Fit** — role/lane stat maps blended with the god's parsed ability scaling,
   so a stat the god's kit actually scales with counts for more.
3. **Meta** — high-elo win rate and pick rate from community data.
4. **Blend** — weighted sum (efficiency .35 / win .45 / pick .05 / fit .15).

Tier-1 starters and statless items sit out the regression: a starter's price
buys a passive rather than its stats, and an item with no stats has no residual
worth computing. Relics and god-specific items are priced but can't take one of
the six core slots — the game doesn't work that way.

All tuning lives in [`data/_weights.yaml`](data/_weights.yaml).

## What the model can and can't do

Measured against a random-baseline control, not against its own inputs:

- It **finds** community-worthy items about **4.9× better than chance**.
- It does **not rank** within them — inside the community's own item set its
  ordering skill is indistinguishable from zero.

So "these builds contain sensible items" is supported; "these builds are in the
right order" is not yet. See [`docs/STATE.md`](docs/STATE.md) §1–2 for the
measurement, and why the obvious agreement metric can't be used to tune the
model.

## Layout

```
pipeline/smite/    Python: scrape -> parse -> score -> assemble -> index
data/              Scraped god/item notes, generated builds, tuning config, icons
viewer/            Vite + React + TypeScript viewer (the site)
docs/STATE.md      Living doc: current state, design decisions, what's left
docs/specs|plans/  Dated point-in-time design documents (never updated)
```

**If you're about to change the model, read [`docs/STATE.md`](docs/STATE.md)
first** — particularly §1 (the agreement metric grades its own input) and §4
(six things that were tried, measured, and shipped off).

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
python -m smite.refresh --all            # re-scrape gods, items, community builds
python -m smite.refresh --discover-items # items referenced but not tracked
python -m smite.recommend --all          # recompute suggested builds
python -m smite.build_index              # rewrite viewer/public/index.json
python -m smite.data_audit               # integrity gate (non-zero exit on findings)
python -m smite.validate --check         # regression floor (not a tuning target)
python -m smite.calibrate                # the leakage-free measure
python -m smite.calibrate_combat         # combat model vs in-game readings
```

Scraping needs Playwright (`python -m playwright install chromium`); the viewer
needs Node 20+.

## Tests

```bash
cd pipeline && python -m pytest smite/tests -q   # 489
cd viewer && npm test -- --run                    # 559
```

Use `npm run build` rather than `tsc --noEmit` — the latter misses errors the
project reference build catches.

## Honest limitations

- **87 of 89 gods.** Cu Chulainn and Ix Chel have empty wiki pages — there's
  nothing to scrape. They're in the roster and get picked up automatically if
  that changes.
- **Joust and Arena have no outcome data at all.** Their gods are shown
  unranked rather than given an invented tier — but their *builds* still ship,
  resting on the model alone. That's two thirds of the shipped builds.
- **The combat model is exact where it's been measured** (0.0% worst case over
  twelve in-game readings) and the penetration caps are the one constant that
  hasn't been.
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
