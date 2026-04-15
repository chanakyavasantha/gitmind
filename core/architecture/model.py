"""Incremental system model extraction plus rule-based architecture findings."""

import ast
import json
import os
from datetime import datetime

from .ast_utils import SKIP_FILES, SOURCE_DIRS, SOURCE_EXT


SYSTEM_MODEL_PATH = os.path.join("metadata", "system_model.json")
FINDINGS_PATH = os.path.join("metadata", "findings.json")
DASHBOARD_PATH = os.path.join("metadata", "dashboard.json")


def _utc_now() -> str:
    return datetime.utcnow().replace(microsecond=0).isoformat() + "Z"


def _rel_path(path: str, repo_root: str) -> str:
    path = path.replace("\\", "/")
    if os.path.isabs(path):
        path = os.path.relpath(path, repo_root)
    return path.replace("\\", "/")


def _module_name(rel_path: str) -> str:
    return rel_path.replace("/", ".").rsplit(".", 1)[0]


def _is_source_file(rel_path: str) -> bool:
    rel_path = rel_path.replace("\\", "/")
    return (
        rel_path.endswith(SOURCE_EXT)
        and os.path.basename(rel_path) not in SKIP_FILES
        and any(
        rel_path.startswith(prefix + "/") for prefix in SOURCE_DIRS
        )
    )


def _repo_output(path: str, repo_root: str) -> str:
    return os.path.join(repo_root, path)


def _load_json(path: str, default):
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return default


def _save_json(path: str, data: dict):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2, sort_keys=True)


def load_system_model(repo_root: str) -> dict:
    return _load_json(
        _repo_output(SYSTEM_MODEL_PATH, repo_root),
        {
            "repo_root": repo_root,
            "generated_at": None,
            "last_commit_hash": None,
            "modules": {},
            "stats": {},
        },
    )


def load_findings(repo_root: str) -> dict:
    return _load_json(
        _repo_output(FINDINGS_PATH, repo_root),
        {"generated_at": None, "summary": {}, "findings": []},
    )


def _list_source_files(repo_root: str) -> list[str]:
    files = []
    for source_dir in SOURCE_DIRS:
        abs_dir = os.path.join(repo_root, source_dir)
        if not os.path.isdir(abs_dir):
            continue
        for root, _, names in os.walk(abs_dir):
            for name in sorted(names):
                if not name.endswith(SOURCE_EXT):
                    continue
                if name in SKIP_FILES:
                    continue
                rel_path = os.path.relpath(os.path.join(root, name), repo_root)
                files.append(_rel_path(rel_path, repo_root))
    return sorted(files)


def _annotation(node) -> str:
    if not node:
        return ""
    try:
        return ast.unparse(node)
    except Exception:
        return ""


def _function_signature(node) -> str:
    args = []
    for arg in getattr(node.args, "posonlyargs", []):
        args.append(arg.arg)
    for arg in node.args.args:
        if arg.arg == "self":
            continue
        annotation = _annotation(arg.annotation)
        args.append(f"{arg.arg}: {annotation}" if annotation else arg.arg)
    if node.args.vararg:
        args.append(f"*{node.args.vararg.arg}")
    for arg in node.args.kwonlyargs:
        annotation = _annotation(arg.annotation)
        args.append(f"{arg.arg}: {annotation}" if annotation else arg.arg)
    if node.args.kwarg:
        args.append(f"**{node.args.kwarg.arg}")
    returns = _annotation(getattr(node, "returns", None))
    signature = f"def {node.name}({', '.join(args)})"
    if returns:
        signature += f" -> {returns}"
    return signature


def _classify_role(rel_path: str, public_functions: list[dict]) -> str:
    if rel_path.startswith("cli/"):
        if "dashboard" in rel_path:
            return "dashboard"
        return "cli"
    if rel_path.startswith("core/"):
        if rel_path in ("core/system_model.py", "core/doc_generator.py"):
            return "compatibility"
        lowered = rel_path.lower()
        if "llm" in lowered:
            return "integration"
        if "metadata" in lowered:
            return "storage"
        if "diff" in lowered:
            return "git_adapter"
        if "engine" in lowered:
            return "orchestrator"
        if "doc" in lowered:
            return "documentation"
        if "system_model" in lowered or "/model.py" in lowered:
            return "architecture_model"
    if any(item["name"] == "main" for item in public_functions):
        return "entrypoint"
    return "module"


