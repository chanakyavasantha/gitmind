import sys
import os

# Allow running from the hooks directory
sys.path.insert(0, os.path.dirname(__file__))

from diff_reader import (
    get_latest_diff,
    get_changed_files,
    get_commit_message,
    get_commit_hash,
)
from llm import analyze_diff
from metadata import update, _repo_root
from doc_generator import (
    generate_adr,
    generate_architecture_doc,
    generate_findings_doc,
    update_contracts,
)
from system_model import update_system_model


def run():
    diff = get_latest_diff()
    if not diff.strip():
        print("[gitmind] No diff found — skipping metadata update.")
        return

    commit_message = get_commit_message()
    commit_hash = get_commit_hash()
    changed_files = get_changed_files()
    repo_root = _repo_root()

    print("[gitmind] Analyzing commit...")

    try:
        summary = analyze_diff(
            diff, commit_message=commit_message, changed_files=changed_files
        )
    except RuntimeError as e:
        print(f"[gitmind] Skipped — {e}")
        return

    update(summary, commit_hash=commit_hash)

    feature = summary.get("feature_name", "unknown")
    print(f"[gitmind] Feature tracked: {feature}")
    print(f"[gitmind] {summary.get('what_changed', '')}")

    # ADR — only for new features (these represent architectural decisions)
    if summary.get("is_new_feature"):
        print("[gitmind] New feature — generating ADR...")
        adr_path = generate_adr(summary, commit_hash, commit_message, repo_root)
        if adr_path:
            print(f"[gitmind] ADR: {os.path.relpath(adr_path, repo_root)}")

    # Module contracts — updated for any changed source files
    contracts_path = update_contracts(changed_files, repo_root)
    if contracts_path:
        print("[gitmind] Contracts updated.")

    source_changes = [f for f in changed_files if f.endswith(".py") and f.startswith(("core/", "cli/"))]
    if source_changes:
        print("[gitmind] Updating architecture model...")
        try:
            arch_update = update_system_model(
                changed_files=changed_files,
                repo_root=repo_root,
                commit_hash=commit_hash,
            )
            changed_modules = arch_update.get("changed_modules", [])
            if changed_modules:
                print(
                    f"[gitmind] Architecture model updated for {len(changed_modules)} module(s)."
                )
            arch_path = generate_architecture_doc(repo_root)
            findings_path = generate_findings_doc(repo_root)
            print(f"[gitmind] Architecture: {os.path.relpath(arch_path, repo_root)}")
            print(f"[gitmind] Findings: {os.path.relpath(findings_path, repo_root)}")
        except RuntimeError as e:
            print(f"[gitmind] Architecture doc skipped — {e}")


if __name__ == "__main__":
    run()
