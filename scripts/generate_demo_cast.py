#!/usr/bin/env python3
"""
Generates a scripted asciinema cast file for the gitmind demo.
Produces docs/demo.cast, then call agg to convert to GIF.
"""

import json
import os

OUT = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", "demo.cast"
)

WIDTH = 82
HEIGHT = 26


def cast(events):
    lines = [
        json.dumps(
            {
                "version": 2,
                "width": WIDTH,
                "height": HEIGHT,
                "title": "gitmind — semantic version control",
            }
        )
    ]
    for t, text in events:
        lines.append(json.dumps([round(t, 3), "o", text]))
    return "\n".join(lines) + "\n"


def type_cmd(t, cmd, delay=0.06):
    """Simulate typing a command character by character."""
    events = []
    events.append((t, "\x1b[32m$\x1b[0m "))
    t += 0.1
    for ch in cmd:
        events.append((t, ch))
        t += delay
    events.append((t, "\r\n"))
    t += 0.1
    return events, t


def output(t, text, pause=0.04):
    """Emit output lines with a small delay between each."""
    events = []
    for line in text:
        events.append((t, line + "\r\n"))
        t += pause
    return events, t


def blank(t, seconds):
    return [(t, "")], t + seconds


def build():
    events = []
    t = 0.3

    # --- prompt ---
    e, t = output(
        t,
        [
            "\x1b[1;36m# gitmind — every commit generates semantic metadata\x1b[0m",
            "",
        ],
        pause=0.5,
    )
    events += e

    # --- show a boring git log ---
    e, t = type_cmd(t, "git log --oneline")
    events += e
    t += 0.3
    e, t = output(
        t,
        [
            "\x1b[33ma3f92b1\x1b[0m fix auth",
            "\x1b[33m9c21d44\x1b[0m update middleware",
            "\x1b[33m3b891ef\x1b[0m refactor",
            "\x1b[33m1a72fce\x1b[0m add login",
            "",
            "\x1b[2m# meaningless. which feature is auth.py part of? is it still active?\x1b[0m",
            "",
        ],
        pause=0.06,
    )
    events += e
    t += 0.6

    # --- install gitmind ---
    e, t = type_cmd(t, "bash gitmind/hooks/install.sh .")
    events += e
    t += 0.3
    e, t = output(
        t,
        [
            "Installing gitmind into /your/project...",
            "Creating virtualenv...",
            "Installing dependencies...",
            "\x1b[32mDone. gitmind is now active.\x1b[0m",
            "",
        ],
        pause=0.1,
    )
    events += e
    t += 0.5

    # --- make a commit ---
    e, t = type_cmd(t, 'git commit -m "add rate limiting to login endpoint"')
    events += e
    t += 0.4

    e, t = output(
        t,
        [
            "\x1b[35m[gitmind]\x1b[0m Analyzing commit...",
        ],
        pause=0.1,
    )
    events += e

    # simulate LLM thinking
    for dot in ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]:
        events.append((t, f"\r\x1b[35m[gitmind]\x1b[0m Analyzing commit... {dot}"))
        t += 0.18

    events.append((t, "\r\x1b[K"))
    t += 0.1

    e, t = output(
        t,
        [
            "\x1b[35m[gitmind]\x1b[0m \x1b[32mFeature tracked:\x1b[0m auth_rate_limiting",
            "\x1b[35m[gitmind]\x1b[0m Added rate limiting to the login endpoint to prevent brute force.",
            "",
            "\x1b[33m[main 4f2a91c]\x1b[0m add rate limiting to login endpoint",
            " 2 files changed, 18 insertions(+), 1 deletion(-)",
            "",
        ],
        pause=0.08,
    )
    events += e
    t += 0.6

    # --- query features ---
    e, t = type_cmd(t, "python3 gitmind/cli/query.py features")
    events += e
    t += 0.3
    e, t = output(
        t,
        [
            "  \x1b[36mauth_rate_limiting\x1b[0m  [active] — 1 commit,  last touched \x1b[33m2026-04-10\x1b[0m",
            "  \x1b[36mauth_middleware\x1b[0m     [active] — 7 commits, last touched \x1b[33m2026-03-22\x1b[0m",
            "  \x1b[36moauth_flow\x1b[0m          [active] — 3 commits, last touched \x1b[33m2026-03-10\x1b[0m",
            "  \x1b[31mlegacy_export\x1b[0m       [stale]  — 2 commits, last touched \x1b[33m2025-11-03\x1b[0m",
            "",
        ],
        pause=0.07,
    )
    events += e
    t += 0.5

    # --- query files ---
    e, t = type_cmd(t, "python3 gitmind/cli/query.py files auth_middleware")
    events += e
    t += 0.3
    e, t = output(
        t,
        [
            "Files touched by 'auth_middleware':",
            "  src/auth.py",
            "  src/middleware.py",
            "  tests/test_auth.py",
            "",
        ],
        pause=0.07,
    )
    events += e
    t += 0.5

    # --- stale scan ---
    e, t = type_cmd(t, "python3 gitmind/cli/query.py stale --days 90")
    events += e
    t += 0.3
    e, t = output(
        t,
        [
            "Features with no activity in the last 90 days:",
            "  \x1b[31mlegacy_export\x1b[0m — last touched 2025-11-03",
            "    files: ['src/export.py', 'src/csv_writer.py']",
            "",
            "\x1b[2m# safe to delete?\x1b[0m",
            "",
        ],
        pause=0.08,
    )
    events += e
    t += 0.8

    # --- closing ---
    e, t = output(
        t,
        [
            "\x1b[1;36m# gitmind — github.com/chanakyavasantha/gitmind\x1b[0m",
        ],
        pause=0.1,
    )
    events += e
    t += 1.0

    events.append((t, ""))  # hold last frame

    return cast(events)


if __name__ == "__main__":
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    content = build()
    with open(OUT, "w") as f:
        f.write(content)
    print(f"Cast written to {OUT}")
    print(
        f"Convert to GIF: agg {OUT} docs/demo.gif --font-size 13 --cols {WIDTH} --rows {HEIGHT}"
    )
