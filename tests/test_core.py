import json
import os
import sys
import tempfile
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "core"))

import metadata as meta_module
from metadata import load, update
from llm import _extract_json, _coerce
from system_model import update_system_model, load_system_model, load_findings


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


def test_coerce_filters_hallucinated_action_paths():
    parsed = {
        "what_changed": "x",
        "why_it_likely_changed": "y",
        "feature_name": "feat",
        "is_new_feature": False,
        "impact": "z",
        "files_touched": [
            "core/llm.py",
            "actions/checkout@v4",
            "uses: actions/setup-python@v5",
        ],
    }
    result = _coerce(parsed, ["core/llm.py"])
    assert "actions/checkout@v4" not in result["files_touched"]
    assert "core/llm.py" in result["files_touched"]


def test_coerce_enforces_max_four_word_feature_name():
    parsed = {
        "what_changed": "x",
        "why_it_likely_changed": "y",
        "feature_name": "one_two_three_four_five_six",
        "is_new_feature": False,
        "impact": "z",
        "files_touched": [],
    }
    result = _coerce(parsed, [])
    parts = result["feature_name"].split("_")
    assert len(parts) <= 4


def test_build_diff_section_uses_file_list_for_large_diffs():
    from llm import _build_diff_section

    large_diff = "x" * 4000
    section = _build_diff_section(large_diff, ["a.py", "b.py"])
    assert "a.py" in section
    assert "large" in section.lower()


def test_build_diff_section_uses_full_diff_for_small_diffs():
    from llm import _build_diff_section

    small_diff = "small diff content"
    section = _build_diff_section(small_diff, ["a.py"])
    assert "small diff content" in section


# --- system model tests ---


def test_update_system_model_creates_incremental_model(tmp_path):
    (tmp_path / "core").mkdir()
    (tmp_path / "cli").mkdir()
    (tmp_path / "metadata").mkdir()
    (tmp_path / "tests").mkdir()

    (tmp_path / "core" / "alpha.py").write_text(
        '"""Alpha module."""\n'
        "from core.beta import helper\n\n"
        "def run():\n"
        "    return helper()\n"
    )
    (tmp_path / "core" / "beta.py").write_text(
        '"""Beta module."""\n\n'
        "def helper():\n"
        "    return 'ok'\n"
    )

    result = update_system_model(
        changed_files=["core/alpha.py", "core/beta.py"],
        repo_root=str(tmp_path),
        commit_hash="abc123",
    )

    model = result["model"]
    assert model["last_commit_hash"] == "abc123"
    assert "core/alpha.py" in model["modules"]
    assert model["modules"]["core/alpha.py"]["dependencies"] == ["core/beta.py"]


def test_update_system_model_removes_deleted_modules(tmp_path):
    (tmp_path / "core").mkdir()
    (tmp_path / "metadata").mkdir()

    file_path = tmp_path / "core" / "alpha.py"
    file_path.write_text("def run():\n    return 1\n")

    update_system_model(
        changed_files=["core/alpha.py"],
        repo_root=str(tmp_path),
        commit_hash="first",
    )
    file_path.unlink()

    result = update_system_model(
        changed_files=["core/alpha.py"],
        repo_root=str(tmp_path),
        commit_hash="second",
    )

    assert "core/alpha.py" not in result["model"]["modules"]


def test_update_system_model_generates_findings_for_critical_untested_modules(tmp_path):
    (tmp_path / "core").mkdir()
    (tmp_path / "metadata").mkdir()
    (tmp_path / "tests").mkdir()

    (tmp_path / "core" / "engine.py").write_text(
        '"""Engine."""\n\n'
        "def run():\n"
        "    return 1\n"
    )

    update_system_model(
        changed_files=["core/engine.py"],
        repo_root=str(tmp_path),
        commit_hash="abc123",
    )

    findings = load_findings(str(tmp_path))
    assert any(
        item["id"] == "untested-critical:core/engine.py"
        for item in findings["findings"]
    )


def test_load_system_model_reads_persisted_file(tmp_path):
    (tmp_path / "core").mkdir()
    (tmp_path / "metadata").mkdir()
    (tmp_path / "core" / "sample.py").write_text("def ping():\n    return 'pong'\n")

    update_system_model(
        changed_files=["core/sample.py"],
        repo_root=str(tmp_path),
        commit_hash="persist",
    )

    loaded = load_system_model(str(tmp_path))
    assert loaded["last_commit_hash"] == "persist"
    assert "core/sample.py" in loaded["modules"]
