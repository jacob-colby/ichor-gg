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
    monkeypatch.setattr(refresh_and_deploy.validate, "main",
                        lambda argv=None: seen.setdefault("argv", argv) or 0)

    refresh_and_deploy.main(["--no-push"])
    assert seen["argv"] is not None, "validate.main() called with no argv — will re-parse sys.argv"
