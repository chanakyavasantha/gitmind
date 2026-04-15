"""
Generates FAANG-style living documentation from the codebase + commit metadata.

Produces three continuously-updated documents:
  docs/architecture.md   — Mermaid component diagram + data flow + module roles
  docs/contracts.md      — Real function signatures (via AST) + LLM-written guarantees
  docs/decisions/NNN.md  — ADR with alternatives considered (only for new features)

Key principle: code is parsed with `ast` for accuracy; LLM is used only to explain
intent and trade-offs — never to guess at signatures or behavior.
"""

import ast
import json
import os
import re
import subprocess
from datetime import datetime
from typing import Optional

import requests
from system_model import load_findings, load_system_model

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5-coder:7b"

# Which directories contain source code worth documenting
SOURCE_DIRS = ("core", "cli")
SOURCE_EXT = ".py"
SKIP_FILES = ("__init__.py",)

# ── AST helpers ──────────────────────────────────────────────────────────────


def _extract_signatures(filepath: str) -> list[dict]:
    """
    Parse a Python file and extract all public function/class signatures.
    Returns list of {type, name, args, docstring, lineno}.
    """
    try:
        with open(filepath) as f:
            source = f.read()
        tree = ast.parse(source, filename=filepath)
    except (SyntaxError, OSError):
        return []

    results = []
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            continue
        name = node.name
        if name.startswith("__") and name.endswith("__") and name != "__init__":
            continue  # skip dunder except __init__

        docstring = ast.get_docstring(node) or ""

        if isinstance(node, ast.ClassDef):
            results.append(
                {
                    "type": "class",
                    "name": name,
                    "args": None,
                    "docstring": docstring,
                    "lineno": node.lineno,
                }
            )
        else:
            args = []
            for arg in node.args.args:
                if arg.arg == "self":
                    continue
                annotation = ""
                if arg.annotation:
                    try:
                        annotation = ast.unparse(arg.annotation)
                    except Exception:
                        pass
                args.append(f"{arg.arg}: {annotation}" if annotation else arg.arg)

            return_annotation = ""
            if node.returns:
                try:
                    return_annotation = ast.unparse(node.returns)
                except Exception:
                    pass

            sig = f"def {name}({', '.join(args)})"
            if return_annotation:
                sig += f" -> {return_annotation}"

            results.append(
                {
                    "type": "function",
                    "name": name,
                    "signature": sig,
                    "docstring": docstring,
                    "lineno": node.lineno,
                }
            )
    return results


def _extract_imports(filepath: str) -> list[str]:
    """Return list of local module names imported by this file."""
    try:
        with open(filepath) as f:
            source = f.read()
        tree = ast.parse(source, filename=filepath)
    except (SyntaxError, OSError):
        return []

    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom):
            if node.module and not node.module.startswith("."):
                imports.append(node.module)
        elif isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)
    return imports


def _scan_source_files(repo_root: str) -> list[str]:
    """Return all source .py files in SOURCE_DIRS, relative to repo_root."""
    result = []
    for d in SOURCE_DIRS:
        dirpath = os.path.join(repo_root, d)
        if not os.path.isdir(dirpath):
            continue
        for fname in sorted(os.listdir(dirpath)):
            if fname.endswith(SOURCE_EXT) and fname not in SKIP_FILES:
                result.append(os.path.join(d, fname))
    return result


# ── LLM helpers ──────────────────────────────────────────────────────────────


def _llm(prompt: str, timeout: int = 90) -> dict:
    """Call Ollama and parse JSON response. Raises RuntimeError on failure."""
    resp = requests.post(
        OLLAMA_URL,
        json={"model": MODEL, "prompt": prompt, "stream": False, "format": "json"},
        timeout=timeout,
    )
    resp.raise_for_status()
    raw = resp.json()["response"]

    raw = re.sub(r"```(?:json)?\s*", "", raw).strip().replace("```", "")
    start = raw.find("{")
    if start == -1:
        raise RuntimeError("No JSON in LLM response")
    depth = 0
    for i, ch in enumerate(raw[start:], start):
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return json.loads(raw[start : i + 1])
    raise RuntimeError("Unterminated JSON in LLM response")


# ── Architecture doc ─────────────────────────────────────────────────────────

