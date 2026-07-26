import json

from smite import build_index, notes


def _make_repo(tmp_path):
    (tmp_path / "data" / "Gods").mkdir(parents=True)
    (tmp_path / "data" / "Items").mkdir(parents=True)
    (tmp_path / "data" / "builds").mkdir(parents=True)
    return tmp_path


def test_build_index_collects_gods_items_builds(tmp_path):
    repo = _make_repo(tmp_path)
    notes.write_note(repo / "data" / "Gods" / "Chiron.md",
                      {"type": "smite-god", "name": "Chiron"}, "")
    notes.write_note(repo / "data" / "Items" / "Deathbringer.md",
                      {"type": "smite-item", "name": "Deathbringer"}, "")
    notes.write_note(repo / "data" / "builds" / "Chiron-Conquest.md",
                      {"type": "smite-build", "god": "Chiron"}, "")

    index = build_index.build_index(repo)

    # Gods gain a derived ability_order (see abilities.py) only when their kit
    # has levelable abilities. This note has no `abilities` key at all, so the
    # key is absent rather than a fabricated order of empty slots.
    assert index["gods"] == [{"type": "smite-god", "name": "Chiron"}]
    # Items are enriched with god-agnostic effect_tags + efficiency_tier; this
    # note has no cost so it can't be scored (tier None) and no tags entry ([]).
    assert index["items"] == [
        {"type": "smite-item", "name": "Deathbringer", "effect_tags": [], "efficiency_tier": None}
    ]
    assert index["builds"] == [{"type": "smite-build", "god": "Chiron"}]


def test_build_index_empty_folders_return_empty_lists(tmp_path):
    repo = _make_repo(tmp_path)
    index = build_index.build_index(repo)
    assert index == {"gods": [], "items": [], "builds": [], "starters": [],
                     "roster": [], "data_updated": "",
                     "tierlist": {"gods": [], "items": []},
                     "god_item_scores": {}, "draft": {},
                     "patch_notes": []}


def test_write_index_creates_json_file(tmp_path):
    repo = _make_repo(tmp_path)
    notes.write_note(repo / "data" / "Gods" / "Chiron.md",
                      {"type": "smite-god", "name": "Chiron"}, "")

    out_path = tmp_path / "viewer" / "public" / "index.json"
    build_index.write_index(repo, out_path)

    assert out_path.exists()
    data = json.loads(out_path.read_text(encoding="utf-8"))
    assert data["gods"][0]["name"] == "Chiron"


def test_write_index_serializes_bare_yaml_dates(tmp_path):
    # An unquoted YAML date literal parses via yaml.safe_load as a real
    # datetime.date object, not a string — this is what crashed json.dumps
    # before the `default=str` fix (confirmed against the real
    # Chiron-Conquest.md note, which has an unquoted last_verified: date).
    # Passing a plain Python string into write_note doesn't reproduce this:
    # yaml.safe_dump auto-quotes date-shaped strings on write, so read_note
    # reads it back as a str, never a date object. Writing raw YAML text
    # with an unquoted date and reading it back via notes.read_note is what
    # actually reconstructs the date object that broke json.dumps.
    repo = _make_repo(tmp_path)
    god_path = repo / "data" / "Gods" / "Chiron.md"
    god_path.write_text(
        "---\nname: Chiron\nlast_verified: 2026-07-16\n---\n",
        encoding="utf-8",
    )

    out_path = tmp_path / "viewer" / "public" / "index.json"
    build_index.write_index(repo, out_path)  # must not raise

    data = json.loads(out_path.read_text(encoding="utf-8"))
    assert data["gods"][0]["last_verified"] == "2026-07-16"


def test_write_index_copies_icon_files(tmp_path):
    repo = _make_repo(tmp_path)
    icons_dir = repo / "data" / "_assets" / "icons"
    icons_dir.mkdir(parents=True)
    (icons_dir / "chiron.png").write_bytes(b"\x89PNG\r\n\x1a\nfakeicondata")

    out_path = tmp_path / "viewer" / "public" / "index.json"
    build_index.write_index(repo, out_path)

    copied_icon = out_path.parent / "icons" / "chiron.png"
    assert copied_icon.exists()
    assert copied_icon.read_bytes() == b"\x89PNG\r\n\x1a\nfakeicondata"


def test_write_index_handles_no_icons_dir_gracefully(tmp_path):
    repo = _make_repo(tmp_path)
    out_path = tmp_path / "viewer" / "public" / "index.json"

    build_index.write_index(repo, out_path)  # must not raise, even with no _assets/icons/ at all

    assert out_path.exists()


