from smite import manage_gods, notes


def _setup(tmp_path, monkeypatch):
    data = tmp_path / "data"; (data / "Gods").mkdir(parents=True)
    builds = tmp_path / "builds"; builds.mkdir()
    notes.write_note(data / "Gods" / "Chiron.md", {"name": "Chiron"}, "")
    notes.write_note(builds / "Chiron-Conquest.md", {"god": "Chiron"}, "")
    notes.write_note(builds / "Chiron-Joust.md", {"god": "Chiron"}, "")
    monkeypatch.setattr(manage_gods, "GODS_ROOT", data / "Gods")
    monkeypatch.setattr(manage_gods, "BUILDS_ROOT", builds)
    monkeypatch.setattr(manage_gods, "_reindex", lambda: None)  # skip the real rebuild
    return data, builds


def test_remove_moves_god_and_builds(tmp_path, monkeypatch):
    data, builds = _setup(tmp_path, monkeypatch)
    rc = manage_gods.remove("Chiron")
    assert rc == 0
    assert not (data / "Gods" / "Chiron.md").exists()
    assert (data / "Gods" / "_removed" / "Chiron.md").exists()
    assert (builds / "_removed" / "Chiron-Conquest.md").exists()
    assert (builds / "_removed" / "Chiron-Joust.md").exists()


def test_remove_unknown_god_fails(tmp_path, monkeypatch):
    _setup(tmp_path, monkeypatch)
    assert manage_gods.remove("Nobody") == 1