_ARCH_PROMPT = """You are a software architect documenting this Python codebase.

Codebase structure:
{module_list}

Import relationships (module → what it imports from the project):
{import_graph}

Public functions per module:
{function_map}

Generate documentation in JSON:
{{
  "overview": "2-3 sentence description of what this system does and its core design principle",
  "data_flow": "Step-by-step description of the main data flow (e.g. 'git commit → hook → diff_reader → llm → metadata')",
  "components": {{
    "module/path.py": {{
      "role": "One sentence: what this module's responsibility is",
      "depends_on": ["other_module.py"]
    }}
  }},
  "mermaid_diagram": "A valid Mermaid flowchart (graph TD) showing components and data flow. Use short node labels. No quotes inside the diagram string."
}}

Rules:
- Only include modules from the provided list
- The mermaid_diagram must be valid Mermaid syntax (graph TD)
- Keep node labels short (2-4 words max)
- Return ONLY the JSON object"""


def generate_architecture_doc(repo_root: str) -> str:
    """
    Rebuild docs/architecture.md from the persisted system model.
    Falls back to source scanning only if the model is not available yet.
    Returns the file path written.
    """
    model = load_system_model(repo_root)
    modules = model.get("modules", {})
    if not modules:
        source_files = _scan_source_files(repo_root)
        modules = {}
        for rel_path in source_files:
            abs_path = os.path.join(repo_root, rel_path)
            sigs = _extract_signatures(abs_path)
            public = [s for s in sigs if not s["name"].startswith("_")]
            modules[rel_path] = {
                "path": rel_path,
                "role": "module",
                "dependencies": [],
                "dependents": [],
                "public_functions": [
                    {
                        "name": s["name"],
                        "signature": s.get("signature", s["name"]),
                        "docstring": s.get("docstring", ""),
                    }
                    for s in public
                    if s["type"] == "function"
                ],
                "public_classes": [
                    {"name": s["name"], "docstring": s.get("docstring", "")}
                    for s in public
                    if s["type"] == "class"
                ],
                "line_count": 0,
                "external_imports": [],
                "docstring": "",
            }

    findings = load_findings(repo_root)
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    stats = model.get("stats", {})
    overview = (
        "gitmind maintains a commit-aware architecture model for the repository, "
        "then renders professional documentation and findings from that model. "
        "The system keeps fact extraction deterministic and uses generated prose "
        "only as a presentation layer."
    )
    data_flow = (
        "git commit -> hook -> engine -> diff reader -> semantic metadata -> "
        "incremental system model -> contracts/docs/findings -> dashboard"
    )

    mermaid = ["graph TD"]
    for path, info in sorted(modules.items()):
        node_id = path.replace("/", "_").replace(".", "_")
        label = os.path.basename(path).replace(".py", "")
        mermaid.append(f'    {node_id}["{label}"]')
        for dep in info.get("dependencies", []):
            dep_id = dep.replace("/", "_").replace(".", "_")
            mermaid.append(f"    {node_id} --> {dep_id}")

    output_path = os.path.join(repo_root, "docs", "architecture.md")

    lines = [
        "# Architecture",
        "",
        "*Auto-generated from the incremental system model. Do not edit manually.*",
        f"*Last updated: {now}*",
        "",
        "---",
        "",
        "## Overview",
        "",
        overview,
        "",
        "## Data Flow",
        "",
        data_flow,
        "",
        "## Current Snapshot",
        "",
        f"- Modules tracked: {stats.get('module_count', len(modules))}",
        f"- Public API symbols: {stats.get('public_api_count', 0)}",
        f"- Dependency edges: {stats.get('dependency_edges', 0)}",
        f"- Entry points: {stats.get('entrypoint_count', 0)}",
        f"- Findings: {findings.get('summary', {}).get('finding_count', 0)} risks, {findings.get('summary', {}).get('strength_count', 0)} strengths",
        "",
        "---",
        "",
        "## Component Diagram",
        "",
        "```mermaid",
        "\n".join(mermaid),
        "```",
        "",
        "---",
        "",
        "## Components",
        "",
    ]

    for module_path, info in sorted(modules.items()):
        role = info.get("role", "")
        depends = info.get("dependencies", [])
        dependents = info.get("dependents", [])
        lines.append(f"### `{module_path}`")
        lines.append("")
        if role:
            lines.append(f"**Role:** `{role}`")
            lines.append("")
        if info.get("docstring"):
            lines.append(info["docstring"].splitlines()[0])
            lines.append("")
        lines.append(
            f"- Lines: {info.get('line_count', 0)}"
        )
        lines.append(
            f"- Public API symbols: {len(info.get('public_functions', [])) + len(info.get('public_classes', []))}"
        )
        if depends:
            lines.append(f"- Depends on: {', '.join(f'`{d}`' for d in depends)}")
        if dependents:
            lines.append(f"- Used by: {', '.join(f'`{d}`' for d in dependents)}")
        if info.get("external_imports"):
            lines.append(
                f"- External imports: {', '.join(f'`{d}`' for d in info['external_imports'][:6])}"
            )
        lines.append("")

    # Component contracts (function signatures) from AST — factual, not LLM-guessed
    lines += [
        "---",
        "",
        "## Function Reference",
        "",
        "_Extracted directly from the current architecture model._",
        "",
    ]

    for rel_path, info in sorted(modules.items()):
        public = [
            {
                "type": "function",
                "name": item["name"],
                "signature": item.get("signature", item["name"]),
                "docstring": item.get("docstring", ""),
            }
            for item in info.get("public_functions", [])
        ] + [
            {
                "type": "class",
                "name": item["name"],
                "docstring": item.get("docstring", ""),
            }
            for item in info.get("public_classes", [])
        ]
        if not public:
            continue
        lines.append(f"### `{rel_path}`")
        lines.append("")
        for item in public:
            if item["type"] == "class":
                lines.append(f"- **class** `{item['name']}`")
            else:
                lines.append(f"- `{item.get('signature', item['name'])}`")
            if item.get("docstring"):
                lines.append(f"  > {item['docstring'].splitlines()[0]}")
        lines.append("")

    with open(output_path, "w") as f:
        f.write("\n".join(lines))

    return output_path


