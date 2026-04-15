"""AST-backed helpers used by documentation and architecture rendering."""

import ast
import os


SOURCE_DIRS = ("core", "cli")
SOURCE_EXT = ".py"
SKIP_FILES = ("__init__.py",)


def extract_signatures(filepath: str) -> list[dict]:
    """Extract public function and class signatures from a Python module."""
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
            continue

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
            continue

        args = []
        for arg in node.args.args:
            if arg.arg == "self":
                continue
            annotation = ""
            if arg.annotation:
                try:
                    annotation = ast.unparse(arg.annotation)
                except Exception:
                    annotation = ""
            args.append(f"{arg.arg}: {annotation}" if annotation else arg.arg)

        return_annotation = ""
        if node.returns:
            try:
                return_annotation = ast.unparse(node.returns)
            except Exception:
                return_annotation = ""

        signature = f"def {name}({', '.join(args)})"
        if return_annotation:
            signature += f" -> {return_annotation}"

        results.append(
            {
                "type": "function",
                "name": name,
                "signature": signature,
                "docstring": docstring,
                "lineno": node.lineno,
            }
        )
    return results


def scan_source_files(repo_root: str) -> list[str]:
    """Return source .py files in tracked source directories."""
    result = []
    for directory in SOURCE_DIRS:
        dirpath = os.path.join(repo_root, directory)
        if not os.path.isdir(dirpath):
            continue
        for root, _, names in os.walk(dirpath):
            for filename in sorted(names):
                if not filename.endswith(SOURCE_EXT) or filename in SKIP_FILES:
                    continue
                result.append(
                    os.path.relpath(os.path.join(root, filename), repo_root).replace(
                        "\\", "/"
                    )
                )
    return sorted(result)
