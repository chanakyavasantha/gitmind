import subprocess


def _is_first_commit() -> bool:
    result = subprocess.run(
        ["git", "rev-parse", "HEAD~1"], capture_output=True, text=True
    )
    return result.returncode != 0


def get_latest_diff() -> str:
    if _is_first_commit():
        result = subprocess.run(["git", "show", "HEAD"], capture_output=True, text=True)
    else:
        result = subprocess.run(
            ["git", "diff", "HEAD~1", "HEAD"], capture_output=True, text=True
        )
    return result.stdout


def get_changed_files() -> list[str]:
    if _is_first_commit():
        result = subprocess.run(
            ["git", "diff-tree", "--no-commit-id", "-r", "--name-only", "HEAD"],
            capture_output=True,
            text=True,
        )
    else:
        result = subprocess.run(
            ["git", "diff", "--name-only", "HEAD~1", "HEAD"],
            capture_output=True,
            text=True,
        )
    raw = result.stdout.strip()
    if not raw:
        return []
    return [f for f in raw.split("\n") if f.strip()]


def get_commit_message() -> str:
    result = subprocess.run(
        ["git", "log", "-1", "--pretty=%B"], capture_output=True, text=True
    )
    return result.stdout.strip()


def get_commit_hash() -> str:
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"], capture_output=True, text=True
    )
    return result.stdout.strip()
