"""`smite.stats_gate`: a stats refresh that turns a test red never ships.

The suite and the recompute are injected, so these run in milliseconds on a
throwaway data root; the real pytest invocation is exercised once, on a
two-test file, to pin the report parsing it depends on.
"""
import json
import subprocess
import sys

import pytest

from smite import stats_gate


def _root(tmp_path, damaru_cost=2750, refresh_state=True):
    root = tmp_path / "data"
    (root / "Items").mkdir(parents=True)
    (root / "Gods").mkdir()
    (root / "Items" / "Damaru.md").write_text(f"---\nname: Damaru\ncost: {damaru_cost}\n---\n")
    (root / "Gods" / "Medusa.md").write_text("---\nname: Medusa\n---\n")
    (root / "_patch.json").write_text(json.dumps({"data_patch": "Open Beta 40"}))
    if refresh_state:
        (root / "_stats_refresh.json").write_text(json.dumps({"wiki_patch": "Open Beta 40"}))
    return root


def _refresh(root):
    """What a successful `stats_refresh` does to the owned paths."""
    (root / "Items" / "Damaru.md").write_text("---\nname: Damaru\ncost: 2500\n---\n")
    (root / "Items" / "Blinking Abyss.md").write_text("---\nname: Blinking Abyss\n---\n")
    (root / "_patch.json").write_text(json.dumps({"data_patch": "Open Beta 46"}))
    (root / "_stats_refresh.json").write_text(json.dumps({"wiki_patch": "Open Beta 46"}))


def _cost(root):
    return (root / "Items" / "Damaru.md").read_text()


class FakeSuite:
    """Fails `fails_when(root)`'s tests, recording each call."""

    def __init__(self, root, failing_on_new=(), failing_on_old=(), raise_on=None):
        self.root, self.calls = root, []
        self.new, self.old, self.raise_on = set(failing_on_new), set(failing_on_old), raise_on

    def __call__(self, nodeids):
        on_new = "2500" in _cost(self.root)
        self.calls.append(("new" if on_new else "old", nodeids))
        if self.raise_on == ("new" if on_new else "old"):
            raise stats_gate.SuiteError("pytest wrote no report")
        failed = self.new if on_new else self.old
        return set(failed) if nodeids is None else set(failed) & set(nodeids)


def _noop():
    pass


def test_no_stat_change_runs_no_tests(tmp_path):
    root = _root(tmp_path)
    stats_gate.save(root, tmp_path / "before")
    (root / "_patch.json").write_text(json.dumps({"data_patch": "Open Beta 40", "patch": "x"}))
    suite = FakeSuite(root)
    assert stats_gate.check(tmp_path / "before", root, suite, _noop) == {"status": "unchanged"}
    assert suite.calls == []


def test_a_green_suite_keeps_the_new_stats(tmp_path):
    root = _root(tmp_path)
    stats_gate.save(root, tmp_path / "before")
    _refresh(root)
    result = stats_gate.check(tmp_path / "before", root, FakeSuite(root), _noop)
    assert result["status"] == "accepted"
    assert "2500" in _cost(root) and (root / "Items" / "Blinking Abyss.md").exists()


def test_a_test_the_refresh_broke_restores_every_owned_path(tmp_path):
    """The load-bearing case: red on new, green on old -> old stats back,
    INCLUDING the patch label and the refresh state, so the history never
    claims a patch whose stats are not the ones on disk."""
    root = _root(tmp_path)
    stats_gate.save(root, tmp_path / "before")
    _refresh(root)
    bad = "smite/tests/test_x.py::test_medusa"
    result = stats_gate.check(tmp_path / "before", root, FakeSuite(root, failing_on_new=[bad]), _noop)
    assert result["status"] == "rejected"
    assert result["attributable"] == [bad]
    assert "2750" in _cost(root)
    assert not (root / "Items" / "Blinking Abyss.md").exists()
    assert json.loads((root / "_patch.json").read_text())["data_patch"] == "Open Beta 40"
    assert json.loads((root / "_stats_refresh.json").read_text())["wiki_patch"] == "Open Beta 40"


def test_a_file_that_did_not_exist_before_is_removed_on_restore(tmp_path):
    root = _root(tmp_path, refresh_state=False)
    stats_gate.save(root, tmp_path / "before")
    _refresh(root)
    stats_gate.check(tmp_path / "before", root, FakeSuite(root, failing_on_new=["t::a"]), _noop)
    assert not (root / "_stats_refresh.json").exists()


