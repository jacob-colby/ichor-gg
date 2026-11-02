"""What in a community build is a TARGET Ichor can be compared against.

A community Conquest "six-item build" is what players were holding when the
match ended, slot by slot. Two kinds of slot in it are not a disagreement with
Ichor, and counting them as one put a quarter of the "Ichor vs community" gap
on things the model was never asked to answer (passives analysis, 2026-11-02):

  unfinished   A tier-1/2 COMPONENT — Evil Eye, Sage's Ring, Medal of Defense,
               Skeggox. Games end before six items are built, so slot 6 holds a
               half-built item on most gods (61 of 90 on 2026-11-02) and slot 5
               on 11. Nobody recommends finishing a build on a component, and
               Ichor never buys one, so the slot is DROPPED from the target.

  unscoreable  A finished purchase Ichor cannot read: an item `scoring.
               is_buildable` refuses for this god only because it has NO STAT
               LINE — a statless relic (Blinking Abyss, Sundering Echo) or a
               statless god-specific item (Vulcan's Mods, Genie's Lamp). It is
               real, and Ichor is blind to it, which is a different statement
               from "Ichor disagrees". Counted as its own labelled class, never
               as a disagreement and never as agreement.

Everything else is `scored`: a buildable item for this god, the thing the
comparison is actually about. A paid relic WITH stats (Shell of Rebuke) is
scored, because Ichor scores it.

THIS IS A COMPARISON LENS, NEVER A MODEL INPUT. `scoring`, `assemble`,
`recommend` and `build_index`'s recommendation fields do not import it — the
community slots keep feeding win and pick exactly as before, so nothing the
site recommends changes. A test pins that boundary.

    python -m smite.community_target      # agreement before and after the cleanup
"""
import json
import sys
from pathlib import Path

from smite import scoring

SCORED = "scored"
UNFINISHED = "unfinished"
UNSCOREABLE = "unscoreable"
UNKNOWN = "unknown"          # a name the item pool does not carry at all

REPO_ROOT = Path(__file__).resolve().parents[2]
INDEX_PATH = REPO_ROOT / "viewer" / "public" / "index.json"


def slot_class(item, god=None) -> str:
    """One community slot's class. `god` is the god's name (or record), so a god-specific
    item with stats (Ratatoskr's acorns) is scored for its owner."""
    if item is None:
        return UNKNOWN
    tier = item.get("tier")
    if isinstance(tier, (int, float)) and not isinstance(tier, bool) and tier < 3:
        return UNFINISHED
    god_rec = {"name": god} if isinstance(god, str) else god
    if scoring.is_buildable(item, god_rec):
        return SCORED
    # Not buildable and not a component: a statless relic or god-specific item
    # (the case this class exists for), or a free base relic, which reaches no
    # community build. Either way Ichor cannot score it, which is not the same
    # as disagreeing with it.
    return UNSCOREABLE


def _name(slot):
    return slot.get("name") if isinstance(slot, dict) else slot


def split(slots, items_by_name, god=None) -> dict:
    """`{class: [names]}` over a community `slot_order`, order kept."""
    out = {SCORED: [], UNFINISHED: [], UNSCOREABLE: [], UNKNOWN: []}
    for s in slots or []:
        n = _name(s)
        out[slot_class(items_by_name.get(n), god)].append(n)
    return out


def target(slots, items_by_name, god=None) -> list:
    """The names a comparison should score against: the `scored` class."""
    return split(slots, items_by_name, god)[SCORED]


def agreement(ours, slots, items_by_name, god=None) -> dict:
    """One god's agreement, raw and cleaned.

    raw      every community slot is a target, as every comparison did before.
    cleaned  unfinished slots dropped; unscoreable slots counted apart."""
    ours = set(ours or [])
    names = [_name(s) for s in slots or []]
    parts = split(slots, items_by_name, god)
    raw_shared = sum(1 for n in names if n in ours)
    shared = sum(1 for n in parts[SCORED] if n in ours)
    return {
        "raw_slots": len(names), "raw_shared": raw_shared,
        "raw_disagree": len(names) - raw_shared,
        "target": len(parts[SCORED]), "shared": shared,
        "disagree": len(parts[SCORED]) - shared,
        "unfinished": parts[UNFINISHED], "unscoreable": parts[UNSCOREABLE],
        "unknown": parts[UNKNOWN],
    }


