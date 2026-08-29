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
