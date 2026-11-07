"""The scheduled workflow is a caller like any other, and it is the one caller
nothing else tests.

F9 of the 2026-08-23 audit was a dead patch-notes page. The cause was not a bug
in `snapshots.py` — every function in it worked and was tested. The cause was
that the only code path calling `write_snapshot` was `refresh_and_deploy`, a
manual patch-day command, and the daily job did not invoke it. A unit test
cannot see that. Reading the YAML can.
"""
import pathlib

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

    THREE of these reporters now, not two. The third fires when the day's data
    is stuck in a pull request nobody can merge, and it arrived with the
    reroute off `git push` to main. It holds the same contract as the other
    two: it comes after the data is safe, and it turns a quiet problem into a
    red run.

    AND EACH REPORTS INDEPENDENTLY. A step runs by default only if every step
    before it succeeded, so three terminal reporters in a row meant the first
    `exit 1` suppressed the others' messages. That was a latent bug in the
    original PAIR rather than something the third step introduced: a run with
    both a rejected stats refresh and a left-out entity only ever told you
    about the first. `!cancelled()` on each condition is the fix, pinned here
    so the suppression cannot come back."""
    steps = _steps("refresh-data.yml")
    runs = [s.get("run", "") for s in steps]
    conds = ["steps.stats_gate.outputs.rejected",
             "steps.new_entities.outputs.rejected",
             "steps.data_pr.outputs.landed"]
    fails = [next(i for i, s in enumerate(steps) if cond in str(s.get("if", "")))
             for cond in conds]
    # The reporters are the run's last steps, after the data is safe.
    assert sorted(fails) == [len(steps) - 3, len(steps) - 2, len(steps) - 1]
    for fail in fails:
        assert "exit 1" in runs[fail]
        assert _index(runs, "git commit") < fail
        # Independent of whether an earlier reporter already failed.
        assert "!cancelled()" in str(steps[fail].get("if", ""))


def test_new_entities_run_after_the_stats_gate_and_before_the_recompute():
    """After, so the two gates never blame each other's change; before the
    snapshot and recompute, so the day's index carries what was added."""
    runs = [s.get("run", "") for s in _steps("refresh-data.yml")]
    add = _index(runs, "smite.new_entities")
    assert _index(runs, "smite.stats_gate check") < add < _index(runs, "smite.snapshots")
    assert add < _index(runs, "smite.recommend --all")


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
