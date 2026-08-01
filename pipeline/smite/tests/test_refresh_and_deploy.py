import pathlib
from unittest import mock

from smite import refresh_and_deploy


def test_validate_is_called_with_explicit_argv(monkeypatch):
    """refresh_and_deploy runs while its own flags (--no-push) sit on sys.argv.
    It must hand validate.main an explicit argv; passing None lets argparse fall
    through to sys.argv, where it hits --no-push and hard-exits mid-pipeline."""
    seen = {}
    monkeypatch.setattr(refresh_and_deploy.refresh, "refresh_all", lambda *a, **k: None)
    monkeypatch.setattr(refresh_and_deploy.recommend, "main", lambda *a, **k: 0)
    monkeypatch.setattr(refresh_and_deploy.recommend, "load_items", lambda: [])
    monkeypatch.setattr(refresh_and_deploy.build_index, "write_index", lambda *a, **k: None)
    monkeypatch.setattr(refresh_and_deploy.snapshots, "write_snapshot", lambda *a, **k: "snap.json")
    monkeypatch.setattr(refresh_and_deploy, "_run_git", lambda *a, **k: None)
    # Whichever branch the developer happens to be on must not decide whether
    # this test runs — the guard has its own tests below.
    monkeypatch.setattr(refresh_and_deploy, "_current_branch",
                        lambda cwd: refresh_and_deploy.DEPLOY_BRANCH)
    monkeypatch.setattr(refresh_and_deploy.validate, "main",
                        lambda argv=None: seen.setdefault("argv", argv) or 0)

    refresh_and_deploy.main(["--no-push"])
    assert seen["argv"] is not None, "validate.main() called with no argv — will re-parse sys.argv"


# ── The branch guard ────────────────────────────────────────────────────────
#
# A refresh commits generated data and pushes to trigger a deploy. Run from a
# feature branch it does all of that to the feature branch: the data never
# reaches production and nothing says so. That happened — a refresh landed on
# an already-merged PR branch, pushed cleanly, built a preview, and left the
# site on stale data for half an hour before anyone noticed.

def _stub_pipeline(monkeypatch, ran):
    for name, attr in (("refresh", "refresh_all"), ("recommend", "main"),
                       ("build_index", "write_index"), ("validate", "main")):
        monkeypatch.setattr(getattr(refresh_and_deploy, name), attr,
                            lambda *a, **k: ran.setdefault("scraped", True))
    monkeypatch.setattr(refresh_and_deploy.recommend, "load_items", lambda: [])
    monkeypatch.setattr(refresh_and_deploy.snapshots, "write_snapshot", lambda *a, **k: "s.json")
    monkeypatch.setattr(refresh_and_deploy, "_run_git",
                        lambda *a, **k: ran.setdefault("committed", True))


def test_refuses_to_run_on_a_branch_that_is_not_the_deploy_branch(monkeypatch):
    ran = {}
    _stub_pipeline(monkeypatch, ran)
    monkeypatch.setattr(refresh_and_deploy, "_current_branch", lambda cwd: "fix/some-work")

    assert refresh_and_deploy.main([]) == 2
    # Refused BEFORE the scrape, not after: the run takes half an hour, and
    # failing at the commit step means doing all of it again.
    assert "scraped" not in ran
    assert "committed" not in ran


def test_refuses_on_a_detached_head(monkeypatch):
    ran = {}
    _stub_pipeline(monkeypatch, ran)
    monkeypatch.setattr(refresh_and_deploy, "_current_branch", lambda cwd: None)
    assert refresh_and_deploy.main([]) == 2
    assert "scraped" not in ran


def test_runs_on_the_deploy_branch(monkeypatch):
    ran = {}
    _stub_pipeline(monkeypatch, ran)
    monkeypatch.setattr(refresh_and_deploy, "_current_branch",
                        lambda cwd: refresh_and_deploy.DEPLOY_BRANCH)
    assert refresh_and_deploy.main(["--no-push"]) == 0
    assert ran.get("scraped") and ran.get("committed")


def test_an_explicit_branch_overrides_the_guard(monkeypatch):
    """Deliberately refreshing onto another branch stays possible — the guard
    exists to stop it happening by accident, not to forbid it."""
    ran = {}
    _stub_pipeline(monkeypatch, ran)
    monkeypatch.setattr(refresh_and_deploy, "_current_branch", lambda cwd: "staging")
    assert refresh_and_deploy.main(["--branch", "staging", "--no-push"]) == 0
    assert ran.get("scraped")


def test_the_commit_list_carries_the_patch_label_and_new_icons():
    """Both were missing, and both had visible symptoms: the site announcing
    the previous patch, and a brand-new item rendering as a bare initial."""
    src = (pathlib.Path(refresh_and_deploy.__file__)).read_text(encoding="utf-8")
    for path in ("data/_patch.json", "data/_assets/icons",
                 "data/_community_items.json", "viewer/public/index.json"):
        assert f'"{path}"' in src, f"{path} missing from the committed path list"
