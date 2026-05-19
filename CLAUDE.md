# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`my-awesome-test-application` is an installable Python package for reading and processing member CSV data (`members.csv`, columns: `id`, `first_name`, `last_name`, `email`, `gender`, `ip_address`). It exposes a typed API for use in other applications and a CLI for command-line access.

## Package Structure

- `my_awesome_test_application/reader.py` — `Member` dataclass and `read_members()` function (the core public API)
- `my_awesome_test_application/__init__.py` — re-exports `Member` and `read_members`; sets `__version__`
- `my_awesome_test_application/__main__.py` — CLI entrypoint

## Environment & Install

```bash
source venv/bin/activate
pip install -e .
```

No external dependencies — stdlib only (`csv`, `pathlib`, `argparse`, `dataclasses`).

## Running

As a script:
```bash
python -m my_awesome_test_application members.csv
python -m my_awesome_test_application members.csv --field email
```

After `pip install -e .`:
```bash
my-awesome-test-application members.csv --field email
```

## Publishing to GitHub

1. Create a repo at github.com
2. `git remote add origin https://github.com/your-username/my-awesome-test-application.git`
3. `git push -u origin main`

Users can then install directly with:
```bash
pip install git+https://github.com/your-username/my-awesome-test-application.git
```

Update the `Homepage` URL in `pyproject.toml` when the GitHub repo is created.
