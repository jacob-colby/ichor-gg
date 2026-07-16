import pytest

from smite import notes


def test_read_note_missing_file_returns_empty(tmp_path):
    frontmatter, body = notes.read_note(tmp_path / "missing.md")
    assert frontmatter == {}
    assert body == ""


def test_write_note_then_read_note_roundtrip(tmp_path):
    path = tmp_path / "Chiron.md"
    notes.write_note(path, {"name": "Chiron", "tier": 3}, "Some body text\n")

    frontmatter, body = notes.read_note(path)
    assert frontmatter == {"name": "Chiron", "tier": 3}
    assert body == "Some body text\n"


def test_merge_god_note_first_write_creates_wiki_block(tmp_path):
    path = tmp_path / "Chiron.md"
    notes.merge_god_note(path, {"name": "Chiron", "pantheon": "Greek"}, "Herbal Medicine heals allies.")

    frontmatter, body = notes.read_note(path)
    assert frontmatter == {"name": "Chiron", "pantheon": "Greek"}
    assert "<!-- WIKI:START -->" in body
    assert "Herbal Medicine heals allies." in body
    assert "<!-- WIKI:END -->" in body


def test_merge_god_note_preserves_content_outside_wiki_block(tmp_path):
    path = tmp_path / "Chiron.md"
    notes.merge_god_note(path, {"name": "Chiron", "pantheon": "Greek"}, "Old ability text.")

    frontmatter, body = notes.read_note(path)
    hand_written = body + "\n## My notes\nGreat into poke comps.\n"
    notes.write_note(path, frontmatter, hand_written)

    notes.merge_god_note(
        path,
        {"name": "Chiron", "pantheon": "Greek", "release_date": "2026-01-27"},
        "New ability text.",
    )

    new_frontmatter, new_body = notes.read_note(path)
    assert new_frontmatter["release_date"] == "2026-01-27"
    assert "New ability text." in new_body
    assert "Old ability text." not in new_body
    assert "## My notes" in new_body
    assert "Great into poke comps." in new_body


def test_merge_god_note_ignores_marker_text_mentioned_inline(tmp_path):
    path = tmp_path / "Chiron.md"
    notes.merge_god_note(path, {"name": "Chiron"}, "Old ability text.")

    frontmatter, body = notes.read_note(path)
    # A hand-written sentence that quotes the marker syntax inline (not on
    # its own line) sits above the real WIKI block.
    hand_written = (
        "The pipeline writes content between `<!-- WIKI:START -->` and "
        "`<!-- WIKI:END -->` markers.\n\n" + body
    )
    notes.write_note(path, frontmatter, hand_written)

    notes.merge_god_note(path, {"name": "Chiron"}, "New ability text.")

    _, new_body = notes.read_note(path)
    assert (
        "The pipeline writes content between `<!-- WIKI:START -->` and "
        "`<!-- WIKI:END -->` markers."
    ) in new_body
    assert "New ability text." in new_body
    assert "Old ability text." not in new_body


def test_merge_god_note_raises_on_multiple_wiki_blocks(tmp_path):
    path = tmp_path / "Chiron.md"
    frontmatter = {"name": "Chiron"}
    body = (
        "<!-- WIKI:START -->\nFirst block.\n<!-- WIKI:END -->\n\n"
        "<!-- WIKI:START -->\nSecond block.\n<!-- WIKI:END -->\n"
    )
    notes.write_note(path, frontmatter, body)

    with pytest.raises(ValueError):
        notes.merge_god_note(path, {"name": "Chiron"}, "New ability text.")


def test_merge_build_note_first_write_creates_community_entry(tmp_path):
    path = tmp_path / "Chiron-Conquest.md"
    notes.merge_build_note(
        path, "Chiron", "Conquest",
        {"aspect": "Aspect of the Heroic Tutor",
         "slot_order": [{"item": "Transcendence", "pick_rate": 0.61, "win_rate": 0.49}]},
    )

    frontmatter, _ = notes.read_note(path)
    assert frontmatter["god"] == "Chiron"
    assert frontmatter["mode"] == "Conquest"
    assert len(frontmatter["builds"]) == 1
    assert frontmatter["builds"][0]["source"] == "community"
    assert frontmatter["builds"][0]["aspect"] == "Aspect of the Heroic Tutor"


def test_merge_build_note_preserves_pro_and_mine_entries(tmp_path):
    path = tmp_path / "Chiron-Conquest.md"
    seed = {
        "type": "smite-build", "god": "Chiron", "mode": "Conquest",
        "builds": [
            {"source": "pro", "slot_order": ["Transcendence", "Devourer's Gauntlet"], "notes": "SPL crit core"},
            {"source": "mine", "slot_order": ["Transcendence", "Ninja Tabi"]},
        ],
    }
    notes.write_note(path, seed, "")

    notes.merge_build_note(
        path, "Chiron", "Conquest",
        {"aspect": "Aspect of the Heroic Tutor",
         "slot_order": [{"item": "Transcendence", "pick_rate": 0.61, "win_rate": 0.49}]},
    )

    frontmatter, _ = notes.read_note(path)
    sources = {b["source"] for b in frontmatter["builds"]}
    assert sources == {"pro", "mine", "community"}
    pro_entry = next(b for b in frontmatter["builds"] if b["source"] == "pro")
    assert pro_entry["notes"] == "SPL crit core"


def test_merge_build_note_replaces_stale_community_entry(tmp_path):
    path = tmp_path / "Chiron-Conquest.md"
    notes.merge_build_note(path, "Chiron", "Conquest", {"aspect": "Old Aspect", "slot_order": []})
    notes.merge_build_note(path, "Chiron", "Conquest", {"aspect": "New Aspect", "slot_order": []})

    frontmatter, _ = notes.read_note(path)
    community_entries = [b for b in frontmatter["builds"] if b["source"] == "community"]
    assert len(community_entries) == 1
    assert community_entries[0]["aspect"] == "New Aspect"


def test_log_refresh_diff_writes_changed_fields(tmp_path):
    log_dir = tmp_path / "_logs"
    notes.log_refresh_diff(log_dir, "Chiron", {"cost": 100}, {"cost": 150})

    logs = list(log_dir.glob("refresh-*.md"))
    assert len(logs) == 1
    content = logs[0].read_text(encoding="utf-8")
    assert "Chiron" in content and "cost" in content and "100" in content and "150" in content


def test_log_refresh_diff_skips_when_no_changes(tmp_path):
    log_dir = tmp_path / "_logs"
    notes.log_refresh_diff(log_dir, "Chiron", {"cost": 100}, {"cost": 100})
    assert not log_dir.exists()
