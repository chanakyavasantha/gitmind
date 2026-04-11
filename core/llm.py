import requests
import json
import re

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "deepseek-coder"

PROMPT_TEMPLATE = """Analyze this git diff and return ONLY valid JSON with no explanation, no markdown, no code blocks.

Return exactly this structure:
{{
    "what_changed": "one sentence describing what changed",
    "why_it_likely_changed": "one sentence on the likely reason",
    "feature_name": "short_snake_case_name",
    "is_new_feature": true,
    "impact": "one sentence on the impact of this change",
    "files_touched": ["file1.py", "file2.py"]
}}

Commit message: {commit_message}

Diff:
{diff}
"""


def analyze_diff(diff: str, commit_message: str = "", changed_files: list = None) -> dict:
    prompt = PROMPT_TEMPLATE.format(
        commit_message=commit_message or "not provided",
        diff=diff[:4000]
    )

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )
        response.raise_for_status()
        raw = response.json()["response"]

        # Strip markdown code fences if model wraps in them
        raw = re.sub(r"```(?:json)?\s*", "", raw).strip()

        parsed = json.loads(raw)

        # Fallback: fill files_touched from git if LLM missed it
        if not parsed.get("files_touched") and changed_files:
            parsed["files_touched"] = changed_files

        return parsed

    except requests.exceptions.ConnectionError:
        raise RuntimeError("Ollama is not running. Start it with: ollama serve")
    except json.JSONDecodeError as e:
        raise RuntimeError(f"LLM returned invalid JSON: {e}\nRaw output: {raw}")
