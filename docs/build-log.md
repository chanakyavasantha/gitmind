# Build Log

This page is generated automatically from `metadata.json` on every push — the tool is documenting itself.

Every entry below was written by gitmind analyzing its own commits via a local LLM (Ollama + deepseek-coder).
No human wrote these summaries. The feature names, file lists, and change descriptions are all LLM output.

---

## Tracked Features

| Feature | Status | Commits | Introduced | Last Active |
|---------|--------|---------|------------|-------------|
| `use_json_is_used_as_it_might_be` | ✅ active | 1 | 2026-04-10 23:02 | 2026-04-10 23:02 |
| `pin_black` | ✅ active | 1 | 2026-04-10 22:40 | 2026-04-10 22:40 |
| `amend_loop_guard` | ✅ active | 1 | 2026-04-10 22:25 | 2026-04-10 22:25 |
| `auto_build_log_generation` | ✅ active | 1 | 2026-04-10 22:00 | 2026-04-10 22:00 |
| `metadata_quality_fixes` | ✅ active | 1 | 2026-04-10 21:48 | 2026-04-10 21:48 |
| `graceful_error_handling` | ✅ active | 1 | 2026-04-10 21:45 | 2026-04-10 21:45 |
| `build_log_doc` | ✅ active | 1 | 2026-04-10 20:30 | 2026-04-10 20:30 |
| `docs_deployment` | ✅ active | 1 | 2026-04-10 20:22 | 2026-04-10 20:22 |
| `repo_professionalisation` | ✅ active | 1 | 2026-04-10 20:21 | 2026-04-10 20:21 |
| `feature_name_sanitization` | ✅ active | 1 | 2026-04-10 20:15 | 2026-04-10 20:15 |
| `json_format_enforcement` | ✅ active | 1 | 2026-04-10 20:10 | 2026-04-10 20:10 |
| `json_parsing_robustness` | ✅ active | 1 | 2026-04-10 20:08 | 2026-04-10 20:08 |
| `first_commit_handling` | ✅ active | 1 | 2026-04-10 20:05 | 2026-04-10 20:05 |
| `core_engine` | ✅ active | 1 | 2026-04-10 20:00 | 2026-04-10 20:00 |

---

## Files Per Feature

**`amend_loop_guard`**

- `hooks/post-commit`
- `hooks/install.sh`

**`auto_build_log_generation`**

- `scripts/generate_build_log.py`
- `.github/workflows/docs.yml`
- `core/metadata.py`
- `metadata.json`

**`build_log_doc`**

- `docs/build-log.md`
- `mkdocs.yml`

**`core_engine`**

- `core/diff_reader.py`
- `core/llm.py`
- `core/metadata.py`
- `core/engine.py`
- `hooks/post-commit`
- `hooks/install.sh`
- `cli/query.py`

**`docs_deployment`**

- `.github/workflows/docs.yml`

**`feature_name_sanitization`**

- `core/llm.py`
- `README.md`

**`first_commit_handling`**

- `core/diff_reader.py`
- `.gitignore`

**`graceful_error_handling`**

- `core/engine.py`
- `core/llm.py`

**`json_format_enforcement`**

- `core/llm.py`

**`json_parsing_robustness`**

- `core/llm.py`

**`metadata_quality_fixes`**

- `core/llm.py`
- `core/diff_reader.py`
- `tests/test_core.py`
- `.gitignore`

**`pin_black`**

- `.github/workflows/ci.yml`
- `pyproject.toml`

**`repo_professionalisation`**

- `.github/workflows/ci.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/release.yml`
- `docs/`
- `tests/test_core.py`
- `CONTRIBUTING.md`
- `CHANGELOG.md`
- `LICENSE`

**`use_json_is_used_as_it_might_be`**

- `_use_json__is_used_as_it_might_be_beneficial_for_handling_json_data_manipulation_tasks_or_similar_actions_more_efficiently_.py`
- `_generate_build_log.py`

---

## Commit History

Most recent first.

### `bf4c65b` — 2026-04-10 23:02

**Feature:** `use_json_is_used_as_it_might_be` *(new)*

**What changed:** The tool has been updated to improve build log generation and document its own development.

**Files:** `_use_json__is_used_as_it_might_be_beneficial_for_handling_json_data_manipulation_tasks_or_similar_actions_more_efficiently_.py`, `_generate_build_log.py`

---

### `a9921c1` — 2026-04-10 22:40

**Feature:** `pin_black`

**What changed:** Pinned black==25.1.0 in CI and added pyproject.toml with target-version=py39 to get consistent formatting across Python versions.

**Why:** CI was installing the latest black which produced different output than local Python 3.9, causing repeated check failures.

**Impact:** CI black check is now deterministic — same output on Python 3.9 locally and Python 3.11 in CI.

**Files:** `.github/workflows/ci.yml`, `pyproject.toml`

---

### `6814f6e` — 2026-04-10 22:25

**Feature:** `amend_loop_guard`

**What changed:** Added GITMIND_RUNNING env var guard to post-commit hook to prevent the metadata amend from triggering the hook again infinitely.

**Why:** --no-verify skips pre-commit and commit-msg hooks but not post-commit, causing an infinite amend loop.

**Impact:** Hook now runs exactly once per commit. metadata.json is included in the same commit automatically.

**Files:** `hooks/post-commit`, `hooks/install.sh`

---

### `1c52311` — 2026-04-10 22:00

**Feature:** `auto_build_log_generation` *(new)*

