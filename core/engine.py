import sys
import os

# Allow running from the hooks directory
sys.path.insert(0, os.path.dirname(__file__))

from diff_reader import get_latest_diff, get_changed_files, get_commit_message, get_commit_hash
from llm import analyze_diff
from metadata import update


def run():
    diff = get_latest_diff()
    if not diff.strip():
        print("[gitmind] No diff found — skipping metadata update.")
        return

    commit_message = get_commit_message()
    commit_hash = get_commit_hash()
    changed_files = get_changed_files()

    print("[gitmind] Analyzing commit...")

    summary = analyze_diff(diff, commit_message=commit_message, changed_files=changed_files)
    update(summary, commit_hash=commit_hash)

    print(f"[gitmind] Feature tracked: {summary.get('feature_name', 'unknown')}")
    print(f"[gitmind] {summary.get('what_changed', '')}")


if __name__ == "__main__":
    run()
