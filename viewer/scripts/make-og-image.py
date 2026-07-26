"""Generate viewer/public/og.png — the 1200x630 card shown when a link to the
site is pasted into Discord, iMessage, Twitter, etc.

Committed as a PNG so the static host needs nothing at build time; this script
exists so the image is reproducible rather than a mystery binary. Re-run after
a rebrand:  python viewer/scripts/make-og-image.py
"""
from pathlib import Path
import random

from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
BG = (11, 14, 19)        # --color-bg0
GOLD = (227, 178, 60)    # --color-gold
INK = (232, 237, 244)    # --color-ink
MUTED = (139, 149, 165)  # --color-muted
LINE = (30, 37, 48)      # --color-line

ROOT = Path(__file__).resolve().parents[2]
ICONS = ROOT / "data" / "_assets" / "icons"
OUT = ROOT / "viewer" / "public" / "og.png"

# Deterministic layout — the same icons in the same places on every run.
random.seed(7)


def _font(size, bold=False):
    """Best available system font; PIL's bitmap default is the last resort."""
    candidates = [
        r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf",
        r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def _god_heads(limit=14):
    heads = sorted(p for p in ICONS.glob("*-head.png"))
    random.shuffle(heads)
    return heads[:limit]


def main():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    # Faint band of god portraits along the bottom — texture, not focus.
    x, y, size = -20, H - 150, 132
    for path in _god_heads():
        if x > W:
            break
        try:
            head = Image.open(path).convert("RGBA").resize((size, size), Image.LANCZOS)
        except Exception:
            continue
        faded = Image.new("RGBA", head.size, (0, 0, 0, 0))
        faded = Image.blend(faded, head, 0.22)
        img.paste(faded, (x, y), faded)
        x += size + 8

    draw.line([(0, H - 158), (W, H - 158)], fill=LINE, width=2)

    # Wordmark + tagline, left-aligned with generous margin.
    draw.text((72, 150), "ichor", font=_font(150, bold=True), fill=GOLD)
    draw.text((78, 320), "SMITE 2 build recommender", font=_font(46), fill=INK)
    draw.text(
        (78, 386),
        "Scores items by gold value \u2014 not by what's popular.",
        font=_font(30),
        fill=MUTED,
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT, "PNG", optimize=True)
    print(f"wrote {OUT} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
