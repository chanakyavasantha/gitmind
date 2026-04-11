import json
import os
from datetime import datetime


def _repo_root() -> str:
    import subprocess

    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True
    )
    return result.stdout.strip() if result.returncode == 0 else os.getcwd()


METADATA_PATH = os.path.join(_repo_root(), "metadata.json")


def load() -> dict:
    if os.path.exists(METADATA_PATH):
        with open(METADATA_PATH) as f:
            return json.load(f)
    return {"features": {}, "history": []}


def save(data: dict):
    with open(METADATA_PATH, "w") as f:
        json.dump(data, f, indent=2)


def update(summary: dict, commit_hash: str = "") -> dict:
    data = load()
    now = datetime.now().isoformat()
    feature = summary.get("feature_name", "unknown")

    if feature not in data["features"]:
        data["features"][feature] = {
            "introduced": now,
            "files_touched": [],
            "still_active": True,
            "last_built_upon": now,
            "is_new_feature": summary.get("is_new_feature", False),
            "commit_count": 0,
        }

    entry = data["features"][feature]

    for f in summary.get("files_touched", []):
        if f and f not in entry["files_touched"]:
            entry["files_touched"].append(f)

    entry["last_built_upon"] = now
    entry["still_active"] = True
    entry["commit_count"] = entry.get("commit_count", 0) + 1

    data["history"].append({"commit_hash": commit_hash, "timestamp": now, **summary})

    save(data)
    return data
