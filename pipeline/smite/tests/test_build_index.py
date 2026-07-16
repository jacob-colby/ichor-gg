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
    assert index["items"] == [{"type": "smite-item", "name": "Deathbringer"}]
    assert index["builds"] == [{"type": "smite-build", "god": "Chiron"}]


def test_build_index_empty_folders_return_empty_lists(tmp_path):
    vault = _make_vault(tmp_path)
    index = build_index.build_index(vault)
    assert index == {"gods": [], "items": [], "builds": []}


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
    # yaml.safe_load parses an unquoted `last_verified: 2026-07-16` frontmatter
    # value into a datetime.date object, which json.dumps rejects unless it's
    # given a fallback serializer. Regression test for that crash.
    vault = _make_vault(tmp_path)
    notes.write_note(vault / "03. Workspaces" / "Gaming" / "SMITE 2" / "Builds" / "Chiron-Conquest.md",
                      {"type": "smite-build", "god": "Chiron", "last_verified": "2026-07-16"}, "")

    out_path = tmp_path / "viewer" / "public" / "index.json"
    build_index.write_index(vault, out_path)

    data = json.loads(out_path.read_text(encoding="utf-8"))
    assert data["builds"][0]["last_verified"] == "2026-07-16"