def _extract_module(abs_path: str, rel_path: str) -> dict:
    with open(abs_path) as f:
        source = f.read()

    tree = ast.parse(source, filename=rel_path)
    module_doc = ast.get_docstring(tree) or ""
    imported_modules = []
    imported_symbols = []
    classes = []
    functions = []

    for node in tree.body:
        if isinstance(node, ast.Import):
            for alias in node.names:
                imported_modules.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imported_modules.append(node.module)
            imported_symbols.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ClassDef):
            if node.name.startswith("_"):
                continue
            classes.append(
                {
                    "name": node.name,
                    "lineno": node.lineno,
                    "docstring": ast.get_docstring(node) or "",
                    "method_count": sum(
                        isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef))
                        for child in node.body
                    ),
                }
            )
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if node.name.startswith("_"):
                continue
            functions.append(
                {
                    "name": node.name,
                    "lineno": node.lineno,
                    "signature": _function_signature(node),
                    "docstring": ast.get_docstring(node) or "",
                }
            )

    writes_to = []
    for pattern in ("metadata.json", "docs/", "metadata/", "http://localhost:11434"):
        if pattern in source:
            writes_to.append(pattern)

    return {
        "path": rel_path,
        "module": _module_name(rel_path),
        "role": _classify_role(rel_path, functions),
        "docstring": module_doc,
        "public_functions": functions,
        "public_classes": classes,
        "raw_imports": sorted(set(imported_modules)),
        "local_imports": sorted(set(imported_modules)),
        "external_imports": [],
        "imported_symbols": sorted(set(imported_symbols)),
        "line_count": len(source.splitlines()),
        "public_api_count": len(functions) + len(classes),
        "entrypoints": {
            "has_main": 'if __name__ == "__main__":' in source,
            "is_dashboard": rel_path == "cli/dashboard.py",
        },
        "writes_to": sorted(set(writes_to)),
        "last_seen": _utc_now(),
    }


def _resolve_local_dependencies(modules: dict) -> dict:
    module_name_to_path = {data["module"]: path for path, data in modules.items()}
    resolved = {}
    for path, data in modules.items():
        deps = []
        for module in data.get("local_imports", []):
            target = None
            if module in module_name_to_path:
                target = module_name_to_path[module]
            else:
                for candidate_module, candidate_path in module_name_to_path.items():
                    if candidate_module.endswith("." + module):
                        target = candidate_path
                        break
            if target and target != path:
                deps.append(target)
        resolved[path] = sorted(set(deps))
    return resolved


def _reverse_dependencies(dependencies: dict) -> dict:
    reverse = {path: [] for path in dependencies}
    for path, deps in dependencies.items():
        for dep in deps:
            reverse.setdefault(dep, []).append(path)
    for path in reverse:
        reverse[path] = sorted(set(reverse[path]))
    return reverse


def _find_cycles(dependencies: dict) -> list[list[str]]:
    cycles = []
    seen = set()

    def visit(node: str, stack: list[str], visiting: set[str]):
        visiting.add(node)
        stack.append(node)
        for dep in dependencies.get(node, []):
            if dep in visiting:
                cycle = stack[stack.index(dep) :] + [dep]
                key = tuple(cycle)
                if key not in seen:
                    seen.add(key)
                    cycles.append(cycle)
                continue
            if dep not in stack:
                visit(dep, stack[:], visiting.copy())

    for node in dependencies:
        visit(node, [], set())
    return cycles


def _has_test_for_module(rel_path: str, repo_root: str) -> bool:
    tests_dir = os.path.join(repo_root, "tests")
    if not os.path.isdir(tests_dir):
        return False
    base = os.path.basename(rel_path).replace(".py", "")
    for name in os.listdir(tests_dir):
        if name.endswith(".py") and base in name:
            return True
    return False


