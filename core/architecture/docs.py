"""Markdown renderers for architecture snapshots and findings."""

import os
from datetime import datetime

from .ast_utils import extract_signatures, scan_source_files
from .model import load_findings, load_system_model


GENERATED_DOCS_DIR = os.path.join("docs", "generated")


def _generated_output(repo_root: str, filename: str) -> str:
    output_dir = os.path.join(repo_root, GENERATED_DOCS_DIR)
    os.makedirs(output_dir, exist_ok=True)
    return os.path.join(output_dir, filename)


def generate_architecture_doc(repo_root: str) -> str:
    """Render docs/generated/architecture.md from the persisted system model."""
    model = load_system_model(repo_root)
    modules = model.get("modules", {})
    if not modules:
        source_files = scan_source_files(repo_root)
        modules = {}
        for rel_path in source_files:
            abs_path = os.path.join(repo_root, rel_path)
            signatures = extract_signatures(abs_path)
            public = [item for item in signatures if not item["name"].startswith("_")]
            modules[rel_path] = {
                "path": rel_path,
                "role": "module",
                "dependencies": [],
                "dependents": [],
                "public_functions": [
                    {
                        "name": item["name"],
                        "signature": item.get("signature", item["name"]),
                        "docstring": item.get("docstring", ""),
                    }
                    for item in public
                    if item["type"] == "function"
                ],
                "public_classes": [
                    {"name": item["name"], "docstring": item.get("docstring", "")}
                    for item in public
                    if item["type"] == "class"
                ],
                "line_count": 0,
                "external_imports": [],
                "docstring": "",
            }

    findings = load_findings(repo_root)
    stats = model.get("stats", {})
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    mermaid = ["graph TD"]
    for path, info in sorted(modules.items()):
        node_id = path.replace("/", "_").replace(".", "_")
        label = os.path.basename(path).replace(".py", "")
        mermaid.append(f'    {node_id}["{label}"]')
        for dep in info.get("dependencies", []):
            dep_id = dep.replace("/", "_").replace(".", "_")
            mermaid.append(f"    {node_id} --> {dep_id}")

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
        (
            "gitmind maintains a commit-aware architecture model for the repository, "
            "then renders professional documentation and findings from that model. "
            "The system keeps fact extraction deterministic and uses generated prose "
            "only as a presentation layer."
        ),
        "",
        "## Data Flow",
        "",
        (
            "git commit -> hook -> engine -> diff reader -> semantic metadata -> "
            "incremental system model -> contracts/docs/findings -> dashboard"
        ),
        "",
        "## Current Snapshot",
        "",
        f"- Modules tracked: {stats.get('module_count', len(modules))}",
        f"- Public API symbols: {stats.get('public_api_count', 0)}",
        f"- Dependency edges: {stats.get('dependency_edges', 0)}",
        f"- Entry points: {stats.get('entrypoint_count', 0)}",
        (
            f"- Findings: {findings.get('summary', {}).get('finding_count', 0)} "
            f"risks, {findings.get('summary', {}).get('strength_count', 0)} strengths"
        ),
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
        lines.append(f"### `{module_path}`")
        lines.append("")
        if info.get("role"):
            lines.append(f"**Role:** `{info['role']}`")
            lines.append("")
        if info.get("docstring"):
            lines.append(info["docstring"].splitlines()[0])
            lines.append("")
        lines.append(f"- Lines: {info.get('line_count', 0)}")
        lines.append(
            "- Public API symbols: "
            f"{len(info.get('public_functions', [])) + len(info.get('public_classes', []))}"
        )
        if info.get("dependencies"):
            lines.append(
                f"- Depends on: {', '.join(f'`{dep}`' for dep in info['dependencies'])}"
            )
        if info.get("dependents"):
            lines.append(
                f"- Used by: {', '.join(f'`{dep}`' for dep in info['dependents'])}"
            )
        if info.get("external_imports"):
            lines.append(
                "- External imports: "
                + ", ".join(f"`{dep}`" for dep in info["external_imports"][:6])
            )
        lines.append("")

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

    output_path = _generated_output(repo_root, "architecture.md")
    with open(output_path, "w") as f:
        f.write("\n".join(lines))
    return output_path


def generate_findings_doc(repo_root: str) -> str:
    """Render docs/generated/quality-findings.md from the stored findings JSON."""
    findings = load_findings(repo_root)
    summary = findings.get("summary", {})
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

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

    output_path = _generated_output(repo_root, "quality-findings.md")
    with open(output_path, "w") as f:
        f.write("\n".join(lines))
    return output_path
