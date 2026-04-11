# gitmind

**Semantic version control.** Git tells you what changed — gitmind tells you why, and what's safe to remove.

Every commit is automatically analyzed by a local LLM (Ollama + deepseek-coder) and stored as structured metadata alongside your code. No API costs. No external services. Works with any editor.

---

## The Problem

Git log tells you files and diffs. It doesn't tell you:
- Which feature does this file belong to?
- Is this code still active or dead?
- What changed in auth over the last 3 months?
- Is it safe to delete this module?

gitmind answers all of that.

---

## How It Works

```
git commit
    ↓
post-commit hook (bash)
    ↓
diff_reader.py  →  reads diff + commit message
    ↓
llm.py          →  Ollama (deepseek-coder) analyzes the diff
    ↓
metadata.json   →  semantic summary stored in repo
    ↓
query.py        →  CLI to query features, files, staleness
```

On every commit, gitmind:
1. Reads the git diff
2. Sends it to a local LLM with a structured prompt
3. Gets back: feature name, what changed, why, impact, files touched
4. Appends to `metadata.json` in the repo

---

## Test Results

Tested on the gitmind repo itself during initial development. Here's what the system captured across 4 real commits:

**Commit 1** — Initial scaffold (root commit, no parent diff — handled gracefully via `git show HEAD` fallback)

**Commit 2** — First commit diff detection issue
```json
{
  "what_changed": "No diff found — skipping metadata update.",
  "feature_name": "first_commit_handling"
}
```
Revealed: `git diff HEAD~1 HEAD` fails on root commits. Fixed with `_is_first_commit()` guard.

**Commit 3** — JSON parsing failure
The model (`deepseek-coder`) returned JSON with `//` comments and trailing garbage text when given an open-ended prompt. Fixed by:
- Adding `format: "json"` to the Ollama API request (forces valid JSON mode)
- Adding `_extract_json()` to strip markdown fences
- Adding `_coerce()` to fix wrong field types (e.g., list where string expected)

**Commit 4** — First successful end-to-end run
```json
{
  "features": {
    "json_format_enforcement": {
      "introduced": "2026-04-10T20:08:41",
      "files_touched": ["core/llm.py"],
      "still_active": true,
      "last_built_upon": "2026-04-10T20:08:41",
      "commit_count": 1
    }
  }
}
```
Hook ran, LLM analyzed the diff, metadata written — full pipeline confirmed working.

**Key finding:** `deepseek-coder` needs `format: "json"` enforced, otherwise it outputs commentary inside JSON. With it enforced, output is clean and parseable.

---

## Quick Start

### Prerequisites

```bash
# Install Ollama (Mac)
curl -fsSL https://ollama.ai/install.sh | sh
ollama serve
ollama pull deepseek-coder
```

### Install into any git repo

```bash
# Clone gitmind
git clone https://github.com/yourusername/gitmind
cd gitmind

# Install the hook into a target repo
bash hooks/install.sh /path/to/your/repo
```

### Install into the current repo

```bash
bash hooks/install.sh .
```

That's it. The next `git commit` in that repo will trigger gitmind automatically.

---

## Query Your Codebase

```bash
# List all tracked features
python3 cli/query.py features

# Files touched by a specific feature
python3 cli/query.py files auth_middleware

# Full semantic commit history
python3 cli/query.py history

# Features with no activity in 90 days (stale/dead code)
python3 cli/query.py stale --days 90
```

---

## Project Structure

```
gitmind/
├── core/
│   ├── diff_reader.py    # reads git diffs, handles first-commit edge case
│   ├── llm.py            # Ollama interface with JSON enforcement + coercion
│   ├── metadata.py       # read/write metadata.json
│   └── engine.py         # orchestrates the pipeline
├── hooks/
│   ├── post-commit       # bash hook installed into target repo
│   └── install.sh        # copies gitmind into any repo, installs hook
├── cli/
│   └── query.py          # CLI query tool
├── metadata.json         # auto-generated — do not edit manually
└── requirements.txt
```

---

## Metadata Schema

```json
{
  "features": {
    "feature_name": {
      "introduced": "2026-04-10T20:00:00",
      "files_touched": ["src/auth.py", "src/middleware.py"],
      "still_active": true,
      "last_built_upon": "2026-04-10T20:00:00",
      "is_new_feature": false,
      "commit_count": 7
    }
  },
  "history": [
    {
      "commit_hash": "abc1234",
      "timestamp": "2026-04-10T20:00:00",
      "what_changed": "Added JWT expiry validation",
      "why_it_likely_changed": "Security requirement to reject expired tokens",
      "feature_name": "auth_middleware",
      "is_new_feature": false,
      "impact": "All protected routes now reject expired tokens",
      "files_touched": ["src/auth.py"]
    }
  ]
}
```

---

## Roadmap

| Phase | Goal | Status |
|-------|------|--------|
| 1 | Core hook — diff → LLM → metadata.json | ✅ Done |
| 2 | Feature grouping across commits | Planned |
| 3 | Staleness detection + removal planner | Planned |
| 4 | Team support — Husky, dotenv, large diff chunking | Planned |
| 5 | SQLite + ChromaDB for semantic search | Planned |
| 6 | VS Code extension + Claude Code integration | Planned |
| 7 | Open source launch | Planned |

---

## Why Local LLM?

- **Free** — no API costs per commit
- **Private** — your code never leaves your machine
- **Fast** — no network latency after model load
- **Offline** — works without internet

Cloud LLM support (Anthropic, OpenAI) is on the roadmap for teams that prefer it.

---

## License

MIT
