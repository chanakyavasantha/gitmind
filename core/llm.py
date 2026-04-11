import requests
import json
import re

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "deepseek-coder"

PROMPT_TEMPLATE = """You are a code analysis tool. Analyze the git diff below and respond with ONLY a JSON object.

Rules:
- Return ONLY the JSON object, nothing else
- No markdown, no backticks, no explanation
- All string fields must use double quotes
- "what_changed" must be a plain string sentence, NOT an array
- "feature_name" must be snake_case, no spaces

JSON structure to return:
{{
    "what_changed": "one sentence string describing what changed",
    "why_it_likely_changed": "one sentence string on the likely reason",
    "feature_name": "snake_case_name",
    "is_new_feature": true,
    "impact": "one sentence string on the impact",
    "files_touched": ["file1.py", "file2.py"]
}}

Commit message: {commit_message}

Diff (truncated to 4000 chars):
{diff}
"""


def _extract_json(text: str) -> str:
    """Extract the first JSON object found in text, stripping markdown fences."""
    # Remove markdown code fences
    text = re.sub(r"```(?:json)?\s*", "", text).strip()
    text = text.replace("```", "").strip()

    # Find the first { ... } block
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
    """Fix common LLM mistakes — wrong types on known fields."""
    for field in ("what_changed", "why_it_likely_changed", "impact", "feature_name"):
        val = parsed.get(field)
        if isinstance(val, list):
            parsed[field] = ", ".join(str(v) for v in val)
        elif not isinstance(val, str):
            parsed[field] = str(val) if val is not None else ""

    if not isinstance(parsed.get("files_touched"), list):
        parsed["files_touched"] = changed_files or []
    elif not parsed["files_touched"] and changed_files:
        parsed["files_touched"] = changed_files

    if not isinstance(parsed.get("is_new_feature"), bool):
        parsed["is_new_feature"] = False

    # Sanitize and truncate feature_name
    name = parsed.get("feature_name", "unknown")
    name = re.sub(r"[^a-z0-9_]", "_", name.lower().strip())
    name = re.sub(r"_+", "_", name).strip("_")  # collapse multiple underscores
    if len(name) > 40:
        name = name[:40].rsplit("_", 1)[0]  # truncate at word boundary
    parsed["feature_name"] = name or "unknown"

    return parsed


def analyze_diff(
    diff: str, commit_message: str = "", changed_files: list = None
) -> dict:
    prompt = PROMPT_TEMPLATE.format(
        commit_message=commit_message or "not provided", diff=diff[:4000]
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
    except json.JSONDecodeError as e:
        raise RuntimeError(f"LLM returned invalid JSON: {e}\nRaw output: {raw}")
