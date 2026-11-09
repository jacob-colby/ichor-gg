"""The scheduled workflow is a caller like any other, and it is the one caller
nothing else tests.

F9 of the 2026-08-23 audit was a dead patch-notes page. The cause was not a bug
in `snapshots.py` — every function in it worked and was tested. The cause was
that the only code path calling `write_snapshot` was `refresh_and_deploy`, a
manual patch-day command, and the daily job did not invoke it. A unit test
cannot see that. Reading the YAML can.
"""
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys

import pytest
import yaml

WORKFLOWS = pathlib.Path(__file__).resolve().parents[3] / ".github" / "workflows"


def _steps(workflow_name: str, job: str = None):
    spec = yaml.safe_load((WORKFLOWS / workflow_name).read_text(encoding="utf-8"))
    jobs = spec["jobs"]
    return jobs[job or next(iter(jobs))]["steps"]


def _run_text(workflow_name: str, job: str = None) -> str:
    return "\n".join(step.get("run", "") for step in _steps(workflow_name, job))


def test_the_daily_job_banks_a_snapshot():
    """Without this the patch-notes store never gets a second file, and
    `patch_notes` is `[]` forever."""
    assert "smite.snapshots" in _run_text("refresh-data.yml")


def test_the_snapshot_is_banked_before_the_index_is_built():
    """`build_index` READS the store to build `patch_notes`. Banked after, a
    change ships one refresh late — the run that scraped it publishes an index
    that cannot see it."""
    runs = [step.get("run", "") for step in _steps("refresh-data.yml")]
    snapshot_at = next(i for i, r in enumerate(runs) if "smite.snapshots" in r)
    index_at = next(i for i, r in enumerate(runs) if "smite.build_index" in r)
    assert snapshot_at < index_at


def test_the_daily_job_commits_the_snapshot_store():
    """It lives under `data/`, which the job stages wholesale — but `data/_cache`
    is un-staged by name right after, so this asserts the store is not swept up
    in some future exclusion."""
    text = _run_text("refresh-data.yml")
    assert "git add data" in text
    assert "data/Analysis" not in text.split("git reset")[-1]


def test_the_daily_job_detects_patches_before_the_index_is_built():
    """`build_index` reads `_patch.json` for the label and the history for
    period attribution; detected after, a new patch ships one day late."""
    runs = [step.get("run", "") for step in _steps("refresh-data.yml")]
    feed_at = next(i for i, r in enumerate(runs) if "smite.patch_feed" in r)
    index_at = next(i for i, r in enumerate(runs) if "smite.build_index" in r)
    assert feed_at < index_at


# -- the watcher -------------------------------------------------------------
#
# The decision this encodes: automated DETECTION, manual ACTION. A scheduled
# `refresh --all` would not have found Ravana (it re-pulls only what is already
# tracked) and could not be gated safely (blanking three gods' kits PASSes
# `validate --check` and yields zero `data_audit` findings). So the scheduled
# job may read the wiki and must never write from it.

def test_the_watcher_is_scheduled():
    spec = yaml.safe_load((WORKFLOWS / "watch-wiki.yml").read_text(encoding="utf-8"))
    # PyYAML resolves the unquoted key `on` to the boolean True (YAML 1.1).
    triggers = spec.get("on", spec.get(True))
    assert "schedule" in triggers


def test_the_watcher_never_writes_data():
    """The load-bearing property. If this job ever commits, the whole argument
    for keeping the scrape manual has been quietly reversed."""
    text = _run_text("watch-wiki.yml")
    for forbidden in ("git commit", "git push", "git add",
                      "smite.refresh", "smite.recommend", "smite.build_index"):
        assert forbidden not in text, f"the watcher must not run `{forbidden}`"


def test_the_watcher_has_no_write_access_to_the_repo():
    spec = yaml.safe_load((WORKFLOWS / "watch-wiki.yml").read_text(encoding="utf-8"))
    assert spec["permissions"]["contents"] == "read"
    assert spec["permissions"]["issues"] == "write"


def test_the_two_scheduled_jobs_do_not_share_a_slot():
    """Both open a checkout of the same repo; queueing them together buys
    nothing and makes a failure harder to read."""
    crons = {}
    for name in ("refresh-data.yml", "watch-wiki.yml"):
        spec = yaml.safe_load((WORKFLOWS / name).read_text(encoding="utf-8"))
        triggers = spec.get("on", spec.get(True))
        crons[name] = [s["cron"] for s in triggers["schedule"]]
    assert crons["refresh-data.yml"] != crons["watch-wiki.yml"]


# -- the stats refresh -------------------------------------------------------

def test_the_daily_job_refreshes_stats_between_patch_detection_and_the_snapshot():
    """After `patch_feed`, because it is due only when the feed has seen a
    newer patch than the data. Before `snapshots`, because the snapshot is
    what turns the new stats into that patch's notes."""
    runs = [step.get("run", "") for step in _steps("refresh-data.yml")]
    feed_at = next(i for i, r in enumerate(runs) if "smite.patch_feed" in r)
    stats_at = next(i for i, r in enumerate(runs) if "smite.stats_refresh" in r)
    snap_at = next(i for i, r in enumerate(runs) if "smite.snapshots" in r)
    assert feed_at < stats_at < snap_at


