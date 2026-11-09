"""Invariants of the COMMITTED aspect store and the Conquest notes derived
from it. Separate from `test_aspect_matches.py` (the parser, guard and rules on
fixtures) because these read `data/` and so describe the data, not the code."""
import json
import re

from smite import aspect_matches as am
from smite import notes


STORE_FILES = sorted(am.STORE_ROOT.glob("*/*.jsonl"))


def test_the_committed_store_holds_only_the_stored_fields():
    """The privacy rule as a test: no field beyond RECORD_KEYS, and no GUID."""
    guid = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-", re.I)
    assert STORE_FILES, "the aspect store is empty"
    for path in STORE_FILES:
        text = path.read_text(encoding="utf-8")
        assert not guid.search(text), path
        for line in text.splitlines():
            r = json.loads(line)
            assert tuple(r) == am.RECORD_KEYS, path
            assert re.fullmatch(r"[0-9a-f]{16}", r["m"]), path


def test_every_committed_record_sits_in_its_own_window():
    meta = am.load_meta()
    for path in STORE_FILES:
        times = []
        for line in path.read_text(encoding="utf-8").splitlines():
            r = json.loads(line)
            assert am.window_of(r["t"], meta) == path.parent.name, (path, r["t"])
            times.append((r["t"], r["m"]))
        assert times == sorted(times) and len({m for _, m in times}) == len(times), path


def test_the_conquest_notes_say_what_the_store_says():
    meta, aggregate = am.load_meta(), am.load_aggregate()
    names, changes = am.item_name_lookup(), am.item_changes()
    for path in sorted(am.BUILDS_ROOT.glob("*-Conquest.md")):
        fm, _ = notes.read_note(path)
        block = am.note_block(fm["god"], am.base_role_of(fm["god"]), am.STORE_ROOT,
                              meta, aggregate, names, changes)
        assert fm.get("community_aspects") == block, f"{path.name}: run aspect_matches derive"


def test_tsukuyomi_mangetsu_is_shown_from_the_committed_store():
    """The acceptance case, on the live store. Its closed windows can only
    grow, and OB45 alone holds 30, so whatever the newer windows add the walk
    never needs OB44 and the entry never goes back to `below minimum` — unless
    a retention policy drops OB45, which should turn this red on purpose. The
    exact read is pinned on a frozen copy in `test_aspect_matches.py`."""
    fm, _ = notes.read_note(am.BUILDS_ROOT / "Tsukuyomi-Conquest.md")
    entry = next(a for a in fm["community_aspects"]["aspects"] if a["aspect"] == "Aspect of Mangetsu")
    counts = entry["matches_by_window"]
    assert counts.get("ob46", 0) >= 21 and counts.get("ob45", 0) >= 30
    assert entry["status"] == "shown" and entry["matches"] >= am.MIN_MATCHES
    assert "ob44" not in entry["windows"]
    assert entry["base_role"] == "Jungle"


def test_every_shown_entry_names_the_patches_it_pools():
    meta = am.load_meta()
    for path in sorted(am.BUILDS_ROOT.glob("*-Conquest.md")):
        fm, _ = notes.read_note(path)
        for a in (fm.get("community_aspects") or {}).get("aspects", []):
            if a["status"] != "shown":
                assert set(a) == {"aspect", "status", "matches_by_window"}, path.name
                continue
            pool = a["windows"]
            assert a["patches"] == am.patch_label(pool), path.name
            assert a["matches"] == sum(a["matches_by_window"].get(w, 0) for w in pool), path.name
            assert (len(pool) > 1) == (a["window_rule"] == "pooled back"), path.name
            assert all(w in meta["windows"] for w in pool), path.name


def test_a_window_the_backfill_did_not_reach_whole_says_so():
    """A window starting before `complete_from` carries `partial_from` equal
    to it (the source's retention cut its start); every other window carries
    none. No window is silently short."""
    meta = am.load_meta()
    assert meta["complete_from"]
    for w, span in meta["windows"].items():
        if span["start"] < meta["complete_from"]:
            assert span.get("partial_from") == meta["complete_from"], w
        else:
            assert "partial_from" not in span, w
