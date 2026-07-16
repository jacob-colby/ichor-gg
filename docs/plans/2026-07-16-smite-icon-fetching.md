# SMITE Icon Fetching Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the dead SmiteSource/Fandom icon-download scaffolding with real portrait/icon fetching folded directly into `refresh_god`/`refresh_item` — extract the image URL from the wiki page already scraped, download via plain `requests` (confirmed ungated), one source of truth.

**Architecture:** Add a small `_extract_image_url` helper to `tools/smite/wiki_parser.py` (both `parse_god_page` and `parse_item_page` call it), add a binary-download helper to `tools/smite/refresh.py` that `refresh_god`/`refresh_item` call after a successful scrape, and delete the now-dead `04. System/Data/SMITE/_assets/icons/{fetch-gods.py,fetch-items.py,generate-placeholders.py,README.md}` scaffolding.

**Tech Stack:** Python, `requests`, `beautifulsoup4` — all already in use, no new dependencies.

**Reference:** [docs/superpowers/specs/2026-07-16-smite-reference-system-design.md](../specs/2026-07-16-smite-reference-system-design.md) — "Assets" section, updated 2026-07-16 with this corrected approach.

---

## Before you start: what's already confirmed true

- `wiki.smite2.com`'s HTML pages are Cloudflare-gated (need Playwright — see `browser_fetch.py`), but its static image files under `/images/...` are **not** gated: `curl -sL -o /dev/null -w "%{http_code}" "https://wiki.smite2.com/images/T3_Deathbringer.png?6d7a6"` returns `200`, confirmed live during planning.
- Both god pages and item pages share the exact same infobox pattern: the first row is the title (`<th colspan="2" class="title">`), the second row is a centered image cell: `<tr><td colspan="2" style="text-align: center;"><span typeof="mw:File"><a ...><img src="/images/..." ...></a></span></td></tr>`. Confirmed on both `https://wiki.smite2.com/w/Chiron` (portrait) and `https://wiki.smite2.com/w/Deathbringer` (icon) via live Playwright fetches during planning.
- The old `fetch-gods.py` (SmiteSource `_icon.png` URLs) now 404s — SmiteSource was redesigned to a Next.js site. `smite.fandom.com` returns 403 (Cloudflare-blocked), matching that script's own README caveat. Both are dead ends; don't try to resurrect them.

---

## Task 1: Extract the portrait/icon image URL in `wiki_parser.py`

**Files:**
- Modify: `tools/smite/wiki_parser.py`
- Modify: `tools/smite/tests/fixtures/chiron_wiki.html`
- Modify: `tools/smite/tests/fixtures/deathbringer_wiki.html`
- Modify: `tools/smite/tests/test_wiki_parser.py`

- [ ] **Step 1: Restore the portrait/icon image row into both fixtures** (this row was stripped in Tasks 4/5 since nothing read it then — real markup, captured from the live pages during planning)

Insert this row into `chiron_wiki.html`, immediately after the `<th colspan="2" class="title">...Chiron...</th></tr>` row and before the `<tr><th colspan="2" class="header"><span ...>Summary</span></th></tr>` row:
```html
<tr>
<td colspan="2" style="text-align: center;"><span typeof="mw:File"><a href="/w/File:T_Chiron(S2)_Default.png" class="mw-file-description"><img src="/images/thumb/T_Chiron%28S2%29_Default.png/280px-T_Chiron%28S2%29_Default.png?157c1" decoding="async" loading="lazy" width="280" height="420" class="mw-file-element"></a></span>
</td></tr>
```

Insert this row into `deathbringer_wiki.html`, immediately after the `<th colspan="2" class="title">...Deathbringer...</th></tr>` row and before the `<tr><th colspan="2" class="header"><span ...>Details</span></th></tr>` row:
```html
<tr>
<td colspan="2" style="text-align: center;"><span typeof="mw:File"><a href="/w/File:T3_Deathbringer.png" class="mw-file-description"><img src="/images/T3_Deathbringer.png?6d7a6" decoding="async" loading="lazy" width="128" height="128" class="mw-file-element"></a></span>
</td></tr>
```

- [ ] **Step 2: Add the failing tests**

```python
# append to tools/smite/tests/test_wiki_parser.py

def test_parse_god_page_extracts_image_url():
    result = wiki_parser.parse_god_page(_chiron_html())
    assert result["image_url"] == "/images/thumb/T_Chiron%28S2%29_Default.png/280px-T_Chiron%28S2%29_Default.png?157c1"


def test_parse_item_page_extracts_image_url():
    result = wiki_parser.parse_item_page(_deathbringer_html())
    assert result["image_url"] == "/images/T3_Deathbringer.png?6d7a6"
```

