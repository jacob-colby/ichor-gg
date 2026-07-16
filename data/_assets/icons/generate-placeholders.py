#!/usr/bin/env python3
"""
generate-placeholders.py — SMITE 2 god portrait icon stubs
===========================================================
Creates valid 64×64 solid-color PNG files for every god in the target roster.
No internet required — uses Python stdlib only (struct + zlib).

Placeholder colors encode god role:
  Hunter    → #4CAF50  (green)
  Mage      → #2196F3  (blue)
  Warrior   → #FF9800  (orange)
  Guardian  → #9C27B0  (purple)
  Assassin  → #F44336  (red)

Each stub is ~150 bytes — well within the 50 KB spec.

Safety rule: files >200 bytes are skipped so real icons already downloaded
are never overwritten.

Usage:
    cd "07. Gaming/_assets/smite2/icons/"
    python3 generate-placeholders.py

Expected output: 31 PNG stubs, each ~150 bytes, role-color coded.
Run fetch-icons.py (internet required) to replace stubs with real icons.
"""

import struct
import zlib
from pathlib import Path

HERE = Path(__file__).parent


# ---------------------------------------------------------------------------
# God roster — (slug, role)
# slug matches the filename used in god-note embed links
# ---------------------------------------------------------------------------
GODS = [
    # Jacob's pool (priority — embedded in all 3 god notes)
    ("chiron",    "Hunter"),
    ("ullr",      "Hunter"),
    ("hou-yi",    "Hunter"),

    # Contextual hunters (referenced in matchup notes)
    ("neith",     "Hunter"),
    ("apollo",    "Hunter"),
    ("artemis",   "Hunter"),
    ("cupid",     "Hunter"),
    ("jing-wei",  "Hunter"),
    ("izanami",   "Hunter"),

    # Broader meta roster
    ("hercules",  "Warrior"),
    ("thor",      "Warrior"),
    ("bellona",   "Warrior"),
    ("loki",      "Assassin"),
    ("bastet",    "Assassin"),
    ("nemesis",   "Assassin"),
    ("susano",    "Assassin"),
    ("fenrir",    "Assassin"),
    ("anubis",    "Mage"),
    ("ra",        "Mage"),
    ("agni",      "Mage"),
    ("hades",     "Mage"),
    ("poseidon",  "Mage"),
    ("kukulkan",  "Mage"),
    ("zeus",      "Mage"),
    ("ah-puch",   "Mage"),
    ("merlin",    "Mage"),
    ("athena",    "Guardian"),
    ("ares",      "Guardian"),
    ("ymir",      "Guardian"),
    ("sobek",     "Guardian"),
    ("medusa",    "Hunter"),   # Medusa is a Hunter in SMITE
]

ROLE_COLOURS = {
    "Hunter":   (0x4C, 0xAF, 0x50),  # #4CAF50 — green
    "Mage":     (0x21, 0x96, 0xF3),  # #2196F3 — blue
    "Warrior":  (0xFF, 0x98, 0x00),  # #FF9800 — orange
    "Guardian": (0x9C, 0x27, 0xB0),  # #9C27B0 — purple
    "Assassin": (0xF4, 0x43, 0x36),  # #F44336 — red
}


# ---------------------------------------------------------------------------
# Minimal PNG writer — no third-party deps
# ---------------------------------------------------------------------------
def _make_png(r: int, g: int, b: int, size: int = 64) -> bytes:
    """Return a valid PNG file: solid colour, <size>×<size>, 8-bit RGB."""

    def chunk(name: bytes, data: bytes) -> bytes:
        c = name + data
        return struct.pack(">I", len(data)) + c + struct.pack(">I", zlib.crc32(c) & 0xFFFFFFFF)

    # IHDR
    ihdr_data = struct.pack(">IIBBBBB", size, size, 8, 2, 0, 0, 0)
    ihdr = chunk(b"IHDR", ihdr_data)

    # IDAT — one filter byte (0x00 = None) per row, then RGB pixels
    raw_row = bytes([0x00]) + bytes([r, g, b] * size)
    raw = raw_row * size
    idat = chunk(b"IDAT", zlib.compress(raw, 9))

    # IEND
    iend = chunk(b"IEND", b"")

    return b"\x89PNG\r\n\x1a\n" + ihdr + idat + iend


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    created = 0
    skipped = 0

    for slug, role in GODS:
        out = HERE / f"{slug}.png"
        if out.exists() and out.stat().st_size > 200:
            print(f"  [skip] {slug}.png — already present ({out.stat().st_size} bytes)")
            skipped += 1
            continue

        colour = ROLE_COLOURS[role]
        png_bytes = _make_png(*colour)
        out.write_bytes(png_bytes)
        print(f"  [stub] {slug}.png — {role} {colour} ({len(png_bytes)} bytes)")
        created += 1

    total = created + skipped
    print(f"\nDone — {created} stubs created, {skipped} skipped (already exist). "
          f"({total} total gods)")
    print("Run fetch-icons.py (internet required) to replace stubs with real icons.")
    print("Obsidian embeds in 01-god-notes/ will render colored squares immediately.")


if __name__ == "__main__":
    main()
