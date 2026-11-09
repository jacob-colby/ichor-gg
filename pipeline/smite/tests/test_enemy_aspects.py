"""`enemy_aspects`: what an enemy playing an aspect builds, pooled over patches."""
import json

from smite import enemy_aspects as ea

STATS = {
    "Rod": {"Intelligence": 90}, "Book": {"Intelligence": 80}, "Soul": {"Intelligence": 70},
    "Blade": {"Strength": 60}, "Bow": {"Attack Speed": 30}, "Bragi": {"Strength": 40, "Intelligence": 40},
    "Plate": {"Physical Protection": 50}, "Mail": {"Magical Protection": 50}, "Heart": {"Max Health": 300},
}
SLUGS = {"rod": "Rod", "book": "Book", "soul": "Soul", "blade": "Blade", "bow": "Bow", "plate": "Plate",
         "mail": "Mail", "heart": "Heart"}


def test_classify():
    c = lambda *n: ea.classify(list(n), STATS)  # noqa: E731
    assert c("Rod", "Book", "Soul", "Plate", "Mail", "Heart") == "magical"
    assert c("Blade", "Bow", "Blade", "Bow", "Plate", "Heart") == "physical"
    assert c("Plate", "Mail", "Heart", "Heart", "Blade", "Rod") == "tank"
    assert c("Bragi", "Bragi", "Bragi", "Plate", "Mail", "Heart") == "mixed"  # hybrids count on both sides
    assert c("Mystery", "Heart") == "tank"  # an item with no stats carries no power


def _store(tmp_path, per_window):
    meta = {"windows": {}, "aspects": {"tsukuyomi": [{"name": "Aspect of Mangetsu", "value": "aspect-of-mangetsu"}]}}
    (tmp_path / "_meta.json").write_text(json.dumps(meta))
    for w, n in per_window.items():
        d = tmp_path / w
        d.mkdir()
        recs = [{"m": f"{w}{i}", "t": "2026-11-01T00:00:00Z", "aspect": "aspect-of-mangetsu", "role": "Mid",
                 "rank": 5000, "placement": 1, "items": ["rod", "book", "soul", "plate", "mail", None],
                 "starter": None, "relic": None, "enemies": []} for i in range(n)]
        (d / "tsukuyomi.jsonl").write_text("\n".join(json.dumps(r) for r in recs) + "\n")
    return tmp_path


def test_pools_patch_windows_so_no_single_window_has_to_clear_the_floor(tmp_path, monkeypatch):
    monkeypatch.setattr(ea.am, "item_name_lookup", lambda: SLUGS)
    root = _store(tmp_path, {"ob44": 17, "ob45": 20, "ob46": 21, "ob47": 6})  # none reaches 30; 64 pooled
    out = ea.build([{"name": "Tsukuyomi"}], [{"name": n, "stats": s} for n, s in STATS.items()], root)
    e = out["Tsukuyomi"]["Aspect of Mangetsu"]
    assert e["matches"] == 64 and e["kind"] == "magical" and e["role"] == "Mid" and e["magical"] == 1.0


def test_below_the_floor_after_pooling_is_absent(tmp_path, monkeypatch):
    monkeypatch.setattr(ea.am, "item_name_lookup", lambda: SLUGS)
    root = _store(tmp_path, {"ob46": 12, "ob47": 10})
    assert ea.build([{"name": "Tsukuyomi"}], [{"name": n, "stats": s} for n, s in STATS.items()], root) == {}