def test_only_the_failing_tests_are_re_run_on_the_old_stats(tmp_path):
    root = _root(tmp_path)
    stats_gate.save(root, tmp_path / "before")
    _refresh(root)
    suite = FakeSuite(root, failing_on_new=["t::a", "t::b"])
    stats_gate.check(tmp_path / "before", root, suite, _noop)
    assert suite.calls == [("new", None), ("old", {"t::a", "t::b"})]


def test_a_failure_the_old_stats_share_is_not_blamed_on_the_refresh(tmp_path):
    """main was already red, or community data moved it: blocking a correct
    patch for that would keep stale prices live for nothing."""
    root = _root(tmp_path)
    stats_gate.save(root, tmp_path / "before")
    _refresh(root)
    suite = FakeSuite(root, failing_on_new=["t::a"], failing_on_old=["t::a"])
    result = stats_gate.check(tmp_path / "before", root, suite, _noop)
    assert result == {"status": "accepted-with-preexisting-failures", "preexisting": ["t::a"]}
    assert "2500" in _cost(root) and (root / "Items" / "Blinking Abyss.md").exists()


def test_one_attributable_failure_among_shared_ones_still_rejects(tmp_path):
    root = _root(tmp_path)
    stats_gate.save(root, tmp_path / "before")
    _refresh(root)
    suite = FakeSuite(root, failing_on_new=["t::a", "t::b"], failing_on_old=["t::a"])
    result = stats_gate.check(tmp_path / "before", root, suite, _noop)
    assert result["status"] == "rejected"
    assert result["attributable"] == ["t::b"] and result["preexisting"] == ["t::a"]
    assert "2750" in _cost(root)


@pytest.mark.parametrize("where", ["new", "old"])
def test_a_suite_that_cannot_report_is_red_not_green(tmp_path, where):
    """Fail-closed: a crash, a collection error, a timeout — none is a pass."""
    root = _root(tmp_path)
    stats_gate.save(root, tmp_path / "before")
    _refresh(root)
    suite = FakeSuite(root, failing_on_new=["t::a"], raise_on=where)
    result = stats_gate.check(tmp_path / "before", root, suite, _noop)
    assert result["status"] == "rejected"
    assert "2750" in _cost(root)


def test_a_recompute_crash_on_the_new_stats_rejects(tmp_path):
    root = _root(tmp_path)
    stats_gate.save(root, tmp_path / "before")
    _refresh(root)
    calls = []

    def recompute():
        calls.append(_cost(root))
        if "2500" in _cost(root):
            raise subprocess.CalledProcessError(1, "recommend")

    result = stats_gate.check(tmp_path / "before", root, FakeSuite(root), recompute)
    assert result["status"] == "rejected"
    assert "2750" in _cost(root)
    assert len(calls) == 2          # tried the new, then rebuilt on the old


def test_the_report_names_each_test_as_an_error_annotation():
    out = stats_gate.report({"status": "rejected", "attributable": ["t::a", "t::b"],
                             "preexisting": ["t::c"]})
    assert out.startswith("::error::")
    assert "::error::  fails on the new stats, passes on the old: t::a" in out
    assert "::warning::  fails on both (not the refresh's doing): t::c" in out


def test_the_rejection_reaches_the_workflow_as_an_output(tmp_path, monkeypatch):
    out = tmp_path / "out"
    monkeypatch.setenv("GITHUB_OUTPUT", str(out))
    monkeypatch.delenv("GITHUB_STEP_SUMMARY", raising=False)
    stats_gate._github_outputs({"status": "rejected", "attributable": ["t::a"]})
    stats_gate._github_outputs({"status": "accepted"})
    assert out.read_text() == "rejected=true\nrejected=false\n"


def test_junit_parsing_matches_pytest_node_ids(tmp_path):
    """The re-run on the old stats passes these ids back to pytest, so they
    have to be real node ids — plain, parametrised and on a class."""
    (tmp_path / "test_j.py").write_text(
        "import pytest\n"
        "def test_a(): assert 0\n"
        "def test_ok(): pass\n"
        "@pytest.mark.parametrize('x', [1, 2])\n"
        "def test_b(x): assert x == 1\n"
        "class TestC:\n"
        "    def test_d(self): assert 0\n")
    report = tmp_path / "j.xml"
    subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider",
                    f"--junitxml={report}", "-o", "junit_family=xunit1", "test_j.py"],
                   cwd=tmp_path, capture_output=True)
    failed = stats_gate.failures_from_junit(report.read_text())
    assert failed == {"test_j.py::test_a", "test_j.py::test_b[2]", "test_j.py::TestC::test_d"}
    rerun = subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider",
                            *sorted(failed)], cwd=tmp_path, capture_output=True, text=True)
    assert "3 failed" in rerun.stdout
