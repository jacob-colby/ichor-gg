# SMITE 2 viewer: manage gods + share-ready (localStorage builds + hosting)

Status: draft — awaiting user approval
Date: 2026-07-19

## Problem

Two coupled goals:
1. **Add/remove gods** from the tracked pool without hand-running the pipeline —
   an owner operation (scraping is Cloudflare-gated Playwright), made easy in-app.
2. **Share with friends.** The viewer is a static Vite app, but two things are
   local-only: the build editor (write endpoint shells Python on localhost) and
   god management (Python + Playwright). To share, the *personal* layer (a
   friend's own "my" builds) must work with **no backend**.

Decided: host the static site (Vercel/Cloudflare Pages) and move **my builds to
browser localStorage** so every visitor can save their own with no server; god
management stays an owner-only local operation, hidden when hosted.

## Design

### Part A — `mine` builds move to localStorage (share-ready core)

Today `mine` builds live in vault notes and reach the viewer through `index.json`
(written by the Python `/api/build` endpoint). There are **no** mine builds today,
so there is nothing to migrate. Going forward, mine builds live **only** in the
browser.

- **`viewer/src/lib/mineStore.ts`** — a tiny localStorage store under key
  `smite:mine-builds` holding `{ "<god>||<mode>": MineBuild[] }`, where
  `MineBuild = {name, slot_order, starter?, notes?}`. API: `getMine(god, mode)`,
  `saveMine(god, mode, build)` (add/replace by name), `deleteMine(god, mode, name)`,
  and a `subscribe(fn)` (or a bumping `useMineBuilds(god, mode)` hook) so the UI
  re-renders on change. All pure; unit-testable with a jsdom localStorage.
- **DetailPanel** merges the store's mine builds for the current god+mode into the
  displayed entries (as `source:"mine"` tabs) alongside the static community +
  suggested entries from `index.json`. Suggested/community are unchanged.
- **BuildEditor** saves/deletes via `mineStore` (synchronous — no fetch, no
  `/api/build`, no page reload). On save it calls a store update; the panel
  re-renders and selects the new tab (the existing `pendingSelect` flow, now
  keyed off the store rather than a re-fetch). The `POST /api/build` path and the
  Vite editor endpoint are **retired from the viewer** (the Python `save_build`
  CLI is left in the repo, unused by the app).
- Net effect: the whole app is static — mine builds work identically local or
  hosted, and the earlier "Vite full-reload drops the god on save" class of bugs
  disappears (no file writes on save).

### Part B — owner add/remove gods (local dev only)

- **`tools/smite/manage_gods.py`** CLI, args-based, validated:
  - `add "<God Name>"` → scrape the god (`refresh_god`) + its Conquest community
    build (`refresh_builds`) + icons, then `recommend --all` + `build_index`.
    Rejects a name that fails to scrape (no partial pool entry).
  - `remove "<God Name>"` → **move** (never delete) `Gods/<god>.md` →
    `Gods/_removed/<god>.md` and `Builds/<god>-*.md` → `Builds/_removed/`, then
    `build_index`. The `*.md` glob is non-recursive, so `_removed/` drops out of
    the pool. Reversible by moving the files back.
  - Validates the name and that `remove` targets an existing tracked god.
- **`viewer/vite.config.ts`** gains a `POST /api/gods` middleware (mirrors the
  existing pattern): body `{action, name}` → spawn `python -m smite.manage_gods
  <action> "<name>"` (fixed argv, no shell), returns `{ok}`/`{ok:false,error}`.
  Localhost/dev only. (The `/api/build` endpoint is removed since Part A retires
  it; `/api/gods` replaces it.)
- **Viewer "Manage gods" UI**, shown **only in dev** (`import.meta.env.DEV`):
  an "＋ Add god" control at the foot of the rail (text input → POST add →
  `reload()` the index on success, with a "scraping…" busy state, since a scrape
  takes ~30–90s), and a small remove affordance per god (confirm → POST remove →
  reload). Hidden entirely in a production build, so friends never see it and it
  can't call a backend that isn't there.

### Part C — hosting readiness

- **Dev-gating:** anything backend-dependent (Manage gods) is behind
  `import.meta.env.DEV`. Everything else (browse, flavors, aspects, mine builds
  via localStorage) works in the static build.
- **Attribution footer:** a small footer crediting wiki.smite2.com + SmiteBrain
  as data sources (polite + honest for a shared tool).
- **Deploy doc:** `viewer/DEPLOY.md` — connect the repo to Vercel/Cloudflare
  Pages (root `viewer/`, build `npm run build`, output `dist/`); on a patch,
  run the local refresh + `build_index`, commit, push → auto-redeploy. Also the
  one-off `npm run build` → Netlify-drop path.
- **Out of scope here (flagged as follow-ups):** a first-run legend explaining
  suggested/community/flavors/aspects/heuristics, and a mobile-responsive pass —
  both worthwhile before a wide share, but separable from this cycle.

## Data flow

- **Mine builds:** BuildEditor → `mineStore` (localStorage) → DetailPanel merges
  into displayed tabs. No network.
- **Add/remove gods (dev):** Manage-gods UI → `POST /api/gods` → `manage_gods`
  (scrape/move + `recommend`/`build_index`) → viewer `reload()` re-fetches
  `index.json`. Owner then commits + pushes → host redeploys for friends.

## Testing

- **Python:** `manage_gods remove` moves the god + build notes into `_removed/`
  and leaves the pool without it (add is integration-verified live, since it
  scrapes). Name validation rejects a non-tracked god on remove.
- **Viewer (vitest/RTL):** `mineStore` add/replace-by-name/delete round-trips
  against a mocked localStorage; DetailPanel shows a localStorage mine build as a
  tab and the editor writes to the store (no fetch); the Manage-gods UI is absent
  when `import.meta.env.DEV` is false.
- **Manual/integration:** in dev, add a real new god (scrapes, appears in the
  rail with builds), remove it (drops from the rail, files moved to `_removed/`);
  save a mine build, reload the page, confirm it persists (localStorage);
  `npm run build` and preview the static `dist/` — confirm no Manage-gods UI and
  mine builds still work.

## Limitations / non-goals

- Adding gods requires the owner's local stack (Python + Playwright); friends
  can't add gods — they browse the owner's pool + save their own builds locally.
- Mine builds are per-browser (localStorage) — not synced across devices or
  shared; clearing site data loses them. Acceptable for a personal build tool.
- Scraping is Cloudflare-gated and can fail transiently; `add` surfaces the error
  and makes no partial pool entry.
- First-run legend + mobile pass are follow-ups, not in this cycle.

## Open questions — resolved during design

- Pinned list meaning → add/remove brand-new gods (owner, local), made easy in-app.
- Share model → static host + localStorage mine builds (no backend for friends).
- Mine builds persistence → localStorage only (no vault dual-write); nothing to
  migrate (no mine builds exist today).
