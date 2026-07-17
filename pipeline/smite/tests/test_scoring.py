from smite import scoring


def test_load_weights_missing_file_returns_defaults(tmp_path):
    w = scoring.load_weights(tmp_path / "nope.yaml")
    assert w["signals"]["efficiency"] == 0.35
    assert w["signals"]["win"] == 0.30
    assert w["signals"]["pick"] == 0.15
    assert w["signals"]["fit"] == 0.20


def test_load_weights_file_overrides_defaults(tmp_path):
    p = tmp_path / "_weights.yaml"
    p.write_text("signals:\n  efficiency: 0.5\n", encoding="utf-8")
    w = scoring.load_weights(p)
    assert w["signals"]["efficiency"] == 0.5
    # unspecified keys fall back to defaults
    assert w["signals"]["win"] == 0.30


def test_load_tags_missing_file_returns_empty(tmp_path):
    assert scoring.load_tags(tmp_path / "nope.yaml") == {}


def test_load_tags_reads_mapping(tmp_path):
    p = tmp_path / "_tags.yaml"
    p.write_text("Brawler's Ruin:\n  - anti-heal\n", encoding="utf-8")
    assert scoring.load_tags(p) == {"Brawler's Ruin": ["anti-heal"]}
