"""Refuse a wiki stats refresh that turns a test red. Keep the old stats.

    python -m smite.stats_gate save  <dir>   # before smite.stats_refresh
    python -m smite.stats_gate check <dir>   # after it; restores <dir> on a red test

WHY. `smite.stats_refresh` validates SHAPE — nothing went null, nothing
collapsed, every number parses — and the job's two gates (`validate --check`,
`calibrate_combat`) check two numbers. Neither runs the ~1000 tests, and on
2026-11-02 the first unattended refresh (Open Beta 40 -> 46, PR #66's branch
run) turned fourteen of them red: one a real parser bug (Blinking Abyss read
`(+10% Strength & Intelligence)`, a damage ratio, as a stat, and became
buildable on it), the rest tests pinned to one patch's numbers. The daily job
does not run pytest, so all of it would have shipped to `main` silently.

WHAT IT DOES. `save` copies the files `stats_refresh` owns (`OWNED`) aside.
`check` compares them with what is live now. No change -> nothing to gate, no
test run. A change -> recompute builds and the index on the new stats (tests
read both), then run the suite. All green -> accepted. Any red -> the failing
tests are re-run on the OLD stats, and:

  * failing on new and passing on old: ATTRIBUTABLE to the refresh. The old
    stats are restored, the builds recomputed on them, each failing test
    printed as `::error::`, and `rejected=true` written to $GITHUB_OUTPUT so
    the job's last step fails the run AFTER the day's community data is
    committed. A stats problem never costs the community refresh, and a
    rejection is never silent: the run goes red and GitHub mails the owner.
  * failing on both: not the refresh's doing (main was already red, or
    community data moved it). The NEW stats are put back, accepted, and the
    failures printed as `::warning::`. Blocking a correct patch because of an
    unrelated red test would keep stale prices live for nothing.

FAIL-CLOSED. A crash in the gate, a suite that cannot be collected or that
writes no report, a timeout: every one restores the old stats and rejects.
The only path that keeps new stats is a suite that ran and either passed or
failed identically without them.

After a rejection `_stats_refresh.json` is the old one too, so the next run
is due again and re-fetches (~14 min) until a human fixes the test or the
data. That is the intended cost: a patch waits, it is not half-applied.
"""
import argparse
import filecmp
import json
import os
import shutil
import subprocess
import sys
import tempfile
import traceback
import xml.etree.ElementTree as ET
from pathlib import Path

from smite import snapshots

DATA_ROOT = snapshots.DATA_ROOT
PIPELINE = Path(__file__).resolve().parents[1]

# What `stats_refresh.run` writes: the swapped directories, the patch history
# and current label (`record_patch` / `write_current_patch`), and its state.
OWNED_DIRS = ("Gods", "Items")
OWNED_FILES = ("_patch.json", "_patch_history.json", "_stats_refresh.json")
MANIFEST = "manifest.json"
TEST_TIMEOUT = 40 * 60


# -- the copy ----------------------------------------------------------------

def save(data_root: Path, dest: Path) -> None:
    data_root, dest = Path(data_root), Path(dest)
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    present = []
    for d in OWNED_DIRS:
        if (data_root / d).is_dir():
            shutil.copytree(data_root / d, dest / d)
            present.append(d)
    for f in OWNED_FILES:
        if (data_root / f).is_file():
            shutil.copy2(data_root / f, dest / f)
            present.append(f)
    (dest / MANIFEST).write_text(json.dumps(sorted(present)), encoding="utf-8")


def restore(saved: Path, data_root: Path) -> None:
    """Make `data_root`'s owned paths exactly what `saved` holds — including
    removing a file that did not exist when it was saved."""
    saved, data_root = Path(saved), Path(data_root)
    present = set(json.loads((saved / MANIFEST).read_text(encoding="utf-8")))
    for d in OWNED_DIRS:
        if (data_root / d).exists():
            shutil.rmtree(data_root / d)
        if d in present:
            shutil.copytree(saved / d, data_root / d)
    for f in OWNED_FILES:
        if (data_root / f).exists():
            (data_root / f).unlink()
        if f in present:
            shutil.copy2(saved / f, data_root / f)


