import json

from smite import build_index, notes


def _make_vault(tmp_path):
    (tmp_path / "04. System" / "Data" / "SMITE" / "Gods").mkdir(parents=True)
    (tmp_path / "04. System" / "Data" / "SMITE" / "Items").mkdir(parents=True)
    (tmp_path / "03. Workspaces" / "Gaming" / "SMITE 2" / "Builds").mkdir(parents=True)
    return tmp_path


def test_build_index_collects_gods_items_builds(tmp_path):
    vault = _make_vault(tmp_path)
    notes.write_note(vault / "04. System" / "Data" / "SMITE" / "Gods" / "Chiron.md",
                      {"type": "smite-god", "name": "Chiron"}, "")
    notes.write_note(vault / "04. System" / "Data" / "SMITE" / "Items" / "Deathbringer.md",
                      {"type": "smite-item", "name": "Deathbringer"}, "")
    notes.write_note(vault / "03. Workspaces" / "Gaming" / "SMITE 2" / "Builds" / "Chiron-Conquest.md",
                      {"type": "smite-build", "god": "Chiron"}, "")

    index = build_index.build_index(vault)

    assert index["gods"] == [{"type": "smite-god", "name": "Chiron"}]
    # Items are enriched with god-agnostic effect_tags + efficiency_tier; this
    # note has no cost so it can't be scored (tier None) and no tags entry ([]).
    assert index["items"] == [
        {"type": "smite-item", "name": "Deathbringer", "effect_tags": [], "efficiency_tier": None}
    ]
    assert index["builds"] == [{"type": "smite-build", "god": "Chiron"}]


def test_build_index_empty_folders_return_empty_lists(tmp_path):
    vault = _make_vault(tmp_path)
    index = build_index.build_index(vault)
    assert index == {"gods": [], "items": [], "builds": [], "starters": []}


def test_write_index_creates_json_file(tmp_path):
    vault = _make_vault(tmp_path)
    notes.write_note(vault / "04. System" / "Data" / "SMITE" / "Gods" / "Chiron.md",
                      {"type": "smite-god", "name": "Chiron"}, "")

    out_path = tmp_path / "viewer" / "public" / "index.json"
    build_index.write_index(vault, out_path)

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
    vault = _make_vault(tmp_path)
    god_path = vault / "04. System" / "Data" / "SMITE" / "Gods" / "Chiron.md"
    god_path.write_text(
        "---\nname: Chiron\nlast_verified: 2026-07-16\n---\n",
        encoding="utf-8",
    )

    out_path = tmp_path / "viewer" / "public" / "index.json"
    build_index.write_index(vault, out_path)  # must not raise

    data = json.loads(out_path.read_text(encoding="utf-8"))
    assert data["gods"][0]["last_verified"] == "2026-07-16"


def test_write_index_copies_icon_files(tmp_path):
    vault = _make_vault(tmp_path)
    icons_dir = vault / "04. System" / "Data" / "SMITE" / "_assets" / "icons"
    icons_dir.mkdir(parents=True)
    (icons_dir / "chiron.png").write_bytes(b"\x89PNG\r\n\x1a\nfakeicondata")

    out_path = tmp_path / "viewer" / "public" / "index.json"
    build_index.write_index(vault, out_path)

    copied_icon = out_path.parent / "icons" / "chiron.png"
    assert copied_icon.exists()
    assert copied_icon.read_bytes() == b"\x89PNG\r\n\x1a\nfakeicondata"


def test_write_index_handles_no_icons_dir_gracefully(tmp_path):
    vault = _make_vault(tmp_path)
    out_path = tmp_path / "viewer" / "public" / "index.json"

    build_index.write_index(vault, out_path)  # must not raise, even with no _assets/icons/ at all

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
