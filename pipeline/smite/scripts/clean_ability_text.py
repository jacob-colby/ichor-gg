"""One-off migration: re-clean ability descriptions in already-scraped notes.

Every one of the 513 scraped abilities shipped the wiki's own "Expand Ability
Video" control as body copy, its stat block twice (once as prose, once as
parsed detail chips), and a leading tagline or the god's own name. The parser
fix in `wiki_parser.clean_ability_description` stops that happening again, but
notes scraped before it keep the bad text until the next full refresh — and a
refresh needs the network.

This applies the identical cleaning to the notes already on disk, using each
ability's own `details` (which were parsed correctly all along) to subtract the
duplicated lines. Idempotent: running it twice changes nothing the second time.

    python -m smite.scripts.clean_ability_text [--dry-run]
"""
import argparse
from pathlib import Path

from smite import notes, wiki_parser


def clean_god(god: dict) -> int:
    """Re-clean every ability description in place. Returns the number changed."""
    changed = 0
    for ability in god.get("abilities") or []:
        before = ability.get("description")
        if not before:
            continue
        after = wiki_parser.clean_ability_description(
            before, ability.get("details"), ability.get("slot", ""), ability.get("name", ""))
        # An ability whose whole description was chrome and duplication ends up
        # empty; drop the key rather than storing "".
        if after != before:
            changed += 1
            if after:
                ability["description"] = after
            else:
                ability.pop("description", None)
    return changed


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true", help="report without writing")
    ap.add_argument("--root", default=".", help="repo root (default: cwd)")
    args = ap.parse_args()

    gods_dir = Path(args.root) / "data" / "Gods"
    if not gods_dir.exists():
        raise SystemExit(f"no such directory: {gods_dir}")

    total_files = total_abilities = 0
    for path in sorted(gods_dir.glob("*.md")):
        god, body = notes.read_note(path)
        changed = clean_god(god)
        if not changed:
            continue
        total_files += 1
        total_abilities += changed
        if not args.dry_run:
            notes.write_note(path, god, body)

    verb = "would clean" if args.dry_run else "cleaned"
    print(f"{verb} {total_abilities} abilities across {total_files} gods")


if __name__ == "__main__":
    main()
