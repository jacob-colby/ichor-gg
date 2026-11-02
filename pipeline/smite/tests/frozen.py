"""Inputs frozen at Open Beta 40, for tests that prove arithmetic.

A worked example — "Medusa's build costs 15400 and does 314.8 DPS at 70
protection", "Daybreak Gavel's Adaptive Stat is worth 70" — is a claim about
the MATH on given inputs. Read off the live `data/`, it is also a claim about
which patch is current, and the first wiki refresh after it was written turns
it red without a line of code changing (2026-11-02: fourteen tests, Open Beta
40 -> 46). Since `refresh-data.yml` now refuses a stats refresh that turns a
test red, a test like that would also block every patch's data forever.

So the arithmetic reads these files, and each such test has a sibling that
holds the same property as an INVARIANT over the live data — "every Adaptive
Stat item is priced at the mean of its two grants", not "Gavel is 70".

`items.json` is `recommend.load_items()` and `gods.json` is
`notes.read_note(...)[0]` for the gods the worked examples use, both taken from
`main` at 836452b (data_patch Open Beta 40). Never regenerate them to make a
test pass: they are fixed inputs, and a hand computation is only checkable
against the inputs it was computed from.
"""
import json
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent / "fixtures" / "frozen" / "ob40"


@lru_cache(maxsize=None)
def _items() -> tuple:
    return tuple(json.loads((ROOT / "items.json").read_text(encoding="utf-8")))


def items() -> list:
    """Every named item, as `recommend.load_items()` returned it. Fresh dicts
    each call, so a test that mutates one cannot leak into another."""
    return json.loads(json.dumps(list(_items())))


def items_by_name() -> dict:
    return {it["name"]: it for it in items()}


def item(name: str) -> dict:
    return items_by_name()[name]


def god(name: str) -> dict:
    return json.loads((ROOT / "gods.json").read_text(encoding="utf-8"))[name]