- [ ] **Step 3: Run test to verify it fails**

Run: `cd tools && python -m pytest smite/tests/test_wiki_parser.py -v -k image_url`
Expected: FAIL with `KeyError: 'image_url'`

- [ ] **Step 4: Add the implementation** — one shared helper, called from both `parse_god_page` and `parse_item_page`

```python
# append to tools/smite/wiki_parser.py, near the other private helpers

def _extract_image_url(infobox):
    """The infobox's first centered <td colspan="2"> row (right after the
    title row) holds the portrait/icon image on both god and item pages —
    confirmed identical structure on both page types during planning."""
    for row in infobox.find_all("tr"):
        td = row.find("td", attrs={"colspan": "2"})
        if td is None:
            continue
        style = td.get("style", "")
        if "text-align: center" not in style:
            continue
        img = td.find("img")
        if img is not None and img.get("src"):
            return img["src"]
    return None
```

Add one line to `parse_god_page` (right after `infobox = soup.find(...)` null-check, anywhere before `return result`):
```python
    result["image_url"] = _extract_image_url(infobox)
```

Add the same line to `parse_item_page`:
```python
    result["image_url"] = _extract_image_url(infobox)
```

- [ ] **Step 5: Run test to verify it passes**

Run: `cd tools && python -m pytest smite/tests/test_wiki_parser.py -v`
Expected: 11 passed (9 existing + 2 new)

- [ ] **Step 6: Commit**

```bash
git add tools/smite/wiki_parser.py tools/smite/tests/fixtures/chiron_wiki.html tools/smite/tests/fixtures/deathbringer_wiki.html tools/smite/tests/test_wiki_parser.py
git commit -m "feat(smite): extract portrait/icon image URL from god and item wiki pages"
```

---

## Task 2: Download the icon in `refresh_god`/`refresh_item`, remove the dead scripts

**Files:**
- Modify: `tools/smite/refresh.py`
- Modify: `tools/smite/tests/test_refresh.py`
- Delete: `04. System/Data/SMITE/_assets/icons/fetch-gods.py`
- Delete: `04. System/Data/SMITE/_assets/icons/fetch-items.py`
- Delete: `04. System/Data/SMITE/_assets/icons/generate-placeholders.py`
- Delete: `04. System/Data/SMITE/_assets/icons/README.md`

- [ ] **Step 1: Write the failing tests**

```python
# append to tools/smite/tests/test_refresh.py

def test_refresh_god_downloads_icon(tmp_path, monkeypatch):
    monkeypatch.setattr(refresh, "DATA_ROOT", tmp_path)
    fetcher = Mock()
    fetcher.fetch.return_value = (FIXTURES / "chiron_wiki.html").read_text(encoding="utf-8")

    with mock.patch("smite.refresh.requests.get") as mock_get:
        mock_get.return_value = Mock(content=b"\x89PNG\r\n\x1a\nfakepngdata", status_code=200)
        mock_get.return_value.raise_for_status = Mock()
        refresh.refresh_god("Chiron", fetcher)

    icon_path = tmp_path / "_assets" / "icons" / "chiron.png"
    assert icon_path.exists()
    assert icon_path.read_bytes() == b"\x89PNG\r\n\x1a\nfakepngdata"
    mock_get.assert_called_once_with(
        "https://wiki.smite2.com/images/thumb/T_Chiron%28S2%29_Default.png/280px-T_Chiron%28S2%29_Default.png?157c1",
        timeout=20,
    )


def test_refresh_god_skips_icon_download_if_already_present(tmp_path, monkeypatch):
    monkeypatch.setattr(refresh, "DATA_ROOT", tmp_path)
    icon_path = tmp_path / "_assets" / "icons" / "chiron.png"
    icon_path.parent.mkdir(parents=True)
    icon_path.write_bytes(b"\x89PNG\r\n\x1a\n" + b"x" * 2000)

    fetcher = Mock()
    fetcher.fetch.return_value = (FIXTURES / "chiron_wiki.html").read_text(encoding="utf-8")

    with mock.patch("smite.refresh.requests.get") as mock_get:
        refresh.refresh_god("Chiron", fetcher)

    mock_get.assert_not_called()


def test_refresh_item_downloads_icon(tmp_path, monkeypatch):
    monkeypatch.setattr(refresh, "DATA_ROOT", tmp_path)
    fetcher = Mock()
    fetcher.fetch.return_value = (FIXTURES / "deathbringer_wiki.html").read_text(encoding="utf-8")

    with mock.patch("smite.refresh.requests.get") as mock_get:
        mock_get.return_value = Mock(content=b"\x89PNG\r\n\x1a\nfakepngdata", status_code=200)
        mock_get.return_value.raise_for_status = Mock()
        refresh.refresh_item("Deathbringer", fetcher)

    icon_path = tmp_path / "_assets" / "icons" / "deathbringer.png"
    assert icon_path.exists()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd tools && python -m pytest smite/tests/test_refresh.py -v -k icon`
