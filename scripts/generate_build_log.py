#!/usr/bin/env python3
"""
Reads metadata.json and generates docs/build-log.md automatically.
Run by the docs.yml workflow before MkDocs builds the site.
"""

import json
import os
import sys
from datetime import datetime
from typing import Optional

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
METADATA_PATH = os.path.join(REPO_ROOT, "metadata.json")
OUTPUT_PATH = os.path.join(REPO_ROOT, "docs", "build-log.md")

# Map file path prefixes to human-readable capability areas.
# Order matters — first match wins.
CAPABILITY_AREAS = [
    ("core/", "Core Pipeline", "Diff reading, LLM analysis, metadata storage"),
    ("core/llm.py", "LLM Integration", "Ollama interface, JSON enforcement, prompt design"),
    ("cli/", "CLI", "Query tool for features, files, staleness"),
    ("hooks/", "Git Hooks", "Post-commit hook, install script, amend loop guard"),
    (".github/workflows/", "CI / CD", "Automated tests, docs deployment, releases"),
    ("tests/", "Test Suite", "Pytest coverage for core pipeline"),
    ("scripts/", "Developer Scripts", "Reindex, build log generation, demo recording"),
    ("docs/", "Documentation", "MkDocs site, quickstart, CLI reference, roadmap"),
    ("mkdocs.yml", "Documentation", "MkDocs site, quickstart, CLI reference, roadmap"),
]


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
        return datetime.fromisoformat(iso).strftime("%Y-%m-%d")
    except Exception:
        return iso[:10] if iso else "unknown"


def _capability_for(path: str) -> Optional[str]:
    for prefix, name, _ in CAPABILITY_AREAS:
        if path.startswith(prefix) or path == prefix.rstrip("/"):
            return name
    return None


def build_capability_summary(metadata: dict) -> list[dict]:
    """
    Derive high-level capability areas from files touched across all commits.
    Returns list of {name, description, files_changed, first_seen, last_seen}.
    """
    areas: dict[str, dict] = {}

    for entry in metadata.get("history", []):
        ts = entry.get("timestamp", "")
        for f in entry.get("files_touched", []):
            cap = _capability_for(f)
            if cap is None:
                continue
            if cap not in areas:
                # Find the description for this capability
                desc = next(
                    (d for p, n, d in CAPABILITY_AREAS if n == cap), ""
                )
                areas[cap] = {
                    "name": cap,
                    "description": desc,
                    "files": set(),
                    "first_seen": ts,
                    "last_seen": ts,
                }
            a = areas[cap]
            a["files"].add(f)
            if ts and (not a["first_seen"] or ts < a["first_seen"]):
                a["first_seen"] = ts
            if ts and ts > a["last_seen"]:
                a["last_seen"] = ts

    # Convert to sorted list (by first_seen)
    result = []
    for cap in areas.values():
        result.append(
            {
                "name": cap["name"],
                "description": cap["description"],
                "file_count": len(cap["files"]),
                "first_seen": cap["first_seen"],
                "last_seen": cap["last_seen"],
            }
        )
    result.sort(key=lambda x: x["first_seen"])
    return result


def render(metadata: dict) -> str:
    history = metadata.get("history", [])
    capabilities = build_capability_summary(metadata)
    total_commits = len(history)
    first_date = format_date(history[0]["timestamp"]) if history else "—"
    last_date = format_date(history[-1]["timestamp"]) if history else "—"

    lines = [
        "# Build Log",
        "",
        "This page is generated automatically from `metadata.json` on every push — gitmind is documenting itself.",
        "Every commit was analyzed by a local LLM (Ollama + qwen2.5-coder:7b). No human wrote these summaries.",
        "",
        f"**{total_commits} commits** · {first_date} → {last_date}",
        "",
        "---",
        "",
    ]

    # Capability summary table
    lines += [
        "## What Was Built",
        "",
        "High-level capability areas derived from files changed across all commits:",
        "",
        "| Capability | What it covers | Files changed | Last active |",
        "|------------|----------------|:-------------:|-------------|",
    ]
    for cap in capabilities:
        lines.append(
            f"| **{cap['name']}** | {cap['description']} "
            f"| {cap['file_count']} | {format_date(cap['last_seen'])} |"
        )

    lines += [
        "",
        "---",
        "",
        "## Development Timeline",
        "",
        "Most recent commit first.",
        "",
    ]

    for entry in reversed(history):
        commit = entry.get("commit_hash", "")[:7]
        ts = format_date(entry.get("timestamp", ""))
        what = entry.get("what_changed", "")
        why = entry.get("why_it_likely_changed", "")
        impact = entry.get("impact", "")
        files = entry.get("files_touched", [])
        is_new = entry.get("is_new_feature", False)
        feature = entry.get("feature_name", "")

        new_badge = " ✨" if is_new else ""
        lines.append(f"### `{commit}` &nbsp; {ts}{new_badge}")
        lines.append("")

        if what:
            lines.append(f"{what}")
            lines.append("")
        if why:
            lines.append(f"*{why}*")
            lines.append("")
        if impact:
            lines.append(f"**Impact:** {impact}")
            lines.append("")
        if files:
            file_list = " &nbsp;·&nbsp; ".join(f"`{f}`" for f in files[:6])
            if len(files) > 6:
                file_list += f" &nbsp;·&nbsp; *+{len(files) - 6} more*"
            lines.append(f"Files: {file_list}")
            lines.append("")
        if feature:
            lines.append(f"<small>*gitmind tag: `{feature}`*</small>")
            lines.append("")
        lines.append("---")
        lines.append("")

    lines += [
        f"*Generated {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')} from `metadata.json`*",
        "",
    ]

    return "\n".join(lines)


def main():
    metadata = load_metadata()
    content = render(metadata)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        f.write(content)

    capabilities = build_capability_summary(metadata)
    commits = len(metadata.get("history", []))
    print(
        f"Generated build-log.md — {len(capabilities)} capability areas, {commits} commits."
    )


if __name__ == "__main__":
    main()
