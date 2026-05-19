import csv
import pytest
from pathlib import Path

from my_awesome_test_application import read_members, Member


@pytest.fixture
def members_csv(tmp_path: Path) -> Path:
    csv_file = tmp_path / "members.csv"
    csv_file.write_text(
        "id,first_name,last_name,email,gender,ip_address\n"
        "1,Jane,Doe,jane@example.com,Female,1.2.3.4\n"
        "2,John,Smith,john@example.com,Male,5.6.7.8\n"
    )
    return csv_file


def test_read_members_returns_correct_count(members_csv):
    assert len(read_members(members_csv)) == 2


def test_read_members_fields(members_csv):
    members = read_members(members_csv)
    jane = members[0]
    assert jane.id == "1"
    assert jane.first_name == "Jane"
    assert jane.last_name == "Doe"
    assert jane.email == "jane@example.com"
    assert jane.gender == "Female"
    assert jane.ip_address == "1.2.3.4"


def test_member_full_name(members_csv):
    members = read_members(members_csv)
    assert members[0].full_name == "Jane Doe"
    assert members[1].full_name == "John Smith"


def test_member_is_dataclass(members_csv):
    member = read_members(members_csv)[0]
    assert isinstance(member, Member)


def test_read_members_accepts_string_path(members_csv):
    members = read_members(str(members_csv))
    assert len(members) == 2


def test_read_members_file_not_found():
    with pytest.raises(FileNotFoundError):
        read_members("nonexistent.csv")


def test_read_members_missing_column(tmp_path):
    bad_csv = tmp_path / "bad.csv"
    bad_csv.write_text("id,first_name\n1,Jane\n")
    with pytest.raises((KeyError, TypeError)):
        read_members(bad_csv)


def test_read_members_empty_file(tmp_path):
    empty_csv = tmp_path / "empty.csv"
    empty_csv.write_text("id,first_name,last_name,email,gender,ip_address\n")
    assert read_members(empty_csv) == []