def generate_findings_doc(repo_root: str) -> str:
    findings = load_findings(repo_root)
    output_path = os.path.join(repo_root, "docs", "quality-findings.md")
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    summary = findings.get("summary", {})

    lines = [
        "# Quality Findings",
        "",
        "*Auto-generated from the incremental system model. Do not edit manually.*",
        f"*Last updated: {now}*",
        "",
        "---",
        "",
        "## Summary",
        "",
        f"- Modules analyzed: {summary.get('module_count', 0)}",
        f"- High severity: {summary.get('high_severity', 0)}",
        f"- Medium severity: {summary.get('medium_severity', 0)}",
        f"- Low severity: {summary.get('low_severity', 0)}",
        f"- Strengths captured: {summary.get('strength_count', 0)}",
        "",
        "---",
        "",
        "## Findings",
        "",
    ]

    for finding in findings.get("findings", []):
        lines.append(f"### {finding.get('title', 'Untitled finding')}")
        lines.append("")
        lines.append(f"- Severity: `{finding.get('severity', 'unknown')}`")
        lines.append(f"- Category: `{finding.get('category', 'general')}`")
        if finding.get("module"):
            lines.append(f"- Module: `{finding['module']}`")
        lines.append(f"- Summary: {finding.get('summary', '')}")
        lines.append("")

    with open(output_path, "w") as f:
        f.write("\n".join(lines))

    return output_path


