"""`data/_passive_classes.yaml` — the passive catalogue — held to the pool.

The catalogue is a hand-authored sidecar like `_tags.yaml`, and like the tags
it is only worth anything while it is COMPLETE: a buildable item whose passive
nobody has classified is exactly the item the next carve-out would miss. Three
things are pinned here, and each is a way the file could go quietly stale:

  * every god-agnostic buildable item with passive text has an entry, and the
    file names no item outside that set — a rename or a new item fails here
    rather than being silently uncatalogued;
  * every class code an entry uses is declared in the file's own vocabulary,
    with its family letter agreeing with the code;
  * an item's `priced` list agrees with what the SHIPPED pricing flags actually
    do to its stat line. This is the one that ties the document to the model:
    a carve-out that ships has to come here and say which clause it priced,
    and a `priced` claim about a clause nothing reprices is refused.

Reads the real data files rather than a fixture, because the claim being
tested is about the real pool. See docs/PASSIVES.md for the argument.
"""
import io

import yaml

from smite import build_quality, recommend, scoring

CATALOGUE_PATH = recommend.DATA_ROOT / "_passive_classes.yaml"


def _load():
    return yaml.safe_load(io.open(CATALOGUE_PATH, encoding="utf-8"))


def _pool_with_passive(items):
    return {it["name"] for it in items
            if scoring.is_buildable(it) and (it.get("passive") or "").strip()}


def test_catalogue_covers_exactly_the_buildable_items_with_passive_text():
    cat = _load()
    pool = _pool_with_passive(recommend.load_items())
    entries = set(cat["items"])
    assert pool - entries == set(), f"uncatalogued: {sorted(pool - entries)}"
    assert entries - pool == set(), f"catalogued but not in the pool: {sorted(entries - pool)}"


def test_every_class_code_is_declared_and_carries_its_family_letter():
    cat = _load()
    vocabulary = cat["classes"]
    for code, spec in vocabulary.items():
        assert spec["family"] == code[0], f"{code} declares family {spec['family']}"
        assert spec.get("name") and spec.get("what")
    for name, entry in cat["items"].items():
        classes = entry.get("classes") or []
        assert classes, f"{name} has no classes"
        unknown = [c for c in classes if c not in vocabulary]
        assert not unknown, f"{name} uses undeclared class(es) {unknown}"
        assert len(set(classes)) == len(classes), f"{name} repeats a class"
        for c in entry.get("priced") or []:
            assert c in classes, f"{name} prices {c} but does not list it"


def test_priced_clauses_agree_with_the_shipped_pricing_flags():
    cat = _load()
    items = recommend.load_items()
    weights = scoring.load_weights(recommend.WEIGHTS_PATH)
    printed, priced = build_quality._stat_lines(items, weights)
    repriced = {n for n in printed if printed[n] != priced[n]}
    pool = _pool_with_passive(items)
    claimed = {n for n, e in cat["items"].items() if e.get("priced")}
    assert claimed == (repriced & pool), (
        f"claims pricing but the flags do not reprice: {sorted(claimed - repriced)}; "
        f"repriced by the flags but the catalogue does not say so: {sorted((repriced & pool) - claimed)}")
