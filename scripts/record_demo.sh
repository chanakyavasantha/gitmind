#!/bin/bash
# Run this script to record the demo GIF.
# Requirements: asciinema, agg (https://github.com/asciinema/agg)
#   brew install asciinema
#   cargo install --git https://github.com/asciinema/agg
#
# Usage:
#   bash scripts/record_demo.sh
#
# Output:
#   demo.cast  — raw asciinema recording
#   docs/demo.gif — GIF for README

set -e

DEMO_REPO="/tmp/gitmind-demo"
GITMIND_DIR="$(cd "$(dirname "$0")/.." && pwd)"

echo "Setting up demo repo..."
rm -rf "$DEMO_REPO"
mkdir -p "$DEMO_REPO"
git -C "$DEMO_REPO" init -q
git -C "$DEMO_REPO" config user.email "demo@gitmind.dev"
git -C "$DEMO_REPO" config user.name "Demo"

bash "$GITMIND_DIR/hooks/install.sh" "$DEMO_REPO" > /dev/null 2>&1

# Write a demo file
cat > "$DEMO_REPO/auth.py" << 'PYEOF'
def login(username, password):
    # TODO: add rate limiting
    if username == "admin" and password == "secret":
        return True
    return False
PYEOF

echo ""
echo "Recording demo — this will open an interactive session."
echo "Type the commands below, then exit."
echo ""
echo "  cd /tmp/gitmind-demo"
echo "  git add auth.py"
echo "  git commit -m 'add login function'"
echo "  cat metadata.json"
echo "  python3 $(pwd)/cli/query.py features"
echo "  exit"
echo ""

asciinema rec demo.cast \
  --title "gitmind — semantic version control" \
  --idle-time-limit 2

echo ""
echo "Converting to GIF..."
if command -v agg &> /dev/null; then
    agg demo.cast docs/demo.gif --font-size 14 --cols 80 --rows 24
    echo "GIF saved to docs/demo.gif"
else
    echo "agg not found. Upload demo.cast to https://asciinema.org and download as GIF."
    echo "Or install agg: cargo install --git https://github.com/asciinema/agg"
fi