# ── Module contracts ─────────────────────────────────────────────────────────

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
    """
    Update docs/contracts.md with real contracts for changed source files.
    Uses AST for signatures and actual source for LLM context.
    Returns path written or None if nothing to update.
    """
    # Filter to documentable source files that actually exist
    source_files = []
    for f in changed_files:
        if f.startswith(".gitmind/"):
            continue
        if not f.endswith(".py"):
            continue
        if os.path.basename(f) in SKIP_FILES:
            continue
        # Only core/ and cli/ files
        if not any(f.startswith(d + "/") for d in SOURCE_DIRS):
            continue
        abs_path = os.path.join(repo_root, f)
        if os.path.isfile(abs_path):
            source_files.append(f)

    if not source_files:
        return None

    contracts_path = os.path.join(repo_root, "docs", "contracts.md")

    # Load existing data cache
    existing: dict = {}
    if os.path.exists(contracts_path):
        existing = _parse_contracts_cache(contracts_path)

    # Generate contracts for each changed file from ACTUAL source
    for rel_path in source_files:
        abs_path = os.path.join(repo_root, rel_path)
        try:
            with open(abs_path) as f:
                source_code = f.read()
        except OSError:
            continue

        sigs = _extract_signatures(abs_path)
        public_sigs = [s for s in sigs if not s["name"].startswith("_")]
        if not public_sigs:
            continue

        sig_lines = "\n".join(
            f"  - {s.get('signature', 'class ' + s['name'])}"
            + (f" — {s['docstring'].splitlines()[0]}" if s.get("docstring") else "")
            for s in public_sigs[:8]
        )

        # Trim source to avoid overwhelming the model
        source_snippet = source_code[:3000]
        if len(source_code) > 3000:
            source_snippet += "\n... (truncated)"

        prompt = _CONTRACTS_PROMPT.format(
            filepath=rel_path,
            source_code=source_snippet,
            signatures=sig_lines,
        )

        try:
            data = _llm(prompt, timeout=90)
            existing[rel_path] = {
                "module_purpose": data.get("module_purpose", ""),
                "guarantees": data.get("guarantees", []),
                "contracts": data.get("contracts", []),
                "updated": datetime.now().strftime("%Y-%m-%d %H:%M"),
            }
        except Exception as e:
            print(f"[gitmind] Contracts skipped for {rel_path} — {e}")
            continue

    if not existing:
        return None

    _write_contracts_file(contracts_path, existing)
    return contracts_path


def _parse_contracts_cache(path: str) -> dict:
    with open(path) as f:
        content = f.read()
    match = re.search(r"<!-- CONTRACTS_DATA:\s*(\{.*?\})\s*-->", content, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError:
            pass
    return {}


def _write_contracts_file(path: str, data: dict):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    lines = [
        "# Module Contracts",
        "",
        "*Auto-generated from source code + LLM analysis. Signatures are extracted by AST — factual, not guessed.*",
        f"*Last updated: {now}*",
        "",
        "---",
        "",
    ]

    for filepath, info in sorted(data.items()):
        if not isinstance(info, dict):
            continue

        purpose = info.get("module_purpose", "")
        guarantees = info.get("guarantees", [])
        contracts = info.get("contracts", [])
        updated = info.get("updated", "")

        lines.append(f"## `{filepath}`")
        lines.append("")
        if purpose:
            lines.append(f"**Purpose:** {purpose}")
            lines.append("")
        if updated:
            lines.append(f"*Last analyzed: {updated}*")
            lines.append("")
        if guarantees:
            lines.append("**Guarantees:**")
            for g in guarantees:
                lines.append(f"- {g}")
            lines.append("")

        if contracts:
            lines.append("### Functions")
            lines.append("")
            for c in contracts:
                name = c.get("name", "")
                sig = c.get("signature", name)
                what = c.get("what_it_does", "")
                inputs = c.get("inputs", "")
                outputs = c.get("outputs", "")
                failure = c.get("failure_modes", "")
                constraints = c.get("constraints", "")

                lines.append(f"#### `{sig}`")
                lines.append("")
                if what:
                    lines.append(what)
                    lines.append("")

                table_rows = []
                if inputs:
                    table_rows.append(("Inputs", inputs))
                if outputs:
                    table_rows.append(("Returns", outputs))
                if failure:
                    table_rows.append(("Failure modes", failure))
                if constraints and constraints.lower() not in ("none", "n/a", ""):
                    table_rows.append(("Constraints", constraints))

                if table_rows:
                    lines.append("| | |")
                    lines.append("|---|---|")
                    for label, val in table_rows:
                        lines.append(f"| **{label}** | {val} |")
                    lines.append("")

        lines.append("---")
        lines.append("")

    # Embedded JSON cache for incremental updates
    lines.append(f"<!-- CONTRACTS_DATA: {json.dumps(data)} -->")
    lines.append("")

    with open(path, "w") as f:
        f.write("\n".join(lines))


# ── ADR generation ───────────────────────────────────────────────────────────

_ADR_PROMPT = """You are a software architect writing an Architecture Decision Record (ADR).

ADRs capture not just WHAT was decided, but WHY — including alternatives that were rejected.

Commit context:
- Feature: {feature_name}
- What changed: {what_changed}
- Why it changed: {why}
- Files: {files}
- Commit message: {commit_message}

Generate an ADR in JSON:
{{
  "title": "Verb + Subject (4-7 words, e.g. 'Use Ollama For Local LLM Inference')",
  "context": "What was the problem or situation that required a decision? What constraints existed? (2-4 sentences)",
  "decision": "What was decided? Be specific about the technical choice made. (2-3 sentences)",
  "alternatives_considered": [
    {{
      "option": "Name of the alternative",
      "reason_rejected": "Why it was not chosen (1-2 sentences)"
    }}
  ],
  "consequences": {{
    "positive": ["What we gain from this decision"],
    "negative": ["What we give up or accept as a trade-off"],
    "risks": ["Potential future problems to watch for"]
  }}
}}

Rules:
- alternatives_considered must have at least 2 realistic alternatives (infer from context if not explicit)
- consequences must be concrete, not generic
- title must start with a verb (Use, Add, Replace, Adopt, Implement, etc.)
- Return ONLY the JSON object"""


def _next_adr_number(decisions_dir: str) -> int:
    if not os.path.isdir(decisions_dir):
        return 1
    existing = [f for f in os.listdir(decisions_dir) if re.match(r"^\d{3}-", f)]
    if not existing:
        return 1
    return max(int(f[:3]) for f in existing) + 1


def _slugify(title: str) -> str:
    slug = title.lower().strip()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"\s+", "-", slug)
    return re.sub(r"-+", "-", slug).strip("-")[:60]


