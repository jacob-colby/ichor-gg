"""Parser for smitebrain.com god build pages — aggregate pick/win rate per
item and per aspect, from ranked-match data. No bot protection on this site
(confirmed with a plain curl fetch during planning) — use cache.py, not
browser_fetch.py, to reach it."""
import re

from bs4 import BeautifulSoup

PICK_WIN_RE = re.compile(r"(\d+)%\s*pick.*?(\d+)%\s*win", re.DOTALL)


def parse_build_page(html: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    items, aspects = [], []

    for img in soup.find_all("img", alt=True):
        name = img["alt"].strip()
        if not name:
            continue
        stat_div = _find_pick_win_div(img)
        if stat_div is None:
            continue
        m = PICK_WIN_RE.search(stat_div.get_text())
        if not m:
            continue
        entry = {"name": name, "pick_rate": int(m.group(1)) / 100, "win_rate": int(m.group(2)) / 100}
        (aspects if name.startswith("Aspect of") else items).append(entry)

    return {"items": items, "aspects": aspects}


def _find_pick_win_div(img_tag):
    container = img_tag.find_parent("div", class_="flex")
    if container is None:
        return None
    return container.find("div", class_="text-xs")
