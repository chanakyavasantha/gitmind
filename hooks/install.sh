#!/bin/bash

# gitmind install script
# Installs the post-commit hook into a target git repo

set -e

GITMIND_SOURCE="$(cd "$(dirname "$0")/.." && pwd)"
TARGET_REPO="${1:-$(pwd)}"

if [ ! -d "$TARGET_REPO/.git" ]; then
    echo "Error: $TARGET_REPO is not a git repository."
    exit 1
fi

GITMIND_DIR="$TARGET_REPO/.gitmind"

echo "Installing gitmind into $TARGET_REPO..."

# Copy gitmind core into the target repo's .gitmind directory
mkdir -p "$GITMIND_DIR/core"
cp "$GITMIND_SOURCE/core/"*.py "$GITMIND_DIR/core/"

# Set up virtualenv in the target repo
if [ ! -d "$GITMIND_DIR/venv" ]; then
    echo "Creating virtualenv..."
    python3 -m venv "$GITMIND_DIR/venv"
fi

echo "Installing dependencies..."
"$GITMIND_DIR/venv/bin/pip" install --quiet requests

# Install the hook
HOOK_PATH="$TARGET_REPO/.git/hooks/post-commit"
cat > "$HOOK_PATH" << 'EOF'
#!/bin/bash
if [ -n "$GITMIND_RUNNING" ]; then exit 0; fi
export GITMIND_RUNNING=1
GITMIND_DIR="$(git rev-parse --show-toplevel)/.gitmind"
if [ ! -d "$GITMIND_DIR" ]; then exit 0; fi
VENV="$GITMIND_DIR/venv"
ENGINE="$GITMIND_DIR/core/engine.py"
if [ -f "$VENV/bin/python" ]; then
    "$VENV/bin/python" "$ENGINE"
else
    python3 "$ENGINE"
fi
REPO_ROOT="$(git rev-parse --show-toplevel)"
if [ -f "$REPO_ROOT/metadata.json" ]; then
    git add "$REPO_ROOT/metadata.json"
    git commit --amend --no-edit --no-verify --quiet
fi
EOF

chmod +x "$HOOK_PATH"

echo "Done. gitmind is now active in $TARGET_REPO"
echo "Make sure Ollama is running: ollama serve"
echo "Make sure the model is pulled: ollama pull deepseek-coder"
