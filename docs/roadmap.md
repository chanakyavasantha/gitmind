# Roadmap

gitmind is built in phases, each one delivering real value before the next begins.

---

## Phase 1 — Core Engine ✅ Done

Every commit generates a semantic summary automatically.

- Git `post-commit` hook in bash
- `diff_reader.py` — reads diff, files, commit message, hash
- `llm.py` — Ollama + deepseek-coder with JSON enforcement and coercion
- `metadata.py` — feature registry + append-only history
- `install.sh` — one command setup into any repo
- CLI: `features`, `files`, `history`, `stale`

---

## Phase 2 — Feature Grouping

Group changes by feature across commits, not just by file.

- LLM identifies whether a change extends an existing feature or introduces a new one
- Cross-commit feature graph: feature → commits → files
- Richer metadata: `depends_on`, `related_features`
- CLI: `gitmind graph auth_middleware`

---

## Phase 3 — Staleness Detection

Identify dead code candidates automatically.

- Scanner checks `last_built_upon` across all features
- Detects shared file conflicts before suggesting removal
- Outputs a removal plan: "safe to delete", "has dependents", "needs review"
- CLI: `gitmind scan` — ranked staleness report

---

## Phase 4 — Team Support

Works across a whole engineering team without manual setup.

- Husky integration — hooks install automatically on `npm install`
- `.env`-based API key management for cloud LLM fallback
- Large diff chunking — commits with 1000+ line diffs handled gracefully
- Configurable model per repo via `.gitmind/config.json`

---

## Phase 5 — Query Layer

Make the metadata actually queryable at scale.

- SQLite migration for structured queries
- ChromaDB for semantic vector search over history
- Natural language queries: "when did auth logic last change"
- CLI: `gitmind why auth.py`, `gitmind history last 30 days`

---

## Phase 6 — Editor Integration

Surface metadata where developers already work.

- VS Code extension — shows feature metadata inline on file open
- Claude Code integration via `AGENTS.md`
- Cursor picks it up automatically since metadata lives in repo

---

## Phase 7 — Open Source Launch

Get real users and community feedback.

- GitHub Actions CI
- Demo GIF in README
- Post on Hacker News and r/devtools
- Contributing guide and good first issues

---

## What's Not on the Roadmap (Yet)

- **Web UI** — CLI first, browser later
- **Cloud sync** — local first by design
- **GitHub integration** — PR-level summaries are interesting but not core

Have an idea? [Open a feature request](https://github.com/chanakyavasantha/gitmind/issues/new?template=feature_request.md).
