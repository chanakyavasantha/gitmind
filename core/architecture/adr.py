"""ADR generation helpers for newly introduced features."""

import os
import re
from datetime import datetime
from typing import Optional

from .llm_client import llm_json


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
- alternatives_considered must have at least 2 realistic alternatives
- consequences must be concrete, not generic
- title must start with a verb
- Return ONLY the JSON object"""


def _next_adr_number(decisions_dir: str) -> int:
    if not os.path.isdir(decisions_dir):
        return 1
    existing = [name for name in os.listdir(decisions_dir) if re.match(r"^\d{3}-", name)]
    if not existing:
        return 1
    return max(int(name[:3]) for name in existing) + 1


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
    """Generate an ADR for a new-feature commit."""
    decisions_dir = os.path.join(repo_root, "docs", "decisions")
    prompt = _ADR_PROMPT.format(
        feature_name=summary.get("feature_name", "unknown"),
        what_changed=summary.get("what_changed", ""),
        why=summary.get("why_it_likely_changed", ""),
        files=", ".join(summary.get("files_touched", [])[:6]) or "(none)",
        commit_message=commit_message,
    )

    try:
        data = llm_json(prompt, timeout=90)
    except Exception as exc:
        print(f"[gitmind] ADR skipped — {exc}")
        return None

    title = data.get("title", "").strip()
    decision = data.get("decision", "").strip()
    if not title or not decision:
        return None

    os.makedirs(decisions_dir, exist_ok=True)
    number = _next_adr_number(decisions_dir)
    filepath = os.path.join(decisions_dir, f"{number:03d}-{_slugify(title)}.md")

    lines = [
        f"# ADR-{number:03d}: {title}",
        "",
        f"**Date:** {datetime.now().strftime('%Y-%m-%d')}",
        f"**Commit:** `{commit_hash[:7]}`",
        "**Status:** Accepted",
        f"**Feature:** `{summary.get('feature_name', 'unknown')}`",
        "",
        "## Context",
        "",
        data.get("context", "").strip(),
        "",
        "## Decision",
        "",
        decision,
        "",
    ]

    alternatives = data.get("alternatives_considered", [])
    if alternatives:
        lines += ["## Alternatives Considered", ""]
        for alternative in alternatives:
            option = alternative.get("option", "")
            reason = alternative.get("reason_rejected", "")
            if option:
                lines.append(f"**{option}**")
                if reason:
                    lines.append(f"> Rejected: {reason}")
                lines.append("")

    consequences = data.get("consequences", {})
    positive = consequences.get("positive", [])
    negative = consequences.get("negative", [])
    risks = consequences.get("risks", [])
    if positive or negative or risks:
        lines += ["## Consequences", ""]
        if positive:
            lines.append("**Gains:**")
            for item in positive:
                lines.append(f"- {item}")
            lines.append("")
        if negative:
            lines.append("**Trade-offs:**")
            for item in negative:
                lines.append(f"- {item}")
            lines.append("")
        if risks:
            lines.append("**Risks to watch:**")
            for item in risks:
                lines.append(f"- {item}")
            lines.append("")

    with open(filepath, "w") as f:
        f.write("\n".join(lines))
    return filepath
