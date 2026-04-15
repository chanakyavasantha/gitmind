# Module Contracts

*Auto-generated from source code + LLM analysis. Signatures are extracted by AST — factual, not guessed.*
*Last updated: 2026-04-14 07:35*

---

## `cli/dashboard.py`

**Purpose:** This module serves a web UI for a local dashboard, which can be customized with various options such as port, staleness threshold, and whether to auto-open in a browser.

*Last analyzed: 2026-04-14 07:35*

**Guarantees:**
- The web server will respond to GET requests for specific endpoints (e.g., /api/data, /dashboard.html) with the appropriate data or HTML content.
- The server will handle metadata.json located at the root of the git repository by default, but can be customized via arguments.

### Functions

#### `def find_metadata() -> Path`

Locates the metadata.json file in the git repository.

| | |
|---|---|
| **Inputs** | None |
| **Returns** | A Path object pointing to the metadata.json file. If not found, returns a Path object pointing to the current working directory with the filename 'metadata.json'. |
| **Failure modes** | No explicit failure modes mentioned; however, if no git repository is found, it will default to the current working directory. |

#### `def make_handler(metadata_path: Path, stale_days: int)`

Creates a request handler class for serving data and HTML content over HTTP.

| | |
|---|---|
| **Inputs** | metadata_path (Path): The path to the metadata.json file. stale_days (int): The default staleness threshold in days. |
| **Returns** | A Handler class with methods to serve data and files over HTTP. |
| **Failure modes** | Raises an exception if the handler cannot find the specified metadata file. |

#### `def main()`

Sets up and runs the web server with command-line arguments for customization.

| | |
|---|---|
| **Inputs** | None |
| **Returns** | Does not return anything; starts an HTTP server that can be accessed via a web browser. |
| **Failure modes** | Raises exceptions if the server cannot bind to the specified port or if it fails to find the metadata file. |

#### `class Handler(BaseHTTPRequestHandler)`

A custom HTTP request handler for serving data and HTML content over HTTP.

| | |
|---|---|
| **Inputs** | None |
| **Returns** | Handles GET requests and sends appropriate responses based on the requested path. |
| **Failure modes** | Raises exceptions if it cannot find specified files or if there is an error in processing requests. |

#### `def log_message(format, *args)`

Suppresses per-request logging to reduce noise.

| | |
|---|---|
| **Inputs** | format (str): The format string for the log message. args: Variable-length argument list for the format string. |
| **Returns** | None |
| **Failure modes** | None; does not raise exceptions or return values. |

#### `def do_GET()`

Handles GET requests and serves appropriate data or files based on the requested path.

| | |
|---|---|
| **Inputs** | None; called by the HTTP server framework when a GET request is received. |
| **Returns** | Sends an HTTP response with the appropriate content type and data. |
| **Failure modes** | Raises exceptions if it cannot find specified files or if there is an error in processing requests. |

---

## `cli/query.py`

**Purpose:** The module provides a CLI interface for querying tracked features, their associated files, commit history, and stale features.

*Last analyzed: 2026-04-14 05:11*

**Guarantees:**
- The module provides a command-line interface to interact with feature tracking data.

### Functions

#### `def cmd_features()`

Lists all tracked features along with their status, commit count, and last touched date.

| | |
|---|---|
| **Inputs** | None |
| **Returns** | Prints feature information to the console. Returns nothing. |
| **Failure modes** | No failure modes are explicitly handled in the code; it will print an error message if no data is available. |

#### `def cmd_files(feature_name)`

Shows files touched by a specified feature.

| | |
|---|---|
| **Inputs** | {'feature_name': 'str, the name of the feature to query'} |
| **Returns** | Prints file names associated with the feature. Returns nothing. |
| **Failure modes** | If the feature is not found, it prints an error message and returns. |

#### `def cmd_history()`

Shows commit history with summaries for each entry.

| | |
|---|---|
| **Inputs** | None |
| **Returns** | Prints commit history entries. Returns nothing. |
| **Failure modes** | No failure modes are explicitly handled in the code; it will print an error message if no data is available. |

#### `def cmd_stale(days=90)`

Shows features with no recent activity based on a specified number of days.

