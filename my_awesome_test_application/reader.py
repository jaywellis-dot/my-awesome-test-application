from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Member:
    """Represents a single member record from a CSV file.

    Attributes:
        id: Unique identifier for the member.
        first_name: Member's first name.
        last_name: Member's last name.
        email: Member's email address.
        gender: Member's gender.
        ip_address: Member's IP address.
    """

    id: str
    first_name: str
    last_name: str
    email: str
    gender: str
    ip_address: str

    @property
    def full_name(self) -> str:
        """Return the member's full name."""
        return f"{self.first_name} {self.last_name}"


def read_members(filepath: str | Path) -> list[Member]:
    """Read members from a CSV file and return them as a list of Member objects.

    The CSV file must have the following columns (in any order):
    ``id``, ``first_name``, ``last_name``, ``email``, ``gender``, ``ip_address``.

    Args:
        filepath: Path to the CSV file. Can be a string or a :class:`pathlib.Path`.

    Returns:
        A list of :class:`Member` objects, one per row in the CSV.

    Raises:
        FileNotFoundError: If the file does not exist at the given path.
        KeyError: If the CSV is missing one or more required columns.

    Example:
        >>> from my_awesome_test_application import read_members
        >>> members = read_members("members.csv")
        >>> for member in members:
        ...     print(member.full_name)
        Fanchette Wycliffe
        Woodrow Sabater
    """
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [Member(**row) for row in reader]
