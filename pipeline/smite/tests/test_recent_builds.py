"""`recent_builds`: the newest matches per god, in the shape the god page filters."""
import json

from smite import recent_builds as rb

META = {
    "windows": {"ob46": {"start": "2026-10-20T00:00:00Z", "end": "2026-11-03T00:00:00Z"},
                "ob47": {"start": "2026-11-03T00:00:00Z", "end": "2026-11-09T00:00:00Z"}},
    "aspects": {"agni": [{"name": "Aspect of Combustion", "value": "aspect-of-combustion"}], "aladdin": []},
}


def _rec(t, placement=1, rank=5000, aspect="aspect-of-combustion", items=("book-of-thoth", None, "mystery-orb")):
    return {"m": t, "t": t, "aspect": aspect, "role": "Mid", "rank": rank, "placement": placement,
            "items": list(items), "starter": "conduit-gem", "relic": "aegis-of-acceleration", "enemies": []}


def _store(tmp_path, records):
    d = tmp_path / "ob47"
    d.mkdir()
    (d / "agni.jsonl").write_text("\n".join(json.dumps(r) for r in records) + "\n")
    return tmp_path


def test_newest_first_with_names_win_and_master(tmp_path):
    root = _store(tmp_path, [_rec("2026-11-04T00:00:00Z", placement=2, rank=4000),
                             _rec("2026-11-05T00:00:00Z", placement=1, rank=4400)])
    out = rb.god_file("agni", META, {"book-of-thoth": "Book of Thoth"}, root)
    first, second = out["builds"]
    assert first["t"] > second["t"]
    assert first["win"] is True and first["master"] is True
    assert second["win"] is False and second["master"] is False
    assert first["items"] == ["Book of Thoth", "Mystery Orb"]  # empty slot dropped, unknown slug titled
    assert first["aspect"] == "Aspect of Combustion" and first["patch"] == "ob47"
    assert first["relic"] == "Aegis of Acceleration"
    assert out["aspects"] == ["Aspect of Combustion"] and out["patches"] == ["ob47"]


def test_no_aspect_match_has_null_aspect(tmp_path):
    root = _store(tmp_path, [_rec("2026-11-04T00:00:00Z", aspect=None)])
    assert rb.god_file("agni", META, {}, root)["builds"][0]["aspect"] is None


def test_keeps_only_the_newest(tmp_path):
    root = _store(tmp_path, [_rec(f"2026-11-04T00:{i // 60:02d}:{i % 60:02d}Z") for i in range(rb.KEEP + 5)])
    out = rb.god_file("agni", META, {}, root)
    assert out["kept"] == rb.KEEP
    assert out["builds"][0]["t"] > out["builds"][-1]["t"]


def test_a_god_with_no_store_has_no_file(tmp_path):
    assert rb.god_file("aladdin", META, {}, tmp_path) is None
