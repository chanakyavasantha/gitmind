# Quick Start

Get gitmind running on a real project in under 5 minutes.

---

## Prerequisites

### 1. Install Ollama

=== "Mac"

    ```bash
    curl -fsSL https://ollama.ai/install.sh | sh
    ```

=== "Linux"

    ```bash
    curl -fsSL https://ollama.ai/install.sh | sh
    ```

=== "Windows"

    Download the installer from [ollama.ai](https://ollama.ai)

### 2. Pull the model

```bash
ollama serve          # start the Ollama server
ollama pull deepseek-coder
```

### 3. Python 3.9+

```bash
python3 --version
```

---

## Install gitmind

```bash
git clone https://github.com/chanakyavasantha/gitmind
cd gitmind
```

### Install into your project

```bash
# Install into any git repo
bash hooks/install.sh /path/to/your/project

# Or install into the current directory
bash hooks/install.sh .
```

This:
- Copies `gitmind/core/` into `your-project/.gitmind/core/`
- Creates a virtualenv at `your-project/.gitmind/venv/`
- Installs the `post-commit` hook into `your-project/.git/hooks/`

---

## Make a commit

```bash
cd /path/to/your/project
git add .
git commit -m "your message"
```

You'll see:

```
[gitmind] Analyzing commit...
[gitmind] Feature tracked: your_feature_name
[gitmind] One sentence summary of what changed
```

A `metadata.json` file appears in `.gitmind/metadata.json`.

---

## Query the metadata

```bash
# From your project root
python3 .gitmind/../path/to/gitmind/cli/query.py features
```

Or add the CLI to your PATH for convenience:

```bash
alias gitmind="python3 /path/to/gitmind/cli/query.py"
gitmind features
gitmind history
gitmind stale
```

---

## Verify it's working

```bash
cat .gitmind/metadata.json
```

You should see structured JSON with your feature names, files, and history.

---

!!! tip "First commit edge case"
    On the very first commit in a repo (no parent), gitmind uses `git show HEAD` instead of `git diff HEAD~1 HEAD`. This is handled automatically.