def _build_findings(model: dict, repo_root: str) -> dict:
    modules = model.get("modules", {})
    dependencies = {
        path: data.get("dependencies", []) for path, data in modules.items()
    }
    reverse = _reverse_dependencies(dependencies)
    findings = []

    for path, data in modules.items():
        inbound = len(reverse.get(path, []))
        outbound = len(data.get("dependencies", []))
        if data.get("role") == "compatibility":
            continue
        if data.get("line_count", 0) > 220:
            findings.append(
                {
                    "id": f"module-size:{path}",
                    "severity": "medium",
                    "category": "maintainability",
                    "title": f"{path} is growing large",
                    "summary": (
                        f"{path} has {data['line_count']} lines; consider splitting "
                        "parsing, rendering, and integration responsibilities."
                    ),
                    "module": path,
                }
            )
        if inbound >= 3:
            findings.append(
                {
                    "id": f"central-module:{path}",
                    "severity": "medium",
                    "category": "coupling",
                    "title": f"{path} is a central dependency",
                    "summary": (
                        f"{inbound} modules depend on {path}; changes here are likely "
                        "to have broad blast radius."
                    ),
                    "module": path,
                }
            )
        if not data.get("docstring"):
            findings.append(
                {
                    "id": f"missing-docstring:{path}",
                    "severity": "low",
                    "category": "documentation",
                    "title": f"{path} is missing a module docstring",
                    "summary": (
                        "Adding a top-level docstring would improve generated "
                        "documentation quality and intent capture."
                    ),
                    "module": path,
                }
            )
        if data.get("role") in ("orchestrator", "architecture_model") and not _has_test_for_module(
            path, repo_root
        ):
            findings.append(
                {
                    "id": f"untested-critical:{path}",
                    "severity": "high",
                    "category": "testing",
                    "title": f"{path} has no direct test coverage",
                    "summary": (
                        "This module orchestrates core behavior but no matching test "
                        "file was found under tests/."
                    ),
                    "module": path,
                }
            )
        if path == "core/engine.py" and data.get("writes_to"):
            findings.append(
                {
                    "id": "engine-side-effects",
                    "severity": "medium",
                    "category": "runtime",
                    "title": "Commit processing has doc-generation side effects",
                    "summary": (
                        "The engine updates metadata and generated docs during commit "
                        "processing; keep heavy analysis incremental to avoid slow hooks."
                    ),
                    "module": path,
                }
            )
        if path == "cli/dashboard.py":
            findings.append(
                {
                    "id": "dashboard-server",
                    "severity": "low",
                    "category": "operability",
                    "title": "Dashboard uses a basic single-process HTTP server",
                    "summary": (
                        "This is fine for local use, but richer dashboards may want a "
                        "structured API layer if interactions grow."
                    ),
                    "module": path,
                }
            )
        if path == "core/llm.py" and outbound == 0:
            findings.append(
                {
                    "id": "llm-boundary",
                    "severity": "low",
                    "category": "architecture",
                    "title": "LLM integration is nicely isolated",
                    "summary": (
                        "Keeping Ollama calls in one module lowers coupling; preserve "
                        "that boundary as the architecture tooling expands."
                    ),
                    "module": path,
                    "kind": "strength",
                }
            )

    for cycle in _find_cycles(dependencies):
        cycle_path = " -> ".join(cycle)
        findings.append(
            {
                "id": f"cycle:{cycle_path}",
                "severity": "high",
                "category": "coupling",
                "title": "Circular dependency detected",
                "summary": cycle_path,
                "module": cycle[0],
            }
        )

    findings.sort(
        key=lambda item: (
            {"high": 0, "medium": 1, "low": 2}.get(item.get("severity"), 3),
            item.get("title", ""),
        )
    )

    summary = {
        "module_count": len(modules),
        "finding_count": len([f for f in findings if f.get("kind") != "strength"]),
        "strength_count": len([f for f in findings if f.get("kind") == "strength"]),
        "high_severity": len([f for f in findings if f.get("severity") == "high"]),
        "medium_severity": len([f for f in findings if f.get("severity") == "medium"]),
        "low_severity": len([f for f in findings if f.get("severity") == "low"]),
    }
    return {"generated_at": _utc_now(), "summary": summary, "findings": findings}


