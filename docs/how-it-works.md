# How It Works

gitmind is a thin pipeline that runs on every `git commit`. Here's what happens under the hood.

---

## Pipeline

```
git commit
    │
    ▼
hooks/post-commit          (bash — triggers on every commit)
    │
    ▼
core/engine.py             (orchestrates the pipeline)
    │
    ├── diff_reader.py     (reads diff, changed files, commit message, hash)
    │
    ├── llm.py             (sends diff to Ollama, parses response)
    │
    └── metadata.py        (updates metadata.json)
```

---

## Step 1 — Git Hook

The hook installed at `.git/hooks/post-commit` is a 5-line bash script:

```bash
GITMIND_DIR="$(git rev-parse --show-toplevel)/.gitmind"
"$GITMIND_DIR/venv/bin/python" "$GITMIND_DIR/core/engine.py"
```

It finds the repo root, activates the virtualenv, runs the engine.

---

## Step 2 — Diff Reader

`diff_reader.py` runs four git commands:

| Command | Purpose |
|---------|---------|
| `git diff HEAD~1 HEAD` | Full diff text (falls back to `git show HEAD` on first commit) |
| `git diff --name-only HEAD~1 HEAD` | List of changed files |
| `git log -1 --pretty=%B` | Commit message |
| `git rev-parse HEAD` | Commit hash |

---

## Step 3 — LLM Analysis

The diff + commit message are sent to Ollama with a structured prompt:

```python
{
    "model": "deepseek-coder",
    "prompt": "...",
    "stream": False,
    "format": "json"     # forces valid JSON output
}
```

The prompt asks for exactly this structure:

```json
{
    "what_changed": "one sentence",
    "why_it_likely_changed": "one sentence",
    "feature_name": "snake_case_name",
    "is_new_feature": true,
    "impact": "one sentence",
    "files_touched": ["file1.py"]
}
```

### JSON Robustness

LLMs don't always return clean JSON. gitmind handles this with two layers:

- **`_extract_json()`** — strips markdown fences, finds the first `{...}` block
- **`_coerce()`** — fixes wrong field types (e.g. list where string expected), sanitizes and truncates `feature_name` to 40 characters

---

## Step 4 — Metadata

`metadata.py` maintains a single `metadata.json` file with two sections:

**Feature registry** — one entry per unique feature, updated on every related commit:

```json
"auth_middleware": {
    "introduced": "2026-04-10T20:00:00",
    "files_touched": ["src/auth.py", "src/middleware.py"],
    "still_active": true,
    "last_built_upon": "2026-04-10T20:00:00",
    "is_new_feature": false,
    "commit_count": 7
}
```

**History** — append-only log of every analyzed commit:

```json
{
    "commit_hash": "4f2a91c",
    "timestamp": "2026-04-10T20:00:00",
    "what_changed": "Added rate limiting to login endpoint",
    "why_it_likely_changed": "Prevent brute force attacks",
    "feature_name": "auth_rate_limiting",
    "is_new_feature": false,
    "impact": "All login attempts now rate limited at 5/minute",
    "files_touched": ["src/auth/login.py"]
}
```

---

## Design Decisions

**Why JSON and not SQLite?**
JSON is the simplest format that works. It lives in the repo, gets committed, gets reviewed in PRs, and is readable by any tool. SQLite comes in Phase 5 when queries get complex.

**Why Ollama and not an API?**
Your code is private. An API-based LLM means every diff leaves your machine. Ollama keeps everything local and free.

**Why `format: "json"` matters**
Without it, `deepseek-coder` appends commentary inside JSON blocks and adds `//` comments — both invalid JSON. The `format` parameter constrains the model's output tokenizer to valid JSON only.
