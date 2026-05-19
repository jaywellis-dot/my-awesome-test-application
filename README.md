# my-awesome-test-application

A Python utility for reading and processing member CSV data. Exposes a clean API for use in other applications and a CLI for quick command-line access.

## Installation

Install directly from GitHub (no PyPI account required):

```bash
pip install git+https://github.com/your-username/my-awesome-test-application.git
```

Or clone and install locally in editable mode:

```bash
git clone https://github.com/your-username/my-awesome-test-application.git
cd my-awesome-test-application
pip install -e .
```

## CSV Format

Your CSV file must have the following columns (order doesn't matter):

| Column | Description |
|---|---|
| `id` | Unique member identifier |
| `first_name` | First name |
| `last_name` | Last name |
| `email` | Email address |
| `gender` | Gender |
| `ip_address` | IP address |

## Usage as a Library

```python
from my_awesome_test_application import read_members

members = read_members("members.csv")

for member in members:
    print(member.full_name)   # "Fanchette Wycliffe"
    print(member.email)       # "fwycliffe0@time.com"
    print(member.id)
    print(member.gender)
    print(member.ip_address)
```

### `read_members(filepath)`

Reads a CSV file and returns a `list[Member]`.

| Parameter | Type | Description |
|---|---|---|
| `filepath` | `str` or `Path` | Path to the CSV file |

Raises `FileNotFoundError` if the file doesn't exist, and `KeyError` if a required column is missing.

### `Member`

A dataclass with the following fields:

| Field | Type | Description |
|---|---|---|
| `id` | `str` | Unique identifier |
| `first_name` | `str` | First name |
| `last_name` | `str` | Last name |
| `email` | `str` | Email address |
| `gender` | `str` | Gender |
| `ip_address` | `str` | IP address |
| `full_name` | `str` (property) | `"{first_name} {last_name}"` |

## Usage as a CLI

After installation, the `my-awesome-test-application` command is available:

```bash
# Print full names (default)
my-awesome-test-application members.csv

# Print a specific field
my-awesome-test-application members.csv --field email
my-awesome-test-application members.csv --field id
my-awesome-test-application members.csv --field gender
my-awesome-test-application members.csv --field ip_address
```

Or run without installing:

```bash
python -m my_awesome_test_application members.csv --field email
```

Available `--field` values: `full_name`, `id`, `first_name`, `last_name`, `email`, `gender`, `ip_address`

## Requirements

- Python 3.9+
- No external dependencies (uses stdlib only)
