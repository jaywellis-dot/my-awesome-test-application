"""my-awesome-test-application

A utility for reading and processing member CSV data.

Typical usage::

    from my_awesome_test_application import read_members

    members = read_members("members.csv")
    for member in members:
        print(member.full_name)
        print(member.email)
"""

from .reader import Member, read_members

__version__ = "0.1.0"
__all__ = ["Member", "read_members"]
