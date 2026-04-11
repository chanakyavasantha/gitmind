# Build Log

This page is generated automatically from `metadata.json` on every push — the tool is documenting itself.

Every entry below was written by gitmind analyzing its own commits via a local LLM (Ollama + deepseek-coder).
No human wrote these summaries. The feature names, file lists, and change descriptions are all LLM output.

---

## Tracked Features

| Feature | Status | Commits | Introduced | Last Active |
|---------|--------|---------|------------|-------------|
| `build_log` | ✅ active | 1 | 2026-04-10 23:17 | 2026-04-10 23:17 |
| `pin_black` | ✅ active | 1 | 2026-04-10 22:46 | 2026-04-10 22:46 |
| `pin_to_py39` | ✅ active | 1 | 2026-04-10 22:31 | 2026-04-10 22:31 |
| `post_commit_hooks` | ✅ active | 1 | 2026-04-10 22:25 | 2026-04-10 22:25 |
| `implementation_of_auth_rate` | ✅ active | 1 | 2026-04-10 22:14 | 2026-04-10 22:14 |
| `blackcicheck` | ✅ active | 1 | 2026-04-10 22:04 | 2026-04-10 22:04 |
| `repo_root_function_added` | ✅ active | 1 | 2026-04-10 21:59 | 2026-04-10 21:59 |
| `buildloggenerationfrommetadatajson` | ✅ active | 1 | 2026-04-10 21:53 | 2026-04-10 21:53 |
| `remove_auth` | ✅ active | 1 | 2026-04-10 21:48 | 2026-04-10 21:48 |
| `auth_middleware_rate_limiting` | ✅ active | 1 | 2026-04-10 21:45 | 2026-04-10 21:45 |
| `initial_gitmind_engine` | ✅ active | 1 | 2026-04-10 21:43 | 2026-04-10 21:43 |
| `docs_deployments` | ✅ active | 1 | 2026-04-10 20:22 | 2026-04-10 20:22 |
| `user_onboarding` | ✅ active | 1 | 2026-04-10 20:10 | 2026-04-10 20:10 |
| `auth_middleware_py_file` | ✅ active | 1 | 2026-04-10 20:08 | 2026-04-10 20:08 |
| `unknown` | ✅ active | 3 | 2026-04-10 20:05 | 2026-04-10 23:02 |
| `gitmind_was_renamed_as` | ✅ active | 1 | 2026-04-10 20:04 | 2026-04-10 20:04 |

---

## Files Per Feature

**`auth_middleware_py_file`**

- `.gitmind/core/llm.py`
- `core/llm.py`

**`auth_middleware_rate_limiting`**

- `.gitmind/core/engine.py`
- `.gitmind/core/llm.py`
- `core/engine.py`
- `core/llm.py`

**`blackcicheck`**

- `.github/workflows/ci.yml`

**`build_log`**

- `README.md`
- `docs/build-log.md`
- `docs/demo.cast`
- `docs/demo.gif`
- `metadata.json`
- `scripts/generate_demo_cast.py`

**`buildloggenerationfrommetadatajson`**

- `.github/workflows/docs.yml`
- `core/metadata.py`
- `docs/build-log.md`
- `metadata.json`
- `scripts/generate_build_log.py`

**`docs_deployments`**

- `.github/workflows/docs.yml`

**`implementation_of_auth_rate`**

- `hooks/install.sh`
- `hooks/post-commit`
- `metadata.json`

**`initial_gitmind_engine`**

- `docs/build-log.md`
- `mkdocs.yml`

**`pin_black`**

- `.github/workflows/ci.yml`
- `metadata.json`
- `pyproject.toml`

**`pin_to_py39`**

- `.github/workflows/ci.yml`
- `metadata.json`

**`post_commit_hooks`**

- `hooks/install.sh`
- `hooks/post-commit`
- `metadata.json`

**`remove_auth`**

- `.gitignore`
- `.gitmind/core/diff_reader.py`
- `.gitmind/core/engine.py`
- `.gitmind/core/llm.py`
- `.gitmind/core/metadata.py`
- `.gitmind/metadata.json`
- `core/diff_reader.py`
- `core/llm.py`
- `tests/test_core.py`

**`repo_root_function_added`**

- `core/metadata.py`

**`unknown`**

