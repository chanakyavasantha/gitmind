"""Small Ollama client for architecture-oriented generation tasks."""

import json
import re

import requests


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5-coder:7b"


def llm_json(prompt: str, timeout: int = 90) -> dict:
    """Call Ollama and parse the first JSON object in the response."""
    response = requests.post(
        OLLAMA_URL,
        json={"model": MODEL, "prompt": prompt, "stream": False, "format": "json"},
        timeout=timeout,
    )
    response.raise_for_status()
    raw = response.json()["response"]

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
