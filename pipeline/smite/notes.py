"""Read/write vault notes with YAML frontmatter, preserving hand-written
content across pipeline refreshes.

Two ownership models, matching the design spec:
- God/Item notes: frontmatter is entirely pipeline-owned; the body has a
  WIKI:START/END marker block for pulled prose (same pattern as the vault's
  existing Daily Hub NOW:START/END block) — everything outside it is the
  user's and untouched.
- Build notes: frontmatter holds a `builds` array with one entry per
  source (community/pro/mine). Refresh only ever replaces the
  `source: community` entry; other entries are preserved verbatim.
"""
import re
from datetime import date
from pathlib import Path

import yaml

FRONTMATTER_RE = re.compile(r"^---\n(.*?\n)---\n?", re.DOTALL)
WIKI_BLOCK_RE = re.compile(r"<!-- WIKI:START -->.*?<!-- WIKI:END -->", re.DOTALL)


def read_note(path: Path) -> tuple:
    if not path.exists():
        return {}, ""
    text = path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    frontmatter = yaml.safe_load(m.group(1)) or {}
    return frontmatter, text[m.end():]


def write_note(path: Path, frontmatter: dict, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    yaml_text = yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True)
    path.write_text(f"---\n{yaml_text}---\n{body}", encoding="utf-8")


def merge_god_note(path: Path, scraped_frontmatter: dict, wiki_block_content: str,
                    log_dir: Path = None) -> None:
    existing_frontmatter, existing_body = read_note(path)

    if log_dir is not None:
        log_refresh_diff(log_dir, scraped_frontmatter.get("name", path.stem),
                          existing_frontmatter, scraped_frontmatter)

    new_block = f"<!-- WIKI:START -->\n{wiki_block_content}\n<!-- WIKI:END -->"
    if WIKI_BLOCK_RE.search(existing_body):
        new_body = WIKI_BLOCK_RE.sub(new_block, existing_body, count=1)
    elif existing_body.strip():
        new_body = f"{new_block}\n\n{existing_body}"
    else:
        new_body = f"{new_block}\n"

    write_note(path, scraped_frontmatter, new_body)


# Item notes follow the exact same ownership rule as god notes.
merge_item_note = merge_god_note


def merge_build_note(path: Path, god: str, mode: str, community_entry: dict) -> None:
    frontmatter, body = read_note(path)
    if not frontmatter:
        frontmatter = {"type": "smite-build", "god": god, "mode": mode, "builds": []}

    builds = [b for b in frontmatter.get("builds", []) if b.get("source") != "community"]
    builds.insert(0, {"source": "community", **community_entry})
    frontmatter["builds"] = builds

    write_note(path, frontmatter, body)


def log_refresh_diff(log_dir: Path, name: str, old_frontmatter: dict, new_frontmatter: dict) -> None:
    changes = []
    for key in sorted(set(old_frontmatter) | set(new_frontmatter)):
        if key == "source_url":
            continue
        if old_frontmatter.get(key) != new_frontmatter.get(key):
            changes.append(f"- **{key}**: `{old_frontmatter.get(key)}` -> `{new_frontmatter.get(key)}`")
    if not changes:
        return
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / f"refresh-{date.today().isoformat()}.md"
    with log_path.open("a", encoding="utf-8") as f:
        f.write(f"## {name}\n" + "\n".join(changes) + "\n\n")