- `.gitignore`
- `.gitmind/core/diff_reader.py`
- `.gitmind/venv/bin/Activate.ps1`
- `.gitmind/venv/bin/activate`
- `.gitmind/venv/bin/activate.csh`
- `.gitmind/venv/bin/activate.fish`
- `.gitmind/venv/bin/normalizer`
- `.gitmind/venv/bin/pip`
- `.gitmind/venv/bin/pip3`
- `.gitmind/venv/bin/pip3.9`
- `.gitmind/venv/bin/python`
- `.gitmind/venv/bin/python3`
- `.gitmind/venv/bin/python3.9`
- `.gitmind/venv/lib/python3.9/site-packages/81d243bd2c585b0f4821__mypyc.cpython-39-darwin.so`
- `.gitmind/venv/lib/python3.9/site-packages/_distutils_hack/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/_distutils_hack/override.py`
- `.gitmind/venv/lib/python3.9/site-packages/certifi-2026.2.25.dist-info/INSTALLER`
- `.gitmind/venv/lib/python3.9/site-packages/certifi-2026.2.25.dist-info/METADATA`
- `.gitmind/venv/lib/python3.9/site-packages/certifi-2026.2.25.dist-info/RECORD`
- `.gitmind/venv/lib/python3.9/site-packages/certifi-2026.2.25.dist-info/WHEEL`
- `.gitmind/venv/lib/python3.9/site-packages/certifi-2026.2.25.dist-info/licenses/LICENSE`
- `.gitmind/venv/lib/python3.9/site-packages/certifi-2026.2.25.dist-info/top_level.txt`
- `.gitmind/venv/lib/python3.9/site-packages/certifi/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/certifi/__main__.py`
- `.gitmind/venv/lib/python3.9/site-packages/certifi/cacert.pem`
- `.gitmind/venv/lib/python3.9/site-packages/certifi/core.py`
- `.gitmind/venv/lib/python3.9/site-packages/certifi/py.typed`
- `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer-3.4.7.dist-info/INSTALLER`
- `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer-3.4.7.dist-info/METADATA`
- `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer-3.4.7.dist-info/RECORD`
- `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer-3.4.7.dist-info/WHEEL`
- `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer-3.4.7.dist-info/entry_points.txt`
- `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer-3.4.7.dist-info/licenses/LICENSE`
- `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer-3.4.7.dist-info/top_level.txt`
- `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer/__main__.py`
- `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer/api.py`
- `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer/cd.cpython-39-darwin.so`
- `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer/cd.py`
- `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer/cli/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer/cli/__main__.py`
- `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer/constant.py`
- `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer/legacy.py`
- `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer/md.cpython-39-darwin.so`
- `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer/md.py`
- `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer/models.py`
- `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer/py.typed`
- `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer/utils.py`
- `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer/version.py`
- `.gitmind/venv/lib/python3.9/site-packages/distutils-precedence.pth`
- `.gitmind/venv/lib/python3.9/site-packages/idna-3.11.dist-info/INSTALLER`
- `.gitmind/venv/lib/python3.9/site-packages/idna-3.11.dist-info/METADATA`
- `.gitmind/venv/lib/python3.9/site-packages/idna-3.11.dist-info/RECORD`
- `.gitmind/venv/lib/python3.9/site-packages/idna-3.11.dist-info/WHEEL`
- `.gitmind/venv/lib/python3.9/site-packages/idna-3.11.dist-info/licenses/LICENSE.md`
- `.gitmind/venv/lib/python3.9/site-packages/idna/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/idna/codec.py`
- `.gitmind/venv/lib/python3.9/site-packages/idna/compat.py`
- `.gitmind/venv/lib/python3.9/site-packages/idna/core.py`
- `.gitmind/venv/lib/python3.9/site-packages/idna/idnadata.py`
- `.gitmind/venv/lib/python3.9/site-packages/idna/intranges.py`
- `.gitmind/venv/lib/python3.9/site-packages/idna/package_data.py`
- `.gitmind/venv/lib/python3.9/site-packages/idna/py.typed`
- `.gitmind/venv/lib/python3.9/site-packages/idna/uts46data.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/INSTALLER`
- `.gitmind/venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/LICENSE.txt`
- `.gitmind/venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/METADATA`
- `.gitmind/venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/RECORD`
- `.gitmind/venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/REQUESTED`
- `.gitmind/venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/WHEEL`
- `.gitmind/venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/entry_points.txt`
- `.gitmind/venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/top_level.txt`
- `.gitmind/venv/lib/python3.9/site-packages/pip/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/__main__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/build_env.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/cache.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/cli/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/cli/autocompletion.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/cli/base_command.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/cli/cmdoptions.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/cli/command_context.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/cli/main.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/cli/main_parser.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/cli/parser.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/cli/progress_bars.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/cli/req_command.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/cli/spinners.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/cli/status_codes.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/commands/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/commands/cache.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/commands/check.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/commands/completion.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/commands/configuration.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/commands/debug.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/commands/download.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/commands/freeze.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/commands/hash.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/commands/help.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/commands/index.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/commands/install.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/commands/list.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/commands/search.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/commands/show.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/commands/uninstall.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/commands/wheel.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/configuration.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/distributions/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/distributions/base.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/distributions/installed.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/distributions/sdist.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/distributions/wheel.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/exceptions.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/index/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/index/collector.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/index/package_finder.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/index/sources.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/locations/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/locations/_distutils.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/locations/_sysconfig.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/locations/base.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/main.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/metadata/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/metadata/base.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/metadata/pkg_resources.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/models/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/models/candidate.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/models/direct_url.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/models/format_control.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/models/index.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/models/link.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/models/scheme.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/models/search_scope.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/models/selection_prefs.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/models/target_python.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/models/wheel.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/network/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/network/auth.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/network/cache.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/network/download.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/network/lazy_wheel.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/network/session.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/network/utils.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/network/xmlrpc.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/operations/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/operations/build/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/operations/build/metadata.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/operations/build/metadata_legacy.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/operations/build/wheel.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/operations/build/wheel_legacy.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/operations/check.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/operations/freeze.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/operations/install/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/operations/install/editable_legacy.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/operations/install/legacy.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/operations/install/wheel.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/operations/prepare.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/pyproject.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/req/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/req/constructors.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/req/req_file.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/req/req_install.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/req/req_set.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/req/req_tracker.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/req/req_uninstall.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/resolution/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/resolution/base.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/resolution/legacy/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/resolution/legacy/resolver.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/base.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/candidates.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/factory.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/found_candidates.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/provider.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/reporter.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/requirements.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/resolver.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/self_outdated_check.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/_log.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/appdirs.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/compat.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/compatibility_tags.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/datetime.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/deprecation.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/direct_url_helpers.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/distutils_args.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/encoding.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/entrypoints.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/filesystem.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/filetypes.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/glibc.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/hashes.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/inject_securetransport.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/logging.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/misc.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/models.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/packaging.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/parallel.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/pkg_resources.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/setuptools_build.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/subprocess.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/temp_dir.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/unpacking.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/urls.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/virtualenv.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/wheel.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/vcs/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/vcs/bazaar.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/vcs/git.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/vcs/mercurial.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/vcs/subversion.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/vcs/versioncontrol.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/wheel_builder.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/appdirs.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/_cmd.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/adapter.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/cache.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/caches/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/caches/file_cache.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/caches/redis_cache.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/compat.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/controller.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/filewrapper.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/heuristics.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/serialize.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/wrapper.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/certifi/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/certifi/__main__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/certifi/cacert.pem`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/certifi/core.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/big5freq.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/big5prober.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/chardistribution.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/charsetgroupprober.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/charsetprober.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/cli/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/cli/chardetect.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/codingstatemachine.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/compat.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/cp949prober.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/enums.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/escprober.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/escsm.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/eucjpprober.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/euckrfreq.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/euckrprober.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/euctwfreq.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/euctwprober.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/gb2312freq.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/gb2312prober.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/hebrewprober.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/jisfreq.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/jpcntx.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/langbulgarianmodel.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/langgreekmodel.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/langhebrewmodel.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/langhungarianmodel.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/langrussianmodel.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/langthaimodel.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/langturkishmodel.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/latin1prober.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/mbcharsetprober.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/mbcsgroupprober.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/mbcssm.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/metadata/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/metadata/languages.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/sbcharsetprober.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/sbcsgroupprober.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/sjisprober.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/universaldetector.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/utf8prober.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/version.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/colorama/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/colorama/ansi.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/colorama/ansitowin32.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/colorama/initialise.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/colorama/win32.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/colorama/winterm.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/_backport/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/_backport/misc.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/_backport/shutil.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/_backport/sysconfig.cfg`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/_backport/sysconfig.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/_backport/tarfile.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/compat.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/database.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/index.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/locators.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/manifest.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/markers.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/metadata.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/resources.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/scripts.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/t32.exe`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/t64.exe`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/util.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/version.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/w32.exe`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/w64.exe`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/wheel.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distro.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/_ihatexml.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/_inputstream.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/_tokenizer.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/_trie/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/_trie/_base.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/_trie/py.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/_utils.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/constants.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/alphabeticalattributes.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/base.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/inject_meta_charset.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/lint.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/optionaltags.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/sanitizer.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/whitespace.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/html5parser.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/serializer.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treeadapters/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treeadapters/genshi.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treeadapters/sax.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treebuilders/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treebuilders/base.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treebuilders/dom.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treebuilders/etree.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treebuilders/etree_lxml.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treewalkers/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treewalkers/base.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treewalkers/dom.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treewalkers/etree.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treewalkers/etree_lxml.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treewalkers/genshi.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/idna/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/idna/codec.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/idna/compat.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/idna/core.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/idna/idnadata.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/idna/intranges.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/idna/package_data.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/idna/uts46data.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/msgpack/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/msgpack/_version.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/msgpack/exceptions.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/msgpack/ext.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/msgpack/fallback.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/packaging/__about__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/packaging/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/packaging/_manylinux.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/packaging/_musllinux.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/packaging/_structures.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/packaging/markers.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/packaging/requirements.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/packaging/specifiers.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/packaging/tags.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/packaging/utils.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/packaging/version.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/pep517/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/pep517/build.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/pep517/check.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/pep517/colorlog.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/pep517/compat.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/pep517/dirtools.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/pep517/envbuild.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/pep517/in_process/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/pep517/in_process/_in_process.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/pep517/meta.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/pep517/wrappers.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/pkg_resources/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/pkg_resources/py31compat.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/progress/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/progress/bar.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/progress/counter.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/progress/spinner.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/pyparsing.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/requests/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/requests/__version__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/requests/_internal_utils.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/requests/adapters.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/requests/api.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/requests/auth.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/requests/certs.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/requests/compat.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/requests/cookies.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/requests/exceptions.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/requests/help.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/requests/hooks.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/requests/models.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/requests/packages.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/requests/sessions.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/requests/status_codes.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/requests/structures.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/requests/utils.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/resolvelib/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/resolvelib/compat/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/resolvelib/compat/collections_abc.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/resolvelib/providers.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/resolvelib/reporters.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/resolvelib/resolvers.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/resolvelib/structs.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/six.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/tenacity/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/tenacity/_asyncio.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/tenacity/_utils.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/tenacity/after.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/tenacity/before.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/tenacity/before_sleep.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/tenacity/nap.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/tenacity/retry.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/tenacity/stop.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/tenacity/tornadoweb.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/tenacity/wait.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/tomli/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/tomli/_parser.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/tomli/_re.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/_collections.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/_version.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/connection.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/connectionpool.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/_appengine_environ.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/_securetransport/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/_securetransport/bindings.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/_securetransport/low_level.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/appengine.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/ntlmpool.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/pyopenssl.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/securetransport.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/socks.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/exceptions.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/fields.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/filepost.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/packages/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/packages/backports/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/packages/backports/makefile.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/packages/six.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/packages/ssl_match_hostname/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/packages/ssl_match_hostname/_implementation.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/poolmanager.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/request.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/response.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/connection.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/proxy.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/queue.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/request.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/response.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/retry.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/ssl_.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/ssltransport.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/timeout.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/url.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/wait.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/vendor.txt`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/webencodings/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/webencodings/labels.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/webencodings/mklabels.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/webencodings/tests.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/webencodings/x_user_defined.py`
- `.gitmind/venv/lib/python3.9/site-packages/pip/py.typed`
- `.gitmind/venv/lib/python3.9/site-packages/pkg_resources/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pkg_resources/_vendor/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pkg_resources/_vendor/appdirs.py`
- `.gitmind/venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/__about__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/_compat.py`
- `.gitmind/venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/_structures.py`
- `.gitmind/venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/_typing.py`
- `.gitmind/venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/markers.py`
- `.gitmind/venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/requirements.py`
- `.gitmind/venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/specifiers.py`
- `.gitmind/venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/tags.py`
- `.gitmind/venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/utils.py`
- `.gitmind/venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/version.py`
- `.gitmind/venv/lib/python3.9/site-packages/pkg_resources/_vendor/pyparsing.py`
- `.gitmind/venv/lib/python3.9/site-packages/pkg_resources/extern/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/pkg_resources/tests/data/my-test-package-source/setup.py`
- `.gitmind/venv/lib/python3.9/site-packages/requests-2.32.5.dist-info/INSTALLER`
- `.gitmind/venv/lib/python3.9/site-packages/requests-2.32.5.dist-info/METADATA`
- `.gitmind/venv/lib/python3.9/site-packages/requests-2.32.5.dist-info/RECORD`
- `.gitmind/venv/lib/python3.9/site-packages/requests-2.32.5.dist-info/REQUESTED`
- `.gitmind/venv/lib/python3.9/site-packages/requests-2.32.5.dist-info/WHEEL`
- `.gitmind/venv/lib/python3.9/site-packages/requests-2.32.5.dist-info/licenses/LICENSE`
- `.gitmind/venv/lib/python3.9/site-packages/requests-2.32.5.dist-info/top_level.txt`
- `.gitmind/venv/lib/python3.9/site-packages/requests/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/requests/__version__.py`
- `.gitmind/venv/lib/python3.9/site-packages/requests/_internal_utils.py`
- `.gitmind/venv/lib/python3.9/site-packages/requests/adapters.py`
- `.gitmind/venv/lib/python3.9/site-packages/requests/api.py`
- `.gitmind/venv/lib/python3.9/site-packages/requests/auth.py`
- `.gitmind/venv/lib/python3.9/site-packages/requests/certs.py`
- `.gitmind/venv/lib/python3.9/site-packages/requests/compat.py`
- `.gitmind/venv/lib/python3.9/site-packages/requests/cookies.py`
- `.gitmind/venv/lib/python3.9/site-packages/requests/exceptions.py`
- `.gitmind/venv/lib/python3.9/site-packages/requests/help.py`
- `.gitmind/venv/lib/python3.9/site-packages/requests/hooks.py`
- `.gitmind/venv/lib/python3.9/site-packages/requests/models.py`
- `.gitmind/venv/lib/python3.9/site-packages/requests/packages.py`
- `.gitmind/venv/lib/python3.9/site-packages/requests/sessions.py`
- `.gitmind/venv/lib/python3.9/site-packages/requests/status_codes.py`
- `.gitmind/venv/lib/python3.9/site-packages/requests/structures.py`
- `.gitmind/venv/lib/python3.9/site-packages/requests/utils.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/INSTALLER`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/LICENSE`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/METADATA`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/RECORD`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/REQUESTED`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/WHEEL`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/entry_points.txt`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/top_level.txt`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_deprecation_warning.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/_msvccompiler.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/archive_util.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/bcppcompiler.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/ccompiler.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/cmd.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/bdist.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/bdist_dumb.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/bdist_msi.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/bdist_rpm.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/bdist_wininst.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/build.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/build_clib.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/build_ext.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/build_py.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/build_scripts.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/check.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/clean.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/config.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/install.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/install_data.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/install_egg_info.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/install_headers.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/install_lib.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/install_scripts.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/py37compat.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/register.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/sdist.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/upload.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/config.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/core.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/cygwinccompiler.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/debug.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/dep_util.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/dir_util.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/dist.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/errors.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/extension.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/fancy_getopt.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/file_util.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/filelist.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/log.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/msvc9compiler.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/msvccompiler.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/py35compat.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/py38compat.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/spawn.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/sysconfig.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/text_file.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/unixccompiler.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/util.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/version.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/versionpredicate.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_imp.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_vendor/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_vendor/more_itertools/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_vendor/more_itertools/more.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_vendor/more_itertools/recipes.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_vendor/ordered_set.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/__about__.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/_compat.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/_structures.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/_typing.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/markers.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/requirements.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/specifiers.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/tags.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/utils.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/version.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/_vendor/pyparsing.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/archive_util.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/build_meta.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/cli-32.exe`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/cli-64.exe`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/cli.exe`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/alias.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/bdist_egg.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/bdist_rpm.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/build_clib.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/build_ext.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/build_py.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/develop.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/dist_info.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/easy_install.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/egg_info.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/install.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/install_egg_info.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/install_lib.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/install_scripts.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/launcher manifest.xml`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/py36compat.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/register.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/rotate.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/saveopts.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/sdist.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/setopt.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/test.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/upload.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/upload_docs.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/config.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/dep_util.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/depends.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/dist.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/errors.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/extension.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/extern/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/glob.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/gui-32.exe`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/gui-64.exe`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/gui.exe`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/installer.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/launch.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/monkey.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/msvc.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/namespaces.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/package_index.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/py34compat.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/sandbox.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/script (dev).tmpl`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/script.tmpl`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/unicode_utils.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/version.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/wheel.py`
- `.gitmind/venv/lib/python3.9/site-packages/setuptools/windows_support.py`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3-2.6.3.dist-info/INSTALLER`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3-2.6.3.dist-info/METADATA`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3-2.6.3.dist-info/RECORD`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3-2.6.3.dist-info/WHEEL`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3-2.6.3.dist-info/licenses/LICENSE.txt`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3/_base_connection.py`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3/_collections.py`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3/_request_methods.py`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3/_version.py`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3/connection.py`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3/connectionpool.py`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3/contrib/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3/contrib/emscripten/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3/contrib/emscripten/connection.py`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3/contrib/emscripten/fetch.py`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3/contrib/emscripten/request.py`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3/contrib/emscripten/response.py`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3/contrib/pyopenssl.py`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3/contrib/socks.py`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3/exceptions.py`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3/fields.py`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3/filepost.py`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3/http2/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3/http2/connection.py`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3/http2/probe.py`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3/poolmanager.py`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3/py.typed`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3/response.py`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3/util/__init__.py`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3/util/connection.py`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3/util/proxy.py`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3/util/request.py`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3/util/response.py`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3/util/retry.py`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3/util/ssl_.py`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3/util/ssl_match_hostname.py`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3/util/ssltransport.py`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3/util/timeout.py`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3/util/url.py`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3/util/util.py`
- `.gitmind/venv/lib/python3.9/site-packages/urllib3/util/wait.py`
- `.gitmind/venv/pyvenv.cfg`
- `core/diff_reader.py`
- `.gitmind/core/llm.py`
- `core/llm.py`
- `README.md`
- `docs/build-log.md`
- `metadata.json`
- `scripts/clean_metadata.py`
- `scripts/generate_build_log.py`
- `scripts/record_demo.sh`

**`user_onboarding`**

- `.gitmind/core/llm.py`
- `README.md`
- `core/llm.py`

---

## Commit History

Most recent first.

### `750b57c` — 2026-04-10 23:17

**Feature:** `build_log`

**What changed:** 'docs/demo.gif' was added to the project, and 'No human wrote these summaries.' The feature names, file lists, and change description were all restructured in order for it to be easier readable.

**Impact:** 'docs/demo.gif' is a GIF which can help in visualizing the process of project.

**Files:** `README.md`, `docs/build-log.md`, `docs/demo.cast`, `docs/demo.gif`, `metadata.json`, `scripts/generate_demo_cast.py`

---

### `4e0a25c` — 2026-04-10 23:02

**Feature:** `unknown`

**What changed:** The build log was updated to include more information.

**Files:** `README.md`, `docs/build-log.md`, `metadata.json`, `scripts/clean_metadata.py`, `scripts/generate_build_log.py`, `scripts/record_demo.sh`

---

### `a9921c1` — 2026-04-10 22:46

**Feature:** `pin_black`

**What changed:** The black version pinning was fixed in the CI workflow and a pyproject.toml file for consistent formatting is added.

**Impact:** The change likely impacts the code style and makes CI more robust against different versions of black. This could be beneficial for all developers.

**Files:** `.github/workflows/ci.yml`, `metadata.json`, `pyproject.toml`

---

### `0e890c6` — 2026-04-10 22:31

**Feature:** `pin_to_py39`

**What changed:** The 'pin black to --target-version py39' commit changes the version pinning in configuration files (black.ini) based on local and CI output.

**Why:** 'Pin Black to — target-version Py39' likely changed as it matches Python versions that tend not handle imports correctly, possibly due to older versions of black being less capable at parsing JSON data or dealing with modules imported during the execution. This could affect code compatibility.

**Impact:** The 'Pin Black version in configuration files (black.ini)' feature likely changed as it changes how black parses JSON data and manages modules imported during the execution due to its change matching Python versions that tend not handle imports correctly.

**Files:** `.github/workflows/ci.yml`, `metadata.json`

---

### `6814f6e` — 2026-04-10 22:25

**Feature:** `post_commit_hooks` *(new)*

**What changed:** The commit message 'fix' guard post-commit hook against infinite amend loop using GITMIND_RUNNING env var.

**Why:** 'Fixing the JSON parsing issue in LL(1) Python by updating diff reader getlatestdifference method.'

**Impact:** The use of GITMIND_RUNNING env var is likely to prevent infinite amend loops.

**Files:** `hooks/install.sh`, `hooks/post-commit`, `metadata.json`

---

### `198021e` — 2026-04-10 22:14

**Feature:** `implementation_of_auth_rate` *(new)*

**What changed:** 'auth middleware', 'rate limiting' and 'user onboarding' have been implemented into our system

**Impact:** 'auth middleware' implementation will allow for more secure authentication and 'rate limiting' can help prevent overloading servers with too many requests.

**Files:** `hooks/install.sh`, `hooks/post-commit`, `metadata.json`

---

### `2b335c7` — 2026-04-10 22:04

**Feature:** `blackcicheck`

**What changed:** 'The commit checks all source dirs in Black CI check'

**Why:**  'It likely changed the testing and linting processes for our code base.' 

**Impact:** The use of Black CI check feature may speed up development by catching style errors before submission.

**Files:** `.github/workflows/ci.yml`

---

### `81e9625` — 2026-04-10 21:59

**Feature:** `repo_root_function_added` *(new)*

**What changed:** The metadata module has been refactored to use a more modular approach with better separation of concerns.

**Why:** 'metadata.py' was changed due to the new modules for improved maintainability and reusability

**Impact:** 'metadata.py' is impacted by the new 'repository/git operations functions'. This will make it easier to manage dependencies and isolate components when large projects are involved

**Files:** `core/metadata.py`

---

### `1c52311` — 2026-04-10 21:53

**Feature:** `buildloggenerationfrommetadatajson` *(new)*

**What changed:** Auto Generate Build Log From Metadata JSON

**Why:** The change likely comes with the addition of a new feature - build log generation from metadata json.

**Files:** `.github/workflows/docs.yml`, `core/metadata.py`, `docs/build-log.md`, `metadata.json`, `scripts/generate_build_log.py`

---

### `201839b` — 2026-04-10 21:48

**Feature:** `remove_auth`

**What changed:** The `auth_middleware` and other modules have been removed from the project.

**Why:** This change likely occurred due to changes in authentication mechanisms used throughout different parts of our application. The removal of these middlewares might simplify certain tasks, decrease complexity for some features or provide a more secure environment altogether as they could no longer be necessary without this context being altered.

**Impact:** This change not only reduces the size of our codebase but also improves performance and security. Some users might face issues due to these changes in their authentication mechanisms as they no longer need them.

**Files:** `.gitignore`, `.gitmind/core/diff_reader.py`, `.gitmind/core/engine.py`, `.gitmind/core/llm.py`, `.gitmind/core/metadata.py`, `.gitmind/metadata.json`, `core/diff_reader.py`, `core/llm.py`, `tests/test_core.py`

---

### `ac5957f` — 2026-04-10 21:45

**Feature:** `auth_middleware_rate_limiting` *(new)*

**What changed:** 'graceful error handling for Ollama timeout and connection errors'

**Why:** The commit likely changed the core engine.py file by implementing exception handlers.

**Impact:** One of their most requested features was to include graceful error handling for Ollama timeout and connection errors. This will prevent the application from crashing when it encounters issues such as timeouts or network connectivity problems.

**Files:** `.gitmind/core/engine.py`, `.gitmind/core/llm.py`, `core/engine.py`, `core/llm.py`

---

### `3644106` — 2026-04-10 21:43

**Feature:** `initial_gitmind_engine` *(new)*

**What changed:** Added the initial scaffold of Gitmind's engine with its own modules for LLM analysis and metadata writing.

**Impact:** The initial version adds the functionality of Gitmind's core components in a modular way. This is useful for future development and maintenance.

**Files:** `docs/build-log.md`, `mkdocs.yml`

---

### `5906386` — 2026-04-10 20:22

**Feature:** `docs_deployments`

**What changed:** Fixed the Git Commit by performing a few actions, including writing to permissions and configuring git for deploying documents.

**Why:** The change likely arose from an issue with docs deployment bot setup in github repository. Also changes were made around document write permission configuration during CI/CD pipeline execution

**Impact:** 'Fixed the Git Commit by performing a few actions, including writing to permissions and configuring git for deploying documents.' might have been beneficial in terms of documentation setup on version control systems.

**Files:** `.github/workflows/docs.yml`

---

### `0de4d70` — 2026-04-10 20:10

**Feature:** `user_onboarding` *(new)*

**What changed:** This commit introduces a new feature in llm.py which is related to user onboarding and rate limiting.

**Impact:** - A significant change as the existing code base does not contain features for handling new users or updating user profiles in a timely manner.

**Files:** `.gitmind/core/llm.py`, `README.md`, `core/llm.py`

---

### `08fe52f` — 2026-04-10 20:08

**Feature:** `auth_middleware_py_file`

**What changed:** The model is using the Ollama format for JSON output.

**Why:** This likely changes a lot of existing models because it allows returning json data in different formats, improving code readability and usability

**Impact:** The feature is likely used in many existing files, so it's a good change that improves overall code quality and usability.

**Files:** `.gitmind/core/llm.py`, `core/llm.py`

---

### `2f91e1d` — 2026-04-10 20:08

**Feature:** `unknown`

**What changed:** 'Extract', 'coerce' and sanitize the field types in llm.py'

**Files:** `.gitmind/core/llm.py`, `core/llm.py`

---

### `ffaff32` — 2026-04-10 20:05

**Feature:** `unknown`

**Files:** `.gitignore`, `.gitmind/core/diff_reader.py`, `.gitmind/venv/bin/Activate.ps1`, `.gitmind/venv/bin/activate`, `.gitmind/venv/bin/activate.csh`, `.gitmind/venv/bin/activate.fish`, `.gitmind/venv/bin/normalizer`, `.gitmind/venv/bin/pip`, `.gitmind/venv/bin/pip3`, `.gitmind/venv/bin/pip3.9`, `.gitmind/venv/bin/python`, `.gitmind/venv/bin/python3`, `.gitmind/venv/bin/python3.9`, `.gitmind/venv/lib/python3.9/site-packages/81d243bd2c585b0f4821__mypyc.cpython-39-darwin.so`, `.gitmind/venv/lib/python3.9/site-packages/_distutils_hack/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/_distutils_hack/override.py`, `.gitmind/venv/lib/python3.9/site-packages/certifi-2026.2.25.dist-info/INSTALLER`, `.gitmind/venv/lib/python3.9/site-packages/certifi-2026.2.25.dist-info/METADATA`, `.gitmind/venv/lib/python3.9/site-packages/certifi-2026.2.25.dist-info/RECORD`, `.gitmind/venv/lib/python3.9/site-packages/certifi-2026.2.25.dist-info/WHEEL`, `.gitmind/venv/lib/python3.9/site-packages/certifi-2026.2.25.dist-info/licenses/LICENSE`, `.gitmind/venv/lib/python3.9/site-packages/certifi-2026.2.25.dist-info/top_level.txt`, `.gitmind/venv/lib/python3.9/site-packages/certifi/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/certifi/__main__.py`, `.gitmind/venv/lib/python3.9/site-packages/certifi/cacert.pem`, `.gitmind/venv/lib/python3.9/site-packages/certifi/core.py`, `.gitmind/venv/lib/python3.9/site-packages/certifi/py.typed`, `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer-3.4.7.dist-info/INSTALLER`, `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer-3.4.7.dist-info/METADATA`, `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer-3.4.7.dist-info/RECORD`, `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer-3.4.7.dist-info/WHEEL`, `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer-3.4.7.dist-info/entry_points.txt`, `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer-3.4.7.dist-info/licenses/LICENSE`, `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer-3.4.7.dist-info/top_level.txt`, `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer/__main__.py`, `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer/api.py`, `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer/cd.cpython-39-darwin.so`, `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer/cd.py`, `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer/cli/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer/cli/__main__.py`, `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer/constant.py`, `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer/legacy.py`, `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer/md.cpython-39-darwin.so`, `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer/md.py`, `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer/models.py`, `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer/py.typed`, `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer/utils.py`, `.gitmind/venv/lib/python3.9/site-packages/charset_normalizer/version.py`, `.gitmind/venv/lib/python3.9/site-packages/distutils-precedence.pth`, `.gitmind/venv/lib/python3.9/site-packages/idna-3.11.dist-info/INSTALLER`, `.gitmind/venv/lib/python3.9/site-packages/idna-3.11.dist-info/METADATA`, `.gitmind/venv/lib/python3.9/site-packages/idna-3.11.dist-info/RECORD`, `.gitmind/venv/lib/python3.9/site-packages/idna-3.11.dist-info/WHEEL`, `.gitmind/venv/lib/python3.9/site-packages/idna-3.11.dist-info/licenses/LICENSE.md`, `.gitmind/venv/lib/python3.9/site-packages/idna/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/idna/codec.py`, `.gitmind/venv/lib/python3.9/site-packages/idna/compat.py`, `.gitmind/venv/lib/python3.9/site-packages/idna/core.py`, `.gitmind/venv/lib/python3.9/site-packages/idna/idnadata.py`, `.gitmind/venv/lib/python3.9/site-packages/idna/intranges.py`, `.gitmind/venv/lib/python3.9/site-packages/idna/package_data.py`, `.gitmind/venv/lib/python3.9/site-packages/idna/py.typed`, `.gitmind/venv/lib/python3.9/site-packages/idna/uts46data.py`, `.gitmind/venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/INSTALLER`, `.gitmind/venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/LICENSE.txt`, `.gitmind/venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/METADATA`, `.gitmind/venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/RECORD`, `.gitmind/venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/REQUESTED`, `.gitmind/venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/WHEEL`, `.gitmind/venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/entry_points.txt`, `.gitmind/venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/top_level.txt`, `.gitmind/venv/lib/python3.9/site-packages/pip/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/__main__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/build_env.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/cache.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/cli/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/cli/autocompletion.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/cli/base_command.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/cli/cmdoptions.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/cli/command_context.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/cli/main.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/cli/main_parser.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/cli/parser.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/cli/progress_bars.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/cli/req_command.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/cli/spinners.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/cli/status_codes.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/commands/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/commands/cache.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/commands/check.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/commands/completion.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/commands/configuration.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/commands/debug.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/commands/download.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/commands/freeze.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/commands/hash.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/commands/help.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/commands/index.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/commands/install.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/commands/list.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/commands/search.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/commands/show.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/commands/uninstall.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/commands/wheel.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/configuration.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/distributions/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/distributions/base.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/distributions/installed.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/distributions/sdist.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/distributions/wheel.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/exceptions.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/index/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/index/collector.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/index/package_finder.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/index/sources.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/locations/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/locations/_distutils.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/locations/_sysconfig.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/locations/base.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/main.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/metadata/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/metadata/base.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/metadata/pkg_resources.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/models/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/models/candidate.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/models/direct_url.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/models/format_control.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/models/index.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/models/link.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/models/scheme.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/models/search_scope.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/models/selection_prefs.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/models/target_python.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/models/wheel.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/network/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/network/auth.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/network/cache.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/network/download.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/network/lazy_wheel.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/network/session.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/network/utils.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/network/xmlrpc.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/operations/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/operations/build/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/operations/build/metadata.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/operations/build/metadata_legacy.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/operations/build/wheel.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/operations/build/wheel_legacy.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/operations/check.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/operations/freeze.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/operations/install/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/operations/install/editable_legacy.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/operations/install/legacy.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/operations/install/wheel.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/operations/prepare.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/pyproject.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/req/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/req/constructors.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/req/req_file.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/req/req_install.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/req/req_set.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/req/req_tracker.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/req/req_uninstall.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/resolution/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/resolution/base.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/resolution/legacy/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/resolution/legacy/resolver.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/base.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/candidates.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/factory.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/found_candidates.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/provider.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/reporter.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/requirements.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/resolver.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/self_outdated_check.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/_log.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/appdirs.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/compat.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/compatibility_tags.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/datetime.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/deprecation.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/direct_url_helpers.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/distutils_args.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/encoding.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/entrypoints.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/filesystem.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/filetypes.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/glibc.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/hashes.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/inject_securetransport.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/logging.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/misc.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/models.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/packaging.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/parallel.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/pkg_resources.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/setuptools_build.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/subprocess.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/temp_dir.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/unpacking.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/urls.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/virtualenv.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/utils/wheel.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/vcs/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/vcs/bazaar.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/vcs/git.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/vcs/mercurial.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/vcs/subversion.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/vcs/versioncontrol.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_internal/wheel_builder.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/appdirs.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/_cmd.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/adapter.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/cache.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/caches/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/caches/file_cache.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/caches/redis_cache.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/compat.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/controller.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/filewrapper.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/heuristics.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/serialize.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/wrapper.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/certifi/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/certifi/__main__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/certifi/cacert.pem`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/certifi/core.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/big5freq.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/big5prober.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/chardistribution.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/charsetgroupprober.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/charsetprober.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/cli/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/cli/chardetect.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/codingstatemachine.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/compat.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/cp949prober.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/enums.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/escprober.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/escsm.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/eucjpprober.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/euckrfreq.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/euckrprober.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/euctwfreq.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/euctwprober.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/gb2312freq.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/gb2312prober.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/hebrewprober.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/jisfreq.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/jpcntx.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/langbulgarianmodel.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/langgreekmodel.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/langhebrewmodel.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/langhungarianmodel.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/langrussianmodel.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/langthaimodel.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/langturkishmodel.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/latin1prober.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/mbcharsetprober.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/mbcsgroupprober.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/mbcssm.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/metadata/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/metadata/languages.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/sbcharsetprober.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/sbcsgroupprober.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/sjisprober.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/universaldetector.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/utf8prober.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/chardet/version.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/colorama/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/colorama/ansi.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/colorama/ansitowin32.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/colorama/initialise.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/colorama/win32.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/colorama/winterm.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/_backport/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/_backport/misc.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/_backport/shutil.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/_backport/sysconfig.cfg`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/_backport/sysconfig.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/_backport/tarfile.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/compat.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/database.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/index.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/locators.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/manifest.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/markers.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/metadata.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/resources.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/scripts.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/t32.exe`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/t64.exe`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/util.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/version.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/w32.exe`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/w64.exe`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distlib/wheel.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/distro.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/_ihatexml.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/_inputstream.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/_tokenizer.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/_trie/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/_trie/_base.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/_trie/py.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/_utils.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/constants.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/alphabeticalattributes.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/base.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/inject_meta_charset.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/lint.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/optionaltags.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/sanitizer.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/whitespace.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/html5parser.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/serializer.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treeadapters/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treeadapters/genshi.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treeadapters/sax.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treebuilders/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treebuilders/base.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treebuilders/dom.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treebuilders/etree.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treebuilders/etree_lxml.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treewalkers/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treewalkers/base.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treewalkers/dom.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treewalkers/etree.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treewalkers/etree_lxml.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treewalkers/genshi.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/idna/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/idna/codec.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/idna/compat.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/idna/core.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/idna/idnadata.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/idna/intranges.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/idna/package_data.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/idna/uts46data.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/msgpack/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/msgpack/_version.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/msgpack/exceptions.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/msgpack/ext.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/msgpack/fallback.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/packaging/__about__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/packaging/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/packaging/_manylinux.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/packaging/_musllinux.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/packaging/_structures.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/packaging/markers.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/packaging/requirements.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/packaging/specifiers.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/packaging/tags.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/packaging/utils.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/packaging/version.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/pep517/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/pep517/build.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/pep517/check.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/pep517/colorlog.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/pep517/compat.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/pep517/dirtools.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/pep517/envbuild.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/pep517/in_process/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/pep517/in_process/_in_process.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/pep517/meta.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/pep517/wrappers.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/pkg_resources/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/pkg_resources/py31compat.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/progress/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/progress/bar.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/progress/counter.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/progress/spinner.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/pyparsing.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/requests/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/requests/__version__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/requests/_internal_utils.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/requests/adapters.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/requests/api.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/requests/auth.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/requests/certs.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/requests/compat.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/requests/cookies.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/requests/exceptions.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/requests/help.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/requests/hooks.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/requests/models.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/requests/packages.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/requests/sessions.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/requests/status_codes.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/requests/structures.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/requests/utils.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/resolvelib/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/resolvelib/compat/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/resolvelib/compat/collections_abc.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/resolvelib/providers.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/resolvelib/reporters.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/resolvelib/resolvers.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/resolvelib/structs.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/six.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/tenacity/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/tenacity/_asyncio.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/tenacity/_utils.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/tenacity/after.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/tenacity/before.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/tenacity/before_sleep.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/tenacity/nap.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/tenacity/retry.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/tenacity/stop.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/tenacity/tornadoweb.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/tenacity/wait.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/tomli/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/tomli/_parser.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/tomli/_re.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/_collections.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/_version.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/connection.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/connectionpool.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/_appengine_environ.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/_securetransport/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/_securetransport/bindings.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/_securetransport/low_level.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/appengine.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/ntlmpool.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/pyopenssl.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/securetransport.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/socks.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/exceptions.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/fields.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/filepost.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/packages/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/packages/backports/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/packages/backports/makefile.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/packages/six.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/packages/ssl_match_hostname/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/packages/ssl_match_hostname/_implementation.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/poolmanager.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/request.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/response.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/connection.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/proxy.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/queue.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/request.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/response.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/retry.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/ssl_.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/ssltransport.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/timeout.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/url.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/wait.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/vendor.txt`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/webencodings/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/webencodings/labels.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/webencodings/mklabels.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/webencodings/tests.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/_vendor/webencodings/x_user_defined.py`, `.gitmind/venv/lib/python3.9/site-packages/pip/py.typed`, `.gitmind/venv/lib/python3.9/site-packages/pkg_resources/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pkg_resources/_vendor/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pkg_resources/_vendor/appdirs.py`, `.gitmind/venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/__about__.py`, `.gitmind/venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/_compat.py`, `.gitmind/venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/_structures.py`, `.gitmind/venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/_typing.py`, `.gitmind/venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/markers.py`, `.gitmind/venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/requirements.py`, `.gitmind/venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/specifiers.py`, `.gitmind/venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/tags.py`, `.gitmind/venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/utils.py`, `.gitmind/venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/version.py`, `.gitmind/venv/lib/python3.9/site-packages/pkg_resources/_vendor/pyparsing.py`, `.gitmind/venv/lib/python3.9/site-packages/pkg_resources/extern/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/pkg_resources/tests/data/my-test-package-source/setup.py`, `.gitmind/venv/lib/python3.9/site-packages/requests-2.32.5.dist-info/INSTALLER`, `.gitmind/venv/lib/python3.9/site-packages/requests-2.32.5.dist-info/METADATA`, `.gitmind/venv/lib/python3.9/site-packages/requests-2.32.5.dist-info/RECORD`, `.gitmind/venv/lib/python3.9/site-packages/requests-2.32.5.dist-info/REQUESTED`, `.gitmind/venv/lib/python3.9/site-packages/requests-2.32.5.dist-info/WHEEL`, `.gitmind/venv/lib/python3.9/site-packages/requests-2.32.5.dist-info/licenses/LICENSE`, `.gitmind/venv/lib/python3.9/site-packages/requests-2.32.5.dist-info/top_level.txt`, `.gitmind/venv/lib/python3.9/site-packages/requests/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/requests/__version__.py`, `.gitmind/venv/lib/python3.9/site-packages/requests/_internal_utils.py`, `.gitmind/venv/lib/python3.9/site-packages/requests/adapters.py`, `.gitmind/venv/lib/python3.9/site-packages/requests/api.py`, `.gitmind/venv/lib/python3.9/site-packages/requests/auth.py`, `.gitmind/venv/lib/python3.9/site-packages/requests/certs.py`, `.gitmind/venv/lib/python3.9/site-packages/requests/compat.py`, `.gitmind/venv/lib/python3.9/site-packages/requests/cookies.py`, `.gitmind/venv/lib/python3.9/site-packages/requests/exceptions.py`, `.gitmind/venv/lib/python3.9/site-packages/requests/help.py`, `.gitmind/venv/lib/python3.9/site-packages/requests/hooks.py`, `.gitmind/venv/lib/python3.9/site-packages/requests/models.py`, `.gitmind/venv/lib/python3.9/site-packages/requests/packages.py`, `.gitmind/venv/lib/python3.9/site-packages/requests/sessions.py`, `.gitmind/venv/lib/python3.9/site-packages/requests/status_codes.py`, `.gitmind/venv/lib/python3.9/site-packages/requests/structures.py`, `.gitmind/venv/lib/python3.9/site-packages/requests/utils.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/INSTALLER`, `.gitmind/venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/LICENSE`, `.gitmind/venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/METADATA`, `.gitmind/venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/RECORD`, `.gitmind/venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/REQUESTED`, `.gitmind/venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/WHEEL`, `.gitmind/venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/entry_points.txt`, `.gitmind/venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/top_level.txt`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_deprecation_warning.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/_msvccompiler.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/archive_util.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/bcppcompiler.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/ccompiler.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/cmd.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/bdist.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/bdist_dumb.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/bdist_msi.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/bdist_rpm.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/bdist_wininst.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/build.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/build_clib.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/build_ext.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/build_py.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/build_scripts.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/check.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/clean.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/config.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/install.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/install_data.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/install_egg_info.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/install_headers.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/install_lib.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/install_scripts.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/py37compat.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/register.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/sdist.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/command/upload.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/config.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/core.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/cygwinccompiler.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/debug.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/dep_util.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/dir_util.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/dist.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/errors.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/extension.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/fancy_getopt.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/file_util.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/filelist.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/log.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/msvc9compiler.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/msvccompiler.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/py35compat.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/py38compat.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/spawn.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/sysconfig.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/text_file.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/unixccompiler.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/util.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/version.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_distutils/versionpredicate.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_imp.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_vendor/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_vendor/more_itertools/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_vendor/more_itertools/more.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_vendor/more_itertools/recipes.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_vendor/ordered_set.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/__about__.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/_compat.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/_structures.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/_typing.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/markers.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/requirements.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/specifiers.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/tags.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/utils.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/version.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/_vendor/pyparsing.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/archive_util.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/build_meta.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/cli-32.exe`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/cli-64.exe`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/cli.exe`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/alias.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/bdist_egg.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/bdist_rpm.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/build_clib.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/build_ext.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/build_py.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/develop.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/dist_info.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/easy_install.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/egg_info.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/install.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/install_egg_info.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/install_lib.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/install_scripts.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/launcher manifest.xml`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/py36compat.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/register.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/rotate.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/saveopts.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/sdist.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/setopt.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/test.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/upload.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/command/upload_docs.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/config.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/dep_util.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/depends.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/dist.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/errors.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/extension.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/extern/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/glob.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/gui-32.exe`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/gui-64.exe`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/gui.exe`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/installer.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/launch.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/monkey.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/msvc.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/namespaces.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/package_index.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/py34compat.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/sandbox.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/script (dev).tmpl`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/script.tmpl`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/unicode_utils.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/version.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/wheel.py`, `.gitmind/venv/lib/python3.9/site-packages/setuptools/windows_support.py`, `.gitmind/venv/lib/python3.9/site-packages/urllib3-2.6.3.dist-info/INSTALLER`, `.gitmind/venv/lib/python3.9/site-packages/urllib3-2.6.3.dist-info/METADATA`, `.gitmind/venv/lib/python3.9/site-packages/urllib3-2.6.3.dist-info/RECORD`, `.gitmind/venv/lib/python3.9/site-packages/urllib3-2.6.3.dist-info/WHEEL`, `.gitmind/venv/lib/python3.9/site-packages/urllib3-2.6.3.dist-info/licenses/LICENSE.txt`, `.gitmind/venv/lib/python3.9/site-packages/urllib3/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/urllib3/_base_connection.py`, `.gitmind/venv/lib/python3.9/site-packages/urllib3/_collections.py`, `.gitmind/venv/lib/python3.9/site-packages/urllib3/_request_methods.py`, `.gitmind/venv/lib/python3.9/site-packages/urllib3/_version.py`, `.gitmind/venv/lib/python3.9/site-packages/urllib3/connection.py`, `.gitmind/venv/lib/python3.9/site-packages/urllib3/connectionpool.py`, `.gitmind/venv/lib/python3.9/site-packages/urllib3/contrib/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/urllib3/contrib/emscripten/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/urllib3/contrib/emscripten/connection.py`, `.gitmind/venv/lib/python3.9/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js`, `.gitmind/venv/lib/python3.9/site-packages/urllib3/contrib/emscripten/fetch.py`, `.gitmind/venv/lib/python3.9/site-packages/urllib3/contrib/emscripten/request.py`, `.gitmind/venv/lib/python3.9/site-packages/urllib3/contrib/emscripten/response.py`, `.gitmind/venv/lib/python3.9/site-packages/urllib3/contrib/pyopenssl.py`, `.gitmind/venv/lib/python3.9/site-packages/urllib3/contrib/socks.py`, `.gitmind/venv/lib/python3.9/site-packages/urllib3/exceptions.py`, `.gitmind/venv/lib/python3.9/site-packages/urllib3/fields.py`, `.gitmind/venv/lib/python3.9/site-packages/urllib3/filepost.py`, `.gitmind/venv/lib/python3.9/site-packages/urllib3/http2/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/urllib3/http2/connection.py`, `.gitmind/venv/lib/python3.9/site-packages/urllib3/http2/probe.py`, `.gitmind/venv/lib/python3.9/site-packages/urllib3/poolmanager.py`, `.gitmind/venv/lib/python3.9/site-packages/urllib3/py.typed`, `.gitmind/venv/lib/python3.9/site-packages/urllib3/response.py`, `.gitmind/venv/lib/python3.9/site-packages/urllib3/util/__init__.py`, `.gitmind/venv/lib/python3.9/site-packages/urllib3/util/connection.py`, `.gitmind/venv/lib/python3.9/site-packages/urllib3/util/proxy.py`, `.gitmind/venv/lib/python3.9/site-packages/urllib3/util/request.py`, `.gitmind/venv/lib/python3.9/site-packages/urllib3/util/response.py`, `.gitmind/venv/lib/python3.9/site-packages/urllib3/util/retry.py`, `.gitmind/venv/lib/python3.9/site-packages/urllib3/util/ssl_.py`, `.gitmind/venv/lib/python3.9/site-packages/urllib3/util/ssl_match_hostname.py`, `.gitmind/venv/lib/python3.9/site-packages/urllib3/util/ssltransport.py`, `.gitmind/venv/lib/python3.9/site-packages/urllib3/util/timeout.py`, `.gitmind/venv/lib/python3.9/site-packages/urllib3/util/url.py`, `.gitmind/venv/lib/python3.9/site-packages/urllib3/util/util.py`, `.gitmind/venv/lib/python3.9/site-packages/urllib3/util/wait.py`, `.gitmind/venv/pyvenv.cfg`, `core/diff_reader.py`

---

### `6e78acd` — 2026-04-10 20:04

**Feature:** `gitmind_was_renamed_as`

**What changed:** 'initial gitmind engine' was a feature that included 'llm analyzer', 'metadata writer', and other tools such as CLI query tool. The install hook also added.

**Why:** The likely reason for this change is to add new features related with LLM (Latent Language Model) analysis, metadata writing capabilities in the gitmind engine

**Impact:** The new feature has improved user experience by providing more precise and personalized meeting reminders based on users’ input from the LLM analyzer. Additionally, it provides an easy way to handle metadata in .gitmind files for further use.

---

*Generated at 2026-04-11 03:22 UTC from `metadata.json`*