Expected: FAIL — `_assets/icons/chiron.png` doesn't get created (no such code path exists yet)

- [ ] **Step 3: Write the implementation**

Add `import requests` to `refresh.py`'s imports (it doesn't currently import `requests` directly — only via `cache.py`). Add this helper function, and call it from `refresh_god` and `refresh_item` right after their existing `notes.merge_*_note(...)` call:

```python
# add near the top of tools/smite/refresh.py, with the other imports
import requests
```

```python
# add as a new function in tools/smite/refresh.py

def _download_icon(image_url: str, slug: str) -> None:
    """Download a god/item portrait/icon from wiki.smite2.com. The HTML
    pages are Cloudflare-gated (hence Playwright elsewhere in this module)
    but the static image files are not — confirmed with a plain requests
    fetch during planning — so this uses requests directly, no browser
    needed. Skips if already downloaded (>1000 bytes), same convention as
    the vault's other Gaming asset-download scripts."""
    if not image_url:
        return
    icons_dir = DATA_ROOT / "_assets" / "icons"
    out_path = icons_dir / f"{slug}.png"
    if out_path.exists() and out_path.stat().st_size > 1000:
        return

    full_url = "https://wiki.smite2.com" + image_url
    response = requests.get(full_url, timeout=20)
    response.raise_for_status()

    icons_dir.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(response.content)
```

In `refresh_god`, after the existing `notes.merge_god_note(...)` call, add:
```python
    _download_icon(parsed.get("image_url"), name.lower().replace(" ", "-").replace("'", ""))
```

In `refresh_item`, after the existing `notes.merge_item_note(...)` call, add the same line (same slug convention as the rest of the codebase).

- [ ] **Step 4: Run test to verify it passes**

Run: `cd tools && python -m pytest smite/tests/test_refresh.py -v`
Expected: all passing (previous count + 3 new)

- [ ] **Step 5: Remove the dead scaffolding**

```bash
git rm "04. System/Data/SMITE/_assets/icons/fetch-gods.py" "04. System/Data/SMITE/_assets/icons/fetch-items.py" "04. System/Data/SMITE/_assets/icons/generate-placeholders.py" "04. System/Data/SMITE/_assets/icons/README.md"
```

- [ ] **Step 6: Run the full suite**

Run: `cd tools && python -m pytest smite/tests/ -v -m "not live"`
Expected: all passing

- [ ] **Step 7: Commit**

```bash
git add tools/smite/refresh.py tools/smite/tests/test_refresh.py
git commit -m "feat(smite): download real portrait/icon via wiki.smite2.com, remove dead SmiteSource scaffolding"
```

---

## Task 3: Real end-to-end run — fetch the actual Chiron/Deathbringer icons

- [ ] **Step 1: Re-run the live refresh to pull real icon files**

```bash
cd tools && python -m smite.refresh --refresh Chiron --kind god --force
cd tools && python -m smite.refresh --refresh Deathbringer --kind item --force
```
Expected: two success messages, and real PNG files now exist at
`04. System/Data/SMITE/_assets/icons/chiron.png` and `.../deathbringer.png`.

- [ ] **Step 2: Verify the downloaded files are real, valid images**

Read the first bytes of each file and confirm a PNG header (`\x89PNG`), and check file size is reasonable (a few KB to ~50KB, not 0 bytes and not an HTML error page saved with a `.png` extension).

- [ ] **Step 3: Final commit**

```bash
git add "04. System/Data/SMITE/_assets/icons/chiron.png" "04. System/Data/SMITE/_assets/icons/deathbringer.png"
git commit -m "chore(smite): fetch real Chiron portrait and Deathbringer icon"
```