def test_the_stats_refresh_is_gated_before_anything_is_committed():
    runs = [step.get("run", "") for step in _steps("refresh-data.yml")]
    stats_at = next(i for i, r in enumerate(runs) if "smite.stats_refresh" in r)
    commit_at = next(i for i, r in enumerate(runs) if "git commit" in r)
    for gate in ("smite.validate --check", "smite.calibrate_combat"):
        gate_at = next(i for i, r in enumerate(runs) if gate in r)
        assert stats_at < gate_at < commit_at


# -- the test gate -----------------------------------------------------------
#
# 2026-11-02: the first unattended stats refresh turned fourteen tests red,
# and the job did not run pytest. These pin the gate's place in the job.

def _index(runs, needle):
    return next(i for i, r in enumerate(runs) if needle in r)


def test_the_stats_are_set_aside_before_the_refresh_and_gated_after_it():
    runs = [step.get("run", "") for step in _steps("refresh-data.yml")]
    save_at = _index(runs, "smite.stats_gate save")
    stats_at = _index(runs, "smite.stats_refresh")
    check_at = _index(runs, "smite.stats_gate check")
    assert _index(runs, "smite.patch_feed") < save_at < stats_at < check_at


def test_the_gate_runs_before_the_snapshot_the_recompute_and_the_commit():
    """A rejected refresh must bank no patch-notes snapshot and reach no
    commit; restoring after either would be too late."""
    runs = [step.get("run", "") for step in _steps("refresh-data.yml")]
    check_at = _index(runs, "smite.stats_gate check")
    assert check_at < _index(runs, "smite.snapshots")
    assert check_at < _index(runs, "smite.recommend --all")
    assert check_at < _index(runs, "git commit")


def test_the_gate_compares_against_the_copy_the_save_step_made():
    runs = [step.get("run", "") for step in _steps("refresh-data.yml")]
    save = runs[_index(runs, "smite.stats_gate save")].split("save", 1)[1].strip()
    check = runs[_index(runs, "smite.stats_gate check")].split("check", 1)[1].strip()
    assert save == check and "RUNNER_TEMP" in save


def test_the_gate_is_not_allowed_to_fail_open():
    steps = _steps("refresh-data.yml")
    gate = next(s for s in steps if "smite.stats_gate check" in s.get("run", ""))
    assert not gate.get("continue-on-error")
    assert gate.get("id") == "stats_gate"


def test_a_rejection_fails_the_run_after_the_commit():
    """Last, so the community data still lands; present, so a rejection is a
    red run and not a line in a green log.

    FOUR of these reporters now. The third fires when the day's data is stuck
    in a pull request nobody can merge, and it arrived with the reroute off
    `git push` to main; the fourth when the per-aspect match feed was refused
    (`smite.aspect_matches`). Each holds the same contract as the first two:
    it comes after the data is safe, and it turns a quiet problem into a red
    run.

    AND EACH REPORTS INDEPENDENTLY. A step runs by default only if every step
    before it succeeded, so three terminal reporters in a row meant the first
    `exit 1` suppressed the others' messages. That was a latent bug in the
    original PAIR rather than something the third step introduced: a run with
    both a rejected stats refresh and a left-out entity only ever told you
    about the first. `!cancelled()` on each condition is the fix, pinned here
    so the suppression cannot come back.

    FIVE since 2026-11-09: a run whose figures step failed has committed
    yesterday's docs/CURRENT.md, which turns `doc_audit` red on main for every
    session, so it is a red run too — reported last, like the others, so the
    data it did not block still lands."""
    steps = _steps("refresh-data.yml")
    runs = [s.get("run", "") for s in steps]
    conds = ["steps.stats_gate.outputs.rejected",
             "steps.new_entities.outputs.rejected",
             "steps.aspect_feed.outputs.rejected",
             "steps.figures.outcome",
             "steps.data_pr.outputs.landed"]
    fails = [next(i for i, s in enumerate(steps) if cond in str(s.get("if", "")))
             for cond in conds]
    # The reporters are the run's last steps, after the data is safe.
    assert sorted(fails) == list(range(len(steps) - len(conds), len(steps)))
    for fail in fails:
        assert "exit 1" in runs[fail]
        assert _index(runs, "git commit") < fail
        # Independent of whether an earlier reporter already failed.
        assert "!cancelled()" in str(steps[fail].get("if", ""))


def test_the_aspect_feed_runs_after_the_community_pull_and_cannot_cost_the_day():
    """`smite.aspect_matches refresh` is all or nothing and exits 1 on a
    refusal. The step must turn that into an output, not a failed step: a
    failed step skips everything after it, including the commit, and a refused
    aspect feed has already left its store untouched. Its reporter is checked
    with the others in `test_a_rejection_fails_the_run_after_the_commit`."""
    steps = _steps("refresh-data.yml")
    runs = [s.get("run", "") for s in steps]
    feed = next(s for s in steps if "smite.aspect_matches refresh" in s.get("run", ""))
    at = steps.index(feed)
    assert feed.get("id") == "aspect_feed"
    assert not feed.get("continue-on-error")
    assert "rejected=true" in feed["run"] and "GITHUB_OUTPUT" in feed["run"]
    assert feed["run"].strip().startswith("if ! python -m smite.aspect_matches refresh")
    assert _index(runs, "smite.refresh --community") < at < _index(runs, "git commit")
    # Before the recompute and the index, so the day's notes and index see it.
    assert at < _index(runs, "smite.recommend --all")


