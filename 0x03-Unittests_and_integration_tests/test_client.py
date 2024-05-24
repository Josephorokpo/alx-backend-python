#!/usr/bin/env python3
"""
This module contains the unit tests for the `GithubOrgClient` class from the `client` module.
"""

import unittest
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test case for the `GithubOrgClient` class."""

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test that `GithubOrgClient.has_license` returns the expected value.

        Parameters:
        - repo: the repository dictionary.
        - license_key: the license key to check.
        - expected: the expected return value.
        """
        client = GithubOrgClient("test_org")
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
