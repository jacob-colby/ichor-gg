"""Walk the SMITE data + build folders and emit one index.json for the
second-monitor viewer to fetch. Re-run after any refresh, or on demand via
the viewer's "reload data" button — no file-watcher, content only changes
on patch days."""
import json
from pathlib import Path

from smite import notes


def build_index(vault_root: Path) -> dict:
    gods_dir = vault_root / "04. System" / "Data" / "SMITE" / "Gods"
    items_dir = vault_root / "04. System" / "Data" / "SMITE" / "Items"
    builds_dir = vault_root / "03. Workspaces" / "Gaming" / "SMITE 2" / "Builds"

    def _all(dir_path: Path) -> list:
        if not dir_path.exists():
            return []
        return [notes.read_note(p)[0] for p in sorted(dir_path.glob("*.md"))]

    return {"gods": _all(gods_dir), "items": _all(items_dir), "builds": _all(builds_dir)}


def write_index(vault_root: Path, out_path: Path) -> None:
    index = build_index(vault_root)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    # Frontmatter fields like `last_verified: 2026-07-16` round-trip through
    # yaml.safe_load as datetime.date objects, which json.dumps can't
    # serialize on its own — stringify anything json doesn't natively support.
    out_path.write_text(json.dumps(index, indent=2, default=str), encoding="utf-8")


if __name__ == "__main__":
    vault_root = Path(__file__).resolve().parents[2]
    write_index(vault_root, vault_root / "viewer" / "public" / "index.json")
    print("Wrote viewer/public/index.json")
