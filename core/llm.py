import requests
import json
import re

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5-coder:7b"
LARGE_DIFF_THRESHOLD = 3000

PROMPT_TEMPLATE = """You are a code analysis tool. Analyze the git commit below and respond with ONLY a JSON object.

Rules:
- Return ONLY the JSON object, nothing else
- No markdown, no backticks, no explanation
- All string fields must use double quotes
- "what_changed" must be a single plain sentence
- "feature_name" must be 2-4 words in snake_case that name the feature, not the implementation
  Good: "auth_middleware", "rate_limiting", "user_onboarding"
  Bad: "fix_the_json_parsing_issue_in_llm_py", "update_diff_reader_getlatestdifference_method"

JSON structure to return:
{{
    "what_changed": "one sentence describing what changed",
    "why_it_likely_changed": "one sentence on the likely reason",
    "feature_name": "two_to_four_words",
    "is_new_feature": true,
    "impact": "one sentence on the impact",
    "files_touched": ["file1.py", "file2.py"]
}}

Commit message: {commit_message}

{diff_section}
"""


def _build_diff_section(diff: str, changed_files: list) -> str:
    """For large diffs, summarize by file list only to avoid overwhelming the model."""
    if len(diff) <= LARGE_DIFF_THRESHOLD:
        return f"Diff:\n{diff}"
    files_str = (
        "\n".join(f"  - {f}" for f in changed_files) if changed_files else "  (none)"
    )
    # Include a small head of the diff for context
    snippet = diff[:800]
    return (
        f"This diff is large ({len(diff)} chars). Changed files:\n{files_str}\n\n"
        f"Diff snippet (first 800 chars):\n{snippet}"
    )


def _extract_json(text: str) -> str:
    """Extract the first JSON object found in text, stripping markdown fences."""
    text = re.sub(r"```(?:json)?\s*", "", text).strip()
    text = text.replace("```", "").strip()

    start = text.find("{")
    if start == -1:
        return text
    depth = 0
    for i, ch in enumerate(text[start:], start):
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return text[start : i + 1]
    return text[start:]


def _coerce(parsed: dict, changed_files: list) -> dict:
    """Fix common LLM mistakes — wrong types, hallucinated file paths, bad feature names."""
    for field in ("what_changed", "why_it_likely_changed", "impact", "feature_name"):
        val = parsed.get(field)
        if isinstance(val, list):
            parsed[field] = ", ".join(str(v) for v in val)
        elif not isinstance(val, str):
            parsed[field] = str(val) if val is not None else ""

    # Filter files_touched: keep only entries that look like real file paths
    # (have a file extension or are known path-like), drop hallucinated tokens
    # like "actions/checkout@v4" that appear in workflow file content
    llm_files = parsed.get("files_touched")
    if not isinstance(llm_files, list) or not llm_files:
        parsed["files_touched"] = changed_files or []
    else:
        real_files = set(changed_files or [])
        parsed["files_touched"] = (
            [
                f
                for f in llm_files
                if f in real_files or (f and "@" not in f and not f.startswith("uses:"))
            ]
            or changed_files
            or []
        )

    if not isinstance(parsed.get("is_new_feature"), bool):
        parsed["is_new_feature"] = False

    # Sanitize and truncate feature_name to max 4 words / 40 chars
    name = parsed.get("feature_name", "unknown")
    name = re.sub(r"[^a-z0-9_]", "_", name.lower().strip())
    name = re.sub(r"_+", "_", name).strip("_")
    # Enforce max 4 word segments
    parts = name.split("_")
    if len(parts) > 4:
        name = "_".join(parts[:4])
    if len(name) > 40:
        name = name[:40].rsplit("_", 1)[0]
    parsed["feature_name"] = name or "unknown"

    return parsed


def analyze_diff(
    diff: str, commit_message: str = "", changed_files: list = None
) -> dict:
    diff_section = _build_diff_section(diff, changed_files or [])
    prompt = PROMPT_TEMPLATE.format(
        commit_message=commit_message or "not provided",
        diff_section=diff_section,
    )

    try:
        response = requests.post(
            OLLAMA_URL,
            json={"model": MODEL, "prompt": prompt, "stream": False, "format": "json"},
            timeout=90,
        )
        response.raise_for_status()
        raw = response.json()["response"]

        extracted = _extract_json(raw)
        parsed = json.loads(extracted)
        return _coerce(parsed, changed_files or [])

    except requests.exceptions.ConnectionError:
        raise RuntimeError("Ollama is not running. Start it with: ollama serve")
    except requests.exceptions.ReadTimeout:
        raise RuntimeError("Ollama timed out — model may be loading, try again")
    except json.JSONDecodeError as e:
        raise RuntimeError(f"LLM returned invalid JSON: {e}\nRaw output: {raw}")