def test_the_aspect_entries_are_rederived_after_every_step_that_feeds_them():
    """An entry flags an item whose stats moved after the windows it reads
    (the snapshot store) and names items from the item notes. The stats
    refresh, the new-entity step and the snapshot all run AFTER the aspect
    feed, so on a patch day the feed step's notes would be stale against the
    day's own snapshot, and `test_the_conquest_notes_say_what_the_store_says`
    would fail the data PR. `derive` reads only the disk."""
    runs = [s.get("run", "") for s in _steps("refresh-data.yml")]
    derive = _index(runs, "smite.aspect_matches derive")
    for feeder in ("smite.aspect_matches refresh", "smite.stats_refresh",
                   "smite.new_entities", "python -m smite.snapshots"):
        assert _index(runs, feeder) <= derive, feeder
    assert derive <= _index(runs, "smite.recommend --all") < _index(runs, "git commit")


def test_the_aspect_store_is_not_ignored_by_git():
    """`git add data` stages it only if no ignore rule swallows it."""
    root = WORKFLOWS.parents[1]
    probe = "data/Analysis/aspect_matches/ob99/some-god.jsonl"
    proc = subprocess.run(["git", "check-ignore", "-q", probe], cwd=root)
    assert proc.returncode == 1, f"{probe} is git-ignored"


def test_new_entities_run_after_the_stats_gate_and_before_the_recompute():
    """After, so the two gates never blame each other's change; before the
    snapshot and recompute, so the day's index carries what was added."""
    runs = [s.get("run", "") for s in _steps("refresh-data.yml")]
    add = _index(runs, "smite.new_entities")
    assert _index(runs, "smite.stats_gate check") < add < _index(runs, "smite.snapshots")
    assert add < _index(runs, "smite.recommend --all")


def test_the_daily_job_regenerates_the_current_figures_from_its_own_output():
    """After the recompute, because `doc_figures` reads the index and builds it
    writes; before the commit, because the commit must carry the figures. In
    any other order the data PR lands yesterday's figures and `doc_audit` is
    red on main for every session — the failure this step exists to end."""
    steps = _steps("refresh-data.yml")
    runs = [s.get("run", "") for s in steps]
    figures = _index(runs, "smite.doc_figures --write")
    assert _index(runs, "smite.build_index") < figures
    assert _index(runs, "smite.side_by_side --json") <= figures
    assert figures < _index(runs, "git commit")


def test_a_figures_failure_never_blocks_the_days_data():
    """`live_window.py`'s rule, applied to the job: nothing may stop a day's
    community data landing unless the data is wrong, and a generator crash is
    not that. The failure is reported at the end instead (see the reporter
    test above)."""
    step = next(s for s in _steps("refresh-data.yml")
                if "smite.doc_figures" in s.get("run", ""))
    assert step.get("id") == "figures"
    assert step.get("continue-on-error") is True


def test_the_daily_job_commits_the_current_figures():
    """docs/ is not under `data/`, so it is staged by name."""
    assert "docs/CURRENT.md" in _pr_step()["run"].split("git reset")[0]


def test_the_job_installs_pytest():
    assert "pytest" in _run_text("refresh-data.yml")


def test_the_new_entity_probe_never_commits_fixtures():
    """It used to run on feature-branch pushes and commit its recording. The
    recording decides "untracked" against live data, so once the new gods were
    added it dropped them from the fixture index and turned test_new_entities
    red on main (f454b88). It is dispatch-only, read-only, and uploads."""
    spec = yaml.safe_load((WORKFLOWS / "probe-new-entities.yml").read_text(encoding="utf-8"))
    triggers = spec.get("on", spec.get(True))
    assert set(triggers) == {"workflow_dispatch"}
    assert spec["permissions"] == {"contents": "read"}
    text = _run_text("probe-new-entities.yml")
    assert "git commit" not in text and "git push" not in text


# -- the data pull request, run for real -------------------------------------
#
# Everything above reads the YAML. The step that opens the day's pull request
# is a decision table written in shell, and reading it was not enough: on a
# second run the same UTC day, after that day's PR had MERGED, it pushed onto
# the merged branch, looked the PR up by branch name and got the merged one
# back (`gh pr view data-refresh-2026-11-06` prints `117 MERGED`, checked
# 2026-11-08), so it opened nothing, could not arm a merged PR, and reported
# that auto-merge was probably off. The afternoon's data then sat on a branch
# with no open PR.
#
# So these tests RUN the step's own script, extracted from the workflow and
# not copied, against a local bare repository standing in for origin and a
# fake `gh` that keeps a list of pull requests. Nothing reaches GitHub: the
# authenticated push URL is rewritten to the local origin, every protocol
# but `file` is refused (`GIT_ALLOW_PROTOCOL`), `gh` resolves to the fake,
# and the real one would find no login in the empty `GH_CONFIG_DIR`.

_DAY = "2026-11-08"
_DAY_BRANCH = f"data-refresh-{_DAY}"
_REPO = "test-owner/ichor-gg"
_PAT = "pat-test-0000"
_FALLBACK = "ghs-test-0000"
_RUN_NUMBER, _RUN_ATTEMPT = "57", "1"
_RERUN_BRANCH = f"{_DAY_BRANCH}-run{_RUN_NUMBER}-{_RUN_ATTEMPT}"

