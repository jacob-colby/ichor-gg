# SMITE 2 — God Portrait Icons

Small square god portrait icons as seen on the in-game god-select screen and
scoreboard. These are the authoritative assets for note embeds — prefer these
over any full splash-art images.

## Target spec
- Format: PNG
- Size: 64×64 px (god-select native) — vault render size `|32`
- Max file size: **< 50 KB** each
- Naming: kebab-case slug matching the god's name (e.g. `chiron.png`, `hou-yi.png`)

## Two-step workflow

### Step 1 — generate placeholder stubs (any machine, no internet)
```bash
cd "04. System/Data/SMITE/_assets/icons/"
python3 generate-placeholders.py
```
Creates 31 solid-color PNG stubs (~150 bytes each, well within 50 KB spec).
Colors encode god role (Hunter=green, Mage=blue, Warrior=orange,
Guardian=purple, Assassin=red). Obsidian icon embeds render immediately.
Skips files that already exist and are >200 bytes — real icons are never overwritten.

### Step 2 — replace with real icons (internet-connected machine)
```bash
cd "04. System/Data/SMITE/_assets/icons/"
python3 fetch-gods.py
# or with Hi-Rez API credentials:
SMITE_DEV_ID=<id> SMITE_AUTH_KEY=<key> python3 fetch-gods.py
```
Expected: 31 PNG files, each 10–40 KB, all within the 50 KB spec.
Priority pool gods (★) are processed first.

## Source — SMITE 2 / Hi-Rez CDN (recommended)

The Hi-Rez / SMITE 2 community API is the cleanest automated source:

### Option A — Official Hi-Rez API (gods endpoint)
```
# 1. Fetch the god list (no auth key needed for the public JSON):
https://api.smitegame.com/smiteapi.svc/GetGodsJson/1/<dev_id>/<sig>/<timestamp>

# Each god entry includes:
entry["godIcon_URL"]    →  direct PNG, typically 64×64 or 128×128, ~10–40 KB
entry["godCard_URL"]    →  full splash art (skip — too large)
```

Hi-Rez public dev ID + key available at https://smitegame.com/api-terms-of-use/
(free registration). The SMITE 1 API exposes the same gods as SMITE 2 (same
roster).

### Option B — Smite.fandom.com infobox portrait (manual browser grab)
The automated fetch is Cloudflare-blocked. In a browser:
1. Open `https://smite.fandom.com/wiki/<GodName>` (e.g. `Chiron`, `Hou_Yi`, `Ullr`)
2. Right-click the infobox portrait → Save image as → rename to `<slug>.png`
3. Resize to 64×64 if needed (macOS Preview / Windows Paint / ImageMagick)

### Option C — SmiteSource / SmiteGuru God Icons
Both community sites serve small god icons:
```
https://www.smitesource.com/images/gods/<GodName>_icon.png
# e.g. https://www.smitesource.com/images/gods/Chiron_icon.png
```
Not guaranteed stable — verify before scripting.

### Download script
See `03. Workspaces/Gaming/_assets/_download.py` → `run_batch("SMITE 2 god
icons …")` which targets this directory using the smitesource.com icon URL
pattern (or Hi-Rez API if you have credentials). Run it on the mini PC where
those domains are reachable.

---

## Jacob's pool (priority backfill)
- [ ] chiron.png
- [ ] ullr.png
- [ ] hou-yi.png

## Hunters (contextual — referenced in matchup notes)
- [ ] neith.png
- [ ] apollo.png
- [ ] cupid.png
- [ ] jing-wei.png
- [ ] izanami.png
- [ ] artemis.png

## Broader meta (optional — fill if you want full roster coverage)
- [ ] hercules.png
- [ ] thor.png
- [ ] loki.png
- [ ] anubis.png
- [ ] athena.png
- [ ] ares.png
- [ ] ymir.png
- [ ] ra.png
- [ ] agni.png
- [ ] hades.png
- [ ] medusa.png
- [ ] poseidon.png
- [ ] fenrir.png
- [ ] sobek.png
- [ ] kukulkan.png
- [ ] zeus.png
- [ ] bellona.png
- [ ] ah-puch.png
- [ ] bastet.png
- [ ] nemesis.png
- [ ] susano.png
- [ ] merlin.png

## Size note
The splash-art / card images from `godCard_URL` are 300–800 KB — over spec.
Use `godIcon_URL` (god-select portrait, 64×64) or the SmiteSource `_icon.png`
variant. Both typically come in at **10–40 KB** — within the 50 KB spec.
Do **not** copy from `../gods/` (full splash art).