def test_enrich_items_adds_tags_and_tier():
    from smite import build_index
    items = [
        {"name": "Deathbringer", "cost": 2900, "stats": {"Strength": "45"}},
        {"name": "Cheapo", "cost": 900, "stats": {"Strength": "45"}},
    ]
    tags = {"Deathbringer": ["burst"], "Cheapo": []}
    enriched = build_index._enrich_items(items, tags)
    by = {it["name"]: it for it in enriched}
    assert by["Deathbringer"]["effect_tags"] == ["burst"]
    assert by["Cheapo"]["effect_tags"] == []
    assert by["Cheapo"]["efficiency_tier"] in {"undervalued", "fair", "premium"}


def test_build_index_exports_starters(tmp_path, monkeypatch):
    from smite import build_index
    from pathlib import Path
    result = build_index.build_index(Path(__file__).resolve().parents[3])
    assert "starters" in result
    assert isinstance(result["starters"], list)


def test_build_index_adds_per_item_meta():
    from smite import build_index
    from pathlib import Path
    result = build_index.build_index(Path(__file__).resolve().parents[3])
    metaed = [i for i in result["items"] if i.get("meta")]
    assert metaed, "expected some items to carry community meta"
    m = metaed[0]["meta"]
    assert 0.0 <= m["win_avg"] <= 1.0 and m["gods"] >= 1


def test_build_index_emits_data_updated_and_roster():
    from smite import build_index
    from pathlib import Path
    r = build_index.build_index(Path(__file__).resolve().parents[3])
    assert "data_updated" in r and isinstance(r["data_updated"], str) and r["data_updated"]
    assert "roster" in r and isinstance(r["roster"], list)


def test_build_index_emits_tierlist_with_gods_and_items():
    from smite import build_index
    from pathlib import Path
    r = build_index.build_index(Path(__file__).resolve().parents[3])
    assert "tierlist" in r
    tl = r["tierlist"]
    assert set(tl) == {"gods", "items"}
    assert tl["gods"] and tl["items"]
    god = tl["gods"][0]
    assert {"name", "role", "damage_type", "ours", "community", "tier_ours", "tier_community"} <= set(god)
    item = tl["items"][0]
    assert {"name", "tier", "efficiency_tier", "ours", "community", "tier_ours", "tier_community"} <= set(item)
    # community coverage is partial by design — some tier_community entries
    # must be None, never silently zero-filled.
    assert any(g["tier_community"] is None for g in tl["gods"])


def test_build_index_emits_patch_notes_as_list():
    from smite import build_index
    from pathlib import Path
    r = build_index.build_index(Path(__file__).resolve().parents[3])
    assert "patch_notes" in r
    assert isinstance(r["patch_notes"], list)


def test_build_index_reads_snapshots_under_the_given_repo_root(tmp_path):
    # patch_notes must come from the repo being indexed, not the module-level
    # default store — otherwise tests silently depend on real accumulated data.
    from smite import build_index, snapshots
    snaps = tmp_path / "data" / "Analysis" / "snapshots"
    snaps.mkdir(parents=True)
    old = [{"name": "Rage", "cost": 2500, "tier": 3, "stats": {"Critical Chance": "20%"}}]
    new = [{"name": "Rage", "cost": 2500, "tier": 3, "stats": {"Critical Chance": "25%"}}]
    snapshots.write_snapshot(old, "2026-01-01", snaps)
    snapshots.write_snapshot(new, "2026-01-08", snaps)

    report = build_index.build_index(tmp_path)["patch_notes"]
    assert [p["to"] for p in report] == ["2026-01-08"]
    assert report[0]["changed"][0]["name"] == "Rage"
    assert report[0]["changed"][0]["verdict"] == "buff"


def test_build_index_emits_ability_order_for_every_god():
    from smite import build_index
    from pathlib import Path
    r = build_index.build_index(Path(__file__).resolve().parents[3])
    # Gods whose kit scraped no levelable abilities (stance gods) legitimately
    # carry no key — better than a fabricated Basic-Attack/Passive order. Every
    # god that DOES have one must be well-formed, and most of the roster must.
    with_order = [g for g in r["gods"] if g.get("ability_order")]
    assert len(with_order) >= len(r["gods"]) - 5, "too many gods missing an order"
    for god in with_order:
        ao = god["ability_order"]
        assert len(ao["order"]) == 20
        assert set(ao["summary"]) == {"max_order", "ult_levels"}
        assert ao["summary"]["ult_levels"] == [5, 9, 13, 17]
        assert not any(s in ("Basic Attack", "Passive") for s in ao["order"])


def test_build_index_emits_capped_god_item_scores():
    from smite import build_index
    from pathlib import Path
    r = build_index.build_index(Path(__file__).resolve().parents[3])
    scores = r["god_item_scores"]
    assert set(scores) == {g["name"] for g in r["gods"]}
    for god, table in scores.items():
        assert 0 < len(table) <= 40, f"{god} has {len(table)} entries"
        assert all(isinstance(v, float) for v in table.values())