def _same_tree(a: Path, b: Path) -> bool:
    if a.is_dir() != b.is_dir():
        return False
    if not a.is_dir():
        return True
    cmp = filecmp.dircmp(a, b)
    if cmp.left_only or cmp.right_only or cmp.funny_files:
        return False
    _, mismatch, errors = filecmp.cmpfiles(a, b, cmp.common_files, shallow=False)
    if mismatch or errors:
        return False
    return all(_same_tree(a / s, b / s) for s in cmp.common_dirs)


def stats_changed(saved: Path, data_root: Path) -> bool:
    """Only the stats count. `_patch*.json` can move without a refresh (the
    wiki check records a label), and a label is not something a test reads."""
    return not all(_same_tree(Path(saved) / d, Path(data_root) / d) for d in OWNED_DIRS)


# -- running the suite ---------------------------------------------------------

class SuiteError(RuntimeError):
    """The suite did not produce a usable verdict. Treated as red."""


def recompute() -> None:
    for module in (["smite.recommend", "--all"], ["smite.build_index"]):
        subprocess.run([sys.executable, "-m", *module], cwd=PIPELINE, check=True,
                       stdout=subprocess.DEVNULL)


def run_suite(nodeids=None) -> set:
    """Node ids that failed or errored. `nodeids` narrows the run. Raises
    SuiteError when pytest wrote no report — a crash is not a pass."""
    with tempfile.TemporaryDirectory() as tmp:
        report = Path(tmp) / "junit.xml"
        cmd = [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", "-m", "not live",
               f"--junitxml={report}", "-o", "junit_family=xunit1"]
        cmd += sorted(nodeids) if nodeids else ["smite/tests"]
        try:
            proc = subprocess.run(cmd, cwd=PIPELINE, timeout=TEST_TIMEOUT,
                                  stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        except subprocess.TimeoutExpired as exc:
            raise SuiteError(f"suite timed out after {TEST_TIMEOUT}s") from exc
        tail = "\n".join(proc.stdout.strip().splitlines()[-3:])
        print(f"[stats gate] pytest exit {proc.returncode}: {tail}")
        if not report.exists():
            raise SuiteError(f"pytest wrote no report (exit {proc.returncode})")
        failed = failures_from_junit(report.read_text(encoding="utf-8"))
        # 0 = all passed, 1 = some failed. 5 = nothing collected is only
        # acceptable when we asked for specific ids that no longer exist.
        if proc.returncode not in (0, 1) and not (nodeids and proc.returncode == 5):
            raise SuiteError(f"pytest exit {proc.returncode}: {tail}")
        if proc.returncode == 1 and not failed:
            raise SuiteError("pytest reported failure but the report names no test")
        return failed


def failures_from_junit(xml_text: str) -> set:
    root = ET.fromstring(xml_text)
    out = set()
    for case in root.iter("testcase"):
        if case.find("failure") is None and case.find("error") is None:
            continue
        # xunit1 gives `file` (smite/tests/test_x.py) and `name` (test_y[param]).
        path = case.get("file")
        name = case.get("name")
        classname = case.get("classname", "")
        if not path:
            path = classname.replace(".", "/") + ".py"
        owner = classname.rsplit(".", 1)[-1]
        if owner and owner != Path(path).stem:
            name = f"{owner}::{name}"          # a test method on a Test* class
        out.add(f"{path}::{name}")
    return out


# -- the decision ------------------------------------------------------------

def check(saved: Path, data_root: Path = DATA_ROOT, suite=run_suite, recompute=recompute) -> dict:
    """{status, failed?, attributable?, preexisting?}. status is 'unchanged',
    'accepted', 'accepted-with-preexisting-failures' or 'rejected'. On
    'rejected' the old stats are back in place and recomputed."""
    saved, data_root = Path(saved), Path(data_root)
    if not stats_changed(saved, data_root):
        return {"status": "unchanged"}
    new_copy = Path(tempfile.mkdtemp(prefix="stats_gate_new_"))
    try:
        save(data_root, new_copy)
        try:
            recompute()
            failed = suite(None)
        except Exception as exc:
            _reject_restore(saved, data_root, recompute)
            return {"status": "rejected", "error": f"{type(exc).__name__}: {exc}", "attributable": []}
        if not failed:
            return {"status": "accepted"}

        restore(saved, data_root)
        try:
            recompute()
            failed_old = suite(failed)
        except Exception as exc:
            _reject_restore(saved, data_root, recompute)
            return {"status": "rejected", "failed": sorted(failed),
                    "error": f"re-run on the old stats failed: {type(exc).__name__}: {exc}",
                    "attributable": sorted(failed)}
        attributable = failed - failed_old
        if attributable:
            return {"status": "rejected", "failed": sorted(failed),
                    "attributable": sorted(attributable),
                    "preexisting": sorted(failed & failed_old)}
        restore(new_copy, data_root)
        recompute()
        return {"status": "accepted-with-preexisting-failures", "preexisting": sorted(failed)}
    finally:
        shutil.rmtree(new_copy, ignore_errors=True)


def _reject_restore(saved, data_root, recompute) -> None:
    restore(saved, data_root)
    try:
        recompute()
    except Exception:
        # The old stats are on disk; the job's own recompute step runs next.
        traceback.print_exc(file=sys.stdout)


def report(result: dict) -> str:
    s = result["status"]
    if s == "unchanged":
        return "[stats gate] no item or god stat changed — nothing to gate"
    if s == "accepted":
        return "[stats gate] accepted: the full suite passes on the new stats"
    if s == "accepted-with-preexisting-failures":
        lines = [f"::warning::[stats gate] accepted, but {len(result['preexisting'])} test(s) fail "
                 "with the old stats too — not the refresh's doing:"]
        return "\n".join(lines + [f"::warning::  {t}" for t in result["preexisting"]])
    lines = ["::error::[stats gate] REJECTED the stats refresh — the old item and god stats are "
             "kept. The community data still commits; this run will fail at its last step."]
    if result.get("error"):
        lines.append(f"::error::  {result['error']}")
    for t in result.get("attributable") or []:
        lines.append(f"::error::  fails on the new stats, passes on the old: {t}")
    for t in result.get("preexisting") or []:
        lines.append(f"::warning::  fails on both (not the refresh's doing): {t}")
    return "\n".join(lines)


def _github_outputs(result: dict) -> None:
    rejected = result["status"] == "rejected"
    out = os.environ.get("GITHUB_OUTPUT")
    if out:
        with open(out, "a", encoding="utf-8") as fh:
            fh.write(f"rejected={'true' if rejected else 'false'}\n")
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary and result["status"] != "unchanged":
        with open(summary, "a", encoding="utf-8") as fh:
            fh.write(f"### Stats gate: {result['status']}\n\n")
            for t in result.get("attributable") or []:
                fh.write(f"- fails on the new stats, passes on the old: `{t}`\n")
            for t in result.get("preexisting") or []:
                fh.write(f"- fails on both: `{t}`\n")
            if result.get("error"):
                fh.write(f"- {result['error']}\n")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Refuse a stats refresh that turns a test red")
    ap.add_argument("action", choices=["save", "check"])
    ap.add_argument("dir", type=Path, help="where the pre-refresh copy lives")
    args = ap.parse_args(argv)
    if args.action == "save":
        save(DATA_ROOT, args.dir)
        print(f"[stats gate] saved the current stats to {args.dir}")
        return 0
    try:
        result = check(args.dir)
    except Exception as exc:
        traceback.print_exc(file=sys.stdout)
        try:
            _reject_restore(args.dir, DATA_ROOT, recompute)
        except Exception:
            traceback.print_exc(file=sys.stdout)
            print("::error::[stats gate] could not restore the old stats — failing the job "
                  "so nothing commits")
            return 1
        result = {"status": "rejected", "error": f"gate crashed: {type(exc).__name__}: {exc}",
                  "attributable": []}
    print(report(result))
    _github_outputs(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