| | |
|---|---|
| **Inputs** | {'days': 'int, the number of days to consider for inactivity (default is 90)'} |
| **Returns** | Prints stale feature names and their last touched date. Returns nothing. |
| **Failure modes** | No failure modes are explicitly handled in the code; it will print an error message if no data is available. |

---

## `core/diff_reader.py`

**Purpose:** This module provides utility functions for interacting with Git repositories, specifically for retrieving the latest diff, changed files, commit message, and commit hash.

*Last analyzed: 2026-04-13 22:05*

**Guarantees:**
- All functions will execute successfully without raising exceptions if given valid input.
- The returned data is consistent with the state of the Git repository at the time of execution.

### Functions

#### `def get_latest_diff() -> str`

Returns the diff between the current commit and its parent.

| | |
|---|---|
| **Inputs** | None |
| **Returns** | The latest diff as a string. Returns an empty string if there is no previous commit to compare with. |
| **Failure modes** | Raises an exception if the `git show` command fails. |

#### `def get_changed_files() -> list[str]`

Returns a list of files that have changed between the current commit and its parent, excluding noise files.

| | |
|---|---|
| **Inputs** | None |
| **Returns** | A list of file paths as strings. Returns an empty list if there are no changed files or if all changed files are considered noise. |
| **Failure modes** | Raises an exception if the `git diff` command fails. |

#### `def get_commit_message() -> str`

Returns the commit message of the latest commit.

| | |
|---|---|
| **Inputs** | None |
| **Returns** | The commit message as a string. Returns an empty string if there is no commit history. |
| **Failure modes** | Raises an exception if the `git log` command fails. |

#### `def get_commit_hash() -> str`

Returns the hash of the latest commit.

| | |
|---|---|
| **Inputs** | None |
| **Returns** | The commit hash as a string. Returns an empty string if there is no commit history. |
| **Failure modes** | Raises an exception if the `git rev-parse` command fails. |

---

## `core/doc_generator.py`

**Purpose:** The module generates FAANG-style living documentation from the codebase and commit metadata.

*Last analyzed: 2026-04-14 02:57*

**Guarantees:**
- Accurate extraction of function and class signatures from source code using AST parsing.
- Continuous updates to documentation files based on source code changes.

### Functions

#### `def generate_architecture_doc(repo_root: str) -> str`

Rebuilds the 'docs/architecture.md' file from the current source code.

| | |
|---|---|
| **Inputs** | {'repo_root': 'The root directory of the repository as a string.'} |
| **Returns** | {'return': "A string representing the content of 'docs/architecture.md'."} |
| **Failure modes** | {'exceptions': 'Raises exceptions if there are issues reading or parsing source files.'} |

#### `def update_contracts(changed_files: list[str], repo_root: str) -> Optional[str]`

Updates the 'docs/contracts.md' file with real contracts for changed source files.

| | |
|---|---|
| **Inputs** | {'changed_files': 'A list of strings representing paths to changed source files.', 'repo_root': 'The root directory of the repository as a string.'} |
| **Returns** | {'return': 'None if successful, otherwise an error message as a string.'} |
| **Failure modes** | {'exceptions': 'Raises exceptions if there are issues reading or parsing source files.'} |

#### `def generate_adr(summary: dict, commit_hash: str, commit_message: str, repo_root: str) -> Optional[str]`

Generates an ADR for a new feature commit and saves it to 'docs/decisions/NNN.md'.

| | |
|---|---|
| **Inputs** | {'summary': 'A dictionary containing summary information about the commit.', 'commit_hash': 'The hash of the commit as a string.', 'commit_message': 'The message of the commit as a string.', 'repo_root': 'The root directory of the repository as a string.'} |
| **Returns** | {'return': 'None if successful, otherwise an error message as a string.'} |
| **Failure modes** | {'exceptions': 'Raises exceptions if there are issues creating or writing to the ADR file.'} |

---

## `core/llm.py`

**Purpose:** This module provides functionality for analyzing git commit diffs and interacting with a language model to generate insights about changes.

*Last analyzed: 2026-04-13 22:45*

**Guarantees:**
- The `analyze_diff` function will always return a dictionary containing analysis of the commit diff.

### Functions

#### `def analyze_diff(diff: str, commit_message: str, changed_files: list) -> dict`

Analyzes the provided git commit diff and returns a dictionary with insights from a language model.

