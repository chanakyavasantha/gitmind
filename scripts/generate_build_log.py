#!/usr/bin/env python3
"""
Reads metadata.json and generates docs/build-log.md automatically.
Run by the docs.yml workflow before MkDocs builds the site.
"""

import json
import os
import sys
from datetime import datetime

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
METADATA_PATH = os.path.join(REPO_ROOT, "metadata.json")
OUTPUT_PATH = os.path.join(REPO_ROOT, "docs", "build-log.md")


def load_metadata() -> dict:
    if not os.path.exists(METADATA_PATH):
        print(
            f"No metadata.json found at {METADATA_PATH} — skipping build log generation."
        )
        sys.exit(0)
    with open(METADATA_PATH) as f:
        return json.load(f)


def format_date(iso: str) -> str:
    try:
        return datetime.fromisoformat(iso).strftime("%Y-%m-%d %H:%M")
    except Exception:
        return iso[:16] if iso else "unknown"


def render(metadata: dict) -> str:
    features = metadata.get("features", {})
    history = metadata.get("history", [])

    lines = [
        "# Build Log",
        "",
        "This page is generated automatically from `metadata.json` on every push — the tool is documenting itself.",
        "",
        "Every entry below was written by gitmind analyzing its own commits via a local LLM (Ollama + deepseek-coder).",
        "No human wrote these summaries. The feature names, file lists, and change descriptions are all LLM output.",
        "",
        "---",
        "",
    ]

    # Feature registry
    lines += [
        "## Tracked Features",
        "",
        "| Feature | Status | Commits | Introduced | Last Active |",
        "|---------|--------|---------|------------|-------------|",
    ]
    for name, info in sorted(
        features.items(), key=lambda x: x[1].get("introduced", ""), reverse=True
    ):
        status = "active" if info.get("still_active") else "stale"
        badge = "✅ active" if status == "active" else "⚠️ stale"
        introduced = format_date(info.get("introduced", ""))
        last = format_date(info.get("last_built_upon", ""))
        count = info.get("commit_count", 0)
        lines.append(f"| `{name}` | {badge} | {count} | {introduced} | {last} |")

    lines += ["", "---", "", "## Files Per Feature", ""]
    for name, info in sorted(features.items()):
        files = info.get("files_touched", [])
        if not files:
            continue
        lines.append(f"**`{name}`**")
        lines.append("")
        for f in files:
            lines.append(f"- `{f}`")
        lines.append("")

    lines += ["---", "", "## Commit History", "", "Most recent first.", ""]
    for entry in reversed(history):
        commit = entry.get("commit_hash", "")[:7]
        ts = format_date(entry.get("timestamp", ""))
        feature = entry.get("feature_name", "unknown")
        what = entry.get("what_changed", "")
        why = entry.get("why_it_likely_changed", "")
        impact = entry.get("impact", "")
        files = entry.get("files_touched", [])
        is_new = entry.get("is_new_feature", False)

        lines.append(f"### `{commit}` — {ts}")
        lines.append("")
        lines.append(f"**Feature:** `{feature}`" + (" *(new)*" if is_new else ""))
        lines.append("")
        if what:
            lines.append(f"**What changed:** {what}")
            lines.append("")
        if why:
            lines.append(f"**Why:** {why}")
            lines.append("")
        if impact:
            lines.append(f"**Impact:** {impact}")
            lines.append("")
        if files:
            lines.append(f"**Files:** " + ", ".join(f"`{f}`" for f in files))
            lines.append("")
        lines.append("---")
        lines.append("")

    lines += [
        f"*Generated at {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')} from `metadata.json`*",
        "",
    ]

    return "\n".join(lines)


def main():
    metadata = load_metadata()
    content = render(metadata)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        f.write(content)

    features = len(metadata.get("features", {}))
    commits = len(metadata.get("history", []))
    print(f"Generated build-log.md — {features} features, {commits} commits tracked.")


if __name__ == "__main__":
    main()