**What changed:** Added scripts/generate_build_log.py which reads metadata.json and generates docs/build-log.md automatically on every push via docs.yml.

**Why:** The hand-written build log would go stale — needed it to update from real metadata on every deploy.

**Impact:** The Build Log page on the docs site now reflects live metadata on every push.

**Files:** `scripts/generate_build_log.py`, `.github/workflows/docs.yml`, `core/metadata.py`, `metadata.json`

---

### `201839b` — 2026-04-10 21:48

**Feature:** `metadata_quality_fixes`

**What changed:** Removed .gitmind/ from git tracking, added large-diff chunking, enforced 4-word feature name limit, and filtered hallucinated file paths from LLM output.

**Why:** Four distinct quality issues identified: .gitmind committed, bad feature names, LLM overwhelmed by large diffs, fake paths like actions/checkout@v4 in files_touched.

**Impact:** Metadata is now cleaner, .gitmind/ is local-only, and large commits get summarised by file list instead of raw diff.

**Files:** `core/llm.py`, `core/diff_reader.py`, `tests/test_core.py`, `.gitignore`

---

### `ac5957f` — 2026-04-10 21:45

**Feature:** `graceful_error_handling`

**What changed:** Wrapped LLM call in try/except so Ollama timeouts and connection errors print a one-liner instead of a 30-line traceback.

**Why:** Ollama went idle between commits and the hook printed a full stack trace into the terminal.

**Impact:** Hook failures are now silent and non-blocking — the commit still succeeds.

**Files:** `core/engine.py`, `core/llm.py`

---

### `3644106` — 2026-04-10 20:30

**Feature:** `build_log_doc` *(new)*

**What changed:** Added a hand-written build log doc capturing the full development story: every commit, what broke, and what gitmind said about itself.

**Why:** New users landing on the repo needed to understand how the project evolved and that the tool was tested on itself.

**Impact:** The Build Log page shows gitmind's own self-documented history.

**Files:** `docs/build-log.md`, `mkdocs.yml`

---

### `5906386` — 2026-04-10 20:22

**Feature:** `docs_deployment`

**What changed:** Added contents:write permission and git config to allow the GitHub Actions bot to push to the gh-pages branch.

**Why:** The docs workflow failed with a 403 — the bot lacked push permission.

**Impact:** Docs now deploy successfully to GitHub Pages on every push to main.

**Files:** `.github/workflows/docs.yml`

---

### `d84525a` — 2026-04-10 20:21

**Feature:** `repo_professionalisation` *(new)*

**What changed:** Added CI/CD workflows, MkDocs Material docs site, 12-test pytest suite, black formatting, CONTRIBUTING, CHANGELOG, LICENSE, and GitHub issue templates.

**Why:** Needed the repo to look credible for open source release.

**Impact:** Every PR now gets a CI check; docs auto-deploy to GitHub Pages on every push to main.

**Files:** `.github/workflows/ci.yml`, `.github/workflows/docs.yml`, `.github/workflows/release.yml`, `docs/`, `tests/test_core.py`, `CONTRIBUTING.md`, `CHANGELOG.md`, `LICENSE`

---

### `0de4d70` — 2026-04-10 20:15

**Feature:** `feature_name_sanitization`

**What changed:** Capped feature names at 4 words / 40 chars with underscore collapsing, and added the README with real test findings.

**Why:** The model was generating 90-character feature names that were unreadable.

**Impact:** Feature names are now short, readable snake_case identifiers.

**Files:** `core/llm.py`, `README.md`

---

### `08fe52f` — 2026-04-10 20:10

**Feature:** `json_format_enforcement`

**What changed:** Added format:json to the Ollama API request to constrain the model's output tokenizer to valid JSON only.

**Why:** Without it, deepseek-coder appended // comments and trailing prose — both invalid JSON.

**Impact:** First successful end-to-end run: hook fired, LLM analyzed diff, metadata written cleanly.

**Files:** `core/llm.py`

---

### `2f91e1d` — 2026-04-10 20:08

**Feature:** `json_parsing_robustness`

**What changed:** Added _extract_json() to strip markdown fences and _coerce() to fix wrong field types returned by the LLM.

**Why:** deepseek-coder returned arrays where strings were expected and wrapped output in markdown code blocks.

**Impact:** Parser now survives malformed LLM responses without crashing.

**Files:** `core/llm.py`

---

### `ffaff32` — 2026-04-10 20:05

**Feature:** `first_commit_handling`

**What changed:** Fixed the root commit edge case where git diff HEAD~1 HEAD fails with no parent, and added .gitignore to exclude the venv.

**Why:** The initial commit had no HEAD~1 to diff against — the hook silently skipped it.

**Impact:** gitmind now handles the very first commit in any repo using git show HEAD as a fallback.

**Files:** `core/diff_reader.py`, `.gitignore`

---

### `6e78acd` — 2026-04-10 20:00

**Feature:** `core_engine` *(new)*

**What changed:** Built the initial gitmind pipeline: diff reader, Ollama LLM analyzer, metadata writer, CLI query tool, and install hook.

**Why:** Project inception — needed a working end-to-end proof of concept.

**Impact:** Every git commit in an instrumented repo now triggers semantic analysis automatically.

**Files:** `core/diff_reader.py`, `core/llm.py`, `core/metadata.py`, `core/engine.py`, `hooks/post-commit`, `hooks/install.sh`, `cli/query.py`

---

*Generated at 2026-04-11 03:17 UTC from `metadata.json`*
