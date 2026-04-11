#!/usr/bin/env python3
"""
Re-runs gitmind's LLM analysis across every commit in the real git history
and rebuilds metadata.json from scratch.

Usage: python3 scripts/reindex.py
Requires: Ollama running with deepseek-coder pulled.
"""

import subprocess
import sys
import os
import json

# Add core to path so we can import directly
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO_ROOT, "core"))

from llm import analyze_diff
from metadata import save
from diff_reader import _is_noise


def git(args) -> str:
    result = subprocess.run(
        ["git"] + args,
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )
    return result.stdout.strip()


def get_commits() -> list[str]:
    """Return all commit hashes oldest-first."""
    out = git(["log", "--reverse", "--pretty=%H"])
    return [h for h in out.splitlines() if h]


def get_diff(commit: str, is_first: bool) -> str:
    if is_first:
        return git(["show", commit])
    return git(["diff", f"{commit}^", commit])


def get_changed_files(commit: str, is_first: bool) -> list[str]:
    if is_first:
        out = git(["diff-tree", "--no-commit-id", "-r", "--name-only", commit])
    else:
        out = git(["diff", "--name-only", f"{commit}^", commit])
    return [f for f in out.splitlines() if f.strip() and not _is_noise(f)]


def get_commit_message(commit: str) -> str:
    return git(["log", "-1", "--pretty=%B", commit])


def get_commit_date(commit: str) -> str:
    return git(["log", "-1", "--pretty=%aI", commit])


def main():
    commits = get_commits()
    print(f"Found {len(commits)} commits to reindex.\n")

    features: dict = {}
    history: list = []

    for i, commit in enumerate(commits):
        short = commit[:7]
        is_first = i == 0
        msg = get_commit_message(commit)
        timestamp = get_commit_date(commit)
        changed_files = get_changed_files(commit, is_first)

        # Skip pure metadata-only commits — they just contain metadata.json
        # and don't represent real feature work
        if changed_files == ["metadata.json"]:
            print(f"  [{short}] skip — metadata-only commit")
            continue

        diff = get_diff(commit, is_first)

        print(f"  [{short}] {msg.splitlines()[0][:60]}")
        print(
            f"           files: {', '.join(changed_files[:4])}"
            + (f" +{len(changed_files)-4} more" if len(changed_files) > 4 else "")
        )

        try:
            summary = analyze_diff(
                diff,
                commit_message=msg,
                changed_files=changed_files,
            )
        except RuntimeError as e:
            print(f"           SKIP — {e}")
            continue

        feature = summary.get("feature_name", "unknown")
        print(f"           → feature: {feature}")

        if feature not in features:
            features[feature] = {
                "introduced": timestamp,
                "files_touched": [],
                "still_active": True,
                "last_built_upon": timestamp,
                "is_new_feature": summary.get("is_new_feature", False),
                "commit_count": 0,
            }

        entry = features[feature]
        for f in changed_files:
            if f and f not in entry["files_touched"]:
                entry["files_touched"].append(f)
        entry["last_built_upon"] = timestamp
        entry["commit_count"] += 1

        history.append(
            {
                "commit_hash": short,
                "timestamp": timestamp,
                "what_changed": summary.get("what_changed", ""),
                "why_it_likely_changed": summary.get("why_it_likely_changed", ""),
                "feature_name": feature,
                "is_new_feature": summary.get("is_new_feature", False),
                "impact": summary.get("impact", ""),
                "files_touched": changed_files,
            }
        )

    data = {"features": features, "history": history}
    save(data)
    print(
        f"\nDone — {len(features)} features, {len(history)} commits written to metadata.json"
    )


if __name__ == "__main__":
    main()