| | |
|---|---|
| **Inputs** | {'diff': 'A string representing the git commit diff (str).', 'commit_message': 'A string representing the commit message (str).', 'changed_files': 'A list of strings representing the files that were changed in the commit (list[str]).'} |
| **Returns** | Returns a dictionary containing insights about the changes made in the commit. The dictionary will always contain the keys 'what_changed', 'why_it_likely_changed', 'feature_name', 'is_new_feature', 'impact', and 'files_touched'. |
| **Failure modes** | The function may raise an exception if it fails to process the input or communicate with the language model. |

---

## `core/metadata.py`

**Purpose:** This module manages metadata about features and their history in a repository.

*Last analyzed: 2026-04-14 01:11*

**Guarantees:**
- The module ensures that metadata is stored persistently and can be loaded and updated safely.

### Functions

#### `def load() -> dict`

Loads the current metadata from a file.

| | |
|---|---|
| **Inputs** | None |
| **Returns** | Returns the metadata as a dictionary. If the metadata file does not exist, returns an empty dictionary with 'features' and 'history' keys. |
| **Failure modes** | Does not fail; always returns a dictionary even if the file does not exist. |

#### `def save(data: dict)`

Saves the provided metadata to a file.

| | |
|---|---|
| **Inputs** | A dictionary containing metadata to be saved. |
| **Returns** | None. Raises an exception if the data cannot be written to the file. |
| **Failure modes** | Raises `OSError` if there is an issue writing to the file. |
| **Constraints** | The input dictionary must be serializable to JSON. |

#### `def update(summary: dict, commit_hash: str = '') -> dict`

Updates the metadata with new feature information and appends a history entry.

| | |
|---|---|
| **Inputs** | A dictionary containing summary information about a feature and an optional commit hash. |
| **Returns** | Returns the updated metadata as a dictionary. Raises exceptions if there are issues saving the data. |
| **Failure modes** | Raises `OSError` if there is an issue writing to the file, or `ValueError` if the input data is invalid. |
| **Constraints** | The 'summary' dictionary must contain a valid 'feature_name' key. |

---