def _build_dashboard_payload(model: dict, findings: dict) -> dict:
    modules = model.get("modules", {})
    top_coupled = sorted(
        (
            {
                "path": path,
                "dependents": len(data.get("dependents", [])),
                "dependencies": len(data.get("dependencies", [])),
                "role": data.get("role", "module"),
            }
            for path, data in modules.items()
        ),
        key=lambda item: (-item["dependents"], -item["dependencies"], item["path"]),
    )[:8]

    diagram = ["graph TD"]
    for path, data in sorted(modules.items()):
        node_id = path.replace("/", "_").replace(".", "_")
        label = os.path.basename(path).replace(".py", "")
        diagram.append(f'    {node_id}["{label}"]')
        for dep in data.get("dependencies", [])[:6]:
            target_id = dep.replace("/", "_").replace(".", "_")
            diagram.append(f"    {node_id} --> {target_id}")

    return {
        "generated_at": _utc_now(),
        "system_summary": model.get("stats", {}),
        "finding_summary": findings.get("summary", {}),
        "top_coupled_modules": top_coupled,
        "recent_findings": findings.get("findings", [])[:12],
        "component_diagram": "\n".join(diagram),
    }


def update_system_model(
    changed_files: list[str],
    repo_root: str,
    commit_hash: str = "",
) -> dict:
    model = load_system_model(repo_root)
    modules = model.get("modules", {})

    tracked_changes = {
        _rel_path(path, repo_root) for path in changed_files if _is_source_file(path)
    }
    if not modules:
        tracked_changes = set(_list_source_files(repo_root))

    for rel_path in list(modules.keys()):
        abs_path = os.path.join(repo_root, rel_path)
        if not os.path.exists(abs_path) or not _is_source_file(rel_path):
            modules.pop(rel_path, None)

    for rel_path in tracked_changes:
        abs_path = os.path.join(repo_root, rel_path)
        if not os.path.isfile(abs_path):
            modules.pop(rel_path, None)
            continue
        try:
            modules[rel_path] = _extract_module(abs_path, rel_path)
        except (OSError, SyntaxError):
            continue

    dependencies = _resolve_local_dependencies(modules)
    dependents = _reverse_dependencies(dependencies)

    for path, data in modules.items():
        data["dependencies"] = dependencies.get(path, [])
        data["dependents"] = dependents.get(path, [])
        resolved_modules = {
            modules[dep]["module"] for dep in data["dependencies"] if dep in modules
        }
        resolved_basenames = {
            modules[dep]["module"].split(".")[-1]
            for dep in data["dependencies"]
            if dep in modules
        }
        data["external_imports"] = sorted(
            {
                module
                for module in data.get("raw_imports", [])
                if module not in resolved_modules
                and module.split(".")[-1] not in resolved_basenames
            }
        )

    model["repo_root"] = repo_root
    model["generated_at"] = _utc_now()
    model["last_commit_hash"] = commit_hash or model.get("last_commit_hash")
    model["modules"] = dict(sorted(modules.items()))
    model["stats"] = {
        "module_count": len(modules),
        "public_api_count": sum(
            data.get("public_api_count", 0) for data in modules.values()
        ),
        "dependency_edges": sum(
            len(data.get("dependencies", [])) for data in modules.values()
        ),
        "entrypoint_count": sum(
            1
            for data in modules.values()
            if data.get("entrypoints", {}).get("has_main")
            or data.get("entrypoints", {}).get("is_dashboard")
        ),
    }

    findings = _build_findings(model, repo_root)
    dashboard = _build_dashboard_payload(model, findings)

    _save_json(_repo_output(SYSTEM_MODEL_PATH, repo_root), model)
    _save_json(_repo_output(FINDINGS_PATH, repo_root), findings)
    _save_json(_repo_output(DASHBOARD_PATH, repo_root), dashboard)

    return {
        "model": model,
        "findings": findings,
        "dashboard": dashboard,
        "changed_modules": sorted(tracked_changes),
    }
