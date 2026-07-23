"""Data-integrity guard for scraped item data. Run after every regenerate as a
CI-style gate: non-zero exit + a readable finding list if anything is wrong.
Items only for now — a god/build audit is a later phase."""
import json
import re
import sys
from collections import Counter
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parents[2]
INDEX_PATH = VAULT_ROOT / "viewer" / "public" / "index.json"

STAT_VALUE_RE = re.compile(r"-?\d+\.?\d*")
TIER3_COST_MIN = 1800
TIER3_COST_MAX = 3600
STAT_VALUE_MAX = 1000


def _stat_findings(name, stats):
    findings = []
    if not isinstance(stats, dict):
        return findings
    for stat_name, value in stats.items():
        match = STAT_VALUE_RE.search(str(value))
        if match is None:
            findings.append({
                "item": name, "issue": "bad-stat-value",
                "detail": f"{stat_name}={value!r} has no numeric value",
            })
            continue
        num = float(match.group())
        if num < 0 or num > STAT_VALUE_MAX:
            findings.append({
                "item": name, "issue": "bad-stat-value",
                "detail": f"{stat_name}={value!r} out of range",
            })
    return findings


def audit_items(items: list) -> list:
    findings = []
    name_counts = Counter(n for it in items if (n := it.get("name")))

    for it in items:
        name = it.get("name")
        tier = it.get("tier")
        cost = it.get("cost")
        stats = it.get("stats") or {}
        is_numeric_tier = isinstance(tier, (int, float)) and not isinstance(tier, bool)

        if not cost:
            findings.append({
                "item": name, "issue": "blank-cost",
                "detail": f"cost is {cost!r}",
            })

        if tier is None or tier == "":
            findings.append({
                "item": name, "issue": "null-tier",
                "detail": f"tier is {tier!r}",
            })

        if not stats and is_numeric_tier:
            findings.append({
                "item": name, "issue": "empty-stats",
                "detail": f"numeric tier {tier!r} has no stats",
            })

        findings.extend(_stat_findings(name, stats))

        if tier == 3 and (cost is None or not (TIER3_COST_MIN <= cost <= TIER3_COST_MAX)):
            findings.append({
                "item": name, "issue": "tier3-cost-outlier",
                "detail": f"cost {cost!r} outside {TIER3_COST_MIN}-{TIER3_COST_MAX}",
            })

        if name and name_counts[name] > 1:
            findings.append({
                "item": name, "issue": "duplicate-name",
                "detail": f"name appears {name_counts[name]} times",
            })

    findings.sort(key=lambda f: (f["item"] or "", f["issue"]))
    return findings


def load_items() -> list:
    data = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    return data.get("items", [])


def main(argv=None) -> int:
    # Item names can contain non-ASCII characters (curly apostrophes, etc.).
    # A redirected/cron stdout may be on a non-UTF-8 codepage (cp437/cp1252 on
    # Windows), so make encoding failures replace instead of crashing the gate.
    try:
        sys.stdout.reconfigure(errors="replace")
    except Exception:
        pass

    try:
        items = load_items()
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        print(f"Item audit: could not load index.json ({exc})")
        return 1

    findings = audit_items(items)
    print(f"Item audit: {len(items)} items, {len(findings)} finding(s)")
    if not findings:
        print("no item issues found")
        return 0
    for f in findings:
        print(f"{f['item']}: {f['issue']} - {f['detail']}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
