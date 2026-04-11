# gitmind

**Git remembers what changed. This remembers why.**

gitmind is a local-first semantic layer on top of git. Every commit is analyzed by a local LLM and stored as structured metadata — so you can answer questions no git log ever could.

---

## The Problem

```bash
git log --oneline
```
```
a3f92b1 fix auth
9c21d44 update middleware
3b891ef refactor
```

This tells you nothing. Which feature does `middleware.py` belong to? Is it still active? When was authentication last worked on? What's safe to delete?

gitmind answers all of that.

---

## What It Does

On every `git commit`, gitmind automatically:

1. Reads the diff
2. Sends it to a local LLM (Ollama + deepseek-coder)
3. Extracts: feature name, what changed, why, impact, files touched
4. Writes it to `metadata.json` in your repo

Then you can query it:

```bash
python3 cli/query.py features
python3 cli/query.py files auth_middleware
python3 cli/query.py stale --days 90
```

---

## Key Properties

- **Local-first** — Ollama runs on your machine. Your code never leaves.
- **Free** — no API costs per commit.
- **Editor agnostic** — metadata lives in the repo. VS Code, Cursor, Neovim — all pick it up.
- **Zero new tools** — hooks into git, nothing else to learn.

---

## Quick Demo

```
$ git commit -m "add rate limiting to login endpoint"

[gitmind] Analyzing commit...
[gitmind] Feature tracked: auth_rate_limiting
[gitmind] Added rate limiting to the login endpoint to prevent brute force attacks

[main 4f2a91c] add rate limiting to login endpoint
```

```bash
$ python3 cli/query.py features

  auth_rate_limiting [active] — 1 commits, last touched 2026-04-10
  oauth_flow         [active] — 7 commits, last touched 2026-03-22
  legacy_export      [stale]  — 2 commits, last touched 2025-11-03
```

---

[Get started in 5 minutes →](quickstart.md)