# A stand-in for `gh`. It models the calls the refresh step makes and nothing
# else: anything it does not recognise exits 97, so a change to the step that
# this fake does not model fails a test instead of passing against a guess.
_FAKE_GH = r'''
import json, os, subprocess, sys

STATE = os.environ["FAKE_GH_STATE"]
with open(STATE, encoding="utf-8") as fh:
    state = json.load(fh)
args = sys.argv[1:]
state["calls"].append({"args": args, "token": os.environ.get("GH_TOKEN", "")})


def finish(out="", code=0, err=""):
    with open(STATE, "w", encoding="utf-8") as fh:
        json.dump(state, fh, indent=1)
    if out:
        sys.stdout.write(out + "\n")
    if err:
        sys.stderr.write(err + "\n")
    sys.exit(code)


def opt(name, default=None):
    return args[args.index(name) + 1] if name in args else default


def tip(branch):
    out = subprocess.run(
        ["git", "--git-dir", os.environ["FAKE_GH_ORIGIN"], "rev-parse", "--verify",
         "--quiet", "refs/heads/" + branch], capture_output=True, text=True)
    return out.stdout.strip() or None


def as_json(pr):
    # A PR that is still open has its branch's tip as head; one that merged
    # or closed keeps the head it had then.
    return {"number": pr["number"], "headRefName": pr["head"],
            "isCrossRepository": pr.get("cross", False), "state": pr["state"],
            "headRefOid": pr.get("head_oid") or tip(pr["head"]),
            "autoMergeRequest": {"mergeMethod": pr["armed"]} if pr.get("armed") else None}


def happens(event, pr):
    """Someone else merges or closes the PR mid-run: `on_view` before the
    step reads it, `on_arm` while it arms. `head_oid` null means it went with
    the branch as it stands, i.e. with this run's commit in it."""
    change = state.get(event, {}).pop(str(pr["number"]), None)
    if change:
        pr["head_oid"] = change.get("head_oid") or tip(pr["head"])
        pr["state"] = change["state"]


# The --jq expressions the step uses, evaluated by hand. Both were run against
# the real repository with gh 2.96.0 on 2026-11-08 and printed what these
# lambdas print: `94 claude/god-passive-classes-draft`, and `MERGED true
# ed094a35...` for #124, `OPEN false 421dce77...` for #94.
JQ = {
    r'map(select(.isCrossRepository | not)) | sort_by(.number) | .[] | "\(.number) \(.headRefName)"':
        lambda rows: "\n".join(f"{r['number']} {r['headRefName']}"
                               for r in sorted(rows, key=lambda r: r["number"])
                               if not r["isCrossRepository"]),
    r'"\(.state) \(.autoMergeRequest != null) \(.headRefOid)"':
        lambda pr: (f"{pr['state']} {'true' if pr['autoMergeRequest'] else 'false'} "
                    f"{pr['headRefOid']}"),
}


def jq(value):
    expr = opt("--jq")
    if expr not in JQ:
        finish(code=97, err=f"fake gh: unmodelled --jq {expr!r}")
    return JQ[expr](value)


def find(number):
    return next((p for p in state["prs"] if p["number"] == number), None)


cmd = args[:2]
if cmd == ["pr", "list"]:
    want = opt("--state", "open").upper()
    rows = [as_json(p) for p in state["prs"]
            if want in ("ALL", p["state"])
            and opt("--base") in (None, "main")
            and opt("--head") in (None, p["head"])]
    finish(jq(rows))
elif cmd == ["pr", "view"]:
    # By number only. By branch name gh returns the newest PR with that head
    # in ANY state, which is the trap the step fell into; it no longer asks.
    if not args[2].isdigit():
        finish(code=97, err=f"fake gh: pr view by branch is not modelled: {args!r}")
    pr = find(int(args[2]))
    if pr is None:
        finish(code=1, err=f"no pull request #{args[2]}")
    happens("on_view", pr)
    finish(jq(as_json(pr)))
elif cmd == ["pr", "create"]:
    head = opt("--head")
    if opt("--base") != "main" or not head:
        finish(code=97, err="fake gh: pr create without --base main --head <branch>")
    if not tip(head):
        finish(code=1, err=f"pull request create failed: {head!r} is not on origin")
    if any(p["head"] == head and p["state"] == "OPEN" and not p.get("cross")
           for p in state["prs"]):
        finish(code=1, err=f'a pull request for branch "{head}" into branch "main" already exists')
    number = max([p["number"] for p in state["prs"]] + [state.get("floor", 0)]) + 1
    state["prs"].append({"number": number, "head": head, "state": "OPEN",
                         "title": opt("--title"), "body": opt("--body")})
    finish(f"https://github.com/{os.environ['GITHUB_REPOSITORY']}/pull/{number}")
elif cmd == ["pr", "merge"]:
    if args[3:] != ["--auto", "--merge"]:
        finish(code=97, err=f"fake gh: only `pr merge N --auto --merge` is modelled, got {args!r}")
    pr = find(int(args[2]))
    happens("on_arm", pr)
    if pr["state"] == "MERGED":
        # EXIT 0, arming nothing. Observed: run 42497271128 (2026-11-08) ran
        # this on #124, merged an hour earlier, and its stuck reporter was
        # skipped, so the step had recorded `landed=armed`.
        finish(err=f"! Pull request #{pr['number']} was already merged")
    if pr["state"] != "OPEN":
        finish(code=1, err=f"Pull request #{pr['number']} is closed")
    if not state.get("auto_merge_allowed", True):
        finish(code=1, err="GraphQL: Auto merge is not allowed for this repository "
                           "(enablePullRequestAutoMerge)")
    pr["armed"] = "MERGE"
    finish()
else:
    finish(code=97, err=f"fake gh: unmodelled command {args!r}")
'''

