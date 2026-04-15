"""Compatibility wrapper for architecture documentation generation."""

from architecture.adr import generate_adr
from architecture.contracts import update_contracts
from architecture.docs import generate_architecture_doc, generate_findings_doc

__all__ = [
    "generate_adr",
    "generate_architecture_doc",
    "generate_findings_doc",
    "update_contracts",
]
