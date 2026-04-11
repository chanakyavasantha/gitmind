import json
import os
import sys
import tempfile
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "core"))

import metadata as meta_module
from metadata import load, update
from llm import _extract_json, _coerce


# --- metadata tests ---


@pytest.fixture(autouse=True)
def isolated_metadata(tmp_path, monkeypatch):
    """Redirect metadata.json writes to a temp file for each test."""
    tmp_file = str(tmp_path / "metadata.json")
    monkeypatch.setattr(meta_module, "METADATA_PATH", tmp_file)
    yield tmp_file


def test_load_returns_empty_structure_when_no_file():
    data = load()
    assert "features" in data
    assert "history" in data
    assert data["features"] == {}
    assert data["history"] == []


def test_update_adds_new_feature():
    summary = {
        "what_changed": "added login endpoint",
        "why_it_likely_changed": "auth feature needed",
        "feature_name": "auth_login",
        "is_new_feature": True,
        "impact": "users can now log in",
        "files_touched": ["src/auth.py"],
    }
    data = update(summary, commit_hash="abc1234")
    assert "auth_login" in data["features"]
    assert data["features"]["auth_login"]["commit_count"] == 1
    assert "src/auth.py" in data["features"]["auth_login"]["files_touched"]


def test_update_increments_commit_count_on_repeat():
    summary = {
        "what_changed": "tweak",
        "why_it_likely_changed": "reason",
        "feature_name": "auth_login",
        "is_new_feature": False,
        "impact": "minor",
        "files_touched": ["src/auth.py"],
    }
    update(summary, commit_hash="aaa")
    data = update(summary, commit_hash="bbb")
    assert data["features"]["auth_login"]["commit_count"] == 2


def test_update_appends_history():
    summary = {
        "what_changed": "x",
        "why_it_likely_changed": "y",
        "feature_name": "feat_a",
        "is_new_feature": True,
        "impact": "z",
        "files_touched": [],
    }
    update(summary, commit_hash="hash1")
    update(summary, commit_hash="hash2")
    data = load()
    assert len(data["history"]) == 2
    assert data["history"][0]["commit_hash"] == "hash1"


def test_update_deduplicates_files_touched():
    summary = {
        "what_changed": "x",
        "why_it_likely_changed": "y",
        "feature_name": "feat_b",
        "is_new_feature": False,
        "impact": "z",
        "files_touched": ["a.py"],
    }
    update(summary, commit_hash="h1")
    data = update(summary, commit_hash="h2")
    assert data["features"]["feat_b"]["files_touched"].count("a.py") == 1


# --- llm parsing tests ---


def test_extract_json_plain():
    raw = '{"key": "value"}'
    assert json.loads(_extract_json(raw)) == {"key": "value"}


def test_extract_json_strips_markdown_fences():
    raw = '```json\n{"key": "value"}\n```'
    assert json.loads(_extract_json(raw)) == {"key": "value"}


def test_extract_json_ignores_leading_text():
    raw = 'Here is the result:\n{"key": "value"}'
    assert json.loads(_extract_json(raw)) == {"key": "value"}


def test_coerce_converts_list_to_string_for_what_changed():
    parsed = {
        "what_changed": [".gitignore", ".env"],
        "why_it_likely_changed": "reason",
        "feature_name": "test_feat",
        "is_new_feature": False,
        "impact": "minor",
        "files_touched": [],
    }
    result = _coerce(parsed, ["a.py"])
    assert isinstance(result["what_changed"], str)


def test_coerce_sanitizes_feature_name():
    parsed = {
        "what_changed": "x",
        "why_it_likely_changed": "y",
        "feature_name": "My Feature Name!!",
        "is_new_feature": False,
        "impact": "z",
        "files_touched": [],
    }
    result = _coerce(parsed, [])
    assert " " not in result["feature_name"]
    assert "!" not in result["feature_name"]


def test_coerce_truncates_long_feature_name():
    parsed = {
        "what_changed": "x",
        "why_it_likely_changed": "y",
        "feature_name": "a" * 100,
        "is_new_feature": False,
        "impact": "z",
        "files_touched": [],
    }
    result = _coerce(parsed, [])
    assert len(result["feature_name"]) <= 40


def test_coerce_fills_files_touched_from_fallback():
    parsed = {
        "what_changed": "x",
        "why_it_likely_changed": "y",
        "feature_name": "feat",
        "is_new_feature": False,
        "impact": "z",
        "files_touched": [],
    }
    result = _coerce(parsed, ["fallback.py"])
    assert "fallback.py" in result["files_touched"]