# `date -u +%Y-%m-%d` is the only form the step uses; pinning it keeps a test
# from straddling UTC midnight. Anything else goes to the real `date`.
_FAKE_DATE = """#!/usr/bin/env bash
if [ "$*" = "-u +%Y-%m-%d" ]; then echo "$FAKE_DAY"; else exec /usr/bin/date "$@"; fi
"""

_FAKE_GH_SHIM = """#!/usr/bin/env bash
exec "$FAKE_PYTHON" "$FAKE_GH" "$@"
"""


def _bash():
    """A POSIX bash; on Windows, specifically Git for Windows' one.

    `shutil.which("bash")` on Windows resolves to System32's WSL launcher
    first, and that bash cannot run this harness against Windows paths."""
    if os.name != "nt":
        return shutil.which("bash")
    git = shutil.which("git")
    for parent in pathlib.Path(git).resolve().parents if git else ():
        for candidate in (parent / "bin" / "bash.exe", parent / "usr" / "bin" / "bash.exe"):
            if candidate.is_file():
                return str(candidate)
    return None


def _write(path: pathlib.Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def _step_by(predicate):
    return next(s for s in _steps("refresh-data.yml") if predicate(s))


def _pr_step():
    return _step_by(lambda s: s.get("id") == "data_pr")


def _stuck_reporter():
    return _step_by(lambda s: "steps.data_pr.outputs.landed" in str(s.get("if", "")))


def _read_outputs(path: pathlib.Path) -> dict:
    if not path.exists():
        return {}
    return dict(line.split("=", 1) for line in path.read_text(encoding="utf-8").splitlines()
                if "=" in line)


class _Run:
    def __init__(self, proc, outputs, summary, state):
        self.returncode = proc.returncode
        self.log = proc.stdout + proc.stderr
        self.outputs = outputs
        self.summary = summary
        self.state = state

    def calls(self, *prefix):
        return [c for c in self.state["calls"] if c["args"][:len(prefix)] == list(prefix)]

    def pr(self, number):
        return next(p for p in self.state["prs"] if p["number"] == int(number))


class _Origin:
    """A throwaway origin with a `main`, the day's branches, and the PR list."""

    def __init__(self, tmp: pathlib.Path):
        self.bash = _bash()
        assert self.bash, ("these tests run the workflow's shell and need bash "
                           "(on Windows, Git for Windows' bash.exe)")
        self.tmp = tmp
        self.origin = tmp / "origin.git"
        self.seed = tmp / "seed"
        self.checkout = tmp / "checkout"
        self.prs = []
        self.knobs = {}
        gitconfig = tmp / "gitconfig"
        text = ("[user]\n\tname = Seed\n\temail = seed@example.invalid\n"
                "[init]\n\tdefaultBranch = main\n")
        # The step pushes to an authenticated github.com URL. Point both tokens'
        # spellings of it at the local origin.
        for token in (_PAT, _FALLBACK):
            text += (f'[url "{self.origin.as_posix()}"]\n'
                     f"\tinsteadOf = https://x-access-token:{token}@github.com/{_REPO}.git\n")
        _write(gitconfig, text)
        self.env = {k: v for k, v in os.environ.items()
                    if not k.startswith(("GIT_", "GH_", "GITHUB_"))}
        self.env.update(GIT_CONFIG_GLOBAL=str(gitconfig), GIT_CONFIG_NOSYSTEM="1",
                        GIT_ALLOW_PROTOCOL="file", GIT_TERMINAL_PROMPT="0",
                        GH_CONFIG_DIR=str(tmp / "gh-config"), GITHUB_REPOSITORY=_REPO)
        self.git(tmp, "init", "-q", "--bare", str(self.origin))
        self.git(tmp, "init", "-q", str(self.seed))
        self.scrape(self.seed, "v0")
        self.commit(self.seed, "M0")
        self.git(self.seed, "remote", "add", "origin", str(self.origin))
        self.git(self.seed, "push", "-q", "origin", "main")

    # -- building the day ----------------------------------------------------

    def git(self, cwd, *args):
        return subprocess.run(["git", *args], cwd=cwd, env=self.env, check=True,
                              capture_output=True, text=True).stdout.strip()

    def scrape(self, root: pathlib.Path, value: str):
        """What the job's earlier steps leave in the tree: data, the index, the
        side-by-side pages, and an HTML cache that must never be committed."""
        for rel in ("data/community.json", "viewer/public/index.json",
                    "viewer/public/side_by_side/thor.json", "docs/CURRENT.md"):
            _write(root / rel, value + "\n")
        _write(root / "data" / "_cache" / f"{value}.html", "<html/>\n")

    def commit(self, root, message):
        self.git(root, "add", "data", "viewer", "docs")
        self.git(root, "reset", "-q", "--", "data/_cache")
        self.git(root, "commit", "-q", "-m", message)

    def day_branch(self, branch, value, cut_from="main"):
        self.git(self.seed, "checkout", "-q", "-b", branch, cut_from)
        self.scrape(self.seed, value)
        self.commit(self.seed, f"{branch}: {value}")
        self.git(self.seed, "push", "-q", "origin", branch)
        self.git(self.seed, "checkout", "-q", "main")

    def merge(self, branch, number):
        """Merged the way `gh pr merge --merge` merges: a merge commit on main."""
        self.git(self.seed, "merge", "-q", "--no-ff", branch,
                 "-m", f"Merge pull request #{number} from {_REPO.split('/')[0]}/{branch}")
        self.git(self.seed, "push", "-q", "origin", "main")

    def pr(self, number, head, state, **extra):
        self.prs.append({"number": number, "head": head, "state": state, **extra})

    # -- reading origin back -------------------------------------------------

    def tip(self, branch):
        out = subprocess.run(["git", "--git-dir", str(self.origin), "rev-parse", "--verify",
                              "--quiet", f"refs/heads/{branch}"],
                             env=self.env, capture_output=True, text=True)
        return out.stdout.strip() or None

    def parent(self, ref):
        return self.git(self.tmp, "--git-dir", str(self.origin), "rev-parse", f"{ref}^")

    def value(self, ref, path="data/community.json"):
        return self.git(self.tmp, "--git-dir", str(self.origin), "show",
                        f"{ref}:{path}")

    def files(self, ref):
        return self.git(self.tmp, "--git-dir", str(self.origin), "ls-tree", "-r",
                        "--name-only", ref).splitlines()

    def branches(self):
        return sorted(self.git(self.tmp, "--git-dir", str(self.origin), "for-each-ref",
                               "--format=%(refname:short)", "refs/heads").splitlines())

    # -- the run -------------------------------------------------------------

    def run(self, value, pat=_PAT):
        """Check out main as actions/checkout would, leave `value` as the day's
        scrape, and run the step's script the way Actions runs a `run:`."""
        tmp = self.tmp
        self.git(tmp, "clone", "-q", str(self.origin), str(self.checkout))
        self.scrape(self.checkout, value)
        bin_dir = tmp / "bin"
        _write(bin_dir / "gh", _FAKE_GH_SHIM)
        _write(bin_dir / "date", _FAKE_DATE)
        _write(tmp / "fake_gh.py", _FAKE_GH)
        for shim in ("gh", "date"):
            (bin_dir / shim).chmod(0o755)
        state_file = tmp / "gh-state.json"
        state_file.write_text(json.dumps({"prs": self.prs, "calls": [], **self.knobs}),
                              encoding="utf-8")
        script = tmp / "data_pr.sh"
        _write(script, _pr_step()["run"])
        outputs, summary = tmp / "github_output", tmp / "step_summary"
        env = dict(self.env,
                   PATH=str(bin_dir) + os.pathsep + self.env.get("PATH", ""),
                   REFRESH_PAT=pat, FALLBACK_TOKEN=_FALLBACK,
                   GITHUB_OUTPUT=outputs.as_posix(), GITHUB_STEP_SUMMARY=summary.as_posix(),
                   GITHUB_SERVER_URL="https://github.com", GITHUB_RUN_ID="4242",
                   GITHUB_RUN_NUMBER=_RUN_NUMBER, GITHUB_RUN_ATTEMPT=_RUN_ATTEMPT,
                   FAKE_DAY=_DAY, FAKE_GH_STATE=state_file.as_posix(),
                   FAKE_GH_ORIGIN=self.origin.as_posix(),
                   FAKE_PYTHON=pathlib.Path(sys.executable).as_posix(),
                   FAKE_GH=(tmp / "fake_gh.py").as_posix(),
                   # Git for Windows rewrites arguments that look like paths on
                   # their way to a native program, `--jq` expressions included.
                   MSYS_NO_PATHCONV="1", MSYS2_ARG_CONV_EXCL="*")
        proc = subprocess.run([self.bash, "--noprofile", "--norc", "-eo", "pipefail",
                               script.as_posix()],
                              cwd=self.checkout, env=env, capture_output=True, text=True,
                              timeout=120)
        return _Run(proc, _read_outputs(outputs),
                    summary.read_text(encoding="utf-8") if summary.exists() else "",
                    json.loads(state_file.read_text(encoding="utf-8")))

    def report(self, outputs):
        """Run the stuck-PR reporter with the env its YAML maps from the PR
        step's outputs, so what the reporter reads is what the step wrote."""
        step = _stuck_reporter()
        env = dict(self.env)
        for var, expr in step.get("env", {}).items():
            m = re.fullmatch(r"\$\{\{ steps\.data_pr\.outputs\.(\w+) \}\}", expr)
            assert m, f"the reporter's {var} is not read from the PR step: {expr}"
            env[var] = outputs.get(m.group(1), "")
        script = self.tmp / "reporter.sh"
        _write(script, step["run"])
        proc = subprocess.run([self.bash, "--noprofile", "--norc", "-eo", "pipefail",
                               script.as_posix()],
                              env=env, capture_output=True, text=True, timeout=60)
        return proc.returncode, proc.stdout + proc.stderr


@pytest.fixture
def origin(tmp_path):
    return _Origin(tmp_path)


def test_the_first_run_of_the_day_opens_the_day_pr_and_arms_it(origin):
    main = origin.tip("main")
    run = origin.run("morning")
    assert run.returncode == 0, run.log
    assert run.outputs["branch"] == _DAY_BRANCH
    assert run.outputs["landed"] == "armed" and run.outputs["token"] == "pat"
    assert origin.parent(_DAY_BRANCH) == main
    assert origin.value(_DAY_BRANCH) == "morning"
    # The day's figures travel with the day's data, in the same commit.
    assert origin.value(_DAY_BRANCH, "docs/CURRENT.md") == "morning"
    assert not any("_cache" in f for f in origin.files(_DAY_BRANCH))
    pr = run.pr(run.outputs["number"])
    assert (pr["head"], pr["state"], pr["armed"]) == (_DAY_BRANCH, "OPEN", "MERGE")
    # The PAT does everything that has to start a check, and never lands in
    # git config (9d1b693a): it is in the push URL and in gh's env only.
    assert {c["token"] for c in run.state["calls"]} == {_PAT}
    assert _PAT not in (origin.checkout / ".git" / "config").read_text(encoding="utf-8")


def test_a_rerun_while_the_day_pr_is_open_stacks_onto_it(origin):
    origin.day_branch(_DAY_BRANCH, "morning")
    origin.pr(124, _DAY_BRANCH, "OPEN")
    before = origin.tip(_DAY_BRANCH)
    run = origin.run("afternoon")
    assert run.returncode == 0, run.log
    assert (run.outputs["branch"], run.outputs["number"]) == (_DAY_BRANCH, "124")
    assert origin.parent(_DAY_BRANCH) == before      # an ordinary child, no force
    assert origin.value(_DAY_BRANCH) == "afternoon"
    assert not run.calls("pr", "create")
    assert run.outputs["landed"] == "armed" and run.pr(124)["armed"] == "MERGE"


@pytest.mark.parametrize("how", ["merged", "closed"])
def test_a_rerun_after_the_day_pr_merged_or_closed_opens_a_new_pr_from_main(origin, how):
    """THE 2026-11-08 DEFECT. The morning PR is gone, so the afternoon's data
    needs a PR of its own, from a branch cut from main. It must not be pushed
    onto the dead branch and reported as an auto-merge problem."""
    origin.day_branch(_DAY_BRANCH, "morning")
    if how == "merged":
        origin.merge(_DAY_BRANCH, 124)
    origin.pr(124, _DAY_BRANCH, how.upper(), **({"armed": "MERGE"} if how == "merged" else {}))
    dead, main = origin.tip(_DAY_BRANCH), origin.tip("main")
    run = origin.run("afternoon")
    assert run.returncode == 0, run.log
    assert origin.tip(_DAY_BRANCH) == dead            # the dead branch is left alone
    assert run.outputs["branch"] == _RERUN_BRANCH
    assert origin.parent(_RERUN_BRANCH) == main
    assert origin.value(_RERUN_BRANCH) == "afternoon"
    pr = run.pr(run.outputs["number"])
    assert pr["number"] == 125
    assert (pr["head"], pr["state"], pr["armed"]) == (_RERUN_BRANCH, "OPEN", "MERGE")
    assert run.outputs["landed"] == "armed"
    assert not run.calls("pr", "merge", "124")


def test_a_third_run_stacks_onto_the_afternoon_pr_rather_than_opening_another(origin):
    """One open data PR per day. A fourth branch from main would conflict with
    the third on every data file the moment either merged."""
    origin.day_branch(_DAY_BRANCH, "morning")
    origin.merge(_DAY_BRANCH, 124)
    origin.pr(124, _DAY_BRANCH, "MERGED", armed="MERGE")
    afternoon = f"{_DAY_BRANCH}-run56-1"
    origin.day_branch(afternoon, "afternoon")
    origin.pr(125, afternoon, "OPEN", armed="MERGE")
    before = origin.tip(afternoon)
    run = origin.run("evening")
    assert run.returncode == 0, run.log
    assert (run.outputs["branch"], run.outputs["number"]) == (afternoon, "125")
    assert origin.parent(afternoon) == before
    assert origin.value(afternoon) == "evening"
    assert not run.calls("pr", "create")
    assert origin.branches() == sorted(["main", _DAY_BRANCH, afternoon])


def test_a_pr_that_is_already_armed_is_not_armed_again(origin):
    origin.day_branch(_DAY_BRANCH, "morning")
    origin.pr(124, _DAY_BRANCH, "OPEN", armed="MERGE")
    run = origin.run("afternoon")
    assert run.returncode == 0, run.log
    assert run.outputs["landed"] == "armed"
    assert not run.calls("pr", "merge")


def test_a_rerun_with_nothing_new_for_the_open_pr_pushes_nothing_and_still_arms(origin):
    origin.day_branch(_DAY_BRANCH, "morning")
    origin.pr(124, _DAY_BRANCH, "OPEN")
    before = origin.tip(_DAY_BRANCH)
    run = origin.run("morning")
    assert run.returncode == 0, run.log
    assert origin.tip(_DAY_BRANCH) == before
    assert run.outputs["landed"] == "armed" and run.pr(124)["armed"] == "MERGE"


@pytest.mark.parametrize("head, cross", [(_DAY_BRANCH, True), (f"{_DAY_BRANCH}-fix", False)])
def test_a_pr_that_only_looks_like_the_days_is_never_touched(origin, head, cross):
    """The repository is public, so anyone can open a PR from a fork branch
    called data-refresh-<today>; and a person's own data-refresh-<today>-fix
    is not this workflow's either. The PAT must not stack onto or arm them."""
    origin.pr(130, head, "OPEN", cross=cross)
    run = origin.run("morning")
    assert run.returncode == 0, run.log
    assert run.outputs["branch"] == _DAY_BRANCH and run.outputs["number"] == "131"
    assert not run.calls("pr", "merge", "130")
    assert "armed" not in run.pr(130)


def test_no_change_against_main_touches_nothing(origin):
    run = origin.run("v0")
    assert run.returncode == 0, run.log
    assert "No change" in run.summary
    assert run.state["calls"] == [] and "landed" not in run.outputs
    assert origin.branches() == ["main"]


def test_without_the_pat_the_data_is_still_pushed_and_the_cause_is_named(origin):
    run = origin.run("morning", pat="")
    assert run.returncode == 0, run.log
    assert run.outputs["token"] == "github_token"
    assert origin.value(_DAY_BRANCH) == "morning"
    assert run.pr(run.outputs["number"])["head"] == _DAY_BRANCH
    assert {c["token"] for c in run.state["calls"]} == {_FALLBACK}
    assert not run.calls("pr", "merge")     # a checkless PR can never satisfy it
    assert (run.outputs["landed"], run.outputs["stuck"]) == ("stuck", "no_pat")
    code, said = origin.report(run.outputs)
    assert code == 1 and "REFRESH_PAT secret is not set" in said
    assert "Allow auto-merge" not in said


def test_auto_merge_refused_on_an_open_pr_is_reported_as_exactly_that(origin):
    origin.knobs["auto_merge_allowed"] = False
    run = origin.run("morning")
    assert run.returncode == 0, run.log
    assert (run.outputs["landed"], run.outputs["stuck"]) == ("stuck", "arm_refused")
    assert run.outputs["pr_state"] == "OPEN"
    assert "Auto merge is not allowed" in run.outputs["arm_error"]
    code, said = origin.report(run.outputs)
    assert code == 1
    assert f"#{run.outputs['number']}" in said and "Auto merge is not allowed" in said
    assert "Allow auto-merge" in said and "mergeable" in said


@pytest.mark.parametrize("event, became", [("on_view", "CLOSED"), ("on_arm", "CLOSED"),
                                           ("on_view", "MERGED"), ("on_arm", "MERGED")])
def test_a_pr_that_stopped_being_open_without_this_runs_data_is_not_blamed_on_auto_merge(
        origin, event, became):
    """Merged or closed by someone, from the head it had before this run's
    push, while the run was arming it. There is no open PR to arm, and saying
    auto-merge is off would send a person to the wrong place.

    `on_arm` + MERGED is the 2026-11-08 shape: gh exits 0 having armed
    nothing, and the step used to take that for `landed=armed` and go green."""
    origin.day_branch(_DAY_BRANCH, "morning")
    origin.pr(124, _DAY_BRANCH, "OPEN")
    origin.knobs[event] = {"124": {"state": became, "head_oid": origin.tip(_DAY_BRANCH)}}
    run = origin.run("afternoon")
    assert run.returncode == 0, run.log
    assert (run.outputs["landed"], run.outputs["stuck"]) == ("stuck", "not_open")
    assert run.outputs["pr_state"] == became
    code, said = origin.report(run.outputs)
    assert code == 1 and f"#124 is {became}" in said and "no open pull request" in said
    assert "Allow auto-merge" not in said and "likely" not in said


@pytest.mark.parametrize("event", ["on_view", "on_arm"])
def test_a_pr_that_merged_with_this_runs_commit_in_it_has_landed(origin, event):
    """Not a failure: the data is on main. Read off the PR's head commit."""
    origin.day_branch(_DAY_BRANCH, "morning")
    origin.pr(124, _DAY_BRANCH, "OPEN")
    origin.knobs[event] = {"124": {"state": "MERGED", "head_oid": None}}
    run = origin.run("afternoon")
    assert run.returncode == 0, run.log
    assert run.outputs["landed"] == "merged" and "stuck" not in run.outputs


def test_the_stuck_reporter_does_not_guess_a_cause_it_was_not_given(origin):
    code, said = origin.report({"landed": "stuck"})
    assert code == 1 and "::error::" in said
    assert "Allow auto-merge" not in said and "REFRESH_PAT secret is not set" not in said


def test_the_checkout_leaves_no_credential_in_git_config():
    """9d1b693a: the PAT is used at the push and nowhere else."""
    checkout = _step_by(lambda s: str(s.get("uses", "")).startswith("actions/checkout"))
    assert checkout["with"]["persist-credentials"] is False
    run = _pr_step()["run"]
    assert "extraheader" not in run and "remote set-url" not in run
