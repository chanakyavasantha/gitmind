# Quality Findings

*Auto-generated from the incremental system model. Do not edit manually.*
*Last updated: 2026-04-15 18:02*

---

## Summary

- Modules analyzed: 14
- High severity: 2
- Medium severity: 3
- Low severity: 6
- Strengths captured: 1

---

## Findings

### core/architecture/model.py has no direct test coverage

- Severity: `high`
- Category: `testing`
- Module: `core/architecture/model.py`
- Summary: This module orchestrates core behavior but no matching test file was found under tests/.

### core/engine.py has no direct test coverage

- Severity: `high`
- Category: `testing`
- Module: `core/engine.py`
- Summary: This module orchestrates core behavior but no matching test file was found under tests/.

### core/architecture/ast_utils.py is a central dependency

- Severity: `medium`
- Category: `coupling`
- Module: `core/architecture/ast_utils.py`
- Summary: 3 modules depend on core/architecture/ast_utils.py; changes here are likely to have broad blast radius.

### core/architecture/docs.py is growing large

- Severity: `medium`
- Category: `maintainability`
- Module: `core/architecture/docs.py`
- Summary: core/architecture/docs.py has 231 lines; consider splitting parsing, rendering, and integration responsibilities.

### core/architecture/model.py is growing large

- Severity: `medium`
- Category: `maintainability`
- Module: `core/architecture/model.py`
- Summary: core/architecture/model.py has 554 lines; consider splitting parsing, rendering, and integration responsibilities.

### Dashboard uses a basic single-process HTTP server

- Severity: `low`
- Category: `operability`
- Module: `cli/dashboard.py`
- Summary: This is fine for local use, but richer dashboards may want a structured API layer if interactions grow.

### LLM integration is nicely isolated

- Severity: `low`
- Category: `architecture`
- Module: `core/llm.py`
- Summary: Keeping Ollama calls in one module lowers coupling; preserve that boundary as the architecture tooling expands.

### core/diff_reader.py is missing a module docstring

- Severity: `low`
- Category: `documentation`
- Module: `core/diff_reader.py`
- Summary: Adding a top-level docstring would improve generated documentation quality and intent capture.

### core/engine.py is missing a module docstring

- Severity: `low`
- Category: `documentation`
- Module: `core/engine.py`
- Summary: Adding a top-level docstring would improve generated documentation quality and intent capture.

### core/llm.py is missing a module docstring

- Severity: `low`
- Category: `documentation`
- Module: `core/llm.py`
- Summary: Adding a top-level docstring would improve generated documentation quality and intent capture.

### core/metadata.py is missing a module docstring

- Severity: `low`
- Category: `documentation`
- Module: `core/metadata.py`
- Summary: Adding a top-level docstring would improve generated documentation quality and intent capture.
