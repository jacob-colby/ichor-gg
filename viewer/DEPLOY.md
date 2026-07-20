# Deploying the SMITE 2 build viewer

The viewer is a static site — no server needed for friends. Personal ("my")
builds live in each visitor's browser (localStorage). God management (add/remove)
is owner-only and works only in local dev (`npm run dev`), not in the hosted
build.

## Host it (recommended: Vercel or Cloudflare Pages)

1. Push this repo to GitHub.
2. New project → import the repo. Set:
   - **Root directory:** `viewer`
   - **Build command:** `npm run build`
   - **Output directory:** `dist`
3. Deploy. You get a URL to share. Pushing to the repo auto-redeploys.

## One-off (no account)

```
cd viewer && npm run build
```
then drag the `viewer/dist/` folder onto https://app.netlify.com/drop .

## Updating data on a patch

From `tools/`:

```
python -m smite.refresh --all      # re-scrape gods/items/builds
python -m smite.recommend --all    # recompute suggested builds
python -m smite.build_index        # rewrite viewer/public/index.json
```

Commit + push → the host redeploys. Friends see the new data on reload.

## Keeping data fresh automatically (optional)

`python -m smite.refresh_and_deploy` (run from the vault, in `tools/`) does the
whole patch update: re-scrape → recompute → rebuild `index.json` → write the
validation + tag-audit reports → commit the generated data → push (which
redeploys the host). Add `--no-push` to stage a commit without pushing.

To run it weekly, add a cron entry **on your canonical git device only** (the one
that owns vault auto-commits — see Vault Hygiene). Example (Mondays 06:00):

    0 6 * * 1  cd /path/to/obsidian-vault/tools && python -m smite.refresh_and_deploy >> /path/to/refresh.log 2>&1

Scraping needs Python + Playwright working on that device. Not installed by
default — enable it when you're confident the scrape runs headless there.

## Notes

- **My builds** are per-browser (localStorage). They aren't synced across devices
  or shared, and clearing site data clears them.
- **Adding a god** requires your local stack (Python + Playwright) — do it in
  `npm run dev`, then commit the regenerated `index.json` + notes and push.
  Friends can browse your pool and save their own builds, but can't add gods.
