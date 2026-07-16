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

    # Anchor off the stat div and search downward for the image, rather than
    # walking up from the image. The stat div's class ("text-xs text-gray-400")
    # is specific enough that it never has its own wrapper problem, and it is
    # always a direct child of the tile container. Walking up from the <img>
    # instead is unsafe: a Tailwind icon-centering wrapper around the <img>
    # (e.g. <div class="flex items-center justify-center ...">) also matches
    # class_="flex", so find_parent from the image can land on that inner
    # wrapper instead of the true tile container, silently dropping the tile.
    for stat_div in soup.find_all("div", class_="text-xs"):
        container = stat_div.find_parent("div", class_="flex")
        if container is None:
            continue
        img = container.find("img", alt=True)
        if img is None:
            continue
        name = img["alt"].strip()
        if not name:
            continue
        m = PICK_WIN_RE.search(stat_div.get_text())
        if not m:
            continue
        entry = {"name": name, "pick_rate": int(m.group(1)) / 100, "win_rate": int(m.group(2)) / 100}
        (aspects if name.startswith("Aspect of") else items).append(entry)

    return {"items": items, "aspects": aspects}
