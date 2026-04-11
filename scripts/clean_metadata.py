#!/usr/bin/env python3
"""
One-time script to rebuild metadata.json from the real git history.
Discards all garbled entries from the amend loop and assigns clean feature names.
Run once: python3 scripts/clean_metadata.py
"""

import json
import os
from datetime import datetime

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
METADATA_PATH = os.path.join(REPO_ROOT, "metadata.json")

# Ground truth: real commits mapped to clean feature names and summaries
COMMITS = [
    {
        "commit_hash": "6e78acd",
        "feature_name": "core_engine",
        "is_new_feature": True,
        "what_changed": "Built the initial gitmind pipeline: diff reader, Ollama LLM analyzer, metadata writer, CLI query tool, and install hook.",
        "why_it_likely_changed": "Project inception — needed a working end-to-end proof of concept.",
        "impact": "Every git commit in an instrumented repo now triggers semantic analysis automatically.",
        "files_touched": [
            "core/diff_reader.py",
            "core/llm.py",
            "core/metadata.py",
            "core/engine.py",
            "hooks/post-commit",
            "hooks/install.sh",
            "cli/query.py",
        ],
        "timestamp": "2026-04-10T20:00:00",
    },
    {
        "commit_hash": "ffaff32",
        "feature_name": "first_commit_handling",
        "is_new_feature": False,
        "what_changed": "Fixed the root commit edge case where git diff HEAD~1 HEAD fails with no parent, and added .gitignore to exclude the venv.",
        "why_it_likely_changed": "The initial commit had no HEAD~1 to diff against — the hook silently skipped it.",
        "impact": "gitmind now handles the very first commit in any repo using git show HEAD as a fallback.",
        "files_touched": ["core/diff_reader.py", ".gitignore"],
        "timestamp": "2026-04-10T20:05:00",
    },
    {
        "commit_hash": "2f91e1d",
        "feature_name": "json_parsing_robustness",
        "is_new_feature": False,
        "what_changed": "Added _extract_json() to strip markdown fences and _coerce() to fix wrong field types returned by the LLM.",
        "why_it_likely_changed": "deepseek-coder returned arrays where strings were expected and wrapped output in markdown code blocks.",
        "impact": "Parser now survives malformed LLM responses without crashing.",
        "files_touched": ["core/llm.py"],
        "timestamp": "2026-04-10T20:08:00",
    },
    {
        "commit_hash": "08fe52f",
        "feature_name": "json_format_enforcement",
        "is_new_feature": False,
        "what_changed": "Added format:json to the Ollama API request to constrain the model's output tokenizer to valid JSON only.",
        "why_it_likely_changed": "Without it, deepseek-coder appended // comments and trailing prose — both invalid JSON.",
        "impact": "First successful end-to-end run: hook fired, LLM analyzed diff, metadata written cleanly.",
        "files_touched": ["core/llm.py"],
        "timestamp": "2026-04-10T20:10:00",
    },
    {
        "commit_hash": "0de4d70",
        "feature_name": "feature_name_sanitization",
        "is_new_feature": False,
        "what_changed": "Capped feature names at 4 words / 40 chars with underscore collapsing, and added the README with real test findings.",
        "why_it_likely_changed": "The model was generating 90-character feature names that were unreadable.",
        "impact": "Feature names are now short, readable snake_case identifiers.",
        "files_touched": ["core/llm.py", "README.md"],
        "timestamp": "2026-04-10T20:15:00",
    },
    {
        "commit_hash": "d84525a",
        "feature_name": "repo_professionalisation",
        "is_new_feature": True,
        "what_changed": "Added CI/CD workflows, MkDocs Material docs site, 12-test pytest suite, black formatting, CONTRIBUTING, CHANGELOG, LICENSE, and GitHub issue templates.",
        "why_it_likely_changed": "Needed the repo to look credible for open source release.",
        "impact": "Every PR now gets a CI check; docs auto-deploy to GitHub Pages on every push to main.",
        "files_touched": [
            ".github/workflows/ci.yml",
            ".github/workflows/docs.yml",
            ".github/workflows/release.yml",
            "docs/",
            "tests/test_core.py",
            "CONTRIBUTING.md",
            "CHANGELOG.md",
            "LICENSE",
        ],
        "timestamp": "2026-04-10T20:21:00",
    },
    {
        "commit_hash": "5906386",
        "feature_name": "docs_deployment",
        "is_new_feature": False,
        "what_changed": "Added contents:write permission and git config to allow the GitHub Actions bot to push to the gh-pages branch.",
        "why_it_likely_changed": "The docs workflow failed with a 403 — the bot lacked push permission.",
        "impact": "Docs now deploy successfully to GitHub Pages on every push to main.",
        "files_touched": [".github/workflows/docs.yml"],
        "timestamp": "2026-04-10T20:22:00",
    },
    {
        "commit_hash": "3644106",
        "feature_name": "build_log_doc",
        "is_new_feature": True,
        "what_changed": "Added a hand-written build log doc capturing the full development story: every commit, what broke, and what gitmind said about itself.",
        "why_it_likely_changed": "New users landing on the repo needed to understand how the project evolved and that the tool was tested on itself.",
        "impact": "The Build Log page shows gitmind's own self-documented history.",
        "files_touched": ["docs/build-log.md", "mkdocs.yml"],
        "timestamp": "2026-04-10T20:30:00",
    },
    {
        "commit_hash": "ac5957f",
        "feature_name": "graceful_error_handling",
        "is_new_feature": False,
        "what_changed": "Wrapped LLM call in try/except so Ollama timeouts and connection errors print a one-liner instead of a 30-line traceback.",
        "why_it_likely_changed": "Ollama went idle between commits and the hook printed a full stack trace into the terminal.",
        "impact": "Hook failures are now silent and non-blocking — the commit still succeeds.",
        "files_touched": ["core/engine.py", "core/llm.py"],
        "timestamp": "2026-04-10T21:45:00",
    },
    {
        "commit_hash": "201839b",
        "feature_name": "metadata_quality_fixes",
        "is_new_feature": False,
        "what_changed": "Removed .gitmind/ from git tracking, added large-diff chunking, enforced 4-word feature name limit, and filtered hallucinated file paths from LLM output.",
        "why_it_likely_changed": "Four distinct quality issues identified: .gitmind committed, bad feature names, LLM overwhelmed by large diffs, fake paths like actions/checkout@v4 in files_touched.",
        "impact": "Metadata is now cleaner, .gitmind/ is local-only, and large commits get summarised by file list instead of raw diff.",
        "files_touched": [
            "core/llm.py",
            "core/diff_reader.py",
            "tests/test_core.py",
            ".gitignore",
        ],
        "timestamp": "2026-04-10T21:48:00",
    },
    {
        "commit_hash": "1c52311",
        "feature_name": "auto_build_log_generation",
        "is_new_feature": True,
        "what_changed": "Added scripts/generate_build_log.py which reads metadata.json and generates docs/build-log.md automatically on every push via docs.yml.",
        "why_it_likely_changed": "The hand-written build log would go stale — needed it to update from real metadata on every deploy.",
        "impact": "The Build Log page on the docs site now reflects live metadata on every push.",
        "files_touched": [
            "scripts/generate_build_log.py",
            ".github/workflows/docs.yml",
            "core/metadata.py",
            "metadata.json",
        ],
        "timestamp": "2026-04-10T22:00:00",
    },
    {
        "commit_hash": "6814f6e",
        "feature_name": "amend_loop_guard",
        "is_new_feature": False,
        "what_changed": "Added GITMIND_RUNNING env var guard to post-commit hook to prevent the metadata amend from triggering the hook again infinitely.",
        "why_it_likely_changed": "--no-verify skips pre-commit and commit-msg hooks but not post-commit, causing an infinite amend loop.",
        "impact": "Hook now runs exactly once per commit. metadata.json is included in the same commit automatically.",
        "files_touched": ["hooks/post-commit", "hooks/install.sh"],
        "timestamp": "2026-04-10T22:25:00",
    },
    {
        "commit_hash": "a9921c1",
        "feature_name": "pin_black",
        "is_new_feature": False,
        "what_changed": "Pinned black==25.1.0 in CI and added pyproject.toml with target-version=py39 to get consistent formatting across Python versions.",
        "why_it_likely_changed": "CI was installing the latest black which produced different output than local Python 3.9, causing repeated check failures.",
        "impact": "CI black check is now deterministic — same output on Python 3.9 locally and Python 3.11 in CI.",
        "files_touched": [".github/workflows/ci.yml", "pyproject.toml"],
        "timestamp": "2026-04-10T22:40:00",
    },
]


def rebuild():
    features = {}
    history = []

    for c in COMMITS:
        name = c["feature_name"]
        ts = c["timestamp"]
        files = c["files_touched"]

        if name not in features:
            features[name] = {
                "introduced": ts,
                "files_touched": [],
                "still_active": True,
                "last_built_upon": ts,
                "is_new_feature": c["is_new_feature"],
                "commit_count": 0,
            }

        entry = features[name]
        for f in files:
            if f and f not in entry["files_touched"]:
                entry["files_touched"].append(f)
        entry["last_built_upon"] = ts
        entry["commit_count"] += 1

        history.append(
            {
                "commit_hash": c["commit_hash"],
                "timestamp": ts,
                "what_changed": c["what_changed"],
                "why_it_likely_changed": c["why_it_likely_changed"],
                "feature_name": name,
                "is_new_feature": c["is_new_feature"],
                "impact": c["impact"],
                "files_touched": files,
            }
        )

    data = {"features": features, "history": history}
    with open(METADATA_PATH, "w") as f:
        json.dump(data, f, indent=2)

    print(f"Rebuilt metadata.json — {len(features)} features, {len(history)} commits.")


if __name__ == "__main__":
    rebuild()
