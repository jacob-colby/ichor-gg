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


def _god(name, damage_type, role, specs):
    return {"name": name, "damage_type": damage_type, "role": role, "specializations": specs}


def test_item_damage_type_from_primary_stat():
    assert scoring.item_damage_type({"stats": {"Strength": "40"}}) == "physical"
    assert scoring.item_damage_type({"stats": {"Intelligence": "70"}}) == "magical"
    assert scoring.item_damage_type({"stats": {"Physical Protection": "50"}}) == "neutral"


def test_passes_damage_filter_excludes_mismatched_offense():
    phys_god = _god("Ullr", "physical", "Hunter", ["Hunter"])
    int_item = {"stats": {"Intelligence": "70"}}
    str_item = {"stats": {"Strength": "40"}}
    neutral_item = {"stats": {"Physical Protection": "50"}}
    assert scoring.passes_damage_filter(str_item, phys_god)
    assert not scoring.passes_damage_filter(int_item, phys_god)
    assert scoring.passes_damage_filter(neutral_item, phys_god)  # neutral always passes


def test_god_fit_rewards_role_relevant_stats():
    weights = scoring.load_weights_default()
    sharpshooter = _god("Chiron", "physical", "Carry", ["Sharpshooter"])
    crit_item = {"stats": {"Critical Chance": "20%", "Attack Speed": "15"}}
    off_stat_item = {"stats": {"Magical Protection": "50"}}
    assert scoring.god_fit_score(crit_item, sharpshooter, weights, []) > \
        scoring.god_fit_score(off_stat_item, sharpshooter, weights, [])
