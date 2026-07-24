"""One-command patch update: re-scrape everything, recompute, rebuild the index,
then commit the generated data narrowly and push (which triggers the static-host
redeploy). Run from the vault on the canonical git device.

    python -m smite.refresh_and_deploy            # scrape + regen + commit + push
    python -m smite.refresh_and_deploy --no-push  # scrape + regen + commit only
"""
import argparse
import subprocess
import sys
from datetime import date

from smite import refresh, recommend, build_index, validate, snapshots


def _run_git(args, cwd):
    subprocess.run(["git", *args], cwd=cwd, check=True)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Refresh + regenerate + deploy")
    parser.add_argument("--no-push", action="store_true", help="commit but do not push")
    args = parser.parse_args(argv)

    refresh.refresh_all()
    recommend.main(["--all"])
    build_index.write_index(
        recommend.VAULT_ROOT,
        recommend.VAULT_ROOT / "viewer" / "public" / "index.json",
    )
    validate.main()

    snapshot_path = snapshots.write_snapshot(recommend.load_items(), date.today().isoformat())
    print(f"refresh_and_deploy: wrote item-stat snapshot to {snapshot_path}")

    root = recommend.VAULT_ROOT
    paths = [
        "03. Workspaces/Gaming/SMITE 2/Builds",
        "04. System/Data/SMITE/Gods",
        "04. System/Data/SMITE/Items",
        "04. System/Data/SMITE/Analysis",
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
