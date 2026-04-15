# gitmind

> Git remembers what changed. This remembers why.

![CI](https://github.com/chanakyavasantha/gitmind/actions/workflows/ci.yml/badge.svg)
![License](https://img.shields.io/github/license/chanakyavasantha/gitmind)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Ollama](https://img.shields.io/badge/LLM-Ollama-black)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

**Semantic version control plus living architecture docs.** Git tells you what changed — gitmind tells you why, what system structure exists today, and where the risks are.

Every commit is automatically analyzed by a local LLM (Ollama + qwen2.5-coder:7b), then merged into structured metadata and an incremental architecture model stored alongside your code. No API costs. No external services. Works with any editor.

---

## Demo

![gitmind demo](docs/demo.gif)

---

## The Problem

```bash
git log --oneline
a3f92b1 fix auth
9c21d44 update middleware
3b891ef refactor
```

This tells you nothing useful. Which feature does `middleware.py` belong to? Is it still active? What's safe to delete after 6 months?

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
llm.py          →  Ollama (qwen2.5-coder:7b) analyzes the diff
    ↓
metadata.json   →  semantic commit/feature history
    ↓
system_model.json / findings.json / dashboard.json
    ↓
docs/*.md       →  architecture, contracts, quality findings
    ↓
dashboard.py    →  local architecture and staleness dashboard
```

---

## Quick Start

```bash
# 1. Install Ollama and pull the model
curl -fsSL https://ollama.ai/install.sh | sh
ollama serve
ollama pull qwen2.5-coder:7b

# 2. Clone gitmind and install into your repo
git clone https://github.com/chanakyavasantha/gitmind
bash gitmind/hooks/install.sh /path/to/your/repo

# 3. Make a commit — gitmind runs automatically
cd /path/to/your/repo
git commit -m "add rate limiting to login"
```

Output:
```
[gitmind] Analyzing commit...
[gitmind] Feature tracked: auth_rate_limiting
[gitmind] Added rate limiting to the login endpoint
```

---

## Query Your Codebase

```bash
# List all tracked features
python3 cli/query.py features

# Files touched by a feature
python3 cli/query.py files auth_middleware

# Full semantic commit history
python3 cli/query.py history

# Dead code candidates — no activity in 90 days
python3 cli/query.py stale --days 90
```

---

## Generated Docs And Dashboard

gitmind now keeps both human-readable docs and machine-readable architecture state in the repo.

Generated markdown:

- `docs/architecture.md` — current system structure, component graph, and public API reference
- `docs/contracts.md` — module contracts for changed source files
- `docs/quality-findings.md` — architecture risks, quality findings, and strengths

Generated JSON:

- `metadata/system_model.json` — incremental architecture model
- `metadata/findings.json` — structured findings for the current codebase
- `metadata/dashboard.json` — precomputed dashboard payload

To inspect them:

```bash
# Open the local dashboard
python3 cli/dashboard.py

# Or serve the docs site
mkdocs serve
```

The dashboard runs at `http://localhost:4242` by default.

---

## Metadata Schema

```json
{
  "features": {
    "auth_middleware": {
      "introduced": "2026-04-10T20:00:00",
      "files_touched": ["src/auth.py", "src/middleware.py"],
      "still_active": true,
      "last_built_upon": "2026-04-10T20:00:00",
      "commit_count": 7
    }
  },
  "history": [
    {
      "commit_hash": "4f2a91c",
      "timestamp": "2026-04-10T20:00:00",
      "what_changed": "Added JWT expiry validation",
      "why_it_likely_changed": "Security requirement to reject expired tokens",
      "feature_name": "auth_middleware",
      "impact": "All protected routes now reject expired tokens",
      "files_touched": ["src/auth.py"]
    }
  ]
}
```

---

## Test Results

Tested on the gitmind repo itself during initial development:

| Commit | Hook result | Finding |
|--------|-------------|---------|
| Initial scaffold | `No diff found` — skipped | Root commit has no `HEAD~1` — fixed with `git show HEAD` fallback |
| First-commit fix | JSON parse error | `deepseek-coder` outputs `//` comments — fixed with `format: "json"` |
| Format enforcement | Parse error still | Field type mismatches — fixed with `_extract_json()` + `_coerce()` |
| Robust parser | **Feature tracked: gitmind** | First clean end-to-end run |
| Model upgrade | Clean names on all commits | Switched to `qwen2.5-coder:7b` — no hallucinations, clean JSON |

**Current model:** `qwen2.5-coder:7b` — significantly better feature naming and JSON reliability than `deepseek-coder`.

---

## Project Structure

```
gitmind/
├── core/
│   ├── architecture/     # extraction, analyzers, contracts, ADRs, renderers
│   ├── diff_reader.py    # reads git diffs, handles first-commit edge case
│   ├── llm.py            # Ollama interface with JSON enforcement + coercion
│   ├── metadata.py       # read/write metadata.json
│   ├── system_model.py   # compatibility wrapper for architecture model
│   ├── doc_generator.py  # compatibility wrapper for doc generation
│   └── engine.py         # orchestrates commit-time updates
├── hooks/
│   ├── post-commit       # bash hook installed into target repo
│   └── install.sh        # copies gitmind into any repo, installs hook
├── cli/
│   ├── query.py          # feature/history query tool
│   ├── dashboard.py      # local dashboard server
│   └── dashboard.html    # dashboard UI
├── metadata/             # generated architecture model + dashboard payload
├── docs/                 # generated and hand-written docs
├── tests/
│   └── test_core.py      # pytest suite
└── requirements.txt
```

---

## Roadmap

| Phase | Goal | Status |
|-------|------|--------|
| 1 | Core hook — diff → LLM → metadata.json | ✅ Done |
| 2 | Feature grouping across commits | Planned |
| 3 | Staleness detection + removal planner | Planned |
| 4 | Team support — Husky, large diff chunking | Planned |
| 5 | SQLite + ChromaDB semantic search | Planned |
| 6 | VS Code extension + Claude Code integration | Planned |
| 7 | Open source launch | Planned |

Full roadmap: [docs/roadmap.md](docs/roadmap.md)

---

## Why Local LLM?

- **Free** — no API costs per commit
- **Private** — your code never leaves your machine
- **Offline** — works without internet after model pull

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

```bash
pip install pytest black
pytest tests/ -v
black core/ cli/
```

## License

MIT