def _community_entry(note):
    for b in note.get("builds") or []:
        if b.get("source") == "community":
            return b
    return None


def _model_core(note, archetype="core"):
    for b in note.get("builds") or []:
        if (b.get("source") == "suggested" and b.get("archetype") == archetype
                and not b.get("aspect") and not b.get("fun")):
            return [_name(s) for s in b.get("slot_order") or []]
    return []


def index_agreement(index, mode="Conquest", archetype="core") -> dict:
    """Per-god and pooled agreement over the shipped index: Ichor's shipped
    `core` (base kit) against the first community entry, the same pair the
    viewer's ledger draws."""
    items_by_name = {it["name"]: it for it in index.get("items") or []}
    per_god = {}
    for note in index.get("builds") or []:
        if note.get("mode") != mode:
            continue
        comm = _community_entry(note)
        ours = _model_core(note, archetype)
        if not comm or not ours:
            continue
        per_god[note["god"]] = agreement(ours, comm.get("slot_order"), items_by_name, note["god"])
    return {"per_god": per_god, "pooled": pooled(per_god)}


def pooled(per_god) -> dict:
    v = list(per_god.values())
    s = lambda k: sum(x[k] for x in v)
    n_unf = sum(len(x["unfinished"]) for x in v)
    n_uns = sum(len(x["unscoreable"]) for x in v)
    raw_dis, dis = s("raw_disagree"), s("disagree")
    mean = lambda f: sum(f(x) for x in v) / len(v) if v else 0.0
    return {
        "gods": len(v),
        "raw_slots": s("raw_slots"), "raw_shared": s("raw_shared"), "raw_disagree": raw_dis,
        "raw_agreement": s("raw_shared") / s("raw_slots") if v and s("raw_slots") else 0.0,
        "raw_mean_agreement": mean(lambda x: x["raw_shared"] / x["raw_slots"] if x["raw_slots"] else 0.0),
        "target": s("target"), "shared": s("shared"), "disagree": dis,
        "agreement": s("shared") / s("target") if v and s("target") else 0.0,
        "mean_agreement": mean(lambda x: x["shared"] / x["target"] if x["target"] else 0.0),
        "unfinished": n_unf, "unscoreable": n_uns,
        "unknown": sum(len(x["unknown"]) for x in v),
        # Of the raw disagreements, the share that was never a model error.
        "not_a_disagreement": (n_unf + n_uns) / raw_dis if raw_dis else 0.0,
    }


def format_report(result) -> str:
    p = result["pooled"]
    lines = [
        f"Ichor `core` vs community Conquest build, {p['gods']} gods",
        "",
        f"  before cleanup  {p['raw_shared']}/{p['raw_slots']} community slots shared "
        f"({p['raw_agreement']:.1%} pooled, {p['raw_mean_agreement']:.1%} mean per god); "
        f"{p['raw_disagree']} counted as disagreements",
        f"  after cleanup   {p['shared']}/{p['target']} scored slots shared "
        f"({p['agreement']:.1%} pooled, {p['mean_agreement']:.1%} mean per god); "
        f"{p['disagree']} disagreements",
        f"  dropped         {p['unfinished']} unfinished component slots",
        f"  separate class  {p['unscoreable']} unscoreable slots (statless relics, god Mods)",
        f"  => {p['not_a_disagreement']:.0%} of the old disagreements were not a model error",
    ]
    if p["unknown"]:
        lines.append(f"  unknown         {p['unknown']} slots name an item the pool lacks")
    return "\n".join(lines)


def main(argv=None) -> int:
    try:
        sys.stdout.reconfigure(errors="replace")
    except Exception:
        pass
    index = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    print(format_report(index_agreement(index)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
