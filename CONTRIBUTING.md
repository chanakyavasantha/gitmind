# Contributing to gitmind

Thanks for your interest. Here's how to get started.

## Setup

```bash
git clone https://github.com/chanakyavasantha/gitmind
cd gitmind
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install pytest black
```

## Running Tests

```bash
pytest tests/ -v
```

All tests should pass before opening a PR.

## Code Style

We use [Black](https://black.readthedocs.io) for formatting:

```bash
black core/ cli/
```

CI will reject PRs that don't pass `black --check`.

## Submitting a PR

1. Fork the repo
2. Create a branch: `git checkout -b feature/your-feature`
3. Make your changes
4. Run tests: `pytest tests/ -v`
5. Run formatter: `black core/ cli/`
6. Open a PR with a clear description of what and why

## Project Structure

```
core/           — pipeline logic (diff reader, LLM, metadata)
cli/            — query interface
hooks/          — bash hook + install script
tests/          — pytest test suite
docs/           — MkDocs documentation
```

## Good First Issues

Look for issues tagged [`good first issue`](https://github.com/chanakyavasantha/gitmind/labels/good%20first%20issue).

## Questions

Open a discussion or an issue — happy to help.