<!-- CONTRACTS_DATA: {"core/diff_reader.py": {"module_purpose": "This module provides utility functions for interacting with Git repositories, specifically for retrieving the latest diff, changed files, commit message, and commit hash.", "guarantees": ["All functions will execute successfully without raising exceptions if given valid input.", "The returned data is consistent with the state of the Git repository at the time of execution."], "contracts": [{"name": "get_latest_diff", "signature": "def get_latest_diff() -> str", "what_it_does": "Returns the diff between the current commit and its parent.", "inputs": "None", "outputs": "The latest diff as a string. Returns an empty string if there is no previous commit to compare with.", "failure_modes": "Raises an exception if the `git show` command fails.", "constraints": "None"}, {"name": "get_changed_files", "signature": "def get_changed_files() -> list[str]", "what_it_does": "Returns a list of files that have changed between the current commit and its parent, excluding noise files.", "inputs": "None", "outputs": "A list of file paths as strings. Returns an empty list if there are no changed files or if all changed files are considered noise.", "failure_modes": "Raises an exception if the `git diff` command fails.", "constraints": "None"}, {"name": "get_commit_message", "signature": "def get_commit_message() -> str", "what_it_does": "Returns the commit message of the latest commit.", "inputs": "None", "outputs": "The commit message as a string. Returns an empty string if there is no commit history.", "failure_modes": "Raises an exception if the `git log` command fails.", "constraints": "None"}, {"name": "get_commit_hash", "signature": "def get_commit_hash() -> str", "what_it_does": "Returns the hash of the latest commit.", "inputs": "None", "outputs": "The commit hash as a string. Returns an empty string if there is no commit history.", "failure_modes": "Raises an exception if the `git rev-parse` command fails.", "constraints": "None"}], "updated": "2026-04-13 22:05"}, "core/llm.py": {"module_purpose": "This module provides functionality for analyzing git commit diffs and interacting with a language model to generate insights about changes.", "guarantees": ["The `analyze_diff` function will always return a dictionary containing analysis of the commit diff."], "contracts": [{"name": "analyze_diff", "signature": "def analyze_diff(diff: str, commit_message: str, changed_files: list) -> dict", "what_it_does": "Analyzes the provided git commit diff and returns a dictionary with insights from a language model.", "inputs": {"diff": "A string representing the git commit diff (str).", "commit_message": "A string representing the commit message (str).", "changed_files": "A list of strings representing the files that were changed in the commit (list[str])."}, "outputs": "Returns a dictionary containing insights about the changes made in the commit. The dictionary will always contain the keys 'what_changed', 'why_it_likely_changed', 'feature_name', 'is_new_feature', 'impact', and 'files_touched'.", "failure_modes": "The function may raise an exception if it fails to process the input or communicate with the language model.", "constraints": "None"}], "updated": "2026-04-13 22:45"}, "core/metadata.py": {"module_purpose": "This module manages metadata about features and their history in a repository.", "guarantees": ["The module ensures that metadata is stored persistently and can be loaded and updated safely."], "contracts": [{"name": "load", "signature": "def load() -> dict", "what_it_does": "Loads the current metadata from a file.", "inputs": "None", "outputs": "Returns the metadata as a dictionary. If the metadata file does not exist, returns an empty dictionary with 'features' and 'history' keys.", "failure_modes": "Does not fail; always returns a dictionary even if the file does not exist.", "constraints": "None"}, {"name": "save", "signature": "def save(data: dict)", "what_it_does": "Saves the provided metadata to a file.", "inputs": "A dictionary containing metadata to be saved.", "outputs": "None. Raises an exception if the data cannot be written to the file.", "failure_modes": "Raises `OSError` if there is an issue writing to the file.", "constraints": "The input dictionary must be serializable to JSON."}, {"name": "update", "signature": "def update(summary: dict, commit_hash: str = '') -> dict", "what_it_does": "Updates the metadata with new feature information and appends a history entry.", "inputs": "A dictionary containing summary information about a feature and an optional commit hash.", "outputs": "Returns the updated metadata as a dictionary. Raises exceptions if there are issues saving the data.", "failure_modes": "Raises `OSError` if there is an issue writing to the file, or `ValueError` if the input data is invalid.", "constraints": "The 'summary' dictionary must contain a valid 'feature_name' key."}], "updated": "2026-04-14 01:11"}, "core/doc_generator.py": {"module_purpose": "The module generates FAANG-style living documentation from the codebase and commit metadata.", "guarantees": ["Accurate extraction of function and class signatures from source code using AST parsing.", "Continuous updates to documentation files based on source code changes."], "contracts": [{"name": "generate_architecture_doc", "signature": "def generate_architecture_doc(repo_root: str) -> str", "what_it_does": "Rebuilds the 'docs/architecture.md' file from the current source code.", "inputs": {"repo_root": "The root directory of the repository as a string."}, "outputs": {"return": "A string representing the content of 'docs/architecture.md'."}, "failure_modes": {"exceptions": "Raises exceptions if there are issues reading or parsing source files."}, "constraints": "None"}, {"name": "update_contracts", "signature": "def update_contracts(changed_files: list[str], repo_root: str) -> Optional[str]", "what_it_does": "Updates the 'docs/contracts.md' file with real contracts for changed source files.", "inputs": {"changed_files": "A list of strings representing paths to changed source files.", "repo_root": "The root directory of the repository as a string."}, "outputs": {"return": "None if successful, otherwise an error message as a string."}, "failure_modes": {"exceptions": "Raises exceptions if there are issues reading or parsing source files."}, "constraints": "None"}, {"name": "generate_adr", "signature": "def generate_adr(summary: dict, commit_hash: str, commit_message: str, repo_root: str) -> Optional[str]", "what_it_does": "Generates an ADR for a new feature commit and saves it to 'docs/decisions/NNN.md'.", "inputs": {"summary": "A dictionary containing summary information about the commit.", "commit_hash": "The hash of the commit as a string.", "commit_message": "The message of the commit as a string.", "repo_root": "The root directory of the repository as a string."}, "outputs": {"return": "None if successful, otherwise an error message as a string."}, "failure_modes": {"exceptions": "Raises exceptions if there are issues creating or writing to the ADR file."}, "constraints": "None"}], "updated": "2026-04-14 02:57"}, "cli/query.py": {"module_purpose": "The module provides a CLI interface for querying tracked features, their associated files, commit history, and stale features.", "guarantees": ["The module provides a command-line interface to interact with feature tracking data."], "contracts": [{"name": "cmd_features", "signature": "def cmd_features()", "what_it_does": "Lists all tracked features along with their status, commit count, and last touched date.", "inputs": "None", "outputs": "Prints feature information to the console. Returns nothing.", "failure_modes": "No failure modes are explicitly handled in the code; it will print an error message if no data is available.", "constraints": "None"}, {"name": "cmd_files", "signature": "def cmd_files(feature_name)", "what_it_does": "Shows files touched by a specified feature.", "inputs": {"feature_name": "str, the name of the feature to query"}, "outputs": "Prints file names associated with the feature. Returns nothing.", "failure_modes": "If the feature is not found, it prints an error message and returns.", "constraints": "None"}, {"name": "cmd_history", "signature": "def cmd_history()", "what_it_does": "Shows commit history with summaries for each entry.", "inputs": "None", "outputs": "Prints commit history entries. Returns nothing.", "failure_modes": "No failure modes are explicitly handled in the code; it will print an error message if no data is available.", "constraints": "None"}, {"name": "cmd_stale", "signature": "def cmd_stale(days=90)", "what_it_does": "Shows features with no recent activity based on a specified number of days.", "inputs": {"days": "int, the number of days to consider for inactivity (default is 90)"}, "outputs": "Prints stale feature names and their last touched date. Returns nothing.", "failure_modes": "No failure modes are explicitly handled in the code; it will print an error message if no data is available.", "constraints": "None"}], "updated": "2026-04-14 05:11"}, "cli/dashboard.py": {"module_purpose": "This module serves a web UI for a local dashboard, which can be customized with various options such as port, staleness threshold, and whether to auto-open in a browser.", "guarantees": ["The web server will respond to GET requests for specific endpoints (e.g., /api/data, /dashboard.html) with the appropriate data or HTML content.", "The server will handle metadata.json located at the root of the git repository by default, but can be customized via arguments."], "contracts": [{"name": "find_metadata", "signature": "def find_metadata() -> Path", "what_it_does": "Locates the metadata.json file in the git repository.", "inputs": "None", "outputs": "A Path object pointing to the metadata.json file. If not found, returns a Path object pointing to the current working directory with the filename 'metadata.json'.", "failure_modes": "No explicit failure modes mentioned; however, if no git repository is found, it will default to the current working directory.", "constraints": "None"}, {"name": "make_handler", "signature": "def make_handler(metadata_path: Path, stale_days: int)", "what_it_does": "Creates a request handler class for serving data and HTML content over HTTP.", "inputs": "metadata_path (Path): The path to the metadata.json file. stale_days (int): The default staleness threshold in days.", "outputs": "A Handler class with methods to serve data and files over HTTP.", "failure_modes": "Raises an exception if the handler cannot find the specified metadata file.", "constraints": "None"}, {"name": "main", "signature": "def main()", "what_it_does": "Sets up and runs the web server with command-line arguments for customization.", "inputs": "None", "outputs": "Does not return anything; starts an HTTP server that can be accessed via a web browser.", "failure_modes": "Raises exceptions if the server cannot bind to the specified port or if it fails to find the metadata file.", "constraints": "None"}, {"name": "Handler", "signature": "class Handler(BaseHTTPRequestHandler)", "what_it_does": "A custom HTTP request handler for serving data and HTML content over HTTP.", "inputs": "None", "outputs": "Handles GET requests and sends appropriate responses based on the requested path.", "failure_modes": "Raises exceptions if it cannot find specified files or if there is an error in processing requests.", "constraints": "None"}, {"name": "log_message", "signature": "def log_message(format, *args)", "what_it_does": "Suppresses per-request logging to reduce noise.", "inputs": "format (str): The format string for the log message. args: Variable-length argument list for the format string.", "outputs": "None", "failure_modes": "None; does not raise exceptions or return values.", "constraints": "None"}, {"name": "do_GET", "signature": "def do_GET()", "what_it_does": "Handles GET requests and serves appropriate data or files based on the requested path.", "inputs": "None; called by the HTTP server framework when a GET request is received.", "outputs": "Sends an HTTP response with the appropriate content type and data.", "failure_modes": "Raises exceptions if it cannot find specified files or if there is an error in processing requests.", "constraints": "None"}], "updated": "2026-04-14 07:35"}} -->
