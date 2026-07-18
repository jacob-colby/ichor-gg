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


def test_merge_god_note_raises_on_unpaired_stray_start_marker(tmp_path):
    path = tmp_path / "Chiron.md"
    notes.merge_god_note(path, {"name": "Chiron"}, "Old ability text.")

    frontmatter, body = notes.read_note(path)
    # A stray, unpaired START marker on its own line (e.g. hand-written docs
    # demonstrating the syntax, with no matching END nearby), followed later
    # by the real complete block.
    hand_written = (
        "Example marker syntax:\n<!-- WIKI:START -->\n"
        "This line is just documentation, no matching END nearby.\n\n" + body
    )
    notes.write_note(path, frontmatter, hand_written)

    with pytest.raises(ValueError):
        notes.merge_god_note(path, {"name": "Chiron"}, "New ability text.")

    # The failed attempt must not have touched the file at all.
    _, unchanged_body = notes.read_note(path)
    assert unchanged_body == hand_written


def test_merge_god_note_raises_on_marker_inside_code_fence(tmp_path):
    path = tmp_path / "Chiron.md"
    notes.merge_god_note(path, {"name": "Chiron"}, "Old ability text.")
    frontmatter, body = notes.read_note(path)

    # Known, accepted limitation: a properly fenced code block that quotes
    # the marker syntax as a documentation example (e.g. explaining the
    # pipeline convention to a future reader) still reads as real marker
    # lines to MARKER_LINE_RE — it can't tell "inside a code fence" from "a
    # real marker". Combined with the real block already in the file, that's
    # 4 marker lines total, which correctly raises rather than silently
    # guessing which pair is real. This test locks that behavior in rather
    # than letting it silently regress.
    hand_written = body + (
        "\n## Note format\nHere's how the pipeline marks its block:\n\n"
        "```\n<!-- WIKI:START -->\n...\n<!-- WIKI:END -->\n```\n"
    )
    notes.write_note(path, frontmatter, hand_written)

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


def test_log_refresh_diff_ignores_source_url_changes(tmp_path):
    log_dir = tmp_path / "_logs"
    notes.log_refresh_diff(
        log_dir, "Chiron",
        {"cost": 100, "source_url": "https://wiki.smite2.com/w/Chiron"},
        {"cost": 100, "source_url": "https://wiki.smite2.com/w/Chiron?v=2"},
    )
    assert not log_dir.exists()


def test_log_refresh_diff_ignores_last_verified_changes(tmp_path):
    """last_verified is set fresh on every single refresh (that's the whole
    point of staleness tracking) — it will differ on every run even when
    nothing else changed, so it must not itself count as a "change" or every
    diff-log entry would claim something changed when it didn't, drowning
    out genuinely useful diff signal."""
    log_dir = tmp_path / "_logs"
    notes.log_refresh_diff(
        log_dir, "Chiron",
        {"cost": 100, "last_verified": "2026-07-01"},
        {"cost": 100, "last_verified": "2026-07-16"},
    )
    assert not log_dir.exists()


def test_merge_suggested_entries_replaces_only_suggested(tmp_path):
    path = tmp_path / "Chiron-Conquest.md"
    notes.write_note(path, {
        "type": "smite-build", "god": "Chiron", "mode": "Conquest",
        "builds": [
            {"source": "community", "slot_order": [{"name": "Trans", "pick_rate": 0.9, "win_rate": 0.5}]},
            {"source": "mine", "slot_order": ["Deathbringer"]},
            {"source": "suggested", "archetype": "core", "slot_order": ["OLD"]},
        ],
    }, "")

    notes.merge_suggested_entries(path, "Chiron", "Conquest", [
        {"source": "suggested", "archetype": "core", "slot_order": ["NEW"]},
    ])

    fm, _ = notes.read_note(path)
    sources = [b["source"] for b in fm["builds"]]
    assert sources.count("community") == 1
    assert sources.count("mine") == 1
    assert sources.count("suggested") == 1
    suggested = next(b for b in fm["builds"] if b["source"] == "suggested")
    assert suggested["slot_order"] == ["NEW"]      # regenerated in place
    mine = next(b for b in fm["builds"] if b["source"] == "mine")
    assert mine["slot_order"] == ["Deathbringer"]  # untouched


def test_merge_suggested_entries_creates_note_when_missing(tmp_path):
    path = tmp_path / "New-Conquest.md"
    notes.merge_suggested_entries(path, "New", "Conquest",
                                  [{"source": "suggested", "slot_order": ["X"]}])
    fm, _ = notes.read_note(path)
    assert fm["god"] == "New"
    assert [b["source"] for b in fm["builds"]] == ["suggested"]


def test_upsert_mine_entry_adds_and_replaces_by_name(tmp_path):
    path = tmp_path / "Chiron-Conquest.md"
    notes.write_note(path, {"type": "smite-build", "god": "Chiron", "mode": "Conquest",
        "builds": [{"source": "community", "slot_order": []},
                   {"source": "suggested", "archetype": "core", "slot_order": ["A"]}]}, "")
    notes.upsert_mine_entry(path, "Chiron", "Conquest",
        {"name": "My Crit", "slot_order": ["Deathbringer"]})
    fm, _ = notes.read_note(path)
    mine = [b for b in fm["builds"] if b["source"] == "mine"]
    assert len(mine) == 1 and mine[0]["name"] == "My Crit" and mine[0]["source"] == "mine"
    assert [b["source"] for b in fm["builds"]].count("community") == 1  # preserved
    notes.upsert_mine_entry(path, "Chiron", "Conquest", {"name": "My Crit", "slot_order": ["Rage"]})
    fm, _ = notes.read_note(path)
    mine = [b for b in fm["builds"] if b["source"] == "mine"]
    assert len(mine) == 1 and mine[0]["slot_order"] == ["Rage"]


def test_delete_mine_entry_removes_only_that_one(tmp_path):
    path = tmp_path / "Chiron-Conquest.md"
    notes.write_note(path, {"type": "smite-build", "god": "Chiron", "mode": "Conquest",
        "builds": [{"source": "community", "slot_order": []},
                   {"source": "mine", "name": "A", "slot_order": []},
                   {"source": "mine", "name": "B", "slot_order": []}]}, "")
    notes.delete_mine_entry(path, "A")
    fm, _ = notes.read_note(path)
    names = [b.get("name") for b in fm["builds"] if b["source"] == "mine"]
    assert names == ["B"]
    assert any(b["source"] == "community" for b in fm["builds"])
