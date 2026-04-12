#!/usr/bin/env python3
"""
gitmind local dashboard — serves a web UI backed by metadata.json.

Usage:
  python3 cli/dashboard.py               # opens browser at localhost:4242
  python3 cli/dashboard.py --port 8080
  python3 cli/dashboard.py --days 30     # custom staleness threshold
  python3 cli/dashboard.py --no-browser  # server only, no auto-open
"""

import argparse
import json
import os
import socketserver
import subprocess
import sys
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse

SCRIPT_DIR = Path(__file__).parent
HTML_PATH = SCRIPT_DIR / "dashboard.html"


def find_metadata() -> Path:
    """Locate metadata.json by walking up to the git root."""
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True,
        cwd=os.getcwd(),
    )
    if result.returncode == 0:
        return Path(result.stdout.strip()) / "metadata.json"
    return Path.cwd() / "metadata.json"


def make_handler(metadata_path: Path, stale_days: int):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, format, *args):
            pass  # suppress per-request noise

        def do_GET(self):
            path = urlparse(self.path).path
            if path == "/api/data":
                self._serve_data()
            elif path in ("/", "/dashboard.html"):
                self._serve_file(HTML_PATH, "text/html; charset=utf-8")
            else:
                self.send_error(404)

        def _serve_data(self):
            if not metadata_path.exists():
                self.send_error(404, "metadata.json not found")
                return
            with open(metadata_path) as f:
                data = json.load(f)
            # Inject server-side config so the frontend knows the default threshold
            data["_config"] = {"stale_days": stale_days}
            body = json.dumps(data).encode()
            self._respond(200, "application/json", body)

        def _serve_file(self, path: Path, content_type: str):
            if not path.exists():
                self.send_error(404, f"{path.name} not found")
                return
            body = path.read_bytes()
            self._respond(200, content_type, body)

        def _respond(self, code: int, content_type: str, body: bytes):
            self.send_response(code)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

    return Handler


def main():
    parser = argparse.ArgumentParser(
        description="gitmind local dashboard",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--port", type=int, default=4242, metavar="PORT")
    parser.add_argument(
        "--days",
        type=int,
        default=90,
        metavar="N",
        help="Default staleness threshold in days (default: 90)",
    )
    parser.add_argument(
        "--no-browser",
        action="store_true",
        help="Start server without opening a browser",
    )
    args = parser.parse_args()

    metadata_path = find_metadata()
    if not metadata_path.exists():
        print(f"  Error: no metadata.json found at {metadata_path}")
        print("  Install gitmind in a repo and make at least one commit first.")
        sys.exit(1)

    Handler = make_handler(metadata_path, args.days)

    with socketserver.TCPServer(("", args.port), Handler) as server:
        url = f"http://localhost:{args.port}"
        print(f"\n  ◆ gitmind dashboard")
        print(f"  → {url}")
        print(f"  → reading: {metadata_path}")
        print(f"  → staleness default: {args.days} days")
        print(f"\n  Press Ctrl+C to stop\n")

        if not args.no_browser:
            threading.Timer(0.4, lambda: webbrowser.open(url)).start()

        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\n  Stopped.")


if __name__ == "__main__":
    main()
