# Changelog

All notable changes to gitmind are documented here.

## [Unreleased]

## [0.1.0] - 2026-04-10

### Added
- Core git hook pipeline: diff → LLM → metadata.json
- `diff_reader.py` — reads diff, changed files, commit message, commit hash
- `llm.py` — Ollama + deepseek-coder integration with `format: "json"` enforcement
- `metadata.py` — feature registry with `introduced`, `files_touched`, `last_built_upon`, `commit_count`
- `engine.py` — orchestrates the full pipeline on every commit
- `install.sh` — one-command install into any git repo
- CLI query tool: `features`, `files`, `history`, `stale`
- Pytest test suite covering metadata and LLM parsing logic
- MkDocs Material documentation site

### Fixed
- Root commit edge case — `git diff HEAD~1 HEAD` fails on first commit; fallback to `git show HEAD`
- LLM JSON reliability — `deepseek-coder` returned `//` comments and trailing text; fixed with `format: "json"` + `_extract_json()` + `_coerce()`
- Feature name sanitization — collapse underscores, strip non-alphanumeric, truncate at 40 chars
