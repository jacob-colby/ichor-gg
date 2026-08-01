"""Write or delete a user 'mine' build from a JSON payload on stdin. Invoked by
the viewer's local write endpoint. Validates god + mode + item names so a
malicious/mistyped payload can't traverse paths or inject junk. Data flows via
stdin JSON only — never shell-interpolated.

Payload: {"action": "save"|"delete", "god": str, "mode": str, "name": str,
          "slot_order": [str], "starter": {"base","upgrade"}?, "notes": str?}
"""
import json
import sys
from pathlib import Path

from smite import notes

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_ROOT = REPO_ROOT / "data"
BUILDS_ROOT = REPO_ROOT / "data" / "builds"
MODES = {"Conquest", "Joust", "Arena"}


def _known(dir_name):
    d = DATA_ROOT / dir_name
    return {notes.read_note(p)[0].get("name") for p in d.glob("*.md")} if d.exists() else set()


def _fail(msg):
    print(json.dumps({"ok": False, "error": msg}))
    return 1


def main(argv=None):
    try:
        payload = json.load(sys.stdin)
    except Exception as exc:
        return _fail(f"bad payload: {exc}")

    god, mode = payload.get("god"), payload.get("mode")
    if god not in _known("Gods") or mode not in MODES:
        return _fail("unknown god or mode")
    path = BUILDS_ROOT / f"{god}-{mode}.md"

    action = payload.get("action")
    if action == "delete":
        notes.delete_mine_entry(path, payload.get("name"))
    elif action == "save":
        name = (payload.get("name") or "").strip()
        if not name:
            return _fail("name required")
        items = _known("Items")
        entry = {"name": name, "slot_order": [s for s in (payload.get("slot_order") or []) if s in items]}
        starter = payload.get("starter") or {}
        if starter.get("base") in items and starter.get("upgrade") in items:
            entry["starter"] = {"base": starter["base"], "upgrade": starter["upgrade"]}
        if payload.get("notes"):
            entry["notes"] = str(payload["notes"])
        notes.upsert_mine_entry(path, god, mode, entry)
    else:
        return _fail("unknown action")

    print(json.dumps({"ok": True}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
