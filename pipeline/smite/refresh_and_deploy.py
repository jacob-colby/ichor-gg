"""One-command patch update: re-scrape everything, recompute, rebuild the index,
then commit the generated data narrowly and push (which triggers the static-host
redeploy). Run from the vault on the canonical git device.

    python -m smite.refresh_and_deploy            # scrape + regen + commit + push
    python -m smite.refresh_and_deploy --no-push  # scrape + regen + commit only
    python -m smite.refresh_and_deploy --branch x # commit to some other branch
"""
import argparse
import subprocess
import sys
from datetime import date

from smite import refresh, recommend, build_index, validate, snapshots


def _run_git(args, cwd):
    subprocess.run(["git", *args], cwd=cwd, check=True)


# The branch a data refresh belongs on. This is a scheduled job that commits
# generated data and pushes to trigger a deploy — run from a feature branch it
# does all of that to the feature branch, so the data never reaches production
# and nothing says so. It has happened: a refresh landed on an already-merged
# PR branch, pushed cleanly, built a preview, and left the site on stale data.
DEPLOY_BRANCH = "main"


def _current_branch(cwd):
    """The checked-out branch, or None in a detached HEAD."""
    out = subprocess.run(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        cwd=cwd, capture_output=True, text=True, check=True,
    ).stdout.strip()
    return None if out == "HEAD" else out


def main(argv=None):
    parser = argparse.ArgumentParser(description="Refresh + regenerate + deploy")
    parser.add_argument("--no-push", action="store_true", help="commit but do not push")
    parser.add_argument("--branch", default=DEPLOY_BRANCH,
                        help=f"branch this refresh may commit to (default: {DEPLOY_BRANCH})")
    args = parser.parse_args(argv)

    # Checked before the scrape, not after: the run takes half an hour, and
    # discovering the problem at the commit step means doing it all again.
    current = _current_branch(recommend.REPO_ROOT)
    if current != args.branch:
        where = "a detached HEAD" if current is None else f"'{current}'"
        fallback = current or "<branch>"
        print(f"refresh_and_deploy: refusing to run on {where}.", file=sys.stderr)
        print(f"  A data refresh commits and pushes; on any branch but "
              f"'{args.branch}' that data never reaches the site.", file=sys.stderr)
        print(f"  Either:  git checkout {args.branch}", file=sys.stderr)
        print(f"  Or:      python -m smite.refresh_and_deploy --branch {fallback}",
              file=sys.stderr)
        return 2

    refresh.refresh_all()
    recommend.main(["--all"])
    build_index.write_index(
        recommend.REPO_ROOT,
        recommend.REPO_ROOT / "viewer" / "public" / "index.json",
    )
    # Explicit argv: this runs with refresh_and_deploy's own flags still on
    # sys.argv, and validate.main(None) would let argparse re-parse them.
    validate.main([])

    snapshot_path = snapshots.write_snapshot(recommend.load_items(), date.today().isoformat())
    print(f"refresh_and_deploy: wrote item-stat snapshot to {snapshot_path}")

    root = recommend.REPO_ROOT
    paths = [
        "data/builds",
        "data/Gods",
        "data/Items",
        "data/Analysis",
        # The community item table. Written by refresh_all, and easy to miss
        # here because it is a single file rather than a directory — left out,
        # it is regenerated every run and committed by none of them.
        "data/_community_items.json",
        # The patch label the viewer prints. Omitted, the site keeps announcing
        # the previous patch while serving the new one's data.
        "data/_patch.json",
        # Art for items the patch introduced. Omitted, a brand-new item renders
        # as a fallback initial — the most visible possible symptom, on exactly
        # the items people came to look at.
        "data/_assets/icons",
        "viewer/public/index.json",
    ]
    _run_git(["add", "--", *paths], root)
    if subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=root).returncode != 0:
        _run_git(["commit", "-m", "chore(smite): scheduled data refresh"], root)
        if not args.no_push:
            _run_git(["push"], root)
        print("refresh_and_deploy: committed" + ("" if args.no_push else " + pushed"))
    else:
        print("refresh_and_deploy: no data changes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
