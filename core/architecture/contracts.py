"""Incremental contract generation for changed source modules."""

import json
import os
import re
from datetime import datetime
from typing import Optional

from .ast_utils import SKIP_FILES, SOURCE_DIRS, extract_signatures
from .llm_client import llm_json


_CONTRACTS_PROMPT = """You are a senior engineer writing precise API contracts for internal documentation.

You are given the ACTUAL source code of a module (not a diff — the full current file).
Extract exact contracts based on what the code actually does.

Module: {filepath}

Source code:
```python
{source_code}
```

Public functions/classes identified by AST:
{signatures}

Generate contracts in JSON:
{{
  "module_purpose": "One sentence: what is the single responsibility of this module?",
  "guarantees": ["List of behavioral guarantees — what callers can always rely on"],
  "contracts": [
    {{
      "name": "function_or_class_name",
      "signature": "exact signature as written in code",
      "what_it_does": "One sentence: its specific job",
      "inputs": "What parameters it accepts and their expected types/values",
      "outputs": "What it returns and when",
      "failure_modes": "When and how it fails — exceptions raised, empty returns, etc.",
      "constraints": "Preconditions or invariants the caller must respect (or 'None')"
    }}
  ]
}}

Rules:
- Base ALL answers on the actual source code shown — do not guess
- Only document PUBLIC functions (no leading underscore)
- Limit to the 6 most important functions if there are many
- Return ONLY the JSON object"""


def update_contracts(changed_files: list[str], repo_root: str) -> Optional[str]:
    """Update docs/contracts.md for changed source files."""
    source_files = []
    for rel_path in changed_files:
        if rel_path.startswith(".gitmind/") or not rel_path.endswith(".py"):
            continue
        if os.path.basename(rel_path) in SKIP_FILES:
            continue
        if not any(rel_path.startswith(directory + "/") for directory in SOURCE_DIRS):
            continue
        abs_path = os.path.join(repo_root, rel_path)
        if os.path.isfile(abs_path):
            source_files.append(rel_path)

    if not source_files:
        return None

    contracts_path = os.path.join(repo_root, "docs", "contracts.md")
    existing = _parse_contracts_cache(contracts_path) if os.path.exists(contracts_path) else {}

    for rel_path in source_files:
        abs_path = os.path.join(repo_root, rel_path)
        try:
            with open(abs_path) as f:
                source_code = f.read()
        except OSError:
            continue

        signatures = extract_signatures(abs_path)
        public_sigs = [item for item in signatures if not item["name"].startswith("_")]
        if not public_sigs:
            continue

        signature_lines = "\n".join(
            f"  - {item.get('signature', 'class ' + item['name'])}"
            + (
                f" — {item['docstring'].splitlines()[0]}"
                if item.get("docstring")
                else ""
            )
            for item in public_sigs[:8]
        )

        source_snippet = source_code[:3000]
        if len(source_code) > 3000:
            source_snippet += "\n... (truncated)"

        prompt = _CONTRACTS_PROMPT.format(
            filepath=rel_path,
            source_code=source_snippet,
            signatures=signature_lines,
        )

        try:
            data = llm_json(prompt, timeout=90)
        except Exception as exc:
            print(f"[gitmind] Contracts skipped for {rel_path} — {exc}")
            continue

        existing[rel_path] = {
            "module_purpose": data.get("module_purpose", ""),
            "guarantees": data.get("guarantees", []),
            "contracts": data.get("contracts", []),
            "updated": datetime.now().strftime("%Y-%m-%d %H:%M"),
        }

    if not existing:
        return None

    _write_contracts_file(contracts_path, existing)
    return contracts_path


def _parse_contracts_cache(path: str) -> dict:
    with open(path) as f:
        content = f.read()
    match = re.search(r"<!-- CONTRACTS_DATA:\s*(\{.*?\})\s*-->", content, re.DOTALL)
    if not match:
        return {}
    try:
        return json.loads(match.group(1))
    except json.JSONDecodeError:
        return {}


def _write_contracts_file(path: str, data: dict):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        "# Module Contracts",
        "",
        (
            "*Auto-generated from source code + LLM analysis. Signatures are "
            "extracted by AST — factual, not guessed.*"
        ),
        f"*Last updated: {now}*",
        "",
        "---",
        "",
    ]

    for filepath, info in sorted(data.items()):
        if not isinstance(info, dict):
            continue

        lines.append(f"## `{filepath}`")
        lines.append("")
        if info.get("module_purpose"):
            lines.append(f"**Purpose:** {info['module_purpose']}")
            lines.append("")
        if info.get("updated"):
            lines.append(f"*Last analyzed: {info['updated']}*")
            lines.append("")
        if info.get("guarantees"):
            lines.append("**Guarantees:**")
            for guarantee in info["guarantees"]:
                lines.append(f"- {guarantee}")
            lines.append("")

        if info.get("contracts"):
            lines.append("### Functions")
            lines.append("")
            for contract in info["contracts"]:
                signature = contract.get("signature", contract.get("name", ""))
                lines.append(f"#### `{signature}`")
                lines.append("")
                if contract.get("what_it_does"):
                    lines.append(contract["what_it_does"])
                    lines.append("")

                rows = []
                if contract.get("inputs"):
                    rows.append(("Inputs", contract["inputs"]))
                if contract.get("outputs"):
                    rows.append(("Returns", contract["outputs"]))
                if contract.get("failure_modes"):
                    rows.append(("Failure modes", contract["failure_modes"]))
                constraints = contract.get("constraints", "")
                if constraints and constraints.lower() not in ("none", "n/a", ""):
                    rows.append(("Constraints", constraints))

                if rows:
                    lines.append("| | |")
                    lines.append("|---|---|")
                    for label, value in rows:
                        lines.append(f"| **{label}** | {value} |")
                    lines.append("")

        lines.append("---")
        lines.append("")

    lines.append(f"<!-- CONTRACTS_DATA: {json.dumps(data)} -->")
    lines.append("")
    with open(path, "w") as f:
        f.write("\n".join(lines))
