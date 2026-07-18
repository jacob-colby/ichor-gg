import io
import json
from pathlib import Path

from smite import save_build, notes


def _setup(tmp_path, monkeypatch):
    data = tmp_path / "data"
    (data / "Gods").mkdir(parents=True)
    (data / "Items").mkdir(parents=True)
    notes.write_note(data / "Gods" / "Chiron.md", {"name": "Chiron"}, "")
    notes.write_note(data / "Items" / "Deathbringer.md", {"name": "Deathbringer"}, "")
    builds = tmp_path / "builds"; builds.mkdir()
    monkeypatch.setattr(save_build, "DATA_ROOT", data)
    monkeypatch.setattr(save_build, "BUILDS_ROOT", builds)
    return builds


def _run(payload, monkeypatch):
    monkeypatch.setattr("sys.stdin", io.StringIO(json.dumps(payload)))
    return save_build.main()


def test_save_build_writes_mine_entry(tmp_path, monkeypatch):
    builds = _setup(tmp_path, monkeypatch)
    rc = _run({"action": "save", "god": "Chiron", "mode": "Conquest",
               "name": "My Build", "slot_order": ["Deathbringer", "Unknown Item"]}, monkeypatch)
    assert rc == 0
    fm, _ = notes.read_note(builds / "Chiron-Conquest.md")
    mine = next(b for b in fm["builds"] if b["source"] == "mine")
    assert mine["name"] == "My Build"
    assert mine["slot_order"] == ["Deathbringer"]  # unknown item filtered out


def test_save_build_rejects_unknown_god(tmp_path, monkeypatch):
    _setup(tmp_path, monkeypatch)
    rc = _run({"action": "save", "god": "../etc", "mode": "Conquest", "name": "x", "slot_order": []}, monkeypatch)
    assert rc == 1


def test_save_build_delete(tmp_path, monkeypatch):
    builds = _setup(tmp_path, monkeypatch)
    _run({"action": "save", "god": "Chiron", "mode": "Conquest", "name": "X", "slot_order": ["Deathbringer"]}, monkeypatch)
    rc = _run({"action": "delete", "god": "Chiron", "mode": "Conquest", "name": "X"}, monkeypatch)
    assert rc == 0
    fm, _ = notes.read_note(builds / "Chiron-Conquest.md")
    assert not [b for b in fm["builds"] if b["source"] == "mine"]
