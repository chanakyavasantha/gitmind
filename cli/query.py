#!/usr/bin/env python3
"""
gitmind query CLI
Usage:
  python cli/query.py features          - list all tracked features
  python cli/query.py files <feature>   - show files touched by a feature
  python cli/query.py history           - show commit history with summaries
  python cli/query.py stale [--days N]  - show features with no recent activity
"""

import sys
import os
import json
from datetime import datetime, timedelta

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "core"))
from metadata import load


def cmd_features():
    data = load()
    features = data.get("features", {})
    if not features:
        print("No features tracked yet.")
        return
    for name, info in features.items():
        status = "active" if info.get("still_active") else "stale"
        print(f"  {name} [{status}] — {info.get('commit_count', 0)} commits, last touched {info.get('last_built_upon', 'unknown')[:10]}")


def cmd_files(feature_name):
    data = load()
    feature = data.get("features", {}).get(feature_name)
    if not feature:
        print(f"Feature '{feature_name}' not found.")
        return
    print(f"Files touched by '{feature_name}':")
    for f in feature.get("files_touched", []):
        print(f"  {f}")


def cmd_history():
    data = load()
    for entry in reversed(data.get("history", [])):
        ts = entry.get("timestamp", "")[:10]
        feature = entry.get("feature_name", "unknown")
        what = entry.get("what_changed", "")
        commit = entry.get("commit_hash", "")[:7]
        print(f"  [{ts}] {commit} {feature}: {what}")


def cmd_stale(days=90):
    data = load()
    cutoff = datetime.now() - timedelta(days=days)
    print(f"Features with no activity in the last {days} days:")
    found = False
    for name, info in data.get("features", {}).items():
        last = info.get("last_built_upon", "")
        if not last:
            continue
        last_dt = datetime.fromisoformat(last)
        if last_dt < cutoff:
            found = True
            print(f"  {name} — last touched {last[:10]}, files: {info.get('files_touched', [])}")
    if not found:
        print("  None found.")


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(0)

    cmd = args[0]

    if cmd == "features":
        cmd_features()
    elif cmd == "files" and len(args) > 1:
        cmd_files(args[1])
    elif cmd == "history":
        cmd_history()
    elif cmd == "stale":
        days = int(args[2]) if len(args) > 2 and args[1] == "--days" else 90
        cmd_stale(days)
    else:
        print(__doc__)
