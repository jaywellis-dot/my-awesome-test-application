"""CLI entrypoint for my-awesome-test-application.

Usage:
    python -m my_awesome_test_application members.csv
    python -m my_awesome_test_application members.csv --field email
"""

import argparse
import sys

from .reader import read_members

VALID_FIELDS = ["full_name", "id", "first_name", "last_name", "email", "gender", "ip_address"]


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="my-awesome-test-application",
        description="Read and display members from a CSV file.",
    )
    parser.add_argument("filepath", help="Path to the members CSV file.")
    parser.add_argument(
        "--field",
        default="full_name",
        choices=VALID_FIELDS,
        help="Which field to print for each member (default: full_name).",
    )

    args = parser.parse_args()

    try:
        members = read_members(args.filepath)
    except FileNotFoundError:
        print(f"Error: file not found: {args.filepath}", file=sys.stderr)
        sys.exit(1)
    except KeyError as e:
        print(f"Error: CSV is missing required column {e}", file=sys.stderr)
        sys.exit(1)

    for member in members:
        print(getattr(member, args.field))


if __name__ == "__main__":
    main()
