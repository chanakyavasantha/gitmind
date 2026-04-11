# CLI Reference

All commands are run via `cli/query.py`.

```bash
python3 cli/query.py <command> [options]
```

---

## `features`

List all tracked features with status, commit count, and last activity.

```bash
python3 cli/query.py features
```

**Output:**

```
  auth_middleware    [active] — 7 commits, last touched 2026-04-10
  oauth_flow         [active] — 3 commits, last touched 2026-03-22
  legacy_export      [stale]  — 2 commits, last touched 2025-11-03
```

---

## `files <feature>`

Show all files ever touched by a feature.

```bash
python3 cli/query.py files auth_middleware
```

**Output:**

```
Files touched by 'auth_middleware':
  src/auth.py
  src/middleware.py
  tests/test_auth.py
```

Use this to answer: "what do I need to change or delete if I remove this feature?"

---

## `history`

Show the full semantic commit history, most recent first.

```bash
python3 cli/query.py history
```

**Output:**

```
  [2026-04-10] 4f2a91c auth_rate_limiting: Added rate limiting to login endpoint
  [2026-04-09] 9c21d44 oauth_flow: Connected OAuth callback to session store
  [2026-03-22] 3b891ef legacy_export: Fixed CSV encoding for special characters
```

---

## `stale`

Show features with no commit activity in the last N days. Default: 90 days.

```bash
python3 cli/query.py stale
python3 cli/query.py stale --days 30
python3 cli/query.py stale --days 180
```

**Output:**

```
Features with no activity in the last 90 days:
  legacy_export — last touched 2025-11-03, files: ['src/export.py', 'src/csv_writer.py']
  old_dashboard — last touched 2025-09-14, files: ['src/dashboard/v1.py']
```

Use this to find dead code candidates before a cleanup sprint.

---

## Metadata file

The underlying data is at `.gitmind/metadata.json`. You can read it directly or build your own tooling on top of it.

```bash
cat .gitmind/metadata.json | python3 -m json.tool
```