def generate_adr(
    summary: dict,
    commit_hash: str,
    commit_message: str,
    repo_root: str,
) -> Optional[str]:
    """
    Generate an ADR for a new feature commit.
    Returns path written, or None if skipped.
    """
    decisions_dir = os.path.join(repo_root, "docs", "decisions")

    prompt = _ADR_PROMPT.format(
        feature_name=summary.get("feature_name", "unknown"),
        what_changed=summary.get("what_changed", ""),
        why=summary.get("why_it_likely_changed", ""),
        files=", ".join(summary.get("files_touched", [])[:6]) or "(none)",
        commit_message=commit_message,
    )

    try:
        data = _llm(prompt, timeout=90)
    except Exception as e:
        print(f"[gitmind] ADR skipped — {e}")
        return None

    title = data.get("title", "").strip()
    context = data.get("context", "").strip()
    decision = data.get("decision", "").strip()
    alternatives = data.get("alternatives_considered", [])
    consequences = data.get("consequences", {})

    if not title or not decision:
        return None

    os.makedirs(decisions_dir, exist_ok=True)
    num = _next_adr_number(decisions_dir)
    filename = f"{num:03d}-{_slugify(title)}.md"
    filepath = os.path.join(decisions_dir, filename)

    today = datetime.now().strftime("%Y-%m-%d")
    short_hash = commit_hash[:7]
    feature = summary.get("feature_name", "unknown")

    lines = [
        f"# ADR-{num:03d}: {title}",
        "",
        f"**Date:** {today}",
        f"**Commit:** `{short_hash}`",
        f"**Status:** Accepted",
        f"**Feature:** `{feature}`",
        "",
        "## Context",
        "",
        context,
        "",
        "## Decision",
        "",
        decision,
        "",
    ]

    if alternatives:
        lines += ["## Alternatives Considered", ""]
        for alt in alternatives:
            option = alt.get("option", "")
            reason = alt.get("reason_rejected", "")
            if option:
                lines.append(f"**{option}**")
                if reason:
                    lines.append(f"> Rejected: {reason}")
                lines.append("")

    pos = consequences.get("positive", [])
    neg = consequences.get("negative", [])
    risks = consequences.get("risks", [])

    if pos or neg or risks:
        lines += ["## Consequences", ""]
        if pos:
            lines.append("**Gains:**")
            for p in pos:
                lines.append(f"- {p}")
            lines.append("")
        if neg:
            lines.append("**Trade-offs:**")
            for n in neg:
                lines.append(f"- {n}")
            lines.append("")
        if risks:
            lines.append("**Risks to watch:**")
            for r in risks:
                lines.append(f"- {r}")
            lines.append("")

    with open(filepath, "w") as f:
        f.write("\n".join(lines))

    return filepath
